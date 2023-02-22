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
@ new Env('碳汇世界')   Carbon_sequestration  
@ 项目地址  https://h5.thxq888.com/register/index.html?invitecode=896428
@ 抓包域名  https://api.thxq888.com的cookie值，m-ii值，user-agent值
@ 青龙变量 export thcookie="cookie&m-ii&user-agent"     多号换行
"""
application = 'thcookie'  # 变量名
token = ''  # 调试token



##################################下面不要动##################################
host ='https://api.thxq888.com'#line:1
def start ():#line:4
    try :#line:5
        O0000OOOOOO00OOO0 =os_qinglong ()#line:6
        print (f"==========共找到{len(O0000OOOOOO00OOO0)}个账号==========")#line:7
        for OO00O0O0000O0OO00 in O0000OOOOOO00OOO0 :#line:8
            print (f"------------正在执行第{O0000OOOOOO00OOO0.index(OO00O0O0000O0OO00) + 1}个账号------------")#line:9
            OOOO0O0000O00OO00 =Template (OO00O0O0000O0OO00 )#line:10
            if OOOO0O0000O00OO00 .base_info ():#line:12
                OOOO0O0000O00OO00 .get_home_index ()#line:14
                OOOO0O0000O00OO00 .get_index ()#line:16
                time .sleep (random .randint (3 ,5 ))#line:19
            else :#line:20
                print ('token失效')#line:21
    except Exception as OOOOOOOOO0OO0O00O :#line:22
        print (OOOOOOOOO0OO0O00O )#line:23
class Template :#line:26
    def __init__ (OO00OOOO0OO0000OO ,OO00OOOO00OO0O00O ):#line:28
        try :#line:29
            OO00OOOO0OO0000OO .cookie =OO00OOOO00OO0O00O .split ('&')[0 ]#line:30
            OO00OOOO0OO0000OO .mii =OO00OOOO00OO0O00O .split ('&')[1 ]#line:31
            OO00OOOO0OO0000OO .ua =OO00OOOO00OO0O00O .split ('&')[2 ]#line:32
            OO00OOOO0OO0000OO .headers ={'Host':'api.thxq888.com','content-type':'application/json;charset=UTF-8','accept-encoding':'gzip','accept':'*/*','user-agent':OO00OOOO0OO0000OO .ua ,'m-lng':'0.0','m-lat':'0.0','m-lt':'2','m-nw':'wifi','m-cv':'1.2','m-iv':'1.0','m-ct':'1','m-cw':'1080','m-ch':'2400','m-sr':'1','m-ii':OO00OOOO0OO0000OO .mii ,'m-lc':'','cookie':OO00OOOO0OO0000OO .cookie ,}#line:52
        except :#line:53
            print ('变量格式错误')#line:54
    def base_info (OO00O0OOOO0OO000O ):#line:57
        try :#line:58
            O0OOO00OOOO0O000O =requests .request ('get',f'{host}/api/UserCenter/GetIndex',headers =OO00O0OOOO0OO000O .headers ).json ()#line:59
            if "Data"in O0OOO00OOOO0O000O :#line:61
                O00O00OO00OO0OO0O =O0OOO00OOOO0O000O ['Data']['UserInfo']['Name']#line:62
                OO0OOOOO0O0OO0O0O =O0OOO00OOOO0O000O ['Data']['LevelInfo']['Level']#line:63
                O0O000O0OO00O00OO =O0OOO00OOOO0O000O ['Data']['Ce']#line:64
                O00OOO00O0O0O0O0O =O0OOO00OOOO0O000O ['Data']['Ci']#line:65
                OO00O00O00O0OO0OO =O0OOO00OOOO0O000O ['Data']['FansCount']#line:66
                OO0OOO0000O0OO00O =O0OOO00OOOO0O000O ['Data']['InviteCode']#line:67
                print (f'【账号信息】:昵称:{O00O00OO00OO0OO0O}丨等级:{OO0OOOOO0O0OO0O0O}丨碳能:{O0O000O0OO00O00OO}丨积分:{O00OOO00O0O0O0O0O}丨好友:{OO00O00O00O0OO0OO}丨邀请码:{OO0OOO0000O0OO00O}')#line:68
                return True #line:69
            else :#line:70
                return False #line:71
        except Exception as O0OOO0OO00O0O0OOO :#line:72
            print (O0OOO0OO00O0O0OOO )#line:73
    def get_home_index (O0OOOOOO00O0OO0O0 ):#line:78
        try :#line:79
            O0O0O000O00OOOOOO =requests .request ('get',f'{host}/api/HomePage/GetHomeIndex',headers =O0OOOOOO00O0OO0O0 .headers ).json ()#line:80
            if 'Data'in O0O0O000O00OOOOOO :#line:82
                if O0O0O000O00OOOOOO ['Data']['CiList']:#line:83
                    for O0O0O0000OO000OO0 in O0O0O000O00OOOOOO ['Data']['CiList']:#line:84
                        O00O0O00O0OO00O00 =O0O0O0000OO000OO0 ['Id']#line:86
                        O0OOOOOO00O0OO0O0 .home_page_take (O00O0O00O0OO00O00 )#line:87
                        time .sleep (random .randint (17 ,20 ))#line:88
        except Exception as OOOOO0OOOO00OOO0O :#line:89
            print (OOOOO0OOOO00OOO0O )#line:90
    def home_page_take (O00OOOOO000OO0OOO ,O0O00O0OOO00OOO00 ):#line:94
        try :#line:95
            OOOO0OOO000OOO0O0 ={"Id":O0O00O0OOO00OOO00 }#line:96
            O00000000O0OO00O0 =requests .request ('post',f'{host}/api/HomePage/Take',headers =O00OOOOO000OO0OOO .headers ,json =OOOO0OOO000OOO0O0 ).json ()#line:97
            if 'Data'in O00000000O0OO00O0 :#line:99
                O0O000O0OO00000OO =O00000000O0OO00O0 ['Data']['Ci']#line:101
                O0000O00O0OO0OOO0 =O00000000O0OO00O0 ['Data']['Ce']#line:102
                print (f'【临时碳能】:收取碳积分:{O0O000O0OO00000OO}丨收取碳能:{O0000O00O0OO0OOO0}')#line:103
        except Exception as OO0O000000O0O0OO0 :#line:104
            print (OO0O000000O0O0OO0 )#line:105
    def get_index (O000O0O00OOOO0000 ):#line:109
        try :#line:110
            for OOO000O00OOO00O0O in range (5 ):#line:111
                OOO000O0OO000OO00 =requests .request ('get','https://api.thxq888.com/api/FriendPage/GetIndex',headers =O000O0O00OOOO0000 .headers ).json ()#line:112
                if 'Data'in OOO000O0OO000OO00 :#line:114
                    if OOO000O0OO000OO00 ['Data']['CiList']:#line:115
                        O0O00O00O00OOO00O =OOO000O0OO000OO00 ['Data']['CiList'][0 ]['Id']#line:116
                        O000O0OO00O0O000O ={"Id":O0O00O00O00OOO00O }#line:117
                        O0OO0000000OO0OO0 =requests .request ('post',f'{host}/api/FriendPage/Take',headers =O000O0O00OOOO0000 .headers ,json =O000O0OO00O0O000O ).json ()#line:118
                        if 'Data'in O0OO0000000OO0OO0 :#line:120
                            O0OO0000000O00O00 =O0OO0000000OO0OO0 ['Data']['Ci']#line:121
                            print (f'【偷碳积分】:收取碳积分:{O0OO0000000O00O00}')#line:122
                        time .sleep (random .randint (17 ,20 ))#line:123
                    else :#line:124
                        break #line:125
        except Exception as O0OO0O0OOOO0OOO00 :#line:126
            print (O0OO0O0OOOO0OOO00 )#line:127
def os_qinglong ():#line:132
    if application in os .environ :#line:133
        O0O0OOOO0O0O0O0OO =os .environ [application ].split ('\n')#line:134
        if len (O0O0OOOO0O0O0O0OO )>0 :#line:135
            return O0O0OOOO0O0O0O0OO #line:136
        else :#line:137
            print (f"{application}变量未启用")#line:138
            print ('脚本退出')#line:139
            sys .exit (1 )#line:140
    else :#line:141
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='cookie'\n尝试使用内置变量")#line:142
        return os_built ()#line:143
def os_built ():#line:146
    if token :#line:147
        OO0O00OO0OOO00O00 =token .split ('\n')#line:148
        if len (OO0O00OO0OOO00O00 )>0 :#line:149
            return OO0O00OO0OOO00O00 #line:150
    else :#line:151
        print (f"内置变量为空")#line:152
        print ('脚本结束')#line:153
        sys .exit (0 )#line:154
if __name__ =='__main__':#line:157
    start ()#line:158
