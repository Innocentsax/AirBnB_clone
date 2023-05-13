#!/usr/bin/python3
""" module for Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    initiation of Review that inherits from BaseModel class

    Public Class Attributes:
       (string) place_id: initalized as empty string
       (string) user_id: initalized as empty string
       (string) text: initalized as empty string
    """
    place_id = ""
    user_id = ""
    text = ""
