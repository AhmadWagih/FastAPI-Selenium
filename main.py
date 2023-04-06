from fastapi import FastAPI,BackgroundTasks
from extract import *
from helper import *
from pydantic import BaseModel
import os

SECRET = os.getenv("SECRET")
app = FastAPI()

class message(BaseModel):
    msg:str

@app.post("/img")
async def testImages(url:str):
    driver = createDriver()
    src = getImages(driver,url)
    imgRes=[]
    for s in src:
        imgRes.append(imageResolution(s))
    driver.close()
    return imgRes

@app.post("/language")
async def testLanguage(url:str):
    driver = createDriver()
    html = getPageSource(driver,url)
    driver.close()
    return html
