import smtplib
import  string

HOST = "smtp.qq.com" #define smtp host
SUBJECT = "Test email from Python"  #define mail topic
TO = "vance.li@btcc.com" # receiver
FROM = "995564286@qq.com"  #sender
text = "Python rules then all!" #mail content
BODY = string.join((
    "From:%s" % FROM,
    "To:%s" % TO,
    "Subject:%s" % SUBJECT,
    "",
    text
),"\r\n")

server = smtplib.SMTP() # create SMTP() object


server.connect(HOST,"25")
server.ehlo("successfully")
server.starttls()   #start security transformation
server.login("995564286@qq.com","ZJJwoaini@") #check your account
server.sendmail(FROM,[TO],BODY) #send mail
server.close()
