import cmd

class HBNBCommand(cmd.Cmd):
    # prompt = "(hbnb)"

    def do_quit(self, args):
        """
        quits the console
        """
        return True

    def do_EOF(self, args):
        """
        EOF
        """
        return True

    def do_create(self, args):
        """
        Creates a new instance of BaseModel
        """
        pass

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        pass

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        Updates the json file
        """
        pass

    def do_all(self, ags):
        """
        Prints all string representation of all instances based or not on the class name
        """
        pass

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        Updates the json file
        """
        pass

console = HBNBCommand()

if __name__ == '__main__':
    HBNBCommand().cmdloop()