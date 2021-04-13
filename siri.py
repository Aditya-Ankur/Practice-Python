import pyttsx3 as pt
import datetime as dt

engine = pt.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)

def speak(audio):
    '''This will speak whatever the text the user wants'''
    engine.say(audio) 
    engine.runAndWait()

def wishMe(): 
    '''This will wish the user'''
    time_hour = int(dt.datetime.now().hour)
    
    if time_hour < 12 and time_hour >= 0:
        speak('Good Morning')
    elif time_hour >= 12 and time_hour < 16:
        speak('Good Afternoon')
    elif time_hour >= 16 and time_hour < 20:
        speak('Good Evening')
    else:
        speak('Good Night')

    speak('Hello I am Siri.')

if __name__ == "__main__":
    wishMe()

