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
@ 青龙变量  青龙配置文件 export ce_token="authorization&赠送金种子数量大于&赠送金种子id"   如果你有20金种子填10就会赠 填21就不会赠送  不赠送全填 999999   多号换行
@ 变量示范    export ce_token="557b8069-1234-4ae7-9e29-b7871f91541b&999999&999999"  用&符号分开数据
@ 我的邀请码是  1937553
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
        OO0O00OOOO00OOO0O =os_qinglong ()#line:7
        print (f"==========共找到{len(OO0O00OOOO00OOO0O)}个账号==========")#line:8
        for OO0000O000000000O in OO0O00OOOO00OOO0O :#line:9
            print (f"------------正在执行第{OO0O00OOOO00OOO0O.index(OO0000O000000000O) + 1}个账号------------")#line:10
            OO0O0O00O0O0OOOO0 =CityEarth (OO0000O000000000O )#line:11
            def O00O0000OOOO0O000 ():#line:13
                if OO0O0O00O0O0OOOO0 .base_info ():#line:15
                    OO0O0O00O0O0OOOO0 .game_map ()#line:19
                    OO0O0O00O0O0OOOO0 .friends_invitation ()#line:21
                    OO0O0O00O0O0OOOO0 .add_clover ()#line:23
                    OO0O0O00O0O0OOOO0 .energy ()#line:25
                    OO0O0O00O0O0OOOO0 .synthetic ()#line:27
                    OO0O0O00O0O0OOOO0 .propsraffle ()#line:29
                    OO0O0O00O0O0OOOO0 .crops_illustrated ()#line:31
                    OO0O0O00O0O0OOOO0 .give_gold ()#line:33
                else :#line:34
                    print ('token失效')#line:35
            O0OO00O00O00O0O0O =threading .Thread (target =O00O0000OOOO0O000 )#line:37
            O0OO00O00O00O0O0O .start ()#line:38
            time .sleep (time_xx )#line:39
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:41
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:42
    except Exception as O000OO0000OO0OO00 :#line:43
        print (O000OO0000OO0OO00 )#line:44
def sign (O0O0O000000O0O00O ):#line:47
    OO0000000OOO0O000 =hashlib .md5 (O0O0O000000O0O00O .encode ()).hexdigest ()#line:48
    OOO0O0000OOO0000O ="scsc%^&*"+OO0000000OOO0O000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:49
    O00O00OO000000OOO =hashlib .md5 (OOO0O0000OOO0000O .encode ()).hexdigest ()#line:50
    return O00O00OO000000OOO #line:51
def timi_new ():#line:54
    return str (int (time .time ()*1000 ))#line:55
