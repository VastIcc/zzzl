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
        O0000OOOOO000000O =os .environ [application ].split ('\n')#line:5
        if len (O0000OOOOO000000O )>0 :#line:6
            return O0000OOOOO000000O #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        OO00O00000O0OOO0O =token .split ('\n')#line:19
        if len (OO00O00000O0OOO0O )>0 :#line:20
            return OO00O00000O0OOO0O #line:21
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
        OO0OO0OOOOO0O00OO =gitee_validation ()#line:38
        if version_of_the_validation ()<OO0OO0OOOOO0O00OO ['Tower']['edition']:#line:39
            print (f'当前脚本名字: {OO0OO0OOOOO0O00OO["Tower"]["text"]}')#line:40
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OO0OOOOO0O00OO["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:41
            print (f'更新内容=>> {OO0OO0OOOOO0O00OO["Tower"]["content"]}')#line:42
        else :#line:43
            print (f'当前脚本名字: {OO0OO0OOOOO0O00OO["Tower"]["text"]}')#line:44
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OO0OOOOO0O00OO["Tower"]["edition"]}   ✅')#line:45
            print (f'更新内容=>> {OO0OO0OOOOO0O00OO["Tower"]["content"]}')#line:46
    except Exception as O0OOOOOO0O0OOO00O :#line:47
        print (O0OOOOOO0O0OOO00O )#line:48
