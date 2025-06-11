import speech_recognition as sr
import pyttsx3
import datetime
import wolframalpha
import webbrowser
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load secrets from .env file
load_dotenv()

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Function to speak text aloud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to convert speech to text
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return ""

# Function to tell current time
def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

# Ask WolframAlpha a question
def ask_wolframalpha(question):
    app_id = os.getenv("WOLFRAM_APP_ID")  # From .env
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    try:
        return next(res.results).text
    except StopIteration:
        return "Sorry, I couldn't find an answer."

# Open common websites by name
def open_website(website_name):
    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://www.github.com",
        "facebook": "https://www.facebook.com",
        "snapchat": "https://www.snapchat.com"
    }
    if website_name in websites:
        webbrowser.open(websites[website_name])
        speak(f"Opening {website_name}...")
    else:
        speak("Sorry, I don't know that website.")

# Secure SMS sender using Twilio
def send_text(contact, message):
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_AUTH")
    from_phone = os.getenv("TWILIO_PHONE")
    to_phone = f"+1{contact}"  # Ensure international format

    client = Client(account_sid, auth_token)
    msg = client.messages.create(
        body=message,
        from_=from_phone,
        to=to_phone
    )
    speak(f"Text sent to {contact}!")

# Main assistant loop
def run_assistant():
    speak("Hello, how can I help you today?")
    while True:
        command = listen()

        if "time" in command:
            tell_time()
        elif "what is" in command or "who is" in command:
            speak(ask_wolframalpha(command))
        elif "open" in command:
            if "youtube" in command:
                open_website("youtube")
            elif "google" in command:
                open_website("google")
            elif "github" in command:
                open_website("github")
            elif "facebook" in command:
                open_website("facebook")
            elif "snapchat" in command:
                open_website("snapchat")
            else:
                speak("Sorry, I can't open that website.")
        elif "text" in command:
            parts = command.split(":")
            if len(parts) == 2:
                contact = parts[0].replace("text", "").strip()
                message = parts[1].strip()
                send_text(contact, message)
            else:
                speak("Sorry, I couldn't understand the message format.")
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")

# Start assistant
if __name__ == "__main__":
    run_assistant()
