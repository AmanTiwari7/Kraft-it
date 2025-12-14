# api/main.py
"""
FastAPI Backend for Kraft-it
Main entry point for the API server
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import routes (we'll create these next)
# from api.routes import pdf_routes, history_routes

# ============================================
# APP INITIALIZATION
# ============================================
app = FastAPI(
    title="Kraft-it API",
    description="Backend API for PDF manipulation toolkit",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI at http://localhost:8000/docs
    redoc_url="/redoc"  # ReDoc at http://localhost:8000/redoc
)

# ============================================
# CORS CONFIGURATION
# ============================================
# This allows your Streamlit frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",  # Streamlit default port
        f"http://localhost:{os.getenv('STREAMLIT_PORT', 8501)}",  # Custom port
        "http://127.0.0.1:8501",
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# ============================================
# ROOT ENDPOINT
# ============================================
@app.get("/")
async def root():
    """Root endpoint - API health check"""
    return {
        "message": "Welcome to Kraft-it API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
        "endpoints": {
            "merge": "/api/merge",
            "split": "/api/split",
            "compress": "/api/compress",
            "convert": "/api/convert",
            "history": "/api/history"
        }
    }

# ============================================
# HEALTH CHECK
# ============================================
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Kraft-it API",
        "version": "1.0.0"
    }

# ============================================
# ERROR HANDLERS
# ============================================
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )

# ============================================
# INCLUDE ROUTERS (uncomment when routes are ready)
# ============================================
# app.include_router(pdf_routes.router, prefix="/api", tags=["PDF Operations"])
# app.include_router(history_routes.router, prefix="/api", tags=["History"])

# ============================================
# STARTUP & SHUTDOWN EVENTS
# ============================================
@app.on_event("startup")
async def startup_event():
    """Run on application startup"""
    print("🚀 Kraft-it API starting up...")
    print(f"📡 Server running on port {os.getenv('BACKEND_PORT', 8000)}")
    print(f"📚 Documentation available at http://localhost:{os.getenv('BACKEND_PORT', 8000)}/docs")

@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown"""
    print("👋 Kraft-it API shutting down...")

# ============================================
# RUN SERVER (for development)
# ============================================
if __name__ == "__main__":
    PORT = int(os.getenv("BACKEND_PORT", 8000))
    HOST = os.getenv("BACKEND_HOST", "0.0.0.0")
    
    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=True,  # Auto-reload on code changes (dev only)
        log_level="debug"
    )