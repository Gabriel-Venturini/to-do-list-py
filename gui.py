import my_functions as file_editor
import PySimpleGUI as psg# 4.60.5

label = psg.Text("Type in a to-do")
input_box = psg.InputText(tooltip="Enter to-do", key="to-do")
list_box = psg.Listbox(values=file_editor.get_todos(), key="items", 
                       enable_events=True, size=[45, 10])

add_button = psg.Button("Add")
exit_button = psg.Button("Exit")
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete")

layout =[[label], 
         [input_box, add_button], 
         [list_box, edit_button, complete_button], 
         [exit_button]]

window = psg.Window('To Do List',  layout=layout, font=('Helvetica', 15))

while True:
    event, value = window.read()
    match event:
        case 'Add':
            todos = file_editor.get_todos()
            new_todo = value["to-do"] + "\n"
            todos.append(new_todo.title())
            file_editor.write_todos(todos)
            window["items"].update(values=todos)
        case 'Edit':
            todo_to_edit = value["items"][0]
            new_todo = value["to-do"]
            get_todos = file_editor.get_todos()
            get_index = get_todos.index(todo_to_edit)
            get_todos[get_index] = new_todo.title() + "\n"
            file_editor.write_todos(get_todos)
            window["items"].update(values=get_todos)
        case 'Complete':
            todo_to_complete = value["items"][0]
            todos = file_editor.get_todos()
            todos.remove(todo_to_complete)
            file_editor.write_todos(todos)
            window["items"].update(values=todos)
            window["to-do"].update(value='')
        case 'items':
            window["to-do"].update(value=value["items"][0])
        case 'Exit':
            break
        case psg.WIN_CLOSED:
            break
window.close()
