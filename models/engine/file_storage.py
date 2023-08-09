#!/usr/bin/python3
"""file_storage.py module for storingand persisting model data."""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """
    FileStorage class for storing and persisting model data:
    ------------------
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        public instance method that returns the
        dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        public instance method that sets in __objects
        the obj with key <obj class name>.id
        Variables:
        ----------
        key [str] -- key format generated.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        public instance method that serializes __objects
        to the JSON file (path: __file_path).
        Variables:
        ----------
        my_dict [dict] -- keys and values to build JSON.
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(my_dict, my_file)

    def reload(self):
        """
        public instance method that deserializes a JSON
        file to __objects.
        """
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                my_dict = json.load(my_file)

            for key, value in my_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
