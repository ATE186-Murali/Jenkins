import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path="D:\\db\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(10)