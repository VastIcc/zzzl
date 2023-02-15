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
        OO00O0O0OO0O000OO =os_qinglong ()#line:10
        print (f"==========共找到{len(OO00O0O0OO0O000OO)}个账号==========")#line:11
        for O0O0OO00O0O00000O in OO00O0O0OO0O000OO :#line:12
            OOOOO0O0000000OO0 =[]#line:13
            print (f"------------正在执行第{OO00O0O0OO0O000OO.index(O0O0OO00O0O00000O) + 1}个账号------------")#line:14
            OOOOOO0OO00O000OO =CityEarth (O0O0OO00O0O00000O ,OOOOO0O0000000OO0 )#line:15
            def O000O0OO000O00000 ():#line:17
                if OOOOOO0OO00O000OO .base_info ():#line:19
                    OOOOOO0OO00O000OO .sealing ()#line:21
                    OOOOOO0OO00O000OO .invitenum ()#line:23
                    OOOOOO0OO00O000OO .game_map ()#line:25
                    OOOOOO0OO00O000OO .friends_invitation ()#line:27
                    OOOOOO0OO00O000OO .add_clover ()#line:29
                    OOOOOO0OO00O000OO .propsraffle ()#line:31
                    OOOOOO0OO00O000OO .synthetic ()#line:33
                    OOOOOO0OO00O000OO .crops_illustrated ()#line:35
                    OOOOOO0OO00O000OO .give_gold ()#line:37
                    OOOOOO0OO00O000OO .withdraw ()#line:39
                    OOOOOO0OO00O000OO .energy ()#line:41
            OO00O0OOO0O000O0O =threading .Thread (target =O000O0OO000O00000 )#line:42
            OO00O0OOO0O000O0O .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        OO0O000000O00O00O =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0O000000O00O00O +' ')#line:48
    except Exception as O000OOO0OO0O0OO0O :#line:49
        print (O000OOO0OO0O0OO0O )#line:50
def sign (O00OOO00O00OOO00O ):#line:53
    OO0OOO0OO00O00000 =hashlib .md5 (O00OOO00O00OOO00O .encode ()).hexdigest ()#line:54
    OO00OOO0OOO0O0OOO ="scsc%^&*"+OO0OOO0OO00O00000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    OO0OO0OO0O0000000 =hashlib .md5 (OO00OOO0OOO0O0OOO .encode ()).hexdigest ()#line:56
    return OO0OO0OO0O0000000 #line:57
