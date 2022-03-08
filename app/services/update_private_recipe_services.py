from werkzeug.exceptions import Conflict
from app.models.recipes_model import Recipe


def verify_recipe_title(data):
    if data:
        verify_title: Recipe = Recipe.query.filter_by(title=data).first()
        if verify_title:
            raise Conflict(description={
                'Error': 'Recipe with this title already registered.'
            })
    
    return None


def verify_repeated_ingredients(data):
    if data:
        new_data = []
        for ingredient in data:
            new_data.append(ingredient.lower().strip())
        data_set = set(new_data)
        if len(data_set) < len(new_data):
            raise Conflict(description={
                'Error': 'Repeated ingredient name are not permitted.'
            })
    
    return None


def verify_repeated_instructions(data):
    if data:
        new_data = []
        for instruction in data:
            new_data.append(instruction.lower().strip())
        data_set = set(new_data)
        if len(data_set) < len(new_data):
            raise Conflict(description={
                'Error': 'Repeated instructions are not permitted.'
            })
    
    return None
