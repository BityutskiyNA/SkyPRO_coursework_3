from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service

api = Namespace('auth')


@api.route('/register')
class UsersView(Resource):

    def post(self):
        user = user_service.create(request.json)
        return f"Пользователь создан, id: {user.id}", 200


@api.route('/login')
class UsersView(Resource):

    def post(self):
        return user_service.auth_by_email(request.json), 200

    def put(self):
        return user_service.auth_by_refresh_token(request.json), 201