# This creates the page for displaying data visualizations.

import streamlit as st
import json
import pandas as pd
import plotly.express as px
from pathlib import Path

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json
json_path = Path(__file__).resolve().parent.parent / "data.json"

with open(json_path, "r") as file:
    music_data = json.load(file)

songs = pd.DataFrame(music_data["data_points"])



st.header("Average Song Duration by Artist")

averages = songs.groupby("artist", as_index=False)["duration"].mean()

fig1 = px.bar(
    averages,
    x="artist",
    y="duration",
    title="Average Song Duration by Artist",
    labels={
        "artist": "Artist",
        "duration": "Average Duration (seconds)"
    },
    color="artist"
)

st.plotly_chart(fig1, use_container_width=True)


st.header("Explore Songs by Artist")

artists = songs["artist"].unique().tolist()

if "selected_artist" not in st.session_state:
    st.session_state.selected_artist = artists[0]

selected_artist = st.selectbox(
    "Choose an artist:",
    artists,
    key="selected_artist"
)

filtered_songs = songs[songs["artist"] == selected_artist]

fig2 = px.scatter(
    filtered_songs,
    x="year",
    y="duration",
    hover_name="song",
    hover_data=["duration","year"],
    title=f"Song Durations and Release Years: {selected_artist}",
    labels={
        "year": "Release Year",
        "duration": "Song Duration (seconds)"
    }
)

fig2.update_traces(marker_size=12)
fig2.update_xaxes(dtick=1, tickformat="d")

st.plotly_chart(fig2, use_container_width=True)


# PART 2: GRAPHS FROM data.csv
st.header("Music Survey Results")

survey_data = pd.read_csv("data.csv")

st.subheader("Favorite Music Genres")

genre_counts = survey_data["Category"].value_counts()

st.bar_chart(genre_counts)




st.subheader("Daily Music Listening Hours")

# Create a session state to remember the slider value
if "max_hours" not in st.session_state:
    st.session_state.max_hours = 24

# Create an interactive slider
max_hours = st.slider(
    "Show people who listen to music up to how many hours per day?",
    min_value=0,
    max_value=24,
    key="max_hours"
)

# Convert the hours column into numbers
survey_data["Value"] = pd.to_numeric(survey_data["Value"], errors="coerce")

# Filter the data based on the slider
filtered_data = survey_data[survey_data["Value"] <= max_hours]

# Create the scatter plot
fig3 = px.scatter(
    filtered_data,
    x="Category",
    y="Value",
    color="Category",
    title="Daily Music Listening Hours by Genre",
    labels={
        "Category": "Favorite Music Genre",
        "Value": "Hours Listening Per Day"
    }
)

# Display the graph
st.plotly_chart(fig3, use_container_width=True)

