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
except Exception as e:
    t = re.findall("d '(.*?)'", str(e))[0]
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
@ 版本  2.1
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
        O000O000O0OO0O000 =os_qinglong ()#line:10
        print (f"==========共找到{len(O000O000O0OO0O000)}个账号==========")#line:11
        for O00OO0O00OOOO000O in O000O000O0OO0O000 :#line:12
            O000O00000O0O0OOO =[]#line:13
            print (f"------------正在执行第{O000O000O0OO0O000.index(O00OO0O00OOOO000O) + 1}个账号------------")#line:14
            OO0O0OOOOOO0O000O =CityEarth (O00OO0O00OOOO000O ,O000O00000O0O0OOO )#line:15
            def O0O0000OOO0O00O0O ():#line:17
                if OO0O0OOOOOO0O000O .base_info ():#line:19
                    OO0O0OOOOOO0O000O .sealing ()#line:21
                    OO0O0OOOOOO0O000O .invitenum ()#line:23
                    OO0O0OOOOOO0O000O .game_map ()#line:25
                    OO0O0OOOOOO0O000O .friends_invitation ()#line:27
                    OO0O0OOOOOO0O000O .add_clover ()#line:29
                    OO0O0OOOOOO0O000O .propsraffle ()#line:31
                    OO0O0OOOOOO0O000O .synthetic ()#line:33
                    OO0O0OOOOOO0O000O .crops_illustrated ()#line:35
                    OO0O0OOOOOO0O000O .give_gold ()#line:37
                    OO0O0OOOOOO0O000O .withdraw ()#line:39
                    OO0O0OOOOOO0O000O .energy ()#line:41
            O00000OO0000OOOO0 =threading .Thread (target =O0O0000OOO0O00O0O )#line:42
            O00000OO0000OOOO0 .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        OOOOOO0OO000000OO =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOOOOO0OO000000OO +' ')#line:48
    except Exception as OO0O00O0O0000OOOO :#line:49
        print (OO0O00O0O0000OOOO )#line:50
def sign (OOO0O0O00O0OO00OO ):#line:53
    OOOO000O000000O0O =hashlib .md5 (OOO0O0O00O0OO00OO .encode ()).hexdigest ()#line:54
    O0OO0OOOOO0O00OOO ="scsc%^&*"+OOOO000O000000O0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    O00O0OO0OOOOOO0OO =hashlib .md5 (O0OO0OOOOO0O00OOO .encode ()).hexdigest ()#line:56
    return O00O0OO0OOOOOO0OO #line:57
