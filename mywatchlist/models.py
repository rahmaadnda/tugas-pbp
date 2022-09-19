from django.db import models

class FilmWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.TextField()