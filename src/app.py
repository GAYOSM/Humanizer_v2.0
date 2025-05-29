import streamlit as st
from grammar_api import correct_text
from utils import clean_text, format_output, is_valid_text, synonymize

def main():
    st.title("AI to Human Content Converter")
    st.write("Convert AI-written content into human-like text using LanguageTool API and synonymization.")

    user_input = st.text_area("Enter AI-written content here:")

    if st.button("Convert"):
        if is_valid_text(user_input):
            cleaned = clean_text(user_input)
            human_text = correct_text(cleaned)
            human_text = synonymize(human_text)
            formatted = format_output(human_text)
            st.subheader("Converted Human-like Text:")
            st.write(formatted)
            # Copy to clipboard button
            copy_code = f"""
            <button onclick="navigator.clipboard.writeText(`{formatted}`)">Copy to Clipboard</button>
            """
            st.markdown(copy_code, unsafe_allow_html=True)
        else:
            st.error("Please enter some text to convert.")

if __name__ == "__main__":
    main()