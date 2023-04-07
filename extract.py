from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

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
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    imgResults = driver.find_elements(By.XPATH,"//img")
    for img in imgResults:
        if (img.get_attribute('src') == r"https://ccweb.imgix.net/https%3A%2F%2Fwww.classcentral.com%2Fimages%2Fillustrations%2Flearning-illustration-holi.png?auto=format&h=650&ixlib=php-3.3.1&s=2367f95a04f9d0237239831d72054f0b"):
            return True
    return False

def getText(driver,url)->str:
    driver.get(url)
    text = driver.find_element(By.XPATH, "/html/body").text
    return text

def checkDropDown(driver,url):
    driver.get(url)
    m=driver.find_elements(By.XPATH, "//*[@id='page-home']/div[1]/header/div[1]/nav/div[1]")
    action = ActionChains(driver)
    action.move_to_element(m).perform()
    n = driver.find_element_by_link_text("Back to JQuery UI")
    return n 
