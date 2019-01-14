from .models import Idc
from .serializers import IdcSerializer
from rest_framework import viewsets

class IdcListViewset(viewsets.ModelViewSet):#viewsets.ModelViewSet继承了所有可操作的类
    '''
    retrieve:
        返回指定idc信息
    list:
        返回idc列表
    update:
        更新idc信息
    destroy:
        删除idc信息
    create:
        创建idc信息
    partial_update:
        更新部分记录
    '''
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer  # 使用idc序列化这个类，也就是serializers.py这个文件
