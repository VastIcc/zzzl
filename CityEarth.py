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
@ 版本  1.2
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
        OOO0000OO0O0OO00O =os_qinglong ()#line:7
        print (f"==========共找到{len(OOO0000OO0O0OO00O)}个账号==========")#line:8
        for OOO00O0OOOOO0OOOO in OOO0000OO0O0OO00O :#line:9
            print (f"------------正在执行第{OOO0000OO0O0OO00O.index(OOO00O0OOOOO0OOOO) + 1}个账号------------")#line:10
            OO0OOOOO00000O0OO =CityEarth (OOO00O0OOOOO0OOOO )#line:11
            def OOO00O0OOOO0O00O0 ():#line:13
                if OO0OOOOO00000O0OO .base_info ():#line:15
                    OO0OOOOO00000O0OO .game_map ()#line:19
                    OO0OOOOO00000O0OO .friends_invitation ()#line:21
                    OO0OOOOO00000O0OO .add_clover ()#line:23
                    OO0OOOOO00000O0OO .energy ()#line:25
                    OO0OOOOO00000O0OO .propsraffle ()#line:27
                    OO0OOOOO00000O0OO .synthetic ()#line:29
                    OO0OOOOO00000O0OO .crops_illustrated ()#line:31
                    OO0OOOOO00000O0OO .give_gold ()#line:33
                else :#line:34
                    print ('token失效')#line:35
            O0O0OO0OO0O0000OO =threading .Thread (target =OOO00O0OOOO0O00O0 )#line:37
            O0O0OO0OO0O0000OO .start ()#line:38
            time .sleep (time_xx )#line:39
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:41
        time .sleep (3 )#line:42
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:43
    except Exception as OO000O0000OO0OO00 :#line:44
        print (OO000O0000OO0OO00 )#line:45
def sign (OOO0O0000O0OOO0O0 ):#line:48
    O0O0O0O00000OOO0O =hashlib .md5 (OOO0O0000O0OOO0O0 .encode ()).hexdigest ()#line:49
    OO000OO0OOO0OO0O0 ="scsc%^&*"+O0O0O0O00000OOO0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:50
    O00OOO00OO00OOOOO =hashlib .md5 (OO000OO0OOO0OO0O0 .encode ()).hexdigest ()#line:51
    return O00OOO00OO00OOOOO #line:52
def timi_new ():#line:55
    return str (int (time .time ()*1000 ))#line:56
