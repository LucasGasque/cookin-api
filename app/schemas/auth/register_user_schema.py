from marshmallow import Schema, ValidationError, fields, post_load, validates
from app.models.auth_model import Auth


class RegisterUserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)

    @validates("password")
    def validate_password(self, password):
        if len(password) < 6:
            raise ValidationError("Error: password needs to be above 6 characthers")

    @post_load
    def make_auth(self, data, **kwargs):
        email = data.get("email")
        data["email"] = email.lower()
        return Auth(**data)
