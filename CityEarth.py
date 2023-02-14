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
        OOOO00O00O00O00OO =os_qinglong ()#line:10
        print (f"==========共找到{len(OOOO00O00O00O00OO)}个账号==========")#line:11
        for OOO00O0OOO0000O0O in OOOO00O00O00O00OO :#line:12
            OO000O00OO0OO000O =[]#line:13
            print (f"------------正在执行第{OOOO00O00O00O00OO.index(OOO00O0OOO0000O0O) + 1}个账号------------")#line:14
            OOOO00O00OOOO0O00 =CityEarth (OOO00O0OOO0000O0O ,OO000O00OO0OO000O )#line:15
            def O00O00O0OO00000O0 ():#line:17
                if OOOO00O00OOOO0O00 .base_info ():#line:19
                    OOOO00O00OOOO0O00 .sealing ()#line:21
                    OOOO00O00OOOO0O00 .invitenum ()#line:23
                    OOOO00O00OOOO0O00 .game_map ()#line:25
                    OOOO00O00OOOO0O00 .friends_invitation ()#line:27
                    OOOO00O00OOOO0O00 .add_clover ()#line:29
                    OOOO00O00OOOO0O00 .propsraffle ()#line:31
                    OOOO00O00OOOO0O00 .synthetic ()#line:33
                    OOOO00O00OOOO0O00 .crops_illustrated ()#line:35
                    OOOO00O00OOOO0O00 .give_gold ()#line:37
                    OOOO00O00OOOO0O00 .withdraw ()#line:39
                    OOOO00O00OOOO0O00 .energy ()#line:41
            O000O00O0O000OO0O =threading .Thread (target =O00O00O0OO00000O0 )#line:42
            O000O00O0O000OO0O .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        OOO0O00000OO00000 =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOO0O00000OO00000 +' ')#line:48
    except Exception as O0O00O0000OO0000O :#line:49
        print (O0O00O0000OO0000O )#line:50
def sign (O00OO0OO00OOOOOOO ):#line:53
    O0O0O00O000OO0O00 =hashlib .md5 (O00OO0OO00OOOOOOO .encode ()).hexdigest ()#line:54
    O0OO00OOO00OO0OO0 ="scsc%^&*"+O0O0O00O000OO0O00 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    O0O0O00OO00O00000 =hashlib .md5 (O0OO00OOO00OO0OO0 .encode ()).hexdigest ()#line:56
    return O0O0O00OO00O00000 #line:57
