from marshmallow import Schema, fields, post_load

from app.models.favorite_recipes_model import FavoriteRecipe


class AddToFavoriteRecipeSchema(Schema):
    
    user_id = fields.UUID(required=True)
    recipe_id = fields.UUID(required=True)
    
    @post_load
    def add_to_favorite_recipe(self, data,**kwargs):
        return FavoriteRecipe(**data)