class CityEarth :#line:58
    def __init__ (O000000000O0OO000 ,O000OOOO00OO00O00 ):#line:60
        try :#line:61
            O000000000O0OO000 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:62
            O000000000O0OO000 .token =O000OOOO00OO00O00 .split ('&')[0 ]#line:63
            O000000000O0OO000 .innerId =O000OOOO00OO00O00 .split ('&')[1 ]#line:64
            O000000000O0OO000 .doneeNo =O000OOOO00OO00O00 .split ('&')[2 ]#line:65
        except :#line:66
            print ('变量格式错误')#line:67
    def base_info (O0OO0O0OOOO0OO000 ):#line:70
        try :#line:71
            OOO000000OO0O0O0O =f'__{timi_new()}'#line:72
            O00000000O00OOO00 ={'authorization':O0OO0O0OOOO0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000000OO0O0O0O ),'signstring':OOO000000OO0O0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:81
            OO0O0OO00O000000O =requests .request ('get',f'{host}/user',headers =O00000000O00OOO00 ).json ()#line:82
            if 'status'in OO0O0OO00O000000O :#line:84
                if OO0O0OO00O000000O ['status']==200 :#line:85
                    O0OOO00O0000O000O =OO0O0OO00O000000O ['data']['nickname']#line:86
                    OO0O0OOO0000OOOO0 =OO0O0OO00O000000O ['data']['inner_id']#line:87
                    OO0O00O00O000OOO0 =OO0O0OO00O000000O ['data']['assets']['gold']#line:88
                    O0O0O00OO0O0O00O0 =OO0O0OO00O000000O ['data']['level']#line:89
                    print (f'【账号信息】:昵称:{O0OOO00O0000O000O[:5]}丨ID:{str(OO0O0OOO0000OOOO0)[:3] + "**" + str(OO0O0OOO0000OOOO0)[5:]}丨等级:{O0O0O00OO0O0O00O0}丨种子:{str(OO0O00O00O000OOO0).split(".")[0]}')#line:90
                if OO0O0OO00O000000O ['status']==401 :#line:91
                    return False #line:92
                if OO0O0OO00O000000O ['status']==500 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as OO0OOO00OO0OOOO00 :#line:96
            print (OO0OOO00OO0OOOO00 )#line:97
    def game_map (O0O0O00OO00OO0O00 ):#line:100
        OO000OO00000O00OO =f'__{timi_new()}'#line:101
        OOO00O0O0O0000000 ={'authorization':O0O0O00OO00OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO00000O00OO ),'signstring':OO000OO00000O00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:110
        OOOO00OOO00OOOO00 =requests .request ('get',f'{host}/game/map',headers =OOO00O0O0O0000000 ).json ()#line:111
        if 'status'in OOOO00OOO00OOOO00 :#line:113
            if OOOO00OOO00OOOO00 ['status']==200 :#line:114
                for OOOO0OO0OOO0O0OOO in OOOO00OOO00OOOO00 ['data']['list'][0 ]['crops']:#line:115
                    OO0OOO00O00OO0O00 =OOOO0OO0OOO0O0OOO ['level']#line:117
                    if OO0OOO00O00OO0O00 ==41 :#line:118
                        O00OOO00OOO000OO0 =OOOO0OO0OOO0O0OOO ['crop_name']#line:119
                        OO0O0O0000OO0O0OO =OOOO0OO0OOO0O0OOO ['count']#line:120
                        if OO0O0O0000OO0O0OO >0 :#line:121
                            print (f'【农业资产】:{O00OOO00OOO000OO0}丨数量:{OO0O0O0000OO0O0OO}')#line:122
    def give_gold (OO0000OO0OOOO000O ):#line:125
        OOOO0OO00O00000O0 =f'__{timi_new()}'#line:126
        O00O0O00OO0OO00O0 ={'authorization':OO0000OO0OOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00O00000O0 ),'signstring':OOOO0OO00O00000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:135
        O0OO00OOOO00000OO =requests .request ('get',f'{host}/user',headers =O00O0O00OO0OO00O0 ).json ()#line:136
        if 'status'in O0OO00OOOO00000OO :#line:137
            if O0OO00OOOO00000OO ['status']==200 :#line:138
                if float (OO0000OO0OOOO000O .doneeNo )!=0 :#line:139
                    OO0O000OO0000O0OO =O0OO00OOOO00000OO ['data']['assets']['gold']#line:140
                    if float (OO0O000OO0000O0OO )>float (OO0000OO0OOOO000O .innerId ):#line:141
                        OO00O0O0O0O00000O =int (float (OO0O000OO0000O0OO )/1.1 )#line:142
                        OOOO0OO00O00000O0 =f'_doneeNo={OO0000OO0OOOO000O.doneeNo}&quantity={OO00O0O0O0O00000O}_{timi_new()}'#line:143
                        O00O0O00OO0OO00O0 ={'authorization':OO0000OO0OOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00O00000O0 ),'signstring':OOOO0OO00O00000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:152
                        OO00OOOOOO0000O0O ={"quantity":OO00O0O0O0O00000O ,"doneeNo":OO0000OO0OOOO000O .doneeNo }#line:156
                        O0OO00OOOOOOOOO0O =requests .request ('post',f'{host}/finance/give-gold',headers =O00O0O00OO0OO00O0 ,data =OO00OOOOOO0000O0O ).json ()#line:157
                        if 'status'in O0OO00OOOOOOOOO0O :#line:159
                            if O0OO00OOOOOOOOO0O ['status']==200 :#line:160
                                if O0OO00OOOOOOOOO0O ['data']:#line:161
                                    print (f'【赠送种子】:赠送{OO00O0O0O0O00000O}种子给{OO0000OO0OOOO000O.doneeNo}成功')#line:162
                else :#line:163
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:164
    def winning_rewards (OO0O0O000O00000O0 ):#line:167
        OO0O0000O0OO0O00O =f'__{timi_new()}'#line:168
        O0OOOOOOOOO0000O0 ={'authorization':OO0O0O000O00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000O0OO0O00O ),'signstring':OO0O0000O0OO0O00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:177
        O0000O0OOO00OOOOO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOOOOOOOO0000O0 ).json ()#line:178
        if 'status'in O0000O0OOO00OOOOO :#line:180
            if O0000O0OOO00OOOOO ['status']==200 :#line:181
                if O0000O0OOO00OOOOO ['data']['amount']:#line:182
                    O000O00O00OO0OO00 =O0000O0OOO00OOOOO ['data']['amount']['gold']#line:183
                    return O000O00O00OO0OO00 #line:184
                else :#line:185
                    return 0 #line:186
    def certification (OOOO0OO000O000OO0 ):#line:189
        OOOOOO0O000OOO0OO =f'__{timi_new()}'#line:190
        O00O0OOOO0OO0O000 ={'authorization':OOOO0OO000O000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O000OOO0OO ),'signstring':OOOOOO0O000OOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:199
        O0O0O00O000OO0O0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00O0OOOO0OO0O000 ).json ()#line:200
        if 'status'in O0O0O00O000OO0O0O :#line:202
            if O0O0O00O000OO0O0O ['status']==200 :#line:203
                if O0O0O00O000OO0O0O ['data']['result']:#line:204
                    O00OOO00000OOOOO0 =O0O0O00O000OO0O0O ['data']['nick_name']#line:205
                    return O00OOO00000OOOOO0 #line:206
                else :#line:207
                    return '未实名'#line:208
    def crops_illustrated (OOOOO0O0OO0000O00 ):#line:211
        OO0OO0OOO0O00000O =f'__{timi_new()}'#line:212
        O0OOOOO0OOOOO000O ={'authorization':OOOOO0O0OO0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OOO0O00000O ),'signstring':OO0OO0OOO0O00000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:221
        OO0OOOO0O00OOO0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OOOOO0OOOOO000O ).json ()#line:222
        if 'status'in OO0OOOO0O00OOO0O0 :#line:224
            if OO0OOOO0O00OOO0O0 ['status']==200 :#line:225
                OOOOO0O00000OO0O0 =OO0OOOO0O00OOO0O0 ['data'][0 ]['crops']#line:226
                for OO0OOOO0OO0OO0OOO in OOOOO0O00000OO0O0 :#line:227
                    if OO0OOOO0OO0OO0OOO ['ill_clover_award']:#line:228
                        if float (OO0OOOO0OO0OO0OOO ['ill_clover_award'])>1 :#line:229
                            if OO0OOOO0OO0OO0OOO ['is_finish']:#line:230
                                if not OO0OOOO0OO0OO0OOO ['is_getit']:#line:231
                                    OO0OO0OOO0O00000O =f'_award_level={OO0OOOO0OO0OO0OOO["level"]}_{timi_new()}'#line:232
                                    O0OOOOO0OOOOO000O ={'authorization':OOOOO0O0OO0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OOO0O00000O ),'signstring':OO0OO0OOO0O00000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:241
                                    O00O000000OO000O0 ={"award_level":OO0OOOO0OO0OO0OOO ['level']}#line:242
                                    O0000O0OO00O0OOO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OOOOO0OOOOO000O ,json =O00O000000OO000O0 ).json ()#line:244
                                    if 'status'in O0000O0OO00O0OOO0 :#line:245
                                        if O0000O0OO00O0OOO0 ['status']==200 :#line:246
                                            OOO0OO0O0O00OOOO0 =O0000O0OO00O0OOO0 ['data']['ill_clover_award']#line:247
                                            print (f'【图鉴奖励】:领取{OO0OOOO0OO0OO0OOO["crop_name"]}成就丨奖励{OOO0OO0O0O00OOOO0}叶子成功')#line:249
                                        if O0000O0OO00O0OOO0 ['status']==500 :#line:250
                                            print (f'【图鉴奖励】:{O0000O0OO00O0OOO0["message"]}')#line:251
    def watched_ad (OOO00O0O000O000O0 ):#line:254
        OOO00000OOO0OO0O0 =f'__{timi_new()}'#line:255
        O000000OO00O0O000 ={'authorization':OOO00O0O000O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00000OOO0OO0O0 ),'signstring':OOO00000OOO0OO0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:264
        O00000OOOO0O0O00O =requests .request ('post',f'{host}/game/watched-ad',headers =O000000OO00O0O000 ).json ()#line:265
        print (O00000OOOO0O0O00O )#line:266
    def user_ad (O0O0O00O000O00O00 ):#line:269
        O000O0OO0O0OOOO00 =f'__{timi_new()}'#line:270
        OOO00OO00O00OO0O0 ={'authorization':O0O0O00O000O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO0O0OOOO00 ),'signstring':O000O0OO0O0OOOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:279
        OOO000OO0000OO0OO =requests .request ('get',f'{host}/user/ad',headers =OOO00OO00O00OO0O0 ).json ()#line:280
        if 'status'in OOO000OO0000OO0OO :#line:282
            if OOO000OO0000OO0OO ['status']==200 :#line:283
                O0000OO0O0O0OO00O =OOO000OO0000OO0OO ['data']['max_time']#line:284
                O0O0O0O00OOO0OO00 =OOO000OO0000OO0OO ['data']['watch_time']#line:285
                OO0O000OO00O0O0OO =OOO000OO0000OO0OO ['data']['added_time']#line:286
                print (f'【获取种子】:获取种子剩余{OO0O000OO00O0O0OO + O0000OO0O0O0OO00O - O0O0O0O00OOO0OO00}次丨好友提供:{OO0O000OO00O0O0OO}次')#line:287
                if OO0O000OO00O0O0OO +O0000OO0O0O0OO00O -O0O0O0O00OOO0OO00 >0 :#line:288
                    time .sleep (random .randint (16 ,19 ))#line:289
                    OO00O00OOOO00O0O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO00OO00O00OO0O0 ).json ()#line:290
                    if 'status'in OO00O00OOOO00O0O0 :#line:292
                        if OO00O00OOOO00O0O0 ['status']==200 :#line:293
                            OOO00000O000OO0O0 =OO00O00OOOO00O0O0 ['data']['silver']#line:294
                            print (f'【获取种子】:获得种子:{OOO00000O000OO0O0}')#line:295
                            return True #line:296
                        if OO00O00OOOO00O0O0 ['status']==500 :#line:297
                            O000OO0O0000OOOO0 =OO00O00OOOO00O0O0 ['message']#line:298
                            print (f'【获取种子】:{O000OO0O0000OOOO0}')#line:299
                            return False #line:300
    def synthetic (O0O0OO0OOO0O0OO0O ):#line:303
        global id ,g #line:304
        try :#line:305
            OO0OO000OOO0O00OO =O0O0OO0OOO0O0OO0O .level_new ()#line:306
            while True :#line:307
                OOOO000O00OOOO000 =f'__{timi_new()}'#line:308
                O0OO00O0O00O00OOO ={'authorization':O0O0OO0OOO0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O00OOOO000 ),'signstring':OOOO000O00OOOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:317
                OOOOO00O0OO0O0000 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO00O0O00O00OOO ).json ()#line:318
                if 'status'in OOOOO00O0OO0O0000 :#line:320
                    if OOOOO00O0OO0O0000 ['status']==200 :#line:321
                        OOOOOOOO0O000O00O =OOOOO00O0OO0O0000 ['data']['cropList']#line:322
                        O00O00OO0O000O0O0 =OOOOO00O0OO0O0000 ['data']['gameCoreDataDBid']#line:323
                        OO00OOO0O0OO00OOO =0 #line:324
                        for OOOO00OOO0OOOOO00 in OOOOOOOO0O000O00O :#line:325
                            if not OOOO00OOO0OOOOO00 :#line:326
                                O0O0OOO00OO0OOO00 =f'_crop_id={O00O00OO0O000O0O0}&site={OO00OOO0O0OO00OOO}_{O0O0OO0OOO0O0OO0O.time}'#line:327
                                O0OOO0000O0O00OO0 ={'authorization':O0O0OO0OOO0O0OO0O .token ,'timestamp':O0O0OO0OOO0O0OO0O .time ,'sign':sign (O0O0OOO00OO0OOO00 ),'signstring':O0O0OOO00OO0OOO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:336
                                OOO0O0O00O0OO0OO0 ={"site":OO00OOO0O0OO00OOO ,"crop_id":O00O00OO0O000O0O0 }#line:337
                                O0OO00O0O0O00O0OO =requests .request ('post',f'{host}/game/crops/buy',headers =O0OOO0000O0O00OO0 ,data =OOO0O0O00O0OO0OO0 ).json ()#line:338
                                time .sleep (random .randint (1 ,3 )/10 )#line:340
                                if 'status'in O0OO00O0O0O00O0OO :#line:341
                                    if O0OO00O0O0O00O0OO ['status']==200 :#line:342
                                        if O0OO00O0O0O00O0OO ['message']=='种子数量不足':#line:343
                                            OO0OO000OOO0O00OO =O0O0OO0OOO0O0OO0O .level_new ()#line:344
                                            print (f'【种植合成】:{O0OO00O0O0O00O0OO["message"]}')#line:345
                                            if not O0O0OO0OOO0O0OO0O .user_ad ():#line:346
                                                return False #line:347
                                        print (f'【种植合成】:种植农作物,位置{OO00OOO0O0OO00OOO}')#line:348
                                    if O0OO00O0O0O00O0OO ['status']==500 :#line:349
                                        print (f'【种植合成】:{O0OO00O0O0O00O0OO["message"]}')#line:350
                                        return False #line:351
                            OO00OOO0O0OO00OOO +=1 #line:352
                        OOO000O000O000O00 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO00O0O00O00OOO ).json ()#line:353
                        O00O0OOO0OOO0OO0O =OOO000O000O000O00 ['data']['cropList']#line:354
                        O0O00OO000000O00O =False #line:355
                        for OOOO00OOO0OOOOO00 in range (12 ):#line:356
                            id =O00O0OOO0OOO0OO0O [OOOO00OOO0OOOOO00 ]['level']#line:357
                            if float (OO0OO000OOO0O00OO )-float (id )>9 :#line:358
                                OO00OO00OO0OOOOO0 =f'_site={OOOO00OOO0OOOOO00}_{timi_new()}'#line:359
                                OOO00OOO0OO00OOO0 ={'accept':'application/json, text/plain, */*','authorization':O0O0OO0OOO0O0OO0O .token ,'timestamp':timi_new (),'sign':sign (OO00OO00OO0OOOOO0 ),'signstring':OO00OO00OO0OOOOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:369
                                OO00000OOO0000000 ={"site":OOOO00OOO0OOOOO00 }#line:370
                                OOOO0OOO0O0O00000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO00OOO0OO00OOO0 ,data =OO00000OOO0000000 ).json ()#line:372
                                if 'status'in OOOO0OOO0O0O00000 :#line:373
                                    if OOOO0OOO0O0O00000 ['status']==200 :#line:374
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:375
                            if id !=0 :#line:376
                                for OOO000000O0OO00O0 in range (11 ):#line:377
                                    O00O0O0O0000O0O00 =OOO000000O0OO00O0 +1 #line:378
                                    g =O00O0OOO0OOO0OO0O [O00O0O0O0000O0O00 ]['level']#line:379
                                    if id ==g :#line:380
                                        OO0OOO0000OO00000 =OOO000000O0OO00O0 +2 #line:381
                                        if OO0OOO0000OO00000 ==OOOO00OOO0OOOOO00 +1 :#line:382
                                            pass #line:383
                                        else :#line:384
                                            O000O00O00O0O0O00 =OOOO00OOO0OOOOO00 +1 #line:385
                                            time .sleep (random .randint (1 ,3 )/10 )#line:387
                                            O00O00OO0OO0O0O0O =f'_site={O000O00O00O0O0O00 - 1}&targetSite={OO0OOO0000OO00000 - 1}_{timi_new()}'#line:388
                                            O0OOOOO00OO0OO0OO ={'accept':'application/json, text/plain, */*','authorization':O0O0OO0OOO0O0OO0O .token ,'timestamp':timi_new (),'sign':sign (O00O00OO0OO0O0O0O ),'signstring':O00O00OO0OO0O0O0O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:403
                                            O00O0O0O0OO0O0000 ={"site":int (O000O00O00O0O0O00 -1 ),"targetSite":int (OO0OOO0000OO00000 -1 )}#line:404
                                            O00O000O00O000O0O =requests .request ('post',f'{host}/game/crops/move',headers =O0OOOOO00OO0OO0OO ,json =O00O0O0O0OO0O0000 ).json ()#line:406
                                            if 'status'in O00O000O00O000O0O :#line:407
                                                if O00O000O00O000O0O ['status']==200 :#line:408
                                                    pass #line:409
                                            print ('【种植合成】:',O000O00O00O0O0O00 ,OO0OOO0000OO00000 ,'合成成功')#line:411
                                            O0O00OO000000O00O =True #line:412
                                    if O0O00OO000000O00O :#line:413
                                        break #line:414
                                if O0O00OO000000O00O :#line:415
                                    break #line:416
        except Exception as OO0OOO0OOOOOO0O0O :#line:417
            O0O0OO0OOO0O0OO0O .synthetic ()#line:418
    def level_new (OOOOO00O0000O000O ):#line:421
        try :#line:422
            O00OOO0O0000O0OO0 =f'__{timi_new()}'#line:423
            O0OO00OO0OOOOOOO0 ={'authorization':OOOOO00O0000O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0O0000O0OO0 ),'signstring':O00OOO0O0000O0OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:432
            O00O000000OO00OO0 =requests .request ('get',f'{host}/user',headers =O0OO00OO0OOOOOOO0 ).json ()#line:433
            if 'status'in O00O000000OO00OO0 :#line:434
                if O00O000000OO00OO0 ['status']==200 :#line:435
                    return float (O00O000000OO00OO0 ['data']['level'])#line:436
        except Exception as OO0OO00O00O00OOO0 :#line:437
            print (OO0OO00O00O00OOO0 )#line:438
    def propsraffle (OOOO0O0000OOOOOOO ):#line:441
        try :#line:442
            while True :#line:443
                O00O0OOO0OO000O0O =f'__{timi_new()}'#line:444
                O0O0OO00O0OO0000O ={'authorization':OOOO0O0000OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO0OO000O0O ),'signstring':O00O0OOO0OO000O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:453
                O0OO00O000OOO0OO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O0OO00O0OO0000O ).json ()#line:454
                if 'status'in O0OO00O000OOO0OO0 :#line:456
                    if O0OO00O000OOO0OO0 ['status']==200 :#line:457
                        O0O0OOOOO0O000OO0 =O0OO00O000OOO0OO0 ['data']['rows']#line:458
                        O00OOO0OOOOOOOO00 =O0OO00O000OOO0OO0 ['data']['vstate']#line:459
                        if O0O0OOOOO0O000OO0 ==5 or O0O0OOOOO0O000OO0 ==6 or O0O0OOOOO0O000OO0 ==7 :#line:460
                            O0O0O0OO0OOO0O0OO =O0OO00O000OOO0OO0 ['data']['silver']#line:461
                            print (f'【转盘抽奖】:获得种子:{O0O0O0OO0OOO0O0OO}')#line:462
                        if O0O0OOOOO0O000OO0 ==1 or O0O0OOOOO0O000OO0 ==2 or O0O0OOOOO0O000OO0 ==3 :#line:463
                            OOO0OOOOOO0O00000 =O0OO00O000OOO0OO0 ['data']['clover']#line:464
                            print (f'【转盘抽奖】:获得三叶草:{OOO0OOOOOO0O00000}')#line:465
                        if O0O0OOOOO0O000OO0 ==4 or O0O0OOOOO0O000OO0 ==8 :#line:466
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:467
                        if O0O0OOOOO0O000OO0 =='抽奖次数已用完':#line:471
                            if O00OOO0OOOOOOOO00 :#line:472
                                OOOOO0O00OOOOO000 =random .randint (160 ,190 )/10 #line:473
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{OOOOO0O00OOOOO000}秒获取抽奖机会')#line:474
                                time .sleep (OOOOO0O00OOOOO000 )#line:475
                                OOOO00O000OO000O0 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O0O0OO00O0OO0000O ).json ()#line:477
                                if 'status'in OOOO00O000OO000O0 :#line:479
                                    if OOOO00O000OO000O0 ['status']==200 :#line:480
                                        print (f'【转盘抽奖】:{OOOO00O000OO000O0["message"]}')#line:481
                                    if OOOO00O000OO000O0 ['status']==500 :#line:482
                                        print (f'【转盘抽奖】:{OOOO00O000OO000O0["message"]}')#line:483
                                        break #line:484
                                time .sleep (random .randint (10 ,15 )/10 )#line:485
                            else :#line:486
                                break #line:487
                time .sleep (random .randint (8 ,15 )/10 )#line:488
        except Exception as OOOOOOO0O000O00OO :#line:489
            print (OOOOOOO0O000O00OO )#line:490
    def friends_invitation (O0OOO0OOOO00OOO0O ):#line:493
        try :#line:494
            OO000000OOOO0O00O =f'__{timi_new()}'#line:495
            O00O000O0OOOOOO00 ={'authorization':O0OOO0OOOO00OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000OOOO0O00O ),'signstring':OO000000OOOO0O00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:504
            OO0O0OOOOOOOO000O =requests .request ('get',f'{host}/friends',headers =O00O000O0OOOOOO00 ).json ()#line:505
            if 'status'in OO0O0OOOOOOOO000O :#line:506
                if OO0O0OOOOOOOO000O ['status']==200 :#line:507
                    O000OO0OOO0OOOO0O =OO0O0OOOOOOOO000O ['data']['myInviteter']#line:508
                    if O000OO0OOO0OOOO0O :#line:509
                        OO00O0O00000OO00O =O000OO0OOO0OOOO0O ['user']['nickname']#line:510
                        O00O0OO00O0OOO000 =O0OOO0OOOO00OOO0O .certification ()#line:511
                        print (f'【查邀请人】:我的邀请人:{OO00O0O00000OO00O}丨实名:{O00O0OO00O0OOO000}')#line:512
                    else :#line:513
                        if O0OOO0OOOO00OOO0O .innerId !='0':#line:514
                            OO000000OOOO0O00O =f'_innerId=1937553_{timi_new()}'#line:515
                            O00O000O0OOOOOO00 ={'authorization':O0OOO0OOOO00OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000OOOO0O00O ),'signstring':OO000000OOOO0O00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:524
                            O00OO0000O00O00O0 ={"innerId":'1937553'}#line:525
                            O0O0OOO0000000O0O =requests .request ('post',f'{host}/friends/my-invitation',headers =O00O000O0OOOOOO00 ,data =O00OO0000O00O00O0 ).json ()#line:527
        except Exception as O000000O000OOO0O0 :#line:528
            print (O000000O000OOO0O0 )#line:529
    def add_clover (O0OO00OO0O0OOO0O0 ):#line:532
        global golden_seed #line:533
        try :#line:534
            OO0O0OOO000O0O0O0 =f'__{timi_new()}'#line:535
            O0O00000O00O0O0O0 ={'authorization':O0OO00OO0O0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOO000O0O0O0 ),'signstring':OO0O0OOO000O0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:544
            O000O0000OOO0O0OO =requests .request ('get',f'{host}/assets/clovers',headers =O0O00000O00O0O0O0 ).json ()#line:545
            if 'status'in O000O0000OOO0O0OO :#line:547
                if O000O0000OOO0O0OO ['status']==200 :#line:548
                    O0OOO0O0OOOO0O000 =O000O0000OOO0O0OO ['data']['clover']#line:549
                    O0000000OOOO0O000 =O000O0000OOO0O0OO ['data']['used_clover']#line:550
                    O00OO000000OOOO00 =float (O0OOO0O0OOOO0O000 )-float (O0000000OOOO0O000 )#line:551
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0000000OOOO0O000}')#line:552
                    if O00OO000000OOOO00 >1 :#line:553
                        OO0O0OOO000O0O0O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00OO000000OOOO00)}_{timi_new()}'#line:554
                        O0O00000O00O0O0O0 ={'authorization':O0OO00OO0O0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOO000O0O0O0 ),'signstring':OO0O0OOO000O0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:563
                        OOOO0O00O00O00O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00OO000000OOOO00 )}#line:564
                        OOOOOOO00O00OO00O =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O00000O00O0O0O0 ,data =OOOO0O00O00O00O0O ).json ()#line:565
                        if 'status'in OOOOOOO00O00OO00O :#line:567
                            if OOOOOOO00O00OO00O ['status']==200 :#line:568
                                print (f'【参与抽奖】:添加三叶草:{OOOOOOO00O00OO00O["data"]}丨数量:{O00OO000000OOOO00}')#line:569
            O0O0OOO00000OO00O =requests .request ('get',f'{host}/lottery',headers =O0O00000O00O0O0O0 ).json ()#line:570
            O0000O0OO0OO0O00O =O0OO00OO0O0OOO0O0 .winning_rewards ()#line:572
            if 'status'in O0O0OOO00000OO00O :#line:573
                if O0O0OOO00000OO00O ['status']==200 :#line:574
                    O00O000O000O000O0 =O0O0OOO00000OO00O ['data'][0 ]['day_get_gold_quantity']#line:575
                    golden_seed +=float (O00O000O000O000O0 )#line:576
                    print (f'【参与抽奖】:预计每天中{O00O000O000O000O0[:6]}颗金种子丨好友收益:{str(O0000O0OO0OO0O00O)[:6]}')#line:577
        except Exception as OO000O00OOO00O0OO :#line:578
            print (OO000O00OOO00O0OO )#line:579
    def energy (O0O0OOO0O0O0O000O ):#line:582
        O00OOOO00OOO000OO =f'__{timi_new()}'#line:583
        OO0000OOOOO00O00O ={'authorization':O0O0OOO0O0O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO00OOO000OO ),'signstring':O00OOOO00OOO000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:592
        OOO00000O000OOO00 =requests .request ('get',f'{host}/energy/general',headers =OO0000OOOOO00O00O ).json ()#line:593
        if 'status'in OOO00000O000OOO00 :#line:595
            if OOO00000O000OOO00 ['status']==200 :#line:596
                OOOOOOO000OO000OO =OOO00000O000OOO00 ['data']['ordinary_water_consumptions']#line:597
                if float (OOOOOOO000OO000OO )<80 :#line:598
                    O00OOOO0OOO000O0O =99 -float (OOOOOOO000OO000OO )#line:599
                    O0OOOOO00000OO0O0 ={"fertilizer":str (O00OOOO0OOO000O0O ).split ('.')[0 ]}#line:600
                    O000OOOO0OO0OOOOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0000OOOOO00O00O ,data =O0OOOOO00000OO0O0 ).json ()#line:602
                    if 'status'in O000OOOO0OO0OOOOO :#line:604
                        if O000OOOO0OO0OOOOO ['status']==200 :#line:605
                            print (f'【购买肥料】:{O000OOOO0OO0OOOOO["message"]}')#line:606
                OO0O0OOO0OO0O0O00 =OOO00000O000OOO00 ['data']['ordinary_water_consumptions']#line:607
                if float (OO0O0OOO0OO0O0O00 )<800 :#line:608
                    O0OOOO00OOO0O000O =999 -float (OO0O0OOO0OO0O0O00 )#line:609
                    OOOOO000OOO0O0000 ={"water":str (O0OOOO00OOO0O000O ).split ('.')[0 ]}#line:610
                    O00OO000O0O0OOOOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0000OOOOO00O00O ,data =OOOOO000OOO0O0000 ).json ()#line:611
                    if 'status'in O00OO000O0O0OOOOO :#line:612
                        if O00OO000O0O0OOOOO ['status']==200 :#line:613
                            print (f'【购买水滴】:{O00OO000O0O0OOOOO["message"]}')#line:614
