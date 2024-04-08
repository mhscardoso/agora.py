from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import Base


class Entity(Base):
    __tablename__ = "entity"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    image_url = Column(String)


class Edge(Base):
    __tablename__ = "edges"

    from_ = Column("from", Integer, ForeignKey("entity.id"), primary_key=True)
    to    = Column(Integer, ForeignKey("entity.id"), primary_key=True)
    description = Column(String)
