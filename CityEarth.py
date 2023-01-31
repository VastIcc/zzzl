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
@ 版本  1.3
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
        O0O0OOO0OOO0OOOOO =os_qinglong ()#line:7
        print (f"==========共找到{len(O0O0OOO0OOO0OOOOO)}个账号==========")#line:8
        for O00O0000000O0O0O0 in O0O0OOO0OOO0OOOOO :#line:9
            print (f"------------正在执行第{O0O0OOO0OOO0OOOOO.index(O00O0000000O0O0O0) + 1}个账号------------")#line:10
            O0O0000O00000OOO0 =CityEarth (O00O0000000O0O0O0 )#line:11
            def O0OOOO0O0OOO00OOO ():#line:13
                if O0O0000O00000OOO0 .base_info ():#line:15
                    O0O0000O00000OOO0 .game_map ()#line:19
                    O0O0000O00000OOO0 .friends_invitation ()#line:21
                    O0O0000O00000OOO0 .add_clover ()#line:23
                    O0O0000O00000OOO0 .energy ()#line:25
                    O0O0000O00000OOO0 .propsraffle ()#line:27
                    O0O0000O00000OOO0 .synthetic ()#line:29
                    O0O0000O00000OOO0 .crops_illustrated ()#line:31
                    O0O0000O00000OOO0 .give_gold ()#line:33
                else :#line:34
                    print ('token失效')#line:35
            OO00000OO00O00O0O =threading .Thread (target =O0OOOO0O0OOO00OOO )#line:37
            OO00000OO00O00O0O .start ()#line:38
            time .sleep (time_xx )#line:39
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:41
        time .sleep (3 )#line:42
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:43
    except Exception as O00O000O0O00O0O00 :#line:44
        print (O00O000O0O00O0O00 )#line:45
def sign (O00O00O000O00O0O0 ):#line:48
    OOOOOO0O0OOO00O0O =hashlib .md5 (O00O00O000O00O0O0 .encode ()).hexdigest ()#line:49
    O0O0OO00O0O00000O ="scsc%^&*"+OOOOOO0O0OOO00O0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:50
    O0000OOO0O0OOO00O =hashlib .md5 (O0O0OO00O0O00000O .encode ()).hexdigest ()#line:51
    return O0000OOO0O0OOO00O #line:52
def timi_new ():#line:55
    return str (int (time .time ()*1000 ))#line:56
