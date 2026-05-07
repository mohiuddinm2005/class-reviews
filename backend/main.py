from fastapi import FastAPI
from bs4 import BeautifulSoup


app = FastAPI()



@app.get("https://api.api-ninjas.com/v1/university")
def school_information():
    return {"name: "}