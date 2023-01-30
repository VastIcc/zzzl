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
        O00000O0O0O000OOO =os_qinglong ()#line:7
        print (f"==========共找到{len(O00000O0O0O000OOO)}个账号==========")#line:8
        for O000O000O0OOOOOOO in O00000O0O0O000OOO :#line:9
            print (f"------------正在执行第{O00000O0O0O000OOO.index(O000O000O0OOOOOOO) + 1}个账号------------")#line:10
            OOOO00OOO00OOO00O =CityEarth (O000O000O0OOOOOOO )#line:11
            def O0O00O000O00000OO ():#line:13
                if OOOO00OOO00OOO00O .base_info ():#line:15
                    OOOO00OOO00OOO00O .game_map ()#line:19
                    OOOO00OOO00OOO00O .friends_invitation ()#line:21
                    OOOO00OOO00OOO00O .add_clover ()#line:23
                    OOOO00OOO00OOO00O .energy ()#line:25
                    OOOO00OOO00OOO00O .propsraffle ()#line:27
                    OOOO00OOO00OOO00O .synthetic ()#line:29
                    OOOO00OOO00OOO00O .crops_illustrated ()#line:31
                    OOOO00OOO00OOO00O .give_gold ()#line:33
                else :#line:34
                    print ('token失效')#line:35
            OOOOOOOO00OO0O0O0 =threading .Thread (target =O0O00O000O00000OO )#line:37
            OOOOOOOO00OO0O0O0 .start ()#line:38
            time .sleep (time_xx )#line:39
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:41
        time .sleep (3 )#line:42
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:43
    except Exception as O0O0O00O00OO0OOOO :#line:44
        print (O0O0O00O00OO0OOOO )#line:45
def sign (OOOO0O0000O0OO0OO ):#line:48
    O000O00O0OO0OO00O =hashlib .md5 (OOOO0O0000O0OO0OO .encode ()).hexdigest ()#line:49
    OO0O0OO00O000OOOO ="scsc%^&*"+O000O00O0OO0OO00O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:50
    O0O0O00OO0OO0OOOO =hashlib .md5 (OO0O0OO00O000OOOO .encode ()).hexdigest ()#line:51
    return O0O0O00OO0OO0OOOO #line:52
def timi_new ():#line:55
    return str (int (time .time ()*1000 ))#line:56
