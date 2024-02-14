import pandas as pd
import streamlit as st
import random

def app():
    """Implements the Streamlit app functionality."""

    # File upload section
    uploaded_file = st.file_uploader("Upload your CSV file:", type=".csv")

    if uploaded_file is not None:
        try:
            # Read the CSV file with correct separator and handle potential errors
            df = pd.read_csv(uploaded_file, sep=";")

            # Display the first row
            st.header("First Row:")
            filtered_data = df[df['cat'] == "Animal"]
            randomNum = random.sample(range(len(filtered_data)), 1)
            st.write(filtered_data.iloc[randomNum])



        except pd.errors.ParserError as e:
            st.error(f"Invalid file format. Make sure it's a valid CSV file separated by ';'. Error: {e}")
        except FileNotFoundError:
            st.error("No file uploaded. Please select a CSV file to proceed.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    app()
