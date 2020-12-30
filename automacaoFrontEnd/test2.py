from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://the-internet.herokuapp.com/challenging_dom")

#xPATH elements
xPathButtonBlue = "//div//a[@class='button']"
xPathButtonRed = "//div//a[@class='button alert']"
xPathButtonGreen = "//div//a[@class='button success']"
xPathTable = "//table//tbody//tr"

wait = WebDriverWait(driver, 10)

#Fuction to perform click tests
def actionButtonSide(xPathButton):
    #Button element search and action
    elementButton = wait.until(EC.element_to_be_clickable((By.XPATH, xPathButton)))
    elementButton.find_element_by_xpath(xPathButton).click()
  
    #Find elements of the table
    trElements = driver.find_elements_by_xpath(xPathTable)
    count = len(trElements)
    for i in range(1,count):
        stringEdit = '//table//tbody//tr[%i]//td[7]//a[1]' % i
        stringDelete = '//table//tbody//tr[%i]//td[7]//a[2]' % i
        driver.find_element_by_xpath(stringEdit).click()
        # time.sleep(1)
        driver.find_element_by_xpath(stringDelete).click()
        # time.sleep(1)
        
try:
    actionButtonSide(xPathButtonBlue)
    actionButtonSide(xPathButtonRed)
    actionButtonSide(xPathButtonGreen)
finally:
    driver.quit()