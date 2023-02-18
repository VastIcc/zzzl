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
@ 版本  2.3
"""
application = 'ce_token'  # 变量名
token = ''
time_xx = random.randint(23, 28)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
version ='3.1.4195311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        OO00OOOOO0000OOO0 =os_qinglong ()#line:10
        print (f"==========共找到{len(OO00OOOOO0000OOO0)}个账号==========")#line:11
        for OO00O0O0O0O0OO0O0 in OO00OOOOO0000OOO0 :#line:12
            OO00OO0OO0OO0O00O =[]#line:13
            print (f"------------正在执行第{OO00OOOOO0000OOO0.index(OO00O0O0O0O0OO0O0) + 1}个账号------------")#line:14
            O00O0000OOO000000 =CityEarth (OO00O0O0O0O0OO0O0 ,OO00OO0OO0OO0O00O )#line:15
            def O000OO00O0000OO00 ():#line:17
                if O00O0000OOO000000 .base_info ():#line:19
                    O00O0000OOO000000 .sealing ()#line:21
                    O00O0000OOO000000 .invitenum ()#line:23
                    O00O0000OOO000000 .game_map ()#line:25
                    O00O0000OOO000000 .friends_invitation ()#line:27
                    O00O0000OOO000000 .add_clover ()#line:29
                    O00O0000OOO000000 .propsraffle ()#line:31
                    O00O0000OOO000000 .synthetic ()#line:33
                    O00O0000OOO000000 .crops_illustrated ()#line:35
                    O00O0000OOO000000 .give_gold ()#line:37
                    O00O0000OOO000000 .withdraw ()#line:39
                    O00O0000OOO000000 .energy ()#line:41
            OOO0OO0O0OOO0O00O =threading .Thread (target =O000OO00O0000OO00 )#line:42
            OOO0OO0O0OOO0O00O .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        O0O0OOOOOO0OO0000 =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O0OOOOOO0OO0000 +' ')#line:48
    except Exception as O0O0O000OO0OO0O00 :#line:49
        print (O0O0O000OO0OO0O00 )#line:50
def sign (OOO00O00O00OO0OOO ):#line:53
    O00OO0000OO0O00O0 =hashlib .md5 (OOO00O00O00OO0OOO .encode ()).hexdigest ()#line:54
    OO0O0O00O0O0OO00O ="scsc%^&*"+O00OO0000OO0O00O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    OOO0OOOOO0O000O0O =hashlib .md5 (OO0O0O00O0O0OO00O .encode ()).hexdigest ()#line:56
    return OOO0OOOOO0O000O0O #line:57
def format_msg ():#line:59
    OOOOOOOO0O0O000OO =""#line:60
    for O0OO0OOO00OOOOO0O in msg_list :#line:61
        OOOOOOOO0O0O000OO +=str (O0OO0OOO00OOOOO0O )+"\r\n"#line:62
    return OOOOOOOO0O0O000OO #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (O000O0OOO0O0O0OO0 ,OO00OOO0O00OOOOOO ,O0O00OOO0O00O00OO ):#line:71
        try :#line:72
            O000O0OOO0O0O0OO0 .msg =O0O00OOO0O00O00OO #line:73
            O000O0OOO0O0O0OO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            O000O0OOO0O0O0OO0 .token =OO00OOO0O00OOOOOO .split ('&')[0 ]#line:75
            O000O0OOO0O0O0OO0 .innerId =OO00OOO0O00OOOOOO .split ('&')[1 ]#line:76
            O000O0OOO0O0O0OO0 .doneeNo =OO00OOO0O00OOOOOO .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (OO00O000O00OO00O0 ):#line:82
        try :#line:83
            OO00O000O00OO00O0 .watched_ad ()#line:85
            O00OOOO0O0OOOOOO0 =f'__{timi_new()}'#line:86
            O0O0O000000OOOOOO ={'authorization':OO00O000O00OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0O0OOOOOO0 ),'signstring':O00OOOO0O0OOOOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            OOO0OO00000OO0OOO =requests .request ('get',f'{host}/user',headers =O0O0O000000OOOOOO ).json ()#line:96
            if 'status'in OOO0OO00000OO0OOO :#line:98
                if OOO0OO00000OO0OOO ['status']==200 :#line:99
                    O00O00OOO000000O0 =OOO0OO00000OO0OOO ['data']['nickname']#line:100
                    OOO0OOO0OO0OOO0OO =OOO0OO00000OO0OOO ['data']['inner_id']#line:101
                    O00OO00OO00O00O0O =OOO0OO00000OO0OOO ['data']['assets']['gold']#line:102
                    OOOOO0O0O00O0000O =OOO0OO00000OO0OOO ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{O00O00OOO000000O0[:5]}丨ID:{OOO0OOO0OO0OOO0OO}丨等级:{OOOOO0O0O00O0000O}丨金种子:{str(O00OO00OO00O00O0O).split(".")[0]}')#line:104
                if OOO0OO00000OO0OOO ['status']==401 :#line:105
                    print (OOO0OO00000OO0OOO ['message'])#line:106
                    OO00O000O00OO00O0 .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if OOO0OO00000OO0OOO ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as OO00OO0OO0OOOOO0O :#line:112
            print (OO00OO0OO0OOOOO0O )#line:113
    def sealing (OOOO00OO0O0000O00 ):#line:116
        try :#line:117
            O00OOO0000O0000O0 =f'__{timi_new()}'#line:118
            O00O0O00O00OO0O0O ={'authorization':OOOO00OO0O0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0000O0000O0 ),'signstring':O00OOO0000O0000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00O0O00O00OO0O0O )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =O00O0O00O00OO0O0O )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00O0O00O00OO0O0O )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00O0O00O00OO0O0O )#line:131
            requests .request ('get',f'{host}/user',headers =O00O0O00O00OO0O0O )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00O0O00O00OO0O0O )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00O0O00O00OO0O0O )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =O00O0O00O00OO0O0O )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =O00O0O00O00OO0O0O )#line:136
            requests .request ('get',f'{host}/assets',headers =O00O0O00O00OO0O0O )#line:137
        except Exception as OO0OOO000O000O00O :#line:138
            print (OO0OOO000O000O00O )#line:139
    def withdraw (O0O00O0O0OO0O0O0O ):#line:143
        OO0OOOOO0OO0000OO =f'__{timi_new()}'#line:144
        O00O0O00OO0OO000O ={'authorization':O0O00O0O0OO0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO0OO0000OO ),'signstring':OO0OOOOO0OO0000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        O00OOOOOOOO000O0O =requests .request ('get',f'{host}/assets',headers =O00O0O00OO0OO000O ).json ()#line:154
        if 'status'in O00OOOOOOOO000O0O :#line:156
            if O00OOOOOOOO000O0O ['status']==200 :#line:157
                O00O0O0OO0OOOOOOO =O00OOOOOOOO000O0O ['data']['cash']#line:158
                if float (O00O0O0OO0OOOOOOO )>20 :#line:159
                    OO0OOOOO0OO0000OO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    O00O0O00OO0OO000O ={'authorization':O0O00O0O0OO0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO0OO0000OO ),'signstring':OO0OOOOO0OO0000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    OO0OOO0O0O0O00000 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    O0OOOOO00OOOO0000 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00O0O00OO0OO000O ,data =OO0OOO0O0O0O00000 ).json ()#line:172
                    print (O0OOOOO00OOOO0000 )#line:173
    def invitenum (OOOOOOO00000O000O ):#line:176
        O0O0OO0000000O0OO =f'__{timi_new()}'#line:177
        OO00O0O000O00OO00 ={'authorization':OOOOOOO00000O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0000000O0OO ),'signstring':O0O0OO0000000O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O0O0OOOOOO00O0O00 =requests .request ('get',f'{host}/invite/invitenum',headers =OO00O0O000O00OO00 ).json ()#line:187
        if 'status'in O0O0OOOOOO00O0O00 :#line:189
            if O0O0OOOOOO00O0O00 ['status']==200 :#line:190
                OO000O0O0OOO0O0O0 =O0O0OOOOOO00O0O00 ['data']['invited_count']#line:191
                OOO0O0O0OOO00O000 =O0O0OOOOOO00O0O00 ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OO000O0O0OOO0O0O0}丨间邀好友:{OOO0O0O0OOO00O000}')#line:193
    def game_map (OO0OOOOO0OOOOO0OO ):#line:196
        try :#line:197
            O000O0O0OO0OOO000 =f'__{timi_new()}'#line:198
            OOOO0OOOO00OOOOOO ={'authorization':OO0OOOOO0OOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O0OO0OOO000 ),'signstring':O000O0O0OO0OOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            O0O00O0OO00OO00O0 =requests .request ('get',f'{host}/game/map',headers =OOOO0OOOO00OOOOOO ).json ()#line:208
            if 'status'in O0O00O0OO00OO00O0 :#line:210
                if O0O00O0OO00OO00O0 ['status']==200 :#line:211
                    for O00000OO0OOOO00O0 in O0O00O0OO00OO00O0 ['data']['list'][0 ]['crops']:#line:212
                        OOO0OOOOOOO0OO00O =O00000OO0OOOO00O0 ['level']#line:214
                        if OOO0OOOOOOO0OO00O ==41 :#line:215
                            O0O000OO0OO0OO0OO =O00000OO0OOOO00O0 ['crop_name']#line:216
                            OOOO0O0O00O0OO0O0 =O00000OO0OOOO00O0 ['count']#line:217
                            if OOOO0O0O00O0OO0O0 >0 :#line:218
                                print (f'【农业资产】:{O0O000OO0OO0OO0OO}丨数量:{OOOO0O0O00O0OO0O0}')#line:219
        except Exception as OOOOO0O00O0O0OOOO :#line:220
            print (OOOOO0O00O0O0OOOO )#line:221
    def give_gold (OO0OOOO000O0000OO ):#line:224
        try :#line:225
            O00OO000OO0OO000O =f'__{timi_new()}'#line:226
            OOOO0OOO000OO00O0 ={'authorization':OO0OOOO000O0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000OO0OO000O ),'signstring':O00OO000OO0OO000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            OOO000000O00OOOO0 =requests .request ('get',f'{host}/user',headers =OOOO0OOO000OO00O0 ).json ()#line:236
            if 'status'in OOO000000O00OOOO0 :#line:237
                if OOO000000O00OOOO0 ['status']==200 :#line:238
                    if float (OO0OOOO000O0000OO .doneeNo )!=0 :#line:239
                        OOOO00O0OOO0000OO =OOO000000O00OOOO0 ['data']['assets']['gold']#line:240
                        if float (OOOO00O0OOO0000OO )>float (OO0OOOO000O0000OO .innerId ):#line:241
                            OOOOO0OOO000OOOO0 =int (float (OOOO00O0OOO0000OO )/1.1 )#line:242
                            O00OO000OO0OO000O =f'_doneeNo={OO0OOOO000O0000OO.doneeNo}&quantity={OOOOO0OOO000OOOO0}_{timi_new()}'#line:243
                            OOOO0OOO000OO00O0 ={'authorization':OO0OOOO000O0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000OO0OO000O ),'signstring':O00OO000OO0OO000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            OO0O0OOO00OOO0OO0 ={"quantity":OOOOO0OOO000OOOO0 ,"doneeNo":OO0OOOO000O0000OO .doneeNo }#line:256
                            OO000O00O0O0O000O =requests .request ('post',f'{host}/finance/give-gold',headers =OOOO0OOO000OO00O0 ,data =OO0O0OOO00OOO0OO0 ).json ()#line:257
                            if 'status'in OO000O00O0O0O000O :#line:259
                                if OO000O00O0O0O000O ['status']==200 :#line:260
                                    if OO000O00O0O0O000O ['data']:#line:261
                                        print (f'【赠送种子】:赠送{OOOOO0OOO000OOOO0}种子给{OO0OOOO000O0000OO.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as O00O0O0OOO00OO0O0 :#line:265
            print (O00O0O0OOO00OO0O0 )#line:266
    def invitation (O000O0OO00OOO0000 ):#line:268
        try :#line:269
            _OO00000OO0O000O0O =float (bundled_def ())/4 #line:270
            O0O000000OO0OO00O =f'_innerId={int(_OO00000OO0O000O0O)}_{timi_new()}'#line:271
            O00O0O0O00O0OO0OO ={'authorization':O000O0OO00OOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000000OO0OO00O ),'signstring':O0O000000OO0OO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            OO000O00000OO00O0 ={"innerId":int (_OO00000OO0O000O0O )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00O0O0O00O0OO0OO ,data =OO000O00000OO00O0 )#line:282
        except Exception as OO0000O0O000OOOO0 :#line:283
            print (OO0000O0O000OOOO0 )#line:284
    def winning_rewards (O0OO0OO0O0OOO0OO0 ):#line:287
        try :#line:288
            OOOO0O0OOO0OOO000 =f'__{timi_new()}'#line:289
            O0O0000000O00O000 ={'authorization':O0OO0OO0O0OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0OOO0OOO000 ),'signstring':OOOO0O0OOO0OOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            OOO0OOOO000OO0OO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O0000000O00O000 ).json ()#line:299
            if 'status'in OOO0OOOO000OO0OO0 :#line:301
                if OOO0OOOO000OO0OO0 ['status']==200 :#line:302
                    if OOO0OOOO000OO0OO0 ['data']['amount']:#line:303
                        O000OOOO0OO00O00O =OOO0OOOO000OO0OO0 ['data']['amount']['gold']#line:304
                        return O000OOOO0OO00O00O #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as OOOOOOOOOOOOO0OOO :#line:308
            print (OOOOOOOOOOOOO0OOO )#line:309
    def certification (OOO0OO0000OO00OOO ):#line:312
        try :#line:313
            OOO00OO0O0O0O000O =f'__{timi_new()}'#line:314
            O0000O0OO000O0OO0 ={'authorization':OOO0OO0000OO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0O0O0O000O ),'signstring':OOO00OO0O0O0O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OO00O00OOO000O0OO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0000O0OO000O0OO0 ).json ()#line:324
            if 'status'in OO00O00OOO000O0OO :#line:326
                if OO00O00OOO000O0OO ['status']==200 :#line:327
                    if OO00O00OOO000O0OO ['data']['result']:#line:328
                        OOO0000OOO0O00O00 =OO00O00OOO000O0OO ['data']['nick_name']#line:329
                        return OOO0000OOO0O00O00 #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as O00O000OOO0O000OO :#line:333
            print (O00O000OOO0O000OO )#line:334
    def crops_illustrated (O00OOOOOOO0O0000O ):#line:337
        try :#line:338
            O000O00O0000O00O0 =f'__{timi_new()}'#line:339
            O0O0OO000O0O00OOO ={'authorization':O00OOOOOOO0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00O0000O00O0 ),'signstring':O000O00O0000O00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            OOO0000O0O000000O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O0OO000O0O00OOO ).json ()#line:349
            if 'status'in OOO0000O0O000000O :#line:351
                if OOO0000O0O000000O ['status']==200 :#line:352
                    O0OOO0O0OO0OO00O0 =OOO0000O0O000000O ['data'][0 ]['crops']#line:353
                    for OOOO0OOO0O0O0000O in O0OOO0O0OO0OO00O0 :#line:354
                        if OOOO0OOO0O0O0000O ['ill_clover_award']:#line:355
                            if float (OOOO0OOO0O0O0000O ['ill_clover_award'])>1 :#line:356
                                if OOOO0OOO0O0O0000O ['is_finish']:#line:357
                                    if not OOOO0OOO0O0O0000O ['is_getit']:#line:358
                                        if O00OOOOOOO0O0000O .certification ()!='未实名':#line:359
                                            O000O00O0000O00O0 =f'_award_level={OOOO0OOO0O0O0000O["level"]}_{timi_new()}'#line:360
                                            O0O0OO000O0O00OOO ={'authorization':O00OOOOOOO0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00O0000O00O0 ),'signstring':O000O00O0000O00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            OOOO000OO0OOO00O0 ={"award_level":OOOO0OOO0O0O0000O ['level']}#line:370
                                            OO0O000O00OOO00O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O0OO000O0O00OOO ,json =OOOO000OO0OOO00O0 ).json ()#line:372
                                            if 'status'in OO0O000O00OOO00O0 :#line:373
                                                if OO0O000O00OOO00O0 ['status']==200 :#line:374
                                                    OOO0OO0O0OO00OO00 =OO0O000O00OOO00O0 ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{OOOO0OOO0O0O0000O["crop_name"]}成就丨奖励{OOO0OO0O0OO00OO00}☘️')#line:377
                                                if OO0O000O00OOO00O0 ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{OO0O000O00OOO00O0["message"]}')#line:379
        except Exception as OO0O00OOO0OO00OO0 :#line:380
            print (OO0O00OOO0OO00OO0 )#line:381
    def watched_ad (OO0OO0O0OOO00OOO0 ):#line:384
        try :#line:385
            O00O0O0O00000O0OO =f'__{timi_new()}'#line:386
            OO0O0O0000O0O0O0O ={'authorization':OO0OO0O0OOO00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O00000O0OO ),'signstring':O00O0O0O00000O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            OOO0O0000OO0OOO0O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O0000O0O0O0O ).json ()#line:396
            if 'status'in OOO0O0000OO0OOO0O :#line:398
                if OOO0O0000OO0OOO0O ['status']==200 :#line:399
                    if 'offlineInfo'in OOO0O0000OO0OOO0O ['data']:#line:400
                        time .sleep (random .randint (5 ,8 ))#line:401
                        O0OO0OOOOOO0OO00O =OOO0O0000OO0OOO0O ['data']['offlineInfo']['off_minute']#line:402
                        OO00OOO000OOOO00O =float (OOO0O0000OO0OOO0O ['data']['silver'])/1000000000000 #line:403
                        time .sleep (1 )#line:404
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0O0O0000O0O0O0O ).json ()#line:405
                        time .sleep (2 )#line:406
                        O0OOOOO00O00O000O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O0000O0O0O0O ).json ()#line:407
                        if 'status'in O0OOOOO00O00O000O :#line:409
                            if O0OOOOO00O00O000O ['status']==200 :#line:410
                                OOO0OOO0O0000O00O =float (O0OOOOO00O00O000O ['data']['silver'])/1000000000000 #line:411
                                OOO0OO00OO0OOO0O0 =str (OOO0OOO0O0000O00O -OO00OOO000OOOO00O )[:6 ]#line:412
                                print (f'【离线奖励】:翻倍离线{O0OO0OOOOOO0OO00O}分钟奖励🌱数量:{OOO0OO00OO0OOO0O0}t粒')#line:413
        except Exception as O00O00OO00O00000O :#line:414
            print (O00O00OO00O00000O )#line:415
    def user_ad (O000O00OOOO00OO0O ):#line:418
        try :#line:419
            OO0OO0000000O0O0O =f'__{timi_new()}'#line:420
            O00OO0000O0O0O00O ={'authorization':O000O00OOOO00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0000000O0O0O ),'signstring':OO0OO0000000O0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:429
            OO000OOOO0O0000OO =requests .request ('get',f'{host}/user/ad',headers =O00OO0000O0O0O00O ).json ()#line:430
            if 'status'in OO000OOOO0O0000OO :#line:432
                if OO000OOOO0O0000OO ['status']==200 :#line:433
                    OO0O0O00OOOO0O0OO =OO000OOOO0O0000OO ['data']['max_time']#line:434
                    O0OO00000000O00OO =OO000OOOO0O0000OO ['data']['watch_time']#line:435
                    O0OO00OOO0O00000O =OO000OOOO0O0000OO ['data']['added_time']#line:436
                    print (f'【获取种子】:获取🌱剩余{O0OO00OOO0O00000O + OO0O0O00OOOO0O0OO - O0OO00000000O00OO}次丨好友提供:{O0OO00OOO0O00000O}次')#line:437
                    if O0OO00OOO0O00000O +OO0O0O00OOOO0O0OO -O0OO00000000O00OO >0 :#line:438
                        time .sleep (random .randint (16 ,19 ))#line:439
                        OO00OO0O0OO0O0O0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00OO0000O0O0O00O ).json ()#line:440
                        if 'status'in OO00OO0O0OO0O0O0O :#line:442
                            if OO00OO0O0OO0O0O0O ['status']==200 :#line:443
                                OO00O00O00O00O0O0 =float (OO00OO0O0OO0O0O0O ['data']['silver'])/1000000000000 #line:444
                                print (f'【获取种子】:获得🌱:{int(OO00O00O00O00O0O0)}t粒')#line:445
                                return True #line:446
                            if OO00OO0O0OO0O0O0O ['status']==500 :#line:447
                                OO0O000OOOOOOO0OO =OO00OO0O0OO0O0O0O ['message']#line:448
                                print (f'【获取种子】:{OO0O000OOOOOOO0OO}')#line:449
                                return False #line:450
        except Exception as O0OO00OOO0O0000OO :#line:451
            print (O0OO00OOO0O0000OO )#line:452
    def synthetic (O0OOO0000O000O0O0 ):#line:455
        global id ,g #line:456
        try :#line:457
            O0OO0O0OOO0O000O0 =O0OOO0000O000O0O0 .level_new ()#line:458
            O0OO0O0000OOO0O0O =random .randint (9 ,11 )#line:459
            OO0OOO0OOOOOOOO00 =f'_site=8&targetSite={O0OO0O0000OOO0O0O}_{timi_new()}'#line:460
            O0O000000O00OO0OO ={'accept':'application/json, text/plain, */*','authorization':O0OOO0000O000O0O0 .token ,'timestamp':timi_new (),'sign':sign (OO0OOO0OOOOOOOO00 ),'signstring':OO0OOO0OOOOOOOO00 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:475
            OOOOO0O00O0000OOO ={"site":int (8 ),"targetSite":int (O0OO0O0000OOO0O0O )}#line:476
            requests .request ('post',f'{host}/game/crops/move',headers =O0O000000O00OO0OO ,json =OOOOO0O00O0000OOO )#line:477
            while True :#line:478
                OOO0OOO0000OO00O0 =f'__{timi_new()}'#line:479
                OOO0OOOOO0O00OO0O ={'authorization':O0OOO0000O000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0000OO00O0 ),'signstring':OOO0OOO0000OO00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                O000O000OO0O00OO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OOOOO0O00OO0O ).json ()#line:489
                if 'status'in O000O000OO0O00OO0 :#line:491
                    if O000O000OO0O00OO0 ['status']==200 :#line:492
                        OOO0000OOOOO0000O =O000O000OO0O00OO0 ['data']['cropList']#line:493
                        OO0O0OO0OO0OO0O00 =O000O000OO0O00OO0 ['data']['gameCoreDataDBid']#line:494
                        OOO00OOO0O000O000 =float (O000O000OO0O00OO0 ['data']['silver'])/1000000000000 #line:495
                        OO0OO0O0000OO0O0O =0 #line:500
                        for O0O0OO0OOO0O00O00 in OOO0000OOOOO0000O :#line:501
                            if not O0O0OO0OOO0O00O00 :#line:502
                                OOOO00O0000OOOOOO =f'_crop_id={OO0O0OO0OO0OO0O00}&site={OO0OO0O0000OO0O0O}_{O0OOO0000O000O0O0.time}'#line:503
                                O0O0O0O0OO0O0O000 ={'authorization':O0OOO0000O000O0O0 .token ,'timestamp':O0OOO0000O000O0O0 .time ,'sign':sign (OOOO00O0000OOOOOO ),'signstring':OOOO00O0000OOOOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
                                OO000O00000000000 ={"site":OO0OO0O0000OO0O0O ,"crop_id":OO0O0OO0OO0OO0O00 }#line:513
                                OOO0O000000O00000 =requests .request ('post',f'{host}/game/crops/buy',headers =O0O0O0O0OO0O0O000 ,data =OO000O00000000000 ).json ()#line:514
                                time .sleep (random .randint (1 ,3 )/10 )#line:516
                                if 'status'in OOO0O000000O00000 :#line:517
                                    if OOO0O000000O00000 ['status']==200 :#line:518
                                        if OOO0O000000O00000 ['message']=='种子数量不足':#line:519
                                            O0OO0O0OOO0O000O0 =O0OOO0000O000O0O0 .level_new ()#line:520
                                            print (f'【种植合成】:{OOO0O000000O00000["message"]}')#line:521
                                            if not O0OOO0000O000O0O0 .user_ad ():#line:522
                                                return False #line:523
                                    if OOO0O000000O00000 ['status']==500 :#line:524
                                        print (f'【种植合成】:{OOO0O000000O00000["message"]}')#line:525
                                        return False #line:526
                            OO0OO0O0000OO0O0O +=1 #line:527
                        OO00O0O0O00OOO0OO =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OOOOO0O00OO0O ).json ()#line:528
                        O0OOOOOO000OOOOOO =OO00O0O0O00OOO0OO ['data']['cropList']#line:529
                        O0O00O0O000OOOO00 =False #line:530
                        for O0O0OO0OOO0O00O00 in range (12 ):#line:531
                            id =O0OOOOOO000OOOOOO [O0O0OO0OOO0O00O00 ]['level']#line:532
                            if float (O0OO0O0OOO0O000O0 )-float (id )>9 :#line:533
                                O00O0O0OOOOO0OO0O =f'_site={O0O0OO0OOO0O00O00}_{timi_new()}'#line:534
                                O0OO0O0OOOOOO00OO ={'accept':'application/json, text/plain, */*','authorization':O0OOO0000O000O0O0 .token ,'timestamp':timi_new (),'sign':sign (O00O0O0OOOOO0OO0O ),'signstring':O00O0O0OOOOO0OO0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:544
                                OO00O0OOO0OO00000 ={"site":O0O0OO0OOO0O00O00 }#line:545
                                O00OO0O00OO000O0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OO0O0OOOOOO00OO ,data =OO00O0OOO0OO00000 ).json ()#line:547
                                if 'status'in O00OO0O00OO000O0O :#line:548
                                    if O00OO0O00OO000O0O ['status']==200 :#line:549
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:550
                            if id !=0 :#line:551
                                for O0O0O0O0O000O0OOO in range (11 ):#line:552
                                    OOO000OOO0O00O0OO =O0O0O0O0O000O0OOO +1 #line:553
                                    g =O0OOOOOO000OOOOOO [OOO000OOO0O00O0OO ]['level']#line:554
                                    if id ==g :#line:555
                                        OOOO0OO0O0O00OOOO =O0O0O0O0O000O0OOO +2 #line:556
                                        if OOOO0OO0O0O00OOOO !=O0O0OO0OOO0O00O00 +1 :#line:557
                                            OOO0O00O000000O00 =O0O0OO0OOO0O00O00 +1 #line:558
                                            time .sleep (random .randint (1 ,3 )/10 )#line:560
                                            OO0OOO0OOOOOOOO00 =f'_site={OOO0O00O000000O00 - 1}&targetSite={OOOO0OO0O0O00OOOO - 1}_{timi_new()}'#line:561
                                            O0O000000O00OO0OO ={'accept':'application/json, text/plain, */*','authorization':O0OOO0000O000O0O0 .token ,'timestamp':timi_new (),'sign':sign (OO0OOO0OOOOOOOO00 ),'signstring':OO0OOO0OOOOOOOO00 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:576
                                            OO00O0O00O0O00O00 ={"site":int (OOO0O00O000000O00 -1 ),"targetSite":int (OOOO0OO0O0O00OOOO -1 )}#line:577
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0O000000O00OO0OO ,json =OO00O0O00O0O00O00 )#line:578
                                            print (f'【种植合成】:位置{OOO0O00O000000O00}和位置{OOOO0OO0O0O00OOOO}合出{int(id) + 1}级农作物')#line:579
                                            O0O00O0O000OOOO00 =True #line:580
                                    if O0O00O0O000OOOO00 :#line:581
                                        break #line:582
                                if O0O00O0O000OOOO00 :#line:583
                                    break #line:584
        except :#line:585
            O0OOO0000O000O0O0 .synthetic ()#line:586
    def level_new (OO0O0OOOO00OOO0O0 ):#line:589
        try :#line:590
            OOO000O0OOO0OO0O0 =f'__{timi_new()}'#line:591
            OOO00OO0OO00OO0OO ={'authorization':OO0O0OOOO00OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0OOO0OO0O0 ),'signstring':OOO000O0OOO0OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            OO000OO0OO0O0O000 =requests .request ('get',f'{host}/user',headers =OOO00OO0OO00OO0OO ).json ()#line:601
            if 'status'in OO000OO0OO0O0O000 :#line:602
                if OO000OO0OO0O0O000 ['status']==200 :#line:603
                    return float (OO000OO0OO0O0O000 ['data']['level'])#line:604
        except Exception as O00O0OO0O0O000O00 :#line:605
            print (O00O0OO0O0O000O00 )#line:606
    def propsraffle (OOO0OOO00OO000O00 ):#line:609
        try :#line:610
            while True :#line:611
                OOOO00OO0O00OO0O0 =f'__{timi_new()}'#line:612
                OO00O0OO00000OOOO ={'authorization':OOO0OOO00OO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO0O00OO0O0 ),'signstring':OOOO00OO0O00OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:621
                OO0OOOO0O00OOOO0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO00O0OO00000OOOO ).json ()#line:622
                if 'status'in OO0OOOO0O00OOOO0O :#line:624
                    if OO0OOOO0O00OOOO0O ['status']==200 :#line:625
                        OOO0OO00000000OO0 =OO0OOOO0O00OOOO0O ['data']['rows']#line:626
                        O0OOOO0OO00000OO0 =OO0OOOO0O00OOOO0O ['data']['vstate']#line:627
                        if OOO0OO00000000OO0 ==5 or OOO0OO00000000OO0 ==6 or OOO0OO00000000OO0 ==7 :#line:628
                            OOOO0OO0O000O000O =OO0OOOO0O00OOOO0O ['data']['silver']#line:629
                            print (f'【转盘抽奖】:获得种子:{OOOO0OO0O000O000O}')#line:630
                        if OOO0OO00000000OO0 ==1 or OOO0OO00000000OO0 ==2 or OOO0OO00000000OO0 ==3 :#line:631
                            OO00O0O00O0OO0000 =OO0OOOO0O00OOOO0O ['data']['clover']#line:632
                            print (f'【转盘抽奖】:获得三叶草:{OO00O0O00O0OO0000}')#line:633
                        if OOO0OO00000000OO0 ==4 or OOO0OO00000000OO0 ==8 :#line:634
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:635
                        if OOO0OO00000000OO0 =='抽奖次数已用完':#line:639
                            break #line:672
                time .sleep (random .randint (8 ,15 )/10 )#line:673
        except Exception as O0OO00OOO000000OO :#line:674
            print (O0OO00OOO000000OO )#line:675
    def friends_invitation (O000O000OO0OO00OO ):#line:678
        try :#line:679
            OO000OOOOO0OO0000 =f'__{timi_new()}'#line:680
            OO0O0OOO0OOO00000 ={'authorization':O000O000OO0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOOO0OO0000 ),'signstring':OO000OOOOO0OO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:689
            O0O00O0OO0OOO00OO =requests .request ('get',f'{host}/friends',headers =OO0O0OOO0OOO00000 ).json ()#line:690
            if 'status'in O0O00O0OO0OOO00OO :#line:691
                if O0O00O0OO0OOO00OO ['status']==200 :#line:692
                    O00O000OO00OOO0O0 =O0O00O0OO0OOO00OO ['data']['myInviteter']#line:693
                    if O00O000OO00OOO0O0 :#line:694
                        OO0OOOO0O0OOO0000 =O00O000OO00OOO0O0 ['user']['nickname']#line:695
                        OO0O00O0000O0OO00 =O000O000OO0OO00OO .certification ()#line:696
                        print (f'【查邀请人】:我的邀请人:{OO0OOOO0O0OOO0000}丨实名:{OO0O00O0000O0OO00}')#line:697
                    else :#line:698
                        if O000O000OO0OO00OO .innerId !='0':#line:699
                            O000O000OO0OO00OO .invitation ()#line:700
        except Exception as OO0O000O0OO0O00OO :#line:701
            print (OO0O000O0OO0O00OO )#line:702
    def add_clover (O0OO00000OOOOO000 ):#line:705
        global golden_seed #line:706
        try :#line:707
            O000O00O0OOOOO000 =f'__{timi_new()}'#line:708
            OOO00O0OOOO000OO0 ={'authorization':O0OO00000OOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00O0OOOOO000 ),'signstring':O000O00O0OOOOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:717
            OO000000000O00OOO =requests .request ('get',f'{host}/assets/clovers',headers =OOO00O0OOOO000OO0 ).json ()#line:718
            if 'status'in OO000000000O00OOO :#line:720
                if OO000000000O00OOO ['status']==200 :#line:721
                    OO000O00O000OOO00 =OO000000000O00OOO ['data']['clover']#line:722
                    OO00O0000OOO0O00O =OO000000000O00OOO ['data']['used_clover']#line:723
                    O00000OOO0OOO0OOO =float (OO000O00O000OOO00 )-float (OO00O0000OOO0O00O )#line:724
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO00O0000OOO0O00O}')#line:725
                    if O0OO00000OOOOO000 .certification ()!='未实名':#line:726
                        if O00000OOO0OOO0OOO >1 :#line:727
                            O000O00O0OOOOO000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00000OOO0OOO0OOO)}_{timi_new()}'#line:728
                            OOO00OOOOOO00O00O ={'authorization':O0OO00000OOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00O0OOOOO000 ),'signstring':O000O00O0OOOOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                            O0OO00OO00000O0O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00000OOO0OOO0OOO )}#line:738
                            O000OOO0O00OOOOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO00OOOOOO00O00O ,data =O0OO00OO00000O0O0 ).json ()#line:739
                            if 'status'in O000OOO0O00OOOOOO :#line:741
                                if O000OOO0O00OOOOOO ['status']==200 :#line:742
                                    print (f'【参与抽奖】:添加☘️:{O000OOO0O00OOOOOO["data"]}丨数量:{O00000OOO0OOO0OOO}')#line:743
                                if O000OOO0O00OOOOOO ['status']==500 :#line:744
                                    print (f'【参与抽奖】:添加☘️:{O000OOO0O00OOOOOO["message"]}')#line:745
            O000O000OO000O0O0 =requests .request ('get',f'{host}/lottery',headers =OOO00O0OOOO000OO0 ).json ()#line:746
            O0OOO0OO00OOOO0O0 =O0OO00000OOOOO000 .winning_rewards ()#line:748
            if 'status'in O000O000OO000O0O0 :#line:749
                if O000O000OO000O0O0 ['status']==200 :#line:750
                    O0O0OOO0OOO000OO0 =O000O000OO000O0O0 ['data'][0 ]['day_get_gold_quantity']#line:751
                    golden_seed +=float (O0O0OOO0OOO000OO0 )#line:752
                    OOO0OO0O0OO0O0OOO =O000O000OO000O0O0 ['data'][1 ]['value']#line:753
                    O00OO0OOO0O0OO0OO =O000O000OO000O0O0 ['data'][0 ]['join_number']#line:754
                    O0OOO0OO00OOOOOO0 =int (float (O000O000OO000O0O0 ['data'][0 ]['totalValue']))#line:755
                    O0OOO000000000OO0 =float (OOO0OO0O0OO0O0OOO /O0OOO0OO00OOOOOO0 )*10000 #line:756
                    O0O000O000O00OOOO =O0OOO0OO00OOOOOO0 /O00OO0OOO0O0OO0OO #line:757
                    print (f'【参与抽奖】:预计每天中{str(O0O0OOO0OOO000OO0)[:6]}颗金种子丨好友收益:{str(O0OOO0OO00OOOO0O0)[:6]}')#line:758
                    print (f'【抽奖统计】:每1万☘️中{str(O0OOO000000000OO0)[:6]}颗金种子丨☘️人均:{str(O0O000O000O00OOOO)[:7]}️')#line:759
        except Exception as O0O0OOO0O00O0000O :#line:760
            print (O0O0OOO0O00O0000O )#line:761
    def energy (OOOOOO00OO0OO000O ):#line:765
        try :#line:766
            while True :#line:767
                O00OOOO00O00O0000 =f'__{timi_new()}'#line:768
                O0OO00OO000O0O0OO ={'authorization':OOOOOO00OO0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO00O00O0000 ),'signstring':O00OOOO00O00O0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:777
                OO0O00OOOOO0OO000 =requests .request ('get',f'{host}/energy/general',headers =O0OO00OO000O0O0OO ).json ()#line:778
                if 'status'in OO0O00OOOOO0OO000 :#line:780
                    if OO0O00OOOOO0OO000 ['status']==200 :#line:781
                        O00O00OOO0O0O0OOO =OO0O00OOOOO0OO000 ['data']['ordinary_water']#line:782
                        OO0OOO0000O0O0OOO =OO0O00OOOOO0OO000 ['data']['ordinary_fertilizer']#line:783
                        print (f'【我的营养】:肥料:{str(OO0OOO0000O0O0OOO).split(".")[0]}丨水滴:{str(O00O00OOO0O0O0OOO).split(".")[0]}')#line:785
                        if float (OO0OOO0000O0O0OOO )<96 :#line:786
                            time .sleep (random .randint (160 ,180 )/10 )#line:787
                            O0OO000O0OO00000O =99 -float (OO0OOO0000O0O0OOO )#line:788
                            OOOOO0OOOO0O0OOO0 ={"fertilizer":str (O0OO000O0OO00000O ).split ('.')[0 ]}#line:789
                            OOO00OOO00O0O0OOO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0OO00OO000O0O0OO ).json ()#line:790
                            if 'status'in OOO00OOO00O0O0OOO :#line:792
                                if OOO00OOO00O0O0OOO ['status']==200 :#line:793
                                    print (f'【购买肥料】:看广告获取肥料:{OOO00OOO00O0O0OOO["message"]}')#line:794
                        if float (O00O00OOO0O0O0OOO )<880 :#line:795
                            time .sleep (random .randint (160 ,180 )/10 )#line:796
                            O00O0OOO0O0O00OOO =999 -float (O00O00OOO0O0O0OOO )#line:797
                            OO00000OO00OO0OO0 ={"water":str (O00O0OOO0O0O00OOO ).split ('.')[0 ]}#line:798
                            OO0O00OOOOOO00O0O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0OO00OO000O0O0OO ).json ()#line:799
                            if 'status'in OO0O00OOOOOO00O0O :#line:801
                                if OO0O00OOOOOO00O0O ['status']==200 :#line:802
                                    print (f'【购买水滴】:看广告获取水滴:{OO0O00OOOOOO00O0O["message"]}')#line:803
                        if float (OO0OOO0000O0O0OOO )>96 and float (O00O00OOO0O0O0OOO )>880 :#line:804
                            break #line:805
        except Exception as O0OO0000OOO000OO0 :#line:807
            print (O0OO0000OOO000OO0 )#line:808
def bundled_def ():#line:810
    O00OOO00O0O0000OO =['5570536','7750212','7911652','7911680','7805624']#line:811
    return O00OOO00O0O0000OO [random .randint (0 ,len (O00OOO00O0O0000OO )-1 )]#line:812
def version_of_the_validation ():#line:816
    return str ((79 -56 )/10 )#line:817
def gitee_validation ():#line:820
    try :#line:821
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:822
    except :#line:823
        sys .exit (0 )#line:824
def update_the_validation ():#line:828
    try :#line:829
        O0OOO00OOOOO0O000 =gitee_validation ()#line:830
        if version_of_the_validation ()<O0OOO00OOOOO0O000 ['CityEarth']['edition']:#line:831
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOO00OOOOO0O000["CityEarth"]["edition"]}   ❌')#line:832
            print (f'更新内容=>>{O0OOO00OOOOO0O000["CityEarth"]["content"]}   🎉')#line:833
        else :#line:834
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOO00OOOOO0O000["CityEarth"]["edition"]}   ✅')#line:835
            print (f'更新内容=>> {O0OOO00OOOOO0O000["CityEarth"]["content"]}   🎉')#line:836
    except Exception as O000OO00OOO00O0O0 :#line:837
        print (O000OO00OOO00O0O0 )#line:838
def os_qinglong ():#line:841
    if application in os .environ :#line:842
        O00O0OOO000OOO0OO =os .environ [application ].split ('\n')#line:843
        if len (O00O0OOO000OOO0OO )>0 :#line:844
            return O00O0OOO000OOO0OO #line:845
        else :#line:846
            print (f"{application}变量未启用")#line:847
            print ('脚本退出')#line:848
            sys .exit (1 )#line:849
    else :#line:850
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:852
        return os_built ()#line:853
def os_built ():#line:856
    if token :#line:857
        OO0O0OO0O0OOO0O00 =token .split ('\n')#line:858
        if len (OO0O0OO0O0OOO0O00 )>0 :#line:859
            return OO0O0OO0O0OOO0O00 #line:860
    else :#line:861
        print (f"内置变量为空")#line:862
        print ('脚本结束')#line:863
        sys .exit (0 )#line:864
if __name__ =='__main__':#line:867
    start ()#line:868
