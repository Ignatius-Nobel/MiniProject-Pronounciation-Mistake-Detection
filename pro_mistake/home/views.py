from django.shortcuts import render,redirect
from django.http import HttpResponse
import speech_recognition as sr
import g2p_en
import pyttsx3
import re


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    engine.say(text)
    engine.runAndWait()


def get_phonetics(word):
    with open("cmudict-0.7b.txt", "r") as f:
        for line in f:
            if line.startswith(word.upper()):
                return ' '.join(re.findall(r"\d*\w+", line)[1:])

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def word(request):
    return render(request,'word.html')
def voice(request):
    return render(request,'speech.html')



# def process_input(request):
    
#     user_input = request.POST.get('user_input', '')  # Retrieve the value of the 'user_input' field
#         # Your code logic here
#     print(f"usr_inp={user_input}")
#     return render(request, 'result.html', {'user_input': user_input})
    #return user_input


    





        
def speech(request):
    if request.method == 'POST':
            user_input = request.POST.get('user_input')
    phonetics = get_phonetics(user_input)
    #print(f"phonetics={phonetics}")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Speak something!")
        audio = r.listen(source)

    try:
        
        transcription = r.recognize_google(audio)
        g2p = g2p_en.G2p()
        phonemes = g2p(transcription)
        phonemes_joined = (' '.join(phonemes))
        #print("phonemes=",' '.join(phonemes))
        
        if phonemes_joined == phonetics:
            return render(request,'result_crct.html')
        else:
            return render(request,'result_wrg.html')
            #text_to_speech(correct_pronunciation_is)
            #text_to_speech(word1)
    except sr.UnknownValueError:
        return HttpResponse("Cannot Understand...")
    except sr.RequestError:
        return HttpResponse("Service not available...")


def next_page(request):
    # Your code logic here
    # This function will handle the button click and redirect to the next page
    return redirect('next_page_url')