from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from accounts.serializers import ContactSerializer
from accounts.models import Contact

# Create your views here.
class ContactListCreateApiView(ListCreateAPIView):
    serializer_class=ContactSerializer
    queryset=Contact.objects.all()