def format_msg ():#line:59
    OOOO000O00O0OO0O0 =""#line:60
    for O0O0O00O00O0000OO in msg_list :#line:61
        OOOO000O00O0OO0O0 +=str (O0O0O00O00O0000OO )+"\r\n"#line:62
    return OOOO000O00O0OO0O0 #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (O0O0O00O000O000O0 ,O0O00000O00OOO000 ,OO0000OOOOO0000O0 ):#line:71
        try :#line:72
            O0O0O00O000O000O0 .msg =OO0000OOOOO0000O0 #line:73
            O0O0O00O000O000O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            O0O0O00O000O000O0 .token =O0O00000O00OOO000 .split ('&')[0 ]#line:75
            O0O0O00O000O000O0 .innerId =O0O00000O00OOO000 .split ('&')[1 ]#line:76
            O0O0O00O000O000O0 .doneeNo =O0O00000O00OOO000 .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (OO000O00OO0O0O0OO ):#line:82
        try :#line:83
            OO000O00OO0O0O0OO .watched_ad ()#line:85
            OO0O0000O00O0OO00 =f'__{timi_new()}'#line:86
            OO0OO0O0O000OO0OO ={'authorization':OO000O00OO0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000O00O0OO00 ),'signstring':OO0O0000O00O0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            O00O00OO00OOOOO0O =requests .request ('get',f'{host}/user',headers =OO0OO0O0O000OO0OO ).json ()#line:96
            if 'status'in O00O00OO00OOOOO0O :#line:98
                if O00O00OO00OOOOO0O ['status']==200 :#line:99
                    OOO00O0O000O0OOOO =O00O00OO00OOOOO0O ['data']['nickname']#line:100
                    OO0OO00OOO00O0000 =O00O00OO00OOOOO0O ['data']['inner_id']#line:101
                    O0OO0OO00O0OO0000 =O00O00OO00OOOOO0O ['data']['assets']['gold']#line:102
                    O0O00000OO00O00OO =O00O00OO00OOOOO0O ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{OOO00O0O000O0OOOO[:5]}丨ID:{OO0OO00OOO00O0000}丨等级:{O0O00000OO00O00OO}丨金种子:{str(O0OO0OO00O0OO0000).split(".")[0]}')#line:104
                if O00O00OO00OOOOO0O ['status']==401 :#line:105
                    print (O00O00OO00OOOOO0O ['message'])#line:106
                    OO000O00OO0O0O0OO .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if O00O00OO00OOOOO0O ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as O0OOOO0OO00OOO000 :#line:112
            print (O0OOOO0OO00OOO000 )#line:113
    def sealing (O00O0OO0O0O00OO00 ):#line:116
        try :#line:117
            O0O000OO0OO0000O0 =f'__{timi_new()}'#line:118
            OOOOOOO0O0OOOOO00 ={'authorization':O00O0OO0O0O00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OO0OO0000O0 ),'signstring':O0O000OO0OO0000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOOOOO0O0OOOOO00 )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =OOOOOOO0O0OOOOO00 )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOOOOO0O0OOOOO00 )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOOOOO0O0OOOOO00 )#line:131
            requests .request ('get',f'{host}/user',headers =OOOOOOO0O0OOOOO00 )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOOOOO0O0OOOOO00 )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOOOOO0O0OOOOO00 )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOOOOO0O0OOOOO00 )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =OOOOOOO0O0OOOOO00 )#line:136
            requests .request ('get',f'{host}/assets',headers =OOOOOOO0O0OOOOO00 )#line:137
        except Exception as O0O0OO00OOO0O0O00 :#line:138
            print (O0O0OO00OOO0O0O00 )#line:139
    def withdraw (OO0O0O0OO0O0OOO0O ):#line:143
        O00O0000O0OO0OO00 =f'__{timi_new()}'#line:144
        OO00OO000O0OO0OO0 ={'authorization':OO0O0O0OO0O0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0000O0OO0OO00 ),'signstring':O00O0000O0OO0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        O00O0O0OOO00O0OOO =requests .request ('get',f'{host}/assets',headers =OO00OO000O0OO0OO0 ).json ()#line:154
        if 'status'in O00O0O0OOO00O0OOO :#line:156
            if O00O0O0OOO00O0OOO ['status']==200 :#line:157
                OOOOO000OOO00OO00 =O00O0O0OOO00O0OOO ['data']['cash']#line:158
                if float (OOOOO000OOO00OO00 )>20 :#line:159
                    O00O0000O0OO0OO00 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    OO00OO000O0OO0OO0 ={'authorization':OO0O0O0OO0O0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0000O0OO0OO00 ),'signstring':O00O0000O0OO0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    OOOOOO00OO00O0O0O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    O000O00000OOOOO0O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO00OO000O0OO0OO0 ,data =OOOOOO00OO00O0O0O ).json ()#line:172
                    print (O000O00000OOOOO0O )#line:173
    def invitenum (O0000OO00OOOOO00O ):#line:176
        OOO00O00OOO0O0O00 =f'__{timi_new()}'#line:177
        O0O0OOO0O0000OOOO ={'authorization':O0000OO00OOOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00OOO0O0O00 ),'signstring':OOO00O00OOO0O0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        OOOO0OO00O00OO00O =requests .request ('get',f'{host}/invite/invitenum',headers =O0O0OOO0O0000OOOO ).json ()#line:187
        if 'status'in OOOO0OO00O00OO00O :#line:189
            if OOOO0OO00O00OO00O ['status']==200 :#line:190
                OOOO0OO000O000O00 =OOOO0OO00O00OO00O ['data']['invited_count']#line:191
                O0O000OO0000000O0 =OOOO0OO00O00OO00O ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OOOO0OO000O000O00}丨间邀好友:{O0O000OO0000000O0}')#line:193
    def game_map (O0OO0O0O0000OOO00 ):#line:196
        try :#line:197
            OOO00OOO0OO00O0O0 =f'__{timi_new()}'#line:198
            O00OO000000O0O00O ={'authorization':O0OO0O0O0000OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO0OO00O0O0 ),'signstring':OOO00OOO0OO00O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            OO00O00000OO0OOO0 =requests .request ('get',f'{host}/game/map',headers =O00OO000000O0O00O ).json ()#line:208
            if 'status'in OO00O00000OO0OOO0 :#line:210
                if OO00O00000OO0OOO0 ['status']==200 :#line:211
                    for O0OO0O00OO000OOOO in OO00O00000OO0OOO0 ['data']['list'][0 ]['crops']:#line:212
                        O00O0OOO00OO0OOO0 =O0OO0O00OO000OOOO ['level']#line:214
                        if O00O0OOO00OO0OOO0 ==41 :#line:215
                            O0O000OOO0OO0OOO0 =O0OO0O00OO000OOOO ['crop_name']#line:216
                            OOOOO000O00OOOO0O =O0OO0O00OO000OOOO ['count']#line:217
                            if OOOOO000O00OOOO0O >0 :#line:218
                                print (f'【农业资产】:{O0O000OOO0OO0OOO0}丨数量:{OOOOO000O00OOOO0O}')#line:219
        except Exception as OO00OO00OOOO0OOOO :#line:220
            print (OO00OO00OOOO0OOOO )#line:221
    def give_gold (O0O0O0OO0OOOOOOO0 ):#line:224
        try :#line:225
            O0O00000O000O0O0O =f'__{timi_new()}'#line:226
            OO000000OOO0O0000 ={'authorization':O0O0O0OO0OOOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000O000O0O0O ),'signstring':O0O00000O000O0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            O00O0O0O0O00O0000 =requests .request ('get',f'{host}/user',headers =OO000000OOO0O0000 ).json ()#line:236
            if 'status'in O00O0O0O0O00O0000 :#line:237
                if O00O0O0O0O00O0000 ['status']==200 :#line:238
                    if float (O0O0O0OO0OOOOOOO0 .doneeNo )!=0 :#line:239
                        O00O000O0000O000O =O00O0O0O0O00O0000 ['data']['assets']['gold']#line:240
                        if float (O00O000O0000O000O )>float (O0O0O0OO0OOOOOOO0 .innerId ):#line:241
                            O0OO0O000OOO0O00O =int (float (O00O000O0000O000O )/1.1 )#line:242
                            O0O00000O000O0O0O =f'_doneeNo={O0O0O0OO0OOOOOOO0.doneeNo}&quantity={O0OO0O000OOO0O00O}_{timi_new()}'#line:243
                            OO000000OOO0O0000 ={'authorization':O0O0O0OO0OOOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000O000O0O0O ),'signstring':O0O00000O000O0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            O0OOO00000O0OO000 ={"quantity":O0OO0O000OOO0O00O ,"doneeNo":O0O0O0OO0OOOOOOO0 .doneeNo }#line:256
                            O0O0O0OOOOO0O0O0O =requests .request ('post',f'{host}/finance/give-gold',headers =OO000000OOO0O0000 ,data =O0OOO00000O0OO000 ).json ()#line:257
                            if 'status'in O0O0O0OOOOO0O0O0O :#line:259
                                if O0O0O0OOOOO0O0O0O ['status']==200 :#line:260
                                    if O0O0O0OOOOO0O0O0O ['data']:#line:261
                                        print (f'【赠送种子】:赠送{O0OO0O000OOO0O00O}种子给{O0O0O0OO0OOOOOOO0.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as OO0O0O0OO0OOO0000 :#line:265
            print (OO0O0O0OO0OOO0000 )#line:266
    def invitation (OOOOOO000OO0O0O00 ):#line:268
        try :#line:269
            _OO000OO00O00OO000 =float (bundled_def ())/4 #line:270
            O000O0OOOO00O00OO =f'_innerId={int(_OO000OO00O00OO000)}_{timi_new()}'#line:271
            OOO00O0O00000OOOO ={'authorization':OOOOOO000OO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOOO00O00OO ),'signstring':O000O0OOOO00O00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            O0O0OOOOOOO0OOOO0 ={"innerId":int (_OO000OO00O00OO000 )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO00O0O00000OOOO ,data =O0O0OOOOOOO0OOOO0 )#line:282
        except Exception as OO0000OOOOOO00O00 :#line:283
            print (OO0000OOOOOO00O00 )#line:284
    def winning_rewards (O000O0O0OO000O00O ):#line:287
        try :#line:288
            O00OO0OO0OO00O0O0 =f'__{timi_new()}'#line:289
            O00OO0O00OO000O00 ={'authorization':O000O0O0OO000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OO0OO00O0O0 ),'signstring':O00OO0OO0OO00O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            O0O00O0OO0O0OOO0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00OO0O00OO000O00 ).json ()#line:299
            if 'status'in O0O00O0OO0O0OOO0O :#line:301
                if O0O00O0OO0O0OOO0O ['status']==200 :#line:302
                    if O0O00O0OO0O0OOO0O ['data']['amount']:#line:303
                        O0O000O00O00OOOOO =O0O00O0OO0O0OOO0O ['data']['amount']['gold']#line:304
                        return O0O000O00O00OOOOO #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as OOOO0OOOO0O0OO0O0 :#line:308
            print (OOOO0OOOO0O0OO0O0 )#line:309
    def certification (O00O0OO0OO0OOOOOO ):#line:312
        try :#line:313
            OOOOOOO0O0OO00O0O =f'__{timi_new()}'#line:314
            O0O0OOO0O0OOO00OO ={'authorization':O00O0OO0OO0OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0O0OO00O0O ),'signstring':OOOOOOO0O0OO00O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OOO0000O0O00O0O0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0O0OOO0O0OOO00OO ).json ()#line:324
            if 'status'in OOO0000O0O00O0O0O :#line:326
                if OOO0000O0O00O0O0O ['status']==200 :#line:327
                    if OOO0000O0O00O0O0O ['data']['result']:#line:328
                        OOOO00OO0O00O0000 =OOO0000O0O00O0O0O ['data']['nick_name']#line:329
                        return OOOO00OO0O00O0000 #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as O00OO0O0O0OO000OO :#line:333
            print (O00OO0O0O0OO000OO )#line:334
    def crops_illustrated (OO0OOOO000OOO0OO0 ):#line:337
        try :#line:338
            OOOO0000O000000O0 =f'__{timi_new()}'#line:339
            O0O0O0OOOO00OOOO0 ={'authorization':OO0OOOO000OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000O000000O0 ),'signstring':OOOO0000O000000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            O0000O0OO00O0000O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O0O0OOOO00OOOO0 ).json ()#line:349
            if 'status'in O0000O0OO00O0000O :#line:351
                if O0000O0OO00O0000O ['status']==200 :#line:352
                    O000O000O000000O0 =O0000O0OO00O0000O ['data'][0 ]['crops']#line:353
                    for OOO000OOO0000O00O in O000O000O000000O0 :#line:354
                        if OOO000OOO0000O00O ['ill_clover_award']:#line:355
                            if float (OOO000OOO0000O00O ['ill_clover_award'])>1 :#line:356
                                if OOO000OOO0000O00O ['is_finish']:#line:357
                                    if not OOO000OOO0000O00O ['is_getit']:#line:358
                                        if OO0OOOO000OOO0OO0 .certification ()!='未实名':#line:359
                                            OOOO0000O000000O0 =f'_award_level={OOO000OOO0000O00O["level"]}_{timi_new()}'#line:360
                                            O0O0O0OOOO00OOOO0 ={'authorization':OO0OOOO000OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000O000000O0 ),'signstring':OOOO0000O000000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            O0OOO00OO0000OO0O ={"award_level":OOO000OOO0000O00O ['level']}#line:370
                                            O0000OO00O0000O00 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O0O0OOOO00OOOO0 ,json =O0OOO00OO0000OO0O ).json ()#line:372
                                            if 'status'in O0000OO00O0000O00 :#line:373
                                                if O0000OO00O0000O00 ['status']==200 :#line:374
                                                    OO0000O0000O0000O =O0000OO00O0000O00 ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{OOO000OOO0000O00O["crop_name"]}成就丨奖励{OO0000O0000O0000O}☘️')#line:377
                                                if O0000OO00O0000O00 ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{O0000OO00O0000O00["message"]}')#line:379
        except Exception as OOOO0OOOO0OOO00OO :#line:380
            print (OOOO0OOOO0OOO00OO )#line:381
    def watched_ad (O00O000O0O0O0OOOO ):#line:384
        try :#line:385
            time .sleep (random .randint (16 ,18 ))#line:386
            O0OOO0OO0O0OOOOOO =f'__{timi_new()}'#line:387
            O00O0O00O0OOO00OO ={'authorization':O00O000O0O0O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO0O0OOOOOO ),'signstring':O0OOO0OO0O0OOOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:396
            OOO0O0OOOO00000O0 =requests .request ('get',f'{host}/game/getAllData',headers =O00O0O00O0OOO00OO ).json ()#line:397
            if 'status'in OOO0O0OOOO00000O0 :#line:399
                if OOO0O0OOOO00000O0 ['status']==200 :#line:400
                    if 'offlineInfo'in OOO0O0OOOO00000O0 ['data']:#line:401
                        O0OO0O000O00000OO =OOO0O0OOOO00000O0 ['data']['offlineInfo']['off_minute']#line:402
                        O000OO0000OOOOO00 =float (OOO0O0OOOO00000O0 ['data']['silver'])/1000000000000 #line:403
                        time .sleep (1 )#line:404
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00O0O00O0OOO00OO ).json ()#line:405
                        time .sleep (2 )#line:406
                        OO0O00OO0000OOOOO =requests .request ('get',f'{host}/game/getAllData',headers =O00O0O00O0OOO00OO ).json ()#line:407
                        if 'status'in OO0O00OO0000OOOOO :#line:409
                            if OO0O00OO0000OOOOO ['status']==200 :#line:410
                                O00OO0000OOOOOOOO =float (OO0O00OO0000OOOOO ['data']['silver'])/1000000000000 #line:411
                                O000OO000OOOOO0O0 =str (O00OO0000OOOOOOOO -O000OO0000OOOOO00 )[:6 ]#line:412
                                print (f'【离线奖励】:翻倍离线{O0OO0O000O00000OO}分钟奖励🌱数量:{O000OO000OOOOO0O0}t粒')#line:413
        except Exception as OOO0O000OO000O000 :#line:414
            print (OOO0O000OO000O000 )#line:415
    def user_ad (OOOOOO0OO0OOOOOO0 ):#line:418
        try :#line:419
            OOO0OOO0O000O0O0O =f'__{timi_new()}'#line:420
            O00OO0O00OO0O0O00 ={'authorization':OOOOOO0OO0OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0O000O0O0O ),'signstring':OOO0OOO0O000O0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:429
            O00OO0OOOO0OOOOO0 =requests .request ('get',f'{host}/user/ad',headers =O00OO0O00OO0O0O00 ).json ()#line:430
            if 'status'in O00OO0OOOO0OOOOO0 :#line:432
                if O00OO0OOOO0OOOOO0 ['status']==200 :#line:433
                    OOO0O0OO0OO0000O0 =O00OO0OOOO0OOOOO0 ['data']['max_time']#line:434
                    OOOOO0OO0O0OOOOOO =O00OO0OOOO0OOOOO0 ['data']['watch_time']#line:435
                    OO0OOOOOO00OOO0OO =O00OO0OOOO0OOOOO0 ['data']['added_time']#line:436
                    print (f'【获取种子】:获取🌱剩余{OO0OOOOOO00OOO0OO + OOO0O0OO0OO0000O0 - OOOOO0OO0O0OOOOOO}次丨好友提供:{OO0OOOOOO00OOO0OO}次')#line:437
                    if OO0OOOOOO00OOO0OO +OOO0O0OO0OO0000O0 -OOOOO0OO0O0OOOOOO >0 :#line:438
                        time .sleep (random .randint (16 ,19 ))#line:439
                        OOOO0OOOOO0O0000O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00OO0O00OO0O0O00 ).json ()#line:440
                        if 'status'in OOOO0OOOOO0O0000O :#line:442
                            if OOOO0OOOOO0O0000O ['status']==200 :#line:443
                                O0O0O000O00OO0O0O =float (OOOO0OOOOO0O0000O ['data']['silver'])/1000000000000 #line:444
                                print (f'【获取种子】:获得🌱:{int(O0O0O000O00OO0O0O)}t粒')#line:445
                                return True #line:446
                            if OOOO0OOOOO0O0000O ['status']==500 :#line:447
                                O000OOOO00OOO0OO0 =OOOO0OOOOO0O0000O ['message']#line:448
                                print (f'【获取种子】:{O000OOOO00OOO0OO0}')#line:449
                                return False #line:450
        except Exception as O0OO0OO000O000000 :#line:451
            print (O0OO0OO000O000000 )#line:452
    def synthetic (OOO00OO0O0O00O0O0 ):#line:455
        global id ,g #line:456
        try :#line:457
            OO00OO0O0OOOOO0OO =OOO00OO0O0O00O0O0 .level_new ()#line:458
            OO00O00000O0O00OO =random .randint (9 ,11 )#line:459
            OOO000OO0OOOOO00O =f'_site=8&targetSite={OO00O00000O0O00OO}_{timi_new()}'#line:460
            OO0OO00000OO0OO00 ={'accept':'application/json, text/plain, */*','authorization':OOO00OO0O0O00O0O0 .token ,'timestamp':timi_new (),'sign':sign (OOO000OO0OOOOO00O ),'signstring':OOO000OO0OOOOO00O ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:475
            OOO000OOOOO0OOO0O ={"site":int (8 ),"targetSite":int (OO00O00000O0O00OO )}#line:476
            requests .request ('post',f'{host}/game/crops/move',headers =OO0OO00000OO0OO00 ,json =OOO000OOOOO0OOO0O )#line:477
            while True :#line:478
                OOO0O0O000O0O000O =f'__{timi_new()}'#line:479
                O000OOO00O00O00OO ={'authorization':OOO00OO0O0O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O000O0O000O ),'signstring':OOO0O0O000O0O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                O00OO0OOO00OOOOOO =requests .request ('get',f'{host}/game/getAllData',headers =O000OOO00O00O00OO ).json ()#line:489
                if 'status'in O00OO0OOO00OOOOOO :#line:491
                    if O00OO0OOO00OOOOOO ['status']==200 :#line:492
                        OO0O000O0O00OO0O0 =O00OO0OOO00OOOOOO ['data']['cropList']#line:493
                        O0O000OOO0O0OOO0O =O00OO0OOO00OOOOOO ['data']['gameCoreDataDBid']#line:494
                        OOOOOOOOOOOO0OOOO =float (O00OO0OOO00OOOOOO ['data']['silver'])/1000000000000 #line:495
                        if OOOOOOOOOOOO0OOOO <6750 :#line:496
                            print (f'【种植合成】:🌱不足6750t')#line:497
                            break #line:498
                        OOO00000O0OOOO0OO =0 #line:499
                        for O0000O00O00O0OOO0 in OO0O000O0O00OO0O0 :#line:500
                            if not O0000O00O00O0OOO0 :#line:501
                                O000O0OO00000OO00 =f'_crop_id={O0O000OOO0O0OOO0O}&site={OOO00000O0OOOO0OO}_{OOO00OO0O0O00O0O0.time}'#line:502
                                O0O0OO0OO00OOO0OO ={'authorization':OOO00OO0O0O00O0O0 .token ,'timestamp':OOO00OO0O0O00O0O0 .time ,'sign':sign (O000O0OO00000OO00 ),'signstring':O000O0OO00000OO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:511
                                O00OO0O0OO0O0OOO0 ={"site":OOO00000O0OOOO0OO ,"crop_id":O0O000OOO0O0OOO0O }#line:512
                                O0OO000000000OOO0 =requests .request ('post',f'{host}/game/crops/buy',headers =O0O0OO0OO00OOO0OO ,data =O00OO0O0OO0O0OOO0 ).json ()#line:513
                                time .sleep (random .randint (1 ,3 )/10 )#line:515
                                if 'status'in O0OO000000000OOO0 :#line:516
                                    if O0OO000000000OOO0 ['status']==200 :#line:517
                                        if O0OO000000000OOO0 ['message']=='种子数量不足':#line:518
                                            OO00OO0O0OOOOO0OO =OOO00OO0O0O00O0O0 .level_new ()#line:519
                                            print (f'【种植合成】:{O0OO000000000OOO0["message"]}')#line:520
                                            if not OOO00OO0O0O00O0O0 .user_ad ():#line:521
                                                return False #line:522
                                    if O0OO000000000OOO0 ['status']==500 :#line:523
                                        print (f'【种植合成】:{O0OO000000000OOO0["message"]}')#line:524
                                        return False #line:525
                            OOO00000O0OOOO0OO +=1 #line:526
                        O000O00000000OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O000OOO00O00O00OO ).json ()#line:527
                        O0O000OO000OO00O0 =O000O00000000OOO0 ['data']['cropList']#line:528
                        O00O0000O0OO0O0OO =False #line:529
                        for O0000O00O00O0OOO0 in range (12 ):#line:530
                            id =O0O000OO000OO00O0 [O0000O00O00O0OOO0 ]['level']#line:531
                            if float (OO00OO0O0OOOOO0OO )-float (id )>9 :#line:532
                                OOO00O00OOO0O0O0O =f'_site={O0000O00O00O0OOO0}_{timi_new()}'#line:533
                                O00O0O00OOO00O00O ={'accept':'application/json, text/plain, */*','authorization':OOO00OO0O0O00O0O0 .token ,'timestamp':timi_new (),'sign':sign (OOO00O00OOO0O0O0O ),'signstring':OOO00O00OOO0O0O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:543
                                OOO0O0O00OOOO0OO0 ={"site":O0000O00O00O0OOO0 }#line:544
                                OO000O00O000O0OO0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00O0O00OOO00O00O ,data =OOO0O0O00OOOO0OO0 ).json ()#line:546
                                if 'status'in OO000O00O000O0OO0 :#line:547
                                    if OO000O00O000O0OO0 ['status']==200 :#line:548
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:549
                            if id !=0 :#line:550
                                for O000O0O00OO00OOO0 in range (11 ):#line:551
                                    OO00O0O0O000O00OO =O000O0O00OO00OOO0 +1 #line:552
                                    g =O0O000OO000OO00O0 [OO00O0O0O000O00OO ]['level']#line:553
                                    if id ==g :#line:554
                                        OO0OOO00OOO000O00 =O000O0O00OO00OOO0 +2 #line:555
                                        if OO0OOO00OOO000O00 !=O0000O00O00O0OOO0 +1 :#line:556
                                            OO0O00O00OOO00O00 =O0000O00O00O0OOO0 +1 #line:557
                                            time .sleep (random .randint (1 ,3 )/10 )#line:559
                                            OOO000OO0OOOOO00O =f'_site={OO0O00O00OOO00O00 - 1}&targetSite={OO0OOO00OOO000O00 - 1}_{timi_new()}'#line:560
                                            OO0OO00000OO0OO00 ={'accept':'application/json, text/plain, */*','authorization':OOO00OO0O0O00O0O0 .token ,'timestamp':timi_new (),'sign':sign (OOO000OO0OOOOO00O ),'signstring':OOO000OO0OOOOO00O ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:575
                                            O0O0O0OOOOOO00O0O ={"site":int (OO0O00O00OOO00O00 -1 ),"targetSite":int (OO0OOO00OOO000O00 -1 )}#line:576
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0OO00000OO0OO00 ,json =O0O0O0OOOOOO00O0O )#line:577
                                            print (f'【种植合成】:位置{OO0O00O00OOO00O00}和位置{OO0OOO00OOO000O00}合出{int(id) + 1}级农作物')#line:578
                                            O00O0000O0OO0O0OO =True #line:579
                                    if O00O0000O0OO0O0OO :#line:580
                                        break #line:581
                                if O00O0000O0OO0O0OO :#line:582
                                    break #line:583
        except :#line:584
            OOO00OO0O0O00O0O0 .synthetic ()#line:585
    def level_new (O0OO0000O000OOO0O ):#line:588
        try :#line:589
            O0OOO00OOOO0OOO00 =f'__{timi_new()}'#line:590
            OOO00000OOOOO0OOO ={'authorization':O0OO0000O000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OOOO0OOO00 ),'signstring':O0OOO00OOOO0OOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:599
            OOOO00O0OOO0O00OO =requests .request ('get',f'{host}/user',headers =OOO00000OOOOO0OOO ).json ()#line:600
            if 'status'in OOOO00O0OOO0O00OO :#line:601
                if OOOO00O0OOO0O00OO ['status']==200 :#line:602
                    return float (OOOO00O0OOO0O00OO ['data']['level'])#line:603
        except Exception as OO0OOOOO0O000OO0O :#line:604
            print (OO0OOOOO0O000OO0O )#line:605
    def propsraffle (O0OOOO0O0O0OOOO0O ):#line:608
        try :#line:609
            while True :#line:610
                OOOO0000O0O0O000O =f'__{timi_new()}'#line:611
                OO00000O000OOO00O ={'authorization':O0OOOO0O0O0OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000O0O0O000O ),'signstring':OOOO0000O0O0O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:620
                OO00O0000O0OO00OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO00000O000OOO00O ).json ()#line:621
                if 'status'in OO00O0000O0OO00OO :#line:623
                    if OO00O0000O0OO00OO ['status']==200 :#line:624
                        O00OO0000OOOOO0OO =OO00O0000O0OO00OO ['data']['rows']#line:625
                        OO000O0OOO0OO0O00 =OO00O0000O0OO00OO ['data']['vstate']#line:626
                        if O00OO0000OOOOO0OO ==5 or O00OO0000OOOOO0OO ==6 or O00OO0000OOOOO0OO ==7 :#line:627
                            O0OO00OO0OO0O0OOO =OO00O0000O0OO00OO ['data']['silver']#line:628
                            print (f'【转盘抽奖】:获得种子:{O0OO00OO0OO0O0OOO}')#line:629
                        if O00OO0000OOOOO0OO ==1 or O00OO0000OOOOO0OO ==2 or O00OO0000OOOOO0OO ==3 :#line:630
                            O000OOO000O0OOO00 =OO00O0000O0OO00OO ['data']['clover']#line:631
                            print (f'【转盘抽奖】:获得三叶草:{O000OOO000O0OOO00}')#line:632
                        if O00OO0000OOOOO0OO ==4 or O00OO0000OOOOO0OO ==8 :#line:633
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:634
                        if O00OO0000OOOOO0OO =='抽奖次数已用完':#line:638
                            break #line:671
                time .sleep (random .randint (8 ,15 )/10 )#line:672
        except Exception as OO0000OO00O0O0000 :#line:673
            print (OO0000OO00O0O0000 )#line:674
    def friends_invitation (OOOO0O0O000OO0000 ):#line:677
        try :#line:678
            OOO0OO0O0O00O000O =f'__{timi_new()}'#line:679
            O00OO0OOOOOO0OOO0 ={'authorization':OOOO0O0O000OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O0O00O000O ),'signstring':OOO0OO0O0O00O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:688
            O0OOO0OO0OOOOO0OO =requests .request ('get',f'{host}/friends',headers =O00OO0OOOOOO0OOO0 ).json ()#line:689
            if 'status'in O0OOO0OO0OOOOO0OO :#line:690
                if O0OOO0OO0OOOOO0OO ['status']==200 :#line:691
                    OOOOOOOO0O0O0OO0O =O0OOO0OO0OOOOO0OO ['data']['myInviteter']#line:692
                    if OOOOOOOO0O0O0OO0O :#line:693
                        O0OO000000OOO0OOO =OOOOOOOO0O0O0OO0O ['user']['nickname']#line:694
                        OO0OOOO0OO0OOOO0O =OOOO0O0O000OO0000 .certification ()#line:695
                        print (f'【查邀请人】:我的邀请人:{O0OO000000OOO0OOO}丨实名:{OO0OOOO0OO0OOOO0O}')#line:696
                    else :#line:697
                        if OOOO0O0O000OO0000 .innerId !='0':#line:698
                            OOOO0O0O000OO0000 .invitation ()#line:699
        except Exception as O0O00OO0OOO0O0OOO :#line:700
            print (O0O00OO0OOO0O0OOO )#line:701
    def add_clover (OO00O0OO0000000OO ):#line:704
        global golden_seed #line:705
        try :#line:706
            OO0O00O00OOO0O0O0 =f'__{timi_new()}'#line:707
            O0OO00O0O0O0O0OO0 ={'authorization':OO00O0OO0000000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O00OOO0O0O0 ),'signstring':OO0O00O00OOO0O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:716
            O0000000O0OO000OO =requests .request ('get',f'{host}/assets/clovers',headers =O0OO00O0O0O0O0OO0 ).json ()#line:717
            if 'status'in O0000000O0OO000OO :#line:719
                if O0000000O0OO000OO ['status']==200 :#line:720
                    O0000O0OOOOO000O0 =O0000000O0OO000OO ['data']['clover']#line:721
                    OOOOOOOOO000O00OO =O0000000O0OO000OO ['data']['used_clover']#line:722
                    OOOOOO00OOO00O00O =float (O0000O0OOOOO000O0 )-float (OOOOOOOOO000O00OO )#line:723
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOOOOOOOO000O00OO}')#line:724
                    if OO00O0OO0000000OO .certification ()!='未实名':#line:725
                        if OOOOOO00OOO00O00O >1 :#line:726
                            OO0O00O00OOO0O0O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOOOO00OOO00O00O)}_{timi_new()}'#line:727
                            O000O00O0000OOO00 ={'authorization':OO00O0OO0000000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O00OOO0O0O0 ),'signstring':OO0O00O00OOO0O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:736
                            O000OO0O0OOO0OOO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOOOO00OOO00O00O )}#line:737
                            OOOOO0000OOO000O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =O000O00O0000OOO00 ,data =O000OO0O0OOO0OOO0 ).json ()#line:738
                            if 'status'in OOOOO0000OOO000O0 :#line:740
                                if OOOOO0000OOO000O0 ['status']==200 :#line:741
                                    print (f'【参与抽奖】:添加☘️:{OOOOO0000OOO000O0["data"]}丨数量:{OOOOOO00OOO00O00O}')#line:742
                                if OOOOO0000OOO000O0 ['status']==500 :#line:743
                                    print (f'【参与抽奖】:添加☘️:{OOOOO0000OOO000O0["message"]}')#line:744
            OO00OOOOO0OO00O0O =requests .request ('get',f'{host}/lottery',headers =O0OO00O0O0O0O0OO0 ).json ()#line:745
            OOO0000O00OOO0O00 =OO00O0OO0000000OO .winning_rewards ()#line:747
            if 'status'in OO00OOOOO0OO00O0O :#line:748
                if OO00OOOOO0OO00O0O ['status']==200 :#line:749
                    OO0OOOOO0OO00OOO0 =OO00OOOOO0OO00O0O ['data'][0 ]['day_get_gold_quantity']#line:750
                    golden_seed +=float (OO0OOOOO0OO00OOO0 )#line:751
                    OOO00O0000000OOO0 =OO00OOOOO0OO00O0O ['data'][1 ]['value']#line:752
                    O0000OO0000OOOOO0 =OO00OOOOO0OO00O0O ['data'][0 ]['join_number']#line:753
                    O0O0OO0O00OOOOO0O =int (float (OO00OOOOO0OO00O0O ['data'][0 ]['totalValue']))#line:754
                    OOOOO0000OO0OO000 =float (OOO00O0000000OOO0 /O0O0OO0O00OOOOO0O )*10000 #line:755
                    O00OO00O0000O0OOO =O0O0OO0O00OOOOO0O /O0000OO0000OOOOO0 #line:756
                    print (f'【参与抽奖】:预计每天中{str(OO0OOOOO0OO00OOO0)[:6]}颗金种子丨好友收益:{str(OOO0000O00OOO0O00)[:6]}')#line:757
                    print (f'【抽奖统计】:每1万☘️中{str(OOOOO0000OO0OO000)[:6]}颗金种子丨☘️人均:{str(O00OO00O0000O0OOO)[:7]}️')#line:758
        except Exception as OO00000OO0O0O00O0 :#line:759
            print (OO00000OO0O0O00O0 )#line:760
    def energy (O0O0O0O0OOO0OO00O ):#line:764
        try :#line:765
            while True :#line:766
                O00O00OOOO0OOOOO0 =f'__{timi_new()}'#line:767
                OOO0O00OOOOO0OO0O ={'authorization':O0O0O0O0OOO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OOOO0OOOOO0 ),'signstring':O00O00OOOO0OOOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:776
                OO0OOO0OOO0OOO000 =requests .request ('get',f'{host}/energy/general',headers =OOO0O00OOOOO0OO0O ).json ()#line:777
                if 'status'in OO0OOO0OOO0OOO000 :#line:779
                    if OO0OOO0OOO0OOO000 ['status']==200 :#line:780
                        OO0OOOO0O0OO0O00O =OO0OOO0OOO0OOO000 ['data']['ordinary_water']#line:781
                        O00O0000O0O0OOOOO =OO0OOO0OOO0OOO000 ['data']['ordinary_fertilizer']#line:782
                        print (f'【我的营养】:肥料:{str(O00O0000O0O0OOOOO).split(".")[0]}丨水滴:{str(OO0OOOO0O0OO0O00O).split(".")[0]}')#line:784
                        if float (O00O0000O0O0OOOOO )<96 :#line:785
                            time .sleep (random .randint (160 ,180 )/10 )#line:786
                            OO00OOO000OOO000O =99 -float (O00O0000O0O0OOOOO )#line:787
                            OO0OOOO0OO0O0OO0O ={"fertilizer":str (OO00OOO000OOO000O ).split ('.')[0 ]}#line:788
                            O0OO00OO00OOOOOO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOO0O00OOOOO0OO0O ).json ()#line:789
                            if 'status'in O0OO00OO00OOOOOO0 :#line:791
                                if O0OO00OO00OOOOOO0 ['status']==200 :#line:792
                                    print (f'【购买肥料】:看广告获取肥料:{O0OO00OO00OOOOOO0["message"]}')#line:793
                        if float (OO0OOOO0O0OO0O00O )<880 :#line:794
                            time .sleep (random .randint (160 ,180 )/10 )#line:795
                            O0OOO0O00O0OO0OOO =999 -float (OO0OOOO0O0OO0O00O )#line:796
                            O0O0OOOOO0000OO00 ={"water":str (O0OOO0O00O0OO0OOO ).split ('.')[0 ]}#line:797
                            O0O0O0OOO0000O000 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOO0O00OOOOO0OO0O ).json ()#line:798
                            if 'status'in O0O0O0OOO0000O000 :#line:800
                                if O0O0O0OOO0000O000 ['status']==200 :#line:801
                                    print (f'【购买水滴】:看广告获取水滴:{O0O0O0OOO0000O000["message"]}')#line:802
                        if float (O00O0000O0O0OOOOO )>96 and float (OO0OOOO0O0OO0O00O )>880 :#line:803
                            break #line:804
        except Exception as O00000OOOO0O0OO0O :#line:806
            print (O00000OOOO0O0OO0O )#line:807
