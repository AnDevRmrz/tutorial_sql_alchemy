from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base

class AlbumCancion(Base):
   __tablename__ = 'album_cancion'

   album = Column(Integer, ForeignKey('album.id'), primary_key=True)
   cancion = Column(Integer, ForeignKey('cancion.id'), primary_key=True)
   Canciones = relationship('cancion', secondary='album_cancion')