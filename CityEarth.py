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
token = '1af25859-0f04-4207-a122-deaf8c5b9b86&5&1932634'
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
        OO0O0O00OOO0OOO00 =os_qinglong ()#line:10
        print (f"==========共找到{len(OO0O0O00OOO0OOO00)}个账号==========")#line:11
        for O0OOOO0O0O0OO0O00 in OO0O0O00OOO0OOO00 :#line:12
            O00OO0OOOOOOOO0O0 =[]#line:13
            print (f"------------正在执行第{OO0O0O00OOO0OOO00.index(O0OOOO0O0O0OO0O00) + 1}个账号------------")#line:14
            O0O000OO0OOO0OO00 =CityEarth (O0OOOO0O0O0OO0O00 ,O00OO0OOOOOOOO0O0 )#line:15
            def OOOO0OO0OO0OO0O00 ():#line:17
                if O0O000OO0OOO0OO00 .base_info ():#line:19
                    O0O000OO0OOO0OO00 .sealing ()#line:21
                    O0O000OO0OOO0OO00 .invitenum ()#line:23
                    O0O000OO0OOO0OO00 .game_map ()#line:25
                    O0O000OO0OOO0OO00 .friends_invitation ()#line:27
                    O0O000OO0OOO0OO00 .add_clover ()#line:29
                    O0O000OO0OOO0OO00 .propsraffle ()#line:31
                    O0O000OO0OOO0OO00 .synthetic ()#line:33
                    O0O000OO0OOO0OO00 .crops_illustrated ()#line:35
                    O0O000OO0OOO0OO00 .give_gold ()#line:37
                    O0O000OO0OOO0OO00 .withdraw ()#line:39
                    O0O000OO0OOO0OO00 .energy ()#line:41
            OO0OO00O0O0O00OOO =threading .Thread (target =OOOO0OO0OO0OO0O00 )#line:42
            OO0OO00O0O0O00OOO .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        OO0000OO00O0O0O00 =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0000OO00O0O0O00 +' ')#line:48
    except Exception as OO0000OOOOOO0O00O :#line:49
        print (OO0000OOOOOO0O00O )#line:50
def sign (O0O0O0OO0O000OO00 ):#line:53
    O00OOO0O0O0OO0000 =hashlib .md5 (O0O0O0OO0O000OO00 .encode ()).hexdigest ()#line:54
    O0OOOOO000O0O000O ="scsc%^&*"+O00OOO0O0O0OO0000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    OO0O0OO0000000O00 =hashlib .md5 (O0OOOOO000O0O000O .encode ()).hexdigest ()#line:56
    return OO0O0OO0000000O00 #line:57
