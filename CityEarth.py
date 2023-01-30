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
        OOOOOO00O00O0O0O0 =os_qinglong ()#line:7
        print (f"==========共找到{len(OOOOOO00O00O0O0O0)}个账号==========")#line:8
        for OOO0OOOOOOOO00O00 in OOOOOO00O00O0O0O0 :#line:9
            print (f"------------正在执行第{OOOOOO00O00O0O0O0.index(OOO0OOOOOOOO00O00) + 1}个账号------------")#line:10
            OO0OOOO0000OOOO0O =CityEarth (OOO0OOOOOOOO00O00 )#line:11
            def OOOOO0000OO0O0OO0 ():#line:13
                if OO0OOOO0000OOOO0O .base_info ():#line:15
                    OO0OOOO0000OOOO0O .game_map ()#line:19
                    OO0OOOO0000OOOO0O .friends_invitation ()#line:21
                    OO0OOOO0000OOOO0O .add_clover ()#line:23
                    OO0OOOO0000OOOO0O .energy ()#line:25
                    OO0OOOO0000OOOO0O .propsraffle ()#line:27
                    OO0OOOO0000OOOO0O .synthetic ()#line:29
                    OO0OOOO0000OOOO0O .crops_illustrated ()#line:31
                    OO0OOOO0000OOOO0O .give_gold ()#line:33
                else :#line:34
                    print ('token失效')#line:35
            O000O0000OOO000OO =threading .Thread (target =OOOOO0000OO0O0OO0 )#line:37
            O000O0000OOO000OO .start ()#line:38
            time .sleep (time_xx )#line:39
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:41
        time .sleep (3 )#line:42
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:43
    except Exception as O00OO0OOO0000OOO0 :#line:44
        print (O00OO0OOO0000OOO0 )#line:45
def sign (OO0OOO0OOOO0OOO0O ):#line:48
    O0O0O0OO0O0O0OO00 =hashlib .md5 (OO0OOO0OOOO0OOO0O .encode ()).hexdigest ()#line:49
    OO00OOOO0OOO00OO0 ="scsc%^&*"+O0O0O0OO0O0O0OO00 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:50
    OOO0OOO000O0O000O =hashlib .md5 (OO00OOOO0OOO00OO0 .encode ()).hexdigest ()#line:51
    return OOO0OOO000O0O000O #line:52
def timi_new ():#line:55
    return str (int (time .time ()*1000 ))#line:56
