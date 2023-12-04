"""
App main file. 
This is the execution point of the project.

Run it using:
python app/main.py
"""
from fastapi import FastAPI, APIRouter, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import models.models as models
from models.database import SessionLocal, engine
from routers.webhooks import webhook_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GloriaFoods - Twilio Integration"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(webhook_router)

@app.get("/")
def health_test():
    '''Checks if the code is running
    '''
    return {
        "details": "running"
    }, status.HTTP_200_OK


if __name__ == "__main__":
    # Testing
    uvicorn.run("main:app", host="0.0.0.0", port=8000)