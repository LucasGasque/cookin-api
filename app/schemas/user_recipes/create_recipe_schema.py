from marshmallow import Schema, fields, post_load, pre_load, validate

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

    @pre_load
    def normalize_title(self, data, **kwargs):
        title = data.get("title")
        if not title:
            raise KeyError
        data["title"] = title.title()
        return data

    @pre_load
    def normalize_ingredients(self, data, **kwargs):
        ingredients = data.get("ingredients")
        data["ingredients"] = [ingredient.title().strip() for ingredient in ingredients]
        if not ingredients:
            raise KeyError
        return data

    @pre_load
    def normalize_instructions(self, data, **kwargs):
        instructions = data.get("instructions")
        data["instructions"] = [instruction.title().strip() for instruction in instructions]
        if not instructions:
            raise KeyError
        return data

    @post_load
    def create_recipe(self, data, **kwargs):
        return Recipe(**data)
