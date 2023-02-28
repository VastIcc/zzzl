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
        OO000O000OOOO0000 =os .environ [application ].split ('\n')#line:5
        if len (OO000O000OOOO0000 )>0 :#line:6
            return OO000O000OOOO0000 #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        O0OOOOOO0OOO00000 =token .split ('\n')#line:19
        if len (O0OOOOOO0OOO00000 )>0 :#line:20
            return O0OOOOOO0OOO00000 #line:21
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
        O000OOO00OO00OO00 =gitee_validation ()#line:35
        if version_of_the_validation ()<O000OOO00OO00OO00 ['Tower']['edition']:#line:36
            print (f'当前脚本名字: {O000OOO00OO00OO00["Tower"]["text"]}')#line:37
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOO00OO00OO00["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:38
            print (f'更新内容=>> {O000OOO00OO00OO00["Tower"]["content"]}')#line:39
        else :#line:40
            print (f'当前脚本名字: {O000OOO00OO00OO00["Tower"]["text"]}')#line:41
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOO00OO00OO00["Tower"]["edition"]}   ✅')#line:42
            print (f'更新内容=>> {O000OOO00OO00OO00["Tower"]["content"]}')#line:43
    except Exception as O00O000O00O0O000O :#line:44
        print (O00O000O00O0O000O )#line:45
