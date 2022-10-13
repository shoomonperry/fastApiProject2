from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

#get list of images
@app.get("/photos")
def images():
    out = []
    for filename in os.listdir("static/photos"):
        out.append({
            "name": filename.split(".")[0],
            "path": "/static/photos/" + filename
        })
    return out

@app.get("/thumbnails")
def images():
    out = []
    for filename in os.listdir("static/thumbnails"):
        out.append({
            "name": filename.split(".")[0],
            "path": "/static/thumbnails/" + filename
        })
    return out