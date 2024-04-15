#!/usr/bin/python3
"""Unit tests for file Base Class"""
import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.place import Place


class TestPlace(unittest.TestCase):
    """UnitTest for Place Class Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_does_module_has_doc(self):
        self.assertTrue(len(models.place.__doc__) > 0)

    def test_does_class_has_doc(self):
        self.assertTrue(len(Place.__doc__) > 0)

    def test_is_place_a_class(self):
        obj = Place()
        self.assertTrue(str(obj.__class__), "<class 'models.place.Place'>")

    def test_does_Place_has_id_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'id'))

    def test_does_Place_has_created_at_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'created_at'))

    def test_does_Place_has_updated_at_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_does_user_has_email_attr(self):
        instance = Place()
        self.assertIsInstance(instance.city_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.name, str)
        self.assertIsInstance(instance.description, str)
        self.assertIsInstance(instance.number_rooms, int)
        self.assertIsInstance(instance.number_bathrooms, int)
        self.assertIsInstance(instance.price_by_night, int)
        self.assertIsInstance(instance.latitude, float)
        self.assertIsInstance(instance.longitude, float)
        self.assertIsInstance(instance.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
