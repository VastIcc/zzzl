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
score_big = '500000'         # 大于5才赠送
##################################配置区##################################
##################################下面不要动##################################
sr =[]#line:1
score =0 #line:2
versions ='1.1.8'#line:3
application ='qc_token'#line:4
token =''#line:5
host ='https://qct.qitusky.cn'#line:7
git ='https://gitee.com'#line:8
def os_qinglong ():#line:9
    if application in os .environ :#line:10
        O0OOOOOO0OOOO0O00 =os .environ [application ].split ('\n')#line:11
        if len (O0OOOOOO0OOOO0O00 )>0 :#line:12
            return O0OOOOOO0OOOO0O00 #line:13
        else :#line:14
            print (f"{application}变量未启用")#line:15
            print ('脚本退出')#line:16
            sys .exit (1 )#line:17
    else :#line:18
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:19
        return os_built ()#line:20
def os_built ():#line:23
    if token :#line:24
        O0O000O00O000OOO0 =token .split ('\n')#line:25
        if len (O0O000O00O000OOO0 )>0 :#line:26
            return O0O000O00O000OOO0 #line:27
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
        OO0O0O0O000000O0O =gitee_validation ()#line:44
        if version_of_the_validation ()<OO0O0O0O000000O0O ['Tower']['edition']:#line:45
            print (f'当前脚本名字: {OO0O0O0O000000O0O["Tower"]["text"]}')#line:46
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0O0O000000O0O["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:47
            print (f'更新内容=>> {OO0O0O0O000000O0O["Tower"]["content"]}')#line:48
        else :#line:49
            print (f'当前脚本名字: {OO0O0O0O000000O0O["Tower"]["text"]}')#line:50
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0O0O000000O0O["Tower"]["edition"]}   ✅')#line:51
            print (f'更新内容=>> {OO0O0O0O000000O0O["Tower"]["content"]}')#line:52
    except Exception as OO000OOOOO00O0OO0 :#line:53
        print (OO000OOOOO00O0OO0 )#line:54
