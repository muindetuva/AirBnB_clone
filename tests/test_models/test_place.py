#!/usr/bin/python3
'''
Contains all tests for the base_model class
'''
from models.base_model import BaseModel
from models.place import Place
import unittest
import os


class TestPlace(unittest.TestCase):
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

        self.model_1 = Place()
        self.model_2 = Place()

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
        Test that class Place has the required attributes and methods
        '''
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_isinstance(self):
        '''
        Check that the created instance is an instance of the BaseModel class
        '''
        self.assertIsInstance(self.model_1, BaseModel)

    def test_is_subclass(self):
        '''
        Check whethe Place is a subclass of basemodel
        '''
        self.assertTrue(issubclass(self.model_1.__class__, BaseModel))

    def test_inherited_attributes(self):
        '''
        Confirm that all the required attributes were imported from BaseModel
        Also confirm that Place's attributes are present
        '''
        self.assertTrue('id' in self.model_1.__dict__)
        self.assertTrue('created_at' in self.model_1.__dict__)
        self.assertTrue('updated_at' in self.model_1.__dict__)

if __name__ == "__main__":
    unittest.main()
