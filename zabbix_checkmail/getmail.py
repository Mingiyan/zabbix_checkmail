#!/usr/bin/python
##### Created by Mingiyan Dordzhiev #####
import smtplib
import os, sys, time
import imaplib, email

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


fromaddr = "noreply1@smail.ru"
toaddr = "noreply1@smail.ru"
mypass = "xx"
realtime = time.strftime("%d") + time.strftime("%m") + time.strftime("%Y") + time.strftime("%H") + time.strftime("%M") + time.strftime("%S")
nowtime = 0
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = realtime

body = "MESSAGE ZABBIX CHECK"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('xx.smail.ru', 25)
#server.starttls()
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

#time.sleep(15)

server = "smail.ru"
port = "143"
login = "noreply1@smail.ru"
password = "xx"

box = imaplib.IMAP4(server, port)
#box = imaplib.IMAP4_SSL(server, port)

box.login(login, password)

typ, count = box.select('INBOX') 

typ, data = box.search(None, 'FROM', '"noreply1@smail.ru"') 
for num in data[0].split() :
    typ, message = box.fetch(num, '(RFC822)')
    
    perem = message[0][1]
   
    mail = email.message_from_string(perem)

    subject = mail.get("Subject")
    h = email.Header.decode_header(subject)
    subject = h[0][0].decode(h[0][1]) if h[0][1] else h[0][0]
    nowtime = subject.encode('utf-8')
    box.store(num, '+FLAGS', '\\Deleted')
 



box.close()
box.logout()

if realtime == nowtime:
    print("1")
else:
    sys.exit(1)

