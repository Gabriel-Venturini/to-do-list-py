import my_functions as file_editor
import PySimpleGUI as psg# 4.60.5

label = psg.Text("Type in a to-do")
input_box = psg.InputText(tooltip="Enter to-do", key="to-do")
add_button = psg.Button("Add")
exit_button = psg.Button("Exit")

window = psg.Window('To Do List',  
                    layout=[[label], [input_box, add_button], [exit_button]], 
                    font=('Helvetica', 15))

while True:
    event, value = window.read()
    match event:
        case 'Add':
            todos = file_editor.get_todos()
            new_todo = value["to-do"] + "\n"
            todos.append(new_todo.title())
            file_editor.write_todos(todos)
        case 'Exit':
            break
        case psg.WIN_CLOSED:
            break
window.close()
