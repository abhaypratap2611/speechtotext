# Import the necessary libraries Rudra Pratap
import speech_recognition as sr  # Library for speech recognition
import pyttsx3  # Library for text-to-speech functionality
import os  # Library for interacting with the operating system
# Define the speech-to-text function
def speech_to_text():
    # Create a speech recognition object
    r = sr.Recognizer()

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Loop indefinitely until the user stops the program
    while True:
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            # Prompt the user to say something
            print("Please say something:")

            # Listen to the audio from the microphone
            audio = r.listen(source)

            try:
                # Convert the audio to text using Google Speech Recognition
                text = r.recognize_google(audio)

                # Print the recognized text
                print("You said: " + text)

                # Additional functionalities
                if "stop the program" in text.lower():
                    # Stop the program if the user says "stop the program"
                    print("Stopping the program.")
                    engine.say("Stopping the program.")
                    engine.runAndWait()
                    break
                elif "open google" in text.lower():
                    # Open Google if the user says "open google"
                    print("Opening Google.")
                    engine.say("Opening Google.")
                    engine.runAndWait()
                    os.system("start (link unavailable)")
                elif "open youtube" in text.lower():
                    # Open YouTube if the user says "open youtube"
                    print("Opening YouTube.")
                    engine.say("Opening YouTube.")
                    engine.runAndWait()
                    os.system("start (link unavailable)")

            except sr.UnknownValueError:
                # Handle the error if Google Speech Recognition could not understand the audio
                print("Google Speech Recognition could not understand your audio")
            except sr.RequestError as e:
                # Handle the error if there was a problem requesting results from Google Speech Recognition
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


# Call the speech-to-text function
speech_to_text()

