class CityEarth :#line:58
    def __init__ (O000OOOO00OO00O00 ,O0000O0O0000O0000 ):#line:60
        try :#line:61
            O000OOOO00OO00O00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:62
            O000OOOO00OO00O00 .token =O0000O0O0000O0000 .split ('&')[0 ]#line:63
            O000OOOO00OO00O00 .innerId =O0000O0O0000O0000 .split ('&')[1 ]#line:64
            O000OOOO00OO00O00 .doneeNo =O0000O0O0000O0000 .split ('&')[2 ]#line:65
        except :#line:66
            print ('变量格式错误')#line:67
    def base_info (O0O00000OO000O00O ):#line:70
        try :#line:71
            OOO000O00OO0O00O0 =f'__{timi_new()}'#line:72
            OO0O0000O0O000O00 ={'authorization':O0O00000OO000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O00OO0O00O0 ),'signstring':OOO000O00OO0O00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:81
            O0O0O0OOO00OOOOO0 =requests .request ('get',f'{host}/user',headers =OO0O0000O0O000O00 ).json ()#line:82
            if 'status'in O0O0O0OOO00OOOOO0 :#line:84
                if O0O0O0OOO00OOOOO0 ['status']==200 :#line:85
                    O000OO0OOOO00O0OO =O0O0O0OOO00OOOOO0 ['data']['nickname']#line:86
                    OO0OO0O0O00O0000O =O0O0O0OOO00OOOOO0 ['data']['inner_id']#line:87
                    O0O0OO0OO0O000O00 =O0O0O0OOO00OOOOO0 ['data']['assets']['gold']#line:88
                    O0O00OOO000OO0OOO =O0O0O0OOO00OOOOO0 ['data']['level']#line:89
                    print (f'【账号信息】:昵称:{O000OO0OOOO00O0OO[:5]}丨ID:{OO0OO0O0O00O0000O}丨等级:{O0O00OOO000OO0OOO}丨种子:{str(O0O0OO0OO0O000O00).split(".")[0]}')#line:90
                if O0O0O0OOO00OOOOO0 ['status']==401 :#line:91
                    return False #line:92
                if O0O0O0OOO00OOOOO0 ['status']==500 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as OO0O00O0OOOOO0000 :#line:96
            print (OO0O00O0OOOOO0000 )#line:97
    def game_map (OO0O0OOOO0O0OOO00 ):#line:100
        try :#line:101
            O0O00O0OO0O00OOO0 =f'__{timi_new()}'#line:102
            O00O0O0OO00O00OO0 ={'authorization':OO0O0OOOO0O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OO0O00OOO0 ),'signstring':O0O00O0OO0O00OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:111
            O00OOO0O0O000OOOO =requests .request ('get',f'{host}/game/map',headers =O00O0O0OO00O00OO0 ).json ()#line:112
            if 'status'in O00OOO0O0O000OOOO :#line:114
                if O00OOO0O0O000OOOO ['status']==200 :#line:115
                    for O0OOOO0O00OO0O0O0 in O00OOO0O0O000OOOO ['data']['list'][0 ]['crops']:#line:116
                        O0OOOOO0O0O0O00O0 =O0OOOO0O00OO0O0O0 ['level']#line:118
                        if O0OOOOO0O0O0O00O0 ==41 :#line:119
                            O0O0O0OOO00O0O0OO =O0OOOO0O00OO0O0O0 ['crop_name']#line:120
                            OO0OO0O000OOOOO0O =O0OOOO0O00OO0O0O0 ['count']#line:121
                            if OO0OO0O000OOOOO0O >0 :#line:122
                                print (f'【农业资产】:{O0O0O0OOO00O0O0OO}丨数量:{OO0OO0O000OOOOO0O}')#line:123
        except Exception as OOOO00O00000OOO0O :#line:124
            print (OOOO00O00000OOO0O )#line:125
    def give_gold (OO0OOOO0O0O0OO00O ):#line:129
        try :#line:130
            OOOOOO00OOOO0OO00 =f'__{timi_new()}'#line:131
            OOO00O0OO0O0O0OOO ={'authorization':OO0OOOO0O0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00OOOO0OO00 ),'signstring':OOOOOO00OOOO0OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:140
            O0OOOOOO0OOOO0O00 =requests .request ('get',f'{host}/user',headers =OOO00O0OO0O0O0OOO ).json ()#line:141
            if 'status'in O0OOOOOO0OOOO0O00 :#line:142
                if O0OOOOOO0OOOO0O00 ['status']==200 :#line:143
                    if float (OO0OOOO0O0O0OO00O .doneeNo )!=0 :#line:144
                        O0O00O0O000O0O0OO =O0OOOOOO0OOOO0O00 ['data']['assets']['gold']#line:145
                        if float (O0O00O0O000O0O0OO )>float (OO0OOOO0O0O0OO00O .innerId ):#line:146
                            O00OOOOOO0OO0OOO0 =int (float (O0O00O0O000O0O0OO )/1.1 )#line:147
                            OOOOOO00OOOO0OO00 =f'_doneeNo={OO0OOOO0O0O0OO00O.doneeNo}&quantity={O00OOOOOO0OO0OOO0}_{timi_new()}'#line:148
                            OOO00O0OO0O0O0OOO ={'authorization':OO0OOOO0O0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00OOOO0OO00 ),'signstring':OOOOOO00OOOO0OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:157
                            OOO0OOO0O0OO00OO0 ={"quantity":O00OOOOOO0OO0OOO0 ,"doneeNo":OO0OOOO0O0O0OO00O .doneeNo }#line:161
                            O0OO0O0000000000O =requests .request ('post',f'{host}/finance/give-gold',headers =OOO00O0OO0O0O0OOO ,data =OOO0OOO0O0OO00OO0 ).json ()#line:162
                            if 'status'in O0OO0O0000000000O :#line:164
                                if O0OO0O0000000000O ['status']==200 :#line:165
                                    if O0OO0O0000000000O ['data']:#line:166
                                        print (f'【赠送种子】:赠送{O00OOOOOO0OO0OOO0}种子给{OO0OOOO0O0O0OO00O.doneeNo}成功')#line:167
                    else :#line:168
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:169
        except Exception as OO0000000O0O00O00 :#line:170
            print (OO0000000O0O00O00 )#line:171
    def winning_rewards (OO0OO0O00O00OOO0O ):#line:175
        try :#line:176
            O0OOOOO0O0O0O0OOO =f'__{timi_new()}'#line:177
            OOOO0O000O00O0000 ={'authorization':OO0OO0O00O00OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0O0O0O0OOO ),'signstring':O0OOOOO0O0O0O0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
            O0OOOO000O0O0OO00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOOO0O000O00O0000 ).json ()#line:187
            if 'status'in O0OOOO000O0O0OO00 :#line:189
                if O0OOOO000O0O0OO00 ['status']==200 :#line:190
                    if O0OOOO000O0O0OO00 ['data']['amount']:#line:191
                        O0OOOOO0O000OO0OO =O0OOOO000O0O0OO00 ['data']['amount']['gold']#line:192
                        return O0OOOOO0O000OO0OO #line:193
                    else :#line:194
                        return 0 #line:195
        except Exception as O00OO0000OO0O000O :#line:196
            print (O00OO0000OO0O000O )#line:197
    def certification (O000OOO0000000OOO ):#line:201
        try :#line:202
            O00000O00O00000OO =f'__{timi_new()}'#line:203
            OOO0O0OOOO00OOO0O ={'authorization':O000OOO0000000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O00O00000OO ),'signstring':O00000O00O00000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:212
            OO0OO0O00OO0OO00O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO0O0OOOO00OOO0O ).json ()#line:213
            if 'status'in OO0OO0O00OO0OO00O :#line:215
                if OO0OO0O00OO0OO00O ['status']==200 :#line:216
                    if OO0OO0O00OO0OO00O ['data']['result']:#line:217
                        OOO0OOO000OO000O0 =OO0OO0O00OO0OO00O ['data']['nick_name']#line:218
                        return OOO0OOO000OO000O0 #line:219
                    else :#line:220
                        return '未实名'#line:221
        except Exception as O00OO0OO0OOO00O00 :#line:222
            print (O00OO0OO0OOO00O00 )#line:223
    def crops_illustrated (O0000O0OOO0OOOOO0 ):#line:227
        try :#line:228
            O0OOO0O0O0000O0OO =f'__{timi_new()}'#line:229
            O00O0O00O00OOO0O0 ={'authorization':O0000O0OOO0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O0O0000O0OO ),'signstring':O0OOO0O0O0000O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:238
            O00OO000O0OOOO0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00O0O00O00OOO0O0 ).json ()#line:239
            if 'status'in O00OO000O0OOOO0O0 :#line:241
                if O00OO000O0OOOO0O0 ['status']==200 :#line:242
                    O00000O00O0OOOOO0 =O00OO000O0OOOO0O0 ['data'][0 ]['crops']#line:243
                    for OO0OO0O0000O0O0OO in O00000O00O0OOOOO0 :#line:244
                        if OO0OO0O0000O0O0OO ['ill_clover_award']:#line:245
                            if float (OO0OO0O0000O0O0OO ['ill_clover_award'])>1 :#line:246
                                if OO0OO0O0000O0O0OO ['is_finish']:#line:247
                                    if not OO0OO0O0000O0O0OO ['is_getit']:#line:248
                                        if O0000O0OOO0OOOOO0 .certification ()!='未实名':#line:249
                                            O0OOO0O0O0000O0OO =f'_award_level={OO0OO0O0000O0O0OO["level"]}_{timi_new()}'#line:250
                                            O00O0O00O00OOO0O0 ={'authorization':O0000O0OOO0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O0O0000O0OO ),'signstring':O0OOO0O0O0000O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:259
                                            O0OO0OO00OOOO000O ={"award_level":OO0OO0O0000O0O0OO ['level']}#line:260
                                            O0O00OOOO000O0OOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00O0O00O00OOO0O0 ,json =O0OO0OO00OOOO000O ).json ()#line:262
                                            if 'status'in O0O00OOOO000O0OOO :#line:263
                                                if O0O00OOOO000O0OOO ['status']==200 :#line:264
                                                    O0OO00OO00O000000 =O0O00OOOO000O0OOO ['data']['ill_clover_award']#line:265
                                                    print (f'【图鉴奖励】:领取{OO0OO0O0000O0O0OO["crop_name"]}成就丨奖励{O0OO00OO00O000000}叶子成功')#line:267
                                                if O0O00OOOO000O0OOO ['status']==500 :#line:268
                                                    print (f'【图鉴奖励】:{O0O00OOOO000O0OOO["message"]}')#line:269
        except Exception as OO0OOO000OO00OOO0 :#line:270
            print (OO0OOO000OO00OOO0 )#line:271
    def watched_ad (OOO0O00OOOO000OOO ):#line:275
        try :#line:276
            OOOOO0O0000O00000 =f'__{timi_new()}'#line:277
            OOO00O0000O00OOO0 ={'authorization':OOO0O00OOOO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O0000O00000 ),'signstring':OOOOO0O0000O00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:286
            O0O000O0OO000OO0O =requests .request ('post',f'{host}/game/watched-ad',headers =OOO00O0000O00OOO0 ).json ()#line:287
            print (O0O000O0OO000OO0O )#line:288
        except Exception as O0O0OO0O0O0OO0OOO :#line:289
            print (O0O0OO0O0O0OO0OOO )#line:290
    def user_ad (O000O0OO0OO0000O0 ):#line:294
        try :#line:295
            O000OOOOO0OO00OOO =f'__{timi_new()}'#line:296
            O0OO00O0OOOO00OO0 ={'authorization':O000O0OO0OO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOO0OO00OOO ),'signstring':O000OOOOO0OO00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:305
            O00OOOO0O0O000O00 =requests .request ('get',f'{host}/user/ad',headers =O0OO00O0OOOO00OO0 ).json ()#line:306
            if 'status'in O00OOOO0O0O000O00 :#line:308
                if O00OOOO0O0O000O00 ['status']==200 :#line:309
                    O0OO00O0O00O00O00 =O00OOOO0O0O000O00 ['data']['max_time']#line:310
                    OO0O0OOO000000OO0 =O00OOOO0O0O000O00 ['data']['watch_time']#line:311
                    OOO0OO0O00O0000O0 =O00OOOO0O0O000O00 ['data']['added_time']#line:312
                    print (f'【获取种子】:获取种子剩余{OOO0OO0O00O0000O0 + O0OO00O0O00O00O00 - OO0O0OOO000000OO0}次丨好友提供:{OOO0OO0O00O0000O0}次')#line:313
                    if OOO0OO0O00O0000O0 +O0OO00O0O00O00O00 -OO0O0OOO000000OO0 >0 :#line:314
                        time .sleep (random .randint (16 ,19 ))#line:315
                        OO0OO0OO0O0OO0O0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OO00O0OOOO00OO0 ).json ()#line:316
                        if 'status'in OO0OO0OO0O0OO0O0O :#line:318
                            if OO0OO0OO0O0OO0O0O ['status']==200 :#line:319
                                O0OOO0000O00000OO =OO0OO0OO0O0OO0O0O ['data']['silver']#line:320
                                print (f'【获取种子】:获得种子:{O0OOO0000O00000OO}')#line:321
                                return True #line:322
                            if OO0OO0OO0O0OO0O0O ['status']==500 :#line:323
                                O0O0O0O000OO00OO0 =OO0OO0OO0O0OO0O0O ['message']#line:324
                                print (f'【获取种子】:{O0O0O0O000OO00OO0}')#line:325
                                return False #line:326
        except Exception as OO0O0O00O00O00O00 :#line:327
            print (OO0O0O00O00O00O00 )#line:328
    def synthetic (O0000OO0OOOOOOOOO ):#line:332
        global id ,g #line:333
        try :#line:334
            OOOOO00O000O00O0O =O0000OO0OOOOOOOOO .level_new ()#line:335
            while True :#line:336
                OO0O00OO0O0O0000O =f'__{timi_new()}'#line:337
                OO0OO00O00O00OO0O ={'authorization':O0000OO0OOOOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OO0O0O0000O ),'signstring':OO0O00OO0O0O0000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:346
                OOOO0000OOO00O00O =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO00O00O00OO0O ).json ()#line:347
                if 'status'in OOOO0000OOO00O00O :#line:349
                    if OOOO0000OOO00O00O ['status']==200 :#line:350
                        O00OO0OO0OOO0O00O =OOOO0000OOO00O00O ['data']['cropList']#line:351
                        OO0O00000OOO0OO00 =OOOO0000OOO00O00O ['data']['gameCoreDataDBid']#line:352
                        O00O0000000000OOO =0 #line:353
                        for OO000OOO0OO00OOO0 in O00OO0OO0OOO0O00O :#line:354
                            if not OO000OOO0OO00OOO0 :#line:355
                                O0000OOO0O0000O0O =f'_crop_id={OO0O00000OOO0OO00}&site={O00O0000000000OOO}_{O0000OO0OOOOOOOOO.time}'#line:356
                                OO0O00OOO00OO00OO ={'authorization':O0000OO0OOOOOOOOO .token ,'timestamp':O0000OO0OOOOOOOOO .time ,'sign':sign (O0000OOO0O0000O0O ),'signstring':O0000OOO0O0000O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:365
                                OOOOOOO00000O0O00 ={"site":O00O0000000000OOO ,"crop_id":OO0O00000OOO0OO00 }#line:366
                                OO0OO000OO000O0OO =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O00OOO00OO00OO ,data =OOOOOOO00000O0O00 ).json ()#line:367
                                time .sleep (random .randint (1 ,3 )/10 )#line:369
                                if 'status'in OO0OO000OO000O0OO :#line:370
                                    if OO0OO000OO000O0OO ['status']==200 :#line:371
                                        if OO0OO000OO000O0OO ['message']=='种子数量不足':#line:372
                                            OOOOO00O000O00O0O =O0000OO0OOOOOOOOO .level_new ()#line:373
                                            print (f'【种植合成】:{OO0OO000OO000O0OO["message"]}')#line:374
                                            if not O0000OO0OOOOOOOOO .user_ad ():#line:375
                                                return False #line:376
                                        print (f'【种植合成】:种植农作物,位置{O00O0000000000OOO}')#line:377
                                    if OO0OO000OO000O0OO ['status']==500 :#line:378
                                        print (f'【种植合成】:{OO0OO000OO000O0OO["message"]}')#line:379
                                        return False #line:380
                            O00O0000000000OOO +=1 #line:381
                        OOO0O00O00OO00OO0 =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO00O00O00OO0O ).json ()#line:382
                        O0O000O0OOOO00O0O =OOO0O00O00OO00OO0 ['data']['cropList']#line:383
                        O0O0OOOO00OO0OO0O =False #line:384
                        for OO000OOO0OO00OOO0 in range (12 ):#line:385
                            id =O0O000O0OOOO00O0O [OO000OOO0OO00OOO0 ]['level']#line:386
                            if float (OOOOO00O000O00O0O )-float (id )>9 :#line:387
                                OO00O0O00O00O0OO0 =f'_site={OO000OOO0OO00OOO0}_{timi_new()}'#line:388
                                OO000O0OOOO0OOOOO ={'accept':'application/json, text/plain, */*','authorization':O0000OO0OOOOOOOOO .token ,'timestamp':timi_new (),'sign':sign (OO00O0O00O00O0OO0 ),'signstring':OO00O0O00O00O0OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:398
                                OO00000OOOOO00O0O ={"site":OO000OOO0OO00OOO0 }#line:399
                                O0OOO0000O0OO0O00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO000O0OOOO0OOOOO ,data =OO00000OOOOO00O0O ).json ()#line:401
                                if 'status'in O0OOO0000O0OO0O00 :#line:402
                                    if O0OOO0000O0OO0O00 ['status']==200 :#line:403
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:404
                            if id !=0 :#line:405
                                for O0O000OO0OOOO00O0 in range (11 ):#line:406
                                    O00OOO0O0O0O0O00O =O0O000OO0OOOO00O0 +1 #line:407
                                    g =O0O000O0OOOO00O0O [O00OOO0O0O0O0O00O ]['level']#line:408
                                    if id ==g :#line:409
                                        OO00OOO0OO0OO000O =O0O000OO0OOOO00O0 +2 #line:410
                                        if OO00OOO0OO0OO000O ==OO000OOO0OO00OOO0 +1 :#line:411
                                            pass #line:412
                                        else :#line:413
                                            OO00O000OO000OO0O =OO000OOO0OO00OOO0 +1 #line:414
                                            time .sleep (random .randint (1 ,3 )/10 )#line:416
                                            OOOOO000OOO0OOO0O =f'_site={OO00O000OO000OO0O - 1}&targetSite={OO00OOO0OO0OO000O - 1}_{timi_new()}'#line:417
                                            OO0OOOO00O0O0OO00 ={'accept':'application/json, text/plain, */*','authorization':O0000OO0OOOOOOOOO .token ,'timestamp':timi_new (),'sign':sign (OOOOO000OOO0OOO0O ),'signstring':OOOOO000OOO0OOO0O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:432
                                            O000OO0O000O000O0 ={"site":int (OO00O000OO000OO0O -1 ),"targetSite":int (OO00OOO0OO0OO000O -1 )}#line:433
                                            OO000OO00O0O00O00 =requests .request ('post',f'{host}/game/crops/move',headers =OO0OOOO00O0O0OO00 ,json =O000OO0O000O000O0 ).json ()#line:435
                                            if 'status'in OO000OO00O0O00O00 :#line:436
                                                if OO000OO00O0O00O00 ['status']==200 :#line:437
                                                    pass #line:438
                                            print ('【种植合成】:',OO00O000OO000OO0O ,OO00OOO0OO0OO000O ,'合成成功')#line:440
                                            O0O0OOOO00OO0OO0O =True #line:441
                                    if O0O0OOOO00OO0OO0O :#line:442
                                        break #line:443
                                if O0O0OOOO00OO0OO0O :#line:444
                                    break #line:445
        except Exception as O0O00O0OOO0OO0OOO :#line:446
            O0000OO0OOOOOOOOO .synthetic ()#line:447
    def level_new (O00O0OOOOOOOO0OOO ):#line:450
        try :#line:451
            O00000O0OOOO00000 =f'__{timi_new()}'#line:452
            O0O00000O0O0OO0O0 ={'authorization':O00O0OOOOOOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0OOOO00000 ),'signstring':O00000O0OOOO00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:461
            O00O0O00O0O00000O =requests .request ('get',f'{host}/user',headers =O0O00000O0O0OO0O0 ).json ()#line:462
            if 'status'in O00O0O00O0O00000O :#line:463
                if O00O0O00O0O00000O ['status']==200 :#line:464
                    return float (O00O0O00O0O00000O ['data']['level'])#line:465
        except Exception as O00O0O0OO0O0000OO :#line:466
            print (O00O0O0OO0O0000OO )#line:467
    def propsraffle (O00OO00000OO00OOO ):#line:470
        try :#line:471
            while True :#line:472
                O00O00O0O000OOO0O =f'__{timi_new()}'#line:473
                O0O0OO0O0000000OO ={'authorization':O00OO00000OO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O000OOO0O ),'signstring':O00O00O0O000OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:482
                OOO0OO0O00O0OO00O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O0OO0O0000000OO ).json ()#line:483
                if 'status'in OOO0OO0O00O0OO00O :#line:485
                    if OOO0OO0O00O0OO00O ['status']==200 :#line:486
                        O00O0O0O0O0O00000 =OOO0OO0O00O0OO00O ['data']['rows']#line:487
                        O00OO0O00O000O0O0 =OOO0OO0O00O0OO00O ['data']['vstate']#line:488
                        if O00O0O0O0O0O00000 ==5 or O00O0O0O0O0O00000 ==6 or O00O0O0O0O0O00000 ==7 :#line:489
                            OO0OO000O00OO00OO =OOO0OO0O00O0OO00O ['data']['silver']#line:490
                            print (f'【转盘抽奖】:获得种子:{OO0OO000O00OO00OO}')#line:491
                        if O00O0O0O0O0O00000 ==1 or O00O0O0O0O0O00000 ==2 or O00O0O0O0O0O00000 ==3 :#line:492
                            O00OO0O000000OO00 =OOO0OO0O00O0OO00O ['data']['clover']#line:493
                            print (f'【转盘抽奖】:获得三叶草:{O00OO0O000000OO00}')#line:494
                        if O00O0O0O0O0O00000 ==4 or O00O0O0O0O0O00000 ==8 :#line:495
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:496
                        if O00O0O0O0O0O00000 =='抽奖次数已用完':#line:500
                            if O00OO0O00O000O0O0 :#line:501
                                O00O00O0O000OOO0O =f'__{timi_new()}'#line:502
                                O0O0OO0O0000000OO ={'authorization':O00OO00000OO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O000OOO0O ),'signstring':O00O00O0O000OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:511
                                O0OOO000O0OO000OO =requests .request ('get',f'{host}/user',headers =O0O0OO0O0000000OO ).json ()#line:512
                                if 'status'in O0OOO000O0OO000OO :#line:513
                                    if O0OOO000O0OO000OO ['status']==200 :#line:514
                                        O00000O0O0O000O00 =O0OOO000O0OO000OO ['data']['level']#line:515
                                        if float (O00000O0O0O000O00 )>39 :#line:516
                                            O00O00O000O0000O0 =random .randint (160 ,190 )/10 #line:517
                                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{O00O00O000O0000O0}秒获取抽奖机会')#line:518
                                            time .sleep (O00O00O000O0000O0 )#line:519
                                            O0OOOOO0OO0O0OO00 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O0O0OO0O0000000OO ).json ()#line:520
                                            if 'status'in O0OOOOO0OO0O0OO00 :#line:522
                                                if O0OOOOO0OO0O0OO00 ['status']==200 :#line:523
                                                    print (f'【转盘抽奖】:{O0OOOOO0OO0O0OO00["message"]}')#line:524
                                                if O0OOOOO0OO0O0OO00 ['status']==500 :#line:525
                                                    print (f'【转盘抽奖】:{O0OOOOO0OO0O0OO00["message"]}')#line:526
                                                    break #line:527
                                            time .sleep (random .randint (10 ,15 )/10 )#line:528
                                        else :#line:529
                                            break #line:530
                            else :#line:531
                                break #line:532
                time .sleep (random .randint (8 ,15 )/10 )#line:533
        except Exception as O0O0000O0OOOO00O0 :#line:534
            print (O0O0000O0OOOO00O0 )#line:535
    def friends_invitation (OO0000O0O00OO0000 ):#line:538
        try :#line:539
            OOO00O00O0OO0OO0O =f'__{timi_new()}'#line:540
            OOOOOOOO0000O0O0O ={'authorization':OO0000O0O00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00O0OO0OO0O ),'signstring':OOO00O00O0OO0OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:549
            OOO00OOOO0000OOO0 =requests .request ('get',f'{host}/friends',headers =OOOOOOOO0000O0O0O ).json ()#line:550
            if 'status'in OOO00OOOO0000OOO0 :#line:551
                if OOO00OOOO0000OOO0 ['status']==200 :#line:552
                    OO00O0O000OOOO0O0 =OOO00OOOO0000OOO0 ['data']['myInviteter']#line:553
                    if OO00O0O000OOOO0O0 :#line:554
                        O0O000OO0000O0OOO =OO00O0O000OOOO0O0 ['user']['nickname']#line:555
                        O00000O00000OOO00 =OO0000O0O00OO0000 .certification ()#line:556
                        print (f'【查邀请人】:我的邀请人:{O0O000OO0000O0OOO}丨实名:{O00000O00000OOO00}')#line:557
                    else :#line:558
                        if OO0000O0O00OO0000 .innerId !='0':#line:559
                            OOO00O00O0OO0OO0O =f'_innerId=1937553_{timi_new()}'#line:560
                            OOOOOOOO0000O0O0O ={'authorization':OO0000O0O00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00O0OO0OO0O ),'signstring':OOO00O00O0OO0OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:569
                            OO0000OOOOOOOO000 ={"innerId":'1937553'}#line:570
                            OO00OO0O000000000 =requests .request ('post',f'{host}/friends/my-invitation',headers =OOOOOOOO0000O0O0O ,data =OO0000OOOOOOOO000 ).json ()#line:572
        except Exception as OO00OO000O0OOO00O :#line:573
            print (OO00OO000O0OOO00O )#line:574
    def add_clover (O00OO0O0O0OO00O0O ):#line:577
        global golden_seed #line:578
        try :#line:579
            OOOOO000000O0O0OO =f'__{timi_new()}'#line:580
            O0O000O00O00O0OO0 ={'authorization':O00OO0O0O0OO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO000000O0O0OO ),'signstring':OOOOO000000O0O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:589
            O0OOOOO00O00OOO00 =requests .request ('get',f'{host}/assets/clovers',headers =O0O000O00O00O0OO0 ).json ()#line:590
            if 'status'in O0OOOOO00O00OOO00 :#line:592
                if O0OOOOO00O00OOO00 ['status']==200 :#line:593
                    OO00000OO00O00OO0 =O0OOOOO00O00OOO00 ['data']['clover']#line:594
                    O0OO00O0O00O000OO =O0OOOOO00O00OOO00 ['data']['used_clover']#line:595
                    O000OOO0O0000O0OO =float (OO00000OO00O00OO0 )-float (O0OO00O0O00O000OO )#line:596
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0OO00O0O00O000OO}')#line:597
                    if O00OO0O0O0OO00O0O .certification ()!='未实名':#line:598
                        if O000OOO0O0000O0OO >1 :#line:599
                            OOOOO000000O0O0OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O000OOO0O0000O0OO)}_{timi_new()}'#line:600
                            O0O000O00O00O0OO0 ={'authorization':O00OO0O0O0OO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO000000O0O0OO ),'signstring':OOOOO000000O0O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:609
                            O00OOO0OOOOO00O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O000OOO0O0000O0OO )}#line:610
                            O0O0000OOO0O0O000 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O000O00O00O0OO0 ,data =O00OOO0OOOOO00O0O ).json ()#line:611
                            if 'status'in O0O0000OOO0O0O000 :#line:613
                                if O0O0000OOO0O0O000 ['status']==200 :#line:614
                                    print (f'【参与抽奖】:添加三叶草:{O0O0000OOO0O0O000["data"]}丨数量:{O000OOO0O0000O0OO}')#line:615
                                if O0O0000OOO0O0O000 ['status']==500 :#line:616
                                    print (f'【参与抽奖】:添加三叶草:{O0O0000OOO0O0O000["message"]}')#line:617
            O0OOO0OOO0O0O00OO =requests .request ('get',f'{host}/lottery',headers =O0O000O00O00O0OO0 ).json ()#line:618
            OOOOO00O000O00OOO =O00OO0O0O0OO00O0O .winning_rewards ()#line:620
            if 'status'in O0OOO0OOO0O0O00OO :#line:621
                if O0OOO0OOO0O0O00OO ['status']==200 :#line:622
                    OOOOO0OO00O00OO0O =O0OOO0OOO0O0O00OO ['data'][0 ]['day_get_gold_quantity']#line:623
                    golden_seed +=float (OOOOO0OO00O00OO0O )#line:624
                    print (f'【参与抽奖】:预计每天中{str(OOOOO0OO00O00OO0O)[:6]}颗金种子丨好友收益:{str(OOOOO00O000O00OOO)[:6]}')#line:625
        except Exception as OOOOOOO0OO0OO00OO :#line:626
            print (OOOOOOO0OO0OO00OO )#line:627
    def energy (OOO0O0O0O0O000OOO ):#line:630
        OOOO0OOO000OOOO0O =f'__{timi_new()}'#line:631
        OO0O0O0O0O000OOOO ={'authorization':OOO0O0O0O0O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO000OOOO0O ),'signstring':OOOO0OOO000OOOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:640
        O00OO00OO0OOOOO00 =requests .request ('get',f'{host}/energy/general',headers =OO0O0O0O0O000OOOO ).json ()#line:641
        if 'status'in O00OO00OO0OOOOO00 :#line:643
            if O00OO00OO0OOOOO00 ['status']==200 :#line:644
                OO0OO0000OO00O00O =O00OO00OO0OOOOO00 ['data']['ordinary_water']#line:645
                OOOOO0O00OOOO000O =O00OO00OO0OOOOO00 ['data']['ordinary_fertilizer']#line:646
                print (f'【我的营养】:肥料:{str(OOOOO0O00OOOO000O).split(".")[0]}丨水滴:{str(OO0OO0000OO00O00O).split(".")[0]}')#line:647
                if float (OOOOO0O00OOOO000O )<96 :#line:648
                    time .sleep (random .randint (160 ,180 )/10 )#line:649
                    O0OOOOO00O0O00O0O =99 -float (OOOOO0O00OOOO000O )#line:650
                    OO0O0O0O0OOO00OO0 ={"fertilizer":str (O0OOOOO00O0O00O0O ).split ('.')[0 ]}#line:651
                    OO00OO00000O0OOO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0O0O0O0O000OOOO ).json ()#line:652
                    if 'status'in OO00OO00000O0OOO0 :#line:654
                        if OO00OO00000O0OOO0 ['status']==200 :#line:655
                            print (f'【购买肥料】:看广告获取肥料:{OO00OO00000O0OOO0["message"]}')#line:656
                if float (OO0OO0000OO00O00O )<880 :#line:657
                    time .sleep (random .randint (160 ,180 )/10 )#line:658
                    O0OOOO0O00O0OOOOO =999 -float (OO0OO0000OO00O00O )#line:659
                    O0O0OOO00O00OO000 ={"water":str (O0OOOO0O00O0OOOOO ).split ('.')[0 ]}#line:660
                    O000OO00OOOOOO0O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0O0O0O0O000OOOO ).json ()#line:661
                    if 'status'in O000OO00OOOOOO0O0 :#line:663
                        if O000OO00OOOOOO0O0 ['status']==200 :#line:664
                            print (f'【购买水滴】:看广告获取水滴:{O000OO00OOOOOO0O0["message"]}')#line:665
