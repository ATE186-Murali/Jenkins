from selenium import webdriver


driver=webdriver.Ie(executable_path="C:\Users\Administrator\Downloads\IEDriverServer_x64_4.0.0\IEDriverServer.exe")

driver.get("https://pypi.org/project/webdriver-manager/")

driver.maximize_window()

