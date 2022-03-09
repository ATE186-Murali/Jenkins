from datetime import datetime
currentsysdatetime=datetime.today()

print(currentsysdatetime)

print(type(currentsysdatetime))

usrsysdatetime=currentsysdatetime.strftime("%d/%m/%Y %H:%M:%S")

print(usrsysdatetime)