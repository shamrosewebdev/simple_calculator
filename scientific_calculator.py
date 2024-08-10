import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input boxes for numbers
num1 = st.number_input("Enter first number", format="%f")
num2 = st.number_input("Enter second number", format="%f")

# Variable to store the result
result = None

# Buttons for operations
if st.button("Add"):
    result = num1 + num2

if st.button("Subtract"):
    result = num1 - num2

if st.button("Multiply"):
    result = num1 * num2

if st.button("Divide"):
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Division by zero is not allowed.")

# Display the result
if result is not None:
    st.write(f"Result: {result}")
