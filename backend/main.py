from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="PDFNova API",
    description="PDFNova PDF Tools Backend",
    version="1.0.0"
)

# Temporary CORS configuration for initial testing.
# We will restrict this to your Blogger domain before production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to PDFNova API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "PDFNova Backend"
    }
