from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/", response_class=JSONResponse)
def read_root() -> dict:
    return {"Hello": "World"}