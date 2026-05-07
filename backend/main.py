from fastapi import FastAPI
from bs4 import BeautifulSoup


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

