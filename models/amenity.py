#!/usr/bin/python3
"""Amenity class model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class Amenity(BaseModel, Base):
    """
    Amenity class
        |Amenity|>---<|Places| (Many to Many)
        |Amenity|---<|place_amenity| (One to Many)
    """

    if models.storage_type == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place = relationship('Place', secondary='place_amenity',
                             back_populates='amenities')
    else:
        name: str = ''
