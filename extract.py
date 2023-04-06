from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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

def getGoogleHomePage(driver)->str:
    driver.get("https://www.google.com")
    return driver.page_source

def doBGWork(inp):
    print("doin bg tasks")
    print(inp.message)
    print("Done")
