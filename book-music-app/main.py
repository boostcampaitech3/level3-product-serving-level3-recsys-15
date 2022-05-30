from .db_utils import BookMusicRecDB
from .data_utils import Music, MusicList,Book,BookList
from fastapi import FastAPI
from urllib import parse

################## main #####################

app = FastAPI()
DB_PATH = '' ########### TODO: DB가 저장된 주소를 넣어주세요 #########
DB = BookMusicRecDB(DB_PATH)


################## server function#####################

@app.get('/book/{book_title}')
def get_book_by_title(book_title:str):
    b_title = parse.unquote(book_title)
    result = DB.get_book_by_title(b_title)
    if len(result) == 0:
        return BookList()
    book_list = []
    for book_id, title, writer, img_url,intro in result:
        book = Book(id=book_id, 
                    title=title,
                    author=writer,
                    img_url=img_url,
                    intro=intro
                    )
        book_list.append(book)
    return BookList(books=book_list)

@app.get('/book/genre/{genre}')
def get_book_by_title(genre:str):
    b_genre = parse.unquote(genre)
    result = DB.get_book_by_genre(b_genre)
    if len(result) == 0:
        return BookList()
    book_list = []
    for book_id, title, writer, img_url,intro in result:
        book = Book(id=book_id, 
                    title=title,
                    author=writer,
                    img_url=img_url,
                    intro=intro
                    )
        book_list.append(book)
    return BookList(books=book_list)

@app.get('/music/{music_title}')
def get_music_by_title(music_title:str):
    m_title = parse.unquote(music_title)
    result = DB.get_music_by_title(m_title)
    if len(result) == 0:
        return MusicList()
    music_list = []
    for id, title, artist, youtube_url in result:
        music = Music(id=id, 
                    title=title,
                    artist=artist,
                    url=youtube_url
                    )
        music_list.append(music)
    return MusicList(musics=music_list)

@app.get('/recommendation/{book_id}')
def get_recommend_list_by_id(book_id:int):
    recommend_musics = DB.get_rec_item_by_book_id(book_id)
    if len(recommend_musics) == 0:
        return MusicList()
    
    song_ids = list(map(int,recommend_musics[0][1].split()))
    result = DB.get_music_by_id(song_ids)
    if len(result) == 0:
        return MusicList()

    music_list = []
    for id, title, artist,youtube_url in result:
        music = Music(id=id, 
                    title=title,
                    artist=artist,
                    url=youtube_url
                    )
        music_list.append(music)
    return MusicList(musics=music_list)

@app.on_event("shutdown")
def shutdown_event():
    global DB
    DB.exit_db()


@app.get("/")
def hello_world():
    return {"test"}