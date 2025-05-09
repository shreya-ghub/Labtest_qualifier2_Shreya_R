import os
import json
import parser
from utils import preprocess_image, ocr_image
from parser import parse_lab_report

folder_path = '/Users/shreyar/Downloads/lbmaske'
output_data=[]

#process each image
for filename in os.listdir(folder_path):
    if filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png','.jpg','.jpeg','.tiff','.bmp')):
         file_path = os.path.join(folder_path, filename )
         print(f"Processing {filename}...")

        try:
            img = preprocess_image(file_path)
            text = ocr_image(img)
            lab_data = parse_lab_report(text)

            output_data.append({
               "filename":filename,
               "is_success":True,
               "data": lab_data
            })   
        except Exception as e:
           output_data.append({
              "filename":filename,
               "is_success":False,
               "error": str[e]
           })
#saving to json
with open('bulk_output_json','w') as f:
   json.dump(output_data, f, indent=4)

print("All images successfully processed and saved to bulk_output.json")

