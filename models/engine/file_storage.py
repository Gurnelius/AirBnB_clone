#!/usr/bin/python3
"""
        FileStorage that serializes instances to a JSON file
        and deserializes JSON file to instances
"""

import json
from os import path


class FileStorage:
        """
        A class for serializing instances to a JSON file and deserializing
        JSON files to instances.

        Private class attributes:
                __file_path: str - path to the JSON file (default: 'file.json')
                __objects: dict - empty but will store all objects by <class name>.id 
                                (e.g., to store a BaseModel object with id=12121212, 
                                the key will be 'BaseModel.12121212')

        Public instance methods:
                all(self):
                Returns:
                        dict: A dictionary containing all stored objects by their IDs.

                new(self, obj):
                Adds a new object to the storage.

                Args:
                        obj: An instance of a class to be stored.

                save(self):
                Serializes stored objects to the JSON file specified by __file_path.

                reload(self):
                Deserializes the JSON file specified by __file_path to populate the storage.
                If the file does not exist, this method does nothing.
        """
        
        __file_path = "file.json"
        __objects = {}
                
        def all(self):
                """Returns the dictionary __objects."""
                return self.__objects

        def new(self, obj):
                """Sets in __objects the obj with key <obj class name>.id."""
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                self.__objects[key] = obj

        def save(self):
                """Serializes __objects to the JSON file."""
                serialized_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
                with open(self.__file_path, 'w') as f:
                        json.dump(serialized_objs, f)

        def reload(self):
                """
                Deserializes the JSON file to __objects.

                If the JSON file (__file_path) exists, it populates __objects with the deserialized data.
                Otherwise, does nothing.
                """
                from models.base_model import BaseModel
                
                if path.exists(self.__file_path):
                        with open(self.__file_path, 'r') as f:
                                data = json.load(f)
                        # Dictionary to hold class names and the corresponding classes
                        class_map = {
                                "BaseModel": BaseModel  # Add more mappings for other classes if needed
                        }
                        for key, value in data.items():
                                class_name, obj_id = key.split('.')
                                # Get the class from the dictionary
                                cls = class_map.get(class_name)
                                if cls:
                                        # Create an instance of the class with its attributes
                                        obj = cls(**value)
                                        # Add the object to __objects
                                        self.__objects[key] = obj
