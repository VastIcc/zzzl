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
versions ='1.1.9'#line:4
application ='qc_token'#line:5
token =''''''#line:6
host ='https://qct.qitusky.cn'#line:8
git ='https://gitee.com'#line:9
def os_qinglong ():#line:10
    if application in os .environ :#line:11
        O00O00OOO000OO0OO =os .environ [application ].split ('\n')#line:12
        if len (O00O00OOO000OO0OO )>0 :#line:13
            return O00O00OOO000OO0OO #line:14
        else :#line:15
            print (f"{application}变量未启用")#line:16
            print ('脚本退出')#line:17
            sys .exit (1 )#line:18
    else :#line:19
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:20
        return os_built ()#line:21
def os_built ():#line:24
    if token :#line:25
        OOOO0OOOOO0O000OO =token .split ('\n')#line:26
        if len (OOOO0OOOOO0O000OO )>0 :#line:27
            return OOOO0OOOOO0O000OO #line:28
    else :#line:29
        print (f"内置变量为空")#line:30
        print ('脚本结束')#line:31
        sys .exit (0 )#line:32
def gitee_validation ():#line:35
    try :#line:36
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:37
    except :#line:38
        sys .exit (0 )#line:39
def update_the_validation ():#line:43
    try :#line:44
        O000O00000OO00O00 =gitee_validation ()#line:45
        if version_of_the_validation ()<O000O00000OO00O00 ['Tower']['edition']:#line:46
            print (f'当前脚本名字: {O000O00000OO00O00["Tower"]["text"]}')#line:47
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000O00000OO00O00["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:48
            print (f'更新内容=>> {O000O00000OO00O00["Tower"]["content"]}')#line:49
        else :#line:50
            print (f'当前脚本名字: {O000O00000OO00O00["Tower"]["text"]}')#line:51
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000O00000OO00O00["Tower"]["edition"]}   ✅')#line:52
            print (f'更新内容=>> {O000O00000OO00O00["Tower"]["content"]}')#line:53
    except Exception as O0O00OO00OO00OO0O :#line:54
        print (O0O00OO00OO00OO0O )#line:55
