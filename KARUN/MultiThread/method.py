import datetime
import time
from  pom import lims
from selenium import webdriver
import threading
def login(usrnm,pswd,browserpath):

    logintime = input("Login time")
    browserdriver=webdriver.Chrome(executable_path=browserpath)
    instance=lims(browserdriver,logintime)
    instance.login("http://agl78:8080/QuaLISWeb/",usrnm,pswd)
    time.sleep(100)







thread1=threading.Thread(target=login,args=("limsadmin","123","E:\driver\chromedriver.exe"))
thread1.start()
thread2=threading.Thread(target=login,args=("limsadmin","123","E:\driver\chromedriver.exe"))
thread2.start()