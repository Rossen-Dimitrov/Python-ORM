from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Text

Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recepie'
    id = Column(
        Integer,
        primary_key=True,
    )
    name = Column(
        String(100),
        nullable=False,
    )
    ingredients = Column(
        Text,
        nullable=False,
    )
    instructions = Column(
        Text,
        nullable=False,
    )

