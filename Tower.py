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
@ 版本 0.6
"""
##################################配置区##################################
score_record = False        # 赠送记录
score_big = '50000'         # 大于5才赠送
##################################配置区##################################
##################################下面不要动##################################
sr =[]#line:1
score =0 #line:2
present_nub =0 #line:3
versions ='1.1.8'#line:4
application ='qc_token'#line:5
token =''#line:6
host ='https://qct.qitusky.cn'#line:8
git ='https://gitee.com'#line:9
def os_qinglong ():#line:10
    if application in os .environ :#line:11
        OO00OOO00OOO00OO0 =os .environ [application ].split ('\n')#line:12
        if len (OO00OOO00OOO00OO0 )>0 :#line:13
            return OO00OOO00OOO00OO0 #line:14
        else :#line:15
            print (f"{application}变量未启用")#line:16
            print ('脚本退出')#line:17
            sys .exit (1 )#line:18
    else :#line:19
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:20
        return os_built ()#line:21
def os_built ():#line:24
    if token :#line:25
        OO000O00O00OOOO0O =token .split ('\n')#line:26
        if len (OO000O00O00OOOO0O )>0 :#line:27
            return OO000O00O00OOOO0O #line:28
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
        OO0OO0OOO0OOO0O00 =gitee_validation ()#line:45
        if version_of_the_validation ()<OO0OO0OOO0OOO0O00 ['Tower']['edition']:#line:46
            print (f'当前脚本名字: {OO0OO0OOO0OOO0O00["Tower"]["text"]}')#line:47
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OO0OOO0OOO0O00["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:48
            print (f'更新内容=>> {OO0OO0OOO0OOO0O00["Tower"]["content"]}')#line:49
        else :#line:50
            print (f'当前脚本名字: {OO0OO0OOO0OOO0O00["Tower"]["text"]}')#line:51
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OO0OOO0OOO0O00["Tower"]["edition"]}   ✅')#line:52
            print (f'更新内容=>> {OO0OO0OOO0OOO0O00["Tower"]["content"]}')#line:53
    except Exception as O00OO00O0O000O0O0 :#line:54
        print (O00OO00O0O000O0O0 )#line:55
class Template :#line:58
    def __init__ (O00OOOOO0000OO0O0 ,O0O0O0OO0OOOO00O0 ):#line:60
        try :#line:61
            O00OOOOO0000OO0O0 .token =O0O0O0OO0OOOO00O0 .split ('&')[0 ]#line:62
            O00OOOOO0000OO0O0 .box =O0O0O0OO0OOOO00O0 .split ('&')[1 ]#line:63
            O00OOOOO0000OO0O0 .present_id =O0O0O0OO0OOOO00O0 .split ('&')[2 ]#line:64
            O00OOOOO0000OO0O0 .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':versions ,'accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':O00OOOOO0000OO0O0 .token ,'server':'true','phone-type':'android',}#line:76
        except :#line:77
            print ('变量格式错误')#line:78
    def base_info (O00OOO0O00O0OOO00 ):#line:81
        global score #line:82
        try :#line:83
            OO00OO00O0O00OO0O =requests .request ('post',f'{host}/api/User/info',headers =O00OOO0O00O0OOO00 .headers ).json ()#line:84
            if 'code'in OO00OO00O0O00OO0O :#line:86
                if OO00OO00O0O00OO0O ['code']==1 :#line:87
                    O000OO000000OOO0O =OO00OO00O0O00OO0O ['data']['nickname']#line:88
                    O00O00000000O0O0O =OO00OO00O0O00OO0O ['data']['id']#line:89
                    score =OO00OO00O0O00OO0O ['data']['score']#line:90
                    print (f'【账号信息】:昵称:{O000OO000000OOO0O[:6]}丨ID:{O00O00000000O0O0O}丨金币:{str(score)[:5]}')#line:91
                if OO00OO00O0O00OO0O ['code']==302 :#line:92
                    return False #line:93
            return True #line:94
        except Exception as O0O0O0OO0000OOOO0 :#line:95
            print (O0O0O0OO0000OOOO0 )#line:96
    def playInfo (OO0O000O0OO00OO0O ):#line:99
        try :#line:100
            OO0000O0O00000OO0 =requests .request ('post',f'{host}/api/Game/playInfo',headers =OO0O000O0OO00OO0O .headers ).json ()#line:101
            if 'code'in OO0000O0O00000OO0 :#line:103
                if OO0000O0O00000OO0 ['code']==1 :#line:104
                    OO000OOOO000O0O0O =OO0000O0O00000OO0 ['data']['play_tier']#line:105
                    O0O0O0OOO0O000OOO =OO0000O0O00000OO0 ['data']['play_tier_need_money']#line:106
                    O0OO00OOO000000OO =OO0000O0O00000OO0 ['data']['user_money']#line:107
                    OOOO00O0000000OO0 =OO0000O0O00000OO0 ['data']['play_finish_money']#line:108
                    O00O00OOO0OO000O0 =OO0000O0O00000OO0 ['data']['surplus_play_nub']#line:109
                    print (f'【参与闯关】:层数:{OO000OOOO000O0O0O}丨剩余:{O00O00OOO0OO000O0}丨花费:{O0O0O0OOO0O000OOO}丨预计:{OOOO00O0000000OO0}')#line:110
                    if float (O0O0O0OOO0O000OOO )<float (O0OO00OOO000000OO ):#line:111
                        if O00O00OOO0OO000O0 >0 :#line:112
                            OO0O000O0OO00OO0O .Game_index ('1')#line:113
                        else :#line:114
                            OO0O000O0OO00OO0O .Game_index ('2')#line:115
                    else :#line:116
                        OO0O000O0OO00OO0O .Game_index ('2')#line:117
        except Exception as OOO0O00000000OO00 :#line:119
            print (OOO0O00000000OO00 )#line:120
    def setAutoPlay (O00O0000OOO0OO00O ):#line:123
        try :#line:124
            O000000OO000O0000 ={'state':'1'}#line:127
            OOO0O0O0O000OOO0O =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O00O0000OOO0OO00O .headers ,data =O000000OO000O0000 ).json ()#line:128
            if 'code'in OOO0O0O0O000OOO0O :#line:130
                if OOO0O0O0O000OOO0O ['code']==1 :#line:131
                    print (f'【自动闯关】:{OOO0O0O0O000OOO0O["msg"]}')#line:132
                if OOO0O0O0O000OOO0O ['code']==0 :#line:133
                    print (f'【自动闯关】:{OOO0O0O0O000OOO0O["msg"]}')#line:134
        except Exception as OO00O000OO0OOO0OO :#line:135
            print (OO00O000OO0OOO0OO )#line:136
    def Game_index (OO0OOOO00OOOOO0OO ,OOOOO000OOO0000OO ):#line:139
        try :#line:140
            O0OOOO0OOOO0000O0 =requests .request ('post',f'{host}/api/Game/index',headers =OO0OOOO00OOOOO0OO .headers ).json ()#line:141
            if 'code'in O0OOOO0OOOO0000O0 :#line:143
                if O0OOOO0OOOO0000O0 ['code']==1 :#line:144
                    if O0OOOO0OOOO0000O0 ['data']['is_auto_play']:#line:145
                        OO0OOOO0O0OOOO0O0 ='✅'#line:146
                    else :#line:147
                        OO0OOOO0O0OOOO0O0 ='❌'#line:148
                    if O0OOOO0OOOO0000O0 ['data']['is_game_ing']:#line:150
                        OO0O0000O0OOOO000 ='✅'#line:151
                    else :#line:152
                        OO0O0000O0OOOO000 ='❌'#line:153
                    if O0OOOO0OOOO0000O0 ['data']['is_vip']:#line:154
                        O0O00OOO0O00OO0O0 ='✅'#line:155
                    else :#line:156
                        O0O00OOO0O00OO0O0 ='❌'#line:157
                    if '正在闯关'in O0OOOO0OOOO0000O0 ['data']['npc_hint']:#line:158
                        O0O0OOOO0OOOOO0O0 =O0OOOO0OOOO0000O0 ['data']['npc_hint'][:8 ]#line:159
                    else :#line:160
                        O0O0OOOO0OOOOO0O0 =O0OOOO0OOOO0000O0 ['data']['npc_hint'][:5 ]#line:161
                    print (f'【游戏状态】:自动:{OO0OOOO0O0OOOO0O0}丨闯关:{OO0O0000O0OOOO000}丨VIP:{O0O00OOO0O00OO0O0}丨{O0O0OOOO0OOOOO0O0}')#line:162
                    if not O0OOOO0OOOO0000O0 ['data']['is_auto_play']:#line:163
                        if OOOOO000OOO0000OO =='1':#line:164
                            OO0OOOO00OOOOO0OO .setAutoPlay ()#line:165
        except Exception as O00OO0O000000OO00 :#line:166
            print (O00OO0O000000OO00 )#line:167
    def LuckyBox (OO0OO0O0000000O0O ):#line:171
        global sr #line:172
        try :#line:173
            O00OOO000OOO0O00O =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OO0OO0O0000000O0O .headers ).json ()#line:174
            if 'code'in O00OOO000OOO0O00O :#line:176
                if O00OOO000OOO0O00O ['code']==1 :#line:177
                    OOO0O00OOO00OOO0O =O00OOO000OOO0O00O ['data']['debris']#line:178
                    O0OOO0OOOOOOO0000 =O00OOO000OOO0O00O ['data']['is_draw']#line:179
                    print (f'【幸运宝箱】:碎片:{str(OOO0O00OOO00OOO0O).split(".")[0]}丨当前设置开启宝箱ID:{OO0OO0O0000000O0O.box}')#line:180
                    if not O0OOO0OOOOOOO0000 :#line:181
                        O0000OOO0OOOO00OO =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OO0OO0O0000000O0O .headers ).json ()#line:182
                        if 'code'in O0000OOO0OOOO00OO :#line:184
                            if O0000OOO0OOOO00OO ['code']==1 :#line:185
                                O0OO0000OO000000O =O0000OOO0OOOO00OO ['data']['nub']#line:186
                                print (f'【领取碎片】:获得:{O0OO0000OO000000O}')#line:187
                    for OO000OOO0O0OO000O in O00OOO000OOO0O00O ['data']['box_list']:#line:188
                        OO0OO00000OO0OO00 =OO000OOO0O0OO000O ['id']#line:190
                        O00OOO0OO0O0000OO =OO000OOO0O0OO000O ['name']#line:191
                        O00O0OO00O0OO0OO0 =OO000OOO0O0OO000O ['inventory']#line:192
                        O00OO000O000O0OOO =OO000OOO0O0OO000O ['need_debris']#line:193
                        if float (OO0OO00000OO0OO00 )==float (OO0OO0O0000000O0O .box ):#line:194
                            print (f'【幸运宝箱】:名称:{O00OOO0OO0O0000OO}丨需要碎片:{O00OO000O000O0OOO}丨剩余:{O00O0OO00O0OO0OO0}')#line:196
                            if float (OOO0O00OOO00OOO0O )>=float (O00OO000O000O0OOO ):#line:197
                                sr .append (OO0OO0O0000000O0O .token +'&'+OO0OO0O0000000O0O .box )#line:198
                                if O00O0OO00O0OO0OO0 >0 :#line:199
                                    OO0O0OOOOO000OOO0 ={'id':OO0OO0O0000000O0O .box }#line:200
                                    O0OO0O0OO0OOOO000 =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =OO0OO0O0000000O0O .headers ,data =OO0O0OOOOO000OOO0 ).json ()#line:201
                                    if 'code'in O0OO0O0OO0OOOO000 :#line:203
                                        if O0OO0O0OO0OOOO000 ['code']==1 :#line:204
                                            print (f'【兑换宝箱】:{O0OO0O0OO0OOOO000["msg"]}丨获得{O0OO0O0OO0OOOO000["data"]["name"]}')#line:205
        except Exception as OO0OO000O00000OOO :#line:206
            print (OO0OO000O00000OOO )#line:207
    def score_record (OO0O0O0OO0O00O0OO ):#line:210
        O0000O000O00OOOOO ={'page':'1','limit':'15','type':'2'}#line:211
        O00O00O00OO0O0000 =requests .request ('post',f'{host}/api/Score/record',headers =OO0O0O0OO0O00O0OO .headers ,data =O0000O000O00OOOOO ).json ()#line:212
        if 'code'in O00O00O00OO0O0000 :#line:214
            if O00O00O00OO0O0000 ['code']==1 :#line:215
                OO00O00OO000000OO =O00O00O00OO0O0000 ['data']['record_list']#line:216
                if OO00O00OO000000OO :#line:217
                    for OO000OOOO00OO0OOO in OO00O00OO000000OO :#line:218
                        O00OOOO000OO00O0O =OO000OOOO00OO0OOO ['user_id']#line:219
                        O0O00000000OOOOO0 =OO000OOOO00OO0OOO ['money']#line:220
                        O0000OOOO00000OOO =OO000OOOO00OO0OOO ['create_time']#line:221
                        OOOO00O0OOOOOO00O =OO000OOOO00OO0OOO ['nickname']#line:222
                        print (f'【赠送记录】:昵称:{OOOO00O0OOOOOO00O}丨ID:{O00OOOO000OO00O0O}丨金额:{O0O00000000OOOOO0}丨时间:{O0000OOOO00000OOO[5:16]}')#line:223
    def score_present (OOO0OOOOOOOO0O0O0 ):#line:226
        global present_nub #line:227
        try :#line:228
            if float (score )>float (score_big ):#line:229
                O000OOO000OOO000O ={'id':OOO0OOOOOOOO0O0O0 .present_id }#line:230
                O0000O00OOOO00O00 =requests .request ('post',f'{host}/api/Score/presentFindUser',headers =OOO0OOOOOOOO0O0O0 .headers ,data =O000OOO000OOO000O ).json ()#line:231
                if 'code'in O0000O00OOOO00O00 :#line:233
                    if O0000O00OOOO00O00 ['code']==1 :#line:234
                        OOO0O0OO00OOO00O0 =O0000O00OOOO00O00 ['data']['grade']#line:235
                        if OOO0O0OO00OOO00O0 =='0':#line:236
                            present_nub =int (float (score )/1.05 )#line:237
                        if OOO0O0OO00OOO00O0 =='1':#line:238
                            present_nub =int (float (score )/1.1 )#line:239
                present_nub =int (float (score )/1.05 )#line:240
                if present_nub >1 :#line:241
                    O00O000OO00O00OOO ={'present_id':OOO0OOOOOOOO0O0O0 .present_id ,'present_nub':present_nub }#line:242
                    O0OOOO0O0OOO00O0O =requests .request ('post',f'{host}/api/Score/present',headers =OOO0OOOOOOOO0O0O0 .headers ,data =O00O000OO00O00OOO ).json ()#line:243
                    if 'code'in O0OOOO0O0OOO00O0O :#line:245
                        if O0OOOO0O0OOO00O0O ['code']==1 :#line:246
                            print (f'【赠送金币】:ID:{OOO0OOOOOOOO0O0O0.present_id}丨金币:{present_nub}丨{O0OOOO0O0OOO00O0O["msg"]}')#line:247
                        elif O0OOOO0O0OOO00O0O ['code']==0 :#line:248
                            print (f'【赠送金币】:ID:{OOO0OOOOOOOO0O0O0.present_id}丨金币:{present_nub}丨{O0OOOO0O0OOO00O0O["msg"]}')#line:249
                        else :#line:250
                            print (O0OOOO0O0OOO00O0O )#line:251
        except Exception as OOOOOOO0OOOO00OO0 :#line:252
            print (OOOOOOO0OOOO00OO0 )#line:253
def start ():#line:256
    try :#line:257
        update_the_validation ()#line:258
        OOOO0O0O0O0O0000O =os_qinglong ()#line:259
        print (f"==========共找到{len(OOOO0O0O0O0O0000O)}个账号==========")#line:260
        for O0O00OO00OO0O0O00 in OOOO0O0O0O0O0000O :#line:261
            print (f"------------正在执行第{OOOO0O0O0O0O0000O.index(O0O00OO00OO0O0O00) + 1}个账号------------")#line:262
            O00OO00O00OOOOOOO =Template (O0O00OO00OO0O0O00 )#line:263
            if O00OO00O00OOOOOOO .base_info ():#line:265
                O00OO00O00OOOOOOO .LuckyBox ()#line:267
                O00OO00O00OOOOOOO .playInfo ()#line:269
                if score_record :#line:270
                    O00OO00O00OOOOOOO .score_record ()#line:272
                O00OO00O00OOOOOOO .score_present ()#line:274
                time .sleep (random .randint (2 ,5 ))#line:276
            else :#line:277
                print ('token失效')#line:278
        print ('开始打印可以抢宝箱的数据')#line:279
        for O0OO00O0OO0OOO00O in sr :#line:280
            print (O0OO00O0OO0OOO00O .strip ())#line:281
    except Exception as O000O00000O0OO0OO :#line:282
        print (O000O00000O0OO0OO )#line:283
def version_of_the_validation ():#line:285
    return str ((62 -56 )/10 )#line:286
if __name__ =='__main__':#line:289
    start ()#line:290
