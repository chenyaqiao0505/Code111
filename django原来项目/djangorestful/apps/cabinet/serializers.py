from rest_framework import serializers
from idcs.serializers import IdcSerializer
from .models import Cabinet
from idcs.models import Idc

class CabinetSerializer(serializers.Serializer):
    idc = serializers.PrimaryKeyRelatedField(many=False,queryset=Idc.objects.all())
    # idc = serializers.SerializerMethodField()

    name = serializers.CharField(required=True)

    def to_representation(self, instance):  #转为json的最后一步
        idc_obj = instance.idc        #在转json之前一步的
        ret = super(CabinetSerializer,self).to_representation(instance)
        ret['idc'] = {
            'id':idc_obj.id,
            'name':idc_obj.name
        }
        return ret


    def to_internal_value(self, data):  #反序列化验证的第一步
        '''
        反序列化的第一步:拿到的是提交过来的原始数据:QueryDict => request.GET, request.POST
        :param data:
        :return:
        '''
        return super(CabinetSerializer,self).to_internal_value(data)

    def create(self, validated_data):
        return Cabinet.objects.create(**validated_data)