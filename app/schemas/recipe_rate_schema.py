from marshmallow import Schema, fields, post_load

from app.models.recipes_rating_model import RecipesRating

class RecipeRateSchema(Schema):
    id = fields.UUID(required=True)
    rating = fields.Integer(required=True)

    @post_load
    def create_recipe_rate(self, data, **kwargs):
        return RecipesRating(**data)