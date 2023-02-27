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
@ 版本 0.1
"""
application = 'qc_token'  # 变量名
token = ''  # 调试token


##################################下面不要动##################################
host ='https://qct.qitusky.cn'#line:1
git ='https://gitee.com'#line:2
def os_qinglong ():#line:3
    if application in os .environ :#line:4
        OOO00O0O0000O0OOO =os .environ [application ].split ('\n')#line:5
        if len (OOO00O0O0000O0OOO )>0 :#line:6
            return OOO00O0O0000O0OOO #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        O000OOOOO0OOO0000 =token .split ('\n')#line:19
        if len (O000OOOOO0OOO0000 )>0 :#line:20
            return O000OOOOO0OOO0000 #line:21
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
        OO0OOO00OOO000OO0 =gitee_validation ()#line:35
        if version_of_the_validation ()<OO0OOO00OOO000OO0 ['Tower']['edition']:#line:36
            print (f'当前脚本名字: {OO0OOO00OOO000OO0["Tower"]["text"]}')#line:37
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OOO00OOO000OO0["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:38
            print (f'更新内容=>> {OO0OOO00OOO000OO0["Tower"]["content"]}')#line:39
        else :#line:40
            print (f'当前脚本名字: {OO0OOO00OOO000OO0["Tower"]["text"]}')#line:41
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OOO00OOO000OO0["Tower"]["edition"]}   ✅')#line:42
            print (f'更新内容=>> {OO0OOO00OOO000OO0["Tower"]["content"]}')#line:43
    except Exception as OO0O0OOOO000O0O0O :#line:44
        print (OO0O0OOOO000O0O0O )#line:45
class Template :#line:50
    def __init__ (O000O0OOO00000O00 ,OO0O0OOO000O0OOOO ):#line:52
        try :#line:53
            O000O0OOO00000O00 .token =OO0O0OOO000O0OOOO .split ('&')[0 ]#line:54
            O000O0OOO00000O00 .box =OO0O0OOO000O0OOOO .split ('&')[1 ]#line:55
            O000O0OOO00000O00 .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':O000O0OOO00000O00 .token ,'server':'true','phone-type':'android',}#line:67
        except Exception as O0OOO0O000000OOO0 :#line:68
            print ('变量格式错误')#line:69
    def base_info (OOOOOO0OOOO00OO0O ):#line:72
        try :#line:73
            O00OOO00O0O00000O =requests .request ('post',f'{host}/api/User/info',headers =OOOOOO0OOOO00OO0O .headers ).json ()#line:74
            if 'code'in O00OOO00O0O00000O :#line:76
                if O00OOO00O0O00000O ['code']==1 :#line:77
                    O0O0000000000O00O =O00OOO00O0O00000O ['data']['nickname']#line:78
                    OO00OO00OO00OO0OO =O00OOO00O0O00000O ['data']['id']#line:79
                    OO00000O0OOO00OO0 =O00OOO00O0O00000O ['data']['score']#line:80
                    print (f'账号信息:昵称:{O0O0000000000O00O}丨ID:{OO00OO00OO00OO0OO}丨金币:{str(OO00000O0OOO00OO0)[:5]}')#line:81
                if O00OOO00O0O00000O ['code']==302 :#line:82
                    return False #line:83
            return True #line:84
        except Exception as OO000O0O0O000000O :#line:85
            print (OO000O0O0O000000O )#line:86
    def playInfo (O0O0OOO00O00OO0OO ):#line:89
        try :#line:90
            OOO0O0OO0OOO0OO0O =requests .request ('post',f'{host}/api/Game/playInfo',headers =O0O0OOO00O00OO0OO .headers ).json ()#line:91
            if 'code'in OOO0O0OO0OOO0OO0O :#line:93
                if OOO0O0OO0OOO0OO0O ['code']==1 :#line:94
                    O0O000OO0OOO0O0OO =OOO0O0OO0OOO0OO0O ['data']['play_tier']#line:95
                    O0OO0O0OOOOO00O0O =OOO0O0OO0OOO0OO0O ['data']['play_tier_need_money']#line:96
                    O0000OO0000OO000O =OOO0O0OO0OOO0OO0O ['data']['user_money']#line:97
                    O0000000OOOO0O0O0 =OOO0O0OO0OOO0OO0O ['data']['play_finish_money']#line:98
                    print (f'参与闯关:层数:{O0O000OO0OOO0O0OO}丨余额:{str(O0000OO0000OO000O).split(".")[0]}丨闯关花费:{O0OO0O0OOOOO00O0O}丨预计获得:{O0000000OOOO0O0O0}')#line:99
        except Exception as O00O00O0OOO0OOO00 :#line:103
            print (O00O00O0OOO0OOO00 )#line:104
    def setAutoPlay (O0000OOO0O00OOOO0 ):#line:107
        try :#line:108
            OOO00OO0O00OO00O0 ={'state':'1'}#line:111
            O00000O000OOOOO0O =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O0000OOO0O00OOOO0 .headers ,data =OOO00OO0O00OO00O0 ).json ()#line:112
            if 'code'in O00000O000OOOOO0O :#line:114
                if O00000O000OOOOO0O ['code']==1 :#line:115
                    print (f'自动闯关:{O00000O000OOOOO0O["msg"]}')#line:116
                if O00000O000OOOOO0O ['code']==0 :#line:117
                    print (f'自动闯关:{O00000O000OOOOO0O["msg"]}')#line:118
        except Exception as O0OO000O000OOO0OO :#line:119
            print (O0OO000O000OOO0OO )#line:120
    def Game_index (OO000O0OO0OO000OO ):#line:123
        OOOO00OO0OO00OOO0 =requests .request ('post',f'{host}/api/Game/index',headers =OO000O0OO0OO000OO .headers ).json ()#line:124
        if 'code'in OOOO00OO0OO00OOO0 :#line:126
            if OOOO00OO0OO00OOO0 ['code']==1 :#line:127
                O0O00O0O0OO00O00O =OOOO00OO0OO00OOO0 ['data']['is_auto_play']#line:128
                OO000000O00OOOOO0 =OOOO00OO0OO00OOO0 ['data']['is_game_ing']#line:129
                OOO000OO0OOOOO000 =OOOO00OO0OO00OOO0 ['data']['is_vip']#line:130
                O0000OO0OOOOOOOOO =OOOO00OO0OO00OOO0 ['data']['npc_hint']#line:131
                print (f'游戏状态:自动闯关:{O0O00O0O0OO00O00O}丨VIP:{OOO000OO0OOOOO000}')#line:132
                if not O0O00O0O0OO00O00O :#line:133
                    OO000O0OO0OO000OO .setAutoPlay ()#line:134
    def LuckyBox (OOOOO000OOOOO0O00 ):#line:137
        try :#line:138
            OOOO0O0O00O000OO0 =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OOOOO000OOOOO0O00 .headers ).json ()#line:139
            if 'code'in OOOO0O0O00O000OO0 :#line:141
                if OOOO0O0O00O000OO0 ['code']==1 :#line:142
                    O0OO00O000000OO0O =OOOO0O0O00O000OO0 ['data']['debris']#line:143
                    OO0000OO000000OO0 =OOOO0O0O00O000OO0 ['data']['is_draw']#line:144
                    print (f'幸运宝箱:碎片:{str(O0OO00O000000OO0O).split(".")[0]}丨当前设置开启宝箱ID:{OOOOO000OOOOO0O00.box}')#line:145
                    if not OO0000OO000000OO0 :#line:146
                        O0O0O00OOO0O0000O =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OOOOO000OOOOO0O00 .headers ).json ()#line:147
                        if 'code'in O0O0O00OOO0O0000O :#line:149
                            if O0O0O00OOO0O0000O ['code']==1 :#line:150
                                OOOOO0OO0O0OO00O0 =O0O0O00OOO0O0000O ['data']['nub']#line:151
                                print (f'领取碎片:获得:{OOOOO0OO0O0OO00O0}')#line:152
                    for O000OOO0OO00O00O0 in OOOO0O0O00O000OO0 ['data']['box_list']:#line:153
                        O0O00OOOO00OO0OO0 =O000OOO0OO00O00O0 ['id']#line:155
                        O000O0OOOO00O0OO0 =O000OOO0OO00O00O0 ['name']#line:156
                        OO0O000O0000OO0OO =O000OOO0OO00O00O0 ['inventory']#line:157
                        OOOOOOOO000OOOOOO =O000OOO0OO00O00O0 ['need_debris']#line:158
                        print (f'        名称:{O000O0OOOO00O0OO0}丨需要碎片:{OOOOOOOO000OOOOOO}丨剩余:{OO0O000O0000OO0OO}')#line:159
                        if float (O0O00OOOO00OO0OO0 )==float (OOOOO000OOOOO0O00 .box ):#line:160
                            if float (O0OO00O000000OO0O )>=float (OOOOOOOO000OOOOOO ):#line:161
                                O0OOOO0OOOO00OO0O ={'id':OOOOO000OOOOO0O00 .box }#line:162
                                OOOOO00000000O000 =requests .request ('post','https://qct.qitusky.cn/api/LuckyBox/exchange',headers =OOOOO000OOOOO0O00 .headers ,data =O0OOOO0OOOO00OO0O ).json ()#line:163
                                if 'code'in OOOOO00000000O000 :#line:165
                                    if OOOOO00000000O000 ['code']==1 :#line:166
                                        print (f'兑换宝箱:{OOOOO00000000O000["msg"]}丨获得{OOOOO00000000O000["data"]["name"]}')#line:167
        except Exception as O0000O00O0O0O0OO0 :#line:170
            print (O0000O00O0O0O0OO0 )#line:171
def start ():#line:174
    try :#line:175
        update_the_validation ()#line:176
        O0000O0O0O0O0O000 =os_qinglong ()#line:177
        print (f"==========共找到{len(O0000O0O0O0O0O000)}个账号==========")#line:178
        for OO0O0OOOO00OO00O0 in O0000O0O0O0O0O000 :#line:179
            print (f"------------正在执行第{O0000O0O0O0O0O000.index(OO0O0OOOO00OO00O0) + 1}个账号------------")#line:180
            OO0OO0OO0O0OO0O00 =Template (OO0O0OOOO00OO00O0 )#line:181
            if OO0OO0OO0O0OO0O00 .base_info ():#line:183
                OO0OO0OO0O0OO0O00 .LuckyBox ()#line:185
                OO0OO0OO0O0OO0O00 .Game_index ()#line:187
                OO0OO0OO0O0OO0O00 .playInfo ()#line:189
                time .sleep (random .randint (2 ,3 ))#line:194
            else :#line:195
                print ('token失效')#line:196
    except Exception as OOO000OOOOO000OOO :#line:197
        print (OOO000OOOOO000OOO )#line:198
def version_of_the_validation ():#line:200
    return str ((57 -56 )/10 )#line:201
if __name__ =='__main__':#line:204
    start ()#line:205

