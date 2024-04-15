#!/usr/bin/python3
"""
DataBase Storage using SQLAlchemy
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review


classes = {'BaseModel': BaseModel, 'Amenity': Amenity,
              'City': City, 'Place': Place, 'Review': Review,
              'State': State, 'User': User}


class DBStorage():
    """
    Manipulate the DB that's storing data
    Arguments:
        __engine: engine var to start the db
        __session: Session that's used to manipulate db
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        DBStorage Constructor
        getting the needed variables from the environment to create
        the database url that's needed for creating the database engine
        and drops all tables if HBNB_ENV is set to 'test'
        """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        db_url = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, db_name)
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Get all objects from the database.
        If a class is specified, return all objects of that class.
        Otherwise, return all objects from all classes.
        Returns:
            dict: A dictionary containing objects indexed by their ID.
        """
        objs_list = []
        objs_dict = {}
        if cls:
            objs_list = self.__session.query(cls).all()
        else:
            for curr_cls in Base.__subclasses__():
                data = self.__session.query(curr_cls).all()
                objs_list.extend(data)
        for obj in objs_list:
            key = '{}.{}'.format(obj.to_dict()['__class__'],
                                 obj.to_dict()['id'])
            objs_dict[key] = obj
        return objs_dict

    def new(self, obj):
        """Add a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creating the tables when importing the module
        and creating session factory using scoped session
        which will handle closing the session automatically
        and make the session is thread-safe
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the current database session"""
        self.__session.close()

    def get(self, cls, id):
        """
        Retrieve one object or None if not found
        """
        if cls not in classes.values():
            return None

        cls_name = cls.__name__
        cls_key = f"{cls_name}.{id}"
        return self.all(classes[cls_name]).get(cls_key, None)

    def count(self, cls=None):
        """
        Count the number of objects in storage
        if cls passed returns count of this cls,
        if not passed, returns count of all objs
        """
        if cls:
            return len(self.all(cls).values())
        else:
            return len(self.all().values())
