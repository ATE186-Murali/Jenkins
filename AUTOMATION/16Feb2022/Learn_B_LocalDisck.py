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


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()

    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

if __name__ == '__main__':
    driveList=get_drives()
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

time.sleep(30)


