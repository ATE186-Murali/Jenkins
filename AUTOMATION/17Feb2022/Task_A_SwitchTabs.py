import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="E:\driver1\chromedriver.exe")
driver.maximize_window()

driver.implicitly_wait(30)
# First tab
driver.get("http://agl78:8080/QuaLISWeb/")

driver.find_element_by_id("idEmail").send_keys("limsadmin")

driver.find_element_by_id("idpassword").send_keys("123")
driver.find_element_by_id("idLogin").click()

driver.find_element_by_id("iMenuID_1").click()
driver.find_element_by_id("iModuleID_1").click()
driver.find_element_by_id("iFormID_45").click()
try:
 driver.find_element_by_xpath("//*[@id='ID_CT_ContainerTypeActionMenu']/a").click()
except:
 time.sleep(3)
 driver.find_element_by_xpath("//*[@id='ID_CT_ContainerTypeActionMenu']/a").click()

driver.find_element_by_xpath("//*[@id='ID_CT_ContainerTypeAddbutton']").click()

print("add button")
# ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]

driver.find_element_by_id("ID_CT_ContainerTypeName").send_keys("Bottle")
driver.find_element_by_id("ID_CT_ContainerTypeADDSubmit").click()

time.sleep(3)


driver.execute_script("window.open('http://agl78:8080/QuaLISWeb/')")

handles=driver.window_handles
handle=handles[1]
print(handle)
driver.switch_to.window(handle)
print(driver.title)


driver.find_element_by_id("idEmail").send_keys("limsadmin")

driver.find_element_by_id("idpassword").send_keys("123")
driver.find_element_by_id("idLogin").click()

driver.find_element_by_id("iMenuID_1").click()
driver.find_element_by_id("iModuleID_1").click()
driver.find_element_by_id("iFormID_45").click()
try:
 driver.find_element_by_xpath("//*[@id='ID_CT_ContainerTypeActionMenu']/a").click()
except:
 time.sleep(3)
 driver.find_element_by_xpath("//*[@id='ID_CT_ContainerTypeActionMenu']/a").click()

try:
 driver.find_element_by_xpath("//*[@id='ID_CT_ContainerTypeDeletebutton']").click()
except:
 time.sleep(3)
 driver.find_element_by_xpath("//*[@id='ID_CT_ContainerTypeDeletebutton']").click()

driver.switch_to.window(handles[0])

time.sleep(3)

try:
 driver.find_element_by_xpath("//*[@id='ID_CT_ContainerTypeActionMenu']/a").click()
except:
 time.sleep(3)
 driver.find_element_by_xpath("//*[@id='ID_CT_ContainerTypeActionMenu']/a").click()

try:
 driver.find_element_by_xpath("//*[@id='ID_CT_ContainerTypeDeletebutton']").click()
except:
 time.sleep(3)
 driver.find_element_by_xpath("//*[@id='ID_CT_ContainerTypeDeletebutton']").click()

