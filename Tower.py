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
        O0O0OO0OOO0O00O0O =os .environ [application ].split ('\n')#line:5
        if len (O0O0OO0OOO0O00O0O )>0 :#line:6
            return O0O0OO0OOO0O00O0O #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        O0OOOOOOOOO0OOO0O =token .split ('\n')#line:19
        if len (O0OOOOOOOOO0OOO0O )>0 :#line:20
            return O0OOOOOOOOO0OOO0O #line:21
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
        O00OOOO0O0000O0OO =gitee_validation ()#line:35
        if version_of_the_validation ()<O00OOOO0O0000O0OO ['Tower']['edition']:#line:36
            print (f'当前脚本名字: {O00OOOO0O0000O0OO["Tower"]["text"]}')#line:37
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OOOO0O0000O0OO["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:38
            print (f'更新内容=>> {O00OOOO0O0000O0OO["Tower"]["content"]}')#line:39
        else :#line:40
            print (f'当前脚本名字: {O00OOOO0O0000O0OO["Tower"]["text"]}')#line:41
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OOOO0O0000O0OO["Tower"]["edition"]}   ✅')#line:42
            print (f'更新内容=>> {O00OOOO0O0000O0OO["Tower"]["content"]}')#line:43
    except Exception as OOOO0000O00000O0O :#line:44
        print (OOOO0000O00000O0O )#line:45