class CityEarth :#line:58
    def __init__ (O00OOO00000OO0O00 ,OOO00O00O0OOO00O0 ):#line:60
        try :#line:61
            O00OOO00000OO0O00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:62
            O00OOO00000OO0O00 .token =OOO00O00O0OOO00O0 .split ('&')[0 ]#line:63
            O00OOO00000OO0O00 .innerId =OOO00O00O0OOO00O0 .split ('&')[1 ]#line:64
            O00OOO00000OO0O00 .doneeNo =OOO00O00O0OOO00O0 .split ('&')[2 ]#line:65
        except :#line:66
            print ('变量格式错误')#line:67
    def base_info (O000O0OO00O0O0O00 ):#line:70
        try :#line:71
            O0OO0000O0OOOO00O =f'__{timi_new()}'#line:72
            OOOO00OO0000OOO0O ={'authorization':O000O0OO00O0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0000O0OOOO00O ),'signstring':O0OO0000O0OOOO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:81
            O0O00000O0000O0OO =requests .request ('get',f'{host}/user',headers =OOOO00OO0000OOO0O ).json ()#line:82
            if 'status'in O0O00000O0000O0OO :#line:84
                if O0O00000O0000O0OO ['status']==200 :#line:85
                    OO0O0OO0O0O0O00O0 =O0O00000O0000O0OO ['data']['nickname']#line:86
                    OOO0OOOOOO0OOO00O =O0O00000O0000O0OO ['data']['inner_id']#line:87
                    OO0OOO0OOO0O0O0OO =O0O00000O0000O0OO ['data']['assets']['gold']#line:88
                    O0OO00O0O0OOO0O00 =O0O00000O0000O0OO ['data']['level']#line:89
                    print (f'【账号信息】:昵称:{OO0O0OO0O0O0O00O0[:5]}丨ID:{OOO0OOOOOO0OOO00O}丨等级:{O0OO00O0O0OOO0O00}丨种子:{str(OO0OOO0OOO0O0O0OO).split(".")[0]}')#line:90
                if O0O00000O0000O0OO ['status']==401 :#line:91
                    return False #line:92
                if O0O00000O0000O0OO ['status']==500 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as OO0O00OO0O0O0OO00 :#line:96
            print (OO0O00OO0O0O0OO00 )#line:97
    def game_map (O000OO0O00OO0O00O ):#line:100
        try :#line:101
            OO000O0OOO00O00O0 =f'__{timi_new()}'#line:102
            OO00OOOOOO00OOOOO ={'authorization':O000OO0O00OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0OOO00O00O0 ),'signstring':OO000O0OOO00O00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:111
            O00O00OO0O00O000O =requests .request ('get',f'{host}/game/map',headers =OO00OOOOOO00OOOOO ).json ()#line:112
            if 'status'in O00O00OO0O00O000O :#line:114
                if O00O00OO0O00O000O ['status']==200 :#line:115
                    for O0OO0OO0O0OO0OO0O in O00O00OO0O00O000O ['data']['list'][0 ]['crops']:#line:116
                        O0OOO0OO00OO0O0O0 =O0OO0OO0O0OO0OO0O ['level']#line:118
                        if O0OOO0OO00OO0O0O0 ==41 :#line:119
                            O0O0OOO0O0OO0O000 =O0OO0OO0O0OO0OO0O ['crop_name']#line:120
                            O000O0O00OOOOO0O0 =O0OO0OO0O0OO0OO0O ['count']#line:121
                            if O000O0O00OOOOO0O0 >0 :#line:122
                                print (f'【农业资产】:{O0O0OOO0O0OO0O000}丨数量:{O000O0O00OOOOO0O0}')#line:123
        except Exception as OO0O00O00OOOOOOO0 :#line:124
            print (OO0O00O00OOOOOOO0 )#line:125
    def give_gold (O0OO0O000OO00000O ):#line:129
        try :#line:130
            OOO000O00O00OOOO0 =f'__{timi_new()}'#line:131
            O0O0OO00OOOOOOO0O ={'authorization':O0OO0O000OO00000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O00O00OOOO0 ),'signstring':OOO000O00O00OOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:140
            O00OO0O00OOO00000 =requests .request ('get',f'{host}/user',headers =O0O0OO00OOOOOOO0O ).json ()#line:141
            if 'status'in O00OO0O00OOO00000 :#line:142
                if O00OO0O00OOO00000 ['status']==200 :#line:143
                    if float (O0OO0O000OO00000O .doneeNo )!=0 :#line:144
                        OO0OOO00OO0OOOO0O =O00OO0O00OOO00000 ['data']['assets']['gold']#line:145
                        if float (OO0OOO00OO0OOOO0O )>float (O0OO0O000OO00000O .innerId ):#line:146
                            OO0OOOO000O00O0OO =int (float (OO0OOO00OO0OOOO0O )/1.1 )#line:147
                            OOO000O00O00OOOO0 =f'_doneeNo={O0OO0O000OO00000O.doneeNo}&quantity={OO0OOOO000O00O0OO}_{timi_new()}'#line:148
                            O0O0OO00OOOOOOO0O ={'authorization':O0OO0O000OO00000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O00O00OOOO0 ),'signstring':OOO000O00O00OOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:157
                            OOO000OOO00000000 ={"quantity":OO0OOOO000O00O0OO ,"doneeNo":O0OO0O000OO00000O .doneeNo }#line:161
                            O0000O0O000O000O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0OO00OOOOOOO0O ,data =OOO000OOO00000000 ).json ()#line:162
                            if 'status'in O0000O0O000O000O0 :#line:164
                                if O0000O0O000O000O0 ['status']==200 :#line:165
                                    if O0000O0O000O000O0 ['data']:#line:166
                                        print (f'【赠送种子】:赠送{OO0OOOO000O00O0OO}种子给{O0OO0O000OO00000O.doneeNo}成功')#line:167
                    else :#line:168
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:169
        except Exception as O0OOOOOO0000O0O00 :#line:170
            print (O0OOOOOO0000O0O00 )#line:171
    def winning_rewards (O0O000OO00OO0OOOO ):#line:175
        try :#line:176
            O00O00000OOO0000O =f'__{timi_new()}'#line:177
            OOO0O00O0O0O0O00O ={'authorization':O0O000OO00OO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00000OOO0000O ),'signstring':O00O00000OOO0000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
            O00O0OO0OOO0OO0O0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO0O00O0O0O0O00O ).json ()#line:187
            if 'status'in O00O0OO0OOO0OO0O0 :#line:189
                if O00O0OO0OOO0OO0O0 ['status']==200 :#line:190
                    if O00O0OO0OOO0OO0O0 ['data']['amount']:#line:191
                        O000OO00OOO0O0O0O =O00O0OO0OOO0OO0O0 ['data']['amount']['gold']#line:192
                        return O000OO00OOO0O0O0O #line:193
                    else :#line:194
                        return 0 #line:195
        except Exception as O00O0OOOO0OO00OOO :#line:196
            print (O00O0OOOO0OO00OOO )#line:197
    def certification (OOOOOO00OOO0O00O0 ):#line:201
        try :#line:202
            OOO000OOO0OOO0O0O =f'__{timi_new()}'#line:203
            O0O0000000000O00O ={'authorization':OOOOOO00OOO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOO0OOO0O0O ),'signstring':OOO000OOO0OOO0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:212
            O0000OOOO000O0O0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0O0000000000O00O ).json ()#line:213
            if 'status'in O0000OOOO000O0O0O :#line:215
                if O0000OOOO000O0O0O ['status']==200 :#line:216
                    if O0000OOOO000O0O0O ['data']['result']:#line:217
                        O0O00OO000O000OO0 =O0000OOOO000O0O0O ['data']['nick_name']#line:218
                        return O0O00OO000O000OO0 #line:219
                    else :#line:220
                        return '未实名'#line:221
        except Exception as O0O0O00O000O0OO0O :#line:222
            print (O0O0O00O000O0OO0O )#line:223
    def crops_illustrated (O0O00OOO0O00OO00O ):#line:227
        try :#line:228
            O000OO000O0000OO0 =f'__{timi_new()}'#line:229
            O0000000OO0O0OOO0 ={'authorization':O0O00OOO0O00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO000O0000OO0 ),'signstring':O000OO000O0000OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:238
            OO00OOOO000OO0O0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0000000OO0O0OOO0 ).json ()#line:239
            if 'status'in OO00OOOO000OO0O0O :#line:241
                if OO00OOOO000OO0O0O ['status']==200 :#line:242
                    O0OOO0O000000O0OO =OO00OOOO000OO0O0O ['data'][0 ]['crops']#line:243
                    for O00OO0000OO00O0OO in O0OOO0O000000O0OO :#line:244
                        if O00OO0000OO00O0OO ['ill_clover_award']:#line:245
                            if float (O00OO0000OO00O0OO ['ill_clover_award'])>1 :#line:246
                                if O00OO0000OO00O0OO ['is_finish']:#line:247
                                    if not O00OO0000OO00O0OO ['is_getit']:#line:248
                                        if O0O00OOO0O00OO00O .certification ()!='未实名':#line:249
                                            O000OO000O0000OO0 =f'_award_level={O00OO0000OO00O0OO["level"]}_{timi_new()}'#line:250
                                            O0000000OO0O0OOO0 ={'authorization':O0O00OOO0O00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO000O0000OO0 ),'signstring':O000OO000O0000OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:259
                                            OOOOOOOOO0OOOO000 ={"award_level":O00OO0000OO00O0OO ['level']}#line:260
                                            OO0OOOO0000OO0OO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0000000OO0O0OOO0 ,json =OOOOOOOOO0OOOO000 ).json ()#line:262
                                            if 'status'in OO0OOOO0000OO0OO0 :#line:263
                                                if OO0OOOO0000OO0OO0 ['status']==200 :#line:264
                                                    OO000OO0O0O00O00O =OO0OOOO0000OO0OO0 ['data']['ill_clover_award']#line:265
                                                    print (f'【图鉴奖励】:领取{O00OO0000OO00O0OO["crop_name"]}成就丨奖励{OO000OO0O0O00O00O}叶子成功')#line:267
                                                if OO0OOOO0000OO0OO0 ['status']==500 :#line:268
                                                    print (f'【图鉴奖励】:{OO0OOOO0000OO0OO0["message"]}')#line:269
        except Exception as OO0O00OO00O0OO00O :#line:270
            print (OO0O00OO00O0OO00O )#line:271
    def watched_ad (O0O00OO0000OO0000 ):#line:275
        try :#line:276
            O0OOO0O0O0O000O00 =f'__{timi_new()}'#line:277
            OOO00O00000OOOOO0 ={'authorization':O0O00OO0000OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O0O0O000O00 ),'signstring':O0OOO0O0O0O000O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:286
            OO00O0000OOO0O000 =requests .request ('post',f'{host}/game/watched-ad',headers =OOO00O00000OOOOO0 ).json ()#line:287
            print (OO00O0000OOO0O000 )#line:288
        except Exception as OOO0O00O0000OO0OO :#line:289
            print (OOO0O00O0000OO0OO )#line:290
    def user_ad (OOOOO0OOO000000OO ):#line:294
        try :#line:295
            OO000OO00O0OOOOOO =f'__{timi_new()}'#line:296
            OOOO0OO00O0000O00 ={'authorization':OOOOO0OOO000000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO00O0OOOOOO ),'signstring':OO000OO00O0OOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:305
            O0O0O0OO00OO0O0O0 =requests .request ('get',f'{host}/user/ad',headers =OOOO0OO00O0000O00 ).json ()#line:306
            if 'status'in O0O0O0OO00OO0O0O0 :#line:308
                if O0O0O0OO00OO0O0O0 ['status']==200 :#line:309
                    O0O00O0OOOO000O0O =O0O0O0OO00OO0O0O0 ['data']['max_time']#line:310
                    O0000OO00000000OO =O0O0O0OO00OO0O0O0 ['data']['watch_time']#line:311
                    OO0O000OOOO00OO00 =O0O0O0OO00OO0O0O0 ['data']['added_time']#line:312
                    print (f'【获取种子】:获取种子剩余{OO0O000OOOO00OO00 + O0O00O0OOOO000O0O - O0000OO00000000OO}次丨好友提供:{OO0O000OOOO00OO00}次')#line:313
                    if OO0O000OOOO00OO00 +O0O00O0OOOO000O0O -O0000OO00000000OO >0 :#line:314
                        time .sleep (random .randint (16 ,19 ))#line:315
                        OOOO00OO0O0000000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOOO0OO00O0000O00 ).json ()#line:316
                        if 'status'in OOOO00OO0O0000000 :#line:318
                            if OOOO00OO0O0000000 ['status']==200 :#line:319
                                OO0OO0000000OOO00 =OOOO00OO0O0000000 ['data']['silver']#line:320
                                print (f'【获取种子】:获得种子:{OO0OO0000000OOO00}')#line:321
                                return True #line:322
                            if OOOO00OO0O0000000 ['status']==500 :#line:323
                                OO0O00000O0O0OOO0 =OOOO00OO0O0000000 ['message']#line:324
                                print (f'【获取种子】:{OO0O00000O0O0OOO0}')#line:325
                                return False #line:326
        except Exception as OO00O00O0OO0O00O0 :#line:327
            print (OO00O00O0OO0O00O0 )#line:328
    def synthetic (OOO0OO00O0OOO0O0O ):#line:332
        global id ,g #line:333
        try :#line:334
            OOOO0OO00OOOOO0O0 =OOO0OO00O0OOO0O0O .level_new ()#line:335
            while True :#line:336
                O0OO0O0OO00OOO00O =f'__{timi_new()}'#line:337
                OOOOO000O0OOOOO0O ={'authorization':OOO0OO00O0OOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0OO00OOO00O ),'signstring':O0OO0O0OO00OOO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:346
                OO000OO00OOO0OO0O =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO000O0OOOOO0O ).json ()#line:347
                if 'status'in OO000OO00OOO0OO0O :#line:349
                    if OO000OO00OOO0OO0O ['status']==200 :#line:350
                        OO00OOO0OOOO0OO0O =OO000OO00OOO0OO0O ['data']['cropList']#line:351
                        OO0OO0O0O00OOO000 =OO000OO00OOO0OO0O ['data']['gameCoreDataDBid']#line:352
                        O000OO0O0O0O0O0O0 =0 #line:353
                        for O00OOOO00OO0O000O in OO00OOO0OOOO0OO0O :#line:354
                            if not O00OOOO00OO0O000O :#line:355
                                OO000OO0OO0OOO0OO =f'_crop_id={OO0OO0O0O00OOO000}&site={O000OO0O0O0O0O0O0}_{OOO0OO00O0OOO0O0O.time}'#line:356
                                O0000OOO000O000O0 ={'authorization':OOO0OO00O0OOO0O0O .token ,'timestamp':OOO0OO00O0OOO0O0O .time ,'sign':sign (OO000OO0OO0OOO0OO ),'signstring':OO000OO0OO0OOO0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:365
                                OOOO0O0O0000O0O00 ={"site":O000OO0O0O0O0O0O0 ,"crop_id":OO0OO0O0O00OOO000 }#line:366
                                OO0O000O0OOO00O00 =requests .request ('post',f'{host}/game/crops/buy',headers =O0000OOO000O000O0 ,data =OOOO0O0O0000O0O00 ).json ()#line:367
                                time .sleep (random .randint (1 ,3 )/10 )#line:369
                                if 'status'in OO0O000O0OOO00O00 :#line:370
                                    if OO0O000O0OOO00O00 ['status']==200 :#line:371
                                        if OO0O000O0OOO00O00 ['message']=='种子数量不足':#line:372
                                            OOOO0OO00OOOOO0O0 =OOO0OO00O0OOO0O0O .level_new ()#line:373
                                            print (f'【种植合成】:{OO0O000O0OOO00O00["message"]}')#line:374
                                            if not OOO0OO00O0OOO0O0O .user_ad ():#line:375
                                                return False #line:376
                                        print (f'【种植合成】:种植农作物,位置{O000OO0O0O0O0O0O0}')#line:377
                                    if OO0O000O0OOO00O00 ['status']==500 :#line:378
                                        print (f'【种植合成】:{OO0O000O0OOO00O00["message"]}')#line:379
                                        return False #line:380
                            O000OO0O0O0O0O0O0 +=1 #line:381
                        OOO00O0OO000OOOOO =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO000O0OOOOO0O ).json ()#line:382
                        O00000000OO0OOOOO =OOO00O0OO000OOOOO ['data']['cropList']#line:383
                        O00OO00O00OOO0O00 =False #line:384
                        for O00OOOO00OO0O000O in range (12 ):#line:385
                            id =O00000000OO0OOOOO [O00OOOO00OO0O000O ]['level']#line:386
                            if float (OOOO0OO00OOOOO0O0 )-float (id )>9 :#line:387
                                OOO00000O0O00O0OO =f'_site={O00OOOO00OO0O000O}_{timi_new()}'#line:388
                                O000O0O00O000O0O0 ={'accept':'application/json, text/plain, */*','authorization':OOO0OO00O0OOO0O0O .token ,'timestamp':timi_new (),'sign':sign (OOO00000O0O00O0OO ),'signstring':OOO00000O0O00O0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:398
                                OO0O000O0OO000O0O ={"site":O00OOOO00OO0O000O }#line:399
                                O00O000OOO0O00OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000O0O00O000O0O0 ,data =OO0O000O0OO000O0O ).json ()#line:401
                                if 'status'in O00O000OOO0O00OOO :#line:402
                                    if O00O000OOO0O00OOO ['status']==200 :#line:403
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:404
                            if id !=0 :#line:405
                                for O0000OO0O0O00OO00 in range (11 ):#line:406
                                    OO0O0O0OO000O00OO =O0000OO0O0O00OO00 +1 #line:407
                                    g =O00000000OO0OOOOO [OO0O0O0OO000O00OO ]['level']#line:408
                                    if id ==g :#line:409
                                        OOO00OO0000OO0O00 =O0000OO0O0O00OO00 +2 #line:410
                                        if OOO00OO0000OO0O00 ==O00OOOO00OO0O000O +1 :#line:411
                                            pass #line:412
                                        else :#line:413
                                            OO00O000000O00O0O =O00OOOO00OO0O000O +1 #line:414
                                            time .sleep (random .randint (1 ,3 )/10 )#line:416
                                            OO00O0OO000OOO0OO =f'_site={OO00O000000O00O0O - 1}&targetSite={OOO00OO0000OO0O00 - 1}_{timi_new()}'#line:417
                                            OO0O0O0OOOOOO000O ={'accept':'application/json, text/plain, */*','authorization':OOO0OO00O0OOO0O0O .token ,'timestamp':timi_new (),'sign':sign (OO00O0OO000OOO0OO ),'signstring':OO00O0OO000OOO0OO ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:432
                                            O00O0O00OOOO00000 ={"site":int (OO00O000000O00O0O -1 ),"targetSite":int (OOO00OO0000OO0O00 -1 )}#line:433
                                            OO0O000OOOOO0OO00 =requests .request ('post',f'{host}/game/crops/move',headers =OO0O0O0OOOOOO000O ,json =O00O0O00OOOO00000 ).json ()#line:435
                                            if 'status'in OO0O000OOOOO0OO00 :#line:436
                                                if OO0O000OOOOO0OO00 ['status']==200 :#line:437
                                                    pass #line:438
                                            print ('【种植合成】:',OO00O000000O00O0O ,OOO00OO0000OO0O00 ,'合成成功')#line:440
                                            O00OO00O00OOO0O00 =True #line:441
                                    if O00OO00O00OOO0O00 :#line:442
                                        break #line:443
                                if O00OO00O00OOO0O00 :#line:444
                                    break #line:445
        except Exception as O0OO0O000OOO0O00O :#line:446
            OOO0OO00O0OOO0O0O .synthetic ()#line:447
    def level_new (O00000O000OOOO0O0 ):#line:450
        try :#line:451
            OOO00O0OOOO000OOO =f'__{timi_new()}'#line:452
            OO000O0O00OOO0OO0 ={'authorization':O00000O000OOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OOOO000OOO ),'signstring':OOO00O0OOOO000OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:461
            O0OOOO0O0O00OOOO0 =requests .request ('get',f'{host}/user',headers =OO000O0O00OOO0OO0 ).json ()#line:462
            if 'status'in O0OOOO0O0O00OOOO0 :#line:463
                if O0OOOO0O0O00OOOO0 ['status']==200 :#line:464
                    return float (O0OOOO0O0O00OOOO0 ['data']['level'])#line:465
        except Exception as OO00000O0O0OOOOOO :#line:466
            print (OO00000O0O0OOOOOO )#line:467
    def propsraffle (O00OO0O0OOOO000OO ):#line:470
        try :#line:471
            while True :#line:472
                O0O00OO0O00O00OO0 =f'__{timi_new()}'#line:473
                O0OO0OO0O0O0OO0OO ={'authorization':O00OO0O0OOOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0O00O00OO0 ),'signstring':O0O00OO0O00O00OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:482
                O00O00O00OOOOO000 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OO0OO0O0O0OO0OO ).json ()#line:483
                if 'status'in O00O00O00OOOOO000 :#line:485
                    if O00O00O00OOOOO000 ['status']==200 :#line:486
                        O000O0O00OO00OOOO =O00O00O00OOOOO000 ['data']['rows']#line:487
                        O000O00000O000OO0 =O00O00O00OOOOO000 ['data']['vstate']#line:488
                        if O000O0O00OO00OOOO ==5 or O000O0O00OO00OOOO ==6 or O000O0O00OO00OOOO ==7 :#line:489
                            O0OOO0O0O0O00OO00 =O00O00O00OOOOO000 ['data']['silver']#line:490
                            print (f'【转盘抽奖】:获得种子:{O0OOO0O0O0O00OO00}')#line:491
                        if O000O0O00OO00OOOO ==1 or O000O0O00OO00OOOO ==2 or O000O0O00OO00OOOO ==3 :#line:492
                            OO0O000OOO00OOOO0 =O00O00O00OOOOO000 ['data']['clover']#line:493
                            print (f'【转盘抽奖】:获得三叶草:{OO0O000OOO00OOOO0}')#line:494
                        if O000O0O00OO00OOOO ==4 or O000O0O00OO00OOOO ==8 :#line:495
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:496
                        if O000O0O00OO00OOOO =='抽奖次数已用完':#line:500
                            if O000O00000O000OO0 :#line:501
                                O0O00OO0O00O00OO0 =f'__{timi_new()}'#line:502
                                O0OO0OO0O0O0OO0OO ={'authorization':O00OO0O0OOOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0O00O00OO0 ),'signstring':O0O00OO0O00O00OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:511
                                OO000OO0OO000O0O0 =requests .request ('get',f'{host}/user',headers =O0OO0OO0O0O0OO0OO ).json ()#line:512
                                if 'status'in OO000OO0OO000O0O0 :#line:513
                                    if OO000OO0OO000O0O0 ['status']==200 :#line:514
                                        O000O0000000O0O00 =OO000OO0OO000O0O0 ['data']['level']#line:515
                                        if float (O000O0000000O0O00 )>39 :#line:516
                                            O0O0O00OO0OOO0OO0 =random .randint (160 ,190 )/10 #line:517
                                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{O0O0O00OO0OOO0OO0}秒获取抽奖机会')#line:518
                                            time .sleep (O0O0O00OO0OOO0OO0 )#line:519
                                            OO000000000O0OO0O =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O0OO0OO0O0O0OO0OO ).json ()#line:520
                                            if 'status'in OO000000000O0OO0O :#line:522
                                                if OO000000000O0OO0O ['status']==200 :#line:523
                                                    print (f'【转盘抽奖】:{OO000000000O0OO0O["message"]}')#line:524
                                                if OO000000000O0OO0O ['status']==500 :#line:525
                                                    print (f'【转盘抽奖】:{OO000000000O0OO0O["message"]}')#line:526
                                                    break #line:527
                                            time .sleep (random .randint (10 ,15 )/10 )#line:528
                                        else :#line:529
                                            break #line:530
                            else :#line:531
                                break #line:532
                time .sleep (random .randint (8 ,15 )/10 )#line:533
        except Exception as OO0OOOOO00000OOOO :#line:534
            print (OO0OOOOO00000OOOO )#line:535
    def friends_invitation (OO0OOOOO00O00O0OO ):#line:538
        try :#line:539
            OOOOO0O00OO0OOOOO =f'__{timi_new()}'#line:540
            OO0OO0OOOOOO0OO00 ={'authorization':OO0OOOOO00O00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O00OO0OOOOO ),'signstring':OOOOO0O00OO0OOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:549
            O0O000000000O0O0O =requests .request ('get',f'{host}/friends',headers =OO0OO0OOOOOO0OO00 ).json ()#line:550
            if 'status'in O0O000000000O0O0O :#line:551
                if O0O000000000O0O0O ['status']==200 :#line:552
                    O00000OOO0000OOOO =O0O000000000O0O0O ['data']['myInviteter']#line:553
                    if O00000OOO0000OOOO :#line:554
                        OO0O0O000OO0OOOO0 =O00000OOO0000OOOO ['user']['nickname']#line:555
                        O00O0OOO00OOOOO0O =OO0OOOOO00O00O0OO .certification ()#line:556
                        print (f'【查邀请人】:我的邀请人:{OO0O0O000OO0OOOO0}丨实名:{O00O0OOO00OOOOO0O}')#line:557
                    else :#line:558
                        if OO0OOOOO00O00O0OO .innerId !='0':#line:559
                            OOOOO0O00OO0OOOOO =f'_innerId=1937553_{timi_new()}'#line:560
                            OO0OO0OOOOOO0OO00 ={'authorization':OO0OOOOO00O00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O00OO0OOOOO ),'signstring':OOOOO0O00OO0OOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:569
                            O0000OO0OOO0O0OOO ={"innerId":'1937553'}#line:570
                            O000O000OOO0OO00O =requests .request ('post',f'{host}/friends/my-invitation',headers =OO0OO0OOOOOO0OO00 ,data =O0000OO0OOO0O0OOO ).json ()#line:572
        except Exception as OOOO00OO0OOO00O0O :#line:573
            print (OOOO00OO0OOO00O0O )#line:574
    def add_clover (OOOOOOOO0O0OOO000 ):#line:577
        global golden_seed #line:578
        try :#line:579
            O000OO0O0OO00OOOO =f'__{timi_new()}'#line:580
            O0OO0O0OO000O0O0O ={'authorization':OOOOOOOO0O0OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O0OO00OOOO ),'signstring':O000OO0O0OO00OOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:589
            O0O0000O00OO00OO0 =requests .request ('get',f'{host}/assets/clovers',headers =O0OO0O0OO000O0O0O ).json ()#line:590
            if 'status'in O0O0000O00OO00OO0 :#line:592
                if O0O0000O00OO00OO0 ['status']==200 :#line:593
                    O00OOOO00000OOOO0 =O0O0000O00OO00OO0 ['data']['clover']#line:594
                    O0OOOOO0OOO000O00 =O0O0000O00OO00OO0 ['data']['used_clover']#line:595
                    O00OO00OOO00OOOO0 =float (O00OOOO00000OOOO0 )-float (O0OOOOO0OOO000O00 )#line:596
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0OOOOO0OOO000O00}')#line:597
                    if OOOOOOOO0O0OOO000 .certification ()!='未实名':#line:598
                        if O00OO00OOO00OOOO0 >1 :#line:599
                            O000OO0O0OO00OOOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00OO00OOO00OOOO0)}_{timi_new()}'#line:600
                            O0OO0O0OO000O0O0O ={'authorization':OOOOOOOO0O0OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O0OO00OOOO ),'signstring':O000OO0O0OO00OOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:609
                            O0000O000OO00O000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00OO00OOO00OOOO0 )}#line:610
                            O0O0000O00OOO0O00 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OO0O0OO000O0O0O ,data =O0000O000OO00O000 ).json ()#line:611
                            if 'status'in O0O0000O00OOO0O00 :#line:613
                                if O0O0000O00OOO0O00 ['status']==200 :#line:614
                                    print (f'【参与抽奖】:添加三叶草:{O0O0000O00OOO0O00["data"]}丨数量:{O00OO00OOO00OOOO0}')#line:615
                                if O0O0000O00OOO0O00 ['status']==500 :#line:616
                                    print (f'【参与抽奖】:添加三叶草:{O0O0000O00OOO0O00["message"]}')#line:617
            OO0O00OO00O000000 =requests .request ('get',f'{host}/lottery',headers =O0OO0O0OO000O0O0O ).json ()#line:618
            O000O00000O0O000O =OOOOOOOO0O0OOO000 .winning_rewards ()#line:620
            if 'status'in OO0O00OO00O000000 :#line:621
                if OO0O00OO00O000000 ['status']==200 :#line:622
                    OO0OOOOO0000O000O =OO0O00OO00O000000 ['data'][0 ]['day_get_gold_quantity']#line:623
                    golden_seed +=float (OO0OOOOO0000O000O )#line:624
                    print (f'【参与抽奖】:预计每天中{str(OO0OOOOO0000O000O)[:6]}颗金种子丨好友收益:{str(O000O00000O0O000O)[:6]}')#line:625
        except Exception as O0O0000O00O00O00O :#line:626
            print (O0O0000O00O00O00O )#line:627
    def energy (OOOO00OOOO0OOOO0O ):#line:630
        O0O00O0OO0OO0O0O0 =f'__{timi_new()}'#line:631
        O00O0OO00000O0000 ={'authorization':OOOO00OOOO0OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OO0OO0O0O0 ),'signstring':O0O00O0OO0OO0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:640
        OO0O0000OOO0OO000 =requests .request ('get',f'{host}/energy/general',headers =O00O0OO00000O0000 ).json ()#line:641
        if 'status'in OO0O0000OOO0OO000 :#line:643
            if OO0O0000OOO0OO000 ['status']==200 :#line:644
                OO0OOOO00OO0000O0 =OO0O0000OOO0OO000 ['data']['ordinary_water']#line:645
                O0OOOOO0O0OO0OOOO =OO0O0000OOO0OO000 ['data']['ordinary_fertilizer']#line:646
                print (f'【我的营养】:肥料:{str(O0OOOOO0O0OO0OOOO).split(".")[0]}丨水滴:{str(OO0OOOO00OO0000O0).split(".")[0]}')#line:647
                if float (O0OOOOO0O0OO0OOOO )<96 :#line:648
                    OOO00OO000O0OO000 =99 -float (O0OOOOO0O0OO0OOOO )#line:649
                    O0OOO0OO00OO000OO ={"fertilizer":str (OOO00OO000O0OO000 ).split ('.')[0 ]}#line:650
                    OO0O0O0000O0O0000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00O0OO00000O0000 ).json ()#line:651
                    if 'status'in OO0O0O0000O0O0000 :#line:653
                        if OO0O0O0000O0O0000 ['status']==200 :#line:654
                            print (f'【购买肥料】:看广告获取肥料:{OO0O0O0000O0O0000["message"]}')#line:655
                if float (OO0OOOO00OO0000O0 )<880 :#line:657
                    OO0OOOOO00000OO00 =999 -float (OO0OOOO00OO0000O0 )#line:658
                    O00O0O00OOO0OO0O0 ={"water":str (OO0OOOOO00000OO00 ).split ('.')[0 ]}#line:659
                    O00O00O00O00OO00O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00O0OO00000O0000 ).json ()#line:660
                    if 'status'in O00O00O00O00OO00O :#line:662
                        if O00O00O00O00OO00O ['status']==200 :#line:663
                            print (f'【购买水滴】:看广告获取水滴:{O00O00O00O00OO00O["message"]}')#line:664
