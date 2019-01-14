from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    '''
    用户序列化类
    这个类的属性都是给前端返回的字段
    '''
    username = serializers.CharField()
    email = serializers.EmailField()
