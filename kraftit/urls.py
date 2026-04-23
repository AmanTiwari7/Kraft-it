"""
URL configuration for kraftit project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

def api_root(request):
    """Root API endpoint"""
    return JsonResponse({
        "message": "Welcome to Kraft-it API",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "health": "/health/",
            "pdf_api": "/api/pdfs/",
            "pdf_merge": "/api/pdf/merge/",
        }
    })

def health_check(request):
    return JsonResponse({"status": "healthy"})

def pdf_api(req):
    return JsonResponse({
        "message": "APIs in PDFs",
        "endpoints": {
            "health": "/health/",
            "pdf_api": "/api/pdfs/",
            "pdf_merge":"/api/pdfs/merge/",
            "test": "/api/pdfs/test/"
        }
    })

urlpatterns = [
    # Root endpoint
    path('', api_root, name='api-root'),
    
    # Health check
    path('health/', health_check, name='health'),
    path('api/pdfs/', pdf_api, name='any'),
    
    # PDF API endpoints
    path('api/pdfs/', include('pdf.urls')),

]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    