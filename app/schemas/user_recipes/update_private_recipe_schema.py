from uuid import UUID
from marshmallow import Schema, fields, validate


class UpdatePrivateRecipeSchema(Schema):

    title = fields.String()
    ingredients = fields.List(cls_or_instance=fields.String)
    instructions = fields.List(cls_or_instance=fields.String)
    category = fields.String(validate=validate.OneOf(["Doce", "Salgado", "Bebida"]))
    preparation_time = fields.Integer()
    difficulty = fields.String(
        validate=validate.OneOf(["Fácil", "Intermediário", "Difícil"])
    )
    portion_size = fields.Integer()
    image_url = fields.Url()
    recipe_id = fields.UUID()
