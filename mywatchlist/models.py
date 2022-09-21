from django.db import models

# Create your models here.
class MovieDetails(models.Model):
    watched = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    movie_rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField(max_length=150)