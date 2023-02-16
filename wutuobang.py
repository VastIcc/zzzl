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

time_xx = random.randint(5, 8)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行


##################################下面不要动##################################
host ='http://www.xishishequ.com'#line:1
mobile =0 #line:2
def start ():#line:3
    try :#line:4
        O0OO0O0O000OO000O =os_qinglong ()#line:5
        print (f"==========共找到{len(O0OO0O0O000OO000O)}个账号==========")#line:6
        for OOOO0000OOOOO0000 in O0OO0O0O000OO000O :#line:7
            print (f"------------正在执行第{O0OO0O0O000OO000O.index(OOOO0000OOOOO0000) + 1}个账号------------")#line:8
            O0OO0O0O000OO000O =Template (OOOO0000OOOOO0000 )#line:9
            def O00OO0O0O00O0000O ():#line:11
                if O0OO0O0O000OO000O .base_info ():#line:13
                    O0OO0O0O000OO000O .mining_over ()#line:15
                    O0OO0O0O000OO000O .mining ()#line:17
                    time .sleep (random .randint (1 ,2 ))#line:19
                else :#line:20
                    print ('token失效')#line:21
            O0O0O0O0000O00O00 =threading .Thread (target =O00OO0O0O00O0000O )#line:23
            O0O0O0O0000O00O00 .start ()#line:24
            time .sleep (time_xx )#line:25
    except Exception as O0000O0O0O0O00O00 :#line:26
        print (O0000O0O0O0O00O00 )#line:27
def login ():#line:30
    try :#line:31
        OO0OOO0OOO0000O0O ={'login':'','type':'2','password':'',}#line:36
        OOO0OO00OO0O00OO0 ={'os':'android','Version-Code':'1','Client-Version':'1.0.0','datetime':str (datetime .datetime .now ())[:23 ],'Accept':'application/json','Content-Type':'application/x-www-form-urlencoded','Content-Length':'61','Host':'www.xishishequ.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.12.13'}#line:49
        OOOO00000OOO0OO0O =requests .request ('post',f'{host}/api/v2/auth/login',headers =OOO0OO00OO0O00OO0 ,data =OO0OOO0OOO0000O0O ).json ()#line:50
        print (OOOO00000OOO0OO0O )#line:51
        O0O0OO0OO0OO0OO00 =OOOO00000OOO0OO0O ['access_token']#line:52
        print (O0O0OO0OO0OO0OO00 )#line:53
        return True #line:54
    except Exception as O0O0OO0OO0OOOOO0O :#line:55
        print (O0O0OO0OO0OOOOO0O )#line:56
class Template :#line:59
    def __init__ (O0OOO0000OOOOO0OO ,O0OO000OOOOOOOOOO ):#line:61
        try :#line:62
            O0OOO0000OOOOO0OO .token =O0OO000OOOOOOOOOO #line:63
            O0OOO0000OOOOO0OO .headers ={'os':'android','Version-Code':'1','Client-Version':'1.0.0','datetime':str (datetime .datetime .now ())[:23 ],'Accept':'application/json','Authorization':f'Bearer {O0OOO0000OOOOO0OO.token}','Content-Length':'0','Host':'www.xishishequ.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.12.13',}#line:76
        except Exception as OO0OOOO000OO00OOO :#line:77
            print ('变量格式错误')#line:78
    def base_info (OO0OO0O00OO000000 ):#line:81
        try :#line:82
            O0O00O0O00O00OOOO =requests .request ('get',f'{host}/api/v2/user',headers =OO0OO0O00OO000000 .headers ).json ()#line:83
            if 'id'in O0O00O0O00O00OOOO :#line:85
                OOOOO0OO00OOOOO00 =O0O00O0O00O00OOOO ['id']#line:86
                O0OO0OO000O0OOO00 =O0O00O0O00O00OOOO ['name']#line:87
                print (f'【账号信息】:ID:{OOOOO0OO00OOOOO00}丨昵称:{O0OO0OO000O0OOO00}')#line:88
                return True #line:89
            return False #line:90
        except Exception as OO00O00OOO0OOO0O0 :#line:91
            print (OO00O00OOO0OOO0O0 )#line:92
    def mining_over (OOOO00O00O0OO00OO ):#line:95
        OOOOOO0OO0O0O0OO0 =requests .request ('post',f'{host}/api/v2/mining/over',headers =OOOO00O00O0OO00OO .headers ).json ()#line:96
        if 'message'in OOOOOO0OO0O0O0OO0 :#line:98
            print (f'【开启收益】:{OOOOOO0OO0O0O0OO0["message"]}')#line:99
            if '正在收益中'!=OOOOOO0OO0O0O0OO0 ['message']:#line:100
                O00OOOO0OO0000O0O =requests .request ('post',f'{host}/api/v2/mining/start',headers =OOOO00O00O0OO00OO .headers ).json ()#line:101
                if 'start_mining'in O00OOOO0OO0000O0O :#line:103
                    print (f'【开启收益】:{O00OOOO0OO0000O0O["start_mining"]}')#line:104
    def mining (O0OO0O0000O000OOO ):#line:107
        O0O00O0000000OO0O =requests .request ('get',f'{host}/api/v2/mining',headers =O0OO0O0000O000OOO .headers ).json ()#line:108
        if 'total_income'in O0O00O0000000OO0O :#line:110
            OO000OO00O0000OO0 =O0O00O0000000OO0O ['total_income']#line:111
            OOOOOOO0000O0O000 =O0O00O0000000OO0O ['current_income']#line:112
            OOOO0O00OO0O0OOOO =float (O0O00O0000000OO0O ['count_down'])/60 #line:113
            print (f'【收益查询】:总收益:{float(OO000OO00O0000OO0)}丨实时收益:{float(OOOOOOO0000O0O000)}丨收益剩余:{int(OOOO0O00OO0O0OOOO)}分钟')#line:114
            if OOOO0O00OO0O0OOOO <10 :#line:115
                time .sleep (OOOOOOO0000O0O000 )#line:116
                time .sleep (random .randint (3 ,8 ))#line:117
                O0OO0O0000O000OOO .mining_over ()#line:118
def os_qinglong ():#line:124
    if application in os .environ :#line:125
        O0OOOOO0000O0OOO0 =os .environ [application ].split ('\n')#line:126
        if len (O0OOOOO0000O0OOO0 )>0 :#line:127
            return O0OOOOO0000O0OOO0 #line:128
        else :#line:129
            print (f"{application}变量未启用")#line:130
            print ('脚本退出')#line:131
            sys .exit (1 )#line:132
    else :#line:133
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='wtbtoken'\n尝试使用内置变量")#line:134
        return os_built ()#line:135
def os_built ():#line:138
    if token :#line:139
        O00000O0O00OOO000 =token .split ('\n')#line:140
        if len (O00000O0O00OOO000 )>0 :#line:141
            return O00000O0O00OOO000 #line:142
    else :#line:143
        print (f"内置变量为空")#line:144
        print ('脚本结束')#line:145
        sys .exit (0 )#line:146
if __name__ =='__main__':#line:149
    start ()#line:150
