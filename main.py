from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/v1")
async def root():
    return {"message": "Hello world from version v1"}
@app.get("/v1/health", status_code=200)
async def health():
    return {"status": "ok"}
@app.get("/v1/test")
async def test():
    url = "http://techblog-v2.dev:8080/v1"
    response = requests.get(url)
    return response.json()