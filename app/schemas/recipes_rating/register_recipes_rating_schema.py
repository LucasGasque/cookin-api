from http import HTTPStatus
from http.client import BAD_REQUEST
from marshmallow import Schema, ValidationError, fields, post_load, validates

from app.models.recipes_rating_model import RecipesRating

class RecipeRateSchema(Schema):
    recipe_id = fields.UUID(required=True) 
    rating = fields.Integer(required=True)
    user_id = fields.UUID(required=True)
    
    @validates("rating")
    def validate_rating(self, rating):
        if rating < 1 or rating > 5:
            raise ValidationError("Error: rating must be between 1 to 5")

    @post_load
    def create_recipe_rate(self, data, **kwargs):
        return RecipesRating(**data)