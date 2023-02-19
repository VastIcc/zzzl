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
token = ''
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
        OO0O000O0OOOOOO0O =os_qinglong ()#line:10
        print (f"==========共找到{len(OO0O000O0OOOOOO0O)}个账号==========")#line:11
        for OO0000000O0OO0000 in OO0O000O0OOOOOO0O :#line:12
            OOO0O0OOO0O0OOO00 =[]#line:13
            print (f"------------正在执行第{OO0O000O0OOOOOO0O.index(OO0000000O0OO0000) + 1}个账号------------")#line:14
            O0O000O00OO0O0OO0 =CityEarth (OO0000000O0OO0000 ,OOO0O0OOO0O0OOO00 )#line:15
            def OOO0OO0OOOOO00OOO ():#line:17
                if O0O000O00OO0O0OO0 .base_info ():#line:19
                    O0O000O00OO0O0OO0 .sealing ()#line:21
                    O0O000O00OO0O0OO0 .invitenum ()#line:23
                    O0O000O00OO0O0OO0 .game_map ()#line:25
                    O0O000O00OO0O0OO0 .friends_invitation ()#line:27
                    O0O000O00OO0O0OO0 .add_clover ()#line:29
                    O0O000O00OO0O0OO0 .propsraffle ()#line:31
                    O0O000O00OO0O0OO0 .synthetic ()#line:33
                    O0O000O00OO0O0OO0 .crops_illustrated ()#line:35
                    O0O000O00OO0O0OO0 .give_gold ()#line:37
                    O0O000O00OO0O0OO0 .withdraw ()#line:39
                    O0O000O00OO0O0OO0 .energy ()#line:41
            OO0000OOOOOO0O0OO =threading .Thread (target =OOO0OO0OOOOO00OOO )#line:42
            OO0000OOOOOO0O0OO .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        OO0O0OO0OOOOOOOOO =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0O0OO0OOOOOOOOO +' ')#line:48
    except Exception as OO00OOOOOOO00OO0O :#line:49
        print (OO00OOOOOOO00OO0O )#line:50
def sign (O0OO000OOOOO0OOOO ):#line:53
    OO0O000O0O0O0OO0O =hashlib .md5 (O0OO000OOOOO0OOOO .encode ()).hexdigest ()#line:54
    O000O0OOO0OO0OO0O ="scsc%^&*"+OO0O000O0O0O0OO0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    O00O0OO0OOOO0O0O0 =hashlib .md5 (O000O0OOO0OO0OO0O .encode ()).hexdigest ()#line:56
    return O00O0OO0OOOO0O0O0 #line:57
