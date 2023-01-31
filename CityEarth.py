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
        O00000O0O00OO0O0O =os_qinglong ()#line:7
        print (f"==========共找到{len(O00000O0O00OO0O0O)}个账号==========")#line:8
        for OOOO0O00O0OOOO0O0 in O00000O0O00OO0O0O :#line:9
            print (f"------------正在执行第{O00000O0O00OO0O0O.index(OOOO0O00O0OOOO0O0) + 1}个账号------------")#line:10
            O0OOO00O00O0OOO00 =CityEarth (OOOO0O00O0OOOO0O0 )#line:11
            def OO000000OOO000O0O ():#line:13
                if O0OOO00O00O0OOO00 .base_info ():#line:15
                    O0OOO00O00O0OOO00 .game_map ()#line:19
                    O0OOO00O00O0OOO00 .friends_invitation ()#line:21
                    O0OOO00O00O0OOO00 .add_clover ()#line:23
                    O0OOO00O00O0OOO00 .energy ()#line:25
                    O0OOO00O00O0OOO00 .propsraffle ()#line:27
                    O0OOO00O00O0OOO00 .synthetic ()#line:29
                    O0OOO00O00O0OOO00 .crops_illustrated ()#line:31
                    O0OOO00O00O0OOO00 .give_gold ()#line:33
                else :#line:34
                    print ('token失效')#line:35
            O0OO000OOOO00O0OO =threading .Thread (target =OO000000OOO000O0O )#line:37
            O0OO000OOOO00O0OO .start ()#line:38
            time .sleep (time_xx )#line:39
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:41
        time .sleep (3 )#line:42
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:43
    except Exception as OOO00O0O0O0000O0O :#line:44
        print (OOO00O0O0O0000O0O )#line:45
def sign (OO00OOO0OO00OO0OO ):#line:48
    OOO00O0OOOO00OO0O =hashlib .md5 (OO00OOO0OO00OO0OO .encode ()).hexdigest ()#line:49
    OO0O0O00O0O0O0OOO ="scsc%^&*"+OOO00O0OOOO00OO0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:50
    O0O0OOOOO000OOO0O =hashlib .md5 (OO0O0O00O0O0O0OOO .encode ()).hexdigest ()#line:51
    return O0O0OOOOO000OOO0O #line:52
def timi_new ():#line:55
    return str (int (time .time ()*1000 ))#line:56
