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
        O00OOOOO000OOO000 =os_qinglong ()#line:10
        print (f"==========共找到{len(O00OOOOO000OOO000)}个账号==========")#line:11
        for OO0000O00OO0OOO00 in O00OOOOO000OOO000 :#line:12
            OO000O000OOO0000O =[]#line:13
            print (f"------------正在执行第{O00OOOOO000OOO000.index(OO0000O00OO0OOO00) + 1}个账号------------")#line:14
            OO0O0OO0OOOOO00O0 =CityEarth (OO0000O00OO0OOO00 ,OO000O000OOO0000O )#line:15
            def OOOO0O00OO0OO0OO0 ():#line:17
                if OO0O0OO0OOOOO00O0 .base_info ():#line:19
                    OO0O0OO0OOOOO00O0 .sealing ()#line:21
                    OO0O0OO0OOOOO00O0 .invitenum ()#line:23
                    OO0O0OO0OOOOO00O0 .game_map ()#line:25
                    OO0O0OO0OOOOO00O0 .friends_invitation ()#line:27
                    OO0O0OO0OOOOO00O0 .add_clover ()#line:29
                    OO0O0OO0OOOOO00O0 .propsraffle ()#line:31
                    OO0O0OO0OOOOO00O0 .synthetic ()#line:33
                    OO0O0OO0OOOOO00O0 .crops_illustrated ()#line:35
                    OO0O0OO0OOOOO00O0 .give_gold ()#line:37
                    OO0O0OO0OOOOO00O0 .withdraw ()#line:39
                    OO0O0OO0OOOOO00O0 .energy ()#line:41
            O00OO0O0OO00OO0O0 =threading .Thread (target =OOOO0O00OO0OO0OO0 )#line:42
            O00OO0O0OO00OO0O0 .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        O000O0O0OOOOOO0OO =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O000O0O0OOOOOO0OO +' ')#line:48
    except Exception as O000OOO0O00O0000O :#line:49
        print (O000OOO0O00O0000O )#line:50
def sign (OOOOOOO000O0OO0OO ):#line:53
    OO00O0O00OO0OO00O =hashlib .md5 (OOOOOOO000O0OO0OO .encode ()).hexdigest ()#line:54
    OOO0OO0OOOOOOOOOO ="scsc%^&*"+OO00O0O00OO0OO00O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    OOOO0OO000OOO0O0O =hashlib .md5 (OOO0OO0OOOOOOOOOO .encode ()).hexdigest ()#line:56
    return OOOO0OO000OOO0O0O #line:57
