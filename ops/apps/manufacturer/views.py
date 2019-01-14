from django.shortcuts import render
from rest_framework import viewsets
from .models import Manufacturer,ProductModel
from .serilaizers import ManufacturerSerializer,ProductSerializer

class ManufacturerViewset(viewsets.ModelViewSet):
    '''
      retrieve:
          返回指定制造商信息
      list:
          返回制造商列表
      update:
          更新制造商信息
      destroy:
          删除制造商信息
      create:
          创建制造商信息
      partial_update:
          更新部分记录
      '''
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ProductViewset(viewsets.ModelViewSet):
    '''
      retrieve:
          返回指定制造商信息
      list:
          返回制造商列表
      update:
          更新制造商信息
      destroy:
          删除制造商信息
      create:
          创建制造商信息
      partial_update:
          更新部分记录
      '''
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer