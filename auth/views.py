from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import permissions,viewsets,status,mixins
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from knox.auth import AuthToken
from django.contrib.auth.signals import user_logged_in

class RegisterView(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def create(self,request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"user created"})

class LoginView(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def create(self,request,format=None):
        try:
            serializer=AuthTokenSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user=serializer.validated_data['user']
            token = AuthToken.objects.create(user)[1]
            user_logged_in.send(sender=user.__class__,
                        request=request, user=user)
            data = {'token':token}
            return Response(data,status=status.HTTP_200_OK)
        except:
            return Response({'message':'user not found'},status=status.HTTP_404_NOT_FOUND)