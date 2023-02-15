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
@ 版本  2.2
"""
application = 'ce_token'  # 变量名
token = ''
time_xx = random.randint(8, 12)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
version ='3.1.4195311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        OOOO00000000OOOOO =os_qinglong ()#line:10
        print (f"==========共找到{len(OOOO00000000OOOOO)}个账号==========")#line:11
        for OO0OO0O0O00O00OOO in OOOO00000000OOOOO :#line:12
            OO0OO0OO0OO00000O =[]#line:13
            print (f"------------正在执行第{OOOO00000000OOOOO.index(OO0OO0O0O00O00OOO) + 1}个账号------------")#line:14
            OOOOOOOOO0OO0O0OO =CityEarth (OO0OO0O0O00O00OOO ,OO0OO0OO0OO00000O )#line:15
            def O000OO000OO000OO0 ():#line:17
                if OOOOOOOOO0OO0O0OO .base_info ():#line:19
                    OOOOOOOOO0OO0O0OO .sealing ()#line:21
                    OOOOOOOOO0OO0O0OO .invitenum ()#line:23
                    OOOOOOOOO0OO0O0OO .game_map ()#line:25
                    OOOOOOOOO0OO0O0OO .friends_invitation ()#line:27
                    OOOOOOOOO0OO0O0OO .add_clover ()#line:29
                    OOOOOOOOO0OO0O0OO .propsraffle ()#line:31
                    OOOOOOOOO0OO0O0OO .synthetic ()#line:33
                    OOOOOOOOO0OO0O0OO .crops_illustrated ()#line:35
                    OOOOOOOOO0OO0O0OO .give_gold ()#line:37
                    OOOOOOOOO0OO0O0OO .withdraw ()#line:39
                    OOOOOOOOO0OO0O0OO .energy ()#line:41
            OO0O0O0OOOO00OOOO =threading .Thread (target =O000OO000OO000OO0 )#line:42
            OO0O0O0OOOO00OOOO .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        O00O0OO0OO0O0OO00 =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00O0OO0OO0O0OO00 +' ')#line:48
    except Exception as O0O0O000O0O0O0OO0 :#line:49
        print (O0O0O000O0O0O0OO0 )#line:50
def sign (O0OOO00000O0OOOOO ):#line:53
    OO0O0OO00OOOO0OO0 =hashlib .md5 (O0OOO00000O0OOOOO .encode ()).hexdigest ()#line:54
    OO00O00OOOO0OO000 ="scsc%^&*"+OO0O0OO00OOOO0OO0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    O00O0OO000000O0O0 =hashlib .md5 (OO00O00OOOO0OO000 .encode ()).hexdigest ()#line:56
    return O00O0OO000000O0O0 #line:57
def format_msg ():#line:59
    OO0O0OOOOO0OO000O =""#line:60
    for O000O0O0O0O0OO00O in msg_list :#line:61
        OO0O0OOOOO0OO000O +=str (O000O0O0O0O0OO00O )+"\r\n"#line:62
    return OO0O0OOOOO0OO000O #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (O00000000OOOOOOOO ,O000OO0O0OO00OO00 ,OOOOO000O0OOO000O ):#line:71
        try :#line:72
            O00000000OOOOOOOO .msg =OOOOO000O0OOO000O #line:73
            O00000000OOOOOOOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            O00000000OOOOOOOO .token =O000OO0O0OO00OO00 .split ('&')[0 ]#line:75
            O00000000OOOOOOOO .innerId =O000OO0O0OO00OO00 .split ('&')[1 ]#line:76
            O00000000OOOOOOOO .doneeNo =O000OO0O0OO00OO00 .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (OO000O00OO00O0OO0 ):#line:82
        try :#line:83
            OO000O00OO00O0OO0 .watched_ad ()#line:85
            OOOO0O00000000OOO =f'__{timi_new()}'#line:86
            OO000000000OO00O0 ={'authorization':OO000O00OO00O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00000000OOO ),'signstring':OOOO0O00000000OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            O000OO0000O00000O =requests .request ('get',f'{host}/user',headers =OO000000000OO00O0 ).json ()#line:96
            if 'status'in O000OO0000O00000O :#line:98
                if O000OO0000O00000O ['status']==200 :#line:99
                    O000O000O00O0OOOO =O000OO0000O00000O ['data']['nickname']#line:100
                    OOOO0OO0O0OO00OOO =O000OO0000O00000O ['data']['inner_id']#line:101
                    OOO00O000O00O0O0O =O000OO0000O00000O ['data']['assets']['gold']#line:102
                    OOOOOOO00O0O00000 =O000OO0000O00000O ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{O000O000O00O0OOOO[:5]}丨ID:{OOOO0OO0O0OO00OOO}丨等级:{OOOOOOO00O0O00000}丨金种子:{str(OOO00O000O00O0O0O).split(".")[0]}')#line:104
                if O000OO0000O00000O ['status']==401 :#line:105
                    print (O000OO0000O00000O ['message'])#line:106
                    OO000O00OO00O0OO0 .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if O000OO0000O00000O ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as O0O0OOO0OOO0OO000 :#line:112
            print (O0O0OOO0OOO0OO000 )#line:113
    def sealing (OO0O0OOO00OOOO0O0 ):#line:116
        try :#line:117
            O00OO00O0OO00OOOO =f'__{timi_new()}'#line:118
            O0OO0OOOOOO0OO0O0 ={'authorization':OO0O0OOO00OOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00O0OO00OOOO ),'signstring':O00OO00O0OO00OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OO0OOOOOO0OO0O0 )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =O0OO0OOOOOO0OO0O0 )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OO0OOOOOO0OO0O0 )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OO0OOOOOO0OO0O0 )#line:131
            requests .request ('get',f'{host}/user',headers =O0OO0OOOOOO0OO0O0 )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OO0OOOOOO0OO0O0 )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OO0OOOOOO0OO0O0 )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OO0OOOOOO0OO0O0 )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =O0OO0OOOOOO0OO0O0 )#line:136
            requests .request ('get',f'{host}/assets',headers =O0OO0OOOOOO0OO0O0 )#line:137
        except Exception as O000O00OO000OO00O :#line:138
            print (O000O00OO000OO00O )#line:139
    def withdraw (OO0O0O0OOOOOO0OOO ):#line:143
        OOOOO0OOO0000OOO0 =f'__{timi_new()}'#line:144
        OOOO00O000OOOO00O ={'authorization':OO0O0O0OOOOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOO0000OOO0 ),'signstring':OOOOO0OOO0000OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        OOOO00O000OOOOO00 =requests .request ('get',f'{host}/assets',headers =OOOO00O000OOOO00O ).json ()#line:154
        if 'status'in OOOO00O000OOOOO00 :#line:156
            if OOOO00O000OOOOO00 ['status']==200 :#line:157
                OO000O0OOOOOOO00O =OOOO00O000OOOOO00 ['data']['cash']#line:158
                if float (OO000O0OOOOOOO00O )>20 :#line:159
                    OOOOO0OOO0000OOO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    OOOO00O000OOOO00O ={'authorization':OO0O0O0OOOOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOO0000OOO0 ),'signstring':OOOOO0OOO0000OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    OO0O000OOOOO00O00 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    OO0OOO0O00OOO000O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOO00O000OOOO00O ,data =OO0O000OOOOO00O00 ).json ()#line:172
                    print (OO0OOO0O00OOO000O )#line:173
    def invitenum (O000O0OO0OOOOOO0O ):#line:176
        O0O0OOO0OO0O0OOOO =f'__{timi_new()}'#line:177
        OO000OOOO0OOOO0OO ={'authorization':O000O0OO0OOOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO0OO0O0OOOO ),'signstring':O0O0OOO0OO0O0OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        OOOOOOOOOO0OOOO0O =requests .request ('get',f'{host}/invite/invitenum',headers =OO000OOOO0OOOO0OO ).json ()#line:187
        if 'status'in OOOOOOOOOO0OOOO0O :#line:189
            if OOOOOOOOOO0OOOO0O ['status']==200 :#line:190
                OOOOO0OO00000OOO0 =OOOOOOOOOO0OOOO0O ['data']['invited_count']#line:191
                OO0O00OOOO0OO000O =OOOOOOOOOO0OOOO0O ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OOOOO0OO00000OOO0}丨间邀好友:{OO0O00OOOO0OO000O}')#line:193
    def game_map (OO00O0O0O00O0OO0O ):#line:196
        try :#line:197
            O0OOO0000O0OO00OO =f'__{timi_new()}'#line:198
            OO0000O00O00OO0OO ={'authorization':OO00O0O0O00O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000O0OO00OO ),'signstring':O0OOO0000O0OO00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            OOO0OO00O00O0OO0O =requests .request ('get',f'{host}/game/map',headers =OO0000O00O00OO0OO ).json ()#line:208
            if 'status'in OOO0OO00O00O0OO0O :#line:210
                if OOO0OO00O00O0OO0O ['status']==200 :#line:211
                    for OOO00O0000O0OOO00 in OOO0OO00O00O0OO0O ['data']['list'][0 ]['crops']:#line:212
                        OO0OO0O00OO0O0O00 =OOO00O0000O0OOO00 ['level']#line:214
                        if OO0OO0O00OO0O0O00 ==41 :#line:215
                            O0O0OOO0OO0OO00O0 =OOO00O0000O0OOO00 ['crop_name']#line:216
                            OOO0OOO0000OO0O00 =OOO00O0000O0OOO00 ['count']#line:217
                            if OOO0OOO0000OO0O00 >0 :#line:218
                                print (f'【农业资产】:{O0O0OOO0OO0OO00O0}丨数量:{OOO0OOO0000OO0O00}')#line:219
        except Exception as OOOOO00O0O00O0OOO :#line:220
            print (OOOOO00O0O00O0OOO )#line:221
    def give_gold (O000OO0O00OOOO0OO ):#line:224
        try :#line:225
            O000OO0O00OOOOOOO =f'__{timi_new()}'#line:226
            O00000O0OO0OOOO00 ={'authorization':O000OO0O00OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O00OOOOOOO ),'signstring':O000OO0O00OOOOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            O0OO000OO00OO0OOO =requests .request ('get',f'{host}/user',headers =O00000O0OO0OOOO00 ).json ()#line:236
            if 'status'in O0OO000OO00OO0OOO :#line:237
                if O0OO000OO00OO0OOO ['status']==200 :#line:238
                    if float (O000OO0O00OOOO0OO .doneeNo )!=0 :#line:239
                        O00O00O000OOOO0O0 =O0OO000OO00OO0OOO ['data']['assets']['gold']#line:240
                        if float (O00O00O000OOOO0O0 )>float (O000OO0O00OOOO0OO .innerId ):#line:241
                            OOOOO0O00OOOOOOOO =int (float (O00O00O000OOOO0O0 )/1.1 )#line:242
                            O000OO0O00OOOOOOO =f'_doneeNo={O000OO0O00OOOO0OO.doneeNo}&quantity={OOOOO0O00OOOOOOOO}_{timi_new()}'#line:243
                            O00000O0OO0OOOO00 ={'authorization':O000OO0O00OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O00OOOOOOO ),'signstring':O000OO0O00OOOOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            O0OO0OOOOOO0O0000 ={"quantity":OOOOO0O00OOOOOOOO ,"doneeNo":O000OO0O00OOOO0OO .doneeNo }#line:256
                            OOOOOO0O0O000000O =requests .request ('post',f'{host}/finance/give-gold',headers =O00000O0OO0OOOO00 ,data =O0OO0OOOOOO0O0000 ).json ()#line:257
                            if 'status'in OOOOOO0O0O000000O :#line:259
                                if OOOOOO0O0O000000O ['status']==200 :#line:260
                                    if OOOOOO0O0O000000O ['data']:#line:261
                                        print (f'【赠送种子】:赠送{OOOOO0O00OOOOOOOO}种子给{O000OO0O00OOOO0OO.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as O0OO000O00OOO000O :#line:265
            print (O0OO000O00OOO000O )#line:266
    def invitation (O0OO0000O00O000O0 ):#line:268
        try :#line:269
            _O0000000000O0000O =float (bundled_def ())/4 #line:270
            OO00OO00000OOOOO0 =f'_innerId={int(_O0000000000O0000O)}_{timi_new()}'#line:271
            O0O0OO0OOO0O0O0O0 ={'authorization':O0OO0000O00O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO00000OOOOO0 ),'signstring':OO00OO00000OOOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            OOO0O000O000O0000 ={"innerId":int (_O0000000000O0000O )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0O0OO0OOO0O0O0O0 ,data =OOO0O000O000O0000 )#line:282
        except Exception as OOOOO0O0OO0000OO0 :#line:283
            print (OOOOO0O0OO0000OO0 )#line:284
    def winning_rewards (O00OOOO0O0OO0O0OO ):#line:287
        try :#line:288
            O00O0O0OOOO00O0OO =f'__{timi_new()}'#line:289
            O0OO000OOO0OO0O00 ={'authorization':O00OOOO0O0OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0OOOO00O0OO ),'signstring':O00O0O0OOOO00O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            O0OO0OO0O0O0O00OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OO000OOO0OO0O00 ).json ()#line:299
            if 'status'in O0OO0OO0O0O0O00OO :#line:301
                if O0OO0OO0O0O0O00OO ['status']==200 :#line:302
                    if O0OO0OO0O0O0O00OO ['data']['amount']:#line:303
                        O000OOOOO0O0O00OO =O0OO0OO0O0O0O00OO ['data']['amount']['gold']#line:304
                        return O000OOOOO0O0O00OO #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as OO0OO0OOO000OOOO0 :#line:308
            print (OO0OO0OOO000OOOO0 )#line:309
    def certification (O0OOO0OO000OO00O0 ):#line:312
        try :#line:313
            O0OOOOO0O0000O00O =f'__{timi_new()}'#line:314
            O000OOOOO00OOOO0O ={'authorization':O0OOO0OO000OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0O0000O00O ),'signstring':O0OOOOO0O0000O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OOOO0OO000OO000O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O000OOOOO00OOOO0O ).json ()#line:324
            if 'status'in OOOO0OO000OO000O0 :#line:326
                if OOOO0OO000OO000O0 ['status']==200 :#line:327
                    if OOOO0OO000OO000O0 ['data']['result']:#line:328
                        OOO00000OOOOO0OO0 =OOOO0OO000OO000O0 ['data']['nick_name']#line:329
                        return OOO00000OOOOO0OO0 #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as OOO0O000O00O0OOOO :#line:333
            print (OOO0O000O00O0OOOO )#line:334
    def crops_illustrated (O0O0O0000OO00OO0O ):#line:337
        try :#line:338
            OO0000O00O00OOOOO =f'__{timi_new()}'#line:339
            OOOO00O0OOOOO0O00 ={'authorization':O0O0O0000OO00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O00O00OOOOO ),'signstring':OO0000O00O00OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            OOO0OOO00OOO00OO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOOO00O0OOOOO0O00 ).json ()#line:349
            if 'status'in OOO0OOO00OOO00OO0 :#line:351
                if OOO0OOO00OOO00OO0 ['status']==200 :#line:352
                    O00O0OOO00O0000OO =OOO0OOO00OOO00OO0 ['data'][0 ]['crops']#line:353
                    for O0O00000OOOOO0O00 in O00O0OOO00O0000OO :#line:354
                        if O0O00000OOOOO0O00 ['ill_clover_award']:#line:355
                            if float (O0O00000OOOOO0O00 ['ill_clover_award'])>1 :#line:356
                                if O0O00000OOOOO0O00 ['is_finish']:#line:357
                                    if not O0O00000OOOOO0O00 ['is_getit']:#line:358
                                        if O0O0O0000OO00OO0O .certification ()!='未实名':#line:359
                                            OO0000O00O00OOOOO =f'_award_level={O0O00000OOOOO0O00["level"]}_{timi_new()}'#line:360
                                            OOOO00O0OOOOO0O00 ={'authorization':O0O0O0000OO00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O00O00OOOOO ),'signstring':OO0000O00O00OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            O0O000000O0O0O000 ={"award_level":O0O00000OOOOO0O00 ['level']}#line:370
                                            O000O0000OO0O0OOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOOO00O0OOOOO0O00 ,json =O0O000000O0O0O000 ).json ()#line:372
                                            if 'status'in O000O0000OO0O0OOO :#line:373
                                                if O000O0000OO0O0OOO ['status']==200 :#line:374
                                                    OOO000O0OOO00O00O =O000O0000OO0O0OOO ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{O0O00000OOOOO0O00["crop_name"]}成就丨奖励{OOO000O0OOO00O00O}☘️')#line:377
                                                if O000O0000OO0O0OOO ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{O000O0000OO0O0OOO["message"]}')#line:379
        except Exception as OOOO00OO0O0O000OO :#line:380
            print (OOOO00OO0O0O000OO )#line:381
    def watched_ad (O0OOO00000OO00000 ):#line:384
        try :#line:385
            OOO000O00OOOO00OO =f'__{timi_new()}'#line:386
            OO0O0O00O000O000O ={'authorization':O0OOO00000OO00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O00OOOO00OO ),'signstring':OOO000O00OOOO00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            O00OOOO00O0O00OO0 =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O00O000O000O ).json ()#line:396
            if 'status'in O00OOOO00O0O00OO0 :#line:398
                if O00OOOO00O0O00OO0 ['status']==200 :#line:399
                    if 'offlineInfo'in O00OOOO00O0O00OO0 ['data']:#line:400
                        OO0O000O0O0OO00O0 =O00OOOO00O0O00OO0 ['data']['offlineInfo']['off_minute']#line:401
                        O0OOOOO00000000O0 =float (O00OOOO00O0O00OO0 ['data']['silver'])/1000000000000 #line:402
                        time .sleep (1 )#line:403
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0O0O00O000O000O ).json ()#line:404
                        time .sleep (2 )#line:405
                        OOO0O000O0O00OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O00O000O000O ).json ()#line:406
                        if 'status'in OOO0O000O0O00OOO0 :#line:408
                            if OOO0O000O0O00OOO0 ['status']==200 :#line:409
                                OO000OOOO000O0000 =float (OOO0O000O0O00OOO0 ['data']['silver'])/1000000000000 #line:410
                                O0OOO0O0O00OOO0O0 =str (OO000OOOO000O0000 -O0OOOOO00000000O0 )[:6 ]#line:411
                                print (f'【离线奖励】:翻倍离线{OO0O000O0O0OO00O0}分钟奖励🌱数量:{O0OOO0O0O00OOO0O0}t粒')#line:412
        except Exception as O000OOOO000O00O00 :#line:413
            print (O000OOOO000O00O00 )#line:414
    def user_ad (O00OO0000O0OO00O0 ):#line:417
        try :#line:418
            O0O0OOOO0O0O0OOO0 =f'__{timi_new()}'#line:419
            OOO0OOOO00000OOO0 ={'authorization':O00OO0000O0OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOO0O0O0OOO0 ),'signstring':O0O0OOOO0O0O0OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:428
            OO000OO0OO000OOOO =requests .request ('get',f'{host}/user/ad',headers =OOO0OOOO00000OOO0 ).json ()#line:429
            if 'status'in OO000OO0OO000OOOO :#line:431
                if OO000OO0OO000OOOO ['status']==200 :#line:432
                    O0000OOO0O0O0O0OO =OO000OO0OO000OOOO ['data']['max_time']#line:433
                    OO00OO00O000O0000 =OO000OO0OO000OOOO ['data']['watch_time']#line:434
                    OO0OO0OOO0OO00O00 =OO000OO0OO000OOOO ['data']['added_time']#line:435
                    print (f'【获取种子】:获取🌱剩余{OO0OO0OOO0OO00O00 + O0000OOO0O0O0O0OO - OO00OO00O000O0000}次丨好友提供:{OO0OO0OOO0OO00O00}次')#line:436
                    if OO0OO0OOO0OO00O00 +O0000OOO0O0O0O0OO -OO00OO00O000O0000 >0 :#line:437
                        time .sleep (random .randint (16 ,19 ))#line:438
                        OO00O00OO00O0O0O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO0OOOO00000OOO0 ).json ()#line:439
                        if 'status'in OO00O00OO00O0O0O0 :#line:441
                            if OO00O00OO00O0O0O0 ['status']==200 :#line:442
                                O0O0OO00O0OO000O0 =float (OO00O00OO00O0O0O0 ['data']['silver'])/1000000000000 #line:443
                                print (f'【获取种子】:获得🌱:{int(O0O0OO00O0OO000O0)}t粒')#line:444
                                return True #line:445
                            if OO00O00OO00O0O0O0 ['status']==500 :#line:446
                                O00OOO000O00OO00O =OO00O00OO00O0O0O0 ['message']#line:447
                                print (f'【获取种子】:{O00OOO000O00OO00O}')#line:448
                                return False #line:449
        except Exception as O00O0O0OOOOOOOOOO :#line:450
            print (O00O0O0OOOOOOOOOO )#line:451
    def synthetic (O0O0OO0OOOO0OOOOO ):#line:454
        global id ,g #line:455
        try :#line:456
            OO000OO0O000O0O00 =O0O0OO0OOOO0OOOOO .level_new ()#line:457
            OOOOO000OO0OO0O00 =random .randint (9 ,11 )#line:458
            OOO00OOO0000OO000 =f'_site=8&targetSite={OOOOO000OO0OO0O00}_{timi_new()}'#line:459
            O0OOOO00O0000OOO0 ={'accept':'application/json, text/plain, */*','authorization':O0O0OO0OOOO0OOOOO .token ,'timestamp':timi_new (),'sign':sign (OOO00OOO0000OO000 ),'signstring':OOO00OOO0000OO000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:474
            O0O0000000O0O0OOO ={"site":int (8 ),"targetSite":int (OOOOO000OO0OO0O00 )}#line:475
            requests .request ('post',f'{host}/game/crops/move',headers =O0OOOO00O0000OOO0 ,json =O0O0000000O0O0OOO )#line:476
            while True :#line:477
                OOO0OOO0OOOOO0O00 =f'__{timi_new()}'#line:478
                OO0000O0O0OOO0O0O ={'authorization':O0O0OO0OOOO0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OOOOO0O00 ),'signstring':OOO0OOO0OOOOO0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:487
                OOOO0000OO0OOO000 =requests .request ('get',f'{host}/game/getAllData',headers =OO0000O0O0OOO0O0O ).json ()#line:488
                if 'status'in OOOO0000OO0OOO000 :#line:490
                    if OOOO0000OO0OOO000 ['status']==200 :#line:491
                        OO0O00O0OO0O0OO00 =OOOO0000OO0OOO000 ['data']['cropList']#line:492
                        OO0000OO000OOOOOO =OOOO0000OO0OOO000 ['data']['gameCoreDataDBid']#line:493
                        OO0000O00O0O0OO0O =float (OOOO0000OO0OOO000 ['data']['silver'])/1000000000000 #line:494
                        if OO0000O00O0O0OO0O <6750 :#line:495
                            print (f'【种植合成】:🌱不足6750t')#line:496
                            break #line:497
                        O000OO0OOO0O0O0O0 =0 #line:498
                        for O000O0O000OO00O00 in OO0O00O0OO0O0OO00 :#line:499
                            if not O000O0O000OO00O00 :#line:500
                                O00000000O0000O00 =f'_crop_id={OO0000OO000OOOOOO}&site={O000OO0OOO0O0O0O0}_{O0O0OO0OOOO0OOOOO.time}'#line:501
                                O00O000O0O000O00O ={'authorization':O0O0OO0OOOO0OOOOO .token ,'timestamp':O0O0OO0OOOO0OOOOO .time ,'sign':sign (O00000000O0000O00 ),'signstring':O00000000O0000O00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:510
                                OO0OO0OOOOOOOOOOO ={"site":O000OO0OOO0O0O0O0 ,"crop_id":OO0000OO000OOOOOO }#line:511
                                O0OOO0OOO00O0OOOO =requests .request ('post',f'{host}/game/crops/buy',headers =O00O000O0O000O00O ,data =OO0OO0OOOOOOOOOOO ).json ()#line:512
                                time .sleep (random .randint (1 ,3 )/10 )#line:514
                                if 'status'in O0OOO0OOO00O0OOOO :#line:515
                                    if O0OOO0OOO00O0OOOO ['status']==200 :#line:516
                                        if O0OOO0OOO00O0OOOO ['message']=='种子数量不足':#line:517
                                            OO000OO0O000O0O00 =O0O0OO0OOOO0OOOOO .level_new ()#line:518
                                            print (f'【种植合成】:{O0OOO0OOO00O0OOOO["message"]}')#line:519
                                            if not O0O0OO0OOOO0OOOOO .user_ad ():#line:520
                                                return False #line:521
                                    if O0OOO0OOO00O0OOOO ['status']==500 :#line:522
                                        print (f'【种植合成】:{O0OOO0OOO00O0OOOO["message"]}')#line:523
                                        return False #line:524
                            O000OO0OOO0O0O0O0 +=1 #line:525
                        O00O00O0OO0O0O0OO =requests .request ('get',f'{host}/game/getAllData',headers =OO0000O0O0OOO0O0O ).json ()#line:526
                        O0O0OO0OOO0OOOOO0 =O00O00O0OO0O0O0OO ['data']['cropList']#line:527
                        O0O00000O0O0OO00O =False #line:528
                        for O000O0O000OO00O00 in range (12 ):#line:529
                            id =O0O0OO0OOO0OOOOO0 [O000O0O000OO00O00 ]['level']#line:530
                            if float (OO000OO0O000O0O00 )-float (id )>9 :#line:531
                                O0O0000000O000OOO =f'_site={O000O0O000OO00O00}_{timi_new()}'#line:532
                                O00OO0O0O0O0O0O0O ={'accept':'application/json, text/plain, */*','authorization':O0O0OO0OOOO0OOOOO .token ,'timestamp':timi_new (),'sign':sign (O0O0000000O000OOO ),'signstring':O0O0000000O000OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:542
                                O0O0O0O00OO00O000 ={"site":O000O0O000OO00O00 }#line:543
                                OOO00O0OOO0OOOO0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00OO0O0O0O0O0O0O ,data =O0O0O0O00OO00O000 ).json ()#line:545
                                if 'status'in OOO00O0OOO0OOOO0O :#line:546
                                    if OOO00O0OOO0OOOO0O ['status']==200 :#line:547
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:548
                            if id !=0 :#line:549
                                for O0OOO0OO00OO00O0O in range (11 ):#line:550
                                    O0OOO0O000OO000OO =O0OOO0OO00OO00O0O +1 #line:551
                                    g =O0O0OO0OOO0OOOOO0 [O0OOO0O000OO000OO ]['level']#line:552
                                    if id ==g :#line:553
                                        OO0O0000000000000 =O0OOO0OO00OO00O0O +2 #line:554
                                        if OO0O0000000000000 !=O000O0O000OO00O00 +1 :#line:555
                                            O0000OO0000O00O00 =O000O0O000OO00O00 +1 #line:556
                                            time .sleep (random .randint (1 ,3 )/10 )#line:558
                                            OOO00OOO0000OO000 =f'_site={O0000OO0000O00O00 - 1}&targetSite={OO0O0000000000000 - 1}_{timi_new()}'#line:559
                                            O0OOOO00O0000OOO0 ={'accept':'application/json, text/plain, */*','authorization':O0O0OO0OOOO0OOOOO .token ,'timestamp':timi_new (),'sign':sign (OOO00OOO0000OO000 ),'signstring':OOO00OOO0000OO000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:574
                                            OO00OOO000O00O0OO ={"site":int (O0000OO0000O00O00 -1 ),"targetSite":int (OO0O0000000000000 -1 )}#line:575
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0OOOO00O0000OOO0 ,json =OO00OOO000O00O0OO )#line:576
                                            print (f'【种植合成】:位置{O0000OO0000O00O00}和位置{OO0O0000000000000}合出{int(id) + 1}级农作物')#line:577
                                            O0O00000O0O0OO00O =True #line:578
                                    if O0O00000O0O0OO00O :#line:579
                                        break #line:580
                                if O0O00000O0O0OO00O :#line:581
                                    break #line:582
        except :#line:583
            O0O0OO0OOOO0OOOOO .synthetic ()#line:584
    def level_new (OOOOOO0000O0OO0OO ):#line:587
        try :#line:588
            OOOO0000O00O0000O =f'__{timi_new()}'#line:589
            O0O0O0000OO0O0000 ={'authorization':OOOOOO0000O0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000O00O0000O ),'signstring':OOOO0000O00O0000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:598
            O00OOO00OOO00O000 =requests .request ('get',f'{host}/user',headers =O0O0O0000OO0O0000 ).json ()#line:599
            if 'status'in O00OOO00OOO00O000 :#line:600
                if O00OOO00OOO00O000 ['status']==200 :#line:601
                    return float (O00OOO00OOO00O000 ['data']['level'])#line:602
        except Exception as O0O0O0O0O0OOOO0OO :#line:603
            print (O0O0O0O0O0OOOO0OO )#line:604
    def propsraffle (O0O00OOOO000000O0 ):#line:607
        try :#line:608
            while True :#line:609
                O0OO0OOO00O0O000O =f'__{timi_new()}'#line:610
                OO0O00O0000000OO0 ={'authorization':O0O00OOOO000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO00O0O000O ),'signstring':O0OO0OOO00O0O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:619
                OO0OOO0000O000OO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0O00O0000000OO0 ).json ()#line:620
                if 'status'in OO0OOO0000O000OO0 :#line:622
                    if OO0OOO0000O000OO0 ['status']==200 :#line:623
                        OOOOO0OO0OOOOOOOO =OO0OOO0000O000OO0 ['data']['rows']#line:624
                        OOO0000000O0O0OOO =OO0OOO0000O000OO0 ['data']['vstate']#line:625
                        if OOOOO0OO0OOOOOOOO ==5 or OOOOO0OO0OOOOOOOO ==6 or OOOOO0OO0OOOOOOOO ==7 :#line:626
                            O00OOOOO0OO00O0O0 =OO0OOO0000O000OO0 ['data']['silver']#line:627
                            print (f'【转盘抽奖】:获得种子:{O00OOOOO0OO00O0O0}')#line:628
                        if OOOOO0OO0OOOOOOOO ==1 or OOOOO0OO0OOOOOOOO ==2 or OOOOO0OO0OOOOOOOO ==3 :#line:629
                            OO0OOO000OO0O0O00 =OO0OOO0000O000OO0 ['data']['clover']#line:630
                            print (f'【转盘抽奖】:获得三叶草:{OO0OOO000OO0O0O00}')#line:631
                        if OOOOO0OO0OOOOOOOO ==4 or OOOOO0OO0OOOOOOOO ==8 :#line:632
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:633
                        if OOOOO0OO0OOOOOOOO =='抽奖次数已用完':#line:637
                            break #line:670
                time .sleep (random .randint (8 ,15 )/10 )#line:671
        except Exception as O00OOOOO00O0O000O :#line:672
            print (O00OOOOO00O0O000O )#line:673
    def friends_invitation (O000OOO0OOO00OOO0 ):#line:676
        try :#line:677
            O000000OO0O00O000 =f'__{timi_new()}'#line:678
            O0O00000000O0O0OO ={'authorization':O000OOO0OOO00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000OO0O00O000 ),'signstring':O000000OO0O00O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:687
            OOOOOO000O0OO000O =requests .request ('get',f'{host}/friends',headers =O0O00000000O0O0OO ).json ()#line:688
            if 'status'in OOOOOO000O0OO000O :#line:689
                if OOOOOO000O0OO000O ['status']==200 :#line:690
                    OOO00OO0O000OO000 =OOOOOO000O0OO000O ['data']['myInviteter']#line:691
                    if OOO00OO0O000OO000 :#line:692
                        O0O0OO0OOOOOOOOOO =OOO00OO0O000OO000 ['user']['nickname']#line:693
                        OO000000O0O0OOO00 =O000OOO0OOO00OOO0 .certification ()#line:694
                        print (f'【查邀请人】:我的邀请人:{O0O0OO0OOOOOOOOOO}丨实名:{OO000000O0O0OOO00}')#line:695
                    else :#line:696
                        if O000OOO0OOO00OOO0 .innerId !='0':#line:697
                            O000OOO0OOO00OOO0 .invitation ()#line:698
        except Exception as O000OO0OOO0O0OOO0 :#line:699
            print (O000OO0OOO0O0OOO0 )#line:700
    def add_clover (O000OOOO000O0O000 ):#line:703
        global golden_seed #line:704
        try :#line:705
            O00O0OOO0OOO000OO =f'__{timi_new()}'#line:706
            OOOOOO0O000000O00 ={'authorization':O000OOOO000O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO0OOO000OO ),'signstring':O00O0OOO0OOO000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:715
            OOOO000000000O000 =requests .request ('get',f'{host}/assets/clovers',headers =OOOOOO0O000000O00 ).json ()#line:716
            if 'status'in OOOO000000000O000 :#line:718
                if OOOO000000000O000 ['status']==200 :#line:719
                    O000O00O0O0OO00OO =OOOO000000000O000 ['data']['clover']#line:720
                    OO0OO000000O000OO =OOOO000000000O000 ['data']['used_clover']#line:721
                    O00O0000O000OO00O =float (O000O00O0O0OO00OO )-float (OO0OO000000O000OO )#line:722
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO0OO000000O000OO}')#line:723
                    if O000OOOO000O0O000 .certification ()!='未实名':#line:724
                        if O00O0000O000OO00O >1 :#line:725
                            O00O0OOO0OOO000OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00O0000O000OO00O)}_{timi_new()}'#line:726
                            O0OO00OO00OOOO0OO ={'authorization':O000OOOO000O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO0OOO000OO ),'signstring':O00O0OOO0OOO000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:735
                            O0O00O0OO0000O0O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00O0000O000OO00O )}#line:736
                            O000OOO000OO00OO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OO00OO00OOOO0OO ,data =O0O00O0OO0000O0O0 ).json ()#line:737
                            if 'status'in O000OOO000OO00OO0 :#line:739
                                if O000OOO000OO00OO0 ['status']==200 :#line:740
                                    print (f'【参与抽奖】:添加☘️:{O000OOO000OO00OO0["data"]}丨数量:{O00O0000O000OO00O}')#line:741
                                if O000OOO000OO00OO0 ['status']==500 :#line:742
                                    print (f'【参与抽奖】:添加☘️:{O000OOO000OO00OO0["message"]}')#line:743
            OOOO0O0O0000O0O0O =requests .request ('get',f'{host}/lottery',headers =OOOOOO0O000000O00 ).json ()#line:744
            OO0OOO000O0O0000O =O000OOOO000O0O000 .winning_rewards ()#line:746
            if 'status'in OOOO0O0O0000O0O0O :#line:747
                if OOOO0O0O0000O0O0O ['status']==200 :#line:748
                    O00O0O000000OOOOO =OOOO0O0O0000O0O0O ['data'][0 ]['day_get_gold_quantity']#line:749
                    golden_seed +=float (O00O0O000000OOOOO )#line:750
                    OOO0O0OO00OO0O00O =OOOO0O0O0000O0O0O ['data'][1 ]['value']#line:751
                    O0O0000OOOO0OOO00 =OOOO0O0O0000O0O0O ['data'][0 ]['join_number']#line:752
                    O000OO0OO0OOOO0OO =int (float (OOOO0O0O0000O0O0O ['data'][0 ]['totalValue']))#line:753
                    O0O000000000O00O0 =float (OOO0O0OO00OO0O00O /O000OO0OO0OOOO0OO )*10000 #line:754
                    O0O0OOOOOOO00000O =O000OO0OO0OOOO0OO /O0O0000OOOO0OOO00 #line:755
                    print (f'【参与抽奖】:预计每天中{str(O00O0O000000OOOOO)[:6]}颗金种子丨好友收益:{str(OO0OOO000O0O0000O)[:6]}')#line:756
                    print (f'【抽奖统计】:每1万☘️中{str(O0O000000000O00O0)[:4]}颗金种子丨☘️人均:{str(O0O0OOOOOOO00000O)[:7]}️')#line:757
        except Exception as OOO0OOOOO0OO0O0OO :#line:758
            print (OOO0OOOOO0OO0O0OO )#line:759
    def energy (OO000OO00OO0OOO0O ):#line:763
        try :#line:764
            while True :#line:765
                O000O0OO00OOO000O =f'__{timi_new()}'#line:766
                O00OOOOOOOO000O0O ={'authorization':OO000OO00OO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO00OOO000O ),'signstring':O000O0OO00OOO000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:775
                OO0OO00OO000OOO00 =requests .request ('get',f'{host}/energy/general',headers =O00OOOOOOOO000O0O ).json ()#line:776
                if 'status'in OO0OO00OO000OOO00 :#line:778
                    if OO0OO00OO000OOO00 ['status']==200 :#line:779
                        O0O00O0OO0000000O =OO0OO00OO000OOO00 ['data']['ordinary_water']#line:780
                        O0O000OOOO000O0OO =OO0OO00OO000OOO00 ['data']['ordinary_fertilizer']#line:781
                        print (f'【我的营养】:肥料:{str(O0O000OOOO000O0OO).split(".")[0]}丨水滴:{str(O0O00O0OO0000000O).split(".")[0]}')#line:783
                        if float (O0O000OOOO000O0OO )<96 :#line:784
                            time .sleep (random .randint (160 ,180 )/10 )#line:785
                            OO0O0OOOO0000OO00 =99 -float (O0O000OOOO000O0OO )#line:786
                            O0O0OO000OO0O0OO0 ={"fertilizer":str (OO0O0OOOO0000OO00 ).split ('.')[0 ]}#line:787
                            O00O00O0OOOOOO0OO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00OOOOOOOO000O0O ).json ()#line:788
                            if 'status'in O00O00O0OOOOOO0OO :#line:790
                                if O00O00O0OOOOOO0OO ['status']==200 :#line:791
                                    print (f'【购买肥料】:看广告获取肥料:{O00O00O0OOOOOO0OO["message"]}')#line:792
                        if float (O0O00O0OO0000000O )<880 :#line:793
                            time .sleep (random .randint (160 ,180 )/10 )#line:794
                            O00O00OO000OO000O =999 -float (O0O00O0OO0000000O )#line:795
                            OO00OO0O00O0O000O ={"water":str (O00O00OO000OO000O ).split ('.')[0 ]}#line:796
                            OO00OOO0OO0OOOOOO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00OOOOOOOO000O0O ).json ()#line:797
                            if 'status'in OO00OOO0OO0OOOOOO :#line:799
                                if OO00OOO0OO0OOOOOO ['status']==200 :#line:800
                                    print (f'【购买水滴】:看广告获取水滴:{OO00OOO0OO0OOOOOO["message"]}')#line:801
                        if float (O0O000OOOO000O0OO )>96 and float (O0O00O0OO0000000O )>880 :#line:802
                            break #line:803
        except Exception as O0OO0OOO000O000O0 :#line:805
            print (O0OO0OOO000O000O0 )#line:806
def bundled_def ():#line:808
    OO0OOO0OOO00000O0 =['5570536','7750212','7911652','7911680','7805624']#line:809
    return OO0OOO0OOO00000O0 [random .randint (0 ,len (OO0OOO0OOO00000O0 )-1 )]#line:810
def version_of_the_validation ():#line:814
    return str ((78 -56 )/10 )#line:815
def gitee_validation ():#line:818
    try :#line:819
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:820
    except :#line:821
        sys .exit (0 )#line:822
def update_the_validation ():#line:826
    try :#line:827
        OOOO0000O0O0O00O0 =gitee_validation ()#line:828
        if version_of_the_validation ()<OOOO0000O0O0O00O0 ['CityEarth']['edition']:#line:829
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO0000O0O0O00O0["CityEarth"]["edition"]}   ❌')#line:830
            print (f'更新内容=>>{OOOO0000O0O0O00O0["CityEarth"]["content"]}   👍')#line:831
        else :#line:832
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO0000O0O0O00O0["CityEarth"]["edition"]}   ✅')#line:833
            print (f'更新内容=>> {OOOO0000O0O0O00O0["CityEarth"]["content"]}   👍')#line:834
    except Exception as O000OOO0O00OOO0O0 :#line:835
        print (O000OOO0O00OOO0O0 )#line:836
def os_qinglong ():#line:839
    if application in os .environ :#line:840
        O000OOOOOO0O0O000 =os .environ [application ].split ('\n')#line:841
        if len (O000OOOOOO0O0O000 )>0 :#line:842
            return O000OOOOOO0O0O000 #line:843
        else :#line:844
            print (f"{application}变量未启用")#line:845
            print ('脚本退出')#line:846
            sys .exit (1 )#line:847
    else :#line:848
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:850
        return os_built ()#line:851
def os_built ():#line:854
    if token :#line:855
        OOOOO0000OO0OOO0O =token .split ('\n')#line:856
        if len (OOOOO0000OO0OOO0O )>0 :#line:857
            return OOOOO0000OO0OOO0O #line:858
    else :#line:859
        print (f"内置变量为空")#line:860
        print ('脚本结束')#line:861
        sys .exit (0 )#line:862
if __name__ =='__main__':#line:865
    start ()#line:866
