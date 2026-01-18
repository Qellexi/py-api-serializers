<<<<<<< HEAD
from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet, ActorViewSet, GenreViewSet, OrderViewSet, MovieSessionViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("actors", ActorViewSet, basename="actors")
router.register("genres", GenreViewSet, basename="genres")
router.register("orders", OrderViewSet, basename="orders")
router.register("movie_sessions", MovieSessionViewSet, basename="movie_sessions")

urlpatterns = [path("", include(router.urls)),
]
=======
# write urls here
>>>>>>> 1f225beee00415b859782acdae7cb6ded83764f9