def version_of_the_validation ():#line:618
    return str ((66 -56 )/10 )#line:619
def gitee_validation ():#line:622
    try :#line:623
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:624
    except Exception as O00O00O00O0O0OO00 :#line:625
        sys .exit (0 )#line:626
def update_the_validation ():#line:630
    try :#line:631
        O0OOOO0O00OOOOO0O =gitee_validation ()#line:632
        if version_of_the_validation ()<O0OOOO0O00OOOOO0O ['CityEarth']['edition']:#line:633
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOO0O00OOOOO0O["CityEarth"]["edition"]}   ❌')#line:634
            print (f'更新内容=>>{O0OOOO0O00OOOOO0O["CityEarth"]["content"]}   👍')#line:635
        else :#line:636
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOO0O00OOOOO0O["CityEarth"]["edition"]}   ✅')#line:637
            print (f'更新内容=>> {O0OOOO0O00OOOOO0O["CityEarth"]["content"]}   👍')#line:638
    except Exception as OO000O0OOO0O0O0OO :#line:639
        print (OO000O0OOO0O0O0OO )#line:640
def os_qinglong ():#line:643
    if application in os .environ :#line:644
        O00OO000O000OO0O0 =os .environ [application ].split ('\n')#line:645
        if len (O00OO000O000OO0O0 )>0 :#line:646
            return O00OO000O000OO0O0 #line:647
        else :#line:648
            print (f"{application}变量未启用")#line:649
            print ('脚本退出')#line:650
            sys .exit (1 )#line:651
    else :#line:652
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:654
        return os_built ()#line:655
def os_built ():#line:658
    if token :#line:659
        OOOO0OO00OO00O000 =token .split ('\n')#line:660
        if len (OOOO0OO00OO00O000 )>0 :#line:661
            return OOOO0OO00OO00O000 #line:662
    else :#line:663
        print (f"内置变量为空")#line:664
        print ('脚本结束')#line:665
        sys .exit (0 )#line:666
if __name__ =='__main__':#line:669
    start ()#line:670
