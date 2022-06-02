import streamlit as st
from apps.streamlit_timeline import timeline
from apps import utils

def app():

    SERVER_URL = "http://0.0.0.0:30002/recommendation"
    # use full page width
    st.set_page_config(page_title="Timeline Example", layout="wide")

    id = st.session_state['book']
    title = st.session_state['title_value']
    img = st.session_state['img_url']
    author = st.session_state['author_value']


    # load data
    data = utils.rec_music(id, SERVER_URL, title, img, author)

    # render timeline
    timeline(data, height=800)

    st.button('다른 책', on_click=utils.delete_all_session)
    

    st.text(st.session_state)