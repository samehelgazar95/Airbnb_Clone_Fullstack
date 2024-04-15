#!/usr/bin/python3
"""Unit tests for file Base Class"""
import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.city import City


class TestCity(unittest.TestCase):
    """UnitTest for City Class Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_does_module_has_doc(self):
        self.assertTrue(len(models.city.__doc__) > 0)

    def test_does_class_has_doc(self):
        self.assertTrue(len(City.__doc__) > 0)

    def test_is_City_a_class(self):
        obj = City()
        self.assertTrue(str(obj.__class__), "<class 'models.city.City'>")

    def test_does_City_has_id_attr(self):
        obj = City()
        self.assertTrue(hasattr(obj, 'id'))

    def test_does_City_has_created_at_attr(self):
        obj = City()
        self.assertTrue(hasattr(obj, 'created_at'))

    def test_does_City_has_updated_at_attr(self):
        obj = City()
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_does_user_has_email_attr(self):
        instance = City()
        self.assertIsInstance(instance.state_id, str)
        self.assertIsInstance(instance.name, str)


if __name__ == "__main__":
    unittest.main()
