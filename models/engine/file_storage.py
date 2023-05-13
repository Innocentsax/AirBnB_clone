#!/usr/bin/python3
''' FileStorage module '''
import json
from models.base_model import BaseModel
import models
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''FileStorage class'''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
        Return:
        the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        sets in objects with key classname.id

        Args:
        object
        '''
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        '''
        serializes __objects to JSON file
        '''
        newdict = {}
        with open(self.__file_path, mode='w+', encoding='utf-8') as f:
            for k, v in self.__objects.items():
                newdict[k] = v.to_dict()
            json.dump(newdict, f)

    def reload(self):
        '''
        deserializes the JSON file
        '''
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                newobjects = json.load(f)
                for k, v in newobjects.items():
                    reloadedobj = eval('{}(**v)'.format(v['__class__']))
                    self.__objects[k] = reloadedobj

        except IOError:
            pass
