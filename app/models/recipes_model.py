from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Time
from sqlalchemy.dialects.postgresql import ARRAY, ENUM, UUID
from sqlalchemy.orm import validates

from app.configs.database import db
from app.exc.category_error import CategoryError
from app.exc.difficulty_error import DifficultyError


@dataclass
class Recipe(db.Model):

    id: str
    title: str
    category: str
    ingredients: list
    instructions: list
    public: bool
    preparation_time: str
    difficulty: str
    portion_size: str
    image_url: str
    author: str
    created_at: str
    updated_at: str

    __tablename__ = "recipes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(200), nullable=False)
    category = Column(
        ENUM("Doce", "Salgado", "Bebida", name="Category"), nullable=False
    )
    ingredients = Column(ARRAY(String), nullable=False)
    instructions = Column(ARRAY(String), nullable=False)
    public = Column(Boolean, default=False)
    preparation_time = Column(Time, nullable=False)
    difficulty = Column(
        ENUM("Fácil", "Intermediário", "Difícil", name="Difficulty"), nullable=False
    )
    portion_size = Column(Integer, nullable=False)
    image_url = Column(String)
    author = Column(String(100))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


    @validates('category')
    def validate_category(self, key, value):
        if value.lower() not in ["doce", "salgado", "bebida"]:
            raise CategoryError(description={
                "error": "Category should be 'Doce', 'Salgado' or 'Bebida'."
            })
        
        return value.title()
    
    
    @validates('difficulty')
    def validate_difficulty(self, key, value):
        if value.lower() not in ["fácil", "intermediário", "difícil"]:
            raise DifficultyError(description={
                "error": "Difficulty should be 'Fácil', 'Intermediário' or 'Difícil'."
            })
        
        return value.title()
    
    
    @validates('title', 'image_url')
    def validate_value_type(self, key, value):
        if type(value) != str:
            raise TypeError('title and image_url should be string type')
        
        return value
    
    
    @validates('portion_size')
    def validate_portion_type(self, key, value):
        if type(value) != int:
            raise TypeError('portion_size must be int type') 
        
        return value 
  