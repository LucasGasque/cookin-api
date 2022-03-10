from marshmallow import Schema, fields

class DeletePrivateRecipeSchema(Schema):
    recipe_id = fields.UUID(required=True)
    auth_id = fields.UUID(required=True)