from django.contrib import admin

<<<<<<< HEAD
from .models import Movie, Actor, Genre, CinemaHall, MovieSession, Order, Ticket

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(CinemaHall)
=======
from .models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
    Order,
    Ticket,
)

admin.site.register(CinemaHall)
admin.site.register(Genre)
admin.site.register(Actor)
>>>>>>> 1f225beee00415b859782acdae7cb6ded83764f9
admin.site.register(Movie)
admin.site.register(MovieSession)
admin.site.register(Order)
admin.site.register(Ticket)
