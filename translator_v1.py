import os
import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
from langdetect import detect
from playsound import playsound
# playsound==1.2.2

r = sr.Recognizer()
translator = google_translator()

while True:
    with sr.Microphone() as src:
        print("Listening...")
        try:
            r.adjust_for_ambient_noise(src)
            audio = r.listen(src)
            speech_text = r.recognize_google(audio)  # strings what was listened
            getLanguage = detect(speech_text)  # detect language
            if translator.translate(speech_text, lang_tgt='en') == "exit":
                print("Closing Application")
                break
            print(f"{getLanguage}: {speech_text}")
        except KeyboardInterrupt:
            print("Application Finished")
            break
        except sr.UnknownValueError:
            print("Could not understand!")
        except sr.RequestError:
            print("Could not request translation from Google!")

        tlLanguage = 'ja'
        try:
            translated_text = translator.translate(speech_text, lang_tgt=tlLanguage)
            print(f"{tlLanguage}: {translated_text}")
            voice = gTTS(translated_text, lang=tlLanguage)
            voice.save("voice.mp3")
            playsound("voice.mp3")
            os.remove("voice.mp3")
        except NameError:
            print("Nothing listened...")
