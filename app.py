import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
#  This is followed by creating a header text for the app:
st.header('st.button')


# Next, we will use conditional statements if and else for printing alternative messages.
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')


# Create a reset button to reset the displayed message
if st.button('Reset'):
    # Reset the displayed message when the reset button is clicked
    st.text('reset')


st.header('Sumeet')

st.write('Hello, *World!* :sunglasses:')

st.write(1234)

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
# st.write(df)

st.write('below is the data',df,'this is after')


# In addition to st.write, you can explore the other ways of displaying text:

st.markdown('Sumeet')
st.header('Vikas')
st.subheader('Kunal')
st.caption('Anurag')
st.text('Shantanu')
st.latex('sam')
st.code('kshitij')