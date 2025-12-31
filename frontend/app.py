import streamlit as st
from api_client import analyze_document

st.set_page_config(
    page_title="AI Document Analyzer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Document Analyzer")
st.markdown("Upload a document to extract insights using AI.")

uploaded_file = st.file_uploader(
    "Upload a document (PDF or image)",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:
    with st.spinner("Analyzing document..."):
        try:
            result = analyze_document(uploaded_file)

            st.success("Document processed successfully!")

            st.subheader("📄 File Information")
            st.write(f"**Filename:** {result['filename']}")
            st.write(f"**Blob URL:** {result['blob_url']}")

            st.subheader("🧠 AI Summary")
            st.write(result["summary"])

        except Exception as e:
            st.error(f"Error: {str(e)}")