class Template :#line:57
    def __init__ (OOOO0O0O0O000OO0O ,O00O000O00OO00O0O ):#line:59
        try :#line:60
            OOOO0O0O0O000OO0O .token =O00O000O00OO00O0O .split ('&')[0 ]#line:61
            OOOO0O0O0O000OO0O .box =O00O000O00OO00O0O .split ('&')[1 ]#line:62
            OOOO0O0O0O000OO0O .present_id =O00O000O00OO00O0O .split ('&')[2 ]#line:63
            OOOO0O0O0O000OO0O .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':versions ,'accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OOOO0O0O0O000OO0O .token ,'server':'true','phone-type':'android',}#line:75
        except :#line:76
            print ('变量格式错误')#line:77
    def base_info (O0O0OO0O00OO0OOO0 ):#line:80
        global score #line:81
        try :#line:82
            OOO0OO00OO000OO0O =requests .request ('post',f'{host}/api/User/info',headers =O0O0OO0O00OO0OOO0 .headers ).json ()#line:83
            if 'code'in OOO0OO00OO000OO0O :#line:85
                if OOO0OO00OO000OO0O ['code']==1 :#line:86
                    OOO0O0OOO0OO0O000 =OOO0OO00OO000OO0O ['data']['nickname']#line:87
                    O0OOOOO0O0OO00OOO =OOO0OO00OO000OO0O ['data']['id']#line:88
                    score =OOO0OO00OO000OO0O ['data']['score']#line:89
                    print (f'【账号信息】:昵称:{OOO0O0OOO0OO0O000[:6]}丨ID:{O0OOOOO0O0OO00OOO}丨金币:{str(score)[:5]}')#line:90
                if OOO0OO00OO000OO0O ['code']==302 :#line:91
                    return False #line:92
            return True #line:93
        except Exception as OO000OO00O0OO00O0 :#line:94
            print (OO000OO00O0OO00O0 )#line:95
    def playInfo (OOO00OOO0O0OO0O0O ):#line:98
        try :#line:99
            OOO000O0O0000OO00 =requests .request ('post',f'{host}/api/Game/playInfo',headers =OOO00OOO0O0OO0O0O .headers ).json ()#line:100
            if 'code'in OOO000O0O0000OO00 :#line:102
                if OOO000O0O0000OO00 ['code']==1 :#line:103
                    OOO0OO000O00OO000 =OOO000O0O0000OO00 ['data']['play_tier']#line:104
                    O00OOOOO0O0O00O00 =OOO000O0O0000OO00 ['data']['play_tier_need_money']#line:105
                    OO00O0OO00000O00O =OOO000O0O0000OO00 ['data']['user_money']#line:106
                    O00O00OOO00OOOO0O =OOO000O0O0000OO00 ['data']['play_finish_money']#line:107
                    O000O0O0O00000000 =OOO000O0O0000OO00 ['data']['surplus_play_nub']#line:108
                    print (f'【参与闯关】:层数:{OOO0OO000O00OO000}丨剩余:{O000O0O0O00000000}丨花费:{O00OOOOO0O0O00O00}丨预计:{O00O00OOO00OOOO0O}')#line:109
                    if float (O00OOOOO0O0O00O00 )<float (OO00O0OO00000O00O ):#line:110
                        if O000O0O0O00000000 >0 :#line:111
                            OOO00OOO0O0OO0O0O .Game_index ('1')#line:112
                        else :#line:113
                            OOO00OOO0O0OO0O0O .Game_index ('2')#line:114
                    else :#line:115
                        OOO00OOO0O0OO0O0O .Game_index ('2')#line:116
        except Exception as O000O0O0000OOOOO0 :#line:118
            print (O000O0O0000OOOOO0 )#line:119
    def setAutoPlay (O0OOOOOOO0O0OO000 ):#line:122
        try :#line:123
            OOOO00O0OO00O0O00 ={'state':'1'}#line:126
            O0O0OOO000O00000O =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =O0OOOOOOO0O0OO000 .headers ,data =OOOO00O0OO00O0O00 ).json ()#line:127
            if 'code'in O0O0OOO000O00000O :#line:129
                if O0O0OOO000O00000O ['code']==1 :#line:130
                    print (f'【自动闯关】:{O0O0OOO000O00000O["msg"]}')#line:131
                if O0O0OOO000O00000O ['code']==0 :#line:132
                    print (f'【自动闯关】:{O0O0OOO000O00000O["msg"]}')#line:133
        except Exception as OO0OO00O0000O0OOO :#line:134
            print (OO0OO00O0000O0OOO )#line:135
    def Game_index (OOOOO0O0OOOO00OO0 ,O00O000000OOOO00O ):#line:138
        try :#line:139
            OOOO00OO0O0OO0O0O =requests .request ('post',f'{host}/api/Game/index',headers =OOOOO0O0OOOO00OO0 .headers ).json ()#line:140
            if 'code'in OOOO00OO0O0OO0O0O :#line:142
                if OOOO00OO0O0OO0O0O ['code']==1 :#line:143
                    if OOOO00OO0O0OO0O0O ['data']['is_auto_play']:#line:144
                        O0000OOO00OO00OO0 ='✅'#line:145
                    else :#line:146
                        O0000OOO00OO00OO0 ='❌'#line:147
                    if OOOO00OO0O0OO0O0O ['data']['is_game_ing']:#line:149
                        O0O00000O0O000O00 ='✅'#line:150
                    else :#line:151
                        O0O00000O0O000O00 ='❌'#line:152
                    if OOOO00OO0O0OO0O0O ['data']['is_vip']:#line:153
                        O00OOOO0OO00O0000 ='✅'#line:154
                    else :#line:155
                        O00OOOO0OO00O0000 ='❌'#line:156
                    if '正在闯关'in OOOO00OO0O0OO0O0O ['data']['npc_hint']:#line:157
                        OO00O00OOO00O0OOO =OOOO00OO0O0OO0O0O ['data']['npc_hint'][:8 ]#line:158
                    else :#line:159
                        OO00O00OOO00O0OOO =OOOO00OO0O0OO0O0O ['data']['npc_hint'][:5 ]#line:160
                    print (f'【游戏状态】:自动:{O0000OOO00OO00OO0}丨闯关:{O0O00000O0O000O00}丨VIP:{O00OOOO0OO00O0000}丨{OO00O00OOO00O0OOO}')#line:161
                    if not OOOO00OO0O0OO0O0O ['data']['is_auto_play']:#line:162
                        if O00O000000OOOO00O =='1':#line:163
                            OOOOO0O0OOOO00OO0 .setAutoPlay ()#line:164
        except Exception as O00O0OOOOOOO0O0O0 :#line:165
            print (O00O0OOOOOOO0O0O0 )#line:166
    def LuckyBox (OOOOOOOOO0O000O00 ):#line:170
        global sr #line:171
        try :#line:172
            OOOO0OOO0OOO00000 =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OOOOOOOOO0O000O00 .headers ).json ()#line:173
            if 'code'in OOOO0OOO0OOO00000 :#line:175
                if OOOO0OOO0OOO00000 ['code']==1 :#line:176
                    O0OOOO00OOOOO0OO0 =OOOO0OOO0OOO00000 ['data']['debris']#line:177
                    O0OO00O00O00O00OO =OOOO0OOO0OOO00000 ['data']['is_draw']#line:178
                    print (f'【幸运宝箱】:碎片:{str(O0OOOO00OOOOO0OO0).split(".")[0]}丨当前设置开启宝箱ID:{OOOOOOOOO0O000O00.box}')#line:179
                    if not O0OO00O00O00O00OO :#line:180
                        O0OOO000OO00O000O =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OOOOOOOOO0O000O00 .headers ).json ()#line:181
                        if 'code'in O0OOO000OO00O000O :#line:183
                            if O0OOO000OO00O000O ['code']==1 :#line:184
                                O00O0O000OOOO00O0 =O0OOO000OO00O000O ['data']['nub']#line:185
                                print (f'【领取碎片】:获得:{O00O0O000OOOO00O0}')#line:186
                    for OO0OO0O0O0OO00OO0 in OOOO0OOO0OOO00000 ['data']['box_list']:#line:187
                        O0OOO0OOO000OO0OO =OO0OO0O0O0OO00OO0 ['id']#line:189
                        OOO0000O000OOO000 =OO0OO0O0O0OO00OO0 ['name']#line:190
                        O0OOOOOOO00O0O0O0 =OO0OO0O0O0OO00OO0 ['inventory']#line:191
                        O000O0O000000O0O0 =OO0OO0O0O0OO00OO0 ['need_debris']#line:192
                        if float (O0OOO0OOO000OO0OO )==float (OOOOOOOOO0O000O00 .box ):#line:193
                            print (f'【幸运宝箱】:名称:{OOO0000O000OOO000}丨需要碎片:{O000O0O000000O0O0}丨剩余:{O0OOOOOOO00O0O0O0}')#line:195
                            if float (O0OOOO00OOOOO0OO0 )>=float (O000O0O000000O0O0 ):#line:196
                                sr .append (OOOOOOOOO0O000O00 .token +'&'+OOOOOOOOO0O000O00 .box )#line:197
                                if O0OOOOOOO00O0O0O0 >0 :#line:198
                                    OO000O0OO0000O00O ={'id':OOOOOOOOO0O000O00 .box }#line:199
                                    OO00OOO000O0O0000 =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =OOOOOOOOO0O000O00 .headers ,data =OO000O0OO0000O00O ).json ()#line:200
                                    if 'code'in OO00OOO000O0O0000 :#line:202
                                        if OO00OOO000O0O0000 ['code']==1 :#line:203
                                            print (f'【兑换宝箱】:{OO00OOO000O0O0000["msg"]}丨获得{OO00OOO000O0O0000["data"]["name"]}')#line:204
        except Exception as O0OO0OOO0OOOOO0O0 :#line:205
            print (O0OO0OOO0OOOOO0O0 )#line:206
    def score_record (O0OO000000000O00O ):#line:209
        O000OO0000OOOOOOO ={'page':'1','limit':'15','type':'2'}#line:210
        O0O0O000OO000000O =requests .request ('post',f'{host}/api/Score/record',headers =O0OO000000000O00O .headers ,data =O000OO0000OOOOOOO ).json ()#line:211
        if 'code'in O0O0O000OO000000O :#line:213
            if O0O0O000OO000000O ['code']==1 :#line:214
                OOOOO00O000O00O00 =O0O0O000OO000000O ['data']['record_list']#line:215
                if OOOOO00O000O00O00 :#line:216
                    for OO0OO000OO0OO0OO0 in OOOOO00O000O00O00 :#line:217
                        OOO00OOO000OO000O =OO0OO000OO0OO0OO0 ['user_id']#line:218
                        OO000000O0O00OOOO =OO0OO000OO0OO0OO0 ['money']#line:219
                        O0O0OOOO000O0O0OO =OO0OO000OO0OO0OO0 ['create_time']#line:220
                        OO0000O00000O000O =OO0OO000OO0OO0OO0 ['nickname']#line:221
                        print (f'【赠送记录】:昵称:{OO0000O00000O000O}丨ID:{OOO00OOO000OO000O}丨金额:{OO000000O0O00OOOO}丨时间:{O0O0OOOO000O0O0OO[5:16]}')#line:222
    def score_present (OOO0O00O00OO00O0O ):#line:225
        try :#line:226
            if float (score )>float (score_big ):#line:227
                O0O0OO0O0O0OOOO00 ={'id':OOO0O00O00OO00O0O .present_id }#line:228
                O00OOO0OO000O0O00 =requests .request ('post',f'{host}/api/Score/presentFindUser',headers =OOO0O00O00OO00O0O .headers ,data =O0O0OO0O0O0OOOO00 ).json ()#line:229
                if 'code'in O00OOO0OO000O0O00 :#line:231
                    if O00OOO0OO000O0O00 ['code']==1 :#line:232
                        OOO0O0O00OO0OO00O =O00OOO0OO000O0O00 ['data']['service_charge']#line:233
                        O00OO000O00OOO0OO =int (float (score )/(1 +(int (OOO0O0O00OO0OO00O )/100 )))#line:234
                        if O00OO000O00OOO0OO >1 :#line:235
                            O000O0O000OOO0O00 ={'present_id':OOO0O00O00OO00O0O .present_id ,'present_nub':O00OO000O00OOO0OO }#line:236
                            O0OO000O00O00OOOO =requests .request ('post',f'{host}/api/Score/present',headers =OOO0O00O00OO00O0O .headers ,data =O000O0O000OOO0O00 ).json ()#line:237
                            if 'code'in O0OO000O00O00OOOO :#line:239
                                if O0OO000O00O00OOOO ['code']==1 :#line:240
                                    print (f'【赠送金币】:ID:{OOO0O00O00OO00O0O.present_id}丨金币:{O00OO000O00OOO0OO}丨{O0OO000O00O00OOOO["msg"]}')#line:241
                                elif O0OO000O00O00OOOO ['code']==0 :#line:242
                                    print (f'【赠送金币】:ID:{OOO0O00O00OO00O0O.present_id}丨金币:{O00OO000O00OOO0OO}丨{O0OO000O00O00OOOO["msg"]}')#line:243
                                else :#line:244
                                    print (O0OO000O00O00OOOO )#line:245
        except Exception as O0OO0O000O0OOOO0O :#line:246
            print (O0OO0O000O0OOOO0O )#line:247
