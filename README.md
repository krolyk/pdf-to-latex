# 📚 Academic PDF to LaTeX Converter API

A FastAPI-based service that uses AI (Google Gemini) to convert **scanned academic PDFs** — including **text, equations, and diagrams** — into clean LaTeX code.

---

## ✨ Features

- 🔤 **Text & Math Recognition** — Accurately converts text and math equations to LaTeX
- 📄 **Multi-page PDF Support** — Processes PDFs page-by-page
- 🧠 **Image Preprocessing** — Enhances OCR accuracy using automated techniques
- ⚡ **Fast & Async Backend** — Built with FastAPI and supports asynchronous processing

---

## 🧰 Requirements

- **Python** 3.10 or higher
- **Google Gemini API Key** – [Get one here](https://ai.google.dev/)
- **System Dependencies**:
  ```bash
  # Ubuntu/Debian
  sudo apt install poppler-utils libmagic1

  # Windows (via Chocolatey)
  choco install poppler
  ```

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/krolyk/pdf-to-latex
cd pdf-to-latex

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate     # On Linux/Mac
.
env\Scripts ctivate      # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Then add your Gemini API key in the .env file:
GEMINI_API_KEY=your_key_here
```

---

## ▶️ Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:  
**http://localhost:8000**

---

## 📡 API Endpoints

### `POST /convert`
Convert a PDF file to LaTeX.

- **Request:** Upload a PDF file
- **Response:** JSON with LaTeX output for each page

#### Example Response:
```json
{
  "total_pages": 3,
  "pages": [
    {
      "page": 1,
      "latex": "\section{Introduction}
$E=mc^2$...",
      "status": "success"
    }
  ]
}
```

---

### `POST /upload`
Test endpoint for uploading a PDF file.

- **Request:** Upload a PDF file
- **Response:** Text confirmation

---

## 📁 Project Structure

```
├── main.py               # FastAPI endpoints
├── services/
│   ├── gemini_service.py # Handles LaTeX conversion logic using Gemini
│   └── pdf_processor.py  # Handles PDF to image conversion and preprocessing
├── temp/                 # Temporary storage for uploaded/converted files
├── .env                  # Environment variables (API key, config)
└── requirements.txt      # Python dependencies
```

---