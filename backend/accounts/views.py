from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from accounts.serializers import ContactSerializer
from accounts.models import Contact
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer,UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from . import jwt as custom_jwt
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import user_logged_in
from django.core.mail import send_mail
from rest_framework.views import APIView


class ContactView(ListCreateAPIView):
     serializer_class=ContactSerializer
     queryset=Contact.objects.all()
     permission_classes=[IsAuthenticated]
       

class RegisterApi(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid()
        self.perform_update(serializer)


        return Response(serializer.data)



class LoginApi(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)

        data = data.data

        acces_token = custom_jwt.jwt_decode_handler(data.get("access"))

        if not User.objects.filter(id=acces_token.get("user_id")).last():
            return Response({"error": True, "message": "No such a user"}, status=status.HTTP_404_NOT_FOUND)

        user = User.objects.filter(id=acces_token.get("user_id")).last()
        user_logged_in.send(sender=type(user), request=request, user=user)

        user_details = UserSerializer(user)

        data["user_details"] = user_details.data
        return Response(data)