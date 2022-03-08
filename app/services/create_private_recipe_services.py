from app.models.recipes_model import Recipe

def verify_values(data):

    verified_recipe: Recipe = Recipe.query.filter_by(title=data.get('title').title()).first()
    
    if verified_recipe:
        raise AttributeError('Receita já registrada')

    list_ingredients = data.get('ingredients')

    for value in list_ingredients:
        if value in list_ingredients:
            if list_ingredients.count(value) > 1:
                raise AttributeError('Ingrediente já registrado')

    list_instructions = data.get('instructions')

    for value in list_instructions:
        if value in list_instructions:
            if list_instructions.count(value) > 1:
                raise AttributeError('Instrução já registrada')
