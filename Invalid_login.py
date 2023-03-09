# coding: utf-8
try:
    import time, requests, re, hashlib, datetime, sys, os, random
except Exception as e:
    t = re.findall("d '(.*?)'", str(e))[0]
    print(f'{t}依赖未安装')
    sys.exit()


appid = 'wx7b6272c42fa733a7'
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 9; PBBT00 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 MMWEBID/3625 MicroMessenger/7.0.17.1720(0x27001134) Process/tools WeChat/arm32 NetType/4G Language/zh_CN ABI/arm64', }
host = 'http://39.108.184.87'
def sign (OOOO0000O00OOOOOO ):#line:13
    O0000000OOOOO00OO =hashlib .md5 (OOOO0000O00OOOOOO .encode ()).hexdigest ()#line:14
    OO0OO0000O0O0OOOO ="scsc%^&*"+O0000000OOOOO00OO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:15
    O0O00O00OOO000O0O =hashlib .md5 (OO0OO0000O0O0OOOO .encode ()).hexdigest ()#line:16
    return O0O00O00OOO000O0O #line:17
def timi_new():
    return str(int(time.time() * 1000))
def post_qrcode():
    try:
        resp = requests.post(
            f'http://open.weixin.qq.com/connect/app/qrconnect?appid={appid}&bundleid=(null)&scope=snsapi_userinfo&state=w&from=message&isappinstalled=0',
            headers=headers).text
        qrcode = re.findall('auth_qrcode" src="(.*?)" />', resp)[0]
        uuid = qrcode.split('qrcode/')[1]
        return uuid
    except Exception as e:
        print(e)
def gettasklist(elephant_user, elephant_pswd, elephant_Task_ID):
    try:
        r1 = requests.request('get',
                              f'{host}/api/gettasklist.asp?username={elephant_user}&password={elephant_pswd}&page=1&y=1&appid={appid}&k={elephant_Task_ID}').json()
        # print(r1)
        if r1['ret'] == '0':
            print(f"任务状态:{r1['date'][0]['State']}")
            if r1['date'][0]['State'] == '二维码已失效' or r1['date'][0]['State'] == '管理员终止':
                return True
        return False
    except Exception as e:
        print(e)
def post_code(uuid, elephant_user, elephant_pswd, elephant_Task_ID):
    time_new = int(time.time())
    try:
        while True:
            if gettasklist(elephant_user, elephant_pswd, elephant_Task_ID):
                return False
            resp = requests.post(f'http://long.open.weixin.qq.com/connect/l/qrconnect?uuid={uuid}&_={time_new})',headers=headers).text
            if '405' in resp:
                code = re.findall("wx_code='(.*?)';", resp)[0]
                return code
            time.sleep(3)
    except Exception as e:
        print(e)
def post_dl(code):
    try:
        signstring = f'__{timi_new()}'
        h1 = {
            'timestamp': str(timi_new()),
            'sign': sign(signstring),
            'signstring': signstring,
            'version': '3.1.4195311',
            'janalytics': 'c167f56858dc424ee3d617c9',
            'Host': 'scsc.sc19319.com',
            'User-Agent': 'okhttp/4.9.1',
        }
        r1 = requests.request('get', 'http://scsc.sc19319.com/loginToken', headers=h1).json()
        if 'status' in r1:
            if r1['status'] == 200:
                b2 = {
                    "loginToken": r1['data'],
                    "code": code,
                    "loginType": "生成世朝"
                }
                signstring1 = f'_code={code}&loginToken={r1["data"]}&loginType=_{timi_new()}'
                h2 = {
                    'timestamp': str(timi_new()),
                    'sign': sign(signstring1),
                    'signstring': signstring1,
                    'version': '3.1.4195311',
                    'janalytics': 'c167f56858dc424ee3d617c9',
                    'Host': 'scsc.sc19319.com',
                    'User-Agent': 'okhttp/4.9.1',
                }
                r2 = requests.request('post', 'http://scsc.sc19319.com/login', headers=h2, data=b2).json()
                if 'status' in r2:
                    if r2['status'] == 200:
                        print('登录成功')
                        return r2['data']['token']
                    if r2['status'] == 500:
                        print(r2['message'])

    except Exception as e:
        print(e)



def addtask(elephant_user, elephant_pswd, elephant_Task_ID):
    uuid = post_qrcode()
    body = f'zcgqewm=https://open.weixin.qq.com/connect/confirm?uuid={uuid}'
    hea = {'Charset': 'UTF-8', 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
           'Cache-Control': 'no-cache', 'accept': 'application/json,text/html', 'Content-Length': '86',
           'User-Agent': 'Dalvik/2.1.0(Linux;U;Android12;2201122CBuild/SKQ1.211006.001)',
           'Host': '39.108.184.87', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', }
    try:
        resp = requests.post(f'{host}/api/addtask.asp?username={elephant_user}&password={elephant_pswd}&zcsqrwid={elephant_Task_ID}',headers=hea, data=body).json()
        if 'msg' in resp:
            print(f'提交任务:{resp["msg"]}')
        code = post_code(uuid, elephant_user, elephant_pswd, elephant_Task_ID)
        if code:
            return post_dl(code)
    except Exception as e:
        print(e)

