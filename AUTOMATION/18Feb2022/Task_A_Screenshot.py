import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="E:\driver1\chromedriver.exe")

driver.maximize_window()

url = "https://www.google.com/"

driver.get(url)

time.sleep(10)

driver.save_screenshot('E:\driver1\screenshot\google.png')


