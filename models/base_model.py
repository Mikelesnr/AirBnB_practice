#!/usr/bin/python3
'''
This module contains the basemodel class for all models in this project
'''

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Custom base for all the classes in the AirBnb console project
    Arttributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime
    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj
    """

    # class constructor
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        This method returns a string
        """
        return f"[{self.__class__.__name__}],{self.id},{self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute:
        'updated_at' - with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Method returns a dictionary containing all 
        keys/values of __dict__ instance
        """
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__
        return map_objects
