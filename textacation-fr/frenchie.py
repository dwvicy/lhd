# importing stuff
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import os


# Recognizer object
recog = sr.Recognizer()

# # microphone instance
mic = sr.Microphone()

# # audio from microphone
with mic as source:
    print("Speak your French now!")
    recog.adjust_for_ambient_noise(source, duration=0.2)
    audio = recog.listen(source)
    mytext = recog.recognize_google(audio)
    mytext = mytext.lower()


if 'bonjour' in mytext:
    translator = Translator()
    from_lang = 'en'
    to_lang = 'fr'

    with mic as source:
        print('qu\'est-ce que c\'est?')
        recog.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog.listen(source)
        lang = recog.recognize_google(audio)

        try:
            print('posez-moi une question, s\'il te plait en francaise!:' + lang)

            zetranslate = translator.translate(
                lang, src=from_lang, dest=to_lang)
            text = zetranslate.text
            zespeak = gTTS(text=text, lang=to_lang, slow=False)
            zespeak.save("textacation.mp3")
            os.system("afplay textacation.mp3")

        except sr.UnknownValueError:
            print("Wut did ya jus say? Sorry to trigger yo frenchie bo")

        except sr.RequestError as e:
            print("Am I audiadiadiable? itzzz 2020 oluvar agen")
