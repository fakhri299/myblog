from accounts.views import * 
from django.urls import path

urlpatterns = [
    path('contacts/',ContactListCreateApiView.as_view(),name='contact-list'),
]