def format_msg ():#line:59
    O0O00O000O00O00O0 =""#line:60
    for OO000OO000OO0OO0O in msg_list :#line:61
        O0O00O000O00O00O0 +=str (OO000OO000OO0OO0O )+"\r\n"#line:62
    return O0O00O000O00O00O0 #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (OO0OOOO0000O00OO0 ,OOO0000OOO00OOO0O ,O0000OOO0OOOOO00O ):#line:71
        try :#line:72
            OO0OOOO0000O00OO0 .msg =O0000OOO0OOOOO00O #line:73
            OO0OOOO0000O00OO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            OO0OOOO0000O00OO0 .token =OOO0000OOO00OOO0O .split ('&')[0 ]#line:75
            OO0OOOO0000O00OO0 .innerId =OOO0000OOO00OOO0O .split ('&')[1 ]#line:76
            OO0OOOO0000O00OO0 .doneeNo =OOO0000OOO00OOO0O .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (O000000O0O00O0OOO ):#line:82
        try :#line:83
            O000000O0O00O0OOO .watched_ad ()#line:85
            O0OOO000O0O0OO0OO =f'__{timi_new()}'#line:86
            O000000O0OO000000 ={'authorization':O000000O0O00O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO000O0O0OO0OO ),'signstring':O0OOO000O0O0OO0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            OO00OO00O0O0OO00O =requests .request ('get',f'{host}/user',headers =O000000O0OO000000 ).json ()#line:96
            if 'status'in OO00OO00O0O0OO00O :#line:98
                if OO00OO00O0O0OO00O ['status']==200 :#line:99
                    OO0OO0000000OOOO0 =OO00OO00O0O0OO00O ['data']['nickname']#line:100
                    OO0OO00O0O0O0OOOO =OO00OO00O0O0OO00O ['data']['inner_id']#line:101
                    OOOOOOO0O0OO0O000 =OO00OO00O0O0OO00O ['data']['assets']['gold']#line:102
                    OO0O0OOOO0OO0OO00 =OO00OO00O0O0OO00O ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{OO0OO0000000OOOO0[:5]}丨ID:{OO0OO00O0O0O0OOOO}丨等级:{OO0O0OOOO0OO0OO00}丨金种子:{str(OOOOOOO0O0OO0O000).split(".")[0]}')#line:104
                if OO00OO00O0O0OO00O ['status']==401 :#line:105
                    print (OO00OO00O0O0OO00O ['message'])#line:106
                    O000000O0O00O0OOO .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if OO00OO00O0O0OO00O ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as OO000OO00OO00OOO0 :#line:112
            print (OO000OO00OO00OOO0 )#line:113
    def sealing (O00OO000O0O000OOO ):#line:116
        try :#line:117
            OO0O0O0OOOO0000O0 =f'__{timi_new()}'#line:118
            OO0OOO0000O0OO0OO ={'authorization':O00OO000O0O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OOOO0000O0 ),'signstring':OO0O0O0OOOO0000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0OOO0000O0OO0OO )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =OO0OOO0000O0OO0OO )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0OOO0000O0OO0OO )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0OOO0000O0OO0OO )#line:131
            requests .request ('get',f'{host}/user',headers =OO0OOO0000O0OO0OO )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0OOO0000O0OO0OO )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0OOO0000O0OO0OO )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0OOO0000O0OO0OO )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =OO0OOO0000O0OO0OO )#line:136
            requests .request ('get',f'{host}/assets',headers =OO0OOO0000O0OO0OO )#line:137
        except Exception as OOO0O00OO000O000O :#line:138
            print (OOO0O00OO000O000O )#line:139
    def withdraw (OOO00O0O0OO0O00OO ):#line:143
        OOOO0OO00000O0O00 =f'__{timi_new()}'#line:144
        OO00OOO0OOOO000OO ={'authorization':OOO00O0O0OO0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00000O0O00 ),'signstring':OOOO0OO00000O0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        O0O00OOO0O0O000OO =requests .request ('get',f'{host}/assets',headers =OO00OOO0OOOO000OO ).json ()#line:154
        if 'status'in O0O00OOO0O0O000OO :#line:156
            if O0O00OOO0O0O000OO ['status']==200 :#line:157
                O0OO0OO0OOOOOOO0O =O0O00OOO0O0O000OO ['data']['cash']#line:158
                if float (O0OO0OO0OOOOOOO0O )>20 :#line:159
                    OOOO0OO00000O0O00 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    OO00OOO0OOOO000OO ={'authorization':OOO00O0O0OO0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00000O0O00 ),'signstring':OOOO0OO00000O0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    O0000O00OOOOOO0O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    O0O0000OOO0O00OOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO00OOO0OOOO000OO ,data =O0000O00OOOOOO0O0 ).json ()#line:172
                    print (O0O0000OOO0O00OOO )#line:173
    def invitenum (OO00OO0O000OO0000 ):#line:176
        OO000000O0O000O0O =f'__{timi_new()}'#line:177
        OOOOO0OO0O00O00OO ={'authorization':OO00OO0O000OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000O0O000O0O ),'signstring':OO000000O0O000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O0OO00OOO0O000O0O =requests .request ('get',f'{host}/invite/invitenum',headers =OOOOO0OO0O00O00OO ).json ()#line:187
        if 'status'in O0OO00OOO0O000O0O :#line:189
            if O0OO00OOO0O000O0O ['status']==200 :#line:190
                OO0OOO0O00O000000 =O0OO00OOO0O000O0O ['data']['invited_count']#line:191
                O00O0OOOOO0000OOO =O0OO00OOO0O000O0O ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OO0OOO0O00O000000}丨间邀好友:{O00O0OOOOO0000OOO}')#line:193
    def game_map (O0OOOO0O0O0OOO0OO ):#line:196
        try :#line:197
            O00O000OOOOO00OOO =f'__{timi_new()}'#line:198
            OOOO0OOOOO0000000 ={'authorization':O0OOOO0O0O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OOOOO00OOO ),'signstring':O00O000OOOOO00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            O00O00OO0O00OO000 =requests .request ('get',f'{host}/game/map',headers =OOOO0OOOOO0000000 ).json ()#line:208
            if 'status'in O00O00OO0O00OO000 :#line:210
                if O00O00OO0O00OO000 ['status']==200 :#line:211
                    for O000000OOO0OOO0O0 in O00O00OO0O00OO000 ['data']['list'][0 ]['crops']:#line:212
                        O0OOO0O0O000000O0 =O000000OOO0OOO0O0 ['level']#line:214
                        if O0OOO0O0O000000O0 ==41 :#line:215
                            OOOO0OO00O0OOO000 =O000000OOO0OOO0O0 ['crop_name']#line:216
                            O0OOO000OOOO0O00O =O000000OOO0OOO0O0 ['count']#line:217
                            if O0OOO000OOOO0O00O >0 :#line:218
                                print (f'【农业资产】:{OOOO0OO00O0OOO000}丨数量:{O0OOO000OOOO0O00O}')#line:219
        except Exception as O0000OOOO00O00O00 :#line:220
            print (O0000OOOO00O00O00 )#line:221
    def give_gold (O00OOOOO0O0O0OO0O ):#line:224
        try :#line:225
            OO0OO000O00O0OOO0 =f'__{timi_new()}'#line:226
            OO00O0O0O0OO0O00O ={'authorization':O00OOOOO0O0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000O00O0OOO0 ),'signstring':OO0OO000O00O0OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            OOO0O00O0OOOO00O0 =requests .request ('get',f'{host}/user',headers =OO00O0O0O0OO0O00O ).json ()#line:236
            if 'status'in OOO0O00O0OOOO00O0 :#line:237
                if OOO0O00O0OOOO00O0 ['status']==200 :#line:238
                    if float (O00OOOOO0O0O0OO0O .doneeNo )!=0 :#line:239
                        O0OO0000OO00OOO0O =OOO0O00O0OOOO00O0 ['data']['assets']['gold']#line:240
                        if float (O0OO0000OO00OOO0O )>float (O00OOOOO0O0O0OO0O .innerId ):#line:241
                            OO0000000OOOOO000 =int (float (O0OO0000OO00OOO0O )/1.1 )#line:242
                            OO0OO000O00O0OOO0 =f'_doneeNo={O00OOOOO0O0O0OO0O.doneeNo}&quantity={OO0000000OOOOO000}_{timi_new()}'#line:243
                            OO00O0O0O0OO0O00O ={'authorization':O00OOOOO0O0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000O00O0OOO0 ),'signstring':OO0OO000O00O0OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            O00OO0OOO0O0000O0 ={"quantity":OO0000000OOOOO000 ,"doneeNo":O00OOOOO0O0O0OO0O .doneeNo }#line:256
                            OO0O00O0OO000O000 =requests .request ('post',f'{host}/finance/give-gold',headers =OO00O0O0O0OO0O00O ,data =O00OO0OOO0O0000O0 ).json ()#line:257
                            if 'status'in OO0O00O0OO000O000 :#line:259
                                if OO0O00O0OO000O000 ['status']==200 :#line:260
                                    if OO0O00O0OO000O000 ['data']:#line:261
                                        print (f'【赠送种子】:赠送{OO0000000OOOOO000}种子给{O00OOOOO0O0O0OO0O.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as OO0O00O0000O00OO0 :#line:265
            print (OO0O00O0000O00OO0 )#line:266
    def invitation (O00O0O0OO00OO00O0 ):#line:268
        try :#line:269
            _O00O0OO00OOO0OO0O =float (bundled_def ())/4 #line:270
            O0O0OO00O00OOOOOO =f'_innerId={int(_O00O0OO00OOO0OO0O)}_{timi_new()}'#line:271
            O00000O00O0O00000 ={'authorization':O00O0O0OO00OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00O00OOOOOO ),'signstring':O0O0OO00O00OOOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            O0OOO000OO00000OO ={"innerId":int (_O00O0OO00OOO0OO0O )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00000O00O0O00000 ,data =O0OOO000OO00000OO )#line:282
        except Exception as O00OO0O0O00OOO0OO :#line:283
            print (O00OO0O0O00OOO0OO )#line:284
    def winning_rewards (O00O0OOOO000O00OO ):#line:287
        try :#line:288
            OO00000O000OO0OOO =f'__{timi_new()}'#line:289
            OOO0O0OO0O0O0OOOO ={'authorization':O00O0OOOO000O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000O000OO0OOO ),'signstring':OO00000O000OO0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            O00O0OO00O0O0OOO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO0O0OO0O0O0OOOO ).json ()#line:299
            if 'status'in O00O0OO00O0O0OOO0 :#line:301
                if O00O0OO00O0O0OOO0 ['status']==200 :#line:302
                    if O00O0OO00O0O0OOO0 ['data']['amount']:#line:303
                        OOOO0OOO0OOO00000 =O00O0OO00O0O0OOO0 ['data']['amount']['gold']#line:304
                        return OOOO0OOO0OOO00000 #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as O00OOOOO0O00OOOO0 :#line:308
            print (O00OOOOO0O00OOOO0 )#line:309
    def certification (OOO0OO0OOO000O0OO ):#line:312
        try :#line:313
            O0O0000O000O0OO0O =f'__{timi_new()}'#line:314
            O0O0OOOO0000O0OO0 ={'authorization':OOO0OO0OOO000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000O000O0OO0O ),'signstring':O0O0000O000O0OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OO0OO00OOOO0OOO0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0O0OOOO0000O0OO0 ).json ()#line:324
            if 'status'in OO0OO00OOOO0OOO0O :#line:326
                if OO0OO00OOOO0OOO0O ['status']==200 :#line:327
                    if OO0OO00OOOO0OOO0O ['data']['result']:#line:328
                        OOOO0OO0O00OOO00O =OO0OO00OOOO0OOO0O ['data']['nick_name']#line:329
                        return OOOO0OO0O00OOO00O #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as OO000O000000OO000 :#line:333
            print (OO000O000000OO000 )#line:334
    def crops_illustrated (OOO0O00O0OO0000OO ):#line:337
        try :#line:338
            OOO000OO0O0000O00 =f'__{timi_new()}'#line:339
            OO000O0O0O0000000 ={'authorization':OOO0O00O0OO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO0O0000O00 ),'signstring':OOO000OO0O0000O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            O000O000O0O0O0O0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO000O0O0O0000000 ).json ()#line:349
            if 'status'in O000O000O0O0O0O0O :#line:351
                if O000O000O0O0O0O0O ['status']==200 :#line:352
                    O000OOOO0000OO0OO =O000O000O0O0O0O0O ['data'][0 ]['crops']#line:353
                    for O0O000O00O000OO00 in O000OOOO0000OO0OO :#line:354
                        if O0O000O00O000OO00 ['ill_clover_award']:#line:355
                            if float (O0O000O00O000OO00 ['ill_clover_award'])>1 :#line:356
                                if O0O000O00O000OO00 ['is_finish']:#line:357
                                    if not O0O000O00O000OO00 ['is_getit']:#line:358
                                        if OOO0O00O0OO0000OO .certification ()!='未实名':#line:359
                                            OOO000OO0O0000O00 =f'_award_level={O0O000O00O000OO00["level"]}_{timi_new()}'#line:360
                                            OO000O0O0O0000000 ={'authorization':OOO0O00O0OO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO0O0000O00 ),'signstring':OOO000OO0O0000O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            OO0O00000000OO00O ={"award_level":O0O000O00O000OO00 ['level']}#line:370
                                            OOO0O0O00OOO000O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO000O0O0O0000000 ,json =OO0O00000000OO00O ).json ()#line:372
                                            if 'status'in OOO0O0O00OOO000O0 :#line:373
                                                if OOO0O0O00OOO000O0 ['status']==200 :#line:374
                                                    O0OOOO00OOOOO0OOO =OOO0O0O00OOO000O0 ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{O0O000O00O000OO00["crop_name"]}成就丨奖励{O0OOOO00OOOOO0OOO}☘️')#line:377
                                                if OOO0O0O00OOO000O0 ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{OOO0O0O00OOO000O0["message"]}')#line:379
        except Exception as O0000OO00OOOO00O0 :#line:380
            print (O0000OO00OOOO00O0 )#line:381
    def watched_ad (OOO00000000O00O00 ):#line:384
        try :#line:385
            O0OO000O00000O000 =f'__{timi_new()}'#line:386
            OO0OO0O00000000OO ={'authorization':OOO00000000O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O00000O000 ),'signstring':O0OO000O00000O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            OOO00000OOOOO0O00 =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO0O00000000OO ).json ()#line:396
            if 'status'in OOO00000OOOOO0O00 :#line:398
                if OOO00000OOOOO0O00 ['status']==200 :#line:399
                    if 'offlineInfo'in OOO00000OOOOO0O00 ['data']:#line:400
                        time .sleep (random .randint (16 ,18 ))#line:401
                        OOO0OOO0OO000O000 =OOO00000OOOOO0O00 ['data']['offlineInfo']['off_minute']#line:402
                        OOOOO00OOO0OOO0O0 =float (OOO00000OOOOO0O00 ['data']['silver'])/1000000000000 #line:403
                        time .sleep (1 )#line:404
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0OO0O00000000OO ).json ()#line:405
                        time .sleep (2 )#line:406
                        O0O00O000000O0O0O =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO0O00000000OO ).json ()#line:407
                        if 'status'in O0O00O000000O0O0O :#line:409
                            if O0O00O000000O0O0O ['status']==200 :#line:410
                                O0O00OO0000O00OO0 =float (O0O00O000000O0O0O ['data']['silver'])/1000000000000 #line:411
                                O0000OOOOO00OOO0O =str (O0O00OO0000O00OO0 -OOOOO00OOO0OOO0O0 )[:6 ]#line:412
                                print (f'【离线奖励】:翻倍离线{OOO0OOO0OO000O000}分钟奖励🌱数量:{O0000OOOOO00OOO0O}t粒')#line:413
        except Exception as O0OO0O000OOOOOO00 :#line:414
            print (O0OO0O000OOOOOO00 )#line:415
    def user_ad (O000OO0OO0OOOO00O ):#line:418
        try :#line:419
            O0O0O00OOOO0OOOOO =f'__{timi_new()}'#line:420
            OO000OO0OOOOO0OOO ={'authorization':O000OO0OO0OOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OOOO0OOOOO ),'signstring':O0O0O00OOOO0OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:429
            OOOO000OO000OO000 =requests .request ('get',f'{host}/user/ad',headers =OO000OO0OOOOO0OOO ).json ()#line:430
            if 'status'in OOOO000OO000OO000 :#line:432
                if OOOO000OO000OO000 ['status']==200 :#line:433
                    O000OOO00O00O000O =OOOO000OO000OO000 ['data']['max_time']#line:434
                    O0O000OOOOOOOO0OO =OOOO000OO000OO000 ['data']['watch_time']#line:435
                    OO000O0OO0000O000 =OOOO000OO000OO000 ['data']['added_time']#line:436
                    print (f'【获取种子】:获取🌱剩余{OO000O0OO0000O000 + O000OOO00O00O000O - O0O000OOOOOOOO0OO}次丨好友提供:{OO000O0OO0000O000}次')#line:437
                    if OO000O0OO0000O000 +O000OOO00O00O000O -O0O000OOOOOOOO0OO >0 :#line:438
                        time .sleep (random .randint (16 ,19 ))#line:439
                        OOOO00OO0OO00O00O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO000OO0OOOOO0OOO ).json ()#line:440
                        if 'status'in OOOO00OO0OO00O00O :#line:442
                            if OOOO00OO0OO00O00O ['status']==200 :#line:443
                                OO0OO00000OO00OO0 =float (OOOO00OO0OO00O00O ['data']['silver'])/1000000000000 #line:444
                                print (f'【获取种子】:获得🌱:{int(OO0OO00000OO00OO0)}t粒')#line:445
                                return True #line:446
                            if OOOO00OO0OO00O00O ['status']==500 :#line:447
                                O00OO00O00O0OOOOO =OOOO00OO0OO00O00O ['message']#line:448
                                print (f'【获取种子】:{O00OO00O00O0OOOOO}')#line:449
                                return False #line:450
        except Exception as O0O0000OOO0000O00 :#line:451
            print (O0O0000OOO0000O00 )#line:452
    def synthetic (OO0OOO0O0OOOOOO00 ):#line:455
        global id ,g #line:456
        try :#line:457
            OO0OOO00000000OO0 =OO0OOO0O0OOOOOO00 .level_new ()#line:458
            O0OO0OO0O00OOOOO0 =random .randint (9 ,11 )#line:459
            OOO00O0O0O0OOO000 =f'_site=8&targetSite={O0OO0OO0O00OOOOO0}_{timi_new()}'#line:460
            O00OOO0000000O0O0 ={'accept':'application/json, text/plain, */*','authorization':OO0OOO0O0OOOOOO00 .token ,'timestamp':timi_new (),'sign':sign (OOO00O0O0O0OOO000 ),'signstring':OOO00O0O0O0OOO000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:475
            OOO00O0OO000OO0OO ={"site":int (8 ),"targetSite":int (O0OO0OO0O00OOOOO0 )}#line:476
            requests .request ('post',f'{host}/game/crops/move',headers =O00OOO0000000O0O0 ,json =OOO00O0OO000OO0OO )#line:477
            while True :#line:478
                O000O00O00OO0O00O =f'__{timi_new()}'#line:479
                OOO0OOO0OOO0OO0OO ={'authorization':OO0OOO0O0OOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00O00OO0O00O ),'signstring':O000O00O00OO0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                OO0O000OO00O00O00 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OOO0OOO0OO0OO ).json ()#line:489
                if 'status'in OO0O000OO00O00O00 :#line:491
                    if OO0O000OO00O00O00 ['status']==200 :#line:492
                        OO0OO00OO0000O000 =OO0O000OO00O00O00 ['data']['cropList']#line:493
                        OO000OOOOOO0OO00O =OO0O000OO00O00O00 ['data']['gameCoreDataDBid']#line:494
                        OOOOOO0O0O000O000 =float (OO0O000OO00O00O00 ['data']['silver'])/1000000000000 #line:495
                        if OOOOOO0O0O000O000 <6750 :#line:496
                            print (f'【种植合成】:🌱不足6750t')#line:497
                            break #line:498
                        OO00000OO0OO0O00O =0 #line:499
                        for O00OO00OOOOOO0OO0 in OO0OO00OO0000O000 :#line:500
                            if not O00OO00OOOOOO0OO0 :#line:501
                                OO00OOOOOO00O0O00 =f'_crop_id={OO000OOOOOO0OO00O}&site={OO00000OO0OO0O00O}_{OO0OOO0O0OOOOOO00.time}'#line:502
                                O0OOOOOO0O000O0OO ={'authorization':OO0OOO0O0OOOOOO00 .token ,'timestamp':OO0OOO0O0OOOOOO00 .time ,'sign':sign (OO00OOOOOO00O0O00 ),'signstring':OO00OOOOOO00O0O00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:511
                                OO0O000OO0OOO0OO0 ={"site":OO00000OO0OO0O00O ,"crop_id":OO000OOOOOO0OO00O }#line:512
                                OO00OOO0OOOO0OOOO =requests .request ('post',f'{host}/game/crops/buy',headers =O0OOOOOO0O000O0OO ,data =OO0O000OO0OOO0OO0 ).json ()#line:513
                                time .sleep (random .randint (1 ,3 )/10 )#line:515
                                if 'status'in OO00OOO0OOOO0OOOO :#line:516
                                    if OO00OOO0OOOO0OOOO ['status']==200 :#line:517
                                        if OO00OOO0OOOO0OOOO ['message']=='种子数量不足':#line:518
                                            OO0OOO00000000OO0 =OO0OOO0O0OOOOOO00 .level_new ()#line:519
                                            print (f'【种植合成】:{OO00OOO0OOOO0OOOO["message"]}')#line:520
                                            if not OO0OOO0O0OOOOOO00 .user_ad ():#line:521
                                                return False #line:522
                                    if OO00OOO0OOOO0OOOO ['status']==500 :#line:523
                                        print (f'【种植合成】:{OO00OOO0OOOO0OOOO["message"]}')#line:524
                                        return False #line:525
                            OO00000OO0OO0O00O +=1 #line:526
                        OO00OO00OOOO00O0O =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OOO0OOO0OO0OO ).json ()#line:527
                        OO0O000O0O0000O00 =OO00OO00OOOO00O0O ['data']['cropList']#line:528
                        OO0O0OOO00O0O000O =False #line:529
                        for O00OO00OOOOOO0OO0 in range (12 ):#line:530
                            id =OO0O000O0O0000O00 [O00OO00OOOOOO0OO0 ]['level']#line:531
                            if float (OO0OOO00000000OO0 )-float (id )>9 :#line:532
                                OOOOOOO000OOO00O0 =f'_site={O00OO00OOOOOO0OO0}_{timi_new()}'#line:533
                                O00000O000OO0O000 ={'accept':'application/json, text/plain, */*','authorization':OO0OOO0O0OOOOOO00 .token ,'timestamp':timi_new (),'sign':sign (OOOOOOO000OOO00O0 ),'signstring':OOOOOOO000OOO00O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:543
                                O0OOOOO00O00O0O00 ={"site":O00OO00OOOOOO0OO0 }#line:544
                                OOOOOO0000O00000O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00000O000OO0O000 ,data =O0OOOOO00O00O0O00 ).json ()#line:546
                                if 'status'in OOOOOO0000O00000O :#line:547
                                    if OOOOOO0000O00000O ['status']==200 :#line:548
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:549
                            if id !=0 :#line:550
                                for O0000OOOO0O0OO000 in range (11 ):#line:551
                                    O0O00O00O0O0O0OO0 =O0000OOOO0O0OO000 +1 #line:552
                                    g =OO0O000O0O0000O00 [O0O00O00O0O0O0OO0 ]['level']#line:553
                                    if id ==g :#line:554
                                        OO0000O0O0O0OO0OO =O0000OOOO0O0OO000 +2 #line:555
                                        if OO0000O0O0O0OO0OO !=O00OO00OOOOOO0OO0 +1 :#line:556
                                            O0O00OO000O00OO0O =O00OO00OOOOOO0OO0 +1 #line:557
                                            time .sleep (random .randint (1 ,3 )/10 )#line:559
                                            OOO00O0O0O0OOO000 =f'_site={O0O00OO000O00OO0O - 1}&targetSite={OO0000O0O0O0OO0OO - 1}_{timi_new()}'#line:560
                                            O00OOO0000000O0O0 ={'accept':'application/json, text/plain, */*','authorization':OO0OOO0O0OOOOOO00 .token ,'timestamp':timi_new (),'sign':sign (OOO00O0O0O0OOO000 ),'signstring':OOO00O0O0O0OOO000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:575
                                            O0O00OO0OOO0OO0OO ={"site":int (O0O00OO000O00OO0O -1 ),"targetSite":int (OO0000O0O0O0OO0OO -1 )}#line:576
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00OOO0000000O0O0 ,json =O0O00OO0OOO0OO0OO )#line:577
                                            print (f'【种植合成】:位置{O0O00OO000O00OO0O}和位置{OO0000O0O0O0OO0OO}合出{int(id) + 1}级农作物')#line:578
                                            OO0O0OOO00O0O000O =True #line:579
                                    if OO0O0OOO00O0O000O :#line:580
                                        break #line:581
                                if OO0O0OOO00O0O000O :#line:582
                                    break #line:583
        except :#line:584
            OO0OOO0O0OOOOOO00 .synthetic ()#line:585
    def level_new (O0OO0OOO0O0000O00 ):#line:588
        try :#line:589
            OO00OOOO00000O00O =f'__{timi_new()}'#line:590
            OOOOOO000OO000000 ={'authorization':O0OO0OOO0O0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOO00000O00O ),'signstring':OO00OOOO00000O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:599
            OO0000O00OO0O0OO0 =requests .request ('get',f'{host}/user',headers =OOOOOO000OO000000 ).json ()#line:600
            if 'status'in OO0000O00OO0O0OO0 :#line:601
                if OO0000O00OO0O0OO0 ['status']==200 :#line:602
                    return float (OO0000O00OO0O0OO0 ['data']['level'])#line:603
        except Exception as O000OOO0OOO00O0OO :#line:604
            print (O000OOO0OOO00O0OO )#line:605
    def propsraffle (O0O0O00O00OO0OO0O ):#line:608
        try :#line:609
            while True :#line:610
                O0O0000000O000OOO =f'__{timi_new()}'#line:611
                OO0OOOO0OO0O0OO00 ={'authorization':O0O0O00O00OO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000000O000OOO ),'signstring':O0O0000000O000OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:620
                OOOOOOOOO0O00O00O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0OOOO0OO0O0OO00 ).json ()#line:621
                if 'status'in OOOOOOOOO0O00O00O :#line:623
                    if OOOOOOOOO0O00O00O ['status']==200 :#line:624
                        OOOOOO00OOO00OO00 =OOOOOOOOO0O00O00O ['data']['rows']#line:625
                        O00OOO0OOOO0O0000 =OOOOOOOOO0O00O00O ['data']['vstate']#line:626
                        if OOOOOO00OOO00OO00 ==5 or OOOOOO00OOO00OO00 ==6 or OOOOOO00OOO00OO00 ==7 :#line:627
                            O000O00OO0O0000OO =OOOOOOOOO0O00O00O ['data']['silver']#line:628
                            print (f'【转盘抽奖】:获得种子:{O000O00OO0O0000OO}')#line:629
                        if OOOOOO00OOO00OO00 ==1 or OOOOOO00OOO00OO00 ==2 or OOOOOO00OOO00OO00 ==3 :#line:630
                            OO0O00000000OO000 =OOOOOOOOO0O00O00O ['data']['clover']#line:631
                            print (f'【转盘抽奖】:获得三叶草:{OO0O00000000OO000}')#line:632
                        if OOOOOO00OOO00OO00 ==4 or OOOOOO00OOO00OO00 ==8 :#line:633
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:634
                        if OOOOOO00OOO00OO00 =='抽奖次数已用完':#line:638
                            break #line:671
                time .sleep (random .randint (8 ,15 )/10 )#line:672
        except Exception as O0O0O0OOOO00OO0O0 :#line:673
            print (O0O0O0OOOO00OO0O0 )#line:674
    def friends_invitation (OOOO00OO0OOOOO0OO ):#line:677
        try :#line:678
            O0000000OOOO00O00 =f'__{timi_new()}'#line:679
            O0OOOOOO00O000O0O ={'authorization':OOOO00OO0OOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000000OOOO00O00 ),'signstring':O0000000OOOO00O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:688
            OO0O0000OO0O0O00O =requests .request ('get',f'{host}/friends',headers =O0OOOOOO00O000O0O ).json ()#line:689
            if 'status'in OO0O0000OO0O0O00O :#line:690
                if OO0O0000OO0O0O00O ['status']==200 :#line:691
                    O00O0OOO000OOOOO0 =OO0O0000OO0O0O00O ['data']['myInviteter']#line:692
                    if O00O0OOO000OOOOO0 :#line:693
                        OO000OOO0O0O0OOO0 =O00O0OOO000OOOOO0 ['user']['nickname']#line:694
                        OO0000OOOO000000O =OOOO00OO0OOOOO0OO .certification ()#line:695
                        print (f'【查邀请人】:我的邀请人:{OO000OOO0O0O0OOO0}丨实名:{OO0000OOOO000000O}')#line:696
                    else :#line:697
                        if OOOO00OO0OOOOO0OO .innerId !='0':#line:698
                            OOOO00OO0OOOOO0OO .invitation ()#line:699
        except Exception as OO0000O0000O00OOO :#line:700
            print (OO0000O0000O00OOO )#line:701
    def add_clover (O0O00OO0O00OO000O ):#line:704
        global golden_seed #line:705
        try :#line:706
            OO0OO0OO00O00O0O0 =f'__{timi_new()}'#line:707
            O000O0OOOO0000O00 ={'authorization':O0O00OO0O00OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO00O00O0O0 ),'signstring':OO0OO0OO00O00O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:716
            OO00O0000OOO00000 =requests .request ('get',f'{host}/assets/clovers',headers =O000O0OOOO0000O00 ).json ()#line:717
            if 'status'in OO00O0000OOO00000 :#line:719
                if OO00O0000OOO00000 ['status']==200 :#line:720
                    O0OOOOOOOOOO00O00 =OO00O0000OOO00000 ['data']['clover']#line:721
                    O0OOOO0O0O0OOO00O =OO00O0000OOO00000 ['data']['used_clover']#line:722
                    O0000O0OO000O0OO0 =float (O0OOOOOOOOOO00O00 )-float (O0OOOO0O0O0OOO00O )#line:723
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OOOO0O0O0OOO00O}')#line:724
                    if O0O00OO0O00OO000O .certification ()!='未实名':#line:725
                        if O0000O0OO000O0OO0 >1 :#line:726
                            OO0OO0OO00O00O0O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0000O0OO000O0OO0)}_{timi_new()}'#line:727
                            OOO0OO000OOO0O00O ={'authorization':O0O00OO0O00OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO00O00O0O0 ),'signstring':OO0OO0OO00O00O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:736
                            O000O0OO0O000OO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0000O0OO000O0OO0 )}#line:737
                            O00O000OO00O00OO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO0OO000OOO0O00O ,data =O000O0OO0O000OO00 ).json ()#line:738
                            if 'status'in O00O000OO00O00OO0 :#line:740
                                if O00O000OO00O00OO0 ['status']==200 :#line:741
                                    print (f'【参与抽奖】:添加☘️:{O00O000OO00O00OO0["data"]}丨数量:{O0000O0OO000O0OO0}')#line:742
                                if O00O000OO00O00OO0 ['status']==500 :#line:743
                                    print (f'【参与抽奖】:添加☘️:{O00O000OO00O00OO0["message"]}')#line:744
            O0O0OO0O00OO000O0 =requests .request ('get',f'{host}/lottery',headers =O000O0OOOO0000O00 ).json ()#line:745
            O0OO0O0OOOOO00O0O =O0O00OO0O00OO000O .winning_rewards ()#line:747
            if 'status'in O0O0OO0O00OO000O0 :#line:748
                if O0O0OO0O00OO000O0 ['status']==200 :#line:749
                    O0O00OO0OOOOOO00O =O0O0OO0O00OO000O0 ['data'][0 ]['day_get_gold_quantity']#line:750
                    golden_seed +=float (O0O00OO0OOOOOO00O )#line:751
                    OOOO00OO00OO000O0 =O0O0OO0O00OO000O0 ['data'][1 ]['value']#line:752
                    O0000OO0OO0O0OO00 =O0O0OO0O00OO000O0 ['data'][0 ]['join_number']#line:753
                    O0OO0000OO0OO000O =int (float (O0O0OO0O00OO000O0 ['data'][0 ]['totalValue']))#line:754
                    O00OO0OOO0OO0OOO0 =float (OOOO00OO00OO000O0 /O0OO0000OO0OO000O )*10000 #line:755
                    O000O0OO000O0OOO0 =O0OO0000OO0OO000O /O0000OO0OO0O0OO00 #line:756
                    print (f'【参与抽奖】:预计每天中{str(O0O00OO0OOOOOO00O)[:6]}颗金种子丨好友收益:{str(O0OO0O0OOOOO00O0O)[:6]}')#line:757
                    print (f'【抽奖统计】:每1万☘️中{str(O00OO0OOO0OO0OOO0)[:6]}颗金种子丨☘️人均:{str(O000O0OO000O0OOO0)[:7]}️')#line:758
        except Exception as O0O00OO0O0OOO00OO :#line:759
            print (O0O00OO0O0OOO00OO )#line:760
    def energy (O00OOO00O0O0000OO ):#line:764
        try :#line:765
            while True :#line:766
                O0OOO0OO000O0OOO0 =f'__{timi_new()}'#line:767
                O0O000O0O000OOOO0 ={'authorization':O00OOO00O0O0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO000O0OOO0 ),'signstring':O0OOO0OO000O0OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:776
                OOOOOOO000O000O0O =requests .request ('get',f'{host}/energy/general',headers =O0O000O0O000OOOO0 ).json ()#line:777
                if 'status'in OOOOOOO000O000O0O :#line:779
                    if OOOOOOO000O000O0O ['status']==200 :#line:780
                        OOOOO00O0O0OO000O =OOOOOOO000O000O0O ['data']['ordinary_water']#line:781
                        OOO0O0O0O00O00O0O =OOOOOOO000O000O0O ['data']['ordinary_fertilizer']#line:782
                        print (f'【我的营养】:肥料:{str(OOO0O0O0O00O00O0O).split(".")[0]}丨水滴:{str(OOOOO00O0O0OO000O).split(".")[0]}')#line:784
                        if float (OOO0O0O0O00O00O0O )<96 :#line:785
                            time .sleep (random .randint (160 ,180 )/10 )#line:786
                            O00O0O00OOOO00OOO =99 -float (OOO0O0O0O00O00O0O )#line:787
                            O0O000O00000O0O0O ={"fertilizer":str (O00O0O00OOOO00OOO ).split ('.')[0 ]}#line:788
                            OOOO00000O00OO0O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0O000O0O000OOOO0 ).json ()#line:789
                            if 'status'in OOOO00000O00OO0O0 :#line:791
                                if OOOO00000O00OO0O0 ['status']==200 :#line:792
                                    print (f'【购买肥料】:看广告获取肥料:{OOOO00000O00OO0O0["message"]}')#line:793
                        if float (OOOOO00O0O0OO000O )<880 :#line:794
                            time .sleep (random .randint (160 ,180 )/10 )#line:795
                            OO0OOOOOO0O0O0000 =999 -float (OOOOO00O0O0OO000O )#line:796
                            O000000000OOO0000 ={"water":str (OO0OOOOOO0O0O0000 ).split ('.')[0 ]}#line:797
                            OO00OOO0O0O0O00OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0O000O0O000OOOO0 ).json ()#line:798
                            if 'status'in OO00OOO0O0O0O00OO :#line:800
                                if OO00OOO0O0O0O00OO ['status']==200 :#line:801
                                    print (f'【购买水滴】:看广告获取水滴:{OO00OOO0O0O0O00OO["message"]}')#line:802
                        if float (OOO0O0O0O00O00O0O )>96 and float (OOOOO00O0O0OO000O )>880 :#line:803
                            break #line:804
        except Exception as O00O000OO00O00O0O :#line:806
            print (O00O000OO00O00O0O )#line:807
