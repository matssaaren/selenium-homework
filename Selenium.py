from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com")
time.sleep(2)
quotes = driver.find_elements(By.CLASS_NAME, "text")
authors = driver.find_elements(By.CLASS_NAME, "author")
for quote, author in zip(quotes, authors):
    print(quote.text + author.text)