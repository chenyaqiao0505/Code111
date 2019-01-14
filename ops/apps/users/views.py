from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UserSerializer
User = get_user_model()

class UserViewset(viewsets.ReadOnlyModelViewSet):
     '''
        retrieve:
            返回一个用户信息
        list:
            返回用户指定信息
     '''
     queryset = User.objects.all()      #指定queryset
     serializer_class = UserSerializer    #指定序列化类