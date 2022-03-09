# 1. Finding the Local Disk
import os.path
import string
import time
from ctypes import windll
from datetime import datetime

import patoolib
import wget
from selenium import webdriver

# To get the driver details
from selenium.webdriver.support.select import Select


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

    seleniumDriverPath = lastDriver + ":\\driver"

# To create the driver folder path
if not os.path.exists(seleniumDriverPath):
        os.mkdir(seleniumDriverPath)

driverpath=seleniumDriverPath+"\\chromedriver_win32.zip"

# To download the chrome zip file if not exist
if not os.path.exists(driverpath):
    wget.download("https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_win32.zip", driverpath)
    patoolib.extract_archive(driverpath, outdir=seleniumDriverPath)

print(seleniumDriverPath+"\\chromedriver.exe")

# To lauch the chrome browser
driver=webdriver.Chrome(executable_path=seleniumDriverPath+"\\chromedriver.exe")


driver.maximize_window()

driver.implicitly_wait(30)


# to register the sample at particular time


driver.get("http://agl78:8080/QuaLISWeb/home.html")
driver.get("http://agl78:8080/QuaLISWeb/")
driver.find_element_by_id("idEmail").send_keys("limsadmin")
driver.find_element_by_id("idpassword").send_keys("123")
driver.find_element_by_id("idLogin").click()


driver.find_element_by_xpath("//a[@id='iMenuID_2']/span").click()
driver.find_element_by_id("iModuleID_10").click()
driver.find_element_by_id("iFormID_43").click()
driver.find_element_by_id("SR_Home").click()
driver.find_element_by_xpath("//div[@id='Actionbutton']/a/span").click()
driver.find_element_by_id("ID_SR_Preregister").click()
driver.find_element_by_id("ID_SR_Dynamic_17001").click()
Select(driver.find_element_by_id("ID_SR_Dynamic_17001")).select_by_visible_text("Inhouse")
driver.find_element_by_id("ID_SR_Dynamic_17003").click()
Select(driver.find_element_by_id("ID_SR_Dynamic_17003")).select_by_visible_text("API")
driver.find_element_by_id("ID_SR_Dynamic_17007").click()
driver.find_element_by_id("ID_SR_Dynamic_17007").clear()
driver.find_element_by_id("ID_SR_Dynamic_17007").send_keys("bn100")
driver.find_element_by_id("ID_SR_Dynamic_17010").click()
driver.find_element_by_id("ID_SR_Dynamic_17010").click()
Select(driver.find_element_by_id("ID_SR_Dynamic_17010")).select_by_visible_text("Long Term")
driver.find_element_by_id("ID_SR_Dynamic_17014").click()
Select(driver.find_element_by_id("ID_SR_Dynamic_17014")).select_by_visible_text("100 degree")
driver.find_element_by_id("ID_SR_Dynamic_17015").click()
driver.find_element_by_id("ID_SR_Dynamic_17015").clear()
driver.find_element_by_id("ID_SR_Dynamic_17015").send_keys("10")
driver.find_element_by_id("ID_SR_Dynamic_17016").click()
Select(driver.find_element_by_id("ID_SR_Dynamic_17016")).select_by_visible_text("Days")
driver.find_element_by_id("ID_SR_Dynamic_17017").click()
driver.find_element_by_id("ID_SR_Dynamic_17017").clear()
driver.find_element_by_id("ID_SR_Dynamic_17017").send_keys("stp100")
driver.find_element_by_id("ID_SR_Dynamic_17023").click()
driver.find_element_by_id("ID_SR_Dynamic_17023").clear()
driver.find_element_by_id("ID_SR_Dynamic_17023").send_keys("ar100")
driver.find_element_by_id("ID_SR_Dynamic_17027").click()
driver.find_element_by_id("ID_SR_Dynamic_17027").click()
driver.find_element_by_id("ID_SR_Dynamic_17027").click()
driver.find_element_by_id("ID_SR_Dynamic_17027").click()
driver.find_element_by_id("ID_SR_Dynamic_17027").click()
Select(driver.find_element_by_id("ID_SR_Dynamic_17027")).select_by_visible_text("QC Room")
driver.find_element_by_id("ID_SR_Dynamic_17030").click()
driver.find_element_by_id("ID_SR_DIV_17001").click()
driver.find_element_by_id("ID_SR_Dynamic_17030").clear()
driver.find_element_by_id("ID_SR_Dynamic_17030").send_keys("cert")
driver.find_element_by_id("ID_SR_Dynamic_17032").click()
driver.find_element_by_id("ID_SR_Dynamic_17032").clear()
driver.find_element_by_id("ID_SR_Dynamic_17032").send_keys("intial")
driver.find_element_by_id("ID_SR_Submit").click()
driver.find_element_by_id("id_srsub_sample_pannel").click()
time.sleep(3)
driver.find_element_by_xpath("//div[@id='Actionbutton']/a").click()
time.sleep(3)
try:
    driver.find_element_by_id("ID_SR_test_addsample").click()
except:
    time.sleep(3)
    driver.find_element_by_id("ID_SR_test_addsample").click()

driver.find_element_by_id("ID_SR_Samples_ID").send_keys("sample 100")
driver.find_element_by_id("ID_SR_SamplesQUANTITY_ID").send_keys("10")
driver.find_element_by_xpath("//div[@id='ID_SSR_OpenFilterPopUP']/button").click()
driver.find_element_by_xpath("//div[@id='ID_APC_ListDiv_43_0']/li/p").click()
driver.find_element_by_id("ID_SR_Submit_Button").click()
driver.find_element_by_id("ID_SR_sampletype").click()
driver.find_element_by_xpath("//div[@id='Actionbutton']/a/span").click()

currentsysdatetime=datetime.today()

usrsysdatetime=currentsysdatetime.strftime("%H:%M:%S")

print(usrsysdatetime)

registerTime= input("Enter the register time: ")
count = 1;

while (count > 0):

    currentsysdatetime = datetime.today()

    usrsysdatetime = currentsysdatetime.strftime("%H:%M:%S")

    print(usrsysdatetime)
    print("Register Time is " + registerTime)
    print("System time is " + usrsysdatetime)
    if registerTime == usrsysdatetime:
        driver.find_element_by_id("ID_SR_Register").click()
        print("Registered at "+usrsysdatetime)
        break


