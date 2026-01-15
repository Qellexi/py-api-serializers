from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet, GenreAPIView, ActorAPIView, CinemaHallViewSet

app_name = "cinema"

router = routers.DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')

cinema_hall_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create",
})

cinema_hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("genres/", GenreAPIView.as_view()),
    path("genres/<int:pk>/", GenreAPIView.as_view()),

    path("actors/", ActorAPIView.as_view()),
    path("actors/<int:pk>/", ActorAPIView.as_view()),

    path("cinema_halls/", cinema_hall_list),
    path("cinema_halls/<int:pk>/", cinema_hall_detail),

    path("", include(router.urls)),
]
