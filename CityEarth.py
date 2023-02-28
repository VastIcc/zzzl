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
@ 版本  2.5
"""
application = 'ce_token'  # 变量名
token = ''
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
version ='3.1.41954131'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        O0OOO0O0O00O0OO0O =os_qinglong ()#line:10
        print (f"==========共找到{len(O0OOO0O0O00O0OO0O)}个账号==========")#line:11
        for OOOOO000O0OO00OO0 in O0OOO0O0O00O0OO0O :#line:12
            O0OO00OO0O00OO0O0 =[]#line:13
            print (f"------------正在执行第{O0OOO0O0O00O0OO0O.index(OOOOO000O0OO00OO0) + 1}个账号------------")#line:14
            O0OOO00O0O0OO0O0O =CityEarth (OOOOO000O0OO00OO0 ,O0OO00OO0O00OO0O0 )#line:15
            def O00O00O00O0OO0O00 ():#line:17
                if O0OOO00O0O0OO0O0O .base_info ():#line:19
                    O0OOO00O0O0OO0O0O .sealing ()#line:21
                    O0OOO00O0O0OO0O0O .invitenum ()#line:23
                    O0OOO00O0O0OO0O0O .game_map ()#line:25
                    O0OOO00O0O0OO0O0O .friends_invitation ()#line:27
                    O0OOO00O0O0OO0O0O .add_clover ()#line:29
                    O0OOO00O0O0OO0O0O .propsraffle ()#line:31
                    O0OOO00O0O0OO0O0O .synthetic ()#line:33
                    O0OOO00O0O0OO0O0O .crops_illustrated ()#line:35
                    O0OOO00O0O0OO0O0O .give_gold ()#line:37
                    O0OOO00O0O0OO0O0O .withdraw ()#line:39
                    O0OOO00O0O0OO0O0O .energy ()#line:41
            O00OOOOO0OOOO0OOO =threading .Thread (target =O00O00O00O0OO0O00 )#line:42
            O00OOOOO0OOOO0OOO .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        OO0OO0OOOOOO000O0 =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0OO0OOOOOO000O0 +' ')#line:48
    except Exception as O0O0O0OO000O0O0OO :#line:49
        print (O0O0O0OO000O0O0OO )#line:50
def sign (OO00OO0O00O000O0O ):#line:53
    O0O0OO0OOO0O0000O =hashlib .md5 (OO00OO0O00O000O0O .encode ()).hexdigest ()#line:54
    O0OOO00O00O0OOO0O ="scsc%^&*"+O0O0OO0OOO0O0000O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    OO00O0000000OO000 =hashlib .md5 (O0OOO00O00O0OOO0O .encode ()).hexdigest ()#line:56
    return OO00O0000000OO000 #line:57
def format_msg ():#line:59
    OOOOOOOOO00O000O0 =""#line:60
    for OO0O0OOOOO00000OO in msg_list :#line:61
        OOOOOOOOO00O000O0 +=str (OO0O0OOOOO00000OO )+"\r\n"#line:62
    return OOOOOOOOO00O000O0 #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (OO0O00O0OO00O0O00 ,OO000000O0O0000O0 ,O0O00OO0O0OO0OO00 ):#line:71
        try :#line:72
            OO0O00O0OO00O0O00 .msg =O0O00OO0O0OO0OO00 #line:73
            OO0O00O0OO00O0O00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            OO0O00O0OO00O0O00 .token =OO000000O0O0000O0 .split ('&')[0 ]#line:75
            OO0O00O0OO00O0O00 .innerId =OO000000O0O0000O0 .split ('&')[1 ]#line:76
            OO0O00O0OO00O0O00 .doneeNo =OO000000O0O0000O0 .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (O0000OOOOO00000OO ):#line:82
        try :#line:83
            O0000OOOOO00000OO .watched_ad ()#line:85
            O000OO0OO00OO000O =f'__{timi_new()}'#line:86
            OO00O0OO0O0OOO00O ={'source':'scsc','authorization':O0000OOOOO00000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0OO00OO000O ),'signstring':O000OO0OO00OO000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:96
            O00OOOO0O00OO00OO =requests .request ('get',f'{host}/user',headers =OO00O0OO0O0OOO00O ).json ()#line:97
            if 'status'in O00OOOO0O00OO00OO :#line:99
                if O00OOOO0O00OO00OO ['status']==200 :#line:100
                    OOO0000OO0OO000O0 =O00OOOO0O00OO00OO ['data']['nickname']#line:101
                    O0OOO00000O00OO00 =O00OOOO0O00OO00OO ['data']['inner_id']#line:102
                    OOOO00O0OO00OO0O0 =O00OOOO0O00OO00OO ['data']['assets']['gold']#line:103
                    O00000OO000OOOOO0 =O00OOOO0O00OO00OO ['data']['level']#line:104
                    print (f'【账号信息】:昵称:{OOO0000OO0OO000O0[:5]}丨ID:{O0OOO00000O00OO00}丨等级:{O00000OO000OOOOO0}丨金种子:{str(OOOO00O0OO00OO0O0).split(".")[0]}')#line:105
                if O00OOOO0O00OO00OO ['status']==401 :#line:106
                    print (O00OOOO0O00OO00OO ['message'])#line:107
                    O0000OOOOO00000OO .msg .append ('有账号失效了')#line:108
                    return False #line:109
                if O00OOOO0O00OO00OO ['status']==500 :#line:110
                    return False #line:111
            return True #line:112
        except Exception as OO0OOOOO0OOOOO000 :#line:113
            print (OO0OOOOO0OOOOO000 )#line:114
    def sealing (OO0OO0O0OO00O00O0 ):#line:117
        try :#line:118
            O0000OO00OOOOO00O =f'__{timi_new()}'#line:119
            O0000OOOO00OOO0OO ={'authorization':OO0OO0O0OO00O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO00OOOOO00O ),'signstring':O0000OO00OOOOO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:128
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0000OOOO00OOO0OO )#line:129
            requests .request ('get',f'{host}/packsack/list',headers =O0000OOOO00OOO0OO )#line:130
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0000OOOO00OOO0OO )#line:131
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0000OOOO00OOO0OO )#line:132
            requests .request ('get',f'{host}/user',headers =O0000OOOO00OOO0OO )#line:133
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0000OOOO00OOO0OO )#line:134
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0000OOOO00OOO0OO )#line:135
            requests .request ('post',f'{host}/announcement/announcement',headers =O0000OOOO00OOO0OO )#line:136
            requests .request ('get',f'{host}/game/getAllData',headers =O0000OOOO00OOO0OO )#line:137
            requests .request ('get',f'{host}/assets',headers =O0000OOOO00OOO0OO )#line:138
        except Exception as OO0OO0OO0OO0O00OO :#line:139
            print (OO0OO0OO0OO0O00OO )#line:140
    def withdraw (O00O0000000O000OO ):#line:144
        O000OOO0OO0OO0O0O =f'__{timi_new()}'#line:145
        OOOOO0000OOOOOO0O ={'authorization':O00O0000000O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0OO0OO0O0O ),'signstring':O000OOO0OO0OO0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:154
        OOOOO00OO0O000OO0 =requests .request ('get',f'{host}/assets',headers =OOOOO0000OOOOOO0O ).json ()#line:155
        if 'status'in OOOOO00OO0O000OO0 :#line:157
            if OOOOO00OO0O000OO0 ['status']==200 :#line:158
                OO0O0000OO0O00000 =OOOOO00OO0O000OO0 ['data']['cash']#line:159
                if float (OO0O0000OO0O00000 )>20 :#line:160
                    O000OOO0OO0OO0O0O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:161
                    OOOOO0000OOOOOO0O ={'authorization':O00O0000000O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0OO0OO0O0O ),'signstring':O000OOO0OO0OO0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:170
                    O00OO0O000O00O0O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:171
                    OOO0OO0O00000OOOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOOO0000OOOOOO0O ,data =O00OO0O000O00O0O0 ).json ()#line:173
                    print (OOO0OO0O00000OOOO )#line:174
    def invitenum (O00O0O00O0O0OO0OO ):#line:177
        O00O0O00O0O00O0O0 =f'__{timi_new()}'#line:178
        OOO00O00000O00OOO ={'authorization':O00O0O00O0O0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O00O0O00O0O0 ),'signstring':O00O0O00O0O00O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:187
        O00OOOO0OOO00O000 =requests .request ('get',f'{host}/invite/invitenum',headers =OOO00O00000O00OOO ).json ()#line:188
        if 'status'in O00OOOO0OOO00O000 :#line:190
            if O00OOOO0OOO00O000 ['status']==200 :#line:191
                O000O0O000000000O =O00OOOO0OOO00O000 ['data']['invited_count']#line:192
                O00OOOO00000OO0O0 =O00OOOO0OOO00O000 ['data']['invited_second_count']#line:193
                print (f'【我的邀请】:直邀好友:{O000O0O000000000O}丨间邀好友:{O00OOOO00000OO0O0}')#line:194
    def game_map (OO0OO0OOOOOOO0O0O ):#line:197
        try :#line:198
            O00OO0OOOOO00O0O0 =f'__{timi_new()}'#line:199
            O0OOO0OOO0O00O0OO ={'authorization':OO0OO0OOOOOOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OOOOO00O0O0 ),'signstring':O00OO0OOOOO00O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:208
            O0000O00OOOOO00OO =requests .request ('get',f'{host}/game/map',headers =O0OOO0OOO0O00O0OO ).json ()#line:209
            if 'status'in O0000O00OOOOO00OO :#line:211
                if O0000O00OOOOO00OO ['status']==200 :#line:212
                    for O0OO000O00O00O00O in O0000O00OOOOO00OO ['data']['list'][0 ]['crops']:#line:213
                        O0O0000OO0OO00O0O =O0OO000O00O00O00O ['level']#line:215
                        if O0O0000OO0OO00O0O ==41 :#line:216
                            OOOOO0O00OOO00O0O =O0OO000O00O00O00O ['crop_name']#line:217
                            OOO000000O0OOO0OO =O0OO000O00O00O00O ['count']#line:218
                            if OOO000000O0OOO0OO >0 :#line:219
                                print (f'【农业资产】:{OOOOO0O00OOO00O0O}丨数量:{OOO000000O0OOO0OO}')#line:220
        except Exception as O0O00O000OO0O00O0 :#line:221
            print (O0O00O000OO0O00O0 )#line:222
    def give_gold (OOOO0O0000OOOOO00 ):#line:225
        try :#line:226
            O0O00O000O0O00O00 =f'__{timi_new()}'#line:227
            O00O00OOOOO0000O0 ={'authorization':OOOO0O0000OOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O000O0O00O00 ),'signstring':O0O00O000O0O00O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:236
            O0OO000O00O00OO0O =requests .request ('get',f'{host}/user',headers =O00O00OOOOO0000O0 ).json ()#line:237
            if 'status'in O0OO000O00O00OO0O :#line:238
                if O0OO000O00O00OO0O ['status']==200 :#line:239
                    if float (OOOO0O0000OOOOO00 .doneeNo )!=0 :#line:240
                        OOO00O0OO0O0O0000 =O0OO000O00O00OO0O ['data']['assets']['gold']#line:241
                        if float (OOO00O0OO0O0O0000 )>float (OOOO0O0000OOOOO00 .innerId ):#line:242
                            O00O0O0000O000O00 =int (float (OOO00O0OO0O0O0000 )/1.1 )#line:243
                            O0O00O000O0O00O00 =f'_doneeNo={OOOO0O0000OOOOO00.doneeNo}&quantity={O00O0O0000O000O00}_{timi_new()}'#line:244
                            O00O00OOOOO0000O0 ={'authorization':OOOO0O0000OOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O000O0O00O00 ),'signstring':O0O00O000O0O00O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:253
                            O00O0OOOO0O00OOOO ={"quantity":O00O0O0000O000O00 ,"doneeNo":OOOO0O0000OOOOO00 .doneeNo }#line:257
                            OOO000OO0O00O00OO =requests .request ('post',f'{host}/finance/give-gold',headers =O00O00OOOOO0000O0 ,data =O00O0OOOO0O00OOOO ).json ()#line:258
                            if 'status'in OOO000OO0O00O00OO :#line:260
                                if OOO000OO0O00O00OO ['status']==200 :#line:261
                                    if OOO000OO0O00O00OO ['data']:#line:262
                                        print (f'【赠送种子】:赠送{O00O0O0000O000O00}种子给{OOOO0O0000OOOOO00.doneeNo}成功')#line:263
                    else :#line:264
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:265
        except Exception as O0O0O000OOOO0OO0O :#line:266
            print (O0O0O000OOOO0OO0O )#line:267
    def invitation (O00OO0OO0OO0OOOO0 ):#line:269
        try :#line:270
            _O0O0O00OO0O00000O =float (bundled_def ())/4 #line:271
            O0OO00OO00OO0OO0O =f'_innerId={int(_O0O0O00OO0O00000O)}_{timi_new()}'#line:272
            OO0O0000OO0000000 ={'authorization':O00OO0OO0OO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO00OO0OO0O ),'signstring':O0OO00OO00OO0OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:281
            OO0O0O0OOO00OOOOO ={"innerId":int (_O0O0O00OO0O00000O )}#line:282
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO0O0000OO0000000 ,data =OO0O0O0OOO00OOOOO )#line:283
        except Exception as OOOO0O0OO0OOOO0O0 :#line:284
            print (OOOO0O0OO0OOOO0O0 )#line:285
    def winning_rewards (OOOOO00O0O0OOOOO0 ):#line:288
        try :#line:289
            O000OOO00O0OO0OOO =f'__{timi_new()}'#line:290
            O0O000OOOOO0000O0 ={'authorization':OOOOO00O0O0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO00O0OO0OOO ),'signstring':O000OOO00O0OO0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:299
            OOOO00OO000OOOO0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O000OOOOO0000O0 ).json ()#line:300
            if 'status'in OOOO00OO000OOOO0O :#line:302
                if OOOO00OO000OOOO0O ['status']==200 :#line:303
                    if OOOO00OO000OOOO0O ['data']['amount']:#line:304
                        O0O00OO0000OOOO0O =OOOO00OO000OOOO0O ['data']['amount']['gold']#line:305
                        return O0O00OO0000OOOO0O #line:306
                    else :#line:307
                        return 0 #line:308
        except Exception as OO0000O0OO0OO0O00 :#line:309
            print (OO0000O0OO0OO0O00 )#line:310
    def certification (OO0O0O0OO00OOO0OO ):#line:313
        try :#line:314
            O0000O00OO0O00OOO =f'__{timi_new()}'#line:315
            O0O0000O0OO000O0O ={'authorization':OO0O0O0OO00OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00OO0O00OOO ),'signstring':O0000O00OO0O00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:324
            O00OOOOOOOO00000O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0O0000O0OO000O0O ).json ()#line:325
            if 'status'in O00OOOOOOOO00000O :#line:327
                if O00OOOOOOOO00000O ['status']==200 :#line:328
                    if O00OOOOOOOO00000O ['data']['result']:#line:329
                        O0000000O00OO00OO =O00OOOOOOOO00000O ['data']['nick_name']#line:330
                        return O0000000O00OO00OO #line:331
                    else :#line:332
                        return '未实名'#line:333
        except Exception as O00OOOO0O0OO0000O :#line:334
            print (O00OOOO0O0OO0000O )#line:335
    def crops_illustrated (O0OOOO0000O00OOO0 ):#line:338
        try :#line:339
            O0OO000OOOOOOO000 =f'__{timi_new()}'#line:340
            OO000OOO0OO000O00 ={'authorization':O0OOOO0000O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000OOOOOOO000 ),'signstring':O0OO000OOOOOOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:349
            OOO0O0O0O0O000000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO000OOO0OO000O00 ).json ()#line:350
            if 'status'in OOO0O0O0O0O000000 :#line:352
                if OOO0O0O0O0O000000 ['status']==200 :#line:353
                    OO0OO00OO0000O0OO =OOO0O0O0O0O000000 ['data'][0 ]['crops']#line:354
                    for O0O000OO0OO0000O0 in OO0OO00OO0000O0OO :#line:355
                        if O0O000OO0OO0000O0 ['ill_clover_award']:#line:356
                            if float (O0O000OO0OO0000O0 ['ill_clover_award'])>1 :#line:357
                                if O0O000OO0OO0000O0 ['is_finish']:#line:358
                                    if not O0O000OO0OO0000O0 ['is_getit']:#line:359
                                        if O0OOOO0000O00OOO0 .certification ()!='未实名':#line:360
                                            O0OO000OOOOOOO000 =f'_award_level={O0O000OO0OO0000O0["level"]}_{timi_new()}'#line:361
                                            OO000OOO0OO000O00 ={'authorization':O0OOOO0000O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000OOOOOOO000 ),'signstring':O0OO000OOOOOOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:370
                                            O0OOOO0000OOOOO00 ={"award_level":O0O000OO0OO0000O0 ['level']}#line:371
                                            OOOOO0OO0O00OO000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO000OOO0OO000O00 ,json =O0OOOO0000OOOOO00 ).json ()#line:373
                                            if 'status'in OOOOO0OO0O00OO000 :#line:374
                                                if OOOOO0OO0O00OO000 ['status']==200 :#line:375
                                                    O0000OO0OO00000O0 =OOOOO0OO0O00OO000 ['data']['ill_clover_award']#line:376
                                                    print (f'【图鉴奖励】:领取{O0O000OO0OO0000O0["crop_name"]}成就丨奖励{O0000OO0OO00000O0}☘️')#line:378
                                                if OOOOO0OO0O00OO000 ['status']==500 :#line:379
                                                    print (f'【图鉴奖励】:{OOOOO0OO0O00OO000["message"]}')#line:380
        except Exception as OO0OOOOO0O0OO00OO :#line:381
            print (OO0OOOOO0O0OO00OO )#line:382
    def watched_ad (OOO00O0000O0OOO0O ):#line:385
        try :#line:386
            OO0O00OOO0OOO00O0 =f'__{timi_new()}'#line:387
            OO00OO0OOOO0OOOO0 ={'authorization':OOO00O0000O0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOO0OOO00O0 ),'signstring':OO0O00OOO0OOO00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:396
            OO0OOO00O00000000 =requests .request ('get',f'{host}/game/getAllData',headers =OO00OO0OOOO0OOOO0 ).json ()#line:397
            if 'status'in OO0OOO00O00000000 :#line:399
                if OO0OOO00O00000000 ['status']==200 :#line:400
                    if 'offlineInfo'in OO0OOO00O00000000 ['data']:#line:401
                        time .sleep (random .randint (3 ,5 ))#line:402
                        OO0OO0OO00OO0000O =OO0OOO00O00000000 ['data']['offlineInfo']['off_minute']#line:403
                        O00O00OOOO0O0O00O =float (OO0OOO00O00000000 ['data']['silver'])/1000000000000 #line:404
                        time .sleep (1 )#line:405
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO00OO0OOOO0OOOO0 ).json ()#line:406
                        time .sleep (2 )#line:407
                        OO00000O000000000 =requests .request ('get',f'{host}/game/getAllData',headers =OO00OO0OOOO0OOOO0 ).json ()#line:408
                        if 'status'in OO00000O000000000 :#line:410
                            if OO00000O000000000 ['status']==200 :#line:411
                                OO00O0OO0000OO00O =float (OO00000O000000000 ['data']['silver'])/1000000000000 #line:412
                                OO0OOOOOOO0O00000 =str (OO00O0OO0000OO00O -O00O00OOOO0O0O00O )[:6 ]#line:413
                                print (f'【离线奖励】:翻倍离线{OO0OO0OO00OO0000O}分钟奖励🌱数量:{OO0OOOOOOO0O00000}t粒')#line:414
        except Exception as O0OO0O0O0O0OO00OO :#line:415
            print (O0OO0O0O0O0OO00OO )#line:416
    def user_ad (OO0OOO0000O0OO0OO ):#line:419
        try :#line:420
            OOOOO00000OOOOOOO =f'__{timi_new()}'#line:421
            O0OOO0OOO000OOO00 ={'authorization':OO0OOO0000O0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00000OOOOOOO ),'signstring':OOOOO00000OOOOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:430
            O0OO0OOOO00OO0O00 =requests .request ('get',f'{host}/user/ad',headers =O0OOO0OOO000OOO00 ).json ()#line:431
            if 'status'in O0OO0OOOO00OO0O00 :#line:433
                if O0OO0OOOO00OO0O00 ['status']==200 :#line:434
                    O00O000OOO000OOO0 =O0OO0OOOO00OO0O00 ['data']['max_time']#line:435
                    OO00000000O000000 =O0OO0OOOO00OO0O00 ['data']['watch_time']#line:436
                    O0OO0O00OOO0O0000 =O0OO0OOOO00OO0O00 ['data']['added_time']#line:437
                    print (f'【获取种子】:获取🌱剩余{O0OO0O00OOO0O0000 + O00O000OOO000OOO0 - OO00000000O000000}次丨好友提供:{O0OO0O00OOO0O0000}次')#line:438
                    if O0OO0O00OOO0O0000 +O00O000OOO000OOO0 -OO00000000O000000 >0 :#line:439
                        time .sleep (random .randint (16 ,19 ))#line:440
                        OOOO00O0O0O0O0O0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OOO0OOO000OOO00 ).json ()#line:441
                        if 'status'in OOOO00O0O0O0O0O0O :#line:443
                            if OOOO00O0O0O0O0O0O ['status']==200 :#line:444
                                O0O0OOO000O0OO000 =float (OOOO00O0O0O0O0O0O ['data']['silver'])/1000000000000 #line:445
                                print (f'【获取种子】:获得🌱:{int(O0O0OOO000O0OO000)}t粒')#line:446
                                return True #line:447
                            if OOOO00O0O0O0O0O0O ['status']==500 :#line:448
                                OO0OOO000000O0O0O =OOOO00O0O0O0O0O0O ['message']#line:449
                                print (f'【获取种子】:{OO0OOO000000O0O0O}')#line:450
                                return False #line:451
        except Exception as OO000O0O0O0O0OOO0 :#line:452
            print (OO000O0O0O0O0OOO0 )#line:453
    def synthetic (OO0O0O0OOO0000O00 ):#line:456
        global id ,g #line:457
        try :#line:458
            OO0O000O0OO0O0OOO =OO0O0O0OOO0000O00 .level_new ()#line:459
            O0OO000O0O0O0OO0O =random .randint (9 ,11 )#line:460
            OOOO00OO0OO00000O =f'_site=8&targetSite={O0OO000O0O0O0OO0O}_{timi_new()}'#line:461
            O00OOOO00000OO00O ={'accept':'application/json, text/plain, */*','authorization':OO0O0O0OOO0000O00 .token ,'timestamp':timi_new (),'sign':sign (OOOO00OO0OO00000O ),'signstring':OOOO00OO0OO00000O ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:476
            OO0OO00000OO0000O ={"site":int (8 ),"targetSite":int (O0OO000O0O0O0OO0O )}#line:477
            requests .request ('post',f'{host}/game/crops/move',headers =O00OOOO00000OO00O ,json =OO0OO00000OO0000O )#line:478
            while True :#line:479
                OO0O0O0OO0O0O0O00 =f'__{timi_new()}'#line:480
                O00O0O000OOOOO0O0 ={'authorization':OO0O0O0OOO0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OO0O0O0O00 ),'signstring':OO0O0O0OO0O0O0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:489
                O0O0OOOO000OOO000 =requests .request ('get',f'{host}/game/getAllData',headers =O00O0O000OOOOO0O0 ).json ()#line:490
                if 'status'in O0O0OOOO000OOO000 :#line:492
                    if O0O0OOOO000OOO000 ['status']==200 :#line:493
                        O0O0OOOO00O00OOOO =O0O0OOOO000OOO000 ['data']['cropList']#line:494
                        OO0O00000000O0O0O =O0O0OOOO000OOO000 ['data']['gameCoreDataDBid']#line:495
                        OOOOO00OO000O0OO0 =float (O0O0OOOO000OOO000 ['data']['silver'])/1000000000000 #line:496
                        OOO000000O00O0OO0 =0 #line:501
                        for O0OO0O00O00000OOO in O0O0OOOO00O00OOOO :#line:502
                            if not O0OO0O00O00000OOO :#line:503
                                OOO0OO00000OOOOOO =f'_crop_id={OO0O00000000O0O0O}&site={OOO000000O00O0OO0}_{OO0O0O0OOO0000O00.time}'#line:504
                                OO000OOO0O0O0O0OO ={'authorization':OO0O0O0OOO0000O00 .token ,'timestamp':OO0O0O0OOO0000O00 .time ,'sign':sign (OOO0OO00000OOOOOO ),'signstring':OOO0OO00000OOOOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
                                OO0OOOO00O0O0OO00 ={"site":OOO000000O00O0OO0 ,"crop_id":OO0O00000000O0O0O }#line:514
                                O00OO00OO0OOO0000 =requests .request ('post',f'{host}/game/crops/buy',headers =OO000OOO0O0O0O0OO ,data =OO0OOOO00O0O0OO00 ).json ()#line:515
                                time .sleep (random .randint (1 ,3 )/10 )#line:517
                                if 'status'in O00OO00OO0OOO0000 :#line:518
                                    if O00OO00OO0OOO0000 ['status']==200 :#line:519
                                        if O00OO00OO0OOO0000 ['message']=='种子数量不足':#line:520
                                            OO0O000O0OO0O0OOO =OO0O0O0OOO0000O00 .level_new ()#line:521
                                            print (f'【种植合成】:{O00OO00OO0OOO0000["message"]}')#line:522
                                            if not OO0O0O0OOO0000O00 .user_ad ():#line:523
                                                return False #line:524
                                    if O00OO00OO0OOO0000 ['status']==500 :#line:525
                                        print (f'【种植合成】:{O00OO00OO0OOO0000["message"]}')#line:526
                                        return False #line:527
                            OOO000000O00O0OO0 +=1 #line:528
                        O0O00OOO00O0O0OOO =requests .request ('get',f'{host}/game/getAllData',headers =O00O0O000OOOOO0O0 ).json ()#line:529
                        O0OO00O00OO0O00O0 =O0O00OOO00O0O0OOO ['data']['cropList']#line:530
                        O00OOO00O00OOO0OO =False #line:531
                        for O0OO0O00O00000OOO in range (12 ):#line:532
                            id =O0OO00O00OO0O00O0 [O0OO0O00O00000OOO ]['level']#line:533
                            if float (OO0O000O0OO0O0OOO )-float (id )>9 :#line:534
                                O00OOOOO00O000000 =f'_site={O0OO0O00O00000OOO}_{timi_new()}'#line:535
                                OOO00000O0OO0000O ={'accept':'application/json, text/plain, */*','authorization':OO0O0O0OOO0000O00 .token ,'timestamp':timi_new (),'sign':sign (O00OOOOO00O000000 ),'signstring':O00OOOOO00O000000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:545
                                O000O0O00O00O0OO0 ={"site":O0OO0O00O00000OOO }#line:546
                                O0OOOO00OOO0OOOOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO00000O0OO0000O ,data =O000O0O00O00O0OO0 ).json ()#line:548
                                if 'status'in O0OOOO00OOO0OOOOO :#line:549
                                    if O0OOOO00OOO0OOOOO ['status']==200 :#line:550
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:551
                            if id !=0 :#line:552
                                for O00OOO0O00OOO0OOO in range (11 ):#line:553
                                    OOO0OOO0OOO00OOO0 =O00OOO0O00OOO0OOO +1 #line:554
                                    g =O0OO00O00OO0O00O0 [OOO0OOO0OOO00OOO0 ]['level']#line:555
                                    if id ==g :#line:556
                                        O0000OO0O00O0000O =O00OOO0O00OOO0OOO +2 #line:557
                                        if O0000OO0O00O0000O !=O0OO0O00O00000OOO +1 :#line:558
                                            OOOO0O00O0OOOO0O0 =O0OO0O00O00000OOO +1 #line:559
                                            time .sleep (random .randint (1 ,3 )/10 )#line:561
                                            OOOO00OO0OO00000O =f'_site={OOOO0O00O0OOOO0O0 - 1}&targetSite={O0000OO0O00O0000O - 1}_{timi_new()}'#line:562
                                            O00OOOO00000OO00O ={'accept':'application/json, text/plain, */*','authorization':OO0O0O0OOO0000O00 .token ,'timestamp':timi_new (),'sign':sign (OOOO00OO0OO00000O ),'signstring':OOOO00OO0OO00000O ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:577
                                            O00OOOOOOO0O00000 ={"site":int (OOOO0O00O0OOOO0O0 -1 ),"targetSite":int (O0000OO0O00O0000O -1 )}#line:578
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00OOOO00000OO00O ,json =O00OOOOOOO0O00000 )#line:579
                                            O00OOO00O00OOO0OO =True #line:581
                                    if O00OOO00O00OOO0OO :#line:582
                                        break #line:583
                                if O00OOO00O00OOO0OO :#line:584
                                    break #line:585
        except :#line:586
            OO0O0O0OOO0000O00 .synthetic ()#line:587
    def level_new (O00000OOOO0OO0OO0 ):#line:590
        try :#line:591
            OOO0OO000OOOO0O00 =f'__{timi_new()}'#line:592
            OO0OOOO0O0O0OOOOO ={'authorization':O00000OOOO0OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO000OOOO0O00 ),'signstring':OOO0OO000OOOO0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:601
            OOO00OOOO0OOOO0O0 =requests .request ('get',f'{host}/user',headers =OO0OOOO0O0O0OOOOO ).json ()#line:602
            if 'status'in OOO00OOOO0OOOO0O0 :#line:603
                if OOO00OOOO0OOOO0O0 ['status']==200 :#line:604
                    return float (OOO00OOOO0OOOO0O0 ['data']['level'])#line:605
        except Exception as OO000O00OO0OOO0O0 :#line:606
            print (OO000O00OO0OOO0O0 )#line:607
    def propsraffle (OO00O0O00OO000OOO ):#line:610
        try :#line:611
            while True :#line:612
                O000000OO00O0O00O =f'__{timi_new()}'#line:613
                OO0O00O00OO0OO0O0 ={'authorization':OO00O0O00OO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000000OO00O0O00O ),'signstring':O000000OO00O0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:622
                OOO00OOO0O000000O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0O00O00OO0OO0O0 ).json ()#line:623
                if 'status'in OOO00OOO0O000000O :#line:625
                    if OOO00OOO0O000000O ['status']==200 :#line:626
                        OOOOO00O0O0O0O0O0 =OOO00OOO0O000000O ['data']['rows']#line:627
                        OO0000OOO00OO0OOO =OOO00OOO0O000000O ['data']['vstate']#line:628
                        if OOOOO00O0O0O0O0O0 ==5 or OOOOO00O0O0O0O0O0 ==6 or OOOOO00O0O0O0O0O0 ==7 :#line:629
                            OOOO000O0OOOO00OO =OOO00OOO0O000000O ['data']['silver']#line:630
                            print (f'【转盘抽奖】:获得种子:{OOOO000O0OOOO00OO}')#line:631
                        if OOOOO00O0O0O0O0O0 ==1 or OOOOO00O0O0O0O0O0 ==2 or OOOOO00O0O0O0O0O0 ==3 :#line:632
                            O000OO0O0OOO000OO =OOO00OOO0O000000O ['data']['clover']#line:633
                            print (f'【转盘抽奖】:获得三叶草:{O000OO0O0OOO000OO}')#line:634
                        if OOOOO00O0O0O0O0O0 ==4 or OOOOO00O0O0O0O0O0 ==8 :#line:635
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:636
                        if OOOOO00O0O0O0O0O0 =='抽奖次数已用完':#line:640
                            break #line:673
                time .sleep (random .randint (8 ,15 )/10 )#line:674
        except Exception as O0000O0000O0O0000 :#line:675
            print (O0000O0000O0O0000 )#line:676
    def friends_invitation (OOOO00O0OOO0O00OO ):#line:679
        try :#line:680
            O0OO0000O0OO00OOO =f'__{timi_new()}'#line:681
            O0O00OOOOOOOO0OOO ={'authorization':OOOO00O0OOO0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0000O0OO00OOO ),'signstring':O0OO0000O0OO00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:690
            O0OO0O0OO0OOO0OO0 =requests .request ('get',f'{host}/friends',headers =O0O00OOOOOOOO0OOO ).json ()#line:691
            if 'status'in O0OO0O0OO0OOO0OO0 :#line:692
                if O0OO0O0OO0OOO0OO0 ['status']==200 :#line:693
                    OO0O00OOO0000O000 =O0OO0O0OO0OOO0OO0 ['data']['myInviteter']#line:694
                    if OO0O00OOO0000O000 :#line:695
                        O000O0O00OOOO00OO =OO0O00OOO0000O000 ['user']['nickname']#line:696
                        OOOOOO0O0000000OO =OOOO00O0OOO0O00OO .certification ()#line:697
                        print (f'【查邀请人】:我的邀请人:{O000O0O00OOOO00OO}丨实名:{OOOOOO0O0000000OO}')#line:698
                    else :#line:699
                        if OOOO00O0OOO0O00OO .innerId !='0':#line:700
                            OOOO00O0OOO0O00OO .invitation ()#line:701
        except Exception as OOOO0O0OO0O00O000 :#line:702
            print (OOOO0O0OO0O00O000 )#line:703
    def add_clover (OO000O0O0OO0O0000 ):#line:706
        global golden_seed #line:707
        try :#line:708
            OOOO0OOO00OOO0000 =f'__{timi_new()}'#line:709
            OO0OO0000OO0O000O ={'authorization':OO000O0O0OO0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO00OOO0000 ),'signstring':OOOO0OOO00OOO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:718
            O000000O0O000000O =requests .request ('get',f'{host}/assets/clovers',headers =OO0OO0000OO0O000O ).json ()#line:719
            if 'status'in O000000O0O000000O :#line:721
                if O000000O0O000000O ['status']==200 :#line:722
                    O000OO0000O0O00O0 =O000000O0O000000O ['data']['clover']#line:723
                    OO00O0O0OO0OOOO0O =O000000O0O000000O ['data']['used_clover']#line:724
                    OOO0O00O000OOO0O0 =float (O000OO0000O0O00O0 )-float (OO00O0O0OO0OOOO0O )#line:725
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO00O0O0OO0OOOO0O}')#line:726
                    if OO000O0O0OO0O0000 .certification ()!='未实名':#line:727
                        if OOO0O00O000OOO0O0 >1 :#line:728
                            OOOO0OOO00OOO0000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO0O00O000OOO0O0)}_{timi_new()}'#line:729
                            O0O0000000OOOO000 ={'authorization':OO000O0O0OO0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO00OOO0000 ),'signstring':OOOO0OOO00OOO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:738
                            O0O0OO0O000000000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO0O00O000OOO0O0 )}#line:739
                            O00OO0O000000O0OO =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O0000000OOOO000 ,data =O0O0OO0O000000000 ).json ()#line:740
                            if 'status'in O00OO0O000000O0OO :#line:742
                                if O00OO0O000000O0OO ['status']==200 :#line:743
                                    print (f'【参与抽奖】:添加☘️:{O00OO0O000000O0OO["data"]}丨数量:{OOO0O00O000OOO0O0}')#line:744
                                if O00OO0O000000O0OO ['status']==500 :#line:745
                                    print (f'【参与抽奖】:添加☘️:{O00OO0O000000O0OO["message"]}')#line:746
            O0OO0OOOO000000O0 =requests .request ('get',f'{host}/lottery',headers =OO0OO0000OO0O000O ).json ()#line:747
            O0O00OOO00OO00OO0 =OO000O0O0OO0O0000 .winning_rewards ()#line:749
            if 'status'in O0OO0OOOO000000O0 :#line:750
                if O0OO0OOOO000000O0 ['status']==200 :#line:751
                    O00O0OOOO00OOOO0O =O0OO0OOOO000000O0 ['data'][0 ]['day_get_gold_quantity']#line:752
                    golden_seed +=float (O00O0OOOO00OOOO0O )#line:753
                    O00O000OO0000OO0O =O0OO0OOOO000000O0 ['data'][1 ]['value']#line:754
                    OO000O00O0OOO00OO =O0OO0OOOO000000O0 ['data'][0 ]['join_number']#line:755
                    OOOOO00O0OOO00OO0 =int (float (O0OO0OOOO000000O0 ['data'][0 ]['totalValue']))#line:756
                    O0O00OO0O000O0O0O =float (O00O000OO0000OO0O /OOOOO00O0OOO00OO0 )*10000 #line:757
                    O0O00O00OOO00OOO0 =OOOOO00O0OOO00OO0 /OO000O00O0OOO00OO #line:758
                    print (f'【参与抽奖】:预计每天中{str(O00O0OOOO00OOOO0O)[:6]}颗金种子丨好友收益:{str(O0O00OOO00OO00OO0)[:6]}')#line:759
                    print (f'【抽奖统计】:每1万☘️中{str(O0O00OO0O000O0O0O)[:6]}颗金种子丨☘️人均:{str(O0O00O00OOO00OOO0)[:7]}️')#line:760
        except Exception as OO0O00O0O0O0O00OO :#line:761
            print (OO0O00O0O0O0O00OO )#line:762
    def energy (OO00OO00OO0OO00OO ):#line:766
        try :#line:767
            while True :#line:768
                O0OO000OOOO00OO0O =f'__{timi_new()}'#line:769
                OOOOO00O0OOOO0OOO ={'authorization':OO00OO00OO0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000OOOO00OO0O ),'signstring':O0OO000OOOO00OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:778
                O00O00O00OO00OO0O =requests .request ('get',f'{host}/energy/general',headers =OOOOO00O0OOOO0OOO ).json ()#line:779
                if 'status'in O00O00O00OO00OO0O :#line:781
                    if O00O00O00OO00OO0O ['status']==200 :#line:782
                        OO0OOOO0O000O0O0O =O00O00O00OO00OO0O ['data']['ordinary_water']#line:783
                        OO0O000O00OO0OOOO =O00O00O00OO00OO0O ['data']['ordinary_fertilizer']#line:784
                        O00O00O00OO0O00O0 =O00O00O00OO00OO0O ['data']['videoStatus']#line:785
                        print (f'【我的营养】:肥料:{str(OO0O000O00OO0OOOO).split(".")[0]}丨水滴:{str(OO0OOOO0O000O0O0O).split(".")[0]}')#line:786
                        if float (OO0O000O00OO0OOOO )<96 :#line:787
                            if O00O00O00OO0O00O0 :#line:788
                                time .sleep (random .randint (160 ,180 )/10 )#line:789
                                OO0OOOOO00OOOO00O =99 -float (OO0O000O00OO0OOOO )#line:790
                                OO00OO000OO0OO0OO ={"fertilizer":str (OO0OOOOO00OOOO00O ).split ('.')[0 ]}#line:791
                                OOOOO0O000O00OO00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOOO00O0OOOO0OOO ).json ()#line:792
                                if 'status'in OOOOO0O000O00OO00 :#line:794
                                    if OOOOO0O000O00OO00 ['status']==200 :#line:795
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOO0O000O00OO00["message"]}')#line:796
                                    if OOOOO0O000O00OO00 ['status']==500 :#line:797
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOO0O000O00OO00["message"]}')#line:798
                                        break #line:799
                        if float (OO0OOOO0O000O0O0O )<880 :#line:800
                            time .sleep (random .randint (160 ,180 )/10 )#line:801
                            O0OOO00O0OOO0000O =999 -float (OO0OOOO0O000O0O0O )#line:802
                            O00O0O00O00OO000O ={"water":str (O0OOO00O0OOO0000O ).split ('.')[0 ]}#line:803
                            OO00O00O00O00O0OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOOO00O0OOOO0OOO ).json ()#line:804
                            if 'status'in OO00O00O00O00O0OO :#line:806
                                if OO00O00O00O00O0OO ['status']==200 :#line:807
                                    print (f'【购买水滴】:看广告获取水滴:{OO00O00O00O00O0OO["message"]}')#line:808
                                if OO00O00O00O00O0OO ['status']==500 :#line:809
                                    print (f'【购买水滴】:看广告获取水滴:{OO00O00O00O00O0OO["message"]}')#line:810
                                    break #line:811
                        break #line:813
        except Exception as OO000O0O00O000OO0 :#line:815
            print (OO000O0O00O000OO0 )#line:816
def bundled_def ():#line:818
    OO000OOO0OOOOO00O =['5570536','7750212','7911652','7911680','7805624']#line:819
    return OO000OOO0OOOOO00O [random .randint (0 ,len (OO000OOO0OOOOO00O )-1 )]#line:820
def version_of_the_validation ():#line:824
    return str ((81 -56 )/10 )#line:825
def gitee_validation ():#line:828
    try :#line:829
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:830
    except :#line:831
        sys .exit (0 )#line:832
def update_the_validation ():#line:836
    try :#line:837
        O00O00O000OOO0OOO =gitee_validation ()#line:838
        if version_of_the_validation ()<O00O00O000OOO0OOO ['CityEarth']['edition']:#line:839
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O00O000OOO0OOO["CityEarth"]["edition"]}   ❌')#line:840
            print (f'更新内容=>>{O00O00O000OOO0OOO["CityEarth"]["content"]}   🎉')#line:841
        else :#line:842
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O00O000OOO0OOO["CityEarth"]["edition"]}   ✅')#line:843
            print (f'更新内容=>> {O00O00O000OOO0OOO["CityEarth"]["content"]}   🎉')#line:844
    except Exception as O0O00O0O00O0OOO0O :#line:845
        print (O0O00O0O00O0OOO0O )#line:846
def os_qinglong ():#line:849
    if application in os .environ :#line:850
        OO0OOO000OO0OO000 =os .environ [application ].split ('\n')#line:851
        if len (OO0OOO000OO0OO000 )>0 :#line:852
            return OO0OOO000OO0OO000 #line:853
        else :#line:854
            print (f"{application}变量未启用")#line:855
            print ('脚本退出')#line:856
            sys .exit (1 )#line:857
    else :#line:858
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:860
        return os_built ()#line:861
def os_built ():#line:864
    if token :#line:865
        OOOOOOO0OOO0O0000 =token .split ('\n')#line:866
        if len (OOOOOOO0OOO0O0000 )>0 :#line:867
            return OOOOOOO0OOO0O0000 #line:868
    else :#line:869
        print (f"内置变量为空")#line:870
        print ('脚本结束')#line:871
        sys .exit (0 )#line:872
if __name__ =='__main__':#line:875
    start ()#line:876
