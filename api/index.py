import os
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get absolute path for marks.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MARKS_FILE = os.path.join(BASE_DIR, "marks.json")

# Debugging: Print file path
print(f"Loading marks from: {MARKS_FILE}")

# Load marks data
try:
    with open(MARKS_FILE, "r") as file:
        data = json.load(file)  # Load the JSON list
        student_marks = {entry["name"]: entry["marks"]
                         for entry in data}  # Convert list to dictionary
        print("Student marks loaded successfully!")  # Debugging
except Exception as e:
    print(f"Error loading marks.json: {e}")
    student_marks = {}


@app.get("/api")
async def get_marks(name: list[str] = Query([])):
    print(f"Received query: {name}")  # Debugging
    marks = [student_marks.get(n, None) for n in name]
    print(f"Returning marks: {marks}")  # Debugging
    return {"marks": marks}
