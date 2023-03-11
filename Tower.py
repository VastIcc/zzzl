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
        OOOOOOO0OO00000O0 =os .environ [application ].split ('\n')#line:12
        if len (OOOOOOO0OO00000O0 )>0 :#line:13
            return OOOOOOO0OO00000O0 #line:14
        else :#line:15
            print (f"{application}变量未启用")#line:16
            print ('脚本退出')#line:17
            sys .exit (1 )#line:18
    else :#line:19
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:20
        return os_built ()#line:21
def os_built ():#line:24
    if token :#line:25
        OOO00000OO0O00000 =token .split ('\n')#line:26
        if len (OOO00000OO0O00000 )>0 :#line:27
            return OOO00000OO0O00000 #line:28
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
        OOO00O000O00OO000 =gitee_validation ()#line:45
        if version_of_the_validation ()<OOO00O000O00OO000 ['Tower']['edition']:#line:46
            print (f'当前脚本名字: {OOO00O000O00OO000["Tower"]["text"]}')#line:47
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO00O000O00OO000["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:48
            print (f'更新内容=>> {OOO00O000O00OO000["Tower"]["content"]}')#line:49
        else :#line:50
            print (f'当前脚本名字: {OOO00O000O00OO000["Tower"]["text"]}')#line:51
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO00O000O00OO000["Tower"]["edition"]}   ✅')#line:52
            print (f'更新内容=>> {OOO00O000O00OO000["Tower"]["content"]}')#line:53
    except Exception as O0O0000O000000OOO :#line:54
        print (O0O0000O000000OOO )#line:55
