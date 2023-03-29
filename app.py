import streamlit as st
from sections.task_1 import task_1
from sections.task_3 import task_3




# Define the Streamlit app
def main():

    st.title("Assignment 4")

    tab1, tab2, tab3 = st.tabs(["Task 1", "Task 3", "Owl"])

    with tab1:
        task_1()
    with tab2:
        task_3()

    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    
   

if __name__ == "__main__":
    main()