def start ():#line:250
    try :#line:251
        update_the_validation ()#line:252
        OO00OOOO000O000O0 =os_qinglong ()#line:253
        print (f"==========共找到{len(OO00OOOO000O000O0)}个账号==========")#line:254
        for O0O0OO0O0O00OOOOO in OO00OOOO000O000O0 :#line:255
            print (f"------------正在执行第{OO00OOOO000O000O0.index(O0O0OO0O0O00OOOOO) + 1}个账号------------")#line:256
            O0OO00O0000OOO00O =Template (O0O0OO0O0O00OOOOO )#line:257
            if O0OO00O0000OOO00O .base_info ():#line:259
                O0OO00O0000OOO00O .LuckyBox ()#line:261
                O0OO00O0000OOO00O .playInfo ()#line:263
                if score_record :#line:264
                    O0OO00O0000OOO00O .score_record ()#line:266
                O0OO00O0000OOO00O .score_present ()#line:268
                time .sleep (random .randint (2 ,5 ))#line:270
            else :#line:271
                print ('token失效')#line:272
        print ('\n开始打印可以抢宝箱的数据')#line:273
        for O0O0OOO000OOO0O00 in sr :#line:274
            print (O0O0OOO000OOO0O00 .strip ())#line:275
    except Exception as O000O0O0O00O00OO0 :#line:276
        print (O000O0O0O00O00OO0 )#line:277
def version_of_the_validation ():#line:279
    return str ((63 -56 )/10 )#line:280
if __name__ =='__main__':#line:283
    start ()#line:284

