#!/usr/bin/python3
"""
Database Storage
"""
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from sqlalchemy import (create_engine)
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """
    Database Storage Class
    """

    __classes = {"User": User, "State": State,
                 "City": City, "Place": Place,
                 "Review": Review, "Amenity": Amenity}
    __engine = None
    __session = None

    def __init__(self):
        """
        Method __init__
        """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            user, password, host, database), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Method all
        """
        return_dict = {}
        if cls is None:
            for entry in self.__classes:
                results = self.__session.query(self.__classes[entry]).all()
                for result in results:
                    key = result.__class__.__name__ + '.' + result.id
                    return_dict[key] = result
        else:
            results = self.__session.query(cls).all()
            for result in results:
                key = result.__class__.__name__ + '.' + result.id
                return_dict[key] = result
        return return_dict

    def new(self, obj):
        """
        Method new
        """
        self.__session.add(obj)

    def save(self):
        """
        Method save
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Method delete
        """
        if obj is not None:
            self.__session.delete(obj, synchronize_session=False)

    def reload(self):
        """
        Method reload
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Method Close
        """
        self.__session.close()
