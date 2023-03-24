# coding: utf-8
try:
    import requests, re, os, sys, time, random
except Exception as E:
    t = re.findall("d '(.*?)'", str(E))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: */15 0,8-23 * * *
@ new Env('千层塔会员版')
@ 千层会员版非会员不可用
@ 项目地址  https://qct.qitusky.cn/invite/?invite_code=1476
@ 抓取  https://qct.qitusky.cn 的ba-user-token值
@ 青龙变量 export qc_token="token&宝箱ID&赠送ID"   1普通宝箱 2白银宝箱 3黄金宝箱 4神秘宝箱 5炫彩宝箱  多号换行
@ 版本 1.0
"""
##################################配置区##################################
snatch = True              # 是否夺宝
score_record = False        # 赠送记录
score_big = '5'         # 大于5才赠送
##################################配置区##################################
##################################下面不要动##################################
sr =[]#line:1
score =0 #line:2
kkk =0 #line:3
_OO0OOO0O0000OO0OO =0 #line:4
versions ='1.1.9'#line:5
application ='qc_token'#line:6
token =''#line:7
host ='https://qct.qitusky.cn'#line:9
git ='https://gitee.com'#line:10
def os_qinglong ():#line:11
    if application in os .environ :#line:12
        O0O00OO0OOO000OO0 =os .environ [application ].split ('\n')#line:13
        if len (O0O00OO0OOO000OO0 )>0 :#line:14
            return O0O00OO0OOO000OO0 #line:15
        else :#line:16
            print (f"{application}变量未启用")#line:17
            print ('脚本退出')#line:18
            sys .exit (1 )#line:19
    else :#line:20
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:21
        return os_built ()#line:22
def os_built ():#line:25
    if token :#line:26
        O0OOO000O0OOO0O0O =token .split ('\n')#line:27
        if len (O0OOO000O0OOO0O0O )>0 :#line:28
            return O0OOO000O0OOO0O0O #line:29
    else :#line:30
        print (f"内置变量为空")#line:31
        print ('脚本结束')#line:32
        sys .exit (0 )#line:33
def gitee_validation ():#line:36
    try :#line:37
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:38
    except :#line:39
        sys .exit (0 )#line:40
def update_the_validation ():#line:44
    try :#line:45
        O00O0000O00OOO000 =gitee_validation ()#line:46
        if version_of_the_validation ()<O00O0000O00OOO000 ['Tower']['edition']:#line:47
            print (f'当前脚本名字: {O00O0000O00OOO000["Tower"]["text"]}')#line:48
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0000O00OOO000["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:49
            print (f'更新内容=>> {O00O0000O00OOO000["Tower"]["content"]}')#line:50
        else :#line:51
            print (f'当前脚本名字: {O00O0000O00OOO000["Tower"]["text"]}')#line:52
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0000O00OOO000["Tower"]["edition"]}   ✅')#line:53
            print (f'更新内容=>> {O00O0000O00OOO000["Tower"]["content"]}')#line:54
    except Exception as O0OOOO0OO0O0O0OO0 :#line:55
        print (O0OOOO0OO0O0O0OO0 )#line:56
class Template :#line:59
    def __init__ (O000OO0OO00OOOO0O ,OOOOOOOOOOOO00OOO ):#line:61
        try :#line:62
            O000OO0OO00OOOO0O .token =OOOOOOOOOOOO00OOO .split ('&')[0 ]#line:63
            O000OO0OO00OOOO0O .box =OOOOOOOOOOOO00OOO .split ('&')[1 ]#line:64
            O000OO0OO00OOOO0O .present_id =OOOOOOOOOOOO00OOO .split ('&')[2 ]#line:65
            O000OO0OO00OOOO0O .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':versions ,'accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':O000OO0OO00OOOO0O .token ,'server':'true','phone-type':'android',}#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (OO00000O00OOOO00O ):#line:82
        global score #line:83
        try :#line:84
            OOOOO0O00O0OO0OOO =requests .request ('post',f'{host}/api/User/info',headers =OO00000O00OOOO00O .headers ).json ()#line:85
            if 'code'in OOOOO0O00O0OO0OOO :#line:87
                if OOOOO0O00O0OO0OOO ['code']==1 :#line:88
                    OOO0O000OO000000O =OOOOO0O00O0OO0OOO ['data']['nickname']#line:89
                    O0O0OOO0OO00OOOOO =OOOOO0O00O0OO0OOO ['data']['id']#line:90
                    score =OOOOO0O00O0OO0OOO ['data']['score']#line:91
                    print (f'【账号信息】:昵称:{OOO0O000OO000000O[:6]}丨ID:{O0O0OOO0OO00OOOOO}丨金币:{str(score)[:5]}')#line:92
                if OOOOO0O00O0OO0OOO ['code']==302 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as OOO00OO0OO00O0OO0 :#line:96
            print (OOO00OO0OO00O0OO0 )#line:97
    def playInfo (O0OO000000OO000OO ):#line:100
        try :#line:101
            O0O00OO0OO0O0O000 =requests .request ('post',f'{host}/api/Game/playInfo',headers =O0OO000000OO000OO .headers ).json ()#line:102
            if 'code'in O0O00OO0OO0O0O000 :#line:104
                if O0O00OO0OO0O0O000 ['code']==1 :#line:105
                    O00000OO000O00OOO =O0O00OO0OO0O0O000 ['data']['play_tier']#line:106
                    OOO00O00OO0OO0000 =O0O00OO0OO0O0O000 ['data']['play_tier_need_money']#line:107
                    OO00O0O0OO0OO00OO =O0O00OO0OO0O0O000 ['data']['user_money']#line:108
                    OO000O0O0OOO00O0O =O0O00OO0OO0O0O000 ['data']['play_finish_money']#line:109
                    O0OOOO00O00OOOOO0 =O0O00OO0OO0O0O000 ['data']['surplus_play_nub']#line:110
                    print (f'【参与闯关】:层数:{O00000OO000O00OOO}丨剩余:{O0OOOO00O00OOOOO0}丨花费:{OOO00O00OO0OO0000}丨预计:{OO000O0O0OOO00O0O}')#line:111
                    if float (OOO00O00OO0OO0000 )<float (OO00O0O0OO0OO00OO ):#line:112
                        if O0OOOO00O00OOOOO0 >0 :#line:113
                            O0OO000000OO000OO .Game_index ('1')#line:114
                        else :#line:115
                            O0OO000000OO000OO .Game_index ('2')#line:116
                    else :#line:117
                        O0OO000000OO000OO .Game_index ('2')#line:118
        except Exception as O00OO0O000OO0O0OO :#line:120
            print (O00OO0O000OO0O0OO )#line:121
    def setAutoPlay (O00O0O0O00O00000O ):#line:124
        try :#line:125
            O00OO000000O0OOOO ={'state':'1'}#line:126
            OO00O0O00O000OOO0 =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O00O0O0O00O00000O .headers ,data =O00OO000000O0OOOO ).json ()#line:127
            if 'code'in OO00O0O00O000OOO0 :#line:129
                if OO00O0O00O000OOO0 ['code']==1 :#line:130
                    print (f'【自动闯关】:{OO00O0O00O000OOO0["msg"]}')#line:131
                if OO00O0O00O000OOO0 ['code']==0 :#line:132
                    print (f'【自动闯关】:{OO00O0O00O000OOO0["msg"]}')#line:133
        except Exception as OOOOO0O00OO00OO00 :#line:134
            print (OOOOO0O00OO00OO00 )#line:135
    def Game_index (O0OOOO0O00O0O000O ,O000OO0O0O0OOOOOO ):#line:138
        try :#line:139
            O000OO0000O00OO00 =requests .request ('post',f'{host}/api/Game/index',headers =O0OOOO0O00O0O000O .headers ).json ()#line:140
            if 'code'in O000OO0000O00OO00 :#line:142
                if O000OO0000O00OO00 ['code']==1 :#line:143
                    if O000OO0000O00OO00 ['data']['is_auto_play']:#line:144
                        OOO0O000O00000OO0 ='✅'#line:145
                    else :#line:146
                        OOO0O000O00000OO0 ='❌'#line:147
                    if O000OO0000O00OO00 ['data']['is_game_ing']:#line:149
                        OO000OO0000OO0OO0 ='✅'#line:150
                    else :#line:151
                        OO000OO0000OO0OO0 ='❌'#line:152
                    if O000OO0000O00OO00 ['data']['is_vip']:#line:153
                        OO0O00OOO0OOO0OO0 ='✅'#line:154
                    else :#line:155
                        OO0O00OOO0OOO0OO0 ='❌'#line:156
                    if '正在闯关'in O000OO0000O00OO00 ['data']['npc_hint']:#line:157
                        OO0OO0O0O00O0OOOO =O000OO0000O00OO00 ['data']['npc_hint'][:8 ]#line:158
                    else :#line:159
                        OO0OO0O0O00O0OOOO =O000OO0000O00OO00 ['data']['npc_hint'][:5 ]#line:160
                    print (f'【游戏状态】:自动:{OOO0O000O00000OO0}丨闯关:{OO000OO0000OO0OO0}丨VIP:{OO0O00OOO0OOO0OO0}丨{OO0OO0O0O00O0OOOO}')#line:161
                    if not O000OO0000O00OO00 ['data']['is_auto_play']:#line:162
                        if O000OO0O0O0OOOOOO =='1':#line:163
                            O0OOOO0O00O0O000O .setAutoPlay ()#line:164
        except Exception as OO00OOO0OO00OO00O :#line:165
            print (OO00OOO0OO00OO00O )#line:166
    def LuckyBox (OOO0O00O00O00O00O ):#line:170
        global sr #line:171
        try :#line:172
            OOO0O0000OOOOOOOO =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OOO0O00O00O00O00O .headers ).json ()#line:173
            if 'code'in OOO0O0000OOOOOOOO :#line:175
                if OOO0O0000OOOOOOOO ['code']==1 :#line:176
                    O00OO00O00O0O0000 =OOO0O0000OOOOOOOO ['data']['debris']#line:177
                    OO00000000O0O00OO =OOO0O0000OOOOOOOO ['data']['is_draw']#line:178
                    print (f'【幸运宝箱】:碎片:{str(O00OO00O00O0O0000).split(".")[0]}丨当前设置开启宝箱ID:{OOO0O00O00O00O00O.box}')#line:179
                    if not OO00000000O0O00OO :#line:180
                        OOO0O000OO0O0O0OO =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OOO0O00O00O00O00O .headers ).json ()#line:181
                        if 'code'in OOO0O000OO0O0O0OO :#line:183
                            if OOO0O000OO0O0O0OO ['code']==1 :#line:184
                                O0O0000O000O000O0 =OOO0O000OO0O0O0OO ['data']['nub']#line:185
                                print (f'【领取碎片】:获得:{O0O0000O000O000O0}')#line:186
                    for O00O000O0O00O00OO in OOO0O0000OOOOOOOO ['data']['box_list']:#line:187
                        OOOOO0O0OO000OO0O =O00O000O0O00O00OO ['id']#line:189
                        OO0O0O0OO0O00000O =O00O000O0O00O00OO ['name']#line:190
                        OOOO000OO0OOO0O00 =O00O000O0O00O00OO ['inventory']#line:191
                        O00OOOOO0O00O00OO =O00O000O0O00O00OO ['need_debris']#line:192
                        if float (OOOOO0O0OO000OO0O )==float (OOO0O00O00O00O00O .box ):#line:193
                            print (f'【幸运宝箱】:名称:{OO0O0O0OO0O00000O}丨需要碎片:{O00OOOOO0O00O00OO}丨剩余:{OOOO000OO0OOO0O00}')#line:194
                            if float (O00OO00O00O0O0000 )>=float (O00OOOOO0O00O00OO ):#line:195
                                sr .append (OOO0O00O00O00O00O .token +'&'+OOO0O00O00O00O00O .box )#line:196
                                if OOOO000OO0OOO0O00 >0 :#line:197
                                    OOO0OOOO0O000000O ={'id':OOO0O00O00O00O00O .box }#line:198
                                    O0OOOOO0OOO0O000O =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =OOO0O00O00O00O00O .headers ,data =OOO0OOOO0O000000O ).json ()#line:199
                                    if 'code'in O0OOOOO0OOO0O000O :#line:201
                                        if O0OOOOO0OOO0O000O ['code']==1 :#line:202
                                            print (f'【兑换宝箱】:{O0OOOOO0OOO0O000O["msg"]}丨获得{O0OOOOO0OOO0O000O["data"]["name"]}')#line:203
                                            OOO0O00O00O00O00O .LuckyBox ()#line:204
        except Exception as O0OOO00OO0OOOO0OO :#line:205
            OOO0O00O00O00O00O .LuckyBox ()#line:206
    def score_record (OO000OOOO0OOOOOOO ):#line:209
        try :#line:210
            O0OO000O00000OOO0 ={'page':'1','limit':'15','type':'2'}#line:211
            OOOOOO000OO0O00OO =requests .request ('post',f'{host}/api/Score/record',headers =OO000OOOO0OOOOOOO .headers ,data =O0OO000O00000OOO0 ).json ()#line:212
            if 'code'in OOOOOO000OO0O00OO :#line:214
                if OOOOOO000OO0O00OO ['code']==1 :#line:215
                    O000O00OO00O0OO0O =OOOOOO000OO0O00OO ['data']['record_list']#line:216
                    if O000O00OO00O0OO0O :#line:217
                        for O0OO0OO0O000O0000 in O000O00OO00O0OO0O :#line:218
                            O0000O0O0OOO00OOO =O0OO0OO0O000O0000 ['user_id']#line:219
                            O0OOO0O000OO00O0O =O0OO0OO0O000O0000 ['money']#line:220
                            O0O00OOOOO0OOOOO0 =O0OO0OO0O000O0000 ['create_time']#line:221
                            O00000O00O0000000 =O0OO0OO0O000O0000 ['nickname']#line:222
                            print (f'【赠送记录】:昵称:{O00000O00O0000000}丨ID:{O0000O0O0OOO00OOO}丨金额:{O0OOO0O000OO00O0O}丨时间:{O0O00OOOOO0OOOOO0[5:16]}')#line:223
        except Exception as O0000OO00O0O0O0OO :#line:224
            print (O0000OO00O0O0O0OO )#line:225
    def score_present (OO0O0OO0O000O00OO ):#line:229
        try :#line:230
            if float (score )>float (score_big ):#line:231
                OOOO00O0OOOOOOOOO ={'id':OO0O0OO0O000O00OO .present_id }#line:232
                OO0OOO000000O0OOO =requests .request ('post',f'{host}/api/Score/presentFindUser',headers =OO0O0OO0O000O00OO .headers ,data =OOOO00O0OOOOOOOOO ).json ()#line:233
                if 'code'in OO0OOO000000O0OOO :#line:235
                    if OO0OOO000000O0OOO ['code']==1 :#line:236
                        O00OOO000OOOOOO0O =OO0OOO000000O0OOO ['data']['service_charge']#line:237
                        O0OO00OOOOOO000OO =int (float (score )/(1 +(int (O00OOO000OOOOOO0O )/100 )))#line:238
                        if O0OO00OOOOOO000OO >1 :#line:239
                            O0O00000O0OOOOO0O ={'present_id':OO0O0OO0O000O00OO .present_id ,'present_nub':O0OO00OOOOOO000OO }#line:240
                            O0O0O0O0O0000OO0O =requests .request ('post',f'{host}/api/Score/present',headers =OO0O0OO0O000O00OO .headers ,data =O0O00000O0OOOOO0O ).json ()#line:241
                            if 'code'in O0O0O0O0O0000OO0O :#line:243
                                if O0O0O0O0O0000OO0O ['code']==1 :#line:244
                                    print (f'【赠送金币】:ID:{OO0O0OO0O000O00OO.present_id}丨金币:{O0OO00OOOOOO000OO}丨{O0O0O0O0O0000OO0O["msg"]}')#line:245
                                elif O0O0O0O0O0000OO0O ['code']==0 :#line:246
                                    print (f'【赠送金币】:ID:{OO0O0OO0O000O00OO.present_id}丨金币:{O0OO00OOOOOO000OO}丨{O0O0O0O0O0000OO0O["msg"]}')#line:247
                                else :#line:248
                                    print (O0O0O0O0O0000OO0O )#line:249
        except Exception as OO0000O0OOOOO0O0O :#line:250
            print (OO0000O0OOOOO0O0O )#line:251
    def figure (O00OOOO000O0OO000 ,OO0O00O00O0O00000 ):#line:254
        try :#line:255
            OO00OOO0O00O000O0 =requests .request ('post',f'{host}/api/figure/index',headers =O00OOOO000O0OO000 .headers ).json ()#line:256
            if 'code'in OO00OOO0O00O000O0 :#line:258
                if OO00OOO0O00O000O0 ['code']==1 :#line:259
                    for O00O00000000O0O00 in OO00OOO0O00O000O0 ['data']['user_figure_list']:#line:260
                        O00OOOOOOO000000O =O00O00000000O0O00 ['name']#line:261
                        if OO0O00O00O0O00000 ==O00OOOOOOO000000O :#line:262
                            return True #line:263
            return False #line:264
        except Exception as OOO0O00000O0OO00O :#line:265
            print (OOO0O00000O0OO00O )#line:266
    def snatch (OO0O0O0OOOO0OOO00 ):#line:269
        try :#line:270
            O0O0O0O0OOOOO00OO =requests .request ('post',f'{host}/api/Snatch/index',headers =OO0O0O0OOOO0OOO00 .headers ).json ()#line:271
            if 'code'in O0O0O0O0OOOOO00OO :#line:273
                if O0O0O0O0OOOOO00OO ['code']==1 :#line:274
                    OOO0OOO00O0000OO0 =O0O0O0O0OOOOO00OO ['data']['snatch_id']#line:275
                    OO0O000O000O00O00 =O0O0O0O0OOOOO00OO ['data']['figure_name']#line:276
                    O0000000O0OO00OO0 =O0O0O0O0OOOOO00OO ['data']['now_figure_nub']#line:277
                    OO0OOOO0OOOOO00OO =O0O0O0O0OOOOO00OO ['data']['max_figure_nub']#line:278
                    if O0000000O0OO00OO0 <OO0OOOO0OOOOO00OO :#line:279
                        if OO0O0O0OOOO0OOO00 .figure (OO0O000O000O00O00 ):#line:280
                            OO0O0O0OOOO0OOO00 .snatch_play_index (OOO0OOO00O0000OO0 )#line:281
        except Exception as O0OO00OOOOO000000 :#line:282
            print (O0OO00OOOOO000000 )#line:283
    def snatch_play_index (O00O0OO0OO0000O0O ,O00O0O0000OO0O00O ):#line:286
        try :#line:287
            OO0O0O0O0OO00OO00 ={'snatch_id':O00O0O0000OO0O00O }#line:288
            OOOO00OOOO0OOOOO0 =requests .request ('post',f'{host}/api/Snatch/PlayIndex',headers =O00O0OO0OO0000O0O .headers ,data =OO0O0O0O0OO00OO00 ).json ()#line:289
            if 'code'in OOOO00OOOO0OOOOO0 :#line:291
                if OOOO00OOOO0OOOOO0 ['code']==1 :#line:292
                    O000000O0O00OO0OO =OOOO00OOOO0OOOOO0 ['data']['surplus_figure_nub']#line:293
                    if O000000O0O00OO0OO >0 :#line:294
                        O00O0OO0OO0000O0O .snatch_play (O00O0O0000OO0O00O )#line:295
        except Exception as O0O00OOOOOOOOO0OO :#line:296
            print (O0O00OOOOOOOOO0OO )#line:297
    def snatch_play (OO00OO00OO0OO0O0O ,OOOO00OOO0OOOOO0O ):#line:300
        try :#line:301
            O0O0000OOO0OOOO00 ={'snatch_id':OOOO00OOO0OOOOO0O ,'nub':'1'}#line:302
            O0000O00O00O0OO00 =requests .request ('post',f'{host}/api/Snatch/play',headers =OO00OO00OO0OO0O0O .headers ,data =O0O0000OOO0OOOO00 ).json ()#line:303
            if 'code'in O0000O00O00O0OO00 :#line:305
                if O0000O00O00O0OO00 ['code']==1 :#line:306
                    print (f'【参与夺宝】:{O0000O00O00O0OO00["msg"]}')#line:307
        except Exception as O0OOO00000OOO0OOO :#line:308
            print (O0OOO00000OOO0OOO )#line:309
    def snatch_record (OOO0000OO0OOOO0OO ):#line:312
        global kkk #line:313
        try :#line:314
            O000OOO00O00O0OOO =requests .request ('post',f'{host}/api/Snatch/record',headers =OOO0000OO0OOOO0OO .headers ).json ()#line:315
            if 'code'in O000OOO00O00O0OOO :#line:317
                if O000OOO00O00O0OOO ['code']==1 :#line:318
                    O000O00000OO00OO0 =O000OOO00O00O0OOO ['data']['record_list']#line:319
                    if O000O00000OO00OO0 :#line:320
                        for OO00OO00OO00O0O0O in O000O00000OO00OO0 :#line:321
                            kkk +=float (OO00OO00OO00O0O0O ["award_money"])#line:323
                            print (f'【夺宝记录】:{OO00OO00OO00O0O0O["name"]}丨收益:{OO00OO00OO00O0O0O["award_money"]}丨{OO00OO00OO00O0O0O["state"]}')#line:324
        except Exception as OOO000O00000OOOO0 :#line:325
            print (OOO000O00000OOOO0 )#line:326
    def withdrawal (OO0OO00O0OOO00OO0 ):#line:330
        global _OO0OOO0O0000OO0OO #line:331
        try :#line:332
            OO00OOO00000O00OO =requests .request ('post',f'{host}/api/Withdrawal/index',headers =OO0OO00O0OOO00OO0 .headers ).json ()#line:333
            if 'code'in OO00OOO00000O00OO :#line:335
                if OO00OOO00000O00OO ['code']==1 :#line:336
                    O00O00OOO000O0O00 =OO00OOO00000O00OO ['data']['user_money']#line:337
                    _OO0OOO0O0000OO0OO +=float (O00O00OOO000O0O00 )#line:338
        except Exception as O00O0O00000OO0000 :#line:340
            print (O00O0O00000OO0000 )#line:341
def start ():#line:346
    try :#line:347
        update_the_validation ()#line:348
        O00000OOOOOO00OOO =os_qinglong ()#line:349
        print (f"==========共找到{len(O00000OOOOOO00OOO)}个账号==========")#line:350
        for O0OO00OOO0OO0OO00 in O00000OOOOOO00OOO :#line:351
            print (f"------------正在执行第{O00000OOOOOO00OOO.index(O0OO00OOO0OO0OO00) + 1}个账号------------")#line:352
            OO0OOOO00O000OOO0 =Template (O0OO00OOO0OO0OO00 )#line:353
            if OO0OOOO00O000OOO0 .base_info ():#line:355
                OO0OOOO00O000OOO0 .LuckyBox ()#line:357
                OO0OOOO00O000OOO0 .playInfo ()#line:359
                if snatch :#line:360
                    OO0OOOO00O000OOO0 .snatch ()#line:362
                OO0OOOO00O000OOO0 .snatch_record ()#line:364
                if score_record :#line:366
                    OO0OOOO00O000OOO0 .score_record ()#line:368
                OO0OOOO00O000OOO0 .withdrawal ()#line:370
                OO0OOOO00O000OOO0 .score_present ()#line:372
                time .sleep (random .randint (1 ,2 ))#line:374
            else :#line:375
                print ('token失效')#line:376
        print (f'夺宝共获取金币:{kkk}')#line:377
        print (f'共损失现金:{_OO0OOO0O0000OO0OO}')#line:378
        print ('\n开始打印可以抢宝箱的数据')#line:379
        for OO0O0O0O00OOO0O0O in sr :#line:380
            print (OO0O0O0O00OOO0O0O .strip ())#line:381
    except Exception as OO0O000OO0OOOO000 :#line:382
        print (OO0O000OO0OOOO000 )#line:383
def version_of_the_validation ():#line:385
    return str ((66 -56 )/10 )#line:386
if __name__ =='__main__':#line:389
    start ()#line:390