def format_msg ():#line:59
    O00O0O0O0O00O0OOO =""#line:60
    for OOOO0O000OO0O0OOO in msg_list :#line:61
        O00O0O0O0O00O0OOO +=str (OOOO0O000OO0O0OOO )+"\r\n"#line:62
    return O00O0O0O0O00O0OOO #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (OOO0OO0OO0000OOO0 ,OO0OO0OO0OOO0000O ,O0000OOO0O0O0O000 ):#line:71
        try :#line:72
            OOO0OO0OO0000OOO0 .msg =O0000OOO0O0O0O000 #line:73
            OOO0OO0OO0000OOO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            OOO0OO0OO0000OOO0 .token =OO0OO0OO0OOO0000O .split ('&')[0 ]#line:75
            OOO0OO0OO0000OOO0 .innerId =OO0OO0OO0OOO0000O .split ('&')[1 ]#line:76
            OOO0OO0OO0000OOO0 .doneeNo =OO0OO0OO0OOO0000O .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (OOO0OOOO00OO00OO0 ):#line:82
        try :#line:83
            OOO0OOOO00OO00OO0 .watched_ad ()#line:85
            O00000O0OOO00000O =f'__{timi_new()}'#line:86
            OOOO0O000000O0000 ={'authorization':OOO0OOOO00OO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0OOO00000O ),'signstring':O00000O0OOO00000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            OOO0OO0O0000000OO =requests .request ('get',f'{host}/user',headers =OOOO0O000000O0000 ).json ()#line:96
            if 'status'in OOO0OO0O0000000OO :#line:98
                if OOO0OO0O0000000OO ['status']==200 :#line:99
                    O00O00O0OOO00O000 =OOO0OO0O0000000OO ['data']['nickname']#line:100
                    OO0O0OO000000000O =OOO0OO0O0000000OO ['data']['inner_id']#line:101
                    O0OOOO000OO0O0000 =OOO0OO0O0000000OO ['data']['assets']['gold']#line:102
                    OOOOO00O0OOOO00O0 =OOO0OO0O0000000OO ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{O00O00O0OOO00O000[:5]}丨ID:{OO0O0OO000000000O}丨等级:{OOOOO00O0OOOO00O0}丨🍂:{str(O0OOOO000OO0O0000).split(".")[0]}')#line:104
                if OOO0OO0O0000000OO ['status']==401 :#line:105
                    print (OOO0OO0O0000000OO ['message'])#line:106
                    OOO0OOOO00OO00OO0 .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if OOO0OO0O0000000OO ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as O00O0OO0O00OO0OOO :#line:112
            print (O00O0OO0O00OO0OOO )#line:113
    def sealing (OOO0OO00O0O0O000O ):#line:116
        try :#line:117
            O000OO00OOO00OO00 =f'__{timi_new()}'#line:118
            O00OO00OOO0O00OOO ={'authorization':OOO0OO00O0O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00OOO00OO00 ),'signstring':O000OO00OOO00OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00OO00OOO0O00OOO )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =O00OO00OOO0O00OOO )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00OO00OOO0O00OOO )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00OO00OOO0O00OOO )#line:131
            requests .request ('get',f'{host}/user',headers =O00OO00OOO0O00OOO )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00OO00OOO0O00OOO )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00OO00OOO0O00OOO )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =O00OO00OOO0O00OOO )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =O00OO00OOO0O00OOO )#line:136
            requests .request ('get',f'{host}/assets',headers =O00OO00OOO0O00OOO )#line:137
        except Exception as O000OOO00O00OO00O :#line:138
            print (O000OOO00O00OO00O )#line:139
    def withdraw (OOO000O0O0000OOOO ):#line:143
        OO00O0O0OO0000O00 =f'__{timi_new()}'#line:144
        OOOOOO00O0OOOOO0O ={'authorization':OOO000O0O0000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0OO0000O00 ),'signstring':OO00O0O0OO0000O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        O0O000O0OOO0OO000 =requests .request ('get',f'{host}/assets',headers =OOOOOO00O0OOOOO0O ).json ()#line:154
        if 'status'in O0O000O0OOO0OO000 :#line:156
            if O0O000O0OOO0OO000 ['status']==200 :#line:157
                O000O0OO00O0OOO00 =O0O000O0OOO0OO000 ['data']['cash']#line:158
                if float (O000O0OO00O0OOO00 )>20 :#line:159
                    OO00O0O0OO0000O00 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    OOOOOO00O0OOOOO0O ={'authorization':OOO000O0O0000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0OO0000O00 ),'signstring':OO00O0O0OO0000O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    O0OOO0OOO0OOO0OO0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    O0O00000000OOOOOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOOOO00O0OOOOO0O ,data =O0OOO0OOO0OOO0OO0 ).json ()#line:172
                    print (O0O00000000OOOOOO )#line:173
    def invitenum (OOOO0O0OO0OO0000O ):#line:176
        O00OO0OOO00O0000O =f'__{timi_new()}'#line:177
        O00OOO0O0000O0O0O ={'authorization':OOOO0O0OO0OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OOO00O0000O ),'signstring':O00OO0OOO00O0000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O00O00000OOOOOOO0 =requests .request ('get',f'{host}/invite/invitenum',headers =O00OOO0O0000O0O0O ).json ()#line:187
        if 'status'in O00O00000OOOOOOO0 :#line:189
            if O00O00000OOOOOOO0 ['status']==200 :#line:190
                OOOO0O000OO0O0O0O =O00O00000OOOOOOO0 ['data']['invited_count']#line:191
                OO0O00O0OO0OO0O00 =O00O00000OOOOOOO0 ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OOOO0O000OO0O0O0O}丨间邀好友:{OO0O00O0OO0OO0O00}')#line:193
    def game_map (OOOO000000OOO0O0O ):#line:196
        try :#line:197
            OOOO00O00O00OOO00 =f'__{timi_new()}'#line:198
            OOO0000OOOO000000 ={'authorization':OOOO000000OOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O00O00OOO00 ),'signstring':OOOO00O00O00OOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            OOOO0O000O0O0OOOO =requests .request ('get',f'{host}/game/map',headers =OOO0000OOOO000000 ).json ()#line:208
            if 'status'in OOOO0O000O0O0OOOO :#line:210
                if OOOO0O000O0O0OOOO ['status']==200 :#line:211
                    for O0OO0OO00OO00O0OO in OOOO0O000O0O0OOOO ['data']['list'][0 ]['crops']:#line:212
                        OO00000O0O0O0000O =O0OO0OO00OO00O0OO ['level']#line:214
                        if OO00000O0O0O0000O ==41 :#line:215
                            O00O0000OO00O0O0O =O0OO0OO00OO00O0OO ['crop_name']#line:216
                            O000OOOOOOOOOOO0O =O0OO0OO00OO00O0OO ['count']#line:217
                            if O000OOOOOOOOOOO0O >0 :#line:218
                                print (f'【农业资产】:{O00O0000OO00O0O0O}丨数量:{O000OOOOOOOOOOO0O}')#line:219
        except Exception as OOOOO000000O00O0O :#line:220
            print (OOOOO000000O00O0O )#line:221
    def give_gold (OO0O0000O0O000O0O ):#line:224
        try :#line:225
            O00O0O000OO00OO0O =f'__{timi_new()}'#line:226
            O0OO00O000O0000OO ={'authorization':OO0O0000O0O000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O000OO00OO0O ),'signstring':O00O0O000OO00OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            O00OO0OO000O00OO0 =requests .request ('get',f'{host}/user',headers =O0OO00O000O0000OO ).json ()#line:236
            if 'status'in O00OO0OO000O00OO0 :#line:237
                if O00OO0OO000O00OO0 ['status']==200 :#line:238
                    if float (OO0O0000O0O000O0O .doneeNo )!=0 :#line:239
                        O000OO0O000OO0O00 =O00OO0OO000O00OO0 ['data']['assets']['gold']#line:240
                        if float (O000OO0O000OO0O00 )>float (OO0O0000O0O000O0O .innerId ):#line:241
                            OO00O0OO0O00OOOO0 =int (float (O000OO0O000OO0O00 )/1.1 )#line:242
                            O00O0O000OO00OO0O =f'_doneeNo={OO0O0000O0O000O0O.doneeNo}&quantity={OO00O0OO0O00OOOO0}_{timi_new()}'#line:243
                            O0OO00O000O0000OO ={'authorization':OO0O0000O0O000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O000OO00OO0O ),'signstring':O00O0O000OO00OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            OO00O0000O00O0OOO ={"quantity":OO00O0OO0O00OOOO0 ,"doneeNo":OO0O0000O0O000O0O .doneeNo }#line:256
                            OO0O00O0000OOO00O =requests .request ('post',f'{host}/finance/give-gold',headers =O0OO00O000O0000OO ,data =OO00O0000O00O0OOO ).json ()#line:257
                            if 'status'in OO0O00O0000OOO00O :#line:259
                                if OO0O00O0000OOO00O ['status']==200 :#line:260
                                    if OO0O00O0000OOO00O ['data']:#line:261
                                        print (f'【赠送种子】:赠送{OO00O0OO0O00OOOO0}种子给{OO0O0000O0O000O0O.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as O0000O000O0OOOOOO :#line:265
            print (O0000O000O0OOOOOO )#line:266
    def invitation (O0OOOOO0000000000 ):#line:268
        try :#line:269
            _O0OO00000OOO00OO0 =float (bundled_def ())/4 #line:270
            OOOO0OOOOOOOOOOO0 =f'_innerId={int(_O0OO00000OOO00OO0)}_{timi_new()}'#line:271
            OOO0O0O00O000OOO0 ={'authorization':O0OOOOO0000000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOOOOOOOOO0 ),'signstring':OOOO0OOOOOOOOOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            O000O0O00OO00O0O0 ={"innerId":int (_O0OO00000OOO00OO0 )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO0O0O00O000OOO0 ,data =O000O0O00OO00O0O0 )#line:282
        except Exception as OOOO0000O0O00O0OO :#line:283
            print (OOOO0000O0O00O0OO )#line:284
    def winning_rewards (OOOOOOO0000OO000O ):#line:287
        try :#line:288
            O000OO000O0000O0O =f'__{timi_new()}'#line:289
            OOOOO0000OO0OO0O0 ={'authorization':OOOOOOO0000OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO000O0000O0O ),'signstring':O000OO000O0000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            OOOO0000O0000OOO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOOOO0000OO0OO0O0 ).json ()#line:299
            if 'status'in OOOO0000O0000OOO0 :#line:301
                if OOOO0000O0000OOO0 ['status']==200 :#line:302
                    if OOOO0000O0000OOO0 ['data']['amount']:#line:303
                        OOO00O0OOO0O0O00O =OOOO0000O0000OOO0 ['data']['amount']['gold']#line:304
                        return OOO00O0OOO0O0O00O #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as OOOO00O0O0OOO0OOO :#line:308
            print (OOOO00O0O0OOO0OOO )#line:309
    def certification (OO0OO00O000OO0OO0 ):#line:312
        try :#line:313
            O000O000000O000OO =f'__{timi_new()}'#line:314
            OOOOO00000OO00O00 ={'authorization':OO0OO00O000OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000000O000OO ),'signstring':O000O000000O000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            O00O0OOO0OOOOO0OO =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOOOO00000OO00O00 ).json ()#line:324
            if 'status'in O00O0OOO0OOOOO0OO :#line:326
                if O00O0OOO0OOOOO0OO ['status']==200 :#line:327
                    if O00O0OOO0OOOOO0OO ['data']['result']:#line:328
                        O0OOO00O0OOOOOO0O =O00O0OOO0OOOOO0OO ['data']['nick_name']#line:329
                        return O0OOO00O0OOOOOO0O #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as O0OOOOO00O0O0OO0O :#line:333
            print (O0OOOOO00O0O0OO0O )#line:334
    def crops_illustrated (O0O00000OOOOOO0O0 ):#line:337
        try :#line:338
            O0OO0OOO00O00000O =f'__{timi_new()}'#line:339
            OO0OOOO0O0OO0O00O ={'authorization':O0O00000OOOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO00O00000O ),'signstring':O0OO0OOO00O00000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            O0OO0OOOO00O0O0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0OOOO0O0OO0O00O ).json ()#line:349
            if 'status'in O0OO0OOOO00O0O0O0 :#line:351
                if O0OO0OOOO00O0O0O0 ['status']==200 :#line:352
                    O00O0O0OO0OO0OOO0 =O0OO0OOOO00O0O0O0 ['data'][0 ]['crops']#line:353
                    for OOOOO0O000O0O00O0 in O00O0O0OO0OO0OOO0 :#line:354
                        if OOOOO0O000O0O00O0 ['ill_clover_award']:#line:355
                            if float (OOOOO0O000O0O00O0 ['ill_clover_award'])>1 :#line:356
                                if OOOOO0O000O0O00O0 ['is_finish']:#line:357
                                    if not OOOOO0O000O0O00O0 ['is_getit']:#line:358
                                        if O0O00000OOOOOO0O0 .certification ()!='未实名':#line:359
                                            O0OO0OOO00O00000O =f'_award_level={OOOOO0O000O0O00O0["level"]}_{timi_new()}'#line:360
                                            OO0OOOO0O0OO0O00O ={'authorization':O0O00000OOOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO00O00000O ),'signstring':O0OO0OOO00O00000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            O00O0O00OO00O0OO0 ={"award_level":OOOOO0O000O0O00O0 ['level']}#line:370
                                            O00O00O0O0000O0O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0OOOO0O0OO0O00O ,json =O00O0O00OO00O0OO0 ).json ()#line:372
                                            if 'status'in O00O00O0O0000O0O0 :#line:373
                                                if O00O00O0O0000O0O0 ['status']==200 :#line:374
                                                    O0O00O00OOO0O0O0O =O00O00O0O0000O0O0 ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{OOOOO0O000O0O00O0["crop_name"]}成就丨奖励{O0O00O00OOO0O0O0O}☘️')#line:377
                                                if O00O00O0O0000O0O0 ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{O00O00O0O0000O0O0["message"]}')#line:379
        except Exception as O000OO0OOOO0OO0O0 :#line:380
            print (O000OO0OOOO0OO0O0 )#line:381
    def watched_ad (O00O00O00O000OO0O ):#line:384
        try :#line:385
            O0O0O00OOO0O0OOOO =f'__{timi_new()}'#line:386
            O00OOO0OO0O00O0OO ={'authorization':O00O00O00O000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OOO0O0OOOO ),'signstring':O0O0O00OOO0O0OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            O0OOO00000O0O0OOO =requests .request ('get',f'{host}/game/getAllData',headers =O00OOO0OO0O00O0OO ).json ()#line:396
            if 'status'in O0OOO00000O0O0OOO :#line:398
                if O0OOO00000O0O0OOO ['status']==200 :#line:399
                    if 'offlineInfo'in O0OOO00000O0O0OOO ['data']:#line:400
                        O00000O0OOO0OOOO0 =O0OOO00000O0O0OOO ['data']['offlineInfo']['off_minute']#line:401
                        OO0O0O0OOO00OO0OO =float (O0OOO00000O0O0OOO ['data']['silver'])/1000000000000 #line:402
                        time .sleep (1 )#line:403
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00OOO0OO0O00O0OO ).json ()#line:404
                        time .sleep (2 )#line:405
                        OOO00000OOO0OO0OO =requests .request ('get',f'{host}/game/getAllData',headers =O00OOO0OO0O00O0OO ).json ()#line:406
                        if 'status'in OOO00000OOO0OO0OO :#line:408
                            if OOO00000OOO0OO0OO ['status']==200 :#line:409
                                OO0OOO00OO0OO0O0O =float (OOO00000OOO0OO0OO ['data']['silver'])/1000000000000 #line:410
                                OO0OOO000O00OOO00 =str (OO0OOO00OO0OO0O0O -OO0O0O0OOO00OO0OO )[:6 ]#line:411
                                print (f'【离线奖励】:翻倍离线{O00000O0OOO0OOOO0}分钟奖励🌱数量:{OO0OOO000O00OOO00}t粒')#line:412
        except Exception as O0OOOOO0O000O00O0 :#line:413
            print (O0OOOOO0O000O00O0 )#line:414
    def user_ad (O000000OO000OOO00 ):#line:417
        try :#line:418
            OOOOO00OO00O0O0O0 =f'__{timi_new()}'#line:419
            O0O000O000000O00O ={'authorization':O000000OO000OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OO00O0O0O0 ),'signstring':OOOOO00OO00O0O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:428
            O0OO0OO0O00O0O0OO =requests .request ('get',f'{host}/user/ad',headers =O0O000O000000O00O ).json ()#line:429
            if 'status'in O0OO0OO0O00O0O0OO :#line:431
                if O0OO0OO0O00O0O0OO ['status']==200 :#line:432
                    O000OO0OO0OOOO000 =O0OO0OO0O00O0O0OO ['data']['max_time']#line:433
                    OO00OO0000O0O0O0O =O0OO0OO0O00O0O0OO ['data']['watch_time']#line:434
                    O0O0OO0OOOO00000O =O0OO0OO0O00O0O0OO ['data']['added_time']#line:435
                    print (f'【获取种子】:获取🌱剩余{O0O0OO0OOOO00000O + O000OO0OO0OOOO000 - OO00OO0000O0O0O0O}次丨好友提供:{O0O0OO0OOOO00000O}次')#line:436
                    if O0O0OO0OOOO00000O +O000OO0OO0OOOO000 -OO00OO0000O0O0O0O >0 :#line:437
                        time .sleep (random .randint (16 ,19 ))#line:438
                        OO000O0000OOO0OOO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O000O000000O00O ).json ()#line:439
                        if 'status'in OO000O0000OOO0OOO :#line:441
                            if OO000O0000OOO0OOO ['status']==200 :#line:442
                                O00O0O00000O0O0O0 =float (OO000O0000OOO0OOO ['data']['silver'])/1000000000000 #line:443
                                print (f'【获取种子】:获得🌱:{int(O00O0O00000O0O0O0)}t粒')#line:444
                                return True #line:445
                            if OO000O0000OOO0OOO ['status']==500 :#line:446
                                O0OO0O00OOOO0O0O0 =OO000O0000OOO0OOO ['message']#line:447
                                print (f'【获取种子】:{O0OO0O00OOOO0O0O0}')#line:448
                                return False #line:449
        except Exception as O000O000O0O0O0000 :#line:450
            print (O000O000O0O0O0000 )#line:451
    def synthetic (O000O00O00OOO0OOO ):#line:454
        global id ,g #line:455
        try :#line:456
            O0O00O0OOOO0OOO0O =O000O00O00OOO0OOO .level_new ()#line:457
            O0000OOOOOOO00OOO =random .randint (9 ,11 )#line:458
            O00O0000O0OOO0000 =f'_site=8&targetSite={O0000OOOOOOO00OOO}_{timi_new()}'#line:459
            OOO00OO0OO00OO0O0 ={'accept':'application/json, text/plain, */*','authorization':O000O00O00OOO0OOO .token ,'timestamp':timi_new (),'sign':sign (O00O0000O0OOO0000 ),'signstring':O00O0000O0OOO0000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:474
            O0OOO000OOO000OOO ={"site":int (8 ),"targetSite":int (O0000OOOOOOO00OOO )}#line:475
            requests .request ('post',f'{host}/game/crops/move',headers =OOO00OO0OO00OO0O0 ,json =O0OOO000OOO000OOO )#line:476
            while True :#line:477
                O00O0000O00OOO0O0 =f'__{timi_new()}'#line:478
                O0000O0O00OO000OO ={'authorization':O000O00O00OOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0000O00OOO0O0 ),'signstring':O00O0000O00OOO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:487
                OOO00O0000O0OOO0O =requests .request ('get',f'{host}/game/getAllData',headers =O0000O0O00OO000OO ).json ()#line:488
                if 'status'in OOO00O0000O0OOO0O :#line:490
                    if OOO00O0000O0OOO0O ['status']==200 :#line:491
                        OO00000O00OOO00O0 =OOO00O0000O0OOO0O ['data']['cropList']#line:492
                        OO0OO000OO0O0O0OO =OOO00O0000O0OOO0O ['data']['gameCoreDataDBid']#line:493
                        OO0O0O000OO00O000 =float (OOO00O0000O0OOO0O ['data']['silver'])/1000000000000 #line:494
                        if OO0O0O000OO00O000 <6750 :#line:495
                            print (f'【种植合成】:🌱不足6750t')#line:496
                            break #line:497
                        O00O0OOO0OO00O0OO =0 #line:498
                        for OOO00000O00OO0O00 in OO00000O00OOO00O0 :#line:499
                            if not OOO00000O00OO0O00 :#line:500
                                O0OOOOOO0OO0000OO =f'_crop_id={OO0OO000OO0O0O0OO}&site={O00O0OOO0OO00O0OO}_{O000O00O00OOO0OOO.time}'#line:501
                                OO0OOO00O00O0OOOO ={'authorization':O000O00O00OOO0OOO .token ,'timestamp':O000O00O00OOO0OOO .time ,'sign':sign (O0OOOOOO0OO0000OO ),'signstring':O0OOOOOO0OO0000OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:510
                                OOO0O000OOO000000 ={"site":O00O0OOO0OO00O0OO ,"crop_id":OO0OO000OO0O0O0OO }#line:511
                                OO0000O000O0O00O0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0OOO00O00O0OOOO ,data =OOO0O000OOO000000 ).json ()#line:512
                                time .sleep (random .randint (1 ,3 )/10 )#line:514
                                if 'status'in OO0000O000O0O00O0 :#line:515
                                    if OO0000O000O0O00O0 ['status']==200 :#line:516
                                        if OO0000O000O0O00O0 ['message']=='种子数量不足':#line:517
                                            O0O00O0OOOO0OOO0O =O000O00O00OOO0OOO .level_new ()#line:518
                                            print (f'【种植合成】:{OO0000O000O0O00O0["message"]}')#line:519
                                            if not O000O00O00OOO0OOO .user_ad ():#line:520
                                                return False #line:521
                                    if OO0000O000O0O00O0 ['status']==500 :#line:522
                                        print (f'【种植合成】:{OO0000O000O0O00O0["message"]}')#line:523
                                        return False #line:524
                            O00O0OOO0OO00O0OO +=1 #line:525
                        OOOO0OO0O0000O00O =requests .request ('get',f'{host}/game/getAllData',headers =O0000O0O00OO000OO ).json ()#line:526
                        OOOO0O000OOO00O0O =OOOO0OO0O0000O00O ['data']['cropList']#line:527
                        O0OOOOOO00OO0OOO0 =False #line:528
                        for OOO00000O00OO0O00 in range (12 ):#line:529
                            id =OOOO0O000OOO00O0O [OOO00000O00OO0O00 ]['level']#line:530
                            if float (O0O00O0OOOO0OOO0O )-float (id )>9 :#line:531
                                O0OOOO00OO000O000 =f'_site={OOO00000O00OO0O00}_{timi_new()}'#line:532
                                OOOO000O0OOOO0OOO ={'accept':'application/json, text/plain, */*','authorization':O000O00O00OOO0OOO .token ,'timestamp':timi_new (),'sign':sign (O0OOOO00OO000O000 ),'signstring':O0OOOO00OO000O000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:542
                                O0O00O0000O0OOO00 ={"site":OOO00000O00OO0O00 }#line:543
                                OOO0OOO0O0O0O0OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOO000O0OOOO0OOO ,data =O0O00O0000O0OOO00 ).json ()#line:545
                                if 'status'in OOO0OOO0O0O0O0OOO :#line:546
                                    if OOO0OOO0O0O0O0OOO ['status']==200 :#line:547
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:548
                            if id !=0 :#line:549
                                for OOOOO0OO00OO0OOO0 in range (11 ):#line:550
                                    OO000O00O0O0000O0 =OOOOO0OO00OO0OOO0 +1 #line:551
                                    g =OOOO0O000OOO00O0O [OO000O00O0O0000O0 ]['level']#line:552
                                    if id ==g :#line:553
                                        O00O0O0O0OOOOO0OO =OOOOO0OO00OO0OOO0 +2 #line:554
                                        if O00O0O0O0OOOOO0OO !=OOO00000O00OO0O00 +1 :#line:555
                                            OO00OO00OOO0O0000 =OOO00000O00OO0O00 +1 #line:556
                                            time .sleep (random .randint (1 ,3 )/10 )#line:558
                                            O00O0000O0OOO0000 =f'_site={OO00OO00OOO0O0000 - 1}&targetSite={O00O0O0O0OOOOO0OO - 1}_{timi_new()}'#line:559
                                            OOO00OO0OO00OO0O0 ={'accept':'application/json, text/plain, */*','authorization':O000O00O00OOO0OOO .token ,'timestamp':timi_new (),'sign':sign (O00O0000O0OOO0000 ),'signstring':O00O0000O0OOO0000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:574
                                            O00O000O00O0OOO00 ={"site":int (OO00OO00OOO0O0000 -1 ),"targetSite":int (O00O0O0O0OOOOO0OO -1 )}#line:575
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOO00OO0OO00OO0O0 ,json =O00O000O00O0OOO00 )#line:576
                                            print (f'【种植合成】:位置{OO00OO00OOO0O0000}和位置{O00O0O0O0OOOOO0OO}合出{int(id) + 1}级农作物')#line:577
                                            O0OOOOOO00OO0OOO0 =True #line:578
                                    if O0OOOOOO00OO0OOO0 :#line:579
                                        break #line:580
                                if O0OOOOOO00OO0OOO0 :#line:581
                                    break #line:582
        except :#line:583
            O000O00O00OOO0OOO .synthetic ()#line:584
    def level_new (O000OO0000000O00O ):#line:587
        try :#line:588
            O00000OOOO0OOO000 =f'__{timi_new()}'#line:589
            OO00O0O00OOO00OO0 ={'authorization':O000OO0000000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOOO0OOO000 ),'signstring':O00000OOOO0OOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:598
            OO0OO000OOO00OO00 =requests .request ('get',f'{host}/user',headers =OO00O0O00OOO00OO0 ).json ()#line:599
            if 'status'in OO0OO000OOO00OO00 :#line:600
                if OO0OO000OOO00OO00 ['status']==200 :#line:601
                    return float (OO0OO000OOO00OO00 ['data']['level'])#line:602
        except Exception as OOOO0O0OOOO0OO0O0 :#line:603
            print (OOOO0O0OOOO0OO0O0 )#line:604
    def propsraffle (OO00O0OO0OO00OOO0 ):#line:607
        try :#line:608
            while True :#line:609
                O00000O0O000OO0OO =f'__{timi_new()}'#line:610
                OO000O00OOO0O0O0O ={'authorization':OO00O0OO0OO00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0O000OO0OO ),'signstring':O00000O0O000OO0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:619
                OO0OOO0O000000O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO000O00OOO0O0O0O ).json ()#line:620
                if 'status'in OO0OOO0O000000O0O :#line:622
                    if OO0OOO0O000000O0O ['status']==200 :#line:623
                        O0OOO000O0O00000O =OO0OOO0O000000O0O ['data']['rows']#line:624
                        OOOO00000O000OO0O =OO0OOO0O000000O0O ['data']['vstate']#line:625
                        if O0OOO000O0O00000O ==5 or O0OOO000O0O00000O ==6 or O0OOO000O0O00000O ==7 :#line:626
                            OOO000OO0OO0O0O00 =OO0OOO0O000000O0O ['data']['silver']#line:627
                            print (f'【转盘抽奖】:获得种子:{OOO000OO0OO0O0O00}')#line:628
                        if O0OOO000O0O00000O ==1 or O0OOO000O0O00000O ==2 or O0OOO000O0O00000O ==3 :#line:629
                            OO0OOOOOO0OOO0OO0 =OO0OOO0O000000O0O ['data']['clover']#line:630
                            print (f'【转盘抽奖】:获得三叶草:{OO0OOOOOO0OOO0OO0}')#line:631
                        if O0OOO000O0O00000O ==4 or O0OOO000O0O00000O ==8 :#line:632
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:633
                        if O0OOO000O0O00000O =='抽奖次数已用完':#line:637
                            break #line:670
                time .sleep (random .randint (8 ,15 )/10 )#line:671
        except Exception as O0O000O000OOO0000 :#line:672
            print (O0O000O000OOO0000 )#line:673
    def friends_invitation (O00OO00OO0OOOO000 ):#line:676
        try :#line:677
            O0000OOO000O000OO =f'__{timi_new()}'#line:678
            OOOO0OO0OOOO0OOO0 ={'authorization':O00OO00OO0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOO000O000OO ),'signstring':O0000OOO000O000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:687
            O00O000OOO00000O0 =requests .request ('get',f'{host}/friends',headers =OOOO0OO0OOOO0OOO0 ).json ()#line:688
            if 'status'in O00O000OOO00000O0 :#line:689
                if O00O000OOO00000O0 ['status']==200 :#line:690
                    O0OO00000O0000O00 =O00O000OOO00000O0 ['data']['myInviteter']#line:691
                    if O0OO00000O0000O00 :#line:692
                        OO0O0000O000O0O00 =O0OO00000O0000O00 ['user']['nickname']#line:693
                        O0O00000O000000O0 =O00OO00OO0OOOO000 .certification ()#line:694
                        print (f'【查邀请人】:我的邀请人:{OO0O0000O000O0O00}丨实名:{O0O00000O000000O0}')#line:695
                    else :#line:696
                        if O00OO00OO0OOOO000 .innerId !='0':#line:697
                            O00OO00OO0OOOO000 .invitation ()#line:698
        except Exception as OOO0000O00O00000O :#line:699
            print (OOO0000O00O00000O )#line:700
    def add_clover (O0OOO00O0O00OOOOO ):#line:703
        global golden_seed #line:704
        try :#line:705
            O00O00000OOO0O0O0 =f'__{timi_new()}'#line:706
            OOOO00OO0O0O0OO0O ={'authorization':O0OOO00O0O00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00000OOO0O0O0 ),'signstring':O00O00000OOO0O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:715
            OOOO00OO00OOO00OO =requests .request ('get',f'{host}/assets/clovers',headers =OOOO00OO0O0O0OO0O ).json ()#line:716
            if 'status'in OOOO00OO00OOO00OO :#line:718
                if OOOO00OO00OOO00OO ['status']==200 :#line:719
                    O0O00OOO0OOO00O00 =OOOO00OO00OOO00OO ['data']['clover']#line:720
                    OO0OO000O0O0O00OO =OOOO00OO00OOO00OO ['data']['used_clover']#line:721
                    O0OOO00OO000OO0O0 =float (O0O00OOO0OOO00O00 )-float (OO0OO000O0O0O00OO )#line:722
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO0OO000O0O0O00OO}')#line:723
                    if O0OOO00O0O00OOOOO .certification ()!='未实名':#line:724
                        if O0OOO00OO000OO0O0 >1 :#line:725
                            O00O00000OOO0O0O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OOO00OO000OO0O0)}_{timi_new()}'#line:726
                            OO00O0OO0OOOO00OO ={'authorization':O0OOO00O0O00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00000OOO0O0O0 ),'signstring':O00O00000OOO0O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:735
                            OOOOO00O00OO00O00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OOO00OO000OO0O0 )}#line:736
                            O00000O0OO0OO000O =requests .request ('post',f'{host}/lottery/add-stake',headers =OO00O0OO0OOOO00OO ,data =OOOOO00O00OO00O00 ).json ()#line:737
                            if 'status'in O00000O0OO0OO000O :#line:739
                                if O00000O0OO0OO000O ['status']==200 :#line:740
                                    print (f'【参与抽奖】:添加☘️:{O00000O0OO0OO000O["data"]}丨数量:{O0OOO00OO000OO0O0}')#line:741
                                if O00000O0OO0OO000O ['status']==500 :#line:742
                                    print (f'【参与抽奖】:添加☘️:{O00000O0OO0OO000O["message"]}')#line:743
            OO000OOO0OOOOOOOO =requests .request ('get',f'{host}/lottery',headers =OOOO00OO0O0O0OO0O ).json ()#line:744
            O0OO0000O0O00O00O =O0OOO00O0O00OOOOO .winning_rewards ()#line:746
            if 'status'in OO000OOO0OOOOOOOO :#line:747
                if OO000OOO0OOOOOOOO ['status']==200 :#line:748
                    O00O0OO00OO0O00OO =OO000OOO0OOOOOOOO ['data'][0 ]['day_get_gold_quantity']#line:749
                    golden_seed +=float (O00O0OO00OO0O00OO )#line:750
                    OOO00OOOO0OOOO00O =OO000OOO0OOOOOOOO ['data'][1 ]['value']#line:751
                    OOO00O00000OOO00O =OO000OOO0OOOOOOOO ['data'][0 ]['join_number']#line:752
                    O000OOOOOO00O0OOO =int (float (OO000OOO0OOOOOOOO ['data'][0 ]['totalValue']))#line:753
                    OOO0O0OOO00O0000O =float (OOO00OOOO0OOOO00O /O000OOOOOO00O0OOO )*10000 #line:754
                    O0O00OOO0OO0OOOO0 =O000OOOOOO00O0OOO /OOO00O00000OOO00O #line:755
                    print (f'【参与抽奖】:预计每天中{str(O00O0OO00OO0O00OO)[:6]}颗🍂丨好友收益:{str(O0OO0000O0O00O00O)[:6]}')#line:756
                    print (f'【抽奖统计】:每1万☘️中{str(OOO0O0OOO00O0000O)[:4]}颗🍂丨人均{str(O0O00OOO0OO0OOOO0)[:7]}☘️')#line:757
        except Exception as O0O00OO0OO00O0OO0 :#line:758
            print (O0O00OO0OO00O0OO0 )#line:759
    def energy (OO00O0OOO00O0OOO0 ):#line:763
        try :#line:764
            while True :#line:765
                OOOOOOOO00OO0OO0O =f'__{timi_new()}'#line:766
                OO00000O0OO00OO0O ={'authorization':OO00O0OOO00O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO00OO0OO0O ),'signstring':OOOOOOOO00OO0OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:775
                O0OOOOO0000O00OO0 =requests .request ('get',f'{host}/energy/general',headers =OO00000O0OO00OO0O ).json ()#line:776
                if 'status'in O0OOOOO0000O00OO0 :#line:778
                    if O0OOOOO0000O00OO0 ['status']==200 :#line:779
                        OO0OOO000O0OO0OO0 =O0OOOOO0000O00OO0 ['data']['ordinary_water']#line:780
                        OOOO0O0O00OOOOO00 =O0OOOOO0000O00OO0 ['data']['ordinary_fertilizer']#line:781
                        print (f'【我的营养】:肥料:{str(OOOO0O0O00OOOOO00).split(".")[0]}丨水滴:{str(OO0OOO000O0OO0OO0).split(".")[0]}')#line:783
                        if float (OOOO0O0O00OOOOO00 )<96 :#line:784
                            time .sleep (random .randint (160 ,180 )/10 )#line:785
                            O0OOO00O000OO00OO =99 -float (OOOO0O0O00OOOOO00 )#line:786
                            OOO0OO00000OOO00O ={"fertilizer":str (O0OOO00O000OO00OO ).split ('.')[0 ]}#line:787
                            OO0OOOOOOO00OOO0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO00000O0OO00OO0O ).json ()#line:788
                            if 'status'in OO0OOOOOOO00OOO0O :#line:790
                                if OO0OOOOOOO00OOO0O ['status']==200 :#line:791
                                    print (f'【购买肥料】:看广告获取肥料:{OO0OOOOOOO00OOO0O["message"]}')#line:792
                        if float (OO0OOO000O0OO0OO0 )<880 :#line:793
                            time .sleep (random .randint (160 ,180 )/10 )#line:794
                            OO00O0OOOOO0OOO00 =999 -float (OO0OOO000O0OO0OO0 )#line:795
                            OOOOOOOOO0OO0OO0O ={"water":str (OO00O0OOOOO0OOO00 ).split ('.')[0 ]}#line:796
                            O00OOO0OOO00O0OO0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO00000O0OO00OO0O ).json ()#line:797
                            if 'status'in O00OOO0OOO00O0OO0 :#line:799
                                if O00OOO0OOO00O0OO0 ['status']==200 :#line:800
                                    print (f'【购买水滴】:看广告获取水滴:{O00OOO0OOO00O0OO0["message"]}')#line:801
                        if float (OOOO0O0O00OOOOO00 )>96 and float (OO0OOO000O0OO0OO0 )>880 :#line:802
                            break #line:803
        except Exception as O000000O00O0OOOOO :#line:805
            print (O000000O00O0OOOOO )#line:806
