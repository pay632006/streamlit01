import streamlit as st
import pandas as pd
import random

def main():
    st.title("Spy Game Setup")

    # Selectbox for number of players
    num_players = st.selectbox("Select number of players:", list(range(3, 16)))

    # Selectbox for number of spies
    num_spies = st.selectbox("Select number of spies:", list(range(1, 6)))

    # Selectbox for category
    category = st.selectbox("Select category:", ["Object", "Animal", "Job", "City", "Country"])

    # Button to start the game
    if st.button("Start"):
        start_game(num_players, num_spies, category)

def start_game(num_players, num_spies, category):
    st.write(f"Starting game with {num_players} players, {num_spies} spies, and category {category}")
    st.write("To start the game go to the Roles page!")

    # Generate random spy indices
    spy_indices = random.sample(range(num_players), num_spies)

    # Create a list to hold the roles
    roles = ["Normal"] * num_players

    # Assign spy roles
    for index in spy_indices:
        roles[index] = "Spy"

    st.session_state.roles = roles
    st.session_state.category = category

    st.session_state.counter = 0
    df = pd.read_csv("Book1.csv", sep=";")

    filtered_data = df[df['cat'] == category]

    randomNum = random.sample(range(len(filtered_data)), 1)
    #st.write(randomNum)
    st.session_state.secret = (filtered_data.iloc[randomNum].iloc[0]['name'])



if __name__ == "__main__":
    main()
