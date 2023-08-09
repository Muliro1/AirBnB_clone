#!/usr/bin/python3
'''A class user that inherits from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    '''represent a class User for the models'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
