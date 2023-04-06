from fastapi import FastAPI,BackgroundTasks
from extract import *
from pydantic import BaseModel
import os

api = FastAPI()
SECRET = os.getenv("SECRET")

class message(BaseModel):
    msg:str
    secret:str


@api.get("/")
async def get():
    return {"message : successfully"}

@api.get("/homepage")
async def homepage():
    driver = createDriver()
    html = getGoogleHomePage(driver)
    driver.close()
    return html

@api.post("/dopgwork")
async def dopgwork(mes = message,backgroundTasks=BackgroundTasks):
    doBGWork(mes)
    print("successful")
