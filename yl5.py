from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)
link = driver.find_element(By.LINK_TEXT, "Checkboxes") # Otsib lingi
link.click() # Laheb lingi sisse
time.sleep(1)
boxes = driver.find_elements(By.TAG_NAME, "Input") # Otsib molemad checkboxid
for box in boxes: # Vajutab molema checkboxile
    box.click()
time.sleep(1)
driver.back()#Laheb tagasi
    