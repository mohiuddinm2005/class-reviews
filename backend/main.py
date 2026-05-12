from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()



@app.get()
def school_information():
    return {"name: "}