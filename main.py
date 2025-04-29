from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Data Model
class MedicalImage(BaseModel):
    filename: str
    size_kb: int
    modality: str  # Example: MRI, CT, X-Ray

# Simulated database
images_db: List[MedicalImage] = []

# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Medical Image Metadata API"}

# Add a new image
@app.post("/images/")
def add_image(image: MedicalImage):
    images_db.append(image)
    return {"message": "Image added successfully", "image": image}

# List all images
@app.get("/images/")
def list_images():
    return images_db

# Get a specific image by filename
@app.get("/images/{filename}")
def get_image(filename: str):
    for img in images_db:
        if img.filename == filename:
            return img
    return {"error": "Image not found"}
