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
time_xx = random.randint(13, 23)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
version ='3.1.4195311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        OO00OO0000OO00000 =os_qinglong ()#line:10
        print (f"==========共找到{len(OO00OO0000OO00000)}个账号==========")#line:11
        for OOO0O000OOO0OOOO0 in OO00OO0000OO00000 :#line:12
            O00OOO00O00OO0000 =[]#line:13
            print (f"------------正在执行第{OO00OO0000OO00000.index(OOO0O000OOO0OOOO0) + 1}个账号------------")#line:14
            O0OO00OO000O0O0OO =CityEarth (OOO0O000OOO0OOOO0 ,O00OOO00O00OO0000 )#line:15
            def O0000O00O0OOOO000 ():#line:17
                if O0OO00OO000O0O0OO .base_info ():#line:19
                    O0OO00OO000O0O0OO .sealing ()#line:21
                    O0OO00OO000O0O0OO .invitenum ()#line:23
                    O0OO00OO000O0O0OO .game_map ()#line:25
                    O0OO00OO000O0O0OO .friends_invitation ()#line:27
                    O0OO00OO000O0O0OO .add_clover ()#line:29
                    O0OO00OO000O0O0OO .propsraffle ()#line:31
                    O0OO00OO000O0O0OO .synthetic ()#line:33
                    O0OO00OO000O0O0OO .crops_illustrated ()#line:35
                    O0OO00OO000O0O0OO .give_gold ()#line:37
                    O0OO00OO000O0O0OO .withdraw ()#line:39
                    O0OO00OO000O0O0OO .energy ()#line:41
            O0O00OO0O0OO0O00O =threading .Thread (target =O0000O00O0OOOO000 )#line:42
            O0O00OO0O0OO0O00O .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        O0O00000OO00O00O0 =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O00000OO00O00O0 +' ')#line:48
    except Exception as O00O0OO0O0O000O00 :#line:49
        print (O00O0OO0O0O000O00 )#line:50
def sign (O00OO00000OOOO0O0 ):#line:53
    O0OO0OOOOO000O0O0 =hashlib .md5 (O00OO00000OOOO0O0 .encode ()).hexdigest ()#line:54
    O00OOOO00OOOOOO0O ="scsc%^&*"+O0OO0OOOOO000O0O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    O0O0OOO0000OOO0OO =hashlib .md5 (O00OOOO00OOOOOO0O .encode ()).hexdigest ()#line:56
    return O0O0OOO0000OOO0OO #line:57
