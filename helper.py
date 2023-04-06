# import cv2
import imquality.brisque as brisque
import PIL.Image
from textblob import TextBlob

def imageResolution(imgUrl:str):
    # img=cv2.imread(imgUrl)
    # length,width,f = img.shape
    # if le
    img = PIL.Image.open(imgUrl)
    score = brisque.score(img)
    return score 

def checkLanguage(text:str):
    b= TextBlob(text)
    print(b)
    language = b.detect_language()
    print(language)

