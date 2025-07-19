import base64
from openai import OpenAI
import os
import platform
import json

API_KEY = ""

os.environ['OPENAI_API_KEY'] = API_KEY
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')



prompt = ("""You are NEO, a virtual assistant for the smart glasses of the same name.
          You""")