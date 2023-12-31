import my_functions as file_editor
import PySimpleGUI as psg# 4.60.5
import time

# psg.theme("DarkBlue") dark mode
# psg.theme("BlueMono") clear mode
psg.theme("DarkBlue")

# LABEL
label_clock = psg.Text("", key="clock")
label = psg.Text("Type in a to-do")

# BOXES
input_box = psg.InputText(tooltip="Enter to-do", key="to-do")
list_box = psg.Listbox(values=file_editor.get_todos(), key="items", 
                       enable_events=True, size=[45, 10])

# BUTTONS
add_button = psg.Button("Add", mouseover_colors="LightBlue2", size=[10,2])
exit_button = psg.Button("Exit", mouseover_colors="LightBlue2", size=[10,2])
edit_button = psg.Button("Edit", mouseover_colors="LightBlue2", size=[10,2])
complete_button = psg.Button("Complete", mouseover_colors="LightBlue2", size=[10,2])

# COLUMNS
col1 = psg.Column([[add_button], [edit_button], [complete_button]])
col2 = psg.Column([[input_box], [list_box], [exit_button]])

# WINDOW LAYOUT
layout =[[label_clock],
        [label], 
        [col2, col1]]

window = psg.Window('To Do List',  layout=layout, font=('Helvetica', 15))

# OPERATION
while True:
    event, value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%d/%m/%Y - %H:%M:%S"))
    match event:
        case 'Add':
            if value["to-do"] == "" or value["to-do"] == " ":
                psg.popup("Please select an item first!", font=("Helvetica", 15))
            else:
                todos = file_editor.get_todos()
                new_todo = value["to-do"] + "\n"
                todos.append(new_todo.title())
                file_editor.write_todos(todos)
                window["items"].update(values=todos)
                window["to-do"].update(value='')
        case 'Edit':
            try:
                todo_to_edit = value["items"][0]
                new_todo = value["to-do"]
                get_todos = file_editor.get_todos()
                get_index = get_todos.index(todo_to_edit)
                get_todos[get_index] = new_todo.title() + "\n"
                file_editor.write_todos(get_todos)
                window["items"].update(values=get_todos)
            except IndexError:
                psg.popup("Please select an item first!", font=("Helvetica", 15))
        case 'Complete':
            try:
                todo_to_complete = value["items"][0]
                todos = file_editor.get_todos()
                todos.remove(todo_to_complete)
                file_editor.write_todos(todos)
                window["items"].update(values=todos)
                window["to-do"].update(value='')
            except IndexError:
                psg.popup("Please select an item first!", font=("Helvetica", 15))
        case 'items':
            window["to-do"].update(value=value["items"][0])
        case 'Exit':
            break
        case psg.WIN_CLOSED:
            break
window.close()
