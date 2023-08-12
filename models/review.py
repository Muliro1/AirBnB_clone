#!/usr/bin/python3
'''class inherent of BaseModel'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''class Review that inherits from the base class'''

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
