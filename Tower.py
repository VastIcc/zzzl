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
        O0OOOOO0O0OO0OO00 =os .environ [application ].split ('\n')#line:5
        if len (O0OOOOO0O0OO0OO00 )>0 :#line:6
            return O0OOOOO0O0OO0OO00 #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        OOO00OOOOO0O0OOOO =token .split ('\n')#line:19
        if len (OOO00OOOOO0O0OOOO )>0 :#line:20
            return OOO00OOOOO0O0OOOO #line:21
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
        OO00O0O000OOOO0OO =gitee_validation ()#line:35
        if version_of_the_validation ()<OO00O0O000OOOO0OO ['Tower']['edition']:#line:36
            print (f'当前脚本名字: {OO00O0O000OOOO0OO["Tower"]["text"]}')#line:37
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O0O000OOOO0OO["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:38
            print (f'更新内容=>> {OO00O0O000OOOO0OO["Tower"]["content"]}')#line:39
        else :#line:40
            print (f'当前脚本名字: {OO00O0O000OOOO0OO["Tower"]["text"]}')#line:41
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O0O000OOOO0OO["Tower"]["edition"]}   ✅')#line:42
            print (f'更新内容=>> {OO00O0O000OOOO0OO["Tower"]["content"]}')#line:43
    except Exception as O000O000OOO0O0O0O :#line:44
        print (O000O000OOO0O0O0O )#line:45
