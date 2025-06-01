from pdf2image import convert_from_path
from PIL import Image
import os

class PDFProcessor:
    def __init__(self, temp_dir="temp"):
        self.temp_dir = temp_dir
        os.makedirs(temp_dir, exist_ok=True)
        
    def pdf_to_images(self, pdf_path: str) -> list[Image.Image]:
        try:
            images = convert_from_path(pdf_path)
            for i, img in enumerate(images):
                img.save(f"temp/page_{i}.png")
            return images
        except Exception as e:
            print(f"PDF conversion error: {e}")
            return []