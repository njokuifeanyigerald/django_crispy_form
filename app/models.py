from django.db import models

class CrispyModel(models.Model):
    songs = models.CharField(max_length=500)
    name_of_artist = models.CharField(max_length=500)
    number_of_awards = models.IntegerField()
    def __str__(self):
        self.songs