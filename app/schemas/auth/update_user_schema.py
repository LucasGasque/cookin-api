from marshmallow import Schema, fields, validate


class UpdateUserSchema(Schema):
    auth_id = fields.UUID(required=True)
    name = fields.String()
    gender = fields.String(
        validate=validate.OneOf(
            [
                "Feminino",
                "Masculino",
                "Outro",
            ]
        ),
    )
    profile_photo = fields.Url(allow_none=True)
