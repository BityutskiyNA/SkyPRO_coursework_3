from project.dao.main import Favorite_movieDAO


class Favorite_movie_service:
    def __init__(self, dao: Favorite_movieDAO) -> None:
        self.dao = dao

    def create(self, user_d):
        self.dao.create(user_d)
        raise self.dao.create(user_d)

    def delete(self, user_id):
        return self.dao.deete(user_id)
