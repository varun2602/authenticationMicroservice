from typing import Any
from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView 
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication, JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .customauth import CustomAuthentication
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
import json
import io
from . import models 
from . import serializers
from . import permissions

class UserLC(ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserRegistrationSerializer
    
class Test(ListCreateAPIView):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerializer
    authentication_classes = [CustomAuthentication, JWTAuthentication]
    permission_classes = [permissions.IsTeacher]

@csrf_exempt
def login_route(request):
  if request.method == "POST":
    json_data = request.body 
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    email = python_data.get("email", None)
    password = python_data.get("password", None)

    if email is not None and password is not None:
        user = authenticate(email = email, password = password)

        if user is not None:
            otp = get_random_string(length=6, allowed_chars='0123456789')
            otp_obj = models.user_otp.objects.create(otp = otp, user = user)
            otp_obj.save()

            subject = 'Your OTP for login'
            message = f'Your OTP for login is: {otp}'
            email_from = "vcosmosv26@gmail.com"
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)

            status_code = status.HTTP_200_OK
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'OTP has been sent to your email',
                'authenticatedUser': {
                    'email': email
                }
            }
            json_data_response = json.dumps(response)
            return HttpResponse(json_data_response, status = status_code)
        else:
            status_code = status.HTTP_401_UNAUTHORIZED
            response = {
                'success': False,
                'statusCode': status_code,
                'message': 'Invalid email or password'
            }
            json_data_response = json.dumps(response)
            return HttpResponse(json_data_response, status=status_code)
    else:
        status_code = status.HTTP_401_UNAUTHORIZED
        response = {
            'success': False,
            'statusCode': status_code,
            'message': 'Invalid email or password'
        }
        json_data_response = json.dumps(response)
        return HttpResponse(json_data_response, status=status_code)



class AuthUserLoginView(APIView):
    serializer_class = serializers.UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)