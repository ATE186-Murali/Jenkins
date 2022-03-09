from datetime import datetime
registerTime= input("Enter the register time")


count=1;

while (count>0):

    currentsysdatetime = datetime.today()

    usrsysdatetime = currentsysdatetime.strftime("%H:%M:%S")

    print(usrsysdatetime)
    print("Register Time is "+registerTime)
    print("System time is "+usrsysdatetime)
    if registerTime==usrsysdatetime:
        driver.find_element_by_id("ID_SR_Register").click()
        break

