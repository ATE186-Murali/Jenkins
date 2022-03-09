import time
import PIL
import pyscreenshot as pyscreenshot
from selenium import webdriver
from PIL import Image
driver=webdriver.Chrome(executable_path="E:\driver1\chromedriver.exe")
driver.maximize_window()
url = "https://www.google.com/"
driver.get(url)

pyscreenshot.grab().save("E:\driver1\screenshot\google.png")
#
# time.sleep(10)
# driver.save_screenshot('E:\driver1\screenshot\google.png')
# screenshot = Image.open('ss.png')
# screenshot.show()
