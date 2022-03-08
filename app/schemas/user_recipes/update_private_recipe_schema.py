from uuid import UUID
from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from app.utils.category_enum_type import CategoryEnumType
from app.utils.difficulty_enum_type import DifficultyEnumType


class UpdatePrivateRecipeSchema(Schema):
    
    title = fields.String()
    ingredients = fields.List(cls_or_instance=fields.String)
    instructions = fields.List(cls_or_instance=fields.String)    
    category = EnumField(CategoryEnumType, allow_none=True)
    preparation_time = fields.Integer()
    difficulty = EnumField(DifficultyEnumType, allow_none=True)    
    portion_size = fields.Integer()
    image_url = fields.Url()
    recipe_id = fields.UUID()
