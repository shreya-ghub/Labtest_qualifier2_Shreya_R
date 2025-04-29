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



