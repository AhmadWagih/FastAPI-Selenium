from fastapi import FastAPI,BackgroundTasks
from extract import *
from helper import *
from pydantic import BaseModel
import os

SECRET = os.getenv("SECRET")
app = FastAPI()


@app.post("/post")
async def testImages(url:str):
    driver = createDriver()
    result = getImages(driver,url)
    html = getText(driver,url)
    # n = checkDropDown(driver,url)
    driver.close()
    err =""
    if result== False:
        err += "Images not high resolution"
    language = checkLanguage(html)
    if(language != "hi"):
        err += "Inner pages not translated"
    return err
