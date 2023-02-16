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
        OO0O0000OO00OO000 =os_qinglong ()#line:5
        print (f"==========共找到{len(OO0O0000OO00OO000)}个账号==========")#line:6
        for OOO0000000O00OOOO in OO0O0000OO00OO000 :#line:7
            print (f"------------正在执行第{OO0O0000OO00OO000.index(OOO0000000O00OOOO) + 1}个账号------------")#line:8
            O0O00O0O000O0OO00 =wtbw (OOO0000000O00OOOO )#line:9
            def OOOO0OOO0O0OO0O00 ():#line:11
                if O0O00O0O000O0OO00 .base_info ():#line:13
                    O0O00O0O000O0OO00 .mining_over ()#line:15
                    O0O00O0O000O0OO00 .mining ()#line:17
                    time .sleep (random .randint (1 ,2 ))#line:18
                else :#line:19
                    print ('token失效')#line:20
            O000000OO0OOO0OO0 =threading .Thread (target =OOOO0OOO0O0OO0O00 )#line:22
            O000000OO0OOO0OO0 .start ()#line:23
            time .sleep (random .randint (5 ,8 ))#line:24
    except Exception as O0OOO00OOOOO00O00 :#line:25
        print (O0OOO00OOOOO00O00 )#line:26
def login ():#line:29
    try :#line:30
        OOO0O00O0O0O00O0O ={'login':'','type':'2','password':'',}#line:35
        O0OOO000OOO00O0OO ={'os':'android','Version-Code':'1','Client-Version':'1.0.0','datetime':str (datetime .datetime .now ())[:23 ],'Accept':'application/json','Content-Type':'application/x-www-form-urlencoded','Content-Length':'61','Host':'www.xishishequ.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.12.13'}#line:48
        O0OOO0OOOO0OO0O00 =requests .request ('post',f'{host}/api/v2/auth/login',headers =O0OOO000OOO00O0OO ,data =OOO0O00O0O0O00O0O ).json ()#line:49
        print (O0OOO0OOOO0OO0O00 )#line:50
        OO0O00OO00OOOO000 =O0OOO0OOOO0OO0O00 ['access_token']#line:51
        print (OO0O00OO00OOOO000 )#line:52
        return True #line:53
    except Exception as O00O0OO0O00O000OO :#line:54
        print (O00O0OO0O00O000OO )#line:55
class wtbw :#line:58
    def __init__ (O0OOOOO0OOO0O0OO0 ,OOOO00O0OOO000O00 ):#line:60
        try :#line:61
            O0OOOOO0OOO0O0OO0 .token =OOOO00O0OOO000O00 #line:62
            O0OOOOO0OOO0O0OO0 .headers ={'os':'android','Version-Code':'1','Client-Version':'1.0.0','datetime':str (datetime .datetime .now ())[:23 ],'Accept':'application/json','Authorization':f'Bearer {O0OOOOO0OOO0O0OO0.token}','Content-Length':'0','Host':'www.xishishequ.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.12.13',}#line:75
        except Exception as OOO0OO0O0OO000OO0 :#line:76
            print ('变量格式错误')#line:77
    def base_info (OOO0O000000O000O0 ):#line:80
        try :#line:81
            OO00OO00OOO0O00OO =requests .request ('get',f'{host}/api/v2/user',headers =OOO0O000000O000O0 .headers ).json ()#line:82
            if 'id'in OO00OO00OOO0O00OO :#line:84
                O0OO0OOOO0O0O0OOO =OO00OO00OOO0O00OO ['id']#line:85
                O0O0OOOOO00O000OO =OO00OO00OOO0O00OO ['name']#line:86
                print (f'【账号信息】:ID:{O0OO0OOOO0O0O0OOO}丨昵称:{O0O0OOOOO00O000OO}')#line:87
                return True #line:88
            return False #line:89
        except Exception as O0O000OOOO0O0OO00 :#line:90
            print (123 )#line:91
    def mining_over (OO0OOOOOOO0000OO0 ):#line:94
        try :#line:95
            O00OO0OO0OOO0000O =requests .request ('post',f'{host}/api/v2/mining/over',headers =OO0OOOOOOO0000OO0 .headers ).json ()#line:96
            if 'message'in O00OO0OO0OOO0000O :#line:98
                print (f'【开启收益】:{O00OO0OO0OOO0000O["message"]}')#line:99
                if '正在收益中'!=O00OO0OO0OOO0000O ['message']:#line:100
                    O0OOO0O0000OO0OOO =requests .request ('post',f'{host}/api/v2/mining/start',headers =OO0OOOOOOO0000OO0 .headers ).json ()#line:101
                    if 'start_mining'in O0OOO0O0000OO0OOO :#line:103
                        print (f'【开启收益】:{O0OOO0O0000OO0OOO["start_mining"]}')#line:104
        except Exception as OOO0OO0O00O000OO0 :#line:106
            print (OOO0OO0O00O000OO0 )#line:107
    def mining (OOOOO0000O000OOO0 ):#line:111
        try :#line:112
            OO0OOO0O0000OO0OO =requests .request ('get',f'{host}/api/v2/mining',headers =OOOOO0000O000OOO0 .headers ).json ()#line:113
            if 'total_income'in OO0OOO0O0000OO0OO :#line:115
                OO0000OOOOOO0O00O =OO0OOO0O0000OO0OO ['total_income']#line:116
                OO0O0O0O0O0OOOOO0 =OO0OOO0O0000OO0OO ['current_income']#line:117
                O0OOOO00000OO0O0O =float (OO0OOO0O0000OO0OO ['count_down'])/60 #line:118
                print (f'【收益查询】:总收益:{int(OO0000OOOOOO0O00O)}丨实时收益:{int(OO0O0O0O0O0OOOOO0)}丨收益剩余:{int(O0OOOO00000OO0O0O)}分钟')#line:119
                if O0OOOO00000OO0O0O <10 :#line:120
                    time .sleep (OO0O0O0O0O0OOOOO0 )#line:121
                    time .sleep (random .randint (3 ,8 ))#line:122
                    OOOOO0000O000OOO0 .mining_over ()#line:123
        except Exception as O0O00O0OO0000OO0O :#line:124
            print (O0O00O0OO0000OO0O )#line:125
def os_qinglong ():#line:130
    if application in os .environ :#line:131
        OOOO0000OOOOO0O00 =os .environ [application ].split ('\n')#line:132
        if len (OOOO0000OOOOO0O00 )>0 :#line:133
            return OOOO0000OOOOO0O00 #line:134
        else :#line:135
            print (f"{application}变量未启用")#line:136
            print ('脚本退出')#line:137
            sys .exit (1 )#line:138
    else :#line:139
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='wtbtoken'\n尝试使用内置变量")#line:140
        return os_built ()#line:141
def os_built ():#line:144
    if token :#line:145
        O0O0O00OOOO0O00O0 =token .split ('\n')#line:146
        if len (O0O0O00OOOO0O00O0 )>0 :#line:147
            return O0O0O00OOOO0O00O0 #line:148
    else :#line:149
        print (f"内置变量为空")#line:150
        print ('脚本结束')#line:151
        sys .exit (0 )#line:152
if __name__ =='__main__':#line:155
    start ()#line:156
