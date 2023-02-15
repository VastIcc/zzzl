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
        O00OOOOO0O00O0OOO =os_qinglong ()#line:10
        print (f"==========共找到{len(O00OOOOO0O00O0OOO)}个账号==========")#line:11
        for OO00000OO00O0OOO0 in O00OOOOO0O00O0OOO :#line:12
            OOO0O0000O0OOO0O0 =[]#line:13
            print (f"------------正在执行第{O00OOOOO0O00O0OOO.index(OO00000OO00O0OOO0) + 1}个账号------------")#line:14
            OOO0O0O00OO0O00OO =CityEarth (OO00000OO00O0OOO0 ,OOO0O0000O0OOO0O0 )#line:15
            def O0000OOOOOO0OOO00 ():#line:17
                if OOO0O0O00OO0O00OO .base_info ():#line:19
                    OOO0O0O00OO0O00OO .sealing ()#line:21
                    OOO0O0O00OO0O00OO .invitenum ()#line:23
                    OOO0O0O00OO0O00OO .game_map ()#line:25
                    OOO0O0O00OO0O00OO .friends_invitation ()#line:27
                    OOO0O0O00OO0O00OO .add_clover ()#line:29
                    OOO0O0O00OO0O00OO .propsraffle ()#line:31
                    OOO0O0O00OO0O00OO .synthetic ()#line:33
                    OOO0O0O00OO0O00OO .crops_illustrated ()#line:35
                    OOO0O0O00OO0O00OO .give_gold ()#line:37
                    OOO0O0O00OO0O00OO .withdraw ()#line:39
                    OOO0O0O00OO0O00OO .energy ()#line:41
            OO00OO000O0OOO00O =threading .Thread (target =O0000OOOOOO0OOO00 )#line:42
            OO00OO000O0OOO00O .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        OOOO00OO0O000OOOO =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOOO00OO0O000OOOO +' ')#line:48
    except Exception as O0OOO0OOO00O0OO0O :#line:49
        print (O0OOO0OOO00O0OO0O )#line:50
def sign (OOO0OOO00O00OOO0O ):#line:53
    O00O000OOOO000O00 =hashlib .md5 (OOO0OOO00O00OOO0O .encode ()).hexdigest ()#line:54
    O00O0000O0OOO0O00 ="scsc%^&*"+O00O000OOOO000O00 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    O00OOO00O0O0000O0 =hashlib .md5 (O00O0000O0OOO0O00 .encode ()).hexdigest ()#line:56
    return O00OOO00O0O0000O0 #line:57
