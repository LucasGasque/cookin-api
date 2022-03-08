from marshmallow import Schema, fields, validate


class UpdateUserSchema(Schema):
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
