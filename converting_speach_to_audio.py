"""
Speach  To Text Using Python's SpeechRecognition Library
"""

# Importing Libraries
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to speach to text
def speach_to_text():
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)

        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print("Text: " + text)
            return text
        except:
            text = "Sorry, I did not get that"
            print(text)
            return text