from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers.image import image
from routers.label import label
from routers.user import user

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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