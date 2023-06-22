#!/usr/bin/python3
""" user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
import os


class User(BaseModel, Base):
    """ class for user
    """
    __tablename__ = 'users'

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade='all, delete', backref='user')
        reviews = relationship("Review", cascade='all, delete', backref='user')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
