import pypyodbc

credential="Driver={SQL Server}; Server=AGL78\SQLEXPRESS2017; Database=T_HYLIMS_875_B01; UID=sa; PWD=admin@123"

dbconnect=pypyodbc.connect(credential)

cursor=dbconnect.cursor()


cursor.execute("SELECT * FROM users")
row = cursor.fetchone()


while row:
    print (row)
    row = cursor.fetchone()