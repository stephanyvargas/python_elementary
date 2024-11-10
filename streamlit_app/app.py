# streamlit_app/app.py

import streamlit as st
import json
import os

# File path for storing questionnaire answers
DATA_FILE = "student_answers.json"

# Function to save data to a JSON file
def save_answers(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# Function to load data from a JSON file
def load_answers():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Streamlit app layout
st.title("Python Elementary School Lessons")
st.sidebar.title("Lesson Navigation")
st.write("👋 Welcome to the interactive Python lessons!")

# Navigation for lesson pages
page = st.sidebar.selectbox("Select a lesson", ["Intro", "Make a Turtle", "Other"])

if page == "Intro":
    st.write("### Intro 📝")
    st.write("Please fill out this fun questionnaire!")

    # Load existing answers if they exist
    answers = load_answers()

    # Questionnaire inputs with emojis and preloaded answers if available
    name = st.text_input("1. 🤔 What is your name?", value=answers.get("name", ""))
    age = st.number_input("2. 🎂 How old are you?", min_value=1, max_value=100, step=1, value=answers.get("age", 10))
    favorite_animal = st.text_input("3. 🐾 What is your favorite animal?", value=answers.get("favorite_animal", ""))
    favorite_color = st.color_picker("4. 🎨 Pick your favorite color:", value=answers.get("favorite_color", "#000000"))
    likes_programming = st.text_area("5. 💻 What do you like about programming?", value=answers.get("likes_programming", ""))
    favorite_game = st.text_input("6. 🎮 What is your favorite game?", value=answers.get("favorite_game", ""))
    hobby = st.text_input("7. 🎨 What is your favorite hobby?", value=answers.get("hobby", ""))
    dream_job = st.text_input("8. 🌟 What job would you like to have when you grow up?", value=answers.get("dream_job", ""))
    favorite_food = st.text_input("9. 🍕 What is your favorite food?", value=answers.get("favorite_food", ""))
    favorite_subject = st.text_input("10. 📚 What is your favorite subject in school?", value=answers.get("favorite_subject", ""))

    # Store answers in a dictionary
    new_answers = {
        "name": name,
        "age": age,
        "favorite_animal": favorite_animal,
        "favorite_color": favorite_color,
        "likes_programming": likes_programming,
        "favorite_game": favorite_game,
        "hobby": hobby,
        "dream_job": dream_job,
        "favorite_food": favorite_food,
        "favorite_subject": favorite_subject
    }

    # Display the submitted answers and save them to a file
    if st.button("Submit"):
        save_answers(new_answers)
        st.write("Thank you for sharing! Here’s what we learned about you:")
        for key, value in new_answers.items():
            st.write(f"**{key.replace('_', ' ').capitalize()}:** {value}")
        st.write("🎉 Great job completing the questionnaire!")

elif page == "Make a Turtle":
    st.write("### Make a Turtle 🐢")
    # Add content or load from streamlit_pages
elif page == "Other":
    st.write("### Other 🎲")
    # Add content or load from streamlit_pages
else:
    st.write("Choose a lesson from the sidebar to get started!")

