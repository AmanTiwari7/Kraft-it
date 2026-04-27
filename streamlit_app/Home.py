# streamlit_app/Home.py
import streamlit as st
from pathlib import Path
import sys

# Add the project root to the path
sys.path.append(str(Path(__file__).parent.parent))

# Import shared components
from streamlit_app.components.sidebar import render_sidebar
from streamlit_app.components.layout import page_header, navigation_cards

# Page configuration - MUST be the first Streamlit command
st.set_page_config(
    page_title="Kraft-it | PDF Toolkit",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/yourusername/kraft-it',
        'Report a bug': "https://github.com/yourusername/kraft-it/issues",
        'About': "# Kraft-it PDF Toolkit\nVersion 1.0.0"
    }
)

# Custom CSS for better UI
st.markdown("""
    <style>
    /* Main header styling */
    .main-header {
        font-size: 3.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #1f77b4, #4a9eff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        padding: 1rem 0;
    }
    
    .sub-header {
        font-size: 1.3rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Feature card styling */
    .feature-card {
        padding: 25px;
        border-radius: 15px;
        margin: 10px 0;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 200px;
        cursor: pointer;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.2);
    }
    
    .feature-card h3 {
        color: white !important;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .feature-card p {
        color: rgba(255,255,255,0.9) !important;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Card color variations */
    .card-blue {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .card-green {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    .card-purple {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    
    .card-orange {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
    }
    
    .card-teal {
        background: linear-gradient(135deg, #30cfd0 0%, #330867 100%);
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Render sidebar
render_sidebar()

# Header
st.markdown('<div class="main-header">📄 Kraft-it</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Your Complete PDF Manipulation Toolkit</div>', unsafe_allow_html=True)

st.markdown("---")

# Feature cards with navigation
st.subheader("🛠️ Available Tools")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card card-blue">
        <h3>🔗 Merge PDFs</h3>
        <p>Combine multiple PDF files into one document seamlessly. Fast, easy, and preserves all formatting.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔗 Go to Merge PDFs", key="nav_merge", use_container_width=True):
        st.switch_page("pages/1_Merge_PDFs.py")

with col2:
    st.markdown("""
    <div class="feature-card card-green">
        <h3>✂️ Split PDFs</h3>
        <p>Extract specific pages or split PDFs into multiple files. Precise control over page selection.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("✂️ Go to Split PDF", key="nav_split", use_container_width=True):
        st.switch_page("pages/2_Split_PDF.py")

with col3:
    st.markdown("""
    <div class="feature-card card-purple">
        <h3>🗜️ Compress PDFs</h3>
        <p>Reduce file size while maintaining quality. Perfect for email attachments and storage.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🗜️ Go to Compress PDF", key="nav_compress", use_container_width=True):
        st.switch_page("pages/3_Compress_PDF.py")

st.markdown("<br>", unsafe_allow_html=True)

col4, col5 = st.columns(2)

with col4:
    st.markdown("""
    <div class="feature-card card-orange">
        <h3>🔄 Convert Files</h3>
        <p>Convert between PDF and other formats. Support for images, documents, and more.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 Go to Convert Files", key="nav_convert", use_container_width=True):
        st.switch_page("pages/4_Convert_Files.py")

with col5:
    st.markdown("""
    <div class="feature-card card-teal">
        <h3>💬 Chat with PDF</h3>
        <p>Upload a PDF and ask questions about its content using AI. Get instant answers.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("💬 Go to Chat", key="nav_chat", use_container_width=True):
        st.switch_page("pages/6_Chat_with_PDF.py")

st.markdown("---")

# How to use section
st.header("🚀 Getting Started")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### Quick Start Guide
    
    1. **Select a tool** - Choose from the cards above or use the sidebar menu
    2. **Upload your files** - Drag and drop or click to browse
    3. **Configure settings** - Adjust options based on your needs
    4. **Process & Download** - Get your processed files instantly
    
    ### Why Choose Kraft-it?
    
    - 🔒 **Secure** - All files are processed locally and deleted after use
    - ⚡ **Fast** - Lightning-fast processing with modern algorithms
    - 🎯 **Simple** - Intuitive interface, no learning curve
    - 🔄 **Reliable** - Robust error handling and validation
    - 📱 **Responsive** - Works on desktop, tablet, and mobile
    """)

with col2:
    st.info("""
    **💡 Pro Tips:**
    
    - Upload multiple files at once
    - Drag and drop for faster workflow
    - Check history for past operations
    - Files auto-delete after processing
    - Use keyboard shortcuts (Ctrl+S)
    """)

st.markdown("---")

# Features section
st.header("✨ Features")

col1, col2 = st.columns(2)

with col1:
    st.success("✅ **Secure Processing** - Files deleted after use")
    st.success("✅ **No Size Limits** - Process large files easily")
    st.success("✅ **Multiple Formats** - Support for PDF, DOCX, images")
    st.success("✅ **Batch Operations** - Process multiple files at once")

with col2:
    st.success("✅ **History Tracking** - Keep track of all operations")
    st.success("✅ **Fast Processing** - Lightning-fast algorithms")
    st.success("✅ **Easy to Use** - Simple, intuitive interface")
    st.success("✅ **Free & Open Source** - No hidden costs")

st.markdown("---")

# Stats or additional info
st.header("📊 Quick Stats")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Supported Formats", "5+", delta="PDF, DOCX, JPG...")

with col2:
    st.metric("Processing Speed", "< 5s", delta="Average time")

with col3:
    st.metric("Max File Size", "10 MB", delta="Configurable")

with col4:
    st.metric("Tools Available", "5", delta="More coming soon")

st.markdown("---")

# Call to action
st.markdown("""
<div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            border-radius: 15px; color: white; margin: 2rem 0;'>
    <h2 style='color: white; margin: 0;'>Ready to Get Started?</h2>
    <p style='color: rgba(255,255,255,0.9); margin: 1rem 0;'>
        Choose a tool from above and start processing your PDFs in seconds!
    </p>
</div>
""", unsafe_allow_html=True)