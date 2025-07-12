from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router

app = FastAPI()
app.include_router(router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify e.g. ["http://localhost:8080"]
    allow_methods=["*"],
    allow_headers=["*"],
)