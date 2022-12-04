import requests

import smtplib

from bs4 import BeautifulSoup

from email.mime.multipart_1 import MIMEMultipart

from email.mime.text import MIMEText

import datetime

now=datetime.datetime.now()

content = ""

def extract_news(url):
    print("extracting...")
    cnt=""
    cnt+=("Top stories")
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    for i, tag in enumerate(soup.find_all("td",attrs={"class":"title","valign":""})):
        cnt+=((str(i+1)+"::" + "tag.text" + "\n" + "<br>") if tag.text!="more" else "")
    return (cnt)

cnt = extract_news("https://news.ycombinator.com/")
content +=cnt
content += ("<br>------<br>")
content +=("<br><br>End of Message")


#lets send the email
print ("composing email")

#email details

SERVER = "smtp.gmail.com"
PORT = 587
FROM = "anesdzehverovic@gmail.com"
TO = "anesdzehverovic@gmail.com"
PASS = "*********"
#message settings
msg = MIMEMultipart()

msg["subject"] = "TOP new stories [Automated Email]" + " " + str(now.day) + "-" + str(now.month)
msg["from"] = FROM
msg["to"] = TO

msg.attach(MIMEText(content,"html"))

print("Initializing server...")
#server details
server = smtplib.SMTP(SERVER,PORT)

server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())

print("email sent")
server.quit()
