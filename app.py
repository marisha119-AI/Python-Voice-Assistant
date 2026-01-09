# ---------------- IMPORTS ----------------
import streamlit as st
from gtts import gTTS
from datetime import datetime
import tempfile
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Python Voice Assistant", layout="centered")

# ---------------- TITLE ----------------
st.title("🎙️ Python Voice Assistant (Mini Alexa)")
st.write("Type your command and the assistant will reply with voice.")

# ---------------- USER INPUT ----------------
user_input = st.text_input("Ask something:")

# ---------------- ASSISTANT LOGIC ----------------
def assistant_reply(command):
    command = command.lower()

    if "hello" in command or "hi" in command:
        return "Hello! How can I help you?"

    elif "time" in command:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

    elif "date" in command:
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}"

    elif "your name" in command:
        return "I am a Python Voice Assistant, your mini Alexa."

    elif "plus" in command:
        try:
            numbers = command.replace("plus", "+")
            result = eval(numbers)
            return f"The result is {result}"
        except:
            return "Sorry, I could not calculate that."

    elif "help" in command:
        return "You can ask about time, date, greetings, or simple calculations."

    else:
        return "Sorry, I did not understand that."

# ---------------- BUTTON ACTION ----------------
if st.button("Get Answer"):
    if user_input.strip() == "":
        st.warning("Please type something.")
    else:
        response = assistant_reply(user_input)
        st.success(response)

        # ---------- TEXT TO SPEECH (SAFE) ----------
        tts = gTTS(text=response, lang="en")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            audio_file = fp.name

        st.audio(audio_file, format="audio/mp3")

        # Cleanup temp file
        os.remove(audio_file)
# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("Developed by Marisha | Powered by Streamlit and gTTS")
# ---------------- IMPORTS ----------------
import streamlit as st
from gtts import gTTS

