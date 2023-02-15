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
        O000OOO00OOO00000 =os_qinglong ()#line:10
        print (f"==========共找到{len(O000OOO00OOO00000)}个账号==========")#line:11
        for OO00O00OOO0OO000O in O000OOO00OOO00000 :#line:12
            O0000O0OO00OO0O0O =[]#line:13
            print (f"------------正在执行第{O000OOO00OOO00000.index(OO00O00OOO0OO000O) + 1}个账号------------")#line:14
            OO00O00O0000O0OOO =CityEarth (OO00O00OOO0OO000O ,O0000O0OO00OO0O0O )#line:15
            def OOO0OOO000OOO0OOO ():#line:17
                if OO00O00O0000O0OOO .base_info ():#line:19
                    OO00O00O0000O0OOO .sealing ()#line:21
                    OO00O00O0000O0OOO .invitenum ()#line:23
                    OO00O00O0000O0OOO .game_map ()#line:25
                    OO00O00O0000O0OOO .friends_invitation ()#line:27
                    OO00O00O0000O0OOO .add_clover ()#line:29
                    OO00O00O0000O0OOO .propsraffle ()#line:31
                    OO00O00O0000O0OOO .synthetic ()#line:33
                    OO00O00O0000O0OOO .crops_illustrated ()#line:35
                    OO00O00O0000O0OOO .give_gold ()#line:37
                    OO00O00O0000O0OOO .withdraw ()#line:39
                    OO00O00O0000O0OOO .energy ()#line:41
            OO00OO0OOOOO0OO00 =threading .Thread (target =OOO0OOO000OOO0OOO )#line:42
            OO00OO0OOOOO0OO00 .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        O0O000OO0OOO0O0OO =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O000OO0OOO0O0OO +' ')#line:48
    except Exception as OOOOOO00OO0O0OO00 :#line:49
        print (OOOOOO00OO0O0OO00 )#line:50
def sign (OOOOO0OO0OO000OO0 ):#line:53
    O000OOO00000O0000 =hashlib .md5 (OOOOO0OO0OO000OO0 .encode ()).hexdigest ()#line:54
    OOOO0O0OO0000OOOO ="scsc%^&*"+O000OOO00000O0000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    OOOO00O000000O00O =hashlib .md5 (OOOO0O0OO0000OOOO .encode ()).hexdigest ()#line:56
    return OOOO00O000000O00O #line:57
