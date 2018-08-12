from django.db import models


class Movies(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.CharField(max_length=100)


class Stars(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()


class StarsInMovies(models.Model):
    star_id = models.ForeignKey('Stars',
                                on_delete=models.SET_NULL, null=True)
    movie_id = models.ForeignKey('Movies',
                                 on_delete=models.CASCADE)


class Genres(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)


class GenresInMovies(models.Model):
    genre_id = models.ForeignKey('Genres',
                                 on_delete=models.SET_NULL, null=True)
    movie_id = models.ForeignKey('Movies',
                                 on_delete=models.CASCADE)


class Customers(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cc_id = models.ForeignKey('CreditCards',
                              on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=20)


class Sales(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey('Customers',
                                    on_delete=models.SET_NULL, null=True)
    movie_id = models.ForeignKey('Movies',
                                 on_delete=models.SET_NULL, null=True)
    sale_date = models.DateField()


class CreditCards(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    expiration = models.DateField()


class Ratings(models.Model):
    movie_id = models.ForeignKey('Movies',
                                 on_delete=models.CASCADE)
    rating = models.FloatField()
    num_votes = models.IntegerField()