class Template :#line:50
    def __init__ (O00O0OO0000OO000O ,O000O00O000O0OOO0 ):#line:52
        try :#line:53
            O00O0OO0000OO000O .token =O000O00O000O0OOO0 .split ('&')[0 ]#line:54
            O00O0OO0000OO000O .box =O000O00O000O0OOO0 .split ('&')[1 ]#line:55
            O00O0OO0000OO000O .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':O00O0OO0000OO000O .token ,'server':'true','phone-type':'android',}#line:67
        except Exception as OOO00000OO00O000O :#line:68
            print ('变量格式错误')#line:69
    def base_info (OO00OO00OOOO0O000 ):#line:72
        try :#line:73
            O0OOOO0O00O0OOOOO =requests .request ('post',f'{host}/api/User/info',headers =OO00OO00OOOO0O000 .headers ).json ()#line:74
            if 'code'in O0OOOO0O00O0OOOOO :#line:76
                if O0OOOO0O00O0OOOOO ['code']==1 :#line:77
                    O000OOOOO00OO000O =O0OOOO0O00O0OOOOO ['data']['nickname']#line:78
                    OO00O0O00OO00O0OO =O0OOOO0O00O0OOOOO ['data']['id']#line:79
                    O0O0000OOOOO00OOO =O0OOOO0O00O0OOOOO ['data']['score']#line:80
                    print (f'账号信息:昵称:{O000OOOOO00OO000O}丨ID:{OO00O0O00OO00O0OO}丨金币:{str(O0O0000OOOOO00OOO)[:5]}')#line:81
                if O0OOOO0O00O0OOOOO ['code']==302 :#line:82
                    return False #line:83
            return True #line:84
        except Exception as O0OOO0OO0OO00O0O0 :#line:85
            print (O0OOO0OO0OO00O0O0 )#line:86
    def playInfo (OOOO00O0O0O0OOO0O ):#line:89
        try :#line:90
            O0O00O00O00OO00OO =requests .request ('post',f'{host}/api/Game/playInfo',headers =OOOO00O0O0O0OOO0O .headers ).json ()#line:91
            if 'code'in O0O00O00O00OO00OO :#line:93
                if O0O00O00O00OO00OO ['code']==1 :#line:94
                    OOOO00O00O0O00OO0 =O0O00O00O00OO00OO ['data']['play_tier']#line:95
                    OOOO0O00OOOOO0OOO =O0O00O00O00OO00OO ['data']['play_tier_need_money']#line:96
                    O0OO0000O00OOO0OO =O0O00O00O00OO00OO ['data']['user_money']#line:97
                    O0OOOO00OO0000O00 =O0O00O00O00OO00OO ['data']['play_finish_money']#line:98
                    print (f'参与闯关:层数:{OOOO00O00O0O00OO0}丨余额:{str(O0OO0000O00OOO0OO).split(".")[0]}丨闯关花费:{OOOO0O00OOOOO0OOO}丨预计获得:{O0OOOO00OO0000O00}')#line:99
        except Exception as O0O0O000O00OOOO0O :#line:103
            print (O0O0O000O00OOOO0O )#line:104
    def setAutoPlay (O00000OOO0O0O0000 ):#line:107
        try :#line:108
            OOO0O0O000OO00O0O ={'state':'1'}#line:111
            OO00O0O0O0OO000OO =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O00000OOO0O0O0000 .headers ,data =OOO0O0O000OO00O0O ).json ()#line:112
            if 'code'in OO00O0O0O0OO000OO :#line:114
                if OO00O0O0O0OO000OO ['code']==1 :#line:115
                    print (f'自动闯关:{OO00O0O0O0OO000OO["msg"]}')#line:116
                if OO00O0O0O0OO000OO ['code']==0 :#line:117
                    print (f'自动闯关:{OO00O0O0O0OO000OO["msg"]}')#line:118
        except Exception as O0O0O00O0OOOO0000 :#line:119
            print (O0O0O00O0OOOO0000 )#line:120
    def Game_index (OOO0O0O00OO0OO00O ):#line:123
        OO0O0OO0O00O00OO0 =requests .request ('post',f'{host}/api/Game/index',headers =OOO0O0O00OO0OO00O .headers ).json ()#line:124
        if 'code'in OO0O0OO0O00O00OO0 :#line:126
            if OO0O0OO0O00O00OO0 ['code']==1 :#line:127
                OOOO0OOO0O0OO0OOO =OO0O0OO0O00O00OO0 ['data']['is_auto_play']#line:128
                O0OOOOOOOOOO0OOO0 =OO0O0OO0O00O00OO0 ['data']['is_game_ing']#line:129
                O00OO0O00000O00OO =OO0O0OO0O00O00OO0 ['data']['is_vip']#line:130
                O0000OO0OOO00000O =OO0O0OO0O00O00OO0 ['data']['npc_hint']#line:131
                print (f'游戏状态:自动闯关:{OOOO0OOO0O0OO0OOO}丨VIP:{O00OO0O00000O00OO}')#line:132
                if not OOOO0OOO0O0OO0OOO :#line:133
                    OOO0O0O00OO0OO00O .setAutoPlay ()#line:134
    def LuckyBox (OO0O0OOO0OOO0000O ):#line:137
        try :#line:138
            OO0OOO0OOO0O000OO =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OO0O0OOO0OOO0000O .headers ).json ()#line:139
            if 'code'in OO0OOO0OOO0O000OO :#line:141
                if OO0OOO0OOO0O000OO ['code']==1 :#line:142
                    O000000OO0000O00O =OO0OOO0OOO0O000OO ['data']['debris']#line:143
                    O0OO00000O000OO00 =OO0OOO0OOO0O000OO ['data']['is_draw']#line:144
                    print (f'幸运宝箱:碎片:{str(O000000OO0000O00O).split(".")[0]}丨当前设置开启宝箱ID:{OO0O0OOO0OOO0000O.box}')#line:145
                    if not O0OO00000O000OO00 :#line:146
                        O00O00O00OOO00OO0 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OO0O0OOO0OOO0000O .headers ).json ()#line:147
                        if 'code'in O00O00O00OOO00OO0 :#line:149
                            if O00O00O00OOO00OO0 ['code']==1 :#line:150
                                O0O0000000OO0O000 =O00O00O00OOO00OO0 ['data']['nub']#line:151
                                print (f'领取碎片:获得:{O0O0000000OO0O000}')#line:152
                    for O00OO00OO00O000O0 in OO0OOO0OOO0O000OO ['data']['box_list']:#line:153
                        OO0000O00OOOO0O00 =O00OO00OO00O000O0 ['id']#line:155
                        OOOOO00OO0000O0OO =O00OO00OO00O000O0 ['name']#line:156
                        O000OOOO00O0000O0 =O00OO00OO00O000O0 ['inventory']#line:157
                        OOOO000OO0OO000O0 =O00OO00OO00O000O0 ['need_debris']#line:158
                        if float (OO0000O00OOOO0O00 )==float (OO0O0OOO0OOO0000O .box ):#line:159
                            print (f'幸运宝箱:名称:{OOOOO00OO0000O0OO}丨需要碎片:{OOOO000OO0OO000O0}丨剩余:{O000OOOO00O0000O0}')#line:160
                            if float (O000000OO0000O00O )>=float (OOOO000OO0OO000O0 ):#line:161
                                OOO000OOO0O00O00O ={'id':OO0O0OOO0OOO0000O .box }#line:162
                                OOO0OOOOO0O0O000O =requests .request ('post','https://qct.qitusky.cn/api/LuckyBox/exchange',headers =OO0O0OOO0OOO0000O .headers ,data =OOO000OOO0O00O00O ).json ()#line:163
                                if 'code'in OOO0OOOOO0O0O000O :#line:165
                                    if OOO0OOOOO0O0O000O ['code']==1 :#line:166
                                        print (f'兑换宝箱:{OOO0OOOOO0O0O000O["msg"]}丨获得{OOO0OOOOO0O0O000O["data"]["name"]}')#line:167
        except Exception as OOO00000000O00OOO :#line:170
            print (OOO00000000O00OOO )#line:171
def start ():#line:174
    try :#line:175
        update_the_validation ()#line:176
        OO0OO0OOO0OOO0OOO =os_qinglong ()#line:177
        print (f"==========共找到{len(OO0OO0OOO0OOO0OOO)}个账号==========")#line:178
        for O0O000OO0OOOO0O00 in OO0OO0OOO0OOO0OOO :#line:179
            print (f"------------正在执行第{OO0OO0OOO0OOO0OOO.index(O0O000OO0OOOO0O00) + 1}个账号------------")#line:180
            O0000OOO000OO0O00 =Template (O0O000OO0OOOO0O00 )#line:181
            if O0000OOO000OO0O00 .base_info ():#line:183
                O0000OOO000OO0O00 .LuckyBox ()#line:185
                O0000OOO000OO0O00 .Game_index ()#line:187
                O0000OOO000OO0O00 .playInfo ()#line:189
                time .sleep (random .randint (2 ,3 ))#line:194
            else :#line:195
                print ('token失效')#line:196
    except Exception as OOO00O0O00O0O0OO0 :#line:197
        print (OOO00O0O00O0O0OO0 )#line:198
def version_of_the_validation ():#line:200
    return str ((58 -56 )/10 )#line:201
if __name__ =='__main__':#line:204
    start ()#line:205

