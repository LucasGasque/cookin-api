from marshmallow import Schema, fields


class DeleteUserSchema(Schema):
    userId = fields.UUID(required=True)
