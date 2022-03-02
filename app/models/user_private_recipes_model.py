from app.configs.database import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey


class UserPrivateRecipe(db.Model):

    __tablename__ = "user_private_recipes"

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.auth_id'), nullable=False)
    recipe_id = Column(UUID(as_uuid=True), ForeignKey('recipes.id'), nullable=False)