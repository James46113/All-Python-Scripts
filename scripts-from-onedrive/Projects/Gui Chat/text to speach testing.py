import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 135)
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.say("meu amor por você é como uma atualização do windows - sem fim")
    engine.runAndWait()
engine.stop()
