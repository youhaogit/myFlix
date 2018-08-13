from rest_framework import serializers

from webapp.models import *
from webapp.utils.pagination import StandardResultsSetPagination


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('id','name',)


class GenresInMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenresInMovies
        fields = ('genre', 'movie')


class StarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stars
        fields = ('id', 'name', 'birth_year')


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('movie', 'rating', 'num_votes')


class MovieInfoSerializer(serializers.ModelSerializer):
    get_genres = GenresSerializer(many=True)
    get_stars = StarsSerializer(many=True)
    get_rating = RatingsSerializer(many=True)

    class Meta:
        model = Movies
        fields = ('id', 'title', 'year', 'director', 'get_genres', 'get_stars', 'get_rating')







