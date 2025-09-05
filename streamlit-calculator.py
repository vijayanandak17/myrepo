import streamlit as st

st.title("My Calculaotr")

a=st.number_input("Enter First number")
b=st.number_input("Enter Second number")

operation = st.selectbox("Choose the Operation", ["Add", "Subtract","Multiply","Divide"])

if st.button("Calculate"):
    if operation == "Add":
        c=a+b
    elif operation == "Subtract":
        c=a-b
    elif operation == "Multiply":
        c=a*b
    elif operation == "Divide":
        if b !=0:
            c=a/b
        else:
            st.error("Cannot Divide by Zero")
            c = None
    if c is not None:
        st.success(f"Answer: {c}")