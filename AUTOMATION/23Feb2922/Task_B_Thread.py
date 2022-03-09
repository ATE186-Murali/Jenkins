import threading
import time

from selenium import webdriver
from  Learn_A_POM import eln

def login(link,organisationID,username,password,path):
    browserdriver = webdriver.Chrome(executable_path=path)
    x = eln(browserdriver)
    x.login(link,organisationID,username,password )
    x.xpathclick("(//*[text()='Orders'])[1]")
    time.sleep(100)

Thread1=threading.Thread(target=login().login(),args=("https://logilabelntesting.azurewebsites.net/","agaramtech.onmicrosoft.com", "arul", "admin","E:\driver\chromedriver.exe"))
Thread1.start()

Thread2=threading.Thread(target=login().login(),args=("https://logilabelntesting.azurewebsites.net/","agaramtech.onmicrosoft.com", "arul", "admin","E:\driver\chromedriver.exe"))
Thread2.start()

Thread3=threading.Thread(target=login().login(),args=("https://logilabelntesting.azurewebsites.net/","agaramtech.onmicrosoft.com", "arul", "admin","E:\driver\chromedriver.exe"))
Thread3.start()