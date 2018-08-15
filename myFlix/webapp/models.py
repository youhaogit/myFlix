from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail


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


# TODO edit manager
class CustomersManager(BaseUserManager):

    def _create_user(self, email, password, **kwargs):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)


class Customers(AbstractBaseUser, PermissionsMixin):
    """
    Customize user to be compliant with django auth system
    """
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    credit_card = models.ForeignKey('CreditCards', on_delete=models.SET_NULL,
                                    null=True, related_name='customers_creditcard')
    address = models.CharField(max_length=200)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomersManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_username(self):
        "Return the identifying username for this User"
        return str(self.id) + ':' + self.get_full_name()





