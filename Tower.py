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
@ 版本 0.7
"""
##################################配置区##################################
score_record = False        # 赠送记录
score_big = '50000'         # 大于5才赠送
##################################配置区##################################
##################################下面不要动##################################

sr =[]#line:1
score =0 #line:2
versions ='1.1.9'#line:3
application ='qc_token'#line:4
token =''#line:5
host ='https://qct.qitusky.cn'#line:7
git ='https://gitee.com'#line:8
def os_qinglong ():#line:9
    if application in os .environ :#line:10
        OOOOO0OOO00O0OOOO =os .environ [application ].split ('\n')#line:11
        if len (OOOOO0OOO00O0OOOO )>0 :#line:12
            return OOOOO0OOO00O0OOOO #line:13
        else :#line:14
            print (f"{application}变量未启用")#line:15
            print ('脚本退出')#line:16
            sys .exit (1 )#line:17
    else :#line:18
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:19
        return os_built ()#line:20
def os_built ():#line:23
    if token :#line:24
        O0000OOO000O0O0OO =token .split ('\n')#line:25
        if len (O0000OOO000O0O0OO )>0 :#line:26
            return O0000OOO000O0O0OO #line:27
    else :#line:28
        print (f"内置变量为空")#line:29
        print ('脚本结束')#line:30
        sys .exit (0 )#line:31
def gitee_validation ():#line:34
    try :#line:35
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:36
    except :#line:37
        sys .exit (0 )#line:38
def update_the_validation ():#line:42
    try :#line:43
        O0O0OOO00OOO00OOO =gitee_validation ()#line:44
        if version_of_the_validation ()<O0O0OOO00OOO00OOO ['Tower']['edition']:#line:45
            print (f'当前脚本名字: {O0O0OOO00OOO00OOO["Tower"]["text"]}')#line:46
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0OOO00OOO00OOO["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:47
            print (f'更新内容=>> {O0O0OOO00OOO00OOO["Tower"]["content"]}')#line:48
        else :#line:49
            print (f'当前脚本名字: {O0O0OOO00OOO00OOO["Tower"]["text"]}')#line:50
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0OOO00OOO00OOO["Tower"]["edition"]}   ✅')#line:51
            print (f'更新内容=>> {O0O0OOO00OOO00OOO["Tower"]["content"]}')#line:52
    except Exception as O00O0OOOOOOO0OO00 :#line:53
        print (O00O0OOOOOOO0OO00 )#line:54
class Template :#line:57
    def __init__ (O0O000O0O0000O00O ,OO00OOOO000000000 ):#line:59
        try :#line:60
            O0O000O0O0000O00O .token =OO00OOOO000000000 .split ('&')[0 ]#line:61
            O0O000O0O0000O00O .box =OO00OOOO000000000 .split ('&')[1 ]#line:62
            O0O000O0O0000O00O .present_id =OO00OOOO000000000 .split ('&')[2 ]#line:63
            O0O000O0O0000O00O .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':versions ,'accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':O0O000O0O0000O00O .token ,'server':'true','phone-type':'android',}#line:75
        except :#line:76
            print ('变量格式错误')#line:77
    def base_info (OO0O000OO0O00000O ):#line:80
        global score #line:81
        try :#line:82
            OO000OOO0000OOO0O =requests .request ('post',f'{host}/api/User/info',headers =OO0O000OO0O00000O .headers ).json ()#line:83
            if 'code'in OO000OOO0000OOO0O :#line:85
                if OO000OOO0000OOO0O ['code']==1 :#line:86
                    O0OOO0OO0000OOO0O =OO000OOO0000OOO0O ['data']['nickname']#line:87
                    OOOOOOO00O0O0OOOO =OO000OOO0000OOO0O ['data']['id']#line:88
                    score =OO000OOO0000OOO0O ['data']['score']#line:89
                    print (f'【账号信息】:昵称:{O0OOO0OO0000OOO0O[:6]}丨ID:{OOOOOOO00O0O0OOOO}丨金币:{str(score)[:5]}')#line:90
                if OO000OOO0000OOO0O ['code']==302 :#line:91
                    return False #line:92
            return True #line:93
        except Exception as O0O00O0OOOOOO0OOO :#line:94
            print (O0O00O0OOOOOO0OOO )#line:95
    def playInfo (O00OOOO00O0O0OOO0 ):#line:98
        try :#line:99
            O00000O000000O0O0 =requests .request ('post',f'{host}/api/Game/playInfo',headers =O00OOOO00O0O0OOO0 .headers ).json ()#line:100
            if 'code'in O00000O000000O0O0 :#line:102
                if O00000O000000O0O0 ['code']==1 :#line:103
                    O0O00OO0OO0O0O00O =O00000O000000O0O0 ['data']['play_tier']#line:104
                    OOOO00OO00OOOOOO0 =O00000O000000O0O0 ['data']['play_tier_need_money']#line:105
                    OO0OO000O000O0OOO =O00000O000000O0O0 ['data']['user_money']#line:106
                    O00OO0OOOOO00O0OO =O00000O000000O0O0 ['data']['play_finish_money']#line:107
                    OO00OOOOO00O0O0O0 =O00000O000000O0O0 ['data']['surplus_play_nub']#line:108
                    print (f'【参与闯关】:层数:{O0O00OO0OO0O0O00O}丨剩余:{OO00OOOOO00O0O0O0}丨花费:{OOOO00OO00OOOOOO0}丨预计:{O00OO0OOOOO00O0OO}')#line:109
                    if float (OOOO00OO00OOOOOO0 )<float (OO0OO000O000O0OOO ):#line:110
                        if OO00OOOOO00O0O0O0 >0 :#line:111
                            O00OOOO00O0O0OOO0 .Game_index ('1')#line:112
                        else :#line:113
                            O00OOOO00O0O0OOO0 .Game_index ('2')#line:114
                    else :#line:115
                        O00OOOO00O0O0OOO0 .Game_index ('2')#line:116
        except Exception as OO0O0OOO00OO000O0 :#line:118
            print (OO0O0OOO00OO000O0 )#line:119
    def setAutoPlay (OO0OO0000OO000OO0 ):#line:122
        try :#line:123
            OO00OOO000OO0O0O0 ={'state':'1'}#line:126
            O000O0OOOO00O0O00 =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =OO0OO0000OO000OO0 .headers ,data =OO00OOO000OO0O0O0 ).json ()#line:127
            if 'code'in O000O0OOOO00O0O00 :#line:129
                if O000O0OOOO00O0O00 ['code']==1 :#line:130
                    print (f'【自动闯关】:{O000O0OOOO00O0O00["msg"]}')#line:131
                if O000O0OOOO00O0O00 ['code']==0 :#line:132
                    print (f'【自动闯关】:{O000O0OOOO00O0O00["msg"]}')#line:133
        except Exception as OOOO00OOOOO00OOO0 :#line:134
            print (OOOO00OOOOO00OOO0 )#line:135
    def Game_index (OOOOOOOO0O0OOO0OO ,O0OOO0000OO00OOOO ):#line:138
        try :#line:139
            O00O0O0OOO0O0OO0O =requests .request ('post',f'{host}/api/Game/index',headers =OOOOOOOO0O0OOO0OO .headers ).json ()#line:140
            if 'code'in O00O0O0OOO0O0OO0O :#line:142
                if O00O0O0OOO0O0OO0O ['code']==1 :#line:143
                    if O00O0O0OOO0O0OO0O ['data']['is_auto_play']:#line:144
                        O0O0OO0O0O00O0O00 ='✅'#line:145
                    else :#line:146
                        O0O0OO0O0O00O0O00 ='❌'#line:147
                    if O00O0O0OOO0O0OO0O ['data']['is_game_ing']:#line:149
                        O0O0OOO00O00O0O00 ='✅'#line:150
                    else :#line:151
                        O0O0OOO00O00O0O00 ='❌'#line:152
                    if O00O0O0OOO0O0OO0O ['data']['is_vip']:#line:153
                        O000000O0O0000000 ='✅'#line:154
                    else :#line:155
                        O000000O0O0000000 ='❌'#line:156
                    if '正在闯关'in O00O0O0OOO0O0OO0O ['data']['npc_hint']:#line:157
                        O000O000OO0O00O00 =O00O0O0OOO0O0OO0O ['data']['npc_hint'][:8 ]#line:158
                    else :#line:159
                        O000O000OO0O00O00 =O00O0O0OOO0O0OO0O ['data']['npc_hint'][:5 ]#line:160
                    print (f'【游戏状态】:自动:{O0O0OO0O0O00O0O00}丨闯关:{O0O0OOO00O00O0O00}丨VIP:{O000000O0O0000000}丨{O000O000OO0O00O00}')#line:161
                    if not O00O0O0OOO0O0OO0O ['data']['is_auto_play']:#line:162
                        if O0OOO0000OO00OOOO =='1':#line:163
                            OOOOOOOO0O0OOO0OO .setAutoPlay ()#line:164
        except Exception as O000OO0O0OOO0OOOO :#line:165
            print (O000OO0O0OOO0OOOO )#line:166
    def LuckyBox (O0OO0O00O00O000O0 ):#line:170
        global sr #line:171
        try :#line:172
            OOOO00OO00OOOOO0O =requests .request ('post',f'{host}/api/LuckyBox/index',headers =O0OO0O00O00O000O0 .headers ).json ()#line:173
            if 'code'in OOOO00OO00OOOOO0O :#line:175
                if OOOO00OO00OOOOO0O ['code']==1 :#line:176
                    OOOO0O0O0O00O0000 =OOOO00OO00OOOOO0O ['data']['debris']#line:177
                    O0OO00O0O000O0OOO =OOOO00OO00OOOOO0O ['data']['is_draw']#line:178
                    print (f'【幸运宝箱】:碎片:{str(OOOO0O0O0O00O0000).split(".")[0]}丨当前设置开启宝箱ID:{O0OO0O00O00O000O0.box}')#line:179
                    if not O0OO00O0O000O0OOO :#line:180
                        O000OO0O00OOO00O0 =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =O0OO0O00O00O000O0 .headers ).json ()#line:181
                        if 'code'in O000OO0O00OOO00O0 :#line:183
                            if O000OO0O00OOO00O0 ['code']==1 :#line:184
                                O0O0O0OO00OOO000O =O000OO0O00OOO00O0 ['data']['nub']#line:185
                                print (f'【领取碎片】:获得:{O0O0O0OO00OOO000O}')#line:186
                    for OOOO0OOOO0OO00000 in OOOO00OO00OOOOO0O ['data']['box_list']:#line:187
                        OO000O0000000O00O =OOOO0OOOO0OO00000 ['id']#line:189
                        O00OOO0O00O0OO0O0 =OOOO0OOOO0OO00000 ['name']#line:190
                        O0O0O00O0OO0O0O0O =OOOO0OOOO0OO00000 ['inventory']#line:191
                        O0O0O0O0OOOO00000 =OOOO0OOOO0OO00000 ['need_debris']#line:192
                        if float (OO000O0000000O00O )==float (O0OO0O00O00O000O0 .box ):#line:193
                            print (f'【幸运宝箱】:名称:{O00OOO0O00O0OO0O0}丨需要碎片:{O0O0O0O0OOOO00000}丨剩余:{O0O0O00O0OO0O0O0O}')#line:195
                            if float (OOOO0O0O0O00O0000 )>=float (O0O0O0O0OOOO00000 ):#line:196
                                sr .append (O0OO0O00O00O000O0 .token +'&'+O0OO0O00O00O000O0 .box )#line:197
                                if O0O0O00O0OO0O0O0O >0 :#line:198
                                    O0OOOOO000OO0O0OO ={'id':O0OO0O00O00O000O0 .box }#line:199
                                    OO0O0000OOOO0000O =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =O0OO0O00O00O000O0 .headers ,data =O0OOOOO000OO0O0OO ).json ()#line:200
                                    if 'code'in OO0O0000OOOO0000O :#line:202
                                        if OO0O0000OOOO0000O ['code']==1 :#line:203
                                            print (f'【兑换宝箱】:{OO0O0000OOOO0000O["msg"]}丨获得{OO0O0000OOOO0000O["data"]["name"]}')#line:204
        except Exception as O0O0O0000000O0000 :#line:205
            print (O0O0O0000000O0000 )#line:206
    def score_record (OO0OO0O00OOO00OO0 ):#line:209
        OOO000OO0O00000O0 ={'page':'1','limit':'15','type':'2'}#line:210
        O000O0OOO000OOO0O =requests .request ('post',f'{host}/api/Score/record',headers =OO0OO0O00OOO00OO0 .headers ,data =OOO000OO0O00000O0 ).json ()#line:211
        if 'code'in O000O0OOO000OOO0O :#line:213
            if O000O0OOO000OOO0O ['code']==1 :#line:214
                OOOO0O0O0O00O00OO =O000O0OOO000OOO0O ['data']['record_list']#line:215
                if OOOO0O0O0O00O00OO :#line:216
                    for OO00O00OOO0O0O000 in OOOO0O0O0O00O00OO :#line:217
                        O0O000OO0OO0O00OO =OO00O00OOO0O0O000 ['user_id']#line:218
                        O000O0O0O000O0O00 =OO00O00OOO0O0O000 ['money']#line:219
                        O0000O0O0O00OOOO0 =OO00O00OOO0O0O000 ['create_time']#line:220
                        O0000000OOO00O0O0 =OO00O00OOO0O0O000 ['nickname']#line:221
                        print (f'【赠送记录】:昵称:{O0000000OOO00O0O0}丨ID:{O0O000OO0OO0O00OO}丨金额:{O000O0O0O000O0O00}丨时间:{O0000O0O0O00OOOO0[5:16]}')#line:222
    def score_present (O0O00O000000OOO00 ):#line:225
        try :#line:226
            if float (score )>float (score_big ):#line:227
                OO0O00OO000O00000 ={'id':O0O00O000000OOO00 .present_id }#line:228
                O00OOO000O0OOOO0O =requests .request ('post',f'{host}/api/Score/presentFindUser',headers =O0O00O000000OOO00 .headers ,data =OO0O00OO000O00000 ).json ()#line:229
                if 'code'in O00OOO000O0OOOO0O :#line:231
                    if O00OOO000O0OOOO0O ['code']==1 :#line:232
                        OOOOO0O000O00O0O0 =O00OOO000O0OOOO0O ['data']['service_charge']#line:233
                        OOO00O0000O0000OO =int (float (score )/(1 +(int (OOOOO0O000O00O0O0 )/100 )))#line:234
                        if OOO00O0000O0000OO >1 :#line:235
                            O00OO00OOO0OOO0O0 ={'present_id':O0O00O000000OOO00 .present_id ,'present_nub':OOO00O0000O0000OO }#line:236
                            O0OOO0O0000O0OOOO =requests .request ('post',f'{host}/api/Score/present',headers =O0O00O000000OOO00 .headers ,data =O00OO00OOO0OOO0O0 ).json ()#line:237
                            if 'code'in O0OOO0O0000O0OOOO :#line:239
                                if O0OOO0O0000O0OOOO ['code']==1 :#line:240
                                    print (f'【赠送金币】:ID:{O0O00O000000OOO00.present_id}丨金币:{OOO00O0000O0000OO}丨{O0OOO0O0000O0OOOO["msg"]}')#line:241
                                elif O0OOO0O0000O0OOOO ['code']==0 :#line:242
                                    print (f'【赠送金币】:ID:{O0O00O000000OOO00.present_id}丨金币:{OOO00O0000O0000OO}丨{O0OOO0O0000O0OOOO["msg"]}')#line:243
                                else :#line:244
                                    print (O0OOO0O0000O0OOOO )#line:245
        except Exception as O000000OOOO0OOOO0 :#line:246
            print (O000000OOOO0OOOO0 )#line:247
def start ():#line:250
    try :#line:251
        update_the_validation ()#line:252
        O0O00O00OO00O0OOO =os_qinglong ()#line:253
        print (f"==========共找到{len(O0O00O00OO00O0OOO)}个账号==========")#line:254
        for OO0O00OO0O0O0OOO0 in O0O00O00OO00O0OOO :#line:255
            print (f"------------正在执行第{O0O00O00OO00O0OOO.index(OO0O00OO0O0O0OOO0) + 1}个账号------------")#line:256
            O0OO0000OO00O0O00 =Template (OO0O00OO0O0O0OOO0 )#line:257
            if O0OO0000OO00O0O00 .base_info ():#line:259
                O0OO0000OO00O0O00 .LuckyBox ()#line:261
                O0OO0000OO00O0O00 .playInfo ()#line:263
                if score_record :#line:264
                    O0OO0000OO00O0O00 .score_record ()#line:266
                O0OO0000OO00O0O00 .score_present ()#line:268
                time .sleep (random .randint (2 ,5 ))#line:270
            else :#line:271
                print ('token失效')#line:272
        print ('\n开始打印可以抢宝箱的数据')#line:273
        for OOOO00OOOOOOOOOO0 in sr :#line:274
            print (OOOO00OOOOOOOOOO0 .strip ())#line:275
    except Exception as OOOOOO0OOOO0OOOO0 :#line:276
        print (OOOOOO0OOOO0OOOO0 )#line:277
def version_of_the_validation ():#line:279
    return str ((63 -56 )/10 )#line:280
if __name__ =='__main__':#line:283
    start ()#line:284
