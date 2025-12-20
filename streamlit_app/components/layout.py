# streamlit_app/components/layout.py
"""
Shared layout components and utilities
"""
import streamlit as st

def page_header(title, icon="📄", description=""):
    """Render a consistent page header"""
    st.markdown(f"""
        <div style='text-align: center; padding: 2rem 0 1rem 0;'>
            <h1 style='color: #1f77b4; font-size: 2.5rem; margin: 0;'>
                {icon} {title}
            </h1>
            {f"<p style='color: #666; font-size: 1.1rem; margin-top: 0.5rem;'>{description}</p>" if description else ""}
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

def success_message(message):
    """Show a success message"""
    st.success(f"✅ {message}")

def error_message(message):
    """Show an error message"""
    st.error(f"❌ {message}")

def info_message(message):
    """Show an info message"""
    st.info(f"ℹ️ {message}")

def warning_message(message):
    """Show a warning message"""
    st.warning(f"⚠️ {message}")

def loading_spinner(message="Processing..."):
    """Context manager for loading spinner"""
    return st.spinner(f"⏳ {message}")

def instructions_expander(instructions_list, title="ℹ️ How to use"):
    """Render collapsible instructions"""
    with st.expander(title):
        for i, instruction in enumerate(instructions_list, 1):
            st.markdown(f"{i}. {instruction}")

def file_info_card(filename, filesize, filetype="PDF"):
    """Display file information in a card"""
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.markdown(f"**📄 {filename}**")
    with col2:
        st.markdown(f"`{filesize:.2f} KB`")
    with col3:
        st.markdown(f"`{filetype}`")

def action_button(label, key=None, help_text="", type="primary"):
    """Render a consistent action button"""
    return st.button(
        label,
        key=key,
        help=help_text,
        type=type,
        use_container_width=True
    )

def navigation_cards():
    """Render navigation cards for quick access"""
    st.subheader("🚀 Quick Access")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔗 Merge PDFs", use_container_width=True):
            st.switch_page("pages/1_Merge_PDFs.py")
    
    with col2:
        if st.button("✂️ Split PDF", use_container_width=True):
            st.switch_page("pages/2_Split_PDF.py")
    
    with col3:
        if st.button("🗜️ Compress PDF", use_container_width=True):
            st.switch_page("pages/3_Compress_PDF.py")

def breadcrumb(pages):
    """Render breadcrumb navigation"""
    breadcrumb_html = " → ".join([f"**{page}**" for page in pages])
    st.markdown(breadcrumb_html)
    st.markdown("---")