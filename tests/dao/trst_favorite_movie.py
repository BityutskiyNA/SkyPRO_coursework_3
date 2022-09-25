import pytest

from project.dao import Favorite_movieDAO
from project.models import Favorite_movie


class TestFavoriteMovieDAO:

    @pytest.fixture
    def favorite_movie_dao(self, db):
        return Favorite_movieDAO(db.session)


    @pytest.fixture
    def genre_1(self, db):
        fm = Favorite_movie()
        fm.movie_id =''
        fm.user_id = ''
        db.session.add(fm)
        db.session.commit()
        return fm


    @pytest.fixture
    def genre_2(self, db):
        fm = Favorite_movie()
        fm.movie_id =''
        fm.user_id = ''
        db.session.add(fm)
        db.session.commit()
        return fm