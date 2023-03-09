from rest_framework import routers
from . views import PostViewSet,UserInfoView

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'userinfo', UserInfoView, basename='userinfo')