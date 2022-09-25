from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})


director: Model = api.model('Режисер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Комедия'),
    'description': fields.String(required=True, max_length=100, example='Комедия'),
    'trailer': fields.String(required=True, max_length=100, example='Комедия'),
    'year': fields.Integer(required=True, example=1),
    'rating':fields.Float(required=True, example=1),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email':  fields.String(required=True, max_length=100, example='Комедия'),
    'password': fields.String(required=True, max_length=100, example='Комедия'),
    'name':  fields.String(required=True, max_length=100, example='Комедия'),
    'surname':  fields.String(required=True, max_length=100, example='Комедия'),
    'favorite_genre_id': fields.Nested(genre),
})

favorite_movie: Model = api.model('Favorite_movie', {
    'id': fields.Integer(required=True, example=1),
    'user_id': fields.Nested(genre),
    'movie_id': fields.Nested(genre),
})
