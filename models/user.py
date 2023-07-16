#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import (Column, String)
from sqlalchemy.orm import relationship
from os import getenv
storage_type = getenv('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if storage_type == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False, default='')
        first_name = Column(String(128), default='')
        last_name = Column(String(128), default='')
        places = relationship(
                              'Place',
                              backref='user',
                              cascade='all, delete-orphan'
                            )

        reviews = relationship(
                              'Review',
                              backref='user',
                              cascade='all, delete-orphan'
                            )
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
