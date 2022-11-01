from selenium import webdriver


def open_page():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://www.google.com")
    driver.close()
