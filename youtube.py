from selenium import webdriver
from selenium.webdriver.firefox.options import Options

fireFoxOptions = Options()  
fireFoxOptions.add_argument("--headless") 
fireFoxOptions.add_argument("--window-size=1920,1080")
fireFoxOptions.add_argument('--start-maximized')
fireFoxOptions.add_argument('--disable-gpu')
fireFoxOptions.add_argument('--no-sandbox')

driver = webdriver.Firefox(options=fireFoxOptions,executable_path=".\driver\geckodriver.exe")
url = 'https://youtube.com/playlist?list=PLRKtsQZFhbkSk82_q7lbLnOKi7KFDxgCM'
driver.get(url)

postElement = driver.find_element_by_css_selector(".qqtRac > form:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(3)")
postElement.click()

def collectingVideotitles():
    elements = []
    objectsPage = driver.find_elements_by_xpath("//*[@id='video-title']")

    for object in objectsPage:
        elements.append(str(object.get_attribute("title")))
    
    for i in elements:
        print(i)

collectingVideotitles()
driver.close() 