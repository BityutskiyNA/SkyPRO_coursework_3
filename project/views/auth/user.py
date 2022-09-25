from flask import request
from flask_restx import Namespace, Resource

from decorators import auth_required
from project.container import user_service

api = Namespace('user')


@api.route('/')
class UsersView(Resource):
    @auth_required
    def get(self, user_id):
        user = user_service.get_item(user_id)
        return f"Пользователь: {user.email}", 200

    @auth_required
    def patch(self, user_id):
        user = user_service.update(request.json, user_id)
        return f"Пользователь создан, id: {user.id}", 200


@api.route('/password')
class UsersView(Resource):
    @auth_required
    def put(self,user_id):
        user = user_service.update_password(request.json, user_id)
        return "Пароль успешно изменен", 201