import streamlit as st
from grammar_api import correct_text
from utils import clean_text, format_output, is_valid_text, synonymize

def main():
    st.title("AI to Human Content Converter")
    st.write("Convert AI-written content into human-like text using LanguageTool API and synonymization.")

    # Use session_state to store input and output
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
    if "output_text" not in st.session_state:
        st.session_state.output_text = ""

    # Text area with value from session_state
    st.session_state.user_input = st.text_area(
        "Enter AI-written content here:",
        value=st.session_state.user_input,
        key="user_input_area"
    )

    col1, col2 = st.columns(2)
    with col1:
        convert_clicked = st.button("Convert")
    with col2:
        clear_clicked = st.button("Clear")

    if convert_clicked:
        if is_valid_text(st.session_state.user_input):
            cleaned = clean_text(st.session_state.user_input)
            human_text = correct_text(cleaned)
            human_text = synonymize(human_text)
            formatted = format_output(human_text)
            st.session_state.output_text = formatted
        else:
            st.error("Please enter some text to convert.")
            st.session_state.output_text = ""

    if clear_clicked:
        st.session_state.user_input = ""
        st.session_state.output_text = ""
        st.rerun()

    if st.session_state.output_text:
        st.subheader("Converted Human-like Text:")
        st.code(
            st.session_state.output_text,
            language="text"
        )

if __name__ == "__main__":
    main()