try :#line:2
    import time ,requests ,re ,hashlib ,datetime ,sys ,os ,random #line:3
except Exception as e :#line:4
    t =re .findall ("d '(.*?)'",str (e ))[0 ]#line:5
    print (f'{t}依赖未安装')#line:6
    sys .exit ()#line:7
appid ='wx7b6272c42fa733a7'#line:10
headers ={'User-Agent':'Mozilla/5.0 (Linux; Android 9; PBBT00 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 MMWEBID/3625 MicroMessenger/7.0.17.1720(0x27001134) Process/tools WeChat/arm32 NetType/4G Language/zh_CN ABI/arm64',}#line:11
host ='http://39.108.184.87'#line:12
def sign (OOOO0000O00OOOOOO ):#line:13
    O0000000OOOOO00OO =hashlib .md5 (OOOO0000O00OOOOOO .encode ()).hexdigest ()#line:14
    OO0OO0000O0O0OOOO ="scsc%^&*"+O0000000OOOOO00OO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:15
    O0O00O00OOO000O0O =hashlib .md5 (OO0OO0000O0O0OOOO .encode ()).hexdigest ()#line:16
    return O0O00O00OOO000O0O #line:17
def timi_new ():#line:20
    return str (int (time .time ()*1000 ))#line:21
def post_qrcode ():#line:25
    try :#line:26
        OO0OO00O0OO00OOOO =requests .post (f'http://open.weixin.qq.com/connect/app/qrconnect?appid={appid}&bundleid=(null)&scope=snsapi_userinfo&state=w&from=message&isappinstalled=0',headers =headers ).text #line:29
        OO000O0O0O0000O00 =re .findall ('auth_qrcode" src="(.*?)" />',OO0OO00O0OO00OOOO )[0 ]#line:30
        O0O000OO00OO000OO =OO000O0O0O0000O00 .split ('qrcode/')[1 ]#line:31
        return O0O000OO00OO000OO #line:32
    except Exception as OOO000O0OO00OO0OO :#line:33
        print (OOO000O0OO00OO0OO )#line:34
def gettasklist (O0O00O0OO000OOO0O ,O0OO0000O0O0OO00O ,O0O00OO000O0O000O ):#line:38
    try :#line:39
        OO00OOOOOOO0OO0OO =requests .request ('get',f'{host}/api/gettasklist.asp?username={O0O00O0OO000OOO0O}&password={O0OO0000O0O0OO00O}&page=1&y=1&appid={appid}&k={O0O00OO000O0O000O}').json ()#line:41
        if OO00OOOOOOO0OO0OO ['ret']=='0':#line:43
            print (f"任务状态:{OO00OOOOOOO0OO0OO['date'][0]['State']}")#line:44
            if OO00OOOOOOO0OO0OO ['date'][0 ]['State']=='二维码已失效'or OO00OOOOOOO0OO0OO ['date'][0 ]['State']=='管理员终止':#line:45
                return True #line:46
        return False #line:47
    except Exception as OOOO0000O0OO0OO0O :#line:48
        print (OOOO0000O0OO0OO0O )#line:49
def post_code (OO00OO0000000OOOO ,OOO00000O0000OO0O ,OOOOO000O0000000O ,O0OOOOO0OO00O0OOO ):#line:54
    OO0O000O00OO0OOO0 =int (time .time ())#line:55
    try :#line:56
        while True :#line:57
            if gettasklist (OOO00000O0000OO0O ,OOOOO000O0000000O ,O0OOOOO0OO00O0OOO ):#line:59
                return False #line:60
            O0OOOOOO0OOOO00O0 =requests .post (f'http://long.open.weixin.qq.com/connect/l/qrconnect?uuid={OO00OO0000000OOOO}&_={OO0O000O00OO0OOO0})',headers =headers ).text #line:62
            if '405'in O0OOOOOO0OOOO00O0 :#line:63
                OOO000OOOO0000OOO =re .findall ("wx_code='(.*?)';",O0OOOOOO0OOOO00O0 )[0 ]#line:64
                return OOO000OOOO0000OOO #line:65
            time .sleep (3 )#line:66
    except Exception as OO00OOO0OOOO00O0O :#line:67
        print (OO00OOO0OOOO00O0O )#line:68
