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
token = ''''''  # 调试token


##################################下面不要动##################################    is_real

host ='https://qct.qitusky.cn'#line:1
git ='https://gitee.com'#line:2
def os_qinglong ():#line:3
    if application in os .environ :#line:4
        OO0OOOO00OO00O0O0 =os .environ [application ].split ('\n')#line:5
        if len (OO0OOOO00OO00O0O0 )>0 :#line:6
            return OO0OOOO00OO00O0O0 #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        O0O0OO0O00O000O0O =token .split ('\n')#line:19
        if len (O0O0OO0O00O000O0O )>0 :#line:20
            return O0O0OO0O00O000O0O #line:21
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
        OO00O0OO00O00OO0O =gitee_validation ()#line:35
        if version_of_the_validation ()<OO00O0OO00O00OO0O ['Tower']['edition']:#line:36
            print (f'当前脚本名字: {OO00O0OO00O00OO0O["Tower"]["text"]}')#line:37
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O0OO00O00OO0O["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:38
            print (f'更新内容=>> {OO00O0OO00O00OO0O["Tower"]["content"]}')#line:39
        else :#line:40
            print (f'当前脚本名字: {OO00O0OO00O00OO0O["Tower"]["text"]}')#line:41
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O0OO00O00OO0O["Tower"]["edition"]}   ✅')#line:42
            print (f'更新内容=>> {OO00O0OO00O00OO0O["Tower"]["content"]}')#line:43
    except Exception as O000O0000O000000O :#line:44
        print (O000O0000O000000O )#line:45
