import streamlit as st
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# def request_home(server_url: str, genre: str, num:int):
#     r = requests.post(
#         server_url, ???, headers=???, timeout=8000
#     )

#     return r

def change_music_page():
    if 'search' in st.session_state:
        del st.session_state['search']
    st.session_state['book'] = ""

def change_search_page():
    st.session_state['search'] = ""




def search_box():
    '''
    검색창 생성
    output : 검색어
    '''
    st.title('kokoapage')
    st.header('책과 음악을 연결하다.')
    search_book = st.text_input('어떤 책을 찾으시는 건가요?', on_change=change_search_page)
    # if search_book:
    #     st.session_state['search'] = search_book
        
    return search_book

def list_main(num:int=3, genre:str='none'):
    '''
    main page 장르별 도서 큐레이팅 column 생성
    input : 도서 개수, 장르
    output : column
    '''
    st.header(genre)

    a = st.columns(num)

    for i in range(num):
        globals()['{}_col{}'.format(genre, i)] = a[i]

    for i in range(num):
        with globals()['{}_col{}'.format(genre, i)]:
            st.subheader("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")
            globals()['{}_col{}_button'.format(genre, i)] = st.button('{}_이 책 보기{}'.format(genre, i))
    
    for i in range(num):
        if globals()['{}_col{}_button'.format(genre, i)]:
            if 'search' in st.session_state:
                del st.session_state['search']
            st.session_state['book'] = i

    return

def list_search(num: int):
    for i in range(num):
        a = st.columns(2)

        for j in range(2):
            globals()['{}_col{}'.format(i, j)] = a[j]
            with globals()['{}_col{}'.format(i, j)]:
                if j == 0:
                    st.image("https://static.streamlit.io/examples/cat.jpg")
                else:
                    st.subheader('book{}'.format(i))
                    st.text('작가')
                    st.text('책소개')
                    globals()['{}_col_{}_button'.format(i, j)] = st.button('{}_노래추천_{}'.format(i, j), on_click=change_music_page)
    # for i in range(num):
    #     if globals()['{}_col_{}_button'.format(i, 1)]:
    #         del st.session_state['search']
    #         st.session_state['book'] = "2"
            
        
    return




def check_and_create_index(es, index:str):
    # define data model
    mappings = {
        'mapping': {
            'properties': {
                'author': {'type': 'keyword'},
                'title': {'type': 'text'},
                'tags': {'type': 'keyword'},
            }
        }
    }

    if not es.indices.exists(index):
        es.indices.create(index=index, body=mappings, ignore=400)

def index_search(es, index: str, keywords: str, filters: str, from_i: int, size: int) -> dict:
    """
    Args:
        es: Elasticsearch client instance.
        index: Name of the index we are going to use.
        keywords: Search keywords.
        filters: Tag name to filter medium stories.
        from_i: Start index of the results for pagination.
        size: Number of results returned in each search.
    """
    # search query
    body = {
        'query': {
            'bool': {
                'must': [
                    {
                        'query_string': {
                            'query': keywords,
                            'fields': ['context'],
                            'default_operator': 'AND',
                        }
                    }
                ],
            }
        },
        'highlight': {
            'pre_tags': ['<b>'],
            'post_tags': ['</b>'],
            'fields': {'context': {}}
        },
        'from': from_i,
        'size': size,
        'aggs': {
            'tags': {
                'terms': {'field': 'tags'}
            },
            'match_count': {'value_count': {'field': '_id'}}
        }
    }

    if filters is not None:
        body['query']['bool']['filter'] = {
            'term': {
                'tags': [filters]
            }
        }

    res = es.search(index=index, body=body)
    # sort popular tags
    sorted_tags = res['aggregations']['tags']['buckets']
    sorted_tags = sorted(
        sorted_tags,
        key = lambda t: t['doc_count'], reverse=True
    )
    res['sorted_tags']= [t['key'] for t in sorted_tags]
    return res