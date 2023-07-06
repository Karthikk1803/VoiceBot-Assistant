engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 160)
engine.say('Voice Bot')
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
 
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
 
    else:
        speak("Good Evening Sir !")
 
    assname =("FRIDAY")
    speak("I am your Assistant")
    speak(assname)
     
def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("Welcome Mr.",uname)
     
    speak("How can i Help you, Sir")
 
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 0.5
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
 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your mail id', 'Password')
    server.sendmail('your mail id', to, content)
    server.close()
