# Define the location of the file
import xlrd as xlrd

loc = "D:\\New XLS Worksheet.xls"

# To open the Workbook     
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0     
sheet.cell_value(0, 0)  