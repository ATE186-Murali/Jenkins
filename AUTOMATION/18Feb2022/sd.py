from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl

kk=MIMEMultipart()
kk['From']='murali.r@agaramtech.com'
kk['To']='karun@agaramtech.com'
kk['CC']='karun@agaramtech.com'
kk['Subject']='Test Mail regarding python'
content="""
This is automatic mail to check sending an mail in the Python
"""
kk.attach(MIMEText(content,'plain'))


# filepath='D:\check\jj.txt'
# fileinbinary=open(filepath,"rb")
# payload=MIMEBase("application","octate-stream")
# payload.set_payload(fileinbinary.read())
# encoders.encode_base64(payload)
# kk.attach(payload)



server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls(context=ssl.create_default_context())
server.login("murali.r@agaramtech.com","IndianArmy@1995")
server.sendmail("karun@agaramtech.com","karun@agaramtech.com",str(kk))
server.close()