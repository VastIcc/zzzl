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
token = ''  # 调试token


##################################下面不要动##################################
host ='https://qct.qitusky.cn'#line:1
git ='https://gitee.com'#line:2
def os_qinglong ():#line:3
    if application in os .environ :#line:4
        O0OOOOO00O0000O00 =os .environ [application ].split ('\n')#line:5
        if len (O0OOOOO00O0000O00 )>0 :#line:6
            return O0OOOOO00O0000O00 #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        OO00000OOO0O0O0O0 =token .split ('\n')#line:19
        if len (OO00000OOO0O0O0O0 )>0 :#line:20
            return OO00000OOO0O0O0O0 #line:21
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
        O0000O0O000O0O000 =gitee_validation ()#line:35
        if version_of_the_validation ()<O0000O0O000O0O000 ['Tower']['edition']:#line:36
            print (f'当前脚本名字: {O0000O0O000O0O000["Tower"]["text"]}')#line:37
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0000O0O000O0O000["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:38
            print (f'更新内容=>> {O0000O0O000O0O000["Tower"]["content"]}')#line:39
        else :#line:40
            print (f'当前脚本名字: {O0000O0O000O0O000["Tower"]["text"]}')#line:41
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0000O0O000O0O000["Tower"]["edition"]}   ✅')#line:42
            print (f'更新内容=>> {O0000O0O000O0O000["Tower"]["content"]}')#line:43
    except Exception as OOO0O0OO00O0OO0OO :#line:44
        print (OOO0O0OO00O0OO0OO )#line:45
