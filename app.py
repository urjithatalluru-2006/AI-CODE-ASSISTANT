import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.set_page_config(
    page_title="AI Code Assistant",
    page_icon="💻",
    layout="wide"
)

st.title("💻 AI Code Assistant")
st.caption("Powered by Google Gemini")

with st.sidebar:

    st.header("Settings")

    model = st.selectbox(
        "Model",
        [
            "gemini-3.5-flash",
            "gemini-3.5-flash-lite",
            "gemini-3.1-flash-lite",
        ]
    )

    task = st.selectbox(
        "Task",
        [
            "Generate Code",
            "Explain Code",
            "Debug Code",
            "Optimize Code",
            "Add Comments",
            "Convert Language"
        ]
    )

language = st.selectbox(
    "Programming Language",
    [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "TypeScript",
        "Go",
        "Rust",
        "PHP"
    ]
)

prompt = st.text_area(
    "Enter your prompt or paste code",
    height=250
)

if st.button("🚀 Generate", use_container_width=True):

    if prompt.strip() == "":
        st.warning("Please enter something.")
        st.stop()

    instructions = {
        "Generate Code":
        f"Generate {language} code for:\n{prompt}",

        "Explain Code":
        f"Explain this {language} code:\n{prompt}",

        "Debug Code":
        f"Find bugs and fix this {language} code:\n{prompt}",

        "Optimize Code":
        f"Optimize this {language} code and improve performance:\n{prompt}",

        "Add Comments":
        f"Add comments to this {language} code:\n{prompt}",

        "Convert Language":
        f"Convert this code into {language}:\n{prompt}"
    }

    with st.spinner("Generating..."):

        try:

            response = client.models.generate_content(
                model=model,
                contents=instructions[task]
            )

            st.success("Done!")

            st.code(
                response.text,
                language=language.lower()
            )

            st.download_button(
                "📥 Download",
                response.text,
                file_name="generated_code.txt"
            )

        except Exception as e:

            st.error(e)