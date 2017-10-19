import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
cn = raw_input('Please Enter Customer Name : ') 

x = raw_input('Please Select Send To  :\n 1)Nima_Tehrani \n 2)Sales \n ')
if x == '1':
    toaddr = "?????@parspooyesh.com" # to address
elif x == '2':
    toaddr = "???@parspooyesh.com" # another to address
else:
    print 'Please Select 1 OR 2 '

fromaddr = "?????????@gmail.com" # your gmail address
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = cn
 
body = "Hi Software output New Install "
 
msg.attach(MIMEText(body, 'plain'))
 
filename = cn + "_output"
attachment = open("/home/output", "rb") # attach this file 
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "??????") #your gmail password
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print 'Send Succsessfully!!!'
time.sleep(5)
