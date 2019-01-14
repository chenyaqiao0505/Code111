from rest_framework import serializers
from .models import Manufacturer,ProductModel
from .models import Server,NetworkDevice,IP

class ServerAutoReportSerializer(serializers.ModelSerializer):
    '''
    服务器序列化
    '''
    ip              = serializers.IPAddressField(required=True)
    hostname        = serializers.CharField(required=True,max_length=20)
    cpu             = serializers.CharField(required=True,max_length=50)
    mem             = serializers.CharField(required=True,max_length=20)
    disk            = serializers.CharField(required=True,max_length=200)
    os              = serializers.CharField(required=True,max_length=50)
    sn              = serializers.CharField(required=True,max_length=50)
    manufacturer    = serializers.CharField(required=True)
    model_name      = serializers.CharField(required=True)
    uuid            = serializers.CharField(required=True,max_length=50)
    network         = serializers.JSONField(required=True)

    class Meta:
        model = Server
        fields = '__all__'

    def validate_manufacturer(self, value):
        ## 验证供应商
        try:
            return Manufacturer.objects.get(vendor_name__exact =value )
        ## 返回传入的供应商正确
        except Manufacturer.DoesNotExist:
        ## 如果传入的供应商名称不存在,就创建一个供应商
            return self.create_manufacturer(value)

    def validate(self, attrs):
        # network = attrs['network']
        # del attrs['network']
        ## 删除掉attrs['network'],因为后面到了create方法,create创建server的字段,发现有attrs['network'],server是没有的,会报错
        manufacturer_obj = attrs['manufacturer']#拿到制造商对象
        try:
            attrs['model_name'] = manufacturer_obj.productmodel_set.get(model_name__exact = attrs['model_name'])
            ## 在供应商和产品表链接查询产品,条件是供应商名字相同
            ## manufacturer_obj.productmodel_set意思就是连接查询,xx_set,连接查询到product表.相当于join
        except ProductModel.DoesNotExist:
            ## 若没有找到,就调用创建产品的方法,创建一个名称是该供应商的产品
            attrs['model_name'] = self.create_product_model(manufacturer_obj,attrs['model_name'])
        return attrs


    def create(self, validated_data):
        network = validated_data.pop("network")
        ## 字典操作
        server_obj = Server.objects.create(**validated_data)
        ## 创建一条server记录
        # server_obj.networkdevice_set = network_queryset
        ## 设置其值为列表,设置一对多的关联关系的
        self.check_server_network_device(server_obj,network)
        return server_obj

    def check_server_network_device(self,server_obj,network):
        '''
        检查指定服务器有没有这些网卡设备,并作关联
        '''
        network_device_queryset = server_obj.networkdevice_set.all()
        ## 拿到的是当前服务器的所有网卡设备
        for device in network:
            try:
                network_device_obj = network_device_queryset.get(name__exact = device['name'])
                ## 在所有网卡设备里面查找,当前网卡设备名是否存在
            except NetworkDevice.DoesNotExist:
                self.create_network_device(server_obj,device)
                ## 没有找到就创建

    def check_ip(self,network_device_obj,ifnets):
        ip_queryset = network_device_obj.ip_set.all()
        ## 拿到所有的ip
        for ifnet in ifnets:

            try:
                ip_queryset.get(ip_addr__exact = ifnet['ip_addr'])
            except IP.DoesNotExist:
                ip_obj = self.create_ip(network_device_obj,ifnet)

    def create_ip(self,network_device_obj,ifnet):
        ifnet['device'] = network_device_obj
        return IP.objects.create(**ifnet)

    def create_network_device(self,server_obj,device):
        ips = device.pop('ips')
        device['host'] = server_obj
        network_device_obj = NetworkDevice.objects.create(**device)
        self.check_ip(network_device_obj,ips)
        return network_device_obj

    def check_network_device(self,server_obj,device):
        ## 检查指定的服务器有没有网卡设备,并作关联
        ips = device.pop('ips')
        device['host'] = server_obj
        network_device_obj = NetworkDevice.objects.create(**device)
        self.check_ip(network_device_obj,ips)
        return network_device_obj


    def create_manufacturer(self,vendor_name):
        #创建供应商
        return Manufacturer.objects.create(vendor_name = vendor_name)

    def create_product_model(self,manufacturer_obj,model_name):
        ## 创建产品,传入两个参数,一个是供应商名称manufacturer_obj,一个是产品名称model_name
        return ProductModel.objects.create(model_name = model_name,vendor = manufacturer_obj)

    def to_representation(self, instance):
        ret = {
            'hostname':instance.hostname,
            'ip':instance.ip
        }
        return ret



class ServerSerializer(serializers.ModelSerializer):
    '''
    服务器序列化
    '''
    class Meta:
        model = Server
        fields = '__all__'


class NetworkDeviceSerializer(serializers.ModelSerializer):
    '''
    网卡序列化
    '''
    class Meta:
        model = NetworkDevice
        fields = '__all__'

class IPSerializer(serializers.ModelSerializer):
    '''
    IP序列化
    '''
    class Meta:
        model = IP
        fields = '__all__'
