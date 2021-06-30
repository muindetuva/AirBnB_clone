#!/usr/bin/python3
"""
Contains comand line interpreter
"""
from models.base_model import BaseModel
from models.__init__ import storage
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = ["BaseModel"]

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
        args = arg.split()
        # Check if the class name has been passed and whether it exists
        try:
            obj = args[0]
            if obj not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
        except:
            print("** class name missing **")
            return

        try:
            id = args[1]
        except:
            print("** instance id missing **")
            return

        key = obj + "." + str(id)
        new_dict = storage.all()

        try:
            print(new_dict[key])
        except Exception as e:
            print("** no instance found **")

    def do_destroy(self, arg):
        '''
        Destroys an Object
        '''
        args = arg.split()
        # Check if the class name has been passed and whether it exists
        try:
            obj = args[0]
            if obj not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
        except:
            print("** class name missing **")
            return

        try:
            id = args[1]
        except:
            print("** instance id missing **")
            return

        key = obj + "." + str(id)
        stored_objs = storage.all()

        try:
            del(stored_objs[key])
            storage.save()
        except Exception as e:
            print("** no instance found **")

    def do_all(self, arg):
        '''
        Prints all string representation of all instances based or not on
        the class name.
        '''
        obj_dict = storage.all()
        obj_list = []
        if not arg:
            for obj in obj_dict.values():
                obj_list.append(str(obj))
            print(obj_list)
        else:
            if arg not in HBNBCommand.__classes:
                print("** class doesn't exis **")
            else:
                for k, obj in obj_dict.items():
                    if arg in k:
                        obj_list.append(str(obj))
                print(obj_list)

    def do_update(self, arg):
        args = arg.split()
        try:
            class_name = args[0]
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
        except:
            print("** class name missing **")
            return

        try:
            id = args[1]
            key = class_name + "." + str(id)
            if key not in storage.all():
                print("** no instance found **")
                return
        except:
            print("** instance id missing **")
            return

        try:
            attribute = args[2]
        except:
            print("** attribute name missing **")
            return

        try:
            value = args[3]
        except:
            print("** value missing **")
            return

        obj = storage.all()[key]
        print(obj)
        print("#" * 10)
        setattr(obj, attribute, str(value))
        print(obj)
    

        


    help_EOF = help_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()