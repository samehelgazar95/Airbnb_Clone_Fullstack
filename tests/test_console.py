#!/usr/bin/python3
"""Unit tests for file Base Class"""
import os
from io import StringIO
import unittest
import json
from unittest.mock import patch
from datetime import datetime
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review


class TestConsole(unittest.TestCase):
    """UnitTest for Console Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

def test_console_methods(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('\n')
            self.assertEqual(f.getvalue(), '')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help')
            self.assertIsInstance(f.getvalue(), str)

        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd('quit')

        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd('EOF')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help quit')
            msg = "Exits the program with formatting\n"
            self.assertEqual(f.getvalue().strip(), msg.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help EOF')
            msg = "Exits the program without formatting\n"
            self.assertEqual(f.getvalue().strip(), msg.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help create')
            msg = "Creates a class of any type\n[Usage]: create <className>\n"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help show')
            msg = "Shows an individual instance of a class\n[Usage]: show <className> <objectId>\n"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help destroy')
            msg = "Destroys an individual instance of a class\n[Usage]: destroy <className> <objectId>\n"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help all')
            msg = "Shows all objects, or all of a class\n[Usage]: all <className>\n"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help update')
            msg = "Updates an object with new information\nUsage: update <className> <id> <attName> <attVal>\n"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg.strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help count')
            msg = "Usage: count <class_name>"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg.strip())


class TestConsole_BaseModel(unittest.TestCase):
    """UnitTest for Console_BaseModel Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_Console_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn(f'BaseModel.{f.getvalue().strip()}',
                          storage.all().keys())

    def test_Console_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj1 = BaseModel()
            obj2 = BaseModel()
            HBNBCommand().onecmd('all BaseModel')
            for ele in json.loads(f.getvalue()):
                self.assertEqual(ele.split(' ')[0], '[BaseModel]')

    def test_Console_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = BaseModel()
            HBNBCommand().onecmd(f'show BaseModel {obj.id}')
            msg = f'[BaseModel] ({obj.id}) {obj.__dict__}'
            self.assertEqual(f.getvalue().strip(), msg)

    def test_Console_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = BaseModel()
            HBNBCommand().onecmd(f'update BaseModel {obj.id} name "Sameh"')
            self.assertIn('name', obj.__dict__.keys())
            self.assertEqual(obj.__dict__['name'], 'Sameh')

    def test_Console_update_multiple(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = BaseModel()
            cmd_line = f'update BaseModel {obj.id} name "Sameh" age 28'
            HBNBCommand().onecmd(cmd_line)
            self.assertNotIn('age', obj.__dict__.keys())


class TestConsole_state(unittest.TestCase):
    """UnitTest for Console_State Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_Console_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State')
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn(f'State.{f.getvalue().strip()}',
                          storage.all().keys())

    def test_Console_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj1 = State()
            obj2 = State()
            HBNBCommand().onecmd('all State')
            for ele in json.loads(f.getvalue()):
                self.assertEqual(ele.split(' ')[0], '[State]')

    def test_Console_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = State()
            HBNBCommand().onecmd(f'show State {obj.id}')
            msg = f'[State] ({obj.id}) {obj.__dict__}'
            self.assertEqual(f.getvalue().strip(), msg)

    def test_Console_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = State()
            HBNBCommand().onecmd(f'update State {obj.id} name "Sameh"')
            self.assertIn('name', obj.__dict__.keys())
            self.assertEqual(obj.__dict__['name'], 'Sameh')

    def test_Console_update_multiple(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = State()
            HBNBCommand().onecmd(f'update State {obj.id} name "Sameh" age 28')
            self.assertNotIn('age', obj.__dict__.keys())


class TestConsole_city(unittest.TestCase):
    """UnitTest for Console_City Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_Console_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City')
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn(f'City.{f.getvalue().strip()}',
                          storage.all().keys())

    def test_Console_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj1 = City()
            obj2 = City()
            HBNBCommand().onecmd('all City')
            for ele in json.loads(f.getvalue()):
                self.assertEqual(ele.split(' ')[0], '[City]')

    def test_Console_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = City()
            HBNBCommand().onecmd(f'show City {obj.id}')
            msg = f'[City] ({obj.id}) {obj.__dict__}'
            self.assertEqual(f.getvalue().strip(), msg)

    def test_Console_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = City()
            HBNBCommand().onecmd(f'update City {obj.id} name "Sameh"')
            self.assertIn('name', obj.__dict__.keys())
            self.assertEqual(obj.__dict__['name'], 'Sameh')

    def test_Console_update_multiple(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = City()
            HBNBCommand().onecmd(f'update City {obj.id} name "Sameh" age 28')
            self.assertNotIn('age', obj.__dict__.keys())


class TestConsole_place(unittest.TestCase):
    """UnitTest for Console_Place Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_Console_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place')
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn(f'Place.{f.getvalue().strip()}',
                          storage.all().keys())

    def test_Console_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj1 = Place()
            obj2 = Place()
            HBNBCommand().onecmd('all Place')
            for ele in json.loads(f.getvalue()):
                self.assertEqual(ele.split(' ')[0], '[Place]')

    def test_Console_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = Place()
            HBNBCommand().onecmd(f'show Place {obj.id}')
            msg = f'[Place] ({obj.id}) {obj.__dict__}'
            self.assertEqual(f.getvalue().strip(), msg)

    def test_Console_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = Place()
            HBNBCommand().onecmd(f'update Place {obj.id} name "Sameh"')
            self.assertIn('name', obj.__dict__.keys())
            self.assertEqual(obj.__dict__['name'], 'Sameh')

    def test_Console_update_multiple(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = Place()
            HBNBCommand().onecmd(f'update Place {obj.id} name "Sameh" age 28')
            self.assertNotIn('age', obj.__dict__.keys())


class TestConsole_amenity(unittest.TestCase):
    """UnitTest for Console_Amenity Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_Console_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Amenity')
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn(f'Amenity.{f.getvalue().strip()}',
                          storage.all().keys())

    def test_Console_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj1 = Amenity()
            obj2 = Amenity()
            HBNBCommand().onecmd('all Amenity')
            for ele in json.loads(f.getvalue()):
                self.assertEqual(ele.split(' ')[0], '[Amenity]')

    def test_Console_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = Amenity()
            HBNBCommand().onecmd(f'show Amenity {obj.id}')
            msg = f'[Amenity] ({obj.id}) {obj.__dict__}'
            self.assertEqual(f.getvalue().strip(), msg)

    def test_Console_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = Amenity()
            HBNBCommand().onecmd(f'update Amenity {obj.id} name "Sameh"')
            self.assertIn('name', obj.__dict__.keys())
            self.assertEqual(obj.__dict__['name'], 'Sameh')

    def test_Console_update_multiple(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = Amenity()
            cmd_line = f'update Amenity {obj.id} name "Sameh" age 28'
            HBNBCommand().onecmd(cmd_line)
            self.assertNotIn('age', obj.__dict__.keys())


class TestConsole_user(unittest.TestCase):
    """UnitTest for Console_User Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_Console_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn(f'User.{f.getvalue().strip()}',
                          storage.all().keys())

    def test_Console_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj1 = User()
            obj2 = User()
            HBNBCommand().onecmd('all User')
            for ele in json.loads(f.getvalue()):
                self.assertEqual(ele.split(' ')[0], '[User]')

    def test_Console_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = User()
            HBNBCommand().onecmd(f'show User {obj.id}')
            msg = f'[User] ({obj.id}) {obj.__dict__}'
            self.assertEqual(f.getvalue().strip(), msg)

    def test_Console_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = User()
            HBNBCommand().onecmd(f'update User {obj.id} name "Sameh"')
            self.assertIn('name', obj.__dict__.keys())
            self.assertEqual(obj.__dict__['name'], 'Sameh')

    def test_Console_update_multiple(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = User()
            HBNBCommand().onecmd(f'update User {obj.id} name "Sameh" age 28')
            self.assertNotIn('age', obj.__dict__.keys())


class TestConsole_review(unittest.TestCase):
    """UnitTest for Console_Review Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_Console_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Review')
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn(f'Review.{f.getvalue().strip()}',
                          storage.all().keys())

    def test_Console_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj1 = Review()
            obj2 = Review()
            HBNBCommand().onecmd('all Review')
            for ele in json.loads(f.getvalue()):
                self.assertEqual(ele.split(' ')[0], '[Review]')

    def test_Console_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = Review()
            HBNBCommand().onecmd(f'show Review {obj.id}')
            msg = f'[Review] ({obj.id}) {obj.__dict__}'
            self.assertEqual(f.getvalue().strip(), msg)

    def test_Console_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = Review()
            HBNBCommand().onecmd(f'update Review {obj.id} name "Sameh"')
            self.assertIn('name', obj.__dict__.keys())
            self.assertEqual(obj.__dict__['name'], 'Sameh')

    def test_Console_update_multiple(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = Review()
            HBNBCommand().onecmd(f'update Review {obj.id} name "Sameh" age 28')
            self.assertNotIn('age', obj.__dict__.keys())


if __name__ == "__main__":
    unittest.main()
