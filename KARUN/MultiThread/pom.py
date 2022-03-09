
import time
from datetime import datetime

usrnamexpath="//*[@id='idEmail']"
passwordnamexpath="//*[@id='idpassword']"
loginxpath="//*[@id='idLogin']"
class lims():
    def __init__(self,driver,time):

        self.time=time
        self.driver=driver
    def login(self,link,un,pwd):

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(link)
        self.driver.find_element_by_xpath(usrnamexpath).send_keys(un)
        time.sleep(5)
        self.driver.find_element_by_xpath(passwordnamexpath).send_keys(pwd)





        count = 1;

        while (count > 0):
            currentsysdatetime = datetime.today()
            usrsysdatetime = currentsysdatetime.strftime("%H:%M:%S")
            print(usrsysdatetime+"syst")
            print(time+"login time")
            if time==usrsysdatetime:

                self.driver.find_element_by_xpath(loginxpath).click()
                break



    def xpathclick(self,loc):
        self.driver.find_element_by_xpath(loc).click()
    def xpathsendkeys(self,loc,send):
        self.driver.find_element_by_xpath(loc).send_keys(send)