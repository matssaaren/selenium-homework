from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True) #Ei pane browserit kinni

driver = webdriver.Chrome()
driver.get("https://www.duckduckgo.com")
time.sleep(2)
box = driver.find_element("name", "q") #Leiab otsingu riba
box.send_keys("Mats")#Kirjutab Mats
box.submit()#Enter
