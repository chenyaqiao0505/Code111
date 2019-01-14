from rest_framework import viewsets
from .models import Cabinet
from .serializers import CabinetSerializer

class CabinetViewset(viewsets.ModelViewSet):
    '''
    retrieve:
        返回指定机柜信息
    list:
        返回机柜列表
    update:
        更新机柜信息
    destroy:
        删除机柜信息
    create:
        创建机柜信息
    partial_update:
        更新部分记录
    '''
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
