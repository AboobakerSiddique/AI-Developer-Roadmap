import streamlit as st

from app.loaders import load_document
from app.chains import analyze_document


st.set_page_config(
    page_title="AI Document Intelligence",
    page_icon="📄",
    layout="wide",
)

st.title("📄 AI Document Intelligence")
st.caption("Upload a PDF or DOCX and turn it into structured insights.")

uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "docx"],
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    temp_path = f"documents/{uploaded_file.name}"

    with open(temp_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    if st.button("Analyze Document", type="primary"):

        with st.spinner("Analyzing document..."):
            text = load_document(temp_path)
            result = analyze_document(text)

        st.divider()

        st.subheader("📋 Summary")
        st.write(result["summary"])

        st.subheader("🔍 Key Information")
        st.write(result["extraction"])

        st.subheader("🏷️ Key Topics")
        st.write(result["topics"])

        st.subheader("✅ Action Items")
        st.write(result["actions"])