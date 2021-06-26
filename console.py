#!/usr/bin/python3
"""
Contains comand line interpreter
"""

import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
            raise SystemExit

    def do_EOF(self, args):
        return True

    def help_quit(self):
        print("Quit command to exit the program")
        print()
    def emptyline(self):
        pass

    help_EOF = help_quit

if __name__== '__main__':
    HBNBCommand().cmdloop()
