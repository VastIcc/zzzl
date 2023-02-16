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
        OO0OOOO0OOOOOO0OO =os_qinglong ()#line:5
        print (f"==========共找到{len(OO0OOOO0OOOOOO0OO)}个账号==========")#line:6
        for O000OOOO0O0O0OOOO in OO0OOOO0OOOOOO0OO :#line:7
            print (f"------------正在执行第{OO0OOOO0OOOOOO0OO.index(O000OOOO0O0O0OOOO) + 1}个账号------------")#line:8
            OOO00OO000OOO00O0 =wtbw (O000OOOO0O0O0OOOO )#line:9
            def OO00000O0O0OOOOO0 ():#line:11
                if OOO00OO000OOO00O0 .base_info ():#line:13
                    OOO00OO000OOO00O0 .mining_over ()#line:15
                    OOO00OO000OOO00O0 .mining ()#line:17
                    time .sleep (random .randint (1 ,2 ))#line:18
                else :#line:19
                    print ('token失效')#line:20
            OO00OOO00O0OO0000 =threading .Thread (target =OO00000O0O0OOOOO0 )#line:22
            OO00OOO00O0OO0000 .start ()#line:23
            time .sleep (random .randint (5 ,8 ))#line:24
    except Exception as O0O0000O0O0O0OOOO :#line:25
        print (O0O0000O0O0O0OOOO )#line:26
def login ():#line:29
    try :#line:30
        O000O000OO000O0OO ={'login':'','type':'2','password':'',}#line:35
        O000O00O0OOO00000 ={'os':'android','Version-Code':'1','Client-Version':'1.0.0','datetime':str (datetime .datetime .now ())[:23 ],'Accept':'application/json','Content-Type':'application/x-www-form-urlencoded','Content-Length':'61','Host':'www.xishishequ.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.12.13'}#line:48
        OOO00OOO0OO0OOO00 =requests .request ('post',f'{host}/api/v2/auth/login',headers =O000O00O0OOO00000 ,data =O000O000OO000O0OO ).json ()#line:49
        print (OOO00OOO0OO0OOO00 )#line:50
        O0000000O00O0O000 =OOO00OOO0OO0OOO00 ['access_token']#line:51
        print (O0000000O00O0O000 )#line:52
        return True #line:53
    except Exception as OOO000O0O00OOO000 :#line:54
        print (OOO000O0O00OOO000 )#line:55
class wtbw :#line:58
    def __init__ (OO000OOOO0000OOO0 ,O00O0O0OO00OO0OO0 ):#line:60
        try :#line:61
            OO000OOOO0000OOO0 .token =O00O0O0OO00OO0OO0 #line:62
            OO000OOOO0000OOO0 .headers ={'os':'android','Version-Code':'1','Client-Version':'1.0.0','datetime':str (datetime .datetime .now ())[:23 ],'Accept':'application/json','Authorization':f'Bearer {OO000OOOO0000OOO0.token}','Content-Length':'0','Host':'www.xishishequ.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.12.13',}#line:75
        except Exception as O0OOO00O00000OO0O :#line:76
            print ('变量格式错误')#line:77
    def base_info (O000O0OO00000OOOO ):#line:80
        try :#line:81
            O0OOOOOO0O0OO000O =requests .request ('get',f'{host}/api/v2/user',headers =O000O0OO00000OOOO .headers ).json ()#line:82
            if 'id'in O0OOOOOO0O0OO000O :#line:84
                OOOO0O0OO0OOO00OO =O0OOOOOO0O0OO000O ['id']#line:85
                O0OO0O0O0OO0OO000 =O0OOOOOO0O0OO000O ['name']#line:86
                print (f'【账号信息】:ID:{OOOO0O0OO0OOO00OO}丨昵称:{O0OO0O0O0OO0OO000}')#line:87
                return True #line:88
            return False #line:89
        except Exception as O0OOO00OOOO0O0O0O :#line:90
            print (123 )#line:91
    def mining_over (O0O0OOOO0O0OOO000 ):#line:94
        try :#line:95
            O0O0O00O00O0O0O0O =requests .request ('post',f'{host}/api/v2/mining/over',headers =O0O0OOOO0O0OOO000 .headers ).json ()#line:96
            if 'message'in O0O0O00O00O0O0O0O :#line:98
                print (f'【开启收益】:{O0O0O00O00O0O0O0O["message"]}')#line:99
                if '正在收益中'!=O0O0O00O00O0O0O0O ['message']:#line:100
                    O0O0OO00O0O0OO0O0 =requests .request ('post',f'{host}/api/v2/mining/start',headers =O0O0OOOO0O0OOO000 .headers ).json ()#line:101
                    if 'start_mining'in O0O0OO00O0O0OO0O0 :#line:103
                        print (f'【开启收益】:{O0O0OO00O0O0OO0O0["start_mining"]}')#line:104
        except Exception as OOO0OOO0O0O00O000 :#line:106
            print (OOO0OOO0O0O00O000 )#line:107
    def mining (O00O0OOOO0000OOO0 ):#line:111
        try :#line:112
            OO0OOOOOOO0O000O0 =requests .request ('get',f'{host}/api/v2/mining',headers =O00O0OOOO0000OOO0 .headers ).json ()#line:113
            if 'total_income'in OO0OOOOOOO0O000O0 :#line:115
                O0O00OO000OO0OO00 =OO0OOOOOOO0O000O0 ['total_income']#line:116
                O00000O0OOO0000OO =OO0OOOOOOO0O000O0 ['current_income']#line:117
                O0OO0OOOOO000OOO0 =float (OO0OOOOOOO0O000O0 ['count_down'])/60 #line:118
                print (f'【收益查询】:总收益:{str(O0O00OO000OO0OO00).split(".")[0]}丨实时收益:{str(O00000O0OOO0000OO).split(".")[0]}丨收益剩余:{int(O0OO0OOOOO000OOO0)}分钟')#line:119
                if O0OO0OOOOO000OOO0 <10 :#line:120
                    time .sleep (O00000O0OOO0000OO )#line:121
                    time .sleep (random .randint (3 ,8 ))#line:122
                    O00O0OOOO0000OOO0 .mining_over ()#line:123
        except Exception as O0O000O0OO0OOO000 :#line:124
            print (O0O000O0OO0OOO000 )#line:125
def os_qinglong ():#line:130
    if application in os .environ :#line:131
        OOO0OOOOO00OO0OOO =os .environ [application ].split ('\n')#line:132
        if len (OOO0OOOOO00OO0OOO )>0 :#line:133
            return OOO0OOOOO00OO0OOO #line:134
        else :#line:135
            print (f"{application}变量未启用")#line:136
            print ('脚本退出')#line:137
            sys .exit (1 )#line:138
    else :#line:139
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='wtbtoken'\n尝试使用内置变量")#line:140
        return os_built ()#line:141
def os_built ():#line:144
    if token :#line:145
        OO00OOOOO00O0O000 =token .split ('\n')#line:146
        if len (OO00OOOOO00O0O000 )>0 :#line:147
            return OO00OOOOO00O0O000 #line:148
    else :#line:149
        print (f"内置变量为空")#line:150
        print ('脚本结束')#line:151
        sys .exit (0 )#line:152
if __name__ =='__main__':#line:155
    start ()#line:156
