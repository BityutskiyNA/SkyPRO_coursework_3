import jwt
from flask import request, abort

from project.config import BaseConfig
from project.container import user_service

constants_config = BaseConfig()

def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Autorization" not in request.headers:
            abort(401)

        data = request.headers.environ['HTTP_AUTORIZATION']
        token = data.split("Bearer ")[-1]

        try:
            data_user = jwt.decode(token, constants_config.SECRET_HERE, algorithms=constants_config.ALGO)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        users = user_service.get_by_email(data_user.get('email'))
        if not users:
            return {"error": "Неверные учётные данные"}, 401

        user_id = data_user.get("user_id")

        if request.content_type != None:
            return func(request.json, user_id)

        kwargs.update({"user_id": user_id})
        return func(*args, **kwargs)

    return wrapper
