from django.conf.urls import url
from .views import idc_list,idc_detail,IdcDetail,IdcList
from . import views
from .views import idc_list_v2,idc_detail_v2,api_root,IdcList_v4,IdcDetail_v4,IdcList_v5,IdcDetail_v5
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
################################################################################
# urlpatterns = [
#     url('^idcs/',idc_list),
#     url('^idcs/(?P<pk>[0-9]+)/$', idc_detail)
#
# ]

urlpatterns = [
    url("^$", api_root),
    url("^idcs/$",idc_list_v2,name='idc-list'),
    url('^idcs/(?P<pk>[0-9]+)/$', idc_detail_v2,name='idc-detail')

]
urlpatterns = format_suffix_patterns(urlpatterns)
################################################################################
urlpatterns = [
    url("^$",api_root),
    url("^idcs/$",IdcList.as_view(),name="idc-list"),
    url('^idcs/(?P<pk>[0-9]+)/$',IdcDetail.as_view(), name='idc-detail')

]
urlpatterns = format_suffix_patterns(urlpatterns)

##################################################################################
urlpatterns = [
    url("^$",api_root),
    url("^idcs/$",IdcList_v4.as_view(),name="idc-list"),
    url('^idcs/(?P<pk>[0-9]+)/$',IdcDetail_v4.as_view(), name='idc-detail')

]
urlpatterns = format_suffix_patterns(urlpatterns)
################################################################################
urlpatterns = [
    url("^$",api_root),
    url("^idcs/$",IdcList_v5.as_view(),name="idc-list"),
    url('^idcs/(?P<pk>[0-9]+)/$',IdcDetail_v5.as_view(), name='idc-detail')

]
urlpatterns = format_suffix_patterns(urlpatterns)
#################################################################################
idc_list = views.IdcListViewset.as_view({
    'get':'list',
    'post':'create'
})
idc_detail = views.IdcListViewset.as_view({
    'put': 'update',
    'delete': 'destroy',
    'get':'retrieve'
})
urlpatterns = [
    url("^$",views.api_root),
    url("^idcs/$",idc_list,name="idc-list"),
    url('^idcs/(?P<pk>[0-9]+)/$',idc_detail, name='idc-detail')
]

#################################################################################
from rest_framework.routers import DefaultRouter
route = DefaultRouter()
route.register('idcs',views.IdcListViewset)
urlpatterns = [
    url(r'^',include(route.urls))
]