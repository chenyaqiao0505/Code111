from rest_framework import viewsets, mixins, response, permissions
from django.contrib.auth import get_user_model
User = get_user_model()

from .serializers import UserSerializer
from .filters import UserFilter
class UserViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定用户信息
    list:
        返回用户列表
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter
    filter_fields = ("username",)
    extra_perm_map = {
        "GET": ['auth.view_user']
    }


class DashboardStatusViewset(viewsets.ViewSet):
    """
    list:
    获取dashboard状态数据
    """
    permission_classes = (permissions.IsAuthenticated,)
    def list(self, request, *args, **kwargs):
        data = self.get_content_data()
        return response.Response(data)

    def get_content_data(self):
        return {
            "aa": 11,
            "bb": 22
        }