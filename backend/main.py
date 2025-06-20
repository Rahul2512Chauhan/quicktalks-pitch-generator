# FastAPI app + API routes
from fastapi import FastAPI
from pydantic import BaseModel
from generator import generate_all_outputs
app = FastAPI()

class InputData(BaseModel):
    title: str
    description :str
    keywords:str = ""

@app.post("/generate")
def generate_all_outputs_endpoint(data: InputData):
    return generate_all_outputs(
        data.title,
        data.description,
        data.keywords
    )