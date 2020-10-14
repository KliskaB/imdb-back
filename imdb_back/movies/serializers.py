from rest_framework import serializers
from django.contrib.auth.models import User
from imdb_back.movies.models import Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'title']