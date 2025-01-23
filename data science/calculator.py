import streamlit as st

st.title('Calculator')
st.markdown("This is a simple calculator")

c1,c2 = st.columns(2)
fnum = c1.number_input("Enter first number",value = 0)
snum = c2.number_input("Enter second number",value = 0)

options = ["Addition","Subtraction","Multiplication","Division"]
choice = st.radio("Select Operation",options)# st.mutliselect dor multiple choice

button = st.button("Calculate")

if button:
    if choice == "Addition":
        result = fnum + snum
    if choice == "Subtraction":
        result = fnum - snum
    if choice == "Multiplication":
        result = fnum * snum
    if choice == "Division":
        result = fnum / snum

st.success(f"Result is {result}")# success show the green color , warning for yellow , red for danger