def version_of_the_validation ():#line:668
    return str ((68 -56 )/10 )#line:669
def gitee_validation ():#line:672
    try :#line:673
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:674
    except :#line:675
        sys .exit (0 )#line:676
def update_the_validation ():#line:680
    try :#line:681
        O00O0OO0O0OO0OO00 =gitee_validation ()#line:682
        if version_of_the_validation ()<O00O0OO0O0OO0OO00 ['CityEarth']['edition']:#line:683
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0OO0O0OO0OO00["CityEarth"]["edition"]}   ❌')#line:684
            print (f'更新内容=>>{O00O0OO0O0OO0OO00["CityEarth"]["content"]}   👍')#line:685
        else :#line:686
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0OO0O0OO0OO00["CityEarth"]["edition"]}   ✅')#line:687
            print (f'更新内容=>> {O00O0OO0O0OO0OO00["CityEarth"]["content"]}   👍')#line:688
    except Exception as OOO0O00OOO00OO0OO :#line:689
        print (OOO0O00OOO00OO0OO )#line:690
def os_qinglong ():#line:693
    if application in os .environ :#line:694
        O0000OO000O0O0O0O =os .environ [application ].split ('\n')#line:695
        if len (O0000OO000O0O0O0O )>0 :#line:696
            return O0000OO000O0O0O0O #line:697
        else :#line:698
            print (f"{application}变量未启用")#line:699
            print ('脚本退出')#line:700
            sys .exit (1 )#line:701
    else :#line:702
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:704
        return os_built ()#line:705
def os_built ():#line:708
    if token :#line:709
        O00OO0OOO00OOOOO0 =token .split ('\n')#line:710
        if len (O00OO0OOO00OOOOO0 )>0 :#line:711
            return O00OO0OOO00OOOOO0 #line:712
    else :#line:713
        print (f"内置变量为空")#line:714
        print ('脚本结束')#line:715
        sys .exit (0 )#line:716
if __name__ =='__main__':#line:719
    start ()#line:720
