# Developed by uin0 © 2025
# Instagram: @uin0

import os
import openai
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("🤖:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        return "لم أفهم، أعد من فضلك."

def chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def main():
    speak("مرحباً، كيف أساعدك؟")
    while True:
        query = listen()
        if query.lower() in ["خروج", "أوقف", "انهاء", "exit", "stop"]:
            speak("مع السلامة!")
            break
        reply = chat(query)
        speak(reply)
        with open("log.txt", "a") as f:
            f.write(f"User: {query}
Assistant: {reply}

")

if __name__ == "__main__":
    main()
