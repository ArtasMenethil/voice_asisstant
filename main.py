import pyttsx3
import speech_recognition as sr
import webbrowser
import pytesseract
import pyaudio
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
from PIL import Image
from pytesseract import image_to_string

text = image_to_string(Image.open('img/Flag.jpg'))

import speech_recognition as sr
record = sr.Recognizer()
s = 1
while s != 0:
    try:
        with sr.Microphone(device_index=0) as source:
            print("Speak")
            audio = record.listen(source)
            res = record.recognize_google(audio)
            res = res.lower()

            if res == "write file":
                f = open("text.txt", "w")
                f.write(text)
                f.close()
            elif res == "read file":
                f = open("text.txt", "r")
                z = f.read()
                print(z)
                f.close()
            elif res == "exit":
                s = 0

    except sr.UnknownValueError:
        print("Голос не распознан")
    except sr.RequestError:
        print("Что-то пошло не так")

else:
    quit()



