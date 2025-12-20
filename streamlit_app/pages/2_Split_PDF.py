# streamlit_app/pages/2_Split_PDF.py
import streamlit as st
import requests

st.set_page_config(page_title="Split PDF", page_icon="✂️", layout="wide")

st.title("✂️ Split PDF File")
st.markdown("Extract specific pages or split a PDF into multiple files.")

# Instructions
with st.expander("ℹ️ How to use"):
    st.markdown("""
    1. Upload a PDF file
    2. Choose split method:
       - **By Page Range**: Extract specific pages (e.g., 1-5, 10-15)
       - **By Page Numbers**: Extract individual pages (e.g., 1, 3, 7)
       - **Split All**: Separate into individual pages
    3. Click 'Split PDF' button
    4. Download the result
    """)

st.markdown("---")

# File uploader
uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=['pdf'],
    help="Upload the PDF you want to split"
)

if uploaded_file:
    st.success(f"✅ File uploaded: {uploaded_file.name} ({uploaded_file.size / 1024:.2f} KB)")
    
    st.markdown("---")
    
    # Split options
    split_method = st.radio(
        "Choose split method:",
        ["By Page Range", "By Page Numbers", "Split All Pages"],
        help="Select how you want to split the PDF"
    )
    
    if split_method == "By Page Range":
        col1, col2 = st.columns(2)
        with col1:
            start_page = st.number_input("Start Page", min_value=1, value=1)
        with col2:
            end_page = st.number_input("End Page", min_value=1, value=5)
        
        st.info(f"📄 Will extract pages {start_page} to {end_page}")
    
    elif split_method == "By Page Numbers":
        page_numbers = st.text_input(
            "Enter page numbers (comma-separated)",
            placeholder="e.g., 1, 3, 5, 7",
            help="Enter specific page numbers you want to extract"
        )
        if page_numbers:
            st.info(f"📄 Will extract pages: {page_numbers}")
    
    else:  # Split All Pages
        st.info("📄 Will split into individual pages")
    
    st.markdown("---")
    
    # Split button
    if st.button("✂️ Split PDF", type="primary", use_container_width=True):
        with st.spinner("Splitting PDF..."):
            try:
                # TODO: Call backend API here
                st.success("✅ PDF split successfully!")
                st.info("🔧 Backend API integration coming soon...")
                
                # Placeholder download button
                st.download_button(
                    label="📥 Download Split PDF(s)",
                    data=b"",
                    file_name="split_output.pdf",
                    mime="application/pdf",
                    disabled=True,
                    help="Backend integration in progress"
                )
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
else:
    st.info("👆 Please upload a PDF file to get started")

# Sidebar info
st.sidebar.markdown("### ✂️ Split PDF")
st.sidebar.markdown("""
**Features:**
- Extract specific pages
- Split by range
- Create individual pages
- Preserve quality
""")