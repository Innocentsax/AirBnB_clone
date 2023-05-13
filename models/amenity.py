#!/usr/bin/python3
""" module for Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    initiation of Amenity that inherits from BaseModel class

    Public Class Attributes:
       (string) name: initialized as empty string
    """
    name = ""
