from rest_framework.routers import SimpleRouter
from imdb_back.users.views import CreateUserViewSet

usersRouter = SimpleRouter()
usersRouter.register(r'api/users/register', CreateUserViewSet)