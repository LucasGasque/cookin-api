from dataclasses import dataclass
from uuid import uuid4

from app.configs.database import db
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import ARRAY, ENUM, UUID


@dataclass
class RecipesModel(db.Model):

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
        ENUM("Doce", "Salgado", "Bebida", name="category"), nullable=False
    )
    ingredients = Column(ARRAY(String), nullable=False)
    instructions = Column(ARRAY(String), nullable=False)
    public = Column(Boolean, default=False)
    preparation_time = Column(DateTime, nullable=False)
    difficulty = Column(
        ENUM("Fácil", "Intermediário", "Difícil", name="difficulty"), nullable=False
    )
    portion_size = Column(String(50), nullable=False)
    image_url = Column(String)
    author = Column(String(100))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
