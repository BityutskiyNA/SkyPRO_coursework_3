from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'
    name = Column(String(100), unique=True, nullable=False)


class User(models.Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    name = Column(String)
    surname = Column(String)
    favorite_genre_id = Column(Integer, ForeignKey("genres.id"))
    favorite_genre = relationship("Genre")

class Movie(models.Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    trailer = Column(String(255))
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    director_id = Column(Integer, ForeignKey("director.id"))
    genre = relationship("Genre")
    director = relationship("Director")

class Director(models.Base):
    __tablename__ = 'director'
    name = Column(String(255))

class Favorite_movie(models.Base):
    __tablename__ = 'favorite_movie'
    user_id = Column(Integer, ForeignKey("user.id"))
    movie_id = Column(Integer, ForeignKey("movie.id"))
    user = relationship("User")
    movie = relationship("Movie")