import streamlit as st
import time

# Streamlit app
def main():
    st.title("Countdown Timer")

    # Dropdown menu to select countdown duration
    countdown_duration = st.selectbox("Select countdown duration (minutes):", list(range(1, 11)))

    # Start button to initiate countdown
    if st.button("Start"):
        st.write("Countdown started!")
        countdown(countdown_duration * 60)

# Function to perform the countdown
def countdown(duration):
    countdown_text = st.empty()
    while duration:
        mins, secs = divmod(duration, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        countdown_text.text("Time left: " + timeformat)
        time.sleep(1)
        duration -= 1
    st.write("Time's up!")

if __name__ == "__main__":
    main()
