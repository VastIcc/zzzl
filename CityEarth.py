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
        OO0O0OOO000OOOOO0 =os_qinglong ()#line:7
        print (f"==========共找到{len(OO0O0OOO000OOOOO0)}个账号==========")#line:8
        for O00O0OOO0O00O00OO in OO0O0OOO000OOOOO0 :#line:9
            print (f"------------正在执行第{OO0O0OOO000OOOOO0.index(O00O0OOO0O00O00OO) + 1}个账号------------")#line:10
            OO000O0OO0OO00OOO =CityEarth (O00O0OOO0O00O00OO )#line:11
            def O0OOOO000OOO0O0O0 ():#line:13
                if OO000O0OO0OO00OOO .base_info ():#line:15
                    OO000O0OO0OO00OOO .game_map ()#line:19
                    OO000O0OO0OO00OOO .friends_invitation ()#line:21
                    OO000O0OO0OO00OOO .add_clover ()#line:23
                    OO000O0OO0OO00OOO .energy ()#line:25
                    OO000O0OO0OO00OOO .propsraffle ()#line:27
                    OO000O0OO0OO00OOO .synthetic ()#line:29
                    OO000O0OO0OO00OOO .crops_illustrated ()#line:31
                    OO000O0OO0OO00OOO .give_gold ()#line:33
                else :#line:34
                    print ('token失效')#line:35
            O0OO000OOOOO000O0 =threading .Thread (target =O0OOOO000OOO0O0O0 )#line:37
            O0OO000OOOOO000O0 .start ()#line:38
            time .sleep (time_xx )#line:39
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:41
        time .sleep (3 )#line:42
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:43
    except Exception as OO00OOO00OOO00OOO :#line:44
        print (OO00OOO00OOO00OOO )#line:45
def sign (O000O000OOOO0OOOO ):#line:48
    O0000O00OOO0OO0OO =hashlib .md5 (O000O000OOOO0OOOO .encode ()).hexdigest ()#line:49
    OO0OOO00O0000O0O0 ="scsc%^&*"+O0000O00OOO0OO0OO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:50
    OO000OOO0O00000O0 =hashlib .md5 (OO0OOO00O0000O0O0 .encode ()).hexdigest ()#line:51
    return OO000OOO0O00000O0 #line:52
def timi_new ():#line:55
    return str (int (time .time ()*1000 ))#line:56
