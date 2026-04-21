try:
    import paddlepaddle_gpu
    USE_GPU = True
except ImportError:
    USE_GPU = False

from paddleocr import PaddleOCR

ocr = PaddleOCR(use_gpu=USE_GPU)

result = ocr.ocr("test.png")

print(result)
