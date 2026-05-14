from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()



@app.get("/school-information")
def school_information(location: str):
    if location != "Upenn":
        return {"error": "Please enter school name"}
    return {
          "name": "Upenn",
          "address": "3451 Walnut Street, Philadelphia, PA 19104",
    }
   
  