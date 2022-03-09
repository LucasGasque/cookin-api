from app.models.recipes_model import Recipe

def verify_values(data):

    verified_recipe: Recipe = Recipe.query.filter_by(title=data.get('title').title()).first()
    
    if verified_recipe:
        raise AttributeError('Recipe with this title already registered.')

    list_ingredients = data.get('ingredients')

    for value in list_ingredients:
        if value in list_ingredients:
            if list_ingredients.count(value) > 1:
                raise AttributeError('Repeated ingredient name are not permitted.')

    list_instructions = data.get('instructions')

    for value in list_instructions:
        if value in list_instructions:
            if list_instructions.count(value) > 1:
                raise AttributeError('Repeated instructions are not permitted.')
