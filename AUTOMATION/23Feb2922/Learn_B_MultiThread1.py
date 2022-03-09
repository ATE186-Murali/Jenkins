import time
from  Learn_A_POM2 import eln
from selenium import webdriver
import threading

x=eln

th1=threading.Thread(target=x.login(),args=("agaramtech.onmicrosoft.com","arul","admin","E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe"))
th1.start()
th2=threading.Thread(target=x.login(),args=("agaramtech.onmicrosoft.com","arul","admin","E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe"))
th2.start()