def format_msg ():#line:59
    OO0OO0OO00O0O000O =""#line:60
    for OO000O0OO00O00OOO in msg_list :#line:61
        OO0OO0OO00O0O000O +=str (OO000O0OO00O00OOO )+"\r\n"#line:62
    return OO0OO0OO00O0O000O #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (O00O0OO00O000O000 ,O00000OO000000OOO ,O0O000OOOOOOO0OO0 ):#line:71
        try :#line:72
            O00O0OO00O000O000 .msg =O0O000OOOOOOO0OO0 #line:73
            O00O0OO00O000O000 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            O00O0OO00O000O000 .token =O00000OO000000OOO .split ('&')[0 ]#line:75
            O00O0OO00O000O000 .innerId =O00000OO000000OOO .split ('&')[1 ]#line:76
            O00O0OO00O000O000 .doneeNo =O00000OO000000OOO .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (O0OOO00OO0000OOO0 ):#line:82
        try :#line:83
            O0OOO00OO0000OOO0 .watched_ad ()#line:85
            OOO0O00OO0O0O000O =f'__{timi_new()}'#line:86
            OOO00OO000000OO0O ={'authorization':O0OOO00OO0000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00OO0O0O000O ),'signstring':OOO0O00OO0O0O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            OOO00O00OO0OOO00O =requests .request ('get',f'{host}/user',headers =OOO00OO000000OO0O ).json ()#line:96
            if 'status'in OOO00O00OO0OOO00O :#line:98
                if OOO00O00OO0OOO00O ['status']==200 :#line:99
                    OO0O0O0OOOO00OOOO =OOO00O00OO0OOO00O ['data']['nickname']#line:100
                    OOO0O0O0OO000OO0O =OOO00O00OO0OOO00O ['data']['inner_id']#line:101
                    OOOO00OO00OOO00O0 =OOO00O00OO0OOO00O ['data']['assets']['gold']#line:102
                    OO0OO00OO000O0O00 =OOO00O00OO0OOO00O ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{OO0O0O0OOOO00OOOO[:5]}丨ID:{OOO0O0O0OO000OO0O}丨等级:{OO0OO00OO000O0O00}丨种子:{str(OOOO00OO00OOO00O0).split(".")[0]}')#line:104
                if OOO00O00OO0OOO00O ['status']==401 :#line:105
                    print (OOO00O00OO0OOO00O ['message'])#line:106
                    O0OOO00OO0000OOO0 .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if OOO00O00OO0OOO00O ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as OOOOOO0O000O000OO :#line:112
            print (OOOOOO0O000O000OO )#line:113
    def sealing (O0OO0O0O000OO0O0O ):#line:116
        try :#line:117
            O0OOO0OOO00OO0OO0 =f'__{timi_new()}'#line:118
            OO00OO00O0OOO000O ={'authorization':O0OO0O0O000OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OOO00OO0OO0 ),'signstring':O0OOO0OOO00OO0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO00OO00O0OOO000O )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =OO00OO00O0OOO000O )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO00OO00O0OOO000O )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO00OO00O0OOO000O )#line:131
            requests .request ('get',f'{host}/user',headers =OO00OO00O0OOO000O )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO00OO00O0OOO000O )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO00OO00O0OOO000O )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =OO00OO00O0OOO000O )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =OO00OO00O0OOO000O )#line:136
            requests .request ('get',f'{host}/assets',headers =OO00OO00O0OOO000O )#line:137
        except Exception as OOOOOOO00OO0OO0O0 :#line:138
            print (OOOOOOO00OO0OO0O0 )#line:139
    def withdraw (O0O0000OO0O0O0000 ):#line:143
        OOO0000OO0OOO0000 =f'__{timi_new()}'#line:144
        OOO000OOO000O0O00 ={'authorization':O0O0000OO0O0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OO0OOO0000 ),'signstring':OOO0000OO0OOO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        O0OOO00OO000O0O0O =requests .request ('get',f'{host}/assets',headers =OOO000OOO000O0O00 ).json ()#line:154
        if 'status'in O0OOO00OO000O0O0O :#line:156
            if O0OOO00OO000O0O0O ['status']==200 :#line:157
                O0O0O0OO0O0O0OO0O =O0OOO00OO000O0O0O ['data']['cash']#line:158
                if float (O0O0O0OO0O0O0OO0O )>20 :#line:159
                    OOO0000OO0OOO0000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    OOO000OOO000O0O00 ={'authorization':O0O0000OO0O0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OO0OOO0000 ),'signstring':OOO0000OO0OOO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    O000O00O0O00OO00O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    O0O00OOO0000OO0OO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOO000OOO000O0O00 ,data =O000O00O0O00OO00O ).json ()#line:172
                    print (O0O00OOO0000OO0OO )#line:173
    def invitenum (O0O00O00OO00O0000 ):#line:176
        O00O000OO000O0000 =f'__{timi_new()}'#line:177
        OO0000OO0OO0OO00O ={'authorization':O0O00O00OO00O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OO000O0000 ),'signstring':O00O000OO000O0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O0O0O0OOOO0O00000 =requests .request ('get',f'{host}/invite/invitenum',headers =OO0000OO0OO0OO00O ).json ()#line:187
        if 'status'in O0O0O0OOOO0O00000 :#line:189
            if O0O0O0OOOO0O00000 ['status']==200 :#line:190
                OOO00000000OOO0OO =O0O0O0OOOO0O00000 ['data']['invited_count']#line:191
                OO0000OO0O0OO0OO0 =O0O0O0OOOO0O00000 ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OOO00000000OOO0OO}丨间邀好友:{OO0000OO0O0OO0OO0}')#line:193
    def game_map (OOO000O0O0O000OOO ):#line:196
        try :#line:197
            OOOOO00O000O00O0O =f'__{timi_new()}'#line:198
            OO0O0OOO00O0000OO ={'authorization':OOO000O0O0O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O000O00O0O ),'signstring':OOOOO00O000O00O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            O0O00OOO0000OOO0O =requests .request ('get',f'{host}/game/map',headers =OO0O0OOO00O0000OO ).json ()#line:208
            if 'status'in O0O00OOO0000OOO0O :#line:210
                if O0O00OOO0000OOO0O ['status']==200 :#line:211
                    for O0OOO0000000O00OO in O0O00OOO0000OOO0O ['data']['list'][0 ]['crops']:#line:212
                        O0O0OO000OO0O00OO =O0OOO0000000O00OO ['level']#line:214
                        if O0O0OO000OO0O00OO ==41 :#line:215
                            O0000O0OO0000O000 =O0OOO0000000O00OO ['crop_name']#line:216
                            OO000O00000000OOO =O0OOO0000000O00OO ['count']#line:217
                            if OO000O00000000OOO >0 :#line:218
                                print (f'【农业资产】:{O0000O0OO0000O000}丨数量:{OO000O00000000OOO}')#line:219
        except Exception as O0OOO00O0O0OO0O00 :#line:220
            print (O0OOO00O0O0OO0O00 )#line:221
    def give_gold (O0O0O0O000O0O00O0 ):#line:224
        try :#line:225
            O00O00OOOO000000O =f'__{timi_new()}'#line:226
            O00O0OO00OOOOO00O ={'authorization':O0O0O0O000O0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OOOO000000O ),'signstring':O00O00OOOO000000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            OOOO00000OOO00000 =requests .request ('get',f'{host}/user',headers =O00O0OO00OOOOO00O ).json ()#line:236
            if 'status'in OOOO00000OOO00000 :#line:237
                if OOOO00000OOO00000 ['status']==200 :#line:238
                    if float (O0O0O0O000O0O00O0 .doneeNo )!=0 :#line:239
                        OO000O0OOOOOO00OO =OOOO00000OOO00000 ['data']['assets']['gold']#line:240
                        if float (OO000O0OOOOOO00OO )>float (O0O0O0O000O0O00O0 .innerId ):#line:241
                            O00O00O0O0OO0O0O0 =int (float (OO000O0OOOOOO00OO )/1.1 )#line:242
                            O00O00OOOO000000O =f'_doneeNo={O0O0O0O000O0O00O0.doneeNo}&quantity={O00O00O0O0OO0O0O0}_{timi_new()}'#line:243
                            O00O0OO00OOOOO00O ={'authorization':O0O0O0O000O0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OOOO000000O ),'signstring':O00O00OOOO000000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            OO0O0000O0OO00OOO ={"quantity":O00O00O0O0OO0O0O0 ,"doneeNo":O0O0O0O000O0O00O0 .doneeNo }#line:256
                            O0O0OO0O00O000OOO =requests .request ('post',f'{host}/finance/give-gold',headers =O00O0OO00OOOOO00O ,data =OO0O0000O0OO00OOO ).json ()#line:257
                            if 'status'in O0O0OO0O00O000OOO :#line:259
                                if O0O0OO0O00O000OOO ['status']==200 :#line:260
                                    if O0O0OO0O00O000OOO ['data']:#line:261
                                        print (f'【赠送种子】:赠送{O00O00O0O0OO0O0O0}种子给{O0O0O0O000O0O00O0.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as OO00O0O0O00000O0O :#line:265
            print (OO00O0O0O00000O0O )#line:266
    def invitation (OO0O00O0OO0000O0O ):#line:268
        try :#line:269
            _O0OOOO0O0O000O00O =float (bundled_def ())/4 #line:270
            OOOOOO00OOOO00000 =f'_innerId={int(_O0OOOO0O0O000O00O)}_{timi_new()}'#line:271
            OO000OO00O00O0OO0 ={'authorization':OO0O00O0OO0000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00OOOO00000 ),'signstring':OOOOOO00OOOO00000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            O0OOO0O00OO00OOOO ={"innerId":int (_O0OOOO0O0O000O00O )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO000OO00O00O0OO0 ,data =O0OOO0O00OO00OOOO )#line:282
        except Exception as OOO000O00OO000OOO :#line:283
            print (OOO000O00OO000OOO )#line:284
    def winning_rewards (OOOO0OOOO00OO0000 ):#line:287
        try :#line:288
            O00O0OOO0OOOOOO0O =f'__{timi_new()}'#line:289
            OO0000OO0O0O0O0OO ={'authorization':OOOO0OOOO00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO0OOOOOO0O ),'signstring':O00O0OOO0OOOOOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            OO00OOOOOO000O0OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO0000OO0O0O0O0OO ).json ()#line:299
            if 'status'in OO00OOOOOO000O0OO :#line:301
                if OO00OOOOOO000O0OO ['status']==200 :#line:302
                    if OO00OOOOOO000O0OO ['data']['amount']:#line:303
                        OO0OOOOO00O0000OO =OO00OOOOOO000O0OO ['data']['amount']['gold']#line:304
                        return OO0OOOOO00O0000OO #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as OO000OOO0O00000OO :#line:308
            print (OO000OOO0O00000OO )#line:309
    def certification (O00O0000O00OOO0OO ):#line:312
        try :#line:313
            O0O0000O0OO0OOO00 =f'__{timi_new()}'#line:314
            O00O0OOOOOO00OOOO ={'authorization':O00O0000O00OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000O0OO0OOO00 ),'signstring':O0O0000O0OO0OOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            O0OOOOO00OO000OO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00O0OOOOOO00OOOO ).json ()#line:324
            if 'status'in O0OOOOO00OO000OO0 :#line:326
                if O0OOOOO00OO000OO0 ['status']==200 :#line:327
                    if O0OOOOO00OO000OO0 ['data']['result']:#line:328
                        O000OOO0O00O0O000 =O0OOOOO00OO000OO0 ['data']['nick_name']#line:329
                        return O000OOO0O00O0O000 #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as OOO0O0O0O0000OOOO :#line:333
            print (OOO0O0O0O0000OOOO )#line:334
    def crops_illustrated (OOOOO000OOO00OOOO ):#line:337
        try :#line:338
            O0OO000O0000OOO0O =f'__{timi_new()}'#line:339
            O0000000OOOOOOO00 ={'authorization':OOOOO000OOO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O0000OOO0O ),'signstring':O0OO000O0000OOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            O0O0OOOO0OO0OO0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0000000OOOOOOO00 ).json ()#line:349
            if 'status'in O0O0OOOO0OO0OO0O0 :#line:351
                if O0O0OOOO0OO0OO0O0 ['status']==200 :#line:352
                    OOO0O0OOO0OO0OO0O =O0O0OOOO0OO0OO0O0 ['data'][0 ]['crops']#line:353
                    for O00O0O00O0OO0000O in OOO0O0OOO0OO0OO0O :#line:354
                        if O00O0O00O0OO0000O ['ill_clover_award']:#line:355
                            if float (O00O0O00O0OO0000O ['ill_clover_award'])>1 :#line:356
                                if O00O0O00O0OO0000O ['is_finish']:#line:357
                                    if not O00O0O00O0OO0000O ['is_getit']:#line:358
                                        if OOOOO000OOO00OOOO .certification ()!='未实名':#line:359
                                            O0OO000O0000OOO0O =f'_award_level={O00O0O00O0OO0000O["level"]}_{timi_new()}'#line:360
                                            O0000000OOOOOOO00 ={'authorization':OOOOO000OOO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O0000OOO0O ),'signstring':O0OO000O0000OOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            O0O000OO000OO00O0 ={"award_level":O00O0O00O0OO0000O ['level']}#line:370
                                            O0O0OO0OOO0000O00 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0000000OOOOOOO00 ,json =O0O000OO000OO00O0 ).json ()#line:372
                                            if 'status'in O0O0OO0OOO0000O00 :#line:373
                                                if O0O0OO0OOO0000O00 ['status']==200 :#line:374
                                                    OOO000OOOO00O0OO0 =O0O0OO0OOO0000O00 ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{O00O0O00O0OO0000O["crop_name"]}成就丨奖励{OOO000OOOO00O0OO0}叶子成功')#line:377
                                                if O0O0OO0OOO0000O00 ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{O0O0OO0OOO0000O00["message"]}')#line:379
        except Exception as O0OO0OO0O00OOOO0O :#line:380
            print (O0OO0OO0O00OOOO0O )#line:381
    def watched_ad (O0OOOO00000O0OOO0 ):#line:384
        try :#line:385
            O00O0O00O00OO000O =f'__{timi_new()}'#line:386
            OO0O000OO000O0OO0 ={'authorization':O0OOOO00000O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O00O00OO000O ),'signstring':O00O0O00O00OO000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            O00OOO0OOOO0000OO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O000OO000O0OO0 ).json ()#line:396
            if 'status'in O00OOO0OOOO0000OO :#line:398
                if O00OOO0OOOO0000OO ['status']==200 :#line:399
                    if 'offlineInfo'in O00OOO0OOOO0000OO ['data']:#line:400
                        OOOO0O0OO000OO00O =O00OOO0OOOO0000OO ['data']['offlineInfo']['off_minute']#line:401
                        OO0O0OOOOO00000O0 =float (O00OOO0OOOO0000OO ['data']['silver'])/1000000000000 #line:402
                        time .sleep (1 )#line:403
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0O000OO000O0OO0 ).json ()#line:404
                        time .sleep (2 )#line:405
                        OOOOOO0OO00OOO0OO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O000OO000O0OO0 ).json ()#line:406
                        if 'status'in OOOOOO0OO00OOO0OO :#line:408
                            if OOOOOO0OO00OOO0OO ['status']==200 :#line:409
                                O00OOO0OOOO00OOOO =float (OOOOOO0OO00OOO0OO ['data']['silver'])/1000000000000 #line:410
                                OO0OOOO0OO000OO00 =str (O00OOO0OOOO00OOOO -OO0O0OOOOO00000O0 )[:6 ]#line:411
                                print (f'【离线奖励】:翻倍离线{OOOO0O0OO000OO00O}分钟奖励种子数量:{OO0OOOO0OO000OO00}t粒')#line:412
        except Exception as O00O00O0O00OOOO00 :#line:413
            print (O00O00O0O00OOOO00 )#line:414
    def user_ad (O0OOOO0O0OOOOO00O ):#line:417
        try :#line:418
            O0OOO00O0000OOO0O =f'__{timi_new()}'#line:419
            OO00OOO0OOOO000OO ={'authorization':O0OOOO0O0OOOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0000OOO0O ),'signstring':O0OOO00O0000OOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:428
            O0O0OO00OOO000O00 =requests .request ('get',f'{host}/user/ad',headers =OO00OOO0OOOO000OO ).json ()#line:429
            if 'status'in O0O0OO00OOO000O00 :#line:431
                if O0O0OO00OOO000O00 ['status']==200 :#line:432
                    OO00OO00O0000OOOO =O0O0OO00OOO000O00 ['data']['max_time']#line:433
                    OOO000000000OO0O0 =O0O0OO00OOO000O00 ['data']['watch_time']#line:434
                    O0OOO0O0OOO0O00OO =O0O0OO00OOO000O00 ['data']['added_time']#line:435
                    print (f'【获取种子】:获取种子剩余{O0OOO0O0OOO0O00OO + OO00OO00O0000OOOO - OOO000000000OO0O0}次丨好友提供:{O0OOO0O0OOO0O00OO}次')#line:436
                    if O0OOO0O0OOO0O00OO +OO00OO00O0000OOOO -OOO000000000OO0O0 >0 :#line:437
                        time .sleep (random .randint (16 ,19 ))#line:438
                        O0OOOOO0O0O0OOO0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO00OOO0OOOO000OO ).json ()#line:439
                        if 'status'in O0OOOOO0O0O0OOO0O :#line:441
                            if O0OOOOO0O0O0OOO0O ['status']==200 :#line:442
                                O00OO0O0OO0OOOOO0 =O0OOOOO0O0O0OOO0O ['data']['silver']#line:443
                                print (f'【获取种子】:获得种子:{O00OO0O0OO0OOOOO0}')#line:444
                                return True #line:445
                            if O0OOOOO0O0O0OOO0O ['status']==500 :#line:446
                                OOO0OOO0O0OO00OO0 =O0OOOOO0O0O0OOO0O ['message']#line:447
                                print (f'【获取种子】:{OOO0OOO0O0OO00OO0}')#line:448
                                return False #line:449
        except Exception as OOO000OOO0OO0O000 :#line:450
            print (OOO000OOO0OO0O000 )#line:451
    def synthetic (O000000OO0OOO0OOO ):#line:454
        global id ,g #line:455
        try :#line:456
            OO0O0O00OO00O0O00 =O000000OO0OOO0OOO .level_new ()#line:457
            O000OO00O0OOOOOOO =random .randint (9 ,11 )#line:458
            O0O00OO0O00000OOO =f'_site=8&targetSite={O000OO00O0OOOOOOO}_{timi_new()}'#line:459
            OOO0O000OOO00O00O ={'accept':'application/json, text/plain, */*','authorization':O000000OO0OOO0OOO .token ,'timestamp':timi_new (),'sign':sign (O0O00OO0O00000OOO ),'signstring':O0O00OO0O00000OOO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:474
            OO0000O00O00OO000 ={"site":int (8 ),"targetSite":int (O000OO00O0OOOOOOO )}#line:475
            requests .request ('post',f'{host}/game/crops/move',headers =OOO0O000OOO00O00O ,json =OO0000O00O00OO000 )#line:476
            while True :#line:477
                O0000O00O000O0OO0 =f'__{timi_new()}'#line:478
                OOO0OOO0O0OOOO000 ={'authorization':O000000OO0OOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00O000O0OO0 ),'signstring':O0000O00O000O0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:487
                OO000OOO00OOO00OO =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OOO0O0OOOO000 ).json ()#line:488
                if 'status'in OO000OOO00OOO00OO :#line:490
                    if OO000OOO00OOO00OO ['status']==200 :#line:491
                        OO00OO00O0OOO0000 =OO000OOO00OOO00OO ['data']['cropList']#line:492
                        OOOOOOOO00O00O0O0 =OO000OOO00OOO00OO ['data']['gameCoreDataDBid']#line:493
                        OO00O00000O0OO000 =0 #line:494
                        for OOO00O0000000O000 in OO00OO00O0OOO0000 :#line:495
                            if not OOO00O0000000O000 :#line:496
                                O0O0OO00O0O00OOOO =f'_crop_id={OOOOOOOO00O00O0O0}&site={OO00O00000O0OO000}_{O000000OO0OOO0OOO.time}'#line:497
                                O0000O000OO00OOO0 ={'authorization':O000000OO0OOO0OOO .token ,'timestamp':O000000OO0OOO0OOO .time ,'sign':sign (O0O0OO00O0O00OOOO ),'signstring':O0O0OO00O0O00OOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:506
                                O0OOOO0OOOO0000O0 ={"site":OO00O00000O0OO000 ,"crop_id":OOOOOOOO00O00O0O0 }#line:507
                                O000OOO00000O0OO0 =requests .request ('post',f'{host}/game/crops/buy',headers =O0000O000OO00OOO0 ,data =O0OOOO0OOOO0000O0 ).json ()#line:508
                                time .sleep (random .randint (1 ,3 )/10 )#line:510
                                if 'status'in O000OOO00000O0OO0 :#line:511
                                    if O000OOO00000O0OO0 ['status']==200 :#line:512
                                        if O000OOO00000O0OO0 ['message']=='种子数量不足':#line:513
                                            OO0O0O00OO00O0O00 =O000000OO0OOO0OOO .level_new ()#line:514
                                            print (f'【种植合成】:{O000OOO00000O0OO0["message"]}')#line:515
                                            if not O000000OO0OOO0OOO .user_ad ():#line:516
                                                return False #line:517
                                    if O000OOO00000O0OO0 ['status']==500 :#line:518
                                        print (f'【种植合成】:{O000OOO00000O0OO0["message"]}')#line:519
                                        return False #line:520
                            OO00O00000O0OO000 +=1 #line:521
                        O0O0O0OO00O00OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OOO0O0OOOO000 ).json ()#line:522
                        OOO00OO00O00O0O00 =O0O0O0OO00O00OOO0 ['data']['cropList']#line:523
                        O0000O000OO0O0OO0 =False #line:524
                        for OOO00O0000000O000 in range (12 ):#line:525
                            id =OOO00OO00O00O0O00 [OOO00O0000000O000 ]['level']#line:526
                            if float (OO0O0O00OO00O0O00 )-float (id )>9 :#line:527
                                OO00OOOOOOO00OO0O =f'_site={OOO00O0000000O000}_{timi_new()}'#line:528
                                OOOOO0O00OOOOO0O0 ={'accept':'application/json, text/plain, */*','authorization':O000000OO0OOO0OOO .token ,'timestamp':timi_new (),'sign':sign (OO00OOOOOOO00OO0O ),'signstring':OO00OOOOOOO00OO0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:538
                                OO0O0000O0O0O000O ={"site":OOO00O0000000O000 }#line:539
                                O0O0O0000O00O0000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOOO0O00OOOOO0O0 ,data =OO0O0000O0O0O000O ).json ()#line:541
                                if 'status'in O0O0O0000O00O0000 :#line:542
                                    if O0O0O0000O00O0000 ['status']==200 :#line:543
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:544
                            if id !=0 :#line:545
                                for OO000O0O0O0O0O0O0 in range (11 ):#line:546
                                    OOO000OO0O0000OOO =OO000O0O0O0O0O0O0 +1 #line:547
                                    g =OOO00OO00O00O0O00 [OOO000OO0O0000OOO ]['level']#line:548
                                    if id ==g :#line:549
                                        O0000OOO000O0O00O =OO000O0O0O0O0O0O0 +2 #line:550
                                        if O0000OOO000O0O00O !=OOO00O0000000O000 +1 :#line:551
                                            OOOO0O00O0O0OO000 =OOO00O0000000O000 +1 #line:552
                                            time .sleep (random .randint (1 ,3 )/10 )#line:554
                                            O0O00OO0O00000OOO =f'_site={OOOO0O00O0O0OO000 - 1}&targetSite={O0000OOO000O0O00O - 1}_{timi_new()}'#line:555
                                            OOO0O000OOO00O00O ={'accept':'application/json, text/plain, */*','authorization':O000000OO0OOO0OOO .token ,'timestamp':timi_new (),'sign':sign (O0O00OO0O00000OOO ),'signstring':O0O00OO0O00000OOO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:570
                                            OOO000OOO000000O0 ={"site":int (OOOO0O00O0O0OO000 -1 ),"targetSite":int (O0000OOO000O0O00O -1 )}#line:571
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOO0O000OOO00O00O ,json =OOO000OOO000000O0 )#line:572
                                            print (f'【种植合成】:位置{OOOO0O00O0O0OO000}和位置{O0000OOO000O0O00O}合出{id}级农作物')#line:573
                                            O0000O000OO0O0OO0 =True #line:574
                                    if O0000O000OO0O0OO0 :#line:575
                                        break #line:576
                                if O0000O000OO0O0OO0 :#line:577
                                    break #line:578
        except :#line:579
            O000000OO0OOO0OOO .synthetic ()#line:580
    def level_new (OOOOOOO00OOO00O0O ):#line:583
        try :#line:584
            O000O000OOOOOO0O0 =f'__{timi_new()}'#line:585
            O0O0OOOO000O0O00O ={'authorization':OOOOOOO00OOO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000OOOOOO0O0 ),'signstring':O000O000OOOOOO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:594
            O0O0OOO0O00O0OO00 =requests .request ('get',f'{host}/user',headers =O0O0OOOO000O0O00O ).json ()#line:595
            if 'status'in O0O0OOO0O00O0OO00 :#line:596
                if O0O0OOO0O00O0OO00 ['status']==200 :#line:597
                    return float (O0O0OOO0O00O0OO00 ['data']['level'])#line:598
        except Exception as O0O00OOOOO00O0O0O :#line:599
            print (O0O00OOOOO00O0O0O )#line:600
    def propsraffle (OOOOOO0O000OOOOO0 ):#line:603
        try :#line:604
            while True :#line:605
                O000O0OO0O0O00000 =f'__{timi_new()}'#line:606
                O0000OOO0000000O0 ={'authorization':OOOOOO0O000OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO0O0O00000 ),'signstring':O000O0OO0O0O00000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:615
                O00OOOO0OO0OOOOOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0000OOO0000000O0 ).json ()#line:616
                if 'status'in O00OOOO0OO0OOOOOO :#line:618
                    if O00OOOO0OO0OOOOOO ['status']==200 :#line:619
                        O0O0OOO000O000000 =O00OOOO0OO0OOOOOO ['data']['rows']#line:620
                        OOOO0O0O00OOO0OOO =O00OOOO0OO0OOOOOO ['data']['vstate']#line:621
                        if O0O0OOO000O000000 ==5 or O0O0OOO000O000000 ==6 or O0O0OOO000O000000 ==7 :#line:622
                            OO00000O000O00000 =O00OOOO0OO0OOOOOO ['data']['silver']#line:623
                            print (f'【转盘抽奖】:获得种子:{OO00000O000O00000}')#line:624
                        if O0O0OOO000O000000 ==1 or O0O0OOO000O000000 ==2 or O0O0OOO000O000000 ==3 :#line:625
                            OO0O000O00O0O0O0O =O00OOOO0OO0OOOOOO ['data']['clover']#line:626
                            print (f'【转盘抽奖】:获得三叶草:{OO0O000O00O0O0O0O}')#line:627
                        if O0O0OOO000O000000 ==4 or O0O0OOO000O000000 ==8 :#line:628
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:629
                        if O0O0OOO000O000000 =='抽奖次数已用完':#line:633
                            break #line:666
                time .sleep (random .randint (8 ,15 )/10 )#line:667
        except Exception as O0OOOO00OOO00OO00 :#line:668
            print (O0OOOO00OOO00OO00 )#line:669
    def friends_invitation (O0OOO00O0OOO000O0 ):#line:672
        try :#line:673
            O00O0OOO000OOO000 =f'__{timi_new()}'#line:674
            O0OOO000O0O0O0O0O ={'authorization':O0OOO00O0OOO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO000OOO000 ),'signstring':O00O0OOO000OOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:683
            O0OO0OO0O00000OO0 =requests .request ('get',f'{host}/friends',headers =O0OOO000O0O0O0O0O ).json ()#line:684
            if 'status'in O0OO0OO0O00000OO0 :#line:685
                if O0OO0OO0O00000OO0 ['status']==200 :#line:686
                    OOO000O00O0O0O0O0 =O0OO0OO0O00000OO0 ['data']['myInviteter']#line:687
                    if OOO000O00O0O0O0O0 :#line:688
                        O00O0OOO000OO0000 =OOO000O00O0O0O0O0 ['user']['nickname']#line:689
                        O00OO0O0O0O0OO000 =O0OOO00O0OOO000O0 .certification ()#line:690
                        print (f'【查邀请人】:我的邀请人:{O00O0OOO000OO0000}丨实名:{O00OO0O0O0O0OO000}')#line:691
                    else :#line:692
                        if O0OOO00O0OOO000O0 .innerId !='0':#line:693
                            O0OOO00O0OOO000O0 .invitation ()#line:694
        except Exception as O000OOO000O00O00O :#line:695
            print (O000OOO000O00O00O )#line:696
    def add_clover (OOO00OO0O0O0O000O ):#line:699
        global golden_seed #line:700
        try :#line:701
            OO00OOO00OO00OO00 =f'__{timi_new()}'#line:702
            O0OO0O000OO0O0O0O ={'authorization':OOO00OO0O0O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO00OO00OO00 ),'signstring':OO00OOO00OO00OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:711
            O0OO0OO00OOOOOO0O =requests .request ('get',f'{host}/assets/clovers',headers =O0OO0O000OO0O0O0O ).json ()#line:712
            if 'status'in O0OO0OO00OOOOOO0O :#line:714
                if O0OO0OO00OOOOOO0O ['status']==200 :#line:715
                    O0O00OOOOOO00OOOO =O0OO0OO00OOOOOO0O ['data']['clover']#line:716
                    OOOO0OO0OO0O0O00O =O0OO0OO00OOOOOO0O ['data']['used_clover']#line:717
                    O00O00OOOO0O0OOO0 =float (O0O00OOOOOO00OOOO )-float (OOOO0OO0OO0O0O00O )#line:718
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OOOO0OO0OO0O0O00O}')#line:719
                    if OOO00OO0O0O0O000O .certification ()!='未实名':#line:720
                        if O00O00OOOO0O0OOO0 >1 :#line:721
                            OO00OOO00OO00OO00 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00O00OOOO0O0OOO0)}_{timi_new()}'#line:722
                            O0OOO000OOOO00OOO ={'authorization':OOO00OO0O0O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO00OO00OO00 ),'signstring':OO00OOO00OO00OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:731
                            OO000OO000O0OO000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00O00OOOO0O0OOO0 )}#line:732
                            OO0OOO000O0O0O000 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OOO000OOOO00OOO ,data =OO000OO000O0OO000 ).json ()#line:733
                            if 'status'in OO0OOO000O0O0O000 :#line:735
                                if OO0OOO000O0O0O000 ['status']==200 :#line:736
                                    print (f'【参与抽奖】:添加三叶草:{OO0OOO000O0O0O000["data"]}丨数量:{O00O00OOOO0O0OOO0}')#line:737
                                if OO0OOO000O0O0O000 ['status']==500 :#line:738
                                    print (f'【参与抽奖】:添加三叶草:{OO0OOO000O0O0O000["message"]}')#line:739
            O00O0OOO0O00OOO0O =requests .request ('get',f'{host}/lottery',headers =O0OO0O000OO0O0O0O ).json ()#line:740
            OOOO0000OOO0000OO =OOO00OO0O0O0O000O .winning_rewards ()#line:742
            if 'status'in O00O0OOO0O00OOO0O :#line:743
                if O00O0OOO0O00OOO0O ['status']==200 :#line:744
                    O0O0OOOOO0O0O0O0O =O00O0OOO0O00OOO0O ['data'][0 ]['day_get_gold_quantity']#line:745
                    golden_seed +=float (O0O0OOOOO0O0O0O0O )#line:746
                    print (f'【参与抽奖】:预计每天中{str(O0O0OOOOO0O0O0O0O)[:6]}颗金种子丨好友收益:{str(OOOO0000OOO0000OO)[:6]}')#line:747
        except Exception as O0O0O0O00O0O0O000 :#line:748
            print (O0O0O0O00O0O0O000 )#line:749
    def energy (O0O0OOOOOOOOOOOOO ):#line:753
        try :#line:754
            while True :#line:755
                OOO0O00000O0OO00O =f'__{timi_new()}'#line:756
                O00O000O0OO0O0000 ={'authorization':O0O0OOOOOOOOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00000O0OO00O ),'signstring':OOO0O00000O0OO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:765
                O00OO00O0OO000OO0 =requests .request ('get',f'{host}/energy/general',headers =O00O000O0OO0O0000 ).json ()#line:766
                if 'status'in O00OO00O0OO000OO0 :#line:768
                    if O00OO00O0OO000OO0 ['status']==200 :#line:769
                        OOOOOO0O0OOOO0O00 =O00OO00O0OO000OO0 ['data']['ordinary_water']#line:770
                        O0O0OO000OOOOOOOO =O00OO00O0OO000OO0 ['data']['ordinary_fertilizer']#line:771
                        print (f'【我的营养】:肥料:{str(O0O0OO000OOOOOOOO).split(".")[0]}丨水滴:{str(OOOOOO0O0OOOO0O00).split(".")[0]}')#line:773
                        if float (O0O0OO000OOOOOOOO )<96 :#line:774
                            time .sleep (random .randint (160 ,180 )/10 )#line:775
                            O0000000O0O00OOO0 =99 -float (O0O0OO000OOOOOOOO )#line:776
                            O00OOOOO00O0OOOOO ={"fertilizer":str (O0000000O0O00OOO0 ).split ('.')[0 ]}#line:777
                            O00000O00OO0O0O0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00O000O0OO0O0000 ).json ()#line:778
                            if 'status'in O00000O00OO0O0O0O :#line:780
                                if O00000O00OO0O0O0O ['status']==200 :#line:781
                                    print (f'【购买肥料】:看广告获取肥料:{O00000O00OO0O0O0O["message"]}')#line:782
                        if float (OOOOOO0O0OOOO0O00 )<880 :#line:783
                            time .sleep (random .randint (160 ,180 )/10 )#line:784
                            OO0O00OO0O00O0OO0 =999 -float (OOOOOO0O0OOOO0O00 )#line:785
                            OOO00OOOO0OOOOOO0 ={"water":str (OO0O00OO0O00O0OO0 ).split ('.')[0 ]}#line:786
                            O00O00OOOO00OOO0O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00O000O0OO0O0000 ).json ()#line:787
                            if 'status'in O00O00OOOO00OOO0O :#line:789
                                if O00O00OOOO00OOO0O ['status']==200 :#line:790
                                    print (f'【购买水滴】:看广告获取水滴:{O00O00OOOO00OOO0O["message"]}')#line:791
                        if float (O0O0OO000OOOOOOOO )>96 and float (OOOOOO0O0OOOO0O00 )>880 :#line:792
                            break #line:793
        except Exception as OO0OOO00O0O00O000 :#line:795
            print (OO0OOO00O0O00O000 )#line:796
