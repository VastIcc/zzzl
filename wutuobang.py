# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import requests
    import random
    import datetime
    import threading
except Exception as e:
    t = re.findall("d '(.*?)'", str(e))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ 项目地址  http://www.xishishequ.com/h5/reg.html?invite_code=B83R2W
@ 抓去域名  http://www.xishishequ.com    Authorization的值 不带Bearer
@ 青龙变量 export smytoken="wtbtoken"     多号换行
@ cron: 8 */12 * * *
@ new Env('乌托邦')
"""
application = 'wtbtoken'  # 变量名
token = ''  # 调试token


##################################下面不要动##################################
host ='http://www.xishishequ.com'#line:1
mobile =0 #line:2
def start ():#line:3
    try :#line:4
        OOOOOO000OOOOO000 =os_qinglong ()#line:5
        print (f"==========共找到{len(OOOOOO000OOOOO000)}个账号==========")#line:6
        for OO000OO0O0O0OO000 in OOOOOO000OOOOO000 :#line:7
            print (f"------------正在执行第{OOOOOO000OOOOO000.index(OO000OO0O0O0OO000) + 1}个账号------------")#line:8
            OO000OOO00OOOOO0O =wtbw (OO000OO0O0O0OO000 )#line:9
            def OOOOO000000O0O00O ():#line:11
                if OO000OOO00OOOOO0O .base_info ():#line:13
                    OO000OOO00OOOOO0O .mining_over ()#line:15
                    OO000OOO00OOOOO0O .mining ()#line:17
                    time .sleep (random .randint (1 ,2 ))#line:18
                else :#line:19
                    print ('token失效')#line:20
            OO00000O000O0O0O0 =threading .Thread (target =OOOOO000000O0O00O )#line:22
            OO00000O000O0O0O0 .start ()#line:23
            time .sleep (random .randint (5 ,8 ))#line:24
    except Exception as OO0000000OOOOOO00 :#line:25
        print (OO0000000OOOOOO00 )#line:26
def login ():#line:29
    try :#line:30
        OO0OO0O00OOOO0O00 ={'login':'','type':'2','password':'',}#line:35
        OOO0O000OO0O00O00 ={'os':'android','Version-Code':'1','Client-Version':'1.0.0','datetime':str (datetime .datetime .now ())[:23 ],'Accept':'application/json','Content-Type':'application/x-www-form-urlencoded','Content-Length':'61','Host':'www.xishishequ.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.12.13'}#line:48
        OO0O0O00O0O0O00O0 =requests .request ('post',f'{host}/api/v2/auth/login',headers =OOO0O000OO0O00O00 ,data =OO0OO0O00OOOO0O00 ).json ()#line:49
        print (OO0O0O00O0O0O00O0 )#line:50
        OO00O000OO0OOO000 =OO0O0O00O0O0O00O0 ['access_token']#line:51
        print (OO00O000OO0OOO000 )#line:52
        return True #line:53
    except Exception as OOOOOO000O0O00O00 :#line:54
        print (OOOOOO000O0O00O00 )#line:55
class wtbw :#line:58
    def __init__ (OOO0OO00O0OOOOO00 ,OOO00OO0OOOO0OO00 ):#line:60
        try :#line:61
            OOO0OO00O0OOOOO00 .token =OOO00OO0OOOO0OO00 #line:62
            OOO0OO00O0OOOOO00 .headers ={'os':'android','Version-Code':'1','Client-Version':'1.0.0','datetime':str (datetime .datetime .now ())[:23 ],'Accept':'application/json','Authorization':f'Bearer {OOO0OO00O0OOOOO00.token}','Content-Length':'0','Host':'www.xishishequ.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.12.13',}#line:75
        except Exception as OO000OOOOO0OOOO00 :#line:76
            print ('变量格式错误')#line:77
    def base_info (O00OOO00O0O0000OO ):#line:80
        try :#line:81
            OOO00000O0OO00O0O =requests .request ('get',f'{host}/api/v2/user',headers =O00OOO00O0O0000OO .headers ).json ()#line:82
            if 'id'in OOO00000O0OO00O0O :#line:84
                O0OO00OOOOOO00000 =OOO00000O0OO00O0O ['id']#line:85
                OOO0OOO0OO00OOO00 =OOO00000O0OO00O0O ['name']#line:86
                print (f'【账号信息】:ID:{O0OO00OOOOOO00000}丨昵称:{OOO0OOO0OO00OOO00}')#line:87
                return True #line:88
            return False #line:89
        except Exception as O00O000O00OO0OOO0 :#line:90
            print (123 )#line:91
    def mining_over (O0000OO0OO0O000O0 ):#line:94
        try :#line:95
            O0OOOOOO00000O000 =requests .request ('post',f'{host}/api/v2/mining/over',headers =O0000OO0OO0O000O0 .headers ).json ()#line:96
            if 'message'in O0OOOOOO00000O000 :#line:98
                print (f'【开启收益】:{O0OOOOOO00000O000["message"]}')#line:99
                if '正在收益中'!=O0OOOOOO00000O000 ['message']:#line:100
                    OOO0O000000O00O0O =requests .request ('post',f'{host}/api/v2/mining/start',headers =O0000OO0OO0O000O0 .headers ).json ()#line:101
                    if 'start_mining'in OOO0O000000O00O0O :#line:103
                        print (f'【开启收益】:{OOO0O000000O00O0O["start_mining"]}')#line:104
        except Exception as OOO0OO0O00O0000OO :#line:106
            print (OOO0OO0O00O0000OO )#line:107
    def mining (O0O0O0O0O00OOOO0O ):#line:111
        try :#line:112
            O0OO0OOO00O0OO00O =requests .request ('get',f'{host}/api/v2/mining',headers =O0O0O0O0O00OOOO0O .headers ).json ()#line:113
            if 'total_income'in O0OO0OOO00O0OO00O :#line:115
                O00OOO000O000O0O0 =O0OO0OOO00O0OO00O ['total_income']#line:116
                O0O0OO0000O000O00 =O0OO0OOO00O0OO00O ['current_income']#line:117
                OOOOOO0OO0000OOOO =float (O0OO0OOO00O0OO00O ['count_down'])/60 #line:118
                print (f'【收益查询】:总收益:{float(O00OOO000O000O0O0)}丨实时收益:{float(O0O0OO0000O000O00)}丨收益剩余:{int(OOOOOO0OO0000OOOO)}分钟')#line:119
                if OOOOOO0OO0000OOOO <10 :#line:120
                    time .sleep (O0O0OO0000O000O00 )#line:121
                    time .sleep (random .randint (3 ,8 ))#line:122
                    O0O0O0O0O00OOOO0O .mining_over ()#line:123
        except Exception as OO000O0OOOO000OOO :#line:124
            print (OO000O0OOOO000OOO )#line:125
def os_qinglong ():#line:130
    if application in os .environ :#line:131
        OO00000OOOO00OOO0 =os .environ [application ].split ('\n')#line:132
        if len (OO00000OOOO00OOO0 )>0 :#line:133
            return OO00000OOOO00OOO0 #line:134
        else :#line:135
            print (f"{application}变量未启用")#line:136
            print ('脚本退出')#line:137
            sys .exit (1 )#line:138
    else :#line:139
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='wtbtoken'\n尝试使用内置变量")#line:140
        return os_built ()#line:141
def os_built ():#line:144
    if token :#line:145
        O0O00O0O00OOO0O0O =token .split ('\n')#line:146
        if len (O0O00O0O00OOO0O0O )>0 :#line:147
            return O0O00O0O00OOO0O0O #line:148
    else :#line:149
        print (f"内置变量为空")#line:150
        print ('脚本结束')#line:151
        sys .exit (0 )#line:152
if __name__ =='__main__':#line:155
    start ()#line:156
