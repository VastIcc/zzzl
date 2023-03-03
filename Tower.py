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


##################################下面不要动##################################    
host ='https://qct.qitusky.cn'#line:1
git ='https://gitee.com'#line:2
def os_qinglong ():#line:3
    if application in os .environ :#line:4
        O00OOOOOOO0OO0000 =os .environ [application ].split ('\n')#line:5
        if len (O00OOOOOOO0OO0000 )>0 :#line:6
            return O00OOOOOOO0OO0000 #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        O00000OOOO0O000OO =token .split ('\n')#line:19
        if len (O00000OOOO0O000OO )>0 :#line:20
            return O00000OOOO0O000OO #line:21
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
        O00OO0OO00O000OOO =gitee_validation ()#line:35
        if version_of_the_validation ()<O00OO0OO00O000OOO ['Tower']['edition']:#line:36
            print (f'当前脚本名字: {O00OO0OO00O000OOO["Tower"]["text"]}')#line:37
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OO0OO00O000OOO["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:38
            print (f'更新内容=>> {O00OO0OO00O000OOO["Tower"]["content"]}')#line:39
        else :#line:40
            print (f'当前脚本名字: {O00OO0OO00O000OOO["Tower"]["text"]}')#line:41
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OO0OO00O000OOO["Tower"]["edition"]}   ✅')#line:42
            print (f'更新内容=>> {O00OO0OO00O000OOO["Tower"]["content"]}')#line:43
    except Exception as O00O00OOO0O00OOO0 :#line:44
        print (O00O00OOO0O00OOO0 )#line:45
