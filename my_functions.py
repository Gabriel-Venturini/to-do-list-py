FILEPATH = 'to_do_list.txt'

def get_todos(file_path=FILEPATH):
    '''' Read a text file and returns
    the list of to-do items.
    '''
    with open(file_path, 'r') as file_local:
            todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, file_path=FILEPATH):
    '''' Receive an argument with the to-do items list
    and writes it in a text file.
    '''
    with open(file_path, 'w') as file_local:
            file_local.writelines(todos_local)

