from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def createDriver()->webdriver.Chrome: # it annotates the return type of the function is webdriver.Chrome
# Create option
    chrome_options = webdriver.ChromeOptions()
# Add arguments, options
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True
    chrome_options.add_experimental_option("prefs",prefs)
# Create Driver including service () and options
    myDrived = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

    return myDrived

def getPageSource(driver,url)->str:
    driver.get(url)
    return driver.page_source

def getImages(driver,url)->str:
    driver.get(url)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    imgResults = driver.find_elements(By.XPATH,"//img")
    print(imgResults)
    src = []
    for img in imgResults:
        src.append(img.get_attribute('src'))
    print(src)
    return src

def getText(driver,url)->str:
    driver.get(url)
    text = driver.find_element(By.XPATH, "/html/body").text
    print(text)
    return text

def checkDropDown(driver,url):
    driver.get(url)
    driver.find_elements(By.XPATH, "//*[@id='page-home']/div[1]/header/div[1]/nav/div[1]")