class CityEarth :#line:58
    def __init__ (OO0OOO00OO000000O ,OO0OO00OO00O000OO ):#line:60
        try :#line:61
            OO0OOO00OO000000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:62
            OO0OOO00OO000000O .token =OO0OO00OO00O000OO .split ('&')[0 ]#line:63
            OO0OOO00OO000000O .innerId =OO0OO00OO00O000OO .split ('&')[1 ]#line:64
            OO0OOO00OO000000O .doneeNo =OO0OO00OO00O000OO .split ('&')[2 ]#line:65
        except :#line:66
            print ('变量格式错误')#line:67
    def base_info (O0000OO00OOOO000O ):#line:70
        try :#line:71
            O0OO0OOOO000OO0OO =f'__{timi_new()}'#line:72
            O000OOOOO00O0OO0O ={'authorization':O0000OO00OOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOOO000OO0OO ),'signstring':O0OO0OOOO000OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:81
            O00O00O0OO00O0O0O =requests .request ('get',f'{host}/user',headers =O000OOOOO00O0OO0O ).json ()#line:82
            if 'status'in O00O00O0OO00O0O0O :#line:84
                if O00O00O0OO00O0O0O ['status']==200 :#line:85
                    OOOOOOOOO00OOOOOO =O00O00O0OO00O0O0O ['data']['nickname']#line:86
                    O000O0O00O0OOO0OO =O00O00O0OO00O0O0O ['data']['inner_id']#line:87
                    O0OOOO00OOOO00O00 =O00O00O0OO00O0O0O ['data']['assets']['gold']#line:88
                    OO0O0O0OOO00OOOO0 =O00O00O0OO00O0O0O ['data']['level']#line:89
                    print (f'【账号信息】:昵称:{OOOOOOOOO00OOOOOO[:5]}丨ID:{O000O0O00O0OOO0OO}丨等级:{OO0O0O0OOO00OOOO0}丨种子:{str(O0OOOO00OOOO00O00).split(".")[0]}')#line:90
                if O00O00O0OO00O0O0O ['status']==401 :#line:91
                    return False #line:92
                if O00O00O0OO00O0O0O ['status']==500 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as OO0000O0O000OOO00 :#line:96
            print (OO0000O0O000OOO00 )#line:97
    def game_map (O00O0O000O0O00O0O ):#line:100
        OO0OOO0OO0O0O0000 =f'__{timi_new()}'#line:101
        OO00O000OO0000O0O ={'authorization':O00O0O000O0O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0OO0O0O0000 ),'signstring':OO0OOO0OO0O0O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:110
        OOO0OOOOO0OO000O0 =requests .request ('get',f'{host}/game/map',headers =OO00O000OO0000O0O ).json ()#line:111
        if 'status'in OOO0OOOOO0OO000O0 :#line:113
            if OOO0OOOOO0OO000O0 ['status']==200 :#line:114
                for OOO0O0OOO00O0O00O in OOO0OOOOO0OO000O0 ['data']['list'][0 ]['crops']:#line:115
                    OOOOOO00OOO00OO0O =OOO0O0OOO00O0O00O ['level']#line:117
                    if OOOOOO00OOO00OO0O ==41 :#line:118
                        OOOO0OOOOOOO0OO00 =OOO0O0OOO00O0O00O ['crop_name']#line:119
                        OO0000O00OO0OO0O0 =OOO0O0OOO00O0O00O ['count']#line:120
                        if OO0000O00OO0OO0O0 >0 :#line:121
                            print (f'【农业资产】:{OOOO0OOOOOOO0OO00}丨数量:{OO0000O00OO0OO0O0}')#line:122
    def give_gold (O0OOO0O0OO00O0OOO ):#line:125
        O00OOO0OO00O000OO =f'__{timi_new()}'#line:126
        OOO000OO0OO000000 ={'authorization':O0OOO0O0OO00O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OO00O000OO ),'signstring':O00OOO0OO00O000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:135
        OO00O0O0O0O0O0O0O =requests .request ('get',f'{host}/user',headers =OOO000OO0OO000000 ).json ()#line:136
        if 'status'in OO00O0O0O0O0O0O0O :#line:137
            if OO00O0O0O0O0O0O0O ['status']==200 :#line:138
                if float (O0OOO0O0OO00O0OOO .doneeNo )!=0 :#line:139
                    OOOO0O00OOOO000OO =OO00O0O0O0O0O0O0O ['data']['assets']['gold']#line:140
                    if float (OOOO0O00OOOO000OO )>float (O0OOO0O0OO00O0OOO .innerId ):#line:141
                        O0OOOOOO000O00000 =int (float (OOOO0O00OOOO000OO )/1.1 )#line:142
                        O00OOO0OO00O000OO =f'_doneeNo={O0OOO0O0OO00O0OOO.doneeNo}&quantity={O0OOOOOO000O00000}_{timi_new()}'#line:143
                        OOO000OO0OO000000 ={'authorization':O0OOO0O0OO00O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OO00O000OO ),'signstring':O00OOO0OO00O000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:152
                        O000OOO00O0OOOO0O ={"quantity":O0OOOOOO000O00000 ,"doneeNo":O0OOO0O0OO00O0OOO .doneeNo }#line:156
                        O00OO0O0O0000OO00 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO000OO0OO000000 ,data =O000OOO00O0OOOO0O ).json ()#line:157
                        if 'status'in O00OO0O0O0000OO00 :#line:159
                            if O00OO0O0O0000OO00 ['status']==200 :#line:160
                                if O00OO0O0O0000OO00 ['data']:#line:161
                                    print (f'【赠送种子】:赠送{O0OOOOOO000O00000}种子给{O0OOO0O0OO00O0OOO.doneeNo}成功')#line:162
                else :#line:163
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:164
    def winning_rewards (O00OOO0O0O0000O00 ):#line:167
        O0O000OOO0O0OOOOO =f'__{timi_new()}'#line:168
        O0O0OOO0O000O00OO ={'authorization':O00OOO0O0O0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOO0O0OOOOO ),'signstring':O0O000OOO0O0OOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:177
        O0OO0OOO0O000O0OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O0OOO0O000O00OO ).json ()#line:178
        if 'status'in O0OO0OOO0O000O0OO :#line:180
            if O0OO0OOO0O000O0OO ['status']==200 :#line:181
                if O0OO0OOO0O000O0OO ['data']['amount']:#line:182
                    O0OOO0OO0OOO0OO00 =O0OO0OOO0O000O0OO ['data']['amount']['gold']#line:183
                    return O0OOO0OO0OOO0OO00 #line:184
                else :#line:185
                    return 0 #line:186
    def certification (OOOO0OOO0OOO0OOO0 ):#line:189
        OO0000O0OOOO0O0O0 =f'__{timi_new()}'#line:190
        O00OO0OO0000O0OOO ={'authorization':OOOO0OOO0OOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O0OOOO0O0O0 ),'signstring':OO0000O0OOOO0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:199
        O0OO00O00O0OO0000 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OO0OO0000O0OOO ).json ()#line:200
        if 'status'in O0OO00O00O0OO0000 :#line:202
            if O0OO00O00O0OO0000 ['status']==200 :#line:203
                if O0OO00O00O0OO0000 ['data']['result']:#line:204
                    OO00O0OO0OOO00000 =O0OO00O00O0OO0000 ['data']['nick_name']#line:205
                    return OO00O0OO0OOO00000 #line:206
                else :#line:207
                    return '未实名'#line:208
    def crops_illustrated (OO0OO000OO00O0O00 ):#line:211
        OOO000OO00OO000O0 =f'__{timi_new()}'#line:212
        OO0O0OO0O0O0000O0 ={'authorization':OO0OO000OO00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO00OO000O0 ),'signstring':OOO000OO00OO000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:221
        O0OOOOO00O00O0000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O0OO0O0O0000O0 ).json ()#line:222
        if 'status'in O0OOOOO00O00O0000 :#line:224
            if O0OOOOO00O00O0000 ['status']==200 :#line:225
                OO00O00OOO0O000O0 =O0OOOOO00O00O0000 ['data'][0 ]['crops']#line:226
                for O0O0O0OO0O00000O0 in OO00O00OOO0O000O0 :#line:227
                    if O0O0O0OO0O00000O0 ['ill_clover_award']:#line:228
                        if float (O0O0O0OO0O00000O0 ['ill_clover_award'])>1 :#line:229
                            if O0O0O0OO0O00000O0 ['is_finish']:#line:230
                                if not O0O0O0OO0O00000O0 ['is_getit']:#line:231
                                    OOO000OO00OO000O0 =f'_award_level={O0O0O0OO0O00000O0["level"]}_{timi_new()}'#line:232
                                    OO0O0OO0O0O0000O0 ={'authorization':OO0OO000OO00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO00OO000O0 ),'signstring':OOO000OO00OO000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:241
                                    O0000O00OO000000O ={"award_level":O0O0O0OO0O00000O0 ['level']}#line:242
                                    O00000OOO000O0OO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O0OO0O0O0000O0 ,json =O0000O00OO000000O ).json ()#line:244
                                    if 'status'in O00000OOO000O0OO0 :#line:245
                                        if O00000OOO000O0OO0 ['status']==200 :#line:246
                                            O0OOOO000OO00O000 =O00000OOO000O0OO0 ['data']['ill_clover_award']#line:247
                                            print (f'【图鉴奖励】:领取{O0O0O0OO0O00000O0["crop_name"]}成就丨奖励{O0OOOO000OO00O000}叶子成功')#line:249
                                        if O00000OOO000O0OO0 ['status']==500 :#line:250
                                            print (f'【图鉴奖励】:{O00000OOO000O0OO0["message"]}')#line:251
    def watched_ad (O0OO0OOOO0OO00OOO ):#line:254
        O0000OOOO00OO000O =f'__{timi_new()}'#line:255
        O0000O0O000OO0O00 ={'authorization':O0OO0OOOO0OO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOO00OO000O ),'signstring':O0000OOOO00OO000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:264
        OOO00OOOO00OOO000 =requests .request ('post',f'{host}/game/watched-ad',headers =O0000O0O000OO0O00 ).json ()#line:265
        print (OOO00OOOO00OOO000 )#line:266
    def user_ad (OOOO0OO0OO0OO00OO ):#line:269
        OOO0O000O00OO00OO =f'__{timi_new()}'#line:270
        OO0O000000O00OO0O ={'authorization':OOOO0OO0OO0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O00OO00OO ),'signstring':OOO0O000O00OO00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:279
        O0OOOOO0O0OOOO0O0 =requests .request ('get',f'{host}/user/ad',headers =OO0O000000O00OO0O ).json ()#line:280
        if 'status'in O0OOOOO0O0OOOO0O0 :#line:282
            if O0OOOOO0O0OOOO0O0 ['status']==200 :#line:283
                OO0OOOOO0OOOO0O0O =O0OOOOO0O0OOOO0O0 ['data']['max_time']#line:284
                OOO0OO00OO000OOOO =O0OOOOO0O0OOOO0O0 ['data']['watch_time']#line:285
                OO000000O000OOO0O =O0OOOOO0O0OOOO0O0 ['data']['added_time']#line:286
                print (f'【获取种子】:获取种子剩余{OO000000O000OOO0O + OO0OOOOO0OOOO0O0O - OOO0OO00OO000OOOO}次丨好友提供:{OO000000O000OOO0O}次')#line:287
                if OO000000O000OOO0O +OO0OOOOO0OOOO0O0O -OOO0OO00OO000OOOO >0 :#line:288
                    time .sleep (random .randint (16 ,19 ))#line:289
                    O0O0000O00OOO0000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO0O000000O00OO0O ).json ()#line:290
                    if 'status'in O0O0000O00OOO0000 :#line:292
                        if O0O0000O00OOO0000 ['status']==200 :#line:293
                            OO00O00OOO00OO000 =O0O0000O00OOO0000 ['data']['silver']#line:294
                            print (f'【获取种子】:获得种子:{OO00O00OOO00OO000}')#line:295
                            return True #line:296
                        if O0O0000O00OOO0000 ['status']==500 :#line:297
                            O000000O0O0OO0O0O =O0O0000O00OOO0000 ['message']#line:298
                            print (f'【获取种子】:{O000000O0O0OO0O0O}')#line:299
                            return False #line:300
    def synthetic (OO000000O00000OOO ):#line:303
        global id ,g #line:304
        try :#line:305
            O0OO0O00OOOOO000O =OO000000O00000OOO .level_new ()#line:306
            while True :#line:307
                O00O0O0O00OO00000 =f'__{timi_new()}'#line:308
                O0OO0O0OOOOO0OO00 ={'authorization':OO000000O00000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O00OO00000 ),'signstring':O00O0O0O00OO00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:317
                O0O000OO0OOO0O00O =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O0OOOOO0OO00 ).json ()#line:318
                if 'status'in O0O000OO0OOO0O00O :#line:320
                    if O0O000OO0OOO0O00O ['status']==200 :#line:321
                        OO0OOO0O00OO0O0O0 =O0O000OO0OOO0O00O ['data']['cropList']#line:322
                        O0000OO0O0O0O00O0 =O0O000OO0OOO0O00O ['data']['gameCoreDataDBid']#line:323
                        OO0OOOOOO000000OO =0 #line:324
                        for OO00OOOOO00OOO0O0 in OO0OOO0O00OO0O0O0 :#line:325
                            if not OO00OOOOO00OOO0O0 :#line:326
                                O0OOO0O00000OOOO0 =f'_crop_id={O0000OO0O0O0O00O0}&site={OO0OOOOOO000000OO}_{OO000000O00000OOO.time}'#line:327
                                OO0O00000OOO00O0O ={'authorization':OO000000O00000OOO .token ,'timestamp':OO000000O00000OOO .time ,'sign':sign (O0OOO0O00000OOOO0 ),'signstring':O0OOO0O00000OOOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:336
                                OOO0O0OO00O00OOOO ={"site":OO0OOOOOO000000OO ,"crop_id":O0000OO0O0O0O00O0 }#line:337
                                O000O000OOOOO0O00 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O00000OOO00O0O ,data =OOO0O0OO00O00OOOO ).json ()#line:338
                                time .sleep (random .randint (1 ,3 )/10 )#line:340
                                if 'status'in O000O000OOOOO0O00 :#line:341
                                    if O000O000OOOOO0O00 ['status']==200 :#line:342
                                        if O000O000OOOOO0O00 ['message']=='种子数量不足':#line:343
                                            O0OO0O00OOOOO000O =OO000000O00000OOO .level_new ()#line:344
                                            print (f'【种植合成】:{O000O000OOOOO0O00["message"]}')#line:345
                                            if not OO000000O00000OOO .user_ad ():#line:346
                                                return False #line:347
                                        print (f'【种植合成】:种植农作物,位置{OO0OOOOOO000000OO}')#line:348
                                    if O000O000OOOOO0O00 ['status']==500 :#line:349
                                        print (f'【种植合成】:{O000O000OOOOO0O00["message"]}')#line:350
                                        return False #line:351
                            OO0OOOOOO000000OO +=1 #line:352
                        OO00OO00O00O00OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O0OOOOO0OO00 ).json ()#line:353
                        O0000OO0O00O000OO =OO00OO00O00O00OO0 ['data']['cropList']#line:354
                        O0OOOOO0O0OOO0O0O =False #line:355
                        for OO00OOOOO00OOO0O0 in range (12 ):#line:356
                            id =O0000OO0O00O000OO [OO00OOOOO00OOO0O0 ]['level']#line:357
                            if float (O0OO0O00OOOOO000O )-float (id )>9 :#line:358
                                O0OOOOOOOOO0OO000 =f'_site={OO00OOOOO00OOO0O0}_{timi_new()}'#line:359
                                OOOO000OOO0OOO0OO ={'accept':'application/json, text/plain, */*','authorization':OO000000O00000OOO .token ,'timestamp':timi_new (),'sign':sign (O0OOOOOOOOO0OO000 ),'signstring':O0OOOOOOOOO0OO000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:369
                                O00OO00000O00O0OO ={"site":OO00OOOOO00OOO0O0 }#line:370
                                OO00OOO0O0OOO0OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOO000OOO0OOO0OO ,data =O00OO00000O00O0OO ).json ()#line:372
                                if 'status'in OO00OOO0O0OOO0OOO :#line:373
                                    if OO00OOO0O0OOO0OOO ['status']==200 :#line:374
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:375
                            if id !=0 :#line:376
                                for O00O0O0000OOOOOOO in range (11 ):#line:377
                                    OOO00OOO0O00OOOOO =O00O0O0000OOOOOOO +1 #line:378
                                    g =O0000OO0O00O000OO [OOO00OOO0O00OOOOO ]['level']#line:379
                                    if id ==g :#line:380
                                        O00OOOOOO0OOO0OOO =O00O0O0000OOOOOOO +2 #line:381
                                        if O00OOOOOO0OOO0OOO ==OO00OOOOO00OOO0O0 +1 :#line:382
                                            pass #line:383
                                        else :#line:384
                                            OO0000O0O00O000OO =OO00OOOOO00OOO0O0 +1 #line:385
                                            time .sleep (random .randint (1 ,3 )/10 )#line:387
                                            O0000OOOOOOOOOO0O =f'_site={OO0000O0O00O000OO - 1}&targetSite={O00OOOOOO0OOO0OOO - 1}_{timi_new()}'#line:388
                                            O0OOOOOO0O000O0O0 ={'accept':'application/json, text/plain, */*','authorization':OO000000O00000OOO .token ,'timestamp':timi_new (),'sign':sign (O0000OOOOOOOOOO0O ),'signstring':O0000OOOOOOOOOO0O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:403
                                            O000OOO00O0O0O0OO ={"site":int (OO0000O0O00O000OO -1 ),"targetSite":int (O00OOOOOO0OOO0OOO -1 )}#line:404
                                            O00000OO00OOO0OOO =requests .request ('post',f'{host}/game/crops/move',headers =O0OOOOOO0O000O0O0 ,json =O000OOO00O0O0O0OO ).json ()#line:406
                                            if 'status'in O00000OO00OOO0OOO :#line:407
                                                if O00000OO00OOO0OOO ['status']==200 :#line:408
                                                    pass #line:409
                                            print ('【种植合成】:',OO0000O0O00O000OO ,O00OOOOOO0OOO0OOO ,'合成成功')#line:411
                                            O0OOOOO0O0OOO0O0O =True #line:412
                                    if O0OOOOO0O0OOO0O0O :#line:413
                                        break #line:414
                                if O0OOOOO0O0OOO0O0O :#line:415
                                    break #line:416
        except Exception as O00000O00OOOOOOO0 :#line:417
            OO000000O00000OOO .synthetic ()#line:418
    def level_new (O0O0O000OO00O00OO ):#line:421
        try :#line:422
            OOOO0OOOOOOO000O0 =f'__{timi_new()}'#line:423
            O0O000OOOOOO0O000 ={'authorization':O0O0O000OO00O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOOOOO000O0 ),'signstring':OOOO0OOOOOOO000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:432
            O0O000O0O0O0OO0OO =requests .request ('get',f'{host}/user',headers =O0O000OOOOOO0O000 ).json ()#line:433
            if 'status'in O0O000O0O0O0OO0OO :#line:434
                if O0O000O0O0O0OO0OO ['status']==200 :#line:435
                    return float (O0O000O0O0O0OO0OO ['data']['level'])#line:436
        except Exception as OO0O0OO00O000000O :#line:437
            print (OO0O0OO00O000000O )#line:438
    def propsraffle (O0OO00OOOOOO0OOO0 ):#line:441
        try :#line:442
            while True :#line:443
                OOO0000O0O0OO0OOO =f'__{timi_new()}'#line:444
                O0OOO00OO000O0000 ={'authorization':O0OO00OOOOOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O0O0OO0OOO ),'signstring':OOO0000O0O0OO0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:453
                O0O0O00O0OO0O0OOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OOO00OO000O0000 ).json ()#line:454
                if 'status'in O0O0O00O0OO0O0OOO :#line:456
                    if O0O0O00O0OO0O0OOO ['status']==200 :#line:457
                        OO00000OOOO0O0000 =O0O0O00O0OO0O0OOO ['data']['rows']#line:458
                        O0OO0O0OOO0O0O0O0 =O0O0O00O0OO0O0OOO ['data']['vstate']#line:459
                        if OO00000OOOO0O0000 ==5 or OO00000OOOO0O0000 ==6 or OO00000OOOO0O0000 ==7 :#line:460
                            OO0O0O00000OOOOO0 =O0O0O00O0OO0O0OOO ['data']['silver']#line:461
                            print (f'【转盘抽奖】:获得种子:{OO0O0O00000OOOOO0}')#line:462
                        if OO00000OOOO0O0000 ==1 or OO00000OOOO0O0000 ==2 or OO00000OOOO0O0000 ==3 :#line:463
                            OOO0OO0OOO0OOO00O =O0O0O00O0OO0O0OOO ['data']['clover']#line:464
                            print (f'【转盘抽奖】:获得三叶草:{OOO0OO0OOO0OOO00O}')#line:465
                        if OO00000OOOO0O0000 ==4 or OO00000OOOO0O0000 ==8 :#line:466
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:467
                        if OO00000OOOO0O0000 =='抽奖次数已用完':#line:471
                            if O0OO0O0OOO0O0O0O0 :#line:472
                                OOO0000O0O0OO0OOO =f'__{timi_new()}'#line:473
                                O0OOO00OO000O0000 ={'authorization':O0OO00OOOOOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O0O0OO0OOO ),'signstring':OOO0000O0O0OO0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:482
                                O0O00000OOOOO00OO =requests .request ('get',f'{host}/user',headers =O0OOO00OO000O0000 ).json ()#line:483
                                if 'status'in O0O00000OOOOO00OO :#line:484
                                    if O0O00000OOOOO00OO ['status']==200 :#line:485
                                        O0OO00O0000O0O0OO =O0O00000OOOOO00OO ['data']['level']#line:486
                                        if float (O0OO00O0000O0O0OO )>39 :#line:487
                                            O0OO0OOOO00OO0OOO =random .randint (160 ,190 )/10 #line:488
                                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{O0OO0OOOO00OO0OOO}秒获取抽奖机会')#line:489
                                            time .sleep (O0OO0OOOO00OO0OOO )#line:490
                                            OOO0O0O00OO00OO00 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O0OOO00OO000O0000 ).json ()#line:491
                                            if 'status'in OOO0O0O00OO00OO00 :#line:493
                                                if OOO0O0O00OO00OO00 ['status']==200 :#line:494
                                                    print (f'【转盘抽奖】:{OOO0O0O00OO00OO00["message"]}')#line:495
                                                if OOO0O0O00OO00OO00 ['status']==500 :#line:496
                                                    print (f'【转盘抽奖】:{OOO0O0O00OO00OO00["message"]}')#line:497
                                                    break #line:498
                                            time .sleep (random .randint (10 ,15 )/10 )#line:499
                                        else :#line:500
                                            break #line:501
                            else :#line:502
                                break #line:503
                time .sleep (random .randint (8 ,15 )/10 )#line:504
        except Exception as OO0OO0O0OOOOOO000 :#line:505
            print (OO0OO0O0OOOOOO000 )#line:506
    def friends_invitation (OO0OOO0O000O0OO00 ):#line:509
        try :#line:510
            OOOO0OOO0OO00O0OO =f'__{timi_new()}'#line:511
            OO00O000O00O00OO0 ={'authorization':OO0OOO0O000O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO0OO00O0OO ),'signstring':OOOO0OOO0OO00O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:520
            OO000O0OO0O0000OO =requests .request ('get',f'{host}/friends',headers =OO00O000O00O00OO0 ).json ()#line:521
            if 'status'in OO000O0OO0O0000OO :#line:522
                if OO000O0OO0O0000OO ['status']==200 :#line:523
                    O00O0000O000O0O00 =OO000O0OO0O0000OO ['data']['myInviteter']#line:524
                    if O00O0000O000O0O00 :#line:525
                        OO0000OO000O0OOO0 =O00O0000O000O0O00 ['user']['nickname']#line:526
                        O00OO00OO0000O0O0 =OO0OOO0O000O0OO00 .certification ()#line:527
                        print (f'【查邀请人】:我的邀请人:{OO0000OO000O0OOO0}丨实名:{O00OO00OO0000O0O0}')#line:528
                    else :#line:529
                        if OO0OOO0O000O0OO00 .innerId !='0':#line:530
                            OOOO0OOO0OO00O0OO =f'_innerId=1937553_{timi_new()}'#line:531
                            OO00O000O00O00OO0 ={'authorization':OO0OOO0O000O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO0OO00O0OO ),'signstring':OOOO0OOO0OO00O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:540
                            OO000000OO0OOOO00 ={"innerId":'1937553'}#line:541
                            O0O0000000OOOOOOO =requests .request ('post',f'{host}/friends/my-invitation',headers =OO00O000O00O00OO0 ,data =OO000000OO0OOOO00 ).json ()#line:543
        except Exception as OOOOO0O0000OOO00O :#line:544
            print (OOOOO0O0000OOO00O )#line:545
    def add_clover (OO0OOOOO0O0OOOO0O ):#line:548
        global golden_seed #line:549
        try :#line:550
            O0OO00O0O0O000OOO =f'__{timi_new()}'#line:551
            O0O00OO0O0OO0OO00 ={'authorization':OO0OOOOO0O0OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0O0O000OOO ),'signstring':O0OO00O0O0O000OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:560
            OOO00OO0OO00OOOOO =requests .request ('get',f'{host}/assets/clovers',headers =O0O00OO0O0OO0OO00 ).json ()#line:561
            if 'status'in OOO00OO0OO00OOOOO :#line:563
                if OOO00OO0OO00OOOOO ['status']==200 :#line:564
                    O0OO000O0O0OO0O00 =OOO00OO0OO00OOOOO ['data']['clover']#line:565
                    O0O0O0OO0OO0OO00O =OOO00OO0OO00OOOOO ['data']['used_clover']#line:566
                    O0OO0O00OO0OOO0OO =float (O0OO000O0O0OO0O00 )-float (O0O0O0OO0OO0OO00O )#line:567
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0O0O0OO0OO0OO00O}')#line:568
                    if OO0OOOOO0O0OOOO0O .certification ():#line:569
                        if O0OO0O00OO0OOO0OO >1 :#line:570
                            O0OO00O0O0O000OOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OO0O00OO0OOO0OO)}_{timi_new()}'#line:571
                            O0O00OO0O0OO0OO00 ={'authorization':OO0OOOOO0O0OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0O0O000OOO ),'signstring':O0OO00O0O0O000OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:580
                            O0OO0O00O0O0O000O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OO0O00OO0OOO0OO )}#line:581
                            OOO00000OOOOO0OOO =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O00OO0O0OO0OO00 ,data =O0OO0O00O0O0O000O ).json ()#line:582
                            if 'status'in OOO00000OOOOO0OOO :#line:584
                                if OOO00000OOOOO0OOO ['status']==200 :#line:585
                                    print (f'【参与抽奖】:添加三叶草:{OOO00000OOOOO0OOO["data"]}丨数量:{O0OO0O00OO0OOO0OO}')#line:586
                                if OOO00000OOOOO0OOO ['status']==500 :#line:587
                                    print (f'【参与抽奖】:添加三叶草:{OOO00000OOOOO0OOO["message"]}')#line:588
            OOOO0000000000O0O =requests .request ('get',f'{host}/lottery',headers =O0O00OO0O0OO0OO00 ).json ()#line:589
            OOOO0O00000OO0O00 =OO0OOOOO0O0OOOO0O .winning_rewards ()#line:591
            if 'status'in OOOO0000000000O0O :#line:592
                if OOOO0000000000O0O ['status']==200 :#line:593
                    O00O00O0OO00O0OOO =OOOO0000000000O0O ['data'][0 ]['day_get_gold_quantity']#line:594
                    golden_seed +=float (O00O00O0OO00O0OOO )#line:595
                    print (f'【参与抽奖】:预计每天中{O00O00O0OO00O0OOO[:6]}颗金种子丨好友收益:{str(OOOO0O00000OO0O00)[:6]}')#line:596
        except Exception as O0OOOOO00O0OOO0OO :#line:597
            print (O0OOOOO00O0OOO0OO )#line:598
    def energy (OO0OO00000000O000 ):#line:601
        OOO00O0O0OO00OO00 =f'__{timi_new()}'#line:602
        O0O0000OOOO0O00OO ={'authorization':OO0OO00000000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0O0OO00OO00 ),'signstring':OOO00O0O0OO00OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:611
        OOO0OOOO00OOOOO00 =requests .request ('get',f'{host}/energy/general',headers =O0O0000OOOO0O00OO ).json ()#line:612
        if 'status'in OOO0OOOO00OOOOO00 :#line:614
            if OOO0OOOO00OOOOO00 ['status']==200 :#line:615
                OO00OO000O0OOOO00 =OOO0OOOO00OOOOO00 ['data']['ordinary_water_consumptions']#line:616
                if float (OO00OO000O0OOOO00 )<80 :#line:617
                    OO0OOOOO0000OOO0O =99 -float (OO00OO000O0OOOO00 )#line:618
                    O00OOOOOO0OO00OOO ={"fertilizer":str (OO0OOOOO0000OOO0O ).split ('.')[0 ]}#line:619
                    OO0O000OOOOO00O00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0O0000OOOO0O00OO ,data =O00OOOOOO0OO00OOO ).json ()#line:620
                    if 'status'in OO0O000OOOOO00O00 :#line:622
                        if OO0O000OOOOO00O00 ['status']==200 :#line:623
                            print (f'【购买肥料】:{OO0O000OOOOO00O00["message"]}')#line:624
                OO0OO00OOO0000000 =OOO0OOOO00OOOOO00 ['data']['ordinary_water_consumptions']#line:625
                if float (OO0OO00OOO0000000 )<800 :#line:626
                    O0O0OOOO000OO00OO =999 -float (OO0OO00OOO0000000 )#line:627
                    OOO00OOO0OOOOO0O0 ={"water":str (O0O0OOOO000OO00OO ).split ('.')[0 ]}#line:628
                    OO0OO00OOOOOOO0O0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O0000OOOO0O00OO ,data =OOO00OOO0OOOOO0O0 ).json ()#line:629
                    if 'status'in OO0OO00OOOOOOO0O0 :#line:630
                        if OO0OO00OOOOOOO0O0 ['status']==200 :#line:631
                            print (f'【购买水滴】:{OO0OO00OOOOOOO0O0["message"]}')#line:632
