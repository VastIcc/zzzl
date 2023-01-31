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
        O0O0O0O00O0O0O0O0 =os_qinglong ()#line:7
        print (f"==========共找到{len(O0O0O0O00O0O0O0O0)}个账号==========")#line:8
        for OOO0000OOO00O0OO0 in O0O0O0O00O0O0O0O0 :#line:9
            print (f"------------正在执行第{O0O0O0O00O0O0O0O0.index(OOO0000OOO00O0OO0) + 1}个账号------------")#line:10
            O0OO0000O0OOO0O0O =CityEarth (OOO0000OOO00O0OO0 )#line:11
            def OO0O0000O0OOO0O0O ():#line:13
                if O0OO0000O0OOO0O0O .base_info ():#line:15
                    O0OO0000O0OOO0O0O .game_map ()#line:19
                    O0OO0000O0OOO0O0O .friends_invitation ()#line:21
                    O0OO0000O0OOO0O0O .add_clover ()#line:23
                    O0OO0000O0OOO0O0O .energy ()#line:25
                    O0OO0000O0OOO0O0O .propsraffle ()#line:27
                    O0OO0000O0OOO0O0O .synthetic ()#line:29
                    O0OO0000O0OOO0O0O .crops_illustrated ()#line:31
                    O0OO0000O0OOO0O0O .give_gold ()#line:33
                else :#line:34
                    print ('token失效')#line:35
            OO000O0OOOO000O00 =threading .Thread (target =OO0O0000O0OOO0O0O )#line:37
            OO000O0OOOO000O00 .start ()#line:38
            time .sleep (time_xx )#line:39
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:41
        time .sleep (3 )#line:42
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:43
    except Exception as OOOOO0O0OO00OO0O0 :#line:44
        print (OOOOO0O0OO00OO0O0 )#line:45
def sign (O0O00O00000O00OOO ):#line:48
    O0O00OOO0OOO0O00O =hashlib .md5 (O0O00O00000O00OOO .encode ()).hexdigest ()#line:49
    OO00O0OO0O00O0OOO ="scsc%^&*"+O0O00OOO0OOO0O00O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:50
    O00OOOOOO000O0O00 =hashlib .md5 (OO00O0OO0O00O0OOO .encode ()).hexdigest ()#line:51
    return O00OOOOOO000O0O00 #line:52
def timi_new ():#line:55
    return str (int (time .time ()*1000 ))#line:56
