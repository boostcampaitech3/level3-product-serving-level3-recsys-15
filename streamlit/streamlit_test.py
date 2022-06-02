from selectors import EpollSelector
from jmespath import search
import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

data = pd.DataFrame()
data['book'] = ['book1', 'book2', 'book3']
data['music'] = ['music1', 'music2', 'music3']

st.title('kokoapage')
st.header('책과 음악을 연결하다.')
search_book = st.text_input('어떤 책을 찾으시는 건가요?')

# main page : 0
# 도서 검색 page : 1
# 음악 추천 page : 2
st.session_state['status'] = 0

if search_book and st.session_state['status'] == 1:
    st.session_state['status'] = 1
    st.session_state['search_book'] = search_book


def main():
    st.text('hello')

def select_book():
    if st.session_state['search_book'] in data['book'].to_list():
        a = st.button('book1')
        b = st.button('book2')
        c = st.button('book3')
    
    else:
        return st.text("해당 도서는 검색할 수 없습니다")

    
    if a:
        st.session_state['book'] = 'book1'
        st.session_state['status'] = 2
    elif b:
        st.session_state['book'] = 'book2'
        st.session_state['status'] = 2
    elif c:
        st.session_state['book'] = 'book3'
        st.session_state['status'] = 2

    return 0


def select_music():
    st.subheader("이 책을 찾으시는 건가요?")
    st.text(st.session_state['book'])
    return 0

if st.session_state['status'] == 0:
    main()


if st.session_state['status'] == 2:
    select_music()

if st.session_state['status'] == 1:
    select_book()



st.session_state