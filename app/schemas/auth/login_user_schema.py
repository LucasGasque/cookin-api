from marshmallow import Schema, fields, post_load


class AuthSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)

    @post_load
    def make_auth(self, data, **kwargs):
        email = data.get("email")
        data["email"] = email.lower()
        return data
