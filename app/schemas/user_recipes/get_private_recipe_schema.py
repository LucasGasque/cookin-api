from marshmallow import Schema,fields, validate


class GetPrivateRecipeSchema(Schema):

    title = fields.String()
    category = fields.String(validate=validate.OneOf([
        "Doce", "Salgado", "Bebida"
    ]))
    difficulty = fields.String(validate=validate.OneOf([
        "Fácil", "Intermediário", "Difícil"
    ]))
    preparation_time = fields.Integer()
    portion_size = fields.Integer()
