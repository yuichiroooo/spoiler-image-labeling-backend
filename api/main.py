import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers.image import image
from routers.label import label
from routers.user import user

load_dotenv()

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")

origins = os.getenv("ALLOWED_HOST")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def hello():
    return {"message": "hello world"}

app.include_router(image)
app.include_router(label)
app.include_router(user)