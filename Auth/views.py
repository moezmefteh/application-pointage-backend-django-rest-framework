from rest_framework import status
from rest_framework.generics import UpdateAPIView
from pointage.settings import SECRET_KEY
from Auth.models import *
from Auth.serializers import *

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt , datetime




class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'success'
        }
        return response


class LoginView(APIView):
    def post(self, request):
        login= request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=login).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        response = Response()

        user = User.objects.get(username=login)        
        employes_serializer = UserSerializer(user) 

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token,
            'data':employes_serializer.data

        }

        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!!')

        user = User.objects.get(username=payload['id']) 
        employes_serializer = UserSerializer(user) 
        return Response(employes_serializer.data) 


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
##########################################################################

# class PropertiesUserUpdate(UpdateAPIView):
#     def put(self, request):

#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!!')

#         user = User.objects.get(username=payload['id']) 
   
#         serializer_class = UserSerializer(user, data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#             return Response(serializer_class.data) 
#         return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

            
##########################################################################     

@api_view(['GET', 'PUT', 'DELETE'])
def PropertiesUserUpdate(request,username):
        # find employe by pk (id)
        try: 
                user = User.objects.get(username=username) 
        except User.DoesNotExist: 
                return Response({'message': 'The employe does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        if request.method == 'GET': 
            employes_serializer = UserSerializer(user) 
            return Response(employes_serializer.data) 
        
        # put a employe
        elif request.method == 'PUT': 
            data = JSONParser().parse(request) 
            employes_serializer = UserSerializer(user, data=data) 
            if employes_serializer.is_valid(): 
                employes_serializer.save() 
                return Response( status=status.HTTP_201_CREATED) 
            return Response(employes_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
            
        # delete an employe by pk
        elif request.method == 'DELETE': 
            user.delete() 
            return Response({'message': 'employe was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)