import cv2
import pytesseract
from PIL import Image
import numpy as np

def preprocess_image(file_path):
    img = cv2.imread(file_path)

    #convertng images to grayscale for easy recognition
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #bilateral filtering for noise reduction while keeping edges
    gray = cv2.bilateralFilter(gray,11,17,17)

    #adaptive thresholding
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        15,12
    )

    return thresh
def ocr_image(image):
    config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
    text = pytesseract.image_to_string(image, config=config)
    return text