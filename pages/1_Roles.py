import streamlit as st

K = len(st.session_state.roles)
# Streamlit app
def main():
    st.title("Show and Hide Secret")

    # Session state to keep track of visibility
    if 'show_secret' not in st.session_state:
        st.session_state.show_secret = False
    if 'counter' not in st.session_state:
        st.session_state.counter = 1

    # Logic to show or hide the secret
    if st.button("Show 1"):
        if st.session_state.counter < K:
            st.session_state.show_secret = True
            st.session_state.counter += 1
    if st.button("Hide 2"):
        st.session_state.show_secret = False

    # Display the secret if the show button is pressed
    if st.session_state.show_secret:
        if st.session_state.roles[st.session_state.counter-1] == "Normal":
            st.write(f"{st.session_state.secret}")
        else:
            st.write("Spy")
    elif st.session_state.counter >= K:
        st.write("Next")
        st.session_state.show_secret = False
    if  st.session_state.counter == 0:
        st.write(f"Player 1")
    elif st.session_state.counter <= K:
        st.write(f"Player {st.session_state.counter}")

if __name__ == "__main__":
    main()
