import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get absolute path to marks.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MARKS_FILE = os.path.join(BASE_DIR, "marks.json")

# Load marks data
with open(MARKS_FILE, "r") as file:
    student_marks = {entry["name"]: entry["marks"] for entry in json.load(file)}

@app.get("/api")
async def get_marks(name: list[str] = []):
    marks = [student_marks.get(n, None) for n in name]
    return {"marks": marks}
