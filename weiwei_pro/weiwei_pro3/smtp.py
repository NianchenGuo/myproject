# coding=utf-8
"""
作者：郭伟伟
功能：发送邮件
日期：20191212
"""

import yagmail

# 链接邮箱服务器

yag = yagmail.SMTP(user="***@163.com", password="***", host='smtp.163.com')

# 邮箱正文

contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']

# 发送邮件

yag.send('***@126.com', 'subject', contents)