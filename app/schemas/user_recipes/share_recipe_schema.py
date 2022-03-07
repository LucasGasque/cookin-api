from marshmallow import Schema, fields

class ShareRecipeSchema(Schema):
    recipe_id = fields.UUID(required=True)