def bundled_def ():#line:809
    OO00O0O0O000O0O00 =['5570536','7750212','7911652','7911680','7805624']#line:810
    return OO00O0O0O000O0O00 [random .randint (0 ,len (OO00O0O0O000O0O00 )-1 )]#line:811
def version_of_the_validation ():#line:815
    return str ((78 -56 )/10 )#line:816
def gitee_validation ():#line:819
    try :#line:820
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:821
    except :#line:822
        sys .exit (0 )#line:823
def update_the_validation ():#line:827
    try :#line:828
        OOOO000O0OO00O0O0 =gitee_validation ()#line:829
        if version_of_the_validation ()<OOOO000O0OO00O0O0 ['CityEarth']['edition']:#line:830
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO000O0OO00O0O0["CityEarth"]["edition"]}   ❌')#line:831
            print (f'更新内容=>>{OOOO000O0OO00O0O0["CityEarth"]["content"]}   🎉')#line:832
        else :#line:833
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO000O0OO00O0O0["CityEarth"]["edition"]}   ✅')#line:834
            print (f'更新内容=>> {OOOO000O0OO00O0O0["CityEarth"]["content"]}   🎉')#line:835
    except Exception as OO0OO0O00OOOO0O00 :#line:836
        print (OO0OO0O00OOOO0O00 )#line:837
def os_qinglong ():#line:840
    if application in os .environ :#line:841
        OO000O0OOOOO00O0O =os .environ [application ].split ('\n')#line:842
        if len (OO000O0OOOOO00O0O )>0 :#line:843
            return OO000O0OOOOO00O0O #line:844
        else :#line:845
            print (f"{application}变量未启用")#line:846
            print ('脚本退出')#line:847
            sys .exit (1 )#line:848
    else :#line:849
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:851
        return os_built ()#line:852
def os_built ():#line:855
    if token :#line:856
        OOOOO0OOOOOOOO0O0 =token .split ('\n')#line:857
        if len (OOOOO0OOOOOOOO0O0 )>0 :#line:858
            return OOOOO0OOOOOOOO0O0 #line:859
    else :#line:860
        print (f"内置变量为空")#line:861
        print ('脚本结束')#line:862
        sys .exit (0 )#line:863
if __name__ =='__main__':#line:866
    start ()#line:867
