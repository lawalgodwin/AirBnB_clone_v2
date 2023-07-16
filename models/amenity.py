#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from os import getenv
storage_type = getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    if storage_type == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)

    else:
        name = ""
