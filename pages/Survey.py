# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Music Listening Survey 🎵")
st.write("Tell us about your music taste and listening habits!")

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    category_input = st.text_input("What is your favorite music genre?")
    value_input = st.text_input("How many hours do you listen to music each day?")

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        if category_input.strip() != "" and value_input.strip() != "":
            try:
                hours = float(value_input)

                if hours < 0 or hours > 24:
                    st.error("Please enter a number between 0 and 24.")
                else:
                    with open("data.csv", "a", newline="") as file:
                        file.write(f"{category_input.strip()},{hours}\n")

                    st.success("Your data has been submitted!")
                    st.write(f"You entered: **Genre** {category_input}, **Hours:** {hours}")

            except ValueError:
                st.error("Please enter a valid number for hours.")

        else:
            st.warning("Please answer both questions!")
            
# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