def post_dl (OO000OO000O0OO0OO ):#line:72
    try :#line:73
        OO0OO00OO0OOO0O00 =f'__{timi_new()}'#line:74
        OO000OOO0OOO000OO ={'timestamp':str (timi_new ()),'sign':sign (OO0OO00OO0OOO0O00 ),'signstring':OO0OO00OO0OOO0O00 ,'version':'3.1.4195311','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:83
        OOOO0OO0OO00OOOO0 =requests .request ('get','http://scsc.sc19319.com/loginToken',headers =OO000OOO0OOO000OO ).json ()#line:84
        if 'status'in OOOO0OO0OO00OOOO0 :#line:86
            if OOOO0OO0OO00OOOO0 ['status']==200 :#line:87
                OOO00OO000000000O ={"loginToken":OOOO0OO0OO00OOOO0 ['data'],"code":OO000OO000O0OO0OO ,"loginType":"生成世朝"}#line:92
                OO0000O000O000O00 =f'_code={OO000OO000O0OO0OO}&loginToken={OOOO0OO0OO00OOOO0["data"]}&loginType=_{timi_new()}'#line:93
                O00O0OO0OOO00O000 ={'timestamp':str (timi_new ()),'sign':sign (OO0000O000O000O00 ),'signstring':OO0000O000O000O00 ,'version':'3.1.4195311','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:102
                OOOO0O0O000000000 =requests .request ('post','http://scsc.sc19319.com/login',headers =O00O0OO0OOO00O000 ,data =OOO00OO000000000O ).json ()#line:103
                if 'status'in OOOO0O0O000000000 :#line:105
                    if OOOO0O0O000000000 ['status']==200 :#line:106
                        print ('登录成功')#line:107
                        return OOOO0O0O000000000 ['data']['token']#line:108
                    if OOOO0O0O000000000 ['status']==500 :#line:109
                        print (OOOO0O0O000000000 ['message'])#line:110
    except Exception as OOO00000O0OOOO0OO :#line:112
        print (OOO00000O0OOOO0OO )#line:113
def addtask (OO0OOOOOO0O0000O0 ,OO0000OO00OO0O000 ,OO0OO00OO0O00000O ):#line:117
    OO0OOOO0O00000000 =post_qrcode ()#line:118
    O00000000OOO000OO =f'zcgqewm=https://open.weixin.qq.com/connect/confirm?uuid={OO0OOOO0O00000000}'#line:119
    OOOO0O00O0OOOOOO0 ={'Charset':'UTF-8','Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Cache-Control':'no-cache','accept':'application/json,text/html','Content-Length':'86','User-Agent':'Dalvik/2.1.0(Linux;U;Android12;2201122CBuild/SKQ1.211006.001)','Host':'39.108.184.87','Connection':'Keep-Alive','Accept-Encoding':'gzip',}#line:123
    try :#line:124
        OOO000O0OO0OOOO0O =requests .post (f'{host}/api/addtask.asp?username={OO0OOOOOO0O0000O0}&password={OO0000OO00OO0O000}&zcsqrwid={OO0OO00OO0O00000O}',headers =OOOO0O00O0OOOOOO0 ,data =O00000000OOO000OO ).json ()#line:125
        if 'msg'in OOO000O0OO0OOOO0O :#line:127
            print (f'提交任务:{OOO000O0OO0OOOO0O["msg"]}')#line:128
        O0OOO0O0OO000O00O =post_code (OO0OOOO0O00000000 ,OO0OOOOOO0O0000O0 ,OO0000OO00OO0O000 ,OO0OO00OO0O00000O )#line:129
        if O0OOO0O0OO000O00O :#line:130
            return post_dl (O0OOO0O0OO000O00O )#line:131
    except Exception as OO0O0OOOOO00000O0 :#line:132
        print (OO0O0OOOOO00000O0 )#line:133
