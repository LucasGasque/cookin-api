from marshmallow import Schema, ValidationError, fields, post_load, pre_load, validates
from app.models.auth_model import Auth


class AuthSchema(Schema):
    email = fields.Email(required=True, strict=True)
    password = fields.String(required=True)

    # @pre_load
    # def normalize_email(self, data, **kwargs):
    #     email = data.get("email")
    #     # data["email"] = email.lower()
    #     return data

    @validates("password")
    def validate_password(self, password):
        if len(password) < 6:
            raise ValidationError("Error: password needs to be above 6 characthers")

    @post_load
    def make_auth(self, data, **kwargs):
        email = data.get("email")
        data["email"] = email.lower()
        return Auth(**data)
