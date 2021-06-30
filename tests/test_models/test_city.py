#!/usr/bin/python3
'''
Contains all tests for the base_model class
'''
from models.base_model import BaseModel
from models.city import City
import unittest
import os


class TestCity(unittest.TestCase):
    '''
    Tests that the BaseModel works okay
    '''
    def setUp(self):
        '''
        Set up method
        Renames the file_storage file to avoid iterfering with data
        '''
        if os.path.isfile("file.json"):
            os.rename("file.json", "backup_file.json")

        self.model_1 = City()
        self.model_2 = City()

    def tearDown(self):
        '''
        Tear down method
        Does clean up
        '''
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("backup_file.json"):
            os.rename("backup_file.json", "file.json")

        del self.model_1
        del self.model_2

    def test_attributes_types(self):
        '''
        Test that all attributes are of the correct type
        '''
        self.assertTrue(type(self.model_1), BaseModel)
        self.assertTrue(type(self.model_1.name), str)

    def test_attributes_exist(self):
        '''
        Test that class City has the required attributes and methods
        '''
        self.assertTrue(hasattr(City, 'name'))
        self.assertTrue(hasattr(City, 'state_id'))

    def test_isinstance(self):
        '''
        Check that the created instance is an instance of the BaseModel class
        '''
        self.assertIsInstance(self.model_1, BaseModel)

    def test_is_subclass(self):
        '''
        Check whethe City is a subclass of basemodel
        '''
        self.assertTrue(issubclass(self.model_1.__class__, BaseModel))

    def test_inherited_attributes(self):
        '''
        Confirm that all the required attributes were imported from BaseModel
        Also confirm that City's attributes are present
        '''
        self.assertTrue('id' in self.model_1.__dict__)
        self.assertTrue('created_at' in self.model_1.__dict__)
        self.assertTrue('updated_at' in self.model_1.__dict__)

if __name__ == "__main__":
    unittest.main()
