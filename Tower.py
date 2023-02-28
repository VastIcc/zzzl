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
        OOOO0O0OOO00O00OO =os .environ [application ].split ('\n')#line:5
        if len (OOOO0O0OOO00O00OO )>0 :#line:6
            return OOOO0O0OOO00O00OO #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        OO0OOO0O00000OOOO =token .split ('\n')#line:19
        if len (OO0OOO0O00000OOOO )>0 :#line:20
            return OO0OOO0O00000OOOO #line:21
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
        OO00000O0OOOO0O00 =gitee_validation ()#line:35
        if version_of_the_validation ()<OO00000O0OOOO0O00 ['Tower']['edition']:#line:36
            print (f'当前脚本名字: {OO00000O0OOOO0O00["Tower"]["text"]}')#line:37
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00000O0OOOO0O00["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:38
            print (f'更新内容=>> {OO00000O0OOOO0O00["Tower"]["content"]}')#line:39
        else :#line:40
            print (f'当前脚本名字: {OO00000O0OOOO0O00["Tower"]["text"]}')#line:41
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00000O0OOOO0O00["Tower"]["edition"]}   ✅')#line:42
            print (f'更新内容=>> {OO00000O0OOOO0O00["Tower"]["content"]}')#line:43
    except Exception as OOOO00O00000O0000 :#line:44
        print (OOOO00O00000O0000 )#line:45
