from fastapi import FastAPI,BackgroundTasks
from extract import *
from pydantic import BaseModel
import os

SECRET = os.getenv("SECRET")
app = FastAPI()

class message(BaseModel):
    msg:str
    secret:str


@app.get("/")
async def get():
    return {"message : successfully"}

@app.get("/homepage")
async def homepage():
    driver = createDriver()
    html = getGoogleHomePage(driver)
    driver.close()
    return html

@app.post("/dopgwork")
async def dopgwork(mes = message,backgroundTasks=BackgroundTasks):
    doBGWork(mes)
    print("successful")
