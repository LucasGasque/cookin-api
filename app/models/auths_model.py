from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db
from app.exc.invalid_email_error import InvalidEmailError


@dataclass
class AuthModel(db.Model):
    email: str

    __tablename__ = "auths"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String(124), nullable=False, unique=True)
    password_hash = Column(String(511), nullable=False)

    @property
    def password(self):
        raise AttributeError("Not allowed to access password")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    @validates("email")
    def normalize_email(self, key, value):
        if "@" in value:
            return value.lower()
        raise InvalidEmailError(
            description={"error": "e-mail should contain @ character"}
        )
