#!/usr/bin/python3
"""
BaseModel class
as a parent class for other models
"""
from os import getenv
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


storage_type = getenv('HBNB_TYPE_STORAGE')
if storage_type == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """The BaseModel class"""

    DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
    key_to_del = '_sa_instance_state'

    if storage_type == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow(),
                            nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow(),
                            nullable=False)

    def __init__(self, *args, **kwargs):
        """Init method with 3 main attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.strptime(val, self.DATE_FORMAT)
                elif key == '__class__':
                    continue
                setattr(self, key, val)

    def __str__(self):
        """Editing the string representation of the object"""
        class_name = self.__class__.__name__
        clean_dict = self.__dict__.copy()
        if self.key_to_del in clean_dict.keys():
            del clean_dict[self.key_to_del]
        string = str("[{}] ({}) {}".format(class_name, self.id, clean_dict))
        return string

    def save(self):
        """
        Updating the updated_at attr to current time
        Importing the storage here
        to avoid the circular import
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """
        Deleting current instance by
        calling the delete method from storage
        """
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Editing the __dict__ representation of the object"""
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary['__class__'] = self.__class__.__name__
        if self.key_to_del in dictionary:
            del dictionary[self.key_to_del]
        return dictionary
