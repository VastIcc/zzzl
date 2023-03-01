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
@ 版本  2.6
"""
application = 'ce_token'  # 变量名
token = ''

##################################配置区##################################
energy =False #line:1
token_zs =''#line:2
zh_mony ='3'#line:3
fertilizer_quantity =40 #line:4
wadverti_quantity =500 #line:5
time_xx =random .randint (12 ,18 )#line:6
version ='3.1.41954131'#line:10
git ='https://gitee.com'#line:11
host ='http://scsc.sc19319.com'#line:12
golden_seed =0 #line:13
msg_list =[]#line:14
def start ():#line:16
    try :#line:17
        update_the_validation ()#line:18
        O0OOO0OOOOOOOOO00 =os_qinglong ()#line:19
        print (f"==========共找到{len(O0OOO0OOOOOOOOO00)}个账号==========")#line:20
        for OO00O0O0OO000OO00 in O0OOO0OOOOOOOOO00 :#line:21
            OO0O00000O0O000OO =[]#line:22
            print (f"------------正在执行第{O0OOO0OOOOOOOOO00.index(OO00O0O0OO000OO00) + 1}个账号------------")#line:23
            OOO00OOOO00OO0OO0 =CityEarth (OO00O0O0OO000OO00 ,OO0O00000O0O000OO )#line:24
            def O0OO0O00000O00OOO ():#line:26
                if OOO00OOOO00OO0OO0 .base_info ():#line:28
                    OOO00OOOO00OO0OO0 .sealing ()#line:30
                    OOO00OOOO00OO0OO0 .invitenum ()#line:32
                    OOO00OOOO00OO0OO0 .game_map ()#line:34
                    OOO00OOOO00OO0OO0 .friends_invitation ()#line:36
                    OOO00OOOO00OO0OO0 .energy ()#line:38
                    OOO00OOOO00OO0OO0 .add_clover ()#line:40
                    OOO00OOOO00OO0OO0 .propsraffle ()#line:42
                    OOO00OOOO00OO0OO0 .synthetic ()#line:44
                    OOO00OOOO00OO0OO0 .crops_illustrated ()#line:46
                    OOO00OOOO00OO0OO0 .give_gold ()#line:48
                    OOO00OOOO00OO0OO0 .withdraw ()#line:50
            OO00OOO0OO0OO000O =threading .Thread (target =O0OO0O00000O00OOO )#line:52
            OO00OOO0OO0OO000O .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理推送通知------------")#line:55
        time .sleep (0.5 )#line:56
        OOOO0OOO000O0OOO0 =format_msg ()#line:57
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOOO0OOO000O0OOO0 +' ')#line:58
    except Exception as O000OO0O0O0000000 :#line:59
        print (O000OO0O0O0000000 )#line:60
def give_gold (OO0OOO0OO00O000OO ):#line:63
        try :#line:64
            O0000OOO0O00OOO0O =zh_mony #line:65
            OO00O00O0000OO0OO =f'_doneeNo={OO0OOO0OO00O000OO}&quantity={O0000OOO0O00OOO0O}_{timi_new()}'#line:66
            OOOOOOOO0OOO000OO ={'source':'scsc','authorization':token_zs .split ('&')[0 ],'timestamp':str (timi_new ()),'sign':sign (OO00O00O0000OO0OO ),'signstring':OO00O00O0000OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:77
            OOO000OO00O00O0O0 ={"quantity":O0000OOO0O00OOO0O ,"doneeNo":OO0OOO0OO00O000OO }#line:81
            O0O000OO0O00OOO0O =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOOOOO0OOO000OO ,data =OOO000OO00O00O0O0 ).json ()#line:82
            if 'status'in O0O000OO0O00OOO0O :#line:84
                if O0O000OO0O00OOO0O ['status']==200 :#line:85
                    if O0O000OO0O00OOO0O ['data']:#line:86
                        print (f'【赠送种子】:赠送{O0000OOO0O00OOO0O}种子给{OO0OOO0OO00O000OO}成功')#line:87
                if O0O000OO0O00OOO0O ['status']==401 :#line:88
                    print (f'【赠送种子】:{O0O000OO0O00OOO0O["message"]}')#line:89
                if O0O000OO0O00OOO0O ['status']==500 :#line:90
                    print (f'【赠送种子】:{O0O000OO0O00OOO0O["message"]}')#line:91
        except Exception as OO0O0O0O0OOOOO0O0 :#line:92
            print (OO0O0O0O0OOOOO0O0 )#line:93
def sign (OOO0000O00000O000 ):#line:96
    O000OOO0O00OOO0O0 =hashlib .md5 (OOO0000O00000O000 .encode ()).hexdigest ()#line:97
    O000OOOOO0OO0OOOO ="scsc%^&*"+O000OOO0O00OOO0O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:98
    O0O0OOOOO0OOO0O00 =hashlib .md5 (O000OOOOO0OO0OOOO .encode ()).hexdigest ()#line:99
    return O0O0OOOOO0OOO0O00 #line:100
def format_msg ():#line:102
    OO0OOOOOO00O0OOO0 =""#line:103
    for OO0OOOOO0OOOOOO0O in msg_list :#line:104
        OO0OOOOOO00O0OOO0 +=str (OO0OOOOO0OOOOOO0O )+"\r\n"#line:105
    return OO0OOOOOO00O0OOO0 #line:106
def timi_new ():#line:108
    return str (int (time .time ()*1000 ))#line:109
class CityEarth :#line:112
    def __init__ (OO0O0O0O00OO00OOO ,O0OOOO00OO0OOOO0O ,O0OOOO0O00000O000 ):#line:114
        try :#line:115
            OO0O0O0O00OO00OOO .msg =O0OOOO0O00000O000 #line:116
            OO0O0O0O00OO00OOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:117
            OO0O0O0O00OO00OOO .token =O0OOOO00OO0OOOO0O .split ('&')[0 ]#line:118
            OO0O0O0O00OO00OOO .innerId =O0OOOO00OO0OOOO0O .split ('&')[1 ]#line:119
            OO0O0O0O00OO00OOO .doneeNo =O0OOOO00OO0OOOO0O .split ('&')[2 ]#line:120
        except :#line:121
            print ('变量格式错误')#line:122
    def base_info (OO0O00OO0O0O0OO00 ):#line:125
        try :#line:126
            OO0O00OO0O0O0OO00 .watched_ad ()#line:128
            OOOO000O0OOO0OOO0 =f'__{timi_new()}'#line:129
            OOOO000O000O0OOO0 ={'source':'scsc','authorization':OO0O00OO0O0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O0OOO0OOO0 ),'signstring':OOOO000O0OOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:140
            OO0000O0O0OO0000O =requests .request ('get',f'{host}/user',headers =OOOO000O000O0OOO0 ).json ()#line:141
            if 'status'in OO0000O0O0OO0000O :#line:143
                if OO0000O0O0OO0000O ['status']==200 :#line:144
                    OO00000OO000OOO00 =OO0000O0O0OO0000O ['data']['nickname']#line:145
                    OOO0000OOOOOOO0OO =OO0000O0O0OO0000O ['data']['inner_id']#line:146
                    O0OO0OO0000OOO00O =OO0000O0O0OO0000O ['data']['assets']['gold']#line:147
                    O0O000000OOOO00O0 =OO0000O0O0OO0000O ['data']['level']#line:148
                    print (f'【账号信息】:昵称:{OO00000OO000OOO00[:5]}丨ID:{OOO0000OOOOOOO0OO}丨等级:{O0O000000OOOO00O0}丨金种子:{str(O0OO0OO0000OOO00O).split(".")[0]}')#line:149
                if OO0000O0O0OO0000O ['status']==401 :#line:150
                    print (OO0000O0O0OO0000O ['message'])#line:151
                    OO0O00OO0O0O0OO00 .msg .append ('有账号失效了')#line:152
                    return False #line:153
                if OO0000O0O0OO0000O ['status']==500 :#line:154
                    return False #line:155
            return True #line:156
        except Exception as OOO0OO000O000O0OO :#line:157
            print (OOO0OO000O000O0OO )#line:158
    def sealing (O00O00000O0OO0000 ):#line:161
        try :#line:162
            O000OOOO00O00OO0O =f'__{timi_new()}'#line:163
            O0000000OOOOO00O0 ={'source':'scsc','authorization':O00O00000O0OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOO00O00OO0O ),'signstring':O000OOOO00O00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:174
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0000000OOOOO00O0 )#line:175
            requests .request ('get',f'{host}/packsack/list',headers =O0000000OOOOO00O0 )#line:176
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0000000OOOOO00O0 )#line:177
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0000000OOOOO00O0 )#line:178
            requests .request ('get',f'{host}/user',headers =O0000000OOOOO00O0 )#line:179
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0000000OOOOO00O0 )#line:180
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0000000OOOOO00O0 )#line:181
            requests .request ('post',f'{host}/announcement/announcement',headers =O0000000OOOOO00O0 )#line:182
            requests .request ('get',f'{host}/game/getAllData',headers =O0000000OOOOO00O0 )#line:183
            requests .request ('get',f'{host}/assets',headers =O0000000OOOOO00O0 )#line:184
        except Exception as O00OO00000OO0OO00 :#line:185
            print (O00OO00000OO0OO00 )#line:186
    def withdraw (O0O00O000O00OOOOO ):#line:190
        OOOO00OO0O0O00O0O =f'__{timi_new()}'#line:191
        O0O00OO00OO00O000 ={'source':'scsc','authorization':O0O00O000O00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO0O0O00O0O ),'signstring':OOOO00OO0O0O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:202
        OO0O0O0O0OOO00000 =requests .request ('get',f'{host}/assets',headers =O0O00OO00OO00O000 ).json ()#line:203
        if 'status'in OO0O0O0O0OOO00000 :#line:205
            if OO0O0O0O0OOO00000 ['status']==200 :#line:206
                OOOOO00OOOO0OOO00 =OO0O0O0O0OOO00000 ['data']['cash']#line:207
                if float (OOOOO00OOOO0OOO00 )>20 :#line:208
                    OOOO00OO0O0O00O0O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:209
                    O0O00OO00OO00O000 ={'authorization':O0O00O000O00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO0O0O00O0O ),'signstring':OOOO00OO0O0O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:219
                    OOO00O0O0000O0O00 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:220
                    O0OO0O0O000O0O00O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O00OO00OO00O000 ,data =OOO00O0O0000O0O00 ).json ()#line:222
                    print (O0OO0O0O000O0O00O )#line:223
    def invitenum (OOO0OOO0O0O00O0O0 ):#line:226
        OOOO00O00OO00O0O0 =f'__{timi_new()}'#line:227
        OOOOO00OO0OO00000 ={'source':'scsc','authorization':OOO0OOO0O0O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O00OO00O0O0 ),'signstring':OOOO00O00OO00O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:238
        OO00O0O00O00O0O00 =requests .request ('get',f'{host}/invite/invitenum',headers =OOOOO00OO0OO00000 ).json ()#line:239
        if 'status'in OO00O0O00O00O0O00 :#line:241
            if OO00O0O00O00O0O00 ['status']==200 :#line:242
                OOOO0O0OO0000OOO0 =OO00O0O00O00O0O00 ['data']['invited_count']#line:243
                OO0O000OOO0O00OO0 =OO00O0O00O00O0O00 ['data']['invited_second_count']#line:244
                print (f'【我的邀请】:直邀好友:{OOOO0O0OO0000OOO0}丨间邀好友:{OO0O000OOO0O00OO0}')#line:245
    def game_map (O0OOO0OOO0000O00O ):#line:248
        try :#line:249
            O00O00O0OO00O0O00 =f'__{timi_new()}'#line:250
            OO0O0OO00OOO00O0O ={'source':'scsc','authorization':O0OOO0OOO0000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0OO00O0O00 ),'signstring':O00O00O0OO00O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:261
            O0O000O0O0000000O =requests .request ('get',f'{host}/game/map',headers =OO0O0OO00OOO00O0O ).json ()#line:262
            if 'status'in O0O000O0O0000000O :#line:264
                if O0O000O0O0000000O ['status']==200 :#line:265
                    for O0OO000O0O000000O in O0O000O0O0000000O ['data']['list'][0 ]['crops']:#line:266
                        O000O0O00O0OOO0OO =O0OO000O0O000000O ['level']#line:268
                        if O000O0O00O0OOO0OO ==41 :#line:269
                            OOO00000000OO00OO =O0OO000O0O000000O ['crop_name']#line:270
                            OO0O00O0OO00O000O =O0OO000O0O000000O ['count']#line:271
                            if OO0O00O0OO00O000O >0 :#line:272
                                print (f'【农业资产】:{OOO00000000OO00OO}丨数量:{OO0O00O0OO00O000O}')#line:273
        except Exception as O0O0OOO0O0O00OO0O :#line:274
            print (O0O0OOO0O0O00OO0O )#line:275
    def give_gold (OOOO0000O00O0O000 ):#line:278
        try :#line:279
            O00000O0O0O0000OO =f'__{timi_new()}'#line:280
            OOO0O0OO0O0OO0OOO ={'source':'scsc','authorization':OOOO0000O00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0O0O0000OO ),'signstring':O00000O0O0O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:291
            O0O0O0O0OO000OO0O =requests .request ('get',f'{host}/user',headers =OOO0O0OO0O0OO0OOO ).json ()#line:292
            if 'status'in O0O0O0O0OO000OO0O :#line:293
                if O0O0O0O0OO000OO0O ['status']==200 :#line:294
                    if float (OOOO0000O00O0O000 .doneeNo )!=0 :#line:295
                        OO00000O0000OOOOO =O0O0O0O0OO000OO0O ['data']['assets']['gold']#line:296
                        if float (OO00000O0000OOOOO )>float (OOOO0000O00O0O000 .innerId ):#line:297
                            OOO0OOOO0OO0O00OO =int (float (OO00000O0000OOOOO )/1.1 )#line:298
                            O00000O0O0O0000OO =f'_doneeNo={OOOO0000O00O0O000.doneeNo}&quantity={OOO0OOOO0OO0O00OO}_{timi_new()}'#line:299
                            OOO0O0OO0O0OO0OOO ={'source':'scsc','authorization':OOOO0000O00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0O0O0000OO ),'signstring':O00000O0O0O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:310
                            O000OO0OO00O0OO0O ={"quantity":OOO0OOOO0OO0O00OO ,"doneeNo":OOOO0000O00O0O000 .doneeNo }#line:314
                            OO0O00O0O0OO000O0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0O0OO0O0OO0OOO ,data =O000OO0OO00O0OO0O ).json ()#line:315
                            if 'status'in OO0O00O0O0OO000O0 :#line:317
                                if OO0O00O0O0OO000O0 ['status']==200 :#line:318
                                    if OO0O00O0O0OO000O0 ['data']:#line:319
                                        print (f'【赠送种子】:赠送{OOO0OOOO0OO0O00OO}种子给{OOOO0000O00O0O000.doneeNo}成功')#line:320
                    else :#line:321
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:322
        except Exception as OO0OO00OO000O0OOO :#line:323
            print (OO0OO00OO000O0OOO )#line:324
    def invitation (OOO0OOOOO0O0OO00O ):#line:326
        try :#line:327
            _OO000OOO000OOOO0O =float (bundled_def ())/4 #line:328
            O0O0O00OOO0O0O0O0 =f'_innerId={int(_OO000OOO000OOOO0O)}_{timi_new()}'#line:329
            O0OO0OOOOOOO0OO00 ={'source':'scsc','authorization':OOO0OOOOO0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OOO0O0O0O0 ),'signstring':O0O0O00OOO0O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:340
            O00OOOO0O0OOO000O ={"innerId":int (_OO000OOO000OOOO0O )}#line:341
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0OO0OOOOOOO0OO00 ,data =O00OOOO0O0OOO000O )#line:342
        except Exception as OOO0O0OO0O0000O0O :#line:343
            print (OOO0O0OO0O0000O0O )#line:344
    def winning_rewards (O0OOO0O00O0O00O00 ):#line:347
        try :#line:348
            OOO0OO0O0O0O0OO00 =f'__{timi_new()}'#line:349
            O0O0000O000OO0000 ={'source':'scsc','authorization':O0OOO0O00O0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O0O0O0OO00 ),'signstring':OOO0OO0O0O0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:360
            O00000OOO00000OO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O0000O000OO0000 ).json ()#line:361
            if 'status'in O00000OOO00000OO0 :#line:363
                if O00000OOO00000OO0 ['status']==200 :#line:364
                    if O00000OOO00000OO0 ['data']['amount']:#line:365
                        OO0000O00O0O000OO =O00000OOO00000OO0 ['data']['amount']['gold']#line:366
                        return OO0000O00O0O000OO #line:367
                    else :#line:368
                        return 0 #line:369
        except Exception as O00OOO0O0O00OO000 :#line:370
            print (O00OOO0O0O00OO000 )#line:371
    def certification (OO000OOO00O0O0OO0 ):#line:374
        try :#line:375
            O0000O00O0O000OOO =f'__{timi_new()}'#line:376
            O0OOO0OO0OOO0OO0O ={'source':'scsc','authorization':OO000OOO00O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00O0O000OOO ),'signstring':O0000O00O0O000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:387
            OO000O000O0OOOOOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0OOO0OO0OOO0OO0O ).json ()#line:388
            if 'status'in OO000O000O0OOOOOO :#line:390
                if OO000O000O0OOOOOO ['status']==200 :#line:391
                    if OO000O000O0OOOOOO ['data']['result']:#line:392
                        O00OOO0OO00O00000 =OO000O000O0OOOOOO ['data']['nick_name']#line:393
                        return O00OOO0OO00O00000 #line:394
                    else :#line:395
                        return '未实名'#line:396
        except Exception as O0000000O000OO00O :#line:397
            print (O0000000O000OO00O )#line:398
    def crops_illustrated (OOOO00OO0OO0OOOO0 ):#line:401
        try :#line:402
            OO00OO00OOO0OO00O =f'__{timi_new()}'#line:403
            OOO000000000OO0OO ={'source':'scsc','authorization':OOOO00OO0OO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO00OOO0OO00O ),'signstring':OO00OO00OOO0OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:414
            O0O0O00OO0OOOO000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO000000000OO0OO ).json ()#line:415
            if 'status'in O0O0O00OO0OOOO000 :#line:417
                if O0O0O00OO0OOOO000 ['status']==200 :#line:418
                    OO0O0000OO00OOOOO =O0O0O00OO0OOOO000 ['data'][0 ]['crops']#line:419
                    for O0OOO000OO0O0OO0O in OO0O0000OO00OOOOO :#line:420
                        if O0OOO000OO0O0OO0O ['ill_clover_award']:#line:421
                            if float (O0OOO000OO0O0OO0O ['ill_clover_award'])>1 :#line:422
                                if O0OOO000OO0O0OO0O ['is_finish']:#line:423
                                    if not O0OOO000OO0O0OO0O ['is_getit']:#line:424
                                        if OOOO00OO0OO0OOOO0 .certification ()!='未实名':#line:425
                                            OO00OO00OOO0OO00O =f'_award_level={O0OOO000OO0O0OO0O["level"]}_{timi_new()}'#line:426
                                            OOO000000000OO0OO ={'source':'scsc','authorization':OOOO00OO0OO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO00OOO0OO00O ),'signstring':OO00OO00OOO0OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:437
                                            OOO0O0000OO00O0O0 ={"award_level":O0OOO000OO0O0OO0O ['level']}#line:438
                                            OOOO0OO0OO00OO000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO000000000OO0OO ,json =OOO0O0000OO00O0O0 ).json ()#line:440
                                            if 'status'in OOOO0OO0OO00OO000 :#line:441
                                                if OOOO0OO0OO00OO000 ['status']==200 :#line:442
                                                    O000O00OO00000OO0 =OOOO0OO0OO00OO000 ['data']['ill_clover_award']#line:443
                                                    print (f'【图鉴奖励】:领取{O0OOO000OO0O0OO0O["crop_name"]}成就丨奖励{O000O00OO00000OO0}☘️')#line:445
                                                if OOOO0OO0OO00OO000 ['status']==500 :#line:446
                                                    print (f'【图鉴奖励】:{OOOO0OO0OO00OO000["message"]}')#line:447
        except Exception as OO0OOO00OO0O0O0O0 :#line:448
            print (OO0OOO00OO0O0O0O0 )#line:449
    def watched_ad (O00OO0O00OO0O00O0 ):#line:452
        try :#line:453
            OOOOOO000O0O00O00 =f'__{timi_new()}'#line:454
            OO0O00O0O00OOOOOO ={'source':'scsc','authorization':O00OO0O00OO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO000O0O00O00 ),'signstring':OOOOOO000O0O00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:465
            O00O0OO000O00OOOO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00O0O00OOOOOO ).json ()#line:466
            if 'status'in O00O0OO000O00OOOO :#line:468
                if O00O0OO000O00OOOO ['status']==200 :#line:469
                    if 'offlineInfo'in O00O0OO000O00OOOO ['data']:#line:470
                        time .sleep (random .randint (3 ,5 ))#line:471
                        O00OO000OO0O0OOOO =O00O0OO000O00OOOO ['data']['offlineInfo']['off_minute']#line:472
                        O0OO0O0O0OOOOOO00 =float (O00O0OO000O00OOOO ['data']['silver'])/1000000000000 #line:473
                        time .sleep (1 )#line:474
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0O00O0O00OOOOOO ).json ()#line:475
                        time .sleep (2 )#line:476
                        OOOO00000O0O0O0O0 =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00O0O00OOOOOO ).json ()#line:477
                        if 'status'in OOOO00000O0O0O0O0 :#line:479
                            if OOOO00000O0O0O0O0 ['status']==200 :#line:480
                                O0000OO00000OO0O0 =float (OOOO00000O0O0O0O0 ['data']['silver'])/1000000000000 #line:481
                                OO000000OOOOOOO0O =str (O0000OO00000OO0O0 -O0OO0O0O0OOOOOO00 )[:6 ]#line:482
                                print (f'【离线奖励】:翻倍离线{O00OO000OO0O0OOOO}分钟奖励🌱数量:{OO000000OOOOOOO0O}t粒')#line:483
        except Exception as OOOO00O0OO0O0OO0O :#line:484
            print (OOOO00O0OO0O0OO0O )#line:485
    def user_ad (O0O0OOOO00OOOO0OO ):#line:488
        try :#line:489
            OOOOOO00O00O00O00 =f'__{timi_new()}'#line:490
            O0O0O0O0OO0O00000 ={'source':'scsc','authorization':O0O0OOOO00OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00O00O00O00 ),'signstring':OOOOOO00O00O00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:501
            OOOO000O000O0O0O0 =requests .request ('get',f'{host}/user/ad',headers =O0O0O0O0OO0O00000 ).json ()#line:502
            if 'status'in OOOO000O000O0O0O0 :#line:504
                if OOOO000O000O0O0O0 ['status']==200 :#line:505
                    OOO00O00O00O00O00 =OOOO000O000O0O0O0 ['data']['max_time']#line:506
                    O0000OO0O00O0OOOO =OOOO000O000O0O0O0 ['data']['watch_time']#line:507
                    O000O000O000O000O =OOOO000O000O0O0O0 ['data']['added_time']#line:508
                    print (f'【获取种子】:获取🌱剩余{O000O000O000O000O + OOO00O00O00O00O00 - O0000OO0O00O0OOOO}次丨好友提供:{O000O000O000O000O}次')#line:509
                    if O000O000O000O000O +OOO00O00O00O00O00 -O0000OO0O00O0OOOO >0 :#line:510
                        time .sleep (random .randint (16 ,19 ))#line:511
                        OOO0OOOOOO00O0O0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O0O0O0OO0O00000 ).json ()#line:512
                        if 'status'in OOO0OOOOOO00O0O0O :#line:514
                            if OOO0OOOOOO00O0O0O ['status']==200 :#line:515
                                O00O0OOO0O0OOOO0O =float (OOO0OOOOOO00O0O0O ['data']['silver'])/1000000000000 #line:516
                                print (f'【获取种子】:获得🌱:{int(O00O0OOO0O0OOOO0O)}t粒')#line:517
                                return True #line:518
                            if OOO0OOOOOO00O0O0O ['status']==500 :#line:519
                                O000O0OOOO00O0O00 =OOO0OOOOOO00O0O0O ['message']#line:520
                                print (f'【获取种子】:{O000O0OOOO00O0O00}')#line:521
                                return False #line:522
        except Exception as OO00O0000OO000O0O :#line:523
            print (OO00O0000OO000O0O )#line:524
    def synthetic (O0OOOO0OO0000O00O ):#line:527
        global id ,g #line:528
        try :#line:529
            O0O0O0OO00OO0O0OO =O0OOOO0OO0000O00O .level_new ()#line:530
            OO0OOO0OOOOOOO0O0 =random .randint (9 ,11 )#line:531
            OO000OOO0O00OO000 =f'_site=8&targetSite={OO0OOO0OOOOOOO0O0}_{timi_new()}'#line:532
            OOOOO0O0O0OO00000 ={'source':'scsc','authorization':O0OOOO0OO0000O00O .token ,'timestamp':timi_new (),'sign':sign (OO000OOO0O00OO000 ),'signstring':OO000OOO0O00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:543
            OOOO000OO0000O000 ={"site":int (8 ),"targetSite":int (OO0OOO0OOOOOOO0O0 )}#line:544
            requests .request ('post',f'{host}/game/crops/move',headers =OOOOO0O0O0OO00000 ,json =OOOO000OO0000O000 )#line:545
            while True :#line:546
                OOOOO0OOO0000O0O0 =f'__{timi_new()}'#line:547
                OO00OOOO00OO0OO00 ={'source':'scsc','authorization':O0OOOO0OO0000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOO0000O0O0 ),'signstring':OOOOO0OOO0000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:558
                OOOO00O00OOOOO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =OO00OOOO00OO0OO00 ).json ()#line:559
                if 'status'in OOOO00O00OOOOO0O0 :#line:561
                    if OOOO00O00OOOOO0O0 ['status']==200 :#line:562
                        OOO0O0OOOO0OO0O0O =OOOO00O00OOOOO0O0 ['data']['cropList']#line:563
                        O0O0O0000O0000O00 =OOOO00O00OOOOO0O0 ['data']['gameCoreDataDBid']#line:564
                        O0O0O0OOOO0OOO00O =float (OOOO00O00OOOOO0O0 ['data']['silver'])/1000000000000 #line:565
                        O0OO0000O000O0O0O =0 #line:570
                        for O0OO0O0O0OOO0OO00 in OOO0O0OOOO0OO0O0O :#line:571
                            if not O0OO0O0O0OOO0OO00 :#line:572
                                O0OOOOO00OO0OOO00 =f'_crop_id={O0O0O0000O0000O00}&site={O0OO0000O000O0O0O}_{O0OOOO0OO0000O00O.time}'#line:573
                                OOO0000O0O0000O00 ={'source':'scsc','authorization':O0OOOO0OO0000O00O .token ,'timestamp':O0OOOO0OO0000O00O .time ,'sign':sign (O0OOOOO00OO0OOO00 ),'signstring':O0OOOOO00OO0OOO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
                                OO0OO0OO000OO0O00 ={"site":O0OO0000O000O0O0O ,"crop_id":O0O0O0000O0000O00 }#line:584
                                OO000OOOOO0OO0O00 =requests .request ('post',f'{host}/game/crops/buy',headers =OOO0000O0O0000O00 ,data =OO0OO0OO000OO0O00 ).json ()#line:585
                                time .sleep (random .randint (1 ,3 )/10 )#line:587
                                if 'status'in OO000OOOOO0OO0O00 :#line:588
                                    if OO000OOOOO0OO0O00 ['status']==200 :#line:589
                                        if OO000OOOOO0OO0O00 ['message']=='种子数量不足':#line:590
                                            O0O0O0OO00OO0O0OO =O0OOOO0OO0000O00O .level_new ()#line:591
                                            print (f'【种植合成】:{OO000OOOOO0OO0O00["message"]}')#line:592
                                            if not O0OOOO0OO0000O00O .user_ad ():#line:593
                                                return False #line:594
                                    if OO000OOOOO0OO0O00 ['status']==500 :#line:595
                                        print (f'【种植合成】:{OO000OOOOO0OO0O00["message"]}')#line:596
                                        return False #line:597
                            O0OO0000O000O0O0O +=1 #line:598
                        O0OOOOO0OO0OOO00O =requests .request ('get',f'{host}/game/getAllData',headers =OO00OOOO00OO0OO00 ).json ()#line:599
                        OO00O0OO0OOO0O0OO =O0OOOOO0OO0OOO00O ['data']['cropList']#line:600
                        O00OO00OO0OO00000 =False #line:601
                        for O0OO0O0O0OOO0OO00 in range (12 ):#line:602
                            id =OO00O0OO0OOO0O0OO [O0OO0O0O0OOO0OO00 ]['level']#line:603
                            if float (O0O0O0OO00OO0O0OO )-float (id )>9 :#line:604
                                O00OOO0OOOO0OO0O0 =f'_site={O0OO0O0O0OOO0OO00}_{timi_new()}'#line:605
                                OO000O0O00OO00O00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0OOOO0OO0000O00O .token ,'timestamp':timi_new (),'sign':sign (O00OOO0OOOO0OO0O0 ),'signstring':O00OOO0OOOO0OO0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:616
                                OO0OO00000OOOOO00 ={"site":O0OO0O0O0OOO0OO00 }#line:617
                                O0000O00OO0O0O0OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO000O0O00OO00O00 ,data =OO0OO00000OOOOO00 ).json ()#line:619
                                if 'status'in O0000O00OO0O0O0OO :#line:620
                                    if O0000O00OO0O0O0OO ['status']==200 :#line:621
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:622
                            if id !=0 :#line:623
                                for O0OOOOOOO00OOO0O0 in range (11 ):#line:624
                                    O0OO0OOOO000O0O0O =O0OOOOOOO00OOO0O0 +1 #line:625
                                    g =OO00O0OO0OOO0O0OO [O0OO0OOOO000O0O0O ]['level']#line:626
                                    if id ==g :#line:627
                                        O0OO000OO0O0O0O00 =O0OOOOOOO00OOO0O0 +2 #line:628
                                        if O0OO000OO0O0O0O00 !=O0OO0O0O0OOO0OO00 +1 :#line:629
                                            OOOO0000O000O0OOO =O0OO0O0O0OOO0OO00 +1 #line:630
                                            time .sleep (random .randint (1 ,3 )/10 )#line:632
                                            OO000OOO0O00OO000 =f'_site={OOOO0000O000O0OOO - 1}&targetSite={O0OO000OO0O0O0O00 - 1}_{timi_new()}'#line:633
                                            OOOOO0O0O0OO00000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0OOOO0OO0000O00O .token ,'timestamp':timi_new (),'sign':sign (OO000OOO0O00OO000 ),'signstring':OO000OOO0O00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:650
                                            OOOO0O000O0O0O0O0 ={"site":int (OOOO0000O000O0OOO -1 ),"targetSite":int (O0OO000OO0O0O0O00 -1 )}#line:651
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOOOO0O0O0OO00000 ,json =OOOO0O000O0O0O0O0 )#line:652
                                            O00OO00OO0OO00000 =True #line:654
                                    if O00OO00OO0OO00000 :#line:655
                                        break #line:656
                                if O00OO00OO0OO00000 :#line:657
                                    break #line:658
        except :#line:659
            O0OOOO0OO0000O00O .synthetic ()#line:660
    def level_new (OO000000O00O00O0O ):#line:663
        try :#line:664
            OOOO0OOO0O00O0OOO =f'__{timi_new()}'#line:665
            OO00000OO0OOOO000 ={'source':'scsc','authorization':OO000000O00O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO0O00O0OOO ),'signstring':OOOO0OOO0O00O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:676
            O00OOOOO00OOOOO00 =requests .request ('get',f'{host}/user',headers =OO00000OO0OOOO000 ).json ()#line:677
            if 'status'in O00OOOOO00OOOOO00 :#line:678
                if O00OOOOO00OOOOO00 ['status']==200 :#line:679
                    return float (O00OOOOO00OOOOO00 ['data']['level'])#line:680
        except Exception as O0000O00OOO0O0000 :#line:681
            print (O0000O00OOO0O0000 )#line:682
    def propsraffle (O000O0OOOOO0OO000 ):#line:685
        try :#line:686
            while True :#line:687
                O00O000OOOO00OO00 =f'__{timi_new()}'#line:688
                O00O00OO00OO00OOO ={'source':'scsc','authorization':O000O0OOOOO0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OOOO00OO00 ),'signstring':O00O000OOOO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:699
                OOO00OOO00O00O0O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00O00OO00OO00OOO ).json ()#line:700
                if 'status'in OOO00OOO00O00O0O0 :#line:702
                    if OOO00OOO00O00O0O0 ['status']==200 :#line:703
                        O0OO00OO0000O0000 =OOO00OOO00O00O0O0 ['data']['rows']#line:704
                        O00OOO00OO00O00OO =OOO00OOO00O00O0O0 ['data']['vstate']#line:705
                        if O0OO00OO0000O0000 ==5 or O0OO00OO0000O0000 ==6 or O0OO00OO0000O0000 ==7 :#line:706
                            O0O0OO0O0O00OO00O =OOO00OOO00O00O0O0 ['data']['silver']#line:707
                            print (f'【转盘抽奖】:获得种子:{O0O0OO0O0O00OO00O}')#line:708
                        if O0OO00OO0000O0000 ==1 or O0OO00OO0000O0000 ==2 or O0OO00OO0000O0000 ==3 :#line:709
                            O00OOO0000O000OOO =OOO00OOO00O00O0O0 ['data']['clover']#line:710
                            print (f'【转盘抽奖】:获得三叶草:{O00OOO0000O000OOO}')#line:711
                        if O0OO00OO0000O0000 ==4 or O0OO00OO0000O0000 ==8 :#line:712
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:713
                        if O0OO00OO0000O0000 =='抽奖次数已用完':#line:717
                            break #line:751
                time .sleep (random .randint (8 ,15 )/10 )#line:752
        except Exception as O00OOOOOO0000000O :#line:753
            print (O00OOOOOO0000000O )#line:754
    def friends_invitation (O0O00O00O000O0O0O ):#line:757
        try :#line:758
            O0OOO0O0O00000O00 =f'__{timi_new()}'#line:759
            OOOOO00OO0000OOOO ={'source':'scsc','authorization':O0O00O00O000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O0O00000O00 ),'signstring':O0OOO0O0O00000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:770
            O0000O00000O0OO00 =requests .request ('get',f'{host}/friends',headers =OOOOO00OO0000OOOO ).json ()#line:771
            if 'status'in O0000O00000O0OO00 :#line:772
                if O0000O00000O0OO00 ['status']==200 :#line:773
                    O00O0O0OOOO0O0O00 =O0000O00000O0OO00 ['data']['myInviteter']#line:774
                    if O00O0O0OOOO0O0O00 :#line:775
                        O0000O0OO0OO00O00 =O00O0O0OOOO0O0O00 ['user']['nickname']#line:776
                        OOOOO00OO0OOOO000 =O0O00O00O000O0O0O .certification ()#line:777
                        print (f'【查邀请人】:我的邀请人:{O0000O0OO0OO00O00}丨实名:{OOOOO00OO0OOOO000}')#line:778
                    else :#line:779
                        if O0O00O00O000O0O0O .innerId !='0':#line:780
                            O0O00O00O000O0O0O .invitation ()#line:781
        except Exception as O000O00O0000OO00O :#line:782
            print (O000O00O0000OO00O )#line:783
    def add_clover (OO000O0OOO00OO00O ):#line:786
        global golden_seed #line:787
        try :#line:788
            OO0O00OOOO0O000OO =f'__{timi_new()}'#line:789
            OOOOOOOOOOO0OO000 ={'source':'scsc','authorization':OO000O0OOO00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOOO0O000OO ),'signstring':OO0O00OOOO0O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:800
            O0OO00OOOO00O00OO =requests .request ('get',f'{host}/assets/clovers',headers =OOOOOOOOOOO0OO000 ).json ()#line:801
            if 'status'in O0OO00OOOO00O00OO :#line:803
                if O0OO00OOOO00O00OO ['status']==200 :#line:804
                    O00O00000O00O000O =O0OO00OOOO00O00OO ['data']['clover']#line:805
                    O0O0OO00O0000OOO0 =O0OO00OOOO00O00OO ['data']['used_clover']#line:806
                    OO000O000O0O00O0O =float (O00O00000O00O000O )-float (O0O0OO00O0000OOO0 )#line:807
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0O0OO00O0000OOO0}')#line:808
                    if OO000O0OOO00OO00O .certification ()!='未实名':#line:809
                        if OO000O000O0O00O0O >1 :#line:810
                            OO0O00OOOO0O000OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO000O000O0O00O0O)}_{timi_new()}'#line:811
                            OOO0000O0OOOOO00O ={'source':'scsc','authorization':OO000O0OOO00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOOO0O000OO ),'signstring':OO0O00OOOO0O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:822
                            OO0O0OO0OOO000000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO000O000O0O00O0O )}#line:823
                            OO0OO000O0O0OO00O =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO0000O0OOOOO00O ,data =OO0O0OO0OOO000000 ).json ()#line:824
                            if 'status'in OO0OO000O0O0OO00O :#line:826
                                if OO0OO000O0O0OO00O ['status']==200 :#line:827
                                    print (f'【参与抽奖】:添加☘️:{OO0OO000O0O0OO00O["data"]}丨数量:{OO000O000O0O00O0O}')#line:828
                                if OO0OO000O0O0OO00O ['status']==500 :#line:829
                                    print (f'【参与抽奖】:添加☘️:{OO0OO000O0O0OO00O["message"]}')#line:830
            OO00O0O0OOOOO0O0O =requests .request ('get',f'{host}/lottery',headers =OOOOOOOOOOO0OO000 ).json ()#line:831
            OOO0O0000O0OOO00O =OO000O0OOO00OO00O .winning_rewards ()#line:833
            if 'status'in OO00O0O0OOOOO0O0O :#line:834
                if OO00O0O0OOOOO0O0O ['status']==200 :#line:835
                    OO0O0O0O00OOO0O0O =OO00O0O0OOOOO0O0O ['data'][0 ]['day_get_gold_quantity']#line:836
                    golden_seed +=float (OO0O0O0O00OOO0O0O )#line:837
                    O0O000OO00OOOO000 =OO00O0O0OOOOO0O0O ['data'][1 ]['value']#line:838
                    OO00OOO0OO00O0OO0 =OO00O0O0OOOOO0O0O ['data'][0 ]['join_number']#line:839
                    O00O0O0O000000OO0 =int (float (OO00O0O0OOOOO0O0O ['data'][0 ]['totalValue']))#line:840
                    OO000OOO0000OOO0O =float (O0O000OO00OOOO000 /O00O0O0O000000OO0 )*10000 #line:841
                    O0O00O00OO0O000O0 =O00O0O0O000000OO0 /OO00OOO0OO00O0OO0 #line:842
                    print (f'【参与抽奖】:预计每天中{str(OO0O0O0O00OOO0O0O)[:6]}颗金种子丨好友收益:{str(OOO0O0000O0OOO00O)[:6]}')#line:843
                    print (f'【抽奖统计】:每1万☘️中{str(OO000OOO0000OOO0O)[:6]}颗金种子丨☘️人均:{str(O0O00O00OO0O000O0)[:7]}️')#line:844
        except Exception as O0OOO0O000O00OO00 :#line:845
            print (O0OOO0O000O00OO00 )#line:846
    def energy (OO0OOOOO00O0O0OOO ):#line:850
        try :#line:851
            while True :#line:852
                OOOOOO0O0O00OO0O0 =f'__{timi_new()}'#line:853
                OO0OOOO000O00OOOO ={'source':'scsc','authorization':OO0OOOOO00O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O0O00OO0O0 ),'signstring':OOOOOO0O0O00OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:864
                OOOOO0OOO0OOO00O0 =requests .request ('get',f'{host}/energy/general',headers =OO0OOOO000O00OOOO ).json ()#line:865
                if 'status'in OOOOO0OOO0OOO00O0 :#line:867
                    if OOOOO0OOO0OOO00O0 ['status']==200 :#line:868
                        OO000OO0OO0OOOOO0 =OOOOO0OOO0OOO00O0 ['data']['ordinary_water']#line:869
                        O00OOOO0O000O0O00 =OOOOO0OOO0OOO00O0 ['data']['ordinary_fertilizer']#line:870
                        O0OOO0000OO0OO0O0 =OOOOO0OOO0OOO00O0 ['data']['videoStatus']#line:871
                        OO000OOO000O0O000 =OOOOO0OOO0OOO00O0 ['data']['waterVideoKey']#line:872
                        print (f'【我的营养】:肥料:{str(O00OOOO0O000O0O00).split(".")[0]}丨水滴:{str(OO000OO0OO0OOOOO0).split(".")[0]}')#line:873
                        if float (O00OOOO0O000O0O00 )<96 :#line:874
                            if O0OOO0000OO0OO0O0 :#line:875
                                time .sleep (random .randint (160 ,180 )/10 )#line:876
                                O0O00OO00O00O00O0 =99 -float (O00OOOO0O000O0O00 )#line:877
                                O0O00O000O000O00O ={"fertilizer":str (O0O00OO00O00O00O0 ).split ('.')[0 ]}#line:878
                                O0OOOO0O00000OOOO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0OOOO000O00OOOO ).json ()#line:879
                                if 'status'in O0OOOO0O00000OOOO :#line:881
                                    if O0OOOO0O00000OOOO ['status']==200 :#line:882
                                        print (f'【购买肥料】:看广告获取肥料:{O0OOOO0O00000OOOO["message"]}')#line:883
                                    if O0OOOO0O00000OOOO ['status']==500 :#line:884
                                        print (f'【购买肥料】:看广告获取肥料:{O0OOOO0O00000OOOO["message"]}')#line:885
                                        break #line:886
                            if energy :#line:887
                                if float (O00OOOO0O000O0O00 )<float (fertilizer_quantity ):#line:888
                                    OOOOO0OO000O0OO0O =f'_fertilizer=10_{timi_new()}'#line:889
                                    OOOOOOOO0O000OOOO ={'source':'scsc','authorization':OO0OOOOO00O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OO000O0OO0O ),'signstring':OOOOO0OO000O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:900
                                    O0OOO00OOOO00OOO0 ={"fertilizer":"10"}#line:901
                                    OOO00OOO000O0O0OO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOOOOOO0O000OOOO ,data =O0OOO00OOOO00OOO0 ).json ()#line:902
                                    if 'status'in OOO00OOO000O0O0OO :#line:904
                                        if OOO00OOO000O0O0OO ['status']==200 :#line:905
                                            print (f'【购买肥料】:购买肥料:{OOO00OOO000O0O0OO["message"]}丨数量:10')#line:906
                                        if OOO00OOO000O0O0OO ['status']==500 :#line:907
                                            print (f'【购买肥料】:购买肥料:{OOO00OOO000O0O0OO["message"]}丨数量:10')#line:908
                                            OO0OOO0OO00OOOOOO =f'__{timi_new()}'#line:909
                                            OOOO0OO0OOOO0O00O ={'source':'scsc','authorization':OO0OOOOO00O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0OO00OOOOOO ),'signstring':OO0OOO0OO00OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:920
                                            O000OOO00OOOO0O00 =requests .request ('get',f'{host}/user',headers =OOOO0OO0OOOO0O00O ).json ()#line:921
                                            if 'status'in O000OOO00OOOO0O00 :#line:922
                                                if O000OOO00OOOO0O00 ['status']==200 :#line:923
                                                    O00OO000O0OO0000O =O000OOO00OOOO0O00 ['data']['inner_id']#line:924
                                                    give_gold (O00OO000O0OO0000O )#line:925
                        if float (OO000OO0OO0OOOOO0 )<880 :#line:927
                            if OO000OOO000O0O000 :#line:928
                                time .sleep (random .randint (160 ,180 )/10 )#line:929
                                O0OO0OOO0O0O00OOO =999 -float (OO000OO0OO0OOOOO0 )#line:930
                                OO0OO0O0000O0O0O0 ={"water":str (O0OO0OOO0O0O00OOO ).split ('.')[0 ]}#line:931
                                O0O0000OO0OOO000O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0OOOO000O00OOOO ).json ()#line:932
                                if 'status'in O0O0000OO0OOO000O :#line:934
                                    if O0O0000OO0OOO000O ['status']==200 :#line:935
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0000OO0OOO000O["message"]}')#line:936
                                    if O0O0000OO0OOO000O ['status']==500 :#line:937
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0000OO0OOO000O["message"]}')#line:938
                                        break #line:939
                            if energy :#line:940
                                if float (OO000OO0OO0OOOOO0 )<float (wadverti_quantity ):#line:941
                                    OO0O000O0OOO0O000 =f'_water=100_{timi_new()}'#line:942
                                    OOOO0000OO000O00O ={'source':'scsc','authorization':OO0OOOOO00O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000O0OOO0O000 ),'signstring':OO0O000O0OOO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:953
                                    O0OO00OO000OOOOOO ={"water":"100"}#line:954
                                    OO0OOOOOOOOO00OO0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOO0000OO000O00O ,data =O0OO00OO000OOOOOO ).json ()#line:955
                                    if 'status'in OO0OOOOOOOOO00OO0 :#line:957
                                        if OO0OOOOOOOOO00OO0 ['status']==200 :#line:958
                                            print (f'【购买水滴】:购买水滴:{OO0OOOOOOOOO00OO0["message"]}丨数量:100')#line:959
                                        if OO0OOOOOOOOO00OO0 ['status']==500 :#line:960
                                            print (f'【购买水滴】:购买水滴:{OO0OOOOOOOOO00OO0["message"]}丨数量:100')#line:961
                        break #line:965
        except Exception as OO00OO00OOOO0OOOO :#line:967
            print (OO00OO00OOOO0OOOO )#line:968
def bundled_def ():#line:970
    OO0O00O0OO0000O00 =['5570536','7750212','7911652','7911680','7805624']#line:971
    return OO0O00O0OO0000O00 [random .randint (0 ,len (OO0O00O0OO0000O00 )-1 )]#line:972
def version_of_the_validation ():#line:976
    return str ((82 -56 )/10 )#line:977
def gitee_validation ():#line:980
    try :#line:981
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:982
    except :#line:983
        sys .exit (0 )#line:984
def update_the_validation ():#line:988
    try :#line:989
        OO00OOO0OO0OO00O0 =gitee_validation ()#line:990
        if version_of_the_validation ()<OO00OOO0OO0OO00O0 ['CityEarth']['edition']:#line:991
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00OOO0OO0OO00O0["CityEarth"]["edition"]}   ❌')#line:992
            print (f'更新内容=>>{OO00OOO0OO0OO00O0["CityEarth"]["content"]}   🎉')#line:993
        else :#line:994
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00OOO0OO0OO00O0["CityEarth"]["edition"]}   ✅')#line:995
            print (f'更新内容=>> {OO00OOO0OO0OO00O0["CityEarth"]["content"]}   🎉')#line:996
    except Exception as OO00000O0OOOO0O0O :#line:997
        print (OO00000O0OOOO0O0O )#line:998
def os_qinglong ():#line:1001
    if application in os .environ :#line:1002
        OO00O000OOO000000 =os .environ [application ].split ('\n')#line:1003
        if len (OO00O000OOO000000 )>0 :#line:1004
            return OO00O000OOO000000 #line:1005
        else :#line:1006
            print (f"{application}变量未启用")#line:1007
            print ('脚本退出')#line:1008
            sys .exit (1 )#line:1009
    else :#line:1010
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:1012
        return os_built ()#line:1013
def os_built ():#line:1016
    if token :#line:1017
        O0OO0O0O0000000O0 =token .split ('\n')#line:1018
        if len (O0OO0O0O0000000O0 )>0 :#line:1019
            return O0OO0O0O0000000O0 #line:1020
    else :#line:1021
        print (f"内置变量为空")#line:1022
        print ('脚本结束')#line:1023
        sys .exit (0 )#line:1024
if __name__ =='__main__':#line:1027
    start ()#line:1028
