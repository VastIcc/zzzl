try :#line:2
    import time ,requests ,re ,hashlib ,datetime ,sys ,os ,random #line:3
except Exception as e :#line:4
    t =re .findall ("d '(.*?)'",str (e ))[0 ]#line:5
    print (f'{t}依赖未安装')#line:6
    sys .exit ()#line:7
appid ='wx7b6272c42fa733a7'#line:10
headers ={'User-Agent':'Mozilla/5.0 (Linux; Android 9; PBBT00 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 MMWEBID/3625 MicroMessenger/7.0.17.1720(0x27001134) Process/tools WeChat/arm32 NetType/4G Language/zh_CN ABI/arm64',}#line:11
host ='http://39.108.184.87'#line:12
def sign (OO0O0000OO00OO0OO ):#line:13
    O0OOOO0OO000O00OO =hashlib .md5 (OO0O0000OO00OO0OO .encode ()).hexdigest ()#line:14
    O0O0OO0OOOOOO0OOO ="scsc%^&*"+O0OOOO0OO000O00OO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:15
    O0OOOOO0000000000 =hashlib .md5 (O0O0OO0OOOOOO0OOO .encode ()).hexdigest ()#line:16
    return O0OOOOO0000000000 #line:17
def timi_new ():#line:18
    return str (int (time .time ()*1000 ))#line:19
def post_qrcode ():#line:20
    try :#line:21
        O0O00O00000O00OO0 =requests .post (f'http://open.weixin.qq.com/connect/app/qrconnect?appid={appid}&bundleid=(null)&scope=snsapi_userinfo&state=w&from=message&isappinstalled=0',headers =headers ).text #line:24
        O0000000OO0O000OO =re .findall ('auth_qrcode" src="(.*?)" />',O0O00O00000O00OO0 )[0 ]#line:25
        OOOO0OO000O0OOOOO =O0000000OO0O000OO .split ('qrcode/')[1 ]#line:26
        return OOOO0OO000O0OOOOO #line:27
    except Exception as O0OOO0OO0O00000OO :#line:28
        print (O0OOO0OO0O00000OO )#line:29
def gettasklist (OO00OOOOOOO0OO0OO ,OO0OO000O00O000O0 ,OOOO0OOO0OOOO000O ):#line:30
    try :#line:31
        OO00OOO0OO0OO00O0 =requests .request ('get',f'{host}/api/gettasklist.asp?username={OO00OOOOOOO0OO0OO}&password={OO0OO000O00O000O0}&page=1&y=1&appid={appid}&k={OOOO0OOO0OOOO000O}').json ()#line:33
        if OO00OOO0OO0OO00O0 ['ret']=='0':#line:35
            print (f"任务状态:{OO00OOO0OO0OO00O0['date'][0]['State']}")#line:36
            if OO00OOO0OO0OO00O0 ['date'][0 ]['State']=='二维码已失效'or OO00OOO0OO0OO00O0 ['date'][0 ]['State']=='管理员终止':#line:37
                return True #line:38
        return False #line:39
    except Exception as OOO00000O000O000O :#line:40
        print (OOO00000O000O000O )#line:41
def post_code (OO0000OO00O000000 ,O00OO0OOOOOO0O0O0 ,OO0O000O0O0OO0O00 ,OO00O00000OO00O0O ):#line:42
    O00OOO0OO0000OOO0 =int (time .time ())#line:43
    try :#line:44
        while True :#line:45
            if gettasklist (O00OO0OOOOOO0O0O0 ,OO0O000O0O0OO0O00 ,OO00O00000OO00O0O ):#line:46
                return False #line:47
            OO0O0OOO00OO0OO00 =requests .post (f'http://long.open.weixin.qq.com/connect/l/qrconnect?uuid={OO0000OO00O000000}&_={O00OOO0OO0000OOO0})',headers =headers ).text #line:48
            if '405'in OO0O0OOO00OO0OO00 :#line:49
                O0OOOO0O00000OO0O =re .findall ("wx_code='(.*?)';",OO0O0OOO00OO0OO00 )[0 ]#line:50
                return O0OOOO0O00000OO0O #line:51
            time .sleep (3 )#line:52
    except Exception as OOOO0O0O0OOO000O0 :#line:53
        print (OOOO0O0O0OOO000O0 )#line:54
