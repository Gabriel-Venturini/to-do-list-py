import streamlit as st
import my_functions as file_editor

todos = file_editor.get_todos()

st.title('To-Do App')
st.write('Did you finish something today?')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='You can add something here! :)', placeholder='Buy some milk')