def bundled_def ():#line:809
    OO00OO00OO0O0OO00 =['5570536','7750212','7911652','7911680','7805624']#line:810
    return OO00OO00OO0O0OO00 [random .randint (0 ,len (OO00OO00OO0O0OO00 )-1 )]#line:811
def version_of_the_validation ():#line:815
    return str ((78 -56 )/10 )#line:816
def gitee_validation ():#line:819
    try :#line:820
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:821
    except :#line:822
        sys .exit (0 )#line:823
def update_the_validation ():#line:827
    try :#line:828
        OOO00O000O0OOOOO0 =gitee_validation ()#line:829
        if version_of_the_validation ()<OOO00O000O0OOOOO0 ['CityEarth']['edition']:#line:830
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO00O000O0OOOOO0["CityEarth"]["edition"]}   ❌')#line:831
            print (f'更新内容=>>{OOO00O000O0OOOOO0["CityEarth"]["content"]}   🎉')#line:832
        else :#line:833
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO00O000O0OOOOO0["CityEarth"]["edition"]}   ✅')#line:834
            print (f'更新内容=>> {OOO00O000O0OOOOO0["CityEarth"]["content"]}   🎉')#line:835
    except Exception as OOOOO0O000000O00O :#line:836
        print (OOOOO0O000000O00O )#line:837
def os_qinglong ():#line:840
    if application in os .environ :#line:841
        OO0OOOO0OO000OOOO =os .environ [application ].split ('\n')#line:842
        if len (OO0OOOO0OO000OOOO )>0 :#line:843
            return OO0OOOO0OO000OOOO #line:844
        else :#line:845
            print (f"{application}变量未启用")#line:846
            print ('脚本退出')#line:847
            sys .exit (1 )#line:848
    else :#line:849
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:851
        return os_built ()#line:852
def os_built ():#line:855
    if token :#line:856
        O0O00OOO00O000OOO =token .split ('\n')#line:857
        if len (O0O00OOO00O000OOO )>0 :#line:858
            return O0O00OOO00O000OOO #line:859
    else :#line:860
        print (f"内置变量为空")#line:861
        print ('脚本结束')#line:862
        sys .exit (0 )#line:863
if __name__ =='__main__':#line:866
    start ()#line:867
