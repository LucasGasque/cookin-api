from app.configs.database import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey


class UserPrivateRecipe(db.Model):

    __tablename__ = "user_private_recipes"

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.auth_id', ondelete="CASCADE"), primary_key=True, nullable=False)
    recipe_id = Column(UUID(as_uuid=True), ForeignKey('recipes.id', ondelete="CASCADE"), primary_key=True, nullable=False)

    owner_id_to_favorites = db.relationship(
        "Recipe", backref="owner_to_favorites", uselist=False
    )