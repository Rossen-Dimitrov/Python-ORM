from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from musicApp.settings import Base


class Album(Base):
    __tablename__ = 'albums'

    id = Column(
        Integer,
        primary_key=True
    )
    album = Column(
        String(30),
        nullable=False,
    )
    image = Column(
        String(250),
        nullable=False,
    )
    price = Column(
        Float,
        nullable=False
    )
    songs = relationship(
        'Song',
        back_populates='albums',
        cascade="all, delete-orphan"
    )


class Song(Base):
    __tablename__ = 'songs'

    id = Column(
        Integer,
        primary_key=True
    )
    song = Column(
        String(200),
        nullable=False,
    )
    album_id = Column(
        Integer,
        ForeignKey('albums.id'),
    )
    album = relationship(
        'Album',
        back_populates='songs'
    )
