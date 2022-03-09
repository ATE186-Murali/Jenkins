import time

from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.microsoft import IEDriverManager




s=Service(IEDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.google.com')

time.sleep(60)