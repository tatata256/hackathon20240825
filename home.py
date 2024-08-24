import streamlit as st
from streamlit_option_menu import option_menu
from page_home import main_home
from page_usage import main_usage
from page_generate import main_generate


# タブとページデフォルトの設定
st.set_page_config(
    page_title="なとサンチーム",
    page_icon="beginner",
    initial_sidebar_state="expanded"
)

# 水平バー
selected = option_menu(None, ["ホーム", "使い方", "音声生成"], 
    icons=['house', 'book', 'mic'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

# ホーム画面
if selected == "ホーム":
    main_home()

# 使い方の画面
elif selected == "使い方":
    main_usage()

# 音声生成の画面
elif selected == "音声生成":
    main_generate()

