import openpyxl
import pypyodbc

credential="Driver={SQL Server}; Server=AGL78\SQLEXPRESS2017; Database=T_HYLIMS_875_B01; UID=sa; PWD=admin@123"

dbconnect=pypyodbc.connect(credential)

cursor=dbconnect.cursor()


cursor.execute("SELECT * FROM users")
result = cursor.fetchall()

initialRow = 1

for x in result:

    initialColumn = 1
    for y in x:
        # print(y)


        loc = "D:\\python\\nibsc - Copy.xlsx"

        workbook = openpyxl.load_workbook(loc)

        sheet = workbook["Sheet1"]

        df = sheet.cell(initialRow, initialColumn).value = y

        workbook.save("D:\\python\\nibsc - Copy.xlsx")

        initialColumn=initialColumn+1

    initialRow=initialRow+1