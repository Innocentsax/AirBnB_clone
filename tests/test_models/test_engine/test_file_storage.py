#!/usr/bin/python3
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorageDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(FileStorage.__doc__) > 0)


class TestFileStoragePep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/file_storage.py'
        file2 = 'tests/test_models/test_engine/test_file_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestFileStorage(unittest.TestCase):
    """ tests for class FileStorage """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        storage = FileStorage()

    def test_all(self):
        """ test all method """
        pass

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
