import streamlit as st
from apps import utils
import requests

def app():
    SERVER_URL = "http://0.0.0.0:30002/book/genre"
    

    utils.search_box()
    st.title('이 책은 어떠세요?')
    utils.list_main(3, "일본", SERVER_URL)
    utils.list_main(3, "프랑스", SERVER_URL)

    

    st.text(st.session_state)