def format_msg ():#line:59
    O00000000000OOO00 =""#line:60
    for OOOO00000OOO00000 in msg_list :#line:61
        O00000000000OOO00 +=str (OOOO00000OOO00000 )+"\r\n"#line:62
    return O00000000000OOO00 #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (O0O0O000OO0OO00O0 ,OOO0O00000O0OO0OO ,O00000OO00000OOO0 ):#line:71
        try :#line:72
            O0O0O000OO0OO00O0 .msg =O00000OO00000OOO0 #line:73
            O0O0O000OO0OO00O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            O0O0O000OO0OO00O0 .token =OOO0O00000O0OO0OO .split ('&')[0 ]#line:75
            O0O0O000OO0OO00O0 .innerId =OOO0O00000O0OO0OO .split ('&')[1 ]#line:76
            O0O0O000OO0OO00O0 .doneeNo =OOO0O00000O0OO0OO .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (OOOOO00OO0OOOO000 ):#line:82
        try :#line:83
            OOOOO00OO0OOOO000 .watched_ad ()#line:85
            OO0O00O0O00OO0000 =f'__{timi_new()}'#line:86
            O00O0O00O000000OO ={'authorization':OOOOO00OO0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O0O00OO0000 ),'signstring':OO0O00O0O00OO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            OO0OO0OOO0O0OO000 =requests .request ('get',f'{host}/user',headers =O00O0O00O000000OO ).json ()#line:96
            if 'status'in OO0OO0OOO0O0OO000 :#line:98
                if OO0OO0OOO0O0OO000 ['status']==200 :#line:99
                    OOOOOOOO0O0OOO0O0 =OO0OO0OOO0O0OO000 ['data']['nickname']#line:100
                    O00O00O000O0OOOOO =OO0OO0OOO0O0OO000 ['data']['inner_id']#line:101
                    OOO00O00000OO0O0O =OO0OO0OOO0O0OO000 ['data']['assets']['gold']#line:102
                    OOOO00OO0O0000OO0 =OO0OO0OOO0O0OO000 ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{OOOOOOOO0O0OOO0O0[:5]}丨ID:{O00O00O000O0OOOOO}丨等级:{OOOO00OO0O0000OO0}丨金种子:{str(OOO00O00000OO0O0O).split(".")[0]}')#line:104
                if OO0OO0OOO0O0OO000 ['status']==401 :#line:105
                    print (OO0OO0OOO0O0OO000 ['message'])#line:106
                    OOOOO00OO0OOOO000 .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if OO0OO0OOO0O0OO000 ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as O0O0OOOO00000OO00 :#line:112
            print (O0O0OOOO00000OO00 )#line:113
    def sealing (O00O0OO000OOOOOOO ):#line:116
        try :#line:117
            OO0OOOO00O00O0O00 =f'__{timi_new()}'#line:118
            OO0OOO000000OOO00 ={'authorization':O00O0OO000OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO00O00O0O00 ),'signstring':OO0OOOO00O00O0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0OOO000000OOO00 )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =OO0OOO000000OOO00 )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0OOO000000OOO00 )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0OOO000000OOO00 )#line:131
            requests .request ('get',f'{host}/user',headers =OO0OOO000000OOO00 )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0OOO000000OOO00 )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0OOO000000OOO00 )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0OOO000000OOO00 )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =OO0OOO000000OOO00 )#line:136
            requests .request ('get',f'{host}/assets',headers =OO0OOO000000OOO00 )#line:137
        except Exception as O0OOO0OO000OOO0O0 :#line:138
            print (O0OOO0OO000OOO0O0 )#line:139
    def withdraw (OO00O0OOO000OO000 ):#line:143
        OO0O000O0OOO00OOO =f'__{timi_new()}'#line:144
        O00OOOO00O000O00O ={'authorization':OO00O0OOO000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000O0OOO00OOO ),'signstring':OO0O000O0OOO00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        OO000O00OOO0O0000 =requests .request ('get',f'{host}/assets',headers =O00OOOO00O000O00O ).json ()#line:154
        if 'status'in OO000O00OOO0O0000 :#line:156
            if OO000O00OOO0O0000 ['status']==200 :#line:157
                OO0O00OOO00O00O00 =OO000O00OOO0O0000 ['data']['cash']#line:158
                if float (OO0O00OOO00O00O00 )>20 :#line:159
                    OO0O000O0OOO00OOO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    O00OOOO00O000O00O ={'authorization':OO00O0OOO000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000O0OOO00OOO ),'signstring':OO0O000O0OOO00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    O00000O000OO0O000 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    OO00OOOO000O0OOO0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00OOOO00O000O00O ,data =O00000O000OO0O000 ).json ()#line:172
                    print (OO00OOOO000O0OOO0 )#line:173
    def invitenum (O0OOOO000O0O0OO00 ):#line:176
        O00O000OOOOOO0000 =f'__{timi_new()}'#line:177
        OOOOO00O0OO0000O0 ={'authorization':O0OOOO000O0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OOOOOO0000 ),'signstring':O00O000OOOOOO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        OO0OO0O00OOOOO00O =requests .request ('get',f'{host}/invite/invitenum',headers =OOOOO00O0OO0000O0 ).json ()#line:187
        if 'status'in OO0OO0O00OOOOO00O :#line:189
            if OO0OO0O00OOOOO00O ['status']==200 :#line:190
                O000OOO0OOO0O000O =OO0OO0O00OOOOO00O ['data']['invited_count']#line:191
                O00OO00OO0O00OOO0 =OO0OO0O00OOOOO00O ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{O000OOO0OOO0O000O}丨间邀好友:{O00OO00OO0O00OOO0}')#line:193
    def game_map (OO00OO0O0OO000OO0 ):#line:196
        try :#line:197
            OOOOOO000O000O0OO =f'__{timi_new()}'#line:198
            OO0000OO00O0OOO0O ={'authorization':OO00OO0O0OO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO000O000O0OO ),'signstring':OOOOOO000O000O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            O00O0OOOOOOOO0O00 =requests .request ('get',f'{host}/game/map',headers =OO0000OO00O0OOO0O ).json ()#line:208
            if 'status'in O00O0OOOOOOOO0O00 :#line:210
                if O00O0OOOOOOOO0O00 ['status']==200 :#line:211
                    for OO0O0O000000O0OOO in O00O0OOOOOOOO0O00 ['data']['list'][0 ]['crops']:#line:212
                        OO00O00O0OOOOO0O0 =OO0O0O000000O0OOO ['level']#line:214
                        if OO00O00O0OOOOO0O0 ==41 :#line:215
                            O000OOOOO000O0OOO =OO0O0O000000O0OOO ['crop_name']#line:216
                            OOOOO00O0OOOO0O00 =OO0O0O000000O0OOO ['count']#line:217
                            if OOOOO00O0OOOO0O00 >0 :#line:218
                                print (f'【农业资产】:{O000OOOOO000O0OOO}丨数量:{OOOOO00O0OOOO0O00}')#line:219
        except Exception as O0OO0OO0000OO00OO :#line:220
            print (O0OO0OO0000OO00OO )#line:221
    def give_gold (OOOO0OO00OO000O0O ):#line:224
        try :#line:225
            OO0O00O000O0O000O =f'__{timi_new()}'#line:226
            OOO000OO0O0O0O0O0 ={'authorization':OOOO0OO00OO000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O000O0O000O ),'signstring':OO0O00O000O0O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            O0O0OO0OO0O00OOOO =requests .request ('get',f'{host}/user',headers =OOO000OO0O0O0O0O0 ).json ()#line:236
            if 'status'in O0O0OO0OO0O00OOOO :#line:237
                if O0O0OO0OO0O00OOOO ['status']==200 :#line:238
                    if float (OOOO0OO00OO000O0O .doneeNo )!=0 :#line:239
                        O00000O00O0000OOO =O0O0OO0OO0O00OOOO ['data']['assets']['gold']#line:240
                        if float (O00000O00O0000OOO )>float (OOOO0OO00OO000O0O .innerId ):#line:241
                            O0O0OOO0000O0O000 =int (float (O00000O00O0000OOO )/1.1 )#line:242
                            OO0O00O000O0O000O =f'_doneeNo={OOOO0OO00OO000O0O.doneeNo}&quantity={O0O0OOO0000O0O000}_{timi_new()}'#line:243
                            OOO000OO0O0O0O0O0 ={'authorization':OOOO0OO00OO000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O000O0O000O ),'signstring':OO0O00O000O0O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            O0OO000OO0O0OOOOO ={"quantity":O0O0OOO0000O0O000 ,"doneeNo":OOOO0OO00OO000O0O .doneeNo }#line:256
                            OO0000OOO0OOOO0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO000OO0O0O0O0O0 ,data =O0OO000OO0O0OOOOO ).json ()#line:257
                            if 'status'in OO0000OOO0OOOO0O0 :#line:259
                                if OO0000OOO0OOOO0O0 ['status']==200 :#line:260
                                    if OO0000OOO0OOOO0O0 ['data']:#line:261
                                        print (f'【赠送种子】:赠送{O0O0OOO0000O0O000}种子给{OOOO0OO00OO000O0O.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as O0O0OO0O0OOO00O00 :#line:265
            print (O0O0OO0O0OOO00O00 )#line:266
    def invitation (O0000000O000O00O0 ):#line:268
        try :#line:269
            _O0OOOO00OOOOO0OO0 =float (bundled_def ())/4 #line:270
            OO000O0OOOO000O00 =f'_innerId={int(_O0OOOO00OOOOO0OO0)}_{timi_new()}'#line:271
            OOOO00O00O00O00O0 ={'authorization':O0000000O000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0OOOO000O00 ),'signstring':OO000O0OOOO000O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            OO0O00O00OO0OO0OO ={"innerId":int (_O0OOOO00OOOOO0OO0 )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOO00O00O00O00O0 ,data =OO0O00O00OO0OO0OO )#line:282
        except Exception as O00O00000OO00O0OO :#line:283
            print (O00O00000OO00O0OO )#line:284
    def winning_rewards (O00O0O0O0OOO00O0O ):#line:287
        try :#line:288
            O0OO00O000000O00O =f'__{timi_new()}'#line:289
            O0O0O0000000OOOOO ={'authorization':O00O0O0O0OOO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O000000O00O ),'signstring':O0OO00O000000O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            O0O0O0OOOOO0OOO00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O0O0000000OOOOO ).json ()#line:299
            if 'status'in O0O0O0OOOOO0OOO00 :#line:301
                if O0O0O0OOOOO0OOO00 ['status']==200 :#line:302
                    if O0O0O0OOOOO0OOO00 ['data']['amount']:#line:303
                        OOO0OO0OOO0O0O000 =O0O0O0OOOOO0OOO00 ['data']['amount']['gold']#line:304
                        return OOO0OO0OOO0O0O000 #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as OOO0O0OO0O0OO0O0O :#line:308
            print (OOO0O0OO0O0OO0O0O )#line:309
    def certification (OOOO0O00OO00O000O ):#line:312
        try :#line:313
            OO0OOOO0000O00000 =f'__{timi_new()}'#line:314
            O00OO0O00OO0OO000 ={'authorization':OOOO0O00OO00O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0000O00000 ),'signstring':OO0OOOO0000O00000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            O0OO00O0OOO00OO00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OO0O00OO0OO000 ).json ()#line:324
            if 'status'in O0OO00O0OOO00OO00 :#line:326
                if O0OO00O0OOO00OO00 ['status']==200 :#line:327
                    if O0OO00O0OOO00OO00 ['data']['result']:#line:328
                        OO000OOOOOO0O00OO =O0OO00O0OOO00OO00 ['data']['nick_name']#line:329
                        return OO000OOOOOO0O00OO #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as OOOOOOO0O0OOO0OOO :#line:333
            print (OOOOOOO0O0OOO0OOO )#line:334
    def crops_illustrated (OOO0000O00OO00O0O ):#line:337
        try :#line:338
            O0O0000OO0O000OOO =f'__{timi_new()}'#line:339
            O0O00O0O0O0OOO00O ={'authorization':OOO0000O00OO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OO0O000OOO ),'signstring':O0O0000OO0O000OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            OOOO0O0O0OOO00OOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O00O0O0O0OOO00O ).json ()#line:349
            if 'status'in OOOO0O0O0OOO00OOO :#line:351
                if OOOO0O0O0OOO00OOO ['status']==200 :#line:352
                    O0O0O000OOOO0OO00 =OOOO0O0O0OOO00OOO ['data'][0 ]['crops']#line:353
                    for O00000OOO00OO0O0O in O0O0O000OOOO0OO00 :#line:354
                        if O00000OOO00OO0O0O ['ill_clover_award']:#line:355
                            if float (O00000OOO00OO0O0O ['ill_clover_award'])>1 :#line:356
                                if O00000OOO00OO0O0O ['is_finish']:#line:357
                                    if not O00000OOO00OO0O0O ['is_getit']:#line:358
                                        if OOO0000O00OO00O0O .certification ()!='未实名':#line:359
                                            O0O0000OO0O000OOO =f'_award_level={O00000OOO00OO0O0O["level"]}_{timi_new()}'#line:360
                                            O0O00O0O0O0OOO00O ={'authorization':OOO0000O00OO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OO0O000OOO ),'signstring':O0O0000OO0O000OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            O0000OO0OOO0OO0OO ={"award_level":O00000OOO00OO0O0O ['level']}#line:370
                                            OOO0OO0O0O0OO0O00 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O00O0O0O0OOO00O ,json =O0000OO0OOO0OO0OO ).json ()#line:372
                                            if 'status'in OOO0OO0O0O0OO0O00 :#line:373
                                                if OOO0OO0O0O0OO0O00 ['status']==200 :#line:374
                                                    OOO00OOO0OOO0O0O0 =OOO0OO0O0O0OO0O00 ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{O00000OOO00OO0O0O["crop_name"]}成就丨奖励{OOO00OOO0OOO0O0O0}☘️')#line:377
                                                if OOO0OO0O0O0OO0O00 ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{OOO0OO0O0O0OO0O00["message"]}')#line:379
        except Exception as O0O0OOOOOOO0OO00O :#line:380
            print (O0O0OOOOOOO0OO00O )#line:381
    def watched_ad (O0000OO0O00000O0O ):#line:384
        try :#line:385
            O0O00000OO0OOO0O0 =f'__{timi_new()}'#line:386
            OO0OOO000OOO0O0O0 ={'authorization':O0000OO0O00000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000OO0OOO0O0 ),'signstring':O0O00000OO0OOO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            OOOO0O0OO00OOO00O =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOO000OOO0O0O0 ).json ()#line:396
            if 'status'in OOOO0O0OO00OOO00O :#line:398
                if OOOO0O0OO00OOO00O ['status']==200 :#line:399
                    if 'offlineInfo'in OOOO0O0OO00OOO00O ['data']:#line:400
                        time .sleep (random .randint (3 ,5 ))#line:401
                        O0O0O0OO0OOO0O0OO =OOOO0O0OO00OOO00O ['data']['offlineInfo']['off_minute']#line:402
                        O00O0O00OO00OO00O =float (OOOO0O0OO00OOO00O ['data']['silver'])/1000000000000 #line:403
                        time .sleep (1 )#line:404
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0OOO000OOO0O0O0 ).json ()#line:405
                        time .sleep (2 )#line:406
                        OO0O0O000000OO0OO =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOO000OOO0O0O0 ).json ()#line:407
                        if 'status'in OO0O0O000000OO0OO :#line:409
                            if OO0O0O000000OO0OO ['status']==200 :#line:410
                                OOO0OOOO00O00OOOO =float (OO0O0O000000OO0OO ['data']['silver'])/1000000000000 #line:411
                                O0OO0OOOOOOO000O0 =str (OOO0OOOO00O00OOOO -O00O0O00OO00OO00O )[:6 ]#line:412
                                print (f'【离线奖励】:翻倍离线{O0O0O0OO0OOO0O0OO}分钟奖励🌱数量:{O0OO0OOOOOOO000O0}t粒')#line:413
        except Exception as OO00OO0OO0OOOO000 :#line:414
            print (OO00OO0OO0OOOO000 )#line:415
    def user_ad (O0OOOOOO00O000O00 ):#line:418
        try :#line:419
            O000OO0OOO00OOOO0 =f'__{timi_new()}'#line:420
            O0O0OOOOO0OO00O0O ={'authorization':O0OOOOOO00O000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0OOO00OOOO0 ),'signstring':O000OO0OOO00OOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:429
            O0O0O000OOOOO000O =requests .request ('get',f'{host}/user/ad',headers =O0O0OOOOO0OO00O0O ).json ()#line:430
            if 'status'in O0O0O000OOOOO000O :#line:432
                if O0O0O000OOOOO000O ['status']==200 :#line:433
                    OOO00OO0O0O0OO0OO =O0O0O000OOOOO000O ['data']['max_time']#line:434
                    O0OO00OOOO00000OO =O0O0O000OOOOO000O ['data']['watch_time']#line:435
                    OOO00OOO0O0O00000 =O0O0O000OOOOO000O ['data']['added_time']#line:436
                    print (f'【获取种子】:获取🌱剩余{OOO00OOO0O0O00000 + OOO00OO0O0O0OO0OO - O0OO00OOOO00000OO}次丨好友提供:{OOO00OOO0O0O00000}次')#line:437
                    if OOO00OOO0O0O00000 +OOO00OO0O0O0OO0OO -O0OO00OOOO00000OO >0 :#line:438
                        time .sleep (random .randint (16 ,19 ))#line:439
                        OOOOOO00O0O0OO0OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O0OOOOO0OO00O0O ).json ()#line:440
                        if 'status'in OOOOOO00O0O0OO0OO :#line:442
                            if OOOOOO00O0O0OO0OO ['status']==200 :#line:443
                                O0OO000O0OO000OO0 =float (OOOOOO00O0O0OO0OO ['data']['silver'])/1000000000000 #line:444
                                print (f'【获取种子】:获得🌱:{int(O0OO000O0OO000OO0)}t粒')#line:445
                                return True #line:446
                            if OOOOOO00O0O0OO0OO ['status']==500 :#line:447
                                OO00000OOO00O0O0O =OOOOOO00O0O0OO0OO ['message']#line:448
                                print (f'【获取种子】:{OO00000OOO00O0O0O}')#line:449
                                return False #line:450
        except Exception as O00000OO00OOOO0O0 :#line:451
            print (O00000OO00OOOO0O0 )#line:452
    def synthetic (O0000000OO00OO00O ):#line:455
        global id ,g #line:456
        try :#line:457
            OO00OOOOO00000O00 =O0000000OO00OO00O .level_new ()#line:458
            O0OOO000O000OO000 =random .randint (9 ,11 )#line:459
            OOO0OOOO00O00O000 =f'_site=8&targetSite={O0OOO000O000OO000}_{timi_new()}'#line:460
            O0OOOOOO00O0OO00O ={'accept':'application/json, text/plain, */*','authorization':O0000000OO00OO00O .token ,'timestamp':timi_new (),'sign':sign (OOO0OOOO00O00O000 ),'signstring':OOO0OOOO00O00O000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:475
            OOOOOOOOO0O00000O ={"site":int (8 ),"targetSite":int (O0OOO000O000OO000 )}#line:476
            requests .request ('post',f'{host}/game/crops/move',headers =O0OOOOOO00O0OO00O ,json =OOOOOOOOO0O00000O )#line:477
            while True :#line:478
                OOO0O0OO0OO0OO0OO =f'__{timi_new()}'#line:479
                OOOOO0OOOO0000OO0 ={'authorization':O0000000OO00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO0OO0OO0OO ),'signstring':OOO0O0OO0OO0OO0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                OO0O00000OO0O0OOO =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO0OOOO0000OO0 ).json ()#line:489
                if 'status'in OO0O00000OO0O0OOO :#line:491
                    if OO0O00000OO0O0OOO ['status']==200 :#line:492
                        OO0O00O0O00000OOO =OO0O00000OO0O0OOO ['data']['cropList']#line:493
                        OOO0OO00O0OOOO0O0 =OO0O00000OO0O0OOO ['data']['gameCoreDataDBid']#line:494
                        O0OOO00OO0OO000OO =float (OO0O00000OO0O0OOO ['data']['silver'])/1000000000000 #line:495
                        OO00O0OO0O00O00O0 =0 #line:500
                        for OOOOO0000O0OOOO0O in OO0O00O0O00000OOO :#line:501
                            if not OOOOO0000O0OOOO0O :#line:502
                                OOOOOOO0O0O00000O =f'_crop_id={OOO0OO00O0OOOO0O0}&site={OO00O0OO0O00O00O0}_{O0000000OO00OO00O.time}'#line:503
                                OOOO000O00000O0O0 ={'authorization':O0000000OO00OO00O .token ,'timestamp':O0000000OO00OO00O .time ,'sign':sign (OOOOOOO0O0O00000O ),'signstring':OOOOOOO0O0O00000O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
                                OO000000O0000OO00 ={"site":OO00O0OO0O00O00O0 ,"crop_id":OOO0OO00O0OOOO0O0 }#line:513
                                OO00O0O00O000OO00 =requests .request ('post',f'{host}/game/crops/buy',headers =OOOO000O00000O0O0 ,data =OO000000O0000OO00 ).json ()#line:514
                                time .sleep (random .randint (1 ,3 )/10 )#line:516
                                if 'status'in OO00O0O00O000OO00 :#line:517
                                    if OO00O0O00O000OO00 ['status']==200 :#line:518
                                        if OO00O0O00O000OO00 ['message']=='种子数量不足':#line:519
                                            OO00OOOOO00000O00 =O0000000OO00OO00O .level_new ()#line:520
                                            print (f'【种植合成】:{OO00O0O00O000OO00["message"]}')#line:521
                                            if not O0000000OO00OO00O .user_ad ():#line:522
                                                return False #line:523
                                    if OO00O0O00O000OO00 ['status']==500 :#line:524
                                        print (f'【种植合成】:{OO00O0O00O000OO00["message"]}')#line:525
                                        return False #line:526
                            OO00O0OO0O00O00O0 +=1 #line:527
                        O0OO00000OO0OO00O =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO0OOOO0000OO0 ).json ()#line:528
                        OOOOO0O0OO0OO0O0O =O0OO00000OO0OO00O ['data']['cropList']#line:529
                        O00O0O0O0O00OOO00 =False #line:530
                        for OOOOO0000O0OOOO0O in range (12 ):#line:531
                            id =OOOOO0O0OO0OO0O0O [OOOOO0000O0OOOO0O ]['level']#line:532
                            if float (OO00OOOOO00000O00 )-float (id )>9 :#line:533
                                O0O0OO0000O0OO0OO =f'_site={OOOOO0000O0OOOO0O}_{timi_new()}'#line:534
                                OO000O0O0O00O0OOO ={'accept':'application/json, text/plain, */*','authorization':O0000000OO00OO00O .token ,'timestamp':timi_new (),'sign':sign (O0O0OO0000O0OO0OO ),'signstring':O0O0OO0000O0OO0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:544
                                O0OO000O0OOOOO0O0 ={"site":OOOOO0000O0OOOO0O }#line:545
                                OO00O0O00OO0OO0OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO000O0O0O00O0OOO ,data =O0OO000O0OOOOO0O0 ).json ()#line:547
                                if 'status'in OO00O0O00OO0OO0OO :#line:548
                                    if OO00O0O00OO0OO0OO ['status']==200 :#line:549
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:550
                            if id !=0 :#line:551
                                for OOOOOO00OO0O000OO in range (11 ):#line:552
                                    OOO0O0O0OOOO000OO =OOOOOO00OO0O000OO +1 #line:553
                                    g =OOOOO0O0OO0OO0O0O [OOO0O0O0OOOO000OO ]['level']#line:554
                                    if id ==g :#line:555
                                        O00OOO00000000O00 =OOOOOO00OO0O000OO +2 #line:556
                                        if O00OOO00000000O00 !=OOOOO0000O0OOOO0O +1 :#line:557
                                            O0OO0O000O00OOOO0 =OOOOO0000O0OOOO0O +1 #line:558
                                            time .sleep (random .randint (1 ,3 )/10 )#line:560
                                            OOO0OOOO00O00O000 =f'_site={O0OO0O000O00OOOO0 - 1}&targetSite={O00OOO00000000O00 - 1}_{timi_new()}'#line:561
                                            O0OOOOOO00O0OO00O ={'accept':'application/json, text/plain, */*','authorization':O0000000OO00OO00O .token ,'timestamp':timi_new (),'sign':sign (OOO0OOOO00O00O000 ),'signstring':OOO0OOOO00O00O000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:576
                                            OO0O000O0O0O0OOOO ={"site":int (O0OO0O000O00OOOO0 -1 ),"targetSite":int (O00OOO00000000O00 -1 )}#line:577
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0OOOOOO00O0OO00O ,json =OO0O000O0O0O0OOOO )#line:578
                                            O00O0O0O0O00OOO00 =True #line:580
                                    if O00O0O0O0O00OOO00 :#line:581
                                        break #line:582
                                if O00O0O0O0O00OOO00 :#line:583
                                    break #line:584
        except :#line:585
            O0000000OO00OO00O .synthetic ()#line:586
    def level_new (OO00OO00OO00000O0 ):#line:589
        try :#line:590
            OO0O00OO00O000O00 =f'__{timi_new()}'#line:591
            O00OO00O0OO0O0OO0 ={'authorization':OO00OO00OO00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OO00O000O00 ),'signstring':OO0O00OO00O000O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            O0OOOO0OOOO0OOO00 =requests .request ('get',f'{host}/user',headers =O00OO00O0OO0O0OO0 ).json ()#line:601
            if 'status'in O0OOOO0OOOO0OOO00 :#line:602
                if O0OOOO0OOOO0OOO00 ['status']==200 :#line:603
                    return float (O0OOOO0OOOO0OOO00 ['data']['level'])#line:604
        except Exception as OO0O0OO0O0O0O00OO :#line:605
            print (OO0O0OO0O0O0O00OO )#line:606
    def propsraffle (O00000OO0000OOO00 ):#line:609
        try :#line:610
            while True :#line:611
                O0O0OO0O00OO0O00O =f'__{timi_new()}'#line:612
                O0000O00O0OOOOO0O ={'authorization':O00000OO0000OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O00OO0O00O ),'signstring':O0O0OO0O00OO0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:621
                OO00OOOOO0OO00O00 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0000O00O0OOOOO0O ).json ()#line:622
                if 'status'in OO00OOOOO0OO00O00 :#line:624
                    if OO00OOOOO0OO00O00 ['status']==200 :#line:625
                        O00OOO0OOOO000O00 =OO00OOOOO0OO00O00 ['data']['rows']#line:626
                        OO00OO000OO0OO0O0 =OO00OOOOO0OO00O00 ['data']['vstate']#line:627
                        if O00OOO0OOOO000O00 ==5 or O00OOO0OOOO000O00 ==6 or O00OOO0OOOO000O00 ==7 :#line:628
                            OO0O0OOO00OO00000 =OO00OOOOO0OO00O00 ['data']['silver']#line:629
                            print (f'【转盘抽奖】:获得种子:{OO0O0OOO00OO00000}')#line:630
                        if O00OOO0OOOO000O00 ==1 or O00OOO0OOOO000O00 ==2 or O00OOO0OOOO000O00 ==3 :#line:631
                            O0O0OO0OOOO0OO0OO =OO00OOOOO0OO00O00 ['data']['clover']#line:632
                            print (f'【转盘抽奖】:获得三叶草:{O0O0OO0OOOO0OO0OO}')#line:633
                        if O00OOO0OOOO000O00 ==4 or O00OOO0OOOO000O00 ==8 :#line:634
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:635
                        if O00OOO0OOOO000O00 =='抽奖次数已用完':#line:639
                            break #line:672
                time .sleep (random .randint (8 ,15 )/10 )#line:673
        except Exception as OOOO0OOO000O00O0O :#line:674
            print (OOOO0OOO000O00O0O )#line:675
    def friends_invitation (OOO0O000O000O0OO0 ):#line:678
        try :#line:679
            O00O0OOOOOO0OOO00 =f'__{timi_new()}'#line:680
            OOO000O00OOOOOOO0 ={'authorization':OOO0O000O000O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOOOOO0OOO00 ),'signstring':O00O0OOOOOO0OOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:689
            OO0OO0OOOOO000OOO =requests .request ('get',f'{host}/friends',headers =OOO000O00OOOOOOO0 ).json ()#line:690
            if 'status'in OO0OO0OOOOO000OOO :#line:691
                if OO0OO0OOOOO000OOO ['status']==200 :#line:692
                    OO00O00O00O00OO00 =OO0OO0OOOOO000OOO ['data']['myInviteter']#line:693
                    if OO00O00O00O00OO00 :#line:694
                        OOOO0000OO0000OO0 =OO00O00O00O00OO00 ['user']['nickname']#line:695
                        O0000000OO00O0000 =OOO0O000O000O0OO0 .certification ()#line:696
                        print (f'【查邀请人】:我的邀请人:{OOOO0000OO0000OO0}丨实名:{O0000000OO00O0000}')#line:697
                    else :#line:698
                        if OOO0O000O000O0OO0 .innerId !='0':#line:699
                            OOO0O000O000O0OO0 .invitation ()#line:700
        except Exception as OOO0O0OOO000OOO0O :#line:701
            print (OOO0O0OOO000OOO0O )#line:702
    def add_clover (OO000000OOO00O000 ):#line:705
        global golden_seed #line:706
        try :#line:707
            O0O00OOO00OO00OOO =f'__{timi_new()}'#line:708
            OO00O000O0OOOOO00 ={'authorization':OO000000OOO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO00OO00OOO ),'signstring':O0O00OOO00OO00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:717
            OO0O0O00OO0O00000 =requests .request ('get',f'{host}/assets/clovers',headers =OO00O000O0OOOOO00 ).json ()#line:718
            if 'status'in OO0O0O00OO0O00000 :#line:720
                if OO0O0O00OO0O00000 ['status']==200 :#line:721
                    OO00O0O0OOO0O0000 =OO0O0O00OO0O00000 ['data']['clover']#line:722
                    OOOOO000000OOO00O =OO0O0O00OO0O00000 ['data']['used_clover']#line:723
                    OO0OO0OOO0OO0000O =float (OO00O0O0OOO0O0000 )-float (OOOOO000000OOO00O )#line:724
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOOOO000000OOO00O}')#line:725
                    if OO000000OOO00O000 .certification ()!='未实名':#line:726
                        if OO0OO0OOO0OO0000O >1 :#line:727
                            O0O00OOO00OO00OOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0OO0OOO0OO0000O)}_{timi_new()}'#line:728
                            O0OO0OO0OO0O0OOOO ={'authorization':OO000000OOO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO00OO00OOO ),'signstring':O0O00OOO00OO00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                            OO00O00OO00OO0O00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0OO0OOO0OO0000O )}#line:738
                            OOO0O0OOO00OO000O =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OO0OO0OO0O0OOOO ,data =OO00O00OO00OO0O00 ).json ()#line:739
                            if 'status'in OOO0O0OOO00OO000O :#line:741
                                if OOO0O0OOO00OO000O ['status']==200 :#line:742
                                    print (f'【参与抽奖】:添加☘️:{OOO0O0OOO00OO000O["data"]}丨数量:{OO0OO0OOO0OO0000O}')#line:743
                                if OOO0O0OOO00OO000O ['status']==500 :#line:744
                                    print (f'【参与抽奖】:添加☘️:{OOO0O0OOO00OO000O["message"]}')#line:745
            O000OO00OOOO0O0O0 =requests .request ('get',f'{host}/lottery',headers =OO00O000O0OOOOO00 ).json ()#line:746
            O0O000OOO0O0O0OOO =OO000000OOO00O000 .winning_rewards ()#line:748
            if 'status'in O000OO00OOOO0O0O0 :#line:749
                if O000OO00OOOO0O0O0 ['status']==200 :#line:750
                    OOOO0000OOOO00OO0 =O000OO00OOOO0O0O0 ['data'][0 ]['day_get_gold_quantity']#line:751
                    golden_seed +=float (OOOO0000OOOO00OO0 )#line:752
                    O000OOOOO00OO00O0 =O000OO00OOOO0O0O0 ['data'][1 ]['value']#line:753
                    OOO0O000O0000O0OO =O000OO00OOOO0O0O0 ['data'][0 ]['join_number']#line:754
                    O0OO0O00OO0000000 =int (float (O000OO00OOOO0O0O0 ['data'][0 ]['totalValue']))#line:755
                    O0O0O0O0O0OO0000O =float (O000OOOOO00OO00O0 /O0OO0O00OO0000000 )*10000 #line:756
                    OOOOO0O00O0OO000O =O0OO0O00OO0000000 /OOO0O000O0000O0OO #line:757
                    print (f'【参与抽奖】:预计每天中{str(OOOO0000OOOO00OO0)[:6]}颗金种子丨好友收益:{str(O0O000OOO0O0O0OOO)[:6]}')#line:758
                    print (f'【抽奖统计】:每1万☘️中{str(O0O0O0O0O0OO0000O)[:6]}颗金种子丨☘️人均:{str(OOOOO0O00O0OO000O)[:7]}️')#line:759
        except Exception as O00O00O00O00O0O00 :#line:760
            print (O00O00O00O00O0O00 )#line:761
    def energy (OO0O0OO00OO0OO0O0 ):#line:765
        try :#line:766
            while True :#line:767
                O00000OOOO00OOOO0 =f'__{timi_new()}'#line:768
                O000OOOOOO00OO0O0 ={'authorization':OO0O0OO00OO0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOOO00OOOO0 ),'signstring':O00000OOOO00OOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:777
                O000O000OOOOOO0OO =requests .request ('get',f'{host}/energy/general',headers =O000OOOOOO00OO0O0 ).json ()#line:778
                if 'status'in O000O000OOOOOO0OO :#line:780
                    if O000O000OOOOOO0OO ['status']==200 :#line:781
                        OO00000OO0O0OO0O0 =O000O000OOOOOO0OO ['data']['ordinary_water']#line:782
                        O000O00O00O00O00O =O000O000OOOOOO0OO ['data']['ordinary_fertilizer']#line:783
                        print (f'【我的营养】:肥料:{str(O000O00O00O00O00O).split(".")[0]}丨水滴:{str(OO00000OO0O0OO0O0).split(".")[0]}')#line:785
                        if float (O000O00O00O00O00O )<96 :#line:786
                            time .sleep (random .randint (160 ,180 )/10 )#line:787
                            OO0000O00OO0O00O0 =99 -float (O000O00O00O00O00O )#line:788
                            OOOO00000OO000O0O ={"fertilizer":str (OO0000O00OO0O00O0 ).split ('.')[0 ]}#line:789
                            OOOO0O0OO000O0O00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O000OOOOOO00OO0O0 ).json ()#line:790
                            if 'status'in OOOO0O0OO000O0O00 :#line:792
                                if OOOO0O0OO000O0O00 ['status']==200 :#line:793
                                    print (f'【购买肥料】:看广告获取肥料:{OOOO0O0OO000O0O00["message"]}')#line:794
                                if OOOO0O0OO000O0O00 ['status']==500 :#line:795
                                    print (f'【购买肥料】:看广告获取肥料:{OOOO0O0OO000O0O00["message"]}')#line:796
                                    break #line:797
                        if float (OO00000OO0O0OO0O0 )<880 :#line:798
                            time .sleep (random .randint (160 ,180 )/10 )#line:799
                            OO0OO0OOOO0OOOO00 =999 -float (OO00000OO0O0OO0O0 )#line:800
                            OOO00O0O00000O00O ={"water":str (OO0OO0OOOO0OOOO00 ).split ('.')[0 ]}#line:801
                            O000OO0O0O000O00O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O000OOOOOO00OO0O0 ).json ()#line:802
                            if 'status'in O000OO0O0O000O00O :#line:804
                                if O000OO0O0O000O00O ['status']==200 :#line:805
                                    print (f'【购买水滴】:看广告获取水滴:{O000OO0O0O000O00O["message"]}')#line:806
                                if O000OO0O0O000O00O ['status']==500 :#line:807
                                    print (f'【购买水滴】:看广告获取水滴:{O000OO0O0O000O00O["message"]}')#line:808
                                    break #line:809
                        if float (O000O00O00O00O00O )>96 and float (OO00000OO0O0OO0O0 )>880 :#line:810
                            break #line:811
        except Exception as O0000OO0OOOOO0OO0 :#line:813
            print (O0000OO0OOOOO0OO0 )#line:814
