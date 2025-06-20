# Handles LLM logic (gemini-1.5-flash)
import google.generativeai as genai
import os
from dotenv import load_dotenv

from prompts import(
    get_30s_pitch_prompt,
    get_60s_pitch_prompt,
    get_resume_bullets_prompts
)

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

#configure gemini
genai.configure(api_key=api_key) # type: ignore
model = genai.GenerativeModel("gemini-1.5-flash") # type: ignore

def query_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Error from Gemini] {e}"


def generate_all_outputs(title:str , description:str , keywords:str = "") -> dict:

    #Get prompts
    prompt_30 = get_30s_pitch_prompt(title , description , keywords)
    prompt_60 = get_60s_pitch_prompt(title , description , keywords)
    prompt_resume = get_resume_bullets_prompts(title , description , keywords)

    #Get model outputs
    pitch_30 = query_gemini(prompt_30)
    pitch_60 = query_gemini(prompt_60)
    resume_bullets_raw = query_gemini(prompt_resume)

    #clean bullet point format
    bullets = [
        line.lstrip("-•").strip()
        for line in resume_bullets_raw.strip().split("\n")
        if line.strip()
    ]

    return {
        "pitch_30":pitch_30,
        "pitch_60":pitch_60,
        "resume_bullets":bullets

    }

