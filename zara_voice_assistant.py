import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)

is_playing = False  # Flag to track YouTube playback

def engine_talk(text):
    """Convert text to speech"""
    print(f"Zara is saying: {text}")
    engine.say(text)
    engine.runAndWait()

def user_commands():
    """Listen to user commands and return the command text"""
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("Start Speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            if 'zara' in command:
                command = command.replace('zara', '').strip()
                print(f"User said: {command}")
                return command
    except Exception as e:
        print(f"Error: {e}")
        return ""

def run_zara():
    """Main assistant logic"""
    global is_playing

    if is_playing:
        return

    command = user_commands()
    if command:
        if 'play' in command:
            song = command.replace('play', '').strip()
            engine_talk('Playing ' + song)
            pywhatkit.playonyt(song)
            is_playing = True

        elif 'time' in command:
            time_now = datetime.datetime.now().strftime('%I:%M %p')
            engine_talk('The current time is ' + time_now)

        elif 'who is' in command:
            name = command.replace('who is', '').strip()
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)

        elif 'joke' in command:
            engine_talk(pyjokes.get_joke())

        elif 'stop' in command:
            engine_talk("Goodbye!")
            sys.exit()

        else:
            engine_talk('I could not hear you properly')
    else:
        engine_talk('I did not catch that. Please speak again.')

# Run Zara
while True:
    run_zara()
