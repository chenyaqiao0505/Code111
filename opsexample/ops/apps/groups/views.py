from rest_framework import viewsets
from django.contrib.auth.models import Group
from .serilaizers import GroupSerializer
from .filter import GroupFilter

class GroupsViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_class = GroupFilter
    filter_fields = ("name",)

