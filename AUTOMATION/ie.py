from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Ie(executable_path="D:\IEDriverServer.exe")
# to maximize the browser window
driver.maximize_window()

driver.get(r"https://www.google.com")