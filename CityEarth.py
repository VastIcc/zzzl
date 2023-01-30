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
except Exception as e:
    t = re.findall("d '(.*?)'", str(e))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: 22 */3 * * *
@ new Env('生城世朝')
@ 项目地址  微信打开  http://share.sc19319.com/scsc/1937553
@ 抓取  http://scsc.sc19319.com 的authorization值
@ 青龙变量  青龙配置文件 export ce_token="authorization&赠送金种子数量大于&赠送金种子id" 
@ 如果你有20金种子填10就会赠 填21就不会赠送  不赠送全填 999999     多号换行
@ 变量示范    export ce_token="557b8069-1234-4ae7-9e29-b7871f91541b&999999&999999"  用&符号分开数据
@ 版本  1.1
"""

application = 'ce_token'  # 变量名
token = ''
time_xx = random.randint(8, 12)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://scsc.sc19319.com'#line:2
golden_seed =0 #line:3
def start ():#line:4
    try :#line:5
        update_the_validation ()#line:6
        O0OOO0OOOO0000000 =os_qinglong ()#line:7
        print (f"==========共找到{len(O0OOO0OOOO0000000)}个账号==========")#line:8
        for OO0OO00OO0O00O0O0 in O0OOO0OOOO0000000 :#line:9
            print (f"------------正在执行第{O0OOO0OOOO0000000.index(OO0OO00OO0O00O0O0) + 1}个账号------------")#line:10
            OO000OOOO0OOOOOOO =CityEarth (OO0OO00OO0O00O0O0 )#line:11
            def O0O00O0OOO0O000OO ():#line:13
                if OO000OOOO0OOOOOOO .base_info ():#line:15
                    OO000OOOO0OOOOOOO .game_map ()#line:19
                    OO000OOOO0OOOOOOO .friends_invitation ()#line:21
                    OO000OOOO0OOOOOOO .add_clover ()#line:23
                    OO000OOOO0OOOOOOO .energy ()#line:25
                    OO000OOOO0OOOOOOO .propsraffle ()#line:27
                    OO000OOOO0OOOOOOO .synthetic ()#line:29
                    OO000OOOO0OOOOOOO .crops_illustrated ()#line:31
                    OO000OOOO0OOOOOOO .give_gold ()#line:33
                else :#line:34
                    print ('token失效')#line:35
            O0OO0O000O0O0OOOO =threading .Thread (target =O0O00O0OOO0O000OO )#line:37
            O0OO0O000O0O0OOOO .start ()#line:38
            time .sleep (time_xx )#line:39
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:41
        time .sleep (3 )#line:42
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:43
    except Exception as O0O0OOOOO0O00O0O0 :#line:44
        print (O0O0OOOOO0O00O0O0 )#line:45
def sign (O00O000OO0OO0OOOO ):#line:48
    OOO0OOOOOOO00OOO0 =hashlib .md5 (O00O000OO0OO0OOOO .encode ()).hexdigest ()#line:49
    OO00000O000OOO0OO ="scsc%^&*"+OOO0OOOOOOO00OOO0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:50
    OO0O0O00OOO0O0O0O =hashlib .md5 (OO00000O000OOO0OO .encode ()).hexdigest ()#line:51
    return OO0O0O00OOO0O0O0O #line:52
def timi_new ():#line:55
    return str (int (time .time ()*1000 ))#line:56
class CityEarth :#line:58
    def __init__ (O00O000O0OOOO000O ,O000O0O0O0O0O0O00 ):#line:60
        try :#line:61
            O00O000O0OOOO000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:62
            O00O000O0OOOO000O .token =O000O0O0O0O0O0O00 .split ('&')[0 ]#line:63
            O00O000O0OOOO000O .innerId =O000O0O0O0O0O0O00 .split ('&')[1 ]#line:64
            O00O000O0OOOO000O .doneeNo =O000O0O0O0O0O0O00 .split ('&')[2 ]#line:65
        except :#line:66
            print ('变量格式错误')#line:67
    def base_info (O0OO0OOOO0000OOO0 ):#line:70
        try :#line:71
            OO00OOO0OOOO0O000 =f'__{timi_new()}'#line:72
            OO0OO00OOOO00O000 ={'authorization':O0OO0OOOO0000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO0OOOO0O000 ),'signstring':OO00OOO0OOOO0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:81
            O00O000000O0O0OO0 =requests .request ('get',f'{host}/user',headers =OO0OO00OOOO00O000 ).json ()#line:82
            if 'status'in O00O000000O0O0OO0 :#line:84
                if O00O000000O0O0OO0 ['status']==200 :#line:85
                    OO0O00OOOO0000OOO =O00O000000O0O0OO0 ['data']['nickname']#line:86
                    OO0O0000O00O0OO00 =O00O000000O0O0OO0 ['data']['inner_id']#line:87
                    OO00000O0000OO000 =O00O000000O0O0OO0 ['data']['assets']['gold']#line:88
                    O00OOOO0OO0000O0O =O00O000000O0O0OO0 ['data']['level']#line:89
                    print (f'【账号信息】:昵称:{OO0O00OOOO0000OOO[:5]}丨ID:{OO0O0000O00O0OO00}丨等级:{O00OOOO0OO0000O0O}丨种子:{str(OO00000O0000OO000).split(".")[0]}')#line:90
                if O00O000000O0O0OO0 ['status']==401 :#line:91
                    return False #line:92
                if O00O000000O0O0OO0 ['status']==500 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as OO00OO0O000O0O000 :#line:96
            print (OO00OO0O000O0O000 )#line:97
    def game_map (OOO0O00O0OO0000O0 ):#line:100
        try :#line:101
            O000OOOO00OO00000 =f'__{timi_new()}'#line:102
            OOO00O00OOOO0OO00 ={'authorization':OOO0O00O0OO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOO00OO00000 ),'signstring':O000OOOO00OO00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:111
            OOO000O0000O0O00O =requests .request ('get',f'{host}/game/map',headers =OOO00O00OOOO0OO00 ).json ()#line:112
            if 'status'in OOO000O0000O0O00O :#line:114
                if OOO000O0000O0O00O ['status']==200 :#line:115
                    for OOOOO00OO0OO00O0O in OOO000O0000O0O00O ['data']['list'][0 ]['crops']:#line:116
                        O0O0O000O0000OOO0 =OOOOO00OO0OO00O0O ['level']#line:118
                        if O0O0O000O0000OOO0 ==41 :#line:119
                            OOO0OO0OOO00000O0 =OOOOO00OO0OO00O0O ['crop_name']#line:120
                            OOO000OOO0OO00O0O =OOOOO00OO0OO00O0O ['count']#line:121
                            if OOO000OOO0OO00O0O >0 :#line:122
                                print (f'【农业资产】:{OOO0OO0OOO00000O0}丨数量:{OOO000OOO0OO00O0O}')#line:123
        except Exception as O0000O0OO00OO000O :#line:124
            print (O0000O0OO00OO000O )#line:125
    def give_gold (OO000O000000000OO ):#line:129
        try :#line:130
            OOOO0O0O0OO0O0OOO =f'__{timi_new()}'#line:131
            OOO0000O0O0OO0O0O ={'authorization':OO000O000000000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O0OO0O0OOO ),'signstring':OOOO0O0O0OO0O0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:140
            OOO0O00OOOO000000 =requests .request ('get',f'{host}/user',headers =OOO0000O0O0OO0O0O ).json ()#line:141
            if 'status'in OOO0O00OOOO000000 :#line:142
                if OOO0O00OOOO000000 ['status']==200 :#line:143
                    if float (OO000O000000000OO .doneeNo )!=0 :#line:144
                        OO00OO0OOO0OO00OO =OOO0O00OOOO000000 ['data']['assets']['gold']#line:145
                        if float (OO00OO0OOO0OO00OO )>float (OO000O000000000OO .innerId ):#line:146
                            O000O00OO000000OO =int (float (OO00OO0OOO0OO00OO )/1.1 )#line:147
                            OOOO0O0O0OO0O0OOO =f'_doneeNo={OO000O000000000OO.doneeNo}&quantity={O000O00OO000000OO}_{timi_new()}'#line:148
                            OOO0000O0O0OO0O0O ={'authorization':OO000O000000000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O0OO0O0OOO ),'signstring':OOOO0O0O0OO0O0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:157
                            O00O0000OOOOOOOO0 ={"quantity":O000O00OO000000OO ,"doneeNo":OO000O000000000OO .doneeNo }#line:161
                            O0OOOOOOOO0OOO0OO =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0000O0O0OO0O0O ,data =O00O0000OOOOOOOO0 ).json ()#line:162
                            if 'status'in O0OOOOOOOO0OOO0OO :#line:164
                                if O0OOOOOOOO0OOO0OO ['status']==200 :#line:165
                                    if O0OOOOOOOO0OOO0OO ['data']:#line:166
                                        print (f'【赠送种子】:赠送{O000O00OO000000OO}种子给{OO000O000000000OO.doneeNo}成功')#line:167
                    else :#line:168
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:169
        except Exception as OO0OOOO0OO0OO0O0O :#line:170
            print (OO0OOOO0OO0OO0O0O )#line:171
    def winning_rewards (OOO0OOOOO00OOO0OO ):#line:175
        try :#line:176
            OOO00000O00000O00 =f'__{timi_new()}'#line:177
            OO0000O000000OOO0 ={'authorization':OOO0OOOOO00OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00000O00000O00 ),'signstring':OOO00000O00000O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
            O0OO00OO000O0O0OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO0000O000000OOO0 ).json ()#line:187
            if 'status'in O0OO00OO000O0O0OO :#line:189
                if O0OO00OO000O0O0OO ['status']==200 :#line:190
                    if O0OO00OO000O0O0OO ['data']['amount']:#line:191
                        OOOO00O0OO0OOO000 =O0OO00OO000O0O0OO ['data']['amount']['gold']#line:192
                        return OOOO00O0OO0OOO000 #line:193
                    else :#line:194
                        return 0 #line:195
        except Exception as OO0O0OO0O00OOO0O0 :#line:196
            print (OO0O0OO0O00OOO0O0 )#line:197
    def certification (OO00000OO0O00O000 ):#line:201
        try :#line:202
            OO0O0OO0000OO0O0O =f'__{timi_new()}'#line:203
            O0O0O000OO0OOO0O0 ={'authorization':OO00000OO0O00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO0000OO0O0O ),'signstring':OO0O0OO0000OO0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:212
            OOOOO000OO0OOOOOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0O0O000OO0OOO0O0 ).json ()#line:213
            if 'status'in OOOOO000OO0OOOOOO :#line:215
                if OOOOO000OO0OOOOOO ['status']==200 :#line:216
                    if OOOOO000OO0OOOOOO ['data']['result']:#line:217
                        O0000OOO00O0O0O00 =OOOOO000OO0OOOOOO ['data']['nick_name']#line:218
                        return O0000OOO00O0O0O00 #line:219
                    else :#line:220
                        return '未实名'#line:221
        except Exception as O0O00O0O0O0O00000 :#line:222
            print (O0O00O0O0O0O00000 )#line:223
    def crops_illustrated (O0O00O000O0OO00OO ):#line:227
        try :#line:228
            OO0OOO0O00O000OO0 =f'__{timi_new()}'#line:229
            O0O0O0OOO0OO00000 ={'authorization':O0O00O000O0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O00O000OO0 ),'signstring':OO0OOO0O00O000OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:238
            O00O00O0O00O00O0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O0O0OOO0OO00000 ).json ()#line:239
            if 'status'in O00O00O0O00O00O0O :#line:241
                if O00O00O0O00O00O0O ['status']==200 :#line:242
                    OOO0O00OO00O0OOO0 =O00O00O0O00O00O0O ['data'][0 ]['crops']#line:243
                    for OOO0O00OO00O00O00 in OOO0O00OO00O0OOO0 :#line:244
                        if OOO0O00OO00O00O00 ['ill_clover_award']:#line:245
                            if float (OOO0O00OO00O00O00 ['ill_clover_award'])>1 :#line:246
                                if OOO0O00OO00O00O00 ['is_finish']:#line:247
                                    if not OOO0O00OO00O00O00 ['is_getit']:#line:248
                                        OO0OOO0O00O000OO0 =f'_award_level={OOO0O00OO00O00O00["level"]}_{timi_new()}'#line:249
                                        O0O0O0OOO0OO00000 ={'authorization':O0O00O000O0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O00O000OO0 ),'signstring':OO0OOO0O00O000OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:258
                                        OOOOOOOOOOO0O0OOO ={"award_level":OOO0O00OO00O00O00 ['level']}#line:259
                                        O0000OO0O0O000000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O0O0OOO0OO00000 ,json =OOOOOOOOOOO0O0OOO ).json ()#line:261
                                        if 'status'in O0000OO0O0O000000 :#line:262
                                            if O0000OO0O0O000000 ['status']==200 :#line:263
                                                O0OOOOO0OOOOO0OO0 =O0000OO0O0O000000 ['data']['ill_clover_award']#line:264
                                                print (f'【图鉴奖励】:领取{OOO0O00OO00O00O00["crop_name"]}成就丨奖励{O0OOOOO0OOOOO0OO0}叶子成功')#line:266
                                            if O0000OO0O0O000000 ['status']==500 :#line:267
                                                print (f'【图鉴奖励】:{O0000OO0O0O000000["message"]}')#line:268
        except Exception as O000OO00O0OOO0000 :#line:269
            print (O000OO00O0OOO0000 )#line:270
    def watched_ad (OO0O0O000OO00O00O ):#line:274
        try :#line:275
            OO0000OO0OO0OOOOO =f'__{timi_new()}'#line:276
            OOOO0O00OO0O0OO00 ={'authorization':OO0O0O000OO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OO0OO0OOOOO ),'signstring':OO0000OO0OO0OOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:285
            O0O0O000OOOO0O0OO =requests .request ('post',f'{host}/game/watched-ad',headers =OOOO0O00OO0O0OO00 ).json ()#line:286
            print (O0O0O000OOOO0O0OO )#line:287
        except Exception as OO00000OOO000O00O :#line:288
            print (OO00000OOO000O00O )#line:289
    def user_ad (OO0O000000000OOOO ):#line:293
        try :#line:294
            OO000OO000O0O0OOO =f'__{timi_new()}'#line:295
            O000O00O00O00OOOO ={'authorization':OO0O000000000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO000O0O0OOO ),'signstring':OO000OO000O0O0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:304
            O0OOO00000OO0O0OO =requests .request ('get',f'{host}/user/ad',headers =O000O00O00O00OOOO ).json ()#line:305
            if 'status'in O0OOO00000OO0O0OO :#line:307
                if O0OOO00000OO0O0OO ['status']==200 :#line:308
                    OOOOO0OOOO0OO00O0 =O0OOO00000OO0O0OO ['data']['max_time']#line:309
                    O00OO0000OO0O0OOO =O0OOO00000OO0O0OO ['data']['watch_time']#line:310
                    O00OOO00OOOOOO0O0 =O0OOO00000OO0O0OO ['data']['added_time']#line:311
                    print (f'【获取种子】:获取种子剩余{O00OOO00OOOOOO0O0 + OOOOO0OOOO0OO00O0 - O00OO0000OO0O0OOO}次丨好友提供:{O00OOO00OOOOOO0O0}次')#line:312
                    if O00OOO00OOOOOO0O0 +OOOOO0OOOO0OO00O0 -O00OO0000OO0O0OOO >0 :#line:313
                        time .sleep (random .randint (16 ,19 ))#line:314
                        O0O00OOO0000O0OO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O000O00O00O00OOOO ).json ()#line:315
                        if 'status'in O0O00OOO0000O0OO0 :#line:317
                            if O0O00OOO0000O0OO0 ['status']==200 :#line:318
                                OO000O00OOO0OOO0O =O0O00OOO0000O0OO0 ['data']['silver']#line:319
                                print (f'【获取种子】:获得种子:{OO000O00OOO0OOO0O}')#line:320
                                return True #line:321
                            if O0O00OOO0000O0OO0 ['status']==500 :#line:322
                                O00O0OOO0O0000OOO =O0O00OOO0000O0OO0 ['message']#line:323
                                print (f'【获取种子】:{O00O0OOO0O0000OOO}')#line:324
                                return False #line:325
        except Exception as OOOOO0000OOO00OO0 :#line:326
            print (OOOOO0000OOO00OO0 )#line:327
    def synthetic (OO00OOO000OO00O00 ):#line:331
        global id ,g #line:332
        try :#line:333
            OOOOO0000O000O000 =OO00OOO000OO00O00 .level_new ()#line:334
            while True :#line:335
                OO0OO000OOOOO0O00 =f'__{timi_new()}'#line:336
                OO00OOO00O0OOO0OO ={'authorization':OO00OOO000OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OOOOO0O00 ),'signstring':OO0OO000OOOOO0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:345
                O00OOO000O0OO0O00 =requests .request ('get',f'{host}/game/getAllData',headers =OO00OOO00O0OOO0OO ).json ()#line:346
                if 'status'in O00OOO000O0OO0O00 :#line:348
                    if O00OOO000O0OO0O00 ['status']==200 :#line:349
                        O00000OO0O0OO0000 =O00OOO000O0OO0O00 ['data']['cropList']#line:350
                        O0000O0O00OO000O0 =O00OOO000O0OO0O00 ['data']['gameCoreDataDBid']#line:351
                        OOO00O0OO000OOOOO =0 #line:352
                        for O0OOO0O00OO0OO0O0 in O00000OO0O0OO0000 :#line:353
                            if not O0OOO0O00OO0OO0O0 :#line:354
                                O00OO0000OOO0O0OO =f'_crop_id={O0000O0O00OO000O0}&site={OOO00O0OO000OOOOO}_{OO00OOO000OO00O00.time}'#line:355
                                O0OO00O0OO0OO00O0 ={'authorization':OO00OOO000OO00O00 .token ,'timestamp':OO00OOO000OO00O00 .time ,'sign':sign (O00OO0000OOO0O0OO ),'signstring':O00OO0000OOO0O0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:364
                                O0OO0O0O00OOO0OOO ={"site":OOO00O0OO000OOOOO ,"crop_id":O0000O0O00OO000O0 }#line:365
                                O0O00O0OOOOO0OO0O =requests .request ('post',f'{host}/game/crops/buy',headers =O0OO00O0OO0OO00O0 ,data =O0OO0O0O00OOO0OOO ).json ()#line:366
                                time .sleep (random .randint (1 ,3 )/10 )#line:368
                                if 'status'in O0O00O0OOOOO0OO0O :#line:369
                                    if O0O00O0OOOOO0OO0O ['status']==200 :#line:370
                                        if O0O00O0OOOOO0OO0O ['message']=='种子数量不足':#line:371
                                            OOOOO0000O000O000 =OO00OOO000OO00O00 .level_new ()#line:372
                                            print (f'【种植合成】:{O0O00O0OOOOO0OO0O["message"]}')#line:373
                                            if not OO00OOO000OO00O00 .user_ad ():#line:374
                                                return False #line:375
                                        print (f'【种植合成】:种植农作物,位置{OOO00O0OO000OOOOO}')#line:376
                                    if O0O00O0OOOOO0OO0O ['status']==500 :#line:377
                                        print (f'【种植合成】:{O0O00O0OOOOO0OO0O["message"]}')#line:378
                                        return False #line:379
                            OOO00O0OO000OOOOO +=1 #line:380
                        OO0OOO0OOO0OO00OO =requests .request ('get',f'{host}/game/getAllData',headers =OO00OOO00O0OOO0OO ).json ()#line:381
                        O000O0O0OOO0OOOO0 =OO0OOO0OOO0OO00OO ['data']['cropList']#line:382
                        O00O0OOO0OOOO0OO0 =False #line:383
                        for O0OOO0O00OO0OO0O0 in range (12 ):#line:384
                            id =O000O0O0OOO0OOOO0 [O0OOO0O00OO0OO0O0 ]['level']#line:385
                            if float (OOOOO0000O000O000 )-float (id )>9 :#line:386
                                O000O00O000O00O0O =f'_site={O0OOO0O00OO0OO0O0}_{timi_new()}'#line:387
                                O0O0OOOOOOOO0OO0O ={'accept':'application/json, text/plain, */*','authorization':OO00OOO000OO00O00 .token ,'timestamp':timi_new (),'sign':sign (O000O00O000O00O0O ),'signstring':O000O00O000O00O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:397
                                O000OOOO0O0OO0O00 ={"site":O0OOO0O00OO0OO0O0 }#line:398
                                O00OO0OO0O000OOOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O0OOOOOOOO0OO0O ,data =O000OOOO0O0OO0O00 ).json ()#line:400
                                if 'status'in O00OO0OO0O000OOOO :#line:401
                                    if O00OO0OO0O000OOOO ['status']==200 :#line:402
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:403
                            if id !=0 :#line:404
                                for O0000000OOOO0OOOO in range (11 ):#line:405
                                    OO0O0O0O0O00O0000 =O0000000OOOO0OOOO +1 #line:406
                                    g =O000O0O0OOO0OOOO0 [OO0O0O0O0O00O0000 ]['level']#line:407
                                    if id ==g :#line:408
                                        O0OOO000O0O00OOOO =O0000000OOOO0OOOO +2 #line:409
                                        if O0OOO000O0O00OOOO ==O0OOO0O00OO0OO0O0 +1 :#line:410
                                            pass #line:411
                                        else :#line:412
                                            OOO000O0OOO00O000 =O0OOO0O00OO0OO0O0 +1 #line:413
                                            time .sleep (random .randint (1 ,3 )/10 )#line:415
                                            OOO0O00O0O00OOO00 =f'_site={OOO000O0OOO00O000 - 1}&targetSite={O0OOO000O0O00OOOO - 1}_{timi_new()}'#line:416
                                            O000OO0O000OOO0O0 ={'accept':'application/json, text/plain, */*','authorization':OO00OOO000OO00O00 .token ,'timestamp':timi_new (),'sign':sign (OOO0O00O0O00OOO00 ),'signstring':OOO0O00O0O00OOO00 ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:431
                                            OO00O0O000OO00OO0 ={"site":int (OOO000O0OOO00O000 -1 ),"targetSite":int (O0OOO000O0O00OOOO -1 )}#line:432
                                            O000OO00OO00O0O00 =requests .request ('post',f'{host}/game/crops/move',headers =O000OO0O000OOO0O0 ,json =OO00O0O000OO00OO0 ).json ()#line:434
                                            if 'status'in O000OO00OO00O0O00 :#line:435
                                                if O000OO00OO00O0O00 ['status']==200 :#line:436
                                                    pass #line:437
                                            print ('【种植合成】:',OOO000O0OOO00O000 ,O0OOO000O0O00OOOO ,'合成成功')#line:439
                                            O00O0OOO0OOOO0OO0 =True #line:440
                                    if O00O0OOO0OOOO0OO0 :#line:441
                                        break #line:442
                                if O00O0OOO0OOOO0OO0 :#line:443
                                    break #line:444
        except Exception as O00O00O0OO00OO0O0 :#line:445
            OO00OOO000OO00O00 .synthetic ()#line:446
    def level_new (O0O0OOO0O00OOOO00 ):#line:449
        try :#line:450
            OOO00OO0OO0OOO000 =f'__{timi_new()}'#line:451
            O0O00O0OOOOOOO0OO ={'authorization':O0O0OOO0O00OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0OO0OOO000 ),'signstring':OOO00OO0OO0OOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:460
            OO0OOO0O000000O00 =requests .request ('get',f'{host}/user',headers =O0O00O0OOOOOOO0OO ).json ()#line:461
            if 'status'in OO0OOO0O000000O00 :#line:462
                if OO0OOO0O000000O00 ['status']==200 :#line:463
                    return float (OO0OOO0O000000O00 ['data']['level'])#line:464
        except Exception as OOOO0OO0OOOO000OO :#line:465
            print (OOOO0OO0OOOO000OO )#line:466
    def propsraffle (O0OO00O0O0000OO0O ):#line:469
        try :#line:470
            while True :#line:471
                O0O0OO00O00000O00 =f'__{timi_new()}'#line:472
                O000O0O0O0O000OO0 ={'authorization':O0OO00O0O0000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00O00000O00 ),'signstring':O0O0OO00O00000O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:481
                OO00OOO00O0O0O000 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O000O0O0O0O000OO0 ).json ()#line:482
                if 'status'in OO00OOO00O0O0O000 :#line:484
                    if OO00OOO00O0O0O000 ['status']==200 :#line:485
                        OOOOOO0O00OOO00OO =OO00OOO00O0O0O000 ['data']['rows']#line:486
                        O0OOO0O00OO0OO0OO =OO00OOO00O0O0O000 ['data']['vstate']#line:487
                        if OOOOOO0O00OOO00OO ==5 or OOOOOO0O00OOO00OO ==6 or OOOOOO0O00OOO00OO ==7 :#line:488
                            OO00OOO00OO000000 =OO00OOO00O0O0O000 ['data']['silver']#line:489
                            print (f'【转盘抽奖】:获得种子:{OO00OOO00OO000000}')#line:490
                        if OOOOOO0O00OOO00OO ==1 or OOOOOO0O00OOO00OO ==2 or OOOOOO0O00OOO00OO ==3 :#line:491
                            O000O0O000O0OOO00 =OO00OOO00O0O0O000 ['data']['clover']#line:492
                            print (f'【转盘抽奖】:获得三叶草:{O000O0O000O0OOO00}')#line:493
                        if OOOOOO0O00OOO00OO ==4 or OOOOOO0O00OOO00OO ==8 :#line:494
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:495
                        if OOOOOO0O00OOO00OO =='抽奖次数已用完':#line:499
                            if O0OOO0O00OO0OO0OO :#line:500
                                O0O0OO00O00000O00 =f'__{timi_new()}'#line:501
                                O000O0O0O0O000OO0 ={'authorization':O0OO00O0O0000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00O00000O00 ),'signstring':O0O0OO00O00000O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:510
                                OO000O0OO0OOOO000 =requests .request ('get',f'{host}/user',headers =O000O0O0O0O000OO0 ).json ()#line:511
                                if 'status'in OO000O0OO0OOOO000 :#line:512
                                    if OO000O0OO0OOOO000 ['status']==200 :#line:513
                                        O0O00O0000O000000 =OO000O0OO0OOOO000 ['data']['level']#line:514
                                        if float (O0O00O0000O000000 )>39 :#line:515
                                            OOO0OO0O0000O0O00 =random .randint (160 ,190 )/10 #line:516
                                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{OOO0OO0O0000O0O00}秒获取抽奖机会')#line:517
                                            time .sleep (OOO0OO0O0000O0O00 )#line:518
                                            O0000OOO0O0O0OO00 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O000O0O0O0O000OO0 ).json ()#line:519
                                            if 'status'in O0000OOO0O0O0OO00 :#line:521
                                                if O0000OOO0O0O0OO00 ['status']==200 :#line:522
                                                    print (f'【转盘抽奖】:{O0000OOO0O0O0OO00["message"]}')#line:523
                                                if O0000OOO0O0O0OO00 ['status']==500 :#line:524
                                                    print (f'【转盘抽奖】:{O0000OOO0O0O0OO00["message"]}')#line:525
                                                    break #line:526
                                            time .sleep (random .randint (10 ,15 )/10 )#line:527
                                        else :#line:528
                                            break #line:529
                            else :#line:530
                                break #line:531
                time .sleep (random .randint (8 ,15 )/10 )#line:532
        except Exception as O0OO0OOO0OO00OO0O :#line:533
            print (O0OO0OOO0OO00OO0O )#line:534
    def friends_invitation (O0OOO0OO000000OOO ):#line:537
        try :#line:538
            O0OO0OOOO00O0000O =f'__{timi_new()}'#line:539
            O0O0OO0OOOOOO0000 ={'authorization':O0OOO0OO000000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOOO00O0000O ),'signstring':O0OO0OOOO00O0000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:548
            OOO000OOOO00OO00O =requests .request ('get',f'{host}/friends',headers =O0O0OO0OOOOOO0000 ).json ()#line:549
            if 'status'in OOO000OOOO00OO00O :#line:550
                if OOO000OOOO00OO00O ['status']==200 :#line:551
                    O0OO00000O0OOO00O =OOO000OOOO00OO00O ['data']['myInviteter']#line:552
                    if O0OO00000O0OOO00O :#line:553
                        O0000O00O0OO0OO00 =O0OO00000O0OOO00O ['user']['nickname']#line:554
                        O0O0O00OOOO0O0OO0 =O0OOO0OO000000OOO .certification ()#line:555
                        print (f'【查邀请人】:我的邀请人:{O0000O00O0OO0OO00}丨实名:{O0O0O00OOOO0O0OO0}')#line:556
                    else :#line:557
                        if O0OOO0OO000000OOO .innerId !='0':#line:558
                            O0OO0OOOO00O0000O =f'_innerId=1937553_{timi_new()}'#line:559
                            O0O0OO0OOOOOO0000 ={'authorization':O0OOO0OO000000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOOO00O0000O ),'signstring':O0OO0OOOO00O0000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:568
                            OO0O0O0OOO000000O ={"innerId":'1937553'}#line:569
                            OO000OOO00O000O00 =requests .request ('post',f'{host}/friends/my-invitation',headers =O0O0OO0OOOOOO0000 ,data =OO0O0O0OOO000000O ).json ()#line:571
        except Exception as OO00OO0OO00OOOOOO :#line:572
            print (OO00OO0OO00OOOOOO )#line:573
    def add_clover (O0O0OO0O0OOOO0000 ):#line:576
        global golden_seed #line:577
        try :#line:578
            OO0OOO000O000O000 =f'__{timi_new()}'#line:579
            O0O0O000O0OOO0OO0 ={'authorization':O0O0OO0O0OOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO000O000O000 ),'signstring':OO0OOO000O000O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:588
            OO0OO000OOOO00O00 =requests .request ('get',f'{host}/assets/clovers',headers =O0O0O000O0OOO0OO0 ).json ()#line:589
            if 'status'in OO0OO000OOOO00O00 :#line:591
                if OO0OO000OOOO00O00 ['status']==200 :#line:592
                    OOOO00OO00OO000O0 =OO0OO000OOOO00O00 ['data']['clover']#line:593
                    OOOO000O0OOOO0OOO =OO0OO000OOOO00O00 ['data']['used_clover']#line:594
                    OOOOOO00O00000000 =float (OOOO00OO00OO000O0 )-float (OOOO000O0OOOO0OOO )#line:595
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OOOO000O0OOOO0OOO}')#line:596
                    if O0O0OO0O0OOOO0000 .certification ()!='未实名':#line:597
                        if OOOOOO00O00000000 >1 :#line:598
                            OO0OOO000O000O000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOOOO00O00000000)}_{timi_new()}'#line:599
                            O0O0O000O0OOO0OO0 ={'authorization':O0O0OO0O0OOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO000O000O000 ),'signstring':OO0OOO000O000O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:608
                            O0O00OOOOO00000O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOOOO00O00000000 )}#line:609
                            OO000O00OO0O0O0OO =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O0O000O0OOO0OO0 ,data =O0O00OOOOO00000O0 ).json ()#line:610
                            if 'status'in OO000O00OO0O0O0OO :#line:612
                                if OO000O00OO0O0O0OO ['status']==200 :#line:613
                                    print (f'【参与抽奖】:添加三叶草:{OO000O00OO0O0O0OO["data"]}丨数量:{OOOOOO00O00000000}')#line:614
                                if OO000O00OO0O0O0OO ['status']==500 :#line:615
                                    print (f'【参与抽奖】:添加三叶草:{OO000O00OO0O0O0OO["message"]}')#line:616
            OO00O000OOOO0OO0O =requests .request ('get',f'{host}/lottery',headers =O0O0O000O0OOO0OO0 ).json ()#line:617
            O0O0OO0O000000O0O =O0O0OO0O0OOOO0000 .winning_rewards ()#line:619
            if 'status'in OO00O000OOOO0OO0O :#line:620
                if OO00O000OOOO0OO0O ['status']==200 :#line:621
                    OO0O0OOOOO0000OO0 =OO00O000OOOO0OO0O ['data'][0 ]['day_get_gold_quantity']#line:622
                    golden_seed +=float (OO0O0OOOOO0000OO0 )#line:623
                    print (f'【参与抽奖】:预计每天中{str(OO0O0OOOOO0000OO0)[:6]}颗金种子丨好友收益:{str(O0O0OO0O000000O0O)[:6]}')#line:624
        except Exception as O0000000000OO00OO :#line:625
            print (O0000000000OO00OO )#line:626
    def energy (OOOOOOO0OO0000OO0 ):#line:629
        OOOOOOOO0OOOOO0OO =f'__{timi_new()}'#line:630
        O0O00OO0000O0O0OO ={'authorization':OOOOOOO0OO0000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO0OOOOO0OO ),'signstring':OOOOOOOO0OOOOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:639
        OO0OOOOO0000O0000 =requests .request ('get',f'{host}/energy/general',headers =O0O00OO0000O0O0OO ).json ()#line:640
        if 'status'in OO0OOOOO0000O0000 :#line:642
            if OO0OOOOO0000O0000 ['status']==200 :#line:643
                O0O00OOO000OOO000 =OO0OOOOO0000O0000 ['data']['ordinary_water_consumptions']#line:644
                if float (O0O00OOO000OOO000 )<80 :#line:645
                    OOOOO0OO00O0O0O0O =99 -float (O0O00OOO000OOO000 )#line:646
                    OO0O0000OO0O00OOO ={"fertilizer":str (OOOOO0OO00O0O0O0O ).split ('.')[0 ]}#line:647
                    O0O0O0000000OOO00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0O00OO0000O0O0OO ,data =OO0O0000OO0O00OOO ).json ()#line:648
                    if 'status'in O0O0O0000000OOO00 :#line:650
                        if O0O0O0000000OOO00 ['status']==200 :#line:651
                            print (f'【购买肥料】:{O0O0O0000000OOO00["message"]}')#line:652
                O00O0O0OO0O0OO000 =OO0OOOOO0000O0000 ['data']['ordinary_water_consumptions']#line:653
                if float (O00O0O0OO0O0OO000 )<800 :#line:654
                    O0O0O0O000OOO000O =999 -float (O00O0O0OO0O0OO000 )#line:655
                    O000OOOOOOOOOO000 ={"water":str (O0O0O0O000OOO000O ).split ('.')[0 ]}#line:656
                    OO00O0OOO0OOOO0OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O00OO0000O0O0OO ,data =O000OOOOOOOOOO000 ).json ()#line:657
                    if 'status'in OO00O0OOO0OOOO0OO :#line:658
                        if OO00O0OOO0OOOO0OO ['status']==200 :#line:659
                            print (f'【购买水滴】:{OO00O0OOO0OOOO0OO["message"]}')#line:660
def version_of_the_validation ():#line:664
    return str ((67 -56 )/10 )#line:665
def gitee_validation ():#line:668
    try :#line:669
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:670
    except Exception as OO0OOO0O0OO000O0O :#line:671
        sys .exit (0 )#line:672
def update_the_validation ():#line:676
    try :#line:677
        OOO0000O000000OO0 =gitee_validation ()#line:678
        if version_of_the_validation ()<OOO0000O000000OO0 ['CityEarth']['edition']:#line:679
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0000O000000OO0["CityEarth"]["edition"]}   ❌')#line:680
            print (f'更新内容=>>{OOO0000O000000OO0["CityEarth"]["content"]}   👍')#line:681
        else :#line:682
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0000O000000OO0["CityEarth"]["edition"]}   ✅')#line:683
            print (f'更新内容=>> {OOO0000O000000OO0["CityEarth"]["content"]}   👍')#line:684
    except Exception as O0O0OOO0O0O00OOOO :#line:685
        print (O0O0OOO0O0O00OOOO )#line:686
def os_qinglong ():#line:689
    if application in os .environ :#line:690
        O0O00OOO00OO0O000 =os .environ [application ].split ('\n')#line:691
        if len (O0O00OOO00OO0O000 )>0 :#line:692
            return O0O00OOO00OO0O000 #line:693
        else :#line:694
            print (f"{application}变量未启用")#line:695
            print ('脚本退出')#line:696
            sys .exit (1 )#line:697
    else :#line:698
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:700
        return os_built ()#line:701
def os_built ():#line:704
    if token :#line:705
        OOOO0O0OOOOOOO0O0 =token .split ('\n')#line:706
        if len (OOOO0O0OOOOOOO0O0 )>0 :#line:707
            return OOOO0O0OOOOOOO0O0 #line:708
    else :#line:709
        print (f"内置变量为空")#line:710
        print ('脚本结束')#line:711
        sys .exit (0 )#line:712
if __name__ =='__main__':#line:715
    start ()#line:716
