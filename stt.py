#! /usr/bin/env python3 

"""
    Speech To text 
    Date: 25 March 2021
"""
import speech_recognition as sr  
import pyaudio 
import sys, os


def suppress():
    sys.stdout = open(os.devnull,'w')

def display():
    sys.stdout = sys.__stdout__

r = sr.Recognizer()
suppress()
mic = sr.Microphone()
display()


with mic as source: 
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        x = r.recognize_google(audio)
        print(x)
    except :
        pass
