# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Music Dashboard",  # The title that appears in the browser tab
    page_icon="🎵",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("Welcome to My Music Dashboard! 🎵")

# INTRODUCTION
st.write(
    "Explore music trends and listening habits through interactive "
    "visualizations! This website was created for my CS 1301 Lab 2 "
    "project. It collects and displays music-related data from "
    "JSON and CSV files."
)

st.write("Use the sidebar on the left to explore the different pages.")

# HOW TO USE THE APP
st.header("How to Use This App")

st.subheader("🎤 Survey Page")
st.write(
    "Take a quick survey about your music preferences! "
    "Enter your favorite music genre and how many hours you "
    "spend listening to music each day. Your responses will "
    "be added to our CSV dataset."
)

st.subheader("📊 Visuals Page")
st.write(
    "Explore four different music visualizations! Compare average "
    "song durations across artists, explore songs by release year, "
    "see the most popular music genres, and use an interactive "
    "slider to explore daily music listening habits."
)

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
# st.image("images/welcome_image.png")
