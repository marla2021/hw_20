import pytest

from unittest.mock import MagicMock
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService
from setup_db import db


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)
    movie1 = Movie(id=1, name='Leon', age=74)
    movie2 = Movie(id=1, name='Fargo', age=79)
    movie3 = Movie(id=1, name='Soul', age=63)

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=4))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie != None
        assert movie.id != None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_new = {"name": "Titanik", "age": 58}
        movie = self.movie_service.create(movie_new)
        assert movie.id != None

    def test_delete(self):
        movie = self.movie_service.delete(1)

    def test_update(self):
        movie_new = {"id": 4, "name": "Titanik", "age": 58}
        movie = self.movie_service.update(movie_new)
