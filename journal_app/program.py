def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------------------')
    print('        JOURNAL APP')
    print('-----------------------------')


def run_event_loop():
    print('Welcome to the journal app')
    cmd = None

    while cmd != 'x':
        cmd = input('What do you want to do? [L]ist, [A]dd, E[x]it: ')

        if cmd.lower().strip() == 'l':
            list_entries()
        elif cmd.lower().strip() == 'a':
            add_entries()
        elif cmd.lower().strip() != 'x':
            print(f'Sorry we don\'t understand {cmd}.')
    print('Done, goodbye...')


def list_entries():
    print('Listing...')


def add_entries():
    print('Adding....')


main()
