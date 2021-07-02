import smtplib 
mailhost='smtp.qq.com'
qqmail = smtplib.SMTP()
qqmail.connect(mailhost,25)