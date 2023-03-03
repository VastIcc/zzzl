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
@ 版本 0.3
"""
application = 'qc_token'  # 变量名
token = ''  # 


##################################下面不要动##################################    is_real
host ='https://qct.qitusky.cn'#line:1
git ='https://gitee.com'#line:2
def os_qinglong ():#line:3
    if application in os .environ :#line:4
        OOOO000O0O0000OO0 =os .environ [application ].split ('\n')#line:5
        if len (OOOO000O0O0000OO0 )>0 :#line:6
            return OOOO000O0O0000OO0 #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        OO00OO0O00O0OO00O =token .split ('\n')#line:19
        if len (OO00OO0O00O0OO00O )>0 :#line:20
            return OO00OO0O00O0OO00O #line:21
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
        OO0000OOO0000O00O =gitee_validation ()#line:35
        if version_of_the_validation ()<OO0000OOO0000O00O ['Tower']['edition']:#line:36
            print (f'当前脚本名字: {OO0000OOO0000O00O["Tower"]["text"]}')#line:37
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0000OOO0000O00O["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:38
            print (f'更新内容=>> {OO0000OOO0000O00O["Tower"]["content"]}')#line:39
        else :#line:40
            print (f'当前脚本名字: {OO0000OOO0000O00O["Tower"]["text"]}')#line:41
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0000OOO0000O00O["Tower"]["edition"]}   ✅')#line:42
            print (f'更新内容=>> {OO0000OOO0000O00O["Tower"]["content"]}')#line:43
    except Exception as O00OOOOOO000OO000 :#line:44
        print (O00OOOOOO000OO000 )#line:45
class Template :#line:48
    def __init__ (OO00000OOO0000O0O ,OO00OO0O0OOOO0OO0 ):#line:50
        try :#line:51
            OO00000OOO0000O0O .token =OO00OO0O0OOOO0OO0 .split ('&')[0 ]#line:52
            OO00000OOO0000O0O .box =OO00OO0O0OOOO0OO0 .split ('&')[1 ]#line:53
            OO00000OOO0000O0O .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OO00000OOO0000O0O .token ,'server':'true','phone-type':'android',}#line:65
        except Exception as O0O00O0OOO000OO0O :#line:66
            print ('变量格式错误')#line:67
    def base_info (OOO0O0OOO0O0O0OO0 ):#line:70
        try :#line:71
            OO0O000O0OOOOOO0O =requests .request ('post',f'{host}/api/User/info',headers =OOO0O0OOO0O0O0OO0 .headers ).json ()#line:72
            if 'code'in OO0O000O0OOOOOO0O :#line:74
                if OO0O000O0OOOOOO0O ['code']==1 :#line:75
                    O0OOO0OOO00OO0O00 =OO0O000O0OOOOOO0O ['data']['nickname']#line:76
                    OOOO0O00O0000O0O0 =OO0O000O0OOOOOO0O ['data']['id']#line:77
                    O000OO0000OOO0OOO =OO0O000O0OOOOOO0O ['data']['score']#line:78
                    print (f'【账号信息】:昵称:{O0OOO0OOO00OO0O00[:6]}丨ID:{OOOO0O00O0000O0O0}丨金币:{str(O000OO0000OOO0OOO)[:5]}')#line:79
                if OO0O000O0OOOOOO0O ['code']==302 :#line:80
                    return False #line:81
            return True #line:82
        except Exception as O00O0O0OOOO000000 :#line:83
            print (O00O0O0OOOO000000 )#line:84
    def playInfo (O000O0OO0000OO000 ):#line:87
        try :#line:88
            OOO0O00O0OOOO000O =requests .request ('post',f'{host}/api/Game/playInfo',headers =O000O0OO0000OO000 .headers ).json ()#line:89
            if 'code'in OOO0O00O0OOOO000O :#line:91
                if OOO0O00O0OOOO000O ['code']==1 :#line:92
                    OO0000O0O0O0O0OO0 =OOO0O00O0OOOO000O ['data']['play_tier']#line:93
                    OOO000O00O00OOO0O =OOO0O00O0OOOO000O ['data']['play_tier_need_money']#line:94
                    OO000000OOO0O0O00 =OOO0O00O0OOOO000O ['data']['user_money']#line:95
                    OO00OO0OO00OO0OO0 =OOO0O00O0OOOO000O ['data']['play_finish_money']#line:96
                    print (f'【参与闯关】:层数:{OO0000O0O0O0O0OO0}丨闯关花费:{OOO000O00O00OOO0O}丨预计获得:{OO00OO0OO00OO0OO0}')#line:97
                    if float (OOO000O00O00OOO0O )<float (OO000000OOO0O0O00 ):#line:98
                        O000O0OO0000OO000 .Game_index ('1')#line:100
                    else :#line:101
                        O000O0OO0000OO000 .Game_index ('2')#line:102
        except Exception as OO0OO00O000OOO0O0 :#line:104
            print (OO0OO00O000OOO0O0 )#line:105
    def setAutoPlay (O00O00O00OOO0O00O ):#line:108
        try :#line:109
            OO0OO00O0O0O00O0O ={'state':'1'}#line:112
            OO0O0O00OO000000O =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O00O00O00OOO0O00O .headers ,data =OO0OO00O0O0O00O0O ).json ()#line:113
            if 'code'in OO0O0O00OO000000O :#line:115
                if OO0O0O00OO000000O ['code']==1 :#line:116
                    print (f'【自动闯关】:{OO0O0O00OO000000O["msg"]}')#line:117
                if OO0O0O00OO000000O ['code']==0 :#line:118
                    print (f'【自动闯关】:{OO0O0O00OO000000O["msg"]}')#line:119
        except Exception as O0O0O000OOOOOOO0O :#line:120
            print (O0O0O000OOOOOOO0O )#line:121
    def Game_index (O0OOOO00OO000000O ,OOOO0OOO000OOO0OO ):#line:124
        OOOO0O00O00O0O0OO =requests .request ('post',f'{host}/api/Game/index',headers =O0OOOO00OO000000O .headers ).json ()#line:125
        if 'code'in OOOO0O00O00O0O0OO :#line:127
            if OOOO0O00O00O0O0OO ['code']==1 :#line:128
                O0O0OOOOOOO00OOO0 =OOOO0O00O00O0O0OO ['data']['is_auto_play']#line:129
                OOOO0O0OOO00000OO =OOOO0O00O00O0O0OO ['data']['is_game_ing']#line:130
                O0OOO00OOO00O0OO0 =OOOO0O00O00O0O0OO ['data']['is_vip']#line:131
                O0O0O000O0OO00O00 =OOOO0O00O00O0O0OO ['data']['npc_hint']#line:132
                if O0OOO00OOO00O0OO0 :#line:133
                    print (f'【游戏状态】:自动闯关:{O0O0OOOOOOO00OOO0}丨VIP:{O0OOO00OOO00O0OO0} ✅')#line:134
                else :#line:135
                    print (f'【游戏状态】:自动闯关:{O0O0OOOOOOO00OOO0}丨VIP:{O0OOO00OOO00O0OO0} ❌')#line:136
                if not O0O0OOOOOOO00OOO0 :#line:137
                    if OOOO0OOO000OOO0OO =='1':#line:138
                        O0OOOO00OO000000O .setAutoPlay ()#line:139
    def LuckyBox (OO00O0000OOOOO00O ):#line:142
        try :#line:143
            OO0OOO0000000OO00 =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OO00O0000OOOOO00O .headers ).json ()#line:144
            if 'code'in OO0OOO0000000OO00 :#line:146
                if OO0OOO0000000OO00 ['code']==1 :#line:147
                    OO0O0OO0O000O0O0O =OO0OOO0000000OO00 ['data']['debris']#line:148
                    OO00O00OOO0OOOO00 =OO0OOO0000000OO00 ['data']['is_draw']#line:149
                    print (f'【幸运宝箱】:碎片:{str(OO0O0OO0O000O0O0O).split(".")[0]}丨当前设置开启宝箱ID:{OO00O0000OOOOO00O.box}')#line:150
                    if not OO00O00OOO0OOOO00 :#line:151
                        O00000OOOOOO0O0O0 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OO00O0000OOOOO00O .headers ).json ()#line:152
                        if 'code'in O00000OOOOOO0O0O0 :#line:154
                            if O00000OOOOOO0O0O0 ['code']==1 :#line:155
                                OOOOO000OOO0O0O0O =O00000OOOOOO0O0O0 ['data']['nub']#line:156
                                print (f'【领取碎片】:获得:{OOOOO000OOO0O0O0O}')#line:157
                    for O00O0O0OOO00OOOOO in OO0OOO0000000OO00 ['data']['box_list']:#line:158
                        O000OO00OOO00O000 =O00O0O0OOO00OOOOO ['id']#line:160
                        O0O00O0OO0OOOO0O0 =O00O0O0OOO00OOOOO ['name']#line:161
                        OOO0O0000O0OO0O00 =O00O0O0OOO00OOOOO ['inventory']#line:162
                        OOO00O0O000O00OO0 =O00O0O0OOO00OOOOO ['need_debris']#line:163
                        if float (O000OO00OOO00O000 )==float (OO00O0000OOOOO00O .box ):#line:164
                            print (f'【幸运宝箱】:名称:{O0O00O0OO0OOOO0O0}丨需要碎片:{OOO00O0O000O00OO0}丨剩余:{OOO0O0000O0OO0O00}')#line:165
                            if float (OO0O0OO0O000O0O0O )>=float (OOO00O0O000O00OO0 ):#line:166
                                O00OOOOOOO0O00O0O ={'id':OO00O0000OOOOO00O .box }#line:167
                                O0OOOOOO000OOOO00 =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =OO00O0000OOOOO00O .headers ,data =O00OOOOOOO0O00O0O ).json ()#line:168
                                if 'code'in O0OOOOOO000OOOO00 :#line:170
                                    if O0OOOOOO000OOOO00 ['code']==1 :#line:171
                                        print (f'【兑换宝箱】:{O0OOOOOO000OOOO00["msg"]}丨获得{O0OOOOOO000OOOO00["data"]["name"]}')#line:172
        except Exception as OOOO00O00OOO000OO :#line:175
            print (OOOO00O00OOO000OO )#line:176
def start ():#line:179
    try :#line:180
        update_the_validation ()#line:181
        OOOO0OO0OOOO00OOO =os_qinglong ()#line:182
        print (f"==========共找到{len(OOOO0OO0OOOO00OOO)}个账号==========")#line:183
        for O00000OO0O0O00000 in OOOO0OO0OOOO00OOO :#line:184
            print (f"------------正在执行第{OOOO0OO0OOOO00OOO.index(O00000OO0O0O00000) + 1}个账号------------")#line:185
            O0O0O0000O00OO000 =Template (O00000OO0O0O00000 )#line:186
            if O0O0O0000O00OO000 .base_info ():#line:188
                O0O0O0000O00OO000 .LuckyBox ()#line:190
                O0O0O0000O00OO000 .playInfo ()#line:192
                time .sleep (random .randint (2 ,3 ))#line:197
            else :#line:198
                print ('token失效')#line:199
    except Exception as O00O00O0O0OOO00OO :#line:200
        print (O00O00O0O0OOO00OO )#line:201
def version_of_the_validation ():#line:203
    return str ((59 -56 )/10 )#line:204
if __name__ =='__main__':#line:207
    start ()#line:208
