from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

DATABASE_URL = 'postgresql+psycopg2://postgres:!QAZxsw2@127.0.0.1/mydatabase'

# engine = create_engine(DATABASE_URL)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

# Base.metadata.create_all(engine)