#!/usr/bin/python3
'''class inherent of BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''class amenity that inherits from the base class'''

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
