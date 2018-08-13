from django.db import models


class Movies(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ' in ' + str(self.year)

    @property
    def get_genres(self):
        genres_list = Genres.objects.filter(genresinmovies_genre__movie=self)
        return genres_list

    @property
    def get_stars(self):
        stars_list = Stars.objects.filter(starsinmovies_star__movie=self)
        return stars_list

    @property
    def get_rating(self):
        rating = Ratings.objects.filter(movie=self)
        return rating


class Stars(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()

    def __str__(self):
        return self.name


class StarsInMovies(models.Model):
    star = models.ForeignKey('Stars',
                            on_delete=models.SET_NULL, null=True, related_name='starsinmovies_star')
    movie = models.ForeignKey('Movies',
                            on_delete=models.CASCADE, related_name='starsinmovies_movie')


class Genres(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class GenresInMovies(models.Model):
    genre = models.ForeignKey('Genres',
                                 on_delete=models.SET_NULL, null=True, related_name='genresinmovies_genre')
    movie = models.ForeignKey('Movies',
                                 on_delete=models.CASCADE, related_name='genresinmovies_movie')

    def __str__(self):
        return self.movie.__str__() + " is of " + self.genre.__str__()


class Customers(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    credit_card = models.ForeignKey('CreditCards',
                              on_delete=models.SET_NULL, null=True, related_name='customers_creditcard')
    address = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=20)


class Sales(models.Model):
    id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey('Customers',
                                    on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey('Movies',
                                 on_delete=models.SET_NULL, null=True)
    sale_date = models.DateField()


class CreditCards(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    expiration = models.DateField()


class Ratings(models.Model):
    movie = models.ForeignKey('Movies',
                                 on_delete=models.CASCADE, related_name='ratings_movie')
    rating = models.FloatField()
    num_votes = models.IntegerField()
