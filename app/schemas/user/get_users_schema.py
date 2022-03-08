from marshmallow import Schema, fields

class UserGetSchema(Schema):
    auth_id = fields.UUID(required=True)