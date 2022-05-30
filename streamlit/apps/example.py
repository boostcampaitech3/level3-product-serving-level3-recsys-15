# Streamlit Timeline Component Example

import streamlit as st
from apps.streamlit_timeline import timeline

def app():
    # use full page width
    st.set_page_config(page_title="Timeline Example", layout="wide")

    # load data
    with open('/opt/ml/final/level3-product-serving-level3-recsys-15/streamlit/apps/example.json', "r", encoding='UTF8') as f:
        data = f.read()

    # render timeline
    timeline(data, height=800)


    st.text(st.session_state)