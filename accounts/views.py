from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .forms import RegisterFrom
from django.contrib import messages
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .seializers import UserLoginSerializer,UserRegisterSerializer
from rest_framework.views import APIView


class UserRegister(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(TokenObtainPairView):
    serializer_class = UserLoginSerializer


class Logout(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=HTTP_200_OK)
