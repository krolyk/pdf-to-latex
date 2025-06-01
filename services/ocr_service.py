import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import io

load_dotenv()

class OCRService:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def image_to_latex(self, image) -> str:
        """Convert image to Latex"""
        try:
            debug_path = "temp/last_sent.png"
            image.save(debug_path)
            print(f"Debug image saved to {debug_path}")

            # Send to Gemini
            response = self.model.generate_content(
                [
                    "Convert this page to clean Latex. "
                    "Preserve:\n"
                    "- Mathematical equation (use $$)\n"
                    "- Diagrams (as tikz code)\n"
                    "- Text formatting (sections, bold/italic)\n"
                    "Return ONLY raw LaTeX code with no additional commentary.", 
                    image
                ],
                stream=True
            )
            response.resolve()
            return response.text.strip()
        
        except Exception as e:
            print(f"OCR Error: {type(e).__name__}: {str(e)}")
            return ""