# start.py - Cross-platform start script for Kraft-it
"""
Start script to run frontend and backend together
Usage: python start.py [frontend|backend|dev]
"""
import subprocess
import sys
import os
import time
import signal
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Store process references for cleanup
processes = []

def cleanup_processes(signum=None, frame=None):
    """Clean up all child processes on exit"""
    print("\n🛑 Shutting down gracefully...")
    for proc in processes:
        try:
            proc.terminate()
            proc.wait(timeout=3)
        except:
            try:
                proc.kill()
            except:
                pass
    print("✅ All servers stopped")
    sys.exit(0)

# Register cleanup handler
signal.signal(signal.SIGINT, cleanup_processes)
signal.signal(signal.SIGTERM, cleanup_processes)

def start_backend():
    """Start FastAPI backend server"""
    port = os.getenv("BACKEND_PORT", "8000")
    print(f"🚀 Starting Backend on port {port}...")
    print(f"📚 API Docs: http://localhost:{port}/docs")
    
    # Only watch api/ folder for changes (not start.py or frontend files!)
    proc = subprocess.Popen([
        "uvicorn",
        "api.main:app",
        "--reload",
        "--reload-dir", "api",  # ← ONLY watch api folder!
        "--reload-dir", "kraft_it",  # ← And core library
        "--port", port,
        "--host", "0.0.0.0"
    ])
    processes.append(proc)
    return proc

def start_frontend():
    """Start Streamlit frontend"""
    port = os.getenv("STREAMLIT_PORT", "8501")
    print(f"🎨 Starting Frontend on port {port}...")
    print(f"🌐 Open: http://localhost:{port}")
    
    # Streamlit has its own auto-reload built-in
    proc = subprocess.Popen([
        "streamlit",
        "run",
        "streamlit_app/Home.py",
        "--server.port", port,
        "--server.address", "localhost",
        "--server.runOnSave", "true",  # ← Auto-reload on file changes
        "--server.fileWatcherType", "auto"  # ← Watch for changes
    ])
    processes.append(proc)
    return proc

def start_dev():
    """Start both frontend and backend in development mode"""
    print("🚀 Starting Kraft-it in Development Mode...")
    print("=" * 50)
    print("💡 Press Ctrl+C to stop all servers")
    print("=" * 50)
    
    # Start backend
    backend_proc = start_backend()
    
    # Wait for backend to initialize
    print("⏳ Waiting for backend to start...")
    time.sleep(3)
    
    # Start frontend
    frontend_proc = start_frontend()
    
    print("\n" + "=" * 50)
    print("✅ Both servers are running!")
    print("=" * 50)
    print(f"📡 Backend:  http://localhost:{os.getenv('BACKEND_PORT', '8000')}")
    print(f"🎨 Frontend: http://localhost:{os.getenv('STREAMLIT_PORT', '8501')}")
    print("=" * 50)
    print("\n💡 Tips....:")
    
    print("   - Edit frontend files → Streamlit auto-reloads")
    print("   - Edit backend files → FastAPI auto-reloads")
    print("   - Edit start.py → Won't trigger reloads anymore!")
    print("\n🛑 Press Ctrl+C to stop all servers\n")
    
    # Keep the script running
    try:
        # Wait for both processes
        backend_proc.wait()
        frontend_proc.wait()
    except KeyboardInterrupt:
        cleanup_processes()

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            mode = sys.argv[1].lower()
            
            if mode == "frontend":
                start_frontend()
                # Keep running
                try:
                    processes[0].wait()
                except KeyboardInterrupt:
                    cleanup_processes()
                    
            elif mode == "backend":
                start_backend()
                # Keep running
                try:
                    processes[0].wait()
                except KeyboardInterrupt:
                    cleanup_processes()
                    
            elif mode == "dev":
                start_dev()
            else:
                print("Usage: python start.py [frontend|backend|dev]")
                print("\nExamples:")
                print("  python start.py dev       # Start both servers")
                print("  python start.py frontend  # Start only frontend")
                print("  python start.py backend   # Start only backend")
        else:
            # Default: start in dev mode
            start_dev()
    except KeyboardInterrupt:
        cleanup_processes()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        cleanup_processes()