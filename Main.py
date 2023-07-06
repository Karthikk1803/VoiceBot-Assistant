if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()
     
    while True:
         
        query = takeCommand().lower()
         
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("https://www.youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("https://www.google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("https://www.stackoverflow.com")  
 
        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")  
            speak(f"Sir, the time is {strTime}")
 
        elif 'email to gaurav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"  
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()  
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
 
        elif 'exit' in query:
            print("Thanks for giving me your time")
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Humans.")
             
        elif 'joke' in query:
            x=pyjokes.get_joke()
            print(x)
            speak(x)
 
        elif 'search' in query or 'Tell me about' in query:
             
            query = query.replace("search", "")
            query = query.replace("Tell me about", "")        
            webbrowser.open(query)

        elif "who am i" in query:
            speak("If you talk then definitely your human.")
 
        elif "what's ur purpose" in query:
            speak("It is to help people")
 
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by Gaurav")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Gaurav ")
 
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
            speak("Background changed successfully")
 
        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)
 
        elif 'news' in query:
            print("Opening Times of India")
            speak("Opening Times of India")
            URL = "https://timesofindia.indiatimes.com/?from=mdr"
            webbrowser.open(URL)
 
         
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call(["shutdown", "/s", "/t", "3"])
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/search/+"+location)
 
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r", "/t", "3"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call(["shutdown", "/h"])
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
 
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('friday.txt', 'w')
            file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("friday.txt", "r")
            print(file.read())
            speak(file.read(6))
 
        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)
             
            with open("VoiceBot.py", "wb") as Pypdf:
                 
                total_length = int(r.headers.get('content-length'))
                 
                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                    if ch:
                      Pypdf.write(ch)
                     
        elif "friday" in query:
             
            wishMe()
            speak("friday in your service Mister")
            speak(assname)
 
        elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)
 
                message = client.messages \
                                .create(
                                    body = takeCommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )
 
                print(message.sid)
 
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
 
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(assname)
 
        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about that, may be you should give me some time")
 
        elif "how are you" in query:
            speak("I'm fine, glad you asked me that")
 
        elif "i love you" in query:
            speak("It's hard to understand")
 
        elif "what is" in query :
             
            import webbrowser
            user_query = query.replace("what is", "")
            speak("Searching Google for the result")
            URL = "https://www.google.com/search?q=" + user_query
            webbrowser.open(URL)

        elif query in ("open microsoft powerpoint", "open powerpoint"):   
            speak("opening powerpoint")
            print("opening powerpoint ")
            os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk')

        elif query in ("open microsoft word", "open word"):   
            speak("opening Word")
            print("opening Word")
            os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk')

        elif "who is" in query:
            import webbrowser
            user_query = query.replace("who is", "")
            print("Searching Google for the result")
            speak("Searching Google for the result")
            URL = "https://www.google.com/search?q=" + user_query
            webbrowser.open(URL)

        elif "play" in query:
            import webbrowser
            user_query = query.replace("play", "")
            print("Searching Youtube for the result")
            speak("Searching Youtube for the result")
            URL = "https://www.youtube.com/results?search_query=" + user_query
            webbrowser.open(URL)

        elif "close" in query or "goodbye" in query:
            print("It was a great experience with you ,thank you!! ")
            speak("It was a great experience with you thank you!! ")
            print("Please come back!!")
            exit()