def post_dl (OO000OOOO0OOO00OO ):#line:55
    try :#line:56
        OOOOO000O00O00OO0 =f'__{timi_new()}'#line:57
        O00OOOO0OO0O0O000 ={'timestamp':str (timi_new ()),'sign':sign (OOOOO000O00O00OO0 ),'signstring':OOOOO000O00O00OO0 ,'version':'3.1.4195311','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:66
        OOO0O00OO00OO0OOO =requests .request ('get','http://scsc.sc19319.com/loginToken',headers =O00OOOO0OO0O0O000 ).json ()#line:67
        if 'status'in OOO0O00OO00OO0OOO :#line:68
            if OOO0O00OO00OO0OOO ['status']==200 :#line:69
                O00O000O000O00OOO ={"loginToken":OOO0O00OO00OO0OOO ['data'],"code":OO000OOOO0OOO00OO ,"loginType":"生成世朝"}#line:74
                OO0OOO000O00O0000 =f'_code={OO000OOOO0OOO00OO}&loginToken={OOO0O00OO00OO0OOO["data"]}&loginType=_{timi_new()}'#line:75
                OOOO0000OOOO00000 ={'timestamp':str (timi_new ()),'sign':sign (OO0OOO000O00O0000 ),'signstring':OO0OOO000O00O0000 ,'version':'3.1.4195311','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:84
                O0O00OO0000OO0OO0 =requests .request ('post','http://scsc.sc19319.com/login',headers =OOOO0000OOOO00000 ,data =O00O000O000O00OOO ).json ()#line:85
                if 'status'in O0O00OO0000OO0OO0 :#line:86
                    if O0O00OO0000OO0OO0 ['status']==200 :#line:87
                        print ('登录成功')#line:88
                        return O0O00OO0000OO0OO0 ['data']['token']#line:89
                    if O0O00OO0000OO0OO0 ['status']==500 :#line:90
                        print (O0O00OO0000OO0OO0 ['message'])#line:91
    except Exception as O00O000OO0OOOO0OO :#line:93
        print (O00O000OO0OOOO0OO )#line:94
def addtask (OO00OOOOO0O0OOO0O ,O0O0O0O0O00O0O000 ,OOOOO00O00OOOOO00 ):#line:98
    OOO0OOO0O00OOOO0O =post_qrcode ()#line:99
    OO0O0OO0OOOO0OOO0 =f'zcgqewm=https://open.weixin.qq.com/connect/confirm?uuid={OOO0OOO0O00OOOO0O}'#line:100
    OO000O00OOOO0O0O0 ={'Charset':'UTF-8','Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Cache-Control':'no-cache','accept':'application/json,text/html','Content-Length':'86','User-Agent':'Dalvik/2.1.0(Linux;U;Android12;2201122CBuild/SKQ1.211006.001)','Host':'39.108.184.87','Connection':'Keep-Alive','Accept-Encoding':'gzip',}#line:104
    try :#line:105
        OO000OO0OOOO0OOOO =requests .post (f'{host}/api/addtask.asp?username={OO00OOOOO0O0OOO0O}&password={O0O0O0O0O00O0O000}&zcsqrwid={OOOOO00O00OOOOO00}',headers =OO000O00OOOO0O0O0 ,data =OO0O0OO0OOOO0OOO0 ).json ()#line:106
        if 'msg'in OO000OO0OOOO0OOOO :#line:107
            print (f'提交任务:{OO000OO0OOOO0OOOO["msg"]}')#line:108
        OO00OOO0O00O0OO00 =post_code (OOO0OOO0O00OOOO0O ,OO00OOOOO0O0OOO0O ,O0O0O0O0O00O0O000 ,OOOOO00O00OOOOO00 )#line:109
        if OO00OOO0O00O0OO00 :#line:110
            return post_dl (OO00OOO0O00O0OO00 )#line:111
    except Exception as O000OO0OO00000O0O :#line:112
        print (O000OO0OO00000O0O )#line:113
