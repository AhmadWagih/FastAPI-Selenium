from fastapi import FastAPI,BackgroundTasks
from extract import *
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
    driver.close()
    return src

@app.post("/language")
async def testLanguage(url:str):
    driver = createDriver()
    html = getPageSource(driver,url)
    driver.close()
    return html