def version_of_the_validation ():#line:669
    return str ((69 -56 )/10 )#line:670
def gitee_validation ():#line:673
    try :#line:674
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:675
    except :#line:676
        sys .exit (0 )#line:677
def update_the_validation ():#line:681
    try :#line:682
        O000OOO00O0O0O0O0 =gitee_validation ()#line:683
        if version_of_the_validation ()<O000OOO00O0O0O0O0 ['CityEarth']['edition']:#line:684
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOO00O0O0O0O0["CityEarth"]["edition"]}   ❌')#line:685
            print (f'更新内容=>>{O000OOO00O0O0O0O0["CityEarth"]["content"]}   👍')#line:686
        else :#line:687
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOO00O0O0O0O0["CityEarth"]["edition"]}   ✅')#line:688
            print (f'更新内容=>> {O000OOO00O0O0O0O0["CityEarth"]["content"]}   👍')#line:689
    except Exception as O0O00OO0O000OO00O :#line:690
        print (O0O00OO0O000OO00O )#line:691
def os_qinglong ():#line:694
    if application in os .environ :#line:695
        O0OOO00O0OOOO0O0O =os .environ [application ].split ('\n')#line:696
        if len (O0OOO00O0OOOO0O0O )>0 :#line:697
            return O0OOO00O0OOOO0O0O #line:698
        else :#line:699
            print (f"{application}变量未启用")#line:700
            print ('脚本退出')#line:701
            sys .exit (1 )#line:702
    else :#line:703
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:705
        return os_built ()#line:706
def os_built ():#line:709
    if token :#line:710
        O00O00OOOO00OO0O0 =token .split ('\n')#line:711
        if len (O00O00OOOO00OO0O0 )>0 :#line:712
            return O00O00OOOO00OO0O0 #line:713
    else :#line:714
        print (f"内置变量为空")#line:715
        print ('脚本结束')#line:716
        sys .exit (0 )#line:717
if __name__ =='__main__':#line:720
    start ()#line:721
