def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    return num1 / num2


import streamlit as st


st.title(' Tayyaba Calculator')

def perform_operation(num1, num2, operation):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
operation = st.selectbox("Select an operation", ('+', '-', '*', '/'))


if st.button('Calculate'):
    result = perform_operation(num1, num2, operation)
    st.write(f"Result: {result}")

st.write("Quit the calculator?")

col1, col2 = st.columns(2)
with col1:
    if st.button('Yes'):
        st.write("Goodbye!🤗")
        st.stop()
with col2:
    if st.button('No'):
        st.write("Let's calculate again!")
        st.empty()

