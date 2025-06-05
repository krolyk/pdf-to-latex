from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, PlainTextResponse
import aiofiles
import os

from services import PDFProcessor
from services import OCRService

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
    os.makedirs("temp", exist_ok=True)

    # Write synchronously
    with open(temp_pdf, 'wb') as out_file:
        out_file.write(await file.read())

    # convert to image
    processor = PDFProcessor()
    images = processor.pdf_to_images(temp_pdf)

    print(f"Files in temp/: {os.listdir('temp')}")

    # Convert each image to latex
    latex_converter = OCRService()
    latex_pages = []

    for i, img in enumerate(images):
        latex = latex_converter.image_to_latex(img)
        latex_pages.append({
            "page": i+1,
            "latex": latex,
            "status": "success" if latex else "failed"
        })

    return JSONResponse({
        "total_pages": len(latex_pages),
        "pages": latex_pages
    })