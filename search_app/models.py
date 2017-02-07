from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    g_id = models.IntegerField(primary_key=True)
    original_name = models.CharField(max_length=200)
    img_url = models.URLField()


class UserExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_movies = models.ManyToManyField(Movie, related_name='users')