class CityEarth :#line:58
    def __init__ (O00O0000O0000OO0O ,O0000OO0O0OOO00OO ):#line:60
        try :#line:61
            O00O0000O0000OO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:62
            O00O0000O0000OO0O .token =O0000OO0O0OOO00OO .split ('&')[0 ]#line:63
            O00O0000O0000OO0O .innerId =O0000OO0O0OOO00OO .split ('&')[1 ]#line:64
            O00O0000O0000OO0O .doneeNo =O0000OO0O0OOO00OO .split ('&')[2 ]#line:65
        except :#line:66
            print ('变量格式错误')#line:67
    def base_info (OOOO00OO00OOOO0O0 ):#line:70
        try :#line:71
            O00OO0O00O00O0OOO =f'__{timi_new()}'#line:72
            O0O0OO0O0O0000O00 ={'authorization':OOOO00OO00OOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O00O00O0OOO ),'signstring':O00OO0O00O00O0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:81
            O0000O0OO0OO0O0O0 =requests .request ('get',f'{host}/user',headers =O0O0OO0O0O0000O00 ).json ()#line:82
            if 'status'in O0000O0OO0OO0O0O0 :#line:84
                if O0000O0OO0OO0O0O0 ['status']==200 :#line:85
                    OOO0OO000O000OO00 =O0000O0OO0OO0O0O0 ['data']['nickname']#line:86
                    O0OO0OOOO0O00O000 =O0000O0OO0OO0O0O0 ['data']['inner_id']#line:87
                    OOO0O000O00000OO0 =O0000O0OO0OO0O0O0 ['data']['assets']['gold']#line:88
                    OO00000O0000OO0OO =O0000O0OO0OO0O0O0 ['data']['level']#line:89
                    print (f'【账号信息】:昵称:{OOO0OO000O000OO00[:5]}丨ID:{O0OO0OOOO0O00O000}丨等级:{OO00000O0000OO0OO}丨种子:{str(OOO0O000O00000OO0).split(".")[0]}')#line:90
                if O0000O0OO0OO0O0O0 ['status']==401 :#line:91
                    return False #line:92
                if O0000O0OO0OO0O0O0 ['status']==500 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as OOO0OO0OOOO0OO0O0 :#line:96
            print (OOO0OO0OOOO0OO0O0 )#line:97
    def game_map (OOO0O000O0O000000 ):#line:100
        OOO00OOOOO0O0OO00 =f'__{timi_new()}'#line:101
        O000O0OOO00OOO0O0 ={'authorization':OOO0O000O0O000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOOOO0O0OO00 ),'signstring':OOO00OOOOO0O0OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:110
        OO0O00OOO0000O0OO =requests .request ('get',f'{host}/game/map',headers =O000O0OOO00OOO0O0 ).json ()#line:111
        if 'status'in OO0O00OOO0000O0OO :#line:113
            if OO0O00OOO0000O0OO ['status']==200 :#line:114
                for OO0O0OO00O0OO00OO in OO0O00OOO0000O0OO ['data']['list'][0 ]['crops']:#line:115
                    OOO0OO00000000OOO =OO0O0OO00O0OO00OO ['level']#line:117
                    if OOO0OO00000000OOO ==41 :#line:118
                        O0O0O00O00OOOO000 =OO0O0OO00O0OO00OO ['crop_name']#line:119
                        OOOOOOO0OO00OOOOO =OO0O0OO00O0OO00OO ['count']#line:120
                        if OOOOOOO0OO00OOOOO >0 :#line:121
                            print (f'【农业资产】:{O0O0O00O00OOOO000}丨数量:{OOOOOOO0OO00OOOOO}')#line:122
    def give_gold (OOOO0OOO0000O0O0O ):#line:125
        OOO0OOO0OO00000OO =f'__{timi_new()}'#line:126
        O0OOO0O000O00O000 ={'authorization':OOOO0OOO0000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OO00000OO ),'signstring':OOO0OOO0OO00000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:135
        O0O00000O0OOOOOO0 =requests .request ('get',f'{host}/user',headers =O0OOO0O000O00O000 ).json ()#line:136
        if 'status'in O0O00000O0OOOOOO0 :#line:137
            if O0O00000O0OOOOOO0 ['status']==200 :#line:138
                if float (OOOO0OOO0000O0O0O .doneeNo )!=0 :#line:139
                    OO00000OOO0OOOO0O =O0O00000O0OOOOOO0 ['data']['assets']['gold']#line:140
                    if float (OO00000OOO0OOOO0O )>float (OOOO0OOO0000O0O0O .innerId ):#line:141
                        OOOOOO0OOOOO00000 =int (float (OO00000OOO0OOOO0O )/1.1 )#line:142
                        OOO0OOO0OO00000OO =f'_doneeNo={OOOO0OOO0000O0O0O.doneeNo}&quantity={OOOOOO0OOOOO00000}_{timi_new()}'#line:143
                        O0OOO0O000O00O000 ={'authorization':OOOO0OOO0000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OO00000OO ),'signstring':OOO0OOO0OO00000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:152
                        OO000OO0O00O0O00O ={"quantity":OOOOOO0OOOOO00000 ,"doneeNo":OOOO0OOO0000O0O0O .doneeNo }#line:156
                        O0OOO00OO000O00O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0OOO0O000O00O000 ,data =OO000OO0O00O0O00O ).json ()#line:157
                        if 'status'in O0OOO00OO000O00O0 :#line:159
                            if O0OOO00OO000O00O0 ['status']==200 :#line:160
                                if O0OOO00OO000O00O0 ['data']:#line:161
                                    print (f'【赠送种子】:赠送{OOOOOO0OOOOO00000}种子给{OOOO0OOO0000O0O0O.doneeNo}成功')#line:162
                else :#line:163
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:164
    def winning_rewards (OOOO0O0OOO00OO00O ):#line:167
        O0O00O00OO0OOO000 =f'__{timi_new()}'#line:168
        OOO0OO0OOO0OO0O0O ={'authorization':OOOO0O0OOO00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00OO0OOO000 ),'signstring':O0O00O00OO0OOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:177
        O00OOOO0OO00O0000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO0OO0OOO0OO0O0O ).json ()#line:178
        if 'status'in O00OOOO0OO00O0000 :#line:180
            if O00OOOO0OO00O0000 ['status']==200 :#line:181
                if O00OOOO0OO00O0000 ['data']['amount']:#line:182
                    OO00000OOO000OOO0 =O00OOOO0OO00O0000 ['data']['amount']['gold']#line:183
                    return OO00000OOO000OOO0 #line:184
                else :#line:185
                    return 0 #line:186
    def certification (OOO00O000OOOO0O00 ):#line:189
        OOO000OO00OOOOOOO =f'__{timi_new()}'#line:190
        OOOOOO0OO0O0O0OOO ={'authorization':OOO00O000OOOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO00OOOOOOO ),'signstring':OOO000OO00OOOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:199
        O0OO0O0O0000O0O0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOOOOO0OO0O0O0OOO ).json ()#line:200
        if 'status'in O0OO0O0O0000O0O0O :#line:202
            if O0OO0O0O0000O0O0O ['status']==200 :#line:203
                if O0OO0O0O0000O0O0O ['data']['result']:#line:204
                    O0OOO0OO0OOOOOOOO =O0OO0O0O0000O0O0O ['data']['nick_name']#line:205
                    return O0OOO0OO0OOOOOOOO #line:206
                else :#line:207
                    return '未实名'#line:208
    def crops_illustrated (O00O0O000OOO0O0O0 ):#line:211
        O0000OO0OO00O00OO =f'__{timi_new()}'#line:212
        OO0O000OOO000OOO0 ={'authorization':O00O0O000OOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO0OO00O00OO ),'signstring':O0000OO0OO00O00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:221
        OOOOOOOOO0OOOO0OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O000OOO000OOO0 ).json ()#line:222
        if 'status'in OOOOOOOOO0OOOO0OO :#line:224
            if OOOOOOOOO0OOOO0OO ['status']==200 :#line:225
                OO00OOO00O000O0OO =OOOOOOOOO0OOOO0OO ['data'][0 ]['crops']#line:226
                for O00OO00OO00OO0OOO in OO00OOO00O000O0OO :#line:227
                    if O00OO00OO00OO0OOO ['ill_clover_award']:#line:228
                        if float (O00OO00OO00OO0OOO ['ill_clover_award'])>1 :#line:229
                            if O00OO00OO00OO0OOO ['is_finish']:#line:230
                                if not O00OO00OO00OO0OOO ['is_getit']:#line:231
                                    O0000OO0OO00O00OO =f'_award_level={O00OO00OO00OO0OOO["level"]}_{timi_new()}'#line:232
                                    OO0O000OOO000OOO0 ={'authorization':O00O0O000OOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO0OO00O00OO ),'signstring':O0000OO0OO00O00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:241
                                    OO00O0OOO0O0OOO0O ={"award_level":O00OO00OO00OO0OOO ['level']}#line:242
                                    OO000O0OO0O0000O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O000OOO000OOO0 ,json =OO00O0OOO0O0OOO0O ).json ()#line:244
                                    if 'status'in OO000O0OO0O0000O0 :#line:245
                                        if OO000O0OO0O0000O0 ['status']==200 :#line:246
                                            O0O0000OO0000OO00 =OO000O0OO0O0000O0 ['data']['ill_clover_award']#line:247
                                            print (f'【图鉴奖励】:领取{O00OO00OO00OO0OOO["crop_name"]}成就丨奖励{O0O0000OO0000OO00}叶子成功')#line:249
                                        if OO000O0OO0O0000O0 ['status']==500 :#line:250
                                            print (f'【图鉴奖励】:{OO000O0OO0O0000O0["message"]}')#line:251
    def watched_ad (OOO00OO0OOO00O0OO ):#line:254
        OO00O0O0OO0OOOO0O =f'__{timi_new()}'#line:255
        O0OO000O0O00O000O ={'authorization':OOO00OO0OOO00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0OO0OOOO0O ),'signstring':OO00O0O0OO0OOOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:264
        OO000OOO0O00OO0OO =requests .request ('post',f'{host}/game/watched-ad',headers =O0OO000O0O00O000O ).json ()#line:265
        print (OO000OOO0O00OO0OO )#line:266
    def user_ad (O0OOO0OO000O0OO0O ):#line:269
        O0OOO00O0O00O0000 =f'__{timi_new()}'#line:270
        OO000000O0O0OOO0O ={'authorization':O0OOO0OO000O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0O00O0000 ),'signstring':O0OOO00O0O00O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:279
        OOOO0OO0000O00OOO =requests .request ('get',f'{host}/user/ad',headers =OO000000O0O0OOO0O ).json ()#line:280
        if 'status'in OOOO0OO0000O00OOO :#line:282
            if OOOO0OO0000O00OOO ['status']==200 :#line:283
                O00O0O0O000O00O00 =OOOO0OO0000O00OOO ['data']['max_time']#line:284
                O000O0O000O000000 =OOOO0OO0000O00OOO ['data']['watch_time']#line:285
                OOOO00O0OO000O0OO =OOOO0OO0000O00OOO ['data']['added_time']#line:286
                print (f'【获取种子】:获取种子剩余{OOOO00O0OO000O0OO + O00O0O0O000O00O00 - O000O0O000O000000}次丨好友提供:{OOOO00O0OO000O0OO}次')#line:287
                if OOOO00O0OO000O0OO +O00O0O0O000O00O00 -O000O0O000O000000 >0 :#line:288
                    time .sleep (random .randint (16 ,19 ))#line:289
                    O000000O0O00000OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO000000O0O0OOO0O ).json ()#line:290
                    if 'status'in O000000O0O00000OO :#line:292
                        if O000000O0O00000OO ['status']==200 :#line:293
                            OO0OOO0OO00O0O0OO =O000000O0O00000OO ['data']['silver']#line:294
                            print (f'【获取种子】:获得种子:{OO0OOO0OO00O0O0OO}')#line:295
                            return True #line:296
                        if O000000O0O00000OO ['status']==500 :#line:297
                            O0000OOOOO00O0OOO =O000000O0O00000OO ['message']#line:298
                            print (f'【获取种子】:{O0000OOOOO00O0OOO}')#line:299
                            return False #line:300
    def synthetic (O0000OO00OO0O0OO0 ):#line:303
        global id ,g #line:304
        try :#line:305
            OO0000OOO00000O00 =O0000OO00OO0O0OO0 .level_new ()#line:306
            while True :#line:307
                OO0O0000O0OOO0OOO =f'__{timi_new()}'#line:308
                OO00OOO00OOOO0O00 ={'authorization':O0000OO00OO0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000O0OOO0OOO ),'signstring':OO0O0000O0OOO0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:317
                OOO0OOO00OO0O0OOO =requests .request ('get',f'{host}/game/getAllData',headers =OO00OOO00OOOO0O00 ).json ()#line:318
                if 'status'in OOO0OOO00OO0O0OOO :#line:320
                    if OOO0OOO00OO0O0OOO ['status']==200 :#line:321
                        O00OO0O00OOO000O0 =OOO0OOO00OO0O0OOO ['data']['cropList']#line:322
                        OO00O0O00O000O00O =OOO0OOO00OO0O0OOO ['data']['gameCoreDataDBid']#line:323
                        OOOOO0OOOO000O000 =0 #line:324
                        for OO00O00O00OOOOOO0 in O00OO0O00OOO000O0 :#line:325
                            if not OO00O00O00OOOOOO0 :#line:326
                                OO00O00OOO00O0O00 =f'_crop_id={OO00O0O00O000O00O}&site={OOOOO0OOOO000O000}_{O0000OO00OO0O0OO0.time}'#line:327
                                OOOOOOOO0O0O00OO0 ={'authorization':O0000OO00OO0O0OO0 .token ,'timestamp':O0000OO00OO0O0OO0 .time ,'sign':sign (OO00O00OOO00O0O00 ),'signstring':OO00O00OOO00O0O00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:336
                                OOOOOO000O0O00OO0 ={"site":OOOOO0OOOO000O000 ,"crop_id":OO00O0O00O000O00O }#line:337
                                O000OO0000OO0OOO0 =requests .request ('post',f'{host}/game/crops/buy',headers =OOOOOOOO0O0O00OO0 ,data =OOOOOO000O0O00OO0 ).json ()#line:338
                                time .sleep (random .randint (1 ,3 )/10 )#line:340
                                if 'status'in O000OO0000OO0OOO0 :#line:341
                                    if O000OO0000OO0OOO0 ['status']==200 :#line:342
                                        if O000OO0000OO0OOO0 ['message']=='种子数量不足':#line:343
                                            OO0000OOO00000O00 =O0000OO00OO0O0OO0 .level_new ()#line:344
                                            print (f'【种植合成】:{O000OO0000OO0OOO0["message"]}')#line:345
                                            if not O0000OO00OO0O0OO0 .user_ad ():#line:346
                                                return False #line:347
                                        print (f'【种植合成】:种植农作物,位置{OOOOO0OOOO000O000}')#line:348
                                    if O000OO0000OO0OOO0 ['status']==500 :#line:349
                                        print (f'【种植合成】:{O000OO0000OO0OOO0["message"]}')#line:350
                                        return False #line:351
                            OOOOO0OOOO000O000 +=1 #line:352
                        O0O0OO000OO00OOOO =requests .request ('get',f'{host}/game/getAllData',headers =OO00OOO00OOOO0O00 ).json ()#line:353
                        O00OOO00O000OOOO0 =O0O0OO000OO00OOOO ['data']['cropList']#line:354
                        OOOO0OOO0O000O0O0 =False #line:355
                        for OO00O00O00OOOOOO0 in range (12 ):#line:356
                            id =O00OOO00O000OOOO0 [OO00O00O00OOOOOO0 ]['level']#line:357
                            if float (OO0000OOO00000O00 )-float (id )>9 :#line:358
                                O0O0000000O00O0O0 =f'_site={OO00O00O00OOOOOO0}_{timi_new()}'#line:359
                                O0O00000O0O0O0O00 ={'accept':'application/json, text/plain, */*','authorization':O0000OO00OO0O0OO0 .token ,'timestamp':timi_new (),'sign':sign (O0O0000000O00O0O0 ),'signstring':O0O0000000O00O0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:369
                                O00OO00000OO0OOO0 ={"site":OO00O00O00OOOOOO0 }#line:370
                                OO0O0OO0O0O000O00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O00000O0O0O0O00 ,data =O00OO00000OO0OOO0 ).json ()#line:372
                                if 'status'in OO0O0OO0O0O000O00 :#line:373
                                    if OO0O0OO0O0O000O00 ['status']==200 :#line:374
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:375
                            if id !=0 :#line:376
                                for OO00OO0OOOO0OO00O in range (11 ):#line:377
                                    OOOOOO0OO0OOOOO0O =OO00OO0OOOO0OO00O +1 #line:378
                                    g =O00OOO00O000OOOO0 [OOOOOO0OO0OOOOO0O ]['level']#line:379
                                    if id ==g :#line:380
                                        O0O0O0OOO0OO0OO00 =OO00OO0OOOO0OO00O +2 #line:381
                                        if O0O0O0OOO0OO0OO00 ==OO00O00O00OOOOOO0 +1 :#line:382
                                            pass #line:383
                                        else :#line:384
                                            O0O000O0O0O0OOOO0 =OO00O00O00OOOOOO0 +1 #line:385
                                            time .sleep (random .randint (1 ,3 )/10 )#line:387
                                            O000OOO000OOOOO0O =f'_site={O0O000O0O0O0OOOO0 - 1}&targetSite={O0O0O0OOO0OO0OO00 - 1}_{timi_new()}'#line:388
                                            O000O000OOO000000 ={'accept':'application/json, text/plain, */*','authorization':O0000OO00OO0O0OO0 .token ,'timestamp':timi_new (),'sign':sign (O000OOO000OOOOO0O ),'signstring':O000OOO000OOOOO0O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:403
                                            OO00O0OO0O0OO0000 ={"site":int (O0O000O0O0O0OOOO0 -1 ),"targetSite":int (O0O0O0OOO0OO0OO00 -1 )}#line:404
                                            OO00OOO0OO0O000OO =requests .request ('post',f'{host}/game/crops/move',headers =O000O000OOO000000 ,json =OO00O0OO0O0OO0000 ).json ()#line:406
                                            if 'status'in OO00OOO0OO0O000OO :#line:407
                                                if OO00OOO0OO0O000OO ['status']==200 :#line:408
                                                    pass #line:409
                                            print ('【种植合成】:',O0O000O0O0O0OOOO0 ,O0O0O0OOO0OO0OO00 ,'合成成功')#line:411
                                            OOOO0OOO0O000O0O0 =True #line:412
                                    if OOOO0OOO0O000O0O0 :#line:413
                                        break #line:414
                                if OOOO0OOO0O000O0O0 :#line:415
                                    break #line:416
        except Exception as O0O00OO0O00O0OO0O :#line:417
            O0000OO00OO0O0OO0 .synthetic ()#line:418
    def level_new (O0000O0OO0000OOOO ):#line:421
        try :#line:422
            OOO0O0OOO0OO000O0 =f'__{timi_new()}'#line:423
            OOOO00O0O000O0000 ={'authorization':O0000O0OO0000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OOO0OO000O0 ),'signstring':OOO0O0OOO0OO000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:432
            O00O00OO0OOO0O000 =requests .request ('get',f'{host}/user',headers =OOOO00O0O000O0000 ).json ()#line:433
            if 'status'in O00O00OO0OOO0O000 :#line:434
                if O00O00OO0OOO0O000 ['status']==200 :#line:435
                    return float (O00O00OO0OOO0O000 ['data']['level'])#line:436
        except Exception as O00O0OO0OOOOO0OO0 :#line:437
            print (O00O0OO0OOOOO0OO0 )#line:438
    def propsraffle (OO0OO0O00O0O00O00 ):#line:441
        try :#line:442
            while True :#line:443
                O00O0OOO000OO0OOO =f'__{timi_new()}'#line:444
                OO000O0O000000000 ={'authorization':OO0OO0O00O0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO000OO0OOO ),'signstring':O00O0OOO000OO0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:453
                O0O000O0OO0OOO00O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO000O0O000000000 ).json ()#line:454
                if 'status'in O0O000O0OO0OOO00O :#line:456
                    if O0O000O0OO0OOO00O ['status']==200 :#line:457
                        OO0O0O00O00O00OOO =O0O000O0OO0OOO00O ['data']['rows']#line:458
                        O00000OOO0OOOOOOO =O0O000O0OO0OOO00O ['data']['vstate']#line:459
                        if OO0O0O00O00O00OOO ==5 or OO0O0O00O00O00OOO ==6 or OO0O0O00O00O00OOO ==7 :#line:460
                            O0OOOOOO00OO00OOO =O0O000O0OO0OOO00O ['data']['silver']#line:461
                            print (f'【转盘抽奖】:获得种子:{O0OOOOOO00OO00OOO}')#line:462
                        if OO0O0O00O00O00OOO ==1 or OO0O0O00O00O00OOO ==2 or OO0O0O00O00O00OOO ==3 :#line:463
                            OO0OOO0O0OOOOO000 =O0O000O0OO0OOO00O ['data']['clover']#line:464
                            print (f'【转盘抽奖】:获得三叶草:{OO0OOO0O0OOOOO000}')#line:465
                        if OO0O0O00O00O00OOO ==4 or OO0O0O00O00O00OOO ==8 :#line:466
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:467
                        if OO0O0O00O00O00OOO =='抽奖次数已用完':#line:471
                            if O00000OOO0OOOOOOO :#line:472
                                O00O0OOO000OO0OOO =f'__{timi_new()}'#line:473
                                OO000O0O000000000 ={'authorization':OO0OO0O00O0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO000OO0OOO ),'signstring':O00O0OOO000OO0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:482
                                OO00O0OO000OO0000 =requests .request ('get',f'{host}/user',headers =OO000O0O000000000 ).json ()#line:483
                                if 'status'in OO00O0OO000OO0000 :#line:484
                                    if OO00O0OO000OO0000 ['status']==200 :#line:485
                                        OO00000OO000O0OO0 =OO00O0OO000OO0000 ['data']['level']#line:486
                                        if float (OO00000OO000O0OO0 )>39 :#line:487
                                            OOO000O0O00O0OO00 =random .randint (160 ,190 )/10 #line:488
                                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{OOO000O0O00O0OO00}秒获取抽奖机会')#line:489
                                            time .sleep (OOO000O0O00O0OO00 )#line:490
                                            O00OOO00OOO0OO00O =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OO000O0O000000000 ).json ()#line:491
                                            if 'status'in O00OOO00OOO0OO00O :#line:493
                                                if O00OOO00OOO0OO00O ['status']==200 :#line:494
                                                    print (f'【转盘抽奖】:{O00OOO00OOO0OO00O["message"]}')#line:495
                                                if O00OOO00OOO0OO00O ['status']==500 :#line:496
                                                    print (f'【转盘抽奖】:{O00OOO00OOO0OO00O["message"]}')#line:497
                                                    break #line:498
                                            time .sleep (random .randint (10 ,15 )/10 )#line:499
                                        else :#line:500
                                            break #line:501
                            else :#line:502
                                break #line:503
                time .sleep (random .randint (8 ,15 )/10 )#line:504
        except Exception as O000OOOO00OOO0OOO :#line:505
            print (O000OOOO00OOO0OOO )#line:506
    def friends_invitation (OO00OO0O0OO0O000O ):#line:509
        try :#line:510
            O00000O0OO00O0000 =f'__{timi_new()}'#line:511
            OOO00O0O00OO0OO0O ={'authorization':OO00OO0O0OO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0OO00O0000 ),'signstring':O00000O0OO00O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:520
            OO0OO0O00OO00OO0O =requests .request ('get',f'{host}/friends',headers =OOO00O0O00OO0OO0O ).json ()#line:521
            if 'status'in OO0OO0O00OO00OO0O :#line:522
                if OO0OO0O00OO00OO0O ['status']==200 :#line:523
                    O000OO00000000OOO =OO0OO0O00OO00OO0O ['data']['myInviteter']#line:524
                    if O000OO00000000OOO :#line:525
                        OOO0O00O0OOOO0OO0 =O000OO00000000OOO ['user']['nickname']#line:526
                        OOO00OOOO000O000O =OO00OO0O0OO0O000O .certification ()#line:527
                        print (f'【查邀请人】:我的邀请人:{OOO0O00O0OOOO0OO0}丨实名:{OOO00OOOO000O000O}')#line:528
                    else :#line:529
                        if OO00OO0O0OO0O000O .innerId !='0':#line:530
                            O00000O0OO00O0000 =f'_innerId=1937553_{timi_new()}'#line:531
                            OOO00O0O00OO0OO0O ={'authorization':OO00OO0O0OO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0OO00O0000 ),'signstring':O00000O0OO00O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:540
                            O000OO0OOOOO0O000 ={"innerId":'1937553'}#line:541
                            O0OOOOO00OO00OOO0 =requests .request ('post',f'{host}/friends/my-invitation',headers =OOO00O0O00OO0OO0O ,data =O000OO0OOOOO0O000 ).json ()#line:543
        except Exception as OO0OO00O00O0000OO :#line:544
            print (OO0OO00O00O0000OO )#line:545
    def add_clover (OOOO0OOOOO00OOO00 ):#line:548
        global golden_seed #line:549
        try :#line:550
            OOOO00O00OO0O0O00 =f'__{timi_new()}'#line:551
            OO000OO000OO0O0OO ={'authorization':OOOO0OOOOO00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O00OO0O0O00 ),'signstring':OOOO00O00OO0O0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:560
            OOOOOOO0O00000000 =requests .request ('get',f'{host}/assets/clovers',headers =OO000OO000OO0O0OO ).json ()#line:561
            if 'status'in OOOOOOO0O00000000 :#line:563
                if OOOOOOO0O00000000 ['status']==200 :#line:564
                    O000OOOO0O0O0OO0O =OOOOOOO0O00000000 ['data']['clover']#line:565
                    O0O0O0OO000000O0O =OOOOOOO0O00000000 ['data']['used_clover']#line:566
                    O0O00OO0OO00O0000 =float (O000OOOO0O0O0OO0O )-float (O0O0O0OO000000O0O )#line:567
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0O0O0OO000000O0O}')#line:568
                    if O0O00OO0OO00O0000 >1 :#line:569
                        OOOO00O00OO0O0O00 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O00OO0OO00O0000)}_{timi_new()}'#line:570
                        OO000OO000OO0O0OO ={'authorization':OOOO0OOOOO00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O00OO0O0O00 ),'signstring':OOOO00O00OO0O0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:579
                        O00O0OOOOOO00O0OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O00OO0OO00O0000 )}#line:580
                        O0000OO0000O00000 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO000OO000OO0O0OO ,data =O00O0OOOOOO00O0OO ).json ()#line:581
                        if 'status'in O0000OO0000O00000 :#line:583
                            if O0000OO0000O00000 ['status']==200 :#line:584
                                print (f'【参与抽奖】:添加三叶草:{O0000OO0000O00000["data"]}丨数量:{O0O00OO0OO00O0000}')#line:585
                            if O0000OO0000O00000 ['status']==500 :#line:586
                                print (f'【参与抽奖】:添加三叶草::{O0000OO0000O00000["message"]}')#line:587
            OO000O000O00O00OO =requests .request ('get',f'{host}/lottery',headers =OO000OO000OO0O0OO ).json ()#line:588
            O00O0000O00000000 =OOOO0OOOOO00OOO00 .winning_rewards ()#line:590
            if 'status'in OO000O000O00O00OO :#line:591
                if OO000O000O00O00OO ['status']==200 :#line:592
                    O0OOO0OOO0O00O000 =OO000O000O00O00OO ['data'][0 ]['day_get_gold_quantity']#line:593
                    golden_seed +=float (O0OOO0OOO0O00O000 )#line:594
                    print (f'【参与抽奖】:预计每天中{O0OOO0OOO0O00O000[:6]}颗金种子丨好友收益:{str(O00O0000O00000000)[:6]}')#line:595
        except Exception as O0OOO0O0000O0OOO0 :#line:596
            print (O0OOO0O0000O0OOO0 )#line:597
    def energy (OOOO00O0O00OOO000 ):#line:600
        OOO0O000O00O000O0 =f'__{timi_new()}'#line:601
        OO0OOO0O000OO0O00 ={'authorization':OOOO00O0O00OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O00O000O0 ),'signstring':OOO0O000O00O000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:610
        OO000OOOOOOO0O00O =requests .request ('get',f'{host}/energy/general',headers =OO0OOO0O000OO0O00 ).json ()#line:611
        if 'status'in OO000OOOOOOO0O00O :#line:613
            if OO000OOOOOOO0O00O ['status']==200 :#line:614
                O00OOOOOOO000OOO0 =OO000OOOOOOO0O00O ['data']['ordinary_water_consumptions']#line:615
                if float (O00OOOOOOO000OOO0 )<80 :#line:616
                    OOOO00O000OOO0OOO =99 -float (O00OOOOOOO000OOO0 )#line:617
                    O0O00O0O000O0OOOO ={"fertilizer":str (OOOO00O000OOO0OOO ).split ('.')[0 ]}#line:618
                    O0O0O0O0O0OOO0000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0OOO0O000OO0O00 ,data =O0O00O0O000O0OOOO ).json ()#line:619
                    if 'status'in O0O0O0O0O0OOO0000 :#line:621
                        if O0O0O0O0O0OOO0000 ['status']==200 :#line:622
                            print (f'【购买肥料】:{O0O0O0O0O0OOO0000["message"]}')#line:623
                OOO0OOOOO0O0O00OO =OO000OOOOOOO0O00O ['data']['ordinary_water_consumptions']#line:624
                if float (OOO0OOOOO0O0O00OO )<800 :#line:625
                    O000OOOOO0O00O000 =999 -float (OOO0OOOOO0O0O00OO )#line:626
                    O0O00O0000000O0OO ={"water":str (O000OOOOO0O00O000 ).split ('.')[0 ]}#line:627
                    O0000O0O0O00O0OO0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0OOO0O000OO0O00 ,data =O0O00O0000000O0OO ).json ()#line:628
                    if 'status'in O0000O0O0O00O0OO0 :#line:629
                        if O0000O0O0O00O0OO0 ['status']==200 :#line:630
                            print (f'【购买水滴】:{O0000O0O0O00O0OO0["message"]}')#line:631
