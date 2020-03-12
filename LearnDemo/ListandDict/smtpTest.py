"""
python3 SMTP简单邮件传输协议，他是一组用于由原地址到目的地址的地址传送邮件的规则，由他来控制信件中的中转方式
python的smtplib提供了一种很方便的途径发送电子邮件，她对smtp协议进行了简单的封装
smtpObj = smptlib.SMTP([host[,port[,local_hostname]]])
host:SMPT服务器主机，你可以指定主机的IP地址或者域名如w3school，这个是可选参数
port:如果你提供了host参数，你需要指定SMTP服务使用的端口号，一般情况下SMTP端口号为25
local_hostname：如果SMTP在你的本机上，你只需要指定服务器地址为localhost即可
from_addr：邮件发送者地址
to_addrs:字符串列表，邮件发送地址
msg:发送消息

"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header


#第三方 SMTP服务

#设置服务器
mail_host = 'smtp.qq.com'
#设置用户名
mail_user = '1045385131'
#设置密码
mail_pass = 'Zhangmin_728'

sender = 'mail.qq.com'
#接收邮件，可设置为你自己的邮箱
receivers = ['zoe.zhang@tineco.com']
#三个参数：第一个为文本内容，第二个为plain设置文本格式，第三个utf-8设置编码
message = MIMEText('Python邮件发送测试。。。','plain','utf-8')
message['From'] = Header('W3school教程','utf-8')
message['To'] = Header("测试",'utf-8')


subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25) #25为SMTP端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Erro:无法发送邮件")