class Template :#line:51
    def __init__ (OOO0O0O0OO0OOO000 ,OO0000O0OO0OOO00O ):#line:53
        try :#line:54
            OOO0O0O0OO0OOO000 .token =OO0000O0OO0OOO00O .split ('&')[0 ]#line:55
            OOO0O0O0OO0OOO000 .box =OO0000O0OO0OOO00O .split ('&')[1 ]#line:56
            OOO0O0O0OO0OOO000 .present_id =OO0000O0OO0OOO00O .split ('&')[2 ]#line:57
            OOO0O0O0OO0OOO000 .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':versions ,'accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OOO0O0O0OO0OOO000 .token ,'server':'true','phone-type':'android',}#line:69
        except :#line:70
            print ('变量格式错误')#line:71
    def base_info (O0OO0O000OOOO0O0O ):#line:74
        global score #line:75
        try :#line:76
            OOO000O00OO000O00 =requests .request ('post',f'{host}/api/User/info',headers =O0OO0O000OOOO0O0O .headers ).json ()#line:77
            if 'code'in OOO000O00OO000O00 :#line:79
                if OOO000O00OO000O00 ['code']==1 :#line:80
                    OOOOO0OO0O0OO00OO =OOO000O00OO000O00 ['data']['nickname']#line:81
                    OO0OOOO0OOO0OO0OO =OOO000O00OO000O00 ['data']['id']#line:82
                    score =OOO000O00OO000O00 ['data']['score']#line:83
                    print (f'【账号信息】:昵称:{OOOOO0OO0O0OO00OO[:6]}丨ID:{OO0OOOO0OOO0OO0OO}丨金币:{str(score)[:5]}')#line:84
                if OOO000O00OO000O00 ['code']==302 :#line:85
                    return False #line:86
            return True #line:87
        except Exception as O0O0O0OOO0000000O :#line:88
            print (O0O0O0OOO0000000O )#line:89
    def playInfo (O00O000O0OO00OO0O ):#line:92
        try :#line:93
            OO00OOO0OO00O00O0 =requests .request ('post',f'{host}/api/Game/playInfo',headers =O00O000O0OO00OO0O .headers ).json ()#line:94
            if 'code'in OO00OOO0OO00O00O0 :#line:96
                if OO00OOO0OO00O00O0 ['code']==1 :#line:97
                    OO0O0O00O00OOOOOO =OO00OOO0OO00O00O0 ['data']['play_tier']#line:98
                    O0OOO0000000O0000 =OO00OOO0OO00O00O0 ['data']['play_tier_need_money']#line:99
                    OOOOOO0OOO0O00OO0 =OO00OOO0OO00O00O0 ['data']['user_money']#line:100
                    O000O00000O00O000 =OO00OOO0OO00O00O0 ['data']['play_finish_money']#line:101
                    OOOOOO0OO0O00OO0O =OO00OOO0OO00O00O0 ['data']['surplus_play_nub']#line:102
                    print (f'【参与闯关】:层数:{OO0O0O00O00OOOOOO}丨剩余:{OOOOOO0OO0O00OO0O}丨花费:{O0OOO0000000O0000}丨预计:{O000O00000O00O000}')#line:103
                    if float (O0OOO0000000O0000 )<float (OOOOOO0OOO0O00OO0 ):#line:104
                        if OOOOOO0OO0O00OO0O >0 :#line:105
                            O00O000O0OO00OO0O .Game_index ('1')#line:106
                        else :#line:107
                            O00O000O0OO00OO0O .Game_index ('2')#line:108
                    else :#line:109
                        O00O000O0OO00OO0O .Game_index ('2')#line:110
        except Exception as O000000000O00OO0O :#line:112
            print (O000000000O00OO0O )#line:113
    def setAutoPlay (O00OO0000OOO0O0OO ):#line:116
        try :#line:117
            O0O0O0OO0OOOOO0O0 ={'state':'1'}#line:118
            O0O0O00000O0O0000 =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O00OO0000OOO0O0OO .headers ,data =O0O0O0OO0OOOOO0O0 ).json ()#line:119
            if 'code'in O0O0O00000O0O0000 :#line:121
                if O0O0O00000O0O0000 ['code']==1 :#line:122
                    print (f'【自动闯关】:{O0O0O00000O0O0000["msg"]}')#line:123
                if O0O0O00000O0O0000 ['code']==0 :#line:124
                    print (f'【自动闯关】:{O0O0O00000O0O0000["msg"]}')#line:125
        except Exception as O0OO000OO0000OOOO :#line:126
            print (O0OO000OO0000OOOO )#line:127
    def Game_index (O0OO000O0OO0OOOO0 ,OO00O00O0O0OO000O ):#line:130
        try :#line:131
            O0OO000O000O00OO0 =requests .request ('post',f'{host}/api/Game/index',headers =O0OO000O0OO0OOOO0 .headers ).json ()#line:132
            if 'code'in O0OO000O000O00OO0 :#line:134
                if O0OO000O000O00OO0 ['code']==1 :#line:135
                    if O0OO000O000O00OO0 ['data']['is_auto_play']:#line:136
                        OO000O000O00O00O0 ='✅'#line:137
                    else :#line:138
                        OO000O000O00O00O0 ='❌'#line:139
                    if O0OO000O000O00OO0 ['data']['is_game_ing']:#line:141
                        OO000O00O000O0O0O ='✅'#line:142
                    else :#line:143
                        OO000O00O000O0O0O ='❌'#line:144
                    if O0OO000O000O00OO0 ['data']['is_vip']:#line:145
                        O000OOOOO0O0OO0OO ='✅'#line:146
                    else :#line:147
                        O000OOOOO0O0OO0OO ='❌'#line:148
                    if '正在闯关'in O0OO000O000O00OO0 ['data']['npc_hint']:#line:149
                        O00000O00OO00O00O =O0OO000O000O00OO0 ['data']['npc_hint'][:8 ]#line:150
                    else :#line:151
                        O00000O00OO00O00O =O0OO000O000O00OO0 ['data']['npc_hint'][:5 ]#line:152
                    print (f'【游戏状态】:自动:{OO000O000O00O00O0}丨闯关:{OO000O00O000O0O0O}丨VIP:{O000OOOOO0O0OO0OO}丨{O00000O00OO00O00O}')#line:153
                    if not O0OO000O000O00OO0 ['data']['is_auto_play']:#line:154
                        if OO00O00O0O0OO000O =='1':#line:155
                            O0OO000O0OO0OOOO0 .setAutoPlay ()#line:156
        except Exception as O0O0OO00O0O0O0O0O :#line:157
            print (O0O0OO00O0O0O0O0O )#line:158
    def LuckyBox (OO0OOO00O0000O000 ):#line:162
        global sr #line:163
        try :#line:164
            O0OO0000OOOO0O0OO =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OO0OOO00O0000O000 .headers ).json ()#line:165
            if 'code'in O0OO0000OOOO0O0OO :#line:167
                if O0OO0000OOOO0O0OO ['code']==1 :#line:168
                    O0000OOO000O00O00 =O0OO0000OOOO0O0OO ['data']['debris']#line:169
                    O0O00O0O00OO0O000 =O0OO0000OOOO0O0OO ['data']['is_draw']#line:170
                    print (f'【幸运宝箱】:碎片:{str(O0000OOO000O00O00).split(".")[0]}丨当前设置开启宝箱ID:{OO0OOO00O0000O000.box}')#line:171
                    if not O0O00O0O00OO0O000 :#line:172
                        O0OO0O000OOO00000 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OO0OOO00O0000O000 .headers ).json ()#line:173
                        if 'code'in O0OO0O000OOO00000 :#line:175
                            if O0OO0O000OOO00000 ['code']==1 :#line:176
                                OO000000000000OOO =O0OO0O000OOO00000 ['data']['nub']#line:177
                                print (f'【领取碎片】:获得:{OO000000000000OOO}')#line:178
                    for OOOO0O00000O0O00O in O0OO0000OOOO0O0OO ['data']['box_list']:#line:179
                        OOO0O00O00O0O000O =OOOO0O00000O0O00O ['id']#line:181
                        O0O00O0O0O0000000 =OOOO0O00000O0O00O ['name']#line:182
                        OOO000O0OOO0OO00O =OOOO0O00000O0O00O ['inventory']#line:183
                        OOOO000000O00O00O =OOOO0O00000O0O00O ['need_debris']#line:184
                        if float (OOO0O00O00O0O000O )==float (OO0OOO00O0000O000 .box ):#line:185
                            print (f'【幸运宝箱】:名称:{O0O00O0O0O0000000}丨需要碎片:{OOOO000000O00O00O}丨剩余:{OOO000O0OOO0OO00O}')#line:186
                            if float (O0000OOO000O00O00 )>=float (OOOO000000O00O00O ):#line:187
                                sr .append (OO0OOO00O0000O000 .token +'&'+OO0OOO00O0000O000 .box )#line:188
                                if OOO000O0OOO0OO00O >0 :#line:189
                                    OO00OO0O0000OO00O ={'id':OO0OOO00O0000O000 .box }#line:190
                                    O0OOOOO0O000OOOO0 =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =OO0OOO00O0000O000 .headers ,data =OO00OO0O0000OO00O ).json ()#line:191
                                    if 'code'in O0OOOOO0O000OOOO0 :#line:193
                                        if O0OOOOO0O000OOOO0 ['code']==1 :#line:194
                                            print (f'【兑换宝箱】:{O0OOOOO0O000OOOO0["msg"]}丨获得{O0OOOOO0O000OOOO0["data"]["name"]}')#line:195
                                            OO0OOO00O0000O000 .LuckyBox ()#line:196
        except Exception as OOO000OO0OO0OO0O0 :#line:197
            OO0OOO00O0000O000 .LuckyBox ()#line:198
    def score_record (OOOO00O000OO0OOOO ):#line:201
        try :#line:202
            OO0OOOOO0OO0O0000 ={'page':'1','limit':'15','type':'2'}#line:203
            O0OOO0000OOO00OO0 =requests .request ('post',f'{host}/api/Score/record',headers =OOOO00O000OO0OOOO .headers ,data =OO0OOOOO0OO0O0000 ).json ()#line:204
            if 'code'in O0OOO0000OOO00OO0 :#line:206
                if O0OOO0000OOO00OO0 ['code']==1 :#line:207
                    OO0000O0O0O0O00O0 =O0OOO0000OOO00OO0 ['data']['record_list']#line:208
                    if OO0000O0O0O0O00O0 :#line:209
                        for O000OO0OOOOO0OO00 in OO0000O0O0O0O00O0 :#line:210
                            OO00O00O000O0O000 =O000OO0OOOOO0OO00 ['user_id']#line:211
                            O00O0OOOO0OOO0000 =O000OO0OOOOO0OO00 ['money']#line:212
                            OOOO0O0OOOOO0O000 =O000OO0OOOOO0OO00 ['create_time']#line:213
                            O000O000OOOO0OOO0 =O000OO0OOOOO0OO00 ['nickname']#line:214
                            print (f'【赠送记录】:昵称:{O000O000OOOO0OOO0}丨ID:{OO00O00O000O0O000}丨金额:{O00O0OOOO0OOO0000}丨时间:{OOOO0O0OOOOO0O000[5:16]}')#line:215
        except Exception as OOOO0OO0000OOOOO0 :#line:216
            print (OOOO0OO0000OOOOO0 )#line:217
    def score_present (O0OOOO000000OOOO0 ):#line:221
        try :#line:222
            if float (score )>float (score_big ):#line:223
                OO00OOOO0O00O0O0O ={'id':O0OOOO000000OOOO0 .present_id }#line:224
                OO000O00O0O000O00 =requests .request ('post',f'{host}/api/Score/presentFindUser',headers =O0OOOO000000OOOO0 .headers ,data =OO00OOOO0O00O0O0O ).json ()#line:225
                if 'code'in OO000O00O0O000O00 :#line:227
                    if OO000O00O0O000O00 ['code']==1 :#line:228
                        OOOOO000O0OOO0000 =OO000O00O0O000O00 ['data']['service_charge']#line:229
                        OOO00OOO000OOO00O =int (float (score )/(1 +(int (OOOOO000O0OOO0000 )/100 )))#line:230
                        if OOO00OOO000OOO00O >1 :#line:231
                            OOO0OO00O0O000OOO ={'present_id':O0OOOO000000OOOO0 .present_id ,'present_nub':OOO00OOO000OOO00O }#line:232
                            OO0O000O0O00O00O0 =requests .request ('post',f'{host}/api/Score/present',headers =O0OOOO000000OOOO0 .headers ,data =OOO0OO00O0O000OOO ).json ()#line:233
                            if 'code'in OO0O000O0O00O00O0 :#line:235
                                if OO0O000O0O00O00O0 ['code']==1 :#line:236
                                    print (f'【赠送金币】:ID:{O0OOOO000000OOOO0.present_id}丨金币:{OOO00OOO000OOO00O}丨{OO0O000O0O00O00O0["msg"]}')#line:237
                                elif OO0O000O0O00O00O0 ['code']==0 :#line:238
                                    print (f'【赠送金币】:ID:{O0OOOO000000OOOO0.present_id}丨金币:{OOO00OOO000OOO00O}丨{OO0O000O0O00O00O0["msg"]}')#line:239
                                else :#line:240
                                    print (OO0O000O0O00O00O0 )#line:241
        except Exception as OOO00O00O0O0OOOOO :#line:242
            print (OOO00O00O0O0OOOOO )#line:243
    def figure (O00O00000OO00O00O ,O0OOOO0O000O0OO0O ):#line:246
        try :#line:247
            O000O0OO0O0OO00O0 =requests .request ('post',f'{host}/api/figure/index',headers =O00O00000OO00O00O .headers ).json ()#line:248
            if 'code'in O000O0OO0O0OO00O0 :#line:250
                if O000O0OO0O0OO00O0 ['code']==1 :#line:251
                    for OO00OO0O000000O00 in O000O0OO0O0OO00O0 ['data']['user_figure_list']:#line:252
                        OO0O0000OOO0OO0OO =OO00OO0O000000O00 ['name']#line:253
                        if O0OOOO0O000O0OO0O ==OO0O0000OOO0OO0OO :#line:254
                            return True #line:255
            return False #line:256
        except Exception as O0O0OO0OOO0OO0000 :#line:257
            print (O0O0OO0OOO0OO0000 )#line:258
    def snatch (OO0OO0O0OOO00OOO0 ):#line:261
        try :#line:262
            O0O00O0000O00O0O0 =requests .request ('post',f'{host}/api/Snatch/index',headers =OO0OO0O0OOO00OOO0 .headers ).json ()#line:263
            if 'code'in O0O00O0000O00O0O0 :#line:265
                if O0O00O0000O00O0O0 ['code']==1 :#line:266
                    O00000000OO00OOOO =O0O00O0000O00O0O0 ['data']['snatch_id']#line:267
                    O00OO0000OO00OO00 =O0O00O0000O00O0O0 ['data']['figure_name']#line:268
                    OO0OO0OO0OOO0OO0O =O0O00O0000O00O0O0 ['data']['now_figure_nub']#line:269
                    OO00O0OO0O0O0O000 =O0O00O0000O00O0O0 ['data']['max_figure_nub']#line:270
                    if OO0OO0OO0OOO0OO0O <OO00O0OO0O0O0O000 :#line:271
                        if OO0OO0O0OOO00OOO0 .figure (O00OO0000OO00OO00 ):#line:272
                            OO0OO0O0OOO00OOO0 .snatch_play_index (O00000000OO00OOOO )#line:273
        except Exception as OOO0OOO00OOOOO00O :#line:274
            print (OOO0OOO00OOOOO00O )#line:275
    def snatch_play_index (OO0OOOO00O0O0O0O0 ,OO00000000OO0000O ):#line:278
        try :#line:279
            OO0O0O0OOO0O0OO0O ={'snatch_id':OO00000000OO0000O }#line:280
            O00O00OO0O0O0O00O =requests .request ('post',f'{host}/api/Snatch/PlayIndex',headers =OO0OOOO00O0O0O0O0 .headers ,data =OO0O0O0OOO0O0OO0O ).json ()#line:281
            if 'code'in O00O00OO0O0O0O00O :#line:283
                if O00O00OO0O0O0O00O ['code']==1 :#line:284
                    OO0O0OO00O000O0OO =O00O00OO0O0O0O00O ['data']['surplus_figure_nub']#line:285
                    if OO0O0OO00O000O0OO >0 :#line:286
                        OO0OOOO00O0O0O0O0 .snatch_play (OO00000000OO0000O )#line:287
        except Exception as O00OO0O0O0OO00O00 :#line:288
            print (O00OO0O0O0OO00O00 )#line:289
    def snatch_play (OOOO0OO000O0OO0O0 ,OO00O000O0OO0O0OO ):#line:292
        try :#line:293
            O00OOOO00O00OO0O0 ={'snatch_id':OO00O000O0OO0O0OO ,'nub':'1'}#line:294
            O0OOOOO00OOO0O0O0 =requests .request ('post',f'{host}/api/Snatch/play',headers =OOOO0OO000O0OO0O0 .headers ,data =O00OOOO00O00OO0O0 ).json ()#line:295
            if 'code'in O0OOOOO00OOO0O0O0 :#line:297
                if O0OOOOO00OOO0O0O0 ['code']==1 :#line:298
                    print (f'【参与夺宝】:{O0OOOOO00OOO0O0O0["msg"]}')#line:299
        except Exception as OOOO000O000OO00O0 :#line:300
            print (OOOO000O000OO00O0 )#line:301
    def snatch_record (O0O0OO0OOO00O000O ):#line:304
        try :#line:305
            O00OO0OOOOOOOO0OO =requests .request ('post',f'{host}/api/Snatch/record',headers =O0O0OO0OOO00O000O .headers ).json ()#line:306
            if 'code'in O00OO0OOOOOOOO0OO :#line:308
                if O00OO0OOOOOOOO0OO ['code']==1 :#line:309
                    OOOOO0O0O00O0O0O0 =O00OO0OOOOOOOO0OO ['data']['record_list']#line:310
                    if OOOOO0O0O00O0O0O0 :#line:311
                        for OOOO000OO0O0OOOO0 in OOOOO0O0O00O0O0O0 :#line:312
                            print (f'【夺宝记录】:{OOOO000OO0O0OOOO0["name"]}丨收益:{OOOO000OO0O0OOOO0["award_money"]}丨{OOOO000OO0O0OOOO0["state"]}')#line:314
        except Exception as OO000O0OOOO000O0O :#line:315
            print (OO000O0OOOO000O0O )#line:316
