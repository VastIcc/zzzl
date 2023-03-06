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
@ cron: 0,20 0,12 * * *
@ new Env('千层塔会员版')
@ 项目地址  https://qct.qitusky.cn/invite/?invite_code=1476
@ 抓取  https://qct.qitusky.cn 的ba-user-token值
@ 青龙变量 export qc_token="token&宝箱ID"   1普通宝箱 2白银宝箱 3黄金宝箱 4神秘宝箱 5炫彩宝箱  多号换行
@ 版本 0.5
"""
##################################配置区##################################
score_record = False        # 赠送记录   赠送
giving = False              # 赠送金币 True为赠送
present_id = ''         # 赠送ID
score_big = '5'             # 大于5才赠送
##################################配置区##################################
score = 0
present_nub = 0
application = 'qc_token'  # 变量名
token = ''  #
##################################下面不要动##################################
host ='https://qct.qitusky.cn'#line:1
git ='https://gitee.com'#line:2
def os_qinglong ():#line:3
    if application in os .environ :#line:4
        O000O00OOO000O0O0 =os .environ [application ].split ('\n')#line:5
        if len (O000O00OOO000O0O0 )>0 :#line:6
            return O000O00OOO000O0O0 #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        O0OO0OO0OOO00O0OO =token .split ('\n')#line:19
        if len (O0OO0OO0OOO00O0OO )>0 :#line:20
            return O0OO0OO0OOO00O0OO #line:21
    else :#line:22
        print (f"内置变量为空")#line:23
        print ('脚本结束')#line:24
        sys .exit (0 )#line:25
def gitee_validation ():#line:28
    try :#line:29
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:30
    except :#line:31
        sys .exit (0 )#line:32
def update_the_validation ():#line:36
    try :#line:37
        OOOOO0O00O0OOO00O =gitee_validation ()#line:38
        if version_of_the_validation ()<OOOOO0O00O0OOO00O ['Tower']['edition']:#line:39
            print (f'当前脚本名字: {OOOOO0O00O0OOO00O["Tower"]["text"]}')#line:40
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOO0O00O0OOO00O["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:41
            print (f'更新内容=>> {OOOOO0O00O0OOO00O["Tower"]["content"]}')#line:42
        else :#line:43
            print (f'当前脚本名字: {OOOOO0O00O0OOO00O["Tower"]["text"]}')#line:44
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOO0O00O0OOO00O["Tower"]["edition"]}   ✅')#line:45
            print (f'更新内容=>> {OOOOO0O00O0OOO00O["Tower"]["content"]}')#line:46
    except Exception as O000OO0O000OO0O00 :#line:47
        print (O000OO0O000OO0O00 )#line:48
class Template :#line:51
    def __init__ (OO00OOO00OO0O0OOO ,OO0O000O0O0O000O0 ):#line:53
        try :#line:54
            OO00OOO00OO0O0OOO .token =OO0O000O0O0O000O0 .split ('&')[0 ]#line:55
            OO00OOO00OO0O0OOO .box =OO0O000O0O0O000O0 .split ('&')[1 ]#line:56
            OO00OOO00OO0O0OOO .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OO00OOO00OO0O0OOO .token ,'server':'true','phone-type':'android',}#line:68
        except Exception as OOO0000OO00000000 :#line:69
            print ('变量格式错误')#line:70
    def base_info (O00000000OO0000O0 ):#line:73
        global score #line:74
        try :#line:75
            O000OO000O0O0OOO0 =requests .request ('post',f'{host}/api/User/info',headers =O00000000OO0000O0 .headers ).json ()#line:76
            if 'code'in O000OO000O0O0OOO0 :#line:78
                if O000OO000O0O0OOO0 ['code']==1 :#line:79
                    O0O0OO000OOOO0O00 =O000OO000O0O0OOO0 ['data']['nickname']#line:80
                    O00OOOOOO00OO0O00 =O000OO000O0O0OOO0 ['data']['id']#line:81
                    score =O000OO000O0O0OOO0 ['data']['score']#line:82
                    print (f'【账号信息】:昵称:{O0O0OO000OOOO0O00[:6]}丨ID:{O00OOOOOO00OO0O00}丨金币:{str(score)[:5]}')#line:83
                if O000OO000O0O0OOO0 ['code']==302 :#line:84
                    return False #line:85
            return True #line:86
        except Exception as OOO0000O0O0O0OO0O :#line:87
            print (OOO0000O0O0O0OO0O )#line:88
    def playInfo (OO0000OO00OO0000O ):#line:91
        try :#line:92
            OOOO000OO00000O0O =requests .request ('post',f'{host}/api/Game/playInfo',headers =OO0000OO00OO0000O .headers ).json ()#line:93
            if 'code'in OOOO000OO00000O0O :#line:95
                if OOOO000OO00000O0O ['code']==1 :#line:96
                    O00O00OOO00O0000O =OOOO000OO00000O0O ['data']['play_tier']#line:97
                    O0O0O00O000000O0O =OOOO000OO00000O0O ['data']['play_tier_need_money']#line:98
                    OOO00O0O0O00OO0O0 =OOOO000OO00000O0O ['data']['user_money']#line:99
                    O0O0OO00OOOOOO0O0 =OOOO000OO00000O0O ['data']['play_finish_money']#line:100
                    OO00O00OOO00OO0OO =OOOO000OO00000O0O ['data']['surplus_play_nub']#line:101
                    print (f'【参与闯关】:层数:{O00O00OOO00O0000O}丨剩余:{OO00O00OOO00OO0OO}丨花费:{O0O0O00O000000O0O}丨预计:{O0O0OO00OOOOOO0O0}')#line:102
                    if float (O0O0O00O000000O0O )<float (OOO00O0O0O00OO0O0 ):#line:103
                        if OO00O00OOO00OO0OO >0 :#line:104
                            OO0000OO00OO0000O .Game_index ('1')#line:105
                        else :#line:106
                            OO0000OO00OO0000O .Game_index ('2')#line:107
                    else :#line:108
                        OO0000OO00OO0000O .Game_index ('2')#line:109
        except Exception as O0OOOOO0OOO0000O0 :#line:111
            print (O0OOOOO0OOO0000O0 )#line:112
    def setAutoPlay (OOOO0O0000OOOOOO0 ):#line:115
        try :#line:116
            OO000000O0O0O0OO0 ={'state':'1'}#line:119
            O000OO0OOO00OO00O =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =OOOO0O0000OOOOOO0 .headers ,data =OO000000O0O0O0OO0 ).json ()#line:120
            if 'code'in O000OO0OOO00OO00O :#line:122
                if O000OO0OOO00OO00O ['code']==1 :#line:123
                    print (f'【自动闯关】:{O000OO0OOO00OO00O["msg"]}')#line:124
                if O000OO0OOO00OO00O ['code']==0 :#line:125
                    print (f'【自动闯关】:{O000OO0OOO00OO00O["msg"]}')#line:126
        except Exception as O0O000O0O0OOOOO00 :#line:127
            print (O0O000O0O0OOOOO00 )#line:128
    def Game_index (O0O0OO00OOOO00OO0 ,OOOOOO00000O00O00 ):#line:131
        try :#line:132
            OO0O0O0O0OOOOOOOO =requests .request ('post',f'{host}/api/Game/index',headers =O0O0OO00OOOO00OO0 .headers ).json ()#line:133
            if 'code'in OO0O0O0O0OOOOOOOO :#line:135
                if OO0O0O0O0OOOOOOOO ['code']==1 :#line:136
                    if OO0O0O0O0OOOOOOOO ['data']['is_auto_play']:#line:137
                        O0OOO00O0O00O000O ='✅'#line:138
                    else :#line:139
                        O0OOO00O0O00O000O ='❌'#line:140
                    if OO0O0O0O0OOOOOOOO ['data']['is_game_ing']:#line:142
                        O00O0O00OOOO0OOO0 ='✅'#line:143
                    else :#line:144
                        O00O0O00OOOO0OOO0 ='❌'#line:145
                    if OO0O0O0O0OOOOOOOO ['data']['is_vip']:#line:146
                        OOOOOOO0O00OO0O00 ='✅'#line:147
                    else :#line:148
                        OOOOOOO0O00OO0O00 ='❌'#line:149
                    if '正在闯关'in OO0O0O0O0OOOOOOOO ['data']['npc_hint']:#line:150
                        OOO00OO0OOO00OO00 =OO0O0O0O0OOOOOOOO ['data']['npc_hint'][:8 ]#line:151
                    else :#line:152
                        OOO00OO0OOO00OO00 =OO0O0O0O0OOOOOOOO ['data']['npc_hint'][:5 ]#line:153
                    print (f'【游戏状态】:自动:{O0OOO00O0O00O000O}丨闯关:{O00O0O00OOOO0OOO0}丨VIP:{OOOOOOO0O00OO0O00}丨{OOO00OO0OOO00OO00}')#line:154
                    if not OO0O0O0O0OOOOOOOO ['data']['is_auto_play']:#line:155
                        if OOOOOO00000O00O00 =='1':#line:156
                            O0O0OO00OOOO00OO0 .setAutoPlay ()#line:157
        except Exception as O0000O0O0O00OOOOO :#line:158
            print (O0000O0O0O00OOOOO )#line:159
    def LuckyBox (O00000OOO00000OO0 ):#line:163
        try :#line:164
            OOOOO0O00O0OOOO0O =requests .request ('post',f'{host}/api/LuckyBox/index',headers =O00000OOO00000OO0 .headers ).json ()#line:165
            if 'code'in OOOOO0O00O0OOOO0O :#line:167
                if OOOOO0O00O0OOOO0O ['code']==1 :#line:168
                    OOOO00OOO00OOOO0O =OOOOO0O00O0OOOO0O ['data']['debris']#line:169
                    OOO00OOOO00O00O0O =OOOOO0O00O0OOOO0O ['data']['is_draw']#line:170
                    print (f'【幸运宝箱】:碎片:{str(OOOO00OOO00OOOO0O).split(".")[0]}丨当前设置开启宝箱ID:{O00000OOO00000OO0.box}')#line:171
                    if not OOO00OOOO00O00O0O :#line:172
                        OOO0O00OO000O0OOO =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =O00000OOO00000OO0 .headers ).json ()#line:173
                        if 'code'in OOO0O00OO000O0OOO :#line:175
                            if OOO0O00OO000O0OOO ['code']==1 :#line:176
                                O0O00OOO0000OOO0O =OOO0O00OO000O0OOO ['data']['nub']#line:177
                                print (f'【领取碎片】:获得:{O0O00OOO0000OOO0O}')#line:178
                    for O0O0O00000O0OO0OO in OOOOO0O00O0OOOO0O ['data']['box_list']:#line:179
                        OO000OO0OO00OO000 =O0O0O00000O0OO0OO ['id']#line:181
                        O00OO00000OOO0O0O =O0O0O00000O0OO0OO ['name']#line:182
                        O0O00OOO0O0O0OOOO =O0O0O00000O0OO0OO ['inventory']#line:183
                        O0OO0OOOOO000OOO0 =O0O0O00000O0OO0OO ['need_debris']#line:184
                        if float (OO000OO0OO00OO000 )==float (O00000OOO00000OO0 .box ):#line:185
                            print (f'【幸运宝箱】:名称:{O00OO00000OOO0O0O}丨需要碎片:{O0OO0OOOOO000OOO0}丨剩余:{O0O00OOO0O0O0OOOO}')#line:186
                            if float (OOOO00OOO00OOOO0O )>=float (O0OO0OOOOO000OOO0 ):#line:187
                                O0O0OOOOOO000O00O ={'id':O00000OOO00000OO0 .box }#line:188
                                O000O0O0O0000OO0O =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =O00000OOO00000OO0 .headers ,data =O0O0OOOOOO000O00O ).json ()#line:189
                                if 'code'in O000O0O0O0000OO0O :#line:191
                                    if O000O0O0O0000OO0O ['code']==1 :#line:192
                                        print (f'【兑换宝箱】:{O000O0O0O0000OO0O["msg"]}丨获得{O000O0O0O0000OO0O["data"]["name"]}')#line:193
        except Exception as OO0OO0O0000000000 :#line:194
            print (OO0OO0O0000000000 )#line:195
    def score_record (OOOO0O0O000O0OOOO ):#line:198
        O00O0OO0O000OOO0O ={'page':'1','limit':'15','type':'2'}#line:199
        OOO0OO000O000O0OO =requests .request ('post',f'{host}/api/Score/record',headers =OOOO0O0O000O0OOOO .headers ,data =O00O0OO0O000OOO0O ).json ()#line:200
        if 'code'in OOO0OO000O000O0OO :#line:202
            if OOO0OO000O000O0OO ['code']==1 :#line:203
                OOOOOO0OO0000000O =OOO0OO000O000O0OO ['data']['record_list']#line:204
                if OOOOOO0OO0000000O :#line:205
                    for OO0OOO0OOOO0000O0 in OOOOOO0OO0000000O :#line:206
                        OOO0OO00O000OOO0O =OO0OOO0OOOO0000O0 ['user_id']#line:207
                        OOOO0O0OOOO0O00O0 =OO0OOO0OOOO0000O0 ['money']#line:208
                        OOO000O000OOOOO0O =OO0OOO0OOOO0000O0 ['create_time']#line:209
                        O0OO000OOO00000O0 =OO0OOO0OOOO0000O0 ['nickname']#line:210
                        print (f'【赠送记录】:昵称:{O0OO000OOO00000O0}丨ID:{OOO0OO00O000OOO0O}丨金额:{OOOO0O0OOOO0O00O0}丨时间:{OOO000O000OOOOO0O[5:16]}')#line:211
    def score_present (O000OO0O0OO0O00O0 ):#line:214
        global present_nub #line:215
        try :#line:216
            if float (score )>float (score_big ):#line:217
                O000OO0OOOO0OO00O ={'id':present_id }#line:218
                O0O00OO0O0OOO0O0O =requests .request ('post',f'{host}/api/Score/presentFindUser',headers =O000OO0O0OO0O00O0 .headers ,data =O000OO0OOOO0OO00O ).json ()#line:219
                if 'code'in O0O00OO0O0OOO0O0O :#line:221
                    if O0O00OO0O0OOO0O0O ['code']==1 :#line:222
                        OO0000000000OOOOO =O0O00OO0O0OOO0O0O ['data']['grade']#line:223
                        if OO0000000000OOOOO =='0':#line:224
                            present_nub =int (float (score )/1.05 )#line:225
                        if OO0000000000OOOOO =='1':#line:226
                            present_nub =int (float (score )/1.1 )#line:227
                present_nub =int (float (score )/1.05 )#line:228
                if present_nub >1 :#line:229
                    O000000OO0O0OO0OO ={'present_id':present_id ,'present_nub':present_nub }#line:230
                    OOO0O0O00O0OOO00O =requests .request ('post',f'{host}/api/Score/present',headers =O000OO0O0OO0O00O0 .headers ,data =O000000OO0O0OO0OO ).json ()#line:231
                    if 'code'in OOO0O0O00O0OOO00O :#line:233
                        if OOO0O0O00O0OOO00O ['code']==1 :#line:234
                            print (f'【赠送金币】:ID:{present_id}丨金币:{present_nub}丨{OOO0O0O00O0OOO00O["msg"]}')#line:235
                        elif OOO0O0O00O0OOO00O ['code']==0 :#line:236
                            print (f'【赠送金币】:ID:{present_id}丨金币:{present_nub}丨{OOO0O0O00O0OOO00O["msg"]}')#line:237
                        else :#line:238
                            print (OOO0O0O00O0OOO00O )#line:239
        except Exception as OO00O0O0OOO0000O0 :#line:240
            print (OO00O0O0OOO0000O0 )#line:241
def start ():#line:244
    try :#line:245
        update_the_validation ()#line:246
        OOOO0OOOO0O0OO0OO =os_qinglong ()#line:247
        print (f"==========共找到{len(OOOO0OOOO0O0OO0OO)}个账号==========")#line:248
        for OOO00O00OOO0OOOO0 in OOOO0OOOO0O0OO0OO :#line:249
            print (f"------------正在执行第{OOOO0OOOO0O0OO0OO.index(OOO00O00OOO0OOOO0) + 1}个账号------------")#line:250
            OOO0OO000O0O0000O =Template (OOO00O00OOO0OOOO0 )#line:251
            if OOO0OO000O0O0000O .base_info ():#line:253
                OOO0OO000O0O0000O .LuckyBox ()#line:255
                OOO0OO000O0O0000O .playInfo ()#line:257
                if score_record :#line:258
                    OOO0OO000O0O0000O .score_record ()#line:260
                if giving :#line:261
                    OOO0OO000O0O0000O .score_present ()#line:263
                time .sleep (random .randint (1 ,2 ))#line:265
            else :#line:266
                print ('token失效')#line:267
    except Exception as OOOOO00OOOOOOO000 :#line:268
        print (OOOOO00OOOOOOO000 )#line:269
def version_of_the_validation ():#line:271
    return str ((61 -56 )/10 )#line:272
if __name__ =='__main__':#line:275
    start ()#line:276
