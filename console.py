#!/usr/bin/python3
''' console module '''
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    ''' HBNB class contains entry point '''

    prompt = '(hbnb) '
    myclasses = ["BaseModel", "User", "Place", "State", "Amenity", "Review",
                 "City"]

    def do_EOF(self, line):
        ''' exit the program '''
        return True

    def help_EOF(self):
        ''' help EOF'''
        print("EOF command to exit the program\n")

    def help_quit(self):
        ''' help quit '''
        print("Quit command to exit the program\n")

    def do_quit(self, arg):
        ''' quit interpreter '''
        return True

    def emptyline(self):
        ''' do nothing with empty line '''
        pass

    def do_create(self, classname):
        ''' create a new instance of '''
        if len(classname) == 0:
            print('** class name missing **')
        elif classname not in self.myclasses:
                print('** class doesn\'t exist **')
                return False
        else:
            new = eval("{}()".format(classname))
            new.save()
            print(new.id)

    def help_create(self):
        ''' help create '''
        print("Create command to create a class\n")

    def do_show(self, line):
        '''represents an instance'''
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return False
        elif args[0] not in self.myclasses:
            print('** class doesn\'t exist **')
            return False

        if len(args) < 2:
            print('** instance id missing **')
            return False

        all_objs = storage.all()
        for i in all_objs.keys():
            if i == "{}.{}".format(args[0], args[1]):
                print(all_objs[i])
                return False
        print('** no instance found **')

    def help_show(self):
        ''' help show '''
        print("Show command to display the string representation of class\n")

    def do_destroy(self, line):
        ''' deletes an instance based on the class id'''
        args = line.split()
        if len(line) == 0:
            print('** class name missing **')
            return False
        elif args[0] not in self.myclasses:
            print('** class doesn\'t exist **')
            return False
        elif len(args) < 2:
            print('** instance id missing **')
            return False
        else:
            all_objs = storage.all()
            for i in all_objs:
                if i == "{}.{}".format(args[0], args[1]):
                    all_objs.pop(i)
                    storage.save()
                    return False
            print('** no instance found **')

    def help_destroy(self):
        ''' help destroy '''
        print("Destroy command to destroy an object\n")

    def do_all(self, line):
        ''' prints all string representations of instances'''
        args = line.split()
        all_objs = storage.all()

        if len(args) == 0:
            for i in all_objs:
                strarg = str(all_objs[i])
                print(strarg)
        elif line not in self.myclasses:
            print('** class doesn\'t exist **')
            return False
        else:
            for i in all_objs:
                if i.startswith(args[0]):
                    strarg = str(all_objs[i])
                    print(strarg)
        return False

    def help_all(self):
        ''' help all'''
        print("All command to show all instances\n")

    def do_update(self, line):
        ''' updates an instance based on class name and id'''
        args = line.split()
        flag = 0

        if len(line) == 0:
            print('** class name missing **')
            return False

        try:
            clsname = line.split()[0]
            eval("{}()".format(clsname))
        except IndexError:
            print('** class doesn\'t exist **')
            return False

        try:
            instanceid = line.split()[1]
        except IndexError:
            print('** instance id missing **')
            return False

        all_objs = storage.all()
        try:
            clschange = all_objs["{}.{}".format(clsname, instanceid)]
        except IndexError:
            print('** no instance found **')
            return False

        try:
            attributename = line.split()[2]
        except IndexError:
            print('** attribute name missing **')
            return False

        try:
            updatevalue = line.split()[3]
        except IndexError:
            print('** value missing **')
            return False

        if updatevalue.isdecimal() is True:
            setattr(clschange, attributename, int(updatevalue))
            storage.save()
        else:
            try:
                setattr(clschange, attributename, float(updatevalue))
                storage.save()
            except:
                setattr(clschange, attributename, str(updatevalue))
                storage.save()

    def help_update(self):
        '''help update'''
        print("update command to update attributes\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
