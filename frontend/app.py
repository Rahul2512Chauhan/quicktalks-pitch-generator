import streamlit as st
import requests
import pyttsx3

# ------------------ Config ------------------
st.set_page_config(page_title="QuickTalks – Pitch Generator", layout="centered")
st.title("🎤 QuickTalks – AI Elevator Pitch Generator")
st.markdown("Generate professional pitch scripts and resume points from your projects in seconds.")

# ------------------ Session State Init ------------------
if "pitch_data" not in st.session_state:
    st.session_state.pitch_data = None

# ------------------ User Input ------------------
with st.container():
    st.markdown("🧠 Input Your Project Info")
    title = st.text_input("📌 Project Title")
    description = st.text_area("📝 Short Description or Resume Bullet")
    keywords = st.text_input("🏷️ Keywords (optional)")

    if st.button("🚀 Generate Pitch"):
        with st.spinner("Thinking hard... 🤖"):
            res = requests.post(
                "http://localhost:8000/generate",
                json={"title": title, "description": description, "keywords": keywords}
            )
            st.session_state.pitch_data = res.json()

# ------------------ Output Display ------------------
data = st.session_state.pitch_data
if data:
    st.divider()
    st.markdown("🎯 Generated Outputs")

    # 30-second Pitch
    with st.container():
        st.markdown("🔹 30-second Pitch")
        st.success(data["pitch_30"])

        col1, col2 = st.columns(2)
        with col1:
            if st.button("▶️ Play 30s Pitch"):
                engine = pyttsx3.init()
                engine.setProperty('rate', 160)
                engine.setProperty('volume', 1)
                engine.say(data["pitch_30"])
                engine.runAndWait()

        with col2:
            st.code(data["pitch_30"], language="text")

    # 1-minute Pitch
    with st.container():
        st.markdown("🔸 1-minute Interview Version")
        st.info(data["pitch_60"])

        col1, col2 = st.columns(2)
        with col1:
            if st.button("▶️ Play 1-Min Pitch"):
                engine = pyttsx3.init()
                engine.setProperty('rate', 160)
                engine.setProperty('volume', 1)
                engine.say(data["pitch_60"])
                engine.runAndWait()

        with col2:
            st.code(data["pitch_60"], language="text")

    # Resume Bullets
    with st.container():
        st.markdown("✅ Resume Bullet Points")
        for i, bullet in enumerate(data["resume_bullets"], 1):
            st.markdown(f"**{i}.** {bullet}")

    st.divider()
