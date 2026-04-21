try:
    import paddlepaddle_gpu
    USE_GPU = True
except ImportError:
    USE_GPU = False

from paddleocr import PaddleOCR

if USE_GPU:
    ocr = PaddleOCR(use_gpu=USE_GPU)
else:
    ocr = PaddleOCR()

result = ocr.ocr("test.png")

print(result)
