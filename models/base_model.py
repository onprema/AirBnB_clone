#!/usr/bin/python3

"""BaseModel module: contains the BaseModel class"""
import uuid
import datetime


class BaseModel:
    """BaseModel Class"""
    def __init__(self):
        """BaseModel constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """string representation of a BaseModel object"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the updated_at attr with current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dict containing all key/vals of the instance"""
        self.__dict__['__class__'] = type(self).__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
