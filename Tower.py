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
@ 版本 0.9
"""
##################################配置区##################################
score_record = False        # 赠送记录
score_big = '5'         # 大于5才赠送
##################################配置区##################################
##################################下面不要动##################################
sr = []
score = 0
kkk = 0
versions = '1.1.9'           # 版本
application = 'qc_token'  # 变量名
token = ''  #
##################################下面不要动##################################
host ='https://qct.qitusky.cn'#line:1
git ='https://gitee.com'#line:2
def os_qinglong ():#line:3
    if application in os .environ :#line:4
        O0O000O0000OOO0OO =os .environ [application ].split ('\n')#line:5
        if len (O0O000O0000OOO0OO )>0 :#line:6
            return O0O000O0000OOO0OO #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        OOOOOOO0OOOO0000O =token .split ('\n')#line:19
        if len (OOOOOOO0OOOO0000O )>0 :#line:20
            return OOOOOOO0OOOO0000O #line:21
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
        OOOO00O000000O00O =gitee_validation ()#line:38
        if version_of_the_validation ()<OOOO00O000000O00O ['Tower']['edition']:#line:39
            print (f'当前脚本名字: {OOOO00O000000O00O["Tower"]["text"]}')#line:40
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO00O000000O00O["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:41
            print (f'更新内容=>> {OOOO00O000000O00O["Tower"]["content"]}')#line:42
        else :#line:43
            print (f'当前脚本名字: {OOOO00O000000O00O["Tower"]["text"]}')#line:44
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO00O000000O00O["Tower"]["edition"]}   ✅')#line:45
            print (f'更新内容=>> {OOOO00O000000O00O["Tower"]["content"]}')#line:46
    except Exception as OO0OOO00O0OO000O0 :#line:47
        print (OO0OOO00O0OO000O0 )#line:48
class Template :#line:51
    def __init__ (O0OOO00OO00OO000O ,O0O0O00O0O00OO0O0 ):#line:53
        try :#line:54
            O0OOO00OO00OO000O .token =O0O0O00O0O00OO0O0 .split ('&')[0 ]#line:55
            O0OOO00OO00OO000O .box =O0O0O00O0O00OO0O0 .split ('&')[1 ]#line:56
            O0OOO00OO00OO000O .present_id =O0O0O00O0O00OO0O0 .split ('&')[2 ]#line:57
            O0OOO00OO00OO000O .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':versions ,'accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':O0OOO00OO00OO000O .token ,'server':'true','phone-type':'android',}#line:69
        except :#line:70
            print ('变量格式错误')#line:71
    def base_info (O0OO0O00OOO00OO00 ):#line:74
        global score #line:75
        try :#line:76
            OOO0O0000000OO0OO =requests .request ('post',f'{host}/api/User/info',headers =O0OO0O00OOO00OO00 .headers ).json ()#line:77
            if 'code'in OOO0O0000000OO0OO :#line:79
                if OOO0O0000000OO0OO ['code']==1 :#line:80
                    OOOO000O00O00O000 =OOO0O0000000OO0OO ['data']['nickname']#line:81
                    OO00O0OO0O0OOO00O =OOO0O0000000OO0OO ['data']['id']#line:82
                    score =OOO0O0000000OO0OO ['data']['score']#line:83
                    print (f'【账号信息】:昵称:{OOOO000O00O00O000[:6]}丨ID:{OO00O0OO0O0OOO00O}丨金币:{str(score)[:5]}')#line:84
                if OOO0O0000000OO0OO ['code']==302 :#line:85
                    return False #line:86
            return True #line:87
        except Exception as OOO000O00OOOOOOO0 :#line:88
            print (OOO000O00OOOOOOO0 )#line:89
    def playInfo (OOOOO00O0O0O0O000 ):#line:92
        try :#line:93
            O0OO0OO00OO00O0OO =requests .request ('post',f'{host}/api/Game/playInfo',headers =OOOOO00O0O0O0O000 .headers ).json ()#line:94
            if 'code'in O0OO0OO00OO00O0OO :#line:96
                if O0OO0OO00OO00O0OO ['code']==1 :#line:97
                    O0OOOOOO0O0O0O0O0 =O0OO0OO00OO00O0OO ['data']['play_tier']#line:98
                    O0OO0O00O00O0OOO0 =O0OO0OO00OO00O0OO ['data']['play_tier_need_money']#line:99
                    O000OO00O0O0OO0O0 =O0OO0OO00OO00O0OO ['data']['user_money']#line:100
                    OOO0O0OOOOOO0O000 =O0OO0OO00OO00O0OO ['data']['play_finish_money']#line:101
                    O000000O0O00OO0OO =O0OO0OO00OO00O0OO ['data']['surplus_play_nub']#line:102
                    print (f'【参与闯关】:层数:{O0OOOOOO0O0O0O0O0}丨剩余:{O000000O0O00OO0OO}丨花费:{O0OO0O00O00O0OOO0}丨预计:{OOO0O0OOOOOO0O000}')#line:103
                    if float (O0OO0O00O00O0OOO0 )<float (O000OO00O0O0OO0O0 ):#line:104
                        if O000000O0O00OO0OO >0 :#line:105
                            OOOOO00O0O0O0O000 .Game_index ('1')#line:106
                        else :#line:107
                            OOOOO00O0O0O0O000 .Game_index ('2')#line:108
                    else :#line:109
                        OOOOO00O0O0O0O000 .Game_index ('2')#line:110
        except Exception as OO0O0O00O0O00O000 :#line:112
            print (OO0O0O00O0O00O000 )#line:113
    def setAutoPlay (O00OOOOOO0OO0OO00 ):#line:116
        try :#line:117
            O0OO0OOOOOOOOO000 ={'state':'1'}#line:118
            O0OOO0O0O0000OO00 =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O00OOOOOO0OO0OO00 .headers ,data =O0OO0OOOOOOOOO000 ).json ()#line:119
            if 'code'in O0OOO0O0O0000OO00 :#line:121
                if O0OOO0O0O0000OO00 ['code']==1 :#line:122
                    print (f'【自动闯关】:{O0OOO0O0O0000OO00["msg"]}')#line:123
                if O0OOO0O0O0000OO00 ['code']==0 :#line:124
                    print (f'【自动闯关】:{O0OOO0O0O0000OO00["msg"]}')#line:125
        except Exception as O0OO00O000O000O00 :#line:126
            print (O0OO00O000O000O00 )#line:127
    def Game_index (O0OO000O0000OOOO0 ,OO00OO000O0O00O0O ):#line:130
        try :#line:131
            O0O00OO00O0O0OOOO =requests .request ('post',f'{host}/api/Game/index',headers =O0OO000O0000OOOO0 .headers ).json ()#line:132
            if 'code'in O0O00OO00O0O0OOOO :#line:134
                if O0O00OO00O0O0OOOO ['code']==1 :#line:135
                    if O0O00OO00O0O0OOOO ['data']['is_auto_play']:#line:136
                        OOOOOO00O000O0000 ='✅'#line:137
                    else :#line:138
                        OOOOOO00O000O0000 ='❌'#line:139
                    if O0O00OO00O0O0OOOO ['data']['is_game_ing']:#line:141
                        OOOOOOO0O0000OOO0 ='✅'#line:142
                    else :#line:143
                        OOOOOOO0O0000OOO0 ='❌'#line:144
                    if O0O00OO00O0O0OOOO ['data']['is_vip']:#line:145
                        O0000O0O0000OOO00 ='✅'#line:146
                    else :#line:147
                        O0000O0O0000OOO00 ='❌'#line:148
                    if '正在闯关'in O0O00OO00O0O0OOOO ['data']['npc_hint']:#line:149
                        O0O00O000OOO0O00O =O0O00OO00O0O0OOOO ['data']['npc_hint'][:8 ]#line:150
                    else :#line:151
                        O0O00O000OOO0O00O =O0O00OO00O0O0OOOO ['data']['npc_hint'][:5 ]#line:152
                    print (f'【游戏状态】:自动:{OOOOOO00O000O0000}丨闯关:{OOOOOOO0O0000OOO0}丨VIP:{O0000O0O0000OOO00}丨{O0O00O000OOO0O00O}')#line:153
                    if not O0O00OO00O0O0OOOO ['data']['is_auto_play']:#line:154
                        if OO00OO000O0O00O0O =='1':#line:155
                            O0OO000O0000OOOO0 .setAutoPlay ()#line:156
        except Exception as O000OO0O0O0O0O000 :#line:157
            print (O000OO0O0O0O0O000 )#line:158
    def LuckyBox (OOOOO0OO000000OO0 ):#line:162
        global sr #line:163
        try :#line:164
            O000O00O0OOOO0000 =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OOOOO0OO000000OO0 .headers ).json ()#line:165
            if 'code'in O000O00O0OOOO0000 :#line:167
                if O000O00O0OOOO0000 ['code']==1 :#line:168
                    O0O0O0O00O0OOOOOO =O000O00O0OOOO0000 ['data']['debris']#line:169
                    OO0O0OOOO0O0O0000 =O000O00O0OOOO0000 ['data']['is_draw']#line:170
                    print (f'【幸运宝箱】:碎片:{str(O0O0O0O00O0OOOOOO).split(".")[0]}丨当前设置开启宝箱ID:{OOOOO0OO000000OO0.box}')#line:171
                    if not OO0O0OOOO0O0O0000 :#line:172
                        OO00O0O0O0000O000 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OOOOO0OO000000OO0 .headers ).json ()#line:173
                        if 'code'in OO00O0O0O0000O000 :#line:175
                            if OO00O0O0O0000O000 ['code']==1 :#line:176
                                O0O0OOO0O0OOO0OOO =OO00O0O0O0000O000 ['data']['nub']#line:177
                                print (f'【领取碎片】:获得:{O0O0OOO0O0OOO0OOO}')#line:178
                    for OO00O0OOOO0OOO000 in O000O00O0OOOO0000 ['data']['box_list']:#line:179
                        OOO0OO0O0OOO0OOO0 =OO00O0OOOO0OOO000 ['id']#line:181
                        O0O0000OOOOOOO00O =OO00O0OOOO0OOO000 ['name']#line:182
                        O000OO0O000O000OO =OO00O0OOOO0OOO000 ['inventory']#line:183
                        OOOOOO00O0000O00O =OO00O0OOOO0OOO000 ['need_debris']#line:184
                        if float (OOO0OO0O0OOO0OOO0 )==float (OOOOO0OO000000OO0 .box ):#line:185
                            print (f'【幸运宝箱】:名称:{O0O0000OOOOOOO00O}丨需要碎片:{OOOOOO00O0000O00O}丨剩余:{O000OO0O000O000OO}')#line:186
                            if float (O0O0O0O00O0OOOOOO )>=float (OOOOOO00O0000O00O ):#line:187
                                sr .append (OOOOO0OO000000OO0 .token +'&'+OOOOO0OO000000OO0 .box )#line:188
                                if O000OO0O000O000OO >0 :#line:189
                                    OO000O0O0OOO0OOOO ={'id':OOOOO0OO000000OO0 .box }#line:190
                                    OOO0O00O00OO0O00O =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =OOOOO0OO000000OO0 .headers ,data =OO000O0O0OOO0OOOO ).json ()#line:191
                                    if 'code'in OOO0O00O00OO0O00O :#line:193
                                        if OOO0O00O00OO0O00O ['code']==1 :#line:194
                                            print (f'【兑换宝箱】:{OOO0O00O00OO0O00O["msg"]}丨获得{OOO0O00O00OO0O00O["data"]["name"]}')#line:195
                                            OOOOO0OO000000OO0 .LuckyBox ()#line:196
        except Exception as OOOO00O00OOO0OO0O :#line:197
            OOOOO0OO000000OO0 .LuckyBox ()#line:198
    def score_record (O0O0OO00O0OO000O0 ):#line:201
        try :#line:202
            O00000OOOO00O0O0O ={'page':'1','limit':'15','type':'2'}#line:203
            O00O00OOO0OO000OO =requests .request ('post',f'{host}/api/Score/record',headers =O0O0OO00O0OO000O0 .headers ,data =O00000OOOO00O0O0O ).json ()#line:204
            if 'code'in O00O00OOO0OO000OO :#line:206
                if O00O00OOO0OO000OO ['code']==1 :#line:207
                    O00OO0OO0O00OOO0O =O00O00OOO0OO000OO ['data']['record_list']#line:208
                    if O00OO0OO0O00OOO0O :#line:209
                        for O0O0OOO0000O0O000 in O00OO0OO0O00OOO0O :#line:210
                            OOOOO00OOOOO0OO0O =O0O0OOO0000O0O000 ['user_id']#line:211
                            O000O0OOOOO0O0000 =O0O0OOO0000O0O000 ['money']#line:212
                            OOO0OO0O0O0OOOOOO =O0O0OOO0000O0O000 ['create_time']#line:213
                            O00O0O000OO000OOO =O0O0OOO0000O0O000 ['nickname']#line:214
                            print (f'【赠送记录】:昵称:{O00O0O000OO000OOO}丨ID:{OOOOO00OOOOO0OO0O}丨金额:{O000O0OOOOO0O0000}丨时间:{OOO0OO0O0O0OOOOOO[5:16]}')#line:215
        except Exception as OOOO0O00OO00O0O00 :#line:216
            print (OOOO0O00OO00O0O00 )#line:217
    def score_present (O0O0O00O0OOO0OO0O ):#line:221
        try :#line:222
            if float (score )>float (score_big ):#line:223
                O0OOO00O0O0OO0OOO ={'id':O0O0O00O0OOO0OO0O .present_id }#line:224
                OO000OOO0OO0O0000 =requests .request ('post',f'{host}/api/Score/presentFindUser',headers =O0O0O00O0OOO0OO0O .headers ,data =O0OOO00O0O0OO0OOO ).json ()#line:225
                if 'code'in OO000OOO0OO0O0000 :#line:227
                    if OO000OOO0OO0O0000 ['code']==1 :#line:228
                        O0OO0OO0OO0O0O000 =OO000OOO0OO0O0000 ['data']['service_charge']#line:229
                        OO00OO0O0OOOO0000 =int (float (score )/(1 +(int (O0OO0OO0OO0O0O000 )/100 )))#line:230
                        if OO00OO0O0OOOO0000 >1 :#line:231
                            OOO0OO0O0O0O0O0OO ={'present_id':O0O0O00O0OOO0OO0O .present_id ,'present_nub':OO00OO0O0OOOO0000 }#line:232
                            OOOO0O0OO000O0000 =requests .request ('post',f'{host}/api/Score/present',headers =O0O0O00O0OOO0OO0O .headers ,data =OOO0OO0O0O0O0O0OO ).json ()#line:233
                            if 'code'in OOOO0O0OO000O0000 :#line:235
                                if OOOO0O0OO000O0000 ['code']==1 :#line:236
                                    print (f'【赠送金币】:ID:{O0O0O00O0OOO0OO0O.present_id}丨金币:{OO00OO0O0OOOO0000}丨{OOOO0O0OO000O0000["msg"]}')#line:237
                                elif OOOO0O0OO000O0000 ['code']==0 :#line:238
                                    print (f'【赠送金币】:ID:{O0O0O00O0OOO0OO0O.present_id}丨金币:{OO00OO0O0OOOO0000}丨{OOOO0O0OO000O0000["msg"]}')#line:239
                                else :#line:240
                                    print (OOOO0O0OO000O0000 )#line:241
        except Exception as OOOO0OOO0O000OOO0 :#line:242
            print (OOOO0OOO0O000OOO0 )#line:243
    def figure (O00OO00O000OOOOOO ,O0OO00OO0O00O000O ):#line:246
        try :#line:247
            OO0O0O00O0OO0OO0O =requests .request ('post',f'{host}/api/figure/index',headers =O00OO00O000OOOOOO .headers ).json ()#line:248
            if 'code'in OO0O0O00O0OO0OO0O :#line:250
                if OO0O0O00O0OO0OO0O ['code']==1 :#line:251
                    for OO0O0OOO0OOOO0O00 in OO0O0O00O0OO0OO0O ['data']['user_figure_list']:#line:252
                        O00OOOO00O00O0O0O =OO0O0OOO0OOOO0O00 ['name']#line:253
                        if O0OO00OO0O00O000O ==O00OOOO00O00O0O0O :#line:254
                            return True #line:255
            return False #line:256
        except Exception as OOOOOOOO0O000OO00 :#line:257
            print (OOOOOOOO0O000OO00 )#line:258
    def snatch (O00O0O0OOO00O00O0 ):#line:261
        try :#line:262
            OO000OOOOOOO000OO =requests .request ('post',f'{host}/api/Snatch/index',headers =O00O0O0OOO00O00O0 .headers ).json ()#line:263
            if 'code'in OO000OOOOOOO000OO :#line:265
                if OO000OOOOOOO000OO ['code']==1 :#line:266
                    O00OOOOOO00OO0000 =OO000OOOOOOO000OO ['data']['snatch_id']#line:267
                    O00O00O0O0OO0O0OO =OO000OOOOOOO000OO ['data']['figure_name']#line:268
                    O0OO0OOO00OO00OOO =OO000OOOOOOO000OO ['data']['now_figure_nub']#line:269
                    O0OO0OOOOO00OOOO0 =OO000OOOOOOO000OO ['data']['max_figure_nub']#line:270
                    if O0OO0OOO00OO00OOO <O0OO0OOOOO00OOOO0 :#line:271
                        if O00O0O0OOO00O00O0 .figure (O00O00O0O0OO0O0OO ):#line:272
                            O00O0O0OOO00O00O0 .snatch_play_index (O00OOOOOO00OO0000 )#line:273
        except Exception as O00O0000OOO0O0OO0 :#line:274
            print (O00O0000OOO0O0OO0 )#line:275
    def snatch_play_index (OOOOO000000O000O0 ,O00000O0O00000O00 ):#line:278
        try :#line:279
            OO0O0O000OOO0OOOO ={'snatch_id':O00000O0O00000O00 }#line:280
            OOOO00O00OO000000 =requests .request ('post',f'{host}/api/Snatch/PlayIndex',headers =OOOOO000000O000O0 .headers ,data =OO0O0O000OOO0OOOO ).json ()#line:281
            if 'code'in OOOO00O00OO000000 :#line:283
                if OOOO00O00OO000000 ['code']==1 :#line:284
                    O0OOOOOOO0O0O0000 =OOOO00O00OO000000 ['data']['surplus_figure_nub']#line:285
                    if O0OOOOOOO0O0O0000 >0 :#line:286
                        OOOOO000000O000O0 .snatch_play (O00000O0O00000O00 )#line:287
        except Exception as OOO000OOO00O00O0O :#line:288
            print (OOO000OOO00O00O0O )#line:289
    def snatch_play (O0O0O0OO00O00O0OO ,OO0O00O00000OOOO0 ):#line:292
        try :#line:293
            OO000O0OO00OOO00O ={'snatch_id':OO0O00O00000OOOO0 ,'nub':'1'}#line:294
            OO0OOOO0O00O0O000 =requests .request ('post',f'{host}/api/Snatch/play',headers =O0O0O0OO00O00O0OO .headers ,data =OO000O0OO00OOO00O ).json ()#line:295
            if 'code'in OO0OOOO0O00O0O000 :#line:297
                if OO0OOOO0O00O0O000 ['code']==1 :#line:298
                    print (f'【参与夺宝】:{OO0OOOO0O00O0O000["msg"]}')#line:299
        except Exception as O0OOO0OO0OO0OOOO0 :#line:300
            print (O0OOO0OO0OO0OOOO0 )#line:301
    def snatch_record (OO00O000OOOOOOOOO ):#line:304
        global kkk #line:305
        try :#line:306
            O0O0O00000OOO0000 =requests .request ('post',f'{host}/api/Snatch/record',headers =OO00O000OOOOOOOOO .headers ).json ()#line:307
            if 'code'in O0O0O00000OOO0000 :#line:309
                if O0O0O00000OOO0000 ['code']==1 :#line:310
                    OOO0O0OOO0000O000 =O0O0O00000OOO0000 ['data']['record_list']#line:311
                    if OOO0O0OOO0000O000 :#line:312
                        for OOOO0OOOOO0O0OOO0 in OOO0O0OOO0000O000 :#line:313
                            kkk +=float (OOOO0OOOOO0O0OOO0 ["award_money"])#line:315
                            print (f'【夺宝记录】:{OOOO0OOOOO0O0OOO0["name"]}丨收益:{OOOO0OOOOO0O0OOO0["award_money"]}丨{OOOO0OOOOO0O0OOO0["state"]}')#line:316
        except Exception as O0000OOO00OO0O0OO :#line:317
            print (O0000OOO00OO0O0OO )#line:318
def start ():#line:322
    try :#line:323
        update_the_validation ()#line:324
        O00OO000O000OOO0O =os_qinglong ()#line:325
        print (f"==========共找到{len(O00OO000O000OOO0O)}个账号==========")#line:326
        for OO00OO00O0O00O00O in O00OO000O000OOO0O :#line:327
            print (f"------------正在执行第{O00OO000O000OOO0O.index(OO00OO00O0O00O00O) + 1}个账号------------")#line:328
            O0O0OO0O0O0000000 =Template (OO00OO00O0O00O00O )#line:329
            if O0O0OO0O0O0000000 .base_info ():#line:331
                O0O0OO0O0O0000000 .LuckyBox ()#line:333
                O0O0OO0O0O0000000 .playInfo ()#line:335
                O0O0OO0O0O0000000 .snatch ()#line:337
                O0O0OO0O0O0000000 .snatch_record ()#line:339
                if score_record :#line:341
                    O0O0OO0O0O0000000 .score_record ()#line:343
                O0O0OO0O0O0000000 .score_present ()#line:345
                time .sleep (random .randint (1 ,2 ))#line:347
            else :#line:348
                print ('token失效')#line:349
        print (f'夺宝共获取金币:{kkk}')#line:350
        print ('\n开始打印可以抢宝箱的数据')#line:351
        for O00OO0O0000000000 in sr :#line:352
            print (O00OO0O0000000000 .strip ())#line:353
    except Exception as O000OO0O000O0OO00 :#line:354
        print (O000OO0O000O0OO00 )#line:355
def version_of_the_validation ():#line:357
    return str ((65 -56 )/10 )#line:358
if __name__ =='__main__':#line:361
    start ()#line:362

