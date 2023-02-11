import openai

# Replace the API key with your own
openai.api_key = "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"

def assistant(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Test the function with a voice input
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    response = assistant(text)
    print("You said: " + text)
    print("Assistant: " + response)
except:
    print("Sorry, I didn't understand what you said.")
