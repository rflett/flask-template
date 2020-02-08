from flask import Flask

from Apis import api
from Extensions.Database import db
from Extensions.Errors import ValidationError
from Extensions.ErrorHandlers import handle_error

app = Flask(__name__)

# this would normally come from a config file
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://db_user:db_pass@127.0.0.1:5432/db_name"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# add the api and its namespaces to the app
api.init_app(app)

# register the db
db.init_app(app)

# register error handlers
app.register_error_handler(ValidationError, handle_error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
