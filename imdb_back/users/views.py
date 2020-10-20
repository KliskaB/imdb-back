from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.mixins import CreateModelMixin
from imdb_back.users.models import User
from imdb_back.users.serializers import UserSerializer, VerifyUserSerializer, UserDetailSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status


class CreateUserViewSet(viewsets.GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class VerifyUserViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = VerifyUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        print(request)
        user = request.user
        content = False
        if(user.verification_code == request.data['verification_code']):
            content = True
            user.is_verified = True
            user.save()
            return Response(content, status=status.HTTP_200_OK)  
        else:
            return Response(content, status=status.HTTP_404_NOT_FOUND)


class UserDetailViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