class CityEarth :#line:58
    def __init__ (O0O0O000000O0OO0O ,OO0000O000OOO0OO0 ):#line:60
        try :#line:61
            O0O0O000000O0OO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:62
            O0O0O000000O0OO0O .token =OO0000O000OOO0OO0 .split ('&')[0 ]#line:63
            O0O0O000000O0OO0O .innerId =OO0000O000OOO0OO0 .split ('&')[1 ]#line:64
            O0O0O000000O0OO0O .doneeNo =OO0000O000OOO0OO0 .split ('&')[2 ]#line:65
        except :#line:66
            print ('变量格式错误')#line:67
    def base_info (OO00OO0O00OO0000O ):#line:70
        try :#line:71
            O0OO0O0OOOOOO00OO =f'__{timi_new()}'#line:72
            OO0OO0O00000OO0O0 ={'authorization':OO00OO0O00OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0OOOOOO00OO ),'signstring':O0OO0O0OOOOOO00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:81
            OO0OOOOOO00O000OO =requests .request ('get',f'{host}/user',headers =OO0OO0O00000OO0O0 ).json ()#line:82
            if 'status'in OO0OOOOOO00O000OO :#line:84
                if OO0OOOOOO00O000OO ['status']==200 :#line:85
                    O00O000O0OOO0O0OO =OO0OOOOOO00O000OO ['data']['nickname']#line:86
                    O0OOO000OO0000OOO =OO0OOOOOO00O000OO ['data']['inner_id']#line:87
                    OOO0O0O0OOOOO0OOO =OO0OOOOOO00O000OO ['data']['assets']['gold']#line:88
                    OOOOO0OO0000OOOO0 =OO0OOOOOO00O000OO ['data']['level']#line:89
                    print (f'【账号信息】:昵称:{O00O000O0OOO0O0OO[:5]}丨ID:{O0OOO000OO0000OOO}丨等级:{OOOOO0OO0000OOOO0}丨种子:{str(OOO0O0O0OOOOO0OOO).split(".")[0]}')#line:90
                if OO0OOOOOO00O000OO ['status']==401 :#line:91
                    return False #line:92
                if OO0OOOOOO00O000OO ['status']==500 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as O0O0OOOO00O00000O :#line:96
            print (O0O0OOOO00O00000O )#line:97
    def game_map (O0OO0O0OOOO0OO0OO ):#line:100
        OOO0OOO0O0O0O000O =f'__{timi_new()}'#line:101
        O0O0OO0000O0O0O00 ={'authorization':O0OO0O0OOOO0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0O0O0O000O ),'signstring':OOO0OOO0O0O0O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:110
        OOO0OO0O000OO0000 =requests .request ('get',f'{host}/game/map',headers =O0O0OO0000O0O0O00 ).json ()#line:111
        if 'status'in OOO0OO0O000OO0000 :#line:113
            if OOO0OO0O000OO0000 ['status']==200 :#line:114
                for OO0O00OOO0OOOOO0O in OOO0OO0O000OO0000 ['data']['list'][0 ]['crops']:#line:115
                    O00000O000OO00OO0 =OO0O00OOO0OOOOO0O ['level']#line:117
                    if O00000O000OO00OO0 ==41 :#line:118
                        O000OOO0000000OOO =OO0O00OOO0OOOOO0O ['crop_name']#line:119
                        OO00OOO0O00OOO00O =OO0O00OOO0OOOOO0O ['count']#line:120
                        if OO00OOO0O00OOO00O >0 :#line:121
                            print (f'【农业资产】:{O000OOO0000000OOO}丨数量:{OO00OOO0O00OOO00O}')#line:122
    def give_gold (O0OOOO000OOOO0000 ):#line:125
        OO0OOOO000OO00OO0 =f'__{timi_new()}'#line:126
        OOO0000O00OO00O0O ={'authorization':O0OOOO000OOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO000OO00OO0 ),'signstring':OO0OOOO000OO00OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:135
        OOOO000O0O0OO0000 =requests .request ('get',f'{host}/user',headers =OOO0000O00OO00O0O ).json ()#line:136
        if 'status'in OOOO000O0O0OO0000 :#line:137
            if OOOO000O0O0OO0000 ['status']==200 :#line:138
                if float (O0OOOO000OOOO0000 .doneeNo )!=0 :#line:139
                    OO0O0O0O0O0O0O0O0 =OOOO000O0O0OO0000 ['data']['assets']['gold']#line:140
                    if float (OO0O0O0O0O0O0O0O0 )>float (O0OOOO000OOOO0000 .innerId ):#line:141
                        O0O0000OOOOOOOO00 =int (float (OO0O0O0O0O0O0O0O0 )/1.1 )#line:142
                        OO0OOOO000OO00OO0 =f'_doneeNo={O0OOOO000OOOO0000.doneeNo}&quantity={O0O0000OOOOOOOO00}_{timi_new()}'#line:143
                        OOO0000O00OO00O0O ={'authorization':O0OOOO000OOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO000OO00OO0 ),'signstring':OO0OOOO000OO00OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:152
                        OO0O0O0O0O00OOO00 ={"quantity":O0O0000OOOOOOOO00 ,"doneeNo":O0OOOO000OOOO0000 .doneeNo }#line:156
                        OOOO00OO0OOO000OO =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0000O00OO00O0O ,data =OO0O0O0O0O00OOO00 ).json ()#line:157
                        if 'status'in OOOO00OO0OOO000OO :#line:159
                            if OOOO00OO0OOO000OO ['status']==200 :#line:160
                                if OOOO00OO0OOO000OO ['data']:#line:161
                                    print (f'【赠送种子】:赠送{O0O0000OOOOOOOO00}种子给{O0OOOO000OOOO0000.doneeNo}成功')#line:162
                else :#line:163
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:164
    def winning_rewards (O0OO0O00OO00000OO ):#line:167
        O000O0OOOO0OOOO00 =f'__{timi_new()}'#line:168
        O00O0000O000OOOOO ={'authorization':O0OO0O00OO00000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOOO0OOOO00 ),'signstring':O000O0OOOO0OOOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:177
        O0000OO0OOOOOO0OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00O0000O000OOOOO ).json ()#line:178
        if 'status'in O0000OO0OOOOOO0OO :#line:180
            if O0000OO0OOOOOO0OO ['status']==200 :#line:181
                if O0000OO0OOOOOO0OO ['data']['amount']:#line:182
                    OOOO0O0O0O0OOO0OO =O0000OO0OOOOOO0OO ['data']['amount']['gold']#line:183
                    return OOOO0O0O0O0OOO0OO #line:184
                else :#line:185
                    return 0 #line:186
    def certification (OO00000O0OOOO0O00 ):#line:189
        O00O0OOOOO000O000 =f'__{timi_new()}'#line:190
        OO0O0000OOOOOOO00 ={'authorization':OO00000O0OOOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOOOO000O000 ),'signstring':O00O0OOOOO000O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:199
        OO00OOO00000OO000 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0O0000OOOOOOO00 ).json ()#line:200
        if 'status'in OO00OOO00000OO000 :#line:202
            if OO00OOO00000OO000 ['status']==200 :#line:203
                if OO00OOO00000OO000 ['data']['result']:#line:204
                    O000000O0OOO000OO =OO00OOO00000OO000 ['data']['nick_name']#line:205
                    return O000000O0OOO000OO #line:206
                else :#line:207
                    return '未实名'#line:208
    def crops_illustrated (O00O00O00OO0000OO ):#line:211
        OOO000OOO0O0OOO0O =f'__{timi_new()}'#line:212
        O0OO0000O00O000OO ={'authorization':O00O00O00OO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOO0O0OOO0O ),'signstring':OOO000OOO0O0OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:221
        OOO00O000OO0OOO00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OO0000O00O000OO ).json ()#line:222
        if 'status'in OOO00O000OO0OOO00 :#line:224
            if OOO00O000OO0OOO00 ['status']==200 :#line:225
                O0000OO0OOOOOO000 =OOO00O000OO0OOO00 ['data'][0 ]['crops']#line:226
                for OOO000O0000O00OOO in O0000OO0OOOOOO000 :#line:227
                    if OOO000O0000O00OOO ['ill_clover_award']:#line:228
                        if float (OOO000O0000O00OOO ['ill_clover_award'])>1 :#line:229
                            if OOO000O0000O00OOO ['is_finish']:#line:230
                                if not OOO000O0000O00OOO ['is_getit']:#line:231
                                    OOO000OOO0O0OOO0O =f'_award_level={OOO000O0000O00OOO["level"]}_{timi_new()}'#line:232
                                    O0OO0000O00O000OO ={'authorization':O00O00O00OO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOO0O0OOO0O ),'signstring':OOO000OOO0O0OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:241
                                    O0OOOO0OO0OO0OOOO ={"award_level":OOO000O0000O00OOO ['level']}#line:242
                                    O00OOO0OO0O0O0000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OO0000O00O000OO ,json =O0OOOO0OO0OO0OOOO ).json ()#line:244
                                    if 'status'in O00OOO0OO0O0O0000 :#line:245
                                        if O00OOO0OO0O0O0000 ['status']==200 :#line:246
                                            OOOOO0OOOO0OO0O00 =O00OOO0OO0O0O0000 ['data']['ill_clover_award']#line:247
                                            print (f'【图鉴奖励】:领取{OOO000O0000O00OOO["crop_name"]}成就丨奖励{OOOOO0OOOO0OO0O00}叶子成功')#line:249
                                        if O00OOO0OO0O0O0000 ['status']==500 :#line:250
                                            print (f'【图鉴奖励】:{O00OOO0OO0O0O0000["message"]}')#line:251
    def watched_ad (OOO0000OOOO0OO000 ):#line:254
        O0O0O0OOOOOOOO0OO =f'__{timi_new()}'#line:255
        OO0OOOOOOO0O0O0OO ={'authorization':OOO0000OOOO0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOOOOOO0OO ),'signstring':O0O0O0OOOOOOOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:264
        O00O0O000O00O0OO0 =requests .request ('post',f'{host}/game/watched-ad',headers =OO0OOOOOOO0O0O0OO ).json ()#line:265
        print (O00O0O000O00O0OO0 )#line:266
    def user_ad (O0O000O0O0O00O000 ):#line:269
        O0OO0O0O000OOOOOO =f'__{timi_new()}'#line:270
        O00OOO00OOOO0000O ={'authorization':O0O000O0O0O00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O000OOOOOO ),'signstring':O0OO0O0O000OOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:279
        O00O0OO0OOO00O00O =requests .request ('get',f'{host}/user/ad',headers =O00OOO00OOOO0000O ).json ()#line:280
        if 'status'in O00O0OO0OOO00O00O :#line:282
            if O00O0OO0OOO00O00O ['status']==200 :#line:283
                O0OO0O0O0O000O0OO =O00O0OO0OOO00O00O ['data']['max_time']#line:284
                O0O0OOOOOO00O00OO =O00O0OO0OOO00O00O ['data']['watch_time']#line:285
                O0OOO0O00OO00OO0O =O00O0OO0OOO00O00O ['data']['added_time']#line:286
                print (f'【获取种子】:获取种子剩余{O0OOO0O00OO00OO0O + O0OO0O0O0O000O0OO - O0O0OOOOOO00O00OO}次丨好友提供:{O0OOO0O00OO00OO0O}次')#line:287
                if O0OOO0O00OO00OO0O +O0OO0O0O0O000O0OO -O0O0OOOOOO00O00OO >0 :#line:288
                    time .sleep (random .randint (16 ,19 ))#line:289
                    O0OO00OO0OOOOO0O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00OOO00OOOO0000O ).json ()#line:290
                    if 'status'in O0OO00OO0OOOOO0O0 :#line:292
                        if O0OO00OO0OOOOO0O0 ['status']==200 :#line:293
                            O00000000OOO000OO =O0OO00OO0OOOOO0O0 ['data']['silver']#line:294
                            print (f'【获取种子】:获得种子:{O00000000OOO000OO}')#line:295
                            return True #line:296
                        if O0OO00OO0OOOOO0O0 ['status']==500 :#line:297
                            O0OO00OOOOO00O000 =O0OO00OO0OOOOO0O0 ['message']#line:298
                            print (f'【获取种子】:{O0OO00OOOOO00O000}')#line:299
                            return False #line:300
    def synthetic (O00O00000O0O0O000 ):#line:303
        global id ,g #line:304
        try :#line:305
            OO00000OO0OOOOOOO =O00O00000O0O0O000 .level_new ()#line:306
            while True :#line:307
                O00O0OOOO0O000OO0 =f'__{timi_new()}'#line:308
                OOOO00O00O00OOO0O ={'authorization':O00O00000O0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOOO0O000OO0 ),'signstring':O00O0OOOO0O000OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:317
                O0OO0O0OO0OOO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =OOOO00O00O00OOO0O ).json ()#line:318
                if 'status'in O0OO0O0OO0OOO0O0O :#line:320
                    if O0OO0O0OO0OOO0O0O ['status']==200 :#line:321
                        O0O0O00O000O00OOO =O0OO0O0OO0OOO0O0O ['data']['cropList']#line:322
                        OOO0O0OO0O00O0O00 =O0OO0O0OO0OOO0O0O ['data']['gameCoreDataDBid']#line:323
                        O00O0OO0O0OOO0000 =0 #line:324
                        for O0OO000OOO00OO000 in O0O0O00O000O00OOO :#line:325
                            if not O0OO000OOO00OO000 :#line:326
                                O0OO0O00O000OO0O0 =f'_crop_id={OOO0O0OO0O00O0O00}&site={O00O0OO0O0OOO0000}_{O00O00000O0O0O000.time}'#line:327
                                OO0O00O0OOO000OOO ={'authorization':O00O00000O0O0O000 .token ,'timestamp':O00O00000O0O0O000 .time ,'sign':sign (O0OO0O00O000OO0O0 ),'signstring':O0OO0O00O000OO0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:336
                                O00O0OO00O000O0OO ={"site":O00O0OO0O0OOO0000 ,"crop_id":OOO0O0OO0O00O0O00 }#line:337
                                O0OO000O0O0O00OOO =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O00O0OOO000OOO ,data =O00O0OO00O000O0OO ).json ()#line:338
                                time .sleep (random .randint (1 ,3 )/10 )#line:340
                                if 'status'in O0OO000O0O0O00OOO :#line:341
                                    if O0OO000O0O0O00OOO ['status']==200 :#line:342
                                        if O0OO000O0O0O00OOO ['message']=='种子数量不足':#line:343
                                            OO00000OO0OOOOOOO =O00O00000O0O0O000 .level_new ()#line:344
                                            print (f'【种植合成】:{O0OO000O0O0O00OOO["message"]}')#line:345
                                            if not O00O00000O0O0O000 .user_ad ():#line:346
                                                return False #line:347
                                        print (f'【种植合成】:种植农作物,位置{O00O0OO0O0OOO0000}')#line:348
                                    if O0OO000O0O0O00OOO ['status']==500 :#line:349
                                        print (f'【种植合成】:{O0OO000O0O0O00OOO["message"]}')#line:350
                                        return False #line:351
                            O00O0OO0O0OOO0000 +=1 #line:352
                        OO000000OOOOOO0OO =requests .request ('get',f'{host}/game/getAllData',headers =OOOO00O00O00OOO0O ).json ()#line:353
                        OOOOO00O00000O0OO =OO000000OOOOOO0OO ['data']['cropList']#line:354
                        O00OO0OOO0OO0OOO0 =False #line:355
                        for O0OO000OOO00OO000 in range (12 ):#line:356
                            id =OOOOO00O00000O0OO [O0OO000OOO00OO000 ]['level']#line:357
                            if float (OO00000OO0OOOOOOO )-float (id )>9 :#line:358
                                OOO00000OO0OO00O0 =f'_site={O0OO000OOO00OO000}_{timi_new()}'#line:359
                                O0O000OO00O0OO0OO ={'accept':'application/json, text/plain, */*','authorization':O00O00000O0O0O000 .token ,'timestamp':timi_new (),'sign':sign (OOO00000OO0OO00O0 ),'signstring':OOO00000OO0OO00O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:369
                                OO00OO00OOOO0O0O0 ={"site":O0OO000OOO00OO000 }#line:370
                                O0OO0O0OO00O000O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O000OO00O0OO0OO ,data =OO00OO00OOOO0O0O0 ).json ()#line:372
                                if 'status'in O0OO0O0OO00O000O0 :#line:373
                                    if O0OO0O0OO00O000O0 ['status']==200 :#line:374
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:375
                            if id !=0 :#line:376
                                for OOOOOO0O0OOOO0000 in range (11 ):#line:377
                                    O00000OO0O00OOOO0 =OOOOOO0O0OOOO0000 +1 #line:378
                                    g =OOOOO00O00000O0OO [O00000OO0O00OOOO0 ]['level']#line:379
                                    if id ==g :#line:380
                                        O00O0O0O000OO000O =OOOOOO0O0OOOO0000 +2 #line:381
                                        if O00O0O0O000OO000O ==O0OO000OOO00OO000 +1 :#line:382
                                            pass #line:383
                                        else :#line:384
                                            O0O0OOOO0000000OO =O0OO000OOO00OO000 +1 #line:385
                                            time .sleep (random .randint (1 ,3 )/10 )#line:387
                                            O0O0O00OO000OOO0O =f'_site={O0O0OOOO0000000OO - 1}&targetSite={O00O0O0O000OO000O - 1}_{timi_new()}'#line:388
                                            O00OOO0OOOOOO00OO ={'accept':'application/json, text/plain, */*','authorization':O00O00000O0O0O000 .token ,'timestamp':timi_new (),'sign':sign (O0O0O00OO000OOO0O ),'signstring':O0O0O00OO000OOO0O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:403
                                            OOOO00000O0OOO0O0 ={"site":int (O0O0OOOO0000000OO -1 ),"targetSite":int (O00O0O0O000OO000O -1 )}#line:404
                                            O00000O00OOOO00OO =requests .request ('post',f'{host}/game/crops/move',headers =O00OOO0OOOOOO00OO ,json =OOOO00000O0OOO0O0 ).json ()#line:406
                                            if 'status'in O00000O00OOOO00OO :#line:407
                                                if O00000O00OOOO00OO ['status']==200 :#line:408
                                                    pass #line:409
                                            print ('【种植合成】:',O0O0OOOO0000000OO ,O00O0O0O000OO000O ,'合成成功')#line:411
                                            O00OO0OOO0OO0OOO0 =True #line:412
                                    if O00OO0OOO0OO0OOO0 :#line:413
                                        break #line:414
                                if O00OO0OOO0OO0OOO0 :#line:415
                                    break #line:416
        except Exception as O0000OO00OO000O0O :#line:417
            O00O00000O0O0O000 .synthetic ()#line:418
    def level_new (OOO0O00O0O00O00O0 ):#line:421
        try :#line:422
            OOOOOO0O0OO0O0OOO =f'__{timi_new()}'#line:423
            OOOOO00O0000O0O00 ={'authorization':OOO0O00O0O00O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O0OO0O0OOO ),'signstring':OOOOOO0O0OO0O0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:432
            OOOOO0OOO0OOOOOO0 =requests .request ('get',f'{host}/user',headers =OOOOO00O0000O0O00 ).json ()#line:433
            if 'status'in OOOOO0OOO0OOOOOO0 :#line:434
                if OOOOO0OOO0OOOOOO0 ['status']==200 :#line:435
                    return float (OOOOO0OOO0OOOOOO0 ['data']['level'])#line:436
        except Exception as OO0OO0O0O0O00O0O0 :#line:437
            print (OO0OO0O0O0O00O0O0 )#line:438
    def propsraffle (OOOOOOOO00OOO00O0 ):#line:441
        try :#line:442
            while True :#line:443
                O0O0O00O00O000000 =f'__{timi_new()}'#line:444
                O00OOOO000O0OO0O0 ={'authorization':OOOOOOOO00OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00O00O000000 ),'signstring':O0O0O00O00O000000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:453
                OO0O00OOOOO0O0OO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00OOOO000O0OO0O0 ).json ()#line:454
                if 'status'in OO0O00OOOOO0O0OO0 :#line:456
                    if OO0O00OOOOO0O0OO0 ['status']==200 :#line:457
                        O0OO0OOO0OO00OOOO =OO0O00OOOOO0O0OO0 ['data']['rows']#line:458
                        OOOO0OOO0O0000OO0 =OO0O00OOOOO0O0OO0 ['data']['vstate']#line:459
                        if O0OO0OOO0OO00OOOO ==5 or O0OO0OOO0OO00OOOO ==6 or O0OO0OOO0OO00OOOO ==7 :#line:460
                            OOOO0000000OOOO0O =OO0O00OOOOO0O0OO0 ['data']['silver']#line:461
                            print (f'【转盘抽奖】:获得种子:{OOOO0000000OOOO0O}')#line:462
                        if O0OO0OOO0OO00OOOO ==1 or O0OO0OOO0OO00OOOO ==2 or O0OO0OOO0OO00OOOO ==3 :#line:463
                            OO00000O00O0OOO0O =OO0O00OOOOO0O0OO0 ['data']['clover']#line:464
                            print (f'【转盘抽奖】:获得三叶草:{OO00000O00O0OOO0O}')#line:465
                        if O0OO0OOO0OO00OOOO ==4 or O0OO0OOO0OO00OOOO ==8 :#line:466
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:467
                        if O0OO0OOO0OO00OOOO =='抽奖次数已用完':#line:471
                            if OOOO0OOO0O0000OO0 :#line:472
                                O0O0O00O00O000000 =f'__{timi_new()}'#line:473
                                O00OOOO000O0OO0O0 ={'authorization':OOOOOOOO00OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00O00O000000 ),'signstring':O0O0O00O00O000000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:482
                                OO00000OO0OOO000O =requests .request ('get',f'{host}/user',headers =O00OOOO000O0OO0O0 ).json ()#line:483
                                if 'status'in OO00000OO0OOO000O :#line:484
                                    if OO00000OO0OOO000O ['status']==200 :#line:485
                                        O0OO0OO0OO0O00O00 =OO00000OO0OOO000O ['data']['level']#line:486
                                        if float (O0OO0OO0OO0O00O00 )>39 :#line:487
                                            OO0O0OOO00OOO00O0 =random .randint (160 ,190 )/10 #line:488
                                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{OO0O0OOO00OOO00O0}秒获取抽奖机会')#line:489
                                            time .sleep (OO0O0OOO00OOO00O0 )#line:490
                                            OOO0O00OO000000O0 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O00OOOO000O0OO0O0 ).json ()#line:491
                                            if 'status'in OOO0O00OO000000O0 :#line:493
                                                if OOO0O00OO000000O0 ['status']==200 :#line:494
                                                    print (f'【转盘抽奖】:{OOO0O00OO000000O0["message"]}')#line:495
                                                if OOO0O00OO000000O0 ['status']==500 :#line:496
                                                    print (f'【转盘抽奖】:{OOO0O00OO000000O0["message"]}')#line:497
                                                    break #line:498
                                            time .sleep (random .randint (10 ,15 )/10 )#line:499
                                        else :#line:500
                                            break #line:501
                            else :#line:502
                                break #line:503
                time .sleep (random .randint (8 ,15 )/10 )#line:504
        except Exception as O0OOO00O0O00O00O0 :#line:505
            print (O0OOO00O0O00O00O0 )#line:506
    def friends_invitation (O00OO0OO0O000O000 ):#line:509
        try :#line:510
            OO0O0O0OO000OO0OO =f'__{timi_new()}'#line:511
            O0O00O0OOO0O0O0O0 ={'authorization':O00OO0OO0O000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OO000OO0OO ),'signstring':OO0O0O0OO000OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:520
            OOOO000O00OOOOOO0 =requests .request ('get',f'{host}/friends',headers =O0O00O0OOO0O0O0O0 ).json ()#line:521
            if 'status'in OOOO000O00OOOOOO0 :#line:522
                if OOOO000O00OOOOOO0 ['status']==200 :#line:523
                    OO0O0O00O00O00000 =OOOO000O00OOOOOO0 ['data']['myInviteter']#line:524
                    if OO0O0O00O00O00000 :#line:525
                        O00O0OOO0OOO00000 =OO0O0O00O00O00000 ['user']['nickname']#line:526
                        OO00OOOOO000OOOO0 =O00OO0OO0O000O000 .certification ()#line:527
                        print (f'【查邀请人】:我的邀请人:{O00O0OOO0OOO00000}丨实名:{OO00OOOOO000OOOO0}')#line:528
                    else :#line:529
                        if O00OO0OO0O000O000 .innerId !='0':#line:530
                            OO0O0O0OO000OO0OO =f'_innerId=1937553_{timi_new()}'#line:531
                            O0O00O0OOO0O0O0O0 ={'authorization':O00OO0OO0O000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OO000OO0OO ),'signstring':OO0O0O0OO000OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:540
                            O0O00OOO000O0OOOO ={"innerId":'1937553'}#line:541
                            O0OO00O00O000OOOO =requests .request ('post',f'{host}/friends/my-invitation',headers =O0O00O0OOO0O0O0O0 ,data =O0O00OOO000O0OOOO ).json ()#line:543
        except Exception as O00O00OOOOOO00000 :#line:544
            print (O00O00OOOOOO00000 )#line:545
    def add_clover (O00000O0OO0OO0O00 ):#line:548
        global golden_seed #line:549
        try :#line:550
            O00O00OO00OOOOOOO =f'__{timi_new()}'#line:551
            O0O000000000OO0O0 ={'authorization':O00000O0OO0OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO00OOOOOOO ),'signstring':O00O00OO00OOOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:560
            O000O0OO0000O00O0 =requests .request ('get',f'{host}/assets/clovers',headers =O0O000000000OO0O0 ).json ()#line:561
            if 'status'in O000O0OO0000O00O0 :#line:563
                if O000O0OO0000O00O0 ['status']==200 :#line:564
                    O00O0O00000OOO0OO =O000O0OO0000O00O0 ['data']['clover']#line:565
                    O0000OO0OOOOOOO00 =O000O0OO0000O00O0 ['data']['used_clover']#line:566
                    O0OOO000O00000O00 =float (O00O0O00000OOO0OO )-float (O0000OO0OOOOOOO00 )#line:567
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0000OO0OOOOOOO00}')#line:568
                    if O0OOO000O00000O00 >1 :#line:569
                        O00O00OO00OOOOOOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OOO000O00000O00)}_{timi_new()}'#line:570
                        O0O000000000OO0O0 ={'authorization':O00000O0OO0OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO00OOOOOOO ),'signstring':O00O00OO00OOOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:579
                        O0O0OOO00OOO0O0O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OOO000O00000O00 )}#line:580
                        OO000O00OOOOOOO00 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O000000000OO0O0 ,data =O0O0OOO00OOO0O0O0 ).json ()#line:581
                        if 'status'in OO000O00OOOOOOO00 :#line:583
                            if OO000O00OOOOOOO00 ['status']==200 :#line:584
                                print (f'【参与抽奖】:添加三叶草:{OO000O00OOOOOOO00["data"]}丨数量:{O0OOO000O00000O00}')#line:585
                            if OO000O00OOOOOOO00 ['status']==500 :#line:586
                                print (f'【参与抽奖】:添加三叶草:{OO000O00OOOOOOO00["message"]}')#line:587
            O0O0OOOO0000OO0O0 =requests .request ('get',f'{host}/lottery',headers =O0O000000000OO0O0 ).json ()#line:588
            O0OOOO0O00OO0OOO0 =O00000O0OO0OO0O00 .winning_rewards ()#line:590
            if 'status'in O0O0OOOO0000OO0O0 :#line:591
                if O0O0OOOO0000OO0O0 ['status']==200 :#line:592
                    O0O000OO0000OO0OO =O0O0OOOO0000OO0O0 ['data'][0 ]['day_get_gold_quantity']#line:593
                    golden_seed +=float (O0O000OO0000OO0OO )#line:594
                    print (f'【参与抽奖】:预计每天中{O0O000OO0000OO0OO[:6]}颗金种子丨好友收益:{str(O0OOOO0O00OO0OOO0)[:6]}')#line:595
        except Exception as O000OOO000000O0OO :#line:596
            print (O000OOO000000O0OO )#line:597
    def energy (O0000O00000OO0000 ):#line:600
        OOOOOO0OOOO00OO00 =f'__{timi_new()}'#line:601
        O000O00O0OOO0OOO0 ={'authorization':O0000O00000OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OOOO00OO00 ),'signstring':OOOOOO0OOOO00OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:610
        O0OO0O0OO0O00OOOO =requests .request ('get',f'{host}/energy/general',headers =O000O00O0OOO0OOO0 ).json ()#line:611
        if 'status'in O0OO0O0OO0O00OOOO :#line:613
            if O0OO0O0OO0O00OOOO ['status']==200 :#line:614
                O00OO000OO00O0O0O =O0OO0O0OO0O00OOOO ['data']['ordinary_water_consumptions']#line:615
                if float (O00OO000OO00O0O0O )<80 :#line:616
                    OO00OO00000O00OO0 =99 -float (O00OO000OO00O0O0O )#line:617
                    OO00OOOO0OOOOOO0O ={"fertilizer":str (OO00OO00000O00OO0 ).split ('.')[0 ]}#line:618
                    O0O0OO0O00O0OOO0O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O000O00O0OOO0OOO0 ,data =OO00OOOO0OOOOOO0O ).json ()#line:619
                    if 'status'in O0O0OO0O00O0OOO0O :#line:621
                        if O0O0OO0O00O0OOO0O ['status']==200 :#line:622
                            print (f'【购买肥料】:{O0O0OO0O00O0OOO0O["message"]}')#line:623
                OOO000O0OOO00OO00 =O0OO0O0OO0O00OOOO ['data']['ordinary_water_consumptions']#line:624
                if float (OOO000O0OOO00OO00 )<800 :#line:625
                    OOO000OO0OO00000O =999 -float (OOO000O0OOO00OO00 )#line:626
                    OOO00OO00OOOOOOOO ={"water":str (OOO000OO0OO00000O ).split ('.')[0 ]}#line:627
                    O00OOOO0O000OOO0O =requests .request ('post',f'{host}/energy/general/buy/water',headers =O000O00O0OOO0OOO0 ,data =OOO00OO00OOOOOOOO ).json ()#line:628
                    if 'status'in O00OOOO0O000OOO0O :#line:629
                        if O00OOOO0O000OOO0O ['status']==200 :#line:630
                            print (f'【购买水滴】:{O00OOOO0O000OOO0O["message"]}')#line:631