def format_msg ():#line:59
    OO000OOO0OOOO0OO0 =""#line:60
    for OOO0OO0O000000O00 in msg_list :#line:61
        OO000OOO0OOOO0OO0 +=str (OOO0OO0O000000O00 )+"\r\n"#line:62
    return OO000OOO0OOOO0OO0 #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (OO00OO00O0000000O ,O00O00O000O0O0OOO ,O0OO00OOOO0OOO000 ):#line:71
        try :#line:72
            OO00OO00O0000000O .msg =O0OO00OOOO0OOO000 #line:73
            OO00OO00O0000000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            OO00OO00O0000000O .token =O00O00O000O0O0OOO .split ('&')[0 ]#line:75
            OO00OO00O0000000O .innerId =O00O00O000O0O0OOO .split ('&')[1 ]#line:76
            OO00OO00O0000000O .doneeNo =O00O00O000O0O0OOO .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (O0O00O00OOOO0O0O0 ):#line:82
        try :#line:83
            O0O00O00OOOO0O0O0 .watched_ad ()#line:85
            O0O0OO000OOOOO00O =f'__{timi_new()}'#line:86
            OO000OO0OO0O000OO ={'authorization':O0O00O00OOOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO000OOOOO00O ),'signstring':O0O0OO000OOOOO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            OO0O00OOOO0OO0OO0 =requests .request ('get',f'{host}/user',headers =OO000OO0OO0O000OO ).json ()#line:96
            if 'status'in OO0O00OOOO0OO0OO0 :#line:98
                if OO0O00OOOO0OO0OO0 ['status']==200 :#line:99
                    O00000O0OOOO00OO0 =OO0O00OOOO0OO0OO0 ['data']['nickname']#line:100
                    O0OO00OO0OO0OOO0O =OO0O00OOOO0OO0OO0 ['data']['inner_id']#line:101
                    O00OO0O0O0OO0OO0O =OO0O00OOOO0OO0OO0 ['data']['assets']['gold']#line:102
                    OOO0OOOOO0OOOOOO0 =OO0O00OOOO0OO0OO0 ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{O00000O0OOOO00OO0[:5]}丨ID:{O0OO00OO0OO0OOO0O}丨等级:{OOO0OOOOO0OOOOOO0}丨金种子:{str(O00OO0O0O0OO0OO0O).split(".")[0]}')#line:104
                if OO0O00OOOO0OO0OO0 ['status']==401 :#line:105
                    print (OO0O00OOOO0OO0OO0 ['message'])#line:106
                    O0O00O00OOOO0O0O0 .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if OO0O00OOOO0OO0OO0 ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as OOOO0OO00OO0000OO :#line:112
            print (OOOO0OO00OO0000OO )#line:113
    def sealing (O0OOOOO0O0O0OO0O0 ):#line:116
        try :#line:117
            OOOO0OO0O000OO0O0 =f'__{timi_new()}'#line:118
            OOO0O00000O000O00 ={'authorization':O0OOOOO0O0O0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO0O000OO0O0 ),'signstring':OOOO0OO0O000OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO0O00000O000O00 )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =OOO0O00000O000O00 )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO0O00000O000O00 )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO0O00000O000O00 )#line:131
            requests .request ('get',f'{host}/user',headers =OOO0O00000O000O00 )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO0O00000O000O00 )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO0O00000O000O00 )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO0O00000O000O00 )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =OOO0O00000O000O00 )#line:136
            requests .request ('get',f'{host}/assets',headers =OOO0O00000O000O00 )#line:137
        except Exception as OOOO00O000OO00OOO :#line:138
            print (OOOO00O000OO00OOO )#line:139
    def withdraw (O0O0000O0O0OO00O0 ):#line:143
        OOOO000O0O0O0OOO0 =f'__{timi_new()}'#line:144
        O0O0000OOOOO0000O ={'authorization':O0O0000O0O0OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O0O0O0OOO0 ),'signstring':OOOO000O0O0O0OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        O0O0O0OO0OO00OOOO =requests .request ('get',f'{host}/assets',headers =O0O0000OOOOO0000O ).json ()#line:154
        if 'status'in O0O0O0OO0OO00OOOO :#line:156
            if O0O0O0OO0OO00OOOO ['status']==200 :#line:157
                OO0OOO00O0OOO0O00 =O0O0O0OO0OO00OOOO ['data']['cash']#line:158
                if float (OO0OOO00O0OOO0O00 )>20 :#line:159
                    OOOO000O0O0O0OOO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    O0O0000OOOOO0000O ={'authorization':O0O0000O0O0OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O0O0O0OOO0 ),'signstring':OOOO000O0O0O0OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    OO000OOOOOOO0OOOO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    O00OOO00000O00000 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O0000OOOOO0000O ,data =OO000OOOOOOO0OOOO ).json ()#line:172
                    print (O00OOO00000O00000 )#line:173
    def invitenum (O0OOO0000O0O0000O ):#line:176
        OO0O0OOOO0O00OOOO =f'__{timi_new()}'#line:177
        OOOOOOO00OOOO00OO ={'authorization':O0OOO0000O0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOOO0O00OOOO ),'signstring':OO0O0OOOO0O00OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O0OO0O000OOOOO0O0 =requests .request ('get',f'{host}/invite/invitenum',headers =OOOOOOO00OOOO00OO ).json ()#line:187
        if 'status'in O0OO0O000OOOOO0O0 :#line:189
            if O0OO0O000OOOOO0O0 ['status']==200 :#line:190
                OO00OO00OOO00000O =O0OO0O000OOOOO0O0 ['data']['invited_count']#line:191
                O000O0O00OOOOO0OO =O0OO0O000OOOOO0O0 ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OO00OO00OOO00000O}丨间邀好友:{O000O0O00OOOOO0OO}')#line:193
    def game_map (O0000OOO00OO00OOO ):#line:196
        try :#line:197
            OO0O0OO0OOO00OO0O =f'__{timi_new()}'#line:198
            OO00000OO000OO00O ={'authorization':O0000OOO00OO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO0OOO00OO0O ),'signstring':OO0O0OO0OOO00OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            OO0O0OOOO000OOOOO =requests .request ('get',f'{host}/game/map',headers =OO00000OO000OO00O ).json ()#line:208
            if 'status'in OO0O0OOOO000OOOOO :#line:210
                if OO0O0OOOO000OOOOO ['status']==200 :#line:211
                    for OOO0O0OOO00000OOO in OO0O0OOOO000OOOOO ['data']['list'][0 ]['crops']:#line:212
                        O0OO0000O0O00OOOO =OOO0O0OOO00000OOO ['level']#line:214
                        if O0OO0000O0O00OOOO ==41 :#line:215
                            O0OO00000O0OOO0OO =OOO0O0OOO00000OOO ['crop_name']#line:216
                            OOOOOOOO0OO0O00O0 =OOO0O0OOO00000OOO ['count']#line:217
                            if OOOOOOOO0OO0O00O0 >0 :#line:218
                                print (f'【农业资产】:{O0OO00000O0OOO0OO}丨数量:{OOOOOOOO0OO0O00O0}')#line:219
        except Exception as O0O000000OOO0OOO0 :#line:220
            print (O0O000000OOO0OOO0 )#line:221
    def give_gold (O0O0OO00O0O0000O0 ):#line:224
        try :#line:225
            O0OO0O00O00O000OO =f'__{timi_new()}'#line:226
            O0O00OO000O00O0OO ={'authorization':O0O0OO00O0O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O00O000OO ),'signstring':O0OO0O00O00O000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            O0O000000O0OOOOOO =requests .request ('get',f'{host}/user',headers =O0O00OO000O00O0OO ).json ()#line:236
            if 'status'in O0O000000O0OOOOOO :#line:237
                if O0O000000O0OOOOOO ['status']==200 :#line:238
                    if float (O0O0OO00O0O0000O0 .doneeNo )!=0 :#line:239
                        O00OOO0O000000O00 =O0O000000O0OOOOOO ['data']['assets']['gold']#line:240
                        if float (O00OOO0O000000O00 )>float (O0O0OO00O0O0000O0 .innerId ):#line:241
                            OOO0O00OO0O0OOO0O =int (float (O00OOO0O000000O00 )/1.1 )#line:242
                            O0OO0O00O00O000OO =f'_doneeNo={O0O0OO00O0O0000O0.doneeNo}&quantity={OOO0O00OO0O0OOO0O}_{timi_new()}'#line:243
                            O0O00OO000O00O0OO ={'authorization':O0O0OO00O0O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O00O000OO ),'signstring':O0OO0O00O00O000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            O0OO00OO0OO0O0O0O ={"quantity":OOO0O00OO0O0OOO0O ,"doneeNo":O0O0OO00O0O0000O0 .doneeNo }#line:256
                            O0O0O0OO0000O00OO =requests .request ('post',f'{host}/finance/give-gold',headers =O0O00OO000O00O0OO ,data =O0OO00OO0OO0O0O0O ).json ()#line:257
                            if 'status'in O0O0O0OO0000O00OO :#line:259
                                if O0O0O0OO0000O00OO ['status']==200 :#line:260
                                    if O0O0O0OO0000O00OO ['data']:#line:261
                                        print (f'【赠送种子】:赠送{OOO0O00OO0O0OOO0O}种子给{O0O0OO00O0O0000O0.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as O0000O00O00OO000O :#line:265
            print (O0000O00O00OO000O )#line:266
    def invitation (OOO0O00O00OO00OOO ):#line:268
        try :#line:269
            _O0O000O0O00OOO0OO =float (bundled_def ())/4 #line:270
            OOO0O0OO000OO000O =f'_innerId={int(_O0O000O0O00OOO0OO)}_{timi_new()}'#line:271
            O0OO0000000O000OO ={'authorization':OOO0O00O00OO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO000OO000O ),'signstring':OOO0O0OO000OO000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            OOO0O0OO00O0OO00O ={"innerId":int (_O0O000O0O00OOO0OO )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0OO0000000O000OO ,data =OOO0O0OO00O0OO00O )#line:282
        except Exception as OO0O0OOOOO0OO0O00 :#line:283
            print (OO0O0OOOOO0OO0O00 )#line:284
    def winning_rewards (O00O0OOO0000OOOOO ):#line:287
        try :#line:288
            OO0O00O0OO0000O00 =f'__{timi_new()}'#line:289
            O000000OOO0000OOO ={'authorization':O00O0OOO0000OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O0OO0000O00 ),'signstring':OO0O00O0OO0000O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            OO00O0OOO00O0O000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O000000OOO0000OOO ).json ()#line:299
            if 'status'in OO00O0OOO00O0O000 :#line:301
                if OO00O0OOO00O0O000 ['status']==200 :#line:302
                    if OO00O0OOO00O0O000 ['data']['amount']:#line:303
                        OO0OO0OOO0OOOOOOO =OO00O0OOO00O0O000 ['data']['amount']['gold']#line:304
                        return OO0OO0OOO0OOOOOOO #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as O000OO0O00OO000OO :#line:308
            print (O000OO0O00OO000OO )#line:309
    def certification (OO0O00O0O0OO0OO00 ):#line:312
        try :#line:313
            OOOOO0O00OO0O0000 =f'__{timi_new()}'#line:314
            O0OOO00O0OO0O00OO ={'authorization':OO0O00O0O0OO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O00OO0O0000 ),'signstring':OOOOO0O00OO0O0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            O0O0O0OO00O00O00O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0OOO00O0OO0O00OO ).json ()#line:324
            if 'status'in O0O0O0OO00O00O00O :#line:326
                if O0O0O0OO00O00O00O ['status']==200 :#line:327
                    if O0O0O0OO00O00O00O ['data']['result']:#line:328
                        OO0O0O0OOO00O0O0O =O0O0O0OO00O00O00O ['data']['nick_name']#line:329
                        return OO0O0O0OOO00O0O0O #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as O0OO0000OOOOOOOOO :#line:333
            print (O0OO0000OOOOOOOOO )#line:334
    def crops_illustrated (O0000OOOOO0O0O00O ):#line:337
        try :#line:338
            O0O0O00O0O0OO0000 =f'__{timi_new()}'#line:339
            O0OOO0O00000OO00O ={'authorization':O0000OOOOO0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00O0O0OO0000 ),'signstring':O0O0O00O0O0OO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            OO000OO00000O0000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OOO0O00000OO00O ).json ()#line:349
            if 'status'in OO000OO00000O0000 :#line:351
                if OO000OO00000O0000 ['status']==200 :#line:352
                    O0OO0O00O0O0O0000 =OO000OO00000O0000 ['data'][0 ]['crops']#line:353
                    for O00OOO00OOOOOOO00 in O0OO0O00O0O0O0000 :#line:354
                        if O00OOO00OOOOOOO00 ['ill_clover_award']:#line:355
                            if float (O00OOO00OOOOOOO00 ['ill_clover_award'])>1 :#line:356
                                if O00OOO00OOOOOOO00 ['is_finish']:#line:357
                                    if not O00OOO00OOOOOOO00 ['is_getit']:#line:358
                                        if O0000OOOOO0O0O00O .certification ()!='未实名':#line:359
                                            O0O0O00O0O0OO0000 =f'_award_level={O00OOO00OOOOOOO00["level"]}_{timi_new()}'#line:360
                                            O0OOO0O00000OO00O ={'authorization':O0000OOOOO0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00O0O0OO0000 ),'signstring':O0O0O00O0O0OO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            O00O00OO0OO0OO0O0 ={"award_level":O00OOO00OOOOOOO00 ['level']}#line:370
                                            O0O0O0OOO000O0000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OOO0O00000OO00O ,json =O00O00OO0OO0OO0O0 ).json ()#line:372
                                            if 'status'in O0O0O0OOO000O0000 :#line:373
                                                if O0O0O0OOO000O0000 ['status']==200 :#line:374
                                                    OOO000O000O0O00O0 =O0O0O0OOO000O0000 ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{O00OOO00OOOOOOO00["crop_name"]}成就丨奖励{OOO000O000O0O00O0}☘️')#line:377
                                                if O0O0O0OOO000O0000 ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{O0O0O0OOO000O0000["message"]}')#line:379
        except Exception as OO0OO0O00O0O0O0OO :#line:380
            print (OO0OO0O00O0O0O0OO )#line:381
    def watched_ad (O0O0000OOOO00OOOO ):#line:384
        try :#line:385
            OO00O0O000OOOO00O =f'__{timi_new()}'#line:386
            OO000O0O00000000O ={'authorization':O0O0000OOOO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O000OOOO00O ),'signstring':OO00O0O000OOOO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            O0O0O0OO000000000 =requests .request ('get',f'{host}/game/getAllData',headers =OO000O0O00000000O ).json ()#line:396
            if 'status'in O0O0O0OO000000000 :#line:398
                if O0O0O0OO000000000 ['status']==200 :#line:399
                    if 'offlineInfo'in O0O0O0OO000000000 ['data']:#line:400
                        time .sleep (random .randint (16 ,18 ))#line:401
                        OOO0O0O0OOO0000O0 =O0O0O0OO000000000 ['data']['offlineInfo']['off_minute']#line:402
                        OO0O00OOOOOO00OOO =float (O0O0O0OO000000000 ['data']['silver'])/1000000000000 #line:403
                        time .sleep (1 )#line:404
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO000O0O00000000O ).json ()#line:405
                        time .sleep (2 )#line:406
                        OOOOO0OOO0OO0000O =requests .request ('get',f'{host}/game/getAllData',headers =OO000O0O00000000O ).json ()#line:407
                        if 'status'in OOOOO0OOO0OO0000O :#line:409
                            if OOOOO0OOO0OO0000O ['status']==200 :#line:410
                                OO0OOOO0OO00OOOO0 =float (OOOOO0OOO0OO0000O ['data']['silver'])/1000000000000 #line:411
                                O0O00OOO0000O0O00 =str (OO0OOOO0OO00OOOO0 -OO0O00OOOOOO00OOO )[:6 ]#line:412
                                print (f'【离线奖励】:翻倍离线{OOO0O0O0OOO0000O0}分钟奖励🌱数量:{O0O00OOO0000O0O00}t粒')#line:413
        except Exception as O00OOO0O0OOO0O0O0 :#line:414
            print (O00OOO0O0OOO0O0O0 )#line:415
    def user_ad (OOO0O00O000000OO0 ):#line:418
        try :#line:419
            O0O0OO0O0OO00O0O0 =f'__{timi_new()}'#line:420
            O00000O0O000OOO00 ={'authorization':OOO0O00O000000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0OO00O0O0 ),'signstring':O0O0OO0O0OO00O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:429
            OO0O00O000O00O0O0 =requests .request ('get',f'{host}/user/ad',headers =O00000O0O000OOO00 ).json ()#line:430
            if 'status'in OO0O00O000O00O0O0 :#line:432
                if OO0O00O000O00O0O0 ['status']==200 :#line:433
                    O00OO0OOO0O00OOOO =OO0O00O000O00O0O0 ['data']['max_time']#line:434
                    OOOOOO00OO0OOOO00 =OO0O00O000O00O0O0 ['data']['watch_time']#line:435
                    O0OOO0O0OO0OOOO00 =OO0O00O000O00O0O0 ['data']['added_time']#line:436
                    print (f'【获取种子】:获取🌱剩余{O0OOO0O0OO0OOOO00 + O00OO0OOO0O00OOOO - OOOOOO00OO0OOOO00}次丨好友提供:{O0OOO0O0OO0OOOO00}次')#line:437
                    if O0OOO0O0OO0OOOO00 +O00OO0OOO0O00OOOO -OOOOOO00OO0OOOO00 >0 :#line:438
                        time .sleep (random .randint (16 ,19 ))#line:439
                        OO0OOO0O00OOO0OO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00000O0O000OOO00 ).json ()#line:440
                        if 'status'in OO0OOO0O00OOO0OO0 :#line:442
                            if OO0OOO0O00OOO0OO0 ['status']==200 :#line:443
                                OO0000OOOO00O0O0O =float (OO0OOO0O00OOO0OO0 ['data']['silver'])/1000000000000 #line:444
                                print (f'【获取种子】:获得🌱:{int(OO0000OOOO00O0O0O)}t粒')#line:445
                                return True #line:446
                            if OO0OOO0O00OOO0OO0 ['status']==500 :#line:447
                                OO000O00OO0OO0O0O =OO0OOO0O00OOO0OO0 ['message']#line:448
                                print (f'【获取种子】:{OO000O00OO0OO0O0O}')#line:449
                                return False #line:450
        except Exception as O0000OO0OO0OO0OOO :#line:451
            print (O0000OO0OO0OO0OOO )#line:452
    def synthetic (O0O000OO0O000O00O ):#line:455
        global id ,g #line:456
        try :#line:457
            OOOOO0O00000O0000 =O0O000OO0O000O00O .level_new ()#line:458
            O0OO000OOO000O000 =random .randint (9 ,11 )#line:459
            OO0O00OOOOO00O0O0 =f'_site=8&targetSite={O0OO000OOO000O000}_{timi_new()}'#line:460
            O0O0O0OOO0OO0O000 ={'accept':'application/json, text/plain, */*','authorization':O0O000OO0O000O00O .token ,'timestamp':timi_new (),'sign':sign (OO0O00OOOOO00O0O0 ),'signstring':OO0O00OOOOO00O0O0 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:475
            O00OOO0OOOO00OO00 ={"site":int (8 ),"targetSite":int (O0OO000OOO000O000 )}#line:476
            requests .request ('post',f'{host}/game/crops/move',headers =O0O0O0OOO0OO0O000 ,json =O00OOO0OOOO00OO00 )#line:477
            while True :#line:478
                OO000O0OO000OOOOO =f'__{timi_new()}'#line:479
                OOOO000O0OOO00O00 ={'authorization':O0O000OO0O000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0OO000OOOOO ),'signstring':OO000O0OO000OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                OO000OO0OO0000OO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO000O0OOO00O00 ).json ()#line:489
                if 'status'in OO000OO0OO0000OO0 :#line:491
                    if OO000OO0OO0000OO0 ['status']==200 :#line:492
                        OOOOOO00O00O0OOOO =OO000OO0OO0000OO0 ['data']['cropList']#line:493
                        OOO0OOOO0000OO0O0 =OO000OO0OO0000OO0 ['data']['gameCoreDataDBid']#line:494
                        O0OOO0O000O000000 =float (OO000OO0OO0000OO0 ['data']['silver'])/1000000000000 #line:495
                        OO000O00O0OOO000O =0 #line:500
                        for O0OO0OOO000OOO0OO in OOOOOO00O00O0OOOO :#line:501
                            if not O0OO0OOO000OOO0OO :#line:502
                                O00OO0O0000O0O00O =f'_crop_id={OOO0OOOO0000OO0O0}&site={OO000O00O0OOO000O}_{O0O000OO0O000O00O.time}'#line:503
                                O0000O0O00O0OO0OO ={'authorization':O0O000OO0O000O00O .token ,'timestamp':O0O000OO0O000O00O .time ,'sign':sign (O00OO0O0000O0O00O ),'signstring':O00OO0O0000O0O00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
                                O00O0000000O0O0OO ={"site":OO000O00O0OOO000O ,"crop_id":OOO0OOOO0000OO0O0 }#line:513
                                OOO0O00OO000OO0O0 =requests .request ('post',f'{host}/game/crops/buy',headers =O0000O0O00O0OO0OO ,data =O00O0000000O0O0OO ).json ()#line:514
                                time .sleep (random .randint (1 ,3 )/10 )#line:516
                                if 'status'in OOO0O00OO000OO0O0 :#line:517
                                    if OOO0O00OO000OO0O0 ['status']==200 :#line:518
                                        if OOO0O00OO000OO0O0 ['message']=='种子数量不足':#line:519
                                            OOOOO0O00000O0000 =O0O000OO0O000O00O .level_new ()#line:520
                                            print (f'【种植合成】:{OOO0O00OO000OO0O0["message"]}')#line:521
                                            if not O0O000OO0O000O00O .user_ad ():#line:522
                                                return False #line:523
                                    if OOO0O00OO000OO0O0 ['status']==500 :#line:524
                                        print (f'【种植合成】:{OOO0O00OO000OO0O0["message"]}')#line:525
                                        return False #line:526
                            OO000O00O0OOO000O +=1 #line:527
                        O0000000OOO0O0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO000O0OOO00O00 ).json ()#line:528
                        O0OOO000OOOO00O0O =O0000000OOO0O0OO0 ['data']['cropList']#line:529
                        O0O0O0OO000O0O000 =False #line:530
                        for O0OO0OOO000OOO0OO in range (12 ):#line:531
                            id =O0OOO000OOOO00O0O [O0OO0OOO000OOO0OO ]['level']#line:532
                            if float (OOOOO0O00000O0000 )-float (id )>9 :#line:533
                                OO0O0O0O0OOOOO0OO =f'_site={O0OO0OOO000OOO0OO}_{timi_new()}'#line:534
                                OOO0OOOOO00OO0000 ={'accept':'application/json, text/plain, */*','authorization':O0O000OO0O000O00O .token ,'timestamp':timi_new (),'sign':sign (OO0O0O0O0OOOOO0OO ),'signstring':OO0O0O0O0OOOOO0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:544
                                O0O00OOOO0OOOOOOO ={"site":O0OO0OOO000OOO0OO }#line:545
                                OO0O0OO000OOOOO0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO0OOOOO00OO0000 ,data =O0O00OOOO0OOOOOOO ).json ()#line:547
                                if 'status'in OO0O0OO000OOOOO0O :#line:548
                                    if OO0O0OO000OOOOO0O ['status']==200 :#line:549
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:550
                            if id !=0 :#line:551
                                for OOOO0000OOO000OO0 in range (11 ):#line:552
                                    OO000000O0O0OOOO0 =OOOO0000OOO000OO0 +1 #line:553
                                    g =O0OOO000OOOO00O0O [OO000000O0O0OOOO0 ]['level']#line:554
                                    if id ==g :#line:555
                                        O0O0OOO0000OO00O0 =OOOO0000OOO000OO0 +2 #line:556
                                        if O0O0OOO0000OO00O0 !=O0OO0OOO000OOO0OO +1 :#line:557
                                            OO0OOO0O0OO00O00O =O0OO0OOO000OOO0OO +1 #line:558
                                            time .sleep (random .randint (1 ,3 )/10 )#line:560
                                            OO0O00OOOOO00O0O0 =f'_site={OO0OOO0O0OO00O00O - 1}&targetSite={O0O0OOO0000OO00O0 - 1}_{timi_new()}'#line:561
                                            O0O0O0OOO0OO0O000 ={'accept':'application/json, text/plain, */*','authorization':O0O000OO0O000O00O .token ,'timestamp':timi_new (),'sign':sign (OO0O00OOOOO00O0O0 ),'signstring':OO0O00OOOOO00O0O0 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:576
                                            O0OOO00OOOO00O00O ={"site":int (OO0OOO0O0OO00O00O -1 ),"targetSite":int (O0O0OOO0000OO00O0 -1 )}#line:577
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0O0O0OOO0OO0O000 ,json =O0OOO00OOOO00O00O )#line:578
                                            print (f'【种植合成】:位置{OO0OOO0O0OO00O00O}和位置{O0O0OOO0000OO00O0}合出{int(id) + 1}级农作物')#line:579
                                            O0O0O0OO000O0O000 =True #line:580
                                    if O0O0O0OO000O0O000 :#line:581
                                        break #line:582
                                if O0O0O0OO000O0O000 :#line:583
                                    break #line:584
        except :#line:585
            O0O000OO0O000O00O .synthetic ()#line:586
    def level_new (OO00OO0O0O0000000 ):#line:589
        try :#line:590
            OOOOO00O0OO0O00O0 =f'__{timi_new()}'#line:591
            O0O0OOOOO0O0O0OO0 ={'authorization':OO00OO0O0O0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0OO0O00O0 ),'signstring':OOOOO00O0OO0O00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            O0O0O0OOOOO00OO0O =requests .request ('get',f'{host}/user',headers =O0O0OOOOO0O0O0OO0 ).json ()#line:601
            if 'status'in O0O0O0OOOOO00OO0O :#line:602
                if O0O0O0OOOOO00OO0O ['status']==200 :#line:603
                    return float (O0O0O0OOOOO00OO0O ['data']['level'])#line:604
        except Exception as O0OOOOOOOO0OOO0OO :#line:605
            print (O0OOOOOOOO0OOO0OO )#line:606
    def propsraffle (OO0000O000OOO000O ):#line:609
        try :#line:610
            while True :#line:611
                O00OO0O00000O00O0 =f'__{timi_new()}'#line:612
                O00OO00OO0OOOOOO0 ={'authorization':OO0000O000OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O00000O00O0 ),'signstring':O00OO0O00000O00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:621
                O0O0O00OO00O000O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00OO00OO0OOOOOO0 ).json ()#line:622
                if 'status'in O0O0O00OO00O000O0 :#line:624
                    if O0O0O00OO00O000O0 ['status']==200 :#line:625
                        OO0OO000000OOOO00 =O0O0O00OO00O000O0 ['data']['rows']#line:626
                        O0OO000OOOOOO00OO =O0O0O00OO00O000O0 ['data']['vstate']#line:627
                        if OO0OO000000OOOO00 ==5 or OO0OO000000OOOO00 ==6 or OO0OO000000OOOO00 ==7 :#line:628
                            OO0O00OO0OOO0OOOO =O0O0O00OO00O000O0 ['data']['silver']#line:629
                            print (f'【转盘抽奖】:获得种子:{OO0O00OO0OOO0OOOO}')#line:630
                        if OO0OO000000OOOO00 ==1 or OO0OO000000OOOO00 ==2 or OO0OO000000OOOO00 ==3 :#line:631
                            OOOO00O0OOO000OOO =O0O0O00OO00O000O0 ['data']['clover']#line:632
                            print (f'【转盘抽奖】:获得三叶草:{OOOO00O0OOO000OOO}')#line:633
                        if OO0OO000000OOOO00 ==4 or OO0OO000000OOOO00 ==8 :#line:634
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:635
                        if OO0OO000000OOOO00 =='抽奖次数已用完':#line:639
                            break #line:672
                time .sleep (random .randint (8 ,15 )/10 )#line:673
        except Exception as O000O0OO000O0OO00 :#line:674
            print (O000O0OO000O0OO00 )#line:675
    def friends_invitation (OO0O0000O000O00O0 ):#line:678
        try :#line:679
            OOOOOOOOOO0OO00OO =f'__{timi_new()}'#line:680
            O00O0O0OO00OOO0OO ={'authorization':OO0O0000O000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOOOO0OO00OO ),'signstring':OOOOOOOOOO0OO00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:689
            O000OO0OOO00OOO00 =requests .request ('get',f'{host}/friends',headers =O00O0O0OO00OOO0OO ).json ()#line:690
            if 'status'in O000OO0OOO00OOO00 :#line:691
                if O000OO0OOO00OOO00 ['status']==200 :#line:692
                    OO000OOO00OOOO0OO =O000OO0OOO00OOO00 ['data']['myInviteter']#line:693
                    if OO000OOO00OOOO0OO :#line:694
                        O00O000OOOO00O000 =OO000OOO00OOOO0OO ['user']['nickname']#line:695
                        OOO00OOO00O0OOOOO =OO0O0000O000O00O0 .certification ()#line:696
                        print (f'【查邀请人】:我的邀请人:{O00O000OOOO00O000}丨实名:{OOO00OOO00O0OOOOO}')#line:697
                    else :#line:698
                        if OO0O0000O000O00O0 .innerId !='0':#line:699
                            OO0O0000O000O00O0 .invitation ()#line:700
        except Exception as OOOOOO0OO0OOO00O0 :#line:701
            print (OOOOOO0OO0OOO00O0 )#line:702
    def add_clover (O0OOO000O0OO0O000 ):#line:705
        global golden_seed #line:706
        try :#line:707
            OOO00000OOO00OO0O =f'__{timi_new()}'#line:708
            O000O0O00O000OOOO ={'authorization':O0OOO000O0OO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00000OOO00OO0O ),'signstring':OOO00000OOO00OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:717
            OO0OOO0000OO00OO0 =requests .request ('get',f'{host}/assets/clovers',headers =O000O0O00O000OOOO ).json ()#line:718
            if 'status'in OO0OOO0000OO00OO0 :#line:720
                if OO0OOO0000OO00OO0 ['status']==200 :#line:721
                    O00000OOOO0OOOO0O =OO0OOO0000OO00OO0 ['data']['clover']#line:722
                    O0O0O00O0O000OO0O =OO0OOO0000OO00OO0 ['data']['used_clover']#line:723
                    O0OOO00O0OO00O0O0 =float (O00000OOOO0OOOO0O )-float (O0O0O00O0O000OO0O )#line:724
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0O0O00O0O000OO0O}')#line:725
                    if O0OOO000O0OO0O000 .certification ()!='未实名':#line:726
                        if O0OOO00O0OO00O0O0 >1 :#line:727
                            OOO00000OOO00OO0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OOO00O0OO00O0O0)}_{timi_new()}'#line:728
                            OO0OOO0OO000O0O0O ={'authorization':O0OOO000O0OO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00000OOO00OO0O ),'signstring':OOO00000OOO00OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                            OO0000OOOOO0OO0OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OOO00O0OO00O0O0 )}#line:738
                            O0OO0O0000000O0O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0OOO0OO000O0O0O ,data =OO0000OOOOO0OO0OO ).json ()#line:739
                            if 'status'in O0OO0O0000000O0O0 :#line:741
                                if O0OO0O0000000O0O0 ['status']==200 :#line:742
                                    print (f'【参与抽奖】:添加☘️:{O0OO0O0000000O0O0["data"]}丨数量:{O0OOO00O0OO00O0O0}')#line:743
                                if O0OO0O0000000O0O0 ['status']==500 :#line:744
                                    print (f'【参与抽奖】:添加☘️:{O0OO0O0000000O0O0["message"]}')#line:745
            OO0OOO000000OOO0O =requests .request ('get',f'{host}/lottery',headers =O000O0O00O000OOOO ).json ()#line:746
            OO0O000O00OOO0O00 =O0OOO000O0OO0O000 .winning_rewards ()#line:748
            if 'status'in OO0OOO000000OOO0O :#line:749
                if OO0OOO000000OOO0O ['status']==200 :#line:750
                    O0OOOO0OOO0O0OO00 =OO0OOO000000OOO0O ['data'][0 ]['day_get_gold_quantity']#line:751
                    golden_seed +=float (O0OOOO0OOO0O0OO00 )#line:752
                    O0O0OOOO00OOOO0OO =OO0OOO000000OOO0O ['data'][1 ]['value']#line:753
                    OOOO0OOOOO000O0O0 =OO0OOO000000OOO0O ['data'][0 ]['join_number']#line:754
                    OOO0O0OOOO00O0O00 =int (float (OO0OOO000000OOO0O ['data'][0 ]['totalValue']))#line:755
                    OOO0OOO0O00O0O0OO =float (O0O0OOOO00OOOO0OO /OOO0O0OOOO00O0O00 )*10000 #line:756
                    O0000O0OO00000000 =OOO0O0OOOO00O0O00 /OOOO0OOOOO000O0O0 #line:757
                    print (f'【参与抽奖】:预计每天中{str(O0OOOO0OOO0O0OO00)[:6]}颗金种子丨好友收益:{str(OO0O000O00OOO0O00)[:6]}')#line:758
                    print (f'【抽奖统计】:每1万☘️中{str(OOO0OOO0O00O0O0OO)[:6]}颗金种子丨☘️人均:{str(O0000O0OO00000000)[:7]}️')#line:759
        except Exception as OOOO0OOO00O00OOO0 :#line:760
            print (OOOO0OOO00O00OOO0 )#line:761
    def energy (OO0OO0O000O0O0000 ):#line:765
        try :#line:766
            while True :#line:767
                O00OOOO0000O000O0 =f'__{timi_new()}'#line:768
                OO0000OOOO0OOOOO0 ={'authorization':OO0OO0O000O0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0000O000O0 ),'signstring':O00OOOO0000O000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:777
                O000O00O000OO0O00 =requests .request ('get',f'{host}/energy/general',headers =OO0000OOOO0OOOOO0 ).json ()#line:778
                if 'status'in O000O00O000OO0O00 :#line:780
                    if O000O00O000OO0O00 ['status']==200 :#line:781
                        OOO000O0OOOOOO0OO =O000O00O000OO0O00 ['data']['ordinary_water']#line:782
                        O00OO0O0OO0O0O0O0 =O000O00O000OO0O00 ['data']['ordinary_fertilizer']#line:783
                        print (f'【我的营养】:肥料:{str(O00OO0O0OO0O0O0O0).split(".")[0]}丨水滴:{str(OOO000O0OOOOOO0OO).split(".")[0]}')#line:785
                        if float (O00OO0O0OO0O0O0O0 )<96 :#line:786
                            time .sleep (random .randint (160 ,180 )/10 )#line:787
                            O0O00O00OOO0O00O0 =99 -float (O00OO0O0OO0O0O0O0 )#line:788
                            OO00OOO00OO0O000O ={"fertilizer":str (O0O00O00OOO0O00O0 ).split ('.')[0 ]}#line:789
                            OOOOO00O0O0OOOO00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0000OOOO0OOOOO0 ).json ()#line:790
                            if 'status'in OOOOO00O0O0OOOO00 :#line:792
                                if OOOOO00O0O0OOOO00 ['status']==200 :#line:793
                                    print (f'【购买肥料】:看广告获取肥料:{OOOOO00O0O0OOOO00["message"]}')#line:794
                        if float (OOO000O0OOOOOO0OO )<880 :#line:795
                            time .sleep (random .randint (160 ,180 )/10 )#line:796
                            O0O0O0000O0O000O0 =999 -float (OOO000O0OOOOOO0OO )#line:797
                            OO0O0O0000OOO0OOO ={"water":str (O0O0O0000O0O000O0 ).split ('.')[0 ]}#line:798
                            O0OOO00O0000O00OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0000OOOO0OOOOO0 ).json ()#line:799
                            if 'status'in O0OOO00O0000O00OO :#line:801
                                if O0OOO00O0000O00OO ['status']==200 :#line:802
                                    print (f'【购买水滴】:看广告获取水滴:{O0OOO00O0000O00OO["message"]}')#line:803
                        if float (O00OO0O0OO0O0O0O0 )>96 and float (OOO000O0OOOOOO0OO )>880 :#line:804
                            break #line:805
        except Exception as OO0OOOO0OOOO0OOO0 :#line:807
            print (OO0OOOO0OOOO0OOO0 )#line:808
