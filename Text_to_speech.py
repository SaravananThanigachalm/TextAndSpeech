import os
from gtts import gTTS

textFile = open("TextToSpeech.txt", "r")
myText = textFile.read().replace("\n"," ")

language = 'en'

speech = gTTS(text=myText, lang = language, slow = False)

textFile.close()

speech.save("TextToSpeech.mp3")
os.system("start TextToSpeech.mp3")