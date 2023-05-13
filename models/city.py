#!/usr/bin/python3
""" module for City class """
from models.base_model import BaseModel


class City(BaseModel):
    """
    initiation of City that inherits from BaseModel class

    Public Class Attributes:
       (string) state_id: initialized as empty string
       (string) name: initialized as empty string
    """
    state_id = ""
    name = ""
