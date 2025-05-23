import streamlit as st

import functions

st.title("TODO APP")
st.subheader("This is my todo app")

def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos=functions.get_todos()

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label=" ",placeholder=" Add new todo...",on_change=add_todo,key='new_todo')
print("Hello")
#st.session_state