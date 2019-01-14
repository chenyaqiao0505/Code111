from django.shortcuts import render
from rest_framework import viewsets,mixins
from .models import Server,NetworkDevice,IP
from .serilaizers import ServerAutoReportSerializer,ServerSerializer,NetworkDeviceSerializer,IPSerializer

class ServerAutoReportViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
    create:
        创建一个服务器
    '''
    queryset = Server.objects.all()
    serializer_class = ServerAutoReportSerializer

class ServerViewset(viewsets.ReadOnlyModelViewSet):
    '''
    retrieve:
        读取一个服务器信息
    list:
        列出所有服务器信息
    '''
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class NetworkDeviceViewset(viewsets.ReadOnlyModelViewSet):
    '''
    retrieve:
        返回指定网卡信息
    list:
        返回网卡列表
    '''
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer

class IPSerializer(viewsets.ReadOnlyModelViewSet):
    '''
    retrieve:
        返回指定IP信息
    list:
        返回IP列表
    '''
    queryset = IP.objects.all()
    serializer_class = IPSerializer