def format_msg ():#line:59
    O00O0OO0O0OO0000O =""#line:60
    for OO0000O0O00O00000 in msg_list :#line:61
        O00O0OO0O0OO0000O +=str (OO0000O0O00O00000 )+"\r\n"#line:62
    return O00O0OO0O0OO0000O #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (O00OOO0OOOO0O00OO ,O0000000OOOO00OOO ,O00OO0OO0000OOOO0 ):#line:71
        try :#line:72
            O00OOO0OOOO0O00OO .msg =O00OO0OO0000OOOO0 #line:73
            O00OOO0OOOO0O00OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            O00OOO0OOOO0O00OO .token =O0000000OOOO00OOO .split ('&')[0 ]#line:75
            O00OOO0OOOO0O00OO .innerId =O0000000OOOO00OOO .split ('&')[1 ]#line:76
            O00OOO0OOOO0O00OO .doneeNo =O0000000OOOO00OOO .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (OOOO000O0OOO0O0O0 ):#line:82
        try :#line:83
            OOOO000O0OOO0O0O0 .watched_ad ()#line:85
            O0000O00O00OOO00O =f'__{timi_new()}'#line:86
            O0O0O000OO0O00000 ={'authorization':OOOO000O0OOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00O00OOO00O ),'signstring':O0000O00O00OOO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            OOOO0O0OO0OO00000 =requests .request ('get',f'{host}/user',headers =O0O0O000OO0O00000 ).json ()#line:96
            if 'status'in OOOO0O0OO0OO00000 :#line:98
                if OOOO0O0OO0OO00000 ['status']==200 :#line:99
                    OOOO00OOOO0O0OO00 =OOOO0O0OO0OO00000 ['data']['nickname']#line:100
                    OOO00OOO0O00O0000 =OOOO0O0OO0OO00000 ['data']['inner_id']#line:101
                    OOO00O00OO0O000O0 =OOOO0O0OO0OO00000 ['data']['assets']['gold']#line:102
                    OOO0O0OO0OOO0O0OO =OOOO0O0OO0OO00000 ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{OOOO00OOOO0O0OO00[:5]}丨ID:{OOO00OOO0O00O0000}丨等级:{OOO0O0OO0OOO0O0OO}丨金种子:{str(OOO00O00OO0O000O0).split(".")[0]}')#line:104
                if OOOO0O0OO0OO00000 ['status']==401 :#line:105
                    print (OOOO0O0OO0OO00000 ['message'])#line:106
                    OOOO000O0OOO0O0O0 .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if OOOO0O0OO0OO00000 ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as O000000000O0OO00O :#line:112
            print (O000000000O0OO00O )#line:113
    def sealing (OOOOO00000O0O0OO0 ):#line:116
        try :#line:117
            OOO00OO0O00OO0000 =f'__{timi_new()}'#line:118
            O0OOO0OO0OO0OO0O0 ={'authorization':OOOOO00000O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0O00OO0000 ),'signstring':OOO00OO0O00OO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OOO0OO0OO0OO0O0 )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =O0OOO0OO0OO0OO0O0 )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OOO0OO0OO0OO0O0 )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OOO0OO0OO0OO0O0 )#line:131
            requests .request ('get',f'{host}/user',headers =O0OOO0OO0OO0OO0O0 )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OOO0OO0OO0OO0O0 )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OOO0OO0OO0OO0O0 )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OOO0OO0OO0OO0O0 )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0OO0OO0OO0O0 )#line:136
            requests .request ('get',f'{host}/assets',headers =O0OOO0OO0OO0OO0O0 )#line:137
        except Exception as O00OO0O0O00OOO0O0 :#line:138
            print (O00OO0O0O00OOO0O0 )#line:139
    def withdraw (OOOOOO0OOOOO0O0O0 ):#line:143
        O0O0OO0OOO0O0O0OO =f'__{timi_new()}'#line:144
        OO0O0OO0O00OO000O ={'authorization':OOOOOO0OOOOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OOO0O0O0OO ),'signstring':O0O0OO0OOO0O0O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        O00000O0000O0O00O =requests .request ('get',f'{host}/assets',headers =OO0O0OO0O00OO000O ).json ()#line:154
        if 'status'in O00000O0000O0O00O :#line:156
            if O00000O0000O0O00O ['status']==200 :#line:157
                O0OO0O00O0OOOOO00 =O00000O0000O0O00O ['data']['cash']#line:158
                if float (O0OO0O00O0OOOOO00 )>20 :#line:159
                    O0O0OO0OOO0O0O0OO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    OO0O0OO0O00OO000O ={'authorization':OOOOOO0OOOOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OOO0O0O0OO ),'signstring':O0O0OO0OOO0O0O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    O000OO000O0O0O0O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    OOOO0000OOO0O0O0O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO0O0OO0O00OO000O ,data =O000OO000O0O0O0O0 ).json ()#line:172
                    print (OOOO0000OOO0O0O0O )#line:173
    def invitenum (O00OO0OO0OO0000OO ):#line:176
        OOOOOOO00O0O0O00O =f'__{timi_new()}'#line:177
        O00000O0OO0OOOO00 ={'authorization':O00OO0OO0OO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO00O0O0O00O ),'signstring':OOOOOOO00O0O0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O00OOO0O0OOO00OO0 =requests .request ('get',f'{host}/invite/invitenum',headers =O00000O0OO0OOOO00 ).json ()#line:187
        if 'status'in O00OOO0O0OOO00OO0 :#line:189
            if O00OOO0O0OOO00OO0 ['status']==200 :#line:190
                OO00O0O00O00OO0O0 =O00OOO0O0OOO00OO0 ['data']['invited_count']#line:191
                O0OOO000O0O0OOOOO =O00OOO0O0OOO00OO0 ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OO00O0O00O00OO0O0}丨间邀好友:{O0OOO000O0O0OOOOO}')#line:193
    def game_map (O0O0O000O0OO0O000 ):#line:196
        try :#line:197
            OOOO0O0000O000O0O =f'__{timi_new()}'#line:198
            O0O0O00OO000O000O ={'authorization':O0O0O000O0OO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0000O000O0O ),'signstring':OOOO0O0000O000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            OO00OO0OO0O0OO000 =requests .request ('get',f'{host}/game/map',headers =O0O0O00OO000O000O ).json ()#line:208
            if 'status'in OO00OO0OO0O0OO000 :#line:210
                if OO00OO0OO0O0OO000 ['status']==200 :#line:211
                    for OOO000O000OO0OOO0 in OO00OO0OO0O0OO000 ['data']['list'][0 ]['crops']:#line:212
                        OO0O0O0OOO0O0OOOO =OOO000O000OO0OOO0 ['level']#line:214
                        if OO0O0O0OOO0O0OOOO ==41 :#line:215
                            O00OO00OOOO00OO00 =OOO000O000OO0OOO0 ['crop_name']#line:216
                            OO0O00OOOOO0OOOOO =OOO000O000OO0OOO0 ['count']#line:217
                            if OO0O00OOOOO0OOOOO >0 :#line:218
                                print (f'【农业资产】:{O00OO00OOOO00OO00}丨数量:{OO0O00OOOOO0OOOOO}')#line:219
        except Exception as OOO000OOOOO0000OO :#line:220
            print (OOO000OOOOO0000OO )#line:221
    def give_gold (O00000O0O0O0O00O0 ):#line:224
        try :#line:225
            OO00OO0OO000O000O =f'__{timi_new()}'#line:226
            O0OOO0OO0O00000OO ={'authorization':O00000O0O0O0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OO000O000O ),'signstring':OO00OO0OO000O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            O0O0OO0O000OO000O =requests .request ('get',f'{host}/user',headers =O0OOO0OO0O00000OO ).json ()#line:236
            if 'status'in O0O0OO0O000OO000O :#line:237
                if O0O0OO0O000OO000O ['status']==200 :#line:238
                    if float (O00000O0O0O0O00O0 .doneeNo )!=0 :#line:239
                        OOOOOOOO0O0O00000 =O0O0OO0O000OO000O ['data']['assets']['gold']#line:240
                        if float (OOOOOOOO0O0O00000 )>float (O00000O0O0O0O00O0 .innerId ):#line:241
                            O0O0O0O0O0OO00000 =int (float (OOOOOOOO0O0O00000 )/1.1 )#line:242
                            OO00OO0OO000O000O =f'_doneeNo={O00000O0O0O0O00O0.doneeNo}&quantity={O0O0O0O0O0OO00000}_{timi_new()}'#line:243
                            O0OOO0OO0O00000OO ={'authorization':O00000O0O0O0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OO000O000O ),'signstring':OO00OO0OO000O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            OOO00OOO0OO0000O0 ={"quantity":O0O0O0O0O0OO00000 ,"doneeNo":O00000O0O0O0O00O0 .doneeNo }#line:256
                            OO00O0O000OO0O000 =requests .request ('post',f'{host}/finance/give-gold',headers =O0OOO0OO0O00000OO ,data =OOO00OOO0OO0000O0 ).json ()#line:257
                            if 'status'in OO00O0O000OO0O000 :#line:259
                                if OO00O0O000OO0O000 ['status']==200 :#line:260
                                    if OO00O0O000OO0O000 ['data']:#line:261
                                        print (f'【赠送种子】:赠送{O0O0O0O0O0OO00000}种子给{O00000O0O0O0O00O0.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as O0O0OOOO0OO0O00O0 :#line:265
            print (O0O0OOOO0OO0O00O0 )#line:266
    def invitation (O000OO0O0O0O0O00O ):#line:268
        try :#line:269
            _O0OOOO0OO0OOOO000 =float (bundled_def ())/4 #line:270
            OOOOOO0O0000000O0 =f'_innerId={int(_O0OOOO0OO0OOOO000)}_{timi_new()}'#line:271
            OOO000O000OOO0OO0 ={'authorization':O000OO0O0O0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O0000000O0 ),'signstring':OOOOOO0O0000000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            OOOO0O0000O0OO0OO ={"innerId":int (_O0OOOO0OO0OOOO000 )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO000O000OOO0OO0 ,data =OOOO0O0000O0OO0OO )#line:282
        except Exception as OOO0OO00OO0O00OO0 :#line:283
            print (OOO0OO00OO0O00OO0 )#line:284
    def winning_rewards (O0OOOOOO00OO00OO0 ):#line:287
        try :#line:288
            O00OO0O000O000OOO =f'__{timi_new()}'#line:289
            O0OOOOO00000OO000 ={'authorization':O0OOOOOO00OO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O000O000OOO ),'signstring':O00OO0O000O000OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            O000O00O000OO0O0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOOOO00000OO000 ).json ()#line:299
            if 'status'in O000O00O000OO0O0O :#line:301
                if O000O00O000OO0O0O ['status']==200 :#line:302
                    if O000O00O000OO0O0O ['data']['amount']:#line:303
                        O0O0O0000OO00000O =O000O00O000OO0O0O ['data']['amount']['gold']#line:304
                        return O0O0O0000OO00000O #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as O0O00O00OO0O000OO :#line:308
            print (O0O00O00OO0O000OO )#line:309
    def certification (O00000OO0OOOO0OO0 ):#line:312
        try :#line:313
            OOOO0O00O0OOO0OOO =f'__{timi_new()}'#line:314
            OO0O0O00OO00O00O0 ={'authorization':O00000OO0OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00O0OOO0OOO ),'signstring':OOOO0O00O0OOO0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            O0O0O0O00OOO000O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0O0O00OO00O00O0 ).json ()#line:324
            if 'status'in O0O0O0O00OOO000O0 :#line:326
                if O0O0O0O00OOO000O0 ['status']==200 :#line:327
                    if O0O0O0O00OOO000O0 ['data']['result']:#line:328
                        O0OO00OO0OOOO0OO0 =O0O0O0O00OOO000O0 ['data']['nick_name']#line:329
                        return O0OO00OO0OOOO0OO0 #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as O0OO00O0000OOOO00 :#line:333
            print (O0OO00O0000OOOO00 )#line:334
    def crops_illustrated (OO0O0OO00000O00OO ):#line:337
        try :#line:338
            O0O0OO0OO000OOOOO =f'__{timi_new()}'#line:339
            OOO0O0O00O0OO0OO0 ={'authorization':OO0O0OO00000O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OO000OOOOO ),'signstring':O0O0OO0OO000OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            OOO00O000O0OOOO0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO0O0O00O0OO0OO0 ).json ()#line:349
            if 'status'in OOO00O000O0OOOO0O :#line:351
                if OOO00O000O0OOOO0O ['status']==200 :#line:352
                    O00OO000O000000O0 =OOO00O000O0OOOO0O ['data'][0 ]['crops']#line:353
                    for OOOO0OOOO0O000O0O in O00OO000O000000O0 :#line:354
                        if OOOO0OOOO0O000O0O ['ill_clover_award']:#line:355
                            if float (OOOO0OOOO0O000O0O ['ill_clover_award'])>1 :#line:356
                                if OOOO0OOOO0O000O0O ['is_finish']:#line:357
                                    if not OOOO0OOOO0O000O0O ['is_getit']:#line:358
                                        if OO0O0OO00000O00OO .certification ()!='未实名':#line:359
                                            O0O0OO0OO000OOOOO =f'_award_level={OOOO0OOOO0O000O0O["level"]}_{timi_new()}'#line:360
                                            OOO0O0O00O0OO0OO0 ={'authorization':OO0O0OO00000O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OO000OOOOO ),'signstring':O0O0OO0OO000OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            O00000O0O0O000000 ={"award_level":OOOO0OOOO0O000O0O ['level']}#line:370
                                            OO00O0O0OOO00OOOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO0O0O00O0OO0OO0 ,json =O00000O0O0O000000 ).json ()#line:372
                                            if 'status'in OO00O0O0OOO00OOOO :#line:373
                                                if OO00O0O0OOO00OOOO ['status']==200 :#line:374
                                                    OO0OO00O0O00OOO00 =OO00O0O0OOO00OOOO ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{OOOO0OOOO0O000O0O["crop_name"]}成就丨奖励{OO0OO00O0O00OOO00}☘️')#line:377
                                                if OO00O0O0OOO00OOOO ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{OO00O0O0OOO00OOOO["message"]}')#line:379
        except Exception as OOO000OOOO00OOOOO :#line:380
            print (OOO000OOOO00OOOOO )#line:381
    def watched_ad (O00O0000O0O00O000 ):#line:384
        try :#line:385
            O00OO0OO0O00O0O0O =f'__{timi_new()}'#line:386
            OOO0OO0OO000OO0O0 ={'authorization':O00O0000O0O00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OO0O00O0O0O ),'signstring':O00OO0OO0O00O0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            O0O000O0OO0OO0000 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OO0OO000OO0O0 ).json ()#line:396
            if 'status'in O0O000O0OO0OO0000 :#line:398
                if O0O000O0OO0OO0000 ['status']==200 :#line:399
                    if 'offlineInfo'in O0O000O0OO0OO0000 ['data']:#line:400
                        OO0O0O0000OOOOOOO =O0O000O0OO0OO0000 ['data']['offlineInfo']['off_minute']#line:401
                        O00OO0OO0O00OOO0O =float (O0O000O0OO0OO0000 ['data']['silver'])/1000000000000 #line:402
                        time .sleep (1 )#line:403
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO0OO0OO000OO0O0 ).json ()#line:404
                        time .sleep (2 )#line:405
                        O0O0O0O0OOO0OO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OO0OO000OO0O0 ).json ()#line:406
                        if 'status'in O0O0O0O0OOO0OO0O0 :#line:408
                            if O0O0O0O0OOO0OO0O0 ['status']==200 :#line:409
                                O000OOO0O0O0OOOO0 =float (O0O0O0O0OOO0OO0O0 ['data']['silver'])/1000000000000 #line:410
                                O0O000OOO0000O000 =str (O000OOO0O0O0OOOO0 -O00OO0OO0O00OOO0O )[:6 ]#line:411
                                print (f'【离线奖励】:翻倍离线{OO0O0O0000OOOOOOO}分钟奖励🌱数量:{O0O000OOO0000O000}t粒')#line:412
        except Exception as O0O0O0O00O0O00O0O :#line:413
            print (O0O0O0O00O0O00O0O )#line:414
    def user_ad (O0OOOO0O000O0OOOO ):#line:417
        try :#line:418
            OOO00O0OO0OOOO00O =f'__{timi_new()}'#line:419
            O00OO0OOOO00OOO00 ={'authorization':O0OOOO0O000O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OO0OOOO00O ),'signstring':OOO00O0OO0OOOO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:428
            O0OO00000O0OOOOOO =requests .request ('get',f'{host}/user/ad',headers =O00OO0OOOO00OOO00 ).json ()#line:429
            if 'status'in O0OO00000O0OOOOOO :#line:431
                if O0OO00000O0OOOOOO ['status']==200 :#line:432
                    O0000OO0O0O0OO000 =O0OO00000O0OOOOOO ['data']['max_time']#line:433
                    OO00OO00OOOOO0O00 =O0OO00000O0OOOOOO ['data']['watch_time']#line:434
                    O0000OO0OO000OOOO =O0OO00000O0OOOOOO ['data']['added_time']#line:435
                    print (f'【获取种子】:获取🌱剩余{O0000OO0OO000OOOO + O0000OO0O0O0OO000 - OO00OO00OOOOO0O00}次丨好友提供:{O0000OO0OO000OOOO}次')#line:436
                    if O0000OO0OO000OOOO +O0000OO0O0O0OO000 -OO00OO00OOOOO0O00 >0 :#line:437
                        time .sleep (random .randint (16 ,19 ))#line:438
                        O00O0OOO00OOOO0O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00OO0OOOO00OOO00 ).json ()#line:439
                        if 'status'in O00O0OOO00OOOO0O0 :#line:441
                            if O00O0OOO00OOOO0O0 ['status']==200 :#line:442
                                OOOO0O00O00O0OOOO =float (O00O0OOO00OOOO0O0 ['data']['silver'])/1000000000000 #line:443
                                print (f'【获取种子】:获得🌱:{int(OOOO0O00O00O0OOOO)}t粒')#line:444
                                return True #line:445
                            if O00O0OOO00OOOO0O0 ['status']==500 :#line:446
                                OOO000OO00OO00O00 =O00O0OOO00OOOO0O0 ['message']#line:447
                                print (f'【获取种子】:{OOO000OO00OO00O00}')#line:448
                                return False #line:449
        except Exception as OO000O00O0OOO00OO :#line:450
            print (OO000O00O0OOO00OO )#line:451
    def synthetic (OOOO000O000OOOOOO ):#line:454
        global id ,g #line:455
        try :#line:456
            OO0OO00OO0OO0OOO0 =OOOO000O000OOOOOO .level_new ()#line:457
            OOOO00000OO0OOOO0 =random .randint (9 ,11 )#line:458
            O0O0O00OO0OO0OOO0 =f'_site=8&targetSite={OOOO00000OO0OOOO0}_{timi_new()}'#line:459
            OO0OO000OOO000O00 ={'accept':'application/json, text/plain, */*','authorization':OOOO000O000OOOOOO .token ,'timestamp':timi_new (),'sign':sign (O0O0O00OO0OO0OOO0 ),'signstring':O0O0O00OO0OO0OOO0 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:474
            OOOOO0OO0OO0OOO0O ={"site":int (8 ),"targetSite":int (OOOO00000OO0OOOO0 )}#line:475
            requests .request ('post',f'{host}/game/crops/move',headers =OO0OO000OOO000O00 ,json =OOOOO0OO0OO0OOO0O )#line:476
            while True :#line:477
                O0000O0O00OOOOOO0 =f'__{timi_new()}'#line:478
                OO00O0000OOO0OO0O ={'authorization':OOOO000O000OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0O00OOOOOO0 ),'signstring':O0000O0O00OOOOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:487
                OO000O0OO0OO00O0O =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0000OOO0OO0O ).json ()#line:488
                if 'status'in OO000O0OO0OO00O0O :#line:490
                    if OO000O0OO0OO00O0O ['status']==200 :#line:491
                        OOOOO00000O00O0O0 =OO000O0OO0OO00O0O ['data']['cropList']#line:492
                        O00O0OOO000O0O000 =OO000O0OO0OO00O0O ['data']['gameCoreDataDBid']#line:493
                        OO0O0OO0OO000000O =float (OO000O0OO0OO00O0O ['data']['silver'])/1000000000000 #line:494
                        if OO0O0OO0OO000000O <6750 :#line:495
                            print (f'【种植合成】:🌱不足6750t')#line:496
                            break #line:497
                        OO000O00OOO0000O0 =0 #line:498
                        for O0000O0O0O00OO000 in OOOOO00000O00O0O0 :#line:499
                            if not O0000O0O0O00OO000 :#line:500
                                OO00O000000O00OOO =f'_crop_id={O00O0OOO000O0O000}&site={OO000O00OOO0000O0}_{OOOO000O000OOOOOO.time}'#line:501
                                O00000O00O0000O00 ={'authorization':OOOO000O000OOOOOO .token ,'timestamp':OOOO000O000OOOOOO .time ,'sign':sign (OO00O000000O00OOO ),'signstring':OO00O000000O00OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:510
                                O0OO00O0000000OOO ={"site":OO000O00OOO0000O0 ,"crop_id":O00O0OOO000O0O000 }#line:511
                                O0O0O00000OO000OO =requests .request ('post',f'{host}/game/crops/buy',headers =O00000O00O0000O00 ,data =O0OO00O0000000OOO ).json ()#line:512
                                time .sleep (random .randint (1 ,3 )/10 )#line:514
                                if 'status'in O0O0O00000OO000OO :#line:515
                                    if O0O0O00000OO000OO ['status']==200 :#line:516
                                        if O0O0O00000OO000OO ['message']=='种子数量不足':#line:517
                                            OO0OO00OO0OO0OOO0 =OOOO000O000OOOOOO .level_new ()#line:518
                                            print (f'【种植合成】:{O0O0O00000OO000OO["message"]}')#line:519
                                            if not OOOO000O000OOOOOO .user_ad ():#line:520
                                                return False #line:521
                                    if O0O0O00000OO000OO ['status']==500 :#line:522
                                        print (f'【种植合成】:{O0O0O00000OO000OO["message"]}')#line:523
                                        return False #line:524
                            OO000O00OOO0000O0 +=1 #line:525
                        O00O0O0OO000O000O =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0000OOO0OO0O ).json ()#line:526
                        OOO000000O000O000 =O00O0O0OO000O000O ['data']['cropList']#line:527
                        O0000000O0O0000O0 =False #line:528
                        for O0000O0O0O00OO000 in range (12 ):#line:529
                            id =OOO000000O000O000 [O0000O0O0O00OO000 ]['level']#line:530
                            if float (OO0OO00OO0OO0OOO0 )-float (id )>9 :#line:531
                                O000OOO000OOOOO0O =f'_site={O0000O0O0O00OO000}_{timi_new()}'#line:532
                                O0000OOO0OO0O0000 ={'accept':'application/json, text/plain, */*','authorization':OOOO000O000OOOOOO .token ,'timestamp':timi_new (),'sign':sign (O000OOO000OOOOO0O ),'signstring':O000OOO000OOOOO0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:542
                                OOO0OOO000OOO0000 ={"site":O0000O0O0O00OO000 }#line:543
                                O0O0OOO0O0O00O000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0000OOO0OO0O0000 ,data =OOO0OOO000OOO0000 ).json ()#line:545
                                if 'status'in O0O0OOO0O0O00O000 :#line:546
                                    if O0O0OOO0O0O00O000 ['status']==200 :#line:547
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:548
                            if id !=0 :#line:549
                                for O000O0OOO0000O00O in range (11 ):#line:550
                                    OOOO0O0000O0O00OO =O000O0OOO0000O00O +1 #line:551
                                    g =OOO000000O000O000 [OOOO0O0000O0O00OO ]['level']#line:552
                                    if id ==g :#line:553
                                        OO0O0O0O000O0OO00 =O000O0OOO0000O00O +2 #line:554
                                        if OO0O0O0O000O0OO00 !=O0000O0O0O00OO000 +1 :#line:555
                                            OOO00OOO0OO0O0O0O =O0000O0O0O00OO000 +1 #line:556
                                            time .sleep (random .randint (1 ,3 )/10 )#line:558
                                            O0O0O00OO0OO0OOO0 =f'_site={OOO00OOO0OO0O0O0O - 1}&targetSite={OO0O0O0O000O0OO00 - 1}_{timi_new()}'#line:559
                                            OO0OO000OOO000O00 ={'accept':'application/json, text/plain, */*','authorization':OOOO000O000OOOOOO .token ,'timestamp':timi_new (),'sign':sign (O0O0O00OO0OO0OOO0 ),'signstring':O0O0O00OO0OO0OOO0 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:574
                                            O0OO00O0O00O00O00 ={"site":int (OOO00OOO0OO0O0O0O -1 ),"targetSite":int (OO0O0O0O000O0OO00 -1 )}#line:575
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0OO000OOO000O00 ,json =O0OO00O0O00O00O00 )#line:576
                                            print (f'【种植合成】:位置{OOO00OOO0OO0O0O0O}和位置{OO0O0O0O000O0OO00}合出{int(id) + 1}级农作物')#line:577
                                            O0000000O0O0000O0 =True #line:578
                                    if O0000000O0O0000O0 :#line:579
                                        break #line:580
                                if O0000000O0O0000O0 :#line:581
                                    break #line:582
        except :#line:583
            OOOO000O000OOOOOO .synthetic ()#line:584
    def level_new (O0O0OOOOO0OO0O0OO ):#line:587
        try :#line:588
            OOO0O0OO0000OO00O =f'__{timi_new()}'#line:589
            OOOOOO0O00000OO00 ={'authorization':O0O0OOOOO0OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO0000OO00O ),'signstring':OOO0O0OO0000OO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:598
            O0O0O0OO000OOOO00 =requests .request ('get',f'{host}/user',headers =OOOOOO0O00000OO00 ).json ()#line:599
            if 'status'in O0O0O0OO000OOOO00 :#line:600
                if O0O0O0OO000OOOO00 ['status']==200 :#line:601
                    return float (O0O0O0OO000OOOO00 ['data']['level'])#line:602
        except Exception as OOO00O00O0O00OO00 :#line:603
            print (OOO00O00O0O00OO00 )#line:604
    def propsraffle (OOO00O0OOOOOOOOOO ):#line:607
        try :#line:608
            while True :#line:609
                OOOOOO0O0O000OOO0 =f'__{timi_new()}'#line:610
                O0OO0000OO00OOOOO ={'authorization':OOO00O0OOOOOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O0O000OOO0 ),'signstring':OOOOOO0O0O000OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:619
                OOO0O0O0O000OO00O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OO0000OO00OOOOO ).json ()#line:620
                if 'status'in OOO0O0O0O000OO00O :#line:622
                    if OOO0O0O0O000OO00O ['status']==200 :#line:623
                        O00O00000O0OOO0O0 =OOO0O0O0O000OO00O ['data']['rows']#line:624
                        OO0O00OO0OO0OOOOO =OOO0O0O0O000OO00O ['data']['vstate']#line:625
                        if O00O00000O0OOO0O0 ==5 or O00O00000O0OOO0O0 ==6 or O00O00000O0OOO0O0 ==7 :#line:626
                            OOOOO000O0OO0O000 =OOO0O0O0O000OO00O ['data']['silver']#line:627
                            print (f'【转盘抽奖】:获得种子:{OOOOO000O0OO0O000}')#line:628
                        if O00O00000O0OOO0O0 ==1 or O00O00000O0OOO0O0 ==2 or O00O00000O0OOO0O0 ==3 :#line:629
                            O000OOO000O00O00O =OOO0O0O0O000OO00O ['data']['clover']#line:630
                            print (f'【转盘抽奖】:获得三叶草:{O000OOO000O00O00O}')#line:631
                        if O00O00000O0OOO0O0 ==4 or O00O00000O0OOO0O0 ==8 :#line:632
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:633
                        if O00O00000O0OOO0O0 =='抽奖次数已用完':#line:637
                            break #line:670
                time .sleep (random .randint (8 ,15 )/10 )#line:671
        except Exception as O0O000OO0OOOO00OO :#line:672
            print (O0O000OO0OOOO00OO )#line:673
    def friends_invitation (OOO0OOOO0OOO00OO0 ):#line:676
        try :#line:677
            O00OO0O0OOOOO00O0 =f'__{timi_new()}'#line:678
            OOO0OO00OOO000OO0 ={'authorization':OOO0OOOO0OOO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0OOOOO00O0 ),'signstring':O00OO0O0OOOOO00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:687
            O000O0OO0OO000000 =requests .request ('get',f'{host}/friends',headers =OOO0OO00OOO000OO0 ).json ()#line:688
            if 'status'in O000O0OO0OO000000 :#line:689
                if O000O0OO0OO000000 ['status']==200 :#line:690
                    O0OOOOOOO0OO0OOO0 =O000O0OO0OO000000 ['data']['myInviteter']#line:691
                    if O0OOOOOOO0OO0OOO0 :#line:692
                        OO00O00O0000O0O0O =O0OOOOOOO0OO0OOO0 ['user']['nickname']#line:693
                        OOOOO00OO0000OOO0 =OOO0OOOO0OOO00OO0 .certification ()#line:694
                        print (f'【查邀请人】:我的邀请人:{OO00O00O0000O0O0O}丨实名:{OOOOO00OO0000OOO0}')#line:695
                    else :#line:696
                        if OOO0OOOO0OOO00OO0 .innerId !='0':#line:697
                            OOO0OOOO0OOO00OO0 .invitation ()#line:698
        except Exception as O0OOOO0O000OOOO0O :#line:699
            print (O0OOOO0O000OOOO0O )#line:700
    def add_clover (O0000OO0OOO0O0OOO ):#line:703
        global golden_seed #line:704
        try :#line:705
            OOO00OO00OO00O0O0 =f'__{timi_new()}'#line:706
            O0OOOOO000OO0OOO0 ={'authorization':O0000OO0OOO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO00OO00O0O0 ),'signstring':OOO00OO00OO00O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:715
            O000000OO0O00000O =requests .request ('get',f'{host}/assets/clovers',headers =O0OOOOO000OO0OOO0 ).json ()#line:716
            if 'status'in O000000OO0O00000O :#line:718
                if O000000OO0O00000O ['status']==200 :#line:719
                    OO00OO00O0O000OOO =O000000OO0O00000O ['data']['clover']#line:720
                    OOO0000O0OOO0OO00 =O000000OO0O00000O ['data']['used_clover']#line:721
                    OOOO000OO0O00O0O0 =float (OO00OO00O0O000OOO )-float (OOO0000O0OOO0OO00 )#line:722
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOO0000O0OOO0OO00}')#line:723
                    if O0000OO0OOO0O0OOO .certification ()!='未实名':#line:724
                        if OOOO000OO0O00O0O0 >1 :#line:725
                            OOO00OO00OO00O0O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOO000OO0O00O0O0)}_{timi_new()}'#line:726
                            OOO0O00000OOOOO00 ={'authorization':O0000OO0OOO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO00OO00O0O0 ),'signstring':OOO00OO00OO00O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:735
                            OO0O0O000OOOOOO0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOO000OO0O00O0O0 )}#line:736
                            OOO0000OOO0OO000O =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO0O00000OOOOO00 ,data =OO0O0O000OOOOOO0O ).json ()#line:737
                            if 'status'in OOO0000OOO0OO000O :#line:739
                                if OOO0000OOO0OO000O ['status']==200 :#line:740
                                    print (f'【参与抽奖】:添加☘️:{OOO0000OOO0OO000O["data"]}丨数量:{OOOO000OO0O00O0O0}')#line:741
                                if OOO0000OOO0OO000O ['status']==500 :#line:742
                                    print (f'【参与抽奖】:添加☘️:{OOO0000OOO0OO000O["message"]}')#line:743
            O00O00O00O0OOO000 =requests .request ('get',f'{host}/lottery',headers =O0OOOOO000OO0OOO0 ).json ()#line:744
            O0O00O0O00OO00OOO =O0000OO0OOO0O0OOO .winning_rewards ()#line:746
            if 'status'in O00O00O00O0OOO000 :#line:747
                if O00O00O00O0OOO000 ['status']==200 :#line:748
                    O00OO00O0O000O00O =O00O00O00O0OOO000 ['data'][0 ]['day_get_gold_quantity']#line:749
                    golden_seed +=float (O00OO00O0O000O00O )#line:750
                    O0O00O0OOO0OOO000 =O00O00O00O0OOO000 ['data'][1 ]['value']#line:751
                    OO0OO000000O00OO0 =O00O00O00O0OOO000 ['data'][0 ]['join_number']#line:752
                    O0OOOOOOOO000OO00 =int (float (O00O00O00O0OOO000 ['data'][0 ]['totalValue']))#line:753
                    OOO000OOOOO0O000O =float (O0O00O0OOO0OOO000 /O0OOOOOOOO000OO00 )*10000 #line:754
                    O0OO00O0OOO000OO0 =O0OOOOOOOO000OO00 /OO0OO000000O00OO0 #line:755
                    print (f'【参与抽奖】:预计每天中{str(O00OO00O0O000O00O)[:6]}颗金种子丨好友收益:{str(O0O00O0O00OO00OOO)[:6]}')#line:756
                    print (f'【抽奖统计】:每1万☘️中{str(OOO000OOOOO0O000O)[:4]}颗金种子丨☘️人均:{str(O0OO00O0OOO000OO0)[:7]}️')#line:757
        except Exception as OO0OO0O000OOOO0OO :#line:758
            print (OO0OO0O000OOOO0OO )#line:759
    def energy (O00OO0OO00O0O0000 ):#line:763
        try :#line:764
            while True :#line:765
                OO0000O0O0O000O0O =f'__{timi_new()}'#line:766
                OOOOOO0OOOO0O00O0 ={'authorization':O00OO0OO00O0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O0O0O000O0O ),'signstring':OO0000O0O0O000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:775
                OOOO0OO000O00OO0O =requests .request ('get',f'{host}/energy/general',headers =OOOOOO0OOOO0O00O0 ).json ()#line:776
                if 'status'in OOOO0OO000O00OO0O :#line:778
                    if OOOO0OO000O00OO0O ['status']==200 :#line:779
                        OOOO0OO0OO0O00OOO =OOOO0OO000O00OO0O ['data']['ordinary_water']#line:780
                        OO0O00O00O00O0OOO =OOOO0OO000O00OO0O ['data']['ordinary_fertilizer']#line:781
                        print (f'【我的营养】:肥料:{str(OO0O00O00O00O0OOO).split(".")[0]}丨水滴:{str(OOOO0OO0OO0O00OOO).split(".")[0]}')#line:783
                        if float (OO0O00O00O00O0OOO )<96 :#line:784
                            time .sleep (random .randint (160 ,180 )/10 )#line:785
                            OO00OO00O00OO00O0 =99 -float (OO0O00O00O00O0OOO )#line:786
                            OOO000O0OOOO0O000 ={"fertilizer":str (OO00OO00O00OO00O0 ).split ('.')[0 ]}#line:787
                            O0OOO00O00OO0OO00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOOOO0OOOO0O00O0 ).json ()#line:788
                            if 'status'in O0OOO00O00OO0OO00 :#line:790
                                if O0OOO00O00OO0OO00 ['status']==200 :#line:791
                                    print (f'【购买肥料】:看广告获取肥料:{O0OOO00O00OO0OO00["message"]}')#line:792
                        if float (OOOO0OO0OO0O00OOO )<880 :#line:793
                            time .sleep (random .randint (160 ,180 )/10 )#line:794
                            OO0O0OOOO00O00O00 =999 -float (OOOO0OO0OO0O00OOO )#line:795
                            OO00000O0O0O0O0OO ={"water":str (OO0O0OOOO00O00O00 ).split ('.')[0 ]}#line:796
                            OO0OO000O0O0OO0OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOOOO0OOOO0O00O0 ).json ()#line:797
                            if 'status'in OO0OO000O0O0OO0OO :#line:799
                                if OO0OO000O0O0OO0OO ['status']==200 :#line:800
                                    print (f'【购买水滴】:看广告获取水滴:{OO0OO000O0O0OO0OO["message"]}')#line:801
                        if float (OO0O00O00O00O0OOO )>96 and float (OOOO0OO0OO0O00OOO )>880 :#line:802
                            break #line:803
        except Exception as O0O0O00OO000O0OO0 :#line:805
            print (O0O0O00OO000O0OO0 )#line:806
