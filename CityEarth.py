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
        OO0OO00000O0000OO =os_qinglong ()#line:10
        print (f"==========共找到{len(OO0OO00000O0000OO)}个账号==========")#line:11
        for OOOO0OO0O0000O000 in OO0OO00000O0000OO :#line:12
            OO0OO0O0O0000O0O0 =[]#line:13
            print (f"------------正在执行第{OO0OO00000O0000OO.index(OOOO0OO0O0000O000) + 1}个账号------------")#line:14
            OO0000OO0O0O0OOOO =CityEarth (OOOO0OO0O0000O000 ,OO0OO0O0O0000O0O0 )#line:15
            def OOOOOOO00OOO000O0 ():#line:17
                if OO0000OO0O0O0OOOO .base_info ():#line:19
                    OO0000OO0O0O0OOOO .sealing ()#line:21
                    OO0000OO0O0O0OOOO .invitenum ()#line:23
                    OO0000OO0O0O0OOOO .game_map ()#line:25
                    OO0000OO0O0O0OOOO .friends_invitation ()#line:27
                    OO0000OO0O0O0OOOO .add_clover ()#line:29
                    OO0000OO0O0O0OOOO .propsraffle ()#line:31
                    OO0000OO0O0O0OOOO .synthetic ()#line:33
                    OO0000OO0O0O0OOOO .crops_illustrated ()#line:35
                    OO0000OO0O0O0OOOO .give_gold ()#line:37
                    OO0000OO0O0O0OOOO .withdraw ()#line:39
                    OO0000OO0O0O0OOOO .energy ()#line:41
            O0O0OOOOO0OOOO00O =threading .Thread (target =OOOOOOO00OOO000O0 )#line:42
            O0O0OOOOO0OOOO00O .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        OOO00O0000O000000 =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOO00O0000O000000 +' ')#line:48
    except Exception as OOOOO00OO00O000O0 :#line:49
        print (OOOOO00OO00O000O0 )#line:50
def sign (OOOOO0O00O00OO0O0 ):#line:53
    OO00O0OO0OOO0OOO0 =hashlib .md5 (OOOOO0O00O00OO0O0 .encode ()).hexdigest ()#line:54
    O00O0O0000OO0OO00 ="scsc%^&*"+OO00O0OO0OOO0OOO0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    O0O00000OOO0000OO =hashlib .md5 (O00O0O0000OO0OO00 .encode ()).hexdigest ()#line:56
    return O0O00000OOO0000OO #line:57
