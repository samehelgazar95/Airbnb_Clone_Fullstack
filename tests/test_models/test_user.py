#!/usr/bin/python3
"""Unit tests for file Base Class"""
import unittest
import os
from models.engine.file_storage import FileStorage
import models
from models.user import User


class TestUser(unittest.TestCase):
    """UnitTest for User Class Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        '''Cleans up after each test_method.'''

    def test_does_module_has_doc(self):
        self.assertTrue(len(models.user.__doc__) > 0)

    def test_does_class_has_doc(self):
        self.assertTrue(len(User.__doc__) > 0)

    def test_is_user_a_class(self):
        instance = User()
        self.assertTrue(str(instance.__class__), "<class 'models.user.User'>")

    def test_does_user_has_id_attr(self):
        instance = User()
        self.assertTrue(hasattr(instance, 'id'))

    def test_does_user_has_created_at_attr(self):
        instance = User()
        self.assertTrue(hasattr(instance, 'created_at'))

    def test_does_user_has_updated_at_attr(self):
        instance = User()
        self.assertTrue(hasattr(instance, 'updated_at'))

    def test_does_user_has_email_attr(self):
        instance = User()
        self.assertIsInstance(instance.email, str)
        self.assertIsInstance(instance.password, str)
        self.assertIsInstance(instance.last_name, str)
        self.assertIsInstance(instance.first_name, str)


if __name__ == "__main__":
    unittest.main()
