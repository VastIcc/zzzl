# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import requests
    import random
except Exception as E:
    t = re.findall("d '(.*?)'", str(E))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: 0,10 0,12 * * *
@ new Env('千层塔会员版')
@ 项目地址  https://qct.qitusky.cn/invite/?invite_code=1476
@ 抓取  https://qct.qitusky.cn 的ba-user-token值
@ 青龙变量 export qc_token="token&宝箱ID"   1普通宝箱 2白银宝箱 3黄金宝箱 4神秘宝箱 5炫彩宝箱  多号换行
@ 版本 0.2
"""
application = 'qc_token'  # 变量名
token = '''cc9b32ef-2ba9-4191-8b32-1c0ae8a15ed1&3'''  # 调试token


##################################下面不要动##################################    is_real
host ='https://qct.qitusky.cn'#line:1
git ='https://gitee.com'#line:2
def os_qinglong ():#line:3
    if application in os .environ :#line:4
        O00O0OO0O000OO0OO =os .environ [application ].split ('\n')#line:5
        if len (O00O0OO0O000OO0OO )>0 :#line:6
            return O00O0OO0O000OO0OO #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        O000O000OO0OOOOO0 =token .split ('\n')#line:19
        if len (O000O000OO0OOOOO0 )>0 :#line:20
            return O000O000OO0OOOOO0 #line:21
    else :#line:22
        print (f"内置变量为空")#line:23
        print ('脚本结束')#line:24
        sys .exit (0 )#line:25
def gitee_validation ():#line:26
    try :#line:27
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:28
    except :#line:29
        sys .exit (0 )#line:30
def update_the_validation ():#line:33
    try :#line:34
        OO000O0OOOO0O00O0 =gitee_validation ()#line:35
        if version_of_the_validation ()<OO000O0OOOO0O00O0 ['Tower']['edition']:#line:36
            print (f'当前脚本名字: {OO000O0OOOO0O00O0["Tower"]["text"]}')#line:37
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO000O0OOOO0O00O0["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:38
            print (f'更新内容=>> {OO000O0OOOO0O00O0["Tower"]["content"]}')#line:39
        else :#line:40
            print (f'当前脚本名字: {OO000O0OOOO0O00O0["Tower"]["text"]}')#line:41
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO000O0OOOO0O00O0["Tower"]["edition"]}   ✅')#line:42
            print (f'更新内容=>> {OO000O0OOOO0O00O0["Tower"]["content"]}')#line:43
    except Exception as OOO000O00OOO0OOO0 :#line:44
        print (OOO000O00OOO0OOO0 )#line:45
class Template :#line:50
    def __init__ (OOO0000O00OOOO000 ,OOO00OO0OOO0O0OO0 ):#line:52
        try :#line:53
            OOO0000O00OOOO000 .token =OOO00OO0OOO0O0OO0 .split ('&')[0 ]#line:54
            OOO0000O00OOOO000 .box =OOO00OO0OOO0O0OO0 .split ('&')[1 ]#line:55
            OOO0000O00OOOO000 .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OOO0000O00OOOO000 .token ,'server':'true','phone-type':'android',}#line:67
        except Exception as OO0O000O0O0O000O0 :#line:68
            print ('变量格式错误')#line:69
    def base_info (OO000000O00OO0O0O ):#line:72
        try :#line:73
            OO0OOO0O0OO00OO0O =requests .request ('post',f'{host}/api/User/info',headers =OO000000O00OO0O0O .headers ).json ()#line:74
            if 'code'in OO0OOO0O0OO00OO0O :#line:76
                if OO0OOO0O0OO00OO0O ['code']==1 :#line:77
                    OOO00OOO00O000OO0 =OO0OOO0O0OO00OO0O ['data']['nickname']#line:78
                    OOO000O00000O0OO0 =OO0OOO0O0OO00OO0O ['data']['id']#line:79
                    OO0O0000OOO0OOOO0 =OO0OOO0O0OO00OO0O ['data']['score']#line:80
                    if OO0OOO0O0OO00OO0O ['data']['is_real']:#line:81
                        print (f'【账号信息】:昵称:{OOO00OOO00O000OO0}丨ID:{OOO000O00000O0OO0}丨金币:{str(OO0O0000OOO0OOOO0)[:5]}丨已实名  ✅')#line:82
                    else :#line:83
                        print (f'【账号信息】:昵称:{OOO00OOO00O000OO0}丨ID:{OOO000O00000O0OO0}丨金币:{str(OO0O0000OOO0OOOO0)[:5]}丨未实名  ❌')#line:84
                if OO0OOO0O0OO00OO0O ['code']==302 :#line:85
                    return False #line:86
            return True #line:87
        except Exception as O0O00O0OOO000OO0O :#line:88
            print (O0O00O0OOO000OO0O )#line:89
    def playInfo (OO0O0000OOO0OO00O ):#line:92
        try :#line:93
            OO0000OOO0O000O0O =requests .request ('post',f'{host}/api/Game/playInfo',headers =OO0O0000OOO0OO00O .headers ).json ()#line:94
            if 'code'in OO0000OOO0O000O0O :#line:96
                if OO0000OOO0O000O0O ['code']==1 :#line:97
                    O00O0OO00OOO00OO0 =OO0000OOO0O000O0O ['data']['play_tier']#line:98
                    OOOO0O00OO0O00000 =OO0000OOO0O000O0O ['data']['play_tier_need_money']#line:99
                    OO000OO0O0OOOOOO0 =OO0000OOO0O000O0O ['data']['user_money']#line:100
                    O0O0OOOO0OO0O0O0O =OO0000OOO0O000O0O ['data']['play_finish_money']#line:101
                    print (f'【参与闯关】:层数:{O00O0OO00OOO00OO0}丨余额:{str(OO000OO0O0OOOOOO0).split(".")[0]}丨闯关花费:{OOOO0O00OO0O00000}丨预计获得:{O0O0OOOO0OO0O0O0O}')#line:102
        except Exception as O00O0O0O000OO0O0O :#line:106
            print (O00O0O0O000OO0O0O )#line:107
    def setAutoPlay (O0O000OOO00O00OOO ):#line:110
        try :#line:111
            O00O0O000OO0OOO0O ={'state':'1'}#line:114
            OO0OOO0O0O0000O0O =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O0O000OOO00O00OOO .headers ,data =O00O0O000OO0OOO0O ).json ()#line:115
            if 'code'in OO0OOO0O0O0000O0O :#line:117
                if OO0OOO0O0O0000O0O ['code']==1 :#line:118
                    print (f'【自动闯关】:{OO0OOO0O0O0000O0O["msg"]}')#line:119
                if OO0OOO0O0O0000O0O ['code']==0 :#line:120
                    print (f'【自动闯关】:{OO0OOO0O0O0000O0O["msg"]}')#line:121
        except Exception as OO0OO0000O00OOO0O :#line:122
            print (OO0OO0000O00OOO0O )#line:123
    def Game_index (OOOOOOOO0O0OOO000 ):#line:126
        OOOOOO0O0O0OO000O =requests .request ('post',f'{host}/api/Game/index',headers =OOOOOOOO0O0OOO000 .headers ).json ()#line:127
        if 'code'in OOOOOO0O0O0OO000O :#line:129
            if OOOOOO0O0O0OO000O ['code']==1 :#line:130
                OOOO0O00O0OOO0O00 =OOOOOO0O0O0OO000O ['data']['is_auto_play']#line:131
                OOOO00O0000OO00OO =OOOOOO0O0O0OO000O ['data']['is_game_ing']#line:132
                O0OOO0O0000000O0O =OOOOOO0O0O0OO000O ['data']['is_vip']#line:133
                OO00OO000O0OO0O00 =OOOOOO0O0O0OO000O ['data']['npc_hint']#line:134
                print (f'【游戏状态】:自动闯关:{OOOO0O00O0OOO0O00}丨VIP:{O0OOO0O0000000O0O}')#line:135
                if not OOOO0O00O0OOO0O00 :#line:136
                    OOOOOOOO0O0OOO000 .setAutoPlay ()#line:137
    def LuckyBox (OOOOOOOOOOOOOOOOO ):#line:140
        try :#line:141
            OO00000O00O00000O =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OOOOOOOOOOOOOOOOO .headers ).json ()#line:142
            if 'code'in OO00000O00O00000O :#line:144
                if OO00000O00O00000O ['code']==1 :#line:145
                    O00OO000OO0OO000O =OO00000O00O00000O ['data']['debris']#line:146
                    O00000O00OO0O0O00 =OO00000O00O00000O ['data']['is_draw']#line:147
                    print (f'【幸运宝箱】:碎片:{str(O00OO000OO0OO000O).split(".")[0]}丨当前设置开启宝箱ID:{OOOOOOOOOOOOOOOOO.box}')#line:148
                    if not O00000O00OO0O0O00 :#line:149
                        OO0OOOOOOO0O00000 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OOOOOOOOOOOOOOOOO .headers ).json ()#line:150
                        if 'code'in OO0OOOOOOO0O00000 :#line:152
                            if OO0OOOOOOO0O00000 ['code']==1 :#line:153
                                O00O0OOOOO0000O00 =OO0OOOOOOO0O00000 ['data']['nub']#line:154
                                print (f'【领取碎片】:获得:{O00O0OOOOO0000O00}')#line:155
                    for O00OO0O00OOOO0O00 in OO00000O00O00000O ['data']['box_list']:#line:156
                        OO00O0O0O000OOO00 =O00OO0O00OOOO0O00 ['id']#line:158
                        O0O00O000OOOOOO00 =O00OO0O00OOOO0O00 ['name']#line:159
                        O00OOO000O00O0O00 =O00OO0O00OOOO0O00 ['inventory']#line:160
                        OO00000O00OOOO00O =O00OO0O00OOOO0O00 ['need_debris']#line:161
                        if float (OO00O0O0O000OOO00 )==float (OOOOOOOOOOOOOOOOO .box ):#line:162
                            print (f'【幸运宝箱】:名称:{O0O00O000OOOOOO00}丨需要碎片:{OO00000O00OOOO00O}丨剩余:{O00OOO000O00O0O00}')#line:163
                            if float (O00OO000OO0OO000O )>=float (OO00000O00OOOO00O ):#line:164
                                O0OO000O00OOOO00O ={'id':OOOOOOOOOOOOOOOOO .box }#line:165
                                O00000000OOOOOOO0 =requests .request ('post','https://qct.qitusky.cn/api/LuckyBox/exchange',headers =OOOOOOOOOOOOOOOOO .headers ,data =O0OO000O00OOOO00O ).json ()#line:166
                                if 'code'in O00000000OOOOOOO0 :#line:168
                                    if O00000000OOOOOOO0 ['code']==1 :#line:169
                                        print (f'【兑换宝箱】:{O00000000OOOOOOO0["msg"]}丨获得{O00000000OOOOOOO0["data"]["name"]}')#line:170
        except Exception as OOO000O0OOO000O00 :#line:173
            print (OOO000O0OOO000O00 )#line:174
def start ():#line:177
    try :#line:178
        update_the_validation ()#line:179
        OOO0O00OO00O0OO0O =os_qinglong ()#line:180
        print (f"==========共找到{len(OOO0O00OO00O0OO0O)}个账号==========")#line:181
        for OOO0OOOO0OO000O0O in OOO0O00OO00O0OO0O :#line:182
            print (f"------------正在执行第{OOO0O00OO00O0OO0O.index(OOO0OOOO0OO000O0O) + 1}个账号------------")#line:183
            OOO0O0OO0000O0OO0 =Template (OOO0OOOO0OO000O0O )#line:184
            if OOO0O0OO0000O0OO0 .base_info ():#line:186
                OOO0O0OO0000O0OO0 .LuckyBox ()#line:188
                OOO0O0OO0000O0OO0 .Game_index ()#line:190
                OOO0O0OO0000O0OO0 .playInfo ()#line:192
                time .sleep (random .randint (2 ,3 ))#line:197
            else :#line:198
                print ('token失效')#line:199
    except Exception as OOO00O0OOO0000O00 :#line:200
        print (OOO00O0OOO0000O00 )#line:201
def version_of_the_validation ():#line:203
    return str ((58 -56 )/10 )#line:204
if __name__ =='__main__':#line:207
    start ()#line:208
