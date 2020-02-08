from flask import request, current_app
from flask_restplus import Namespace, fields, Resource

from Extensions.Database import db
from Extensions.Errors import ValidationError
from Models.User import User

api = Namespace(
    name="User",
    path="/user",
    description="Manage a user"
)

user_request = api.model("User Request", {
    "username": fields.String(required=True),
    "email": fields.String(required=True),
    "age": fields.Integer(min=1, max=99),
    "city": fields.String(enum=["BNE", "MEL", "SYD"])
})
user_response = api.inherit("User Response", user_request, {
    "id": fields.Integer
})


@api.route("/")
class UserController(Resource):
    @api.expect(user_request, validate=True)
    @api.marshal_with(user_response, code=201)
    def post(self, **kwargs):
        """Create a user"""
        body = request.get_json()

        # check user doesn't exist
        if db.session.query(User.id).filter_by(username=body["username"]).scalar() is not None:
            current_app.logger.info(f"user {body['username']} exists")
            raise ValidationError("Sorry, that username is already taken!")

        # create user
        new_user = User(
            username=body["username"],
            email=body["email"],
            age=body.get("age"),
            city=body.get("city"),
        )
        new_user.save()

        current_app.logger.info(f"created user {new_user.username}")

        return new_user.asdict(), 201