class Template :#line:50
    def __init__ (O0O00O0OO00O000O0 ,O000OOO0OO0000OOO ):#line:52
        try :#line:53
            O0O00O0OO00O000O0 .token =O000OOO0OO0000OOO .split ('&')[0 ]#line:54
            O0O00O0OO00O000O0 .box =O000OOO0OO0000OOO .split ('&')[1 ]#line:55
            O0O00O0OO00O000O0 .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':O0O00O0OO00O000O0 .token ,'server':'true','phone-type':'android',}#line:67
        except Exception as O0O00OOOO00O0OOO0 :#line:68
            print ('变量格式错误')#line:69
    def base_info (O0O0000O00OO00000 ):#line:72
        try :#line:73
            O0O00000OOO0OOOO0 =requests .request ('post',f'{host}/api/User/info',headers =O0O0000O00OO00000 .headers ).json ()#line:74
            if 'code'in O0O00000OOO0OOOO0 :#line:76
                if O0O00000OOO0OOOO0 ['code']==1 :#line:77
                    O00O000O00O0O0000 =O0O00000OOO0OOOO0 ['data']['nickname']#line:78
                    O0OO0O0OO0OO0O0OO =O0O00000OOO0OOOO0 ['data']['id']#line:79
                    OO0OOO0OO0OOOOOO0 =O0O00000OOO0OOOO0 ['data']['score']#line:80
                    print (f'账号信息:昵称:{O00O000O00O0O0000}丨ID:{O0OO0O0OO0OO0O0OO}丨金币:{str(OO0OOO0OO0OOOOOO0)[:5]}')#line:81
                if O0O00000OOO0OOOO0 ['code']==302 :#line:82
                    return False #line:83
            return True #line:84
        except Exception as O0OO0O0OO0O000000 :#line:85
            print (O0OO0O0OO0O000000 )#line:86
    def playInfo (OOOOO000OO00O0000 ):#line:89
        try :#line:90
            OOO0OO0OOOOOOO0O0 =requests .request ('post',f'{host}/api/Game/playInfo',headers =OOOOO000OO00O0000 .headers ).json ()#line:91
            if 'code'in OOO0OO0OOOOOOO0O0 :#line:93
                if OOO0OO0OOOOOOO0O0 ['code']==1 :#line:94
                    O0OOO0OOO000O00OO =OOO0OO0OOOOOOO0O0 ['data']['play_tier']#line:95
                    OO00O00OOO0000O00 =OOO0OO0OOOOOOO0O0 ['data']['play_tier_need_money']#line:96
                    O0O0OOO00OOO0O0O0 =OOO0OO0OOOOOOO0O0 ['data']['user_money']#line:97
                    OOOO0OOOOO0O0OO00 =OOO0OO0OOOOOOO0O0 ['data']['play_finish_money']#line:98
                    print (f'参与闯关:层数:{O0OOO0OOO000O00OO}丨余额:{str(O0O0OOO00OOO0O0O0).split(".")[0]}丨闯关花费:{OO00O00OOO0000O00}丨预计获得:{OOOO0OOOOO0O0OO00}')#line:99
        except Exception as O0OO00O0O0O0OOO0O :#line:103
            print (O0OO00O0O0O0OOO0O )#line:104
    def setAutoPlay (OO0O0OO0OOOO0OOO0 ):#line:107
        try :#line:108
            O0OOO000O0O0O0O0O ={'state':'1'}#line:111
            O00OO0O0O0000O00O =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =OO0O0OO0OOOO0OOO0 .headers ,data =O0OOO000O0O0O0O0O ).json ()#line:112
            if 'code'in O00OO0O0O0000O00O :#line:114
                if O00OO0O0O0000O00O ['code']==1 :#line:115
                    print (f'自动闯关:{O00OO0O0O0000O00O["msg"]}')#line:116
                if O00OO0O0O0000O00O ['code']==0 :#line:117
                    print (f'自动闯关:{O00OO0O0O0000O00O["msg"]}')#line:118
        except Exception as O00OOO0O0O00000O0 :#line:119
            print (O00OOO0O0O00000O0 )#line:120
    def Game_index (OO00OO0O0O00OOOO0 ):#line:123
        O0000O0OOO0O00O00 =requests .request ('post',f'{host}/api/Game/index',headers =OO00OO0O0O00OOOO0 .headers ).json ()#line:124
        if 'code'in O0000O0OOO0O00O00 :#line:126
            if O0000O0OOO0O00O00 ['code']==1 :#line:127
                O00OOO0OOO00O000O =O0000O0OOO0O00O00 ['data']['is_auto_play']#line:128
                OOO0OO000O000O000 =O0000O0OOO0O00O00 ['data']['is_game_ing']#line:129
                O0OO00OO0O0OOOO0O =O0000O0OOO0O00O00 ['data']['is_vip']#line:130
                O0O0OOOOO00O000OO =O0000O0OOO0O00O00 ['data']['npc_hint']#line:131
                print (f'游戏状态:自动闯关:{O00OOO0OOO00O000O}丨VIP:{O0OO00OO0O0OOOO0O}')#line:132
                if not O00OOO0OOO00O000O :#line:133
                    OO00OO0O0O00OOOO0 .setAutoPlay ()#line:134
    def LuckyBox (O0O0O0000O0OOOOOO ):#line:137
        try :#line:138
            O00O0O000O0O0000O =requests .request ('post',f'{host}/api/LuckyBox/index',headers =O0O0O0000O0OOOOOO .headers ).json ()#line:139
            if 'code'in O00O0O000O0O0000O :#line:141
                if O00O0O000O0O0000O ['code']==1 :#line:142
                    OO0O0O0O0OOOO0O00 =O00O0O000O0O0000O ['data']['debris']#line:143
                    OO0OO0OOO0O0O000O =O00O0O000O0O0000O ['data']['is_draw']#line:144
                    print (f'幸运宝箱:碎片:{str(OO0O0O0O0OOOO0O00).split(".")[0]}丨当前设置开启宝箱ID:{O0O0O0000O0OOOOOO.box}')#line:145
                    if not OO0OO0OOO0O0O000O :#line:146
                        O0OOOOO000OOO0OOO =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =O0O0O0000O0OOOOOO .headers ).json ()#line:147
                        if 'code'in O0OOOOO000OOO0OOO :#line:149
                            if O0OOOOO000OOO0OOO ['code']==1 :#line:150
                                OOO00O0OO0OO000OO =O0OOOOO000OOO0OOO ['data']['nub']#line:151
                                print (f'领取碎片:获得:{OOO00O0OO0OO000OO}')#line:152
                    for O00O00OO0OOO0OOO0 in O00O0O000O0O0000O ['data']['box_list']:#line:153
                        OO0O0OOO000OO000O =O00O00OO0OOO0OOO0 ['id']#line:155
                        O0O0OOO00OOOOO000 =O00O00OO0OOO0OOO0 ['name']#line:156
                        O00O00OOOOOOOO0OO =O00O00OO0OOO0OOO0 ['inventory']#line:157
                        O0O00O00OOO00O0OO =O00O00OO0OOO0OOO0 ['need_debris']#line:158
                        if float (OO0O0OOO000OO000O )==float (O0O0O0000O0OOOOOO .box ):#line:159
                            print (f'        名称:{O0O0OOO00OOOOO000}丨需要碎片:{O0O00O00OOO00O0OO}丨剩余:{O00O00OOOOOOOO0OO}')#line:160
                            if float (OO0O0O0O0OOOO0O00 )>=float (O0O00O00OOO00O0OO ):#line:161
                                OO0O0O0O00OO0OOO0 ={'id':O0O0O0000O0OOOOOO .box }#line:162
                                OO00O00O0OOO00OO0 =requests .request ('post','https://qct.qitusky.cn/api/LuckyBox/exchange',headers =O0O0O0000O0OOOOOO .headers ,data =OO0O0O0O00OO0OOO0 ).json ()#line:163
                                if 'code'in OO00O00O0OOO00OO0 :#line:165
                                    if OO00O00O0OOO00OO0 ['code']==1 :#line:166
                                        print (f'兑换宝箱:{OO00O00O0OOO00OO0["msg"]}丨获得{OO00O00O0OOO00OO0["data"]["name"]}')#line:167
        except Exception as O00O0000OO000OOOO :#line:170
            print (O00O0000OO000OOOO )#line:171
def start ():#line:174
    try :#line:175
        update_the_validation ()#line:176
        O000OO0000000000O =os_qinglong ()#line:177
        print (f"==========共找到{len(O000OO0000000000O)}个账号==========")#line:178
        for O0O00OOO0000O0OO0 in O000OO0000000000O :#line:179
            print (f"------------正在执行第{O000OO0000000000O.index(O0O00OOO0000O0OO0) + 1}个账号------------")#line:180
            O0O0OO0OO000O0OO0 =Template (O0O00OOO0000O0OO0 )#line:181
            if O0O0OO0OO000O0OO0 .base_info ():#line:183
                O0O0OO0OO000O0OO0 .LuckyBox ()#line:185
                O0O0OO0OO000O0OO0 .Game_index ()#line:187
                O0O0OO0OO000O0OO0 .playInfo ()#line:189
                time .sleep (random .randint (2 ,3 ))#line:194
            else :#line:195
                print ('token失效')#line:196
    except Exception as O00O0O0OOOOOOOO0O :#line:197
        print (O00O0O0OOOOOOOO0O )#line:198
def version_of_the_validation ():#line:200
    return str ((58 -56 )/10 )#line:201
if __name__ =='__main__':#line:204
    start ()#line:205
