#!/usr/bin/python3
"""Unit tests for file Base Class"""
import unittest
from datetime import datetime
import os
from models.engine.file_storage import FileStorage
import models
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """UnitTest for Base Class Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_does_module_has_doc(self):
        self.assertTrue(len(models.base_model.__doc__) > 0)

    def test_does_class_has_doc(self):
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_is_basemodel_a_class(self):
        instance = BaseModel()
        cls_str = "<class 'models.base_model.BaseModel'>"
        self.assertTrue(str(instance.__class__), cls_str)

    def test_does_basemodel_has_id_attr(self):
        instance = BaseModel()
        self.assertTrue(hasattr(instance, 'id'))

    def test_does_basemodel_has_created_at_attr(self):
        instance = BaseModel()
        self.assertTrue(hasattr(instance, 'created_at'))

    def test_does_basemodel_has_updated_at_attr(self):
        instance = BaseModel()
        self.assertTrue(hasattr(instance, 'updated_at'))

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        instance = BaseModel()
        self.assertIsNotNone(instance.id)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_str(self):
        instance = BaseModel()
        instance.created_at = datetime(2024, 1, 1, 1, 1, 1, 123456)
        cls_name = instance.to_dict()['__class__']
        excepted_str = f"[{cls_name}] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), excepted_str)

    def test_to_dict(self):
        instance = BaseModel()
        instance.created_at = datetime(2024, 1, 1, 0, 0, 0, 123456)
        expected_dict = {
            'id': instance.id,
            'created_at': '2024-01-01T00:00:00.123456',
            'updated_at': instance.updated_at.isoformat(),
            '__class__': instance.to_dict()['__class__']
        }
        self.assertEqual(instance.to_dict(), expected_dict)

    def test_save(self):
        instance = BaseModel()
        instance.created_at = datetime(2024, 1, 1, 0, 0, 0, 123456)
        expected_dict = {
            'id': instance.id,
            'created_at': '2024-01-01T00:00:00.123456',
            'updated_at': instance.updated_at.isoformat(),
            '__class__': instance.to_dict()['__class__']
        }
        self.assertEqual(instance.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
