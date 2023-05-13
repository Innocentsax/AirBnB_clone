#!/usr/bin/python3
import unittest
import pep8
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestAmenityDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Amenity.__doc__) > 0)


class TestAmenityPep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/amenity.py'
        file2 = 'tests/test_models/test_amenity.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestAmenity(unittest.TestCase):
    """ tests for class Amenity """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.amenity = Amenity()

    def test_subclass(self):
        """ test that amenity is a subclass of basemodel """
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_id(self):
        """ test id """
        self.assertEqual(str, type(self.amenity.id))

    def test_created_at(self):
        """ test created_at """
        self.assertEqual(datetime, type(self.amenity.created_at))

    def test_updated_at(self):
        """ test updated_at """
        self.assertEqual(datetime, type(self.amenity.updated_at))

    def test_name(self):
        """ test name """
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.amenity.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(self.amenity))

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
