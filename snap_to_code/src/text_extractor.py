from paddleocr import PaddleOCR

class TextExtractor:
    def extract_text(self, image_path: str) -> str:
        ocr = PaddleOCR(use_angle_cls=True, lang='en')

        # Perform OCR
        # image_path = "image.jpg"
        print(image_path)
        print(type(image_path))
        results = ocr.ocr(str(image_path))

        # Extract text
        # for result in results:

        extracted_text = "\n".join([line[1][0] for result in results for line in result])

        return extracted_text
