# streamlit_app/config.py
"""
Configuration file for Kraft-it application
Manages ports, API endpoints, and app settings
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================
# PORT CONFIGURATION
# ============================================
STREAMLIT_PORT = int(os.getenv("STREAMLIT_PORT", 8501))
BACKEND_PORT = int(os.getenv("BACKEND_PORT", 8000))

# ============================================
# API CONFIGURATION
# ============================================
BACKEND_HOST = os.getenv("BACKEND_HOST", "localhost")
BACKEND_URL = f"http://{BACKEND_HOST}:{BACKEND_PORT}"

# API Endpoints
API_ENDPOINTS = {
    "merge": f"{BACKEND_URL}/api/merge",
    "split": f"{BACKEND_URL}/api/split",
    "compress": f"{BACKEND_URL}/api/compress",
    "convert": f"{BACKEND_URL}/api/convert",
    "history": f"{BACKEND_URL}/api/history",
    "chat_upload": f"{BACKEND_URL}/api/chat/upload",
    "chat_ask": f"{BACKEND_URL}/api/chat/ask",
}

# ============================================
# FILE UPLOAD SETTINGS
# ============================================
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", 10))
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024
ALLOWED_EXTENSIONS = ['pdf', 'docx', 'jpg', 'jpeg', 'png']

# ============================================
# APP SETTINGS
# ============================================
APP_NAME = "Kraft-it"
APP_VERSION = "1.0.0"
DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"

# ============================================
# FOLDERS
# ============================================
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER", "outputs")
TEMP_FOLDER = os.getenv("TEMP_FOLDER", "temp")

# Create folders if they don't exist
for folder in [UPLOAD_FOLDER, OUTPUT_FOLDER, TEMP_FOLDER]:
    os.makedirs(folder, exist_ok=True)

# ============================================
# DATABASE SETTINGS
# ============================================
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@localhost:5432/kraftit_db"
)