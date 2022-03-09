import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


s=Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.implicitly_wait(30)
driver.get('http://10.10.10.4:8889/secure/Dashboard.jspa')

for i in "abcdefabcdefghijklmnopqrsutvwxyzabcdefghijklmnopqrsutvwxyzabcdefghijklmnopqrsutvwxyzabcdefghijklmnopqrsutvwxyzabcdefghijklmnopqrsutvwxyzghijklmnopqrsutvwxyz":

    time.sleep(60)
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
    print(" Unable to login")

time.sleep(30)