def format_msg ():#line:59
    O0O0000OO0O0O00OO =""#line:60
    for OOOO0OO0OO0O0000O in msg_list :#line:61
        O0O0000OO0O0O00OO +=str (OOOO0OO0OO0O0000O )+"\r\n"#line:62
    return O0O0000OO0O0O00OO #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (O0O000000O0O000O0 ,OOO0O0O0O0OO000O0 ,O000O0O0O00OO0OOO ):#line:71
        try :#line:72
            O0O000000O0O000O0 .msg =O000O0O0O00OO0OOO #line:73
            O0O000000O0O000O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            O0O000000O0O000O0 .token =OOO0O0O0O0OO000O0 .split ('&')[0 ]#line:75
            O0O000000O0O000O0 .innerId =OOO0O0O0O0OO000O0 .split ('&')[1 ]#line:76
            O0O000000O0O000O0 .doneeNo =OOO0O0O0O0OO000O0 .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (O0O0O0OO0OOO000OO ):#line:82
        try :#line:83
            O0O0O0OO0OOO000OO .watched_ad ()#line:85
            O000OOO0O000O0O0O =f'__{timi_new()}'#line:86
            O00000OO000OOO0O0 ={'authorization':O0O0O0OO0OOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0O000O0O0O ),'signstring':O000OOO0O000O0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            OOO0000OOO0O00OO0 =requests .request ('get',f'{host}/user',headers =O00000OO000OOO0O0 ).json ()#line:96
            if 'status'in OOO0000OOO0O00OO0 :#line:98
                if OOO0000OOO0O00OO0 ['status']==200 :#line:99
                    OOO0OO0O0O000O00O =OOO0000OOO0O00OO0 ['data']['nickname']#line:100
                    O00O0OO0O00O00000 =OOO0000OOO0O00OO0 ['data']['inner_id']#line:101
                    O0O00OO00O000OOO0 =OOO0000OOO0O00OO0 ['data']['assets']['gold']#line:102
                    O00O0OO0OO00O0OOO =OOO0000OOO0O00OO0 ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{OOO0OO0O0O000O00O[:5]}丨ID:{O00O0OO0O00O00000}丨等级:{O00O0OO0OO00O0OOO}丨金种子:{str(O0O00OO00O000OOO0).split(".")[0]}')#line:104
                if OOO0000OOO0O00OO0 ['status']==401 :#line:105
                    print (OOO0000OOO0O00OO0 ['message'])#line:106
                    O0O0O0OO0OOO000OO .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if OOO0000OOO0O00OO0 ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as OO00OOO00000OO0O0 :#line:112
            print (OO00OOO00000OO0O0 )#line:113
    def sealing (O00O000O0000O0OOO ):#line:116
        try :#line:117
            O0OOOO0O00000OO0O =f'__{timi_new()}'#line:118
            OOO0000O0000OOOO0 ={'authorization':O00O000O0000O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0O00000OO0O ),'signstring':O0OOOO0O00000OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO0000O0000OOOO0 )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =OOO0000O0000OOOO0 )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO0000O0000OOOO0 )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO0000O0000OOOO0 )#line:131
            requests .request ('get',f'{host}/user',headers =OOO0000O0000OOOO0 )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO0000O0000OOOO0 )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO0000O0000OOOO0 )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO0000O0000OOOO0 )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =OOO0000O0000OOOO0 )#line:136
            requests .request ('get',f'{host}/assets',headers =OOO0000O0000OOOO0 )#line:137
        except Exception as O0OO000O0OO0O00O0 :#line:138
            print (O0OO000O0OO0O00O0 )#line:139
    def withdraw (O0OO00O000O000OO0 ):#line:143
        OO00OO0O0O00OO0O0 =f'__{timi_new()}'#line:144
        OO0OO0O0OOO0O000O ={'authorization':O0OO00O000O000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0O0O00OO0O0 ),'signstring':OO00OO0O0O00OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        OO000OO00OO0000O0 =requests .request ('get',f'{host}/assets',headers =OO0OO0O0OOO0O000O ).json ()#line:154
        if 'status'in OO000OO00OO0000O0 :#line:156
            if OO000OO00OO0000O0 ['status']==200 :#line:157
                O000OO0O0O00O00O0 =OO000OO00OO0000O0 ['data']['cash']#line:158
                if float (O000OO0O0O00O00O0 )>20 :#line:159
                    OO00OO0O0O00OO0O0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    OO0OO0O0OOO0O000O ={'authorization':O0OO00O000O000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0O0O00OO0O0 ),'signstring':OO00OO0O0O00OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    OOOOOO0OO0OO0000O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    O0OO0O0OOOOOO0O00 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO0OO0O0OOO0O000O ,data =OOOOOO0OO0OO0000O ).json ()#line:172
                    print (O0OO0O0OOOOOO0O00 )#line:173
    def invitenum (OOOOOO0O00O0OOO00 ):#line:176
        O0O00OOOOO00O0000 =f'__{timi_new()}'#line:177
        O0O00O0OOO0OOOOOO ={'authorization':OOOOOO0O00O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOOOO00O0000 ),'signstring':O0O00OOOOO00O0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O00O000000O00OOOO =requests .request ('get',f'{host}/invite/invitenum',headers =O0O00O0OOO0OOOOOO ).json ()#line:187
        if 'status'in O00O000000O00OOOO :#line:189
            if O00O000000O00OOOO ['status']==200 :#line:190
                OOOO0OOO000O0OOO0 =O00O000000O00OOOO ['data']['invited_count']#line:191
                OOOOOOO00000O0O00 =O00O000000O00OOOO ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OOOO0OOO000O0OOO0}丨间邀好友:{OOOOOOO00000O0O00}')#line:193
    def game_map (O0OO00OO0OO00O00O ):#line:196
        try :#line:197
            OOOO000OOO0O00000 =f'__{timi_new()}'#line:198
            O0OOOO00O0OO00OO0 ={'authorization':O0OO00OO0OO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000OOO0O00000 ),'signstring':OOOO000OOO0O00000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            OOOOO0O000OOOO0O0 =requests .request ('get',f'{host}/game/map',headers =O0OOOO00O0OO00OO0 ).json ()#line:208
            if 'status'in OOOOO0O000OOOO0O0 :#line:210
                if OOOOO0O000OOOO0O0 ['status']==200 :#line:211
                    for OO0OOO0O0O0OO0000 in OOOOO0O000OOOO0O0 ['data']['list'][0 ]['crops']:#line:212
                        O0OOOOO00000000OO =OO0OOO0O0O0OO0000 ['level']#line:214
                        if O0OOOOO00000000OO ==41 :#line:215
                            O00000OO000O00O00 =OO0OOO0O0O0OO0000 ['crop_name']#line:216
                            O00O0OO00O0OOO00O =OO0OOO0O0O0OO0000 ['count']#line:217
                            if O00O0OO00O0OOO00O >0 :#line:218
                                print (f'【农业资产】:{O00000OO000O00O00}丨数量:{O00O0OO00O0OOO00O}')#line:219
        except Exception as OOO0O00O0O0O00O0O :#line:220
            print (OOO0O00O0O0O00O0O )#line:221
    def give_gold (OO000OOO0O0OOOO0O ):#line:224
        try :#line:225
            O00OO0O000O00O0OO =f'__{timi_new()}'#line:226
            OO00O0O0OOOO00O0O ={'authorization':OO000OOO0O0OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O000O00O0OO ),'signstring':O00OO0O000O00O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            OOO0O0000O0O0O0OO =requests .request ('get',f'{host}/user',headers =OO00O0O0OOOO00O0O ).json ()#line:236
            if 'status'in OOO0O0000O0O0O0OO :#line:237
                if OOO0O0000O0O0O0OO ['status']==200 :#line:238
                    if float (OO000OOO0O0OOOO0O .doneeNo )!=0 :#line:239
                        OOO00O0O000O00O0O =OOO0O0000O0O0O0OO ['data']['assets']['gold']#line:240
                        if float (OOO00O0O000O00O0O )>float (OO000OOO0O0OOOO0O .innerId ):#line:241
                            OO0000OO0OOOOO0O0 =int (float (OOO00O0O000O00O0O )/1.1 )#line:242
                            O00OO0O000O00O0OO =f'_doneeNo={OO000OOO0O0OOOO0O.doneeNo}&quantity={OO0000OO0OOOOO0O0}_{timi_new()}'#line:243
                            OO00O0O0OOOO00O0O ={'authorization':OO000OOO0O0OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O000O00O0OO ),'signstring':O00OO0O000O00O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            O0OO00O0O0O000000 ={"quantity":OO0000OO0OOOOO0O0 ,"doneeNo":OO000OOO0O0OOOO0O .doneeNo }#line:256
                            OOO0OOOO0O00OO0OO =requests .request ('post',f'{host}/finance/give-gold',headers =OO00O0O0OOOO00O0O ,data =O0OO00O0O0O000000 ).json ()#line:257
                            if 'status'in OOO0OOOO0O00OO0OO :#line:259
                                if OOO0OOOO0O00OO0OO ['status']==200 :#line:260
                                    if OOO0OOOO0O00OO0OO ['data']:#line:261
                                        print (f'【赠送种子】:赠送{OO0000OO0OOOOO0O0}种子给{OO000OOO0O0OOOO0O.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as OOOO0O00O00OO00O0 :#line:265
            print (OOOO0O00O00OO00O0 )#line:266
    def invitation (O000OOO0000000OOO ):#line:268
        try :#line:269
            _O00O000OOO0OO0O0O =float (bundled_def ())/4 #line:270
            OOOOOO0OOO0O0OO00 =f'_innerId={int(_O00O000OOO0OO0O0O)}_{timi_new()}'#line:271
            OOO000O00OOOOOO0O ={'authorization':O000OOO0000000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OOO0O0OO00 ),'signstring':OOOOOO0OOO0O0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            OO0000OO00O00OOOO ={"innerId":int (_O00O000OOO0OO0O0O )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO000O00OOOOOO0O ,data =OO0000OO00O00OOOO )#line:282
        except Exception as O0O0O00O0OOOO0OO0 :#line:283
            print (O0O0O00O0OOOO0OO0 )#line:284
    def winning_rewards (O0000O0O0000OO0OO ):#line:287
        try :#line:288
            OO0OOOOOO0O0OO0OO =f'__{timi_new()}'#line:289
            O000OO0000O000OOO ={'authorization':O0000O0O0000OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOOO0O0OO0OO ),'signstring':OO0OOOOOO0O0OO0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            O0O00OO00O0OOO0O0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O000OO0000O000OOO ).json ()#line:299
            if 'status'in O0O00OO00O0OOO0O0 :#line:301
                if O0O00OO00O0OOO0O0 ['status']==200 :#line:302
                    if O0O00OO00O0OOO0O0 ['data']['amount']:#line:303
                        OO0000OO000O00O0O =O0O00OO00O0OOO0O0 ['data']['amount']['gold']#line:304
                        return OO0000OO000O00O0O #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as OO0OOO00000OOO0O0 :#line:308
            print (OO0OOO00000OOO0O0 )#line:309
    def certification (O00O0OO0O0OOO0OO0 ):#line:312
        try :#line:313
            OO00OO000000OO000 =f'__{timi_new()}'#line:314
            O0OOOO00OOO0O0OO0 ={'authorization':O00O0OO0O0OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO000000OO000 ),'signstring':OO00OO000000OO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OOO0OO00OOO00O00O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0OOOO00OOO0O0OO0 ).json ()#line:324
            if 'status'in OOO0OO00OOO00O00O :#line:326
                if OOO0OO00OOO00O00O ['status']==200 :#line:327
                    if OOO0OO00OOO00O00O ['data']['result']:#line:328
                        OO0OO00OO00OO0O00 =OOO0OO00OOO00O00O ['data']['nick_name']#line:329
                        return OO0OO00OO00OO0O00 #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as OOO000OO0O000O00O :#line:333
            print (OOO000OO0O000O00O )#line:334
    def crops_illustrated (OOO000O00OOOO0O00 ):#line:337
        try :#line:338
            OO000000O00O0OOOO =f'__{timi_new()}'#line:339
            OOOOO0000O00OOOO0 ={'authorization':OOO000O00OOOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000O00O0OOOO ),'signstring':OO000000O00O0OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            OOOOO0OO0O0OOOO00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOOOO0000O00OOOO0 ).json ()#line:349
            if 'status'in OOOOO0OO0O0OOOO00 :#line:351
                if OOOOO0OO0O0OOOO00 ['status']==200 :#line:352
                    O0O0O000000O00O0O =OOOOO0OO0O0OOOO00 ['data'][0 ]['crops']#line:353
                    for O0OOOOOOOO0OO00OO in O0O0O000000O00O0O :#line:354
                        if O0OOOOOOOO0OO00OO ['ill_clover_award']:#line:355
                            if float (O0OOOOOOOO0OO00OO ['ill_clover_award'])>1 :#line:356
                                if O0OOOOOOOO0OO00OO ['is_finish']:#line:357
                                    if not O0OOOOOOOO0OO00OO ['is_getit']:#line:358
                                        if OOO000O00OOOO0O00 .certification ()!='未实名':#line:359
                                            OO000000O00O0OOOO =f'_award_level={O0OOOOOOOO0OO00OO["level"]}_{timi_new()}'#line:360
                                            OOOOO0000O00OOOO0 ={'authorization':OOO000O00OOOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000O00O0OOOO ),'signstring':OO000000O00O0OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            O0O0O00O0O0OOOO0O ={"award_level":O0OOOOOOOO0OO00OO ['level']}#line:370
                                            OO0000000O0O0OOOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOOOO0000O00OOOO0 ,json =O0O0O00O0O0OOOO0O ).json ()#line:372
                                            if 'status'in OO0000000O0O0OOOO :#line:373
                                                if OO0000000O0O0OOOO ['status']==200 :#line:374
                                                    O0OOOOOO00OOO00OO =OO0000000O0O0OOOO ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{O0OOOOOOOO0OO00OO["crop_name"]}成就丨奖励{O0OOOOOO00OOO00OO}☘️')#line:377
                                                if OO0000000O0O0OOOO ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{OO0000000O0O0OOOO["message"]}')#line:379
        except Exception as OO0OOOOO0OOOO00OO :#line:380
            print (OO0OOOOO0OOOO00OO )#line:381
    def watched_ad (OOO000OO00O0O00OO ):#line:384
        try :#line:385
            time .sleep (random .randint (16 ,18 ))#line:386
            OOO00O0OO0000O000 =f'__{timi_new()}'#line:387
            O0OOOO000O000OOOO ={'authorization':OOO000OO00O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OO0000O000 ),'signstring':OOO00O0OO0000O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:396
            O0O0O0O0OOOOOOOOO =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOO000O000OOOO ).json ()#line:397
            if 'status'in O0O0O0O0OOOOOOOOO :#line:399
                if O0O0O0O0OOOOOOOOO ['status']==200 :#line:400
                    if 'offlineInfo'in O0O0O0O0OOOOOOOOO ['data']:#line:401
                        OOO0OOOOO0O0OO0O0 =O0O0O0O0OOOOOOOOO ['data']['offlineInfo']['off_minute']#line:402
                        OOOO00OO00O0OOOOO =float (O0O0O0O0OOOOOOOOO ['data']['silver'])/1000000000000 #line:403
                        time .sleep (1 )#line:404
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0OOOO000O000OOOO ).json ()#line:405
                        time .sleep (2 )#line:406
                        OOOO0OO000O0000O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOO000O000OOOO ).json ()#line:407
                        if 'status'in OOOO0OO000O0000O0 :#line:409
                            if OOOO0OO000O0000O0 ['status']==200 :#line:410
                                O0O00OOO000OO00OO =float (OOOO0OO000O0000O0 ['data']['silver'])/1000000000000 #line:411
                                O00O0O0O0OOOOOO0O =str (O0O00OOO000OO00OO -OOOO00OO00O0OOOOO )[:6 ]#line:412
                                print (f'【离线奖励】:翻倍离线{OOO0OOOOO0O0OO0O0}分钟奖励🌱数量:{O00O0O0O0OOOOOO0O}t粒')#line:413
        except Exception as O00OOO00OO0OOO0O0 :#line:414
            print (O00OOO00OO0OOO0O0 )#line:415
    def user_ad (O000O0OO00OO0OOOO ):#line:418
        try :#line:419
            O0O0OO00O0O00O0O0 =f'__{timi_new()}'#line:420
            O000O0O00OOOOOO0O ={'authorization':O000O0OO00OO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00O0O00O0O0 ),'signstring':O0O0OO00O0O00O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:429
            OOOOO00000OOOO0O0 =requests .request ('get',f'{host}/user/ad',headers =O000O0O00OOOOOO0O ).json ()#line:430
            if 'status'in OOOOO00000OOOO0O0 :#line:432
                if OOOOO00000OOOO0O0 ['status']==200 :#line:433
                    O0000O00OOOO0OOO0 =OOOOO00000OOOO0O0 ['data']['max_time']#line:434
                    O0O0000OO0O0000OO =OOOOO00000OOOO0O0 ['data']['watch_time']#line:435
                    O0O0OO0OO0OO0OO0O =OOOOO00000OOOO0O0 ['data']['added_time']#line:436
                    print (f'【获取种子】:获取🌱剩余{O0O0OO0OO0OO0OO0O + O0000O00OOOO0OOO0 - O0O0000OO0O0000OO}次丨好友提供:{O0O0OO0OO0OO0OO0O}次')#line:437
                    if O0O0OO0OO0OO0OO0O +O0000O00OOOO0OOO0 -O0O0000OO0O0000OO >0 :#line:438
                        time .sleep (random .randint (16 ,19 ))#line:439
                        OO0O0O0OO000OOO00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O000O0O00OOOOOO0O ).json ()#line:440
                        if 'status'in OO0O0O0OO000OOO00 :#line:442
                            if OO0O0O0OO000OOO00 ['status']==200 :#line:443
                                O0000OOOO0000000O =float (OO0O0O0OO000OOO00 ['data']['silver'])/1000000000000 #line:444
                                print (f'【获取种子】:获得🌱:{int(O0000OOOO0000000O)}t粒')#line:445
                                return True #line:446
                            if OO0O0O0OO000OOO00 ['status']==500 :#line:447
                                O00O0000O0OO0000O =OO0O0O0OO000OOO00 ['message']#line:448
                                print (f'【获取种子】:{O00O0000O0OO0000O}')#line:449
                                return False #line:450
        except Exception as OOO0OOO0000000OO0 :#line:451
            print (OOO0OOO0000000OO0 )#line:452
    def synthetic (OO0OOOOOO0O000O0O ):#line:455
        global id ,g #line:456
        try :#line:457
            OOOO0O0O00OO0OOOO =OO0OOOOOO0O000O0O .level_new ()#line:458
            OO0OO0OO0OO00O000 =random .randint (9 ,11 )#line:459
            O0O000OO00OO0O0OO =f'_site=8&targetSite={OO0OO0OO0OO00O000}_{timi_new()}'#line:460
            O00OOOO0O00OO00O0 ={'accept':'application/json, text/plain, */*','authorization':OO0OOOOOO0O000O0O .token ,'timestamp':timi_new (),'sign':sign (O0O000OO00OO0O0OO ),'signstring':O0O000OO00OO0O0OO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:475
            O0000O000OOO00OO0 ={"site":int (8 ),"targetSite":int (OO0OO0OO0OO00O000 )}#line:476
            requests .request ('post',f'{host}/game/crops/move',headers =O00OOOO0O00OO00O0 ,json =O0000O000OOO00OO0 )#line:477
            while True :#line:478
                OO0OOO0O000OOO000 =f'__{timi_new()}'#line:479
                O0O00O0OO00000OOO ={'authorization':OO0OOOOOO0O000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O000OOO000 ),'signstring':OO0OOO0O000OOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                OOO00OO00O00OOO0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O00O0OO00000OOO ).json ()#line:489
                if 'status'in OOO00OO00O00OOO0O :#line:491
                    if OOO00OO00O00OOO0O ['status']==200 :#line:492
                        OO0O000OOOO00OO0O =OOO00OO00O00OOO0O ['data']['cropList']#line:493
                        O00OO00000O000000 =OOO00OO00O00OOO0O ['data']['gameCoreDataDBid']#line:494
                        O0O00OOOO00OOO0O0 =float (OOO00OO00O00OOO0O ['data']['silver'])/1000000000000 #line:495
                        if O0O00OOOO00OOO0O0 <6750 :#line:496
                            print (f'【种植合成】:🌱不足6750t')#line:497
                            break #line:498
                        O00OO0OO000O0OO00 =0 #line:499
                        for OO0O000O000OO0OO0 in OO0O000OOOO00OO0O :#line:500
                            if not OO0O000O000OO0OO0 :#line:501
                                OOO00OOOOO000O00O =f'_crop_id={O00OO00000O000000}&site={O00OO0OO000O0OO00}_{OO0OOOOOO0O000O0O.time}'#line:502
                                O00O0OOO0O00OOOO0 ={'authorization':OO0OOOOOO0O000O0O .token ,'timestamp':OO0OOOOOO0O000O0O .time ,'sign':sign (OOO00OOOOO000O00O ),'signstring':OOO00OOOOO000O00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:511
                                O0O00OO0OOO00OOOO ={"site":O00OO0OO000O0OO00 ,"crop_id":O00OO00000O000000 }#line:512
                                OOOOOOO0O00OO0O0O =requests .request ('post',f'{host}/game/crops/buy',headers =O00O0OOO0O00OOOO0 ,data =O0O00OO0OOO00OOOO ).json ()#line:513
                                time .sleep (random .randint (1 ,3 )/10 )#line:515
                                if 'status'in OOOOOOO0O00OO0O0O :#line:516
                                    if OOOOOOO0O00OO0O0O ['status']==200 :#line:517
                                        if OOOOOOO0O00OO0O0O ['message']=='种子数量不足':#line:518
                                            OOOO0O0O00OO0OOOO =OO0OOOOOO0O000O0O .level_new ()#line:519
                                            print (f'【种植合成】:{OOOOOOO0O00OO0O0O["message"]}')#line:520
                                            if not OO0OOOOOO0O000O0O .user_ad ():#line:521
                                                return False #line:522
                                    if OOOOOOO0O00OO0O0O ['status']==500 :#line:523
                                        print (f'【种植合成】:{OOOOOOO0O00OO0O0O["message"]}')#line:524
                                        return False #line:525
                            O00OO0OO000O0OO00 +=1 #line:526
                        OO00OOOO000OO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O00O0OO00000OOO ).json ()#line:527
                        O0O0O000O0OOO0OOO =OO00OOOO000OO0O0O ['data']['cropList']#line:528
                        OO000OO0O00OO0O00 =False #line:529
                        for OO0O000O000OO0OO0 in range (12 ):#line:530
                            id =O0O0O000O0OOO0OOO [OO0O000O000OO0OO0 ]['level']#line:531
                            if float (OOOO0O0O00OO0OOOO )-float (id )>9 :#line:532
                                O00OOO0O00OOOOO0O =f'_site={OO0O000O000OO0OO0}_{timi_new()}'#line:533
                                OOO0O00OO000O0OO0 ={'accept':'application/json, text/plain, */*','authorization':OO0OOOOOO0O000O0O .token ,'timestamp':timi_new (),'sign':sign (O00OOO0O00OOOOO0O ),'signstring':O00OOO0O00OOOOO0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:543
                                O00OOOOO0000OOOOO ={"site":OO0O000O000OO0OO0 }#line:544
                                OOOO00O0O0000000O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO0O00OO000O0OO0 ,data =O00OOOOO0000OOOOO ).json ()#line:546
                                if 'status'in OOOO00O0O0000000O :#line:547
                                    if OOOO00O0O0000000O ['status']==200 :#line:548
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:549
                            if id !=0 :#line:550
                                for O0O000O000O0O00O0 in range (11 ):#line:551
                                    O00000O0O0OOO0OO0 =O0O000O000O0O00O0 +1 #line:552
                                    g =O0O0O000O0OOO0OOO [O00000O0O0OOO0OO0 ]['level']#line:553
                                    if id ==g :#line:554
                                        O00O0O0O0O0O00OOO =O0O000O000O0O00O0 +2 #line:555
                                        if O00O0O0O0O0O00OOO !=OO0O000O000OO0OO0 +1 :#line:556
                                            O0000O00OO000000O =OO0O000O000OO0OO0 +1 #line:557
                                            time .sleep (random .randint (1 ,3 )/10 )#line:559
                                            O0O000OO00OO0O0OO =f'_site={O0000O00OO000000O - 1}&targetSite={O00O0O0O0O0O00OOO - 1}_{timi_new()}'#line:560
                                            O00OOOO0O00OO00O0 ={'accept':'application/json, text/plain, */*','authorization':OO0OOOOOO0O000O0O .token ,'timestamp':timi_new (),'sign':sign (O0O000OO00OO0O0OO ),'signstring':O0O000OO00OO0O0OO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:575
                                            O0OOOOOOO0OOOO00O ={"site":int (O0000O00OO000000O -1 ),"targetSite":int (O00O0O0O0O0O00OOO -1 )}#line:576
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00OOOO0O00OO00O0 ,json =O0OOOOOOO0OOOO00O )#line:577
                                            print (f'【种植合成】:位置{O0000O00OO000000O}和位置{O00O0O0O0O0O00OOO}合出{int(id) + 1}级农作物')#line:578
                                            OO000OO0O00OO0O00 =True #line:579
                                    if OO000OO0O00OO0O00 :#line:580
                                        break #line:581
                                if OO000OO0O00OO0O00 :#line:582
                                    break #line:583
        except :#line:584
            OO0OOOOOO0O000O0O .synthetic ()#line:585
    def level_new (O00OO0000O000OO0O ):#line:588
        try :#line:589
            O0O00OOOO0O0OO0OO =f'__{timi_new()}'#line:590
            O000O0O0OO0O0OOO0 ={'authorization':O00OO0000O000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOOO0O0OO0OO ),'signstring':O0O00OOOO0O0OO0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:599
            OOO000OO000OOOO0O =requests .request ('get',f'{host}/user',headers =O000O0O0OO0O0OOO0 ).json ()#line:600
            if 'status'in OOO000OO000OOOO0O :#line:601
                if OOO000OO000OOOO0O ['status']==200 :#line:602
                    return float (OOO000OO000OOOO0O ['data']['level'])#line:603
        except Exception as OO0O0OO0OO000O0OO :#line:604
            print (OO0O0OO0OO000O0OO )#line:605
    def propsraffle (O000O0OO0OO00OO0O ):#line:608
        try :#line:609
            while True :#line:610
                O0O0OO0OO00OOO00O =f'__{timi_new()}'#line:611
                OOO0O0O0O0O0O0O0O ={'authorization':O000O0OO0OO00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OO00OOO00O ),'signstring':O0O0OO0OO00OOO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:620
                O0000OOO000000O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO0O0O0O0O0O0O0O ).json ()#line:621
                if 'status'in O0000OOO000000O0O :#line:623
                    if O0000OOO000000O0O ['status']==200 :#line:624
                        O0O00OOO0000O00O0 =O0000OOO000000O0O ['data']['rows']#line:625
                        O0OO000OO0OO0OO00 =O0000OOO000000O0O ['data']['vstate']#line:626
                        if O0O00OOO0000O00O0 ==5 or O0O00OOO0000O00O0 ==6 or O0O00OOO0000O00O0 ==7 :#line:627
                            O000O0O0OOOO0O00O =O0000OOO000000O0O ['data']['silver']#line:628
                            print (f'【转盘抽奖】:获得种子:{O000O0O0OOOO0O00O}')#line:629
                        if O0O00OOO0000O00O0 ==1 or O0O00OOO0000O00O0 ==2 or O0O00OOO0000O00O0 ==3 :#line:630
                            O00O0O0OO0OOO0OO0 =O0000OOO000000O0O ['data']['clover']#line:631
                            print (f'【转盘抽奖】:获得三叶草:{O00O0O0OO0OOO0OO0}')#line:632
                        if O0O00OOO0000O00O0 ==4 or O0O00OOO0000O00O0 ==8 :#line:633
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:634
                        if O0O00OOO0000O00O0 =='抽奖次数已用完':#line:638
                            break #line:671
                time .sleep (random .randint (8 ,15 )/10 )#line:672
        except Exception as O00OO000OOO0O0O00 :#line:673
            print (O00OO000OOO0O0O00 )#line:674
    def friends_invitation (OOO0O0O0O00OO0O00 ):#line:677
        try :#line:678
            O0O0000OOO000OOOO =f'__{timi_new()}'#line:679
            O00O00OOO0OOOOOOO ={'authorization':OOO0O0O0O00OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OOO000OOOO ),'signstring':O0O0000OOO000OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:688
            OO00OO00OO0OOOO0O =requests .request ('get',f'{host}/friends',headers =O00O00OOO0OOOOOOO ).json ()#line:689
            if 'status'in OO00OO00OO0OOOO0O :#line:690
                if OO00OO00OO0OOOO0O ['status']==200 :#line:691
                    O0OOO0000OOO0O0O0 =OO00OO00OO0OOOO0O ['data']['myInviteter']#line:692
                    if O0OOO0000OOO0O0O0 :#line:693
                        O0OOO00000O0O000O =O0OOO0000OOO0O0O0 ['user']['nickname']#line:694
                        O0OO000OOOOO00OOO =OOO0O0O0O00OO0O00 .certification ()#line:695
                        print (f'【查邀请人】:我的邀请人:{O0OOO00000O0O000O}丨实名:{O0OO000OOOOO00OOO}')#line:696
                    else :#line:697
                        if OOO0O0O0O00OO0O00 .innerId !='0':#line:698
                            OOO0O0O0O00OO0O00 .invitation ()#line:699
        except Exception as OOOO0OO00OO000OOO :#line:700
            print (OOOO0OO00OO000OOO )#line:701
    def add_clover (O0O00OO00O0O0O0OO ):#line:704
        global golden_seed #line:705
        try :#line:706
            OOOO0OO0000OO0O00 =f'__{timi_new()}'#line:707
            OOOO0000O00000OOO ={'authorization':O0O00OO00O0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO0000OO0O00 ),'signstring':OOOO0OO0000OO0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:716
            O0OOO0O0O0O000OOO =requests .request ('get',f'{host}/assets/clovers',headers =OOOO0000O00000OOO ).json ()#line:717
            if 'status'in O0OOO0O0O0O000OOO :#line:719
                if O0OOO0O0O0O000OOO ['status']==200 :#line:720
                    OOO00O0O0OO0OO00O =O0OOO0O0O0O000OOO ['data']['clover']#line:721
                    O0O0O00OO0000OO0O =O0OOO0O0O0O000OOO ['data']['used_clover']#line:722
                    OOO0OO0OO0000000O =float (OOO00O0O0OO0OO00O )-float (O0O0O00OO0000OO0O )#line:723
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0O0O00OO0000OO0O}')#line:724
                    if O0O00OO00O0O0O0OO .certification ()!='未实名':#line:725
                        if OOO0OO0OO0000000O >1 :#line:726
                            OOOO0OO0000OO0O00 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO0OO0OO0000000O)}_{timi_new()}'#line:727
                            OOOOOOOO0OO000O0O ={'authorization':O0O00OO00O0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO0000OO0O00 ),'signstring':OOOO0OO0000OO0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:736
                            O000OO00000O00O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO0OO0OO0000000O )}#line:737
                            O00000OO0000O000O =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOOOOOO0OO000O0O ,data =O000OO00000O00O0O ).json ()#line:738
                            if 'status'in O00000OO0000O000O :#line:740
                                if O00000OO0000O000O ['status']==200 :#line:741
                                    print (f'【参与抽奖】:添加☘️:{O00000OO0000O000O["data"]}丨数量:{OOO0OO0OO0000000O}')#line:742
                                if O00000OO0000O000O ['status']==500 :#line:743
                                    print (f'【参与抽奖】:添加☘️:{O00000OO0000O000O["message"]}')#line:744
            OOO0O0OO000OOO000 =requests .request ('get',f'{host}/lottery',headers =OOOO0000O00000OOO ).json ()#line:745
            OOOO00O0OO0OO0OOO =O0O00OO00O0O0O0OO .winning_rewards ()#line:747
            if 'status'in OOO0O0OO000OOO000 :#line:748
                if OOO0O0OO000OOO000 ['status']==200 :#line:749
                    OO00OO0OO0000OOOO =OOO0O0OO000OOO000 ['data'][0 ]['day_get_gold_quantity']#line:750
                    golden_seed +=float (OO00OO0OO0000OOOO )#line:751
                    OO000O000O00OOOO0 =OOO0O0OO000OOO000 ['data'][1 ]['value']#line:752
                    OOOO0O000OOO000O0 =OOO0O0OO000OOO000 ['data'][0 ]['join_number']#line:753
                    O00OOOOO0OO0O00O0 =int (float (OOO0O0OO000OOO000 ['data'][0 ]['totalValue']))#line:754
                    O0OOO0OO0O00OOO00 =float (OO000O000O00OOOO0 /O00OOOOO0OO0O00O0 )*10000 #line:755
                    O000OO0OO0O00OOO0 =O00OOOOO0OO0O00O0 /OOOO0O000OOO000O0 #line:756
                    print (f'【参与抽奖】:预计每天中{str(OO00OO0OO0000OOOO)[:6]}颗金种子丨好友收益:{str(OOOO00O0OO0OO0OOO)[:6]}')#line:757
                    print (f'【抽奖统计】:每1万☘️中{str(O0OOO0OO0O00OOO00)[:4]}颗金种子丨☘️人均:{str(O000OO0OO0O00OOO0)[:7]}️')#line:758
        except Exception as O0O0O00OOO0OOO0O0 :#line:759
            print (O0O0O00OOO0OOO0O0 )#line:760
    def energy (O0OO0O00OO000O0OO ):#line:764
        try :#line:765
            while True :#line:766
                O0OOOO0O000000000 =f'__{timi_new()}'#line:767
                O0000OO00OO0O0OO0 ={'authorization':O0OO0O00OO000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0O000000000 ),'signstring':O0OOOO0O000000000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:776
                O0OOO0OOOOO000OO0 =requests .request ('get',f'{host}/energy/general',headers =O0000OO00OO0O0OO0 ).json ()#line:777
                if 'status'in O0OOO0OOOOO000OO0 :#line:779
                    if O0OOO0OOOOO000OO0 ['status']==200 :#line:780
                        OOO000OO000OO000O =O0OOO0OOOOO000OO0 ['data']['ordinary_water']#line:781
                        O000000OOOOO00OO0 =O0OOO0OOOOO000OO0 ['data']['ordinary_fertilizer']#line:782
                        print (f'【我的营养】:肥料:{str(O000000OOOOO00OO0).split(".")[0]}丨水滴:{str(OOO000OO000OO000O).split(".")[0]}')#line:784
                        if float (O000000OOOOO00OO0 )<96 :#line:785
                            time .sleep (random .randint (160 ,180 )/10 )#line:786
                            OO0O00OO000OOO000 =99 -float (O000000OOOOO00OO0 )#line:787
                            O00O00OO00O0O00OO ={"fertilizer":str (OO0O00OO000OOO000 ).split ('.')[0 ]}#line:788
                            OOOO000OOO0OO0OOO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0000OO00OO0O0OO0 ).json ()#line:789
                            if 'status'in OOOO000OOO0OO0OOO :#line:791
                                if OOOO000OOO0OO0OOO ['status']==200 :#line:792
                                    print (f'【购买肥料】:看广告获取肥料:{OOOO000OOO0OO0OOO["message"]}')#line:793
                        if float (OOO000OO000OO000O )<880 :#line:794
                            time .sleep (random .randint (160 ,180 )/10 )#line:795
                            OOOO0OOOOO0OOOO00 =999 -float (OOO000OO000OO000O )#line:796
                            OOO0O0O0O0O00OO00 ={"water":str (OOOO0OOOOO0OOOO00 ).split ('.')[0 ]}#line:797
                            O0OO0O0O00O000OOO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0000OO00OO0O0OO0 ).json ()#line:798
                            if 'status'in O0OO0O0O00O000OOO :#line:800
                                if O0OO0O0O00O000OOO ['status']==200 :#line:801
                                    print (f'【购买水滴】:看广告获取水滴:{O0OO0O0O00O000OOO["message"]}')#line:802
                        if float (O000000OOOOO00OO0 )>96 and float (OOO000OO000OO000O )>880 :#line:803
                            break #line:804
        except Exception as OOO0O0O0O00O00OO0 :#line:806
            print (OOO0O0O0O00O00OO0 )#line:807
