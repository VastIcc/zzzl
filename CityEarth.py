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
token = '68058bb0-0121-4cdf-9b58-0892762d3704&5&1932634'
time_xx = random.randint(8, 12)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://scsc.sc19319.com'#line:2
golden_seed =0 #line:3
def start ():#line:4
    try :#line:5
        update_the_validation ()#line:6
        O0O00OO0000O00O0O =os_qinglong ()#line:7
        print (f"==========共找到{len(O0O00OO0000O00O0O)}个账号==========")#line:8
        for O00O00O0O0000OO0O in O0O00OO0000O00O0O :#line:9
            print (f"------------正在执行第{O0O00OO0000O00O0O.index(O00O00O0O0000OO0O) + 1}个账号------------")#line:10
            O00OO000O00OOOO00 =CityEarth (O00O00O0O0000OO0O )#line:11
            def OO0OOO000OOOOO000 ():#line:13
                if O00OO000O00OOOO00 .base_info ():#line:15
                    O00OO000O00OOOO00 .game_map ()#line:19
                    O00OO000O00OOOO00 .friends_invitation ()#line:21
                    O00OO000O00OOOO00 .add_clover ()#line:23
                    O00OO000O00OOOO00 .energy ()#line:25
                    O00OO000O00OOOO00 .propsraffle ()#line:27
                    O00OO000O00OOOO00 .synthetic ()#line:29
                    O00OO000O00OOOO00 .crops_illustrated ()#line:31
                    O00OO000O00OOOO00 .give_gold ()#line:33
                else :#line:34
                    print ('token失效')#line:35
            O00O0O0O00O000OOO =threading .Thread (target =OO0OOO000OOOOO000 )#line:37
            O00O0O0O00O000OOO .start ()#line:38
            time .sleep (time_xx )#line:39
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:41
        time .sleep (3 )#line:42
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:43
    except Exception as O0000O000O000O00O :#line:44
        print (O0000O000O000O00O )#line:45
def sign (O0O00OOO0OOOO0OOO ):#line:48
    O0OO0O0000OO0000O =hashlib .md5 (O0O00OOO0OOOO0OOO .encode ()).hexdigest ()#line:49
    OOO00O0OO00O0O00O ="scsc%^&*"+O0OO0O0000OO0000O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:50
    O000O0OOO000O0OOO =hashlib .md5 (OOO00O0OO00O0O00O .encode ()).hexdigest ()#line:51
    return O000O0OOO000O0OOO #line:52
def timi_new ():#line:55
    return str (int (time .time ()*1000 ))#line:56
