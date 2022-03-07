from marshmallow import Schema, fields,post_load,pre_load,validates

from app.exc.category_error import CategoryError
from app.exc.difficulty_error import DifficultyError
from app.models.recipes_model import Recipe


class RecipeSchema(Schema):        
    
    title = fields.String(required=True)
    image_url = fields.Url()
    portion_size = fields.Integer()
    category = fields.String(required=True)
    ingredients = fields.List(cls_or_instance=fields.String)
    instructions = fields.List(cls_or_instance=fields.String)
    public = fields.Boolean()
    preparation_time = fields.Time(format="%H:%M")
    difficulty = fields.String(required=True)
    created_at = fields.DateTime(format="%d/%m/%Y %H:%M:%S")
    author = fields.String() 

    
    @pre_load
    def normalize_title(self, data, **kwargs):
        title = data.get('title')
        if not title:
            raise KeyError
        data['title'] = title.title()
        return data   
    
    
    @validates('category')
    def validate_category(self, category):
        if category.lower() not in ["doce", "salgado", "bebida"]:
            raise CategoryError(description={
                "error": "Category should be 'Doce', 'Salgado' or 'Bebida'."
            })        
        
        return category.title()
    
    
    @validates('difficulty')
    def validate_difficulty(self, difficulty):
        if difficulty.lower() not in ["fácil", "intermediário", "difícil"]:
            raise DifficultyError(description={
                "error": "Difficulty should be 'Fácil', 'Intermediário' or 'Difícil'."
            })
        
        return difficulty.title()  
    
    
    @post_load
    def create_recipe(self,data,**kwargs):
        return Recipe(**data)
    