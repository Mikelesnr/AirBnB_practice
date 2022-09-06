import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

classes = {'BaseModel': BaseModel, 'User': User,
           'Amenity': Amenity, 'City': City, 'State': State,
           'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, args):
        """
        quits the console
        """
        return True

    def do_EOF(self, args):
        """
        Inbuit end of line method that quits concole
        """
        return True

    def do_help(self, arg):
        """parses argument into superclass help function
        to get information about the argument
        """
        return super().do_help(arg)

    def do_create(self, arg):
        """
        Creates a new instance.
        """
        validate_classname = False
        args = arg.split()
        if not validate_classname(args):
            return

        new_obj = self.classes[args[0]]()
        new_obj.save()
        print(new_obj.id)


console = HBNBCommand()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