class CityEarth :#line:58
    def __init__ (OO0OOO00O0OO000O0 ,O0OOO0O0O0O000OOO ):#line:60
        try :#line:61
            OO0OOO00O0OO000O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:62
            OO0OOO00O0OO000O0 .token =O0OOO0O0O0O000OOO .split ('&')[0 ]#line:63
            OO0OOO00O0OO000O0 .innerId =O0OOO0O0O0O000OOO .split ('&')[1 ]#line:64
            OO0OOO00O0OO000O0 .doneeNo =O0OOO0O0O0O000OOO .split ('&')[2 ]#line:65
        except :#line:66
            print ('变量格式错误')#line:67
    def base_info (OO0000O000O0O0O00 ):#line:70
        try :#line:71
            OOOOOO0OO0000O0O0 =f'__{timi_new()}'#line:72
            O0O000OO0OOOOOOO0 ={'authorization':OO0000O000O0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OO0000O0O0 ),'signstring':OOOOOO0OO0000O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:81
            O0O0000O0O000OOO0 =requests .request ('get',f'{host}/user',headers =O0O000OO0OOOOOOO0 ).json ()#line:82
            if 'status'in O0O0000O0O000OOO0 :#line:84
                if O0O0000O0O000OOO0 ['status']==200 :#line:85
                    OO0O0000O000O000O =O0O0000O0O000OOO0 ['data']['nickname']#line:86
                    O0OO0O00OO0OO0O00 =O0O0000O0O000OOO0 ['data']['inner_id']#line:87
                    O00O0O000000OOO0O =O0O0000O0O000OOO0 ['data']['assets']['gold']#line:88
                    O0OOOOOOO0OO00000 =O0O0000O0O000OOO0 ['data']['level']#line:89
                    print (f'【账号信息】:昵称:{OO0O0000O000O000O[:5]}丨ID:{O0OO0O00OO0OO0O00}丨等级:{O0OOOOOOO0OO00000}丨种子:{str(O00O0O000000OOO0O).split(".")[0]}')#line:90
                if O0O0000O0O000OOO0 ['status']==401 :#line:91
                    return False #line:92
                if O0O0000O0O000OOO0 ['status']==500 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as OOOO00OO000000O0O :#line:96
            print (OOOO00OO000000O0O )#line:97
    def game_map (OOO0O000O0OOOOO0O ):#line:100
        O0O0OOOOOO00000OO =f'__{timi_new()}'#line:101
        OOO0OOO00O0000O00 ={'authorization':OOO0O000O0OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOOOO00000OO ),'signstring':O0O0OOOOOO00000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:110
        O00OOOOO00O000000 =requests .request ('get',f'{host}/game/map',headers =OOO0OOO00O0000O00 ).json ()#line:111
        if 'status'in O00OOOOO00O000000 :#line:113
            if O00OOOOO00O000000 ['status']==200 :#line:114
                for OOO00OOO000O0000O in O00OOOOO00O000000 ['data']['list'][0 ]['crops']:#line:115
                    OOO00000O00OOOOOO =OOO00OOO000O0000O ['level']#line:117
                    if OOO00000O00OOOOOO ==41 :#line:118
                        O00OO0O00OOO0O00O =OOO00OOO000O0000O ['crop_name']#line:119
                        O00O0000O0O00O00O =OOO00OOO000O0000O ['count']#line:120
                        if O00O0000O0O00O00O >0 :#line:121
                            print (f'【农业资产】:{O00OO0O00OOO0O00O}丨数量:{O00O0000O0O00O00O}')#line:122
    def give_gold (O0OOO0O0OO0OO0O0O ):#line:125
        O000OOOOO00O000OO =f'__{timi_new()}'#line:126
        OO00OOOOO0OO00000 ={'authorization':O0OOO0O0OO0OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOO00O000OO ),'signstring':O000OOOOO00O000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:135
        O000O0000OO0OO00O =requests .request ('get',f'{host}/user',headers =OO00OOOOO0OO00000 ).json ()#line:136
        if 'status'in O000O0000OO0OO00O :#line:137
            if O000O0000OO0OO00O ['status']==200 :#line:138
                if float (O0OOO0O0OO0OO0O0O .doneeNo )!=0 :#line:139
                    O0O000O00O00OO0OO =O000O0000OO0OO00O ['data']['assets']['gold']#line:140
                    if float (O0O000O00O00OO0OO )>float (O0OOO0O0OO0OO0O0O .innerId ):#line:141
                        O00OO000OOO00O0OO =int (float (O0O000O00O00OO0OO )/1.1 )#line:142
                        O000OOOOO00O000OO =f'_doneeNo={O0OOO0O0OO0OO0O0O.doneeNo}&quantity={O00OO000OOO00O0OO}_{timi_new()}'#line:143
                        OO00OOOOO0OO00000 ={'authorization':O0OOO0O0OO0OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOO00O000OO ),'signstring':O000OOOOO00O000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:152
                        O0OO0O00O00O00O0O ={"quantity":O00OO000OOO00O0OO ,"doneeNo":O0OOO0O0OO0OO0O0O .doneeNo }#line:156
                        OOOOOO0O0OO0O00OO =requests .request ('post',f'{host}/finance/give-gold',headers =OO00OOOOO0OO00000 ,data =O0OO0O00O00O00O0O ).json ()#line:157
                        if 'status'in OOOOOO0O0OO0O00OO :#line:159
                            if OOOOOO0O0OO0O00OO ['status']==200 :#line:160
                                if OOOOOO0O0OO0O00OO ['data']:#line:161
                                    print (f'【赠送种子】:赠送{O00OO000OOO00O0OO}种子给{O0OOO0O0OO0OO0O0O.doneeNo}成功')#line:162
                else :#line:163
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:164
    def winning_rewards (O0OOOO000O0O0O00O ):#line:167
        OOOOOOO00O0O0O0O0 =f'__{timi_new()}'#line:168
        O0OOOO0OO0000O0O0 ={'authorization':O0OOOO000O0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO00O0O0O0O0 ),'signstring':OOOOOOO00O0O0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:177
        O0000O00O00OO00O0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOOO0OO0000O0O0 ).json ()#line:178
        if 'status'in O0000O00O00OO00O0 :#line:180
            if O0000O00O00OO00O0 ['status']==200 :#line:181
                if O0000O00O00OO00O0 ['data']['amount']:#line:182
                    OO000OO0OO00O0O00 =O0000O00O00OO00O0 ['data']['amount']['gold']#line:183
                    return OO000OO0OO00O0O00 #line:184
                else :#line:185
                    return 0 #line:186
    def certification (O00OO0O00O000OOO0 ):#line:189
        OOO0OO0O000O000O0 =f'__{timi_new()}'#line:190
        O000O0O0O00OO0O00 ={'authorization':O00OO0O00O000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O000O000O0 ),'signstring':OOO0OO0O000O000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:199
        O000O0O0000OOO0OO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O000O0O0O00OO0O00 ).json ()#line:200
        if 'status'in O000O0O0000OOO0OO :#line:202
            if O000O0O0000OOO0OO ['status']==200 :#line:203
                if O000O0O0000OOO0OO ['data']['result']:#line:204
                    O00OOOOO0000OOOO0 =O000O0O0000OOO0OO ['data']['nick_name']#line:205
                    return O00OOOOO0000OOOO0 #line:206
                else :#line:207
                    return '未实名'#line:208
    def crops_illustrated (OO0OOOO0OO00O0000 ):#line:211
        O0OO00O000OO0OOOO =f'__{timi_new()}'#line:212
        OO0OO0OO000O0O0O0 ={'authorization':OO0OOOO0OO00O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O000OO0OOOO ),'signstring':O0OO00O000OO0OOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:221
        OOO00OO0OOO00O0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0OO0OO000O0O0O0 ).json ()#line:222
        if 'status'in OOO00OO0OOO00O0O0 :#line:224
            if OOO00OO0OOO00O0O0 ['status']==200 :#line:225
                OOOO0O0OO000OO000 =OOO00OO0OOO00O0O0 ['data'][0 ]['crops']#line:226
                for OO000000000000OOO in OOOO0O0OO000OO000 :#line:227
                    if OO000000000000OOO ['ill_clover_award']:#line:228
                        if float (OO000000000000OOO ['ill_clover_award'])>1 :#line:229
                            if OO000000000000OOO ['is_finish']:#line:230
                                if not OO000000000000OOO ['is_getit']:#line:231
                                    O0OO00O000OO0OOOO =f'_award_level={OO000000000000OOO["level"]}_{timi_new()}'#line:232
                                    OO0OO0OO000O0O0O0 ={'authorization':OO0OOOO0OO00O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O000OO0OOOO ),'signstring':O0OO00O000OO0OOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:241
                                    OOO000O00O000OO0O ={"award_level":OO000000000000OOO ['level']}#line:242
                                    O0O0O0OOOO00OOOO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0OO0OO000O0O0O0 ,json =OOO000O00O000OO0O ).json ()#line:244
                                    if 'status'in O0O0O0OOOO00OOOO0 :#line:245
                                        if O0O0O0OOOO00OOOO0 ['status']==200 :#line:246
                                            O00000000O0000OO0 =O0O0O0OOOO00OOOO0 ['data']['ill_clover_award']#line:247
                                            print (f'【图鉴奖励】:领取{OO000000000000OOO["crop_name"]}成就丨奖励{O00000000O0000OO0}叶子成功')#line:249
                                        if O0O0O0OOOO00OOOO0 ['status']==500 :#line:250
                                            print (f'【图鉴奖励】:{O0O0O0OOOO00OOOO0["message"]}')#line:251
    def watched_ad (O000O000OO0OOO000 ):#line:254
        OO00OO00O000O0000 =f'__{timi_new()}'#line:255
        OOOOOOO0OOOO0000O ={'authorization':O000O000OO0OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO00O000O0000 ),'signstring':OO00OO00O000O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:264
        O00OOOOO0OO0OOOOO =requests .request ('post',f'{host}/game/watched-ad',headers =OOOOOOO0OOOO0000O ).json ()#line:265
        print (O00OOOOO0OO0OOOOO )#line:266
    def user_ad (OO00O00OOOOO00O00 ):#line:269
        O00O0O0000OO0OO0O =f'__{timi_new()}'#line:270
        OOO000O0000O0O00O ={'authorization':OO00O00OOOOO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0000OO0OO0O ),'signstring':O00O0O0000OO0OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:279
        O0O0OO0O00OOO00O0 =requests .request ('get',f'{host}/user/ad',headers =OOO000O0000O0O00O ).json ()#line:280
        if 'status'in O0O0OO0O00OOO00O0 :#line:282
            if O0O0OO0O00OOO00O0 ['status']==200 :#line:283
                OO0OOO0O0OOOOO00O =O0O0OO0O00OOO00O0 ['data']['max_time']#line:284
                O00000OO0O0O0O0O0 =O0O0OO0O00OOO00O0 ['data']['watch_time']#line:285
                O000OO0OOO00O0000 =O0O0OO0O00OOO00O0 ['data']['added_time']#line:286
                print (f'【获取种子】:获取种子剩余{O000OO0OOO00O0000 + OO0OOO0O0OOOOO00O - O00000OO0O0O0O0O0}次丨好友提供:{O000OO0OOO00O0000}次')#line:287
                if O000OO0OOO00O0000 +OO0OOO0O0OOOOO00O -O00000OO0O0O0O0O0 >0 :#line:288
                    time .sleep (random .randint (16 ,19 ))#line:289
                    O0O000OO00O000O00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO000O0000O0O00O ).json ()#line:290
                    if 'status'in O0O000OO00O000O00 :#line:292
                        if O0O000OO00O000O00 ['status']==200 :#line:293
                            OOOO000OOOOO00000 =O0O000OO00O000O00 ['data']['silver']#line:294
                            print (f'【获取种子】:获得种子:{OOOO000OOOOO00000}')#line:295
                            return True #line:296
                        if O0O000OO00O000O00 ['status']==500 :#line:297
                            OOO0OOO00O00000OO =O0O000OO00O000O00 ['message']#line:298
                            print (f'【获取种子】:{OOO0OOO00O00000OO}')#line:299
                            return False #line:300
    def synthetic (OOO0O0OO0OOOO00O0 ):#line:303
        global id ,g #line:304
        try :#line:305
            OOO00000OO00O0000 =OOO0O0OO0OOOO00O0 .level_new ()#line:306
            while True :#line:307
                OOO00O0OOOOOOOO00 =f'__{timi_new()}'#line:308
                O0OO000O00OO0O0O0 ={'authorization':OOO0O0OO0OOOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OOOOOOOO00 ),'signstring':OOO00O0OOOOOOOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:317
                OOOO0O000OO0OOOOO =requests .request ('get',f'{host}/game/getAllData',headers =O0OO000O00OO0O0O0 ).json ()#line:318
                if 'status'in OOOO0O000OO0OOOOO :#line:320
                    if OOOO0O000OO0OOOOO ['status']==200 :#line:321
                        O0O0OOO00O00O0O00 =OOOO0O000OO0OOOOO ['data']['cropList']#line:322
                        OOOOOO00OO00000O0 =OOOO0O000OO0OOOOO ['data']['gameCoreDataDBid']#line:323
                        O000000OOOO00O00O =0 #line:324
                        for OOOOO0O0O00O00OOO in O0O0OOO00O00O0O00 :#line:325
                            if not OOOOO0O0O00O00OOO :#line:326
                                OO0O0OO00000O0O00 =f'_crop_id={OOOOOO00OO00000O0}&site={O000000OOOO00O00O}_{OOO0O0OO0OOOO00O0.time}'#line:327
                                OO0O0O0O0O0OO0OO0 ={'authorization':OOO0O0OO0OOOO00O0 .token ,'timestamp':OOO0O0OO0OOOO00O0 .time ,'sign':sign (OO0O0OO00000O0O00 ),'signstring':OO0O0OO00000O0O00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:336
                                O0OOOOOOOOO0OOO0O ={"site":O000000OOOO00O00O ,"crop_id":OOOOOO00OO00000O0 }#line:337
                                OO000O0O000OO0OOO =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O0O0O0O0OO0OO0 ,data =O0OOOOOOOOO0OOO0O ).json ()#line:338
                                time .sleep (random .randint (1 ,3 )/10 )#line:340
                                if 'status'in OO000O0O000OO0OOO :#line:341
                                    if OO000O0O000OO0OOO ['status']==200 :#line:342
                                        if OO000O0O000OO0OOO ['message']=='种子数量不足':#line:343
                                            OOO00000OO00O0000 =OOO0O0OO0OOOO00O0 .level_new ()#line:344
                                            print (f'【种植合成】:{OO000O0O000OO0OOO["message"]}')#line:345
                                            if not OOO0O0OO0OOOO00O0 .user_ad ():#line:346
                                                return False #line:347
                                        print (f'【种植合成】:种植农作物,位置{O000000OOOO00O00O}')#line:348
                                    if OO000O0O000OO0OOO ['status']==500 :#line:349
                                        print (f'【种植合成】:{OO000O0O000OO0OOO["message"]}')#line:350
                                        return False #line:351
                            O000000OOOO00O00O +=1 #line:352
                        OO00OO0000OO0OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO000O00OO0O0O0 ).json ()#line:353
                        OOOO00OOOO0OO000O =OO00OO0000OO0OOO0 ['data']['cropList']#line:354
                        O0O000OO000O0O00O =False #line:355
                        for OOOOO0O0O00O00OOO in range (12 ):#line:356
                            id =OOOO00OOOO0OO000O [OOOOO0O0O00O00OOO ]['level']#line:357
                            if float (OOO00000OO00O0000 )-float (id )>9 :#line:358
                                OOOOO0O0O0O0OO000 =f'_site={OOOOO0O0O00O00OOO}_{timi_new()}'#line:359
                                O000O0OOOO0O000O0 ={'accept':'application/json, text/plain, */*','authorization':OOO0O0OO0OOOO00O0 .token ,'timestamp':timi_new (),'sign':sign (OOOOO0O0O0O0OO000 ),'signstring':OOOOO0O0O0O0OO000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:369
                                O0OO0O000OOOOOOOO ={"site":OOOOO0O0O00O00OOO }#line:370
                                O0OOO0O000OOOOO00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000O0OOOO0O000O0 ,data =O0OO0O000OOOOOOOO ).json ()#line:372
                                if 'status'in O0OOO0O000OOOOO00 :#line:373
                                    if O0OOO0O000OOOOO00 ['status']==200 :#line:374
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:375
                            if id !=0 :#line:376
                                for OOOO00OO000OOOOOO in range (11 ):#line:377
                                    OO0O00000000OOOOO =OOOO00OO000OOOOOO +1 #line:378
                                    g =OOOO00OOOO0OO000O [OO0O00000000OOOOO ]['level']#line:379
                                    if id ==g :#line:380
                                        O00O0OO0O00O0O000 =OOOO00OO000OOOOOO +2 #line:381
                                        if O00O0OO0O00O0O000 ==OOOOO0O0O00O00OOO +1 :#line:382
                                            pass #line:383
                                        else :#line:384
                                            OO00O0O0OOOO0000O =OOOOO0O0O00O00OOO +1 #line:385
                                            time .sleep (random .randint (1 ,3 )/10 )#line:387
                                            OOOO0OO00O000O0O0 =f'_site={OO00O0O0OOOO0000O - 1}&targetSite={O00O0OO0O00O0O000 - 1}_{timi_new()}'#line:388
                                            OOOO0OO0000OOO0OO ={'accept':'application/json, text/plain, */*','authorization':OOO0O0OO0OOOO00O0 .token ,'timestamp':timi_new (),'sign':sign (OOOO0OO00O000O0O0 ),'signstring':OOOO0OO00O000O0O0 ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:403
                                            O0OO0OOOO0OO0OOOO ={"site":int (OO00O0O0OOOO0000O -1 ),"targetSite":int (O00O0OO0O00O0O000 -1 )}#line:404
                                            O0O0O0OO000OOOOOO =requests .request ('post',f'{host}/game/crops/move',headers =OOOO0OO0000OOO0OO ,json =O0OO0OOOO0OO0OOOO ).json ()#line:406
                                            if 'status'in O0O0O0OO000OOOOOO :#line:407
                                                if O0O0O0OO000OOOOOO ['status']==200 :#line:408
                                                    pass #line:409
                                            print ('【种植合成】:',OO00O0O0OOOO0000O ,O00O0OO0O00O0O000 ,'合成成功')#line:411
                                            O0O000OO000O0O00O =True #line:412
                                    if O0O000OO000O0O00O :#line:413
                                        break #line:414
                                if O0O000OO000O0O00O :#line:415
                                    break #line:416
        except Exception as OO000000000OO0O0O :#line:417
            OOO0O0OO0OOOO00O0 .synthetic ()#line:418
    def level_new (O000OOO0OO0000000 ):#line:421
        try :#line:422
            O0O00OO0OO0000OO0 =f'__{timi_new()}'#line:423
            O0OO0OO000O0O00O0 ={'authorization':O000OOO0OO0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0OO0000OO0 ),'signstring':O0O00OO0OO0000OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:432
            O00000OO0OO0O0OOO =requests .request ('get',f'{host}/user',headers =O0OO0OO000O0O00O0 ).json ()#line:433
            if 'status'in O00000OO0OO0O0OOO :#line:434
                if O00000OO0OO0O0OOO ['status']==200 :#line:435
                    return float (O00000OO0OO0O0OOO ['data']['level'])#line:436
        except Exception as O0000OO0O000OOOOO :#line:437
            print (O0000OO0O000OOOOO )#line:438
    def propsraffle (O00O00000OO00OOO0 ):#line:441
        try :#line:442
            while True :#line:443
                O00O0OO00OOOO0O00 =f'__{timi_new()}'#line:444
                OOOOO0O0OO0OOO00O ={'authorization':O00O00000OO00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO00OOOO0O00 ),'signstring':O00O0OO00OOOO0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:453
                OOOO00OO0O0OOOO0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOOO0O0OO0OOO00O ).json ()#line:454
                if 'status'in OOOO00OO0O0OOOO0O :#line:456
                    if OOOO00OO0O0OOOO0O ['status']==200 :#line:457
                        O0O0000OOOOO0OOO0 =OOOO00OO0O0OOOO0O ['data']['rows']#line:458
                        OO000O0OO0OO0OOO0 =OOOO00OO0O0OOOO0O ['data']['vstate']#line:459
                        if O0O0000OOOOO0OOO0 ==5 or O0O0000OOOOO0OOO0 ==6 or O0O0000OOOOO0OOO0 ==7 :#line:460
                            O000OO0000OOO000O =OOOO00OO0O0OOOO0O ['data']['silver']#line:461
                            print (f'【转盘抽奖】:获得种子:{O000OO0000OOO000O}')#line:462
                        if O0O0000OOOOO0OOO0 ==1 or O0O0000OOOOO0OOO0 ==2 or O0O0000OOOOO0OOO0 ==3 :#line:463
                            OOOOO0OO00OO0000O =OOOO00OO0O0OOOO0O ['data']['clover']#line:464
                            print (f'【转盘抽奖】:获得三叶草:{OOOOO0OO00OO0000O}')#line:465
                        if O0O0000OOOOO0OOO0 ==4 or O0O0000OOOOO0OOO0 ==8 :#line:466
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:467
                        if O0O0000OOOOO0OOO0 =='抽奖次数已用完':#line:471
                            if OO000O0OO0OO0OOO0 :#line:472
                                O00O0OO00OOOO0O00 =f'__{timi_new()}'#line:473
                                OOOOO0O0OO0OOO00O ={'authorization':O00O00000OO00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO00OOOO0O00 ),'signstring':O00O0OO00OOOO0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:482
                                OO00OOO00OO000OO0 =requests .request ('get',f'{host}/user',headers =OOOOO0O0OO0OOO00O ).json ()#line:483
                                if 'status'in OO00OOO00OO000OO0 :#line:484
                                    if OO00OOO00OO000OO0 ['status']==200 :#line:485
                                        O0O0O0O00OO000OO0 =OO00OOO00OO000OO0 ['data']['level']#line:486
                                        if float (O0O0O0O00OO000OO0 )>39 :#line:487
                                            O0OO0O00O0OOOOO00 =random .randint (160 ,190 )/10 #line:488
                                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{O0OO0O00O0OOOOO00}秒获取抽奖机会')#line:489
                                            time .sleep (O0OO0O00O0OOOOO00 )#line:490
                                            OOOOO0000O0O0000O =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OOOOO0O0OO0OOO00O ).json ()#line:491
                                            if 'status'in OOOOO0000O0O0000O :#line:493
                                                if OOOOO0000O0O0000O ['status']==200 :#line:494
                                                    print (f'【转盘抽奖】:{OOOOO0000O0O0000O["message"]}')#line:495
                                                if OOOOO0000O0O0000O ['status']==500 :#line:496
                                                    print (f'【转盘抽奖】:{OOOOO0000O0O0000O["message"]}')#line:497
                                                    break #line:498
                                            time .sleep (random .randint (10 ,15 )/10 )#line:499
                                        else :#line:500
                                            break #line:501
                            else :#line:502
                                break #line:503
                time .sleep (random .randint (8 ,15 )/10 )#line:504
        except Exception as OOOOOOO0O0OO00OO0 :#line:505
            print (OOOOOOO0O0OO00OO0 )#line:506
    def friends_invitation (O0000OOOO0OOO0OO0 ):#line:509
        try :#line:510
            O0O0O0O0OO0O0000O =f'__{timi_new()}'#line:511
            OO0O0O0O00O0OO00O ={'authorization':O0000OOOO0OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0OO0O0000O ),'signstring':O0O0O0O0OO0O0000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:520
            OO00OO0OOOO0OOO0O =requests .request ('get',f'{host}/friends',headers =OO0O0O0O00O0OO00O ).json ()#line:521
            if 'status'in OO00OO0OOOO0OOO0O :#line:522
                if OO00OO0OOOO0OOO0O ['status']==200 :#line:523
                    OOO00O00OOO0OO0OO =OO00OO0OOOO0OOO0O ['data']['myInviteter']#line:524
                    if OOO00O00OOO0OO0OO :#line:525
                        O0O0O0OO0O0O0O0OO =OOO00O00OOO0OO0OO ['user']['nickname']#line:526
                        OO0O0O0OOO000O0O0 =O0000OOOO0OOO0OO0 .certification ()#line:527
                        print (f'【查邀请人】:我的邀请人:{O0O0O0OO0O0O0O0OO}丨实名:{OO0O0O0OOO000O0O0}')#line:528
                    else :#line:529
                        if O0000OOOO0OOO0OO0 .innerId !='0':#line:530
                            O0O0O0O0OO0O0000O =f'_innerId=1937553{timi_new()}'#line:531
                            OO0O0O0O00O0OO00O ={'authorization':O0000OOOO0OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0OO0O0000O ),'signstring':O0O0O0O0OO0O0000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:540
                            O00OO0O00OOOO0OOO ={"innerId":'1937008'}#line:541
                            O0O00OO00O0O0OO0O =requests .request ('post',f'{host}/friends/my-invitation',headers =OO0O0O0O00O0OO00O ,data =O00OO0O00OOOO0OOO ).json ()#line:543
        except Exception as O00OOOO0O0OO00OO0 :#line:544
            print (O00OOOO0O0OO00OO0 )#line:545
    def add_clover (OO00OO0O0OO000OOO ):#line:548
        global golden_seed #line:549
        try :#line:550
            O00000OO0OOOO0OOO =f'__{timi_new()}'#line:551
            O0O0OOO0OOO0O00OO ={'authorization':OO00OO0O0OO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO0OOOO0OOO ),'signstring':O00000OO0OOOO0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:560
            OOOOOOO0OO000OOO0 =requests .request ('get',f'{host}/assets/clovers',headers =O0O0OOO0OOO0O00OO ).json ()#line:561
            if 'status'in OOOOOOO0OO000OOO0 :#line:563
                if OOOOOOO0OO000OOO0 ['status']==200 :#line:564
                    O00OO0000O0OOOOO0 =OOOOOOO0OO000OOO0 ['data']['clover']#line:565
                    OOO00O00OOO00OO00 =OOOOOOO0OO000OOO0 ['data']['used_clover']#line:566
                    OO0OOO0OO00OOO0OO =float (O00OO0000O0OOOOO0 )-float (OOO00O00OOO00OO00 )#line:567
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OOO00O00OOO00OO00}')#line:568
                    if OO00OO0O0OO000OOO .certification ()!='未实名':#line:569
                        if OO0OOO0OO00OOO0OO >1 :#line:570
                            O00000OO0OOOO0OOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0OOO0OO00OOO0OO)}_{timi_new()}'#line:571
                            O0O0OOO0OOO0O00OO ={'authorization':OO00OO0O0OO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO0OOOO0OOO ),'signstring':O00000OO0OOOO0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:580
                            O0OO00000000000OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0OOO0OO00OOO0OO )}#line:581
                            OO0O0OOOO00O00000 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O0OOO0OOO0O00OO ,data =O0OO00000000000OO ).json ()#line:582
                            if 'status'in OO0O0OOOO00O00000 :#line:584
                                if OO0O0OOOO00O00000 ['status']==200 :#line:585
                                    print (f'【参与抽奖】:添加三叶草:{OO0O0OOOO00O00000["data"]}丨数量:{OO0OOO0OO00OOO0OO}')#line:586
                                if OO0O0OOOO00O00000 ['status']==500 :#line:587
                                    print (f'【参与抽奖】:添加三叶草:{OO0O0OOOO00O00000["message"]}')#line:588
            OOO0OOO000OO0O0O0 =requests .request ('get',f'{host}/lottery',headers =O0O0OOO0OOO0O00OO ).json ()#line:589
            O0000OO0O0OO00O00 =OO00OO0O0OO000OOO .winning_rewards ()#line:591
            if 'status'in OOO0OOO000OO0O0O0 :#line:592
                if OOO0OOO000OO0O0O0 ['status']==200 :#line:593
                    OO00OOOOO00O0O0O0 =OOO0OOO000OO0O0O0 ['data'][0 ]['day_get_gold_quantity']#line:594
                    golden_seed +=float (OO00OOOOO00O0O0O0 )#line:595
                    print (f'【参与抽奖】:预计每天中{OO00OOOOO00O0O0O0[:6]}颗金种子丨好友收益:{str(O0000OO0O0OO00O00)[:6]}')#line:596
        except Exception as O0OOOOO000O0O0O0O :#line:597
            print (O0OOOOO000O0O0O0O )#line:598
    def energy (O000O00OO0O000000 ):#line:601
        O000000OO000OOOOO =f'__{timi_new()}'#line:602
        OOO0O0OO0000O0OO0 ={'authorization':O000O00OO0O000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000OO000OOOOO ),'signstring':O000000OO000OOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:611
        O0000OO0OOO000O0O =requests .request ('get',f'{host}/energy/general',headers =OOO0O0OO0000O0OO0 ).json ()#line:612
        if 'status'in O0000OO0OOO000O0O :#line:614
            if O0000OO0OOO000O0O ['status']==200 :#line:615
                OO00O0OOOOOO000OO =O0000OO0OOO000O0O ['data']['ordinary_water_consumptions']#line:616
                if float (OO00O0OOOOOO000OO )<80 :#line:617
                    OOO0O0OOOO0OOO000 =99 -float (OO00O0OOOOOO000OO )#line:618
                    O0OOOO000O000000O ={"fertilizer":str (OOO0O0OOOO0OOO000 ).split ('.')[0 ]}#line:619
                    OO0O0O0OO0OO00000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO0O0OO0000O0OO0 ,data =O0OOOO000O000000O ).json ()#line:620
                    if 'status'in OO0O0O0OO0OO00000 :#line:622
                        if OO0O0O0OO0OO00000 ['status']==200 :#line:623
                            print (f'【购买肥料】:{OO0O0O0OO0OO00000["message"]}')#line:624
                O0OO0OO00OO00OO0O =O0000OO0OOO000O0O ['data']['ordinary_water_consumptions']#line:625
                if float (O0OO0OO00OO00OO0O )<800 :#line:626
                    OOO000O000O000000 =999 -float (O0OO0OO00OO00OO0O )#line:627
                    O000OO0O0OOOOO00O ={"water":str (OOO000O000O000000 ).split ('.')[0 ]}#line:628
                    OO0O0OOO00OOOO000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO0O0OO0000O0OO0 ,data =O000OO0O0OOOOO00O ).json ()#line:629
                    if 'status'in OO0O0OOO00OOOO000 :#line:630
                        if OO0O0OOO00OOOO000 ['status']==200 :#line:631
                            print (f'【购买水滴】:{OO0O0OOO00OOOO000["message"]}')#line:632
