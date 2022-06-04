import streamlit as st
import requests
import os
import json
from collections import OrderedDict
from elasticsearch import Elasticsearch, helpers

def request_book(server_url: str, id: str):
    '''
    FastAPI request method
    '''
    r = requests.get(
        os.path.join(server_url, str(id)), timeout=8000
    )
    return r


def change_music_page(id_value, title_value, img_value, author_value):
    '''
    on_click method
    session_state에 선택한 도서 정보 저장
    '''
    if 'search' in st.session_state:
        del st.session_state['search']
    st.session_state['book'] = id_value
    st.session_state['img_url'] = img_value
    st.session_state['author_value'] = author_value
    st.session_state['title_value'] = title_value

def change_search_page():
    '''
    on_change method
    별도 저장하는 기능 없음
    '''
    st.session_state['search'] = ""

def delete_all_session():
    '''
    onclick method
    모든 session state 제거
    '''
    for key in st.session_state.keys():
        del st.session_state[key]

def make_music_json(r:list, book:str, img:str, author:str):
    '''
    노래 추천 json 파일 생성
    output : json파일
    '''
    musics = OrderedDict()
    book_component = OrderedDict()
    book_component['text'] = {'headline':book+'<br>', 'text':'<p>{}</p>'.format(author)}
    book_component['media'] = {'url': img}
    musics['title'] = book_component
    events = []
    for i in range(len(r)):
        music_component = OrderedDict()
        music_component['media'] = {'url': r[i]['url']}
        music_component['text'] = {'headline': "{}<br><br>{}".format(r[i]['artist'], r[i]['title']), 'text': " "}
        music_component['start_date'] = {'year': "{}".format(i)}
        events.append(music_component)
    musics['title'] = book_component
    musics['events'] = events

    return json.dumps(musics)
    
    

def search_box():
    '''
    검색창 생성
    output : 검색어
    '''
    st.title('kokoapage')
    st.header('책과 음악을 연결하다.')
    search_book = st.text_input('어떤 책을 찾으시는 건가요?', on_change=change_search_page)
    
    
    if search_book:
        st.session_state['search'] = search_book
        
    return search_book

def list_main(num:int=3, genre:str='none', server_url:str = "http://0.0.0.0:30002/book/genre"):
    '''
    main page 장르별 도서 큐레이팅 column 생성
    input : 도서 개수, 장르
    output : column
    '''
    r = request_book(server_url, genre)
    books_list = r.json()['books'][:num]

    length = num if len(books_list) >= num else len(books_list)

    st.header(genre)

    a = st.columns(length)
    b = st.columns(length)
    c = st.columns(length)

    for i in range(length):
        globals()['{}_col{}'.format(genre, i)] = a[i]
        globals()['{}_col_second{}'.format(genre, i)] = b[i]
        globals()['{}_col_third{}'.format(genre, i)] = c[i]

    for i in range(length):
        with globals()['{}_col{}'.format(genre, i)]:
            st.subheader(books_list[i]['title'])
        with globals()['{}_col_second{}'.format(genre, i)]:
            st.image(books_list[i]['img_url'],width=200)
            id_value = books_list[i]['id']
            title_value = books_list[i]['title']
            img_value = books_list[i]['img_url']
            author_value = books_list[i]['author']
        with globals()['{}_col_third{}'.format(genre, i)]:
            globals()['{}_col{}_button'.format(genre, i)] = st.button(label = '이 책 보기',key=id_value, on_click=change_music_page, args=(id_value, title_value, img_value, author_value))

    return

def list_search(search_input:list):
    num = len(search_input)
    if num == 0:
        return st.subheader("검색한 도서는 찾을 수 없습니다.")

    for i in range(num):
        a = st.columns(2)

        for j in range(2):
            globals()['{}_col{}'.format(i, j)] = a[j]
            with globals()['{}_col{}'.format(i, j)]:
                if j == 0:
                    st.image(search_input[i]['_source']['image'],width=200)
                else:
                    st.subheader(search_input[i]['_source']['title'])
                    st.text(search_input[i]['_source']['author'])
                    id_value = search_input[i]['_id']
                    title_value = search_input[i]['_source']['title']
                    img_value = search_input[i]['_source']['image']
                    author_value = search_input[i]['_source']['author']
                    globals()['{}_col_{}_button'.format(i, j)] = st.button(label = '       이 책 보기       ',key=id_value, on_click=change_music_page, args=(id_value, title_value, img_value, author_value))
         
    return

def rec_music(id:str, server_url:str, book:str, img:str, author:str):
    r = request_book(server_url, id)
    r = r.json()['musics']
    r_json = make_music_json(r, book, img, author)

    return r_json




# Elastic search
def search_by_elasticsearch(server_url:str, index:str, search_input:str):
    _ES_URL = server_url
    _ES_INDEX = index
    es_client = Elasticsearch(_ES_URL, timeout = 60*1)
    res = es_client.search(
    index=_ES_INDEX,
    body={'from':0, 'size':10,
        "query":
            {"match":
                {'title':{
                    "query":search_input,
                    "fuzziness": "AUTO"
                    }
                }
            }
        }
    )
    return res['hits']['hits']

