from marshmallow import Schema, fields

class UserGetByIdSchema(Schema):
    auth_id = fields.UUID(required=True)
    user_id = fields.UUID(required=True)
    