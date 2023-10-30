def get_todos(file_path='to_do_list.txt'):
    '''' Read a text file and returns
    the list of to-do items.
    '''
    with open(file_path, 'r') as file_local:
            todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, file_path='to_do_list.txt'):
    '''' Receive an argument with the to-do items list
    and writes it in a text file.
    '''
    with open(file_path, 'w') as file_local:
            file_local.writelines(todos_local)


while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = get_todos()
        todos.append(todo.title())
        write_todos(todos_local=todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = f'{index + 1}-{item}'.strip('\n')
            print(item)

    elif user_action.startswith('edit'):
        try:
            todos = get_todos()
            number = int(user_action[5:])
            number -= 1
            new_todo = input('Enter new to-do: ')
            todos[number] = new_todo.title() + '\n'
            write_todos(todos_local=todos)
        except ValueError:
            print('Your command is not valid!')
            continue

    elif user_action.startswith('complete'):
        try:
            todos = get_todos()
            number = user_action[9:]
            index = int(number) - 1 # - 1 for the user input be correct with the syntax
            to_complete = todos[index]
            todos.pop(index)
            write_todos(todos_local=todos)
            print(f'{to_complete} was completed.')
        except IndexError:
            print('There is no item with that number!')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Command not found!')

print('Bye!')
