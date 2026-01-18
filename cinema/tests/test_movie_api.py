from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

<<<<<<< HEAD
from cinema.serializers import MovieSerializer
from cinema.models import Movie
from cinema.views import MovieViewSet
from rest_framework.viewsets import ModelViewSet
=======
from cinema.models import Movie, Genre, Actor
>>>>>>> 1f225beee00415b859782acdae7cb6ded83764f9


class MovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
<<<<<<< HEAD
        Movie.objects.create(
            title="Titanic",
            description="Titanic description",
            duration=200,
        )
        Movie.objects.create(
            title="Batman",
            description="Batman description",
            duration=190,
        )

    def test_movie_viewset_is_subclass_model_viewset(self):
        self.assertTrue(issubclass(MovieViewSet, ModelViewSet))

    def test_get_movies(self):
        movies = self.client.get("/api/cinema/movies/")
        serializer = MovieSerializer(Movie.objects.all(), many=True)
        self.assertEqual(movies.status_code, status.HTTP_200_OK)
        self.assertEqual(movies.data, serializer.data)
=======
        drama = Genre.objects.create(
            name="Drama",
        )
        comedy = Genre.objects.create(
            name="Comedy",
        )
        actress = Actor.objects.create(first_name="Kate", last_name="Winslet")
        movie = Movie.objects.create(
            title="Titanic",
            description="Titanic description",
            duration=123,
        )
        movie.genres.add(drama)
        movie.genres.add(comedy)
        movie.actors.add(actress)

    def test_get_movies(self):
        movies = self.client.get("/api/cinema/movies/")
        titanic = {
            "title": "Titanic",
            "description": "Titanic description",
            "duration": 123,
            "genres": ["Drama", "Comedy"],
            "actors": ["Kate Winslet"],
        }
        print(movies.data)
        self.assertEqual(movies.status_code, status.HTTP_200_OK)
        for field in titanic:
            self.assertEqual(movies.data[0][field], titanic[field])
>>>>>>> 1f225beee00415b859782acdae7cb6ded83764f9

    def test_post_movies(self):
        movies = self.client.post(
            "/api/cinema/movies/",
            {
                "title": "Superman",
                "description": "Superman description",
<<<<<<< HEAD
                "duration": 170,
=======
                "duration": 123,
                "actors": [1],
                "genres": [1, 2],
>>>>>>> 1f225beee00415b859782acdae7cb6ded83764f9
            },
        )
        db_movies = Movie.objects.all()
        self.assertEqual(movies.status_code, status.HTTP_201_CREATED)
<<<<<<< HEAD
        self.assertEqual(db_movies.count(), 3)
=======
        self.assertEqual(db_movies.count(), 2)
>>>>>>> 1f225beee00415b859782acdae7cb6ded83764f9
        self.assertEqual(db_movies.filter(title="Superman").count(), 1)

    def test_post_invalid_movies(self):
        movies = self.client.post(
            "/api/cinema/movies/",
            {
                "title": "Superman",
                "description": "Superman description",
<<<<<<< HEAD
                "duration": "two hundred",
=======
                "duration": 123,
                "actors": [
                    {
                        "id": 3,
                    }
                ],
>>>>>>> 1f225beee00415b859782acdae7cb6ded83764f9
            },
        )
        superman_movies = Movie.objects.filter(title="Superman")
        self.assertEqual(movies.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(superman_movies.count(), 0)

    def test_get_movie(self):
<<<<<<< HEAD
        response = self.client.get("/api/cinema/movies/2/")
        serializer = MovieSerializer(
            Movie(
                id=2,
                title="Batman",
                description="Batman description",
                duration=190,
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
=======
        response = self.client.get("/api/cinema/movies/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Titanic")
        self.assertEqual(response.data["description"], "Titanic description")
        self.assertEqual(response.data["duration"], 123)
        self.assertEqual(response.data["genres"][0]["name"], "Drama")
        self.assertEqual(response.data["genres"][1]["name"], "Comedy")
        self.assertEqual(response.data["actors"][0]["first_name"], "Kate")
        self.assertEqual(response.data["actors"][0]["last_name"], "Winslet")
        self.assertEqual(
            response.data["actors"][0]["full_name"], "Kate Winslet"
        )
>>>>>>> 1f225beee00415b859782acdae7cb6ded83764f9

    def test_get_invalid_movie(self):
        response = self.client.get("/api/cinema/movies/100/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_movie(self):
        self.client.put(
            "/api/cinema/movies/1/",
            {
                "title": "Watchman",
                "description": "Watchman description",
<<<<<<< HEAD
                "duration": 190,
=======
                "duration": 321,
                "genres": [1, 2],
                "actors": [1],
>>>>>>> 1f225beee00415b859782acdae7cb6ded83764f9
            },
        )
        db_movie = Movie.objects.get(id=1)
        self.assertEqual(
<<<<<<< HEAD
            [db_movie.title, db_movie.description, db_movie.duration],
            [
                "Watchman",
                "Watchman description",
                190,
=======
            [db_movie.title, db_movie.description],
            [
                "Watchman",
                "Watchman description",
>>>>>>> 1f225beee00415b859782acdae7cb6ded83764f9
            ],
        )
        self.assertEqual(db_movie.title, "Watchman")

<<<<<<< HEAD
    def test_put_invalid_movie(self):
        response = self.client.put(
            "/api/cinema/movies/1/",
            {
                "title": "Watchmen",
                "description": "Watchmen description",
                "duration": "fifty",
            },
        )
        db_movie = Movie.objects.get(id=1)
        self.assertEqual(db_movie.duration, 200)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_movie(self):
        response = self.client.patch(
            "/api/cinema/movies/1/",
            {
                "title": "Watchmen",
            },
        )
        db_movie = Movie.objects.get(id=1)
        self.assertEqual(db_movie.title, "Watchmen")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_invalid_movie(self):
        response = self.client.patch(
            "/api/cinema/movies/1/",
            {
                "duration": "fifty",
            },
        )
        db_movie = Movie.objects.get(id=1)
        self.assertEqual(db_movie.duration, 200)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

=======
>>>>>>> 1f225beee00415b859782acdae7cb6ded83764f9
    def test_delete_movie(self):
        response = self.client.delete(
            "/api/cinema/movies/1/",
        )
        db_movies_id_1 = Movie.objects.filter(id=1)
        self.assertEqual(db_movies_id_1.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_movie(self):
        response = self.client.delete(
            "/api/cinema/movies/1000/",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
