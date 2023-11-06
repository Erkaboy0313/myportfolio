from rest_framework import viewsets,permissions,status
from rest_framework.response import Response
from . models import UserInfo,Services,Skills,Education,Portfolio,Cuntuct_us,Experience
from . serializers import  UserInfoSerializer,ServiceSerializer,SkillSerializer,EducationSerializer,PortfolioSerializer,CuntuctSerializer,ExperienceSerializer
from django.contrib.auth.models import User

class UserInfoView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    
    def list(self, request, *args, **kwargs):
        user = self.queryset.filter(user = request.user).first()
        serializer = self.get_serializer(user,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ServiceView(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def list(self, request, *args, **kwargs):
        user = request.user
        services = self.queryset.filter(user = user)
        serializer = self.get_serializer(services,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class SkillView(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = request.user
        sills = self.queryset.filter(user = user)
        serializer = self.get_serializer(sills,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class EducationView(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def list(self, request, *args, **kwargs):
        user = request.user
        education = self.queryset.filter(user = user)
        serializer = self.get_serializer(education,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class PortfolioView(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = request.user
        portfolios = self.queryset.filter(user = user)
        serializer = self.get_serializer(portfolios,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class CuntactView(viewsets.ModelViewSet):
    queryset = Cuntuct_us.objects.all()
    serializer_class = CuntuctSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def list(self, request, *args, **kwargs):
        user = request.user
        cuntucts = self.queryset.filter(user = user)
        serializer = self.get_serializer(cuntucts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ExperienceView(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def list(self, request, *args, **kwargs):
        user = request.user
        experience = self.queryset.filter(user = user)
        serializer = self.get_serializer(experience,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

