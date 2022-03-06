from email.policy import strict
from marshmallow import Schema, ValidationError, fields, post_load, pre_load, validates
from app.models.users_model import User


class UserSchema(Schema):
    auth_id = fields.UUID(required=True)
    name = fields.String(required=True, strict=True)
    gender = fields.String(required=True, strict=True)
    profile_photo = fields.String(allow_none=True, strict=True)

    @pre_load
    def receive_data(self, data, **kwargs):
        gender = data.get("gender")
        if type(gender) == str:
            data["gender"] = gender.title()
        return data

    @validates("gender")
    def validate_gender(self, gender):
        if gender not in ["Feminino", "Masculino", "Outro"]:
            raise ValidationError("Error: gender must be either 'Feminino', 'Masculino' or 'Outro'")

    @post_load
    def make_user(self, data, **kwargs):
        name = data.get("name")
        profile_photo = data.get("profile_photo")
        data["name"] = name.title()
        data["profile_photo"] = profile_photo.lower()
        return User(**data)
