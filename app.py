import streamlit as st
import random

# Initialize session state variables if they don't exist
if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Set page config
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎮",
    layout="centered"
)

# Title and instructions
st.title("🎮 Number Guessing Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# Game logic
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        
        if guess < st.session_state.target_number:
            st.error("Too low! Try a higher number.")
        elif guess > st.session_state.target_number:
            st.error("Too high! Try a lower number.")
        else:
            st.success(f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True
            
    st.write(f"Attempts: {st.session_state.attempts}")

# Reset button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.experimental_rerun() 