def bundled_def ():#line:810
    OO0000OOOO00OO000 =['5570536','7750212','7911652','7911680','7805624']#line:811
    return OO0000OOOO00OO000 [random .randint (0 ,len (OO0000OOOO00OO000 )-1 )]#line:812
def version_of_the_validation ():#line:816
    return str ((78 -56 )/10 )#line:817
def gitee_validation ():#line:820
    try :#line:821
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:822
    except :#line:823
        sys .exit (0 )#line:824
def update_the_validation ():#line:828
    try :#line:829
        OOOO00O0OOOOO000O =gitee_validation ()#line:830
        if version_of_the_validation ()<OOOO00O0OOOOO000O ['CityEarth']['edition']:#line:831
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO00O0OOOOO000O["CityEarth"]["edition"]}   ❌')#line:832
            print (f'更新内容=>>{OOOO00O0OOOOO000O["CityEarth"]["content"]}   🎉')#line:833
        else :#line:834
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO00O0OOOOO000O["CityEarth"]["edition"]}   ✅')#line:835
            print (f'更新内容=>> {OOOO00O0OOOOO000O["CityEarth"]["content"]}   🎉')#line:836
    except Exception as OOO00OO000O0O00O0 :#line:837
        print (OOO00OO000O0O00O0 )#line:838
def os_qinglong ():#line:841
    if application in os .environ :#line:842
        O0O0000OOOO00O000 =os .environ [application ].split ('\n')#line:843
        if len (O0O0000OOOO00O000 )>0 :#line:844
            return O0O0000OOOO00O000 #line:845
        else :#line:846
            print (f"{application}变量未启用")#line:847
            print ('脚本退出')#line:848
            sys .exit (1 )#line:849
    else :#line:850
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:852
        return os_built ()#line:853
def os_built ():#line:856
    if token :#line:857
        OOO00O00O000O0OOO =token .split ('\n')#line:858
        if len (OOO00O00O000O0OOO )>0 :#line:859
            return OOO00O00O000O0OOO #line:860
    else :#line:861
        print (f"内置变量为空")#line:862
        print ('脚本结束')#line:863
        sys .exit (0 )#line:864
if __name__ =='__main__':#line:867
    start ()#line:868
