import base64
import hashlib
import hmac
import calendar
import datetime
from typing import Optional, List
import jwt
from flask_restx import abort

from project.config import BaseConfig
from project.dao.main import UsersDAO
from project.exceptions import ItemNotFound
from project.models import User


base_config = BaseConfig()

class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def get_hash(self, password):
        hash_p = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), base_config.PWD_HASH_SALT,
                                     base_config.PWD_HASH_ITERATIONS)
        return base64.b64encode(hash_p)

    def create(self, user_d):
        password = user_d.get("password")
        user_d['password'] = self.get_hash(password)
        return self.dao.create(user_d)

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_by_email(self, email: int) -> User:
        if user := self.dao.get_by_email(email):
            return user
        raise ItemNotFound(f'User with email={email} not exists.')

    def get_all(self, page: Optional[int] = None) -> List[User]:
        return self.dao.get_all(page=page)

    def auth_by_email(self, data):
        email = data.get("email")
        users = self.dao.get_by_email(email)

        if not users:
            return {"error": "Неверные учётные данные"}, 401

        other_password = data.get("password")
        for user in users:
            if self.test_hash(user.password, other_password) == True:
                tokens = self.return_token(user)
                return tokens, 201
        return {"error": "Неверные учётные данные"}, 401

    def auth_by_refresh_token(self, data):
        refresh_token = data.get("refresh_token")
        try:
            token = jwt.decode(refresh_token, base_config.SECRET_HERE, algorithms=base_config.ALGO)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        user = self.dao.get_by_email(token['email'])

        if not user:
            return {"error": "Неверные учётные данные"}, 401

        tokens = self.return_token(user[0])
        return tokens, 201

    def return_token(self, user):
        data_auth = {
            "email": user.email,
            "user_id": user.id
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data_auth["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data_auth, base_config.SECRET_HERE, algorithm=base_config.ALGO)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data_auth["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data_auth, base_config.SECRET_HERE, algorithm=base_config.ALGO)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens

    def test_hash(self, password_hash, other_password):
        return hmac.compare_digest(password_hash, self.get_hash(other_password))

    def update(self, user_data, user_id):
        return self.dao.update(user_data, user_id)

    def update_password(self, user_data, user_id):
        password = user_data.get("new_password")
        new_password = self.get_hash(password)

        user = self.dao.get_by_id(user_id)

        if not user:
            return {"error": "Неверные учётные данные"}, 401

        old_password = user_data.get("old_password")


        if self.test_hash(user.password, old_password) == True:
            return self.dao.update_password(new_password, user_id), 201
        return {"error": "Неверные учётные данные"}, 401

