from marshmallow import Schema, fields, post_load, validate

from app.models.users_model import User


class UserSchema(Schema):
    auth_id = fields.UUID(required=True)
    name = fields.String(required=True)
    gender = fields.String(
        required=True,
        validate=validate.OneOf(
            [
                "Feminino",
                "Masculino",
                "Outro",
            ]
        ),
    )
    profile_photo = fields.Url(allow_none=True)

    @post_load
    def make_user(self, data, **kwargs):
        name = data.get("name")
        data["name"] = name.title()
        return User(**data)
