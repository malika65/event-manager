from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
import jwt
from rest_framework import generics, status, views, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Author, ConfirmCode
from django.shortcuts import redirect
from django.http import HttpResponsePermanentRedirect
import os
from rest_framework.views import APIView
from django.utils.crypto import get_random_string

from .utils import (
    send_verified_link, send_password_reset_link
)
from .serializers import (
    EmailRegistrateSerializer,
    EmailConfirmCode, 
    AuthorLoginSerializer,
    ResetPasswordEmailRequestSerializer,
    
)


# Регистрация
@api_view(['POST'])
def email_register(request):
    serializer = EmailRegistrateSerializer(data=request.data)
    serializer.is_valid(raise_exception = True)
    email = serializer.data['email']
    password = serializer.data['password']
    author = Author(email=email)
    author.set_password(password)
    author.save()
    code = ConfirmCode.objects.create(author=author)
    send_verified_link(f'Ваш код поддтверждения почты {code.code}/', email)
    return Response({
        "success":True,
        "data":"User created"},
        status.HTTP_201_CREATED
    )


@api_view(['GET'])
def confirm_email(request,code):
    confirm = EmailConfirmCode(data={"code":code})
    confirm.is_valid(raise_exception=True)
    conf_code = ConfirmCode.objects.get(code=code)
    user = conf_code.author
    user.verified = True 
    user.save()
    token = Token.objects.update_or_create(user_id=user.id)

    return Response({
        "success":True,
        "data": {"token":str(token[0])}},
        status.HTTP_200_OK
    )


    
# Логин
@api_view(['POST'])
def user_login(request):
    serializer = AuthorLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    response = {
        'success' : 'True',
        'status code' : status.HTTP_200_OK,
        'message': 'User logged in  successfully',
        'token' : serializer.data['token'],
        }
    status_code = status.HTTP_200_OK

    return Response(response, status=status_code)


@api_view(['POST'])
def request_password_reset(request):
    serializer = ResetPasswordEmailRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception = True)
    email = serializer.data['email']
    author = Author.objects.filter(email=email)
    if author:
        code = ConfirmCode.objects.create(author=author.last(),reset=True)
        send_verified_link(f'Чтобы подтвердить почту для сброса пароля, перейдите по ссылке - http://127.0.0.1:8000/password-reset/{code.code}/',code.author.email)
            
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
    
    return Response({'fail': 'There is no such user'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def set_new_password(request,code):
    if ConfirmCode.objects.filter(code=code):
        code = ConfirmCode.objects.get(code=code,reset = True)
        if not code.confirm:
            code.confirm = True
            code.save()
            new_password = get_random_string(length=8)
            code.author.set_password(new_password)
            code.author.save()
            send_verified_link(f'Ваш пароль: {new_password}',code.author.email)
            

        return Response({'success': True, 'message': 'Password reset success. Check your mail for new password'}, status=status.HTTP_200_OK)

