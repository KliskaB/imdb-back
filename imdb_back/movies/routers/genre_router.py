from rest_framework.routers import SimpleRouter
from imdb_back.movies.views import GenresViewSet

genresRouter = SimpleRouter()
genresRouter.register(r'api/movies/genres', GenresViewSet)