import os
sysname=os.getlogin()
alphabets=[chr(97+i).upper() for i in range(26)]
print(alphabets)
print(len(alphabets))
for j in (range(len(alphabets))):
    driverformat=alphabets[j]+":/"
    print(driverformat)
    drivercheck=os.path.exists(driverformat)
    if drivercheck==True:
        print("Drive Present in " + sysname, driverformat)
        finalselecteddrive=driverformat
print("Final Selected drive "+finalselecteddrive)