class Template :#line:50
    def __init__ (O0OO0OOOOO00OO0OO ,OO0O0O000OO0OO000 ):#line:52
        try :#line:53
            O0OO0OOOOO00OO0OO .token =OO0O0O000OO0OO000 .split ('&')[0 ]#line:54
            O0OO0OOOOO00OO0OO .box =OO0O0O000OO0OO000 .split ('&')[1 ]#line:55
            O0OO0OOOOO00OO0OO .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':O0OO0OOOOO00OO0OO .token ,'server':'true','phone-type':'android',}#line:67
        except Exception as O0OO000OO0OOO00O0 :#line:68
            print ('变量格式错误')#line:69
    def base_info (O00OO0OO00OOOOOOO ):#line:72
        try :#line:73
            OO0OO0O0O0O0O0OOO =requests .request ('post',f'{host}/api/User/info',headers =O00OO0OO00OOOOOOO .headers ).json ()#line:74
            if 'code'in OO0OO0O0O0O0O0OOO :#line:76
                if OO0OO0O0O0O0O0OOO ['code']==1 :#line:77
                    O0O00OO0OO00000O0 =OO0OO0O0O0O0O0OOO ['data']['nickname']#line:78
                    O000OO00OOO0O0O00 =OO0OO0O0O0O0O0OOO ['data']['id']#line:79
                    OOOOOOOO0OO0O0O00 =OO0OO0O0O0O0O0OOO ['data']['score']#line:80
                    print (f'账号信息:昵称:{O0O00OO0OO00000O0}丨ID:{O000OO00OOO0O0O00}丨金币:{str(OOOOOOOO0OO0O0O00)[:5]}')#line:81
                if OO0OO0O0O0O0O0OOO ['code']==302 :#line:82
                    return False #line:83
            return True #line:84
        except Exception as O000O0000O0O0OOOO :#line:85
            print (O000O0000O0O0OOOO )#line:86
    def playInfo (OO0000OOOO00O0000 ):#line:89
        try :#line:90
            OOOOO0OO000OOOO00 =requests .request ('post',f'{host}/api/Game/playInfo',headers =OO0000OOOO00O0000 .headers ).json ()#line:91
            if 'code'in OOOOO0OO000OOOO00 :#line:93
                if OOOOO0OO000OOOO00 ['code']==1 :#line:94
                    O0O0O0OOO0OO00OO0 =OOOOO0OO000OOOO00 ['data']['play_tier']#line:95
                    O0000OO0O000OO0O0 =OOOOO0OO000OOOO00 ['data']['play_tier_need_money']#line:96
                    O00000O0O0O0O0OO0 =OOOOO0OO000OOOO00 ['data']['user_money']#line:97
                    O0O00OOOO0OO0O00O =OOOOO0OO000OOOO00 ['data']['play_finish_money']#line:98
                    print (f'参与闯关:层数:{O0O0O0OOO0OO00OO0}丨余额:{str(O00000O0O0O0O0OO0).split(".")[0]}丨闯关花费:{O0000OO0O000OO0O0}丨预计获得:{O0O00OOOO0OO0O00O}')#line:99
        except Exception as O000000OOO0OO0OO0 :#line:103
            print (O000000OOO0OO0OO0 )#line:104
    def setAutoPlay (OOO0O0O0000O00O00 ):#line:107
        try :#line:108
            O00O0O00O0O0OOO0O ={'state':'1'}#line:111
            OO0O0OOO0O0O00O0O =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =OOO0O0O0000O00O00 .headers ,data =O00O0O00O0O0OOO0O ).json ()#line:112
            if 'code'in OO0O0OOO0O0O00O0O :#line:114
                if OO0O0OOO0O0O00O0O ['code']==1 :#line:115
                    print (f'自动闯关:{OO0O0OOO0O0O00O0O["msg"]}')#line:116
                if OO0O0OOO0O0O00O0O ['code']==0 :#line:117
                    print (f'自动闯关:{OO0O0OOO0O0O00O0O["msg"]}')#line:118
        except Exception as O00O00000000OOOOO :#line:119
            print (O00O00000000OOOOO )#line:120
    def Game_index (O000O0O0O0OO0OOOO ):#line:123
        OOO00OO00O0O0O00O =requests .request ('post',f'{host}/api/Game/index',headers =O000O0O0O0OO0OOOO .headers ).json ()#line:124
        if 'code'in OOO00OO00O0O0O00O :#line:126
            if OOO00OO00O0O0O00O ['code']==1 :#line:127
                OOO0OO0O00OO0O0OO =OOO00OO00O0O0O00O ['data']['is_auto_play']#line:128
                OO0OOOOO000OO0OOO =OOO00OO00O0O0O00O ['data']['is_game_ing']#line:129
                O00O0O00OOO0O0OOO =OOO00OO00O0O0O00O ['data']['is_vip']#line:130
                OOO0OO0OOO0OOO00O =OOO00OO00O0O0O00O ['data']['npc_hint']#line:131
                print (f'游戏状态:自动闯关:{OOO0OO0O00OO0O0OO}丨VIP:{O00O0O00OOO0O0OOO}')#line:132
                if not OOO0OO0O00OO0O0OO :#line:133
                    O000O0O0O0OO0OOOO .setAutoPlay ()#line:134
    def LuckyBox (OO0OOOOO000000O0O ):#line:137
        try :#line:138
            OO00O0O0000OO00OO =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OO0OOOOO000000O0O .headers ).json ()#line:139
            if 'code'in OO00O0O0000OO00OO :#line:141
                if OO00O0O0000OO00OO ['code']==1 :#line:142
                    O0OOO00O00OO0O00O =OO00O0O0000OO00OO ['data']['debris']#line:143
                    O0O0OOO00OOO000OO =OO00O0O0000OO00OO ['data']['is_draw']#line:144
                    print (f'幸运宝箱:碎片:{str(O0OOO00O00OO0O00O).split(".")[0]}丨当前设置开启宝箱ID:{OO0OOOOO000000O0O.box}')#line:145
                    if not O0O0OOO00OOO000OO :#line:146
                        OOO0O0OOOOOO0O0O0 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OO0OOOOO000000O0O .headers ).json ()#line:147
                        if 'code'in OOO0O0OOOOOO0O0O0 :#line:149
                            if OOO0O0OOOOOO0O0O0 ['code']==1 :#line:150
                                O00OOO0O00OO00OO0 =OOO0O0OOOOOO0O0O0 ['data']['nub']#line:151
                                print (f'领取碎片:获得:{O00OOO0O00OO00OO0}')#line:152
                    for O0O00OO0OO000O00O in OO00O0O0000OO00OO ['data']['box_list']:#line:153
                        O0OOOO0000O0OO00O =O0O00OO0OO000O00O ['id']#line:155
                        O000000OO00OO0OO0 =O0O00OO0OO000O00O ['name']#line:156
                        OOOOOO0O0O0O0O0OO =O0O00OO0OO000O00O ['inventory']#line:157
                        O0OOO00OOOO0O00OO =O0O00OO0OO000O00O ['need_debris']#line:158
                        if float (O0OOOO0000O0OO00O )==float (OO0OOOOO000000O0O .box ):#line:159
                            if float (O0OOO00O00OO0O00O )>=float (O0OOO00OOOO0O00OO ):#line:160
                                print (f'        名称:{O000000OO00OO0OO0}丨需要碎片:{O0OOO00OOOO0O00OO}丨剩余:{OOOOOO0O0O0O0O0OO}')#line:161
                                OO0OO00O0OOOO0000 ={'id':OO0OOOOO000000O0O .box }#line:162
                                O0OO0000O00OOO00O =requests .request ('post','https://qct.qitusky.cn/api/LuckyBox/exchange',headers =OO0OOOOO000000O0O .headers ,data =OO0OO00O0OOOO0000 ).json ()#line:163
                                if 'code'in O0OO0000O00OOO00O :#line:165
                                    if O0OO0000O00OOO00O ['code']==1 :#line:166
                                        print (f'兑换宝箱:{O0OO0000O00OOO00O["msg"]}丨获得{O0OO0000O00OOO00O["data"]["name"]}')#line:167
        except Exception as OOOOOOO0OOOO0O0OO :#line:170
            print (OOOOOOO0OOOO0O0OO )#line:171
def start ():#line:174
    try :#line:175
        update_the_validation ()#line:176
        O0000O00O0O000O0O =os_qinglong ()#line:177
        print (f"==========共找到{len(O0000O00O0O000O0O)}个账号==========")#line:178
        for OOOO000OOOOOO00O0 in O0000O00O0O000O0O :#line:179
            print (f"------------正在执行第{O0000O00O0O000O0O.index(OOOO000OOOOOO00O0) + 1}个账号------------")#line:180
            O0O000O00OOO00O00 =Template (OOOO000OOOOOO00O0 )#line:181
            if O0O000O00OOO00O00 .base_info ():#line:183
                O0O000O00OOO00O00 .LuckyBox ()#line:185
                O0O000O00OOO00O00 .Game_index ()#line:187
                O0O000O00OOO00O00 .playInfo ()#line:189
                time .sleep (random .randint (2 ,3 ))#line:194
            else :#line:195
                print ('token失效')#line:196
    except Exception as OO0OO0OOOOOO00OOO :#line:197
        print (OO0OO0OOOOOO00OOO )#line:198
def version_of_the_validation ():#line:200
    return str ((58 -56 )/10 )#line:201
if __name__ =='__main__':#line:204
    start ()#line:205
