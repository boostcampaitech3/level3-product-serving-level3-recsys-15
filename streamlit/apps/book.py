import streamlit as st
from apps import utils
import sys
from elasticsearch import Elasticsearch

def app():
    # elastic search parameter
    # PAGE_SIZE = 5
    # INDEX = "book_data"
    # DOMAIN = "0.0.0.0"
    # es = Elasticsearch(host=DOMAIN)

    # utils.search_box()
    # st.title('이 책을 찾으시는 건가요?')


    # if st.session_state['search']:
    #     results = utils.index_search(es, INDEX, st.session_state['search'], '', 0, PAGE_SIZE)
    utils.search_box()
    utils.list_search(5)

    st.text(st.session_state)