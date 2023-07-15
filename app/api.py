from rest_framework import routers
from . views import UserInfoView,ServiceView,SkillView,EducationView,PortfolioView,CuntactView,ExperienceView

router = routers.DefaultRouter()

router.register(r'userinfo', UserInfoView, basename='userinfo')
router.register(r'service', ServiceView, basename='service')
router.register(r'skill', SkillView, basename='skill')
router.register(r'education', EducationView, basename='education')
router.register(r'portfolio', PortfolioView, basename='portfolio')
router.register(r'cuntuct', CuntactView, basename='cuntuct')
router.register(r'experiece', ExperienceView, basename='experiece')