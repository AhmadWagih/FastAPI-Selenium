import numpy
import cv2
from textblob import TextBlob

def imageResolution(imgUrl:str):
    img=cv2.imread(imgUrl)
    length,width,f = img.shape
    print(length)
    print(width)

def checkLanguage(text:str):
    b= TextBlob(text)
    language = b.detect_language()
    print(language)

