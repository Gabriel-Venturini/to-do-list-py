import my_functions as file_editor

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = file_editor.get_todos()
        todos.append(todo.title())
        file_editor.write_todos(todos_local=todos)

    elif user_action.startswith('show'):
        todos = file_editor.get_todos()
        for index, item in enumerate(todos):
            item = f'{index + 1}-{item}'.strip('\n')
            print(item)

    elif user_action.startswith('edit'):
        try:
            todos = file_editor.get_todos()
            number = int(user_action[5:])
            number -= 1
            new_todo = input('Enter new to-do: ')
            todos[number] = new_todo.title() + '\n'
            file_editor.write_todos(todos_local=todos)
        except ValueError:
            print('Your command is not valid!')
            continue

    elif user_action.startswith('complete'):
        try:
            todos = file_editor.get_todos()
            number = user_action[9:]
            index = int(number) - 1 # - 1 for the user input be correct with the syntax
            to_complete = todos[index]
            todos.pop(index)
            file_editor.write_todos(todos_local=todos)
            print(f'{to_complete} was completed.')
        except IndexError:
            print('There is no item with that number!')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Command not found!')

print('Bye!')