def version_of_the_validation ():#line:635
    return str ((67 -56 )/10 )#line:636
def gitee_validation ():#line:639
    try :#line:640
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:641
    except Exception as OOO0OO0OO0O0O00OO :#line:642
        sys .exit (0 )#line:643
def update_the_validation ():#line:647
    try :#line:648
        O0O0OO00O0O0O0OO0 =gitee_validation ()#line:649
        if version_of_the_validation ()<O0O0OO00O0O0O0OO0 ['CityEarth']['edition']:#line:650
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0OO00O0O0O0OO0["CityEarth"]["edition"]}   ❌')#line:651
            print (f'更新内容=>>{O0O0OO00O0O0O0OO0["CityEarth"]["content"]}   👍')#line:652
        else :#line:653
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0OO00O0O0O0OO0["CityEarth"]["edition"]}   ✅')#line:654
            print (f'更新内容=>> {O0O0OO00O0O0O0OO0["CityEarth"]["content"]}   👍')#line:655
    except Exception as O0O0O0OOOO0O00O0O :#line:656
        print (O0O0O0OOOO0O00O0O )#line:657
def os_qinglong ():#line:660
    if application in os .environ :#line:661
        O0OOOOO00OO0O000O =os .environ [application ].split ('\n')#line:662
        if len (O0OOOOO00OO0O000O )>0 :#line:663
            return O0OOOOO00OO0O000O #line:664
        else :#line:665
            print (f"{application}变量未启用")#line:666
            print ('脚本退出')#line:667
            sys .exit (1 )#line:668
    else :#line:669
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:671
        return os_built ()#line:672
def os_built ():#line:675
    if token :#line:676
        O0O0O0OOOO0O0O00O =token .split ('\n')#line:677
        if len (O0O0O0OOOO0O0O00O )>0 :#line:678
            return O0O0O0OOOO0O0O00O #line:679
    else :#line:680
        print (f"内置变量为空")#line:681
        print ('脚本结束')#line:682
        sys .exit (0 )#line:683
if __name__ =='__main__':#line:686
    start ()#line:687
