#!/usr/bin/python3
'''
Module contains class user
'''
from base_model import BaseModel


class User(BaseModel):
    '''
    Inherits from BaseModel
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
