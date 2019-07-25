import speech_recognition as sr
import os
from gtts import gTTS
r = sr.Recognizer()
# welcome="Te tamne joi rahyo che"
welcome="Tē tamanē jō'ī rahyō chē"
# welcome="સુપ્રભાત"
tts0=gTTS(welcome,lang='hi')
tts0.save('welcome.mp3')
os.system("welcome.mp3")

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    os.system("welcome.mp3")
    audio = r.listen(source)


# check=r.recognize_google(audio)
# print(check)
# # check="Hello Nitasha Gupta. Good morning!"
# tts=gTTS("Did you say "+check,lang='en')
# tts.save("speech.mp3")
# os.system("speech.mp3")

