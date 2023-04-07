from fastapi import FastAPI,BackgroundTasks
from extract import *
from helper import *
from pydantic import BaseModel
import os

SECRET = os.getenv("SECRET")
app = FastAPI()


@app.post("/post")
async def test(url:str):
    driver = createDriver()
    result = getImages(driver,url)
    html = getText(driver,url)
    source = getPageSource(driver,url)
    # n = checkDropDown(driver,url)
    driver.close()
    err =""
    if result== False:
        err += "Images not high resolution"
    language = checkLanguage(html)
    if(language != "hi"):
        err += "\n pages not translated"
    if(not checkWrongPage(html)):
        err += "\n Wrong Page"
    if(not checkDrop(source)):
        err += "\n Javascript dropdown not working properly"
    return err