class CityEarth :#line:58
    def __init__ (OO0O00OOO0OO00O0O ,O000OO0OOOO0OOO00 ):#line:60
        try :#line:61
            OO0O00OOO0OO00O0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:62
            OO0O00OOO0OO00O0O .token =O000OO0OOOO0OOO00 .split ('&')[0 ]#line:63
            OO0O00OOO0OO00O0O .innerId =O000OO0OOOO0OOO00 .split ('&')[1 ]#line:64
            OO0O00OOO0OO00O0O .doneeNo =O000OO0OOOO0OOO00 .split ('&')[2 ]#line:65
        except :#line:66
            print ('变量格式错误')#line:67
    def base_info (O00OOO00OOOO00OO0 ):#line:70
        try :#line:71
            OOOO0O000OO0O00O0 =f'__{timi_new()}'#line:72
            O0O0O000OOO0OO0OO ={'authorization':O00OOO00OOOO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O000OO0O00O0 ),'signstring':OOOO0O000OO0O00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:81
            OOO00O000O0OOOOOO =requests .request ('get',f'{host}/user',headers =O0O0O000OOO0OO0OO ).json ()#line:82
            if 'status'in OOO00O000O0OOOOOO :#line:84
                if OOO00O000O0OOOOOO ['status']==200 :#line:85
                    OOO00O0O0O00O0O00 =OOO00O000O0OOOOOO ['data']['nickname']#line:86
                    OO0O00OO0OO0OO000 =OOO00O000O0OOOOOO ['data']['inner_id']#line:87
                    O0O0OOO000OOO000O =OOO00O000O0OOOOOO ['data']['assets']['gold']#line:88
                    O000O00O000000O00 =OOO00O000O0OOOOOO ['data']['level']#line:89
                    print (f'【账号信息】:昵称:{OOO00O0O0O00O0O00[:5]}丨ID:{OO0O00OO0OO0OO000}丨等级:{O000O00O000000O00}丨种子:{str(O0O0OOO000OOO000O).split(".")[0]}')#line:90
                if OOO00O000O0OOOOOO ['status']==401 :#line:91
                    return False #line:92
                if OOO00O000O0OOOOOO ['status']==500 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as O00OO00O0O00O0O0O :#line:96
            print (O00OO00O0O00O0O0O )#line:97
    def game_map (OOO00O000000OO0OO ):#line:100
        try :#line:101
            OOO0OOOOOO00OO0OO =f'__{timi_new()}'#line:102
            OOOOOOOO00O00O0O0 ={'authorization':OOO00O000000OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOOO00OO0OO ),'signstring':OOO0OOOOOO00OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:111
            OO0OO0000OOO0O00O =requests .request ('get',f'{host}/game/map',headers =OOOOOOOO00O00O0O0 ).json ()#line:112
            if 'status'in OO0OO0000OOO0O00O :#line:114
                if OO0OO0000OOO0O00O ['status']==200 :#line:115
                    for OOO0O0OO0OO00000O in OO0OO0000OOO0O00O ['data']['list'][0 ]['crops']:#line:116
                        O00OO000O000OOOO0 =OOO0O0OO0OO00000O ['level']#line:118
                        if O00OO000O000OOOO0 ==41 :#line:119
                            O00000O0OOOO0OO00 =OOO0O0OO0OO00000O ['crop_name']#line:120
                            OO000O00O0O0O0O00 =OOO0O0OO0OO00000O ['count']#line:121
                            if OO000O00O0O0O0O00 >0 :#line:122
                                print (f'【农业资产】:{O00000O0OOOO0OO00}丨数量:{OO000O00O0O0O0O00}')#line:123
        except Exception as OOOO0OO0O0O0OOO00 :#line:124
            print (OOOO0OO0O0O0OOO00 )#line:125
    def give_gold (OOO0OOO0O00O0OO0O ):#line:129
        try :#line:130
            OO00O000OO000OO0O =f'__{timi_new()}'#line:131
            OOO0OOO0000OO000O ={'authorization':OOO0OOO0O00O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000OO000OO0O ),'signstring':OO00O000OO000OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:140
            O0OOOO0O0000O00OO =requests .request ('get',f'{host}/user',headers =OOO0OOO0000OO000O ).json ()#line:141
            if 'status'in O0OOOO0O0000O00OO :#line:142
                if O0OOOO0O0000O00OO ['status']==200 :#line:143
                    if float (OOO0OOO0O00O0OO0O .doneeNo )!=0 :#line:144
                        OOO00OO0O0000OOOO =O0OOOO0O0000O00OO ['data']['assets']['gold']#line:145
                        if float (OOO00OO0O0000OOOO )>float (OOO0OOO0O00O0OO0O .innerId ):#line:146
                            OO00O0OOO00OO00OO =int (float (OOO00OO0O0000OOOO )/1.1 )#line:147
                            OO00O000OO000OO0O =f'_doneeNo={OOO0OOO0O00O0OO0O.doneeNo}&quantity={OO00O0OOO00OO00OO}_{timi_new()}'#line:148
                            OOO0OOO0000OO000O ={'authorization':OOO0OOO0O00O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000OO000OO0O ),'signstring':OO00O000OO000OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:157
                            O000OO0O0O00O00OO ={"quantity":OO00O0OOO00OO00OO ,"doneeNo":OOO0OOO0O00O0OO0O .doneeNo }#line:161
                            OO00O0OOOOOOOO0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0OOO0000OO000O ,data =O000OO0O0O00O00OO ).json ()#line:162
                            if 'status'in OO00O0OOOOOOOO0O0 :#line:164
                                if OO00O0OOOOOOOO0O0 ['status']==200 :#line:165
                                    if OO00O0OOOOOOOO0O0 ['data']:#line:166
                                        print (f'【赠送种子】:赠送{OO00O0OOO00OO00OO}种子给{OOO0OOO0O00O0OO0O.doneeNo}成功')#line:167
                    else :#line:168
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:169
        except Exception as OOOO000000O0O0OOO :#line:170
            print (OOOO000000O0O0OOO )#line:171
    def winning_rewards (OOO0O00O0OO00OOOO ):#line:175
        try :#line:176
            OO0000O000000OOO0 =f'__{timi_new()}'#line:177
            O0OO0O0OOOO0OO0OO ={'authorization':OOO0O00O0OO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O000000OOO0 ),'signstring':OO0000O000000OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
            OOO00O000O0O0O000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OO0O0OOOO0OO0OO ).json ()#line:187
            if 'status'in OOO00O000O0O0O000 :#line:189
                if OOO00O000O0O0O000 ['status']==200 :#line:190
                    if OOO00O000O0O0O000 ['data']['amount']:#line:191
                        OO0O000O000000O0O =OOO00O000O0O0O000 ['data']['amount']['gold']#line:192
                        return OO0O000O000000O0O #line:193
                    else :#line:194
                        return 0 #line:195
        except Exception as OOO00OO0OO0O0OO00 :#line:196
            print (OOO00OO0OO0O0OO00 )#line:197
    def certification (O0000O00O0OO00O0O ):#line:201
        try :#line:202
            OO00O00O000O00OOO =f'__{timi_new()}'#line:203
            OOOOOOO0O000O0OO0 ={'authorization':O0000O00O0OO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00O000O00OOO ),'signstring':OO00O00O000O00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:212
            O000OOO0OOO00OO00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOOOOOO0O000O0OO0 ).json ()#line:213
            if 'status'in O000OOO0OOO00OO00 :#line:215
                if O000OOO0OOO00OO00 ['status']==200 :#line:216
                    if O000OOO0OOO00OO00 ['data']['result']:#line:217
                        O0OO0OO0OOO0OOO0O =O000OOO0OOO00OO00 ['data']['nick_name']#line:218
                        return O0OO0OO0OOO0OOO0O #line:219
                    else :#line:220
                        return '未实名'#line:221
        except Exception as OO00O00000OOO000O :#line:222
            print (OO00O00000OOO000O )#line:223
    def crops_illustrated (OO0O0OO0OO0O00OOO ):#line:227
        try :#line:228
            OOO000OOOOO0000O0 =f'__{timi_new()}'#line:229
            OOO0O00O000O00O00 ={'authorization':OO0O0OO0OO0O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOOOO0000O0 ),'signstring':OOO000OOOOO0000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:238
            O00OO0O0O00OO0000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO0O00O000O00O00 ).json ()#line:239
            if 'status'in O00OO0O0O00OO0000 :#line:241
                if O00OO0O0O00OO0000 ['status']==200 :#line:242
                    OO000O00OOO00OOO0 =O00OO0O0O00OO0000 ['data'][0 ]['crops']#line:243
                    for O000000OO0O00OOOO in OO000O00OOO00OOO0 :#line:244
                        if O000000OO0O00OOOO ['ill_clover_award']:#line:245
                            if float (O000000OO0O00OOOO ['ill_clover_award'])>1 :#line:246
                                if O000000OO0O00OOOO ['is_finish']:#line:247
                                    if not O000000OO0O00OOOO ['is_getit']:#line:248
                                        if OO0O0OO0OO0O00OOO .certification ()!='未实名':#line:249
                                            OOO000OOOOO0000O0 =f'_award_level={O000000OO0O00OOOO["level"]}_{timi_new()}'#line:250
                                            OOO0O00O000O00O00 ={'authorization':OO0O0OO0OO0O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOOOO0000O0 ),'signstring':OOO000OOOOO0000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:259
                                            OOO00OO0O00O0OOOO ={"award_level":O000000OO0O00OOOO ['level']}#line:260
                                            O0OO0000OO000O0OO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO0O00O000O00O00 ,json =OOO00OO0O00O0OOOO ).json ()#line:262
                                            if 'status'in O0OO0000OO000O0OO :#line:263
                                                if O0OO0000OO000O0OO ['status']==200 :#line:264
                                                    OO0O0O00OO000OOO0 =O0OO0000OO000O0OO ['data']['ill_clover_award']#line:265
                                                    print (f'【图鉴奖励】:领取{O000000OO0O00OOOO["crop_name"]}成就丨奖励{OO0O0O00OO000OOO0}叶子成功')#line:267
                                                if O0OO0000OO000O0OO ['status']==500 :#line:268
                                                    print (f'【图鉴奖励】:{O0OO0000OO000O0OO["message"]}')#line:269
        except Exception as O000O000OO00OO00O :#line:270
            print (O000O000OO00OO00O )#line:271
    def watched_ad (O0OO000000O0O000O ):#line:275
        try :#line:276
            OO0O0OO0OO00OO00O =f'__{timi_new()}'#line:277
            O0O0OO0OO000OOO00 ={'authorization':O0OO000000O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO0OO00OO00O ),'signstring':OO0O0OO0OO00OO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:286
            O0O0O000OO000OOO0 =requests .request ('post',f'{host}/game/watched-ad',headers =O0O0OO0OO000OOO00 ).json ()#line:287
            print (O0O0O000OO000OOO0 )#line:288
        except Exception as OO000OO000O00OO0O :#line:289
            print (OO000OO000O00OO0O )#line:290
    def user_ad (O00OOOOOOOOO0O0O0 ):#line:294
        try :#line:295
            OOO0OO000OO0OOOOO =f'__{timi_new()}'#line:296
            O0OO0O0O000O00000 ={'authorization':O00OOOOOOOOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO000OO0OOOOO ),'signstring':OOO0OO000OO0OOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:305
            OO00O00O0OOOO0OOO =requests .request ('get',f'{host}/user/ad',headers =O0OO0O0O000O00000 ).json ()#line:306
            if 'status'in OO00O00O0OOOO0OOO :#line:308
                if OO00O00O0OOOO0OOO ['status']==200 :#line:309
                    O0OOOOO00O0O0000O =OO00O00O0OOOO0OOO ['data']['max_time']#line:310
                    O0OOO00O00OO0O000 =OO00O00O0OOOO0OOO ['data']['watch_time']#line:311
                    OOO000OO0000OOO00 =OO00O00O0OOOO0OOO ['data']['added_time']#line:312
                    print (f'【获取种子】:获取种子剩余{OOO000OO0000OOO00 + O0OOOOO00O0O0000O - O0OOO00O00OO0O000}次丨好友提供:{OOO000OO0000OOO00}次')#line:313
                    if OOO000OO0000OOO00 +O0OOOOO00O0O0000O -O0OOO00O00OO0O000 >0 :#line:314
                        time .sleep (random .randint (16 ,19 ))#line:315
                        O00O0OO0OO0OOOOOO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OO0O0O000O00000 ).json ()#line:316
                        if 'status'in O00O0OO0OO0OOOOOO :#line:318
                            if O00O0OO0OO0OOOOOO ['status']==200 :#line:319
                                OOOOO0O0O0000O0O0 =O00O0OO0OO0OOOOOO ['data']['silver']#line:320
                                print (f'【获取种子】:获得种子:{OOOOO0O0O0000O0O0}')#line:321
                                return True #line:322
                            if O00O0OO0OO0OOOOOO ['status']==500 :#line:323
                                OOO00O0O0OO00000O =O00O0OO0OO0OOOOOO ['message']#line:324
                                print (f'【获取种子】:{OOO00O0O0OO00000O}')#line:325
                                return False #line:326
        except Exception as O0OOOOO00000OOOO0 :#line:327
            print (O0OOOOO00000OOOO0 )#line:328
    def synthetic (OO0O0O000OO000000 ):#line:332
        global id ,g #line:333
        try :#line:334
            OOO000O0OO00OO0OO =OO0O0O000OO000000 .level_new ()#line:335
            while True :#line:336
                O00O00O000O00O00O =f'__{timi_new()}'#line:337
                O000OO0O0OO0O0O00 ={'authorization':OO0O0O000OO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O000O00O00O ),'signstring':O00O00O000O00O00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:346
                OOOO0OOOO00O00000 =requests .request ('get',f'{host}/game/getAllData',headers =O000OO0O0OO0O0O00 ).json ()#line:347
                if 'status'in OOOO0OOOO00O00000 :#line:349
                    if OOOO0OOOO00O00000 ['status']==200 :#line:350
                        O00000OOOOO0O0OOO =OOOO0OOOO00O00000 ['data']['cropList']#line:351
                        O000OO0OO00O0O0O0 =OOOO0OOOO00O00000 ['data']['gameCoreDataDBid']#line:352
                        O00O00O0OO0OOO0OO =0 #line:353
                        for OO0OO0OOOO0OOOO00 in O00000OOOOO0O0OOO :#line:354
                            if not OO0OO0OOOO0OOOO00 :#line:355
                                OO00O00O0OO0O0O0O =f'_crop_id={O000OO0OO00O0O0O0}&site={O00O00O0OO0OOO0OO}_{OO0O0O000OO000000.time}'#line:356
                                OO0O0OO000000OO00 ={'authorization':OO0O0O000OO000000 .token ,'timestamp':OO0O0O000OO000000 .time ,'sign':sign (OO00O00O0OO0O0O0O ),'signstring':OO00O00O0OO0O0O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:365
                                OOOO0O0O00000OOOO ={"site":O00O00O0OO0OOO0OO ,"crop_id":O000OO0OO00O0O0O0 }#line:366
                                OO0O000OOOO00OO00 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O0OO000000OO00 ,data =OOOO0O0O00000OOOO ).json ()#line:367
                                time .sleep (random .randint (1 ,3 )/10 )#line:369
                                if 'status'in OO0O000OOOO00OO00 :#line:370
                                    if OO0O000OOOO00OO00 ['status']==200 :#line:371
                                        if OO0O000OOOO00OO00 ['message']=='种子数量不足':#line:372
                                            OOO000O0OO00OO0OO =OO0O0O000OO000000 .level_new ()#line:373
                                            print (f'【种植合成】:{OO0O000OOOO00OO00["message"]}')#line:374
                                            if not OO0O0O000OO000000 .user_ad ():#line:375
                                                return False #line:376
                                        print (f'【种植合成】:种植农作物,位置{O00O00O0OO0OOO0OO}')#line:377
                                    if OO0O000OOOO00OO00 ['status']==500 :#line:378
                                        print (f'【种植合成】:{OO0O000OOOO00OO00["message"]}')#line:379
                                        return False #line:380
                            O00O00O0OO0OOO0OO +=1 #line:381
                        OO0OOO00OO00OOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O000OO0O0OO0O0O00 ).json ()#line:382
                        OO0O0000000OO00OO =OO0OOO00OO00OOOO0 ['data']['cropList']#line:383
                        O00O00O0000OO0OOO =False #line:384
                        for OO0OO0OOOO0OOOO00 in range (12 ):#line:385
                            id =OO0O0000000OO00OO [OO0OO0OOOO0OOOO00 ]['level']#line:386
                            if float (OOO000O0OO00OO0OO )-float (id )>9 :#line:387
                                O0O000000000O0OOO =f'_site={OO0OO0OOOO0OOOO00}_{timi_new()}'#line:388
                                O0O0O000O0O00OO00 ={'accept':'application/json, text/plain, */*','authorization':OO0O0O000OO000000 .token ,'timestamp':timi_new (),'sign':sign (O0O000000000O0OOO ),'signstring':O0O000000000O0OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:398
                                O00OOOO0OO0000O0O ={"site":OO0OO0OOOO0OOOO00 }#line:399
                                O00O0O0000O00O00O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O0O000O0O00OO00 ,data =O00OOOO0OO0000O0O ).json ()#line:401
                                if 'status'in O00O0O0000O00O00O :#line:402
                                    if O00O0O0000O00O00O ['status']==200 :#line:403
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:404
                            if id !=0 :#line:405
                                for O0O0O000OO0OO0O0O in range (11 ):#line:406
                                    O0O0O00OO0OOOO0OO =O0O0O000OO0OO0O0O +1 #line:407
                                    g =OO0O0000000OO00OO [O0O0O00OO0OOOO0OO ]['level']#line:408
                                    if id ==g :#line:409
                                        OOOOO000O0O00OOOO =O0O0O000OO0OO0O0O +2 #line:410
                                        if OOOOO000O0O00OOOO ==OO0OO0OOOO0OOOO00 +1 :#line:411
                                            pass #line:412
                                        else :#line:413
                                            OOO0OOOOOO0OOO0O0 =OO0OO0OOOO0OOOO00 +1 #line:414
                                            time .sleep (random .randint (1 ,3 )/10 )#line:416
                                            OOOOO000O0OO00OO0 =f'_site={OOO0OOOOOO0OOO0O0 - 1}&targetSite={OOOOO000O0O00OOOO - 1}_{timi_new()}'#line:417
                                            OOOO0OO0O00O0000O ={'accept':'application/json, text/plain, */*','authorization':OO0O0O000OO000000 .token ,'timestamp':timi_new (),'sign':sign (OOOOO000O0OO00OO0 ),'signstring':OOOOO000O0OO00OO0 ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:432
                                            O0OOO00O0O0OO00OO ={"site":int (OOO0OOOOOO0OOO0O0 -1 ),"targetSite":int (OOOOO000O0O00OOOO -1 )}#line:433
                                            OO00OO0OOOOO0000O =requests .request ('post',f'{host}/game/crops/move',headers =OOOO0OO0O00O0000O ,json =O0OOO00O0O0OO00OO ).json ()#line:435
                                            if 'status'in OO00OO0OOOOO0000O :#line:436
                                                if OO00OO0OOOOO0000O ['status']==200 :#line:437
                                                    pass #line:438
                                            print ('【种植合成】:',OOO0OOOOOO0OOO0O0 ,OOOOO000O0O00OOOO ,'合成成功')#line:440
                                            O00O00O0000OO0OOO =True #line:441
                                    if O00O00O0000OO0OOO :#line:442
                                        break #line:443
                                if O00O00O0000OO0OOO :#line:444
                                    break #line:445
        except Exception as OO00O0OO00000O000 :#line:446
            OO0O0O000OO000000 .synthetic ()#line:447
    def level_new (OO0O0O000O00000O0 ):#line:450
        try :#line:451
            O0OOO00O0OOOOOOOO =f'__{timi_new()}'#line:452
            OO0O0OO00000OOOOO ={'authorization':OO0O0O000O00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0OOOOOOOO ),'signstring':O0OOO00O0OOOOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:461
            OO0O0O0OO00OOOO00 =requests .request ('get',f'{host}/user',headers =OO0O0OO00000OOOOO ).json ()#line:462
            if 'status'in OO0O0O0OO00OOOO00 :#line:463
                if OO0O0O0OO00OOOO00 ['status']==200 :#line:464
                    return float (OO0O0O0OO00OOOO00 ['data']['level'])#line:465
        except Exception as OO0O0O0OO0O0000OO :#line:466
            print (OO0O0O0OO0O0000OO )#line:467
    def propsraffle (O0000OO000OO0O00O ):#line:470
        try :#line:471
            while True :#line:472
                O00OOO0000000O0OO =f'__{timi_new()}'#line:473
                O0O0O0OOOOO0OO00O ={'authorization':O0000OO000OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0000000O0OO ),'signstring':O00OOO0000000O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:482
                OO0O0O00OOO0000O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O0O0OOOOO0OO00O ).json ()#line:483
                if 'status'in OO0O0O00OOO0000O0 :#line:485
                    if OO0O0O00OOO0000O0 ['status']==200 :#line:486
                        OOO0OOO0O0O00OOOO =OO0O0O00OOO0000O0 ['data']['rows']#line:487
                        OO00OOO00OOOOOO0O =OO0O0O00OOO0000O0 ['data']['vstate']#line:488
                        if OOO0OOO0O0O00OOOO ==5 or OOO0OOO0O0O00OOOO ==6 or OOO0OOO0O0O00OOOO ==7 :#line:489
                            O0O0000O00OO00000 =OO0O0O00OOO0000O0 ['data']['silver']#line:490
                            print (f'【转盘抽奖】:获得种子:{O0O0000O00OO00000}')#line:491
                        if OOO0OOO0O0O00OOOO ==1 or OOO0OOO0O0O00OOOO ==2 or OOO0OOO0O0O00OOOO ==3 :#line:492
                            O0O0OOOO00O0OOO0O =OO0O0O00OOO0000O0 ['data']['clover']#line:493
                            print (f'【转盘抽奖】:获得三叶草:{O0O0OOOO00O0OOO0O}')#line:494
                        if OOO0OOO0O0O00OOOO ==4 or OOO0OOO0O0O00OOOO ==8 :#line:495
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:496
                        if OOO0OOO0O0O00OOOO =='抽奖次数已用完':#line:500
                            if OO00OOO00OOOOOO0O :#line:501
                                O00OOO0000000O0OO =f'__{timi_new()}'#line:502
                                O0O0O0OOOOO0OO00O ={'authorization':O0000OO000OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0000000O0OO ),'signstring':O00OOO0000000O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:511
                                O0OOO0OOO00OOO0OO =requests .request ('get',f'{host}/user',headers =O0O0O0OOOOO0OO00O ).json ()#line:512
                                if 'status'in O0OOO0OOO00OOO0OO :#line:513
                                    if O0OOO0OOO00OOO0OO ['status']==200 :#line:514
                                        OOOOO0O0O000O000O =O0OOO0OOO00OOO0OO ['data']['level']#line:515
                                        if float (OOOOO0O0O000O000O )>39 :#line:516
                                            O00O0000OO00O0OOO =random .randint (160 ,190 )/10 #line:517
                                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{O00O0000OO00O0OOO}秒获取抽奖机会')#line:518
                                            time .sleep (O00O0000OO00O0OOO )#line:519
                                            O0O0OOO0O000OO0OO =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O0O0O0OOOOO0OO00O ).json ()#line:520
                                            if 'status'in O0O0OOO0O000OO0OO :#line:522
                                                if O0O0OOO0O000OO0OO ['status']==200 :#line:523
                                                    print (f'【转盘抽奖】:{O0O0OOO0O000OO0OO["message"]}')#line:524
                                                if O0O0OOO0O000OO0OO ['status']==500 :#line:525
                                                    print (f'【转盘抽奖】:{O0O0OOO0O000OO0OO["message"]}')#line:526
                                                    break #line:527
                                            time .sleep (random .randint (10 ,15 )/10 )#line:528
                                        else :#line:529
                                            break #line:530
                            else :#line:531
                                break #line:532
                time .sleep (random .randint (8 ,15 )/10 )#line:533
        except Exception as OO0OO00O00O000OO0 :#line:534
            print (OO0OO00O00O000OO0 )#line:535
    def friends_invitation (O0O0O0O000OO0O0O0 ):#line:538
        try :#line:539
            O00O0OOOO0O0000O0 =f'__{timi_new()}'#line:540
            OOO0OOO0000O0O00O ={'authorization':O0O0O0O000OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOOO0O0000O0 ),'signstring':O00O0OOOO0O0000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:549
            OOOO0O0O00O0000OO =requests .request ('get',f'{host}/friends',headers =OOO0OOO0000O0O00O ).json ()#line:550
            if 'status'in OOOO0O0O00O0000OO :#line:551
                if OOOO0O0O00O0000OO ['status']==200 :#line:552
                    OOOOOO0OO00OO0OOO =OOOO0O0O00O0000OO ['data']['myInviteter']#line:553
                    if OOOOOO0OO00OO0OOO :#line:554
                        OO000OO0O0O00O000 =OOOOOO0OO00OO0OOO ['user']['nickname']#line:555
                        OO00O00000O000000 =O0O0O0O000OO0O0O0 .certification ()#line:556
                        print (f'【查邀请人】:我的邀请人:{OO000OO0O0O00O000}丨实名:{OO00O00000O000000}')#line:557
                    else :#line:558
                        if O0O0O0O000OO0O0O0 .innerId !='0':#line:559
                            O00O0OOOO0O0000O0 =f'_innerId=1937553_{timi_new()}'#line:560
                            OOO0OOO0000O0O00O ={'authorization':O0O0O0O000OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOOO0O0000O0 ),'signstring':O00O0OOOO0O0000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:569
                            O0O00O0000O000000 ={"innerId":'1937553'}#line:570
                            OOOO000O0OO000OO0 =requests .request ('post',f'{host}/friends/my-invitation',headers =OOO0OOO0000O0O00O ,data =O0O00O0000O000000 ).json ()#line:572
        except Exception as O000O0O0OO0000O00 :#line:573
            print (O000O0O0OO0000O00 )#line:574
    def add_clover (OOO0O0O0OO0OO00OO ):#line:577
        global golden_seed #line:578
        try :#line:579
            O00000O0O0OOO000O =f'__{timi_new()}'#line:580
            OO000OOO00O0O0000 ={'authorization':OOO0O0O0OO0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0O0OOO000O ),'signstring':O00000O0O0OOO000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:589
            O0OOO000O0OO000OO =requests .request ('get',f'{host}/assets/clovers',headers =OO000OOO00O0O0000 ).json ()#line:590
            if 'status'in O0OOO000O0OO000OO :#line:592
                if O0OOO000O0OO000OO ['status']==200 :#line:593
                    OO00O0O0OOO0OOOOO =O0OOO000O0OO000OO ['data']['clover']#line:594
                    O00OOOO00000OOO00 =O0OOO000O0OO000OO ['data']['used_clover']#line:595
                    OO000000OOO00O000 =float (OO00O0O0OOO0OOOOO )-float (O00OOOO00000OOO00 )#line:596
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O00OOOO00000OOO00}')#line:597
                    if OOO0O0O0OO0OO00OO .certification ()!='未实名':#line:598
                        if OO000000OOO00O000 >1 :#line:599
                            O00000O0O0OOO000O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO000000OOO00O000)}_{timi_new()}'#line:600
                            OO000OOO00O0O0000 ={'authorization':OOO0O0O0OO0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0O0OOO000O ),'signstring':O00000O0O0OOO000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:609
                            OO000000OOOO0OO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO000000OOO00O000 )}#line:610
                            OO00O00O0OO0OO0O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO000OOO00O0O0000 ,data =OO000000OOOO0OO00 ).json ()#line:611
                            if 'status'in OO00O00O0OO0OO0O0 :#line:613
                                if OO00O00O0OO0OO0O0 ['status']==200 :#line:614
                                    print (f'【参与抽奖】:添加三叶草:{OO00O00O0OO0OO0O0["data"]}丨数量:{OO000000OOO00O000}')#line:615
                                if OO00O00O0OO0OO0O0 ['status']==500 :#line:616
                                    print (f'【参与抽奖】:添加三叶草:{OO00O00O0OO0OO0O0["message"]}')#line:617
            O0OO0000000OOOO00 =requests .request ('get',f'{host}/lottery',headers =OO000OOO00O0O0000 ).json ()#line:618
            OOO00OOOOO0OO0OO0 =OOO0O0O0OO0OO00OO .winning_rewards ()#line:620
            if 'status'in O0OO0000000OOOO00 :#line:621
                if O0OO0000000OOOO00 ['status']==200 :#line:622
                    O0000O0O00O0000OO =O0OO0000000OOOO00 ['data'][0 ]['day_get_gold_quantity']#line:623
                    golden_seed +=float (O0000O0O00O0000OO )#line:624
                    print (f'【参与抽奖】:预计每天中{str(O0000O0O00O0000OO)[:6]}颗金种子丨好友收益:{str(OOO00OOOOO0OO0OO0)[:6]}')#line:625
        except Exception as OOO00OO0OOOOO00OO :#line:626
            print (OOO00OO0OOOOO00OO )#line:627
    def energy (O0OO00O0OOO00O00O ):#line:630
        O00O0000O00O0O00O =f'__{timi_new()}'#line:631
        OO000O00O00OO0O0O ={'authorization':O0OO00O0OOO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0000O00O0O00O ),'signstring':O00O0000O00O0O00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:640
        O000OOOOOOOO00OO0 =requests .request ('get',f'{host}/energy/general',headers =OO000O00O00OO0O0O ).json ()#line:641
        if 'status'in O000OOOOOOOO00OO0 :#line:643
            if O000OOOOOOOO00OO0 ['status']==200 :#line:644
                O00O000OOO0OOO000 =O000OOOOOOOO00OO0 ['data']['ordinary_water']#line:645
                O0OOO0O00OO0000O0 =O000OOOOOOOO00OO0 ['data']['ordinary_fertilizer']#line:646
                print (f'【我的营养】:肥料:{str(O0OOO0O00OO0000O0).split(".")[0]}丨水滴:{str(O00O000OOO0OOO000).split(".")[0]}')#line:647
                if float (O0OOO0O00OO0000O0 )<96 :#line:648
                    O000O0OO0OO0O0O00 =99 -float (O0OOO0O00OO0000O0 )#line:649
                    O00O0O0O0O0O00O00 ={"fertilizer":str (O000O0OO0OO0O0O00 ).split ('.')[0 ]}#line:650
                    OOOOO000O00000000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO000O00O00OO0O0O ).json ()#line:651
                    if 'status'in OOOOO000O00000000 :#line:653
                        if OOOOO000O00000000 ['status']==200 :#line:654
                            print (f'【购买肥料】:看广告获取肥料:{OOOOO000O00000000["message"]}')#line:655
                if float (O00O000OOO0OOO000 )<960 :#line:657
                    OO00O0000O000O000 =999 -float (O00O000OOO0OOO000 )#line:658
                    OOO000O000OO0O0OO ={"water":str (OO00O0000O000O000 ).split ('.')[0 ]}#line:659
                    OO0000OO00O0O00O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO000O00O00OO0O0O ).json ()#line:660
                    if 'status'in OO0000OO00O0O00O0 :#line:662
                        if OO0000OO00O0O00O0 ['status']==200 :#line:663
                            print (f'【购买水滴】:看广告获取水滴:{OO0000OO00O0O00O0["message"]}')#line:664
