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
    driver.close()
    imgRes=[]
    for s in src:
        res=imageResolution(s)
        # if res<1 :
        #     return False
        imgRes.append(res)
    return imgRes
    return True

@app.post("/language")
async def testLanguage(url:str):
    driver = createDriver()
    html = getText(driver,url)
    driver.close()
    # language = checkLanguage(html)
    # if(language != "Indian"):
    #     return False
    return html
    return True
