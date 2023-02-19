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
@ 版本  2.4
"""
application = 'ce_token'  # 变量名
token = '5187ca80-44e0-41be-9754-af851acaea52&5&1932634'
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
version ='3.1.4195311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        OOOO000O0OOO00OOO =os_qinglong ()#line:10
        print (f"==========共找到{len(OOOO000O0OOO00OOO)}个账号==========")#line:11
        for OOOOO0OO0O00OO000 in OOOO000O0OOO00OOO :#line:12
            O000O000OO0O0OOOO =[]#line:13
            print (f"------------正在执行第{OOOO000O0OOO00OOO.index(OOOOO0OO0O00OO000) + 1}个账号------------")#line:14
            OOOO0OO0O00O0O0OO =CityEarth (OOOOO0OO0O00OO000 ,O000O000OO0O0OOOO )#line:15
            def OOO000OOOOO000O00 ():#line:17
                if OOOO0OO0O00O0O0OO .base_info ():#line:19
                    OOOO0OO0O00O0O0OO .sealing ()#line:21
                    OOOO0OO0O00O0O0OO .invitenum ()#line:23
                    OOOO0OO0O00O0O0OO .game_map ()#line:25
                    OOOO0OO0O00O0O0OO .friends_invitation ()#line:27
                    OOOO0OO0O00O0O0OO .add_clover ()#line:29
                    OOOO0OO0O00O0O0OO .propsraffle ()#line:31
                    OOOO0OO0O00O0O0OO .synthetic ()#line:33
                    OOOO0OO0O00O0O0OO .crops_illustrated ()#line:35
                    OOOO0OO0O00O0O0OO .give_gold ()#line:37
                    OOOO0OO0O00O0O0OO .withdraw ()#line:39
                    OOOO0OO0O00O0O0OO .energy ()#line:41
            OO0OOO0OO00O0O00O =threading .Thread (target =OOO000OOOOO000O00 )#line:42
            OO0OOO0OO00O0O00O .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        O00000O00OO00O0O0 =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00000O00OO00O0O0 +' ')#line:48
    except Exception as OO00OO00OOO0000O0 :#line:49
        print (OO00OO00OOO0000O0 )#line:50
def sign (OOO0000OOO000000O ):#line:53
    O00O00O0000OOOO0O =hashlib .md5 (OOO0000OOO000000O .encode ()).hexdigest ()#line:54
    O0O0000O000OOO0O0 ="scsc%^&*"+O00O00O0000OOOO0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    OO0OO00O000OOO00O =hashlib .md5 (O0O0000O000OOO0O0 .encode ()).hexdigest ()#line:56
    return OO0OO00O000OOO00O #line:57
def format_msg ():#line:59
    O0OO0OOOO00O00OO0 =""#line:60
    for OO0OO0000O00O00O0 in msg_list :#line:61
        O0OO0OOOO00O00OO0 +=str (OO0OO0000O00O00O0 )+"\r\n"#line:62
    return O0OO0OOOO00O00OO0 #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (O0O0OOO0O0OOOOO0O ,OO000O00O00O00OOO ,OO000000O00O0000O ):#line:71
        try :#line:72
            O0O0OOO0O0OOOOO0O .msg =OO000000O00O0000O #line:73
            O0O0OOO0O0OOOOO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            O0O0OOO0O0OOOOO0O .token =OO000O00O00O00OOO .split ('&')[0 ]#line:75
            O0O0OOO0O0OOOOO0O .innerId =OO000O00O00O00OOO .split ('&')[1 ]#line:76
            O0O0OOO0O0OOOOO0O .doneeNo =OO000O00O00O00OOO .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (OO0OOOOOOO00OOOO0 ):#line:82
        try :#line:83
            OO0OOOOOOO00OOOO0 .watched_ad ()#line:85
            OO00O00O0OO0OO0O0 =f'__{timi_new()}'#line:86
            O0000OOOOO00OO00O ={'authorization':OO0OOOOOOO00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00O0OO0OO0O0 ),'signstring':OO00O00O0OO0OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            OOOOO0000OOO00O0O =requests .request ('get',f'{host}/user',headers =O0000OOOOO00OO00O ).json ()#line:96
            if 'status'in OOOOO0000OOO00O0O :#line:98
                if OOOOO0000OOO00O0O ['status']==200 :#line:99
                    O000000000OO00OO0 =OOOOO0000OOO00O0O ['data']['nickname']#line:100
                    O000000OO00O0O00O =OOOOO0000OOO00O0O ['data']['inner_id']#line:101
                    OO00O000OO0000O00 =OOOOO0000OOO00O0O ['data']['assets']['gold']#line:102
                    O00OOO00OOO00OO00 =OOOOO0000OOO00O0O ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{O000000000OO00OO0[:5]}丨ID:{O000000OO00O0O00O}丨等级:{O00OOO00OOO00OO00}丨金种子:{str(OO00O000OO0000O00).split(".")[0]}')#line:104
                if OOOOO0000OOO00O0O ['status']==401 :#line:105
                    print (OOOOO0000OOO00O0O ['message'])#line:106
                    OO0OOOOOOO00OOOO0 .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if OOOOO0000OOO00O0O ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as O0000OOOO0000OOO0 :#line:112
            print (O0000OOOO0000OOO0 )#line:113
    def sealing (OOOO00000OO000OO0 ):#line:116
        try :#line:117
            O000OO0O0O00OO000 =f'__{timi_new()}'#line:118
            OOOOOO00O00O000O0 ={'authorization':OOOO00000OO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O0O00OO000 ),'signstring':O000OO0O0O00OO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOOOO00O00O000O0 )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =OOOOOO00O00O000O0 )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOOOO00O00O000O0 )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOOOO00O00O000O0 )#line:131
            requests .request ('get',f'{host}/user',headers =OOOOOO00O00O000O0 )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOOOO00O00O000O0 )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOOOO00O00O000O0 )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOOOO00O00O000O0 )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =OOOOOO00O00O000O0 )#line:136
            requests .request ('get',f'{host}/assets',headers =OOOOOO00O00O000O0 )#line:137
        except Exception as O0OO0O0OO0OO0O00O :#line:138
            print (O0OO0O0OO0OO0O00O )#line:139
    def withdraw (OO00O0O00O0O000O0 ):#line:143
        OOO0000O000OO0O00 =f'__{timi_new()}'#line:144
        O000O0OO000OOO000 ={'authorization':OO00O0O00O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O000OO0O00 ),'signstring':OOO0000O000OO0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        OOO0O0OOOO0O000O0 =requests .request ('get',f'{host}/assets',headers =O000O0OO000OOO000 ).json ()#line:154
        if 'status'in OOO0O0OOOO0O000O0 :#line:156
            if OOO0O0OOOO0O000O0 ['status']==200 :#line:157
                O00OO0O0O000000O0 =OOO0O0OOOO0O000O0 ['data']['cash']#line:158
                if float (O00OO0O0O000000O0 )>20 :#line:159
                    OOO0000O000OO0O00 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    O000O0OO000OOO000 ={'authorization':OO00O0O00O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O000OO0O00 ),'signstring':OOO0000O000OO0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    O0O00O0O0OOOO000O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    OO000OO00O0OO000O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O000O0OO000OOO000 ,data =O0O00O0O0OOOO000O ).json ()#line:172
                    print (OO000OO00O0OO000O )#line:173
    def invitenum (O0O0O000OO00O0O0O ):#line:176
        OO00O00OO0OO0000O =f'__{timi_new()}'#line:177
        O0OOOO00O00O000OO ={'authorization':O0O0O000OO00O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO0OO0000O ),'signstring':OO00O00OO0OO0000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O0000OO000OOO00O0 =requests .request ('get',f'{host}/invite/invitenum',headers =O0OOOO00O00O000OO ).json ()#line:187
        if 'status'in O0000OO000OOO00O0 :#line:189
            if O0000OO000OOO00O0 ['status']==200 :#line:190
                OO00O0OO0OOO0OO0O =O0000OO000OOO00O0 ['data']['invited_count']#line:191
                OO0O00OO00O00OO00 =O0000OO000OOO00O0 ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OO00O0OO0OOO0OO0O}丨间邀好友:{OO0O00OO00O00OO00}')#line:193
    def game_map (OOOOO0O000OOOOO00 ):#line:196
        try :#line:197
            OOOO00000OO0O0OOO =f'__{timi_new()}'#line:198
            OO0OOOOOO000O0OOO ={'authorization':OOOOO0O000OOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00000OO0O0OOO ),'signstring':OOOO00000OO0O0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            OOO00OO0O0OO0000O =requests .request ('get',f'{host}/game/map',headers =OO0OOOOOO000O0OOO ).json ()#line:208
            if 'status'in OOO00OO0O0OO0000O :#line:210
                if OOO00OO0O0OO0000O ['status']==200 :#line:211
                    for OO00000OO00O00O00 in OOO00OO0O0OO0000O ['data']['list'][0 ]['crops']:#line:212
                        OO000OO0O00O0OO0O =OO00000OO00O00O00 ['level']#line:214
                        if OO000OO0O00O0OO0O ==41 :#line:215
                            O000O00000O0OO00O =OO00000OO00O00O00 ['crop_name']#line:216
                            O0OOO00OOO0OO00OO =OO00000OO00O00O00 ['count']#line:217
                            if O0OOO00OOO0OO00OO >0 :#line:218
                                print (f'【农业资产】:{O000O00000O0OO00O}丨数量:{O0OOO00OOO0OO00OO}')#line:219
        except Exception as O0OO000OO0OO00OOO :#line:220
            print (O0OO000OO0OO00OOO )#line:221
    def give_gold (OO0OO0OOOO0OOOOO0 ):#line:224
        try :#line:225
            OOO0O0O0O00OOOO00 =f'__{timi_new()}'#line:226
            OO000O0O0O00OO00O ={'authorization':OO0OO0OOOO0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0O00OOOO00 ),'signstring':OOO0O0O0O00OOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            O000O00OO00000OOO =requests .request ('get',f'{host}/user',headers =OO000O0O0O00OO00O ).json ()#line:236
            if 'status'in O000O00OO00000OOO :#line:237
                if O000O00OO00000OOO ['status']==200 :#line:238
                    if float (OO0OO0OOOO0OOOOO0 .doneeNo )!=0 :#line:239
                        O0OO0OOOO000OOO00 =O000O00OO00000OOO ['data']['assets']['gold']#line:240
                        if float (O0OO0OOOO000OOO00 )>float (OO0OO0OOOO0OOOOO0 .innerId ):#line:241
                            O0000OOOO00OO0O00 =int (float (O0OO0OOOO000OOO00 )/1.1 )#line:242
                            OOO0O0O0O00OOOO00 =f'_doneeNo={OO0OO0OOOO0OOOOO0.doneeNo}&quantity={O0000OOOO00OO0O00}_{timi_new()}'#line:243
                            OO000O0O0O00OO00O ={'authorization':OO0OO0OOOO0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0O00OOOO00 ),'signstring':OOO0O0O0O00OOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            O00OO0O0O00OOOO00 ={"quantity":O0000OOOO00OO0O00 ,"doneeNo":OO0OO0OOOO0OOOOO0 .doneeNo }#line:256
                            O0O000O0O0O0O0OO0 =requests .request ('post',f'{host}/finance/give-gold',headers =OO000O0O0O00OO00O ,data =O00OO0O0O00OOOO00 ).json ()#line:257
                            if 'status'in O0O000O0O0O0O0OO0 :#line:259
                                if O0O000O0O0O0O0OO0 ['status']==200 :#line:260
                                    if O0O000O0O0O0O0OO0 ['data']:#line:261
                                        print (f'【赠送种子】:赠送{O0000OOOO00OO0O00}种子给{OO0OO0OOOO0OOOOO0.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as OO0OO00000OO0000O :#line:265
            print (OO0OO00000OO0000O )#line:266
    def invitation (OO000OO0000O0OOO0 ):#line:268
        try :#line:269
            _OO00O0O000OOOO000 =float (bundled_def ())/4 #line:270
            OOOO00OOOOO0OO000 =f'_innerId={int(_OO00O0O000OOOO000)}_{timi_new()}'#line:271
            OOOO00OOO00OO0OO0 ={'authorization':OO000OO0000O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOOOO0OO000 ),'signstring':OOOO00OOOOO0OO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            OOOO000000O000O00 ={"innerId":int (_OO00O0O000OOOO000 )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOO00OOO00OO0OO0 ,data =OOOO000000O000O00 )#line:282
        except Exception as OO00OOO0O0O0OOO0O :#line:283
            print (OO00OOO0O0O0OOO0O )#line:284
    def winning_rewards (OO00O00O0000O0O0O ):#line:287
        try :#line:288
            O0O00O0000OOO00O0 =f'__{timi_new()}'#line:289
            OO00O0OOOO0O0O0OO ={'authorization':OO00O00O0000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0000OOO00O0 ),'signstring':O0O00O0000OOO00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            OO00O000O000O0O00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO00O0OOOO0O0O0OO ).json ()#line:299
            if 'status'in OO00O000O000O0O00 :#line:301
                if OO00O000O000O0O00 ['status']==200 :#line:302
                    if OO00O000O000O0O00 ['data']['amount']:#line:303
                        OO00OO00O0OOOO0OO =OO00O000O000O0O00 ['data']['amount']['gold']#line:304
                        return OO00OO00O0OOOO0OO #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as OO0OO0OOOOO0000OO :#line:308
            print (OO0OO0OOOOO0000OO )#line:309
    def certification (OO0O0000OOOOO00OO ):#line:312
        try :#line:313
            O0OOO0O0O0O0000O0 =f'__{timi_new()}'#line:314
            O0O000O0OO0O00OO0 ={'authorization':OO0O0000OOOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O0O0O0000O0 ),'signstring':O0OOO0O0O0O0000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OO0OO0O00OOO00O0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0O000O0OO0O00OO0 ).json ()#line:324
            if 'status'in OO0OO0O00OOO00O0O :#line:326
                if OO0OO0O00OOO00O0O ['status']==200 :#line:327
                    if OO0OO0O00OOO00O0O ['data']['result']:#line:328
                        O0O0O0O0O00O0O00O =OO0OO0O00OOO00O0O ['data']['nick_name']#line:329
                        return O0O0O0O0O00O0O00O #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as OOO00OOOO0O0O0OO0 :#line:333
            print (OOO00OOOO0O0O0OO0 )#line:334
    def crops_illustrated (OOOOOO00OOO00000O ):#line:337
        try :#line:338
            OOOO0O00O0O0000O0 =f'__{timi_new()}'#line:339
            OOO0O0O0000OO0OOO ={'authorization':OOOOOO00OOO00000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00O0O0000O0 ),'signstring':OOOO0O00O0O0000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            OO00O0OO0OOOOOOOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO0O0O0000OO0OOO ).json ()#line:349
            if 'status'in OO00O0OO0OOOOOOOO :#line:351
                if OO00O0OO0OOOOOOOO ['status']==200 :#line:352
                    OO0O0O0O0OOOOOO00 =OO00O0OO0OOOOOOOO ['data'][0 ]['crops']#line:353
                    for O000OOOOO0OO000O0 in OO0O0O0O0OOOOOO00 :#line:354
                        if O000OOOOO0OO000O0 ['ill_clover_award']:#line:355
                            if float (O000OOOOO0OO000O0 ['ill_clover_award'])>1 :#line:356
                                if O000OOOOO0OO000O0 ['is_finish']:#line:357
                                    if not O000OOOOO0OO000O0 ['is_getit']:#line:358
                                        if OOOOOO00OOO00000O .certification ()!='未实名':#line:359
                                            OOOO0O00O0O0000O0 =f'_award_level={O000OOOOO0OO000O0["level"]}_{timi_new()}'#line:360
                                            OOO0O0O0000OO0OOO ={'authorization':OOOOOO00OOO00000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00O0O0000O0 ),'signstring':OOOO0O00O0O0000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            OO0O0O0OOO0O0OO0O ={"award_level":O000OOOOO0OO000O0 ['level']}#line:370
                                            O0000O0O0OOO0OO0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO0O0O0000OO0OOO ,json =OO0O0O0OOO0O0OO0O ).json ()#line:372
                                            if 'status'in O0000O0O0OOO0OO0O :#line:373
                                                if O0000O0O0OOO0OO0O ['status']==200 :#line:374
                                                    O0O00000000O0O0O0 =O0000O0O0OOO0OO0O ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{O000OOOOO0OO000O0["crop_name"]}成就丨奖励{O0O00000000O0O0O0}☘️')#line:377
                                                if O0000O0O0OOO0OO0O ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{O0000O0O0OOO0OO0O["message"]}')#line:379
        except Exception as O0000OO00000OO000 :#line:380
            print (O0000OO00000OO000 )#line:381
    def watched_ad (O00O0O00OOOO0OOOO ):#line:384
        try :#line:385
            OOO00O000OOO00000 =f'__{timi_new()}'#line:386
            O0OOO000OOOO000OO ={'authorization':O00O0O00OOOO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O000OOO00000 ),'signstring':OOO00O000OOO00000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            O00000000O0OOO000 =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO000OOOO000OO ).json ()#line:396
            if 'status'in O00000000O0OOO000 :#line:398
                if O00000000O0OOO000 ['status']==200 :#line:399
                    if 'offlineInfo'in O00000000O0OOO000 ['data']:#line:400
                        time .sleep (random .randint (3 ,5 ))#line:401
                        O0O0O0OOOO0O0OO0O =O00000000O0OOO000 ['data']['offlineInfo']['off_minute']#line:402
                        OO0O0000O0OO0OO0O =float (O00000000O0OOO000 ['data']['silver'])/1000000000000 #line:403
                        time .sleep (1 )#line:404
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0OOO000OOOO000OO ).json ()#line:405
                        time .sleep (2 )#line:406
                        OO0OO0O0OO0OOO00O =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO000OOOO000OO ).json ()#line:407
                        if 'status'in OO0OO0O0OO0OOO00O :#line:409
                            if OO0OO0O0OO0OOO00O ['status']==200 :#line:410
                                O0O0O000O0OOOOO00 =float (OO0OO0O0OO0OOO00O ['data']['silver'])/1000000000000 #line:411
                                O0OO0OO0O000O00O0 =str (O0O0O000O0OOOOO00 -OO0O0000O0OO0OO0O )[:6 ]#line:412
                                print (f'【离线奖励】:翻倍离线{O0O0O0OOOO0O0OO0O}分钟奖励🌱数量:{O0OO0OO0O000O00O0}t粒')#line:413
        except Exception as OOOOOOO0OO0OOOOO0 :#line:414
            print (OOOOOOO0OO0OOOOO0 )#line:415
    def user_ad (O0O0OO00O0OO00OOO ):#line:418
        try :#line:419
            O00OO0OOOOO0O00OO =f'__{timi_new()}'#line:420
            O0OO00O0OO0O0O0O0 ={'authorization':O0O0OO00O0OO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OOOOO0O00OO ),'signstring':O00OO0OOOOO0O00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:429
            O00O00O000O0O0OOO =requests .request ('get',f'{host}/user/ad',headers =O0OO00O0OO0O0O0O0 ).json ()#line:430
            if 'status'in O00O00O000O0O0OOO :#line:432
                if O00O00O000O0O0OOO ['status']==200 :#line:433
                    O0O000OO0O00O0000 =O00O00O000O0O0OOO ['data']['max_time']#line:434
                    OOOO00OO00O000O00 =O00O00O000O0O0OOO ['data']['watch_time']#line:435
                    O0O0OOOO0O00OOOO0 =O00O00O000O0O0OOO ['data']['added_time']#line:436
                    print (f'【获取种子】:获取🌱剩余{O0O0OOOO0O00OOOO0 + O0O000OO0O00O0000 - OOOO00OO00O000O00}次丨好友提供:{O0O0OOOO0O00OOOO0}次')#line:437
                    if O0O0OOOO0O00OOOO0 +O0O000OO0O00O0000 -OOOO00OO00O000O00 >0 :#line:438
                        time .sleep (random .randint (16 ,19 ))#line:439
                        OOO000OO0OOOO0000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OO00O0OO0O0O0O0 ).json ()#line:440
                        if 'status'in OOO000OO0OOOO0000 :#line:442
                            if OOO000OO0OOOO0000 ['status']==200 :#line:443
                                O0OOOO00O00OOOOOO =float (OOO000OO0OOOO0000 ['data']['silver'])/1000000000000 #line:444
                                print (f'【获取种子】:获得🌱:{int(O0OOOO00O00OOOOOO)}t粒')#line:445
                                return True #line:446
                            if OOO000OO0OOOO0000 ['status']==500 :#line:447
                                OO00O0O000OO0O00O =OOO000OO0OOOO0000 ['message']#line:448
                                print (f'【获取种子】:{OO00O0O000OO0O00O}')#line:449
                                return False #line:450
        except Exception as OOOO00OO00OO00O00 :#line:451
            print (OOOO00OO00OO00O00 )#line:452
    def synthetic (OOO000O0000O0OO0O ):#line:455
        global id ,g #line:456
        try :#line:457
            O00OO0OOOO0OO000O =OOO000O0000O0OO0O .level_new ()#line:458
            OO00O00O0OOOO0OO0 =random .randint (9 ,11 )#line:459
            O000O0O0O00OOOOOO =f'_site=8&targetSite={OO00O00O0OOOO0OO0}_{timi_new()}'#line:460
            O0O0000O0O00O000O ={'accept':'application/json, text/plain, */*','authorization':OOO000O0000O0OO0O .token ,'timestamp':timi_new (),'sign':sign (O000O0O0O00OOOOOO ),'signstring':O000O0O0O00OOOOOO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:475
            OO0000OO0O0O0OO00 ={"site":int (8 ),"targetSite":int (OO00O00O0OOOO0OO0 )}#line:476
            requests .request ('post',f'{host}/game/crops/move',headers =O0O0000O0O00O000O ,json =OO0000OO0O0O0OO00 )#line:477
            while True :#line:478
                OOOOOOO0OO0OOOO00 =f'__{timi_new()}'#line:479
                O0O0O0OO0OOO000OO ={'authorization':OOO000O0000O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0OO0OOOO00 ),'signstring':OOOOOOO0OO0OOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                O00OOOO0OO0OOO000 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0OO0OOO000OO ).json ()#line:489
                if 'status'in O00OOOO0OO0OOO000 :#line:491
                    if O00OOOO0OO0OOO000 ['status']==200 :#line:492
                        O000OO0O0OOOOOOO0 =O00OOOO0OO0OOO000 ['data']['cropList']#line:493
                        OOOO000OO000OO0O0 =O00OOOO0OO0OOO000 ['data']['gameCoreDataDBid']#line:494
                        O0O0000O0OOO000OO =float (O00OOOO0OO0OOO000 ['data']['silver'])/1000000000000 #line:495
                        O00O00OO0000000O0 =0 #line:500
                        for OOO0O0OOO000O0O0O in O000OO0O0OOOOOOO0 :#line:501
                            if not OOO0O0OOO000O0O0O :#line:502
                                OOOOOOO0OOOOO0OOO =f'_crop_id={OOOO000OO000OO0O0}&site={O00O00OO0000000O0}_{OOO000O0000O0OO0O.time}'#line:503
                                OOO000O0O0O00OO00 ={'authorization':OOO000O0000O0OO0O .token ,'timestamp':OOO000O0000O0OO0O .time ,'sign':sign (OOOOOOO0OOOOO0OOO ),'signstring':OOOOOOO0OOOOO0OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
                                O0OOO0OO00OOOOO00 ={"site":O00O00OO0000000O0 ,"crop_id":OOOO000OO000OO0O0 }#line:513
                                O0OOO00OO000000OO =requests .request ('post',f'{host}/game/crops/buy',headers =OOO000O0O0O00OO00 ,data =O0OOO0OO00OOOOO00 ).json ()#line:514
                                time .sleep (random .randint (1 ,3 )/10 )#line:516
                                if 'status'in O0OOO00OO000000OO :#line:517
                                    if O0OOO00OO000000OO ['status']==200 :#line:518
                                        if O0OOO00OO000000OO ['message']=='种子数量不足':#line:519
                                            O00OO0OOOO0OO000O =OOO000O0000O0OO0O .level_new ()#line:520
                                            print (f'【种植合成】:{O0OOO00OO000000OO["message"]}')#line:521
                                            if not OOO000O0000O0OO0O .user_ad ():#line:522
                                                return False #line:523
                                    if O0OOO00OO000000OO ['status']==500 :#line:524
                                        print (f'【种植合成】:{O0OOO00OO000000OO["message"]}')#line:525
                                        return False #line:526
                            O00O00OO0000000O0 +=1 #line:527
                        O0OO00O0O0000OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0OO0OOO000OO ).json ()#line:528
                        O000000O00OO00OOO =O0OO00O0O0000OOO0 ['data']['cropList']#line:529
                        OO0OO0000O00000O0 =False #line:530
                        for OOO0O0OOO000O0O0O in range (12 ):#line:531
                            id =O000000O00OO00OOO [OOO0O0OOO000O0O0O ]['level']#line:532
                            if float (O00OO0OOOO0OO000O )-float (id )>9 :#line:533
                                OO000O0O0O0OOOO00 =f'_site={OOO0O0OOO000O0O0O}_{timi_new()}'#line:534
                                OOOO0OO0O0O00O000 ={'accept':'application/json, text/plain, */*','authorization':OOO000O0000O0OO0O .token ,'timestamp':timi_new (),'sign':sign (OO000O0O0O0OOOO00 ),'signstring':OO000O0O0O0OOOO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:544
                                OOO0OOOO00OOO0O00 ={"site":OOO0O0OOO000O0O0O }#line:545
                                O0000O00O0O0O0O0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOO0OO0O0O00O000 ,data =OOO0OOOO00OOO0O00 ).json ()#line:547
                                if 'status'in O0000O00O0O0O0O0O :#line:548
                                    if O0000O00O0O0O0O0O ['status']==200 :#line:549
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:550
                            if id !=0 :#line:551
                                for OO00O0O000000O00O in range (11 ):#line:552
                                    O00OO00OOOO0OO00O =OO00O0O000000O00O +1 #line:553
                                    g =O000000O00OO00OOO [O00OO00OOOO0OO00O ]['level']#line:554
                                    if id ==g :#line:555
                                        OO000OO000OO0OOO0 =OO00O0O000000O00O +2 #line:556
                                        if OO000OO000OO0OOO0 !=OOO0O0OOO000O0O0O +1 :#line:557
                                            OO000OO0O00OO0O00 =OOO0O0OOO000O0O0O +1 #line:558
                                            time .sleep (random .randint (1 ,3 )/10 )#line:560
                                            O000O0O0O00OOOOOO =f'_site={OO000OO0O00OO0O00 - 1}&targetSite={OO000OO000OO0OOO0 - 1}_{timi_new()}'#line:561
                                            O0O0000O0O00O000O ={'accept':'application/json, text/plain, */*','authorization':OOO000O0000O0OO0O .token ,'timestamp':timi_new (),'sign':sign (O000O0O0O00OOOOOO ),'signstring':O000O0O0O00OOOOOO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:576
                                            O00OOOOO00O0OO0O0 ={"site":int (OO000OO0O00OO0O00 -1 ),"targetSite":int (OO000OO000OO0OOO0 -1 )}#line:577
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0O0000O0O00O000O ,json =O00OOOOO00O0OO0O0 )#line:578
                                            OO0OO0000O00000O0 =True #line:580
                                    if OO0OO0000O00000O0 :#line:581
                                        break #line:582
                                if OO0OO0000O00000O0 :#line:583
                                    break #line:584
        except :#line:585
            OOO000O0000O0OO0O .synthetic ()#line:586
    def level_new (OOO00O0OOOO0000O0 ):#line:589
        try :#line:590
            OOOOOOOO00OO00O0O =f'__{timi_new()}'#line:591
            O0O00000O0O0OOO0O ={'authorization':OOO00O0OOOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO00OO00O0O ),'signstring':OOOOOOOO00OO00O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            OOOOOO0OO0OO0000O =requests .request ('get',f'{host}/user',headers =O0O00000O0O0OOO0O ).json ()#line:601
            if 'status'in OOOOOO0OO0OO0000O :#line:602
                if OOOOOO0OO0OO0000O ['status']==200 :#line:603
                    return float (OOOOOO0OO0OO0000O ['data']['level'])#line:604
        except Exception as O00OO0000OOO00O00 :#line:605
            print (O00OO0000OOO00O00 )#line:606
    def propsraffle (O0OOO00O0OO0OO00O ):#line:609
        try :#line:610
            while True :#line:611
                OOOO00OOOO0O00OO0 =f'__{timi_new()}'#line:612
                OOO00OOO00O000OO0 ={'authorization':O0OOO00O0OO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOOO0O00OO0 ),'signstring':OOOO00OOOO0O00OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:621
                OO0O0O0OOO00OO000 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO00OOO00O000OO0 ).json ()#line:622
                if 'status'in OO0O0O0OOO00OO000 :#line:624
                    if OO0O0O0OOO00OO000 ['status']==200 :#line:625
                        O0O0OO00OOOO0O00O =OO0O0O0OOO00OO000 ['data']['rows']#line:626
                        OO0O0O0000OOO00OO =OO0O0O0OOO00OO000 ['data']['vstate']#line:627
                        if O0O0OO00OOOO0O00O ==5 or O0O0OO00OOOO0O00O ==6 or O0O0OO00OOOO0O00O ==7 :#line:628
                            OOO00OO00O0O0O0OO =OO0O0O0OOO00OO000 ['data']['silver']#line:629
                            print (f'【转盘抽奖】:获得种子:{OOO00OO00O0O0O0OO}')#line:630
                        if O0O0OO00OOOO0O00O ==1 or O0O0OO00OOOO0O00O ==2 or O0O0OO00OOOO0O00O ==3 :#line:631
                            O00OOO00O0OOO0OO0 =OO0O0O0OOO00OO000 ['data']['clover']#line:632
                            print (f'【转盘抽奖】:获得三叶草:{O00OOO00O0OOO0OO0}')#line:633
                        if O0O0OO00OOOO0O00O ==4 or O0O0OO00OOOO0O00O ==8 :#line:634
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:635
                        if O0O0OO00OOOO0O00O =='抽奖次数已用完':#line:639
                            break #line:672
                time .sleep (random .randint (8 ,15 )/10 )#line:673
        except Exception as OO00000OO0OO00O00 :#line:674
            print (OO00000OO0OO00O00 )#line:675
    def friends_invitation (O00O0OOOO000000O0 ):#line:678
        try :#line:679
            O0OOOO00OOO0O00OO =f'__{timi_new()}'#line:680
            O0OOO0O0O00OO0OO0 ={'authorization':O00O0OOOO000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00OOO0O00OO ),'signstring':O0OOOO00OOO0O00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:689
            OOO0000O00OOOO00O =requests .request ('get',f'{host}/friends',headers =O0OOO0O0O00OO0OO0 ).json ()#line:690
            if 'status'in OOO0000O00OOOO00O :#line:691
                if OOO0000O00OOOO00O ['status']==200 :#line:692
                    O0O000OO00O00O0O0 =OOO0000O00OOOO00O ['data']['myInviteter']#line:693
                    if O0O000OO00O00O0O0 :#line:694
                        O0OOOO0O0O00OO000 =O0O000OO00O00O0O0 ['user']['nickname']#line:695
                        OOO000O0O00OO000O =O00O0OOOO000000O0 .certification ()#line:696
                        print (f'【查邀请人】:我的邀请人:{O0OOOO0O0O00OO000}丨实名:{OOO000O0O00OO000O}')#line:697
                    else :#line:698
                        if O00O0OOOO000000O0 .innerId !='0':#line:699
                            O00O0OOOO000000O0 .invitation ()#line:700
        except Exception as OOO00000O000O0000 :#line:701
            print (OOO00000O000O0000 )#line:702
    def add_clover (O0O0OOOO00O0O00O0 ):#line:705
        global golden_seed #line:706
        try :#line:707
            O0O00OOOOOO0O0OO0 =f'__{timi_new()}'#line:708
            O000OOO0O0O0O0000 ={'authorization':O0O0OOOO00O0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOOOOO0O0OO0 ),'signstring':O0O00OOOOOO0O0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:717
            O0000OO0O00O00OOO =requests .request ('get',f'{host}/assets/clovers',headers =O000OOO0O0O0O0000 ).json ()#line:718
            if 'status'in O0000OO0O00O00OOO :#line:720
                if O0000OO0O00O00OOO ['status']==200 :#line:721
                    O00OO0O0O0O00O000 =O0000OO0O00O00OOO ['data']['clover']#line:722
                    OO0O000OOOOO0O0OO =O0000OO0O00O00OOO ['data']['used_clover']#line:723
                    OOO0000OOO00O0O00 =float (O00OO0O0O0O00O000 )-float (OO0O000OOOOO0O0OO )#line:724
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO0O000OOOOO0O0OO}')#line:725
                    if O0O0OOOO00O0O00O0 .certification ()!='未实名':#line:726
                        if OOO0000OOO00O0O00 >1 :#line:727
                            O0O00OOOOOO0O0OO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO0000OOO00O0O00)}_{timi_new()}'#line:728
                            O000O0O0OO0O0000O ={'authorization':O0O0OOOO00O0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOOOOO0O0OO0 ),'signstring':O0O00OOOOOO0O0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                            O00OOO00000OOO000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO0000OOO00O0O00 )}#line:738
                            OO0000OO0OO0OOOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =O000O0O0OO0O0000O ,data =O00OOO00000OOO000 ).json ()#line:739
                            if 'status'in OO0000OO0OO0OOOOO :#line:741
                                if OO0000OO0OO0OOOOO ['status']==200 :#line:742
                                    print (f'【参与抽奖】:添加☘️:{OO0000OO0OO0OOOOO["data"]}丨数量:{OOO0000OOO00O0O00}')#line:743
                                if OO0000OO0OO0OOOOO ['status']==500 :#line:744
                                    print (f'【参与抽奖】:添加☘️:{OO0000OO0OO0OOOOO["message"]}')#line:745
            OO0O00O0OO0OOO000 =requests .request ('get',f'{host}/lottery',headers =O000OOO0O0O0O0000 ).json ()#line:746
            O0OOO0OOOO00OO0OO =O0O0OOOO00O0O00O0 .winning_rewards ()#line:748
            if 'status'in OO0O00O0OO0OOO000 :#line:749
                if OO0O00O0OO0OOO000 ['status']==200 :#line:750
                    O000OOO000000OO0O =OO0O00O0OO0OOO000 ['data'][0 ]['day_get_gold_quantity']#line:751
                    golden_seed +=float (O000OOO000000OO0O )#line:752
                    OOO0O00O000O0O0OO =OO0O00O0OO0OOO000 ['data'][1 ]['value']#line:753
                    O0O000000OOO00000 =OO0O00O0OO0OOO000 ['data'][0 ]['join_number']#line:754
                    OO0OO0O00O000OOOO =int (float (OO0O00O0OO0OOO000 ['data'][0 ]['totalValue']))#line:755
                    OOOOO00O000O0OO00 =float (OOO0O00O000O0O0OO /OO0OO0O00O000OOOO )*10000 #line:756
                    OO0OOOOOO000000O0 =OO0OO0O00O000OOOO /O0O000000OOO00000 #line:757
                    print (f'【参与抽奖】:预计每天中{str(O000OOO000000OO0O)[:6]}颗金种子丨好友收益:{str(O0OOO0OOOO00OO0OO)[:6]}')#line:758
                    print (f'【抽奖统计】:每1万☘️中{str(OOOOO00O000O0OO00)[:6]}颗金种子丨☘️人均:{str(OO0OOOOOO000000O0)[:7]}️')#line:759
        except Exception as O00OO0O0O0OOO000O :#line:760
            print (O00OO0O0O0OOO000O )#line:761
    def energy (O000OOO0OOO000O0O ):#line:765
        try :#line:766
            while True :#line:767
                O0OOO0OO0O0O0000O =f'__{timi_new()}'#line:768
                O00O0000O0O0OOO0O ={'authorization':O000OOO0OOO000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO0O0O0000O ),'signstring':O0OOO0OO0O0O0000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:777
                OOOO000OO00O00OO0 =requests .request ('get',f'{host}/energy/general',headers =O00O0000O0O0OOO0O ).json ()#line:778
                if 'status'in OOOO000OO00O00OO0 :#line:780
                    if OOOO000OO00O00OO0 ['status']==200 :#line:781
                        O0OO0O00O0O0OO000 =OOOO000OO00O00OO0 ['data']['ordinary_water']#line:782
                        OO0O0O00O0O0OO000 =OOOO000OO00O00OO0 ['data']['ordinary_fertilizer']#line:783
                        OO0O00O00000OO00O =OOOO000OO00O00OO0 ['data']['videoStatus']#line:784
                        print (f'【我的营养】:肥料:{str(OO0O0O00O0O0OO000).split(".")[0]}丨水滴:{str(O0OO0O00O0O0OO000).split(".")[0]}')#line:785
                        if float (OO0O0O00O0O0OO000 )<96 :#line:786
                            if OO0O00O00000OO00O :#line:787
                                time .sleep (random .randint (160 ,180 )/10 )#line:788
                                O0O0OOOO000O00OOO =99 -float (OO0O0O00O0O0OO000 )#line:789
                                OO0OO0OOOO000OO00 ={"fertilizer":str (O0O0OOOO000O00OOO ).split ('.')[0 ]}#line:790
                                OOOOOOOOOO0OO0O00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00O0000O0O0OOO0O ).json ()#line:791
                                if 'status'in OOOOOOOOOO0OO0O00 :#line:793
                                    if OOOOOOOOOO0OO0O00 ['status']==200 :#line:794
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOOOOOOO0OO0O00["message"]}')#line:795
                                    if OOOOOOOOOO0OO0O00 ['status']==500 :#line:796
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOOOOOOO0OO0O00["message"]}')#line:797
                                        break #line:798
                        if float (O0OO0O00O0O0OO000 )<880 :#line:799
                            time .sleep (random .randint (160 ,180 )/10 )#line:800
                            O000OOO00000O000O =999 -float (O0OO0O00O0O0OO000 )#line:801
                            OOO00OO0O00000OOO ={"water":str (O000OOO00000O000O ).split ('.')[0 ]}#line:802
                            O0OOO00OO00OOO000 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00O0000O0O0OOO0O ).json ()#line:803
                            if 'status'in O0OOO00OO00OOO000 :#line:805
                                if O0OOO00OO00OOO000 ['status']==200 :#line:806
                                    print (f'【购买水滴】:看广告获取水滴:{O0OOO00OO00OOO000["message"]}')#line:807
                                if O0OOO00OO00OOO000 ['status']==500 :#line:808
                                    print (f'【购买水滴】:看广告获取水滴:{O0OOO00OO00OOO000["message"]}')#line:809
                                    break #line:810
                        if float (OO0O0O00O0O0OO000 )>96 and float (O0OO0O00O0O0OO000 )>880 :#line:811
                            break #line:812
        except Exception as OOOO00O0OOO00O00O :#line:814
            print (OOOO00O0OOO00O00O )#line:815
def bundled_def ():#line:817
    OO0000000O0000O00 =['5570536','7750212','7911652','7911680','7805624']#line:818
    return OO0000000O0000O00 [random .randint (0 ,len (OO0000000O0000O00 )-1 )]#line:819
def version_of_the_validation ():#line:823
    return str ((80 -56 )/10 )#line:824
def gitee_validation ():#line:827
    try :#line:828
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:829
    except :#line:830
        sys .exit (0 )#line:831
def update_the_validation ():#line:835
    try :#line:836
        O00OO00OOOO000OOO =gitee_validation ()#line:837
        if version_of_the_validation ()<O00OO00OOOO000OOO ['CityEarth']['edition']:#line:838
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OO00OOOO000OOO["CityEarth"]["edition"]}   ❌')#line:839
            print (f'更新内容=>>{O00OO00OOOO000OOO["CityEarth"]["content"]}   🎉')#line:840
        else :#line:841
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OO00OOOO000OOO["CityEarth"]["edition"]}   ✅')#line:842
            print (f'更新内容=>> {O00OO00OOOO000OOO["CityEarth"]["content"]}   🎉')#line:843
    except Exception as OO0O0OOOO0O0OOO0O :#line:844
        print (OO0O0OOOO0O0OOO0O )#line:845
def os_qinglong ():#line:848
    if application in os .environ :#line:849
        O00OOO000O00O0OOO =os .environ [application ].split ('\n')#line:850
        if len (O00OOO000O00O0OOO )>0 :#line:851
            return O00OOO000O00O0OOO #line:852
        else :#line:853
            print (f"{application}变量未启用")#line:854
            print ('脚本退出')#line:855
            sys .exit (1 )#line:856
    else :#line:857
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:859
        return os_built ()#line:860
def os_built ():#line:863
    if token :#line:864
        O00OO0000OO0O0O00 =token .split ('\n')#line:865
        if len (O00OO0000OO0O0O00 )>0 :#line:866
            return O00OO0000OO0O0O00 #line:867
    else :#line:868
        print (f"内置变量为空")#line:869
        print ('脚本结束')#line:870
        sys .exit (0 )#line:871
if __name__ =='__main__':#line:874
    start ()#line:875