class Template :#line:58
    def __init__ (OO00O0O0OO0OO0OO0 ,O00000O0OOO0OO0OO ):#line:60
        try :#line:61
            OO00O0O0OO0OO0OO0 .token =O00000O0OOO0OO0OO .split ('&')[0 ]#line:62
            OO00O0O0OO0OO0OO0 .box =O00000O0OOO0OO0OO .split ('&')[1 ]#line:63
            OO00O0O0OO0OO0OO0 .present_id =O00000O0OOO0OO0OO .split ('&')[2 ]#line:64
            OO00O0O0OO0OO0OO0 .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':versions ,'accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OO00O0O0OO0OO0OO0 .token ,'server':'true','phone-type':'android',}#line:76
        except :#line:77
            print ('变量格式错误')#line:78
    def base_info (O0OO00O0O00OO0O0O ):#line:81
        global score #line:82
        try :#line:83
            O0000OOOOO0OOO0O0 =requests .request ('post',f'{host}/api/User/info',headers =O0OO00O0O00OO0O0O .headers ).json ()#line:84
            if 'code'in O0000OOOOO0OOO0O0 :#line:86
                if O0000OOOOO0OOO0O0 ['code']==1 :#line:87
                    O000OO00OOO00OO0O =O0000OOOOO0OOO0O0 ['data']['nickname']#line:88
                    OOO0O00O00000O00O =O0000OOOOO0OOO0O0 ['data']['id']#line:89
                    score =O0000OOOOO0OOO0O0 ['data']['score']#line:90
                    print (f'【账号信息】:昵称:{O000OO00OOO00OO0O[:6]}丨ID:{OOO0O00O00000O00O}丨金币:{str(score)[:5]}')#line:91
                if O0000OOOOO0OOO0O0 ['code']==302 :#line:92
                    return False #line:93
            return True #line:94
        except Exception as O00O0O0OO00OO0O00 :#line:95
            print (O00O0O0OO00OO0O00 )#line:96
    def playInfo (O00OOO0OOOO0000OO ):#line:99
        try :#line:100
            O00O00O0OO00O0O00 =requests .request ('post',f'{host}/api/Game/playInfo',headers =O00OOO0OOOO0000OO .headers ).json ()#line:101
            if 'code'in O00O00O0OO00O0O00 :#line:103
                if O00O00O0OO00O0O00 ['code']==1 :#line:104
                    OO0OOOO0O000O00OO =O00O00O0OO00O0O00 ['data']['play_tier']#line:105
                    O0000O0O0O0O0OO00 =O00O00O0OO00O0O00 ['data']['play_tier_need_money']#line:106
                    OOO0OO00OO0OO0OO0 =O00O00O0OO00O0O00 ['data']['user_money']#line:107
                    OO00O000OOOO00O0O =O00O00O0OO00O0O00 ['data']['play_finish_money']#line:108
                    O0000OOO000000000 =O00O00O0OO00O0O00 ['data']['surplus_play_nub']#line:109
                    print (f'【参与闯关】:层数:{OO0OOOO0O000O00OO}丨剩余:{O0000OOO000000000}丨花费:{O0000O0O0O0O0OO00}丨预计:{OO00O000OOOO00O0O}')#line:110
                    if float (O0000O0O0O0O0OO00 )<float (OOO0OO00OO0OO0OO0 ):#line:111
                        if O0000OOO000000000 >0 :#line:112
                            O00OOO0OOOO0000OO .Game_index ('1')#line:113
                        else :#line:114
                            O00OOO0OOOO0000OO .Game_index ('2')#line:115
                    else :#line:116
                        O00OOO0OOOO0000OO .Game_index ('2')#line:117
        except Exception as OO00OOO0000OO00OO :#line:119
            print (OO00OOO0000OO00OO )#line:120
    def setAutoPlay (OOOO0OOOO0OOO0O00 ):#line:123
        try :#line:124
            OO000O0OO0OOO0000 ={'state':'1'}#line:125
            O0000O00O00O000OO =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =OOOO0OOOO0OOO0O00 .headers ,data =OO000O0OO0OOO0000 ).json ()#line:126
            if 'code'in O0000O00O00O000OO :#line:128
                if O0000O00O00O000OO ['code']==1 :#line:129
                    print (f'【自动闯关】:{O0000O00O00O000OO["msg"]}')#line:130
                if O0000O00O00O000OO ['code']==0 :#line:131
                    print (f'【自动闯关】:{O0000O00O00O000OO["msg"]}')#line:132
        except Exception as O0O00O0OOO00OOO0O :#line:133
            print (O0O00O0OOO00OOO0O )#line:134
    def Game_index (O0OOOO000OO000OO0 ,OOO0O0OOO00OO0O0O ):#line:137
        try :#line:138
            OOO0O0OO000O0OOO0 =requests .request ('post',f'{host}/api/Game/index',headers =O0OOOO000OO000OO0 .headers ).json ()#line:139
            if 'code'in OOO0O0OO000O0OOO0 :#line:141
                if OOO0O0OO000O0OOO0 ['code']==1 :#line:142
                    if OOO0O0OO000O0OOO0 ['data']['is_auto_play']:#line:143
                        OO0O000O00OOOOOOO ='✅'#line:144
                    else :#line:145
                        OO0O000O00OOOOOOO ='❌'#line:146
                    if OOO0O0OO000O0OOO0 ['data']['is_game_ing']:#line:148
                        OOOO000OOOOO000O0 ='✅'#line:149
                    else :#line:150
                        OOOO000OOOOO000O0 ='❌'#line:151
                    if OOO0O0OO000O0OOO0 ['data']['is_vip']:#line:152
                        O0O0O00OOOO0OOO0O ='✅'#line:153
                    else :#line:154
                        O0O0O00OOOO0OOO0O ='❌'#line:155
                    if '正在闯关'in OOO0O0OO000O0OOO0 ['data']['npc_hint']:#line:156
                        O0OO0OOO000OOOOOO =OOO0O0OO000O0OOO0 ['data']['npc_hint'][:8 ]#line:157
                    else :#line:158
                        O0OO0OOO000OOOOOO =OOO0O0OO000O0OOO0 ['data']['npc_hint'][:5 ]#line:159
                    print (f'【游戏状态】:自动:{OO0O000O00OOOOOOO}丨闯关:{OOOO000OOOOO000O0}丨VIP:{O0O0O00OOOO0OOO0O}丨{O0OO0OOO000OOOOOO}')#line:160
                    if not OOO0O0OO000O0OOO0 ['data']['is_auto_play']:#line:161
                        if OOO0O0OOO00OO0O0O =='1':#line:162
                            O0OOOO000OO000OO0 .setAutoPlay ()#line:163
        except Exception as O000OO0000OO0OOO0 :#line:164
            print (O000OO0000OO0OOO0 )#line:165
    def LuckyBox (O00O00O00O00OO00O ):#line:169
        global sr #line:170
        try :#line:171
            O000O00O00OOO0OO0 =requests .request ('post',f'{host}/api/LuckyBox/index',headers =O00O00O00O00OO00O .headers ).json ()#line:172
            if 'code'in O000O00O00OOO0OO0 :#line:174
                if O000O00O00OOO0OO0 ['code']==1 :#line:175
                    O000O0O0OO00O0OO0 =O000O00O00OOO0OO0 ['data']['debris']#line:176
                    OOOOO0O000OO00000 =O000O00O00OOO0OO0 ['data']['is_draw']#line:177
                    print (f'【幸运宝箱】:碎片:{str(O000O0O0OO00O0OO0).split(".")[0]}丨当前设置开启宝箱ID:{O00O00O00O00OO00O.box}')#line:178
                    if not OOOOO0O000OO00000 :#line:179
                        O00OOOOOOO0OOOO00 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =O00O00O00O00OO00O .headers ).json ()#line:180
                        if 'code'in O00OOOOOOO0OOOO00 :#line:182
                            if O00OOOOOOO0OOOO00 ['code']==1 :#line:183
                                OOO0OO0OO0O00000O =O00OOOOOOO0OOOO00 ['data']['nub']#line:184
                                print (f'【领取碎片】:获得:{OOO0OO0OO0O00000O}')#line:185
                    for OOOOO000000O0OOO0 in O000O00O00OOO0OO0 ['data']['box_list']:#line:186
                        O000OOOOO0O0OO0OO =OOOOO000000O0OOO0 ['id']#line:188
                        OO000OOOOOOOOOOOO =OOOOO000000O0OOO0 ['name']#line:189
                        OO0O000OO0000OOO0 =OOOOO000000O0OOO0 ['inventory']#line:190
                        OO000000O00OOO000 =OOOOO000000O0OOO0 ['need_debris']#line:191
                        if float (O000OOOOO0O0OO0OO )==float (O00O00O00O00OO00O .box ):#line:192
                            print (f'【幸运宝箱】:名称:{OO000OOOOOOOOOOOO}丨需要碎片:{OO000000O00OOO000}丨剩余:{OO0O000OO0000OOO0}')#line:193
                            if float (O000O0O0OO00O0OO0 )>=float (OO000000O00OOO000 ):#line:194
                                sr .append (O00O00O00O00OO00O .token +'&'+O00O00O00O00OO00O .box )#line:195
                                if OO0O000OO0000OOO0 >0 :#line:196
                                    OO0O0O00OOO000OOO ={'id':O00O00O00O00OO00O .box }#line:197
                                    OOOOO000OOO00O000 =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =O00O00O00O00OO00O .headers ,data =OO0O0O00OOO000OOO ).json ()#line:198
                                    if 'code'in OOOOO000OOO00O000 :#line:200
                                        if OOOOO000OOO00O000 ['code']==1 :#line:201
                                            print (f'【兑换宝箱】:{OOOOO000OOO00O000["msg"]}丨获得{OOOOO000OOO00O000["data"]["name"]}')#line:202
                                            O00O00O00O00OO00O .LuckyBox ()#line:203
        except Exception as OOO0OO0O0O00O0O0O :#line:204
            O00O00O00O00OO00O .LuckyBox ()#line:205
    def score_record (O00OOOOO0O0O0OO00 ):#line:208
        try :#line:209
            O0000OOO00OO00OOO ={'page':'1','limit':'15','type':'2'}#line:210
            O0O00OO0000OOOOO0 =requests .request ('post',f'{host}/api/Score/record',headers =O00OOOOO0O0O0OO00 .headers ,data =O0000OOO00OO00OOO ).json ()#line:211
            if 'code'in O0O00OO0000OOOOO0 :#line:213
                if O0O00OO0000OOOOO0 ['code']==1 :#line:214
                    O0O0O00000O00OOOO =O0O00OO0000OOOOO0 ['data']['record_list']#line:215
                    if O0O0O00000O00OOOO :#line:216
                        for OO00O00OOO00O000O in O0O0O00000O00OOOO :#line:217
                            OO0OOO0O0000OOO00 =OO00O00OOO00O000O ['user_id']#line:218
                            OOO0O0OO0OOOO00OO =OO00O00OOO00O000O ['money']#line:219
                            OO000O00OO0000O00 =OO00O00OOO00O000O ['create_time']#line:220
                            OO0O00O00O0OO0OOO =OO00O00OOO00O000O ['nickname']#line:221
                            print (f'【赠送记录】:昵称:{OO0O00O00O0OO0OOO}丨ID:{OO0OOO0O0000OOO00}丨金额:{OOO0O0OO0OOOO00OO}丨时间:{OO000O00OO0000O00[5:16]}')#line:222
        except Exception as O00OOO0O0000O000O :#line:223
            print (O00OOO0O0000O000O )#line:224
    def score_present (OOO000000OO00OO0O ):#line:228
        try :#line:229
            if float (score )>float (score_big ):#line:230
                O0000O000OOOOOOO0 ={'id':OOO000000OO00OO0O .present_id }#line:231
                O0O0000OO0O0000OO =requests .request ('post',f'{host}/api/Score/presentFindUser',headers =OOO000000OO00OO0O .headers ,data =O0000O000OOOOOOO0 ).json ()#line:232
                if 'code'in O0O0000OO0O0000OO :#line:234
                    if O0O0000OO0O0000OO ['code']==1 :#line:235
                        OOOO00OOO0000O0OO =O0O0000OO0O0000OO ['data']['service_charge']#line:236
                        O0OOOO000O00OOOO0 =int (float (score )/(1 +(int (OOOO00OOO0000O0OO )/100 )))#line:237
                        if O0OOOO000O00OOOO0 >1 :#line:238
                            O00OOO000OO0O0OOO ={'present_id':OOO000000OO00OO0O .present_id ,'present_nub':O0OOOO000O00OOOO0 }#line:239
                            O0O0OOOOOO00O0OO0 =requests .request ('post',f'{host}/api/Score/present',headers =OOO000000OO00OO0O .headers ,data =O00OOO000OO0O0OOO ).json ()#line:240
                            if 'code'in O0O0OOOOOO00O0OO0 :#line:242
                                if O0O0OOOOOO00O0OO0 ['code']==1 :#line:243
                                    print (f'【赠送金币】:ID:{OOO000000OO00OO0O.present_id}丨金币:{O0OOOO000O00OOOO0}丨{O0O0OOOOOO00O0OO0["msg"]}')#line:244
                                elif O0O0OOOOOO00O0OO0 ['code']==0 :#line:245
                                    print (f'【赠送金币】:ID:{OOO000000OO00OO0O.present_id}丨金币:{O0OOOO000O00OOOO0}丨{O0O0OOOOOO00O0OO0["msg"]}')#line:246
                                else :#line:247
                                    print (O0O0OOOOOO00O0OO0 )#line:248
        except Exception as OO0OOO00O000O00O0 :#line:249
            print (OO0OOO00O000O00O0 )#line:250
    def figure (O00O000OOO00000O0 ,OOO00OO0O000OO0O0 ):#line:253
        try :#line:254
            OOO00000000O0O0OO =requests .request ('post',f'{host}/api/figure/index',headers =O00O000OOO00000O0 .headers ).json ()#line:255
            if 'code'in OOO00000000O0O0OO :#line:257
                if OOO00000000O0O0OO ['code']==1 :#line:258
                    for OO00OO0O000O00OO0 in OOO00000000O0O0OO ['data']['user_figure_list']:#line:259
                        OOOO0O0000OO0O00O =OO00OO0O000O00OO0 ['name']#line:260
                        if OOO00OO0O000OO0O0 ==OOOO0O0000OO0O00O :#line:261
                            return True #line:262
            return False #line:263
        except Exception as OOO0OOOOOO0OOOOOO :#line:264
            print (OOO0OOOOOO0OOOOOO )#line:265
    def snatch (O00O0O0OO000OO0OO ):#line:268
        try :#line:269
            O00OOOOOO0000O0O0 =requests .request ('post',f'{host}/api/Snatch/index',headers =O00O0O0OO000OO0OO .headers ).json ()#line:270
            if 'code'in O00OOOOOO0000O0O0 :#line:272
                if O00OOOOOO0000O0O0 ['code']==1 :#line:273
                    OOO0000000O000000 =O00OOOOOO0000O0O0 ['data']['snatch_id']#line:274
                    O00OOOOO0OOOO00OO =O00OOOOOO0000O0O0 ['data']['figure_name']#line:275
                    O00OO0O000O0O0OOO =O00OOOOOO0000O0O0 ['data']['now_figure_nub']#line:276
                    O0000O0O0O0O000O0 =O00OOOOOO0000O0O0 ['data']['max_figure_nub']#line:277
                    if O00OO0O000O0O0OOO <O0000O0O0O0O000O0 :#line:278
                        if O00O0O0OO000OO0OO .figure (O00OOOOO0OOOO00OO ):#line:279
                            O00O0O0OO000OO0OO .snatch_play_index (OOO0000000O000000 )#line:280
        except Exception as O0O000000OOOO0O00 :#line:281
            print (O0O000000OOOO0O00 )#line:282
    def snatch_play_index (OO0OO00OO00OO00OO ,O00O000OOO00O0OO0 ):#line:285
        try :#line:286
            O0O0OOOOO0OO00OO0 ={'snatch_id':O00O000OOO00O0OO0 }#line:287
            O0O00OO0OO000O00O =requests .request ('post',f'{host}/api/Snatch/PlayIndex',headers =OO0OO00OO00OO00OO .headers ,data =O0O0OOOOO0OO00OO0 ).json ()#line:288
            if 'code'in O0O00OO0OO000O00O :#line:290
                if O0O00OO0OO000O00O ['code']==1 :#line:291
                    O0000OOOOOO0O0000 =O0O00OO0OO000O00O ['data']['surplus_figure_nub']#line:292
                    if O0000OOOOOO0O0000 >0 :#line:293
                        OO0OO00OO00OO00OO .snatch_play (O00O000OOO00O0OO0 )#line:294
        except Exception as OO0OO0000000OO000 :#line:295
            print (OO0OO0000000OO000 )#line:296
    def snatch_play (OO0OOOOOO0O00OO00 ,OO0000OO0O0O000OO ):#line:299
        try :#line:300
            O0000OO0OOOOO0O00 ={'snatch_id':OO0000OO0O0O000OO ,'nub':'1'}#line:301
            O0000OOOOOOOO0O00 =requests .request ('post',f'{host}/api/Snatch/play',headers =OO0OOOOOO0O00OO00 .headers ,data =O0000OO0OOOOO0O00 ).json ()#line:302
            if 'code'in O0000OOOOOOOO0O00 :#line:304
                if O0000OOOOOOOO0O00 ['code']==1 :#line:305
                    print (f'【参与夺宝】:{O0000OOOOOOOO0O00["msg"]}')#line:306
        except Exception as OO0O0O0OO0OOOO000 :#line:307
            print (OO0O0O0OO0OOOO000 )#line:308
    def snatch_record (OO00OO00OO0OO0OO0 ):#line:311
        global kkk #line:312
        try :#line:313
            OO0O00OO0O0OO0OOO =requests .request ('post',f'{host}/api/Snatch/record',headers =OO00OO00OO0OO0OO0 .headers ).json ()#line:314
            if 'code'in OO0O00OO0O0OO0OOO :#line:316
                if OO0O00OO0O0OO0OOO ['code']==1 :#line:317
                    O0O0000O0OO00O00O =OO0O00OO0O0OO0OOO ['data']['record_list']#line:318
                    if O0O0000O0OO00O00O :#line:319
                        for O0O00OO0OO000OO0O in O0O0000O0OO00O00O :#line:320
                            kkk +=float (O0O00OO0OO000OO0O ["award_money"])#line:322
                            print (f'【夺宝记录】:{O0O00OO0OO000OO0O["name"]}丨收益:{O0O00OO0OO000OO0O["award_money"]}丨{O0O00OO0OO000OO0O["state"]}')#line:323
        except Exception as O00000OO00O0OOOO0 :#line:324
            print (O00000OO00O0OOOO0 )#line:325
