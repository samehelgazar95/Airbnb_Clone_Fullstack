#!/usr/bin/python3
"""City class model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class City(BaseModel, Base):
    """
    City class:
        |City|---<|Place| (One to Many)
    """

    if models.storage_type == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship('State', back_populates='cities')
        places = relationship('Place', back_populates='city',
                              cascade='all, delete, delete-orphan')
    else:
        state_id: str = ''
        name: str = ''