class CityEarth :#line:58
    def __init__ (O0OOO0000O00OOO00 ,OOOOO0OOO0000OOO0 ):#line:60
        try :#line:61
            O0OOO0000O00OOO00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:62
            O0OOO0000O00OOO00 .token =OOOOO0OOO0000OOO0 .split ('&')[0 ]#line:63
            O0OOO0000O00OOO00 .innerId =OOOOO0OOO0000OOO0 .split ('&')[1 ]#line:64
            O0OOO0000O00OOO00 .doneeNo =OOOOO0OOO0000OOO0 .split ('&')[2 ]#line:65
        except :#line:66
            print ('变量格式错误')#line:67
    def base_info (O0OOOOO0O0O0O0000 ):#line:70
        try :#line:71
            OOO000OO00O0OOOO0 =f'__{timi_new()}'#line:72
            OOO0O00O0O0000OOO ={'authorization':O0OOOOO0O0O0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO00O0OOOO0 ),'signstring':OOO000OO00O0OOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:81
            OO0O0OO0000OO000O =requests .request ('get',f'{host}/user',headers =OOO0O00O0O0000OOO ).json ()#line:82
            if 'status'in OO0O0OO0000OO000O :#line:84
                if OO0O0OO0000OO000O ['status']==200 :#line:85
                    OOOO0OOO0OO00OOOO =OO0O0OO0000OO000O ['data']['nickname']#line:86
                    OOO0O000O0O00O0OO =OO0O0OO0000OO000O ['data']['inner_id']#line:87
                    OOO000O000000O00O =OO0O0OO0000OO000O ['data']['assets']['gold']#line:88
                    OO00O0000OO00000O =OO0O0OO0000OO000O ['data']['level']#line:89
                    print (f'【账号信息】:昵称:{OOOO0OOO0OO00OOOO[:5]}丨ID:{OOO0O000O0O00O0OO}丨等级:{OO00O0000OO00000O}丨种子:{str(OOO000O000000O00O).split(".")[0]}')#line:90
                if OO0O0OO0000OO000O ['status']==401 :#line:91
                    return False #line:92
                if OO0O0OO0000OO000O ['status']==500 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as OOOO000O0O0OOO0OO :#line:96
            print (OOOO000O0O0OOO0OO )#line:97
    def game_map (O00OO00OOOOO00O0O ):#line:100
        try :#line:101
            O000OO000000O00O0 =f'__{timi_new()}'#line:102
            O0O0O0O00000OOO0O ={'authorization':O00OO00OOOOO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO000000O00O0 ),'signstring':O000OO000000O00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:111
            O000OO000O0000OO0 =requests .request ('get',f'{host}/game/map',headers =O0O0O0O00000OOO0O ).json ()#line:112
            if 'status'in O000OO000O0000OO0 :#line:114
                if O000OO000O0000OO0 ['status']==200 :#line:115
                    for OO000O00OO0O0OO0O in O000OO000O0000OO0 ['data']['list'][0 ]['crops']:#line:116
                        OO0OO00OOOOO00OO0 =OO000O00OO0O0OO0O ['level']#line:118
                        if OO0OO00OOOOO00OO0 ==41 :#line:119
                            O00O0OO00OOOOOO00 =OO000O00OO0O0OO0O ['crop_name']#line:120
                            OOO0O00O0O00O00O0 =OO000O00OO0O0OO0O ['count']#line:121
                            if OOO0O00O0O00O00O0 >0 :#line:122
                                print (f'【农业资产】:{O00O0OO00OOOOOO00}丨数量:{OOO0O00O0O00O00O0}')#line:123
        except Exception as O0O00O0000O0O00O0 :#line:124
            print (O0O00O0000O0O00O0 )#line:125
    def give_gold (O0O0OOO0O00000O00 ):#line:129
        try :#line:130
            OOO0OOO0OOO0OO0O0 =f'__{timi_new()}'#line:131
            OOO00O000OOOO0000 ={'authorization':O0O0OOO0O00000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OOO0OO0O0 ),'signstring':OOO0OOO0OOO0OO0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:140
            OOO0000OOO0O0OOO0 =requests .request ('get',f'{host}/user',headers =OOO00O000OOOO0000 ).json ()#line:141
            if 'status'in OOO0000OOO0O0OOO0 :#line:142
                if OOO0000OOO0O0OOO0 ['status']==200 :#line:143
                    if float (O0O0OOO0O00000O00 .doneeNo )!=0 :#line:144
                        O0O00O000OOO0OO00 =OOO0000OOO0O0OOO0 ['data']['assets']['gold']#line:145
                        if float (O0O00O000OOO0OO00 )>float (O0O0OOO0O00000O00 .innerId ):#line:146
                            O00OOOOO00OOO00O0 =int (float (O0O00O000OOO0OO00 )/1.1 )#line:147
                            OOO0OOO0OOO0OO0O0 =f'_doneeNo={O0O0OOO0O00000O00.doneeNo}&quantity={O00OOOOO00OOO00O0}_{timi_new()}'#line:148
                            OOO00O000OOOO0000 ={'authorization':O0O0OOO0O00000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OOO0OO0O0 ),'signstring':OOO0OOO0OOO0OO0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:157
                            O0OOOO0O000000000 ={"quantity":O00OOOOO00OOO00O0 ,"doneeNo":O0O0OOO0O00000O00 .doneeNo }#line:161
                            OO000OO0OOO0OOOO0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO00O000OOOO0000 ,data =O0OOOO0O000000000 ).json ()#line:162
                            if 'status'in OO000OO0OOO0OOOO0 :#line:164
                                if OO000OO0OOO0OOOO0 ['status']==200 :#line:165
                                    if OO000OO0OOO0OOOO0 ['data']:#line:166
                                        print (f'【赠送种子】:赠送{O00OOOOO00OOO00O0}种子给{O0O0OOO0O00000O00.doneeNo}成功')#line:167
                    else :#line:168
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:169
        except Exception as O0OOOOO0O0OO00O0O :#line:170
            print (O0OOOOO0O0OO00O0O )#line:171
    def winning_rewards (OOOOO00O0OO0O00O0 ):#line:175
        try :#line:176
            O00OO0O00000O0000 =f'__{timi_new()}'#line:177
            OOO0O0O0O0000O00O ={'authorization':OOOOO00O0OO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O00000O0000 ),'signstring':O00OO0O00000O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
            OOO0OOOOOO0OO0OO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO0O0O0O0000O00O ).json ()#line:187
            if 'status'in OOO0OOOOOO0OO0OO0 :#line:189
                if OOO0OOOOOO0OO0OO0 ['status']==200 :#line:190
                    if OOO0OOOOOO0OO0OO0 ['data']['amount']:#line:191
                        O0O0OO0OOOOOO0O00 =OOO0OOOOOO0OO0OO0 ['data']['amount']['gold']#line:192
                        return O0O0OO0OOOOOO0O00 #line:193
                    else :#line:194
                        return 0 #line:195
        except Exception as OOO0O00OO0OO00000 :#line:196
            print (OOO0O00OO0OO00000 )#line:197
    def certification (O00OO0000O00O0000 ):#line:201
        try :#line:202
            OOOOO0O0O000O00O0 =f'__{timi_new()}'#line:203
            OOOOOO00O0OOOOO0O ={'authorization':O00OO0000O00O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O0O000O00O0 ),'signstring':OOOOO0O0O000O00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:212
            O0OOOO0O0O00OOO0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOOOOO00O0OOOOO0O ).json ()#line:213
            if 'status'in O0OOOO0O0O00OOO0O :#line:215
                if O0OOOO0O0O00OOO0O ['status']==200 :#line:216
                    if O0OOOO0O0O00OOO0O ['data']['result']:#line:217
                        OO0000OOOOOOOO00O =O0OOOO0O0O00OOO0O ['data']['nick_name']#line:218
                        return OO0000OOOOOOOO00O #line:219
                    else :#line:220
                        return '未实名'#line:221
        except Exception as OO00OO0O0O00O0O00 :#line:222
            print (OO00OO0O0O00O0O00 )#line:223
    def crops_illustrated (O0OO0OOO00O0OOO00 ):#line:227
        try :#line:228
            OOO0OOOOO0O00O0O0 =f'__{timi_new()}'#line:229
            O0O0OO0000O0OOO0O ={'authorization':O0OO0OOO00O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOO0O00O0O0 ),'signstring':OOO0OOOOO0O00O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:238
            OO0OO0OOO0O00O000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O0OO0000O0OOO0O ).json ()#line:239
            if 'status'in OO0OO0OOO0O00O000 :#line:241
                if OO0OO0OOO0O00O000 ['status']==200 :#line:242
                    OO0O0OO0OO0O00OO0 =OO0OO0OOO0O00O000 ['data'][0 ]['crops']#line:243
                    for OOOO00000OOOO0O0O in OO0O0OO0OO0O00OO0 :#line:244
                        if OOOO00000OOOO0O0O ['ill_clover_award']:#line:245
                            if float (OOOO00000OOOO0O0O ['ill_clover_award'])>1 :#line:246
                                if OOOO00000OOOO0O0O ['is_finish']:#line:247
                                    if not OOOO00000OOOO0O0O ['is_getit']:#line:248
                                        if O0OO0OOO00O0OOO00 .certification ()!='未实名':#line:249
                                            OOO0OOOOO0O00O0O0 =f'_award_level={OOOO00000OOOO0O0O["level"]}_{timi_new()}'#line:250
                                            O0O0OO0000O0OOO0O ={'authorization':O0OO0OOO00O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOO0O00O0O0 ),'signstring':OOO0OOOOO0O00O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:259
                                            OO000000O000OOO00 ={"award_level":OOOO00000OOOO0O0O ['level']}#line:260
                                            OO00000OO0OO0O00O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O0OO0000O0OOO0O ,json =OO000000O000OOO00 ).json ()#line:262
                                            if 'status'in OO00000OO0OO0O00O :#line:263
                                                if OO00000OO0OO0O00O ['status']==200 :#line:264
                                                    OO0OO00OO0O00O0O0 =OO00000OO0OO0O00O ['data']['ill_clover_award']#line:265
                                                    print (f'【图鉴奖励】:领取{OOOO00000OOOO0O0O["crop_name"]}成就丨奖励{OO0OO00OO0O00O0O0}叶子成功')#line:267
                                                if OO00000OO0OO0O00O ['status']==500 :#line:268
                                                    print (f'【图鉴奖励】:{OO00000OO0OO0O00O["message"]}')#line:269
        except Exception as O00O0OO0O000O0000 :#line:270
            print (O00O0OO0O000O0000 )#line:271
    def watched_ad (O0O0O0O00OO0000O0 ):#line:275
        try :#line:276
            O0OOO00O0OOOOOOO0 =f'__{timi_new()}'#line:277
            OOO00O0O0000O00OO ={'authorization':O0O0O0O00OO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0OOOOOOO0 ),'signstring':O0OOO00O0OOOOOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:286
            O00O0000OOOOOO0O0 =requests .request ('post',f'{host}/game/watched-ad',headers =OOO00O0O0000O00OO ).json ()#line:287
            print (O00O0000OOOOOO0O0 )#line:288
        except Exception as OO0O0O00OO0O0OO0O :#line:289
            print (OO0O0O00OO0O0OO0O )#line:290
    def user_ad (O0000O0O00OO00OO0 ):#line:294
        try :#line:295
            OO00O000O0OOO00O0 =f'__{timi_new()}'#line:296
            O0OO0O00OO0O0000O ={'authorization':O0000O0O00OO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000O0OOO00O0 ),'signstring':OO00O000O0OOO00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:305
            O00O0O00OOOOO00OO =requests .request ('get',f'{host}/user/ad',headers =O0OO0O00OO0O0000O ).json ()#line:306
            if 'status'in O00O0O00OOOOO00OO :#line:308
                if O00O0O00OOOOO00OO ['status']==200 :#line:309
                    O0O0OO0OOOO0OOOO0 =O00O0O00OOOOO00OO ['data']['max_time']#line:310
                    O00OO0O0OO0O0OOO0 =O00O0O00OOOOO00OO ['data']['watch_time']#line:311
                    OOOO00000O0O00OO0 =O00O0O00OOOOO00OO ['data']['added_time']#line:312
                    print (f'【获取种子】:获取种子剩余{OOOO00000O0O00OO0 + O0O0OO0OOOO0OOOO0 - O00OO0O0OO0O0OOO0}次丨好友提供:{OOOO00000O0O00OO0}次')#line:313
                    if OOOO00000O0O00OO0 +O0O0OO0OOOO0OOOO0 -O00OO0O0OO0O0OOO0 >0 :#line:314
                        time .sleep (random .randint (16 ,19 ))#line:315
                        OOO0O00O0OOOO0OOO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OO0O00OO0O0000O ).json ()#line:316
                        if 'status'in OOO0O00O0OOOO0OOO :#line:318
                            if OOO0O00O0OOOO0OOO ['status']==200 :#line:319
                                O0OOOO0OO0O0O00OO =OOO0O00O0OOOO0OOO ['data']['silver']#line:320
                                print (f'【获取种子】:获得种子:{O0OOOO0OO0O0O00OO}')#line:321
                                return True #line:322
                            if OOO0O00O0OOOO0OOO ['status']==500 :#line:323
                                OOO00OOO00OO0O0OO =OOO0O00O0OOOO0OOO ['message']#line:324
                                print (f'【获取种子】:{OOO00OOO00OO0O0OO}')#line:325
                                return False #line:326
        except Exception as OO0O000OO0OO0O00O :#line:327
            print (OO0O000OO0OO0O00O )#line:328
    def synthetic (O0OO000000OOO000O ):#line:332
        global id ,g #line:333
        try :#line:334
            O00OO00OOO0OO0O00 =O0OO000000OOO000O .level_new ()#line:335
            while True :#line:336
                O00000OO00OO000OO =f'__{timi_new()}'#line:337
                OO00OO0OOOOOOO0OO ={'authorization':O0OO000000OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO00OO000OO ),'signstring':O00000OO00OO000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:346
                O0OOOO000OO00OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OO00OO0OOOOOOO0OO ).json ()#line:347
                if 'status'in O0OOOO000OO00OOO0 :#line:349
                    if O0OOOO000OO00OOO0 ['status']==200 :#line:350
                        OOOOO000O0O0O0O0O =O0OOOO000OO00OOO0 ['data']['cropList']#line:351
                        OOOOO000OO00O00OO =O0OOOO000OO00OOO0 ['data']['gameCoreDataDBid']#line:352
                        O00OOOO00O0OOO000 =0 #line:353
                        for O0000OO0OO00O00OO in OOOOO000O0O0O0O0O :#line:354
                            if not O0000OO0OO00O00OO :#line:355
                                OOOOOO00OO0O00O0O =f'_crop_id={OOOOO000OO00O00OO}&site={O00OOOO00O0OOO000}_{O0OO000000OOO000O.time}'#line:356
                                O0OO000OOO0O0OOOO ={'authorization':O0OO000000OOO000O .token ,'timestamp':O0OO000000OOO000O .time ,'sign':sign (OOOOOO00OO0O00O0O ),'signstring':OOOOOO00OO0O00O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:365
                                O0OO000O0000O00O0 ={"site":O00OOOO00O0OOO000 ,"crop_id":OOOOO000OO00O00OO }#line:366
                                O0O000OOO0OOO00O0 =requests .request ('post',f'{host}/game/crops/buy',headers =O0OO000OOO0O0OOOO ,data =O0OO000O0000O00O0 ).json ()#line:367
                                time .sleep (random .randint (1 ,3 )/10 )#line:369
                                if 'status'in O0O000OOO0OOO00O0 :#line:370
                                    if O0O000OOO0OOO00O0 ['status']==200 :#line:371
                                        if O0O000OOO0OOO00O0 ['message']=='种子数量不足':#line:372
                                            O00OO00OOO0OO0O00 =O0OO000000OOO000O .level_new ()#line:373
                                            print (f'【种植合成】:{O0O000OOO0OOO00O0["message"]}')#line:374
                                            if not O0OO000000OOO000O .user_ad ():#line:375
                                                return False #line:376
                                        print (f'【种植合成】:种植农作物,位置{O00OOOO00O0OOO000}')#line:377
                                    if O0O000OOO0OOO00O0 ['status']==500 :#line:378
                                        print (f'【种植合成】:{O0O000OOO0OOO00O0["message"]}')#line:379
                                        return False #line:380
                            O00OOOO00O0OOO000 +=1 #line:381
                        OO000OOOO0OO000OO =requests .request ('get',f'{host}/game/getAllData',headers =OO00OO0OOOOOOO0OO ).json ()#line:382
                        OO00O0OO0000O0O00 =OO000OOOO0OO000OO ['data']['cropList']#line:383
                        OOO00OOO00O000OO0 =False #line:384
                        for O0000OO0OO00O00OO in range (12 ):#line:385
                            id =OO00O0OO0000O0O00 [O0000OO0OO00O00OO ]['level']#line:386
                            if float (O00OO00OOO0OO0O00 )-float (id )>9 :#line:387
                                O00O0O00O000000O0 =f'_site={O0000OO0OO00O00OO}_{timi_new()}'#line:388
                                OO00O000OOOO0000O ={'accept':'application/json, text/plain, */*','authorization':O0OO000000OOO000O .token ,'timestamp':timi_new (),'sign':sign (O00O0O00O000000O0 ),'signstring':O00O0O00O000000O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:398
                                O00O000O00OOO0OOO ={"site":O0000OO0OO00O00OO }#line:399
                                O0000O00OO0OOOOOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO00O000OOOO0000O ,data =O00O000O00OOO0OOO ).json ()#line:401
                                if 'status'in O0000O00OO0OOOOOO :#line:402
                                    if O0000O00OO0OOOOOO ['status']==200 :#line:403
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:404
                            if id !=0 :#line:405
                                for OO0O000OO0OOOO00O in range (11 ):#line:406
                                    OOOO00O0OOOOOOO00 =OO0O000OO0OOOO00O +1 #line:407
                                    g =OO00O0OO0000O0O00 [OOOO00O0OOOOOOO00 ]['level']#line:408
                                    if id ==g :#line:409
                                        O0OOOOOO0O00O0OOO =OO0O000OO0OOOO00O +2 #line:410
                                        if O0OOOOOO0O00O0OOO ==O0000OO0OO00O00OO +1 :#line:411
                                            pass #line:412
                                        else :#line:413
                                            O00O0O0OO0O000O0O =O0000OO0OO00O00OO +1 #line:414
                                            time .sleep (random .randint (1 ,3 )/10 )#line:416
                                            O0OOOO0O0O0O000OO =f'_site={O00O0O0OO0O000O0O - 1}&targetSite={O0OOOOOO0O00O0OOO - 1}_{timi_new()}'#line:417
                                            OO00000OO0OOOO000 ={'accept':'application/json, text/plain, */*','authorization':O0OO000000OOO000O .token ,'timestamp':timi_new (),'sign':sign (O0OOOO0O0O0O000OO ),'signstring':O0OOOO0O0O0O000OO ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:432
                                            OO0OOO00O000OOO0O ={"site":int (O00O0O0OO0O000O0O -1 ),"targetSite":int (O0OOOOOO0O00O0OOO -1 )}#line:433
                                            OOOO0000OO0OOO00O =requests .request ('post',f'{host}/game/crops/move',headers =OO00000OO0OOOO000 ,json =OO0OOO00O000OOO0O ).json ()#line:435
                                            if 'status'in OOOO0000OO0OOO00O :#line:436
                                                if OOOO0000OO0OOO00O ['status']==200 :#line:437
                                                    pass #line:438
                                            print ('【种植合成】:',O00O0O0OO0O000O0O ,O0OOOOOO0O00O0OOO ,'合成成功')#line:440
                                            OOO00OOO00O000OO0 =True #line:441
                                    if OOO00OOO00O000OO0 :#line:442
                                        break #line:443
                                if OOO00OOO00O000OO0 :#line:444
                                    break #line:445
        except Exception as OO0OO00O00OO0O00O :#line:446
            O0OO000000OOO000O .synthetic ()#line:447
    def level_new (OOO0O0OOO0OOOOOO0 ):#line:450
        try :#line:451
            O0O0OOO00OO0O000O =f'__{timi_new()}'#line:452
            O000000OO0OOOO0O0 ={'authorization':OOO0O0OOO0OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO00OO0O000O ),'signstring':O0O0OOO00OO0O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:461
            OO00O00O0O0000O0O =requests .request ('get',f'{host}/user',headers =O000000OO0OOOO0O0 ).json ()#line:462
            if 'status'in OO00O00O0O0000O0O :#line:463
                if OO00O00O0O0000O0O ['status']==200 :#line:464
                    return float (OO00O00O0O0000O0O ['data']['level'])#line:465
        except Exception as OOOOOO00OO00OO000 :#line:466
            print (OOOOOO00OO00OO000 )#line:467
    def propsraffle (O0O0O0OOOOOO0000O ):#line:470
        try :#line:471
            while True :#line:472
                OOO00O000O000OO0O =f'__{timi_new()}'#line:473
                OOO0O00O0O0O0O000 ={'authorization':O0O0O0OOOOOO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O000O000OO0O ),'signstring':OOO00O000O000OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:482
                O000000OO00O0OOO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO0O00O0O0O0O000 ).json ()#line:483
                if 'status'in O000000OO00O0OOO0 :#line:485
                    if O000000OO00O0OOO0 ['status']==200 :#line:486
                        OO00O0O0000OOOOO0 =O000000OO00O0OOO0 ['data']['rows']#line:487
                        O0O000000OOOO0OO0 =O000000OO00O0OOO0 ['data']['vstate']#line:488
                        if OO00O0O0000OOOOO0 ==5 or OO00O0O0000OOOOO0 ==6 or OO00O0O0000OOOOO0 ==7 :#line:489
                            OOOOOO0O0O00000OO =O000000OO00O0OOO0 ['data']['silver']#line:490
                            print (f'【转盘抽奖】:获得种子:{OOOOOO0O0O00000OO}')#line:491
                        if OO00O0O0000OOOOO0 ==1 or OO00O0O0000OOOOO0 ==2 or OO00O0O0000OOOOO0 ==3 :#line:492
                            OOO000O0O0000O00O =O000000OO00O0OOO0 ['data']['clover']#line:493
                            print (f'【转盘抽奖】:获得三叶草:{OOO000O0O0000O00O}')#line:494
                        if OO00O0O0000OOOOO0 ==4 or OO00O0O0000OOOOO0 ==8 :#line:495
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:496
                        if OO00O0O0000OOOOO0 =='抽奖次数已用完':#line:500
                            if O0O000000OOOO0OO0 :#line:501
                                OOO00O000O000OO0O =f'__{timi_new()}'#line:502
                                OOO0O00O0O0O0O000 ={'authorization':O0O0O0OOOOOO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O000O000OO0O ),'signstring':OOO00O000O000OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:511
                                O00O0000O00OO00O0 =requests .request ('get',f'{host}/user',headers =OOO0O00O0O0O0O000 ).json ()#line:512
                                if 'status'in O00O0000O00OO00O0 :#line:513
                                    if O00O0000O00OO00O0 ['status']==200 :#line:514
                                        OO00OO0O00000O000 =O00O0000O00OO00O0 ['data']['level']#line:515
                                        if float (OO00OO0O00000O000 )>39 :#line:516
                                            OOO00OO0O000OOO0O =random .randint (160 ,190 )/10 #line:517
                                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{OOO00OO0O000OOO0O}秒获取抽奖机会')#line:518
                                            time .sleep (OOO00OO0O000OOO0O )#line:519
                                            OOOOO0OO0O00O0OO0 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OOO0O00O0O0O0O000 ).json ()#line:520
                                            if 'status'in OOOOO0OO0O00O0OO0 :#line:522
                                                if OOOOO0OO0O00O0OO0 ['status']==200 :#line:523
                                                    print (f'【转盘抽奖】:{OOOOO0OO0O00O0OO0["message"]}')#line:524
                                                if OOOOO0OO0O00O0OO0 ['status']==500 :#line:525
                                                    print (f'【转盘抽奖】:{OOOOO0OO0O00O0OO0["message"]}')#line:526
                                                    break #line:527
                                            time .sleep (random .randint (10 ,15 )/10 )#line:528
                                        else :#line:529
                                            break #line:530
                            else :#line:531
                                break #line:532
                time .sleep (random .randint (8 ,15 )/10 )#line:533
        except Exception as OO0O00OO0O00O00OO :#line:534
            print (OO0O00OO0O00O00OO )#line:535
    def friends_invitation (O0O00O0O0OO00O000 ):#line:538
        try :#line:539
            O0O0O0OO0O0O0O0OO =f'__{timi_new()}'#line:540
            O0O0O00O00OOO00O0 ={'authorization':O0O00O0O0OO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO0O0O0O0OO ),'signstring':O0O0O0OO0O0O0O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:549
            OOO0OO00O0O0OOO0O =requests .request ('get',f'{host}/friends',headers =O0O0O00O00OOO00O0 ).json ()#line:550
            if 'status'in OOO0OO00O0O0OOO0O :#line:551
                if OOO0OO00O0O0OOO0O ['status']==200 :#line:552
                    OOOO0O0OO0OOOO000 =OOO0OO00O0O0OOO0O ['data']['myInviteter']#line:553
                    if OOOO0O0OO0OOOO000 :#line:554
                        OOOOO00OO00O00OOO =OOOO0O0OO0OOOO000 ['user']['nickname']#line:555
                        OO0O0O000O0O00OO0 =O0O00O0O0OO00O000 .certification ()#line:556
                        print (f'【查邀请人】:我的邀请人:{OOOOO00OO00O00OOO}丨实名:{OO0O0O000O0O00OO0}')#line:557
                    else :#line:558
                        if O0O00O0O0OO00O000 .innerId !='0':#line:559
                            O0O0O0OO0O0O0O0OO =f'_innerId=1937553_{timi_new()}'#line:560
                            O0O0O00O00OOO00O0 ={'authorization':O0O00O0O0OO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO0O0O0O0OO ),'signstring':O0O0O0OO0O0O0O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:569
                            OOO0OOOO0O00000O0 ={"innerId":'1937553'}#line:570
                            OO0O0OOO0000OO0OO =requests .request ('post',f'{host}/friends/my-invitation',headers =O0O0O00O00OOO00O0 ,data =OOO0OOOO0O00000O0 ).json ()#line:572
        except Exception as O00OOOO00OOOOO0OO :#line:573
            print (O00OOOO00OOOOO0OO )#line:574
    def add_clover (O00O00O0O0OOOOOOO ):#line:577
        global golden_seed #line:578
        try :#line:579
            O000O000O0O0O00OO =f'__{timi_new()}'#line:580
            OOOOOOOOO0OO0OOO0 ={'authorization':O00O00O0O0OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000O0O0O00OO ),'signstring':O000O000O0O0O00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:589
            OOO0OOO0O0O000O0O =requests .request ('get',f'{host}/assets/clovers',headers =OOOOOOOOO0OO0OOO0 ).json ()#line:590
            if 'status'in OOO0OOO0O0O000O0O :#line:592
                if OOO0OOO0O0O000O0O ['status']==200 :#line:593
                    OO00OO00OOOO00OOO =OOO0OOO0O0O000O0O ['data']['clover']#line:594
                    OO0OOO0O0O0O0O0O0 =OOO0OOO0O0O000O0O ['data']['used_clover']#line:595
                    O0OO0OO0OOOOOO000 =float (OO00OO00OOOO00OOO )-float (OO0OOO0O0O0O0O0O0 )#line:596
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OO0OOO0O0O0O0O0O0}')#line:597
                    if O00O00O0O0OOOOOOO .certification ()!='未实名':#line:598
                        if O0OO0OO0OOOOOO000 >1 :#line:599
                            O000O000O0O0O00OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OO0OO0OOOOOO000)}_{timi_new()}'#line:600
                            OOOOOOOOO0OO0OOO0 ={'authorization':O00O00O0O0OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000O0O0O00OO ),'signstring':O000O000O0O0O00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:609
                            OO0OOO0OO0O0O000O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OO0OO0OOOOOO000 )}#line:610
                            OO0OO00O0O0O00O0O =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOOOOOOO0OO0OOO0 ,data =OO0OOO0OO0O0O000O ).json ()#line:611
                            if 'status'in OO0OO00O0O0O00O0O :#line:613
                                if OO0OO00O0O0O00O0O ['status']==200 :#line:614
                                    print (f'【参与抽奖】:添加三叶草:{OO0OO00O0O0O00O0O["data"]}丨数量:{O0OO0OO0OOOOOO000}')#line:615
                                if OO0OO00O0O0O00O0O ['status']==500 :#line:616
                                    print (f'【参与抽奖】:添加三叶草:{OO0OO00O0O0O00O0O["message"]}')#line:617
            O0OO0O0OOOOOO0000 =requests .request ('get',f'{host}/lottery',headers =OOOOOOOOO0OO0OOO0 ).json ()#line:618
            O0OO00OO0O00O0OOO =O00O00O0O0OOOOOOO .winning_rewards ()#line:620
            if 'status'in O0OO0O0OOOOOO0000 :#line:621
                if O0OO0O0OOOOOO0000 ['status']==200 :#line:622
                    O00000OO0OO0OOO00 =O0OO0O0OOOOOO0000 ['data'][0 ]['day_get_gold_quantity']#line:623
                    golden_seed +=float (O00000OO0OO0OOO00 )#line:624
                    print (f'【参与抽奖】:预计每天中{str(O00000OO0OO0OOO00)[:6]}颗金种子丨好友收益:{str(O0OO00OO0O00O0OOO)[:6]}')#line:625
        except Exception as O00OOO0O00O000O0O :#line:626
            print (O00OOO0O00O000O0O )#line:627
    def energy (OOO0O00O0OO0O0OO0 ):#line:630
        OO000OOOOOO00OOO0 =f'__{timi_new()}'#line:631
        OOOOO00OOO0OOO0OO ={'authorization':OOO0O00O0OO0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOOOO00OOO0 ),'signstring':OO000OOOOOO00OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:640
        OO00OO000O0OO00OO =requests .request ('get',f'{host}/energy/general',headers =OOOOO00OOO0OOO0OO ).json ()#line:641
        if 'status'in OO00OO000O0OO00OO :#line:643
            if OO00OO000O0OO00OO ['status']==200 :#line:644
                O0OOOO0O0OOOO000O =OO00OO000O0OO00OO ['data']['ordinary_water_consumptions']#line:645
                if float (O0OOOO0O0OOOO000O )<80 :#line:646
                    OO0OOOOO0OO00O000 =99 -float (O0OOOO0O0OOOO000O )#line:647
                    O00OOO0OOOO0O0O0O ={"fertilizer":str (OO0OOOOO0OO00O000 ).split ('.')[0 ]}#line:648
                    O000OO0OOOO000OOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOOO00OOO0OOO0OO ,data =O00OOO0OOOO0O0O0O ).json ()#line:649
                    if 'status'in O000OO0OOOO000OOO :#line:651
                        if O000OO0OOOO000OOO ['status']==200 :#line:652
                            print (f'【购买肥料】:{O000OO0OOOO000OOO["message"]}')#line:653
                O0OO0O000OO0O0O00 =OO00OO000O0OO00OO ['data']['ordinary_water_consumptions']#line:654
                if float (O0OO0O000OO0O0O00 )<800 :#line:655
                    O000O0OO00O0OO0O0 =999 -float (O0OO0O000OO0O0O00 )#line:656
                    O0O0000O00O00O0OO ={"water":str (O000O0OO00O0OO0O0 ).split ('.')[0 ]}#line:657
                    OO000OOO0O0000OOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOOO00OOO0OOO0OO ,data =O0O0000O00O00O0OO ).json ()#line:658
                    if 'status'in OO000OOO0O0000OOO :#line:659
                        if OO000OOO0O0000OOO ['status']==200 :#line:660
                            print (f'【购买水滴】:{OO000OOO0O0000OOO["message"]}')#line:661
