# streamlit_app/pages/1_Merge_PDFs.py
import streamlit as st
import requests
from pathlib import Path
import io

st.set_page_config(page_title="Merge PDFs", page_icon="🔗", layout="wide")

st.title("🔗 Merge PDF Files")
st.markdown("Combine multiple PDF files into a single document.")

# Instructions
with st.expander("ℹ️ How to use"):
    st.markdown("""
    1. Upload 2 or more PDF files
    2. Arrange them in the order you want
    3. Click 'Merge PDFs' button
    4. Download the merged PDF
    """)

st.markdown("---")

# File uploader
uploaded_files = st.file_uploader(
    "Upload PDF files to merge",
    type=['pdf'],
    accept_multiple_files=True,
    help="You can upload multiple PDF files at once"
)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} file(s) uploaded")
    
    # Display uploaded files
    st.subheader("📑 Uploaded Files:")
    for idx, file in enumerate(uploaded_files, 1):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{idx}. {file.name}")
        with col2:
            st.write(f"{file.size / 1024:.2f} KB")
    
    st.markdown("---")
    
    # Merge button
    if st.button("🔗 Merge PDFs", type="primary", use_container_width=True):
        if len(uploaded_files) < 2:
            st.error("⚠️ Please upload at least 2 PDF files to merge.")
        else:
            with st.spinner("Merging PDFs..."):
                try:
                    # TODO: Call backend API here
                    # For now, just show a placeholder
                    
                    # Example API call (uncomment when backend is ready):
                    # files = [('files', (file.name, file, 'application/pdf')) 
                    #          for file in uploaded_files]
                    # response = requests.post(
                    #     'http://localhost:8000/api/merge',
                    #     files=files
                    # )
                    
                    st.success("✅ PDFs merged successfully!")
                    st.info("🔧 Backend API integration coming soon...")
                    
                    # Placeholder download button
                    st.download_button(
                        label="📥 Download Merged PDF",
                        data=b"",  # Will contain actual PDF data from backend
                        file_name="merged_output.pdf",
                        mime="application/pdf",
                        disabled=True,  # Enable when backend is ready
                        help="Backend integration in progress"
                    )
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
else:
    st.info("👆 Please upload PDF files to get started")

# Sidebar info
st.sidebar.markdown("### 🔗 Merge PDFs")
st.sidebar.markdown("""
**Features:**
- Combine unlimited PDFs
- Preserve formatting
- Fast processing
- Maintain quality
""")