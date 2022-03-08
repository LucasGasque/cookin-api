from marshmallow import Schema, fields

class GetFavoriteRecipesSchema(Schema):
    auth_id = fields.UUID(required=True)