def bundled_def ():#line:808
    O00O00OOO0OOOO00O =['5570536','7750212','7911652','7911680','7805624']#line:809
    return O00O00OOO0OOOO00O [random .randint (0 ,len (O00O00OOO0OOOO00O )-1 )]#line:810
def version_of_the_validation ():#line:814
    return str ((78 -56 )/10 )#line:815
def gitee_validation ():#line:818
    try :#line:819
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:820
    except :#line:821
        sys .exit (0 )#line:822
def update_the_validation ():#line:826
    try :#line:827
        OO0O0OOO0OOOO0000 =gitee_validation ()#line:828
        if version_of_the_validation ()<OO0O0OOO0OOOO0000 ['CityEarth']['edition']:#line:829
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0OOO0OOOO0000["CityEarth"]["edition"]}   ❌')#line:830
            print (f'更新内容=>>{OO0O0OOO0OOOO0000["CityEarth"]["content"]}   🎉')#line:831
        else :#line:832
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0OOO0OOOO0000["CityEarth"]["edition"]}   ✅')#line:833
            print (f'更新内容=>> {OO0O0OOO0OOOO0000["CityEarth"]["content"]}   🎉')#line:834
    except Exception as O0000OO00OOO0O0OO :#line:835
        print (O0000OO00OOO0O0OO )#line:836
def os_qinglong ():#line:839
    if application in os .environ :#line:840
        OO0OOO000O0OO0O0O =os .environ [application ].split ('\n')#line:841
        if len (OO0OOO000O0OO0O0O )>0 :#line:842
            return OO0OOO000O0OO0O0O #line:843
        else :#line:844
            print (f"{application}变量未启用")#line:845
            print ('脚本退出')#line:846
            sys .exit (1 )#line:847
    else :#line:848
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:850
        return os_built ()#line:851
def os_built ():#line:854
    if token :#line:855
        OO000O0000O0000OO =token .split ('\n')#line:856
        if len (OO000O0000O0000OO )>0 :#line:857
            return OO000O0000O0000OO #line:858
    else :#line:859
        print (f"内置变量为空")#line:860
        print ('脚本结束')#line:861
        sys .exit (0 )#line:862
if __name__ =='__main__':#line:865
    start ()#line:866
