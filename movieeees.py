import streamlit as st
import pandas as pd

# Load the dataset
movie_data = pd.read_csv("movie_dataset.csv")

# Title of the app
st.title("Movie Recommendation Tool")

# Genre selection
genre = st.selectbox("Select a Genre", movie_data["Genre(s)"].unique())

# Mood input
mood = st.text_input("Enter mood keyword (e.g., happy, thrilling)")

# Button to get recommendations
if st.button("Get Recommendations"):
    if mood:  # Check if mood is provided
        recommendations = movie_data[
            (movie_data["Genre(s)"].str.strip().str.lower() == genre.lower()) &
            (movie_data["Mood"].str.contains(mood, case=False, na=False))
        ]

        if not recommendations.empty:
            st.write("### Recommended Movies:")
            st.table(recommendations[["Movie Title", "Genre(s)", "Mood", "Description"]])
        else:
            st.write("No matches found for that genre and mood combination.")
    else:
        st.write("Please enter a mood keyword.")
