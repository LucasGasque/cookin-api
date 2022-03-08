from marshmallow import Schema, fields

class GetPrivateRecipeByIdSchema(Schema):
    auth_id = fields.UUID(required=True)
    recipe_id = fields.UUID(required=True)