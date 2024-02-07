#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""
<<<<<<< HEAD
        self.assertEqual(len(models.storage.all()), 0)
        new_state = State(name="California")
        models.storage.new(new_state)
        models.storage.save()
        self.assertEqual(len(models.storage.all()), 1)
        new_user = User(email="testemail@hello.world", password="password")
        models.storage.new(new_user)
        models.storage.save()
        self.assertEqual(len(models.storage.all()), 2)
=======
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""
<<<<<<< HEAD
        current_count = len(models.storage.all())
        new_state = State(name="Neveda")
        models.storage.new(new_state)
        self.assertEqual(current_count + 1, len(models.storage.all()))
        models.storage.save()
=======
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
<<<<<<< HEAD
        current_count = len(models.storage.all())
        new_state = State(name="New York")
        models.storage.new(new_state)
        self.assertEqual(current_count + 1, len(models.storage.all()))
        models.storage.reload()
        self.assertEqual(current_count, len(models.storage.all()))
        new_state = State(name="New York")
        models.storage.new(new_state)
        models.storage.save()
        self.assertEqual(current_count + 1, len(models.storage.all()))
        models.storage.reload()
        self.assertEqual(current_count + 1, len(models.storage.all()))

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get(self):
        """Test that get properly retrieves objects"""
        new_state = State(name="California")
        models.storage.new(new_state)
        models.storage.save()
        state_id = new_state.id
        state_name = new_state.name
        get_state = models.storage.get(State, state_id)
        self.assertEqual(state_id, get_state.id)
        self.assertEqual(state_name, get_state.name)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count(self):
        """Test that count properly counts objects"""
        count_states = models.storage.count(State)
        new_state = State(name="New mexico")
        models.storage.new(new_state)
        models.storage.save()
        count_states2 = models.storage.count(State)
        self.assertEqual(count_states + 1, count_states2)
        count_all = models.storage.count()
        new_user = User(email="testemail@main.net", password="password")
        models.storage.new(new_user)
        models.storage.save()
        count_all2 = models.storage.count()
        self.assertEqual(count_all + 1, count_all2)
=======
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