def version_of_the_validation ():#line:668
    return str ((68 -56 )/10 )#line:669
def gitee_validation ():#line:672
    try :#line:673
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:674
    except :#line:675
        sys .exit (0 )#line:676
def update_the_validation ():#line:680
    try :#line:681
        OOOOO00O00O0OO0OO =gitee_validation ()#line:682
        if version_of_the_validation ()<OOOOO00O00O0OO0OO ['CityEarth']['edition']:#line:683
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOO00O00O0OO0OO["CityEarth"]["edition"]}   ❌')#line:684
            print (f'更新内容=>>{OOOOO00O00O0OO0OO["CityEarth"]["content"]}   👍')#line:685
        else :#line:686
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOO00O00O0OO0OO["CityEarth"]["edition"]}   ✅')#line:687
            print (f'更新内容=>> {OOOOO00O00O0OO0OO["CityEarth"]["content"]}   👍')#line:688
    except Exception as O0OOOOO00O000O0O0 :#line:689
        print (O0OOOOO00O000O0O0 )#line:690
def os_qinglong ():#line:693
    if application in os .environ :#line:694
        OO0O00O00O0OOOOOO =os .environ [application ].split ('\n')#line:695
        if len (OO0O00O00O0OOOOOO )>0 :#line:696
            return OO0O00O00O0OOOOOO #line:697
        else :#line:698
            print (f"{application}变量未启用")#line:699
            print ('脚本退出')#line:700
            sys .exit (1 )#line:701
    else :#line:702
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:704
        return os_built ()#line:705
def os_built ():#line:708
    if token :#line:709
        OOO0OOOO0O0O00O00 =token .split ('\n')#line:710
        if len (OOO0OOOO0O0O00O00 )>0 :#line:711
            return OOO0OOOO0O0O00O00 #line:712
    else :#line:713
        print (f"内置变量为空")#line:714
        print ('脚本结束')#line:715
        sys .exit (0 )#line:716
if __name__ =='__main__':#line:719
    start ()#line:720
