 # Streamlit UI
import streamlit as st
import requests

st.title("🎤 QuickTalks – AI Elevator Pitch Generator")

title = st.text_input("Project Title")
description = st.text_area("Short Description")
keywords = st.text_input("Keywords (optonal)")

if st.button("Generate Pitch"):
    with st.spinner("Generating...."):
        res = requests.post(
            "http://localhost:8000/generate/",
            json = {"title":title , "description":description , "keywords":keywords}
        )

        data = res.json()
        st.subheader("🔹 30-second Pitch")
        st.write(data["pitch-30"])

        st.subheader("🔸 1-minute Version")
        st.write(data["pitch_60"])
        st.subheader("✅ Resume Bullet Points")
        for bullet in data["resume_bullets"]:
            st.markdown(f"-{bullet}")

