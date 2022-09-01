import cmd


class HBNBCommand(cmd.Cmd):
    """

    console class
    """

    prompt = "(hbnb)"


if __name__ == '__main__':
    cli = HBNBCommand()
    cli.cmdloop()
