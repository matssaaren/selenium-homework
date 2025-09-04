from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
time.sleep(2)
button = driver.find_element(By.TAG_NAME, "button") # Otsib nupu
for i in range(5):# Vajutab sama nuppu 5 korda
    button.click()
time.sleep(1)
buttons = driver.find_elements(By.CLASS_NAME, "added-manually") #Leiab koik uued elemendid
for button in buttons: # Kustutab koik vajutades nende peale
    button.click()