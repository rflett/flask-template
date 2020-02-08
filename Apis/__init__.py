from flask_restplus import Api
from Controllers.UserController import api as user_v1
from Controllers.UsersController import api as users_v1

api = Api(
    title="My User API",
    version="1.0"
)

api.add_namespace(user_v1)
api.add_namespace(users_v1)
