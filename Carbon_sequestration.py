# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import requests
    import random
except Exception as e:
    t = re.findall("d '(.*?)'", str(e))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: 8 9,15,20 * * *
@ new Env('碳汇世界')
@ 项目地址  https://h5.thxq888.com/register/index.html?invitecode=896428
@ 抓包域名  https://api.thxq888.com的cookie值，m-ii值，user-agent值
@ 青龙变量 export thcookie="cookie&m-ii&user-agent"     多号换行
"""
application = 'thcookie'  # 变量名
token = ''  # 调试token



##################################下面不要动##################################
host ='https://api.thxq888.com'#line:1
mobile =0 #line:2
def start ():#line:5
    try :#line:6
        O0OOOO00O000O0000 =os_qinglong ()#line:7
        print (f"==========共找到{len(O0OOOO00O000O0000)}个账号==========")#line:8
        for OO000OOOOO0OO00OO in O0OOOO00O000O0000 :#line:9
            print (f"------------正在执行第{O0OOOO00O000O0000.index(OO000OOOOO0OO00OO) + 1}个账号------------")#line:10
            OOOO0OOOO000O000O =Template (OO000OOOOO0OO00OO )#line:11
            if OOOO0OOOO000O000O .base_info ():#line:13
                OOOO0OOOO000O000O .get_home_index ()#line:15
                OOOO0OOOO000O000O .get_index ()#line:17
                time .sleep (random .randint (3 ,5 ))#line:20
            else :#line:21
                print ('token失效')#line:22
    except Exception as O0O0O00OO0OO0O0O0 :#line:23
        print (O0O0O00OO0OO0O0O0 )#line:24
class Template :#line:27
    def __init__ (OOO0OO000O0000000 ,OO0OO0OO000000OO0 ):#line:29
        try :#line:30
            OOO0OO000O0000000 .cookie =OO0OO0OO000000OO0 .split ('&')[0 ]#line:31
            OOO0OO000O0000000 .mii =OO0OO0OO000000OO0 .split ('&')[1 ]#line:32
            OOO0OO000O0000000 .ua =OO0OO0OO000000OO0 .split ('&')[2 ]#line:33
            OOO0OO000O0000000 .headers ={'Host':'api.thxq888.com','content-type':'application/json;charset=UTF-8','accept-encoding':'gzip','accept':'*/*','user-agent':OOO0OO000O0000000 .ua ,'m-lng':'0.0','m-lat':'0.0','m-lt':'2','m-nw':'wifi','m-cv':'1.2','m-iv':'1.0','m-ct':'1','m-cw':'1080','m-ch':'2400','m-sr':'1','m-ii':OOO0OO000O0000000 .mii ,'m-lc':'','cookie':OOO0OO000O0000000 .cookie ,}#line:53
        except :#line:54
            print ('变量格式错误')#line:55
    def base_info (O0O0O00OOOO0OOOOO ):#line:58
        try :#line:59
            OO000OOOOOO0000OO =requests .request ('get',f'{host}/api/UserCenter/GetIndex',headers =O0O0O00OOOO0OOOOO .headers ).json ()#line:60
            if "Data"in OO000OOOOOO0000OO :#line:62
                OO00O0000OOOO0O00 =OO000OOOOOO0000OO ['Data']['UserInfo']['Name']#line:63
                OO0OO0O00OO0O0O00 =OO000OOOOOO0000OO ['Data']['LevelInfo']['Level']#line:64
                O0OOO00OOOO0OO00O =OO000OOOOOO0000OO ['Data']['Ce']#line:65
                O0O00OOOOO0OO0O0O =OO000OOOOOO0000OO ['Data']['Ci']#line:66
                OOO0OOOOO0OO00O0O =OO000OOOOOO0000OO ['Data']['FansCount']#line:67
                O00O0000O00O0OOO0 =OO000OOOOOO0000OO ['Data']['InviteCode']#line:68
                print (f'【账号信息】:昵称:{OO00O0000OOOO0O00}丨等级:{OO0OO0O00OO0O0O00}丨碳能:{O0OOO00OOOO0OO00O}丨积分:{O0O00OOOOO0OO0O0O}丨好友:{OOO0OOOOO0OO00O0O}丨邀请码:{O00O0000O00O0OOO0}')#line:69
                return True #line:70
            else :#line:71
                return False #line:72
        except Exception as OOOOOO0OOO0OOOO0O :#line:73
            print (OOOOOO0OOO0OOOO0O )#line:74
    def get_home_index (OOOOOOO00O0OOOOOO ):#line:79
        try :#line:80
            O00000OO000OOOOO0 =requests .request ('get',f'{host}/api/HomePage/GetHomeIndex',headers =OOOOOOO00O0OOOOOO .headers ).json ()#line:81
            if 'Data'in O00000OO000OOOOO0 :#line:83
                if O00000OO000OOOOO0 ['Data']['CiList']:#line:84
                    for O0OOOO0000O000OOO in O00000OO000OOOOO0 ['Data']['CiList']:#line:85
                        OO0O00000O0O00O00 =O0OOOO0000O000OOO ['Id']#line:87
                        OOOOOOO00O0OOOOOO .home_page_take (OO0O00000O0O00O00 )#line:88
                        time .sleep (random .randint (17 ,20 ))#line:89
        except Exception as OO0000O0000OOOOOO :#line:90
            print (OO0000O0000OOOOOO )#line:91
    def home_page_take (OO00O00O00O0O0000 ,O0O0O00OOOO0O0O00 ):#line:95
        try :#line:96
            OO00OO0OO00OO00OO ={"Id":O0O0O00OOOO0O0O00 }#line:97
            O0OO00OO000O0OOOO =requests .request ('post',f'{host}/api/HomePage/Take',headers =OO00O00O00O0O0000 .headers ,json =OO00OO0OO00OO00OO ).json ()#line:98
            print (O0OO00OO000O0OOOO )#line:99
            if 'Data'in O0OO00OO000O0OOOO :#line:100
                OO0O00O0OOO0O0000 =O0OO00OO000O0OOOO ['Data']['Ci']#line:102
                O0000O0OO00OO0OOO =O0OO00OO000O0OOOO ['Data']['Ce']#line:103
                print (f'【临时碳能】:收取碳积分:{OO0O00O0OOO0O0000}丨收取碳能:{O0000O0OO00OO0OOO}')#line:104
        except Exception as O0OO0OO0000O00OOO :#line:105
            print (O0OO0OO0000O00OOO )#line:106
    def get_index (O0000OO0OOO0OO0O0 ):#line:110
        try :#line:111
            for OOO0O000O0O0OO0O0 in range (5 ):#line:112
                OO0OO00000O0000OO =requests .request ('get','https://api.thxq888.com/api/FriendPage/GetIndex',headers =O0000OO0OOO0OO0O0 .headers ).json ()#line:113
                if 'Data'in OO0OO00000O0000OO :#line:115
                    if OO0OO00000O0000OO ['Data']['CiList']:#line:116
                        O0O0OOOO0O00O00O0 =OO0OO00000O0000OO ['Data']['CiList'][0 ]['Id']#line:117
                        OO00O0OO00O000O0O ={"Id":O0O0OOOO0O00O00O0 }#line:118
                        OO00000OOOOOO00OO =requests .request ('post',f'{host}/api/FriendPage/Take',headers =O0000OO0OOO0OO0O0 .headers ,json =OO00O0OO00O000O0O ).json ()#line:119
                        if 'Data'in OO00000OOOOOO00OO :#line:121
                            O0000O00OOO00OOO0 =OO00000OOOOOO00OO ['Data']['Ci']#line:122
                            print (f'【偷碳积分】:收取碳积分:{O0000O00OOO00OOO0}')#line:123
                        time .sleep (random .randint (17 ,20 ))#line:124
                    else :#line:125
                        break #line:126
        except Exception as OO0OO000OOOOOOOOO :#line:127
            print (OO0OO000OOOOOOOOO )#line:128
def os_qinglong ():#line:133
    if application in os .environ :#line:134
        OO0000O0000O0OO0O =os .environ [application ].split ('\n')#line:135
        if len (OO0000O0000O0OO0O )>0 :#line:136
            return OO0000O0000O0OO0O #line:137
        else :#line:138
            print (f"{application}变量未启用")#line:139
            print ('脚本退出')#line:140
            sys .exit (1 )#line:141
    else :#line:142
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='cookie'\n尝试使用内置变量")#line:143
        return os_built ()#line:144
def os_built ():#line:147
    if token :#line:148
        OO0OOO000OO0O0000 =token .split ('\n')#line:149
        if len (OO0OOO000OO0O0000 )>0 :#line:150
            return OO0OOO000OO0O0000 #line:151
    else :#line:152
        print (f"内置变量为空")#line:153
        print ('脚本结束')#line:154
        sys .exit (0 )#line:155
if __name__ =='__main__':#line:158
    start ()#line:159
