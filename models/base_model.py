#!/usr/bin/python3
"""
Base model class. Other classes will be
inherited from this class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
     A base class representing a model with common attributes and methods.

    Attributes:
        id (str): A unique identifier for the instance.
        created_at (datetime): The date and time when the instance
        was created.
        updated_at (datetime): The date and time when the instance
        was last updated.

    Public Methods:
        __init__(*args, **kwargs):
            Initializes a new instance of the BaseModel class.
            If called without arguments, creates a new instance with a unique id, 
            and sets created_at and updated_at to the current datetime.
            If called with keyword arguments, initializes the instance 
            with the provided attributes.
            The provided attributes may include 'id', 'created_at', and
            'updated_at' as string representations 
            of datetime objects in ISO format ('YYYY-MM-DDTHH:MM:SS.ssssss').
        
        __str__():
            Returns a string representation of the instance in the format:
            '[BaseModel] (<id>) <__dict__>'

        save():
            Updates the 'updated_at' attribute of the instance to the current datetime.

        to_dict():
            Returns a dictionary representation of the instance.
            The dictionary contains all instance attributes,
            including 'id', 'created_at', and 'updated_at'
            converted to string representations in ISO format
            ('YYYY-MM-DDTHH:MM:SS.ssssss').
    """
    
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class."""
        if kwargs:
            class_name = kwargs.pop('__class__', None)
            if class_name is None or class_name != self.__class__.__name__:
                raise ValueError("Invalid class name provided")

            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance."""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute of the instance
        to the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        type_ = type(my_model_json[key])
        print("\t{}: ({}) - {}".format(key, type_, my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
