import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path="E:\driver1\chromedriver.exe")
driver.maximize_window()

driver.implicitly_wait(30)
driver.get("http://agl78:8080/QuaLISWeb/")
driver.find_element_by_id("idEmail").send_keys("limsadmin")
driver.find_element_by_id("idpassword").send_keys("123")
driver.find_element_by_id("idLogin").click()
driver.find_element_by_id("iMenuID_2").click()
driver.find_element_by_id("iModuleID_28").click()
driver.find_element_by_id("iFormID_110").click()
driver.find_element_by_id("ID_JA_Home").click()
driver.find_element_by_id("ID_JB_filter").click()
driver.find_element_by_id("ID_ja_refresh").click()
driver.find_element_by_xpath("//div[@id='ID_JAST_Headerdiv']/div[2]/div[2]").click()
driver.find_element_by_id("ID_JB_sample").click()
driver.find_element_by_xpath("//div[@id='ID_JAS_Headerdiv']/div[2]/div[2]").click()
driver.find_element_by_id("ID_JA_test").click()

testList=driver.find_elements_by_xpath("//*[@id='ID_jat_DynamicData']/div")


testList[len(testList)-1].click()

# scroll=driver.find_element_by_xpath("(//*[name()='svg']//*[name()='path' and @d='M416 208H272V64c0-17.67-14.33-32-32-32h-32c-17.67 0-32 14.33-32 32v144H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h144v144c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32V304h144c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z'])[3]")
# scroll.location_once_scrolled_into_view


print(driver.find_element_by_xpath("//*[@id='ID_Pannel_603_8165']/div[1]/h4/a").click())


driver.find_element(By.TAG_NAME, "body").send_keys(Keys.HOME)

driver.find_element(By.TAG_NAME, "body").send_keys(Keys.HOME)

#testList=driver.find_element_by_xpath("//*[@id='ID_JB_ActionMenu']/a").click()
