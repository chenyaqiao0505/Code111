from django.shortcuts import render
from django.http import HttpResponse
from .models import Idc
from .serializers import IdcSerializer
from django.shortcuts import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


###########################################################################
class JsonResponse(HttpResponse):
    def __init__(self, data,**kwargs):
        kwargs.setdefault('content_type', 'application/json')
        content = JSONRenderer().render(data)
        super(JsonResponse,self).__init__(content=data, **kwargs)


def idc_list(request,*args,**kwargs):
    if request.method == 'GET':
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset,many=True)
        return JsonResponse(serializer.data)
        # content = JSONRenderer().render(serializer.data)
        # return HttpResponse(content,content_type="application/json")
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IdcSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
    #         content = JSONRenderer().render(serializer.data)
    #         return HttpResponse(content,content_type="application/json")
    # return HttpResponse("")

def idc_detail(request,pk,*args,**kwargs):
    try:
        idc = Idc.objects.get(pk = pk)
    except Idc.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = IdcSerializer(idc)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        content = JSONParser().parse(request)
        serializer = IdcSerializer(idc,data=content)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        idc.delete()
        return HttpResponse(status=204)

############################################   版本二   #####################################
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import  reverse

@api_view(["GET","POST"])
def idc_list_v2(request,*args,**kwargs):

    if request.method == "GET":
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = IdcSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
def idc_detail_v2(request,pk,*args,**kwargs):

    try:
        idc = Idc.objects.get(pk = pk)
    except Idc.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IdcSerializer(idc)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IdcSerializer(idc,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        idc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def api_root(request,format = None,*args,**kwargs):
    return Response({
        # "idcs": "http://127.0.0.1:8000/idcs/"
        "idcs": reverse("idc-list",request=request,format = format)

    })

#################################版本三###################################################
from rest_framework.views import APIView
from django.http import Http404

class IdcList(APIView):
    def get(self,request,format = None):
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset,many=True)
        return Response (serializer.data)
    def post(self,request,format = None):
        serializer = IdcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
class IdcDetail(APIView):
    def get_objects(self,pk):
        try:
            return Idc.objects.get(pk = pk)
        except Idc.DoesNotExist:
            raise Http404

    def get(self,request,pk,format = None):
        idc = self.get_objects(pk)
        serializer = IdcSerializer(idc)
        return Response(serializer.data)

    def put(self,request,pk,format = None):
        idc = self.get_objects(pk)
        serializer = IdcSerializer(idc)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format = None):
        idc = self.get_objects(pk)
        idc.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

###############################版本四混合#################################################
from rest_framework import mixins,generics

class IdcList_v4(generics.GenericAPIView,
                 mixins.CreateModelMixin,
                 mixins.ListModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

class IdcDetail_v4(generics.CreateAPIView,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer        #使用idc序列化这个类，也就是serializers.py这个文件

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destory(request,*args,**kwargs)


###############################版本五高级混合#################################################

class IdcList_v5(generics.ListCreateAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer  # 使用idc序列化这个类，也就是serializers.py这个文件

class IdcDetail_v5(generics.RetrieveUpdateAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer  # 使用idc序列化这个类，也就是serializers.py这个文件


###############################版本六 视图集#################################################
from rest_framework import viewsets
class IdcListViewset(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer  # 使用idc序列化这个类，也就是serializers.py这个文件


###############################版本七 视图集#################################################
from rest_framework import viewsets
class IdcListViewset(viewsets.ModelViewSet):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer  # 使用idc序列化这个类，也就是serializers.py这个文件























