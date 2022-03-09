import time
time.sleep()


from selenium import webdriver

# Launch Browser
driver=webdriver.Chrome(executable_path="E:\driver\chromedriver.exe")


# Maximize
driver.maximize_window()

time.sleep()