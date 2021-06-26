#!/usr/bin/python3
"""
Contains comand line interpreter
"""
import inspect, sys
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.__init__ import storage
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    __classes =["BaseModel"]
    def do_quit(self, args):
            raise SystemExit

    def do_EOF(self, args):
        return True

    def help_quit(self):
        print("Quit command to exit the program")
        print()
    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name is missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class does not exist **")
        else:
            model_1 = BaseModel()
            model_1.save()
            print(model_1.id)

    def do_show(self, arg):
        arg_list = arg.split()
        if len(arg_list) >= 1:
            obj = arg_list[0]
        else:
            raise Exception("** Class name is missing **")
        if len(arg_list) >= 2:
            id = arg_list[1]
        else:
            raise Exception("** instance id missing **")

        if obj is None:
            print("** class name missing **")
        elif id is None:
            print("** instance id missing **")
        elif obj not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            key = obj + "." + str(id)
            new_dict = storage.all()
#            new_obj = FileStorage()
 #           new_dict = new_obj.all()
            try:
                  print(new_dict[key])
            except Exception as e:
                  print("** no instance found **")


    help_EOF = help_quit

if __name__== '__main__':
    HBNBCommand().cmdloop()
