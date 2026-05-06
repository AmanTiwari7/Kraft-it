# streamlit_app/pages/6_Chat_with_PDF.py
import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Chat with PDF", page_icon="💬", layout="wide")

st.title("💬 Chat with PDF")
st.markdown("Upload a PDF and ask questions about its content.")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "uploaded_pdf" not in st.session_state:
    st.session_state.uploaded_pdf = None

if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

# Instructions
with st.expander("ℹ️ How to use"):
    st.markdown("""
    1. Upload a PDF file
    2. Wait for the PDF to be processed
    3. Ask questions about the PDF content
    4. Get AI-powered answers based on the document
    """)

st.markdown("---")

# Create two columns: sidebar for upload, main for chat
col1, col2 = st.columns([1, 2])

# ============================================
# LEFT COLUMN - PDF UPLOAD SECTION
# ============================================
with col1:
    st.subheader("📄 Upload PDF")
    
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=['pdf'],
        accept_multiple_files=False,
        help="Upload a single PDF file to chat with"
    )
    
    if uploaded_file is not None:
        st.session_state.uploaded_pdf = uploaded_file
        
        # Display file info
        st.success("✅ File uploaded successfully")
        st.metric("File Name", uploaded_file.name)
        st.metric("File Size", f"{uploaded_file.size / 1024:.2f} KB")
        
        st.markdown("---")
        
        # Process PDF button
        if st.button("🔄 Process PDF", type="primary", use_container_width=True):
            with st.spinner("Processing PDF..."):
                try:
                    # TODO: Send PDF to backend API for processing
                    # Example backend call:
                    files = {'file': (uploaded_file.name, uploaded_file, 'application/pdf')}
                    response = requests.post(
                        'http://localhost:8000/api/chat/upload/',
                        files=files
                    )
                    if response.status_code == 200:
                        st.session_state.pdf_processed = True
                        st.success("✅ PDF processed successfully!")
                    else:
                        st.error("Failed to process PDF")
                    
                    # For now, just mark as processed (simulate)
                    st.session_state.pdf_processed = True
                    st.success("✅ PDF processed successfully!")
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Error processing PDF: {str(e)}")
        
        st.markdown("---")
        
        # Clear chat history when new PDF is uploaded
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.session_state.pdf_processed = False
            st.rerun()

# ============================================
# RIGHT COLUMN - CHAT SECTION
# ============================================
with col2:
    if st.session_state.uploaded_pdf is None:
        st.info("👈 Please upload a PDF file to start chatting")
    
    elif not st.session_state.pdf_processed:
        st.info("👈 Please click 'Process PDF' to start chatting")
    
    else:
        st.subheader("💬 Chat")
        
        # Display chat history
        chat_container = st.container()
        
        with chat_container:
            for message in st.session_state.chat_history:
                if message["role"] == "user":
                    with st.chat_message("user"):
                        st.markdown(message["content"])
                else:
                    with st.chat_message("assistant"):
                        st.markdown(message["content"])
        
        st.markdown("---")
        
        # Chat input
        user_input = st.chat_input(
            "Ask a question about the PDF...",
            disabled=not st.session_state.pdf_processed
        )
        
        if user_input:
            # Add user message to chat history
            st.session_state.chat_history.append({
                "role": "user",
                "content": user_input,
                "timestamp": datetime.now().isoformat()
            })
            
            # Display user message immediately
            with st.chat_message("user"):
                st.markdown(user_input)
            
            # Get response from backend
            with st.spinner("Getting response..."):
                try:
                    # TODO: Send question to backend API
                    # Example backend call:
                    # response = requests.post(
                    #     'http://localhost:8000/api/chat/ask/',
                    #     json={
                    #         'question': user_input,
                    #         'pdf_id': st.session_state.pdf_id  # Store this when processing PDF
                    #     }
                    # )
                    # if response.status_code == 200:
                    #     answer = response.json()['answer']
                    # else:
                    #     answer = "Sorry, I couldn't process that question."
                    
                    # For now, just show a placeholder response
                    answer = f"I received your question: '{user_input}'. Please implement the backend API to get AI-powered answers."
                    
                    # Add assistant message to chat history
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": answer,
                        "timestamp": datetime.now().isoformat()
                    })
                    
                    # Display assistant message
                    with st.chat_message("assistant"):
                        st.markdown(answer)
                    
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Error getting response: {str(e)}")

# ============================================
# FOOTER - USAGE STATS
# ============================================
st.markdown("---")

if st.session_state.uploaded_pdf and st.session_state.pdf_processed:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Messages", len(st.session_state.chat_history))
    
    with col2:
        questions = len([m for m in st.session_state.chat_history if m["role"] == "user"])
        st.metric("Questions Asked", questions)
    
    with col3:
        answers = len([m for m in st.session_state.chat_history if m["role"] == "assistant"])
        st.metric("Answers Received", answers)
