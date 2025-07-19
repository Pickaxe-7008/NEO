import base64
from openai import OpenAI
import os
import platform
import json
from commands import *
from SystemVariables import *

API_KEY = ""

os.environ['OPENAI_API_KEY'] = API_KEY


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def NEO_Run(inp):
    NEO = OpenAI()
    prompt = f"""[SYSTEM] You are NEO, an intelligent assistant embedded in a pair of smart glasses of the same name.
                 Current system information: volume: {volume} out of 1.0, battery: {battery} out of 100, HUD active: {HUD}. 
                 Current datetime: {time.strftime('%m/%d/%Y %I:%M:%S %p')}
                 Your purpose is to assist the user using your range of capabilities, including conversation, as well as the following tools:

              -increase_volume(amt) #Description: System volume will be increased by 'amt', volume is between 0.0 and 1.0.
              -decrease_volume(amt) #Description: System volume will be decreased by 'amt', volume is between 0.0 and 1.0.
              -HUD_on() #Description: HUD will be turned on.
              -HUD_off() #Description: HUD will be turned off.
              -take_picture() #Description: Takes picture.
              -speak(text) #Description: Speaks 'text' to the user. Can be used for conversational tasks.

              Here is the user's voice input: {inp}

              Based on the voice input and current system state, return one or more function calls to execute. If no function is needed, return only speak() with a response.
              Only respond with function calls like:
              speak("Sure, taking a picture now.")
              take_picture()

              DO NOT return explanations. Return only valid Python-style function calls.
              """


