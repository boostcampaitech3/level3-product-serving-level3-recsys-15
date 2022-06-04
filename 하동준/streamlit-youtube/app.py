import streamlit as st
import io
import os
import yaml
import pandas as pd
import numpy as np
from streamlit_player import st_player
# import SessionState
st.set_page_config(layout='wide')
st.title("Cocoapage")

# Embed a youtube video
# bookcsv = pd.read_csv('/opt/ml/finalproject/booksample1000emb.csv')
# songcsv = pd.read_csv('/opt/ml/finalproject/songemb.csv')
# sample = songcsv.sample(8)

urllist = []
urllist.append('https://youtu.be/R_CLhKdK0GQ')
urllist.append('https://youtu.be/MV9kclfajk8')
urllist.append('https://youtu.be/PqdAchjnlnA')
urllist.append('https://youtu.be/MgsAqBd1HOQ')
urllist.append('https://youtu.be/nZqwQCLYgjk')
url = urllist[-1]


last_page = len(urllist)-1
if 'page_number' not in st.session_state:
    st.session_state['page_number'] = 0

# session_state = SessionState.get(page_number = 0)
prev, mid ,nexts = st.columns([1, 10, 1])

if prev.button("prev"):
    # st.write("yes")
    if st.session_state.page_number - 1 < 0:
        st.session_state.page_number = last_page
        url = urllist[st.session_state.page_number]
        st.write(st.session_state.page_number)
    else:
        st.session_state.page_number -= 1
        url = urllist[st.session_state.page_number]
        st.write(st.session_state.page_number)



if nexts.button("next"):
    # st.write("yes")
    if st.session_state.page_number + 1 > last_page:
        st.session_state.page_number = 0
        url = urllist[st.session_state.page_number]
        st.write(st.session_state.page_number)
    else:
        st.session_state.page_number += 1
        url = urllist[st.session_state.page_number]
        st.write(st.session_state.page_number)

st_player(url)
# st.video(url)


# if next.button("Next"):

    # if session_state.page_number + 1 > last_page:
    #     session_state.page_number = 0
    # else:
    #     session_state.page_number += 1

# if prev.button("Previous"):
#     st.write('previously on')
    # if session_state.page_number - 1 < 0:
    #     session_state.page_number = last_page
    # else:
    #     session_state.page_number -= 1

# # Get start and end indices of the next page of the dataframe
# start_idx = session_state.page_number * N 
# end_idx = (1 + session_state.page_number) * N

# # Index into the sub dataframe
# sub_df = data.iloc[start_idx:end_idx]
# st.write(sub_df)
# url = 'https://youtu.be/MgsAqBd1HOQ?list=PLXou8-_JNU7_KM_5a4adMR_uqcrebFUrS'

# st.header("유튜브")
# st.video(url, format="video/mp4", start_time=0)
# st_player(url)
# st_player('https://youtu.be/x-k8gL_r__U')
# st.dataframe(bookcsv)


# searchquery = st.text_input("책 아이디를 검색하세요.")




# if(searchquery):
#     st.write(searchquery)