class Template :#line:50
    def __init__ (O0O00OO000O000000 ,O00OOO0O0OO0OO0O0 ):#line:52
        try :#line:53
            O0O00OO000O000000 .token =O00OOO0O0OO0OO0O0 .split ('&')[0 ]#line:54
            O0O00OO000O000000 .box =O00OOO0O0OO0OO0O0 .split ('&')[1 ]#line:55
            O0O00OO000O000000 .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':O0O00OO000O000000 .token ,'server':'true','phone-type':'android',}#line:67
        except Exception as OOOOOOO00O0OO0OOO :#line:68
            print ('变量格式错误')#line:69
    def base_info (OO000O000OO0OOOOO ):#line:72
        try :#line:73
            OO00O00OO0OOOO00O =requests .request ('post',f'{host}/api/User/info',headers =OO000O000OO0OOOOO .headers ).json ()#line:74
            if 'code'in OO00O00OO0OOOO00O :#line:76
                if OO00O00OO0OOOO00O ['code']==1 :#line:77
                    OO0000O000O000O0O =OO00O00OO0OOOO00O ['data']['nickname']#line:78
                    O0OOO0OOO00O00O00 =OO00O00OO0OOOO00O ['data']['id']#line:79
                    OOOOOOO0000OOO0O0 =OO00O00OO0OOOO00O ['data']['score']#line:80
                    if OO00O00OO0OOOO00O ['data']['is_real']:#line:81
                        print (f'【账号信息】:昵称:{OO0000O000O000O0O}丨ID:{O0OOO0OOO00O00O00}丨金币:{str(OOOOOOO0000OOO0O0)[:5]}丨已实名  ✅')#line:82
                    else :#line:83
                        print (f'【账号信息】:昵称:{str(OO0000O000O000O0O)[:4]}丨ID:{O0OOO0OOO00O00O00}丨金币:{str(OOOOOOO0000OOO0O0)[:5]}丨未实名  ❌')#line:84
                if OO00O00OO0OOOO00O ['code']==302 :#line:85
                    return False #line:86
            return True #line:87
        except Exception as O0O00OO00O0O0OOOO :#line:88
            print (O0O00OO00O0O0OOOO )#line:89
    def playInfo (OOO0OOO00OOOOOO0O ):#line:92
        try :#line:93
            OOOO00O00OOO00OOO =requests .request ('post',f'{host}/api/Game/playInfo',headers =OOO0OOO00OOOOOO0O .headers ).json ()#line:94
            if 'code'in OOOO00O00OOO00OOO :#line:96
                if OOOO00O00OOO00OOO ['code']==1 :#line:97
                    OO0OOO0O00O000OO0 =OOOO00O00OOO00OOO ['data']['play_tier']#line:98
                    O0O0000O00O00000O =OOOO00O00OOO00OOO ['data']['play_tier_need_money']#line:99
                    O0OOOO00OO00OOOO0 =OOOO00O00OOO00OOO ['data']['user_money']#line:100
                    OOOO00O00OO00000O =OOOO00O00OOO00OOO ['data']['play_finish_money']#line:101
                    print (f'【参与闯关】:层数:{OO0OOO0O00O000OO0}丨余额:{str(O0OOOO00OO00OOOO0).split(".")[0]}丨闯关花费:{O0O0000O00O00000O}丨预计获得:{OOOO00O00OO00000O}')#line:102
        except Exception as OO000OO00OOO000OO :#line:106
            print (OO000OO00OOO000OO )#line:107
    def setAutoPlay (O0OO0O0OO000OO00O ):#line:110
        try :#line:111
            O0O0O000OOOOOO0OO ={'state':'1'}#line:114
            O00000O0O0OOOOOO0 =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O0OO0O0OO000OO00O .headers ,data =O0O0O000OOOOOO0OO ).json ()#line:115
            if 'code'in O00000O0O0OOOOOO0 :#line:117
                if O00000O0O0OOOOOO0 ['code']==1 :#line:118
                    print (f'【自动闯关】:{O00000O0O0OOOOOO0["msg"]}')#line:119
                if O00000O0O0OOOOOO0 ['code']==0 :#line:120
                    print (f'【自动闯关】:{O00000O0O0OOOOOO0["msg"]}')#line:121
        except Exception as O0OO00OOO0O000OO0 :#line:122
            print (O0OO00OOO0O000OO0 )#line:123
    def Game_index (OO0O000OOO00O000O ):#line:126
        OOOO00O0OOOO0O0OO =requests .request ('post',f'{host}/api/Game/index',headers =OO0O000OOO00O000O .headers ).json ()#line:127
        if 'code'in OOOO00O0OOOO0O0OO :#line:129
            if OOOO00O0OOOO0O0OO ['code']==1 :#line:130
                O0OO00O000O0O0O00 =OOOO00O0OOOO0O0OO ['data']['is_auto_play']#line:131
                OO0O0OO0OO0OOOOO0 =OOOO00O0OOOO0O0OO ['data']['is_game_ing']#line:132
                OOO00O00O00O00O00 =OOOO00O0OOOO0O0OO ['data']['is_vip']#line:133
                OOOO00O00O0OO0O0O =OOOO00O0OOOO0O0OO ['data']['npc_hint']#line:134
                print (f'【游戏状态】:自动闯关:{O0OO00O000O0O0O00}丨VIP:{OOO00O00O00O00O00}')#line:135
                if not O0OO00O000O0O0O00 :#line:136
                    OO0O000OOO00O000O .setAutoPlay ()#line:137
    def LuckyBox (OOOO0O00O00000000 ):#line:140
        try :#line:141
            OOO0OOOOO0OOOOOO0 =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OOOO0O00O00000000 .headers ).json ()#line:142
            if 'code'in OOO0OOOOO0OOOOOO0 :#line:144
                if OOO0OOOOO0OOOOOO0 ['code']==1 :#line:145
                    O0O0OOO00OO000O0O =OOO0OOOOO0OOOOOO0 ['data']['debris']#line:146
                    O0OO0O0000O0O0000 =OOO0OOOOO0OOOOOO0 ['data']['is_draw']#line:147
                    print (f'【幸运宝箱】:碎片:{str(O0O0OOO00OO000O0O).split(".")[0]}丨当前设置开启宝箱ID:{OOOO0O00O00000000.box}')#line:148
                    if not O0OO0O0000O0O0000 :#line:149
                        O00OOO0OOOO0O000O =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OOOO0O00O00000000 .headers ).json ()#line:150
                        if 'code'in O00OOO0OOOO0O000O :#line:152
                            if O00OOO0OOOO0O000O ['code']==1 :#line:153
                                O00OOOO0000O0O000 =O00OOO0OOOO0O000O ['data']['nub']#line:154
                                print (f'【领取碎片】:获得:{O00OOOO0000O0O000}')#line:155
                    for OO0OOOOO0OOOO0OO0 in OOO0OOOOO0OOOOOO0 ['data']['box_list']:#line:156
                        OOO0OOO0000O00000 =OO0OOOOO0OOOO0OO0 ['id']#line:158
                        OO0OOO00O00O00O0O =OO0OOOOO0OOOO0OO0 ['name']#line:159
                        OOO00OO0OO0O0O0O0 =OO0OOOOO0OOOO0OO0 ['inventory']#line:160
                        OO0O0000OOO000000 =OO0OOOOO0OOOO0OO0 ['need_debris']#line:161
                        if float (OOO0OOO0000O00000 )==float (OOOO0O00O00000000 .box ):#line:162
                            print (f'【幸运宝箱】:名称:{OO0OOO00O00O00O0O}丨需要碎片:{OO0O0000OOO000000}丨剩余:{OOO00OO0OO0O0O0O0}')#line:163
                            if float (O0O0OOO00OO000O0O )>=float (OO0O0000OOO000000 ):#line:164
                                O0OOOOO0000OO00OO ={'id':OOOO0O00O00000000 .box }#line:165
                                OO0O0O0O000O0OOO0 =requests .request ('post','https://qct.qitusky.cn/api/LuckyBox/exchange',headers =OOOO0O00O00000000 .headers ,data =O0OOOOO0000OO00OO ).json ()#line:166
                                if 'code'in OO0O0O0O000O0OOO0 :#line:168
                                    if OO0O0O0O000O0OOO0 ['code']==1 :#line:169
                                        print (f'【兑换宝箱】:{OO0O0O0O000O0OOO0["msg"]}丨获得{OO0O0O0O000O0OOO0["data"]["name"]}')#line:170
        except Exception as O0O0OOOO0000O0O00 :#line:173
            print (O0O0OOOO0000O0O00 )#line:174
def start ():#line:177
    try :#line:178
        update_the_validation ()#line:179
        OO0O0000OOOO000OO =os_qinglong ()#line:180
        print (f"==========共找到{len(OO0O0000OOOO000OO)}个账号==========")#line:181
        for OOOOO00OOOOOOO0OO in OO0O0000OOOO000OO :#line:182
            print (f"------------正在执行第{OO0O0000OOOO000OO.index(OOOOO00OOOOOOO0OO) + 1}个账号------------")#line:183
            O00O0O0O0OO0OO000 =Template (OOOOO00OOOOOOO0OO )#line:184
            if O00O0O0O0OO0OO000 .base_info ():#line:186
                O00O0O0O0OO0OO000 .LuckyBox ()#line:188
                O00O0O0O0OO0OO000 .Game_index ()#line:190
                O00O0O0O0OO0OO000 .playInfo ()#line:192
                time .sleep (random .randint (2 ,3 ))#line:197
            else :#line:198
                print ('token失效')#line:199
    except Exception as OO0O00OOO0O0OO00O :#line:200
        print (OO0O00OOO0O0OO00O )#line:201
def version_of_the_validation ():#line:203
    return str ((58 -56 )/10 )#line:204
if __name__ =='__main__':#line:207
    start ()#line:208