def bundled_def ():#line:816
    O00OO0O0OO00OOOO0 =['5570536','7750212','7911652','7911680','7805624']#line:817
    return O00OO0O0OO00OOOO0 [random .randint (0 ,len (O00OO0O0OO00OOOO0 )-1 )]#line:818
def version_of_the_validation ():#line:822
    return str ((80 -56 )/10 )#line:823
def gitee_validation ():#line:826
    try :#line:827
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:828
    except :#line:829
        sys .exit (0 )#line:830
def update_the_validation ():#line:834
    try :#line:835
        OO00O000OOOO0O0OO =gitee_validation ()#line:836
        if version_of_the_validation ()<OO00O000OOOO0O0OO ['CityEarth']['edition']:#line:837
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O000OOOO0O0OO["CityEarth"]["edition"]}   ❌')#line:838
            print (f'更新内容=>>{OO00O000OOOO0O0OO["CityEarth"]["content"]}   🎉')#line:839
        else :#line:840
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O000OOOO0O0OO["CityEarth"]["edition"]}   ✅')#line:841
            print (f'更新内容=>> {OO00O000OOOO0O0OO["CityEarth"]["content"]}   🎉')#line:842
    except Exception as OO00OOO0O00OOOO0O :#line:843
        print (OO00OOO0O00OOOO0O )#line:844
def os_qinglong ():#line:847
    if application in os .environ :#line:848
        O000OO0O000OO00OO =os .environ [application ].split ('\n')#line:849
        if len (O000OO0O000OO00OO )>0 :#line:850
            return O000OO0O000OO00OO #line:851
        else :#line:852
            print (f"{application}变量未启用")#line:853
            print ('脚本退出')#line:854
            sys .exit (1 )#line:855
    else :#line:856
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:858
        return os_built ()#line:859
def os_built ():#line:862
    if token :#line:863
        O00000OO0OOOO00O0 =token .split ('\n')#line:864
        if len (O00000OO0OOOO00O0 )>0 :#line:865
            return O00000OO0OOOO00O0 #line:866
    else :#line:867
        print (f"内置变量为空")#line:868
        print ('脚本结束')#line:869
        sys .exit (0 )#line:870
if __name__ =='__main__':#line:873
    start ()#line:874
