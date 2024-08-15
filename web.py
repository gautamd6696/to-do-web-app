import streamlit as st
import file_operations as fo
import os

if not os.path.exists("to_dos.txt"):
    with open("to_dos.txt", "w") as file:
        pass

to_do_list = fo.get_list()


def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    to_do_list.append(new_todo)
    fo.write(to_do_list)


st.title("To-Do Manager")
st.subheader("This app increases your productivity")

st.text_input(label="Enter a to-do below", on_change=add_todo, key="new_todo")

for i, to_do in enumerate(to_do_list):
    checkbox = st.checkbox(to_do, key=f"to_do.{i}")
    if checkbox:
        to_do_list.pop(i)
        fo.write(to_do_list)
        del st.session_state[f"to_do.{i}"]
        st.rerun()