def version_of_the_validation ():#line:665
    return str ((68 -56 )/10 )#line:666
def gitee_validation ():#line:669
    try :#line:670
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:671
    except :#line:672
        sys .exit (0 )#line:673
def update_the_validation ():#line:677
    try :#line:678
        OOO0O00O000O00000 =gitee_validation ()#line:679
        if version_of_the_validation ()<OOO0O00O000O00000 ['CityEarth']['edition']:#line:680
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0O00O000O00000["CityEarth"]["edition"]}   ❌')#line:681
            print (f'更新内容=>>{OOO0O00O000O00000["CityEarth"]["content"]}   👍')#line:682
        else :#line:683
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0O00O000O00000["CityEarth"]["edition"]}   ✅')#line:684
            print (f'更新内容=>> {OOO0O00O000O00000["CityEarth"]["content"]}   👍')#line:685
    except Exception as OO0O0O0OOOO0O0OO0 :#line:686
        print (OO0O0O0OOOO0O0OO0 )#line:687
def os_qinglong ():#line:690
    if application in os .environ :#line:691
        OOOOOOO000OO0O0O0 =os .environ [application ].split ('\n')#line:692
        if len (OOOOOOO000OO0O0O0 )>0 :#line:693
            return OOOOOOO000OO0O0O0 #line:694
        else :#line:695
            print (f"{application}变量未启用")#line:696
            print ('脚本退出')#line:697
            sys .exit (1 )#line:698
    else :#line:699
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:701
        return os_built ()#line:702
def os_built ():#line:705
    if token :#line:706
        O00O0OOO00O0OOOOO =token .split ('\n')#line:707
        if len (O00O0OOO00O0OOOOO )>0 :#line:708
            return O00O0OOO00O0OOOOO #line:709
    else :#line:710
        print (f"内置变量为空")#line:711
        print ('脚本结束')#line:712
        sys .exit (0 )#line:713
if __name__ =='__main__':#line:716
    start ()#line:717
