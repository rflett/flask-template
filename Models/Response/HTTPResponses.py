from flask_restplus import Model, fields

bad_request = Model("BadRequest", {
    "error": fields.String
})
