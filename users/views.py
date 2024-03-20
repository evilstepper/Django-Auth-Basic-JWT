from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from users.serializers import UserSerializer
from .models import User
import jwt, datetime
from MainAuth.Modules.sign_up import signup_user
from MainAuth.Modules.sign_in import signin_user
from MainAuth.Modules.sign_out import sign_out_user
from MainAuth.Modules.me import get_me

class Sign_Up(APIView):
    def post(self, request):
        data = request.data
        user_data = signup_user(data)
        return Response(user_data)

class Sign_In(APIView):
    
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        response = signin_user(email, password)
        
        return response
    
class Me(APIView):
    def get(self, request):
        user_data = get_me(request)
        return Response(user_data)
    
class Sign_Out(APIView):
    def post(self, request):
        return sign_out_user(request)

