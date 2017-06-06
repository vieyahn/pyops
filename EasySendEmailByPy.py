
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from email.utils import parseaddr, formataddr
from email.header import Header



#information
from_addr = ""
smtp_server = ""
to_addr = ""
pwd = ""

#body
msg = MIMEMultipart()

body_msg = MIMEText('tunnelblick configuration file...', 'plain', 'utf-8')
msg.attach(body_msg)

def add_attach(file_path):
    part = MIMEApplication(open(file_path,'rb').read())
    filename = "test.py"  # file_path.split('/')[-1]
    msg.add_header("Content-Disposition","attachment",filename="8888.tar.gz") #filename must keep file format,but you can rename it
    msg.attach(part)


#part = MIMEApplication(open('test.py','rb').read())
#part.add_header("Content-Disposition","attachment",filename="000000.py")
#msg.attach(part)

#part = MIMEApplication(open('test.tar.gz','rb').read())
#part.add_header("Content-Disposition","attachment",filename="888888.tar.gz")
#msg.attach(part)

#add_attach("/Users/vance/PyT/Training/FlaskDog/schema.sql")
add_attach('test.tar.gz')
add_attach('test.py')
#header
def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
msg['From'] = _format_addr(u'Devops Team <%s>' % from_addr) #title address

#msg['to'] = _format_addr(u"比特币中国 <%s>" % to_addr)
msg['to'] = input("Input your email address to receive the file: ")
msg['Subject'] = Header('VPN Setting','utf-8').encode()

#server
server = smtplib.SMTP(smtp_server)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, pwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()