def format_msg ():#line:59
    OO0000OOOOOO0OOO0 =""#line:60
    for OO00000O0O00OO0OO in msg_list :#line:61
        OO0000OOOOOO0OOO0 +=str (OO00000O0O00OO0OO )+"\r\n"#line:62
    return OO0000OOOOOO0OOO0 #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (OOO0OOOO0OO0O0O0O ,O000O00000O00O0OO ,OOOO00O0O00O00OO0 ):#line:71
        try :#line:72
            OOO0OOOO0OO0O0O0O .msg =OOOO00O0O00O00OO0 #line:73
            OOO0OOOO0OO0O0O0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            OOO0OOOO0OO0O0O0O .token =O000O00000O00O0OO .split ('&')[0 ]#line:75
            OOO0OOOO0OO0O0O0O .innerId =O000O00000O00O0OO .split ('&')[1 ]#line:76
            OOO0OOOO0OO0O0O0O .doneeNo =O000O00000O00O0OO .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (O0OOO0000OOOOOO0O ):#line:82
        try :#line:83
            O0OOO0000OOOOOO0O .watched_ad ()#line:85
            OOO0000OOOOOOOO00 =f'__{timi_new()}'#line:86
            O000O0000OOO0000O ={'authorization':O0OOO0000OOOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OOOOOOOO00 ),'signstring':OOO0000OOOOOOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            O00O00OOOO0000O0O =requests .request ('get',f'{host}/user',headers =O000O0000OOO0000O ).json ()#line:96
            if 'status'in O00O00OOOO0000O0O :#line:98
                if O00O00OOOO0000O0O ['status']==200 :#line:99
                    OO0OO0O0OO0O000OO =O00O00OOOO0000O0O ['data']['nickname']#line:100
                    O00O00O0O0OOOO0O0 =O00O00OOOO0000O0O ['data']['inner_id']#line:101
                    O0OOO00000000OO00 =O00O00OOOO0000O0O ['data']['assets']['gold']#line:102
                    OO0O0O0OOO0OOO00O =O00O00OOOO0000O0O ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{OO0OO0O0OO0O000OO[:5]}丨ID:{O00O00O0O0OOOO0O0}丨等级:{OO0O0O0OOO0OOO00O}丨种子:{str(O0OOO00000000OO00).split(".")[0]}')#line:104
                if O00O00OOOO0000O0O ['status']==401 :#line:105
                    print (O00O00OOOO0000O0O ['message'])#line:106
                    O0OOO0000OOOOOO0O .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if O00O00OOOO0000O0O ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as O0O00O0OO000O0O0O :#line:112
            print (O0O00O0OO000O0O0O )#line:113
    def sealing (OO0OO0O0O0000O0OO ):#line:116
        try :#line:117
            OO000OOOOOOO0O0O0 =f'__{timi_new()}'#line:118
            O0O0OO0OOOO0OO0OO ={'authorization':OO0OO0O0O0000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOOOOO0O0O0 ),'signstring':OO000OOOOOOO0O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0O0OO0OOOO0OO0OO )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =O0O0OO0OOOO0OO0OO )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0O0OO0OOOO0OO0OO )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0O0OO0OOOO0OO0OO )#line:131
            requests .request ('get',f'{host}/user',headers =O0O0OO0OOOO0OO0OO )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0O0OO0OOOO0OO0OO )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0O0OO0OOOO0OO0OO )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =O0O0OO0OOOO0OO0OO )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO0OOOO0OO0OO )#line:136
            requests .request ('get',f'{host}/assets',headers =O0O0OO0OOOO0OO0OO )#line:137
        except Exception as OO00000O00OOO0000 :#line:138
            print (OO00000O00OOO0000 )#line:139
    def withdraw (O0O0OO000OOO0O000 ):#line:143
        OOOO0OOOOO00OO000 =f'__{timi_new()}'#line:144
        O0OO000OOOO00OO00 ={'authorization':O0O0OO000OOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOOO00OO000 ),'signstring':OOOO0OOOOO00OO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        OO0O0OOOO0000OO00 =requests .request ('get',f'{host}/assets',headers =O0OO000OOOO00OO00 ).json ()#line:154
        if 'status'in OO0O0OOOO0000OO00 :#line:156
            if OO0O0OOOO0000OO00 ['status']==200 :#line:157
                O000O000O0OO0OOO0 =OO0O0OOOO0000OO00 ['data']['cash']#line:158
                if float (O000O000O0OO0OOO0 )>20 :#line:159
                    OOOO0OOOOO00OO000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    O0OO000OOOO00OO00 ={'authorization':O0O0OO000OOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOOO00OO000 ),'signstring':OOOO0OOOOO00OO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    O0OO0OO0OOO00OOO0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    O0OOOO0OO00O0O0OO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0OO000OOOO00OO00 ,data =O0OO0OO0OOO00OOO0 ).json ()#line:172
                    print (O0OOOO0OO00O0O0OO )#line:173
    def invitenum (O0O0000O00OO000O0 ):#line:176
        O0000O00OO0OO0OO0 =f'__{timi_new()}'#line:177
        O00000O0OOO00OO0O ={'authorization':O0O0000O00OO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00OO0OO0OO0 ),'signstring':O0000O00OO0OO0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O0O0O0OO0OO00O00O =requests .request ('get',f'{host}/invite/invitenum',headers =O00000O0OOO00OO0O ).json ()#line:187
        if 'status'in O0O0O0OO0OO00O00O :#line:189
            if O0O0O0OO0OO00O00O ['status']==200 :#line:190
                O0O0O000OOOOOOOOO =O0O0O0OO0OO00O00O ['data']['invited_count']#line:191
                OO00OOO0O0OOO000O =O0O0O0OO0OO00O00O ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{O0O0O000OOOOOOOOO}丨间邀好友:{OO00OOO0O0OOO000O}')#line:193
    def game_map (O0O0OOO0OOOO00OOO ):#line:196
        try :#line:197
            OO00OOOO0O000O0O0 =f'__{timi_new()}'#line:198
            O00OOOOO0OOOO0OOO ={'authorization':O0O0OOO0OOOO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOO0O000O0O0 ),'signstring':OO00OOOO0O000O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            OO000OO00OO0OOOOO =requests .request ('get',f'{host}/game/map',headers =O00OOOOO0OOOO0OOO ).json ()#line:208
            if 'status'in OO000OO00OO0OOOOO :#line:210
                if OO000OO00OO0OOOOO ['status']==200 :#line:211
                    for O0OO0OO0OO0000OO0 in OO000OO00OO0OOOOO ['data']['list'][0 ]['crops']:#line:212
                        OOO0OOOO00O0OOOOO =O0OO0OO0OO0000OO0 ['level']#line:214
                        if OOO0OOOO00O0OOOOO ==41 :#line:215
                            O0OO00O00OO00O0O0 =O0OO0OO0OO0000OO0 ['crop_name']#line:216
                            OO0OO0000OOOO0O00 =O0OO0OO0OO0000OO0 ['count']#line:217
                            if OO0OO0000OOOO0O00 >0 :#line:218
                                print (f'【农业资产】:{O0OO00O00OO00O0O0}丨数量:{OO0OO0000OOOO0O00}')#line:219
        except Exception as O0000OOO0000O0OOO :#line:220
            print (O0000OOO0000O0OOO )#line:221
    def give_gold (OOOOOO00O0000O000 ):#line:224
        try :#line:225
            OO0OO000OOO00OO0O =f'__{timi_new()}'#line:226
            O000O0000O0000OO0 ={'authorization':OOOOOO00O0000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OOO00OO0O ),'signstring':OO0OO000OOO00OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            OO00000O0OO0OOO00 =requests .request ('get',f'{host}/user',headers =O000O0000O0000OO0 ).json ()#line:236
            if 'status'in OO00000O0OO0OOO00 :#line:237
                if OO00000O0OO0OOO00 ['status']==200 :#line:238
                    if float (OOOOOO00O0000O000 .doneeNo )!=0 :#line:239
                        O000O00O0OO0O00O0 =OO00000O0OO0OOO00 ['data']['assets']['gold']#line:240
                        if float (O000O00O0OO0O00O0 )>float (OOOOOO00O0000O000 .innerId ):#line:241
                            OOOOOO0OOO0OO00OO =int (float (O000O00O0OO0O00O0 )/1.1 )#line:242
                            OO0OO000OOO00OO0O =f'_doneeNo={OOOOOO00O0000O000.doneeNo}&quantity={OOOOOO0OOO0OO00OO}_{timi_new()}'#line:243
                            O000O0000O0000OO0 ={'authorization':OOOOOO00O0000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OOO00OO0O ),'signstring':OO0OO000OOO00OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            O0OO00OO0000O0O0O ={"quantity":OOOOOO0OOO0OO00OO ,"doneeNo":OOOOOO00O0000O000 .doneeNo }#line:256
                            O000OO0OOOOOO000O =requests .request ('post',f'{host}/finance/give-gold',headers =O000O0000O0000OO0 ,data =O0OO00OO0000O0O0O ).json ()#line:257
                            if 'status'in O000OO0OOOOOO000O :#line:259
                                if O000OO0OOOOOO000O ['status']==200 :#line:260
                                    if O000OO0OOOOOO000O ['data']:#line:261
                                        print (f'【赠送种子】:赠送{OOOOOO0OOO0OO00OO}种子给{OOOOOO00O0000O000.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as O0O000O00O0O0OO0O :#line:265
            print (O0O000O00O0O0OO0O )#line:266
    def invitation (O0OO000O0OOOO00OO ):#line:268
        try :#line:269
            _OO000000O0O0O00O0 =float (bundled_def ())/4 #line:270
            OOO00O00O0OO0O00O =f'_innerId={int(_OO000000O0O0O00O0)}_{timi_new()}'#line:271
            OOO0O00O0O0O0OO00 ={'authorization':O0OO000O0OOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00O0OO0O00O ),'signstring':OOO00O00O0OO0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            O0OOOO000000OOO0O ={"innerId":int (_OO000000O0O0O00O0 )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO0O00O0O0O0OO00 ,data =O0OOOO000000OOO0O )#line:282
        except Exception as OOOOO0O0OO0O0O0OO :#line:283
            print (OOOOO0O0OO0O0O0OO )#line:284
    def winning_rewards (O000OO0O0O0OOO0O0 ):#line:287
        try :#line:288
            OOOOO000O0O000OO0 =f'__{timi_new()}'#line:289
            OOOOOO00000OO0O0O ={'authorization':O000OO0O0O0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO000O0O000OO0 ),'signstring':OOOOO000O0O000OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            O00OOO0OOOOOOOO0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOOOOO00000OO0O0O ).json ()#line:299
            if 'status'in O00OOO0OOOOOOOO0O :#line:301
                if O00OOO0OOOOOOOO0O ['status']==200 :#line:302
                    if O00OOO0OOOOOOOO0O ['data']['amount']:#line:303
                        OOOO0O00OO00OO00O =O00OOO0OOOOOOOO0O ['data']['amount']['gold']#line:304
                        return OOOO0O00OO00OO00O #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as OO0O00OOOOO0O0O0O :#line:308
            print (OO0O00OOOOO0O0O0O )#line:309
    def certification (OOOO0000OOOOO0OO0 ):#line:312
        try :#line:313
            O0OOO0O0OOOOOO0OO =f'__{timi_new()}'#line:314
            OO0OOO0OOO0O00000 ={'authorization':OOOO0000OOOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O0OOOOOO0OO ),'signstring':O0OOO0O0OOOOOO0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            O00O0000O000000O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0OOO0OOO0O00000 ).json ()#line:324
            if 'status'in O00O0000O000000O0 :#line:326
                if O00O0000O000000O0 ['status']==200 :#line:327
                    if O00O0000O000000O0 ['data']['result']:#line:328
                        O0OOO00O0OO00O000 =O00O0000O000000O0 ['data']['nick_name']#line:329
                        return O0OOO00O0OO00O000 #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as OOO0O00000O00O0O0 :#line:333
            print (OOO0O00000O00O0O0 )#line:334
    def crops_illustrated (OOOOO0OOO0O00O00O ):#line:337
        try :#line:338
            O0OOOO0000000OOO0 =f'__{timi_new()}'#line:339
            O0O00000OOOOO0O00 ={'authorization':OOOOO0OOO0O00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0000000OOO0 ),'signstring':O0OOOO0000000OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            OOO0OO0O0OO0O0OO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O00000OOOOO0O00 ).json ()#line:349
            if 'status'in OOO0OO0O0OO0O0OO0 :#line:351
                if OOO0OO0O0OO0O0OO0 ['status']==200 :#line:352
                    OOOO00O00O0O0O00O =OOO0OO0O0OO0O0OO0 ['data'][0 ]['crops']#line:353
                    for O0O0O000O0O00OO00 in OOOO00O00O0O0O00O :#line:354
                        if O0O0O000O0O00OO00 ['ill_clover_award']:#line:355
                            if float (O0O0O000O0O00OO00 ['ill_clover_award'])>1 :#line:356
                                if O0O0O000O0O00OO00 ['is_finish']:#line:357
                                    if not O0O0O000O0O00OO00 ['is_getit']:#line:358
                                        if OOOOO0OOO0O00O00O .certification ()!='未实名':#line:359
                                            O0OOOO0000000OOO0 =f'_award_level={O0O0O000O0O00OO00["level"]}_{timi_new()}'#line:360
                                            O0O00000OOOOO0O00 ={'authorization':OOOOO0OOO0O00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0000000OOO0 ),'signstring':O0OOOO0000000OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            OO00O0OOO000O0O0O ={"award_level":O0O0O000O0O00OO00 ['level']}#line:370
                                            O0O00OOO00OOOOO0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O00000OOOOO0O00 ,json =OO00O0OOO000O0O0O ).json ()#line:372
                                            if 'status'in O0O00OOO00OOOOO0O :#line:373
                                                if O0O00OOO00OOOOO0O ['status']==200 :#line:374
                                                    OOOOO0OOOOOOO0OOO =O0O00OOO00OOOOO0O ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{O0O0O000O0O00OO00["crop_name"]}成就丨奖励{OOOOO0OOOOOOO0OOO}叶子成功')#line:377
                                                if O0O00OOO00OOOOO0O ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{O0O00OOO00OOOOO0O["message"]}')#line:379
        except Exception as OOO000O0000000OOO :#line:380
            print (OOO000O0000000OOO )#line:381
    def watched_ad (OO0OO000O0OOO00OO ):#line:384
        try :#line:385
            OOO0000OO0OO00OOO =f'__{timi_new()}'#line:386
            O0O000OO0OOOO00OO ={'authorization':OO0OO000O0OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OO0OO00OOO ),'signstring':OOO0000OO0OO00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            O0O00O00O0OO0OO00 =requests .request ('get',f'{host}/game/getAllData',headers =O0O000OO0OOOO00OO ).json ()#line:396
            if 'status'in O0O00O00O0OO0OO00 :#line:398
                if O0O00O00O0OO0OO00 ['status']==200 :#line:399
                    if 'offlineInfo'in O0O00O00O0OO0OO00 ['data']:#line:400
                        O00000000OO000O00 =O0O00O00O0OO0OO00 ['data']['offlineInfo']['off_minute']#line:401
                        OOO0O0O0OO0O000O0 =float (O0O00O00O0OO0OO00 ['data']['silver'])/1000000000000 #line:402
                        time .sleep (1 )#line:403
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O000OO0OOOO00OO ).json ()#line:404
                        time .sleep (2 )#line:405
                        O00O000OO000OO000 =requests .request ('get',f'{host}/game/getAllData',headers =O0O000OO0OOOO00OO ).json ()#line:406
                        if 'status'in O00O000OO000OO000 :#line:408
                            if O00O000OO000OO000 ['status']==200 :#line:409
                                OOOO0OOOO00O0O0OO =float (O00O000OO000OO000 ['data']['silver'])/1000000000000 #line:410
                                OOOOO000O00OOOO00 =str (OOOO0OOOO00O0O0OO -OOO0O0O0OO0O000O0 )[:6 ]#line:411
                                print (f'【离线奖励】:翻倍离线{O00000000OO000O00}分钟奖励种子数量:{OOOOO000O00OOOO00}t粒')#line:412
        except Exception as O00OO0000OOO0O0OO :#line:413
            print (O00OO0000OOO0O0OO )#line:414
    def user_ad (O000000OOO0000OOO ):#line:417
        try :#line:418
            O000OO0O000O000OO =f'__{timi_new()}'#line:419
            O00OO0000O0O0OO0O ={'authorization':O000000OOO0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O000O000OO ),'signstring':O000OO0O000O000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:428
            O0O0000000O0O0OO0 =requests .request ('get',f'{host}/user/ad',headers =O00OO0000O0O0OO0O ).json ()#line:429
            if 'status'in O0O0000000O0O0OO0 :#line:431
                if O0O0000000O0O0OO0 ['status']==200 :#line:432
                    O0000000OO00OOOOO =O0O0000000O0O0OO0 ['data']['max_time']#line:433
                    OOOOOO000O0O00000 =O0O0000000O0O0OO0 ['data']['watch_time']#line:434
                    OO0OOO00000000OOO =O0O0000000O0O0OO0 ['data']['added_time']#line:435
                    print (f'【获取种子】:获取种子剩余{OO0OOO00000000OOO + O0000000OO00OOOOO - OOOOOO000O0O00000}次丨好友提供:{OO0OOO00000000OOO}次')#line:436
                    if OO0OOO00000000OOO +O0000000OO00OOOOO -OOOOOO000O0O00000 >0 :#line:437
                        time .sleep (random .randint (16 ,19 ))#line:438
                        OO00O000000O00O00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00OO0000O0O0OO0O ).json ()#line:439
                        if 'status'in OO00O000000O00O00 :#line:441
                            if OO00O000000O00O00 ['status']==200 :#line:442
                                OO00000OOO0O0OO0O =OO00O000000O00O00 ['data']['silver']#line:443
                                print (f'【获取种子】:获得种子:{OO00000OOO0O0OO0O}')#line:444
                                return True #line:445
                            if OO00O000000O00O00 ['status']==500 :#line:446
                                OOO0O00O0O000O0O0 =OO00O000000O00O00 ['message']#line:447
                                print (f'【获取种子】:{OOO0O00O0O000O0O0}')#line:448
                                return False #line:449
        except Exception as OOO0OOOOOO0O0O0O0 :#line:450
            print (OOO0OOOOOO0O0O0O0 )#line:451
    def synthetic (OO0O0O00OOOO00OO0 ):#line:454
        global id ,g #line:455
        try :#line:456
            OOOOO0O000O00O000 =OO0O0O00OOOO00OO0 .level_new ()#line:457
            OOOO0OOOOO0OO0O0O =random .randint (9 ,11 )#line:458
            OOO00O0OO0O0O0OO0 =f'_site=8&targetSite={OOOO0OOOOO0OO0O0O}_{timi_new()}'#line:459
            O0OOO00000O0OO00O ={'accept':'application/json, text/plain, */*','authorization':OO0O0O00OOOO00OO0 .token ,'timestamp':timi_new (),'sign':sign (OOO00O0OO0O0O0OO0 ),'signstring':OOO00O0OO0O0O0OO0 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:474
            OO0O000OO00000OOO ={"site":int (8 ),"targetSite":int (OOOO0OOOOO0OO0O0O )}#line:475
            requests .request ('post',f'{host}/game/crops/move',headers =O0OOO00000O0OO00O ,json =OO0O000OO00000OOO )#line:476
            while True :#line:477
                OOO0OOO0OOOOOOOOO =f'__{timi_new()}'#line:478
                OO0OO0OO00OOOO0O0 ={'authorization':OO0O0O00OOOO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OOOOOOOOO ),'signstring':OOO0OOO0OOOOOOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:487
                O00OO0000OOO00OOO =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO0OO00OOOO0O0 ).json ()#line:488
                if 'status'in O00OO0000OOO00OOO :#line:490
                    if O00OO0000OOO00OOO ['status']==200 :#line:491
                        OOOOOOO00OO0O00O0 =O00OO0000OOO00OOO ['data']['cropList']#line:492
                        OOO0O000OO00OOO0O =O00OO0000OOO00OOO ['data']['gameCoreDataDBid']#line:493
                        OO00OO00O00O0O000 =0 #line:494
                        for OO0000O0OO0O000O0 in OOOOOOO00OO0O00O0 :#line:495
                            if not OO0000O0OO0O000O0 :#line:496
                                OO0OO0000000OOO00 =f'_crop_id={OOO0O000OO00OOO0O}&site={OO00OO00O00O0O000}_{OO0O0O00OOOO00OO0.time}'#line:497
                                OOOO0OO0OO00000OO ={'authorization':OO0O0O00OOOO00OO0 .token ,'timestamp':OO0O0O00OOOO00OO0 .time ,'sign':sign (OO0OO0000000OOO00 ),'signstring':OO0OO0000000OOO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:506
                                O0O000O0OO0000O00 ={"site":OO00OO00O00O0O000 ,"crop_id":OOO0O000OO00OOO0O }#line:507
                                OO0OO0O00O0O0OO00 =requests .request ('post',f'{host}/game/crops/buy',headers =OOOO0OO0OO00000OO ,data =O0O000O0OO0000O00 ).json ()#line:508
                                time .sleep (random .randint (1 ,3 )/10 )#line:510
                                if 'status'in OO0OO0O00O0O0OO00 :#line:511
                                    if OO0OO0O00O0O0OO00 ['status']==200 :#line:512
                                        if OO0OO0O00O0O0OO00 ['message']=='种子数量不足':#line:513
                                            OOOOO0O000O00O000 =OO0O0O00OOOO00OO0 .level_new ()#line:514
                                            print (f'【种植合成】:{OO0OO0O00O0O0OO00["message"]}')#line:515
                                            if not OO0O0O00OOOO00OO0 .user_ad ():#line:516
                                                return False #line:517
                                    if OO0OO0O00O0O0OO00 ['status']==500 :#line:518
                                        print (f'【种植合成】:{OO0OO0O00O0O0OO00["message"]}')#line:519
                                        return False #line:520
                            OO00OO00O00O0O000 +=1 #line:521
                        OO000O0OOO000O000 =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO0OO00OOOO0O0 ).json ()#line:522
                        O0O0OO000O00OOO00 =OO000O0OOO000O000 ['data']['cropList']#line:523
                        O0OO00OOOO0O00OOO =False #line:524
                        for OO0000O0OO0O000O0 in range (12 ):#line:525
                            id =O0O0OO000O00OOO00 [OO0000O0OO0O000O0 ]['level']#line:526
                            if float (OOOOO0O000O00O000 )-float (id )>9 :#line:527
                                OO0OOOO0000O00000 =f'_site={OO0000O0OO0O000O0}_{timi_new()}'#line:528
                                O0O0000OO00000O0O ={'accept':'application/json, text/plain, */*','authorization':OO0O0O00OOOO00OO0 .token ,'timestamp':timi_new (),'sign':sign (OO0OOOO0000O00000 ),'signstring':OO0OOOO0000O00000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:538
                                O0OO000OOOOO00O00 ={"site":OO0000O0OO0O000O0 }#line:539
                                O0O0OO00OO0OOOOOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O0000OO00000O0O ,data =O0OO000OOOOO00O00 ).json ()#line:541
                                if 'status'in O0O0OO00OO0OOOOOO :#line:542
                                    if O0O0OO00OO0OOOOOO ['status']==200 :#line:543
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:544
                            if id !=0 :#line:545
                                for OO00O000O0O0OO00O in range (11 ):#line:546
                                    OO00O0OOOOOO0000O =OO00O000O0O0OO00O +1 #line:547
                                    g =O0O0OO000O00OOO00 [OO00O0OOOOOO0000O ]['level']#line:548
                                    if id ==g :#line:549
                                        OO0O00O0O0000OOO0 =OO00O000O0O0OO00O +2 #line:550
                                        if OO0O00O0O0000OOO0 !=OO0000O0OO0O000O0 +1 :#line:551
                                            OOO000OOO00O0OO0O =OO0000O0OO0O000O0 +1 #line:552
                                            time .sleep (random .randint (1 ,3 )/10 )#line:554
                                            OOO00O0OO0O0O0OO0 =f'_site={OOO000OOO00O0OO0O - 1}&targetSite={OO0O00O0O0000OOO0 - 1}_{timi_new()}'#line:555
                                            O0OOO00000O0OO00O ={'accept':'application/json, text/plain, */*','authorization':OO0O0O00OOOO00OO0 .token ,'timestamp':timi_new (),'sign':sign (OOO00O0OO0O0O0OO0 ),'signstring':OOO00O0OO0O0O0OO0 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:570
                                            O00OO00000O0OOO00 ={"site":int (OOO000OOO00O0OO0O -1 ),"targetSite":int (OO0O00O0O0000OOO0 -1 )}#line:571
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0OOO00000O0OO00O ,json =O00OO00000O0OOO00 )#line:572
                                            print (f'【种植合成】:位置{OOO000OOO00O0OO0O}和位置{OO0O00O0O0000OOO0}合出{int(id) + 1}级农作物')#line:573
                                            O0OO00OOOO0O00OOO =True #line:574
                                    if O0OO00OOOO0O00OOO :#line:575
                                        break #line:576
                                if O0OO00OOOO0O00OOO :#line:577
                                    break #line:578
        except :#line:579
            OO0O0O00OOOO00OO0 .synthetic ()#line:580
    def level_new (O00O00OO0OO00000O ):#line:583
        try :#line:584
            O0OOO0O000O0OO0O0 =f'__{timi_new()}'#line:585
            OO000OO0OOO00O000 ={'authorization':O00O00OO0OO00000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O000O0OO0O0 ),'signstring':O0OOO0O000O0OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:594
            O0O0OOO000000O0O0 =requests .request ('get',f'{host}/user',headers =OO000OO0OOO00O000 ).json ()#line:595
            if 'status'in O0O0OOO000000O0O0 :#line:596
                if O0O0OOO000000O0O0 ['status']==200 :#line:597
                    return float (O0O0OOO000000O0O0 ['data']['level'])#line:598
        except Exception as OOO00OO000O000O0O :#line:599
            print (OOO00OO000O000O0O )#line:600
    def propsraffle (OOOO0O0OO0O0O0OO0 ):#line:603
        try :#line:604
            while True :#line:605
                O0O0O000OOO0OOO00 =f'__{timi_new()}'#line:606
                O0O00O0OOO00OO000 ={'authorization':OOOO0O0OO0O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000OOO0OOO00 ),'signstring':O0O0O000OOO0OOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:615
                O00O00O0000O000O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O00O0OOO00OO000 ).json ()#line:616
                if 'status'in O00O00O0000O000O0 :#line:618
                    if O00O00O0000O000O0 ['status']==200 :#line:619
                        OOOO0O0OO0OO0O0OO =O00O00O0000O000O0 ['data']['rows']#line:620
                        O0OOOO000OOOOO00O =O00O00O0000O000O0 ['data']['vstate']#line:621
                        if OOOO0O0OO0OO0O0OO ==5 or OOOO0O0OO0OO0O0OO ==6 or OOOO0O0OO0OO0O0OO ==7 :#line:622
                            O0O000O0000OO00OO =O00O00O0000O000O0 ['data']['silver']#line:623
                            print (f'【转盘抽奖】:获得种子:{O0O000O0000OO00OO}')#line:624
                        if OOOO0O0OO0OO0O0OO ==1 or OOOO0O0OO0OO0O0OO ==2 or OOOO0O0OO0OO0O0OO ==3 :#line:625
                            O0OOO00OO00OO00O0 =O00O00O0000O000O0 ['data']['clover']#line:626
                            print (f'【转盘抽奖】:获得三叶草:{O0OOO00OO00OO00O0}')#line:627
                        if OOOO0O0OO0OO0O0OO ==4 or OOOO0O0OO0OO0O0OO ==8 :#line:628
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:629
                        if OOOO0O0OO0OO0O0OO =='抽奖次数已用完':#line:633
                            break #line:666
                time .sleep (random .randint (8 ,15 )/10 )#line:667
        except Exception as O0000O0OOO0O00OO0 :#line:668
            print (O0000O0OOO0O00OO0 )#line:669
    def friends_invitation (O00O0O00OO0O00OO0 ):#line:672
        try :#line:673
            OO0000OO00O00OO00 =f'__{timi_new()}'#line:674
            O00OO0O000O0OO0O0 ={'authorization':O00O0O00OO0O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OO00O00OO00 ),'signstring':OO0000OO00O00OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:683
            O0O000OOOOOO0O000 =requests .request ('get',f'{host}/friends',headers =O00OO0O000O0OO0O0 ).json ()#line:684
            if 'status'in O0O000OOOOOO0O000 :#line:685
                if O0O000OOOOOO0O000 ['status']==200 :#line:686
                    OO0000OO0OOOOOOO0 =O0O000OOOOOO0O000 ['data']['myInviteter']#line:687
                    if OO0000OO0OOOOOOO0 :#line:688
                        OOOO0OO000000OO00 =OO0000OO0OOOOOOO0 ['user']['nickname']#line:689
                        OO0O0O00OO0O00O0O =O00O0O00OO0O00OO0 .certification ()#line:690
                        print (f'【查邀请人】:我的邀请人:{OOOO0OO000000OO00}丨实名:{OO0O0O00OO0O00O0O}')#line:691
                    else :#line:692
                        if O00O0O00OO0O00OO0 .innerId !='0':#line:693
                            O00O0O00OO0O00OO0 .invitation ()#line:694
        except Exception as OO0OO00000O00OOOO :#line:695
            print (OO0OO00000O00OOOO )#line:696
    def add_clover (OO00000000O0O0OO0 ):#line:699
        global golden_seed #line:700
        try :#line:701
            O0OOO0000OO00OO00 =f'__{timi_new()}'#line:702
            OOOO00OO0000O00O0 ={'authorization':OO00000000O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000OO00OO00 ),'signstring':O0OOO0000OO00OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:711
            OOO00OOO0O0O00O00 =requests .request ('get',f'{host}/assets/clovers',headers =OOOO00OO0000O00O0 ).json ()#line:712
            if 'status'in OOO00OOO0O0O00O00 :#line:714
                if OOO00OOO0O0O00O00 ['status']==200 :#line:715
                    O0O00OO00O00O00OO =OOO00OOO0O0O00O00 ['data']['clover']#line:716
                    OO0O0O000O0O00O00 =OOO00OOO0O0O00O00 ['data']['used_clover']#line:717
                    O0O0OOOO0OO0O0O00 =float (O0O00OO00O00O00OO )-float (OO0O0O000O0O00O00 )#line:718
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OO0O0O000O0O00O00}')#line:719
                    if OO00000000O0O0OO0 .certification ()!='未实名':#line:720
                        if O0O0OOOO0OO0O0O00 >1 :#line:721
                            O0OOO0000OO00OO00 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O0OOOO0OO0O0O00)}_{timi_new()}'#line:722
                            O0O00O0O00OOO0O0O ={'authorization':OO00000000O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000OO00OO00 ),'signstring':O0OOO0000OO00OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:731
                            OO00OO00OOO0O00OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O0OOOO0OO0O0O00 )}#line:732
                            OOO00OOO00OO0O000 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O00O0O00OOO0O0O ,data =OO00OO00OOO0O00OO ).json ()#line:733
                            if 'status'in OOO00OOO00OO0O000 :#line:735
                                if OOO00OOO00OO0O000 ['status']==200 :#line:736
                                    print (f'【参与抽奖】:添加三叶草:{OOO00OOO00OO0O000["data"]}丨数量:{O0O0OOOO0OO0O0O00}')#line:737
                                if OOO00OOO00OO0O000 ['status']==500 :#line:738
                                    print (f'【参与抽奖】:添加三叶草:{OOO00OOO00OO0O000["message"]}')#line:739
            O000OOO000O0O0OO0 =requests .request ('get',f'{host}/lottery',headers =OOOO00OO0000O00O0 ).json ()#line:740
            O000000OOO0O000OO =OO00000000O0O0OO0 .winning_rewards ()#line:742
            if 'status'in O000OOO000O0O0OO0 :#line:743
                if O000OOO000O0O0OO0 ['status']==200 :#line:744
                    O0OOOOO0O0O0OO0O0 =O000OOO000O0O0OO0 ['data'][0 ]['day_get_gold_quantity']#line:745
                    golden_seed +=float (O0OOOOO0O0O0OO0O0 )#line:746
                    print (f'【参与抽奖】:预计每天中{str(O0OOOOO0O0O0OO0O0)[:6]}颗金种子丨好友收益:{str(O000000OOO0O000OO)[:6]}')#line:747
        except Exception as O0000O0O00OO0OO00 :#line:748
            print (O0000O0O00OO0OO00 )#line:749
    def energy (OO0OO00OO000OOO00 ):#line:753
        try :#line:754
            while True :#line:755
                OO00OO0OO00000OOO =f'__{timi_new()}'#line:756
                OOOO00O000OO0O0OO ={'authorization':OO0OO00OO000OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OO00000OOO ),'signstring':OO00OO0OO00000OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:765
                O0OO00O00OOOO0000 =requests .request ('get',f'{host}/energy/general',headers =OOOO00O000OO0O0OO ).json ()#line:766
                if 'status'in O0OO00O00OOOO0000 :#line:768
                    if O0OO00O00OOOO0000 ['status']==200 :#line:769
                        O00000OOO00000O0O =O0OO00O00OOOO0000 ['data']['ordinary_water']#line:770
                        O0O000O0000OOOOOO =O0OO00O00OOOO0000 ['data']['ordinary_fertilizer']#line:771
                        print (f'【我的营养】:肥料:{str(O0O000O0000OOOOOO).split(".")[0]}丨水滴:{str(O00000OOO00000O0O).split(".")[0]}')#line:773
                        if float (O0O000O0000OOOOOO )<96 :#line:774
                            time .sleep (random .randint (160 ,180 )/10 )#line:775
                            O0O0O0O0O0O00OO00 =99 -float (O0O000O0000OOOOOO )#line:776
                            OO000O0OOOO0OO000 ={"fertilizer":str (O0O0O0O0O0O00OO00 ).split ('.')[0 ]}#line:777
                            O00OO0OOO00OOO00O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOO00O000OO0O0OO ).json ()#line:778
                            if 'status'in O00OO0OOO00OOO00O :#line:780
                                if O00OO0OOO00OOO00O ['status']==200 :#line:781
                                    print (f'【购买肥料】:看广告获取肥料:{O00OO0OOO00OOO00O["message"]}')#line:782
                        if float (O00000OOO00000O0O )<880 :#line:783
                            time .sleep (random .randint (160 ,180 )/10 )#line:784
                            O00O00O0OOOO0O000 =999 -float (O00000OOO00000O0O )#line:785
                            OOOO000000O0O0OOO ={"water":str (O00O00O0OOOO0O000 ).split ('.')[0 ]}#line:786
                            O0O00OOOOOOO000OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOO00O000OO0O0OO ).json ()#line:787
                            if 'status'in O0O00OOOOOOO000OO :#line:789
                                if O0O00OOOOOOO000OO ['status']==200 :#line:790
                                    print (f'【购买水滴】:看广告获取水滴:{O0O00OOOOOOO000OO["message"]}')#line:791
                        if float (O0O000O0000OOOOOO )>96 and float (O00000OOO00000O0O )>880 :#line:792
                            break #line:793
        except Exception as OOO00OOO0OOOOOOOO :#line:795
            print (OOO00OOO0OOOOOOOO )#line:796
