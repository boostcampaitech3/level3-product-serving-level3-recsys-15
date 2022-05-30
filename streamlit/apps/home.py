import streamlit as st
from apps import utils

def app():
    utils.search_box()
    st.title('Genres')
    utils.list_main(5, "코미디")
    utils.list_main(5, "로맨스")
    utils.list_main(5, "SF")
    

    st.text(st.session_state)
