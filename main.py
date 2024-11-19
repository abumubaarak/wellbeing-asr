from datetime import datetime
from pydantic import BaseModel
import instructor
from openai import OpenAI
import wave
from faster_whisper import WhisperModel
from fastapi import FastAPI,WebSocket,Request

from BaseResponse import Analysis

client = instructor.from_openai(OpenAI(
  organization='org-1RKpzvEArSyvC6mFuTq5daAA',
  project='proj_8EJ9RzVQ22rJnaGb1hNYgUYW',
  
  api_key="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"
))

class Symptoms(BaseModel):
    symptoms:str


app = FastAPI()
model_size = "distil-small.en"

files= []

# Run on GPU with FP16
model = WhisperModel(model_size,device="cpu", compute_type="float32")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/analyseSymptoms")
def analyseSymptoms(request:Symptoms):
    stream = client.chat.completions.create(
    model="gpt-4o",

    messages=[
        {"role": "system", "content": "Do not provide any non-medical advice or unrelated information."},
        {"role": "system", "content": "You are a medical expert providing detailed analyses of symptoms. Your responses should focus solely on medical information, including diagnosis explanations, potential conditions, and medication recommendations. Avoid providing non-medical advice or general information.  If the symptoms is not a valid MEDICAL SYMPTOMS return invalid"},
        {"role": "user", "content":request.symptoms +" .Based on this, provide a well-detailed diagnosis of the most likely illness and explain why in detail start by giving the Introduction(Briefly summarize the symptoms),Diagnosis Explanation(Discuss the most likely illness, why it fits the symptoms.) without adding heading or section or consideration or giving the next action In 102 words. Also, give the top 3 possible illnesses with confidence percentages(100% maximum) without numbering or heading but in a new line. Recommend 3 medications with purpose, with dosages, typically used to treat it."}],

     response_model=Analysis
    
     
     
)
    print(request.symptoms)
    print(stream)
    return stream


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        fileName = str(int(datetime.now().timestamp())) +'.wav'
        data = await websocket.receive_bytes()
        with wave.open(fileName, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(16000)
            wf.writeframes(data)
            files.append(fileName)
        segments, info = model.transcribe(fileName, beam_size=10,temperature=0)
        for segment in segments:
            await websocket.send_text(segment.text)                