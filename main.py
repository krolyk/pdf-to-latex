from fastapi import FastAPI, UploadFile, File
from fastapi.responses import PlainTextResponse
import aiofiles
import os

from services.pdf_processor import PDFProcessor
from services.ocr_service import OCRService

app = FastAPI()

@app.post("/upload", response_class=PlainTextResponse)
async def upload_file(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    temp_path = "temp/uploaded.pdf"
    os.makedirs("temp", exist_ok=True)
    
    async with aiofiles.open(temp_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    
    return f"File {file.filename} saved successfully!"

@app.post("/convert")
async def convert_pdf(file: UploadFile = File(...)):
    # save uploaded file
    temp_pdf = "temp/uploaded.pdf"
    async with aiofiles.open(temp_pdf, 'wb') as out_file:
        await out_file.write(await file.read())

    # convert to image
    processor = PDFProcessor()
    images = processor.pdf_to_images(temp_pdf)

    # extract text from each image using OCR
    ocr = OCRService()
    extracted_texts = []
    for img in images:
        text = ocr.extract_text(img)
        extracted_texts.append(text)

    return {"message" : f"Converted {len(images)} pages",
            "text" : extracted_texts
            }