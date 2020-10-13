from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth.models import User
from imdb_back.users.serializers import UserSerializer


# Create your views here.

class CreateUserViewSet(viewsets.GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
