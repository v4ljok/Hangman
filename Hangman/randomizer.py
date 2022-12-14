from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def randomword():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("http://watchout4snakes.com/Random/RandomWord")
    time.sleep(1)
    word = driver.find_element(By.ID, "result")
    return word.text