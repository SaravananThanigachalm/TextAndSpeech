import speech_recognition as sr

Audio_File = ("SpeechToText.wav")

r = sr.Recognizer()

with sr.AudioFile(Audio_File) as s:
    audio = r.record(s)

myFile = open("SpeechToText.txt", "w")

try:
    print(r.recognize_google(audio), file= myFile)
    myFile.close()
except sr.UnknownValueError:
    print("Google speech could not understant the speech file")
except sr.RequestError:
    print("Couldn't get results from Google Speech Recognition")