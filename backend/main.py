from fastapi import FastAPI
from bs4 import BeautifulSoup


app = FastAPI()



@app.get()
def school_information():
    return {"name: "}