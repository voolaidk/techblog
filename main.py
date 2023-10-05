from fastapi import FastAPI
import requests
import uvicorn
import platform

app = FastAPI()

@app.get("/v1")
async def root():
    return {"message": "Hello world from version v1"}
@app.get("/v1/health", status_code=200)
async def health():
    return {"status": "ok"}

@app.get("/v1/info")
async def get_os_info():
    return platform.architecture()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8081, log_level="info")
