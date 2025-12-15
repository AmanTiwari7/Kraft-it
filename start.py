"""
Start script to run frontend and backend together
Usage: python start.py [frontend|backend|dev]
"""
import subprocess
import sys
import os
import time
from dotenv import load_dotenv

load_dotenv()

def start_backend():
    """Start FastAPI backend server"""
    port = os.getenv("BACKEND_PORT", "8000")
    print(f"🚀 Starting Backend on port {port}...")
    print(f"📚 API Docs: http://localhost:{port}/docs")
    
    subprocess.run([
        "uvicorn",
        "api.main:app",
        "--reload",
        "--port", port,
        "--host", "0.0.0.0"
    ])

def start_frontend():
    """Start Streamlit frontend"""
    port = os.getenv("STREAMLIT_PORT", "8501")
    print(f"🎨 Starting Frontend on port {port}...")
    print(f"🌐 Open: http://localhost:{port}")
    
    subprocess.run([
        "streamlit",
        "run",
        "streamlit_app/Home.py",
        "--server.port", port,
        "--server.address", "localhost"
    ])

def start_dev():
    """Start both frontend and backend in development mode"""
    import threading
    
    print("🚀 Starting Kraft-it in Development Mode...")
    print("=" * 50)
    
    # Start backend in a separate thread
    backend_thread = threading.Thread(target=start_backend, daemon=True)
    backend_thread.start()
    
    # Wait for backend to start
    time.sleep(2)
    
    # Start frontend (blocking)
    start_frontend()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        
        if mode == "frontend":
            start_frontend()
        elif mode == "backend":
            start_backend()
        elif mode == "dev":
            start_dev()
        else:
            print("Usage: python start.py [frontend|backend|dev]")
    else:
        # Default: start in dev mode
        start_dev()