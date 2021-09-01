from rest_framework import serializers 
from Auth.models import *
 
 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                  'first_name',
                  'last_name',
                  'cin',
                  'username',
                  'password',
                  'codeQR',
                  'poste',
                  'image',
                  'email',
                  'telephone']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                  'first_name',
                  'last_name',
                  'cin',
                  'codeQR',
                  'poste',
                  'image',
                  'email',
                  'telephone'
                    ]