class Template :#line:58
    def __init__ (OO000O0OOO0OOO0O0 ,OOO00O00O00O00O00 ):#line:60
        try :#line:61
            OO000O0OOO0OOO0O0 .token =OOO00O00O00O00O00 .split ('&')[0 ]#line:62
            OO000O0OOO0OOO0O0 .box =OOO00O00O00O00O00 .split ('&')[1 ]#line:63
            OO000O0OOO0OOO0O0 .present_id =OOO00O00O00O00O00 .split ('&')[2 ]#line:64
            OO000O0OOO0OOO0O0 .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':versions ,'accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OO000O0OOO0OOO0O0 .token ,'server':'true','phone-type':'android',}#line:76
        except :#line:77
            print ('变量格式错误')#line:78
    def base_info (O0O0OOOOO0O000OOO ):#line:81
        global score #line:82
        try :#line:83
            O0OOO0O0OOO00OO00 =requests .request ('post',f'{host}/api/User/info',headers =O0O0OOOOO0O000OOO .headers ).json ()#line:84
            if 'code'in O0OOO0O0OOO00OO00 :#line:86
                if O0OOO0O0OOO00OO00 ['code']==1 :#line:87
                    O000O0000000O00OO =O0OOO0O0OOO00OO00 ['data']['nickname']#line:88
                    O0O0OO0O00OO00O00 =O0OOO0O0OOO00OO00 ['data']['id']#line:89
                    score =O0OOO0O0OOO00OO00 ['data']['score']#line:90
                    print (f'【账号信息】:昵称:{O000O0000000O00OO[:6]}丨ID:{O0O0OO0O00OO00O00}丨金币:{str(score)[:5]}')#line:91
                if O0OOO0O0OOO00OO00 ['code']==302 :#line:92
                    return False #line:93
            return True #line:94
        except Exception as O0OOOOO00O0O0OO0O :#line:95
            print (O0OOOOO00O0O0OO0O )#line:96
    def playInfo (O0O00O00O00OO00O0 ):#line:99
        try :#line:100
            O0OO0OO00OO0OO00O =requests .request ('post',f'{host}/api/Game/playInfo',headers =O0O00O00O00OO00O0 .headers ).json ()#line:101
            if 'code'in O0OO0OO00OO0OO00O :#line:103
                if O0OO0OO00OO0OO00O ['code']==1 :#line:104
                    O0OOO0O00O0O00O00 =O0OO0OO00OO0OO00O ['data']['play_tier']#line:105
                    O0O0OOOOOO0OO0O0O =O0OO0OO00OO0OO00O ['data']['play_tier_need_money']#line:106
                    O0O0OOO00OO0OOOOO =O0OO0OO00OO0OO00O ['data']['user_money']#line:107
                    OO0000OOO0O0OO0O0 =O0OO0OO00OO0OO00O ['data']['play_finish_money']#line:108
                    O0O00O0O0O0O000OO =O0OO0OO00OO0OO00O ['data']['surplus_play_nub']#line:109
                    print (f'【参与闯关】:层数:{O0OOO0O00O0O00O00}丨剩余:{O0O00O0O0O0O000OO}丨花费:{O0O0OOOOOO0OO0O0O}丨预计:{OO0000OOO0O0OO0O0}')#line:110
                    if float (O0O0OOOOOO0OO0O0O )<float (O0O0OOO00OO0OOOOO ):#line:111
                        if O0O00O0O0O0O000OO >0 :#line:112
                            O0O00O00O00OO00O0 .Game_index ('1')#line:113
                        else :#line:114
                            O0O00O00O00OO00O0 .Game_index ('2')#line:115
                    else :#line:116
                        O0O00O00O00OO00O0 .Game_index ('2')#line:117
        except Exception as O0O0O0O000OOO0O0O :#line:119
            print (O0O0O0O000OOO0O0O )#line:120
    def setAutoPlay (OO000OO0O000OO0O0 ):#line:123
        try :#line:124
            O00000000O00O0O0O ={'state':'1'}#line:127
            O00O0000O0O0OOO00 =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =OO000OO0O000OO0O0 .headers ,data =O00000000O00O0O0O ).json ()#line:128
            if 'code'in O00O0000O0O0OOO00 :#line:130
                if O00O0000O0O0OOO00 ['code']==1 :#line:131
                    print (f'【自动闯关】:{O00O0000O0O0OOO00["msg"]}')#line:132
                if O00O0000O0O0OOO00 ['code']==0 :#line:133
                    print (f'【自动闯关】:{O00O0000O0O0OOO00["msg"]}')#line:134
        except Exception as OO0OOOO00OO0OO000 :#line:135
            print (OO0OOOO00OO0OO000 )#line:136
    def Game_index (OO0OO00OOOO000O0O ,OOO0O00O0O0OO0OO0 ):#line:139
        try :#line:140
            O00000000OO00OO00 =requests .request ('post',f'{host}/api/Game/index',headers =OO0OO00OOOO000O0O .headers ).json ()#line:141
            if 'code'in O00000000OO00OO00 :#line:143
                if O00000000OO00OO00 ['code']==1 :#line:144
                    if O00000000OO00OO00 ['data']['is_auto_play']:#line:145
                        O0OOO0O0O0O0O0000 ='✅'#line:146
                    else :#line:147
                        O0OOO0O0O0O0O0000 ='❌'#line:148
                    if O00000000OO00OO00 ['data']['is_game_ing']:#line:150
                        OO0O0O000O0OOO00O ='✅'#line:151
                    else :#line:152
                        OO0O0O000O0OOO00O ='❌'#line:153
                    if O00000000OO00OO00 ['data']['is_vip']:#line:154
                        OO00OO00OOOO00000 ='✅'#line:155
                    else :#line:156
                        OO00OO00OOOO00000 ='❌'#line:157
                    if '正在闯关'in O00000000OO00OO00 ['data']['npc_hint']:#line:158
                        OOOO00O0O0O00OOOO =O00000000OO00OO00 ['data']['npc_hint'][:8 ]#line:159
                    else :#line:160
                        OOOO00O0O0O00OOOO =O00000000OO00OO00 ['data']['npc_hint'][:5 ]#line:161
                    print (f'【游戏状态】:自动:{O0OOO0O0O0O0O0000}丨闯关:{OO0O0O000O0OOO00O}丨VIP:{OO00OO00OOOO00000}丨{OOOO00O0O0O00OOOO}')#line:162
                    if not O00000000OO00OO00 ['data']['is_auto_play']:#line:163
                        if OOO0O00O0O0OO0OO0 =='1':#line:164
                            OO0OO00OOOO000O0O .setAutoPlay ()#line:165
        except Exception as O0O0O000O00OOO00O :#line:166
            print (O0O0O000O00OOO00O )#line:167
    def LuckyBox (O0OOO0OO00O0O0O00 ):#line:171
        global sr #line:172
        try :#line:173
            O000O0O00O0OO00O0 =requests .request ('post',f'{host}/api/LuckyBox/index',headers =O0OOO0OO00O0O0O00 .headers ).json ()#line:174
            if 'code'in O000O0O00O0OO00O0 :#line:176
                if O000O0O00O0OO00O0 ['code']==1 :#line:177
                    OO0O00OOOOOOO000O =O000O0O00O0OO00O0 ['data']['debris']#line:178
                    O0O000OOO0O0000O0 =O000O0O00O0OO00O0 ['data']['is_draw']#line:179
                    print (f'【幸运宝箱】:碎片:{str(OO0O00OOOOOOO000O).split(".")[0]}丨当前设置开启宝箱ID:{O0OOO0OO00O0O0O00.box}')#line:180
                    if not O0O000OOO0O0000O0 :#line:181
                        OOOOO000O0O000O00 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =O0OOO0OO00O0O0O00 .headers ).json ()#line:182
                        if 'code'in OOOOO000O0O000O00 :#line:184
                            if OOOOO000O0O000O00 ['code']==1 :#line:185
                                OOOO0O0OO0O00O000 =OOOOO000O0O000O00 ['data']['nub']#line:186
                                print (f'【领取碎片】:获得:{OOOO0O0OO0O00O000}')#line:187
                    for O0OO0O0O0O00OOOO0 in O000O0O00O0OO00O0 ['data']['box_list']:#line:188
                        OOO000000O0O0O000 =O0OO0O0O0O00OOOO0 ['id']#line:190
                        O0O0000000OO0OOO0 =O0OO0O0O0O00OOOO0 ['name']#line:191
                        OOO0000OO00OO0OOO =O0OO0O0O0O00OOOO0 ['inventory']#line:192
                        O00O00OO000O00OO0 =O0OO0O0O0O00OOOO0 ['need_debris']#line:193
                        if float (OOO000000O0O0O000 )==float (O0OOO0OO00O0O0O00 .box ):#line:194
                            print (f'【幸运宝箱】:名称:{O0O0000000OO0OOO0}丨需要碎片:{O00O00OO000O00OO0}丨剩余:{OOO0000OO00OO0OOO}')#line:196
                            if float (OO0O00OOOOOOO000O )>=float (O00O00OO000O00OO0 ):#line:197
                                sr .append (O0OOO0OO00O0O0O00 .token +'&'+O0OOO0OO00O0O0O00 .box )#line:198
                                if OOO0000OO00OO0OOO >0 :#line:199
                                    O00OO0OOOOOOOO000 ={'id':O0OOO0OO00O0O0O00 .box }#line:200
                                    OOO0O0OO000OOOO0O =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =O0OOO0OO00O0O0O00 .headers ,data =O00OO0OOOOOOOO000 ).json ()#line:201
                                    if 'code'in OOO0O0OO000OOOO0O :#line:203
                                        if OOO0O0OO000OOOO0O ['code']==1 :#line:204
                                            print (f'【兑换宝箱】:{OOO0O0OO000OOOO0O["msg"]}丨获得{OOO0O0OO000OOOO0O["data"]["name"]}')#line:205
        except Exception as OO00O0OOOOO00OO0O :#line:206
            print (OO00O0OOOOO00OO0O )#line:207
    def score_record (OOO00O00OO00O0000 ):#line:210
        O0O0OO000OO00O00O ={'page':'1','limit':'15','type':'2'}#line:211
        O0O0O00O0OOO0OO0O =requests .request ('post',f'{host}/api/Score/record',headers =OOO00O00OO00O0000 .headers ,data =O0O0OO000OO00O00O ).json ()#line:212
        if 'code'in O0O0O00O0OOO0OO0O :#line:214
            if O0O0O00O0OOO0OO0O ['code']==1 :#line:215
                O000OOOO000OO0OO0 =O0O0O00O0OOO0OO0O ['data']['record_list']#line:216
                if O000OOOO000OO0OO0 :#line:217
                    for OO000O0OO0OOO00O0 in O000OOOO000OO0OO0 :#line:218
                        OO0O0O0OOOO0OO00O =OO000O0OO0OOO00O0 ['user_id']#line:219
                        O00O0OOO00O00OO00 =OO000O0OO0OOO00O0 ['money']#line:220
                        OO00OOOOOOOO0O0OO =OO000O0OO0OOO00O0 ['create_time']#line:221
                        O000OOOOO0OO000O0 =OO000O0OO0OOO00O0 ['nickname']#line:222
                        print (f'【赠送记录】:昵称:{O000OOOOO0OO000O0}丨ID:{OO0O0O0OOOO0OO00O}丨金额:{O00O0OOO00O00OO00}丨时间:{OO00OOOOOOOO0O0OO[5:16]}')#line:223
    def score_present (OOOOOOOOOO000OO00 ):#line:226
        global present_nub #line:227
        try :#line:228
            if float (score )>float (score_big ):#line:229
                O00OOO000OO000OOO ={'id':OOOOOOOOOO000OO00 .present_id }#line:230
                O0O0OO0OO0OO0000O =requests .request ('post',f'{host}/api/Score/presentFindUser',headers =OOOOOOOOOO000OO00 .headers ,data =O00OOO000OO000OOO ).json ()#line:231
                if 'code'in O0O0OO0OO0OO0000O :#line:233
                    if O0O0OO0OO0OO0000O ['code']==1 :#line:234
                        O00O00OOOO0OO000O =O0O0OO0OO0OO0000O ['data']['grade']#line:235
                        if O00O00OOOO0OO000O =='0':#line:236
                            present_nub =int (float (score )/1.05 )#line:237
                        if O00O00OOOO0OO000O =='1':#line:238
                            present_nub =int (float (score )/1.1 )#line:239
                if present_nub >1 :#line:240
                    O00000O0O0O00O0O0 ={'present_id':OOOOOOOOOO000OO00 .present_id ,'present_nub':present_nub }#line:241
                    OO0O0OOOO00OOOOOO =requests .request ('post',f'{host}/api/Score/present',headers =OOOOOOOOOO000OO00 .headers ,data =O00000O0O0O00O0O0 ).json ()#line:242
                    if 'code'in OO0O0OOOO00OOOOOO :#line:244
                        if OO0O0OOOO00OOOOOO ['code']==1 :#line:245
                            print (f'【赠送金币】:ID:{OOOOOOOOOO000OO00.present_id}丨金币:{present_nub}丨{OO0O0OOOO00OOOOOO["msg"]}')#line:246
                        elif OO0O0OOOO00OOOOOO ['code']==0 :#line:247
                            print (f'【赠送金币】:ID:{OOOOOOOOOO000OO00.present_id}丨金币:{present_nub}丨{OO0O0OOOO00OOOOOO["msg"]}')#line:248
                        else :#line:249
                            print (OO0O0OOOO00OOOOOO )#line:250
        except Exception as OO00000O0OO00OOO0 :#line:251
            print (OO00000O0OO00OOO0 )#line:252
