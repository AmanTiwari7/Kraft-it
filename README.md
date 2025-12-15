# 📄 Kraft-it - Complete PDF Manipulation Toolkit

![CI/CD Pipeline](https://github.com/YourUsername/Kraft-it/workflows/Simple%20CI/badge.svg)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A complete Python utility for PDF merging, compression, and document manipulation. All-in-one PDF editing toolkit built with Streamlit, FastAPI, and PostgreSQL.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- PostgreSQL (optional, for history tracking)
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/YourUsername/Kraft-it.git
cd Kraft-it

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
# Edit .env with your settings
```

---

## 🎮 Running the Application

### Method 1: Using Python Script (Recommended)

```bash
# Start both frontend and backend
python start.py dev

# Or start separately:
python start.py frontend  # Only Streamlit UI
python start.py backend   # Only FastAPI server
```

### Method 2: Using Make Commands

```bash
# Start development environment
make dev

# Or start separately:
make frontend  # Only frontend
make backend   # Only backend

# Other useful commands:
make install   # Install dependencies
make test      # Run tests
make lint      # Check code quality
make format    # Format code
make clean     # Clean temp files
```

### Method 3: Manual Start

**Terminal 1 - Backend:**
```bash
uvicorn api.main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
streamlit run streamlit_app/Home.py --server.port 8501
```

### Method 4: PowerShell (Windows)

```powershell
# Start both servers
.\start-dev.ps1
```

---

## 🌐 Access Points

Once running, access the application at:

- **Frontend (Streamlit)**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs (Swagger UI)
- **Alternative API Docs**: http://localhost:8000/redoc

---

## 📁 Project Structure

```
Kraft-it/
│
├── kraft_it/                 # Core PDF manipulation library
│   ├── __init__.py
│   ├── merge.py             # PDF merging logic
│   ├── split.py             # PDF splitting logic
│   ├── compress.py          # PDF compression
│   ├── convert.py           # File conversion
│   ├── database/            # Database models and config
│   ├── services/            # Business logic services
│   └── utils/               # Helper functions
│
├── streamlit_app/           # Frontend UI
│   ├── Home.py             # Main entry point
│   ├── pages/              # Multi-page app
│   │   ├── 1_Merge_PDFs.py
│   │   ├── 2_Split_PDF.py
│   │   ├── 3_Compress_PDF.py
│   │   ├── 4_Convert_Files.py
│   │   └── 5_History_or_Logs.py
│   ├── components/         # Reusable UI components
│   └── config.py           # Frontend configuration
│
├── api/                     # Backend API
│   ├── main.py             # FastAPI application
│   └── routes/             # API endpoints
│       ├── pdf_routes.py
│       └── history_routes.py
│
├── tests/                   # Test suite
│   ├── test_merge.py
│   ├── test_split.py
│   └── test_compress.py
│
├── docs/                    # Documentation
├── docker/                  # Docker configuration
│
├── .env                     # Environment variables (create from .env.example)
├── requirements.txt         # Python dependencies
├── start.py                # Start script
├── Makefile                # Command shortcuts
└── README.md               # This file
```

---

## 🎯 Features

### Current Features
- ✅ **Merge PDFs**: Combine multiple PDF files into one
- ✅ **Split PDFs**: Extract pages or split into multiple files
- ✅ **Compress PDFs**: Reduce file size
- ✅ **Convert Files**: Convert between different formats
- ✅ **History Tracking**: Keep track of all operations
- ✅ **Clean UI**: Beautiful Streamlit interface
- ✅ **REST API**: FastAPI backend for programmatic access

### Coming Soon
- 🔄 **Rotate Pages**: Rotate PDF pages
- 🔐 **Password Protection**: Add/remove PDF passwords
- 🖼️ **Extract Images**: Extract images from PDFs
- 📝 **Add Watermarks**: Add text/image watermarks
- 🔍 **OCR Support**: Extract text from scanned PDFs

---

## 🔧 Configuration

### Port Configuration

Edit `.env` file to change ports:

```env
# Frontend port
STREAMLIT_PORT=8501

# Backend port
BACKEND_PORT=8000
```

### Database Configuration

```env
DATABASE_URL=postgresql://username:password@localhost:5432/kraftit_db
```

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=kraft_it --cov-report=html

# Run specific test file
pytest tests/test_merge.py -v
```

---

## 📚 API Documentation

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API health check |
| `/health` | GET | Health status |
| `/api/merge` | POST | Merge PDF files |
| `/api/split` | POST | Split PDF file |
| `/api/compress` | POST | Compress PDF |
| `/api/convert` | POST | Convert file formats |
| `/api/history` | GET | Get operation history |

### Example API Call

```python
import requests

# Merge PDFs
files = [
    ('files', open('file1.pdf', 'rb')),
    ('files', open('file2.pdf', 'rb'))
]
response = requests.post('http://localhost:8000/api/merge', files=files)
```

---

## 🐳 Docker Support

```bash
# Build image
docker build -t kraftit -f docker/Dockerfile .

# Run with docker-compose
docker-compose -f docker/docker-compose.yml up
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Backend powered by [FastAPI](https://fastapi.tiangolo.com/)
- PDF manipulation using [PyPDF](https://pypdf.readthedocs.io/)

---

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the [documentation](docs/)
- Contact: your.email@example.com

---

## 🗺️ Roadmap

- [x] Basic PDF operations
- [x] Streamlit UI
- [x] FastAPI backend
- [ ] Database integration
- [ ] User authentication
- [ ] Cloud deployment
- [ ] Mobile app

---

**Made with ❤️ by Developers**