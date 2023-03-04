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
        O00O00O0O0OO00000 =os .environ [application ].split ('\n')#line:5
        if len (O00O00O0O0OO00000 )>0 :#line:6
            return O00O00O0O0OO00000 #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        O00OO0000000OO0OO =token .split ('\n')#line:19
        if len (O00OO0000000OO0OO )>0 :#line:20
            return O00OO0000000OO0OO #line:21
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
        OOO0O0O0O0O00OO00 =gitee_validation ()#line:35
        if version_of_the_validation ()<OOO0O0O0O0O00OO00 ['Tower']['edition']:#line:36
            print (f'当前脚本名字: {OOO0O0O0O0O00OO00["Tower"]["text"]}')#line:37
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0O0O0O0O00OO00["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:38
            print (f'更新内容=>> {OOO0O0O0O0O00OO00["Tower"]["content"]}')#line:39
        else :#line:40
            print (f'当前脚本名字: {OOO0O0O0O0O00OO00["Tower"]["text"]}')#line:41
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0O0O0O0O00OO00["Tower"]["edition"]}   ✅')#line:42
            print (f'更新内容=>> {OOO0O0O0O0O00OO00["Tower"]["content"]}')#line:43
    except Exception as O00O000O0OOOOOOO0 :#line:44
        print (O00O000O0OOOOOOO0 )#line:45
