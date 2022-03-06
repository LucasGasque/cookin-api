from marshmallow import Schema, ValidationError, fields, post_load, pre_load, validates
from app.models.users_model import User


class UserSchema(Schema):
    auth_id = fields.UUID(required=True)
    name = fields.String(required=True)
    gender = fields.String(required=True)
    profile_photo = fields.String(required=True)

    @pre_load
    def normalize_data(self, data, **kwargs):
        name = data.get("name")
        gender = data.get("gender")
        profile_photo = data.get("profile_photo")
        data["name"] = name.title()
        data["gender"] = gender.title()
        data["profile_photo"] = profile_photo.lower()
        return data

    @validates("password")
    def validate_password(self, password):
        if len(password) < 6:
            raise ValidationError("Error: password needs to be above 6 characthers")

    @post_load
    def make_auth(self, data, **kwargs):
        return Auth(**data)
