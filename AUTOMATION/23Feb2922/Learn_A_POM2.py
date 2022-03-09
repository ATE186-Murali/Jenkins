import time

from selenium import webdriver
from  Learn_A_POM import eln


def login(self):
    browserdriver = webdriver.Chrome(executable_path="E:\driver\chromedriver.exe")
    x = eln(browserdriver)
    x.login("https://logilabelntesting.azurewebsites.net/", "agaramtech.onmicrosoft.com", "arul", "admin")
    x.xpathclick("(//*[text()='Orders'])[1]")
    time.sleep(100)



