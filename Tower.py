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
        O00OO000O000000OO =os .environ [application ].split ('\n')#line:5
        if len (O00OO000O000000OO )>0 :#line:6
            return O00OO000O000000OO #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        OOOO0O0OO000OOOO0 =token .split ('\n')#line:19
        if len (OOOO0O0OO000OOOO0 )>0 :#line:20
            return OOOO0O0OO000OOOO0 #line:21
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
        OO0O000OO000O00OO =gitee_validation ()#line:38
        if version_of_the_validation ()<OO0O000OO000O00OO ['Tower']['edition']:#line:39
            print (f'当前脚本名字: {OO0O000OO000O00OO["Tower"]["text"]}')#line:40
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O000OO000O00OO["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:41
            print (f'更新内容=>> {OO0O000OO000O00OO["Tower"]["content"]}')#line:42
        else :#line:43
            print (f'当前脚本名字: {OO0O000OO000O00OO["Tower"]["text"]}')#line:44
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O000OO000O00OO["Tower"]["edition"]}   ✅')#line:45
            print (f'更新内容=>> {OO0O000OO000O00OO["Tower"]["content"]}')#line:46
    except Exception as OO00000OO000O000O :#line:47
        print (OO00000OO000O000O )#line:48
class Template :#line:51
    def __init__ (OOO0O0O0O0O000O0O ,O0O00000O0OO0000O ):#line:53
        try :#line:54
            OOO0O0O0O0O000O0O .token =O0O00000O0OO0000O .split ('&')[0 ]#line:55
            OOO0O0O0O0O000O0O .box =O0O00000O0OO0000O .split ('&')[1 ]#line:56
            OOO0O0O0O0O000O0O .present_id =O0O00000O0OO0000O .split ('&')[2 ]#line:57
            OOO0O0O0O0O000O0O .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':versions ,'accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OOO0O0O0O0O000O0O .token ,'server':'true','phone-type':'android',}#line:69
        except :#line:70
            print ('变量格式错误')#line:71
    def base_info (O0O0O00OO0O0O0O0O ):#line:74
        global score #line:75
        try :#line:76
            OOO000OO0OOOOO000 =requests .request ('post',f'{host}/api/User/info',headers =O0O0O00OO0O0O0O0O .headers ).json ()#line:77
            if 'code'in OOO000OO0OOOOO000 :#line:79
                if OOO000OO0OOOOO000 ['code']==1 :#line:80
                    O0OOO0O000000O0OO =OOO000OO0OOOOO000 ['data']['nickname']#line:81
                    OOO0000O0OO0000O0 =OOO000OO0OOOOO000 ['data']['id']#line:82
                    score =OOO000OO0OOOOO000 ['data']['score']#line:83
                    print (f'【账号信息】:昵称:{O0OOO0O000000O0OO[:6]}丨ID:{OOO0000O0OO0000O0}丨金币:{str(score)[:5]}')#line:84
                if OOO000OO0OOOOO000 ['code']==302 :#line:85
                    return False #line:86
            return True #line:87
        except Exception as OO00000O0OO00OO0O :#line:88
            print (OO00000O0OO00OO0O )#line:89
    def playInfo (OOO0000O000O0OOO0 ):#line:92
        try :#line:93
            O0O0OOOO00OO0O00O =requests .request ('post',f'{host}/api/Game/playInfo',headers =OOO0000O000O0OOO0 .headers ).json ()#line:94
            if 'code'in O0O0OOOO00OO0O00O :#line:96
                if O0O0OOOO00OO0O00O ['code']==1 :#line:97
                    OO000OO0O00OOOO00 =O0O0OOOO00OO0O00O ['data']['play_tier']#line:98
                    O0O0O00O0OOOO0O00 =O0O0OOOO00OO0O00O ['data']['play_tier_need_money']#line:99
                    O0000000O0000000O =O0O0OOOO00OO0O00O ['data']['user_money']#line:100
                    O0O000O0OOO00OOO0 =O0O0OOOO00OO0O00O ['data']['play_finish_money']#line:101
                    O0O00O00OOO00O00O =O0O0OOOO00OO0O00O ['data']['surplus_play_nub']#line:102
                    print (f'【参与闯关】:层数:{OO000OO0O00OOOO00}丨剩余:{O0O00O00OOO00O00O}丨花费:{O0O0O00O0OOOO0O00}丨预计:{O0O000O0OOO00OOO0}')#line:103
                    if float (O0O0O00O0OOOO0O00 )<float (O0000000O0000000O ):#line:104
                        if O0O00O00OOO00O00O >0 :#line:105
                            OOO0000O000O0OOO0 .Game_index ('1')#line:106
                        else :#line:107
                            OOO0000O000O0OOO0 .Game_index ('2')#line:108
                    else :#line:109
                        OOO0000O000O0OOO0 .Game_index ('2')#line:110
        except Exception as O00OOO00O00O00O0O :#line:112
            print (O00OOO00O00O00O0O )#line:113
    def setAutoPlay (O0O00O0OO0OO000OO ):#line:116
        try :#line:117
            O00OOO0OOOO000O0O ={'state':'1'}#line:120
            OO0OO0O0OO0OO0OOO =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O0O00O0OO0OO000OO .headers ,data =O00OOO0OOOO000O0O ).json ()#line:121
            if 'code'in OO0OO0O0OO0OO0OOO :#line:123
                if OO0OO0O0OO0OO0OOO ['code']==1 :#line:124
                    print (f'【自动闯关】:{OO0OO0O0OO0OO0OOO["msg"]}')#line:125
                if OO0OO0O0OO0OO0OOO ['code']==0 :#line:126
                    print (f'【自动闯关】:{OO0OO0O0OO0OO0OOO["msg"]}')#line:127
        except Exception as O00OOOO0OO00O0O00 :#line:128
            print (O00OOOO0OO00O0O00 )#line:129
    def Game_index (O00O000OOOOO0OO00 ,OO00OOOOOOOO0O000 ):#line:132
        try :#line:133
            OO0O00O000O0OOO0O =requests .request ('post',f'{host}/api/Game/index',headers =O00O000OOOOO0OO00 .headers ).json ()#line:134
            if 'code'in OO0O00O000O0OOO0O :#line:136
                if OO0O00O000O0OOO0O ['code']==1 :#line:137
                    if OO0O00O000O0OOO0O ['data']['is_auto_play']:#line:138
                        OO0OO00O000O000O0 ='✅'#line:139
                    else :#line:140
                        OO0OO00O000O000O0 ='❌'#line:141
                    if OO0O00O000O0OOO0O ['data']['is_game_ing']:#line:143
                        O0O00O0O0O00OO0O0 ='✅'#line:144
                    else :#line:145
                        O0O00O0O0O00OO0O0 ='❌'#line:146
                    if OO0O00O000O0OOO0O ['data']['is_vip']:#line:147
                        O0O0OOO00O0O00O00 ='✅'#line:148
                    else :#line:149
                        O0O0OOO00O0O00O00 ='❌'#line:150
                    if '正在闯关'in OO0O00O000O0OOO0O ['data']['npc_hint']:#line:151
                        OOO0OOO0O0O000O0O =OO0O00O000O0OOO0O ['data']['npc_hint'][:8 ]#line:152
                    else :#line:153
                        OOO0OOO0O0O000O0O =OO0O00O000O0OOO0O ['data']['npc_hint'][:5 ]#line:154
                    print (f'【游戏状态】:自动:{OO0OO00O000O000O0}丨闯关:{O0O00O0O0O00OO0O0}丨VIP:{O0O0OOO00O0O00O00}丨{OOO0OOO0O0O000O0O}')#line:155
                    if not OO0O00O000O0OOO0O ['data']['is_auto_play']:#line:156
                        if OO00OOOOOOOO0O000 =='1':#line:157
                            O00O000OOOOO0OO00 .setAutoPlay ()#line:158
        except Exception as OO0O0O0O00000OO0O :#line:159
            print (OO0O0O0O00000OO0O )#line:160
    def LuckyBox (O0OO0OO0OOOOOO0OO ):#line:164
        global sr #line:165
        try :#line:166
            OO0000O0000O0OO00 =requests .request ('post',f'{host}/api/LuckyBox/index',headers =O0OO0OO0OOOOOO0OO .headers ).json ()#line:167
            if 'code'in OO0000O0000O0OO00 :#line:169
                if OO0000O0000O0OO00 ['code']==1 :#line:170
                    O0O000O00000000OO =OO0000O0000O0OO00 ['data']['debris']#line:171
                    OOO0O0OOO00O00000 =OO0000O0000O0OO00 ['data']['is_draw']#line:172
                    print (f'【幸运宝箱】:碎片:{str(O0O000O00000000OO).split(".")[0]}丨当前设置开启宝箱ID:{O0OO0OO0OOOOOO0OO.box}')#line:173
                    if not OOO0O0OOO00O00000 :#line:174
                        OOO0O0O00OOOO0000 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =O0OO0OO0OOOOOO0OO .headers ).json ()#line:175
                        if 'code'in OOO0O0O00OOOO0000 :#line:177
                            if OOO0O0O00OOOO0000 ['code']==1 :#line:178
                                O0OO000O0O0O0O0O0 =OOO0O0O00OOOO0000 ['data']['nub']#line:179
                                print (f'【领取碎片】:获得:{O0OO000O0O0O0O0O0}')#line:180
                    for O0OO00OO0OO0OOOOO in OO0000O0000O0OO00 ['data']['box_list']:#line:181
                        OOOO0OO0O0OOO00OO =O0OO00OO0OO0OOOOO ['id']#line:183
                        O000OO00OOOOO000O =O0OO00OO0OO0OOOOO ['name']#line:184
                        OOOO0000000O0O000 =O0OO00OO0OO0OOOOO ['inventory']#line:185
                        OO000OO00O0OO00OO =O0OO00OO0OO0OOOOO ['need_debris']#line:186
                        if float (OOOO0OO0O0OOO00OO )==float (O0OO0OO0OOOOOO0OO .box ):#line:187
                            print (f'【幸运宝箱】:名称:{O000OO00OOOOO000O}丨需要碎片:{OO000OO00O0OO00OO}丨剩余:{OOOO0000000O0O000}')#line:189
                            if float (O0O000O00000000OO )>=float (OO000OO00O0OO00OO ):#line:190
                                sr .append (O0OO0OO0OOOOOO0OO .token +'&'+O0OO0OO0OOOOOO0OO .box )#line:191
                                if OOOO0000000O0O000 >0 :#line:192
                                    O0O0OO0O0OO0OO00O ={'id':O0OO0OO0OOOOOO0OO .box }#line:193
                                    OO00O000O000OO000 =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =O0OO0OO0OOOOOO0OO .headers ,data =O0O0OO0O0OO0OO00O ).json ()#line:194
                                    if 'code'in OO00O000O000OO000 :#line:196
                                        if OO00O000O000OO000 ['code']==1 :#line:197
                                            print (f'【兑换宝箱】:{OO00O000O000OO000["msg"]}丨获得{OO00O000O000OO000["data"]["name"]}')#line:198
        except Exception as O00O00O0OO0000O0O :#line:199
            print (O00O00O0OO0000O0O )#line:200
    def score_record (OO0O000OOOOOOOOO0 ):#line:203
        O000OOOOOO0O0O0OO ={'page':'1','limit':'15','type':'2'}#line:204
        OO00O0OOO00O0OOO0 =requests .request ('post',f'{host}/api/Score/record',headers =OO0O000OOOOOOOOO0 .headers ,data =O000OOOOOO0O0O0OO ).json ()#line:205
        if 'code'in OO00O0OOO00O0OOO0 :#line:207
            if OO00O0OOO00O0OOO0 ['code']==1 :#line:208
                O0O000OOO0OOO0O0O =OO00O0OOO00O0OOO0 ['data']['record_list']#line:209
                if O0O000OOO0OOO0O0O :#line:210
                    for OOOO00O0O0OOO0OO0 in O0O000OOO0OOO0O0O :#line:211
                        O0O0O0O000000OO0O =OOOO00O0O0OOO0OO0 ['user_id']#line:212
                        OOOO000OOO0O0O000 =OOOO00O0O0OOO0OO0 ['money']#line:213
                        O000O0000OOO0OOOO =OOOO00O0O0OOO0OO0 ['create_time']#line:214
                        O0O0O0OO00OO0000O =OOOO00O0O0OOO0OO0 ['nickname']#line:215
                        print (f'【赠送记录】:昵称:{O0O0O0OO00OO0000O}丨ID:{O0O0O0O000000OO0O}丨金额:{OOOO000OOO0O0O000}丨时间:{O000O0000OOO0OOOO[5:16]}')#line:216
    def score_present (OOO00O00000OO0000 ):#line:219
        try :#line:220
            if float (score )>float (score_big ):#line:221
                OOO0O000OOO0O0OO0 ={'id':OOO00O00000OO0000 .present_id }#line:222
                OO000OOO00O00000O =requests .request ('post',f'{host}/api/Score/presentFindUser',headers =OOO00O00000OO0000 .headers ,data =OOO0O000OOO0O0OO0 ).json ()#line:223
                if 'code'in OO000OOO00O00000O :#line:225
                    if OO000OOO00O00000O ['code']==1 :#line:226
                        OO0O0000OO0O00OO0 =OO000OOO00O00000O ['data']['service_charge']#line:227
                        O00OO00O0O000OOO0 =int (float (score )/(1 +(int (OO0O0000OO0O00OO0 )/100 )))#line:228
                        if O00OO00O0O000OOO0 >1 :#line:229
                            O0O0000O0OO00000O ={'present_id':OOO00O00000OO0000 .present_id ,'present_nub':O00OO00O0O000OOO0 }#line:230
                            O0O00O0OO0O00O0O0 =requests .request ('post',f'{host}/api/Score/present',headers =OOO00O00000OO0000 .headers ,data =O0O0000O0OO00000O ).json ()#line:231
                            if 'code'in O0O00O0OO0O00O0O0 :#line:233
                                if O0O00O0OO0O00O0O0 ['code']==1 :#line:234
                                    print (f'【赠送金币】:ID:{OOO00O00000OO0000.present_id}丨金币:{O00OO00O0O000OOO0}丨{O0O00O0OO0O00O0O0["msg"]}')#line:235
                                elif O0O00O0OO0O00O0O0 ['code']==0 :#line:236
                                    print (f'【赠送金币】:ID:{OOO00O00000OO0000.present_id}丨金币:{O00OO00O0O000OOO0}丨{O0O00O0OO0O00O0O0["msg"]}')#line:237
                                else :#line:238
                                    print (O0O00O0OO0O00O0O0 )#line:239
        except Exception as OOOOOO00O000OOOO0 :#line:240
            print (OOOOOO00O000OOOO0 )#line:241
    def figure (OOO0000O0OO00O000 ,OOO0OOOOOO0OO00OO ):#line:244
        try :#line:245
            OOO00OOO0OO0OO00O =requests .request ('post',f'{host}/api/figure/index',headers =OOO0000O0OO00O000 .headers ).json ()#line:246
            if 'code'in OOO00OOO0OO0OO00O :#line:248
                if OOO00OOO0OO0OO00O ['code']==1 :#line:249
                    for O0O0OO00O0O0O0OOO in OOO00OOO0OO0OO00O ['data']['user_figure_list']:#line:250
                        O0O0OOO00OO00OO0O =O0O0OO00O0O0O0OOO ['name']#line:251
                        if OOO0OOOOOO0OO00OO ==O0O0OOO00OO00OO0O :#line:252
                            return True #line:253
            return False #line:254
        except Exception as O000OOO0OOO00OOOO :#line:255
            print (O000OOO0OOO00OOOO )#line:256
    def snatch (O0OOO00OO000O0O0O ):#line:259
        try :#line:260
            OO0OO0OOO0O000000 =requests .request ('post',f'{host}/api/Snatch/index',headers =O0OOO00OO000O0O0O .headers ).json ()#line:261
            if 'code'in OO0OO0OOO0O000000 :#line:263
                if OO0OO0OOO0O000000 ['code']==1 :#line:264
                    O0OO0O0OOOOOOOOO0 =OO0OO0OOO0O000000 ['data']['snatch_id']#line:265
                    OOO00OO0OO0O00000 =OO0OO0OOO0O000000 ['data']['figure_name']#line:266
                    O000O0000OO0O0OO0 =OO0OO0OOO0O000000 ['data']['now_figure_nub']#line:267
                    OO0OO0000O0000OO0 =OO0OO0OOO0O000000 ['data']['max_figure_nub']#line:268
                    if O000O0000OO0O0OO0 <OO0OO0000O0000OO0 :#line:269
                        if O0OOO00OO000O0O0O .figure (OOO00OO0OO0O00000 ):#line:270
                            O0OOO00OO000O0O0O .snatch_play_index (O0OO0O0OOOOOOOOO0 )#line:271
        except Exception as O00000OOO0OO00O0O :#line:272
            print (O00000OOO0OO00O0O )#line:273
    def snatch_play_index (O000OO0000OO0OOO0 ,O00O000O000O0O00O ):#line:276
        try :#line:277
            OO000OO00OOOO0OO0 ={'snatch_id':O00O000O000O0O00O }#line:278
            O0OOOO0000OO0O00O =requests .request ('post',f'{host}/api/Snatch/PlayIndex',headers =O000OO0000OO0OOO0 .headers ,data =OO000OO00OOOO0OO0 ).json ()#line:279
            if 'code'in O0OOOO0000OO0O00O :#line:281
                if O0OOOO0000OO0O00O ['code']==1 :#line:282
                    O00OO00O000OO0O00 =O0OOOO0000OO0O00O ['data']['surplus_figure_nub']#line:283
                    if O00OO00O000OO0O00 >0 :#line:284
                        O000OO0000OO0OOO0 .snatch_play (O00O000O000O0O00O )#line:285
        except Exception as O000O0O0OOOO0000O :#line:286
            print (O000O0O0OOOO0000O )#line:287
    def snatch_play (O0O0OO0OOOO00O0OO ,OO00OOOOOO00OOOO0 ):#line:290
        try :#line:291
            O000OO00OOO0O000O ={'snatch_id':OO00OOOOOO00OOOO0 ,'nub':'1'}#line:292
            OOOO000OO0000O0O0 =requests .request ('post',f'{host}/api/Snatch/play',headers =O0O0OO0OOOO00O0OO .headers ,data =O000OO00OOO0O000O ).json ()#line:293
            if 'code'in OOOO000OO0000O0O0 :#line:295
                if OOOO000OO0000O0O0 ['code']==1 :#line:296
                    print (f'【参与夺宝】:{OOOO000OO0000O0O0["msg"]}')#line:297
        except Exception as O0O0OOOO0O0OOOOO0 :#line:298
            print (O0O0OOOO0O0OOOOO0 )#line:299
