from accounts.views import * 
from django.urls import path

urlpatterns = [
    path('contacts/',ContactView.as_view(),),
    path('register/',RegisterApi.as_view()),
    path('login/',LoginApi.as_view()),
    path('<int:pk>/',UserDetail.as_view(),),
    path('users',UserList.as_view(),),
]