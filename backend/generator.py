# Handles LLM logic (Zephyr or GPT-3.5)
import requests
from prompts import(
    get_30s_pitch_prompt,
    get_60s_pitch_prompt,
    get_resume_bullets_prompts
)

def query_zephyr_locally(prompt: str) -> str:
    """
    Query a locally running Zephyr model (via Ollama) and return the response.
    """
    payload = {
        "model": "zephyr",  # Make sure this matches your Ollama model name
        "prompt": prompt,
        "temperature": 0.7,
        "stream": False,
        "options": {
            "num_predict": 512
        }
    }

    try:
        res = requests.post("http://localhost:11434/api/generate", json=payload)
        res.raise_for_status()
        return res.json().get("response", "").strip()
    except requests.exceptions.RequestException as e:
        return f"[Error] Failed to connect to Zephyr: {e}"

def generate_all_outputs(title:str , description:str , keywords:str = "") -> dict:

    #Get prompts
    prompt_30 = get_30s_pitch_prompt(title , description , keywords)
    prompt_60 = get_60s_pitch_prompt(title , description , keywords)
    prompt_resume = get_resume_bullets_prompts(title , description , keywords)

    #Get model outputs
    pitch_30 = query_zephyr_locally(prompt_30)
    pitch_60 = query_zephyr_locally(prompt_60)
    resume_bullets_raw = query_zephyr_locally(prompt_resume)

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

