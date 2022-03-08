from marshmallow import Schema, fields


class DeleteFromFavoritesRecipeSchema(Schema):
    user_id = fields.UUID(required=True)
    recipe_id = fields.UUID(required=True)
