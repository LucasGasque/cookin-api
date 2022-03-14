from app.configs.database import db

from dataclasses import dataclass

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer


@dataclass
class RecipesRating(db.Model):
    rating: int

    __tablename__ = "recipes_rating"

    rating = Column(Integer, nullable=False)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.auth_id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    recipe_id = Column(
        UUID(as_uuid=True),
        ForeignKey("recipes.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
