import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

sender = 'onebyonetodie@163.com'
receiver = '819384238@qq.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'onebyonetodie@163.com'
password = 'qq819384238'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'

msgText = MIMEText(
    ''' Some  HTML  text  and an image.good!''', 'html', 'utf-8')
msgRoot.attach(msgText)

fp = open('image.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('onebyonetodie', '')
msgRoot.attach(msgImage)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
print('发送完毕~！')