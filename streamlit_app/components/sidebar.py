# streamlit_app/components/sidebar.py
"""
Shared sidebar component for all pages
"""
import streamlit as st

def render_sidebar():
    """Render the sidebar with navigation and info"""
    
    with st.sidebar:
        # Logo/Header
        st.markdown("""
            <div style='text-align: center; padding: 1rem 0;'>
                <h2 style='color: #1f77b4; margin: 0;'>📄 Kraft-it</h2>
                <p style='color: #666; font-size: 0.9rem; margin: 0;'>PDF Toolkit</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Navigation info
        st.markdown("### 🧭 Navigation")
        st.info("""
        Use the menu above to navigate between tools:
        - 🏠 Home
        - 🔗 Merge PDFs
        - ✂️ Split PDF
        - 🗜️ Compress PDF
        - 🔄 Convert Files
        """)
        
        st.markdown("---")
        
        # Tips section
        st.markdown("### 💡 Tips")
        tips = [
            "Upload multiple files at once",
            "Drag and drop files for faster upload",
            "Check history for past operations",
            "Files are automatically deleted after processing"
        ]
        
        import random
        st.info(random.choice(tips))
        
        st.markdown("---")
        
        # Footer
        st.markdown("""
            <div style='text-align: center; font-size: 0.8rem; color: #666;'>
                <p><strong>Kraft-it v1.0</strong></p>
                <p>Built with ❤️ using</p>
                <p>🎨 Streamlit | ⚡ FastAPI | 🐍 Python</p>
            </div>
        """, unsafe_allow_html=True)

def update_stats(files_count=0, operation=False):
    """Update session statistics"""
    if files_count > 0:
        st.session_state.files_processed += files_count
    if operation:
        st.session_state.operations_count += 1