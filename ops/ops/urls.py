from django.contrib import admin
from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from idcs.views import IdcListViewset
from users.views import UserViewset
from cabinet.views import CabinetViewset
from manufacturer.views import ManufacturerViewset,ProductViewset
from servers.views import ServerAutoReportViewset,NetworkDeviceViewset,IPSerializer,ServerViewset

route = DefaultRouter()
route.register('idcs',IdcListViewset,base_name='idcs')
route.register('users',UserViewset,base_name='users')
route.register('cabinet',CabinetViewset,base_name='cabinet')
route.register('Manufacturer',ManufacturerViewset,base_name='Manufacturer')
route.register('Product',ProductViewset,base_name='Product')

route.register('ServerAutoReport',ServerAutoReportViewset,base_name='ServerAutoReport')
route.register('NetworkDevice',NetworkDeviceViewset,base_name='NetworkDevice')
route.register('IP',IPSerializer,base_name='IP')
route.register('Servers',ServerViewset,base_name='Servers')




urlpatterns = [
    url(r'^',include(route.urls)),
    url(r'^docs/',include_docs_urls('数据接口API文档'))
]
