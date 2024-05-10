from django.db import models

class Song(models.Model):
    GENRES = [('c', 'classical'), ('r', 'rock')]
    thumbnail = models.CharField(max_length=122, default='default')
    name = models.CharField(max_length=122, default='song')
    genre = models.CharField(max_length=1, choices=GENRES)
    description = models.TextField(default='Some new nice song')

    def __str__(self):
        return self.name