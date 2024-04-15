#!/usr/bin/python3
"""User class model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class User(BaseModel, Base):
    """
    User class
        |User|---<|Place| (One to Many)
        |User|---<|Review| (One to Many)
    """

    if models.storage_type == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship('Place', back_populates='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', back_populates='user',
                               cascade='all, delete, delete-orphan')
    else:
        email: str = ''
        password: str = ''
        first_name: str = ''
        last_name: str = ''
