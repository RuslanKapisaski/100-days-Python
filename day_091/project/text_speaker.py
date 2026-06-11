from gtts import gTTS


def speak(text):
    try:
        print("Converting text to speech...")

        tts = gTTS(text=text, lang="bg")
        tts.save("audiobook.mp3")

        print("Audiobook saved as audiobook.mp3")

    except Exception as e:
        print(f"Error converting text to speech: {e}")