import pytest

from unittest.mock import MagicMock
from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService
from setup_db import db

@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)
    stiven = Director(id=1, name='Stiven', age=74)
    martin = Director(id=1, name='Martin', age=79)
    tim = Director(id=1, name='Tim', age=63)

    director_dao.get_one = MagicMock(return_value = stiven)
    director_dao.get_all = MagicMock(return_value=[stiven, martin, tim])
    director_dao.create = MagicMock(return_value= Director(id=4))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director != None
        assert director.id != None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_new = {"name": "Kventin", "age":58}
        director = self.director_service.create(director_new)
        assert director.id != None

    def test_delete(self):
        director = self.director_service.delete(1)

    def test_update(self):
        director_new = {"id":4,"name": "Kventin", "age":58}
        director = self.director_service.update(director_new)
