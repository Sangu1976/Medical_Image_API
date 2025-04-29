# Medical_Image_API
Simple REST API for managing medical imaging metadata built with FastAPI

# Medical Image Metadata REST API

This is a simple RESTful API built using **FastAPI** that simulates a basic medical image management system.

## Features

- Add new medical image metadata (filename, size, modality).
- Retrieve all stored medical images.
- Retrieve specific medical images by filename.
- Automatically generated API documentation with Swagger UI.

## Technologies Used

- Python 3.12
- FastAPI
- Uvicorn

## How to Run

1. Clone the repository or download the project files.
2. Install dependencies:

```bash
pip install fastapi uvicorn

## Run the Server

uvicorn main:app --reload

## Open your browser and navigate to:

API Home: http://127.0.0.1:8000

API Documentation (Swagger UI): http://127.0.0.1:8000/docs

Example Usage
POST /images/ — Add a new medical image.

GET /images/ — List all stored images.

GET /images/{filename} — Retrieve an image by filename.

Author
Sangeetha Joseph