class Template :#line:50
    def __init__ (O0OO0OOOOO0O0OOO0 ,OO0OOO000O00OOO0O ):#line:52
        try :#line:53
            O0OO0OOOOO0O0OOO0 .token =OO0OOO000O00OOO0O .split ('&')[0 ]#line:54
            O0OO0OOOOO0O0OOO0 .box =OO0OOO000O00OOO0O .split ('&')[1 ]#line:55
            O0OO0OOOOO0O0OOO0 .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':O0OO0OOOOO0O0OOO0 .token ,'server':'true','phone-type':'android',}#line:67
        except Exception as O0000000OO0OOO0OO :#line:68
            print ('变量格式错误')#line:69
    def base_info (O00O0000O00OO00O0 ):#line:72
        try :#line:73
            OO000000000O0O00O =requests .request ('post',f'{host}/api/User/info',headers =O00O0000O00OO00O0 .headers ).json ()#line:74
            if 'code'in OO000000000O0O00O :#line:76
                if OO000000000O0O00O ['code']==1 :#line:77
                    O000OO0OO00000000 =OO000000000O0O00O ['data']['nickname']#line:78
                    OOO0OO000O000O000 =OO000000000O0O00O ['data']['id']#line:79
                    OO0000OOOOOO0O0O0 =OO000000000O0O00O ['data']['score']#line:80
                    print (f'账号信息:昵称:{O000OO0OO00000000}丨ID:{OOO0OO000O000O000}丨金币:{str(OO0000OOOOOO0O0O0)[:5]}')#line:81
                if OO000000000O0O00O ['code']==302 :#line:82
                    return False #line:83
            return True #line:84
        except Exception as O0O0OO0O00OOOO0O0 :#line:85
            print (O0O0OO0O00OOOO0O0 )#line:86
    def playInfo (OO0OO00OOOO0O0O00 ):#line:89
        try :#line:90
            O00OO000000OOO0O0 =requests .request ('post',f'{host}/api/Game/playInfo',headers =OO0OO00OOOO0O0O00 .headers ).json ()#line:91
            if 'code'in O00OO000000OOO0O0 :#line:93
                if O00OO000000OOO0O0 ['code']==1 :#line:94
                    OO0O0OO00O00O0OO0 =O00OO000000OOO0O0 ['data']['play_tier']#line:95
                    O00OOO00OO0O00OOO =O00OO000000OOO0O0 ['data']['play_tier_need_money']#line:96
                    O00OO0O0O00000O00 =O00OO000000OOO0O0 ['data']['user_money']#line:97
                    OO0O0000OO000OO0O =O00OO000000OOO0O0 ['data']['play_finish_money']#line:98
                    print (f'参与闯关:层数:{OO0O0OO00O00O0OO0}丨余额:{str(O00OO0O0O00000O00).split(".")[0]}丨闯关花费:{O00OOO00OO0O00OOO}丨预计获得:{OO0O0000OO000OO0O}')#line:99
        except Exception as O0000000OO0OO0OOO :#line:103
            print (O0000000OO0OO0OOO )#line:104
    def setAutoPlay (OOO0000OO0OOOO000 ):#line:107
        try :#line:108
            OOO0OOO0000OO0OOO ={'state':'1'}#line:111
            OO0000OO000OOO00O =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =OOO0000OO0OOOO000 .headers ,data =OOO0OOO0000OO0OOO ).json ()#line:112
            if 'code'in OO0000OO000OOO00O :#line:114
                if OO0000OO000OOO00O ['code']==1 :#line:115
                    print (f'自动闯关:{OO0000OO000OOO00O["msg"]}')#line:116
                if OO0000OO000OOO00O ['code']==0 :#line:117
                    print (f'自动闯关:{OO0000OO000OOO00O["msg"]}')#line:118
        except Exception as OOOO00O0OO00O00OO :#line:119
            print (OOOO00O0OO00O00OO )#line:120
    def Game_index (O000OO0O0O00000O0 ):#line:123
        O0OOOOOOO00000OOO =requests .request ('post',f'{host}/api/Game/index',headers =O000OO0O0O00000O0 .headers ).json ()#line:124
        if 'code'in O0OOOOOOO00000OOO :#line:126
            if O0OOOOOOO00000OOO ['code']==1 :#line:127
                O00O0O000O0O000O0 =O0OOOOOOO00000OOO ['data']['is_auto_play']#line:128
                OO0O0O0000O000O0O =O0OOOOOOO00000OOO ['data']['is_game_ing']#line:129
                O0000OO0000OO0O00 =O0OOOOOOO00000OOO ['data']['is_vip']#line:130
                O00000O0000OOO00O =O0OOOOOOO00000OOO ['data']['npc_hint']#line:131
                print (f'游戏状态:自动闯关:{O00O0O000O0O000O0}丨VIP:{O0000OO0000OO0O00}')#line:132
                if not O00O0O000O0O000O0 :#line:133
                    O000OO0O0O00000O0 .setAutoPlay ()#line:134
    def LuckyBox (O00O0000000OO0O0O ):#line:137
        try :#line:138
            O0OOO0000OO0O00OO =requests .request ('post',f'{host}/api/LuckyBox/index',headers =O00O0000000OO0O0O .headers ).json ()#line:139
            if 'code'in O0OOO0000OO0O00OO :#line:141
                if O0OOO0000OO0O00OO ['code']==1 :#line:142
                    OOO0OOOOOO0OOO000 =O0OOO0000OO0O00OO ['data']['debris']#line:143
                    OO0OO000OO0O00O0O =O0OOO0000OO0O00OO ['data']['is_draw']#line:144
                    print (f'幸运宝箱:碎片:{str(OOO0OOOOOO0OOO000).split(".")[0]}丨当前设置开启宝箱ID:{O00O0000000OO0O0O.box}')#line:145
                    if not OO0OO000OO0O00O0O :#line:146
                        print ('领取碎片')#line:147
                        O0O0O000OOOOO0O00 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =O00O0000000OO0O0O .headers ).json ()#line:148
                        if 'code'in O0O0O000OOOOO0O00 :#line:150
                            if O0O0O000OOOOO0O00 ['code']==1 :#line:151
                                O000000O0000OO0OO =O0O0O000OOOOO0O00 ['data']['nub']#line:152
                                print (f'领取碎片:获得:{O000000O0000OO0OO}')#line:153
                    for OOO000O00O0O000O0 in O0OOO0000OO0O00OO ['data']['box_list']:#line:154
                        O0OO000O0OO00000O =OOO000O00O0O000O0 ['id']#line:156
                        O0OOOO0OOOOO000OO =OOO000O00O0O000O0 ['name']#line:157
                        O00O0O00OO0O0O0OO =OOO000O00O0O000O0 ['inventory']#line:158
                        OOO00OOOO0O000000 =OOO000O00O0O000O0 ['need_debris']#line:159
                        print (f'        名称:{O0OOOO0OOOOO000OO}丨需要碎片:{OOO00OOOO0O000000}丨剩余:{O00O0O00OO0O0O0OO}')#line:160
                        if float (O0OO000O0OO00000O )==float (O00O0000000OO0O0O .box ):#line:161
                            if float (OOO0OOOOOO0OOO000 )>=float (OOO00OOOO0O000000 ):#line:162
                                O0O000O0OO0O0O000 ={'id':O00O0000000OO0O0O .box }#line:163
                                OO0O0O000OOO0OOOO =requests .request ('post','https://qct.qitusky.cn/api/LuckyBox/exchange',headers =O00O0000000OO0O0O .headers ,data =O0O000O0OO0O0O000 ).json ()#line:164
                                if 'code'in OO0O0O000OOO0OOOO :#line:166
                                    if OO0O0O000OOO0OOOO ['code']==1 :#line:167
                                        print (f'兑换宝箱:{OO0O0O000OOO0OOOO["msg"]}丨获得{OO0O0O000OOO0OOOO["data"]["name"]}')#line:168
        except Exception as O000OOOOOOO0O00OO :#line:171
            print (O000OOOOOOO0O00OO )#line:172
def start ():#line:175
    try :#line:176
        update_the_validation ()#line:177
        OO000O0OO00O0O000 =os_qinglong ()#line:178
        print (f"==========共找到{len(OO000O0OO00O0O000)}个账号==========")#line:179
        for OO000OOO0000OO00O in OO000O0OO00O0O000 :#line:180
            print (f"------------正在执行第{OO000O0OO00O0O000.index(OO000OOO0000OO00O) + 1}个账号------------")#line:181
            OOO00OOOOOOO0OO0O =Template (OO000OOO0000OO00O )#line:182
            if OOO00OOOOOOO0OO0O .base_info ():#line:184
                OOO00OOOOOOO0OO0O .LuckyBox ()#line:186
                OOO00OOOOOOO0OO0O .Game_index ()#line:188
                OOO00OOOOOOO0OO0O .playInfo ()#line:190
                time .sleep (random .randint (2 ,3 ))#line:195
            else :#line:196
                print ('token失效')#line:197
    except Exception as O000OOOO0O0OOO000 :#line:198
        print (O000OOOO0O0OOO000 )#line:199
def version_of_the_validation ():#line:201
    return str ((57 -56 )/10 )#line:202
if __name__ =='__main__':#line:205
    start ()#line:206

