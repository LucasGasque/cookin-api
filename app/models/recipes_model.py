from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY, ENUM, UUID
from sqlalchemy.orm import relationship, backref

from app.configs.database import db


@dataclass
class Recipe(db.Model):

    id: str
    title: str
    category: str
    ingredients: list
    instructions: list
    public: bool
    preparation_time: int
    difficulty: str
    portion_size: int
    image_url: str
    author: str
    created_at: str
    updated_at: str
    ratings: list

    __tablename__ = "recipes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(200), nullable=False)
    category = Column(
        ENUM("Doce", "Salgado", "Bebida", name="Category"), nullable=False
    )
    ingredients = Column(ARRAY(String), nullable=False)
    instructions = Column(ARRAY(String), nullable=False)
    public = Column(Boolean, default=False)
    preparation_time = Column(Integer, nullable=False)
    difficulty = Column(
        ENUM("Fácil", "Intermediário", "Difícil", name="Difficulty"), nullable=False
    )
    portion_size = Column(Integer, nullable=False)
    image_url = Column(String, default="https://i.ibb.co/1Rwkzqz/Mc-LGrrxni.jpg")    
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


    ratings = relationship(
        "RecipesRating", backref="recipes", uselist=True
    )

    author = relationship(
        "User", secondary="user_private_recipes", backref=backref("recipe", uselist=False)
    )