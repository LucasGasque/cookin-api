from dataclasses import dataclass

from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy import Column, ForeignKey, String

from app.configs.database import db

@dataclass
class User(db.Model):
    name: str
    gender: str
    profile_photo: str

    __tablename__ = "users"

    auth_id = Column(UUID(as_uuid=True), ForeignKey("auths.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    gender = Column(ENUM("Feminino", "Masculino", "Outro", name="gender"), nullable=False)
    profile_photo = Column(String, default="https://w7.pngwing.com/pngs/442/477/png-transparent-computer-icons-user-profile-avatar-profile-heroes-profile-user-thumbnail.png")  

    auth = db.relationship(
      "Auth",
      backref=db.backref("user", uselist=False, cascade="all,delete")
    )
    
    private_recipe = db.relationship("Recipe", secondary='user_private_recipes', backref=db.backref("recipe", uselist=True))
