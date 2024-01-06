import streamlit as st
import time 




# custom_css = """
#     body {
#         background-color: #1E1E1E;
#     }
# """

# # Apply custom CSS using st.markdown
# st.markdown(
#     f'<style>{custom_css}</style>',
#     unsafe_allow_html=True
# )

st.set_page_config(initial_sidebar_state="collapsed",
                   layout='wide',
    page_icon="🌙",page_title="Ex-stream-ly Cool App")

# st.title("Custom Configuration Example")

st.info('this is the form you need to submit ')


with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')
     st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

my_bar=st.progress(0)

for i in range(100):
  time.sleep(0.01)
  my_bar.progress(i+1)

st.header('Hello this is my 2nd project')

st.sidebar.header('Inputs here')

user_name=st.sidebar.text_input('what is your name')
user_age=st.sidebar.number_input('what is your age')
user_favourtie=st.sidebar.selectbox('which is your favourite game',['','football','cricket','baseball'])
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])

st.header('Output')

col1, col2, col3 ,col4= st.columns(4)

# with col1:
#     if user_name!='':
#         st.subheader(user_name)
#     else:
#        st.subheader('write your name')

# with col2:
#     if user_age!=0.0:
#         st.subheader(user_age)
#     else:
#        st.subheader('write your **age**!:sunglasses')



with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_age != '':
    st.write(f'{user_age} is your  **age**!')
  else:
    st.write('👈 Enter your **age**!')

with col3:
  if user_favourtie != '':
    st.write(f'🍴 **{user_favourtie}** is your favorite **sports**!')
  else:
    st.write('👈 Please choose your favorite **sports**!')

with col4:
  if user_emoji != '':
    st.write(f'🍴 **{user_emoji}** is your favorite **emoji**!')
  else:
    st.write('👈 Please choose your favorite **emoji**!')

submit_button=st.button('Submit')

if submit_button:
  st.write('you have submitted the form')


# st.write(user_age)
# st.write(user_favourtie)
# st.write(user_emoji)
