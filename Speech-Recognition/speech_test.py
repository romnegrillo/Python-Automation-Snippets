import speech_recognition as sr

r = sr.Recognizer()

input("Press enter.")

with sr.Microphone(device_index = 0) as source:

    try:
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)

        input("Press enter.")
        text = r.recognize_google(audio)
        print(text)
        
    except:
        print("Sorry cannot recognize your voice.")

