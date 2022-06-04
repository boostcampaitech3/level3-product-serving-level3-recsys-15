import sqlite3

class BookMusicRecDB:

    def __init__(self, file_path:str):
        self.con = sqlite3.connect(file_path,check_same_thread=False)

    def exit_db(self):
        self.con.close()

    def get_book_by_title(self, title):
        db_query = f'SELECT book_id, name, writer, images, intro FROM book WHERE name LIKE \'%{title}%\''
        cur = self.con.execute(db_query)
        return cur.fetchall()

    def get_rec_item_by_book_id(self,book_id):
        db_query = f'SELECT book_id, song_id FROM recommendation WHERE book_id={book_id}'
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