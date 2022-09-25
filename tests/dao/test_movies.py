import pytest

from project.dao import MoviesDAO
from project.models import Movie


class TestMoviesDAO:

    @pytest.fixture
    def movies_dao(self, db):
        return MoviesDAO(db.session)

    @pytest.fixture
    def movie_1(self, db):
        m = Movie()
        m.title = "Омерзительная восьмерка"
        m.year = 2015
        m.director = 2
        m.genre = 4
        m.rating = 7.8
        m.trailer = "https://www.youtube.com/watch?v=lmB9VWm0okU"
        m.description = "США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке " \
                        "Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников." \
                        "Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось" \
                        "весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… " \
                        "И один из них - не тот, за кого себя выдает."
        db.session.add(m)
        db.session.commit()
        return m

    @pytest.fixture
    def movie_2(self, db):
        m = Movie(title="Боевик")
        m.title = "Йеллоустоун"
        m.year = 2018
        m.director = 1
        m.genre = 17
        m.rating = 8.6
        m.trailer = "https://www.youtube.com/watch?v=UKei_d0cbP4"
        m.description = "Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне " \
                        "от автора «Ветреной реки»"
        db.session.add(m)
        db.session.commit()
        return m
