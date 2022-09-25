from .genres import api as genres_ns
from .movies import api as movies_ns
from .directors import api as directors_ns
from .favorite_movie import api as favorite_movie_ns

__all__ = [
    'genres_ns',
    'movies_ns',
    'directors_ns',
    'favorite_movie_ns',
]