def start ():#line:255
    try :#line:256
        update_the_validation ()#line:257
        OO0000OOOO00O0OOO =os_qinglong ()#line:258
        print (f"==========共找到{len(OO0000OOOO00O0OOO)}个账号==========")#line:259
        for OO0O00O0O0O000O00 in OO0000OOOO00O0OOO :#line:260
            print (f"------------正在执行第{OO0000OOOO00O0OOO.index(OO0O00O0O0O000O00) + 1}个账号------------")#line:261
            OOOOOO00OOO00O0OO =Template (OO0O00O0O0O000O00 )#line:262
            if OOOOOO00OOO00O0OO .base_info ():#line:264
                OOOOOO00OOO00O0OO .LuckyBox ()#line:266
                OOOOOO00OOO00O0OO .playInfo ()#line:268
                if score_record :#line:269
                    OOOOOO00OOO00O0OO .score_record ()#line:271
                OOOOOO00OOO00O0OO .score_present ()#line:273
                time .sleep (random .randint (2 ,5 ))#line:275
            else :#line:276
                print ('token失效')#line:277
        print ('\n开始打印可以抢宝箱的数据')#line:278
        for O0OO0OO0O0O0000O0 in sr :#line:279
            print (O0OO0OO0O0O0000O0 .strip ())#line:280
    except Exception as OO0OOO00O000OO0O0 :#line:281
        print (OO0OOO00O000OO0O0 )#line:282
def version_of_the_validation ():#line:284
    return str ((62 -56 )/10 )#line:285
if __name__ =='__main__':#line:288
    start ()#line:289
