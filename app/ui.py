# SAMPLE STREAMLIT UI
import streamlit as st # type: ignore
from app.controller import handle_user_input


def main_ui():
    st.title("Natural Language Interface to Neo4j")
    
    user_input = st.text_input("Ask something about your graph DB:")

    if st.button("Submit") and user_input:
        with st.spinner("Processing..."):
            response = handle_user_input(user_input)

        st.subheader("Generated Cypher Query:")
        st.code(response["cypher_query"], language="cypher")

        st.subheader("Raw Result:")
        st.json(response["result"])

        st.subheader("Explanation:")
        st.write(response["explanation"])

        # place for the result
        st.subheader("Model Answer")
        st.write(response["answer"])
