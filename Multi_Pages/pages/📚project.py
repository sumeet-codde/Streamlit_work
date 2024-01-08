import streamlit as st


if 'input' not in st.session_state:
    st.session_state['input']=None

st.title('Projects')

st.write('you entered the text is :',st.session_state['input'])