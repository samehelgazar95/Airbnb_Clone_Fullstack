#!/usr/bin/python3
"""Unit tests for file Base Class"""
import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.state import State


class TestState(unittest.TestCase):
    """UnitTest for State Class Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_does_module_has_doc(self):
        self.assertTrue(len(models.state.__doc__) > 0)

    def test_does_class_has_doc(self):
        self.assertTrue(len(State.__doc__) > 0)

    def test_is_state_a_class(self):
        b = State()
        self.assertTrue(str(b.__class__), "<class 'models.state.State'>")

    def test_does_state_has_id_attr(self):
        b = State()
        self.assertTrue(hasattr(b, 'id'))

    def test_does_state_has_created_at_attr(self):
        b = State()
        self.assertTrue(hasattr(b, 'created_at'))

    def test_does_state_has_updated_at_attr(self):
        b = State()
        self.assertTrue(hasattr(b, 'updated_at'))

    def test_does_user_has_email_attr(self):
        instance = State()
        self.assertIsInstance(instance.name, str)


if __name__ == "__main__":
    unittest.main()
