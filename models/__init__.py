#!/usr/bin/python3
'''
Instantiates Models
'''
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
