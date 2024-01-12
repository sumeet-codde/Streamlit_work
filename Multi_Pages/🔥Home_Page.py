import streamlit as st
import toml

st.set_page_config('Multi_page_Application')



st.title('MultiPage_application')
config_data = toml.load("config.toml")

if 'input' not in st.session_state:
    st.session_state['input']=""

input=st.text_input('Enter the text',st.session_state['input'])
clicked=st.button('Submit')

if clicked:
    st.session_state['input']=input
    st.write('You entered the following  text:',input)
else:
    st.write("enter the text")