

# Advanced Voice Assistant

This project is an advanced voice assistant capable of performing various tasks such as greeting the user, telling the time and date, searching the web, sending emails, providing weather updates, setting reminders, and answering general knowledge questions using Wikipedia.

## Features

1. **Greeting**
   - Greets the user when they say "hello".
   
2. **Time**
   - Tells the current time when asked.

3. **Date**
   - Tells the current date when asked.

4. **Web Search**
   - Searches the web for a user-provided query.

5. **Email**
   - Sends an email to a specified recipient.

6. **Weather**
   - Provides the current weather information for a user-specified city.

7. **Reminder**
   - Sets a reminder with a user-specified message and delay.

8. **General Knowledge**
   - Answers general knowledge questions using Wikipedia.

## Installation

### Prerequisites

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/installation/)

### Libraries

Install the required libraries using the following command:
```bash
pip install pyttsx3 SpeechRecognition wikipedia requests python-dotenv
```

### Environment Variables

Create a `.env` file(This is optional) in the root directory of the project and add your email credentials and OpenWeatherMap API key:
```
EMAIL_USER=your-email@example.com
EMAIL_PASS=your-email-password
RECEPTION_EMAIL=recepiant-email@example.com
WEATHER_API_KEY=your-openweathermap-api-key
```

## Usage

### Running the Assistant

Run the `voice_assistant.py` file to start the voice assistant:
```bash
python voice_assistant.py
```

### Voice Commands

1. **Greeting**
   - Say "hello" to receive a greeting from the assistant.

2. **Time**
   - Ask "What is the time?" to get the current time.

3. **Date**
   - Ask "What is the date?" to get the current date.

4. **Web Search**
   - Say "search" followed by your query to search the web.

5. **Email**
   - Say "email" to send an email.

6. **Weather**
   - Say "weather" and provide a city name to get the weather information.

7. **Reminder**
   - Say "reminder" and provide a message and delay time to set a reminder.

8. **General Knowledge**
   - Ask a question starting with "answer" to get an answer from Wikipedia.

9. **Goodbye**
   - Say "goodbye" to exit the assistant.

## Code Overview

### main.py

The main script contains the following functions:

- `set_voice(voice_name)`: Sets the voice of the assistant.
- `list_voices()`: Lists available voices.
- `speak(text)`: Speaks out the given text.
- `listen()`: Listens for speech input and returns the recognized text.
- `perform_task(query)`: Performs tasks based on the user's voice command.
- `send_email()`: Sends an email using the provided credentials.
- `get_weather()`: Fetches and speaks the weather information for a specified city.
- `set_reminder()`: Sets a reminder with a specified message and delay.
- `answer_question()`: Answers general knowledge questions using Wikipedia.
- `main()`: Continuously listens for commands and performs tasks.



## Acknowledgments


- The [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/) library is used for text-to-speech conversion.
- [OpenWeatherMap](https://openweathermap.org/) API is used for fetching weather information.
- The [Wikipedia](https://pypi.org/project/wikipedia/) library is used for answering general knowledge questions.

---

