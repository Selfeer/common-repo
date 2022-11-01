from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def open_page():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://www.google.com")
    driver.close()
