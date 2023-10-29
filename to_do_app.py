
while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:] + '\n'

        with open('to_do_list.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo.title())

        with open('to_do_list.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('to_do_list.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = f'{index + 1}-{item}'.strip('\n')
            print(item)

    elif 'edit' in user_action:
        with open('to_do_list.txt', 'r') as file:
            todos = file.readlines()

        number = int(user_action[5:])
        number -= 1

        new_todo = input('Enter new to-do: ')
        todos[number] = new_todo.title() + '\n'

        with open('to_do_list.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        with open('to_do_list.txt', 'r') as file:
            todos = file.readlines()

        number = user_action[9:]
        index = int(number)
        index -= 1

        to_complete = todos[index]
        todos.pop(index)

        with open('to_do_list.txt', 'w') as file:
            file.writelines(todos)

        print(f'{to_complete} was completed.')

    elif 'exit' in user_action:
        break

    else:
        print('Command not found!')

print('Bye!')
