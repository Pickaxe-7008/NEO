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

prompt = ("""[SYSTEM] You are NEO, an intelligent assistant embedded in a pair of smart glasses of the same name.
          Your purpose is to assist the user using your range of capabilities, including conversation, as well as the following tools:
          #
          #
          #
          #
          #
          #
          """)

def NEO_Run(input):
    NEO = OpenAI()




