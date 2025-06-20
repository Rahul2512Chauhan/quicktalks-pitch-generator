# FastAPI app + API routes
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    title: str
    description :str
    keywords:str = ""

@app.post("/generate")
def generate_outputs(data: InputData):
    return{
        "pitch_30": "30-seconds pitch placeholder",
        "pitch_60": "1-minute pitch placeholder",
        "resume_bullets": ["Bullet 1" , "Bullet 2"]
    }