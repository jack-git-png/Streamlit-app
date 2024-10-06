import streamlit as st
from streamlit_option_menu import option_menu

navigation_bar = option_menu(
    menu_title=None,
    icons=("house-door","gear"),
    options=["Home","Documment"],
    default_index=1,
    orientation="horizontal")
