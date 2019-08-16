# How to run headless Chrome with Selenium

from selenium import webdriver

path_to_driver = "../chromedriver_win32/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument("headless")

browser = webdriver.Chrome(
    executable_path=path_to_driver, chrome_options=options)

browser.get("https://instagram.com")
