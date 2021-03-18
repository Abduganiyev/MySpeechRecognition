import speech_recognition as sr
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listen, speak everything...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        print("STOP")
    try:
        text = r.recognize_google(audio, language="ru-RU").lower()
        print("You said: " + text)
    except sr.UnknownValueError:
        print("не распознано")
        text = command()
    except sr.AttributeError::
        print("not recognized")
        text = command()
    except sr.TimeoutError:
        print("The attempt to establish a connection was unsuccessful.")
    return text
def makeSomething(command):
    if "прив" in command:
        print("Привет")
    elif "пока" in command:
        print("Пока")
    elif "hi" in command:
        print("hi")
    elif "hello" in command:
        print("hello")
    else:
        pass
 
while True:
    makeSomething(command())