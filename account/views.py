from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import *

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = """
            Your're successfully registered!
            """
            return Response(message)
            


class ActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response("You're successfully activated your account!")
            


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer



class LogoutView(APIView):
    pass


class ForgotPasswordView(APIView):
    pass 


class ChangePasswordView(APIView):
    pass