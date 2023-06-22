#!/usr/bin/python3
""" state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from models.city import City
from sqlalchemy.orm import relationship
import models
import os

class State(BaseModel, Base):
    """ class for State
    """
    __tablename__ = 'states'
    if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
        name = ''

        @property
        def cities(self):
            """
            Info for cities
            """
            new_list = []
            all_entries = models.storage.all(City)
            for key, value in all_entries.items():
                if self.id == value.state_id:
                    new_list.append(value)

            return new_list
    else:
        name = Column("name", String(128), nullable=False)
        cities = relationship("City", cascade='all, delete', backref='state')
