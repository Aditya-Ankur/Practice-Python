import pyttsx3

# This is the speaking API that will speak whatever you want

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
print(voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

# for voice in voices: 
#     # to get the info. about various voices in our PC  
#     print("Voice:") 
#     print("ID: %s" %voice.id) 
#     print("Name: %s" %voice.name) 
#     print("Age: %s" %voice.age) 
#     print("Gender: %s" %voice.gender) 
#     print("Languages Known: %s" %voice.languages) 

if __name__ == "__main__":
    speak("Hello World")
