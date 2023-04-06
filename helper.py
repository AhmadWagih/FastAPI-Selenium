# import cv2
import imquality.brisque as brisque
import PIL.Image
from langdetect import detect, DetectorFactory

def imageResolution(imgUrl:str):
    # img=cv2.imread(imgUrl)
    # length,width,f = img.shape
    # if le
    img = PIL.Image.open(imgUrl)
    score = brisque.score(img)
    return score 

def checkLanguage(text:str):
    DetectorFactory.seed = 0
    language=detect(text)
    return language

