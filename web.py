import streamlit as st
import my_functions as file_editor

todos = file_editor.get_todos()

def add_todo():
    ''' Gets the key of input box using session_state
    then append the value to the list and updates it
    for the user'''
    todo = st.session_state['new_todo']
    if len(todo) > 1:
        # avoids the user inputing an empty item
        todos.append(todo.title() + '\n')
        file_editor.write_todos(todos)


st.title('To-Do App')
st.write('Did you finish something today?')

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox: # if item == True then remove the item
        todos.remove(todo)
        file_editor.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun() # rerun the listbox

new_todo = st.text_input(label='', placeholder='Add a new to-do...',
on_change=add_todo, key='new_todo')

st.session_state # print log