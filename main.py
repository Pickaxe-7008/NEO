import commands
import NEO
import speech_recognition as sr


def get_command():
    #replace with whisper api later
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=5)
        try:
            query = r.recognize_google(audio, language="en-US")
        except:
            query = ""
    return query.lower()

def execute(inp):
    NEO.NEO_Run(inp)

def runner():
    listening = False
    counter = 0
    while True:
        command = get_command()
        print("command:" + command)
        if listening:
            if command != "":
                execute(command)
                listening = False
            else:
                counter += 1
                if counter == 5:
                    listening = False
        else:
            if command == "neo":
                listening = True

if __name__ == "__main__":
    runner()