def bundled_def ():#line:798
    O0O0OOOO0O00OOO0O =['5570536','7750212','7911652','7911680','7805624']#line:799
    return O0O0OOOO0O00OOO0O [random .randint (0 ,len (O0O0OOOO0O00OOO0O )-1 )]#line:800
def version_of_the_validation ():#line:804
    return str ((77 -56 )/10 )#line:805
def gitee_validation ():#line:808
    try :#line:809
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:810
    except :#line:811
        sys .exit (0 )#line:812
def update_the_validation ():#line:816
    try :#line:817
        O0000O0OO0O0OO0OO =gitee_validation ()#line:818
        if version_of_the_validation ()<O0000O0OO0O0OO0OO ['CityEarth']['edition']:#line:819
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0000O0OO0O0OO0OO["CityEarth"]["edition"]}   ❌')#line:820
            print (f'更新内容=>>{O0000O0OO0O0OO0OO["CityEarth"]["content"]}   👍')#line:821
        else :#line:822
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0000O0OO0O0OO0OO["CityEarth"]["edition"]}   ✅')#line:823
            print (f'更新内容=>> {O0000O0OO0O0OO0OO["CityEarth"]["content"]}   👍')#line:824
    except Exception as OO000O000OO000OO0 :#line:825
        print (OO000O000OO000OO0 )#line:826
def os_qinglong ():#line:829
    if application in os .environ :#line:830
        O0OOO000OO0OO00OO =os .environ [application ].split ('\n')#line:831
        if len (O0OOO000OO0OO00OO )>0 :#line:832
            return O0OOO000OO0OO00OO #line:833
        else :#line:834
            print (f"{application}变量未启用")#line:835
            print ('脚本退出')#line:836
            sys .exit (1 )#line:837
    else :#line:838
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:840
        return os_built ()#line:841
def os_built ():#line:844
    if token :#line:845
        OO00O0O00000OO0O0 =token .split ('\n')#line:846
        if len (OO00O0O00000OO0O0 )>0 :#line:847
            return OO00O0O00000OO0O0 #line:848
    else :#line:849
        print (f"内置变量为空")#line:850
        print ('脚本结束')#line:851
        sys .exit (0 )#line:852
if __name__ =='__main__':#line:855
    start ()#line:856
