# coding: utf-8
try:
    import requests, re, os, sys, time, random
except Exception as E:
    t = re.findall("d '(.*?)'", str(E))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: 10,25 0,12 * * *
@ new Env('千层塔会员版')
@ 项目地址  https://qct.qitusky.cn/invite/?invite_code=1476
@ 抓取  https://qct.qitusky.cn 的ba-user-token值
@ 青龙变量 export qc_token="token&宝箱ID&赠送ID"   1普通宝箱 2白银宝箱 3黄金宝箱 4神秘宝箱 5炫彩宝箱  多号换行
@ 版本 0.8
"""
##################################配置区##################################
score_record = False        # 赠送记录
score_big = '50000'         # 大于5才赠送
##################################配置区##################################
##################################下面不要动##################################
sr = []
score = 0
versions = '1.1.9'           # 版本
application = 'qc_token'  # 变量名
token = ''  #
##################################下面不要动##################################
host ='https://qct.qitusky.cn'#line:1
git ='https://gitee.com'#line:2
def os_qinglong ():#line:3
    if application in os .environ :#line:4
        O0OO00OOO0O00OO00 =os .environ [application ].split ('\n')#line:5
        if len (O0OO00OOO0O00OO00 )>0 :#line:6
            return O0OO00OOO0O00OO00 #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        O000O0OO00000OOO0 =token .split ('\n')#line:19
        if len (O000O0OO00000OOO0 )>0 :#line:20
            return O000O0OO00000OOO0 #line:21
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
        O00O0O000000O0OOO =gitee_validation ()#line:38
        if version_of_the_validation ()<O00O0O000000O0OOO ['Tower']['edition']:#line:39
            print (f'当前脚本名字: {O00O0O000000O0OOO["Tower"]["text"]}')#line:40
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0O000000O0OOO["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:41
            print (f'更新内容=>> {O00O0O000000O0OOO["Tower"]["content"]}')#line:42
        else :#line:43
            print (f'当前脚本名字: {O00O0O000000O0OOO["Tower"]["text"]}')#line:44
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0O000000O0OOO["Tower"]["edition"]}   ✅')#line:45
            print (f'更新内容=>> {O00O0O000000O0OOO["Tower"]["content"]}')#line:46
    except Exception as O0OOOO0OOOO0OO0OO :#line:47
        print (O0OOOO0OOOO0OO0OO )#line:48
class Template :#line:51
    def __init__ (O0OO0O0O000000O0O ,OO0OO0OOO00OOOOO0 ):#line:53
        try :#line:54
            O0OO0O0O000000O0O .token =OO0OO0OOO00OOOOO0 .split ('&')[0 ]#line:55
            O0OO0O0O000000O0O .box =OO0OO0OOO00OOOOO0 .split ('&')[1 ]#line:56
            O0OO0O0O000000O0O .present_id =OO0OO0OOO00OOOOO0 .split ('&')[2 ]#line:57
            O0OO0O0O000000O0O .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':versions ,'accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':O0OO0O0O000000O0O .token ,'server':'true','phone-type':'android',}#line:69
        except :#line:70
            print ('变量格式错误')#line:71
    def base_info (O000OO000O0OO0O00 ):#line:74
        global score #line:75
        try :#line:76
            OOOOO0000OOO00000 =requests .request ('post',f'{host}/api/User/info',headers =O000OO000O0OO0O00 .headers ).json ()#line:77
            if 'code'in OOOOO0000OOO00000 :#line:79
                if OOOOO0000OOO00000 ['code']==1 :#line:80
                    O000O00OOO00O0OO0 =OOOOO0000OOO00000 ['data']['nickname']#line:81
                    OOO0OO0OO00O000O0 =OOOOO0000OOO00000 ['data']['id']#line:82
                    score =OOOOO0000OOO00000 ['data']['score']#line:83
                    print (f'【账号信息】:昵称:{O000O00OOO00O0OO0[:6]}丨ID:{OOO0OO0OO00O000O0}丨金币:{str(score)[:5]}')#line:84
                if OOOOO0000OOO00000 ['code']==302 :#line:85
                    return False #line:86
            return True #line:87
        except Exception as O0OOO0OO0000000O0 :#line:88
            print (O0OOO0OO0000000O0 )#line:89
    def playInfo (O0OOOOOO0OO0OO0O0 ):#line:92
        try :#line:93
            OO000OOO0O0OOO00O =requests .request ('post',f'{host}/api/Game/playInfo',headers =O0OOOOOO0OO0OO0O0 .headers ).json ()#line:94
            if 'code'in OO000OOO0O0OOO00O :#line:96
                if OO000OOO0O0OOO00O ['code']==1 :#line:97
                    O0O00OO00O0O00000 =OO000OOO0O0OOO00O ['data']['play_tier']#line:98
                    O0O000OOO0O00OOOO =OO000OOO0O0OOO00O ['data']['play_tier_need_money']#line:99
                    OOOOO00O0O0OO0000 =OO000OOO0O0OOO00O ['data']['user_money']#line:100
                    O00OO00OO0OOO000O =OO000OOO0O0OOO00O ['data']['play_finish_money']#line:101
                    O00OO000OOOO00OOO =OO000OOO0O0OOO00O ['data']['surplus_play_nub']#line:102
                    print (f'【参与闯关】:层数:{O0O00OO00O0O00000}丨剩余:{O00OO000OOOO00OOO}丨花费:{O0O000OOO0O00OOOO}丨预计:{O00OO00OO0OOO000O}')#line:103
                    if float (O0O000OOO0O00OOOO )<float (OOOOO00O0O0OO0000 ):#line:104
                        if O00OO000OOOO00OOO >0 :#line:105
                            O0OOOOOO0OO0OO0O0 .Game_index ('1')#line:106
                        else :#line:107
                            O0OOOOOO0OO0OO0O0 .Game_index ('2')#line:108
                    else :#line:109
                        O0OOOOOO0OO0OO0O0 .Game_index ('2')#line:110
        except Exception as OO0O000O00OO0O0OO :#line:112
            print (OO0O000O00OO0O0OO )#line:113
    def setAutoPlay (O0000OO0OO000OO00 ):#line:116
        try :#line:117
            OOOOO00OOOOO00OO0 ={'state':'1'}#line:120
            OOO0OO0O0OO0000OO =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O0000OO0OO000OO00 .headers ,data =OOOOO00OOOOO00OO0 ).json ()#line:121
            if 'code'in OOO0OO0O0OO0000OO :#line:123
                if OOO0OO0O0OO0000OO ['code']==1 :#line:124
                    print (f'【自动闯关】:{OOO0OO0O0OO0000OO["msg"]}')#line:125
                if OOO0OO0O0OO0000OO ['code']==0 :#line:126
                    print (f'【自动闯关】:{OOO0OO0O0OO0000OO["msg"]}')#line:127
        except Exception as O0O000OOO0O0O0OO0 :#line:128
            print (O0O000OOO0O0O0OO0 )#line:129
    def Game_index (OO0OOO0O000000O0O ,OOOO0O0000OOOO00O ):#line:132
        try :#line:133
            O00OO0OOO0OO000O0 =requests .request ('post',f'{host}/api/Game/index',headers =OO0OOO0O000000O0O .headers ).json ()#line:134
            if 'code'in O00OO0OOO0OO000O0 :#line:136
                if O00OO0OOO0OO000O0 ['code']==1 :#line:137
                    if O00OO0OOO0OO000O0 ['data']['is_auto_play']:#line:138
                        OOO0OO00OOO000O0O ='✅'#line:139
                    else :#line:140
                        OOO0OO00OOO000O0O ='❌'#line:141
                    if O00OO0OOO0OO000O0 ['data']['is_game_ing']:#line:143
                        O0000O00OOOOOOO0O ='✅'#line:144
                    else :#line:145
                        O0000O00OOOOOOO0O ='❌'#line:146
                    if O00OO0OOO0OO000O0 ['data']['is_vip']:#line:147
                        O000O00OOOO0O0OO0 ='✅'#line:148
                    else :#line:149
                        O000O00OOOO0O0OO0 ='❌'#line:150
                    if '正在闯关'in O00OO0OOO0OO000O0 ['data']['npc_hint']:#line:151
                        O0O0O0OOO00O0O0O0 =O00OO0OOO0OO000O0 ['data']['npc_hint'][:8 ]#line:152
                    else :#line:153
                        O0O0O0OOO00O0O0O0 =O00OO0OOO0OO000O0 ['data']['npc_hint'][:5 ]#line:154
                    print (f'【游戏状态】:自动:{OOO0OO00OOO000O0O}丨闯关:{O0000O00OOOOOOO0O}丨VIP:{O000O00OOOO0O0OO0}丨{O0O0O0OOO00O0O0O0}')#line:155
                    if not O00OO0OOO0OO000O0 ['data']['is_auto_play']:#line:156
                        if OOOO0O0000OOOO00O =='1':#line:157
                            OO0OOO0O000000O0O .setAutoPlay ()#line:158
        except Exception as O0000000OOOO0OO00 :#line:159
            print (O0000000OOOO0OO00 )#line:160
    def LuckyBox (OOO0O0OO00OO0OO0O ):#line:164
        global sr #line:165
        try :#line:166
            OOOO0OO000O0OO0OO =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OOO0O0OO00OO0OO0O .headers ).json ()#line:167
            if 'code'in OOOO0OO000O0OO0OO :#line:169
                if OOOO0OO000O0OO0OO ['code']==1 :#line:170
                    OO0O0OO00OO0OO000 =OOOO0OO000O0OO0OO ['data']['debris']#line:171
                    OOO0O00O00OO0O0OO =OOOO0OO000O0OO0OO ['data']['is_draw']#line:172
                    print (f'【幸运宝箱】:碎片:{str(OO0O0OO00OO0OO000).split(".")[0]}丨当前设置开启宝箱ID:{OOO0O0OO00OO0OO0O.box}')#line:173
                    if not OOO0O00O00OO0O0OO :#line:174
                        OO00O00O0OO0O0000 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OOO0O0OO00OO0OO0O .headers ).json ()#line:175
                        if 'code'in OO00O00O0OO0O0000 :#line:177
                            if OO00O00O0OO0O0000 ['code']==1 :#line:178
                                OOOOO00O00OO0O000 =OO00O00O0OO0O0000 ['data']['nub']#line:179
                                print (f'【领取碎片】:获得:{OOOOO00O00OO0O000}')#line:180
                    for O0O0OO0OO00OO000O in OOOO0OO000O0OO0OO ['data']['box_list']:#line:181
                        OOOOOOO00O00OOO0O =O0O0OO0OO00OO000O ['id']#line:183
                        O00O00O0O0OO00OO0 =O0O0OO0OO00OO000O ['name']#line:184
                        O00OOOO0O0O00O000 =O0O0OO0OO00OO000O ['inventory']#line:185
                        O0O0O0OO000OOO00O =O0O0OO0OO00OO000O ['need_debris']#line:186
                        if float (OOOOOOO00O00OOO0O )==float (OOO0O0OO00OO0OO0O .box ):#line:187
                            print (f'【幸运宝箱】:名称:{O00O00O0O0OO00OO0}丨需要碎片:{O0O0O0OO000OOO00O}丨剩余:{O00OOOO0O0O00O000}')#line:189
                            if float (OO0O0OO00OO0OO000 )>=float (O0O0O0OO000OOO00O ):#line:190
                                sr .append (OOO0O0OO00OO0OO0O .token +'&'+OOO0O0OO00OO0OO0O .box )#line:191
                                if O00OOOO0O0O00O000 >0 :#line:192
                                    OO000OO0OO0000OO0 ={'id':OOO0O0OO00OO0OO0O .box }#line:193
                                    OO0O00O0OOOO0O000 =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =OOO0O0OO00OO0OO0O .headers ,data =OO000OO0OO0000OO0 ).json ()#line:194
                                    if 'code'in OO0O00O0OOOO0O000 :#line:196
                                        if OO0O00O0OOOO0O000 ['code']==1 :#line:197
                                            print (f'【兑换宝箱】:{OO0O00O0OOOO0O000["msg"]}丨获得{OO0O00O0OOOO0O000["data"]["name"]}')#line:198
        except Exception as OOO00OOO00OOOO0OO :#line:199
            print (OOO00OOO00OOOO0OO )#line:200
    def score_record (O0OO00O0OO0O0000O ):#line:203
        O0OO0OO0O0OO00OO0 ={'page':'1','limit':'15','type':'2'}#line:204
        O000O00OO0OOOO00O =requests .request ('post',f'{host}/api/Score/record',headers =O0OO00O0OO0O0000O .headers ,data =O0OO0OO0O0OO00OO0 ).json ()#line:205
        if 'code'in O000O00OO0OOOO00O :#line:207
            if O000O00OO0OOOO00O ['code']==1 :#line:208
                OOOO0OO0O0O0OOO0O =O000O00OO0OOOO00O ['data']['record_list']#line:209
                if OOOO0OO0O0O0OOO0O :#line:210
                    for OOOO00O0OOO00000O in OOOO0OO0O0O0OOO0O :#line:211
                        OOO000O0O000O0000 =OOOO00O0OOO00000O ['user_id']#line:212
                        O0000O0O0OOOO00O0 =OOOO00O0OOO00000O ['money']#line:213
                        OO000OO0000O00OO0 =OOOO00O0OOO00000O ['create_time']#line:214
                        OOOO0O0OO000OOO00 =OOOO00O0OOO00000O ['nickname']#line:215
                        print (f'【赠送记录】:昵称:{OOOO0O0OO000OOO00}丨ID:{OOO000O0O000O0000}丨金额:{O0000O0O0OOOO00O0}丨时间:{OO000OO0000O00OO0[5:16]}')#line:216
    def score_present (O0000O000O0O000OO ):#line:219
        try :#line:220
            if float (score )>float (score_big ):#line:221
                O0O0OO00O0OOO0OO0 ={'id':O0000O000O0O000OO .present_id }#line:222
                O0O0000O00OOOOOOO =requests .request ('post',f'{host}/api/Score/presentFindUser',headers =O0000O000O0O000OO .headers ,data =O0O0OO00O0OOO0OO0 ).json ()#line:223
                if 'code'in O0O0000O00OOOOOOO :#line:225
                    if O0O0000O00OOOOOOO ['code']==1 :#line:226
                        O0O0O0O0O000OOO00 =O0O0000O00OOOOOOO ['data']['service_charge']#line:227
                        OO00OO000O00OO0O0 =int (float (score )/(1 +(int (O0O0O0O0O000OOO00 )/100 )))#line:228
                        if OO00OO000O00OO0O0 >1 :#line:229
                            OOO000O0O000OO00O ={'present_id':O0000O000O0O000OO .present_id ,'present_nub':OO00OO000O00OO0O0 }#line:230
                            O000OOOOO0O0OO0OO =requests .request ('post',f'{host}/api/Score/present',headers =O0000O000O0O000OO .headers ,data =OOO000O0O000OO00O ).json ()#line:231
                            if 'code'in O000OOOOO0O0OO0OO :#line:233
                                if O000OOOOO0O0OO0OO ['code']==1 :#line:234
                                    print (f'【赠送金币】:ID:{O0000O000O0O000OO.present_id}丨金币:{OO00OO000O00OO0O0}丨{O000OOOOO0O0OO0OO["msg"]}')#line:235
                                elif O000OOOOO0O0OO0OO ['code']==0 :#line:236
                                    print (f'【赠送金币】:ID:{O0000O000O0O000OO.present_id}丨金币:{OO00OO000O00OO0O0}丨{O000OOOOO0O0OO0OO["msg"]}')#line:237
                                else :#line:238
                                    print (O000OOOOO0O0OO0OO )#line:239
        except Exception as O000OO0000000000O :#line:240
            print (O000OO0000000000O )#line:241
    def figure (O0OOOO0OO000OOO00 ,O00O00OO00OOO0000 ):#line:244
        try :#line:245
            OOO000OO00OOOOO00 =requests .request ('post',f'{host}/api/figure/index',headers =O0OOOO0OO000OOO00 .headers ).json ()#line:246
            if 'code'in OOO000OO00OOOOO00 :#line:248
                if OOO000OO00OOOOO00 ['code']==1 :#line:249
                    for OO0O000OOO00OO0O0 in OOO000OO00OOOOO00 ['data']['user_figure_list']:#line:250
                        OO0O0OO00O0O0O0O0 =OO0O000OOO00OO0O0 ['name']#line:251
                        if O00O00OO00OOO0000 ==OO0O0OO00O0O0O0O0 :#line:252
                            return True #line:253
            return False #line:254
        except Exception as O0OOO0OOOO000OO0O :#line:255
            print (O0OOO0OOOO000OO0O )#line:256
    def snatch (OOOO0O000OOO00O0O ):#line:259
        try :#line:260
            OO0OO00O0O0O0O000 =requests .request ('post',f'{host}/api/Snatch/index',headers =OOOO0O000OOO00O0O .headers ).json ()#line:261
            if 'code'in OO0OO00O0O0O0O000 :#line:263
                if OO0OO00O0O0O0O000 ['code']==1 :#line:264
                    O0O0000OOOO0O0000 =OO0OO00O0O0O0O000 ['data']['snatch_id']#line:265
                    O0O0O00O00O0000O0 =OO0OO00O0O0O0O000 ['data']['figure_name']#line:266
                    O00O00OOOOOOO0OOO =OO0OO00O0O0O0O000 ['data']['now_figure_nub']#line:267
                    O000OO00OO0O0O000 =OO0OO00O0O0O0O000 ['data']['max_figure_nub']#line:268
                    if O00O00OOOOOOO0OOO <O000OO00OO0O0O000 :#line:269
                        if OOOO0O000OOO00O0O .figure (O0O0O00O00O0000O0 ):#line:270
                            OOOO0O000OOO00O0O .snatch_play_index (O0O0000OOOO0O0000 )#line:271
        except Exception as O00000O0O0OOOO000 :#line:272
            print (O00000O0O0OOOO000 )#line:273
    def snatch_play_index (OOOOO00OO0O00O000 ,OOOO0OOOOO0OO000O ):#line:276
        try :#line:277
            OO0OO0O00OOOOO0OO ={'snatch_id':OOOO0OOOOO0OO000O }#line:278
            OOOOO0O00000OOO00 =requests .request ('post',f'{host}/api/Snatch/PlayIndex',headers =OOOOO00OO0O00O000 .headers ,data =OO0OO0O00OOOOO0OO ).json ()#line:279
            if 'code'in OOOOO0O00000OOO00 :#line:281
                if OOOOO0O00000OOO00 ['code']==1 :#line:282
                    O0OO0OOOO00O0OO0O =OOOOO0O00000OOO00 ['data']['surplus_figure_nub']#line:283
                    if O0OO0OOOO00O0OO0O >0 :#line:284
                        OOOOO00OO0O00O000 .snatch_play (OOOO0OOOOO0OO000O )#line:285
        except Exception as OOO00OO0O0000O000 :#line:286
            print (OOO00OO0O0000O000 )#line:287
    def snatch_play (OOOO00OO00OOO00OO ,O00000OO0OOOO0000 ):#line:290
        try :#line:291
            OO0O0O0OOO00OOOO0 ={'snatch_id':O00000OO0OOOO0000 ,'nub':'1'}#line:292
            OO0O0O0000OO000O0 =requests .request ('post',f'{host}/api/Snatch/play',headers =OOOO00OO00OOO00OO .headers ,data =OO0O0O0OOO00OOOO0 ).json ()#line:293
            if 'code'in OO0O0O0000OO000O0 :#line:295
                if OO0O0O0000OO000O0 ['code']==1 :#line:296
                    print (f'【参与夺宝】:{OO0O0O0000OO000O0["msg"]}')#line:297
        except Exception as OO0000OOOOOO0OO00 :#line:298
            print (OO0000OOOOOO0OO00 )#line:299
    def snatch_record (OOO0O0O0OO0OO0O0O ):#line:302
        try :#line:303
            OOO0OO0000O0OOOO0 =requests .request ('post',f'{host}/api/Snatch/record',headers =OOO0O0O0OO0OO0O0O .headers ).json ()#line:304
            if 'code'in OOO0OO0000O0OOOO0 :#line:306
                if OOO0OO0000O0OOOO0 ['code']==1 :#line:307
                    O00O0OOO000O0O0O0 =OOO0OO0000O0OOOO0 ['data']['record_list']#line:308
                    if O00O0OOO000O0O0O0 :#line:309
                        for O00OO000OO0O0000O in O00O0OOO000O0O0O0 :#line:310
                            print (f'【夺宝记录】:{O00OO000OO0O0000O["name"]}丨收益:{O00OO000OO0O0000O["award_money"]}丨{O00OO000OO0O0000O["state"]}')#line:312
        except Exception as O0OOOOOO00OO0000O :#line:313
            print (O0OOOOOO00OO0000O )#line:314
def start ():#line:318
    try :#line:319
        update_the_validation ()#line:320
        O00000O0O0OOO0OOO =os_qinglong ()#line:321
        print (f"==========共找到{len(O00000O0O0OOO0OOO)}个账号==========")#line:322
        for O0OOOO00OO000OO00 in O00000O0O0OOO0OOO :#line:323
            print (f"------------正在执行第{O00000O0O0OOO0OOO.index(O0OOOO00OO000OO00) + 1}个账号------------")#line:324
            OOOO0O0O00O00OO00 =Template (O0OOOO00OO000OO00 )#line:325
            if OOOO0O0O00O00OO00 .base_info ():#line:327
                OOOO0O0O00O00OO00 .LuckyBox ()#line:329
                OOOO0O0O00O00OO00 .playInfo ()#line:331
                OOOO0O0O00O00OO00 .snatch ()#line:333
                OOOO0O0O00O00OO00 .snatch_record ()#line:335
                if score_record :#line:337
                    OOOO0O0O00O00OO00 .score_record ()#line:339
                OOOO0O0O00O00OO00 .score_present ()#line:341
                time .sleep (random .randint (2 ,5 ))#line:343
            else :#line:344
                print ('token失效')#line:345
        print ('\n开始打印可以抢宝箱的数据')#line:346
        for O0O0O0O0O0OO00O00 in sr :#line:347
            print (O0O0O0O0O0OO00O00 .strip ())#line:348
    except Exception as OO0OOOO0O0OOO0OO0 :#line:349
        print (OO0OOOO0O0OOO0OO0 )#line:350
def version_of_the_validation ():#line:352
    return str ((64 -56 )/10 )#line:353
if __name__ =='__main__':#line:356
    start ()#line:357
