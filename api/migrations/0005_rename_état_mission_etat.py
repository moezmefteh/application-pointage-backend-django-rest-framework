# Generated by Django 3.2.6 on 2021-09-01 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_pointage_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='état',
            new_name='etat',
        ),
    ]
