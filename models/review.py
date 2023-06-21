#!/usr/bin/python3
""" review class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Review(BaseModel, Base):
    """ class for Review
    """
    __tablename__ = 'reviews'

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column("text", String(1024), nullable=False)
