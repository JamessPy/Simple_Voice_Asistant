import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import time
import os # to remove created audio files
from PIL import Image
import pyautogui #screenshot
import pyttsx3
import urllib.request
from time import ctime
import json
class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
            time.sleep(5)
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(asis_obj.name + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    # 1: hello
    if there_exists(['hey','hello']):
        greetings = ["hey, how can I help you"]
        engine_speak(greetings)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):

        if person_obj.name:
            engine_speak(f"My name is {asis_obj.name}, {person_obj.name}") 
        else:
            engine_speak(f"My name is {asis_obj.name}. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember " + person_name)
        person_obj.setName(person_name)
    
    if there_exists(["what is my name"]):
        engine_speak("Your name must be " + person_obj.name)
    
    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name) 

    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    #date
    if there_exists(["what's the date"]):
        print(ctime())
        engine_speak(ctime())

    #google and youtube search
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")
    
    
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        search_term = search_term.replace("on youtube","").replace("search","")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")


    #ip information
    if there_exists(['get my ip information']):
        url = 'http://ipinfo.io/json'
        response = urllib.request.urlopen(url)
        data = json.load(response)

        IP=data['ip']
        org=data['org']
        city = data['city']
        country=data['country']
        region=data['region']

        print ('Your IP detail\n ')
        print ('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))
        engine_speak(f"Your IP address is {IP} and the country is {country} and the city is {city}")

    #weather
    if there_exists(["weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")

    #wikipedia search
    if there_exists(["what is the"]):
        search_term = voice_data.split("the")[-1]
        url=('https://en.wikipedia.org/wiki/'+search_term)
        webbrowser.get().open(url)
        engine_speak(f"Here is the what i found on wikipedia for {search_term}") 
     
    #calculator
    if there_exists(["plus","minus","multiply","divide","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply' or 'x':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")
        
     # screenshot
    if there_exists(["capture","my screen","screenshot"]):
        myScreenshot = pyautogui.screenshot()
        r = random.randint(1,10000)
        file = 'C:/Users/metoPy/Desktop/screenshoot/screen' + str(r) + '.png'
        myScreenshot.save(file)
        engine_speak("It's done ")
    
    
    # location
    if there_exists(["where am i"]):
        #webbrowser.open("https://www.google.nl / maps / place/" + location + "")
        url = 'http://ipinfo.io/json'
        response = urllib.request.urlopen(url)
        data = json.load(response)
        region=data['region']
        engine_speak(f"You must be somewhere in {region}")    
    
    if there_exists(["location"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per Google maps") 
    
   
    # exit
    if there_exists(["exit", "goodbye"]):
        engine_speak("bye")
        exit()

time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Alexsis'
person_obj.name = ""
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Recording") 
    print("Done")
    print("Speech to text:", voice_data)
    respond(voice_data) 