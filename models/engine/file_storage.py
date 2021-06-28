#!/usr/bin/python3
'''
Contains the file storage class
'''
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    '''
    The file storage class
    attributes:
        __file_path: A path to the json file
        __objects: A dictionary to store all objects
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
        Returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        Adds to __objects a new object
        '''
        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        serializes __objects to the JSON file (path: __file_path)
        '''
        # serialize the dictionary
        json_dict = {}
        for k, obj in FileStorage.__objects.items():
            json_dict[k] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        '''
        deserializes the JSON file to __objects
        '''
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                json_dict = json.load(f)
                for obj_dict in json_dict.values():
                    class_name = obj_dict["__class__"]
                    self.new(eval(class_name)(**obj_dict))
        except FileNotFoundError:
            return