def start ():#line:320
    try :#line:321
        update_the_validation ()#line:322
        O000OO0OOOOOOO00O =os_qinglong ()#line:323
        print (f"==========共找到{len(O000OO0OOOOOOO00O)}个账号==========")#line:324
        for OOOO00000O0OOO0OO in O000OO0OOOOOOO00O :#line:325
            print (f"------------正在执行第{O000OO0OOOOOOO00O.index(OOOO00000O0OOO0OO) + 1}个账号------------")#line:326
            OO0000O0OOOO00OOO =Template (OOOO00000O0OOO0OO )#line:327
            if OO0000O0OOOO00OOO .base_info ():#line:329
                OO0000O0OOOO00OOO .LuckyBox ()#line:331
                OO0000O0OOOO00OOO .playInfo ()#line:333
                OO0000O0OOOO00OOO .snatch ()#line:335
                OO0000O0OOOO00OOO .snatch_record ()#line:337
                if score_record :#line:339
                    OO0000O0OOOO00OOO .score_record ()#line:341
                OO0000O0OOOO00OOO .score_present ()#line:343
                time .sleep (random .randint (1 ,2 ))#line:345
            else :#line:346
                print ('token失效')#line:347
        print ('\n开始打印可以抢宝箱的数据')#line:348
        for O00OO0OO0OO00OO0O in sr :#line:349
            print (O00OO0OO0OO00OO0O .strip ())#line:350
    except Exception as O0O0O0OOO000000O0 :#line:351
        print (O0O0O0OOO000000O0 )#line:352
def version_of_the_validation ():#line:354
    return str ((65 -56 )/10 )#line:355
if __name__ =='__main__':#line:358
    start ()#line:359
