#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
from os import getenv
storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == "db":
    place_amenity = Table(
                          'place_amenity',
                          Base.metadata,
                          Column(
                                 'place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 nullable=False,
                                 primary_key=True),
                          Column(
                                 'amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 nullable=False,
                                 primary_key=True)
                         )


class Place(BaseModel, Base):
    """ A place to stay """
    if storage_type == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), default='')
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)

        reviews = relationship(
                              'Review',
                              backref='place',
                              cascade='all, delete-orphan'
                              )

        amenities = relationship(
                                 'Amenity',
                                 secondary=place_amenity,
                                 viewonly=False,
                                )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """returns list of amenity instances base on
            the attribute `amenity_ids` that
            contains all `Amenity.id` linked to the Place
            """
            all_amenities = models.storage.all(Amenity).values()
            return [a for a in all_amenities if a.place_id == self.id]

        @amenities.setter
        def amenities(self, amenity):
            """Populate the amenity_ids attribute with amenity ids"""
            if type(amenity).__name__ == Amenity:
                self.amenity_ids.append(amenity.id)
            else:
                return

    @property
    def reviews(self):
        """returns the list of reviews with place_id = current Place.id"""
        reviews = models.storage.all(Review)
        list_of_reviews = [r for r in reviews if r.place_id == self.id]
        return list_of_review
