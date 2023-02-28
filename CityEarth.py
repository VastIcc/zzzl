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
@ 版本  2.5
"""
application = 'ce_token'  # 变量名
token = ''
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
version ='3.1.41954131'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        OOOO0O00O0OO00000 =os_qinglong ()#line:10
        print (f"==========共找到{len(OOOO0O00O0OO00000)}个账号==========")#line:11
        for OOO0O000OOO000OO0 in OOOO0O00O0OO00000 :#line:12
            O0O000OOOOOO0O0O0 =[]#line:13
            print (f"------------正在执行第{OOOO0O00O0OO00000.index(OOO0O000OOO000OO0) + 1}个账号------------")#line:14
            OO0O0O000000000O0 =CityEarth (OOO0O000OOO000OO0 ,O0O000OOOOOO0O0O0 )#line:15
            def O00OOO0O0O00O00OO ():#line:17
                if OO0O0O000000000O0 .base_info ():#line:19
                    OO0O0O000000000O0 .sealing ()#line:21
                    OO0O0O000000000O0 .invitenum ()#line:23
                    OO0O0O000000000O0 .game_map ()#line:25
                    OO0O0O000000000O0 .friends_invitation ()#line:27
                    OO0O0O000000000O0 .add_clover ()#line:29
                    OO0O0O000000000O0 .propsraffle ()#line:31
                    OO0O0O000000000O0 .synthetic ()#line:33
                    OO0O0O000000000O0 .crops_illustrated ()#line:35
                    OO0O0O000000000O0 .give_gold ()#line:37
                    OO0O0O000000000O0 .withdraw ()#line:39
                    OO0O0O000000000O0 .energy ()#line:41
            OO00OO0O000OOOO00 =threading .Thread (target =O00OOO0O0O00O00OO )#line:42
            OO00OO0O000OOOO00 .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        OO00000O00OO0O000 =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO00000O00OO0O000 +' ')#line:48
    except Exception as OOOO0O0OOOO00000O :#line:49
        print (OOOO0O0OOOO00000O )#line:50
def sign (OOOOO0O0OOO0000OO ):#line:53
    OOO000O00OO0OO000 =hashlib .md5 (OOOOO0O0OOO0000OO .encode ()).hexdigest ()#line:54
    OOOOO000O00O000O0 ="scsc%^&*"+OOO000O00OO0OO000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    O0O0OOO00OOO0O0OO =hashlib .md5 (OOOOO000O00O000O0 .encode ()).hexdigest ()#line:56
    return O0O0OOO00OOO0O0OO #line:57
def format_msg ():#line:59
    OOOO00OO0OO000O0O =""#line:60
    for OO00O0O00OOOO000O in msg_list :#line:61
        OOOO00OO0OO000O0O +=str (OO00O0O00OOOO000O )+"\r\n"#line:62
    return OOOO00OO0OO000O0O #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (O0OOOO0OOO00000OO ,O0O0OOOO00O0OO0OO ,O00O00OO0O0OOO000 ):#line:71
        try :#line:72
            O0OOOO0OOO00000OO .msg =O00O00OO0O0OOO000 #line:73
            O0OOOO0OOO00000OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            O0OOOO0OOO00000OO .token =O0O0OOOO00O0OO0OO .split ('&')[0 ]#line:75
            O0OOOO0OOO00000OO .innerId =O0O0OOOO00O0OO0OO .split ('&')[1 ]#line:76
            O0OOOO0OOO00000OO .doneeNo =O0O0OOOO00O0OO0OO .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (O0O00O000000O0O00 ):#line:82
        try :#line:83
            O0O00O000000O0O00 .watched_ad ()#line:85
            OOO00OO0OOO0OOO0O =f'__{timi_new()}'#line:86
            OO00000000OOO000O ={'source':'scsc','authorization':O0O00O000000O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0OOO0OOO0O ),'signstring':OOO00OO0OOO0OOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:96
            O0O0OO00OO0O0OOOO =requests .request ('get',f'{host}/user',headers =OO00000000OOO000O ).json ()#line:97
            if 'status'in O0O0OO00OO0O0OOOO :#line:99
                if O0O0OO00OO0O0OOOO ['status']==200 :#line:100
                    OOO0O00000O00O0OO =O0O0OO00OO0O0OOOO ['data']['nickname']#line:101
                    OO0O0000OO0000OOO =O0O0OO00OO0O0OOOO ['data']['inner_id']#line:102
                    O0OOO0000O0O0OO00 =O0O0OO00OO0O0OOOO ['data']['assets']['gold']#line:103
                    O0OOOOOO00O0O0O00 =O0O0OO00OO0O0OOOO ['data']['level']#line:104
                    print (f'【账号信息】:昵称:{OOO0O00000O00O0OO[:5]}丨ID:{OO0O0000OO0000OOO}丨等级:{O0OOOOOO00O0O0O00}丨金种子:{str(O0OOO0000O0O0OO00).split(".")[0]}')#line:105
                if O0O0OO00OO0O0OOOO ['status']==401 :#line:106
                    print (O0O0OO00OO0O0OOOO ['message'])#line:107
                    O0O00O000000O0O00 .msg .append ('有账号失效了')#line:108
                    return False #line:109
                if O0O0OO00OO0O0OOOO ['status']==500 :#line:110
                    return False #line:111
            return True #line:112
        except Exception as OO0O000O0O00O0O00 :#line:113
            print (OO0O000O0O00O0O00 )#line:114
    def sealing (OO0O000OOOO0000O0 ):#line:117
        try :#line:118
            O00O0OO000000O0O0 =f'__{timi_new()}'#line:119
            OOOO000OOOO0O00OO ={'source':'scsc','authorization':OO0O000OOOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO000000O0O0 ),'signstring':O00O0OO000000O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:129
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOO000OOOO0O00OO )#line:130
            requests .request ('get',f'{host}/packsack/list',headers =OOOO000OOOO0O00OO )#line:131
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOO000OOOO0O00OO )#line:132
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOO000OOOO0O00OO )#line:133
            requests .request ('get',f'{host}/user',headers =OOOO000OOOO0O00OO )#line:134
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOO000OOOO0O00OO )#line:135
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOO000OOOO0O00OO )#line:136
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOO000OOOO0O00OO )#line:137
            requests .request ('get',f'{host}/game/getAllData',headers =OOOO000OOOO0O00OO )#line:138
            requests .request ('get',f'{host}/assets',headers =OOOO000OOOO0O00OO )#line:139
        except Exception as O0O00OOO0O0OOO000 :#line:140
            print (O0O00OOO0O0OOO000 )#line:141
    def withdraw (O0O00OOO000O0OOOO ):#line:145
        O00O0OO00O0O00O0O =f'__{timi_new()}'#line:146
        OOOO0000OOOOOOO00 ={'source':'scsc','authorization':O0O00OOO000O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO00O0O00O0O ),'signstring':O00O0OO00O0O00O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:156
        OO000OOO0O0O00O0O =requests .request ('get',f'{host}/assets',headers =OOOO0000OOOOOOO00 ).json ()#line:157
        if 'status'in OO000OOO0O0O00O0O :#line:159
            if OO000OOO0O0O00O0O ['status']==200 :#line:160
                O0O0OO0O0OOOOO000 =OO000OOO0O0O00O0O ['data']['cash']#line:161
                if float (O0O0OO0O0OOOOO000 )>20 :#line:162
                    O00O0OO00O0O00O0O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:163
                    OOOO0000OOOOOOO00 ={'authorization':O0O00OOO000O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO00O0O00O0O ),'signstring':O00O0OO00O0O00O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:172
                    O00O000O0O0O0OOO0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:173
                    O00000OOOO0O0OO00 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOO0000OOOOOOO00 ,data =O00O000O0O0O0OOO0 ).json ()#line:175
                    print (O00000OOOO0O0OO00 )#line:176
    def invitenum (O000OOO000OOO0O0O ):#line:179
        O0O00OO0O0O000OO0 =f'__{timi_new()}'#line:180
        O0O00O0O000OO0OO0 ={'source':'scsc','authorization':O000OOO000OOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0O0O000OO0 ),'signstring':O0O00OO0O0O000OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:190
        OOOOOOO00O0O0O0O0 =requests .request ('get',f'{host}/invite/invitenum',headers =O0O00O0O000OO0OO0 ).json ()#line:191
        if 'status'in OOOOOOO00O0O0O0O0 :#line:193
            if OOOOOOO00O0O0O0O0 ['status']==200 :#line:194
                OOOOO0O0O00O00O0O =OOOOOOO00O0O0O0O0 ['data']['invited_count']#line:195
                OOOO0OOOO0O0OOOO0 =OOOOOOO00O0O0O0O0 ['data']['invited_second_count']#line:196
                print (f'【我的邀请】:直邀好友:{OOOOO0O0O00O00O0O}丨间邀好友:{OOOO0OOOO0O0OOOO0}')#line:197
    def game_map (O000O000O00OOO0O0 ):#line:200
        try :#line:201
            O000O0OOOO000OOOO =f'__{timi_new()}'#line:202
            OO00OOO0000O00OOO ={'source':'scsc','authorization':O000O000O00OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOOO000OOOO ),'signstring':O000O0OOOO000OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:212
            O0000O00000OO0OO0 =requests .request ('get',f'{host}/game/map',headers =OO00OOO0000O00OOO ).json ()#line:213
            if 'status'in O0000O00000OO0OO0 :#line:215
                if O0000O00000OO0OO0 ['status']==200 :#line:216
                    for OOOOO000O0OOOO000 in O0000O00000OO0OO0 ['data']['list'][0 ]['crops']:#line:217
                        OOO00O0OOOO000OO0 =OOOOO000O0OOOO000 ['level']#line:219
                        if OOO00O0OOOO000OO0 ==41 :#line:220
                            OO0OO0O0OOOOOOOOO =OOOOO000O0OOOO000 ['crop_name']#line:221
                            O0O0OOOO00O000OO0 =OOOOO000O0OOOO000 ['count']#line:222
                            if O0O0OOOO00O000OO0 >0 :#line:223
                                print (f'【农业资产】:{OO0OO0O0OOOOOOOOO}丨数量:{O0O0OOOO00O000OO0}')#line:224
        except Exception as OO00OO0OO00OO000O :#line:225
            print (OO00OO0OO00OO000O )#line:226
    def give_gold (OO00O0OOOO0O000O0 ):#line:229
        try :#line:230
            OOO0O0O0OO0OO0OO0 =f'__{timi_new()}'#line:231
            OOOO000OO0O0OO0O0 ={'source':'scsc','authorization':OO00O0OOOO0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OO0OO0OO0 ),'signstring':OOO0O0O0OO0OO0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:241
            O0OO0OO0O00O0O00O =requests .request ('get',f'{host}/user',headers =OOOO000OO0O0OO0O0 ).json ()#line:242
            if 'status'in O0OO0OO0O00O0O00O :#line:243
                if O0OO0OO0O00O0O00O ['status']==200 :#line:244
                    if float (OO00O0OOOO0O000O0 .doneeNo )!=0 :#line:245
                        OOOO0OO0000OOOOO0 =O0OO0OO0O00O0O00O ['data']['assets']['gold']#line:246
                        if float (OOOO0OO0000OOOOO0 )>float (OO00O0OOOO0O000O0 .innerId ):#line:247
                            OOO00O0OO0OOOOO00 =int (float (OOOO0OO0000OOOOO0 )/1.1 )#line:248
                            OOO0O0O0OO0OO0OO0 =f'_doneeNo={OO00O0OOOO0O000O0.doneeNo}&quantity={OOO00O0OO0OOOOO00}_{timi_new()}'#line:249
                            OOOO000OO0O0OO0O0 ={'source':'scsc','authorization':OO00O0OOOO0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OO0OO0OO0 ),'signstring':OOO0O0O0OO0OO0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:259
                            O00O0000O0OO0OO00 ={"quantity":OOO00O0OO0OOOOO00 ,"doneeNo":OO00O0OOOO0O000O0 .doneeNo }#line:263
                            O0000O00O0000000O =requests .request ('post',f'{host}/finance/give-gold',headers =OOOO000OO0O0OO0O0 ,data =O00O0000O0OO0OO00 ).json ()#line:264
                            if 'status'in O0000O00O0000000O :#line:266
                                if O0000O00O0000000O ['status']==200 :#line:267
                                    if O0000O00O0000000O ['data']:#line:268
                                        print (f'【赠送种子】:赠送{OOO00O0OO0OOOOO00}种子给{OO00O0OOOO0O000O0.doneeNo}成功')#line:269
                    else :#line:270
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:271
        except Exception as O0O00O0O000OO0000 :#line:272
            print (O0O00O0O000OO0000 )#line:273
    def invitation (O0OO00O0O0O0OO0O0 ):#line:275
        try :#line:276
            _OOO00O000000OOO0O =float (bundled_def ())/4 #line:277
            OO00OO00OOO0OOO00 =f'_innerId={int(_OOO00O000000OOO0O)}_{timi_new()}'#line:278
            OO00OOO0OO000000O ={'source':'scsc','authorization':O0OO00O0O0O0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO00OOO0OOO00 ),'signstring':OO00OO00OOO0OOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:288
            OOO0O0O0OO0000000 ={"innerId":int (_OOO00O000000OOO0O )}#line:289
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO00OOO0OO000000O ,data =OOO0O0O0OO0000000 )#line:290
        except Exception as OO00OOOO00O0O00OO :#line:291
            print (OO00OOOO00O0O00OO )#line:292
    def winning_rewards (OO0OOOOO000OOO000 ):#line:295
        try :#line:296
            O0OO0OOO0OO0OOOOO =f'__{timi_new()}'#line:297
            O0000O0OO00OO0OO0 ={'source':'scsc','authorization':OO0OOOOO000OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO0OO0OOOOO ),'signstring':O0OO0OOO0OO0OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:307
            O000O00O0OOOO0O00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0000O0OO00OO0OO0 ).json ()#line:308
            if 'status'in O000O00O0OOOO0O00 :#line:310
                if O000O00O0OOOO0O00 ['status']==200 :#line:311
                    if O000O00O0OOOO0O00 ['data']['amount']:#line:312
                        O0OO00O00O0OOOO0O =O000O00O0OOOO0O00 ['data']['amount']['gold']#line:313
                        return O0OO00O00O0OOOO0O #line:314
                    else :#line:315
                        return 0 #line:316
        except Exception as OOO0000OO000O0O00 :#line:317
            print (OOO0000OO000O0O00 )#line:318
    def certification (OO000000OO0O000O0 ):#line:321
        try :#line:322
            O00000OO000O00OOO =f'__{timi_new()}'#line:323
            O00O00OOO0OOOOOO0 ={'source':'scsc','authorization':OO000000OO0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO000O00OOO ),'signstring':O00000OO000O00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:333
            OOO0O0OOOO00O000O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00O00OOO0OOOOOO0 ).json ()#line:334
            if 'status'in OOO0O0OOOO00O000O :#line:336
                if OOO0O0OOOO00O000O ['status']==200 :#line:337
                    if OOO0O0OOOO00O000O ['data']['result']:#line:338
                        O00O0OOO0O0OO00O0 =OOO0O0OOOO00O000O ['data']['nick_name']#line:339
                        return O00O0OOO0O0OO00O0 #line:340
                    else :#line:341
                        return '未实名'#line:342
        except Exception as OOO0O0OOO0O0O0OO0 :#line:343
            print (OOO0O0OOO0O0O0OO0 )#line:344
    def crops_illustrated (O0OO00O0O00O0O0OO ):#line:347
        try :#line:348
            OOO0OO00000O0OO00 =f'__{timi_new()}'#line:349
            OO00000OOO00OOOO0 ={'source':'scsc','authorization':O0OO00O0O00O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00000O0OO00 ),'signstring':OOO0OO00000O0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:359
            O000O00OO00O0000O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO00000OOO00OOOO0 ).json ()#line:360
            if 'status'in O000O00OO00O0000O :#line:362
                if O000O00OO00O0000O ['status']==200 :#line:363
                    OO000OOOOO00OO000 =O000O00OO00O0000O ['data'][0 ]['crops']#line:364
                    for OO000OOOO00OO0O00 in OO000OOOOO00OO000 :#line:365
                        if OO000OOOO00OO0O00 ['ill_clover_award']:#line:366
                            if float (OO000OOOO00OO0O00 ['ill_clover_award'])>1 :#line:367
                                if OO000OOOO00OO0O00 ['is_finish']:#line:368
                                    if not OO000OOOO00OO0O00 ['is_getit']:#line:369
                                        if O0OO00O0O00O0O0OO .certification ()!='未实名':#line:370
                                            OOO0OO00000O0OO00 =f'_award_level={OO000OOOO00OO0O00["level"]}_{timi_new()}'#line:371
                                            OO00000OOO00OOOO0 ={'source':'scsc','authorization':O0OO00O0O00O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00000O0OO00 ),'signstring':OOO0OO00000O0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:381
                                            O000O0000OOO0O0O0 ={"award_level":OO000OOOO00OO0O00 ['level']}#line:382
                                            OO0O0O0OOO00O000O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO00000OOO00OOOO0 ,json =O000O0000OOO0O0O0 ).json ()#line:384
                                            if 'status'in OO0O0O0OOO00O000O :#line:385
                                                if OO0O0O0OOO00O000O ['status']==200 :#line:386
                                                    O0O00000O000OO0OO =OO0O0O0OOO00O000O ['data']['ill_clover_award']#line:387
                                                    print (f'【图鉴奖励】:领取{OO000OOOO00OO0O00["crop_name"]}成就丨奖励{O0O00000O000OO0OO}☘️')#line:389
                                                if OO0O0O0OOO00O000O ['status']==500 :#line:390
                                                    print (f'【图鉴奖励】:{OO0O0O0OOO00O000O["message"]}')#line:391
        except Exception as OO00OOOOOOO0O000O :#line:392
            print (OO00OOOOOOO0O000O )#line:393
    def watched_ad (OOO0OO0OO0000000O ):#line:396
        try :#line:397
            OO000O0OO00OOOOO0 =f'__{timi_new()}'#line:398
            OOO000O0O0O00OOO0 ={'source':'scsc','authorization':OOO0OO0OO0000000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0OO00OOOOO0 ),'signstring':OO000O0OO00OOOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            OOOO0000O0O00O0OO =requests .request ('get',f'{host}/game/getAllData',headers =OOO000O0O0O00OOO0 ).json ()#line:409
            if 'status'in OOOO0000O0O00O0OO :#line:411
                if OOOO0000O0O00O0OO ['status']==200 :#line:412
                    if 'offlineInfo'in OOOO0000O0O00O0OO ['data']:#line:413
                        time .sleep (random .randint (3 ,5 ))#line:414
                        OO0OO0OO0OOOOO00O =OOOO0000O0O00O0OO ['data']['offlineInfo']['off_minute']#line:415
                        O000000O0OO00O000 =float (OOOO0000O0O00O0OO ['data']['silver'])/1000000000000 #line:416
                        time .sleep (1 )#line:417
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO000O0O0O00OOO0 ).json ()#line:418
                        time .sleep (2 )#line:419
                        OO00OOOOO0OO00000 =requests .request ('get',f'{host}/game/getAllData',headers =OOO000O0O0O00OOO0 ).json ()#line:420
                        if 'status'in OO00OOOOO0OO00000 :#line:422
                            if OO00OOOOO0OO00000 ['status']==200 :#line:423
                                O0OOOOO000OOO00O0 =float (OO00OOOOO0OO00000 ['data']['silver'])/1000000000000 #line:424
                                OOO0O0O0O0O000OOO =str (O0OOOOO000OOO00O0 -O000000O0OO00O000 )[:6 ]#line:425
                                print (f'【离线奖励】:翻倍离线{OO0OO0OO0OOOOO00O}分钟奖励🌱数量:{OOO0O0O0O0O000OOO}t粒')#line:426
        except Exception as O00O0OO00OO000O00 :#line:427
            print (O00O0OO00OO000O00 )#line:428
    def user_ad (OO0OO0OO00O00O00O ):#line:431
        try :#line:432
            O00OO00000OO00OOO =f'__{timi_new()}'#line:433
            OOOO000O00O00OOO0 ={'source':'scsc','authorization':OO0OO0OO00O00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00000OO00OOO ),'signstring':O00OO00000OO00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:443
            O000O0O0OOOOO0O00 =requests .request ('get',f'{host}/user/ad',headers =OOOO000O00O00OOO0 ).json ()#line:444
            if 'status'in O000O0O0OOOOO0O00 :#line:446
                if O000O0O0OOOOO0O00 ['status']==200 :#line:447
                    OOOO0OOOOO0000O00 =O000O0O0OOOOO0O00 ['data']['max_time']#line:448
                    O000OO00000000OOO =O000O0O0OOOOO0O00 ['data']['watch_time']#line:449
                    O00O00OOO00OOO000 =O000O0O0OOOOO0O00 ['data']['added_time']#line:450
                    print (f'【获取种子】:获取🌱剩余{O00O00OOO00OOO000 + OOOO0OOOOO0000O00 - O000OO00000000OOO}次丨好友提供:{O00O00OOO00OOO000}次')#line:451
                    if O00O00OOO00OOO000 +OOOO0OOOOO0000O00 -O000OO00000000OOO >0 :#line:452
                        time .sleep (random .randint (16 ,19 ))#line:453
                        O00O0O00O0OO00OO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOOO000O00O00OOO0 ).json ()#line:454
                        if 'status'in O00O0O00O0OO00OO0 :#line:456
                            if O00O0O00O0OO00OO0 ['status']==200 :#line:457
                                O0O00OO0OOOOO0OO0 =float (O00O0O00O0OO00OO0 ['data']['silver'])/1000000000000 #line:458
                                print (f'【获取种子】:获得🌱:{int(O0O00OO0OOOOO0OO0)}t粒')#line:459
                                return True #line:460
                            if O00O0O00O0OO00OO0 ['status']==500 :#line:461
                                O00O000O0000OOO00 =O00O0O00O0OO00OO0 ['message']#line:462
                                print (f'【获取种子】:{O00O000O0000OOO00}')#line:463
                                return False #line:464
        except Exception as O0O0O0O00OO00OO00 :#line:465
            print (O0O0O0O00OO00OO00 )#line:466
    def synthetic (O0O000OO0OO0O000O ):#line:469
        global id ,g #line:470
        try :#line:471
            OO00OOO0O0OO0OO00 =O0O000OO0OO0O000O .level_new ()#line:472
            O000OOO0OO0O0OOO0 =random .randint (9 ,11 )#line:473
            OO00O0OOOOOOO000O =f'_site=8&targetSite={O000OOO0OO0O0OOO0}_{timi_new()}'#line:474
            OOOO0O000OO00OO0O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O000OO0OO0O000O .token ,'timestamp':timi_new (),'sign':sign (OO00O0OOOOOOO000O ),'signstring':OO00O0OOOOOOO000O ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:490
            OOOOO00OO0000O0O0 ={"site":int (8 ),"targetSite":int (O000OOO0OO0O0OOO0 )}#line:491
            requests .request ('post',f'{host}/game/crops/move',headers =OOOO0O000OO00OO0O ,json =OOOOO00OO0000O0O0 )#line:492
            while True :#line:493
                O0O0O0OO0OOO0O0O0 =f'__{timi_new()}'#line:494
                O000O0O0O000OOOOO ={'source':'scsc','authorization':O0O000OO0OO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO0OOO0O0O0 ),'signstring':O0O0O0OO0OOO0O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:504
                O0OOOO0O00000O00O =requests .request ('get',f'{host}/game/getAllData',headers =O000O0O0O000OOOOO ).json ()#line:505
                if 'status'in O0OOOO0O00000O00O :#line:507
                    if O0OOOO0O00000O00O ['status']==200 :#line:508
                        O0O0OOOO0OOOOO000 =O0OOOO0O00000O00O ['data']['cropList']#line:509
                        O00O0O00OOOO0O0OO =O0OOOO0O00000O00O ['data']['gameCoreDataDBid']#line:510
                        OOOO0OOOO0000OOO0 =float (O0OOOO0O00000O00O ['data']['silver'])/1000000000000 #line:511
                        OO000O000O0O0O0OO =0 #line:516
                        for O0O00O0OO0O00OO00 in O0O0OOOO0OOOOO000 :#line:517
                            if not O0O00O0OO0O00OO00 :#line:518
                                O00O0O0OOOO000OO0 =f'_crop_id={O00O0O00OOOO0O0OO}&site={OO000O000O0O0O0OO}_{O0O000OO0OO0O000O.time}'#line:519
                                OO0O0O00OOOO0O000 ={'source':'scsc','authorization':O0O000OO0OO0O000O .token ,'timestamp':O0O000OO0OO0O000O .time ,'sign':sign (O00O0O0OOOO000OO0 ),'signstring':O00O0O0OOOO000OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:529
                                O000OOO00OOOOOO0O ={"site":OO000O000O0O0O0OO ,"crop_id":O00O0O00OOOO0O0OO }#line:530
                                O0O0O0O0OOOOO0OO0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O0O00OOOO0O000 ,data =O000OOO00OOOOOO0O ).json ()#line:531
                                time .sleep (random .randint (1 ,3 )/10 )#line:533
                                if 'status'in O0O0O0O0OOOOO0OO0 :#line:534
                                    if O0O0O0O0OOOOO0OO0 ['status']==200 :#line:535
                                        if O0O0O0O0OOOOO0OO0 ['message']=='种子数量不足':#line:536
                                            OO00OOO0O0OO0OO00 =O0O000OO0OO0O000O .level_new ()#line:537
                                            print (f'【种植合成】:{O0O0O0O0OOOOO0OO0["message"]}')#line:538
                                            if not O0O000OO0OO0O000O .user_ad ():#line:539
                                                return False #line:540
                                    if O0O0O0O0OOOOO0OO0 ['status']==500 :#line:541
                                        print (f'【种植合成】:{O0O0O0O0OOOOO0OO0["message"]}')#line:542
                                        return False #line:543
                            OO000O000O0O0O0OO +=1 #line:544
                        OOO00O00O00OO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =O000O0O0O000OOOOO ).json ()#line:545
                        OO00OO000000OOOO0 =OOO00O00O00OO0O0O ['data']['cropList']#line:546
                        O0O0000OOOOO0OO00 =False #line:547
                        for O0O00O0OO0O00OO00 in range (12 ):#line:548
                            id =OO00OO000000OOOO0 [O0O00O0OO0O00OO00 ]['level']#line:549
                            if float (OO00OOO0O0OO0OO00 )-float (id )>9 :#line:550
                                OOOO0000000OOO0OO =f'_site={O0O00O0OO0O00OO00}_{timi_new()}'#line:551
                                OOOOOO0OOOO0000O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O000OO0OO0O000O .token ,'timestamp':timi_new (),'sign':sign (OOOO0000000OOO0OO ),'signstring':OOOO0000000OOO0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:562
                                O00O00OOOOO0000OO ={"site":O0O00O0OO0O00OO00 }#line:563
                                OO0O000OO00000000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOOOO0OOOO0000O0 ,data =O00O00OOOOO0000OO ).json ()#line:565
                                if 'status'in OO0O000OO00000000 :#line:566
                                    if OO0O000OO00000000 ['status']==200 :#line:567
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:568
                            if id !=0 :#line:569
                                for OO00O0O0O0OOO00O0 in range (11 ):#line:570
                                    O0O00O00O000O00O0 =OO00O0O0O0OOO00O0 +1 #line:571
                                    g =OO00OO000000OOOO0 [O0O00O00O000O00O0 ]['level']#line:572
                                    if id ==g :#line:573
                                        O0000O0000000OOOO =OO00O0O0O0OOO00O0 +2 #line:574
                                        if O0000O0000000OOOO !=O0O00O0OO0O00OO00 +1 :#line:575
                                            OOOOO0OOOO000O0O0 =O0O00O0OO0O00OO00 +1 #line:576
                                            time .sleep (random .randint (1 ,3 )/10 )#line:578
                                            OO00O0OOOOOOO000O =f'_site={OOOOO0OOOO000O0O0 - 1}&targetSite={O0000O0000000OOOO - 1}_{timi_new()}'#line:579
                                            OOOO0O000OO00OO0O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O000OO0OO0O000O .token ,'timestamp':timi_new (),'sign':sign (OO00O0OOOOOOO000O ),'signstring':OO00O0OOOOOOO000O ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:595
                                            O00OO0O0OOOOO0OOO ={"site":int (OOOOO0OOOO000O0O0 -1 ),"targetSite":int (O0000O0000000OOOO -1 )}#line:596
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOOO0O000OO00OO0O ,json =O00OO0O0OOOOO0OOO )#line:597
                                            O0O0000OOOOO0OO00 =True #line:599
                                    if O0O0000OOOOO0OO00 :#line:600
                                        break #line:601
                                if O0O0000OOOOO0OO00 :#line:602
                                    break #line:603
        except :#line:604
            O0O000OO0OO0O000O .synthetic ()#line:605
    def level_new (OOOOO0OOOO00OO000 ):#line:608
        try :#line:609
            O0OO000O00O000OO0 =f'__{timi_new()}'#line:610
            O00O00OOOO000O000 ={'source':'scsc','authorization':OOOOO0OOOO00OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O00O000OO0 ),'signstring':O0OO000O00O000OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:620
            O000O00OO0OO0OO0O =requests .request ('get',f'{host}/user',headers =O00O00OOOO000O000 ).json ()#line:621
            if 'status'in O000O00OO0OO0OO0O :#line:622
                if O000O00OO0OO0OO0O ['status']==200 :#line:623
                    return float (O000O00OO0OO0OO0O ['data']['level'])#line:624
        except Exception as O0OOOOOO0OO0OOOOO :#line:625
            print (O0OOOOOO0OO0OOOOO )#line:626
    def propsraffle (O0O0OO0OO0000O0O0 ):#line:629
        try :#line:630
            while True :#line:631
                O00OO0000O00O000O =f'__{timi_new()}'#line:632
                O00O0OO000000O000 ={'source':'scsc','authorization':O0O0OO0OO0000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0000O00O000O ),'signstring':O00OO0000O00O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:642
                O00O00OO0O00OO0O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00O0OO000000O000 ).json ()#line:643
                if 'status'in O00O00OO0O00OO0O0 :#line:645
                    if O00O00OO0O00OO0O0 ['status']==200 :#line:646
                        O00O0OOO0O00OO0OO =O00O00OO0O00OO0O0 ['data']['rows']#line:647
                        O0O0O0O0OOO0OOOO0 =O00O00OO0O00OO0O0 ['data']['vstate']#line:648
                        if O00O0OOO0O00OO0OO ==5 or O00O0OOO0O00OO0OO ==6 or O00O0OOO0O00OO0OO ==7 :#line:649
                            O00O0OOOOOO000OOO =O00O00OO0O00OO0O0 ['data']['silver']#line:650
                            print (f'【转盘抽奖】:获得种子:{O00O0OOOOOO000OOO}')#line:651
                        if O00O0OOO0O00OO0OO ==1 or O00O0OOO0O00OO0OO ==2 or O00O0OOO0O00OO0OO ==3 :#line:652
                            OOOO000000O00O000 =O00O00OO0O00OO0O0 ['data']['clover']#line:653
                            print (f'【转盘抽奖】:获得三叶草:{OOOO000000O00O000}')#line:654
                        if O00O0OOO0O00OO0OO ==4 or O00O0OOO0O00OO0OO ==8 :#line:655
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:656
                        if O00O0OOO0O00OO0OO =='抽奖次数已用完':#line:660
                            break #line:693
                time .sleep (random .randint (8 ,15 )/10 )#line:694
        except Exception as O000O0000OO000O00 :#line:695
            print (O000O0000OO000O00 )#line:696
    def friends_invitation (O00OO0O0OOO0000O0 ):#line:699
        try :#line:700
            OOO00OO0O0O0O00OO =f'__{timi_new()}'#line:701
            O0O00000O0OOOO0OO ={'source':'scsc','authorization':O00OO0O0OOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0O0O0O00OO ),'signstring':OOO00OO0O0O0O00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:711
            OOO00000OOOO0OO00 =requests .request ('get',f'{host}/friends',headers =O0O00000O0OOOO0OO ).json ()#line:712
            if 'status'in OOO00000OOOO0OO00 :#line:713
                if OOO00000OOOO0OO00 ['status']==200 :#line:714
                    O00OOO00OOOO00OOO =OOO00000OOOO0OO00 ['data']['myInviteter']#line:715
                    if O00OOO00OOOO00OOO :#line:716
                        OO0O000O0OOO0OOO0 =O00OOO00OOOO00OOO ['user']['nickname']#line:717
                        O00OO0OO0OO00O00O =O00OO0O0OOO0000O0 .certification ()#line:718
                        print (f'【查邀请人】:我的邀请人:{OO0O000O0OOO0OOO0}丨实名:{O00OO0OO0OO00O00O}')#line:719
                    else :#line:720
                        if O00OO0O0OOO0000O0 .innerId !='0':#line:721
                            O00OO0O0OOO0000O0 .invitation ()#line:722
        except Exception as O0O0O0O0000O0O0OO :#line:723
            print (O0O0O0O0000O0O0OO )#line:724
    def add_clover (O00000OOO000O0OOO ):#line:727
        global golden_seed #line:728
        try :#line:729
            OO0O00000O00OOOO0 =f'__{timi_new()}'#line:730
            OO0O00O0OO0O00O0O ={'source':'scsc','authorization':O00000OOO000O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00000O00OOOO0 ),'signstring':OO0O00000O00OOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:740
            O00000OO0OOO00OOO =requests .request ('get',f'{host}/assets/clovers',headers =OO0O00O0OO0O00O0O ).json ()#line:741
            if 'status'in O00000OO0OOO00OOO :#line:743
                if O00000OO0OOO00OOO ['status']==200 :#line:744
                    OO00000OO0O0O000O =O00000OO0OOO00OOO ['data']['clover']#line:745
                    OO000O0000OO0O000 =O00000OO0OOO00OOO ['data']['used_clover']#line:746
                    OOO0OOO000OOOO000 =float (OO00000OO0O0O000O )-float (OO000O0000OO0O000 )#line:747
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO000O0000OO0O000}')#line:748
                    if O00000OOO000O0OOO .certification ()!='未实名':#line:749
                        if OOO0OOO000OOOO000 >1 :#line:750
                            OO0O00000O00OOOO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO0OOO000OOOO000)}_{timi_new()}'#line:751
                            O00OOOO0O0O0000OO ={'source':'scsc','authorization':O00000OOO000O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00000O00OOOO0 ),'signstring':OO0O00000O00OOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:761
                            O0000OO0OOOO0O000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO0OOO000OOOO000 )}#line:762
                            OO000O0O00OOOO0OO =requests .request ('post',f'{host}/lottery/add-stake',headers =O00OOOO0O0O0000OO ,data =O0000OO0OOOO0O000 ).json ()#line:763
                            if 'status'in OO000O0O00OOOO0OO :#line:765
                                if OO000O0O00OOOO0OO ['status']==200 :#line:766
                                    print (f'【参与抽奖】:添加☘️:{OO000O0O00OOOO0OO["data"]}丨数量:{OOO0OOO000OOOO000}')#line:767
                                if OO000O0O00OOOO0OO ['status']==500 :#line:768
                                    print (f'【参与抽奖】:添加☘️:{OO000O0O00OOOO0OO["message"]}')#line:769
            OOOO000O00OO00O0O =requests .request ('get',f'{host}/lottery',headers =OO0O00O0OO0O00O0O ).json ()#line:770
            O00OO0000O0OOOOOO =O00000OOO000O0OOO .winning_rewards ()#line:772
            if 'status'in OOOO000O00OO00O0O :#line:773
                if OOOO000O00OO00O0O ['status']==200 :#line:774
                    OOOOOO000O00O00OO =OOOO000O00OO00O0O ['data'][0 ]['day_get_gold_quantity']#line:775
                    golden_seed +=float (OOOOOO000O00O00OO )#line:776
                    O00O0O0O00O000000 =OOOO000O00OO00O0O ['data'][1 ]['value']#line:777
                    O0OO00O00O0OO0OOO =OOOO000O00OO00O0O ['data'][0 ]['join_number']#line:778
                    OO0OO00OOO0O0O00O =int (float (OOOO000O00OO00O0O ['data'][0 ]['totalValue']))#line:779
                    OO00OO00O0OO000O0 =float (O00O0O0O00O000000 /OO0OO00OOO0O0O00O )*10000 #line:780
                    O0OO0OO000O0OOOOO =OO0OO00OOO0O0O00O /O0OO00O00O0OO0OOO #line:781
                    print (f'【参与抽奖】:预计每天中{str(OOOOOO000O00O00OO)[:6]}颗金种子丨好友收益:{str(O00OO0000O0OOOOOO)[:6]}')#line:782
                    print (f'【抽奖统计】:每1万☘️中{str(OO00OO00O0OO000O0)[:6]}颗金种子丨☘️人均:{str(O0OO0OO000O0OOOOO)[:7]}️')#line:783
        except Exception as OO00O0OOO0OOOOO0O :#line:784
            print (OO00O0OOO0OOOOO0O )#line:785
    def energy (OO00OOOOO000O00OO ):#line:789
        try :#line:790
            while True :#line:791
                O0OO0OOO0OO000OOO =f'__{timi_new()}'#line:792
                O00O00O0O000O0O0O ={'source':'scsc','authorization':OO00OOOOO000O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO0OO000OOO ),'signstring':O0OO0OOO0OO000OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:802
                OOO00OOO0O00O0O0O =requests .request ('get',f'{host}/energy/general',headers =O00O00O0O000O0O0O ).json ()#line:803
                if 'status'in OOO00OOO0O00O0O0O :#line:805
                    if OOO00OOO0O00O0O0O ['status']==200 :#line:806
                        OO00O0OO00O00O00O =OOO00OOO0O00O0O0O ['data']['ordinary_water']#line:807
                        OO000OO00000OO0O0 =OOO00OOO0O00O0O0O ['data']['ordinary_fertilizer']#line:808
                        OO0O0OO0O0OO00000 =OOO00OOO0O00O0O0O ['data']['videoStatus']#line:809
                        print (f'【我的营养】:肥料:{str(OO000OO00000OO0O0).split(".")[0]}丨水滴:{str(OO00O0OO00O00O00O).split(".")[0]}')#line:810
                        if float (OO000OO00000OO0O0 )<96 :#line:811
                            if OO0O0OO0O0OO00000 :#line:812
                                time .sleep (random .randint (160 ,180 )/10 )#line:813
                                OOO00OOO000OO0O0O =99 -float (OO000OO00000OO0O0 )#line:814
                                OOOO0O0OO000O0OOO ={"fertilizer":str (OOO00OOO000OO0O0O ).split ('.')[0 ]}#line:815
                                O00O00OOO000O00OO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00O00O0O000O0O0O ).json ()#line:816
                                if 'status'in O00O00OOO000O00OO :#line:818
                                    if O00O00OOO000O00OO ['status']==200 :#line:819
                                        print (f'【购买肥料】:看广告获取肥料:{O00O00OOO000O00OO["message"]}')#line:820
                                    if O00O00OOO000O00OO ['status']==500 :#line:821
                                        print (f'【购买肥料】:看广告获取肥料:{O00O00OOO000O00OO["message"]}')#line:822
                                        break #line:823
                        if float (OO00O0OO00O00O00O )<880 :#line:824
                            time .sleep (random .randint (160 ,180 )/10 )#line:825
                            O0O00O000O0000O00 =999 -float (OO00O0OO00O00O00O )#line:826
                            O0OO00O00OOO0O000 ={"water":str (O0O00O000O0000O00 ).split ('.')[0 ]}#line:827
                            OOOO0O000O0OOO0O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00O00O0O000O0O0O ).json ()#line:828
                            if 'status'in OOOO0O000O0OOO0O0 :#line:830
                                if OOOO0O000O0OOO0O0 ['status']==200 :#line:831
                                    print (f'【购买水滴】:看广告获取水滴:{OOOO0O000O0OOO0O0["message"]}')#line:832
                                if OOOO0O000O0OOO0O0 ['status']==500 :#line:833
                                    print (f'【购买水滴】:看广告获取水滴:{OOOO0O000O0OOO0O0["message"]}')#line:834
                                    break #line:835
                        break #line:837
        except Exception as O000000OOOOOO00OO :#line:839
            print (O000000OOOOOO00OO )#line:840
def bundled_def ():#line:842
    OO00OO0000000OOOO =['5570536','7750212','7911652','7911680','7805624']#line:843
    return OO00OO0000000OOOO [random .randint (0 ,len (OO00OO0000000OOOO )-1 )]#line:844
def version_of_the_validation ():#line:848
    return str ((80 -56 )/10 )#line:849
def gitee_validation ():#line:852
    try :#line:853
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:854
    except :#line:855
        sys .exit (0 )#line:856
def update_the_validation ():#line:860
    try :#line:861
        O0O0O00O000O00O0O =gitee_validation ()#line:862
        if version_of_the_validation ()<O0O0O00O000O00O0O ['CityEarth']['edition']:#line:863
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0O00O000O00O0O["CityEarth"]["edition"]}   ❌')#line:864
            print (f'更新内容=>>{O0O0O00O000O00O0O["CityEarth"]["content"]}   🎉')#line:865
        else :#line:866
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0O00O000O00O0O["CityEarth"]["edition"]}   ✅')#line:867
            print (f'更新内容=>> {O0O0O00O000O00O0O["CityEarth"]["content"]}   🎉')#line:868
    except Exception as O0O0OO00OOOOO0O00 :#line:869
        print (O0O0OO00OOOOO0O00 )#line:870
def os_qinglong ():#line:873
    if application in os .environ :#line:874
        O00O00O0O0O00O0OO =os .environ [application ].split ('\n')#line:875
        if len (O00O00O0O0O00O0OO )>0 :#line:876
            return O00O00O0O0O00O0OO #line:877
        else :#line:878
            print (f"{application}变量未启用")#line:879
            print ('脚本退出')#line:880
            sys .exit (1 )#line:881
    else :#line:882
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:884
        return os_built ()#line:885
def os_built ():#line:888
    if token :#line:889
        OO00O00OO0OO0O000 =token .split ('\n')#line:890
        if len (OO00O00OO0OO0O000 )>0 :#line:891
            return OO00O00OO0OO0O000 #line:892
    else :#line:893
        print (f"内置变量为空")#line:894
        print ('脚本结束')#line:895
        sys .exit (0 )#line:896
if __name__ =='__main__':#line:899
    start ()#line:900
