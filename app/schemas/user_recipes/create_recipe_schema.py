from marshmallow import Schema, fields, post_load, validate

from app.models.recipes_model import Recipe

class RecipeSchema(Schema):
    title = fields.String(required=True)
    image_url = fields.Url()
    portion_size = fields.Integer()
    category = fields.String(
        required=True, validate=validate.OneOf(["Doce", "Salgado", "Bebida"])
    )
    ingredients = fields.List(cls_or_instance=fields.String)
    instructions = fields.List(cls_or_instance=fields.String)
    public = fields.Boolean()
    preparation_time = fields.Integer()
    difficulty = fields.String(
        required=True, validate=validate.OneOf(["Fácil", "Intermediário", "Difícil"])
    )
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    author = fields.String()

    @post_load
    def create_recipe(self, data, **kwargs):
        title = data.get("title")
        ingredients = data.get("ingredients")
        instructions = data.get("instructions")
 
        data["title"] = title.title().strip()
        data["ingredients"] = [ingredient.capitalize().strip() for ingredient in ingredients]
        data["instructions"] = [instruction.capitalize().strip() for instruction in instructions]

        return Recipe(**data)