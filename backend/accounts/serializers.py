from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from accounts.models import Contact
from django.contrib.auth.models import User




class ContactSerializer(ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'


class RegisterSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'first_name', 'last_name',
                    'email', 'username', 'password')
            extra_kwargs = {
                'password': {'write_only': True},
            }
        
        def create(self, validated_data):
            user=User.objects.create(
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                email=validated_data['email'],
                username=validated_data['username'],
                password=validated_data['password']
            )

            return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'email', 'username')