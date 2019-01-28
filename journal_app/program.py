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
    journal_data = []

    while cmd != 'x':
        cmd = input('What do you want to do? [L]ist, [A]dd, E[x]it: ')

        if cmd.lower().strip() == 'l':
            list_entries(journal_data)
        elif cmd.lower().strip() == 'a':
            add_entries(journal_data)
        elif cmd.lower().strip() != 'x':
            print(f'Sorry we don\'t understand {cmd}.')
    print('Done, goodbye...')


def list_entries(data):
    print('Your entries:')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print(f'# {idx+1}  {entry}')


def add_entries(data):
    text = input('Type your entry, <enter> to exit: ')
    data.append(text)


main()
