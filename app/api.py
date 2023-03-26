from rest_framework import routers
from . views import UserInfoView

router = routers.DefaultRouter()

router.register(r'userinfo', UserInfoView, basename='userinfo')