import streamlit as st

K = len(st.session_state.roles)
# Streamlit app
def main():
    st.title("Secret or Spy")

    # Session state to keep track of visibility
    if 'show_secret' not in st.session_state:
        st.session_state.show_secret = False

    if st.session_state.counter < K:
        text1 = (f"Player {st.session_state.counter+1}")
    else:
        text1 = ("Start the timer!")
    #st.write(f"{st.session_state.counter}")


    # Create two columns
    col1, col2 = st.columns(2)

    # Add dynamic text and buttons to each column
 

    with col2:
        text_container = st.text("********")  # Display dynamic text
        if st.button("2-- Hide"): 
            st.session_state.show_secret = False 
            text_container.text("********")  
    with col1:
        st.text(text1)  # Display dynamic text
        if st.button("1-- Show"):
            if st.session_state.counter < K:
                st.session_state.show_secret = True
                st.session_state.counter += 1
                if (st.session_state.counter != 0 and st.session_state.counter <= K)  or (st.session_state.show_secret == True):
                    if st.session_state.roles[st.session_state.counter-1] == "Normal":
                        text2 = (f"{st.session_state.secret}")

                    else:
                        text2 = ("Spy جاسوس بد جنس ")
                else:
                    text2 = ("********")
            else:
                text2 = ("********")
            text_container.text(text2)  

if __name__ == "__main__":
    main()
