import streamlit as st

from dotenv import load_dotenv

load_dotenv()
import os

st.set_page_config(page_title="👩‍🏫Academic helper")
st.title("👩‍🏫Academic helper")

google_api_key = st.sidebar.text_input("Google GenAI API Key")


def generate_response(topic):
    os.environ["GOOGLE_API_KEY"] = google_api_key
    from agent import graph

    st.markdown(graph.invoke({"topic": topic})["review"])


with st.form("my_form"):
    topic = st.text_area(
        "Enter topic(you would need to wait for 2 minutes to get the response):",
        "What is a topic you want to research?",
    )
    submitted = st.form_submit_button("Submit")
    if not google_api_key:
        st.warning("Please enter your Google GenAI API key!", icon="⚠")
    if submitted and google_api_key:
        generate_response(topic)
