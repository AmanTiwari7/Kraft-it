"""
API views for PDF operations
"""
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
# from utils.merge import merge_pdfs

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def merge_pdf(request):
    """
    Merge multiple PDF files into one
    
    POST /api/pdf/merge/
    Body: files (multiple PDF files)
    """
    files = request.FILES.getlist('files')
    
    if len(files) < 2:
        return Response(
            {"error": "At least 2 PDF files are required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # TODO: Implement actual PDF merging logic using core/
    # from core.merge import merge_pdfs
    # result = merge_pdfs(files, "C:\\Users\\Aman Tiwari\Desktop\\VSCode Files\\Kraft-it\\media\\outputs")
    
    return Response({
        "message": "PDF merge endpoint",
        "files_received": len(files),
        "filenames": [f.name for f in files]
    })


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def split_pdf(request):
    """
    Split a PDF file into multiple files
    
    POST /api/pdf/split/
    Body: file (single PDF file), pages (optional)
    """
    if 'file' not in request.FILES:
        return Response(
            {"error": "PDF file is required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    file = request.FILES['file']
    pages = request.data.get('pages', 'all')
    
    # TODO: Implement actual PDF splitting logic
    # from core.split import split_pdf
    # result = split_pdf(file, pages)
    
    return Response({
        "message": "PDF split endpoint (implementation pending)",
        "filename": file.name,
        "pages": pages
    })


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def compress_pdf(request):
    """
    Compress a PDF file to reduce size
    
    POST /api/pdf/compress/
    Body: file (single PDF file), quality (optional)
    """
    if 'file' not in request.FILES:
        return Response(
            {"error": "PDF file is required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    file = request.FILES['file']
    quality = request.data.get('quality', 'medium')
    
    # TODO: Implement actual PDF compression logic
    # from core.compress import compress_pdf
    # result = compress_pdf(file, quality)
    
    return Response({
        "message": "PDF compress endpoint (implementation pending)",
        "filename": file.name,
        "quality": quality
    })


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def convert_file(request):
    """
    Convert files between different formats
    
    POST /api/pdf/convert/
    Body: file, output_format
    """
    if 'file' not in request.FILES:
        return Response(
            {"error": "File is required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    file = request.FILES['file']
    output_format = request.data.get('output_format', 'pdf')
    
    # TODO: Implement actual file conversion logic
    # from core.convert import convert_file
    # result = convert_file(file, output_format)
    
    return Response({
        "message": "File conversion endpoint (implementation pending)",
        "filename": file.name,
        "output_format": output_format
    })