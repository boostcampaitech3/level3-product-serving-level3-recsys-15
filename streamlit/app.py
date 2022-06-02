import streamlit as st
from multiapps import MultiApp
from apps import home, book, example

app = MultiApp()


app.add_app('home', home.app)
app.add_app('book', book.app)
app.add_app('music', example.app)

app.run()