class Template :#line:48
    def __init__ (OO0O00OOOOOOO0000 ,O00O00OO00O0OO000 ):#line:50
        try :#line:51
            OO0O00OOOOOOO0000 .token =O00O00OO00O0OO000 .split ('&')[0 ]#line:52
            OO0O00OOOOOOO0000 .box =O00O00OO00O0OO000 .split ('&')[1 ]#line:53
            OO0O00OOOOOOO0000 .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OO0O00OOOOOOO0000 .token ,'server':'true','phone-type':'android',}#line:65
        except Exception as OOO0O00OO00000O00 :#line:66
            print ('变量格式错误')#line:67
    def base_info (O0O0O0OOO0OOOOO0O ):#line:70
        try :#line:71
            OOO0O0OO00OOOO0O0 =requests .request ('post',f'{host}/api/User/info',headers =O0O0O0OOO0OOOOO0O .headers ).json ()#line:72
            if 'code'in OOO0O0OO00OOOO0O0 :#line:74
                if OOO0O0OO00OOOO0O0 ['code']==1 :#line:75
                    O0000OO0000OOOO0O =OOO0O0OO00OOOO0O0 ['data']['nickname']#line:76
                    OO0OO00OOO00000OO =OOO0O0OO00OOOO0O0 ['data']['id']#line:77
                    O0O0O0000OO00000O =OOO0O0OO00OOOO0O0 ['data']['score']#line:78
                    print (f'【账号信息】:昵称:{O0000OO0000OOOO0O[:6]}丨ID:{OO0OO00OOO00000OO}丨金币:{str(O0O0O0000OO00000O)[:5]}')#line:79
                if OOO0O0OO00OOOO0O0 ['code']==302 :#line:80
                    return False #line:81
            return True #line:82
        except Exception as OOOOO0OOOOO0OOOOO :#line:83
            print (OOOOO0OOOOO0OOOOO )#line:84
    def playInfo (OOO0O000OO0OO0O00 ):#line:87
        try :#line:88
            O0O00000O00OOO0OO =requests .request ('post',f'{host}/api/Game/playInfo',headers =OOO0O000OO0OO0O00 .headers ).json ()#line:89
            if 'code'in O0O00000O00OOO0OO :#line:91
                if O0O00000O00OOO0OO ['code']==1 :#line:92
                    OOO000O00OO00OOOO =O0O00000O00OOO0OO ['data']['play_tier']#line:93
                    OO0OO0O0O0OOO000O =O0O00000O00OOO0OO ['data']['play_tier_need_money']#line:94
                    O00O0O000O00OO00O =O0O00000O00OOO0OO ['data']['user_money']#line:95
                    O00OO00O0O00OO00O =O0O00000O00OOO0OO ['data']['play_finish_money']#line:96
                    OOOO0OOO00O0OO00O =O0O00000O00OOO0OO ['data']['surplus_play_nub']#line:97
                    print (f'【参与闯关】:层数:{OOO000O00OO00OOOO}丨剩余:{OOOO0OOO00O0OO00O}丨花费:{OO0OO0O0O0OOO000O}丨预计:{O00OO00O0O00OO00O}')#line:98
                    if float (OO0OO0O0O0OOO000O )<float (O00O0O000O00OO00O ):#line:99
                        if OOOO0OOO00O0OO00O >0 :#line:100
                            OOO0O000OO0OO0O00 .Game_index ('1')#line:101
                        else :#line:102
                            OOO0O000OO0OO0O00 .Game_index ('2')#line:103
                    else :#line:104
                        OOO0O000OO0OO0O00 .Game_index ('2')#line:105
        except Exception as O0O0O000000OOO0O0 :#line:107
            print (O0O0O000000OOO0O0 )#line:108
    def setAutoPlay (OOO00O0O00OO0O00O ):#line:111
        try :#line:112
            O0O00O00OO00O00O0 ={'state':'1'}#line:115
            O0OOOO0000OO0O000 =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =OOO00O0O00OO0O00O .headers ,data =O0O00O00OO00O00O0 ).json ()#line:116
            if 'code'in O0OOOO0000OO0O000 :#line:118
                if O0OOOO0000OO0O000 ['code']==1 :#line:119
                    print (f'【自动闯关】:{O0OOOO0000OO0O000["msg"]}')#line:120
                if O0OOOO0000OO0O000 ['code']==0 :#line:121
                    print (f'【自动闯关】:{O0OOOO0000OO0O000["msg"]}')#line:122
        except Exception as OOOOO00O0000OOO00 :#line:123
            print (OOOOO00O0000OOO00 )#line:124
    def Game_index (O0O00O0OO0OOOOOOO ,O00OO00OO0OOOO0OO ):#line:127
        try :#line:128
            OOOO0O0O0O0OOO0OO =requests .request ('post',f'{host}/api/Game/index',headers =O0O00O0OO0OOOOOOO .headers ).json ()#line:129
            if 'code'in OOOO0O0O0O0OOO0OO :#line:131
                if OOOO0O0O0O0OOO0OO ['code']==1 :#line:132
                    if OOOO0O0O0O0OOO0OO ['data']['is_auto_play']:#line:133
                        OOO00OOOO000O000O ='✅'#line:134
                    else :#line:135
                        OOO00OOOO000O000O ='❌'#line:136
                    if OOOO0O0O0O0OOO0OO ['data']['is_game_ing']:#line:138
                        O00000OO0OO0O0000 ='✅'#line:139
                    else :#line:140
                        O00000OO0OO0O0000 ='❌'#line:141
                    if OOOO0O0O0O0OOO0OO ['data']['is_vip']:#line:142
                        O0OOOOO0O000O0OOO ='✅'#line:143
                    else :#line:144
                        O0OOOOO0O000O0OOO ='❌'#line:145
                    if '正在闯关'in OOOO0O0O0O0OOO0OO ['data']['npc_hint']:#line:146
                        OOO0O000OOO00OO0O =OOOO0O0O0O0OOO0OO ['data']['npc_hint'][:8 ]#line:147
                    else :#line:148
                        OOO0O000OOO00OO0O =OOOO0O0O0O0OOO0OO ['data']['npc_hint'][:5 ]#line:149
                    print (f'【游戏状态】:自动:{OOO00OOOO000O000O}丨闯关:{O00000OO0OO0O0000}丨VIP:{O0OOOOO0O000O0OOO}丨{OOO0O000OOO00OO0O}')#line:150
                    if not OOOO0O0O0O0OOO0OO ['data']['is_auto_play']:#line:151
                        if O00OO00OO0OOOO0OO =='1':#line:152
                            O0O00O0OO0OOOOOOO .setAutoPlay ()#line:153
        except Exception as OO000O0O00OO00OOO :#line:154
            print (OO000O0O00OO00OOO )#line:155
    def LuckyBox (O0O0O00O00OO00OOO ):#line:159
        try :#line:160
            O00O0OO0O00O00OO0 =requests .request ('post',f'{host}/api/LuckyBox/index',headers =O0O0O00O00OO00OOO .headers ).json ()#line:161
            if 'code'in O00O0OO0O00O00OO0 :#line:163
                if O00O0OO0O00O00OO0 ['code']==1 :#line:164
                    O0OO00O00OO0O00OO =O00O0OO0O00O00OO0 ['data']['debris']#line:165
                    O0OOO000O0O0O0000 =O00O0OO0O00O00OO0 ['data']['is_draw']#line:166
                    print (f'【幸运宝箱】:碎片:{str(O0OO00O00OO0O00OO).split(".")[0]}丨当前设置开启宝箱ID:{O0O0O00O00OO00OOO.box}')#line:167
                    if not O0OOO000O0O0O0000 :#line:168
                        OOO0O00OOOOO0OOO0 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =O0O0O00O00OO00OOO .headers ).json ()#line:169
                        if 'code'in OOO0O00OOOOO0OOO0 :#line:171
                            if OOO0O00OOOOO0OOO0 ['code']==1 :#line:172
                                O0O0000O00O000O0O =OOO0O00OOOOO0OOO0 ['data']['nub']#line:173
                                print (f'【领取碎片】:获得:{O0O0000O00O000O0O}')#line:174
                    for OO0O0O0O0OO0000OO in O00O0OO0O00O00OO0 ['data']['box_list']:#line:175
                        OO000O0OO0OOO00O0 =OO0O0O0O0OO0000OO ['id']#line:177
                        O00O0O00OO0OOO0OO =OO0O0O0O0OO0000OO ['name']#line:178
                        OOOO00O0O0OOO0OO0 =OO0O0O0O0OO0000OO ['inventory']#line:179
                        O0000OOO0OO0OOO0O =OO0O0O0O0OO0000OO ['need_debris']#line:180
                        if float (OO000O0OO0OOO00O0 )==float (O0O0O00O00OO00OOO .box ):#line:181
                            print (f'【幸运宝箱】:名称:{O00O0O00OO0OOO0OO}丨需要碎片:{O0000OOO0OO0OOO0O}丨剩余:{OOOO00O0O0OOO0OO0}')#line:182
                            if float (O0OO00O00OO0O00OO )>=float (O0000OOO0OO0OOO0O ):#line:183
                                OOO0OO000OO0O0O00 ={'id':O0O0O00O00OO00OOO .box }#line:184
                                O000O000000O00OO0 =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =O0O0O00O00OO00OOO .headers ,data =OOO0OO000OO0O0O00 ).json ()#line:185
                                if 'code'in O000O000000O00OO0 :#line:187
                                    if O000O000000O00OO0 ['code']==1 :#line:188
                                        print (f'【兑换宝箱】:{O000O000000O00OO0["msg"]}丨获得{O000O000000O00OO0["data"]["name"]}')#line:189
        except Exception as OOO0OOOO00O000OO0 :#line:190
            print (OOO0OOOO00O000OO0 )#line:191
    def score_record (OO00O00O0O00OO00O ):#line:194
        OO0O0OO000O000O0O ={'page':'1','limit':'15','type':'2'}#line:195
        OOO0OO0O0000OO0OO =requests .request ('post',f'{host}/api/Score/record',headers =OO00O00O0O00OO00O .headers ,data =OO0O0OO000O000O0O ).json ()#line:196
        if 'code'in OOO0OO0O0000OO0OO :#line:198
            if OOO0OO0O0000OO0OO ['code']==1 :#line:199
                OOOOOOOOO00OO0OOO =OOO0OO0O0000OO0OO ['data']['record_list']#line:200
                if OOOOOOOOO00OO0OOO :#line:201
                    for O0O0O0O0O00O0O0OO in OOOOOOOOO00OO0OOO :#line:202
                        O00OOO0OO00OOO0OO =O0O0O0O0O00O0O0OO ['user_id']#line:203
                        O0OO0OO0O0OO0000O =O0O0O0O0O00O0O0OO ['money']#line:204
                        OO0OOOO0O0OOOO000 =O0O0O0O0O00O0O0OO ['create_time']#line:205
                        O000O00000O0OO000 =O0O0O0O0O00O0O0OO ['nickname']#line:206
                        print (f'【赠送记录】:昵称:{O000O00000O0OO000}丨ID:{O00OOO0OO00OOO0OO}丨金额:{O0OO0OO0O0OO0000O}丨时间:{OO0OOOO0O0OOOO000[5:16]}')#line:207
def start ():#line:208
    try :#line:209
        update_the_validation ()#line:210
        O0OOO000OOO0O00O0 =os_qinglong ()#line:211
        print (f"==========共找到{len(O0OOO000OOO0O00O0)}个账号==========")#line:212
        for OOOO0000000O0O000 in O0OOO000OOO0O00O0 :#line:213
            print (f"------------正在执行第{O0OOO000OOO0O00O0.index(OOOO0000000O0O000) + 1}个账号------------")#line:214
            OO0O0O0OO0OOOO00O =Template (OOOO0000000O0O000 )#line:215
            if OO0O0O0OO0OOOO00O .base_info ():#line:217
                OO0O0O0OO0OOOO00O .LuckyBox ()#line:219
                OO0O0O0OO0OOOO00O .playInfo ()#line:221
                if score :#line:222
                    OO0O0O0OO0OOOO00O .score_record ()#line:224
                time .sleep (random .randint (1 ,3 ))#line:226
            else :#line:227
                print ('token失效')#line:228
    except Exception as O0O000O000O000OOO :#line:229
        print (O0O000O000O000OOO )#line:230
def version_of_the_validation ():#line:232
    return str ((60 -56 )/10 )#line:233
if __name__ =='__main__':#line:236
    start ()#line:237
