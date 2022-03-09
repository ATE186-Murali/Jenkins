from datetime import datetime

import openpyxl
import pypyodbc

credential="Driver={SQL Server}; Server=AGL78\SQLEXPRESS2017; Database=T_HYLIMS_875_B01; UID=sa; PWD=admin@123"

dbconnect=pypyodbc.connect(credential)

cursor=dbconnect.cursor()


result=cursor.execute("SELECT * FROM users")

result = cursor.fetchall()

i = 0

for x in result:

    j = 0
    for y in x:

        loc = "D:\\python\\nibsc - Copy.xlsx"

        workbook = openpyxl.load_workbook(loc)

        sheet = workbook["Sheet1"]

        df = sheet.cell(i+1, j+1).value = y

        currentsysdatetime = datetime.today()
        usrsysdatetime = currentsysdatetime.strftime("%d%m%Y_%H%M%S")

        usrsysdatetime=usrsysdatetime+""

        workbook.save("D:\\python\\nibsc - " + usrsysdatetime + ".xlsx")



        j=j+1

    i=i+1



