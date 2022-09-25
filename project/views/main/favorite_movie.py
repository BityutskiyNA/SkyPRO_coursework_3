from flask import request
from flask_restx import Namespace, Resource

from decorators import auth_required
from project.container import favorite_movie_dao

api = Namespace('favorites')


@api.route('/movies/<int:movie_id>')
class UsersView(Resource):
    @auth_required
    def post(self, movie_id, user_id):
        user = favorite_movie_dao.create(movie_id, user_id)
        return f"Запись создана: {user.id}", 200

    @auth_required
    def delete(self, user_id, movie_id):
        user = favorite_movie_dao.delete(movie_id, user_id)
        return f"Запись удалена", 200
