#!/usr/bin/python3
""" city class"""
from sqlalchemy import Column, String, Integer, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.place import Place
import os


class City(BaseModel, Base):
    """City Class
    Attribs:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade='all, delete', backref='cities')
    else:
        name = ''
        state_id = ''
