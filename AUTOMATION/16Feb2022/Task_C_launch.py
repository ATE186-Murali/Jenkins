import os
import string
import time
from ctypes import windll
from zipfile import ZipFile
import patoolib
import wget
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as dharani
from selenium.webdriver.support.wait import WebDriverWait


def getDrivers():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()

    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives

if __name__ == '__main__':
    driveList=getDrivers()
    totalDrivers=(len(driveList))

    lastDriver=driveList[totalDrivers-1]

    print(lastDriver)

seleniumDriverPath=lastDriver+":\\driver"

print(lastDriver+":\driver1")

try:
    os.makedirs(lastDriver + "\driver1")
except:
    print("already avilable")

folder=lastDriver+":\\driver1"


downloadpath=folder
rarfile=folder+"\chromedriver_win32.zip"

wget.download("https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_win32.zip",downloadpath)

patoolib.extract_archive(rarfile, outdir=downloadpath)



driver=webdriver.Chrome(executable_path=downloadpath+"\chromedriver.exe")


driver.maximize_window()

driver.implicitly_wait(30)
driver.get('http://10.10.10.4:8889/secure/Dashboard.jspa')

a=driver.find_element_by_xpath("//input[@id='login-form-username']").send_keys("ate186")

b=driver.find_element(By.XPATH,"//input[@id='login-form-password']").send_keys("muralimurali")

c=driver.find_element(By.XPATH,"//input[@id='login']").click()

url=driver.current_url

title = driver.title

print("The opened URL is "+url)

print("The opened title is "+title)

time.sleep(5)

driver.find_element(By.XPATH,"//img[@alt='User profile for Murali R']").click()

print("clicked profile ")

driver.find_element(By.XPATH,"//*[@id='log_out']").click()
print("clicked the logout")

logout=driver.find_element(By.XPATH,"//strong[contains(text(),'You are now logged out. Any automatic login has also been stopped.')]")

if logout.is_displayed():
    print("Logged Out Successfully")
else:
    print(" Unable to Logout")
