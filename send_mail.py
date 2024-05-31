import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('dipaksunny009@gmail.com','prtt gvok etmk ezgi')
    msg=EmailMessage()
    msg['FROM']='dipaksunny009@gmail.com'
    msg['SUBJECT']=subject
    msg['TO']=to
    msg.set_content(body)
    server.send_message(msg) 
    server.quit()