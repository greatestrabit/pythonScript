import imaplib
import os
import time

def get_newmail_count():
    obj = imaplib.IMAP4_SSL('imaphz.qiye.163.com', '993')
    obj.login('xiaodu.email@gmail.com', 'passowrd')
    obj.select()
    idlist = obj.search(None, 'UnSeen')[1]
    id = idlist[0].decode('utf-8')

    if id:
        return id.count(' ') + 1

    return 0


def send_notify(count):
    notice = '有' + str(count) + '封未读邮件'
    cmd = 'notify-send "新邮件通知" ' + notice + ' -i face-crying'
    os.system(cmd)


while 1:
    count = get_newmail_count()
    if count:
        send_notify(count)

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(5)
