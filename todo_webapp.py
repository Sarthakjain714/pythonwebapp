import streamlit
import functions

todos=functions.get_todos()
def addtodo():
    newtodo=streamlit.session_state['new_todo']
    todos.append(newtodo+'\n')
    functions.write_todos(todos)

def completetodo():
    for index,todo in enumerate(todos):
        # print(streamlit.session_state[todo])
        if(streamlit.session_state[todo]==True):
            print(todo,index)

            todos.pop(index)
            functions.write_todos(todos)
            del streamlit.session_state[todo]


streamlit.title("TODO APP")
streamlit.write("Todos :")


for i in todos:
    streamlit.checkbox(i,key=i)

Complete=streamlit.button("Complete", on_click=completetodo)
streamlit.text_input(label="Add todo",placeholder="Enter todo text",key='new_todo',on_change=addtodo)
streamlit.session_state
