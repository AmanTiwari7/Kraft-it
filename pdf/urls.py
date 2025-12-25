"""
URL patterns for PDF operations
"""
from django.urls import path
from . import views

app_name = 'pdf'

urlpatterns = [
    path('merge/', views.merge_pdf, name='merge'),
    path('split/', views.split_pdf, name='split'),
    path('compress/', views.compress_pdf, name='compress'),
    path('convert/', views.convert_file, name='convert'),
]