import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("Guess The Number")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said:{query}\n')

    except Exception:
        # print(e)
        print('Say that again')
        return 'none'
    return query

# number = takecommand().lower()

n=random.randint(1,100)
guess=1
speak('Guess a number from 1 to 100\n')
    
while (guess<10):
    number =(takecommand().lower())
    # if number == "xx":
    #     number=20
    # elif number == "xxxviii":
    #     number = 38
    a = int(number)
    print(a)
    a = int(a)
    if(a==n):
        print(f'Congratulations !!! You Won in {guess} Guesses')
        speak(f'Congratulations !!! You Won in {guess} Guesses')
        break
    elif (a>n):
        print('You Guessed Bigger Number')
        speak('You Guessed Bigger Number')
        
    else:
        print("You Guessed Smaller Number")
        speak("You Guessed Smaller Number")
       
    print(f"Number of Guesses Reamaining {11-(guess+1)}")
    speak(f"Number of Guesses Reamaining are {11-(guess+1)}")

    print("Guess The Number Again")
    speak("Guess The Number Again")

    guess = guess+1

if(guess==10):
    print("You ran out of chances")
    speak("You ran out of chances")

