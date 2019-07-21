import speech_recognition as sr
import os
from gtts import gTTS

tts_en=gTTS('hello',lang='en')
tts_gu=gTTS('morning',lang='gu')

with open('testing.mp3','wb') as f:
    tts_en.write_to_fp(f)
    tts_gu.write_to_fp(p)