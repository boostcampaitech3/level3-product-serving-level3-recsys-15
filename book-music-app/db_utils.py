# 할 일
# 0. 칼럼 정리 -> 통일성을 맞출 필요가 있다
# 1. 존재하지 않는 title 또는 column일 경우 data 처리하기

import sqlite3

class BookMusicRecDB:

    def __init__(self, file_path):
        # 왜 같은 Thread이면 안될까? -> 비정상적으로 끊겼을 때 DB를 보호하기 위해서겠지?
        self.con = sqlite3.connect(file_path,check_same_thread=False)

    def exit_db(self):
        self.con.close()

    def get_book_by_title(self, title):
        db_query = f'SELECT book_id, name, writer, images, intro FROM book WHERE name LIKE \'%{title}%\''
        cur = self.con.execute(db_query)
        return cur.fetchall()

    def get_rec_item_by_book_id(self,book_id):
        db_query = f'SELECT book_id, top_10 FROM recommendation_title WHERE book_id={book_id}'
        cur = self.con.execute(db_query)
        return cur.fetchall()

    def get_music_by_id(self,ids):
        db_query = f'SELECT song_id, song_title, artist, youtube_url FROM song WHERE song_id in {tuple(ids)}'
        cur = self.con.execute(db_query)
        return cur.fetchall()

    def get_music_by_title(self, title):
        db_query = f'SELECT song_id, song_title, artist, youtube_url FROM song WHERE song_title LIKE \'%{title}%\''
        cur = self.con.execute(db_query)
        return cur.fetchall()

    def get_book_by_genre(self, genre):
        db_query = f'SELECT book_id, name, writer, images, intro FROM book WHERE last_genre LIKE \'%{genre}%\''
        cur = self.con.execute(db_query)
        return cur.fetchall()