import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

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


console = HBNBCommand()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
