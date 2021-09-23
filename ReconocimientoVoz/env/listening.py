import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as sources:
    print("Habla algo:")
    audio = r.listen(sources)

    try:
        texto = r.recognize_google_cloud(audio)

        print("Dijiste: {}", format(texto))
    except:
        print("no te pude entender")