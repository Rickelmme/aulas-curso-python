from dataclasses import dataclass


def execute_command(command):
    if command == 'ls':
        print('$ listing files')
    elif command == 'cd':
        print('$ changing directory')
    else:
        print('$ command not implemented')


# execute_command('ls')


def execute_command(command):
    match command:
        case 'ls':
            print('$ listing files')
        case 'cd':
            print('$ changing directory')
        case _:  # Não obrigatório
            print('$ command not implemented')


# execute_command('pwd')

def execute_command(command):
    match command.split():
        case ['ls', *directories, '--force']:
            for directory in directories:
                print('$ listing files FORCED', directory)
        case ['ls', *directories]:
            for directory in directories:
                print('$ listing files ', directory)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:
            print('$ command not implemented')


# execute_command('ls /home /users /etc --force')
# execute_command('ls /home /users /etc')

def execute_command(command):
    match command.split():
        case ['ls' | 'list', *directories]:
            for directory in directories:
                print('$ listing files from', directory)
        case ['cd' | 'change', path]:
            print('$ changing directory to', path)
        case _:
            print('$ command not implemented')


# execute_command('ls /home /users /etc')
# execute_command('list /home /users /etc')

def execute_command(command):
    match command.split():
        case ['ls' | 'list', *directories] if len(directories) > 1:
            for directory in directories:
                print('$ listing ALL directories from', directory)
        case ['ls' | 'list', *directories] if len(directories) <= 1:
            print('$ listing ONE directory from', directories[0])
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:
            print('$ command not implemented')


# execute_command('ls /home /users /etc')
# execute_command('ls /home')

def execute_command(command):
    match command.split():
        case ['ls' | 'list' as the_command, *directories] as the_list \
                if len(directories) > 1:
            for directory in directories:
                print('$ listing ALL directories from', directory)
            print(f'{the_command=}, {the_list=}')
        case ['ls' | 'list', *directories] if len(directories) <= 1:
            print('$ listing ONE directory from', directories[0])
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:
            print('$ command not implemented')


# execute_command('ls /home /users /etc')
# execute_command('ls /home')

def execute_command(command):
    match command:
        case {'command': 'ls', 'directories': [_, *_]}:
            print('DEU MATCH')
            for directory in command['directories']:
                print('$ listing ALL directories from', directory)
        case _:
            print('$ command not implemented')


# execute_command({'command': 'ls', 'directories': ['/users', '/home']})

@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command(command: Command):
    match command:
        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ listing ALL directories from', directory)
        case Command(command=_, directories=[_, *_]):
            for directory in command.directories:
                print('$ changing to', directory)
        case _:
            print('$ command not implemented')


command_1 = Command('ls', ['/users'])
command_2 = Command('cd', ['/users'])
execute_command(command_1)
execute_command(command_2)
