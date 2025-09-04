from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)
username = driver.find_element(By.NAME, "username")
username.send_keys('tomsmith') # Leiab username formi ja kirjutab kasutaja nime
username = driver.find_element(By.NAME, "password")
username.send_keys('SuperSecretPassword!') # Sama parooliga
button = driver.find_element(By.CLASS_NAME, "radius") # Leiab submit nupu
button.click()#Submitib