def bundled_def ():#line:809
    OO00OO0O0OOOOO0O0 =['5570536','7750212','7911652','7911680','7805624']#line:810
    return OO00OO0O0OOOOO0O0 [random .randint (0 ,len (OO00OO0O0OOOOO0O0 )-1 )]#line:811
def version_of_the_validation ():#line:815
    return str ((78 -56 )/10 )#line:816
def gitee_validation ():#line:819
    try :#line:820
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:821
    except :#line:822
        sys .exit (0 )#line:823
def update_the_validation ():#line:827
    try :#line:828
        OO0O0OOO0000OOOO0 =gitee_validation ()#line:829
        if version_of_the_validation ()<OO0O0OOO0000OOOO0 ['CityEarth']['edition']:#line:830
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0OOO0000OOOO0["CityEarth"]["edition"]}   ❌')#line:831
            print (f'更新内容=>>{OO0O0OOO0000OOOO0["CityEarth"]["content"]}   🎉')#line:832
        else :#line:833
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0OOO0000OOOO0["CityEarth"]["edition"]}   ✅')#line:834
            print (f'更新内容=>> {OO0O0OOO0000OOOO0["CityEarth"]["content"]}   🎉')#line:835
    except Exception as OOOOO000OO00OO00O :#line:836
        print (OOOOO000OO00OO00O )#line:837
def os_qinglong ():#line:840
    if application in os .environ :#line:841
        O00OOOOOOO0O00000 =os .environ [application ].split ('\n')#line:842
        if len (O00OOOOOOO0O00000 )>0 :#line:843
            return O00OOOOOOO0O00000 #line:844
        else :#line:845
            print (f"{application}变量未启用")#line:846
            print ('脚本退出')#line:847
            sys .exit (1 )#line:848
    else :#line:849
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:851
        return os_built ()#line:852
def os_built ():#line:855
    if token :#line:856
        O000O00000O00OO00 =token .split ('\n')#line:857
        if len (O000O00000O00OO00 )>0 :#line:858
            return O000O00000O00OO00 #line:859
    else :#line:860
        print (f"内置变量为空")#line:861
        print ('脚本结束')#line:862
        sys .exit (0 )#line:863
if __name__ =='__main__':#line:866
    start ()#line:867
