import streamlit as st
from multiapps import MultiApp
from apps import home, book, music

app = MultiApp()


app.add_app('home', home.app)
app.add_app('book', book.app)
app.add_app('music', music.app)

app.run()