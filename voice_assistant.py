import os
import getpass
import smtplib
import requests
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import time
import threading
import wikipedia
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() #This is optional

# Initialize text-to-speech engine
engine = pyttsx3.init()

def set_voice(voice_name=""):
    voices = engine.getProperty('voices')
    for voice in voices:
        if voice_name in voice.name:
            engine.setProperty('voice', voice.id)
            break

# List available voices
def list_voices():
    voices = engine.getProperty('voices')
    for voice in voices:
        print(f"Voice: {voice.name}, ID: {voice.id}")


list_voices()

# uncomment the below command to get female assistant (e.g., "Zira" for a female voice on Windows)
#set_voice("Zira")  # Change "Zira" to the desired female voice name from the list

# Function to speak out the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print("User said:", query)
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that. Can you please repeat?")
            return listen()
        except sr.RequestError as e:
            speak("Sorry, I couldn't process your request. Please try again later.")
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

# Function to perform tasks based on user's voice command
def perform_task(query):
    if "hello" in query:
        speak("Hello! How can I assist you today?")
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)
        speak("How can i assist u further.....if nothing please say goodbye to exit")
    elif "date" in query:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak("Today's date is " + current_date)
        speak("How can i assist u further.....if nothing please say goodbye to exit")
    elif "search" in query:
        speak("What would you like me to search for?")
        search_query = listen()
        if search_query:
            url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
            webbrowser.open(url)
            speak("Here are the search results for " + search_query)
        
        speak("How can i assist u further.....if nothing please say goodbye to exit")
    elif "email" in query:
        send_email()
        speak("How can i assist u further.....if nothing please say goodbye to exit")
    elif "weather" in query:
        get_weather()
        speak("How can i assist u further.....if nothing please say goodbye to exit")
    elif "reminder" in query:
        set_reminder()
        speak("How can i assist u further.....if nothing please say goodbye to exit")
    elif "answer" in query:
        answer_question()
        speak("How can i assist u further.....if nothing please say goodbye to exit")

    elif "goodbye" in query:
        speak("Ok goodbye! have a nice day! ")
        exit()

# Function to send an email
def send_email():
    Host = "smtp.gmail.com"  # Corrected the typo in the hostname for gmail
  # Host = "smtp-mail.outlook.com" # for outlook/Hotmail
  # Host = "smtp.mail.yahoo.com" # For Yahoo
  # Host = "smtp.office365.com"  # For Office 365
  
 
    port = 587
    FROM_EMAIL = "USER_EMAIL"
    TO_EMAIL = "RECEPTION_EMAIL"  # Email address of the recipient
    PASSWORD = "USER_PASS"    # USER_EMAIL password, better use an app password

    MESSAGE = """Subject: Mail sent by project
    Message from voice assistant
    THIS IS JUST A TEST MESSAGE
    """
    try:
        # Initialize connection to the server
        smtp = smtplib.SMTP(Host, port)

        # Echo the server response
        status_code, response = smtp.ehlo()
        print(f"[*] Echoing the server: {status_code} {response}")

        # Start TLS connection
        status_code, response = smtp.starttls()
        print(f"[*] Starting TLS connection: {status_code} {response}")

        # Log in to the server
        status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
        print(f"[*] Logging in: {status_code} {response}")

        # Send the email
        smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
        
    except Exception as e:
        speak("some error has been occured as shown in the terminal !")
        print(f"Error is : {e}")
    finally:
        # Quit the connection
        smtp.quit()
        speak("Process over! How can i assist u more?")

    

# Function to get the weather
def get_weather():
    API_key = "WEATHER_API_KEY"

    speak("Please provide the city name")
    cityName = listen()

    completeURL = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={API_key}"

    response = requests.get(completeURL)
    data = response.json()

    if response.status_code == 200:
        kelvin_temp = data['main']['temp']
        celsius_temp = kelvin_temp - 273.15
        weather_desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Weather in {cityName}:")
        print(f"Temperature: {celsius_temp:.2f}°C")
        print(f"Weather: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

        speak(f"Weather in {cityName}:")
        speak(f"Temperature: {celsius_temp:.2f} degrees Celsius")
        speak(f"Weather: {weather_desc}")
        speak(f"Humidity: {humidity}%")
        speak(f"Wind Speed: {wind_speed} meters per second")
    else:
        speak("Some error has occurred as shown in the terminal!")
        print(f"Error: {data['message']}")

        
# Function to set a reminder

def set_reminder():
    speak("provide reminder message")
    reminder_message = listen()

    if reminder_message:  # Check if a valid reminder message was received
        speak("Enter delay in seconds")
        try:
            delay = int(input("Enter delay in sec: "))
            speak(f"Reminder set for {delay} seconds. Please wait...")
            time.sleep(delay)  # Wait for the specified delay
            speak(f"Reminder: {reminder_message}")
        except ValueError:
            speak("Sorry, I couldn't understand the delay time.")
    else:
        speak("No reminder message received. Exiting.")




# Function to answer a general knowledge question
def answer_question():
    speak("What do you want to know?")
    question = listen()
    speak("Let me find the answer for you.")
    try:
        result = wikipedia.summary(question, sentences=1)
        speak("According to Wikipedia, " + result.split('.')[0] + ".")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any information about that.")
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results for that query. Can you please be more specific?")
    except Exception as e:
        speak("Sorry, I encountered an error while processing your request.")

# Main function to continuously listen for commands
def main():
    speak("Hello! I'm your advanced voice assistant. How can I assist you today?")
    while True:
        query = listen()
        if query:
            perform_task(query)

if __name__ == "__main__":
    main()
