#!/usr/bin/python
import subprocess
import requests
import json
import time

"""
请先安装genymotion
实时读取genymotion日志,如有微信日志,发送消息到钉钉
"""

cmd = "~/Software/genymotion/tools/adb logcat"

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

headers = {
    'Content-Type': 'application/json',
}
params = {
    'access_token': '4b7734ada5d8ccd9fd3ad83eb2f67f236a135aa08d6a1e4',
}
payload = {
    'text': {
        'content': '收到一条微信消息',
    },
    'msgtype': 'text',
}
url = 'https://oapi.dingtalk.com/robot/send'

start = time.time()
sendtime = time.time()

while True:
    out = p.stdout.readline()
    if out == '':
        break
    if out != '' and "requestLayout() improperly called by com.tencent.mm.plugin.appbrand.widget.desktop" in out.decode("utf-8"):
        print(out)
        end = time.time()

        if end - start > 10 and end - sendtime > 5:
            requests.post(url, headers=headers, params=params, data=json.dumps(payload))
            sendtime = time.time()
