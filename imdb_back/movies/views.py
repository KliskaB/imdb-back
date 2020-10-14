from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from imdb_back.movies.models import Genre
from imdb_back.movies.serializers import GenreSerializer
from rest_framework import permissions


# Create your views here.

class GenresViewSet(viewsets.ModelViewSet, ListModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]