def bundled_def ():#line:808
    OOOOO000OOOO0O0O0 =['5570536','7750212','7911652','7911680','7805624']#line:809
    return OOOOO000OOOO0O0O0 [random .randint (0 ,len (OOOOO000OOOO0O0O0 )-1 )]#line:810
def version_of_the_validation ():#line:814
    return str ((78 -56 )/10 )#line:815
def gitee_validation ():#line:818
    try :#line:819
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:820
    except :#line:821
        sys .exit (0 )#line:822
def update_the_validation ():#line:826
    try :#line:827
        OOOOO0O0000O0OO00 =gitee_validation ()#line:828
        if version_of_the_validation ()<OOOOO0O0000O0OO00 ['CityEarth']['edition']:#line:829
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOO0O0000O0OO00["CityEarth"]["edition"]}   ❌')#line:830
            print (f'更新内容=>>{OOOOO0O0000O0OO00["CityEarth"]["content"]}   👍')#line:831
        else :#line:832
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOO0O0000O0OO00["CityEarth"]["edition"]}   ✅')#line:833
            print (f'更新内容=>> {OOOOO0O0000O0OO00["CityEarth"]["content"]}   👍')#line:834
    except Exception as OOO0OO0O00OO0O000 :#line:835
        print (OOO0OO0O00OO0O000 )#line:836
def os_qinglong ():#line:839
    if application in os .environ :#line:840
        OOO0OO00O00OO0000 =os .environ [application ].split ('\n')#line:841
        if len (OOO0OO00O00OO0000 )>0 :#line:842
            return OOO0OO00O00OO0000 #line:843
        else :#line:844
            print (f"{application}变量未启用")#line:845
            print ('脚本退出')#line:846
            sys .exit (1 )#line:847
    else :#line:848
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:850
        return os_built ()#line:851
def os_built ():#line:854
    if token :#line:855
        OO0OO00O0OO0O0000 =token .split ('\n')#line:856
        if len (OO0OO00O0OO0O0000 )>0 :#line:857
            return OO0OO00O0OO0O0000 #line:858
    else :#line:859
        print (f"内置变量为空")#line:860
        print ('脚本结束')#line:861
        sys .exit (0 )#line:862
if __name__ =='__main__':#line:865
    start ()#line:866
