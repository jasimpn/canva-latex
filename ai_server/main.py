API_KEY='qDsWgWWFE6gckXjSNs2fAj58IazPDx5T'
import base64
import os
from mistralai import Mistral

client = Mistral(api_key=API_KEY)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_path = "/home/jasim/Documents/ai_server/snip 2.jpg"
base64_image = encode_image(image_path)

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "image_url",
        "image_url": f"data:image/jpeg;base64,{base64_image}" 
    },
    include_image_base64=True
)
latex=ocr_response.pages[0].markdown


latex = latex.replace("$$", "").strip()
print(latex)
