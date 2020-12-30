from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
xPathButton = "//button[contains(text(),'Start')]"
xPathMessageHW = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/h4[1]"

try:
    element = WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.XPATH, xPathButton)))
    element.find_element_by_xpath(xPathButton).click()

    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xPathMessageHW)))
    returnMessage = element.find_element_by_xpath(xPathMessageHW).text

    assert returnMessage == 'Hello World!'

    print(returnMessage)
finally:
    driver.quit()