def start ():#line:329
    try :#line:330
        update_the_validation ()#line:331
        O0O00O00O0OO0OO0O =os_qinglong ()#line:332
        print (f"==========共找到{len(O0O00O00O0OO0OO0O)}个账号==========")#line:333
        for O0O0OO00O0OO00O00 in O0O00O00O0OO0OO0O :#line:334
            print (f"------------正在执行第{O0O00O00O0OO0OO0O.index(O0O0OO00O0OO00O00) + 1}个账号------------")#line:335
            OOOOOO0OO0OOOOO00 =Template (O0O0OO00O0OO00O00 )#line:336
            if OOOOOO0OO0OOOOO00 .base_info ():#line:338
                OOOOOO0OO0OOOOO00 .LuckyBox ()#line:340
                OOOOOO0OO0OOOOO00 .playInfo ()#line:342
                if snatch :#line:343
                    OOOOOO0OO0OOOOO00 .snatch ()#line:345
                OOOOOO0OO0OOOOO00 .snatch_record ()#line:347
                if score_record :#line:349
                    OOOOOO0OO0OOOOO00 .score_record ()#line:351
                OOOOOO0OO0OOOOO00 .score_present ()#line:353
                time .sleep (random .randint (1 ,2 ))#line:355
            else :#line:356
                print ('token失效')#line:357
        print (f'夺宝共获取金币:{kkk}')#line:358
        print ('\n开始打印可以抢宝箱的数据')#line:359
        for OO00O0O000O0O000O in sr :#line:360
            print (OO00O0O000O0O000O .strip ())#line:361
    except Exception as O0OO00000O000OO0O :#line:362
        print (O0OO00000O000OO0O )#line:363
def version_of_the_validation ():#line:365
    return str ((66 -56 )/10 )#line:366
if __name__ =='__main__':#line:369
    start ()#line:370
