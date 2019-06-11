from random import randint
import time
import subprocess

ip_address = ''

while True:
    ip_address = '104.' + str(randint(16, 31)) + '.' + str(randint(0, 255)) + '.' + str(randint(1, 254))

    cmd = 'ping ' + ip_address

    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while True:
        out = p.stdout.readline().decode('utf-8')
        if out == '':
            break
        if out != '':
            if 'bytes from ' in out:
                print('找到可用ip: ' + ip_address)
                print("修改/etc/hosts文件,添加项:\n" + ip_address + " free-ss.site\n访问该网站")
                exit(0)
            elif 'PING' in out:
                print(out)
            elif 'Unreachable' in out:
                print(out)
                break

    time.sleep(0.5)
