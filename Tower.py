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
@ 版本 0.4
"""
##################################配置区##################################    surplus_play_nub
score = False   # 赠送记录
##################################配置区##################################

application = 'qc_token'  # 变量名
token = ''  #
##################################下面不要动##################################
host ='https://qct.qitusky.cn'#line:1
git ='https://gitee.com'#line:2
def os_qinglong ():#line:3
    if application in os .environ :#line:4
        O0OOOOO0000O0OOOO =os .environ [application ].split ('\n')#line:5
        if len (O0OOOOO0000O0OOOO )>0 :#line:6
            return O0OOOOO0000O0OOOO #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        O0OO0O000OO0O00OO =token .split ('\n')#line:19
        if len (O0OO0O000OO0O00OO )>0 :#line:20
            return O0OO0O000OO0O00OO #line:21
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
        O0OO00OOOO00OOO00 =gitee_validation ()#line:35
        if version_of_the_validation ()<O0OO00OOOO00OOO00 ['Tower']['edition']:#line:36
            print (f'当前脚本名字: {O0OO00OOOO00OOO00["Tower"]["text"]}')#line:37
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00OOOO00OOO00["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:38
            print (f'更新内容=>> {O0OO00OOOO00OOO00["Tower"]["content"]}')#line:39
        else :#line:40
            print (f'当前脚本名字: {O0OO00OOOO00OOO00["Tower"]["text"]}')#line:41
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00OOOO00OOO00["Tower"]["edition"]}   ✅')#line:42
            print (f'更新内容=>> {O0OO00OOOO00OOO00["Tower"]["content"]}')#line:43
    except Exception as OOO0000O0OO0O0O0O :#line:44
        print (OOO0000O0OO0O0O0O )#line:45
class Template :#line:48
    def __init__ (OOO0O0O000O0O000O ,O00O0O00O0OO0O0O0 ):#line:50
        try :#line:51
            OOO0O0O000O0O000O .token =O00O0O00O0OO0O0O0 .split ('&')[0 ]#line:52
            OOO0O0O000O0O000O .box =O00O0O00O0OO0O0O0 .split ('&')[1 ]#line:53
            OOO0O0O000O0O000O .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OOO0O0O000O0O000O .token ,'server':'true','phone-type':'android',}#line:65
        except Exception as O000OOOOOOOO0OO0O :#line:66
            print ('变量格式错误')#line:67
    def base_info (OOOOO0O0O0O0O00OO ):#line:70
        try :#line:71
            O0O0O00OO0000OO0O =requests .request ('post',f'{host}/api/User/info',headers =OOOOO0O0O0O0O00OO .headers ).json ()#line:72
            if 'code'in O0O0O00OO0000OO0O :#line:74
                if O0O0O00OO0000OO0O ['code']==1 :#line:75
                    O0OOOO0O00O00OO0O =O0O0O00OO0000OO0O ['data']['nickname']#line:76
                    OOOO0O00O0O0000OO =O0O0O00OO0000OO0O ['data']['id']#line:77
                    OO0O0O0OO000O000O =O0O0O00OO0000OO0O ['data']['score']#line:78
                    print (f'【账号信息】:昵称:{O0OOOO0O00O00OO0O[:6]}丨ID:{OOOO0O00O0O0000OO}丨金币:{str(OO0O0O0OO000O000O)[:5]}')#line:79
                if O0O0O00OO0000OO0O ['code']==302 :#line:80
                    return False #line:81
            return True #line:82
        except Exception as O000O00OO00O0O0OO :#line:83
            print (O000O00OO00O0O0OO )#line:84
    def playInfo (OO0O00OOO0O0O0000 ):#line:87
        try :#line:88
            O000OO0O0OOO0OOOO =requests .request ('post',f'{host}/api/Game/playInfo',headers =OO0O00OOO0O0O0000 .headers ).json ()#line:89
            if 'code'in O000OO0O0OOO0OOOO :#line:91
                if O000OO0O0OOO0OOOO ['code']==1 :#line:92
                    OO000O0OO0O00OO00 =O000OO0O0OOO0OOOO ['data']['play_tier']#line:93
                    OO0OO0OOOO00O00OO =O000OO0O0OOO0OOOO ['data']['play_tier_need_money']#line:94
                    O0O00OO00OO0O0OO0 =O000OO0O0OOO0OOOO ['data']['user_money']#line:95
                    OO0OO0OO000OOOO0O =O000OO0O0OOO0OOOO ['data']['play_finish_money']#line:96
                    O0OOOOO0OOOOO000O =O000OO0O0OOO0OOOO ['data']['surplus_play_nub']#line:97
                    print (f'【参与闯关】:层数:{OO000O0OO0O00OO00}丨剩余:{O0OOOOO0OOOOO000O}丨花费:{OO0OO0OOOO00O00OO}丨预计:{OO0OO0OO000OOOO0O}')#line:98
                    if float (OO0OO0OOOO00O00OO )<float (O0O00OO00OO0O0OO0 ):#line:99
                        if O0OOOOO0OOOOO000O >0 :#line:100
                            OO0O00OOO0O0O0000 .Game_index ('1')#line:101
                        else :#line:102
                            OO0O00OOO0O0O0000 .Game_index ('2')#line:103
                    else :#line:104
                        OO0O00OOO0O0O0000 .Game_index ('2')#line:105
        except Exception as OO00000OO0OOOO00O :#line:107
            print (OO00000OO0OOOO00O )#line:108
    def setAutoPlay (O000O00O0OO00O000 ):#line:111
        try :#line:112
            O0O00OOO00OO0O0O0 ={'state':'1'}#line:115
            O00O00OOOO000OOO0 =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O000O00O0OO00O000 .headers ,data =O0O00OOO00OO0O0O0 ).json ()#line:116
            if 'code'in O00O00OOOO000OOO0 :#line:118
                if O00O00OOOO000OOO0 ['code']==1 :#line:119
                    print (f'【自动闯关】:{O00O00OOOO000OOO0["msg"]}')#line:120
                if O00O00OOOO000OOO0 ['code']==0 :#line:121
                    print (f'【自动闯关】:{O00O00OOOO000OOO0["msg"]}')#line:122
        except Exception as OOOO0OO0OOO00O0O0 :#line:123
            print (OOOO0OO0OOO00O0O0 )#line:124
    def Game_index (O0OO000O0OOOO00O0 ,O0OO00OOOOO0OO00O ):#line:127
        try :#line:128
            O00000OOOO0O0O0O0 =requests .request ('post',f'{host}/api/Game/index',headers =O0OO000O0OOOO00O0 .headers ).json ()#line:129
            if 'code'in O00000OOOO0O0O0O0 :#line:131
                if O00000OOOO0O0O0O0 ['code']==1 :#line:132
                    if O00000OOOO0O0O0O0 ['data']['is_auto_play']:#line:133
                        O0O00O0OO0O0OOO0O ='✅'#line:134
                    else :#line:135
                        O0O00O0OO0O0OOO0O ='❌'#line:136
                    if O00000OOOO0O0O0O0 ['data']['is_game_ing']:#line:138
                        OO0O0OO00O0O00OOO ='✅'#line:139
                    else :#line:140
                        OO0O0OO00O0O00OOO ='❌'#line:141
                    if O00000OOOO0O0O0O0 ['data']['is_vip']:#line:142
                        OOO000O0O00000OOO ='✅'#line:143
                    else :#line:144
                        OOO000O0O00000OOO ='❌'#line:145
                    if '正在闯关'in O00000OOOO0O0O0O0 ['data']['npc_hint']:#line:146
                        OO00OOOO00OO0OO0O =O00000OOOO0O0O0O0 ['data']['npc_hint'][:8 ]#line:147
                    else :#line:148
                        OO00OOOO00OO0OO0O =O00000OOOO0O0O0O0 ['data']['npc_hint'][:5 ]#line:149
                    print (f'【游戏状态】:自动:{O0O00O0OO0O0OOO0O}丨闯关:{OO0O0OO00O0O00OOO}丨VIP:{OOO000O0O00000OOO}丨{OO00OOOO00OO0OO0O}')#line:150
                    if not O00000OOOO0O0O0O0 ['data']['is_auto_play']:#line:151
                        if O0OO00OOOOO0OO00O =='1':#line:152
                            O0OO000O0OOOO00O0 .setAutoPlay ()#line:153
        except Exception as OOOOO0O00000O00O0 :#line:154
            print (OOOOO0O00000O00O0 )#line:155
    def LuckyBox (OO0OOOO000O0O0O00 ):#line:159
        try :#line:160
            OOOO000O000OO0O00 =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OO0OOOO000O0O0O00 .headers ).json ()#line:161
            if 'code'in OOOO000O000OO0O00 :#line:163
                if OOOO000O000OO0O00 ['code']==1 :#line:164
                    O000O00OOO0OOOOOO =OOOO000O000OO0O00 ['data']['debris']#line:165
                    OO00O0OO0000OO0OO =OOOO000O000OO0O00 ['data']['is_draw']#line:166
                    print (f'【幸运宝箱】:碎片:{str(O000O00OOO0OOOOOO).split(".")[0]}丨当前设置开启宝箱ID:{OO0OOOO000O0O0O00.box}')#line:167
                    if not OO00O0OO0000OO0OO :#line:168
                        O000OO0O0OO00OOO0 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OO0OOOO000O0O0O00 .headers ).json ()#line:169
                        if 'code'in O000OO0O0OO00OOO0 :#line:171
                            if O000OO0O0OO00OOO0 ['code']==1 :#line:172
                                O0OOOOO0OOO0O000O =O000OO0O0OO00OOO0 ['data']['nub']#line:173
                                print (f'【领取碎片】:获得:{O0OOOOO0OOO0O000O}')#line:174
                    for OOO0000O0OO00OO0O in OOOO000O000OO0O00 ['data']['box_list']:#line:175
                        O0OOO00O000O00000 =OOO0000O0OO00OO0O ['id']#line:177
                        OO000OOOO00000O00 =OOO0000O0OO00OO0O ['name']#line:178
                        O0OO0O00O0O000O00 =OOO0000O0OO00OO0O ['inventory']#line:179
                        O00O0O0OO0O0O00OO =OOO0000O0OO00OO0O ['need_debris']#line:180
                        if float (O0OOO00O000O00000 )==float (OO0OOOO000O0O0O00 .box ):#line:181
                            print (f'【幸运宝箱】:名称:{OO000OOOO00000O00}丨需要碎片:{O00O0O0OO0O0O00OO}丨剩余:{O0OO0O00O0O000O00}')#line:182
                            if float (O000O00OOO0OOOOOO )>=float (O00O0O0OO0O0O00OO ):#line:183
                                O000O0O0OO0000O00 ={'id':OO0OOOO000O0O0O00 .box }#line:184
                                OOO0O0O0O00O00000 =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =OO0OOOO000O0O0O00 .headers ,data =O000O0O0OO0000O00 ).json ()#line:185
                                if 'code'in OOO0O0O0O00O00000 :#line:187
                                    if OOO0O0O0O00O00000 ['code']==1 :#line:188
                                        print (f'【兑换宝箱】:{OOO0O0O0O00O00000["msg"]}丨获得{OOO0O0O0O00O00000["data"]["name"]}')#line:189
        except Exception as OOO0O0OOOO0OOOO00 :#line:190
            print (OOO0O0OOOO0OOOO00 )#line:191
    def score_record (O0000O0000O0O00OO ):#line:194
        O00O00O00OO0OO00O ={'page':'1','limit':'15','type':'2'}#line:195
        O00O0OO000OOOO000 =requests .request ('post',f'{host}/api/Score/record',headers =O0000O0000O0O00OO .headers ,data =O00O00O00OO0OO00O ).json ()#line:196
        if 'code'in O00O0OO000OOOO000 :#line:198
            if O00O0OO000OOOO000 ['code']==1 :#line:199
                OOOOOO000OO00O0O0 =O00O0OO000OOOO000 ['data']['record_list']#line:200
                if OOOOOO000OO00O0O0 :#line:201
                    for OO00O00O0OO00O0O0 in OOOOOO000OO00O0O0 :#line:202
                        O000O00O0000O0OOO =OO00O00O0OO00O0O0 ['user_id']#line:203
                        O0O0O000O0OO0OO0O =OO00O00O0OO00O0O0 ['money']#line:204
                        O0O0O000O00O0OOOO =OO00O00O0OO00O0O0 ['create_time']#line:205
                        O00O0OOO0O00O0OO0 =OO00O00O0OO00O0O0 ['nickname']#line:206
                        print (f'【赠送记录】:昵称:{O00O0OOO0O00O0OO0}丨ID:{O000O00O0000O0OOO}丨金额:{O0O0O000O0OO0OO0O}丨时间:{O0O0O000O00O0OOOO[5:16]}')#line:207
def start ():#line:208
    try :#line:209
        update_the_validation ()#line:210
        OO00OO000O0000O00 =os_qinglong ()#line:211
        print (f"==========共找到{len(OO00OO000O0000O00)}个账号==========")#line:212
        for O0O0O0O0OOO0OO00O in OO00OO000O0000O00 :#line:213
            print (f"------------正在执行第{OO00OO000O0000O00.index(O0O0O0O0OOO0OO00O) + 1}个账号------------")#line:214
            OO0OOOOOO0O0O000O =Template (O0O0O0O0OOO0OO00O )#line:215
            if OO0OOOOOO0O0O000O .base_info ():#line:217
                OO0OOOOOO0O0O000O .LuckyBox ()#line:219
                OO0OOOOOO0O0O000O .playInfo ()#line:221
                if score :#line:222
                    OO0OOOOOO0O0O000O .score_record ()#line:224
                time .sleep (random .randint (5 ,8 ))#line:226
            else :#line:227
                print ('token失效')#line:228
    except Exception as O000OOOOOO00OOOOO :#line:229
        print (O000OOOOOO00OOOOO )#line:230
def version_of_the_validation ():#line:232
    return str ((60 -56 )/10 )#line:233
if __name__ =='__main__':#line:236
    start ()#line:237

