# start.py - Start script for Kraft-it (Django Backend)
"""
Start script to run Django backend and Streamlit frontend
Usage: python start.py [frontend|backend|dev|help]
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
    """Start Django backend server"""
    port = os.getenv("BACKEND_PORT", "8000")
    
    # Check if manage.py exists in root
    if not Path("manage.py").exists():
        print("❌ Error: manage.py not found in project root!")
        print("💡 Your Django project should have manage.py in Kraft-it/")
        print("\nExpected structure:")
        print("  Kraft-it/")
        print("  ├── manage.py          ← Should be here")
        print("  ├── kraftit/           ← Django config folder")
        print("  └── streamlit_app/")
        sys.exit(1)
    
    print(f"🚀 Starting Django Backend on port {port}...")
    
    # Run Django development server
    # Django's runserver already has auto-reload built-in!
    proc = subprocess.Popen([
        "python",
        "manage.py",
        "runserver",
        f"0.0.0.0:{port}"
    ])
    processes.append(proc)
    return proc

def     start_frontend():
    """Start Streamlit frontend"""
    port = os.getenv("STREAMLIT_PORT", "8501")
    print(f"🎨 Starting Frontend on port {port}...")
    print(f"🌐 Open: http://localhost:{port}")
    
    # Streamlit has its own auto-reload built-in
    proc = subprocess.Popen([
        "python", "-m", "streamlit",
        "run",
        "streamlit_app/Home.py",
        "--server.port", port,
        "--server.address", "localhost",
        "--server.runOnSave", "true",
        "--server.fileWatcherType", "auto"
    ])
    processes.append(proc)
    return proc

def start_dev():
    """Start both frontend and backend in development mode"""
    print("🚀 Starting Kraft-it in Development Mode (Django Backend)...")
    print("=" * 50)
    
    # Check Django setup
    if not Path("manage.py").exists():
        print("\n❌ Django backend not initialized!")
        print("\n📚 Your structure should be:")
        print("   Kraft-it/")
        print("   ├── manage.py              ← Django management")
        print("   ├── kraftit/               ← Django config")
        print("   │   ├── settings.py")
        print("   │   ├── urls.py")
        print("   │   └── wsgi.py")
        print("   ├── pdf/                   ← PDF app")
        print("   ├── streamlit_app/         ← Frontend")
        print("   └── start.py               ← This file")
        print("\n💡 If manage.py exists, make sure you're in the right directory!")
        sys.exit(1)
    
    # Start backend
    backend_proc = start_backend()
    
    # Wait for backend to initialize
    print("⏳ Waiting for Django to start...")
    time.sleep(3)
    
    # Start frontend
    frontend_proc = start_frontend()
    
    print("\n" + "=" * 50)
    print("✅ Both servers are running!")
    print("=" * 50)
    print(f"📡 Backend:  http://localhost:{os.getenv('BACKEND_PORT', '8000')}")
    print(f"🎨 Frontend: http://localhost:{os.getenv('STREAMLIT_PORT', '8501')}")
    print("=" * 50)
    
    # Keep the script running
    try:
        backend_proc.wait()
        frontend_proc.wait()
    except KeyboardInterrupt:
        cleanup_processes()

def django_commands():
    """Show helpful Django commands"""
    print("\n📚 Useful Django Commands:")
    print("=" * 50)
    print("\n🔧 Database:")
    print("   python manage.py makemigrations      # Create migrations")
    print("   python manage.py migrate             # Apply migrations")
    print("   python manage.py dbshell             # Database shell")
    
    print("\n👤 Users:")
    print("   python manage.py createsuperuser     # Create admin user")
    print("   python manage.py changepassword      # Change password")
    
    print("\n🎨 Apps:")
    print("   python manage.py startapp myapp      # Create new app")
    
    print("\n🧪 Testing:")
    print("   python manage.py test                # Run Django tests")
    print("   pytest tests/                        # Run pytest")
    
    print("\n📊 Management:")
    print("   python manage.py shell               # Django shell")
    print("   python manage.py showmigrations      # Show migrations")
    print("   python manage.py check               # Check for issues")
    print("   python manage.py collectstatic       # Collect static files")
    
    print("\n🚀 Server:")
    print("   python start.py backend              # Start backend only")
    print("   python start.py frontend             # Start frontend only")
    print("   python start.py dev                  # Start both")
    
    print("\n📁 Your Project Structure:")
    print("   Kraft-it/")
    print("   ├── manage.py              # Django management")
    print("   ├── kraftit/               # Django config folder")
    print("   ├── pdf/                   # PDF operations app")
    print("   ├── media/                 # Uploaded files")
    print("   ├── streamlit_app/         # Frontend UI")
    print("   └── start.py               # This script")
    print("\n" + "=" * 50)

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            mode = sys.argv[1].lower()
            
            if mode == "frontend":
                start_frontend()
                try:
                    processes[0].wait()
                except KeyboardInterrupt:
                    cleanup_processes()
                    
            elif mode == "backend":
                start_backend()
                try:
                    processes[0].wait()
                except KeyboardInterrupt:
                    cleanup_processes()
                    
            elif mode == "dev":
                start_dev()
                
            elif mode == "help" or mode == "commands":
                django_commands()
                
            else:
                print("Usage: python start.py [frontend|backend|dev|help]")
                print("\nExamples:")
                print("  python start.py dev       # Start both servers")
                print("  python start.py backend   # Start Django only")
                print("  python start.py frontend  # Start Streamlit only")
                print("  python start.py help      # Show Django commands")
        else:
            # Default: start in dev mode
            start_dev()
    except KeyboardInterrupt:
        cleanup_processes()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        cleanup_processes()