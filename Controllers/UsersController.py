from flask import current_app
from flask_restplus import Namespace, fields, Resource

from Models.User import User

api = Namespace(
    name="Users",
    path="/users",
    description="Manage users"
)

user_dto = api.model("User Dto", {
    "username": fields.String(required=True),
    "email": fields.String(required=True),
    "age": fields.Integer(min=1, max=99),
    "city": fields.String(enum=["BNE", "MEL", "SYD"])
})


@api.route("/")
class UsersController(Resource):
    @api.marshal_with(user_dto, as_list=True)
    @api.response(200, "Success")
    def get(self, **kwargs):
        """Get all users"""
        users = User.query.all()
        current_app.logger.info(f"returning {len(users)} users")
        return [u.asdict() for u in users], 200
