#importing libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
#PyAudio
import pyjokes
import wikipedia
listener=sr.Recognizer()


def engine_talk(text):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def user_command():
    try:
        with sr.Microphone() as source:
            #listener.adjust_for_ambient_noise(source)
            print("Start Speaking: ")
            voice=listener.listen(source,20,3)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
            return command
    except:
        pass    
    
def run_alexa():
    command=user_command()
    if 'play' in command:
        song=command.replace('play','')
        engine_talk("playing"+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        engine_talk("The current time is "+time)
    elif 'who is' in command:
        engine_talk("looking for "+command)
        engine_talk('please wait....')
        name=command.replace('who is','')
        info=wikipedia.summary(name,1)
        engine_talk(info)
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke()) 
    elif 'date' in command:
        engine_talk('Sorry, I have an headache')
    elif 'are you single' in command:
        engine_talk('I am in relationship with internet')
    else:
        engine_talk("can not recognize you ! come again ")

#run_alexa()
    