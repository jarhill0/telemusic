from .bot import run


def main():
    from sys import argv

    from .helpers import set_listener_name, set_key, set_listener_id

    USAGE = """\nUsage:
    telemusic:      view this help message
    telemusic run:  run the bot
    telemusic set:  set values (value names and values required)

Known values:
    key:    telegram API key of the bot
    id:     telegram ID of the listener, determined with /id
    name:   human name of the listener
    """

    cmds = argv[1:]
    if len(cmds) == 0:
        print(USAGE)
    elif cmds[0] == 'run':
        print('Running bot.')
        run()
        return 0
    elif cmds[0] == 'set':
        if len(cmds) < 3:
            print('At least one pair of name and value must be provided.')
            return 1
        if len(cmds) % 2 != 1:
            print('Each name must have a corresponding value')
            return 1

        pairs = cmds[1:]
        for i in range(0, len(pairs), 2):
            name = pairs[i].lower()
            value = pairs[i + 1]

            if name == 'name':
                set_listener_name(value)
            elif name == 'id':
                set_listener_id(value)
            elif name == 'key':
                set_key(value)
            else:
                print('Unknown value name {!r}.'.format(name))

        return 0
