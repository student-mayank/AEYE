import hugging_face as hf
import google.generativeai as genai
import os 
import imgInput as imgI
import pyttsx3
import speech_recognition as sr
import streamlit as st
from dotenv import *
load_dotenv(find_dotenv())

#voice command
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)    
        print("Unable to Recognize your voice.")  
        return "None"
     
    return query

def geminiRes(text):
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content("explain in brief" + text)
    print(response.text)
    return response.text




def voiceCommand():
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    
    speak("Good morning, What is your command")
    while True:
         
        query = takeCommand().lower()
        
        print(query)
        if 'say hello' in query:
            speak("Say Hello, exiting")    
        elif 'explain image' in query:
            imgI.imgInput()
            speak(hf.Img2Text("img.png"))
        elif 'who is this person' in query:
            print("Face Recognition")
        else :
            print("Gemini")
            speak(geminiRes(query))
            
            # print(query)



