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
        user = request.user
        serializer = VerifyUserSerializer(user, data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user)
        return Response(True, status=status.HTTP_200_OK)  


class UserDetailViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
