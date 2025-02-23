from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie

# emojis --> https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Venue ID", page_icon="images/icon.png", layout="wide")

# Load images
img_logo = Image.open("images/venueid_logo.png")
img_text = Image.open("images/venueid_text2.png")
img_slogan = Image.open("images/venueid_slogan.png")


# Header
with st.container():
    
    left_column, right_column = st.columns(2)
    # Logo
    with left_column:
        st.image(img_logo)
    # Title text
    with right_column:        
        st.write("##")
        st.write("##")
        st.image(img_text)
        st.image(img_slogan)

# Directories
with st.container():
    st.write("---")

    left, middle, right = st.columns(3)
    if left.button("Find a Venue", icon="🔍", use_container_width=True):
        st.switch_page("pages/page_1.py")  # Redirects to page_1
    if middle.button("About", icon="❓", use_container_width=True):
        st.switch_page("pages/page_2.py")  # Redirects to page_2
    if right.button("Future Expansion", icon="🌏", use_container_width=True):
        st.switch_page("pages/page_3.py")  # Redirects to page_3