def version_of_the_validation ():#line:636
    return str ((67 -56 )/10 )#line:637
def gitee_validation ():#line:640
    try :#line:641
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:642
    except Exception as O0OO00O00OO0OO0O0 :#line:643
        sys .exit (0 )#line:644
def update_the_validation ():#line:648
    try :#line:649
        OO0000OO0O0O0OOOO =gitee_validation ()#line:650
        if version_of_the_validation ()<OO0000OO0O0O0OOOO ['CityEarth']['edition']:#line:651
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0000OO0O0O0OOOO["CityEarth"]["edition"]}   ❌')#line:652
            print (f'更新内容=>>{OO0000OO0O0O0OOOO["CityEarth"]["content"]}   👍')#line:653
        else :#line:654
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0000OO0O0O0OOOO["CityEarth"]["edition"]}   ✅')#line:655
            print (f'更新内容=>> {OO0000OO0O0O0OOOO["CityEarth"]["content"]}   👍')#line:656
    except Exception as OO0OO0O00OOO0000O :#line:657
        print (OO0OO0O00OOO0000O )#line:658
def os_qinglong ():#line:661
    if application in os .environ :#line:662
        OO0OO0O0O0000OO0O =os .environ [application ].split ('\n')#line:663
        if len (OO0OO0O0O0000OO0O )>0 :#line:664
            return OO0OO0O0O0000OO0O #line:665
        else :#line:666
            print (f"{application}变量未启用")#line:667
            print ('脚本退出')#line:668
            sys .exit (1 )#line:669
    else :#line:670
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:672
        return os_built ()#line:673
def os_built ():#line:676
    if token :#line:677
        OO0O0O000OO0OOOOO =token .split ('\n')#line:678
        if len (OO0O0O000OO0OOOOO )>0 :#line:679
            return OO0O0O000OO0OOOOO #line:680
    else :#line:681
        print (f"内置变量为空")#line:682
        print ('脚本结束')#line:683
        sys .exit (0 )#line:684
if __name__ =='__main__':#line:687
    start ()#line:688
