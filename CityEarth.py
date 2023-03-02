# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import hashlib
    import json
    import requests
    import random
    import threading
    from notify import send
except Exception as E:
    t = re.findall("d '(.*?)'", str(E))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: 8 1-23/2 * * *
@ new Env('生城世朝')
@ 项目地址  https://sc19319.oss-cn-hangzhou.aliyuncs.com/scsc/prod/1.9.3.1.S4195.apk
@ 抓取  http://scsc.sc19319.com 的authorization值
@ 青龙变量  青龙配置文件 export ce_token="authorization&赠送金种子数量大于&赠送金种子id" 
@ 如果你有20金种子填10就会赠 填21就不会赠送  不赠送全填 999999     多号换行
@ 变量示范    export ce_token="557b8069-1234-4ae7-9e29-b7871f91541b&999999&999999"  用&符号分开数据
@ 版本  2.7
"""
application = 'ce_token'  # 变量名
token = ''

##################################配置区##################################
energy =True #line:1
time_xx =random .randint (12 ,18 )#line:2
version ='3.1.41954131'#line:6
git ='https://gitee.com'#line:7
host ='http://scsc.sc19319.com'#line:8
golden_seed =0 #line:9
msg_list =[]#line:10
def start ():#line:12
    try :#line:13
        update_the_validation ()#line:14
        OOOO0O00OO0000OO0 =os_qinglong ()#line:15
        print (f"==========共找到{len(OOOO0O00OO0000OO0)}个账号==========")#line:16
        for OO0O0OO00OO00OO00 in OOOO0O00OO0000OO0 :#line:17
            O0OO0000OO000O0OO =[]#line:18
            print (f"------------正在执行第{OOOO0O00OO0000OO0.index(OO0O0OO00OO00OO00) + 1}个账号------------")#line:19
            OOO0OOO00O0OOO000 =CityEarth (OO0O0OO00OO00OO00 ,O0OO0000OO000O0OO )#line:20
            def O0OO0OOO00OOO0O00 ():#line:22
                if OOO0OOO00O0OOO000 .base_info ():#line:24
                    OOO0OOO00O0OOO000 .sealing ()#line:26
                    OOO0OOO00O0OOO000 .invitenum ()#line:28
                    OOO0OOO00O0OOO000 .game_map ()#line:30
                    OOO0OOO00O0OOO000 .friends_invitation ()#line:32
                    OOO0OOO00O0OOO000 .energy ()#line:34
                    OOO0OOO00O0OOO000 .add_clover ()#line:36
                    OOO0OOO00O0OOO000 .propsraffle ()#line:38
                    OOO0OOO00O0OOO000 .synthetic ()#line:40
                    OOO0OOO00O0OOO000 .crops_illustrated ()#line:42
                    OOO0OOO00O0OOO000 .give_gold ()#line:44
                    OOO0OOO00O0OOO000 .withdraw ()#line:46
            OO0O0O0O000OO0OO0 =threading .Thread (target =O0OO0OOO00OOO0O00 )#line:48
            OO0O0O0O000OO0OO0 .start ()#line:49
            time .sleep (time_xx )#line:50
        print (f"------------正在处理推送通知------------")#line:51
        time .sleep (0.5 )#line:52
        O00000000OO0000OO =format_msg ()#line:53
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00000000OO0000OO +' ')#line:54
    except Exception as O000OO000O00OOOO0 :#line:55
        print (O000OO000O00OOOO0 )#line:56
def give_gold (OOOOO00O00OOO0OOO ,O00OOO0OO00OO0OO0 ):#line:59
        try :#line:60
            OO000000O00000O00 =f'_doneeNo={OOOOO00O00OOO0OOO}&quantity={int(O00OOO0OO00OO0OO0)}_{timi_new()}'#line:61
            O0O000O0OO0OO0O00 ={'source':'scsc','authorization':os_qinglong ()[0 ].split ('&')[0 ],'timestamp':str (timi_new ()),'sign':sign (OO000000O00000O00 ),'signstring':OO000000O00000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:72
            OOO0OO0OOO00OO0O0 ={"quantity":int (O00OOO0OO00OO0OO0 ),"doneeNo":OOOOO00O00OOO0OOO }#line:76
            O00OOOO000OO0O0OO =requests .request ('post',f'{host}/finance/give-gold',headers =O0O000O0OO0OO0O00 ,data =OOO0OO0OOO00OO0O0 ).json ()#line:77
            if 'status'in O00OOOO000OO0O0OO :#line:79
                if O00OOOO000OO0O0OO ['status']==200 :#line:80
                    if O00OOOO000OO0O0OO ['data']:#line:81
                        print (f'【赠送种子】:赠送{int(O00OOO0OO00OO0OO0)}种子给{OOOOO00O00OOO0OOO}成功')#line:82
                if O00OOOO000OO0O0OO ['status']==401 :#line:83
                    print (f'【赠送种子】:{O00OOOO000OO0O0OO["message"]}')#line:84
                if O00OOOO000OO0O0OO ['status']==500 :#line:85
                    print (f'【赠送种子】:{O00OOOO000OO0O0OO["message"]}')#line:86
        except Exception as O0OOOOOO0OOO00O00 :#line:87
            print (O0OOOOOO0OOO00O00 )#line:88
def sign (O00O0OO0O00O00000 ):#line:91
    O00O00000O000000O =hashlib .md5 (O00O0OO0O00O00000 .encode ()).hexdigest ()#line:92
    OOOOOOOO0OOO0OO00 ="scsc%^&*"+O00O00000O000000O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:93
    OOOOO0O0OOOO0000O =hashlib .md5 (OOOOOOOO0OOO0OO00 .encode ()).hexdigest ()#line:94
    return OOOOO0O0OOOO0000O #line:95
def format_msg ():#line:97
    O0O00O0O0OO00OO0O =""#line:98
    for OOO000O00O00O0O00 in msg_list :#line:99
        O0O00O0O0OO00OO0O +=str (OOO000O00O00O0O00 )+"\r\n"#line:100
    return O0O00O0O0OO00OO0O #line:101
def timi_new ():#line:103
    return str (int (time .time ()*1000 ))#line:104
class CityEarth :#line:107
    def __init__ (O00OOO000OOOOO0OO ,OO0O000O000000O0O ,OO0O0O0OO00O0O0OO ):#line:109
        try :#line:110
            O00OOO000OOOOO0OO .msg =OO0O0O0OO00O0O0OO #line:111
            O00OOO000OOOOO0OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:112
            O00OOO000OOOOO0OO .token =OO0O000O000000O0O .split ('&')[0 ]#line:113
            O00OOO000OOOOO0OO .innerId =OO0O000O000000O0O .split ('&')[1 ]#line:114
            O00OOO000OOOOO0OO .doneeNo =OO0O000O000000O0O .split ('&')[2 ]#line:115
        except :#line:116
            print ('变量格式错误')#line:117
    def base_info (O0O0OO000OOOOOOO0 ):#line:120
        try :#line:121
            O0O0OO000OOOOOOO0 .watched_ad ()#line:123
            OOO0O00OO0000OOO0 =f'__{timi_new()}'#line:124
            OOOOOOOOO0OOO0OOO ={'source':'scsc','authorization':O0O0OO000OOOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00OO0000OOO0 ),'signstring':OOO0O00OO0000OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:135
            O000OOOO00O00O00O =requests .request ('get',f'{host}/user',headers =OOOOOOOOO0OOO0OOO ).json ()#line:136
            if 'status'in O000OOOO00O00O00O :#line:138
                if O000OOOO00O00O00O ['status']==200 :#line:139
                    O0000000OOOO0O000 =O000OOOO00O00O00O ['data']['nickname']#line:140
                    O0000OOOOO0000O0O =O000OOOO00O00O00O ['data']['inner_id']#line:141
                    O0O00OO0OOO0000O0 =O000OOOO00O00O00O ['data']['assets']['gold']#line:142
                    O0OO000O00OOOO000 =O000OOOO00O00O00O ['data']['level']#line:143
                    print (f'【账号信息】:昵称:{O0000000OOOO0O000[:5]}丨ID:{O0000OOOOO0000O0O}丨等级:{O0OO000O00OOOO000}丨金种子:{str(O0O00OO0OOO0000O0).split(".")[0]}')#line:144
                if O000OOOO00O00O00O ['status']==401 :#line:145
                    print (O000OOOO00O00O00O ['message'])#line:146
                    O0O0OO000OOOOOOO0 .msg .append ('有账号失效了')#line:147
                    return False #line:148
                if O000OOOO00O00O00O ['status']==500 :#line:149
                    return False #line:150
            return True #line:151
        except Exception as OO0O0000O0OO0O00O :#line:152
            print (OO0O0000O0OO0O00O )#line:153
    def sealing (OOOOOOO0OO00OOO0O ):#line:156
        try :#line:157
            OOO0O0O0OO0O0OOOO =f'__{timi_new()}'#line:158
            O0OO0O0000000O000 ={'source':'scsc','authorization':OOOOOOO0OO00OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OO0O0OOOO ),'signstring':OOO0O0O0OO0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OO0O0000000O000 )#line:170
            requests .request ('get',f'{host}/packsack/list',headers =O0OO0O0000000O000 )#line:171
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OO0O0000000O000 )#line:172
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OO0O0000000O000 )#line:173
            requests .request ('get',f'{host}/user',headers =O0OO0O0000000O000 )#line:174
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OO0O0000000O000 )#line:175
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OO0O0000000O000 )#line:176
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OO0O0000000O000 )#line:177
            requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O0000000O000 )#line:178
            requests .request ('get',f'{host}/assets',headers =O0OO0O0000000O000 )#line:179
        except Exception as OOO00O0000OO00OO0 :#line:180
            print (OOO00O0000OO00OO0 )#line:181
    def withdraw (OOO000O0O00O0000O ):#line:185
        OOOOO00O000OO0O0O =f'__{timi_new()}'#line:186
        O000OO00OOO00OOO0 ={'source':'scsc','authorization':OOO000O0O00O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O000OO0O0O ),'signstring':OOOOO00O000OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:197
        OO0O000000OOO00OO =requests .request ('get',f'{host}/assets',headers =O000OO00OOO00OOO0 ).json ()#line:198
        if 'status'in OO0O000000OOO00OO :#line:200
            if OO0O000000OOO00OO ['status']==200 :#line:201
                O0O00O0O00OOOOO00 =OO0O000000OOO00OO ['data']['cash']#line:202
                if float (O0O00O0O00OOOOO00 )>20 :#line:203
                    OOOOO00O000OO0O0O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:204
                    O000OO00OOO00OOO0 ={'authorization':OOO000O0O00O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O000OO0O0O ),'signstring':OOOOO00O000OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
                    OOO00OO0O0O00OO00 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:215
                    OO0OOOO000O000OO0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O000OO00OOO00OOO0 ,data =OOO00OO0O0O00OO00 ).json ()#line:217
                    print (OO0OOOO000O000OO0 )#line:218
    def invitenum (O00OOOO00OOOOOOO0 ):#line:221
        OO0OOO000000O0O00 =f'__{timi_new()}'#line:222
        OOOO0000O0OOO0O0O ={'source':'scsc','authorization':O00OOOO00OOOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO000000O0O00 ),'signstring':OO0OOO000000O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:233
        OOOOOOO0O0OO00O00 =requests .request ('get',f'{host}/invite/invitenum',headers =OOOO0000O0OOO0O0O ).json ()#line:234
        if 'status'in OOOOOOO0O0OO00O00 :#line:236
            if OOOOOOO0O0OO00O00 ['status']==200 :#line:237
                OO00O000O0O00O0OO =OOOOOOO0O0OO00O00 ['data']['invited_count']#line:238
                O00000OOOO0OOOOO0 =OOOOOOO0O0OO00O00 ['data']['invited_second_count']#line:239
                print (f'【我的邀请】:直邀好友:{OO00O000O0O00O0OO}丨间邀好友:{O00000OOOO0OOOOO0}')#line:240
    def game_map (OOO00O00O00O000O0 ):#line:243
        try :#line:244
            O0OO0OO0OO0O0OO00 =f'__{timi_new()}'#line:245
            O0OO0000OO0OOO0O0 ={'source':'scsc','authorization':OOO00O00O00O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0OO0O0OO00 ),'signstring':O0OO0OO0OO0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:256
            O0OO0OOO0O0OO0OO0 =requests .request ('get',f'{host}/game/map',headers =O0OO0000OO0OOO0O0 ).json ()#line:257
            if 'status'in O0OO0OOO0O0OO0OO0 :#line:259
                if O0OO0OOO0O0OO0OO0 ['status']==200 :#line:260
                    for OO0O00000O0O0O00O in O0OO0OOO0O0OO0OO0 ['data']['list'][0 ]['crops']:#line:261
                        O0OOOO0O00OOO0OO0 =OO0O00000O0O0O00O ['level']#line:263
                        if O0OOOO0O00OOO0OO0 ==41 :#line:264
                            OOOOO0O000O0O000O =OO0O00000O0O0O00O ['crop_name']#line:265
                            O0O0000O00O000OOO =OO0O00000O0O0O00O ['count']#line:266
                            if O0O0000O00O000OOO >0 :#line:267
                                print (f'【农业资产】:{OOOOO0O000O0O000O}丨数量:{O0O0000O00O000OOO}')#line:268
        except Exception as OOO0O0O00OO0O0OO0 :#line:269
            print (OOO0O0O00OO0O0OO0 )#line:270
    def give_gold (OOOOOOOO0OOOO0OO0 ):#line:273
        try :#line:274
            O0O0OOOO00OOO0O0O =f'__{timi_new()}'#line:275
            OO000000O00O0O000 ={'source':'scsc','authorization':OOOOOOOO0OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOO00OOO0O0O ),'signstring':O0O0OOOO00OOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:286
            OO000O00O0O000O0O =requests .request ('get',f'{host}/user',headers =OO000000O00O0O000 ).json ()#line:287
            if 'status'in OO000O00O0O000O0O :#line:288
                if OO000O00O0O000O0O ['status']==200 :#line:289
                    if float (OOOOOOOO0OOOO0OO0 .doneeNo )!=0 :#line:290
                        OO0OOO0OOO00O0O0O =OO000O00O0O000O0O ['data']['assets']['gold']#line:291
                        if float (OO0OOO0OOO00O0O0O )>float (OOOOOOOO0OOOO0OO0 .innerId ):#line:292
                            OO000O00O0OOO00O0 =int (float (OO0OOO0OOO00O0O0O )/1.1 )#line:293
                            O0O0OOOO00OOO0O0O =f'_doneeNo={OOOOOOOO0OOOO0OO0.doneeNo}&quantity={OO000O00O0OOO00O0}_{timi_new()}'#line:294
                            OO000000O00O0O000 ={'source':'scsc','authorization':OOOOOOOO0OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOO00OOO0O0O ),'signstring':O0O0OOOO00OOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:305
                            OO0OO000O00OOO0O0 ={"quantity":OO000O00O0OOO00O0 ,"doneeNo":OOOOOOOO0OOOO0OO0 .doneeNo }#line:309
                            OOOOOO0O0OO00000O =requests .request ('post',f'{host}/finance/give-gold',headers =OO000000O00O0O000 ,data =OO0OO000O00OOO0O0 ).json ()#line:310
                            if 'status'in OOOOOO0O0OO00000O :#line:312
                                if OOOOOO0O0OO00000O ['status']==200 :#line:313
                                    if OOOOOO0O0OO00000O ['data']:#line:314
                                        print (f'【赠送种子】:赠送{OO000O00O0OOO00O0}种子给{OOOOOOOO0OOOO0OO0.doneeNo}成功')#line:315
                    else :#line:316
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:317
        except Exception as OO0O0O00000O0OOOO :#line:318
            print (OO0O0O00000O0OOOO )#line:319
    def invitation (O0O0OO0O0000OOOO0 ):#line:321
        try :#line:322
            _O0O0OOOOO0OOO0O0O =float (bundled_def ())/4 #line:323
            O0O00O00000O0OOOO =f'_innerId={int(_O0O0OOOOO0OOO0O0O)}_{timi_new()}'#line:324
            O00O0000O0O0OOO00 ={'source':'scsc','authorization':O0O0OO0O0000OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00000O0OOOO ),'signstring':O0O00O00000O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:335
            O00OO0OO000O0000O ={"innerId":int (_O0O0OOOOO0OOO0O0O )}#line:336
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00O0000O0O0OOO00 ,data =O00OO0OO000O0000O )#line:337
        except Exception as OOOOOO0OO00000OO0 :#line:338
            print (OOOOOO0OO00000OO0 )#line:339
    def winning_rewards (O00O00OO0000OO000 ):#line:342
        try :#line:343
            O00OO0O0O00OOOOO0 =f'__{timi_new()}'#line:344
            O0OO00O0O00O0O00O ={'source':'scsc','authorization':O00O00OO0000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0O00OOOOO0 ),'signstring':O00OO0O0O00OOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:355
            O00OO0OO0OOOOO00O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OO00O0O00O0O00O ).json ()#line:356
            if 'status'in O00OO0OO0OOOOO00O :#line:358
                if O00OO0OO0OOOOO00O ['status']==200 :#line:359
                    if O00OO0OO0OOOOO00O ['data']['amount']:#line:360
                        O0000OOOO0O0O000O =O00OO0OO0OOOOO00O ['data']['amount']['gold']#line:361
                        return O0000OOOO0O0O000O #line:362
                    else :#line:363
                        return 0 #line:364
        except Exception as O0OO0O00OO00O0O00 :#line:365
            print (O0OO0O00OO00O0O00 )#line:366
    def certification (OO00O0OO0O000000O ):#line:369
        try :#line:370
            O0000OOO0O0000O00 =f'__{timi_new()}'#line:371
            OO0OO0OOO0OOOO00O ={'source':'scsc','authorization':OO00O0OO0O000000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOO0O0000O00 ),'signstring':O0000OOO0O0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:382
            O00O00OOOO0000OO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0OO0OOO0OOOO00O ).json ()#line:383
            if 'status'in O00O00OOOO0000OO0 :#line:385
                if O00O00OOOO0000OO0 ['status']==200 :#line:386
                    if O00O00OOOO0000OO0 ['data']['result']:#line:387
                        O00OO0O0OOOO00OO0 =O00O00OOOO0000OO0 ['data']['nick_name']#line:388
                        return O00OO0O0OOOO00OO0 #line:389
                    else :#line:390
                        return '未实名'#line:391
        except Exception as OO0O00OOO0O0000OO :#line:392
            print (OO0O00OOO0O0000OO )#line:393
    def crops_illustrated (OO0O0O0O00O00OOOO ):#line:396
        try :#line:397
            O00000O0OOO0OOO00 =f'__{timi_new()}'#line:398
            OOOO0OOOO00OO000O ={'source':'scsc','authorization':OO0O0O0O00O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0OOO0OOO00 ),'signstring':O00000O0OOO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:409
            OOOO0OO0O0000OO0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOOO0OOOO00OO000O ).json ()#line:410
            if 'status'in OOOO0OO0O0000OO0O :#line:412
                if OOOO0OO0O0000OO0O ['status']==200 :#line:413
                    OOOO000000OO00000 =OOOO0OO0O0000OO0O ['data'][0 ]['crops']#line:414
                    for O000OOO0OO0000O0O in OOOO000000OO00000 :#line:415
                        if O000OOO0OO0000O0O ['ill_clover_award']:#line:416
                            if float (O000OOO0OO0000O0O ['ill_clover_award'])>1 :#line:417
                                if O000OOO0OO0000O0O ['is_finish']:#line:418
                                    if not O000OOO0OO0000O0O ['is_getit']:#line:419
                                        if OO0O0O0O00O00OOOO .certification ()!='未实名':#line:420
                                            O00000O0OOO0OOO00 =f'_award_level={O000OOO0OO0000O0O["level"]}_{timi_new()}'#line:421
                                            OOOO0OOOO00OO000O ={'source':'scsc','authorization':OO0O0O0O00O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0OOO0OOO00 ),'signstring':O00000O0OOO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:432
                                            O0OOO00000OOO000O ={"award_level":O000OOO0OO0000O0O ['level']}#line:433
                                            OO000O00O0OO000OO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOOO0OOOO00OO000O ,json =O0OOO00000OOO000O ).json ()#line:435
                                            if 'status'in OO000O00O0OO000OO :#line:436
                                                if OO000O00O0OO000OO ['status']==200 :#line:437
                                                    O0OO00000OO0OO0O0 =OO000O00O0OO000OO ['data']['ill_clover_award']#line:438
                                                    print (f'【图鉴奖励】:领取{O000OOO0OO0000O0O["crop_name"]}成就丨奖励{O0OO00000OO0OO0O0}☘️')#line:440
                                                if OO000O00O0OO000OO ['status']==500 :#line:441
                                                    print (f'【图鉴奖励】:{OO000O00O0OO000OO["message"]}')#line:442
        except Exception as OOO00OO0O00OO0O00 :#line:443
            print (OOO00OO0O00OO0O00 )#line:444
    def watched_ad (O0000000OOOOO00O0 ):#line:447
        try :#line:448
            OOO0OO0OO0OO00O0O =f'__{timi_new()}'#line:449
            O00OO0O0OOO00O0OO ={'source':'scsc','authorization':O0000000OOOOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OO0OO00O0O ),'signstring':OOO0OO0OO0OO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:460
            OO0OO0O0O0OOO0000 =requests .request ('get',f'{host}/game/getAllData',headers =O00OO0O0OOO00O0OO ).json ()#line:461
            if 'status'in OO0OO0O0O0OOO0000 :#line:463
                if OO0OO0O0O0OOO0000 ['status']==200 :#line:464
                    if 'offlineInfo'in OO0OO0O0O0OOO0000 ['data']:#line:465
                        time .sleep (random .randint (3 ,5 ))#line:466
                        OO000O0O0O00O0000 =OO0OO0O0O0OOO0000 ['data']['offlineInfo']['off_minute']#line:467
                        OO0O00O000000OO0O =float (OO0OO0O0O0OOO0000 ['data']['silver'])/1000000000000 #line:468
                        time .sleep (1 )#line:469
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00OO0O0OOO00O0OO ).json ()#line:470
                        time .sleep (2 )#line:471
                        OO0O0O0OOO0000OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O00OO0O0OOO00O0OO ).json ()#line:472
                        if 'status'in OO0O0O0OOO0000OO0 :#line:474
                            if OO0O0O0OOO0000OO0 ['status']==200 :#line:475
                                O00OOOOO0OO000OOO =float (OO0O0O0OOO0000OO0 ['data']['silver'])/1000000000000 #line:476
                                O0O000O0000000O0O =str (O00OOOOO0OO000OOO -OO0O00O000000OO0O )[:6 ]#line:477
                                print (f'【离线奖励】:翻倍离线{OO000O0O0O00O0000}分钟奖励🌱数量:{O0O000O0000000O0O}t粒')#line:478
        except Exception as OOO000O0OOO00000O :#line:479
            print (OOO000O0OOO00000O )#line:480
    def user_ad (O0OOO0OOO00OOO0OO ):#line:483
        try :#line:484
            OO0OO000OO00O0OOO =f'__{timi_new()}'#line:485
            OOO0000O00OO0OO0O ={'source':'scsc','authorization':O0OOO0OOO00OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OO00O0OOO ),'signstring':OO0OO000OO00O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:496
            O0OO0O0OOO0OO0000 =requests .request ('get',f'{host}/user/ad',headers =OOO0000O00OO0OO0O ).json ()#line:497
            if 'status'in O0OO0O0OOO0OO0000 :#line:499
                if O0OO0O0OOO0OO0000 ['status']==200 :#line:500
                    OOOOO00O0OO0O0000 =O0OO0O0OOO0OO0000 ['data']['max_time']#line:501
                    O00000000O0O00O00 =O0OO0O0OOO0OO0000 ['data']['watch_time']#line:502
                    O00O0OO0O000OO00O =O0OO0O0OOO0OO0000 ['data']['added_time']#line:503
                    print (f'【获取种子】:获取🌱剩余{O00O0OO0O000OO00O + OOOOO00O0OO0O0000 - O00000000O0O00O00}次丨好友提供:{O00O0OO0O000OO00O}次')#line:504
                    if O00O0OO0O000OO00O +OOOOO00O0OO0O0000 -O00000000O0O00O00 >0 :#line:505
                        time .sleep (random .randint (16 ,19 ))#line:506
                        OO000OOOOO0O0O0OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO0000O00OO0OO0O ).json ()#line:507
                        if 'status'in OO000OOOOO0O0O0OO :#line:509
                            if OO000OOOOO0O0O0OO ['status']==200 :#line:510
                                O00OOO0OO00OOOO0O =float (OO000OOOOO0O0O0OO ['data']['silver'])/1000000000000 #line:511
                                print (f'【获取种子】:获得🌱:{int(O00OOO0OO00OOOO0O)}t粒')#line:512
                                return True #line:513
                            if OO000OOOOO0O0O0OO ['status']==500 :#line:514
                                O0OO00O00000OOOO0 =OO000OOOOO0O0O0OO ['message']#line:515
                                print (f'【获取种子】:{O0OO00O00000OOOO0}')#line:516
                                return False #line:517
        except Exception as O0OO0000000000OOO :#line:518
            print (O0OO0000000000OOO )#line:519
    def synthetic (O000O0O0OOOO00O0O ):#line:522
        global id ,g #line:523
        try :#line:524
            OO0OO0OO0000O0OOO =O000O0O0OOOO00O0O .level_new ()#line:525
            OOO000O00OOOOO000 =random .randint (9 ,11 )#line:526
            O0O00OO0OO00000OO =f'_site=8&targetSite={OOO000O00OOOOO000}_{timi_new()}'#line:527
            O0O0O0O000OOO0000 ={'source':'scsc','authorization':O000O0O0OOOO00O0O .token ,'timestamp':timi_new (),'sign':sign (O0O00OO0OO00000OO ),'signstring':O0O00OO0OO00000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:538
            OO0000O0O00O00O0O ={"site":int (8 ),"targetSite":int (OOO000O00OOOOO000 )}#line:539
            requests .request ('post',f'{host}/game/crops/move',headers =O0O0O0O000OOO0000 ,json =OO0000O0O00O00O0O )#line:540
            while True :#line:541
                O0OO0O00O00OO0O00 =f'__{timi_new()}'#line:542
                O0OOOOO000O0O0000 ={'source':'scsc','authorization':O000O0O0OOOO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O00OO0O00 ),'signstring':O0OO0O00O00OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:553
                OO000O0OO00O0OOOO =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOOO000O0O0000 ).json ()#line:554
                if 'status'in OO000O0OO00O0OOOO :#line:556
                    if OO000O0OO00O0OOOO ['status']==200 :#line:557
                        OO00O00O000OOO000 =OO000O0OO00O0OOOO ['data']['cropList']#line:558
                        OOO00O00OO00O0OO0 =OO000O0OO00O0OOOO ['data']['gameCoreDataDBid']#line:559
                        OO00OOOO0O0O0O0O0 =float (OO000O0OO00O0OOOO ['data']['silver'])/1000000000000 #line:560
                        OOOOOO000O00O000O =0 #line:565
                        for OOOOOOOOOOO000000 in OO00O00O000OOO000 :#line:566
                            if not OOOOOOOOOOO000000 :#line:567
                                O000OO00O0OO00OOO =f'_crop_id={OOO00O00OO00O0OO0}&site={OOOOOO000O00O000O}_{O000O0O0OOOO00O0O.time}'#line:568
                                OOO0O0O00O0O0OOOO ={'source':'scsc','authorization':O000O0O0OOOO00O0O .token ,'timestamp':O000O0O0OOOO00O0O .time ,'sign':sign (O000OO00O0OO00OOO ),'signstring':O000OO00O0OO00OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:578
                                OO0OO0O000000OOO0 ={"site":OOOOOO000O00O000O ,"crop_id":OOO00O00OO00O0OO0 }#line:579
                                OO000OOOO0OO00OOO =requests .request ('post',f'{host}/game/crops/buy',headers =OOO0O0O00O0O0OOOO ,data =OO0OO0O000000OOO0 ).json ()#line:580
                                time .sleep (random .randint (1 ,3 )/10 )#line:582
                                if 'status'in OO000OOOO0OO00OOO :#line:583
                                    if OO000OOOO0OO00OOO ['status']==200 :#line:584
                                        if OO000OOOO0OO00OOO ['message']=='种子数量不足':#line:585
                                            OO0OO0OO0000O0OOO =O000O0O0OOOO00O0O .level_new ()#line:586
                                            print (f'【种植合成】:{OO000OOOO0OO00OOO["message"]}')#line:587
                                            if not O000O0O0OOOO00O0O .user_ad ():#line:588
                                                return False #line:589
                                    if OO000OOOO0OO00OOO ['status']==500 :#line:590
                                        print (f'【种植合成】:{OO000OOOO0OO00OOO["message"]}')#line:591
                                        return False #line:592
                            OOOOOO000O00O000O +=1 #line:593
                        OO00OOO000OOO0OOO =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOOO000O0O0000 ).json ()#line:594
                        OO00000OOOOO0OO0O =OO00OOO000OOO0OOO ['data']['cropList']#line:595
                        OOOO0000OO00000OO =False #line:596
                        for OOOOOOOOOOO000000 in range (12 ):#line:597
                            id =OO00000OOOOO0OO0O [OOOOOOOOOOO000000 ]['level']#line:598
                            if float (OO0OO0OO0000O0OOO )-float (id )>9 :#line:599
                                OO0O0OOOO0000O0OO =f'_site={OOOOOOOOOOO000000}_{timi_new()}'#line:600
                                O0O0O00OOOOO000OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000O0O0OOOO00O0O .token ,'timestamp':timi_new (),'sign':sign (OO0O0OOOO0000O0OO ),'signstring':OO0O0OOOO0000O0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:611
                                O00OOOOOOOOOOOO00 ={"site":OOOOOOOOOOO000000 }#line:612
                                OO000000000OOOOO0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O0O00OOOOO000OO ,data =O00OOOOOOOOOOOO00 ).json ()#line:614
                                if 'status'in OO000000000OOOOO0 :#line:615
                                    if OO000000000OOOOO0 ['status']==200 :#line:616
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:617
                            if id !=0 :#line:618
                                for OO0OO000O00O000O0 in range (11 ):#line:619
                                    O000O0OO00O00000O =OO0OO000O00O000O0 +1 #line:620
                                    g =OO00000OOOOO0OO0O [O000O0OO00O00000O ]['level']#line:621
                                    if id ==g :#line:622
                                        OOOO00OO0000O0OOO =OO0OO000O00O000O0 +2 #line:623
                                        if OOOO00OO0000O0OOO !=OOOOOOOOOOO000000 +1 :#line:624
                                            OO00O000O0OOO0OOO =OOOOOOOOOOO000000 +1 #line:625
                                            time .sleep (random .randint (1 ,3 )/10 )#line:627
                                            O0O00OO0OO00000OO =f'_site={OO00O000O0OOO0OOO - 1}&targetSite={OOOO00OO0000O0OOO - 1}_{timi_new()}'#line:628
                                            O0O0O0O000OOO0000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000O0O0OOOO00O0O .token ,'timestamp':timi_new (),'sign':sign (O0O00OO0OO00000OO ),'signstring':O0O00OO0OO00000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:645
                                            OOO000OO0O0OO000O ={"site":int (OO00O000O0OOO0OOO -1 ),"targetSite":int (OOOO00OO0000O0OOO -1 )}#line:646
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0O0O0O000OOO0000 ,json =OOO000OO0O0OO000O )#line:647
                                            OOOO0000OO00000OO =True #line:649
                                    if OOOO0000OO00000OO :#line:650
                                        break #line:651
                                if OOOO0000OO00000OO :#line:652
                                    break #line:653
        except :#line:654
            O000O0O0OOOO00O0O .synthetic ()#line:655
    def level_new (O0OOOO0000OOOO0O0 ):#line:658
        try :#line:659
            O000OO0OOOO0OOO00 =f'__{timi_new()}'#line:660
            O00OOOOOO0OOOO0O0 ={'source':'scsc','authorization':O0OOOO0000OOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0OOOO0OOO00 ),'signstring':O000OO0OOOO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:671
            OO00OO00O00OO00OO =requests .request ('get',f'{host}/user',headers =O00OOOOOO0OOOO0O0 ).json ()#line:672
            if 'status'in OO00OO00O00OO00OO :#line:673
                if OO00OO00O00OO00OO ['status']==200 :#line:674
                    return float (OO00OO00O00OO00OO ['data']['level'])#line:675
        except Exception as O000O00O0OO00000O :#line:676
            print (O000O00O0OO00000O )#line:677
    def propsraffle (OOO00OOO0O0OOO0OO ):#line:680
        try :#line:681
            while True :#line:682
                O0O000OO0OO0O0000 =f'__{timi_new()}'#line:683
                O0000OOOOO0O0OO00 ={'source':'scsc','authorization':OOO00OOO0O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OO0OO0O0000 ),'signstring':O0O000OO0OO0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:694
                OOOO00OOO0OO00O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0000OOOOO0O0OO00 ).json ()#line:695
                if 'status'in OOOO00OOO0OO00O0O :#line:697
                    if OOOO00OOO0OO00O0O ['status']==200 :#line:698
                        OO0O0000OOO000OO0 =OOOO00OOO0OO00O0O ['data']['rows']#line:699
                        OO0OO0O00O0O0OOOO =OOOO00OOO0OO00O0O ['data']['vstate']#line:700
                        if OO0O0000OOO000OO0 ==5 or OO0O0000OOO000OO0 ==6 or OO0O0000OOO000OO0 ==7 :#line:701
                            O0000O0000OO0OO0O =OOOO00OOO0OO00O0O ['data']['silver']#line:702
                            print (f'【转盘抽奖】:获得种子:{O0000O0000OO0OO0O}')#line:703
                        if OO0O0000OOO000OO0 ==1 or OO0O0000OOO000OO0 ==2 or OO0O0000OOO000OO0 ==3 :#line:704
                            OOOOO0OO0O00O00OO =OOOO00OOO0OO00O0O ['data']['clover']#line:705
                            print (f'【转盘抽奖】:获得三叶草:{OOOOO0OO0O00O00OO}')#line:706
                        if OO0O0000OOO000OO0 ==4 or OO0O0000OOO000OO0 ==8 :#line:707
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:708
                        if OO0O0000OOO000OO0 =='抽奖次数已用完':#line:712
                            break #line:746
                time .sleep (random .randint (8 ,15 )/10 )#line:747
        except Exception as OO0000OO00OO00O0O :#line:748
            print (OO0000OO00OO00O0O )#line:749
    def friends_invitation (O0OOOO0O00OOO000O ):#line:752
        try :#line:753
            O0OOO0OO00OOO0OOO =f'__{timi_new()}'#line:754
            OOO0000O00O00O00O ={'source':'scsc','authorization':O0OOOO0O00OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO00OOO0OOO ),'signstring':O0OOO0OO00OOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:765
            OO0OOO0OOOOOO00OO =requests .request ('get',f'{host}/friends',headers =OOO0000O00O00O00O ).json ()#line:766
            if 'status'in OO0OOO0OOOOOO00OO :#line:767
                if OO0OOO0OOOOOO00OO ['status']==200 :#line:768
                    OO0O0O00OOO0OOOOO =OO0OOO0OOOOOO00OO ['data']['myInviteter']#line:769
                    if OO0O0O00OOO0OOOOO :#line:770
                        OOOO0OO0OOOOO0OOO =OO0O0O00OOO0OOOOO ['user']['nickname']#line:771
                        OOOO0O00OOO0O0OOO =O0OOOO0O00OOO000O .certification ()#line:772
                        print (f'【查邀请人】:我的邀请人:{OOOO0OO0OOOOO0OOO}丨实名:{OOOO0O00OOO0O0OOO}')#line:773
                    else :#line:774
                        if O0OOOO0O00OOO000O .innerId !='0':#line:775
                            O0OOOO0O00OOO000O .invitation ()#line:776
        except Exception as OOOO0O0O0O000OOOO :#line:777
            print (OOOO0O0O0O000OOOO )#line:778
    def add_clover (O0OO00OOOO00OOOO0 ):#line:781
        global golden_seed #line:782
        try :#line:783
            OOO00OO0O00O000O0 =f'__{timi_new()}'#line:784
            O00O0O0OO00OO0OOO ={'source':'scsc','authorization':O0OO00OOOO00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0O00O000O0 ),'signstring':OOO00OO0O00O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:795
            OO0O000000O0000O0 =requests .request ('get',f'{host}/assets/clovers',headers =O00O0O0OO00OO0OOO ).json ()#line:796
            if 'status'in OO0O000000O0000O0 :#line:798
                if OO0O000000O0000O0 ['status']==200 :#line:799
                    O00OO0O0O0O00OO0O =OO0O000000O0000O0 ['data']['clover']#line:800
                    OOO0O0OO00O0O0OO0 =OO0O000000O0000O0 ['data']['used_clover']#line:801
                    OOO0O00OOO00OO00O =float (O00OO0O0O0O00OO0O )-float (OOO0O0OO00O0O0OO0 )#line:802
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOO0O0OO00O0O0OO0}')#line:803
                    if O0OO00OOOO00OOOO0 .certification ()!='未实名':#line:804
                        if OOO0O00OOO00OO00O >1 :#line:805
                            OOO00OO0O00O000O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO0O00OOO00OO00O)}_{timi_new()}'#line:806
                            O0O0OOOOOO00O0OOO ={'source':'scsc','authorization':O0OO00OOOO00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0O00O000O0 ),'signstring':OOO00OO0O00O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:817
                            OOOOOOO0OO00OOO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO0O00OOO00OO00O )}#line:818
                            OOOOO000OO00OO000 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O0OOOOOO00O0OOO ,data =OOOOOOO0OO00OOO00 ).json ()#line:819
                            if 'status'in OOOOO000OO00OO000 :#line:821
                                if OOOOO000OO00OO000 ['status']==200 :#line:822
                                    print (f'【参与抽奖】:添加☘️:{OOOOO000OO00OO000["data"]}丨数量:{OOO0O00OOO00OO00O}')#line:823
                                if OOOOO000OO00OO000 ['status']==500 :#line:824
                                    print (f'【参与抽奖】:添加☘️:{OOOOO000OO00OO000["message"]}')#line:825
            OO000OO000O0OOOOO =requests .request ('get',f'{host}/lottery',headers =O00O0O0OO00OO0OOO ).json ()#line:826
            O0O0OO0O00O000OO0 =O0OO00OOOO00OOOO0 .winning_rewards ()#line:828
            if 'status'in OO000OO000O0OOOOO :#line:829
                if OO000OO000O0OOOOO ['status']==200 :#line:830
                    O00OOOOO000OOOO00 =OO000OO000O0OOOOO ['data'][0 ]['day_get_gold_quantity']#line:831
                    golden_seed +=float (O00OOOOO000OOOO00 )#line:832
                    OO00OO0O00000OO0O =OO000OO000O0OOOOO ['data'][1 ]['value']#line:833
                    OOOOOO000OOOOO0O0 =OO000OO000O0OOOOO ['data'][0 ]['join_number']#line:834
                    O000O00O0O00OO0O0 =int (float (OO000OO000O0OOOOO ['data'][0 ]['totalValue']))#line:835
                    O0OOO000O0O0O0O00 =float (OO00OO0O00000OO0O /O000O00O0O00OO0O0 )*10000 #line:836
                    O0OO0O0O000OO00O0 =O000O00O0O00OO0O0 /OOOOOO000OOOOO0O0 #line:837
                    print (f'【参与抽奖】:预计每天中{str(O00OOOOO000OOOO00)[:6]}颗金种子丨好友收益:{str(O0O0OO0O00O000OO0)[:6]}')#line:838
                    print (f'【抽奖统计】:每1万☘️中{str(O0OOO000O0O0O0O00)[:6]}颗金种子丨☘️人均:{str(O0OO0O0O000OO00O0)[:7]}️')#line:839
        except Exception as OO0000OO00OOOOO0O :#line:840
            print (OO0000OO00OOOOO0O )#line:841
    def energy (O0O00OOO0000OOO0O ):#line:845
        try :#line:846
            while True :#line:847
                O0OOO00OO00OO00OO =f'__{timi_new()}'#line:848
                O0OOO0OOO000O0OOO ={'source':'scsc','authorization':O0O00OOO0000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OO00OO00OO ),'signstring':O0OOO00OO00OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:859
                O00OOOO0OOO0000OO =requests .request ('get',f'{host}/energy/general',headers =O0OOO0OOO000O0OOO ).json ()#line:860
                if 'status'in O00OOOO0OOO0000OO :#line:862
                    if O00OOOO0OOO0000OO ['status']==200 :#line:863
                        O0OOO0OOO0O000O00 =O00OOOO0OOO0000OO ['data']['ordinary_water']#line:864
                        O0O0O0OOO000OOO00 =O00OOOO0OOO0000OO ['data']['ordinary_fertilizer']#line:865
                        O0O0000OO0O0O0OOO =O00OOOO0OOO0000OO ['data']['videoStatus']#line:866
                        O000000OO000O0OO0 =O00OOOO0OOO0000OO ['data']['waterVideoKey']#line:867
                        print (f'【我的营养】:肥料:{str(O0O0O0OOO000OOO00).split(".")[0]}丨水滴:{str(O0OOO0OOO0O000O00).split(".")[0]}')#line:868
                        if float (O0O0O0OOO000OOO00 )<96 :#line:869
                            if O0O0000OO0O0O0OOO :#line:870
                                time .sleep (random .randint (160 ,180 )/10 )#line:871
                                O0O0OOO0O0OO00OO0 =99 -float (O0O0O0OOO000OOO00 )#line:872
                                OOO000O0OO00O0OO0 ={"fertilizer":str (O0O0OOO0O0OO00OO0 ).split ('.')[0 ]}#line:873
                                O000O000OOOOO00O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0OOO0OOO000O0OOO ).json ()#line:874
                                if 'status'in O000O000OOOOO00O0 :#line:876
                                    if O000O000OOOOO00O0 ['status']==200 :#line:877
                                        print (f'【购买肥料】:看广告获取肥料:{O000O000OOOOO00O0["message"]}')#line:878
                                    if O000O000OOOOO00O0 ['status']==500 :#line:879
                                        print (f'【购买肥料】:看广告获取肥料:{O000O000OOOOO00O0["message"]}')#line:880
                                        break #line:881
                            if energy :#line:882
                                O0O0OOO0O0OO00OO0 =99 -float (O0O0O0OOO000OOO00 )#line:883
                                OO0OOOOO0000OOOO0 =f'_fertilizer={int(O0O0OOO0O0OO00OO0)}_{timi_new()}'#line:884
                                OOOOO00O00OOO00O0 ={'source':'scsc','authorization':O0O00OOO0000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO0000OOOO0 ),'signstring':OO0OOOOO0000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:895
                                OO0OOOOOOO00O0O0O ={"fertilizer":int (O0O0OOO0O0OO00OO0 )}#line:896
                                O00OOOOO0O0O00O00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOOO00O00OOO00O0 ,data =OO0OOOOOOO00O0O0O ).json ()#line:897
                                if 'status'in O00OOOOO0O0O00O00 :#line:899
                                    if O00OOOOO0O0O00O00 ['status']==200 :#line:900
                                        print (f'【购买肥料】:购买肥料:{O00OOOOO0O0O00O00["message"]}丨数量:{int(O0O0OOO0O0OO00OO0)}')#line:901
                                    if O00OOOOO0O0O00O00 ['status']==500 :#line:902
                                        print (f'【购买肥料】:购买肥料:{O00OOOOO0O0O00O00["message"]}丨数量:{int(O0O0OOO0O0OO00OO0)}')#line:903
                                        OO0O0OOOO0O00000O =O00OOOOO0O0O00O00 ["message"].split ('-')[1 ]#line:904
                                        O00O00O00O00000O0 =f'__{timi_new()}'#line:905
                                        OO000000OOOO0O000 ={'source':'scsc','authorization':O0O00OOO0000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O00O00000O0 ),'signstring':O00O00O00O00000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:916
                                        OO000OOO000O00O00 =requests .request ('get',f'{host}/user',headers =OO000000OOOO0O000 ).json ()#line:917
                                        if 'status'in OO000OOO000O00O00 :#line:918
                                            if OO000OOO000O00O00 ['status']==200 :#line:919
                                                OO000OOO00O000O00 =OO000OOO000O00O00 ['data']['inner_id']#line:920
                                                give_gold (OO000OOO00O000O00 ,float (OO0O0OOOO0O00000O )+1 )#line:921
                                                O0O00OOO0000OOO0O .energy ()#line:922
                        if float (O0OOO0OOO0O000O00 )<880 :#line:923
                            if O000000OO000O0OO0 :#line:924
                                time .sleep (random .randint (160 ,180 )/10 )#line:925
                                O0OOOO0OO00OO0OO0 =999 -float (O0OOO0OOO0O000O00 )#line:926
                                OOOOO0OOOO00OOOOO ={"water":str (O0OOOO0OO00OO0OO0 ).split ('.')[0 ]}#line:927
                                O00000000OO0O000O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0OOO0OOO000O0OOO ).json ()#line:928
                                if 'status'in O00000000OO0O000O :#line:930
                                    if O00000000OO0O000O ['status']==200 :#line:931
                                        print (f'【购买水滴】:看广告获取水滴:{O00000000OO0O000O["message"]}')#line:932
                                    if O00000000OO0O000O ['status']==500 :#line:933
                                        print (f'【购买水滴】:看广告获取水滴:{O00000000OO0O000O["message"]}')#line:934
                                        break #line:935
                            if energy :#line:936
                                O0OOOO0OO00OO0OO0 =999 -float (O0OOO0OOO0O000O00 )#line:937
                                OOOO00O0OOOO0OO0O =f'_water={int(O0OOOO0OO00OO0OO0)}_{timi_new()}'#line:938
                                O0O0O0000O0O0000O ={'source':'scsc','authorization':O0O00OOO0000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0OOOO0OO0O ),'signstring':OOOO00O0OOOO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:949
                                OOOOOO000O00OO000 ={"water":int (O0OOOO0OO00OO0OO0 )}#line:950
                                O00O0OO00000000OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O0O0000O0O0000O ,data =OOOOOO000O00OO000 ).json ()#line:952
                                if 'status'in O00O0OO00000000OO :#line:954
                                    if O00O0OO00000000OO ['status']==200 :#line:955
                                        print (f'【购买水滴】:购买水滴:{O00O0OO00000000OO["message"]}丨数量:{int(O0OOOO0OO00OO0OO0)}')#line:956
                                    if O00O0OO00000000OO ['status']==500 :#line:957
                                        print (f'【购买水滴】:购买水滴:{O00O0OO00000000OO["message"]}丨数量:{int(O0OOOO0OO00OO0OO0)}')#line:958
                                        OO0O0OOOO0O00000O =O00O0OO00000000OO ["message"].split ('-')[1 ]#line:959
                                        O00O00O00O00000O0 =f'__{timi_new()}'#line:960
                                        OO000000OOOO0O000 ={'source':'scsc','authorization':O0O00OOO0000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O00O00000O0 ),'signstring':O00O00O00O00000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:971
                                        OO000OOO000O00O00 =requests .request ('get',f'{host}/user',headers =OO000000OOOO0O000 ).json ()#line:972
                                        if 'status'in OO000OOO000O00O00 :#line:973
                                            if OO000OOO000O00O00 ['status']==200 :#line:974
                                                OO000OOO00O000O00 =OO000OOO000O00O00 ['data']['inner_id']#line:975
                                                give_gold (OO000OOO00O000O00 ,float (OO0O0OOOO0O00000O )+1 )#line:976
                                                O0O00OOO0000OOO0O .energy ()#line:977
                        break #line:978
        except Exception as O0O00O00O0O00O000 :#line:980
            print (O0O00O00O0O00O000 )#line:981
def bundled_def ():#line:983
    OO00OO0OOOO00OO00 =['5570536','7750212','7911652','7911680','7805624']#line:984
    return OO00OO0OOOO00OO00 [random .randint (0 ,len (OO00OO0OOOO00OO00 )-1 )]#line:985
def version_of_the_validation ():#line:989
    return str ((83 -56 )/10 )#line:990
def gitee_validation ():#line:993
    try :#line:994
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:995
    except :#line:996
        sys .exit (0 )#line:997
def update_the_validation ():#line:1001
    try :#line:1002
        O0OO00OOO00O0OOO0 =gitee_validation ()#line:1003
        if version_of_the_validation ()<O0OO00OOO00O0OOO0 ['CityEarth']['edition']:#line:1004
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00OOO00O0OOO0["CityEarth"]["edition"]}   ❌')#line:1005
            print (f'更新内容=>>{O0OO00OOO00O0OOO0["CityEarth"]["content"]}   🎉')#line:1006
        else :#line:1007
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00OOO00O0OOO0["CityEarth"]["edition"]}   ✅')#line:1008
            print (f'更新内容=>> {O0OO00OOO00O0OOO0["CityEarth"]["content"]}   🎉')#line:1009
    except Exception as OO0OOO00O0OO0O0OO :#line:1010
        print (OO0OOO00O0OO0O0OO )#line:1011
def os_qinglong ():#line:1014
    if application in os .environ :#line:1015
        O0O000000OO0O0000 =os .environ [application ].split ('\n')#line:1016
        if len (O0O000000OO0O0000 )>0 :#line:1017
            return O0O000000OO0O0000 #line:1018
        else :#line:1019
            print (f"{application}变量未启用")#line:1020
            print ('脚本退出')#line:1021
            sys .exit (1 )#line:1022
    else :#line:1023
        if token :#line:1024
            O0O000000OO0O0000 =token .split ('\n')#line:1025
            if len (O0O000000OO0O0000 )>0 :#line:1026
                return O0O000000OO0O0000 #line:1027
        else :#line:1028
            print (f"内置变量为空")#line:1029
            print ('脚本结束')#line:1030
            sys .exit (0 )#line:1031
if __name__ =='__main__':#line:1036
    start ()#line:1037
