import pytest

from unittest.mock import MagicMock
from dao.model.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService
from setup_db import db


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)
    drama = Genre(id=1, name='drama', age=74)
    sport = Genre(id=1, name='sport', age=79)
    anime = Genre(id=1, name='anime', age=63)

    genre_dao.get_one = MagicMock(return_value=drama)
    genre_dao.get_all = MagicMock(return_value=[drama, sport, anime])
    genre_dao.create = MagicMock(return_value=Genre(id=4))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre != None
        assert genre.id != None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_new = {"name": "action", "age": 58}
        genre = self.genre_service.create(genre_new)
        assert genre.id != None

    def test_delete(self):
        genre = self.genre_service.delete(1)

    def test_update(self):
        genre_new = {"id": 4, "name": "action", "age": 58}
        genre = self.genre_service.update(genre_new)
