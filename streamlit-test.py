import streamlit as st

st.title("My Streamlit Application")

name=st.text_input("Enter you Name")

if st.button("Say Hello"):
    if name:
        st.success(f"Hello {name}, Welcome to my Page")
    else:
        st.warning("Please enter your Name")
