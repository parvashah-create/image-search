import streamlit as st
from sections.task_1 import task_1
from sections.task_3 import task_3
from sections.task_2 import task_2




# Define the Streamlit app
def main():

    st.title("Assignment 4")

    tab1, tab2, tab3 = st.tabs(["Task 1", "Task 2", "Task 3"])

    with tab1:
        task_1()
    with tab2:
        task_2()

    with tab3:
        task_3()
    
   

if __name__ == "__main__":
    main()
