from rest_framework import serializers
from .models import Idc

class IdcSerializer(serializers.Serializer):
    '''
    IDC 序列化类
    '''
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(required= True,
                                 max_length = 32,
                                 label='机房名称',
                                 help_text='机房名称',
                                 error_messages={"blank":"这个机房名称不能为空",
                                                 "required":"这个名称是必要字段"})

    address = serializers.CharField(required= True,
                                    max_length =256,
                                    label='机房地址',
                                    help_text='机房地址',
                                    error_messages = {"blank": "这个机房名称不能为空",
                                                      "required": "这个名称是必要字段"})
    phone = serializers.CharField(required= True,
                                  max_length =15,
                                  label='联系人电话',
                                  help_text='联系人电话',
                                  error_messages = {"blank": "这个机房名称不能为空",
                                                    "required": "这个名称是必要字段"})
    email = serializers.EmailField(required= True)

    letter = serializers.CharField(required= True,
                                   max_length =5,
                                   label='机房简称',
                                   help_text='机房简称',
                                   error_messages = {"blank": "这个机房名称不能为空",
                                                     "required": "这个名称是必要字段"})


    def create(self, validated_data):
        return Idc.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.address = validated_data.get('address',instance.address)
        instance.phone = validated_data.get('phone',instance.phone)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance