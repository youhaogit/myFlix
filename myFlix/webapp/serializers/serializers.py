from rest_framework import serializers

from webapp.models import Movies, Genres, GenresInMovies
from webapp.utils.pagination import StandardResultsSetPagination


class MovieInfoSerializer(serializers.ModelSerializer):

    genres = serializers.SerializerMethodField(read_only=True)
    stars = serializers.CharField(source='get_stars')
    rating = serializers.CharField(source='get_rating')

    class Meta:
        model = Movies
        fields = ('id', 'title', 'year', 'director', 'genres', 'stars', 'rating')

    def get_genres(self, obj):
        # values = obj.get_values()
        genres = Genres.objects.filter(genresinmovies__movie=obj)

        return GenresSerializer(genres, many=True).data


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('id','name',)


class GenresInMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenresInMovies
        fields = ('genre', 'movie')
