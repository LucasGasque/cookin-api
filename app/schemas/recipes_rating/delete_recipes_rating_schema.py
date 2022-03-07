from marshmallow import Schema, fields, post_load

from app.models.recipes_rating_model import RecipesRating

class RatingRecipeDeleteSchema(Schema):
    recipe_id = fields.UUID(required=True)
    auth_id = fields.UUID(required=True)

@post_load
def delete_rate(self, data, **kwargs):
    return RecipesRating(data)