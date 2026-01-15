from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Genre: {self.name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Actor: {self.first_name} {self.last_name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return f"CinemaHall: {self.name} (rows: {self.rows}, seats_in_row: {self.seats_in_row})"

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"Movie: {self.title} - {self.duration} ({self.description})"
