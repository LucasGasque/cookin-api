from marshmallow import Schema, fields, post_load
from app.models.auths_model import Auth

class AuthSchema(Schema):
    email = fields.Email()
    password_hash = fields.String()
    
    @post_load
    def make_auth(self, data, **kwargs):
        return Auth(**data)