def format_msg ():#line:59
    OOOO0OOO0000OO000 =""#line:60
    for O000OOO000O0O0OOO in msg_list :#line:61
        OOOO0OOO0000OO000 +=str (O000OOO000O0O0OOO )+"\r\n"#line:62
    return OOOO0OOO0000OO000 #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (O00OO00OOO0OOO0O0 ,O0O0O0OOOOOOOOOO0 ,OO00O0OO0O0OO00OO ):#line:71
        try :#line:72
            O00OO00OOO0OOO0O0 .msg =OO00O0OO0O0OO00OO #line:73
            O00OO00OOO0OOO0O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            O00OO00OOO0OOO0O0 .token =O0O0O0OOOOOOOOOO0 .split ('&')[0 ]#line:75
            O00OO00OOO0OOO0O0 .innerId =O0O0O0OOOOOOOOOO0 .split ('&')[1 ]#line:76
            O00OO00OOO0OOO0O0 .doneeNo =O0O0O0OOOOOOOOOO0 .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (O0O00000OO0000O00 ):#line:82
        try :#line:83
            O0O00000OO0000O00 .watched_ad ()#line:85
            OO00O0O000O00O00O =f'__{timi_new()}'#line:86
            O00OOO0O0O0000OOO ={'authorization':O0O00000OO0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O000O00O00O ),'signstring':OO00O0O000O00O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            O000OOOO0OO00OOO0 =requests .request ('get',f'{host}/user',headers =O00OOO0O0O0000OOO ).json ()#line:96
            if 'status'in O000OOOO0OO00OOO0 :#line:98
                if O000OOOO0OO00OOO0 ['status']==200 :#line:99
                    O000OOO00OO00OOOO =O000OOOO0OO00OOO0 ['data']['nickname']#line:100
                    O0OOO0O00OOOO000O =O000OOOO0OO00OOO0 ['data']['inner_id']#line:101
                    O0O00OO000O00O000 =O000OOOO0OO00OOO0 ['data']['assets']['gold']#line:102
                    O000O0OO0000O000O =O000OOOO0OO00OOO0 ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{O000OOO00OO00OOOO[:5]}丨ID:{O0OOO0O00OOOO000O}丨等级:{O000O0OO0000O000O}丨金种子:{str(O0O00OO000O00O000).split(".")[0]}')#line:104
                if O000OOOO0OO00OOO0 ['status']==401 :#line:105
                    print (O000OOOO0OO00OOO0 ['message'])#line:106
                    O0O00000OO0000O00 .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if O000OOOO0OO00OOO0 ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as O00OO00O0OOOOO0OO :#line:112
            print (O00OO00O0OOOOO0OO )#line:113
    def sealing (OOOO0OO0O000OOO00 ):#line:116
        try :#line:117
            OO0OOO00O00O0000O =f'__{timi_new()}'#line:118
            O0OO00O00O00OOO00 ={'authorization':OOOO0OO0O000OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO00O00O0000O ),'signstring':OO0OOO00O00O0000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OO00O00O00OOO00 )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =O0OO00O00O00OOO00 )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OO00O00O00OOO00 )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OO00O00O00OOO00 )#line:131
            requests .request ('get',f'{host}/user',headers =O0OO00O00O00OOO00 )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OO00O00O00OOO00 )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OO00O00O00OOO00 )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OO00O00O00OOO00 )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =O0OO00O00O00OOO00 )#line:136
            requests .request ('get',f'{host}/assets',headers =O0OO00O00O00OOO00 )#line:137
        except Exception as OO0OOOO00OO000OO0 :#line:138
            print (OO0OOOO00OO000OO0 )#line:139
    def withdraw (OO000OO000OOOOOOO ):#line:143
        OO0O0O00OO00OO0O0 =f'__{timi_new()}'#line:144
        O000O0O0O00OO0000 ={'authorization':OO000OO000OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O00OO00OO0O0 ),'signstring':OO0O0O00OO00OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        OO000OO00000O00OO =requests .request ('get',f'{host}/assets',headers =O000O0O0O00OO0000 ).json ()#line:154
        if 'status'in OO000OO00000O00OO :#line:156
            if OO000OO00000O00OO ['status']==200 :#line:157
                OOO000OO0OO00OO00 =OO000OO00000O00OO ['data']['cash']#line:158
                if float (OOO000OO0OO00OO00 )>20 :#line:159
                    OO0O0O00OO00OO0O0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    O000O0O0O00OO0000 ={'authorization':OO000OO000OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O00OO00OO0O0 ),'signstring':OO0O0O00OO00OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    O0O0OOOOO000O000O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    OOOOO0OOO00O0OOO0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O000O0O0O00OO0000 ,data =O0O0OOOOO000O000O ).json ()#line:172
                    print (OOOOO0OOO00O0OOO0 )#line:173
    def invitenum (O00OO0OOOOOO0OOOO ):#line:176
        OO000O0O00O00000O =f'__{timi_new()}'#line:177
        OO0OOOO0OOOO0O000 ={'authorization':O00OO0OOOOOO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O00O00000O ),'signstring':OO000O0O00O00000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        OO0OO000O000OOOOO =requests .request ('get',f'{host}/invite/invitenum',headers =OO0OOOO0OOOO0O000 ).json ()#line:187
        if 'status'in OO0OO000O000OOOOO :#line:189
            if OO0OO000O000OOOOO ['status']==200 :#line:190
                O00OOOOO0O0O00000 =OO0OO000O000OOOOO ['data']['invited_count']#line:191
                OOO000OOOO00O0OOO =OO0OO000O000OOOOO ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{O00OOOOO0O0O00000}丨间邀好友:{OOO000OOOO00O0OOO}')#line:193
    def game_map (O0O00OO000000OOOO ):#line:196
        try :#line:197
            OO0O00000OOO0OOOO =f'__{timi_new()}'#line:198
            OO00O0O0O0O00O00O ={'authorization':O0O00OO000000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00000OOO0OOOO ),'signstring':OO0O00000OOO0OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            O0OOO00OO0O00OOOO =requests .request ('get',f'{host}/game/map',headers =OO00O0O0O0O00O00O ).json ()#line:208
            if 'status'in O0OOO00OO0O00OOOO :#line:210
                if O0OOO00OO0O00OOOO ['status']==200 :#line:211
                    for OO0000O000OOO0O0O in O0OOO00OO0O00OOOO ['data']['list'][0 ]['crops']:#line:212
                        OOO0O0OO0OOO000O0 =OO0000O000OOO0O0O ['level']#line:214
                        if OOO0O0OO0OOO000O0 ==41 :#line:215
                            O0OO00OOOO00OO0O0 =OO0000O000OOO0O0O ['crop_name']#line:216
                            OOOO0OO000OO0OOO0 =OO0000O000OOO0O0O ['count']#line:217
                            if OOOO0OO000OO0OOO0 >0 :#line:218
                                print (f'【农业资产】:{O0OO00OOOO00OO0O0}丨数量:{OOOO0OO000OO0OOO0}')#line:219
        except Exception as OO00O00OOO0O0O000 :#line:220
            print (OO00O00OOO0O0O000 )#line:221
    def give_gold (O00O0000OOO0O00O0 ):#line:224
        try :#line:225
            O000OOO00O0O0OO0O =f'__{timi_new()}'#line:226
            O0000000OO00OO0OO ={'authorization':O00O0000OOO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO00O0O0OO0O ),'signstring':O000OOO00O0O0OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            O0O0OOO0O0OOOO000 =requests .request ('get',f'{host}/user',headers =O0000000OO00OO0OO ).json ()#line:236
            if 'status'in O0O0OOO0O0OOOO000 :#line:237
                if O0O0OOO0O0OOOO000 ['status']==200 :#line:238
                    if float (O00O0000OOO0O00O0 .doneeNo )!=0 :#line:239
                        O00000O0OOOO00OO0 =O0O0OOO0O0OOOO000 ['data']['assets']['gold']#line:240
                        if float (O00000O0OOOO00OO0 )>float (O00O0000OOO0O00O0 .innerId ):#line:241
                            O0O0000OO0O00OO00 =int (float (O00000O0OOOO00OO0 )/1.1 )#line:242
                            O000OOO00O0O0OO0O =f'_doneeNo={O00O0000OOO0O00O0.doneeNo}&quantity={O0O0000OO0O00OO00}_{timi_new()}'#line:243
                            O0000000OO00OO0OO ={'authorization':O00O0000OOO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO00O0O0OO0O ),'signstring':O000OOO00O0O0OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            OO0O00000O000OO00 ={"quantity":O0O0000OO0O00OO00 ,"doneeNo":O00O0000OOO0O00O0 .doneeNo }#line:256
                            OOOO0OOOOO0OO0000 =requests .request ('post',f'{host}/finance/give-gold',headers =O0000000OO00OO0OO ,data =OO0O00000O000OO00 ).json ()#line:257
                            if 'status'in OOOO0OOOOO0OO0000 :#line:259
                                if OOOO0OOOOO0OO0000 ['status']==200 :#line:260
                                    if OOOO0OOOOO0OO0000 ['data']:#line:261
                                        print (f'【赠送种子】:赠送{O0O0000OO0O00OO00}种子给{O00O0000OOO0O00O0.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as O0OOOOOOO0000OO0O :#line:265
            print (O0OOOOOOO0000OO0O )#line:266
    def invitation (O000O000OOO0O0OO0 ):#line:268
        try :#line:269
            _OOOO00OOOOOO0O00O =float (bundled_def ())/4 #line:270
            O0OOO0OO0O000OOO0 =f'_innerId={int(_OOOO00OOOOOO0O00O)}_{timi_new()}'#line:271
            O0000OO0OO00O000O ={'authorization':O000O000OOO0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO0O000OOO0 ),'signstring':O0OOO0OO0O000OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            OOOOOOO000OO0OO0O ={"innerId":int (_OOOO00OOOOOO0O00O )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0000OO0OO00O000O ,data =OOOOOOO000OO0OO0O )#line:282
        except Exception as OOOO000OOOOO0O0O0 :#line:283
            print (OOOO000OOOOO0O0O0 )#line:284
    def winning_rewards (OOOOO00O00OOOO0OO ):#line:287
        try :#line:288
            OOOO0000000OOOOO0 =f'__{timi_new()}'#line:289
            OO0O0OO000OO0O000 ={'authorization':OOOOO00O00OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000000OOOOO0 ),'signstring':OOOO0000000OOOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            OO0OOO00OO00OOO0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO0O0OO000OO0O000 ).json ()#line:299
            if 'status'in OO0OOO00OO00OOO0O :#line:301
                if OO0OOO00OO00OOO0O ['status']==200 :#line:302
                    if OO0OOO00OO00OOO0O ['data']['amount']:#line:303
                        OO0OOOOOO0O0O0OOO =OO0OOO00OO00OOO0O ['data']['amount']['gold']#line:304
                        return OO0OOOOOO0O0O0OOO #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as OO00OO000O00OO0O0 :#line:308
            print (OO00OO000O00OO0O0 )#line:309
    def certification (O000O0O00OO0O0OOO ):#line:312
        try :#line:313
            OOO000OOOOOO0OOOO =f'__{timi_new()}'#line:314
            O0O00OO0OOOOO0000 ={'authorization':O000O0O00OO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOOOOO0OOOO ),'signstring':OOO000OOOOOO0OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OOO0OOOO0OO000000 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0O00OO0OOOOO0000 ).json ()#line:324
            if 'status'in OOO0OOOO0OO000000 :#line:326
                if OOO0OOOO0OO000000 ['status']==200 :#line:327
                    if OOO0OOOO0OO000000 ['data']['result']:#line:328
                        OO0OO00OOOOO0OOO0 =OOO0OOOO0OO000000 ['data']['nick_name']#line:329
                        return OO0OO00OOOOO0OOO0 #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as O0OOO0OO0O0O000O0 :#line:333
            print (O0OOO0OO0O0O000O0 )#line:334
    def crops_illustrated (O0O00O0OO0OO000OO ):#line:337
        try :#line:338
            O00O00O0O0000OOO0 =f'__{timi_new()}'#line:339
            OO00O0O0O0O00OOOO ={'authorization':O0O00O0OO0OO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O0000OOO0 ),'signstring':O00O00O0O0000OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            O0OOOO0OOO0O0OO0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO00O0O0O0O00OOOO ).json ()#line:349
            if 'status'in O0OOOO0OOO0O0OO0O :#line:351
                if O0OOOO0OOO0O0OO0O ['status']==200 :#line:352
                    OOOO00OOO0O000O0O =O0OOOO0OOO0O0OO0O ['data'][0 ]['crops']#line:353
                    for OOO00O0OO00000OOO in OOOO00OOO0O000O0O :#line:354
                        if OOO00O0OO00000OOO ['ill_clover_award']:#line:355
                            if float (OOO00O0OO00000OOO ['ill_clover_award'])>1 :#line:356
                                if OOO00O0OO00000OOO ['is_finish']:#line:357
                                    if not OOO00O0OO00000OOO ['is_getit']:#line:358
                                        if O0O00O0OO0OO000OO .certification ()!='未实名':#line:359
                                            O00O00O0O0000OOO0 =f'_award_level={OOO00O0OO00000OOO["level"]}_{timi_new()}'#line:360
                                            OO00O0O0O0O00OOOO ={'authorization':O0O00O0OO0OO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O0000OOO0 ),'signstring':O00O00O0O0000OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            OO0OO00OO00000OO0 ={"award_level":OOO00O0OO00000OOO ['level']}#line:370
                                            OOOO00O00O000O0OO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO00O0O0O0O00OOOO ,json =OO0OO00OO00000OO0 ).json ()#line:372
                                            if 'status'in OOOO00O00O000O0OO :#line:373
                                                if OOOO00O00O000O0OO ['status']==200 :#line:374
                                                    OOOOOO00O0O0OOOO0 =OOOO00O00O000O0OO ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{OOO00O0OO00000OOO["crop_name"]}成就丨奖励{OOOOOO00O0O0OOOO0}☘️')#line:377
                                                if OOOO00O00O000O0OO ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{OOOO00O00O000O0OO["message"]}')#line:379
        except Exception as OOO000O0OOOO00O0O :#line:380
            print (OOO000O0OOOO00O0O )#line:381
    def watched_ad (O0O0O0OOOO0OO0O0O ):#line:384
        try :#line:385
            OOOO000O000000OO0 =f'__{timi_new()}'#line:386
            OO0O000O0O00OOO00 ={'authorization':O0O0O0OOOO0OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O000000OO0 ),'signstring':OOOO000O000000OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            O0OO00OOO00OOOOOO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O000O0O00OOO00 ).json ()#line:396
            if 'status'in O0OO00OOO00OOOOOO :#line:398
                if O0OO00OOO00OOOOOO ['status']==200 :#line:399
                    if 'offlineInfo'in O0OO00OOO00OOOOOO ['data']:#line:400
                        O00O0O00OOO000O0O =O0OO00OOO00OOOOOO ['data']['offlineInfo']['off_minute']#line:401
                        OO0OO00OO0O00O000 =float (O0OO00OOO00OOOOOO ['data']['silver'])/1000000000000 #line:402
                        time .sleep (1 )#line:403
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0O000O0O00OOO00 ).json ()#line:404
                        time .sleep (2 )#line:405
                        OO00O0O0000000OOO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O000O0O00OOO00 ).json ()#line:406
                        if 'status'in OO00O0O0000000OOO :#line:408
                            if OO00O0O0000000OOO ['status']==200 :#line:409
                                O0O00OO0O00OOO0O0 =float (OO00O0O0000000OOO ['data']['silver'])/1000000000000 #line:410
                                O0000000OOO0OOOOO =str (O0O00OO0O00OOO0O0 -OO0OO00OO0O00O000 )[:6 ]#line:411
                                print (f'【离线奖励】:翻倍离线{O00O0O00OOO000O0O}分钟奖励🌱数量:{O0000000OOO0OOOOO}t粒')#line:412
        except Exception as OOOOOOO0000O0O00O :#line:413
            print (OOOOOOO0000O0O00O )#line:414
    def user_ad (OOO0O00OOOO000OO0 ):#line:417
        try :#line:418
            O00OO0000O00O00OO =f'__{timi_new()}'#line:419
            O000OOOO000O00000 ={'authorization':OOO0O00OOOO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0000O00O00OO ),'signstring':O00OO0000O00O00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:428
            O0OOOO0O0O000O0O0 =requests .request ('get',f'{host}/user/ad',headers =O000OOOO000O00000 ).json ()#line:429
            if 'status'in O0OOOO0O0O000O0O0 :#line:431
                if O0OOOO0O0O000O0O0 ['status']==200 :#line:432
                    O0OO0O00O0OOO0OOO =O0OOOO0O0O000O0O0 ['data']['max_time']#line:433
                    OOO0000000OO00O00 =O0OOOO0O0O000O0O0 ['data']['watch_time']#line:434
                    OO0OOOO0OO0OOOO0O =O0OOOO0O0O000O0O0 ['data']['added_time']#line:435
                    print (f'【获取种子】:获取🌱剩余{OO0OOOO0OO0OOOO0O + O0OO0O00O0OOO0OOO - OOO0000000OO00O00}次丨好友提供:{OO0OOOO0OO0OOOO0O}次')#line:436
                    if OO0OOOO0OO0OOOO0O +O0OO0O00O0OOO0OOO -OOO0000000OO00O00 >0 :#line:437
                        time .sleep (random .randint (16 ,19 ))#line:438
                        OO0O000O00000OO0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O000OOOO000O00000 ).json ()#line:439
                        if 'status'in OO0O000O00000OO0O :#line:441
                            if OO0O000O00000OO0O ['status']==200 :#line:442
                                O0O000OOOO0000OOO =float (OO0O000O00000OO0O ['data']['silver'])/1000000000000 #line:443
                                print (f'【获取种子】:获得🌱:{int(O0O000OOOO0000OOO)}t粒')#line:444
                                return True #line:445
                            if OO0O000O00000OO0O ['status']==500 :#line:446
                                OO00O0000OO0OOO0O =OO0O000O00000OO0O ['message']#line:447
                                print (f'【获取种子】:{OO00O0000OO0OOO0O}')#line:448
                                return False #line:449
        except Exception as OOO000000000OOOOO :#line:450
            print (OOO000000000OOOOO )#line:451
    def synthetic (OO000O00O000OOO00 ):#line:454
        global id ,g #line:455
        try :#line:456
            OOO0O0OOO0O0OO0OO =OO000O00O000OOO00 .level_new ()#line:457
            O00OO00OOOO0O0OOO =random .randint (9 ,11 )#line:458
            O00O0O0000O00O0OO =f'_site=8&targetSite={O00OO00OOOO0O0OOO}_{timi_new()}'#line:459
            O0OOO00OOOOOO0O00 ={'accept':'application/json, text/plain, */*','authorization':OO000O00O000OOO00 .token ,'timestamp':timi_new (),'sign':sign (O00O0O0000O00O0OO ),'signstring':O00O0O0000O00O0OO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:474
            OO00O0OO0O0O00O0O ={"site":int (8 ),"targetSite":int (O00OO00OOOO0O0OOO )}#line:475
            requests .request ('post',f'{host}/game/crops/move',headers =O0OOO00OOOOOO0O00 ,json =OO00O0OO0O0O00O0O )#line:476
            while True :#line:477
                OO0OO00O0O0OO0OOO =f'__{timi_new()}'#line:478
                OOO0OO00O0OO00OOO ={'authorization':OO000O00O000OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00O0O0OO0OOO ),'signstring':OO0OO00O0O0OO0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:487
                OOOO0O0OO00000OO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OO00O0OO00OOO ).json ()#line:488
                if 'status'in OOOO0O0OO00000OO0 :#line:490
                    if OOOO0O0OO00000OO0 ['status']==200 :#line:491
                        O00O0OO0OO0OO0OOO =OOOO0O0OO00000OO0 ['data']['cropList']#line:492
                        OOOO0000O0OOOOO00 =OOOO0O0OO00000OO0 ['data']['gameCoreDataDBid']#line:493
                        O0O00OOO00O0O0OO0 =float (OOOO0O0OO00000OO0 ['data']['silver'])/1000000000000 #line:494
                        if O0O00OOO00O0O0OO0 <6750 :#line:495
                            print (f'【种植合成】:🌱不足6750t')#line:496
                            break #line:497
                        OOOOOOOOOOO000O00 =0 #line:498
                        for OOOOO000O0O0O00O0 in O00O0OO0OO0OO0OOO :#line:499
                            if not OOOOO000O0O0O00O0 :#line:500
                                OOOO0000OOOOO00OO =f'_crop_id={OOOO0000O0OOOOO00}&site={OOOOOOOOOOO000O00}_{OO000O00O000OOO00.time}'#line:501
                                O00OO0O0O0O00OOOO ={'authorization':OO000O00O000OOO00 .token ,'timestamp':OO000O00O000OOO00 .time ,'sign':sign (OOOO0000OOOOO00OO ),'signstring':OOOO0000OOOOO00OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:510
                                OO0O00OO0000OOOOO ={"site":OOOOOOOOOOO000O00 ,"crop_id":OOOO0000O0OOOOO00 }#line:511
                                O0000O00O0O0O0O00 =requests .request ('post',f'{host}/game/crops/buy',headers =O00OO0O0O0O00OOOO ,data =OO0O00OO0000OOOOO ).json ()#line:512
                                time .sleep (random .randint (1 ,3 )/10 )#line:514
                                if 'status'in O0000O00O0O0O0O00 :#line:515
                                    if O0000O00O0O0O0O00 ['status']==200 :#line:516
                                        if O0000O00O0O0O0O00 ['message']=='种子数量不足':#line:517
                                            OOO0O0OOO0O0OO0OO =OO000O00O000OOO00 .level_new ()#line:518
                                            print (f'【种植合成】:{O0000O00O0O0O0O00["message"]}')#line:519
                                            if not OO000O00O000OOO00 .user_ad ():#line:520
                                                return False #line:521
                                    if O0000O00O0O0O0O00 ['status']==500 :#line:522
                                        print (f'【种植合成】:{O0000O00O0O0O0O00["message"]}')#line:523
                                        return False #line:524
                            OOOOOOOOOOO000O00 +=1 #line:525
                        O0OOO00O00O00OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OO00O0OO00OOO ).json ()#line:526
                        O0O00O000O0OOO0OO =O0OOO00O00O00OOO0 ['data']['cropList']#line:527
                        O0O00O0OOO0OOOOO0 =False #line:528
                        for OOOOO000O0O0O00O0 in range (12 ):#line:529
                            id =O0O00O000O0OOO0OO [OOOOO000O0O0O00O0 ]['level']#line:530
                            if float (OOO0O0OOO0O0OO0OO )-float (id )>9 :#line:531
                                OO0O00OOO0OO000OO =f'_site={OOOOO000O0O0O00O0}_{timi_new()}'#line:532
                                OOOOOOOO0O0OOO000 ={'accept':'application/json, text/plain, */*','authorization':OO000O00O000OOO00 .token ,'timestamp':timi_new (),'sign':sign (OO0O00OOO0OO000OO ),'signstring':OO0O00OOO0OO000OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:542
                                O0O0O00OOOOO000OO ={"site":OOOOO000O0O0O00O0 }#line:543
                                O000OOO0OOO0OO00O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOOOOOO0O0OOO000 ,data =O0O0O00OOOOO000OO ).json ()#line:545
                                if 'status'in O000OOO0OOO0OO00O :#line:546
                                    if O000OOO0OOO0OO00O ['status']==200 :#line:547
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:548
                            if id !=0 :#line:549
                                for OOOO0O0O00O0O0O00 in range (11 ):#line:550
                                    OOOO0OOO000OO0OO0 =OOOO0O0O00O0O0O00 +1 #line:551
                                    g =O0O00O000O0OOO0OO [OOOO0OOO000OO0OO0 ]['level']#line:552
                                    if id ==g :#line:553
                                        O0OO0OO0000O00O00 =OOOO0O0O00O0O0O00 +2 #line:554
                                        if O0OO0OO0000O00O00 !=OOOOO000O0O0O00O0 +1 :#line:555
                                            OO0OO0OOOO0O0O0OO =OOOOO000O0O0O00O0 +1 #line:556
                                            time .sleep (random .randint (1 ,3 )/10 )#line:558
                                            O00O0O0000O00O0OO =f'_site={OO0OO0OOOO0O0O0OO - 1}&targetSite={O0OO0OO0000O00O00 - 1}_{timi_new()}'#line:559
                                            O0OOO00OOOOOO0O00 ={'accept':'application/json, text/plain, */*','authorization':OO000O00O000OOO00 .token ,'timestamp':timi_new (),'sign':sign (O00O0O0000O00O0OO ),'signstring':O00O0O0000O00O0OO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:574
                                            O000OOOOOOOO0OOOO ={"site":int (OO0OO0OOOO0O0O0OO -1 ),"targetSite":int (O0OO0OO0000O00O00 -1 )}#line:575
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0OOO00OOOOOO0O00 ,json =O000OOOOOOOO0OOOO )#line:576
                                            print (f'【种植合成】:位置{OO0OO0OOOO0O0O0OO}和位置{O0OO0OO0000O00O00}合出{int(id) + 1}级农作物')#line:577
                                            O0O00O0OOO0OOOOO0 =True #line:578
                                    if O0O00O0OOO0OOOOO0 :#line:579
                                        break #line:580
                                if O0O00O0OOO0OOOOO0 :#line:581
                                    break #line:582
        except :#line:583
            OO000O00O000OOO00 .synthetic ()#line:584
    def level_new (OO0000O0O0OOOOOO0 ):#line:587
        try :#line:588
            O0O00O00OOO0OOO00 =f'__{timi_new()}'#line:589
            OO0OOO0000OO000O0 ={'authorization':OO0000O0O0OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00OOO0OOO00 ),'signstring':O0O00O00OOO0OOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:598
            O0OO00O0OO0OO0O00 =requests .request ('get',f'{host}/user',headers =OO0OOO0000OO000O0 ).json ()#line:599
            if 'status'in O0OO00O0OO0OO0O00 :#line:600
                if O0OO00O0OO0OO0O00 ['status']==200 :#line:601
                    return float (O0OO00O0OO0OO0O00 ['data']['level'])#line:602
        except Exception as O000O0000OOOOO000 :#line:603
            print (O000O0000OOOOO000 )#line:604
    def propsraffle (O000O0OOO00O0O00O ):#line:607
        try :#line:608
            while True :#line:609
                OOOO0OOO0O00OOOO0 =f'__{timi_new()}'#line:610
                OO000O00000OO0O00 ={'authorization':O000O0OOO00O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO0O00OOOO0 ),'signstring':OOOO0OOO0O00OOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:619
                OOOOO00OO0OOOO0O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO000O00000OO0O00 ).json ()#line:620
                if 'status'in OOOOO00OO0OOOO0O0 :#line:622
                    if OOOOO00OO0OOOO0O0 ['status']==200 :#line:623
                        OO00OO00OOO0O00OO =OOOOO00OO0OOOO0O0 ['data']['rows']#line:624
                        O0OOOO0O00O0O0OOO =OOOOO00OO0OOOO0O0 ['data']['vstate']#line:625
                        if OO00OO00OOO0O00OO ==5 or OO00OO00OOO0O00OO ==6 or OO00OO00OOO0O00OO ==7 :#line:626
                            OOO0OO00OO00OO0O0 =OOOOO00OO0OOOO0O0 ['data']['silver']#line:627
                            print (f'【转盘抽奖】:获得种子:{OOO0OO00OO00OO0O0}')#line:628
                        if OO00OO00OOO0O00OO ==1 or OO00OO00OOO0O00OO ==2 or OO00OO00OOO0O00OO ==3 :#line:629
                            OOOOO00O00O00O0O0 =OOOOO00OO0OOOO0O0 ['data']['clover']#line:630
                            print (f'【转盘抽奖】:获得三叶草:{OOOOO00O00O00O0O0}')#line:631
                        if OO00OO00OOO0O00OO ==4 or OO00OO00OOO0O00OO ==8 :#line:632
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:633
                        if OO00OO00OOO0O00OO =='抽奖次数已用完':#line:637
                            break #line:670
                time .sleep (random .randint (8 ,15 )/10 )#line:671
        except Exception as OOOO000O0O00O0OOO :#line:672
            print (OOOO000O0O00O0OOO )#line:673
    def friends_invitation (OOO0O000O0OOO000O ):#line:676
        try :#line:677
            O00000OOO0O00O00O =f'__{timi_new()}'#line:678
            O000O00O000O00000 ={'authorization':OOO0O000O0OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOO0O00O00O ),'signstring':O00000OOO0O00O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:687
            OOO0O00O0O0O0O000 =requests .request ('get',f'{host}/friends',headers =O000O00O000O00000 ).json ()#line:688
            if 'status'in OOO0O00O0O0O0O000 :#line:689
                if OOO0O00O0O0O0O000 ['status']==200 :#line:690
                    OOO000O0OOOOOOOO0 =OOO0O00O0O0O0O000 ['data']['myInviteter']#line:691
                    if OOO000O0OOOOOOOO0 :#line:692
                        O000O0O0O0OO0O0O0 =OOO000O0OOOOOOOO0 ['user']['nickname']#line:693
                        OO0O0000OO00O000O =OOO0O000O0OOO000O .certification ()#line:694
                        print (f'【查邀请人】:我的邀请人:{O000O0O0O0OO0O0O0}丨实名:{OO0O0000OO00O000O}')#line:695
                    else :#line:696
                        if OOO0O000O0OOO000O .innerId !='0':#line:697
                            OOO0O000O0OOO000O .invitation ()#line:698
        except Exception as O0O00000OOOOOOO0O :#line:699
            print (O0O00000OOOOOOO0O )#line:700
    def add_clover (OO0O00O00000O00O0 ):#line:703
        global golden_seed #line:704
        try :#line:705
            O0OO00OO0O0OO0O0O =f'__{timi_new()}'#line:706
            O00O0O0OO00O00OO0 ={'authorization':OO0O00O00000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO0O0OO0O0O ),'signstring':O0OO00OO0O0OO0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:715
            OO0O00OO00OOO0OO0 =requests .request ('get',f'{host}/assets/clovers',headers =O00O0O0OO00O00OO0 ).json ()#line:716
            if 'status'in OO0O00OO00OOO0OO0 :#line:718
                if OO0O00OO00OOO0OO0 ['status']==200 :#line:719
                    O0O0OO0O00000O000 =OO0O00OO00OOO0OO0 ['data']['clover']#line:720
                    OOOOOO00O0OOOOO0O =OO0O00OO00OOO0OO0 ['data']['used_clover']#line:721
                    O00000OOOOOO0OOO0 =float (O0O0OO0O00000O000 )-float (OOOOOO00O0OOOOO0O )#line:722
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOOOOO00O0OOOOO0O}')#line:723
                    if OO0O00O00000O00O0 .certification ()!='未实名':#line:724
                        if O00000OOOOOO0OOO0 >1 :#line:725
                            O0OO00OO0O0OO0O0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00000OOOOOO0OOO0)}_{timi_new()}'#line:726
                            OOOO0000O0O0O00OO ={'authorization':OO0O00O00000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO0O0OO0O0O ),'signstring':O0OO00OO0O0OO0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:735
                            O00OOOOO00O0O0O00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00000OOOOOO0OOO0 )}#line:736
                            O00OO00O0OOOO00O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOO0000O0O0O00OO ,data =O00OOOOO00O0O0O00 ).json ()#line:737
                            if 'status'in O00OO00O0OOOO00O0 :#line:739
                                if O00OO00O0OOOO00O0 ['status']==200 :#line:740
                                    print (f'【参与抽奖】:添加☘️:{O00OO00O0OOOO00O0["data"]}丨数量:{O00000OOOOOO0OOO0}')#line:741
                                if O00OO00O0OOOO00O0 ['status']==500 :#line:742
                                    print (f'【参与抽奖】:添加☘️:{O00OO00O0OOOO00O0["message"]}')#line:743
            OOO00000O0O0O00O0 =requests .request ('get',f'{host}/lottery',headers =O00O0O0OO00O00OO0 ).json ()#line:744
            O0000O00O0000O0OO =OO0O00O00000O00O0 .winning_rewards ()#line:746
            if 'status'in OOO00000O0O0O00O0 :#line:747
                if OOO00000O0O0O00O0 ['status']==200 :#line:748
                    O0O00O0OOO0O0OO0O =OOO00000O0O0O00O0 ['data'][0 ]['day_get_gold_quantity']#line:749
                    golden_seed +=float (O0O00O0OOO0O0OO0O )#line:750
                    O00O0O0OO000O0O0O =OOO00000O0O0O00O0 ['data'][1 ]['value']#line:751
                    O00OOOO0OOOOOO000 =OOO00000O0O0O00O0 ['data'][0 ]['join_number']#line:752
                    OO000OOO000O0O0O0 =int (float (OOO00000O0O0O00O0 ['data'][0 ]['totalValue']))#line:753
                    OOO00O0OOO0000O0O =float (O00O0O0OO000O0O0O /OO000OOO000O0O0O0 )*10000 #line:754
                    O0O00O0000O0O00OO =OO000OOO000O0O0O0 /O00OOOO0OOOOOO000 #line:755
                    print (f'【参与抽奖】:预计每天中{str(O0O00O0OOO0O0OO0O)[:6]}颗金种子丨好友收益:{str(O0000O00O0000O0OO)[:6]}')#line:756
                    print (f'【抽奖统计】:每1万☘️中{str(OOO00O0OOO0000O0O)[:4]}颗金种子丨人均{str(O0O00O0000O0O00OO)[:7]}☘️')#line:757
        except Exception as OO0OO0O000OOO0OO0 :#line:758
            print (OO0OO0O000OOO0OO0 )#line:759
    def energy (O0OO00000O0OO0O0O ):#line:763
        try :#line:764
            while True :#line:765
                O0O000O00OO0O0OO0 =f'__{timi_new()}'#line:766
                O0O0O0O0O000O0OOO ={'authorization':O0OO00000O0OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000O00OO0O0OO0 ),'signstring':O0O000O00OO0O0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:775
                O000000OOOO00O00O =requests .request ('get',f'{host}/energy/general',headers =O0O0O0O0O000O0OOO ).json ()#line:776
                if 'status'in O000000OOOO00O00O :#line:778
                    if O000000OOOO00O00O ['status']==200 :#line:779
                        O000O00000OOO00OO =O000000OOOO00O00O ['data']['ordinary_water']#line:780
                        O0O000OO00000O0OO =O000000OOOO00O00O ['data']['ordinary_fertilizer']#line:781
                        print (f'【我的营养】:肥料:{str(O0O000OO00000O0OO).split(".")[0]}丨水滴:{str(O000O00000OOO00OO).split(".")[0]}')#line:783
                        if float (O0O000OO00000O0OO )<96 :#line:784
                            time .sleep (random .randint (160 ,180 )/10 )#line:785
                            O0O0O0OOO0OO00OOO =99 -float (O0O000OO00000O0OO )#line:786
                            O0O000O0OOO0O0000 ={"fertilizer":str (O0O0O0OOO0OO00OOO ).split ('.')[0 ]}#line:787
                            OOO0O0O00OO0O000O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0O0O0O0O000O0OOO ).json ()#line:788
                            if 'status'in OOO0O0O00OO0O000O :#line:790
                                if OOO0O0O00OO0O000O ['status']==200 :#line:791
                                    print (f'【购买肥料】:看广告获取肥料:{OOO0O0O00OO0O000O["message"]}')#line:792
                        if float (O000O00000OOO00OO )<880 :#line:793
                            time .sleep (random .randint (160 ,180 )/10 )#line:794
                            OO0000OOO0O000OOO =999 -float (O000O00000OOO00OO )#line:795
                            OOO0O00O0O0OOOOO0 ={"water":str (OO0000OOO0O000OOO ).split ('.')[0 ]}#line:796
                            OO00OO0O000000O00 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0O0O0O0O000O0OOO ).json ()#line:797
                            if 'status'in OO00OO0O000000O00 :#line:799
                                if OO00OO0O000000O00 ['status']==200 :#line:800
                                    print (f'【购买水滴】:看广告获取水滴:{OO00OO0O000000O00["message"]}')#line:801
                        if float (O0O000OO00000O0OO )>96 and float (O000O00000OOO00OO )>880 :#line:802
                            break #line:803
        except Exception as O0O0000OO0OOO0O0O :#line:805
            print (O0O0000OO0OOO0O0O )#line:806
