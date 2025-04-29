Lab Test OCR API

This is an FastAPI-based backend service that reads lab test results from uploaded medical report images through OCR (Optical Character Recognition). It scans the images, extracts text data through Tesseract OCR, and structures parsed lab test results from the text.

Features: 

Upload medical report images (e.g. PNG, JPEG).
Text extraction using OCR through Tesseract.
Smart parsing to identify lab test names, values, units, and reference ranges.
API response is structured and normalized data.

TechStack:
FastAPI - for building API
Tesseract OCR - text extraction from images
OpenCV - image preprocessing
Python- programming language

Sample outputs:

<img width="629" alt="Screenshot 2025-04-29 at 11 36 40 AM" src="https://github.com/user-attachments/assets/d3c0a47c-ee47-4712-8379-092906baf3d3" />
<img width="623" alt="Screenshot 2025-04-29 at 1 17 01 PM" src="https://github.com/user-attachments/assets/eda8497d-5651-43a7-9ae1-cbfb209123d7" />



