import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit
import datetime
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak(text):
    try:
        engine = pyttsx3.init('sapi5')
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Error in speech:", e)

# Weather function
def get_weather(city="Pune"):
    api_key = os.getenv("WEATHER_API_KEY")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        res = requests.get(url)
        data = res.json()

        if res.status_code != 200:
            speak("Unable to fetch weather data")
            print(data)
            return

        temp = data['main']['temp']
        desc = data['weather'][0]['description']

        speak(f"The temperature in {city} is {temp} degree Celsius with {desc}")

    except Exception as e:
        print(e)
        speak("Something went wrong while fetching weather")

# Command processor
def process_command(command):
    command = command.lower().strip()
    print(f"Processing command: {command}")

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif command.startswith("play"):
        song = command.replace("play", "").strip()
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "time" in command:
        print("time block hit")
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")

    elif "date" in command:
        print("date block hit")
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    elif "weather" in command:
        speak("Fetching weather details")
        get_weather("Pune")

    elif "bye" in command or "stop" in command:
        speak("Goodbye!")
        return False

    else:
        speak("Sorry, I didn't understand that command.")

    return True


# Main
if __name__ == "__main__":
    speak("Initializing Alexa.....  How can I assist you?")
    

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                print("Listening...")
                audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")

                if not process_command(command):
                    break

            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that.")

            except sr.RequestError:
                speak("Network error. Please check your connection.")

    
        