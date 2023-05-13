#!/usr/bin/python3
"""Test suite for Review class in models.review"""
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        self.review = Review()
        self.attr_list = [
            "place_id",
            "user_id",
            "text"
        ]

    def test_review_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attrs_are_class_attrs(self):
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.review, attr))

    def test_class_attrs(self):
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.review, attr)), str)
            self.assertFalse(bool(getattr(self.review, attr)))