def start ():#line:301
    try :#line:302
        update_the_validation ()#line:303
        OO0OO0OOO00OOOO00 =os_qinglong ()#line:304
        print (f"==========共找到{len(OO0OO0OOO00OOOO00)}个账号==========")#line:305
        for OOO0O00OOOOOOO00O in OO0OO0OOO00OOOO00 :#line:306
            print (f"------------正在执行第{OO0OO0OOO00OOOO00.index(OOO0O00OOOOOOO00O) + 1}个账号------------")#line:307
            O0O0O0O00O00O0O0O =Template (OOO0O00OOOOOOO00O )#line:308
            if O0O0O0O00O00O0O0O .base_info ():#line:310
                O0O0O0O00O00O0O0O .LuckyBox ()#line:312
                O0O0O0O00O00O0O0O .playInfo ()#line:314
                O0O0O0O00O00O0O0O .snatch ()#line:316
                if score_record :#line:317
                    O0O0O0O00O00O0O0O .score_record ()#line:319
                O0O0O0O00O00O0O0O .score_present ()#line:321
                time .sleep (random .randint (2 ,5 ))#line:323
            else :#line:324
                print ('token失效')#line:325
        print ('\n开始打印可以抢宝箱的数据')#line:326
        for O000O0O0O0O0OOOOO in sr :#line:327
            print (O000O0O0O0O0OOOOO .strip ())#line:328
    except Exception as O00O0OO0O0OOO00OO :#line:329
        print (O00O0OO0O0OOO00OO )#line:330
def version_of_the_validation ():#line:332
    return str ((64 -56 )/10 )#line:333
if __name__ =='__main__':#line:336
    start ()#line:337
