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
    result = getImages(driver,url)
    driver.close()
    return result

@app.post("/language")
async def testLanguage(url:str):
    driver = createDriver()
    html = getText(driver,url)
    driver.close()
    language = checkLanguage(html)
    if(language != "hi"):
        return False
    return True

@app.post("/dropdown")
async def testDropDown(url:str):
    driver = createDriver()
    n = checkDropDown(driver,url)
    return n 