from rest_framework.routers import DefaultRouter
from .views import GroupsViewset

group_router = DefaultRouter()
group_router.register('Groups', GroupsViewset, base_name="Groups")
