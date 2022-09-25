import pytest

from project.dao import UsersDAO
from project.models import User


class TestUsersDAO:

    @pytest.fixture
    def users_dao(self, db):
        return UsersDAO(db.session)

    @pytest.fixture
    def genre_1(self, db):
        u = User()
        u.email =''
        u.name = ''
        u.favorite_genre_id = ''
        u.password = ''
        u.surname = ''
        db.session.add(u)
        db.session.commit()
        return u

    @pytest.fixture
    def genre_2(self, db):
        u = User()
        u.email = ''
        u.name = ''
        u.favorite_genre_id = ''
        u.password = ''
        u.surname = ''
        db.session.add(u)
        db.session.commit()
        return u