def version_of_the_validation ():#line:635
    return str ((67 -56 )/10 )#line:636
def gitee_validation ():#line:639
    try :#line:640
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:641
    except Exception as O0O0O0000O00OO00O :#line:642
        sys .exit (0 )#line:643
def update_the_validation ():#line:647
    try :#line:648
        OO00O000000OOO0OO =gitee_validation ()#line:649
        if version_of_the_validation ()<OO00O000000OOO0OO ['CityEarth']['edition']:#line:650
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O000000OOO0OO["CityEarth"]["edition"]}   ❌')#line:651
            print (f'更新内容=>>{OO00O000000OOO0OO["CityEarth"]["content"]}   👍')#line:652
        else :#line:653
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O000000OOO0OO["CityEarth"]["edition"]}   ✅')#line:654
            print (f'更新内容=>> {OO00O000000OOO0OO["CityEarth"]["content"]}   👍')#line:655
    except Exception as OOOO0O00O0OO0O000 :#line:656
        print (OOOO0O00O0OO0O000 )#line:657
def os_qinglong ():#line:660
    if application in os .environ :#line:661
        OOOO00O0O000OOO0O =os .environ [application ].split ('\n')#line:662
        if len (OOOO00O0O000OOO0O )>0 :#line:663
            return OOOO00O0O000OOO0O #line:664
        else :#line:665
            print (f"{application}变量未启用")#line:666
            print ('脚本退出')#line:667
            sys .exit (1 )#line:668
    else :#line:669
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:671
        return os_built ()#line:672
def os_built ():#line:675
    if token :#line:676
        OO000O0OOOOOO0000 =token .split ('\n')#line:677
        if len (OO000O0OOOOOO0000 )>0 :#line:678
            return OO000O0OOOOOO0000 #line:679
    else :#line:680
        print (f"内置变量为空")#line:681
        print ('脚本结束')#line:682
        sys .exit (0 )#line:683
if __name__ =='__main__':#line:686
    start ()#line:687