class Template :#line:48
    def __init__ (OO0OOOO00O00OO000 ,OOO000OOOO0000O00 ):#line:50
        try :#line:51
            OO0OOOO00O00OO000 .token =OOO000OOOO0000O00 .split ('&')[0 ]#line:52
            OO0OOOO00O00OO000 .box =OOO000OOOO0000O00 .split ('&')[1 ]#line:53
            OO0OOOO00O00OO000 .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OO0OOOO00O00OO000 .token ,'server':'true','phone-type':'android',}#line:65
        except Exception as O0OO000000OO000O0 :#line:66
            print ('变量格式错误')#line:67
    def base_info (OOOOOO0OO0OOOOO00 ):#line:70
        try :#line:71
            OOO0OO00000O00OOO =requests .request ('post',f'{host}/api/User/info',headers =OOOOOO0OO0OOOOO00 .headers ).json ()#line:72
            if 'code'in OOO0OO00000O00OOO :#line:74
                if OOO0OO00000O00OOO ['code']==1 :#line:75
                    O000OO0O0OO0OOOOO =OOO0OO00000O00OOO ['data']['nickname']#line:76
                    OOO0OO0OO0O00O000 =OOO0OO00000O00OOO ['data']['id']#line:77
                    O0O0OO0O000OO000O =OOO0OO00000O00OOO ['data']['score']#line:78
                    print (f'【账号信息】:昵称:{O000OO0O0OO0OOOOO[:6]}丨ID:{OOO0OO0OO0O00O000}丨金币:{str(O0O0OO0O000OO000O)[:5]}')#line:79
                if OOO0OO00000O00OOO ['code']==302 :#line:80
                    return False #line:81
            return True #line:82
        except Exception as OO0OO0OOO0OOO00O0 :#line:83
            print (OO0OO0OOO0OOO00O0 )#line:84
    def playInfo (O000OOO0O0O00O00O ):#line:87
        try :#line:88
            O0O0OO000OOO0OOO0 =requests .request ('post',f'{host}/api/Game/playInfo',headers =O000OOO0O0O00O00O .headers ).json ()#line:89
            if 'code'in O0O0OO000OOO0OOO0 :#line:91
                if O0O0OO000OOO0OOO0 ['code']==1 :#line:92
                    O00O000O00O000OO0 =O0O0OO000OOO0OOO0 ['data']['play_tier']#line:93
                    O0OO00OO0000OO000 =O0O0OO000OOO0OOO0 ['data']['play_tier_need_money']#line:94
                    OO0O0OO0O0O0OO000 =O0O0OO000OOO0OOO0 ['data']['user_money']#line:95
                    O0O00OO0O00O000OO =O0O0OO000OOO0OOO0 ['data']['play_finish_money']#line:96
                    print (f'【参与闯关】:层数:{O00O000O00O000OO0}丨闯关花费:{O0OO00OO0000OO000}丨预计获得:{O0O00OO0O00O000OO}')#line:97
                    if float (O0OO00OO0000OO000 )<float (OO0O0OO0O0O0OO000 ):#line:98
                        O000OOO0O0O00O00O .Game_index ('1')#line:100
                    else :#line:101
                        O000OOO0O0O00O00O .Game_index ('2')#line:102
        except Exception as OO000OO0OOOO00OO0 :#line:104
            print (OO000OO0OOOO00OO0 )#line:105
    def setAutoPlay (O000000000OO0OOO0 ):#line:108
        try :#line:109
            O0O0O00OO0000OOO0 ={'state':'1'}#line:112
            OOO00O0OOOO000O0O =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O000000000OO0OOO0 .headers ,data =O0O0O00OO0000OOO0 ).json ()#line:113
            if 'code'in OOO00O0OOOO000O0O :#line:115
                if OOO00O0OOOO000O0O ['code']==1 :#line:116
                    print (f'【自动闯关】:{OOO00O0OOOO000O0O["msg"]}')#line:117
                if OOO00O0OOOO000O0O ['code']==0 :#line:118
                    print (f'【自动闯关】:{OOO00O0OOOO000O0O["msg"]}')#line:119
        except Exception as O000OO0OO0OOO0OOO :#line:120
            print (O000OO0OO0OOO0OOO )#line:121
    def Game_index (OOOOO000OO0O0OO0O ,O00OO00OOO00OO0OO ):#line:124
        try :#line:125
            OO00OO0OO000O0O0O =requests .request ('post',f'{host}/api/Game/index',headers =OOOOO000OO0O0OO0O .headers ).json ()#line:126
            if 'code'in OO00OO0OO000O0O0O :#line:128
                if OO00OO0OO000O0O0O ['code']==1 :#line:129
                    if OO00OO0OO000O0O0O ['data']['is_auto_play']:#line:130
                        O0000OO0OO00OOOOO ='✅'#line:131
                    else :#line:132
                        O0000OO0OO00OOOOO ='❌'#line:133
                    if OO00OO0OO000O0O0O ['data']['is_game_ing']:#line:135
                        OOOO0O0OOOO00OOOO ='✅'#line:136
                    else :#line:137
                        OOOO0O0OOOO00OOOO ='❌'#line:138
                    if OO00OO0OO000O0O0O ['data']['is_vip']:#line:139
                        OO0OO0OOOOO0O00OO ='✅'#line:140
                    else :#line:141
                        OO0OO0OOOOO0O00OO ='❌'#line:142
                    if '正在闯关'in OO00OO0OO000O0O0O ['data']['npc_hint']:#line:143
                        O00000O000OOO00OO =OO00OO0OO000O0O0O ['data']['npc_hint'][:8 ]#line:144
                    else :#line:145
                        O00000O000OOO00OO =OO00OO0OO000O0O0O ['data']['npc_hint'][:5 ]#line:146
                    print (f'【游戏状态】:自动:{O0000OO0OO00OOOOO}丨闯关:{OOOO0O0OOOO00OOOO}丨VIP:{OO0OO0OOOOO0O00OO}丨{O00000O000OOO00OO}')#line:147
                    if not OO00OO0OO000O0O0O ['data']['is_auto_play']:#line:148
                        if O00OO00OOO00OO0OO =='1':#line:149
                            OOOOO000OO0O0OO0O .setAutoPlay ()#line:150
        except Exception as OOO00OOOO0O0O0O00 :#line:151
            print (OOO00OOOO0O0O0O00 )#line:152
    def LuckyBox (OOO0000OO0O0000O0 ):#line:156
        try :#line:157
            OO0O0O0OOOO0OO00O =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OOO0000OO0O0000O0 .headers ).json ()#line:158
            if 'code'in OO0O0O0OOOO0OO00O :#line:160
                if OO0O0O0OOOO0OO00O ['code']==1 :#line:161
                    O0OOOO000O0O00OO0 =OO0O0O0OOOO0OO00O ['data']['debris']#line:162
                    OO0O0O0OO00O000O0 =OO0O0O0OOOO0OO00O ['data']['is_draw']#line:163
                    print (f'【幸运宝箱】:碎片:{str(O0OOOO000O0O00OO0).split(".")[0]}丨当前设置开启宝箱ID:{OOO0000OO0O0000O0.box}')#line:164
                    if not OO0O0O0OO00O000O0 :#line:165
                        O00O0OO0O0OO00OO0 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OOO0000OO0O0000O0 .headers ).json ()#line:166
                        if 'code'in O00O0OO0O0OO00OO0 :#line:168
                            if O00O0OO0O0OO00OO0 ['code']==1 :#line:169
                                O0OOOOOO00O000OO0 =O00O0OO0O0OO00OO0 ['data']['nub']#line:170
                                print (f'【领取碎片】:获得:{O0OOOOOO00O000OO0}')#line:171
                    for O0OO00OOO0O00O0OO in OO0O0O0OOOO0OO00O ['data']['box_list']:#line:172
                        O0O00OO000000000O =O0OO00OOO0O00O0OO ['id']#line:174
                        OOO000000O0000OOO =O0OO00OOO0O00O0OO ['name']#line:175
                        O00O000O0OOO00O0O =O0OO00OOO0O00O0OO ['inventory']#line:176
                        OOOOO0OO0OOO00OOO =O0OO00OOO0O00O0OO ['need_debris']#line:177
                        if float (O0O00OO000000000O )==float (OOO0000OO0O0000O0 .box ):#line:178
                            print (f'【幸运宝箱】:名称:{OOO000000O0000OOO}丨需要碎片:{OOOOO0OO0OOO00OOO}丨剩余:{O00O000O0OOO00O0O}')#line:179
                            if float (O0OOOO000O0O00OO0 )>=float (OOOOO0OO0OOO00OOO ):#line:180
                                O00O000O0OO0OOO0O ={'id':OOO0000OO0O0000O0 .box }#line:181
                                OO0O0000OOOO0O0O0 =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =OOO0000OO0O0000O0 .headers ,data =O00O000O0OO0OOO0O ).json ()#line:182
                                if 'code'in OO0O0000OOOO0O0O0 :#line:184
                                    if OO0O0000OOOO0O0O0 ['code']==1 :#line:185
                                        print (f'【兑换宝箱】:{OO0O0000OOOO0O0O0["msg"]}丨获得{OO0O0000OOOO0O0O0["data"]["name"]}')#line:186
        except Exception as OOO0OO00OO0O00OO0 :#line:187
            print (OOO0OO00OO0O00OO0 )#line:188
def start ():#line:191
    try :#line:192
        update_the_validation ()#line:193
        O00O0OO0O000000OO =os_qinglong ()#line:194
        print (f"==========共找到{len(O00O0OO0O000000OO)}个账号==========")#line:195
        for O0OOO000O0O000O0O in O00O0OO0O000000OO :#line:196
            print (f"------------正在执行第{O00O0OO0O000000OO.index(O0OOO000O0O000O0O) + 1}个账号------------")#line:197
            O00OOO000O0O0O0OO =Template (O0OOO000O0O000O0O )#line:198
            if O00OOO000O0O0O0OO .base_info ():#line:200
                O00OOO000O0O0O0OO .LuckyBox ()#line:202
                O00OOO000O0O0O0OO .playInfo ()#line:204
                time .sleep (random .randint (1 ,3 ))#line:207
            else :#line:208
                print ('token失效')#line:209
    except Exception as OO00OO0O0OOO0OO0O :#line:210
        print (OO00OO0O0OOO0OO0O )#line:211
def version_of_the_validation ():#line:213
    return str ((59 -56 )/10 )#line:214
if __name__ =='__main__':#line:217
    start ()#line:218