def version_of_the_validation ():#line:636
    return str ((67 -56 )/10 )#line:637
def gitee_validation ():#line:640
    try :#line:641
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:642
    except Exception as OOOO0OO0O000O0OOO :#line:643
        sys .exit (0 )#line:644
def update_the_validation ():#line:648
    try :#line:649
        O000OOO0O0OOO0O00 =gitee_validation ()#line:650
        if version_of_the_validation ()<O000OOO0O0OOO0O00 ['CityEarth']['edition']:#line:651
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOO0O0OOO0O00["CityEarth"]["edition"]}   ❌')#line:652
            print (f'更新内容=>>{O000OOO0O0OOO0O00["CityEarth"]["content"]}   👍')#line:653
        else :#line:654
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOO0O0OOO0O00["CityEarth"]["edition"]}   ✅')#line:655
            print (f'更新内容=>> {O000OOO0O0OOO0O00["CityEarth"]["content"]}   👍')#line:656
    except Exception as OO0000OOOO00OO0OO :#line:657
        print (OO0000OOOO00OO0OO )#line:658
def os_qinglong ():#line:661
    if application in os .environ :#line:662
        O0000OOOOO00OO00O =os .environ [application ].split ('\n')#line:663
        if len (O0000OOOOO00OO00O )>0 :#line:664
            return O0000OOOOO00OO00O #line:665
        else :#line:666
            print (f"{application}变量未启用")#line:667
            print ('脚本退出')#line:668
            sys .exit (1 )#line:669
    else :#line:670
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:672
        return os_built ()#line:673
def os_built ():#line:676
    if token :#line:677
        O000O0O00O000O000 =token .split ('\n')#line:678
        if len (O000O0O00O000O000 )>0 :#line:679
            return O000O0O00O000O000 #line:680
    else :#line:681
        print (f"内置变量为空")#line:682
        print ('脚本结束')#line:683
        sys .exit (0 )#line:684
if __name__ =='__main__':#line:687
    start ()#line:688
