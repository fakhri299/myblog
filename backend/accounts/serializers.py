from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from accounts.models import Contact



class ContactSerializer(ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'
