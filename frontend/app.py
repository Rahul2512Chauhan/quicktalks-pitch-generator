 # Streamlit UI
import streamlit as st
import requests
import pyttsx3

st.set_page_config(page_title="QuickTalks – Pitch Generator", layout="centered")
st.title("🎤 QuickTalks – AI Elevator Pitch Generator")

# Initialize session state to store data persistently
if "pitch_data" not in st.session_state:
    st.session_state.pitch_data = None

#user inputs
title = st.text_input("📌 Project Title")
description = st.text_area("📝 Short Description")
keywords = st.text_input("🏷️ Keywords (optonal)")


#generate pitch button
if st.button("Generate Pitch"):
    with st.spinner("Generating...."):
        res = requests.post(
            "http://localhost:8000/generate/",
            json = {"title":title , "description":description , "keywords":keywords}
        )
        st.session_state.pitch_data = res.json() #save to session state
        data = res.json()

# Show outputs if available
data = st.session_state.pitch_data
if data:
    st.subheader("🔹 30-second Pitch")
    st.write(data["pitch_30"])

    st.subheader("🔸 1-minute Version")
    st.write(data["pitch_60"])

    st.subheader("✅ Resume Bullet Points")
    for bullet in data["resume_bullets"]:
        st.markdown(f"- {bullet}")

# Text-to-speech function
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()

# Only show Play buttons after data exists
if data:
    st.markdown("🔊 Listen to Your Pitches")

    if st.button("▶️ Play 30s Pitch"):
        speak(data["pitch_30"])

    if st.button("▶️ Play 1-Min Pitch"):
        speak(data["pitch_60"])