class Template :#line:50
    def __init__ (OO0OOOO00OOO0OOO0 ,OO0O00O0OOO0O000O ):#line:52
        try :#line:53
            OO0OOOO00OOO0OOO0 .token =OO0O00O0OOO0O000O .split ('&')[0 ]#line:54
            OO0OOOO00OOO0OOO0 .box =OO0O00O0OOO0O000O .split ('&')[1 ]#line:55
            OO0OOOO00OOO0OOO0 .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OO0OOOO00OOO0OOO0 .token ,'server':'true','phone-type':'android',}#line:67
        except Exception as O00OOO00OO0O00OOO :#line:68
            print ('变量格式错误')#line:69
    def base_info (OOO00O00000OOOO00 ):#line:72
        try :#line:73
            O00OO0O0O000OO000 =requests .request ('post',f'{host}/api/User/info',headers =OOO00O00000OOOO00 .headers ).json ()#line:74
            if 'code'in O00OO0O0O000OO000 :#line:76
                if O00OO0O0O000OO000 ['code']==1 :#line:77
                    O00O0O0OO0O00OOO0 =O00OO0O0O000OO000 ['data']['nickname']#line:78
                    O0O0O0OO0OOOO0OOO =O00OO0O0O000OO000 ['data']['id']#line:79
                    OO0O000O0O00OO00O =O00OO0O0O000OO000 ['data']['score']#line:80
                    print (f'【账号信息】:昵称:{O00O0O0OO0O00OOO0}丨ID:{O0O0O0OO0OOOO0OOO}丨金币:{str(OO0O000O0O00OO00O)[:5]}')#line:81
                if O00OO0O0O000OO000 ['code']==302 :#line:82
                    return False #line:83
            return True #line:84
        except Exception as OOOOO000O000O0OOO :#line:85
            print (OOOOO000O000O0OOO )#line:86
    def playInfo (OO00OOOO0OO00000O ):#line:89
        try :#line:90
            O0OO0OO00OO0OO000 =requests .request ('post',f'{host}/api/Game/playInfo',headers =OO00OOOO0OO00000O .headers ).json ()#line:91
            if 'code'in O0OO0OO00OO0OO000 :#line:93
                if O0OO0OO00OO0OO000 ['code']==1 :#line:94
                    O000OOOOO0O0O0O00 =O0OO0OO00OO0OO000 ['data']['play_tier']#line:95
                    OOOOO0O00OOOOOO00 =O0OO0OO00OO0OO000 ['data']['play_tier_need_money']#line:96
                    O0OO00000OO0OO0O0 =O0OO0OO00OO0OO000 ['data']['user_money']#line:97
                    OO00OO0000O0O00OO =O0OO0OO00OO0OO000 ['data']['play_finish_money']#line:98
                    print (f'【参与闯关】:层数:{O000OOOOO0O0O0O00}丨余额:{str(O0OO00000OO0OO0O0).split(".")[0]}丨闯关花费:{OOOOO0O00OOOOOO00}丨预计获得:{OO00OO0000O0O00OO}')#line:99
        except Exception as O0OOOOO00O00O0OO0 :#line:103
            print (O0OOOOO00O00O0OO0 )#line:104
    def setAutoPlay (OOOOOO0OO00O00OOO ):#line:107
        try :#line:108
            OOO000O0000000O00 ={'state':'1'}#line:111
            O0000O0O0OOO0O00O =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =OOOOOO0OO00O00OOO .headers ,data =OOO000O0000000O00 ).json ()#line:112
            if 'code'in O0000O0O0OOO0O00O :#line:114
                if O0000O0O0OOO0O00O ['code']==1 :#line:115
                    print (f'【自动闯关】:{O0000O0O0OOO0O00O["msg"]}')#line:116
                if O0000O0O0OOO0O00O ['code']==0 :#line:117
                    print (f'【自动闯关】:{O0000O0O0OOO0O00O["msg"]}')#line:118
        except Exception as O00O00OOOOOO0OOO0 :#line:119
            print (O00O00OOOOOO0OOO0 )#line:120
    def Game_index (O00OO0O00O000O0OO ):#line:123
        OO00000OO0OOO0OOO =requests .request ('post',f'{host}/api/Game/index',headers =O00OO0O00O000O0OO .headers ).json ()#line:124
        if 'code'in OO00000OO0OOO0OOO :#line:126
            if OO00000OO0OOO0OOO ['code']==1 :#line:127
                O00OOO0O0OOO00OO0 =OO00000OO0OOO0OOO ['data']['is_auto_play']#line:128
                OO0OOOOO0OOOO00O0 =OO00000OO0OOO0OOO ['data']['is_game_ing']#line:129
                OO0O0O000O0OO0OOO =OO00000OO0OOO0OOO ['data']['is_vip']#line:130
                O0000O0O0O0OOOO0O =OO00000OO0OOO0OOO ['data']['npc_hint']#line:131
                print (f'【游戏状态】:自动闯关:{O00OOO0O0OOO00OO0}丨VIP:{OO0O0O000O0OO0OOO}')#line:132
                if not O00OOO0O0OOO00OO0 :#line:133
                    O00OO0O00O000O0OO .setAutoPlay ()#line:134
    def LuckyBox (OO00OO000OO0OO0O0 ):#line:137
        try :#line:138
            OOO00OO0O0O0000OO =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OO00OO000OO0OO0O0 .headers ).json ()#line:139
            if 'code'in OOO00OO0O0O0000OO :#line:141
                if OOO00OO0O0O0000OO ['code']==1 :#line:142
                    O0O000OO0O00O0OOO =OOO00OO0O0O0000OO ['data']['debris']#line:143
                    OOOO0OO00OO00OOOO =OOO00OO0O0O0000OO ['data']['is_draw']#line:144
                    print (f'【幸运宝箱】:碎片:{str(O0O000OO0O00O0OOO).split(".")[0]}丨当前设置开启宝箱ID:{OO00OO000OO0OO0O0.box}')#line:145
                    if not OOOO0OO00OO00OOOO :#line:146
                        O0O000OO000OOO00O =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OO00OO000OO0OO0O0 .headers ).json ()#line:147
                        if 'code'in O0O000OO000OOO00O :#line:149
                            if O0O000OO000OOO00O ['code']==1 :#line:150
                                OO0O0OOO0OOOO0OOO =O0O000OO000OOO00O ['data']['nub']#line:151
                                print (f'【领取碎片】:获得:{OO0O0OOO0OOOO0OOO}')#line:152
                    for OO0000OO0000OO00O in OOO00OO0O0O0000OO ['data']['box_list']:#line:153
                        O000O0O0000OOO0OO =OO0000OO0000OO00O ['id']#line:155
                        OOOOOO00O0OOO0OOO =OO0000OO0000OO00O ['name']#line:156
                        OOOOO0OO00O00OO0O =OO0000OO0000OO00O ['inventory']#line:157
                        O0O0000O00O000000 =OO0000OO0000OO00O ['need_debris']#line:158
                        if float (O000O0O0000OOO0OO )==float (OO00OO000OO0OO0O0 .box ):#line:159
                            print (f'【幸运宝箱】:名称:{OOOOOO00O0OOO0OOO}丨需要碎片:{O0O0000O00O000000}丨剩余:{OOOOO0OO00O00OO0O}')#line:160
                            if float (O0O000OO0O00O0OOO )>=float (O0O0000O00O000000 ):#line:161
                                OOO0O0OOO0OOOO000 ={'id':OO00OO000OO0OO0O0 .box }#line:162
                                OOO000000OOOO000O =requests .request ('post','https://qct.qitusky.cn/api/LuckyBox/exchange',headers =OO00OO000OO0OO0O0 .headers ,data =OOO0O0OOO0OOOO000 ).json ()#line:163
                                if 'code'in OOO000000OOOO000O :#line:165
                                    if OOO000000OOOO000O ['code']==1 :#line:166
                                        print (f'【兑换宝箱】:{OOO000000OOOO000O["msg"]}丨获得{OOO000000OOOO000O["data"]["name"]}')#line:167
        except Exception as O0O00000000OOO00O :#line:170
            print (O0O00000000OOO00O )#line:171
def start ():#line:174
    try :#line:175
        update_the_validation ()#line:176
        OOOO0OOOO000O0O0O =os_qinglong ()#line:177
        print (f"==========共找到{len(OOOO0OOOO000O0O0O)}个账号==========")#line:178
        for OOO000OO0OO0O0OOO in OOOO0OOOO000O0O0O :#line:179
            print (f"------------正在执行第{OOOO0OOOO000O0O0O.index(OOO000OO0OO0O0OOO) + 1}个账号------------")#line:180
            OO0OO00O00OOOO000 =Template (OOO000OO0OO0O0OOO )#line:181
            if OO0OO00O00OOOO000 .base_info ():#line:183
                OO0OO00O00OOOO000 .LuckyBox ()#line:185
                OO0OO00O00OOOO000 .Game_index ()#line:187
                OO0OO00O00OOOO000 .playInfo ()#line:189
                time .sleep (random .randint (2 ,3 ))#line:194
            else :#line:195
                print ('token失效')#line:196
    except Exception as O0O000000OOO0O0O0 :#line:197
        print (O0O000000OOO0O0O0 )#line:198
def version_of_the_validation ():#line:200
    return str ((58 -56 )/10 )#line:201
if __name__ =='__main__':#line:204
    start ()#line:205