def bundled_def ():#line:798
    OOO0O0O0O000OOOO0 =['5570536','7750212','7911652','7911680','7805624']#line:799
    return OOO0O0O0O000OOOO0 [random .randint (0 ,len (OOO0O0O0O000OOOO0 )-1 )]#line:800
def version_of_the_validation ():#line:804
    return str ((77 -56 )/10 )#line:805
def gitee_validation ():#line:808
    try :#line:809
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:810
    except :#line:811
        sys .exit (0 )#line:812
def update_the_validation ():#line:816
    try :#line:817
        OO0OO00OO00OO0O0O =gitee_validation ()#line:818
        if version_of_the_validation ()<OO0OO00OO00OO0O0O ['CityEarth']['edition']:#line:819
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OO00OO00OO0O0O["CityEarth"]["edition"]}   ❌')#line:820
            print (f'更新内容=>>{OO0OO00OO00OO0O0O["CityEarth"]["content"]}   👍')#line:821
        else :#line:822
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OO00OO00OO0O0O["CityEarth"]["edition"]}   ✅')#line:823
            print (f'更新内容=>> {OO0OO00OO00OO0O0O["CityEarth"]["content"]}   👍')#line:824
    except Exception as OOO0OOO000000O0O0 :#line:825
        print (OOO0OOO000000O0O0 )#line:826
def os_qinglong ():#line:829
    if application in os .environ :#line:830
        O0OOOO0OOO0O00O00 =os .environ [application ].split ('\n')#line:831
        if len (O0OOOO0OOO0O00O00 )>0 :#line:832
            return O0OOOO0OOO0O00O00 #line:833
        else :#line:834
            print (f"{application}变量未启用")#line:835
            print ('脚本退出')#line:836
            sys .exit (1 )#line:837
    else :#line:838
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:840
        return os_built ()#line:841
def os_built ():#line:844
    if token :#line:845
        O0OOO0O0OOOOO000O =token .split ('\n')#line:846
        if len (O0OOO0O0OOOOO000O )>0 :#line:847
            return O0OOO0O0OOOOO000O #line:848
    else :#line:849
        print (f"内置变量为空")#line:850
        print ('脚本结束')#line:851
        sys .exit (0 )#line:852
if __name__ =='__main__':#line:855
    start ()#line:856
