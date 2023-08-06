from gtts import gTTS
import os

def text_to_speech(text, filename='output.mp3'):
    tts = gTTS(text)
    tts.save(filename)
    os.system(f'"{filename}"')

if __name__ == "__main__":
    input_text = input("Enter the text you want to convert to speech: ")
    text_to_speech(input_text)
