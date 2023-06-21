#!/usr/bin/python3
""" place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
import os
from sqlalchemy.orm import relationship
from models.review import Review


metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    """
    __tablename__ = 'places'

    if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):

        @property
        def reviews(self):
            """
            Returns review instances
            """
            new_list = []
            all_entries = models.storage.all()
            for key, value in all_entries.items():
                split_key = entry.split('.')
                if split_key[1] == Place.id:
                    new_list.append(value)
            return new_list

        @property
        def amenities(self):
            """
            Returns amenity instances
            """
            return amenity_ids

        @amenities.setter
        def amenities(self, val):
            """
            Append Amenity.id
            """
            all_entries = models.storage.all()
            for key, value in all_entries.items():
                split_key = entry.split('.')
                if split_key[1] == Amenity.id:
                    amenity_ids.append(value)

    else:
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, backref="place_amenities")
        reviews = relationship("Review", cascade='all, delete',
                               backref='place')
