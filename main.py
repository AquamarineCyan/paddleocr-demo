from paddleocr import PaddleOCR

ocr = PaddleOCR(use_gpu=True)

result = ocr.ocr("test.png")

print(result)