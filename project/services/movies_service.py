from typing import Optional, List

from project.dao.main import MoviesDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def get_all(self, status: Optional[int] = None, page: Optional[int] = None) -> List[Movie]:
        return self.dao.get_all_sort(status=status, page=page)