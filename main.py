from fastapi import FastAPI,BackgroundTasks
from extract import *
from pydantic import BaseModel
import os

SECRET = os.getenv("SECRET")
app = FastAPI()

class message(BaseModel):
    msg:str
    secret:str

@app.post("/post")
async def testURL(url:str):
    driver = createDriver()
    html = getPageSource(driver,url)
    driver.close()
    return html
