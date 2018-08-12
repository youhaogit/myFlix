# Generated by Django 2.1 on 2018-08-12 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCards',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('expiration', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('cc_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.CreditCards')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='GenresInMovies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.Genres')),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('director', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('num_votes', models.IntegerField()),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Movies')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sale_date', models.DateField()),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.Customers')),
                ('movie_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.Movies')),
            ],
        ),
        migrations.CreateModel(
            name='Stars',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('birth_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StarsInMovies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Movies')),
                ('star_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.Stars')),
            ],
        ),
        migrations.AddField(
            model_name='genresinmovies',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Movies'),
        ),
    ]
