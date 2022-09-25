from typing import Optional, List

from flask_sqlalchemy import BaseQuery
from sqlalchemy import desc
from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO, T
from project.models import Genre, Movie, Director, User, Favorite_movie


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre

class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all_sort(self, status, page: Optional[int] = None) -> List[T]:
        stmt: BaseQuery = self._db_session.query(self.__model__)

        if status == 'new':
            stmt = stmt.order_by(desc(self.__model__.year))

        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()

class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director

class UsersDAO(BaseDAO[User]):
    __model__ = User

    def create(self, user_d):
        ent = User(**user_d)
        self._db_session.add(ent)
        self._db_session.commit()
        return ent

    def get_by_email(self, email):
        return self._db_session.query(User).filter_by(email=email).all()

    def update(self, user_d, user_id):
        user = self.get_by_id(user_id)
        if user_d.get("surname") != None:
            user.surname = user_d.get("surname")
        if user_d.get("name") != None:
            user.name = user_d.get("name")
        if user_d.get("favorite_genre_id") != None:
            user.favorite_genre_id = user_d.get("favorite_genre_id")

        self._db_session.add(user)
        self._db_session.commit()

        return user

    def update_password(self, new_password, user_id):
        user = self.get_by_id(user_id)
        user.password = new_password

        self._db_session.add(user)
        self._db_session.commit()

        return user

class Favorite_movieDAO(BaseDAO[Favorite_movie]):
    __model__ = Favorite_movie

    def create(self,movie_id, user_id):
        ent = Favorite_movie()
        ent.user_id = user_id
        ent.movie_id = movie_id
        self._db_session.add(ent)
        self._db_session.commit()
        return ent

    def delete(self, movie_id, user_id):
        ent = self._db_session.query(Favorite_movie).filter_by(user_id=user_id, movie_id=movie_id).all()
        for fm in ent:
            self._db_session.delete(fm)
        self._db_session.commit()