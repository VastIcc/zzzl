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
@ 青龙变量 export qc_token="token&宝箱ID&赠送ID"   1普通宝箱 2白银宝箱 3黄金宝箱 4神秘宝箱 5炫彩宝箱  多号换行
@ 版本 0.5
"""
##################################配置区##################################
score_record = False        # 赠送记录   
score_big = '80000'         # 大于5才赠送
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
        O0O0O00OO00O000O0 =os .environ [application ].split ('\n')#line:5
        if len (O0O0O00OO00O000O0 )>0 :#line:6
            return O0O0O00OO00O000O0 #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        OOO00O0O0O0000O0O =token .split ('\n')#line:19
        if len (OOO00O0O0O0000O0O )>0 :#line:20
            return OOO00O0O0O0000O0O #line:21
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
        OO0O0OO0O00O0000O =gitee_validation ()#line:38
        if version_of_the_validation ()<OO0O0OO0O00O0000O ['Tower']['edition']:#line:39
            print (f'当前脚本名字: {OO0O0OO0O00O0000O["Tower"]["text"]}')#line:40
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0OO0O00O0000O["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:41
            print (f'更新内容=>> {OO0O0OO0O00O0000O["Tower"]["content"]}')#line:42
        else :#line:43
            print (f'当前脚本名字: {OO0O0OO0O00O0000O["Tower"]["text"]}')#line:44
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0OO0O00O0000O["Tower"]["edition"]}   ✅')#line:45
            print (f'更新内容=>> {OO0O0OO0O00O0000O["Tower"]["content"]}')#line:46
    except Exception as O0OOOO0OO00O00OOO :#line:47
        print (O0OOOO0OO00O00OOO )#line:48
class Template :#line:51
    def __init__ (OOOO0OO000OO0OOOO ,O0OO000OO000O0000 ):#line:53
        try :#line:54
            OOOO0OO000OO0OOOO .token =O0OO000OO000O0000 .split ('&')[0 ]#line:55
            OOOO0OO000OO0OOOO .box =O0OO000OO000O0000 .split ('&')[1 ]#line:56
            OOOO0OO000OO0OOOO .present_id =O0OO000OO000O0000 .split ('&')[2 ]#line:57
            OOOO0OO000OO0OOOO .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OOOO0OO000OO0OOOO .token ,'server':'true','phone-type':'android',}#line:69
        except Exception as OOO0OO00O0O0O0OO0 :#line:70
            print ('变量格式错误')#line:71
    def base_info (OOOOO00O0000OO0O0 ):#line:74
        global score #line:75
        try :#line:76
            O0O0O0OO00O000OO0 =requests .request ('post',f'{host}/api/User/info',headers =OOOOO00O0000OO0O0 .headers ).json ()#line:77
            if 'code'in O0O0O0OO00O000OO0 :#line:79
                if O0O0O0OO00O000OO0 ['code']==1 :#line:80
                    OOOO000O00O00O00O =O0O0O0OO00O000OO0 ['data']['nickname']#line:81
                    OO0OO00O0000OO0O0 =O0O0O0OO00O000OO0 ['data']['id']#line:82
                    score =O0O0O0OO00O000OO0 ['data']['score']#line:83
                    print (f'【账号信息】:昵称:{OOOO000O00O00O00O[:6]}丨ID:{OO0OO00O0000OO0O0}丨金币:{str(score)[:5]}')#line:84
                if O0O0O0OO00O000OO0 ['code']==302 :#line:85
                    return False #line:86
            return True #line:87
        except Exception as OOO0OOOO00O00O0O0 :#line:88
            print (OOO0OOOO00O00O0O0 )#line:89
    def playInfo (O000O0000O00OO00O ):#line:92
        try :#line:93
            OO0000OOOOO0O0000 =requests .request ('post',f'{host}/api/Game/playInfo',headers =O000O0000O00OO00O .headers ).json ()#line:94
            if 'code'in OO0000OOOOO0O0000 :#line:96
                if OO0000OOOOO0O0000 ['code']==1 :#line:97
                    OO00O0OOO00O0000O =OO0000OOOOO0O0000 ['data']['play_tier']#line:98
                    OOO00OO000000OOO0 =OO0000OOOOO0O0000 ['data']['play_tier_need_money']#line:99
                    O000OOO0O00OOO0O0 =OO0000OOOOO0O0000 ['data']['user_money']#line:100
                    O0O0O0O0O0000O00O =OO0000OOOOO0O0000 ['data']['play_finish_money']#line:101
                    O0OOO0OOO00OOOOOO =OO0000OOOOO0O0000 ['data']['surplus_play_nub']#line:102
                    print (f'【参与闯关】:层数:{OO00O0OOO00O0000O}丨剩余:{O0OOO0OOO00OOOOOO}丨花费:{OOO00OO000000OOO0}丨预计:{O0O0O0O0O0000O00O}')#line:103
                    if float (OOO00OO000000OOO0 )<float (O000OOO0O00OOO0O0 ):#line:104
                        if O0OOO0OOO00OOOOOO >0 :#line:105
                            O000O0000O00OO00O .Game_index ('1')#line:106
                        else :#line:107
                            O000O0000O00OO00O .Game_index ('2')#line:108
                    else :#line:109
                        O000O0000O00OO00O .Game_index ('2')#line:110
        except Exception as O0OO0OO0O00OO0000 :#line:112
            print (O0OO0OO0O00OO0000 )#line:113
    def setAutoPlay (OOO0OOOOO00O0OOO0 ):#line:116
        try :#line:117
            O00O0OOOOO0O0OO0O ={'state':'1'}#line:120
            O0OOOO0OO000O0OO0 =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =OOO0OOOOO00O0OOO0 .headers ,data =O00O0OOOOO0O0OO0O ).json ()#line:121
            if 'code'in O0OOOO0OO000O0OO0 :#line:123
                if O0OOOO0OO000O0OO0 ['code']==1 :#line:124
                    print (f'【自动闯关】:{O0OOOO0OO000O0OO0["msg"]}')#line:125
                if O0OOOO0OO000O0OO0 ['code']==0 :#line:126
                    print (f'【自动闯关】:{O0OOOO0OO000O0OO0["msg"]}')#line:127
        except Exception as O000000OO0OOO00O0 :#line:128
            print (O000000OO0OOO00O0 )#line:129
    def Game_index (OO0O0OO00OO0OO000 ,OO0OOO0OO00OO0OO0 ):#line:132
        try :#line:133
            OO0O00O0OO00O0000 =requests .request ('post',f'{host}/api/Game/index',headers =OO0O0OO00OO0OO000 .headers ).json ()#line:134
            if 'code'in OO0O00O0OO00O0000 :#line:136
                if OO0O00O0OO00O0000 ['code']==1 :#line:137
                    if OO0O00O0OO00O0000 ['data']['is_auto_play']:#line:138
                        OO0O0O000OOOO0O00 ='✅'#line:139
                    else :#line:140
                        OO0O0O000OOOO0O00 ='❌'#line:141
                    if OO0O00O0OO00O0000 ['data']['is_game_ing']:#line:143
                        O0OOO0OO0OOOOOO00 ='✅'#line:144
                    else :#line:145
                        O0OOO0OO0OOOOOO00 ='❌'#line:146
                    if OO0O00O0OO00O0000 ['data']['is_vip']:#line:147
                        OOOOO00O00000OO0O ='✅'#line:148
                    else :#line:149
                        OOOOO00O00000OO0O ='❌'#line:150
                    if '正在闯关'in OO0O00O0OO00O0000 ['data']['npc_hint']:#line:151
                        O00OO0OO000OOOOOO =OO0O00O0OO00O0000 ['data']['npc_hint'][:8 ]#line:152
                    else :#line:153
                        O00OO0OO000OOOOOO =OO0O00O0OO00O0000 ['data']['npc_hint'][:5 ]#line:154
                    print (f'【游戏状态】:自动:{OO0O0O000OOOO0O00}丨闯关:{O0OOO0OO0OOOOOO00}丨VIP:{OOOOO00O00000OO0O}丨{O00OO0OO000OOOOOO}')#line:155
                    if not OO0O00O0OO00O0000 ['data']['is_auto_play']:#line:156
                        if OO0OOO0OO00OO0OO0 =='1':#line:157
                            OO0O0OO00OO0OO000 .setAutoPlay ()#line:158
        except Exception as OOO000OO000OO0000 :#line:159
            print (OOO000OO000OO0000 )#line:160
    def LuckyBox (O0000OO0OOO0OO0OO ):#line:164
        try :#line:165
            O00O0O0O000OOOO0O =requests .request ('post',f'{host}/api/LuckyBox/index',headers =O0000OO0OOO0OO0OO .headers ).json ()#line:166
            if 'code'in O00O0O0O000OOOO0O :#line:168
                if O00O0O0O000OOOO0O ['code']==1 :#line:169
                    OO00OO000O0OO00O0 =O00O0O0O000OOOO0O ['data']['debris']#line:170
                    OO0OOOO0OO0OOO00O =O00O0O0O000OOOO0O ['data']['is_draw']#line:171
                    print (f'【幸运宝箱】:碎片:{str(OO00OO000O0OO00O0).split(".")[0]}丨当前设置开启宝箱ID:{O0000OO0OOO0OO0OO.box}')#line:172
                    if not OO0OOOO0OO0OOO00O :#line:173
                        O0O000O00OOO00OO0 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =O0000OO0OOO0OO0OO .headers ).json ()#line:174
                        if 'code'in O0O000O00OOO00OO0 :#line:176
                            if O0O000O00OOO00OO0 ['code']==1 :#line:177
                                O0OOOO0000O0OO000 =O0O000O00OOO00OO0 ['data']['nub']#line:178
                                print (f'【领取碎片】:获得:{O0OOOO0000O0OO000}')#line:179
                    for OOOO0000OOOO0O0OO in O00O0O0O000OOOO0O ['data']['box_list']:#line:180
                        O00O0O0OO0000000O =OOOO0000OOOO0O0OO ['id']#line:182
                        O00O0OOO0OO0O0000 =OOOO0000OOOO0O0OO ['name']#line:183
                        O0OOOOOO00OOO0000 =OOOO0000OOOO0O0OO ['inventory']#line:184
                        O00OO0000OO0OO0OO =OOOO0000OOOO0O0OO ['need_debris']#line:185
                        if float (O00O0O0OO0000000O )==float (O0000OO0OOO0OO0OO .box ):#line:186
                            print (f'【幸运宝箱】:名称:{O00O0OOO0OO0O0000}丨需要碎片:{O00OO0000OO0OO0OO}丨剩余:{O0OOOOOO00OOO0000}')#line:187
                            if float (OO00OO000O0OO00O0 )>=float (O00OO0000OO0OO0OO ):#line:188
                                OOO00000OOO0O0O0O ={'id':O0000OO0OOO0OO0OO .box }#line:189
                                O00O0O0O000OO0OO0 =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =O0000OO0OOO0OO0OO .headers ,data =OOO00000OOO0O0O0O ).json ()#line:190
                                if 'code'in O00O0O0O000OO0OO0 :#line:192
                                    if O00O0O0O000OO0OO0 ['code']==1 :#line:193
                                        print (f'【兑换宝箱】:{O00O0O0O000OO0OO0["msg"]}丨获得{O00O0O0O000OO0OO0["data"]["name"]}')#line:194
        except Exception as O0O0000O0OOO0O0O0 :#line:195
            print (O0O0000O0OOO0O0O0 )#line:196
    def score_record (O0OOOOOO0O0O000O0 ):#line:199
        O00OOOOO000OO0OOO ={'page':'1','limit':'15','type':'2'}#line:200
        OOOOO0OO00OOO0OO0 =requests .request ('post',f'{host}/api/Score/record',headers =O0OOOOOO0O0O000O0 .headers ,data =O00OOOOO000OO0OOO ).json ()#line:201
        if 'code'in OOOOO0OO00OOO0OO0 :#line:203
            if OOOOO0OO00OOO0OO0 ['code']==1 :#line:204
                OO0O000OOO0O000O0 =OOOOO0OO00OOO0OO0 ['data']['record_list']#line:205
                if OO0O000OOO0O000O0 :#line:206
                    for O00OOO0OO0O0O00OO in OO0O000OOO0O000O0 :#line:207
                        OO0OOO00O0OOOOOO0 =O00OOO0OO0O0O00OO ['user_id']#line:208
                        OOOOOOO0000OO0000 =O00OOO0OO0O0O00OO ['money']#line:209
                        O000O0000000O0O0O =O00OOO0OO0O0O00OO ['create_time']#line:210
                        O000OOO000O0O0000 =O00OOO0OO0O0O00OO ['nickname']#line:211
                        print (f'【赠送记录】:昵称:{O000OOO000O0O0000}丨ID:{OO0OOO00O0OOOOOO0}丨金额:{OOOOOOO0000OO0000}丨时间:{O000O0000000O0O0O[5:16]}')#line:212
    def score_present (OO0000OO0OO0OO0OO ):#line:215
        global present_nub #line:216
        try :#line:217
            if float (score )>float (score_big ):#line:218
                OO00000O0O000O00O ={'id':OO0000OO0OO0OO0OO .present_id }#line:219
                OOOO00OO00O00OOOO =requests .request ('post',f'{host}/api/Score/presentFindUser',headers =OO0000OO0OO0OO0OO .headers ,data =OO00000O0O000O00O ).json ()#line:220
                if 'code'in OOOO00OO00O00OOOO :#line:222
                    if OOOO00OO00O00OOOO ['code']==1 :#line:223
                        OO00O00OOOO0OO000 =OOOO00OO00O00OOOO ['data']['grade']#line:224
                        if OO00O00OOOO0OO000 =='0':#line:225
                            present_nub =int (float (score )/1.05 )#line:226
                        if OO00O00OOOO0OO000 =='1':#line:227
                            present_nub =int (float (score )/1.1 )#line:228
                present_nub =int (float (score )/1.05 )#line:229
                if present_nub >1 :#line:230
                    OO0OO0000OO000O0O ={'present_id':OO0000OO0OO0OO0OO .present_id ,'present_nub':present_nub }#line:231
                    OO0OO000OO000OO00 =requests .request ('post',f'{host}/api/Score/present',headers =OO0000OO0OO0OO0OO .headers ,data =OO0OO0000OO000O0O ).json ()#line:232
                    if 'code'in OO0OO000OO000OO00 :#line:234
                        if OO0OO000OO000OO00 ['code']==1 :#line:235
                            print (f'【赠送金币】:ID:{OO0000OO0OO0OO0OO.present_id}丨金币:{present_nub}丨{OO0OO000OO000OO00["msg"]}')#line:236
                        elif OO0OO000OO000OO00 ['code']==0 :#line:237
                            print (f'【赠送金币】:ID:{OO0000OO0OO0OO0OO.present_id}丨金币:{present_nub}丨{OO0OO000OO000OO00["msg"]}')#line:238
                        else :#line:239
                            print (OO0OO000OO000OO00 )#line:240
        except Exception as O000OOOOOOO00O0O0 :#line:241
            print (O000OOOOOOO00O0O0 )#line:242
def start ():#line:245
    try :#line:246
        update_the_validation ()#line:247
        O0OOOOO0OOO0O000O =os_qinglong ()#line:248
        print (f"==========共找到{len(O0OOOOO0OOO0O000O)}个账号==========")#line:249
        for OO0OO0O0OO0OO0O00 in O0OOOOO0OOO0O000O :#line:250
            print (f"------------正在执行第{O0OOOOO0OOO0O000O.index(OO0OO0O0OO0OO0O00) + 1}个账号------------")#line:251
            OOO000O0OO00OO0O0 =Template (OO0OO0O0OO0OO0O00 )#line:252
            if OOO000O0OO00OO0O0 .base_info ():#line:254
                OOO000O0OO00OO0O0 .LuckyBox ()#line:256
                OOO000O0OO00OO0O0 .playInfo ()#line:258
                if score_record :#line:259
                    OOO000O0OO00OO0O0 .score_record ()#line:261
                OOO000O0OO00OO0O0 .score_present ()#line:263
                time .sleep (random .randint (2 ,3 ))#line:265
            else :#line:266
                print ('token失效')#line:267
    except Exception as OO0000OO0OOO00O00 :#line:268
        print (OO0000OO0OOO00O00 )#line:269
def version_of_the_validation ():#line:271
    return str ((61 -56 )/10 )#line:272
if __name__ =='__main__':#line:275
    start ()#line:276
