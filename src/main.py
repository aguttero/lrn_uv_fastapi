from fastapi import FastAPI
import sys

app = FastAPI()

@app.get ("/")
async def root():
    return {"message": "Hello World! This is Panorámix"}

@app.get("/getpythonversion")
async def get_python_version():
    return {"version": sys.version}