def bundled_def ():#line:808
    OO00O0O0OOOOO0O00 =['5570536','7750212','7911652','7911680','7805624']#line:809
    return OO00O0O0OOOOO0O00 [random .randint (0 ,len (OO00O0O0OOOOO0O00 )-1 )]#line:810
def version_of_the_validation ():#line:814
    return str ((78 -56 )/10 )#line:815
def gitee_validation ():#line:818
    try :#line:819
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:820
    except :#line:821
        sys .exit (0 )#line:822
def update_the_validation ():#line:826
    try :#line:827
        O000OOO000OO0OO00 =gitee_validation ()#line:828
        if version_of_the_validation ()<O000OOO000OO0OO00 ['CityEarth']['edition']:#line:829
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOO000OO0OO00["CityEarth"]["edition"]}   ❌')#line:830
            print (f'更新内容=>>{O000OOO000OO0OO00["CityEarth"]["content"]}   👍')#line:831
        else :#line:832
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOO000OO0OO00["CityEarth"]["edition"]}   ✅')#line:833
            print (f'更新内容=>> {O000OOO000OO0OO00["CityEarth"]["content"]}   👍')#line:834
    except Exception as O00OO0O0O00OOO00O :#line:835
        print (O00OO0O0O00OOO00O )#line:836
def os_qinglong ():#line:839
    if application in os .environ :#line:840
        OO0O0O00O00OO0OOO =os .environ [application ].split ('\n')#line:841
        if len (OO0O0O00O00OO0OOO )>0 :#line:842
            return OO0O0O00O00OO0OOO #line:843
        else :#line:844
            print (f"{application}变量未启用")#line:845
            print ('脚本退出')#line:846
            sys .exit (1 )#line:847
    else :#line:848
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:850
        return os_built ()#line:851
def os_built ():#line:854
    if token :#line:855
        OO00O0OO0OO0OO0OO =token .split ('\n')#line:856
        if len (OO00O0OO0OO0OO0OO )>0 :#line:857
            return OO00O0OO0OO0OO0OO #line:858
    else :#line:859
        print (f"内置变量为空")#line:860
        print ('脚本结束')#line:861
        sys .exit (0 )#line:862
if __name__ =='__main__':#line:865
    start ()#line:866
