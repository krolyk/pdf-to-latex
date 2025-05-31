from paddleocr import PaddleOCR
import numpy as np

class OCRService:
    def __init__(self):
        self.ocr = PaddleOCR(lang='en')

    def extract_text(self, image) -> str:
        # convert PIL image to numpy array
        img_np = np.array(image)
        try:
            result = self.ocr.ocr(img_np)

            text = ""
            if result is not None:
                for line in result[0] if result[0] else []:
                    if line and line[1]:
                        text += line[1][0] + "\n"
            return text.strip()
        
        except Exception as e:
            print(f"OCR Error: {e}")
            return ""