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
        OO00O0OO0OOO000O0 =os_qinglong ()#line:7
        print (f"==========共找到{len(OO00O0OO0OOO000O0)}个账号==========")#line:8
        for OO000O0000OOO0OO0 in OO00O0OO0OOO000O0 :#line:9
            print (f"------------正在执行第{OO00O0OO0OOO000O0.index(OO000O0000OOO0OO0) + 1}个账号------------")#line:10
            O0OO0O00O000OO0O0 =CityEarth (OO000O0000OOO0OO0 )#line:11
            def O0OOO0O0OO0OO0OOO ():#line:13
                if O0OO0O00O000OO0O0 .base_info ():#line:15
                    O0OO0O00O000OO0O0 .game_map ()#line:19
                    O0OO0O00O000OO0O0 .friends_invitation ()#line:21
                    O0OO0O00O000OO0O0 .add_clover ()#line:23
                    O0OO0O00O000OO0O0 .energy ()#line:25
                    O0OO0O00O000OO0O0 .propsraffle ()#line:27
                    O0OO0O00O000OO0O0 .synthetic ()#line:29
                    O0OO0O00O000OO0O0 .crops_illustrated ()#line:31
                    O0OO0O00O000OO0O0 .give_gold ()#line:33
                else :#line:34
                    print ('token失效')#line:35
            O0O00O0O0OO0O0000 =threading .Thread (target =O0OOO0O0OO0OO0OOO )#line:37
            O0O00O0O0OO0O0000 .start ()#line:38
            time .sleep (time_xx )#line:39
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:41
        time .sleep (3 )#line:42
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:43
    except Exception as OOO0OO00OO00O0O00 :#line:44
        print (OOO0OO00OO00O0O00 )#line:45
def sign (OO00O0O00OOO0O0OO ):#line:48
    OO00OO00O0OO0O0O0 =hashlib .md5 (OO00O0O00OOO0O0OO .encode ()).hexdigest ()#line:49
    O0000OOO000000OOO ="scsc%^&*"+OO00OO00O0OO0O0O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:50
    OO0O0O00O00OO000O =hashlib .md5 (O0000OOO000000OOO .encode ()).hexdigest ()#line:51
    return OO0O0O00O00OO000O #line:52
def timi_new ():#line:55
    return str (int (time .time ()*1000 ))#line:56
class CityEarth :#line:58
    def __init__ (O0OOO00OO000OO00O ,O00OO0O0OO00OO000 ):#line:60
        try :#line:61
            O0OOO00OO000OO00O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:62
            O0OOO00OO000OO00O .token =O00OO0O0OO00OO000 .split ('&')[0 ]#line:63
            O0OOO00OO000OO00O .innerId =O00OO0O0OO00OO000 .split ('&')[1 ]#line:64
            O0OOO00OO000OO00O .doneeNo =O00OO0O0OO00OO000 .split ('&')[2 ]#line:65
        except :#line:66
            print ('变量格式错误')#line:67
    def base_info (O000OOOO0OO00O0O0 ):#line:70
        try :#line:71
            O000OO00O0O0OOOOO =f'__{timi_new()}'#line:72
            O0OOOO0OO0000O000 ={'authorization':O000OOOO0OO00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00O0O0OOOOO ),'signstring':O000OO00O0O0OOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:81
            O00O00O0OOO00000O =requests .request ('get',f'{host}/user',headers =O0OOOO0OO0000O000 ).json ()#line:82
            if 'status'in O00O00O0OOO00000O :#line:84
                if O00O00O0OOO00000O ['status']==200 :#line:85
                    OOO00OO0O0OO0000O =O00O00O0OOO00000O ['data']['nickname']#line:86
                    OO0O000O0000OOOOO =O00O00O0OOO00000O ['data']['inner_id']#line:87
                    OOO0OO0OOO000O0O0 =O00O00O0OOO00000O ['data']['assets']['gold']#line:88
                    O0000OOO0O00O0OO0 =O00O00O0OOO00000O ['data']['level']#line:89
                    print (f'【账号信息】:昵称:{OOO00OO0O0OO0000O[:5]}丨ID:{OO0O000O0000OOOOO}丨等级:{O0000OOO0O00O0OO0}丨种子:{str(OOO0OO0OOO000O0O0).split(".")[0]}')#line:90
                if O00O00O0OOO00000O ['status']==401 :#line:91
                    return False #line:92
                if O00O00O0OOO00000O ['status']==500 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as O00OO0O0000000O0O :#line:96
            print (O00OO0O0000000O0O )#line:97
    def game_map (O0000O000OOO0OOOO ):#line:100
        O000000000OOOO0OO =f'__{timi_new()}'#line:101
        O0O000O0O000O00O0 ={'authorization':O0000O000OOO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000000000OOOO0OO ),'signstring':O000000000OOOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:110
        O000000OOOOOO0000 =requests .request ('get',f'{host}/game/map',headers =O0O000O0O000O00O0 ).json ()#line:111
        if 'status'in O000000OOOOOO0000 :#line:113
            if O000000OOOOOO0000 ['status']==200 :#line:114
                for O0O00O0O0O00OOO00 in O000000OOOOOO0000 ['data']['list'][0 ]['crops']:#line:115
                    OO00O00O0OOOOOO00 =O0O00O0O0O00OOO00 ['level']#line:117
                    if OO00O00O0OOOOOO00 ==41 :#line:118
                        OOO0OOO0000OOO00O =O0O00O0O0O00OOO00 ['crop_name']#line:119
                        OO00OO00O0O0OOOOO =O0O00O0O0O00OOO00 ['count']#line:120
                        if OO00OO00O0O0OOOOO >0 :#line:121
                            print (f'【农业资产】:{OOO0OOO0000OOO00O}丨数量:{OO00OO00O0O0OOOOO}')#line:122
    def give_gold (OOO0OOO00OOO00OO0 ):#line:125
        OOO000O000OOO00OO =f'__{timi_new()}'#line:126
        OOO00OO00OO00000O ={'authorization':OOO0OOO00OOO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O000OOO00OO ),'signstring':OOO000O000OOO00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:135
        OOO0OO0OO0O0OO00O =requests .request ('get',f'{host}/user',headers =OOO00OO00OO00000O ).json ()#line:136
        if 'status'in OOO0OO0OO0O0OO00O :#line:137
            if OOO0OO0OO0O0OO00O ['status']==200 :#line:138
                if float (OOO0OOO00OOO00OO0 .doneeNo )!=0 :#line:139
                    O0OO0O0O0OO00O00O =OOO0OO0OO0O0OO00O ['data']['assets']['gold']#line:140
                    if float (O0OO0O0O0OO00O00O )>float (OOO0OOO00OOO00OO0 .innerId ):#line:141
                        OO00O0OO000O0O00O =int (float (O0OO0O0O0OO00O00O )/1.1 )#line:142
                        OOO000O000OOO00OO =f'_doneeNo={OOO0OOO00OOO00OO0.doneeNo}&quantity={OO00O0OO000O0O00O}_{timi_new()}'#line:143
                        OOO00OO00OO00000O ={'authorization':OOO0OOO00OOO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O000OOO00OO ),'signstring':OOO000O000OOO00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:152
                        O00OO0OO00O0O0OO0 ={"quantity":OO00O0OO000O0O00O ,"doneeNo":OOO0OOO00OOO00OO0 .doneeNo }#line:156
                        OOOOOO000000OOOO0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO00OO00OO00000O ,data =O00OO0OO00O0O0OO0 ).json ()#line:157
                        if 'status'in OOOOOO000000OOOO0 :#line:159
                            if OOOOOO000000OOOO0 ['status']==200 :#line:160
                                if OOOOOO000000OOOO0 ['data']:#line:161
                                    print (f'【赠送种子】:赠送{OO00O0OO000O0O00O}种子给{OOO0OOO00OOO00OO0.doneeNo}成功')#line:162
                else :#line:163
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:164
    def winning_rewards (OO000000OO0O00O00 ):#line:167
        OO000000O0OO0O000 =f'__{timi_new()}'#line:168
        O0OOOOO0OOOO00O00 ={'authorization':OO000000OO0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000O0OO0O000 ),'signstring':OO000000O0OO0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:177
        OOO00O00O000OO00O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOOOO0OOOO00O00 ).json ()#line:178
        if 'status'in OOO00O00O000OO00O :#line:180
            if OOO00O00O000OO00O ['status']==200 :#line:181
                if OOO00O00O000OO00O ['data']['amount']:#line:182
                    O0O00O0OOO0OO00O0 =OOO00O00O000OO00O ['data']['amount']['gold']#line:183
                    return O0O00O0OOO0OO00O0 #line:184
                else :#line:185
                    return 0 #line:186
    def certification (OO0OO0O00OOO0O000 ):#line:189
        OOOOOOOOOOO0O0OOO =f'__{timi_new()}'#line:190
        OO00O000OO0OOOO0O ={'authorization':OO0OO0O00OOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOOOOO0O0OOO ),'signstring':OOOOOOOOOOO0O0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:199
        O00OOO0000000OOO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO00O000OO0OOOO0O ).json ()#line:200
        if 'status'in O00OOO0000000OOO0 :#line:202
            if O00OOO0000000OOO0 ['status']==200 :#line:203
                if O00OOO0000000OOO0 ['data']['result']:#line:204
                    O00O0O00000OOO0O0 =O00OOO0000000OOO0 ['data']['nick_name']#line:205
                    return O00O0O00000OOO0O0 #line:206
                else :#line:207
                    return '未实名'#line:208
    def crops_illustrated (O00OOOOOOO0O0O0OO ):#line:211
        O0000000O0O0O000O =f'__{timi_new()}'#line:212
        OOOOOOO0OOO0O0O00 ={'authorization':O00OOOOOOO0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000000O0O0O000O ),'signstring':O0000000O0O0O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:221
        O0O0O0OO0O0O00O0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOOOOOO0OOO0O0O00 ).json ()#line:222
        if 'status'in O0O0O0OO0O0O00O0O :#line:224
            if O0O0O0OO0O0O00O0O ['status']==200 :#line:225
                O000000O0O0O00000 =O0O0O0OO0O0O00O0O ['data'][0 ]['crops']#line:226
                for OO00O0O000OO00OOO in O000000O0O0O00000 :#line:227
                    if OO00O0O000OO00OOO ['ill_clover_award']:#line:228
                        if float (OO00O0O000OO00OOO ['ill_clover_award'])>1 :#line:229
                            if OO00O0O000OO00OOO ['is_finish']:#line:230
                                if not OO00O0O000OO00OOO ['is_getit']:#line:231
                                    O0000000O0O0O000O =f'_award_level={OO00O0O000OO00OOO["level"]}_{timi_new()}'#line:232
                                    OOOOOOO0OOO0O0O00 ={'authorization':O00OOOOOOO0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000000O0O0O000O ),'signstring':O0000000O0O0O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:241
                                    O0000O0OO0OO0O00O ={"award_level":OO00O0O000OO00OOO ['level']}#line:242
                                    OO000000OO0OO000O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOOOOOO0OOO0O0O00 ,json =O0000O0OO0OO0O00O ).json ()#line:244
                                    if 'status'in OO000000OO0OO000O :#line:245
                                        if OO000000OO0OO000O ['status']==200 :#line:246
                                            O00O000O0OOO0O000 =OO000000OO0OO000O ['data']['ill_clover_award']#line:247
                                            print (f'【图鉴奖励】:领取{OO00O0O000OO00OOO["crop_name"]}成就丨奖励{O00O000O0OOO0O000}叶子成功')#line:249
                                        if OO000000OO0OO000O ['status']==500 :#line:250
                                            print (f'【图鉴奖励】:{OO000000OO0OO000O["message"]}')#line:251
    def watched_ad (OOO00OO0O0OO00OOO ):#line:254
        OO0O00O0OO0O0O000 =f'__{timi_new()}'#line:255
        OOO0O00OO00OOOO00 ={'authorization':OOO00OO0O0OO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O0OO0O0O000 ),'signstring':OO0O00O0OO0O0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:264
        O00O000O000O0O000 =requests .request ('post',f'{host}/game/watched-ad',headers =OOO0O00OO00OOOO00 ).json ()#line:265
        print (O00O000O000O0O000 )#line:266
    def user_ad (O00000O0000OO0000 ):#line:269
        OO00O00OO0OOOO0O0 =f'__{timi_new()}'#line:270
        O00OOOOOO0000000O ={'authorization':O00000O0000OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO0OOOO0O0 ),'signstring':OO00O00OO0OOOO0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:279
        OO0000000O0OOO000 =requests .request ('get',f'{host}/user/ad',headers =O00OOOOOO0000000O ).json ()#line:280
        if 'status'in OO0000000O0OOO000 :#line:282
            if OO0000000O0OOO000 ['status']==200 :#line:283
                O0OOO000O0O000O00 =OO0000000O0OOO000 ['data']['max_time']#line:284
                OO0OO0OOO0O0OO0O0 =OO0000000O0OOO000 ['data']['watch_time']#line:285
                OOO0O0000O00OOO00 =OO0000000O0OOO000 ['data']['added_time']#line:286
                print (f'【获取种子】:获取种子剩余{OOO0O0000O00OOO00 + O0OOO000O0O000O00 - OO0OO0OOO0O0OO0O0}次丨好友提供:{OOO0O0000O00OOO00}次')#line:287
                if OOO0O0000O00OOO00 +O0OOO000O0O000O00 -OO0OO0OOO0O0OO0O0 >0 :#line:288
                    time .sleep (random .randint (16 ,19 ))#line:289
                    OO00OO0OOO00OOO00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00OOOOOO0000000O ).json ()#line:290
                    if 'status'in OO00OO0OOO00OOO00 :#line:292
                        if OO00OO0OOO00OOO00 ['status']==200 :#line:293
                            OO00O0O0O00O0OOOO =OO00OO0OOO00OOO00 ['data']['silver']#line:294
                            print (f'【获取种子】:获得种子:{OO00O0O0O00O0OOOO}')#line:295
                            return True #line:296
                        if OO00OO0OOO00OOO00 ['status']==500 :#line:297
                            OOOO0OOOO0O0OO0OO =OO00OO0OOO00OOO00 ['message']#line:298
                            print (f'【获取种子】:{OOOO0OOOO0O0OO0OO}')#line:299
                            return False #line:300
    def synthetic (OOOO0O0O00O0OO00O ):#line:303
        global id ,g #line:304
        try :#line:305
            OOOOO0OOO0O0000OO =OOOO0O0O00O0OO00O .level_new ()#line:306
            while True :#line:307
                OO00OOO00OOO000OO =f'__{timi_new()}'#line:308
                O000000O00O0OOO00 ={'authorization':OOOO0O0O00O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO00OOO000OO ),'signstring':OO00OOO00OOO000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:317
                OOO0O0000000000O0 =requests .request ('get',f'{host}/game/getAllData',headers =O000000O00O0OOO00 ).json ()#line:318
                if 'status'in OOO0O0000000000O0 :#line:320
                    if OOO0O0000000000O0 ['status']==200 :#line:321
                        O00OOO0OOO000000O =OOO0O0000000000O0 ['data']['cropList']#line:322
                        OO0OO000O0O0OO00O =OOO0O0000000000O0 ['data']['gameCoreDataDBid']#line:323
                        OOOOOOOOOOO0O00OO =0 #line:324
                        for O00O0O0OOOO0O0O0O in O00OOO0OOO000000O :#line:325
                            if not O00O0O0OOOO0O0O0O :#line:326
                                O0O000O00O0OOO000 =f'_crop_id={OO0OO000O0O0OO00O}&site={OOOOOOOOOOO0O00OO}_{OOOO0O0O00O0OO00O.time}'#line:327
                                OO0OOOOO0000OO00O ={'authorization':OOOO0O0O00O0OO00O .token ,'timestamp':OOOO0O0O00O0OO00O .time ,'sign':sign (O0O000O00O0OOO000 ),'signstring':O0O000O00O0OOO000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:336
                                OO0OO0O000OOO0000 ={"site":OOOOOOOOOOO0O00OO ,"crop_id":OO0OO000O0O0OO00O }#line:337
                                OO00O00O00O0O00O0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0OOOOO0000OO00O ,data =OO0OO0O000OOO0000 ).json ()#line:338
                                time .sleep (random .randint (1 ,3 )/10 )#line:340
                                if 'status'in OO00O00O00O0O00O0 :#line:341
                                    if OO00O00O00O0O00O0 ['status']==200 :#line:342
                                        if OO00O00O00O0O00O0 ['message']=='种子数量不足':#line:343
                                            OOOOO0OOO0O0000OO =OOOO0O0O00O0OO00O .level_new ()#line:344
                                            print (f'【种植合成】:{OO00O00O00O0O00O0["message"]}')#line:345
                                            if not OOOO0O0O00O0OO00O .user_ad ():#line:346
                                                return False #line:347
                                        print (f'【种植合成】:种植农作物,位置{OOOOOOOOOOO0O00OO}')#line:348
                                    if OO00O00O00O0O00O0 ['status']==500 :#line:349
                                        print (f'【种植合成】:{OO00O00O00O0O00O0["message"]}')#line:350
                                        return False #line:351
                            OOOOOOOOOOO0O00OO +=1 #line:352
                        OOO0O0O000OOOO00O =requests .request ('get',f'{host}/game/getAllData',headers =O000000O00O0OOO00 ).json ()#line:353
                        OOOOOO0OOO00OO0O0 =OOO0O0O000OOOO00O ['data']['cropList']#line:354
                        OO0O0OOOO0OOO00OO =False #line:355
                        for O00O0O0OOOO0O0O0O in range (12 ):#line:356
                            id =OOOOOO0OOO00OO0O0 [O00O0O0OOOO0O0O0O ]['level']#line:357
                            if float (OOOOO0OOO0O0000OO )-float (id )>9 :#line:358
                                O00000O0O0OOO0OOO =f'_site={O00O0O0OOOO0O0O0O}_{timi_new()}'#line:359
                                OOO0O00OOOO0OOOOO ={'accept':'application/json, text/plain, */*','authorization':OOOO0O0O00O0OO00O .token ,'timestamp':timi_new (),'sign':sign (O00000O0O0OOO0OOO ),'signstring':O00000O0O0OOO0OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:369
                                OOOOOO000000O0O0O ={"site":O00O0O0OOOO0O0O0O }#line:370
                                O000O00O0000O000O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO0O00OOOO0OOOOO ,data =OOOOOO000000O0O0O ).json ()#line:372
                                if 'status'in O000O00O0000O000O :#line:373
                                    if O000O00O0000O000O ['status']==200 :#line:374
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:375
                            if id !=0 :#line:376
                                for O0O00OOOO0O0000O0 in range (11 ):#line:377
                                    O0OO000000O0O0000 =O0O00OOOO0O0000O0 +1 #line:378
                                    g =OOOOOO0OOO00OO0O0 [O0OO000000O0O0000 ]['level']#line:379
                                    if id ==g :#line:380
                                        O000OO0OOOO0000OO =O0O00OOOO0O0000O0 +2 #line:381
                                        if O000OO0OOOO0000OO ==O00O0O0OOOO0O0O0O +1 :#line:382
                                            pass #line:383
                                        else :#line:384
                                            OO0O000O0OOOOO000 =O00O0O0OOOO0O0O0O +1 #line:385
                                            time .sleep (random .randint (1 ,3 )/10 )#line:387
                                            OOOO0OO0OO0O000O0 =f'_site={OO0O000O0OOOOO000 - 1}&targetSite={O000OO0OOOO0000OO - 1}_{timi_new()}'#line:388
                                            OOO00OOOO0OO00O0O ={'accept':'application/json, text/plain, */*','authorization':OOOO0O0O00O0OO00O .token ,'timestamp':timi_new (),'sign':sign (OOOO0OO0OO0O000O0 ),'signstring':OOOO0OO0OO0O000O0 ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:403
                                            OOO000OO0O00O00OO ={"site":int (OO0O000O0OOOOO000 -1 ),"targetSite":int (O000OO0OOOO0000OO -1 )}#line:404
                                            OOOOOOOO0OOOOO000 =requests .request ('post',f'{host}/game/crops/move',headers =OOO00OOOO0OO00O0O ,json =OOO000OO0O00O00OO ).json ()#line:406
                                            if 'status'in OOOOOOOO0OOOOO000 :#line:407
                                                if OOOOOOOO0OOOOO000 ['status']==200 :#line:408
                                                    pass #line:409
                                            print ('【种植合成】:',OO0O000O0OOOOO000 ,O000OO0OOOO0000OO ,'合成成功')#line:411
                                            OO0O0OOOO0OOO00OO =True #line:412
                                    if OO0O0OOOO0OOO00OO :#line:413
                                        break #line:414
                                if OO0O0OOOO0OOO00OO :#line:415
                                    break #line:416
        except Exception as O00O00OOO0000OOO0 :#line:417
            OOOO0O0O00O0OO00O .synthetic ()#line:418
    def level_new (O0OOOO00OOOO0OO00 ):#line:421
        try :#line:422
            O000000O00OO0O0O0 =f'__{timi_new()}'#line:423
            O0O00OO0000O0OO0O ={'authorization':O0OOOO00OOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O00OO0O0O0 ),'signstring':O000000O00OO0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:432
            O0O0OOO0OOO000OOO =requests .request ('get',f'{host}/user',headers =O0O00OO0000O0OO0O ).json ()#line:433
            if 'status'in O0O0OOO0OOO000OOO :#line:434
                if O0O0OOO0OOO000OOO ['status']==200 :#line:435
                    return float (O0O0OOO0OOO000OOO ['data']['level'])#line:436
        except Exception as OO00OO000000O0000 :#line:437
            print (OO00OO000000O0000 )#line:438
    def propsraffle (OOO00OOO000000O00 ):#line:441
        try :#line:442
            while True :#line:443
                O0OOO0O00O00OOO0O =f'__{timi_new()}'#line:444
                O0O0OOOOOOO00OO0O ={'authorization':OOO00OOO000000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O00O00OOO0O ),'signstring':O0OOO0O00O00OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:453
                OO00OO0O000OOO0O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O0OOOOOOO00OO0O ).json ()#line:454
                if 'status'in OO00OO0O000OOO0O0 :#line:456
                    if OO00OO0O000OOO0O0 ['status']==200 :#line:457
                        OOOOOO0OO0OO0O00O =OO00OO0O000OOO0O0 ['data']['rows']#line:458
                        OO00OO000000OOO00 =OO00OO0O000OOO0O0 ['data']['vstate']#line:459
                        if OOOOOO0OO0OO0O00O ==5 or OOOOOO0OO0OO0O00O ==6 or OOOOOO0OO0OO0O00O ==7 :#line:460
                            OO00O0OOO0OO0OO00 =OO00OO0O000OOO0O0 ['data']['silver']#line:461
                            print (f'【转盘抽奖】:获得种子:{OO00O0OOO0OO0OO00}')#line:462
                        if OOOOOO0OO0OO0O00O ==1 or OOOOOO0OO0OO0O00O ==2 or OOOOOO0OO0OO0O00O ==3 :#line:463
                            O000O0O00OOO0OOOO =OO00OO0O000OOO0O0 ['data']['clover']#line:464
                            print (f'【转盘抽奖】:获得三叶草:{O000O0O00OOO0OOOO}')#line:465
                        if OOOOOO0OO0OO0O00O ==4 or OOOOOO0OO0OO0O00O ==8 :#line:466
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:467
                        if OOOOOO0OO0OO0O00O =='抽奖次数已用完':#line:471
                            if OO00OO000000OOO00 :#line:472
                                O0OOO0O00O00OOO0O =f'__{timi_new()}'#line:473
                                O0O0OOOOOOO00OO0O ={'authorization':OOO00OOO000000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O00O00OOO0O ),'signstring':O0OOO0O00O00OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:482
                                O0O0000OO000000OO =requests .request ('get',f'{host}/user',headers =O0O0OOOOOOO00OO0O ).json ()#line:483
                                if 'status'in O0O0000OO000000OO :#line:484
                                    if O0O0000OO000000OO ['status']==200 :#line:485
                                        O0O0OOOO000OOOOOO =O0O0000OO000000OO ['data']['level']#line:486
                                        if float (O0O0OOOO000OOOOOO )>39 :#line:487
                                            O0OO00000O0000OOO =random .randint (160 ,190 )/10 #line:488
                                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{O0OO00000O0000OOO}秒获取抽奖机会')#line:489
                                            time .sleep (O0OO00000O0000OOO )#line:490
                                            O00O0O000O0OOO0OO =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O0O0OOOOOOO00OO0O ).json ()#line:491
                                            if 'status'in O00O0O000O0OOO0OO :#line:493
                                                if O00O0O000O0OOO0OO ['status']==200 :#line:494
                                                    print (f'【转盘抽奖】:{O00O0O000O0OOO0OO["message"]}')#line:495
                                                if O00O0O000O0OOO0OO ['status']==500 :#line:496
                                                    print (f'【转盘抽奖】:{O00O0O000O0OOO0OO["message"]}')#line:497
                                                    break #line:498
                                            time .sleep (random .randint (10 ,15 )/10 )#line:499
                                        else :#line:500
                                            break #line:501
                            else :#line:502
                                break #line:503
                time .sleep (random .randint (8 ,15 )/10 )#line:504
        except Exception as O0OOO00O0O000O0O0 :#line:505
            print (O0OOO00O0O000O0O0 )#line:506
    def friends_invitation (O0OO0OO0OOOOOO0OO ):#line:509
        try :#line:510
            OO0OOO0000OOO000O =f'__{timi_new()}'#line:511
            O00000OO00O000OO0 ={'authorization':O0OO0OO0OOOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0000OOO000O ),'signstring':OO0OOO0000OOO000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:520
            O0000000O00OO0OOO =requests .request ('get',f'{host}/friends',headers =O00000OO00O000OO0 ).json ()#line:521
            if 'status'in O0000000O00OO0OOO :#line:522
                if O0000000O00OO0OOO ['status']==200 :#line:523
                    O0O00OO00000OO0OO =O0000000O00OO0OOO ['data']['myInviteter']#line:524
                    if O0O00OO00000OO0OO :#line:525
                        O00000000000OO0O0 =O0O00OO00000OO0OO ['user']['nickname']#line:526
                        O0OOO000000OOOO0O =O0OO0OO0OOOOOO0OO .certification ()#line:527
                        print (f'【查邀请人】:我的邀请人:{O00000000000OO0O0}丨实名:{O0OOO000000OOOO0O}')#line:528
                    else :#line:529
                        if O0OO0OO0OOOOOO0OO .innerId !='0':#line:530
                            OO0OOO0000OOO000O =f'_innerId=1937553_{timi_new()}'#line:531
                            O00000OO00O000OO0 ={'authorization':O0OO0OO0OOOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0000OOO000O ),'signstring':OO0OOO0000OOO000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:540
                            O0O000OOOOOOOO000 ={"innerId":'1937553'}#line:541
                            OO00O0O00OO0OOOO0 =requests .request ('post',f'{host}/friends/my-invitation',headers =O00000OO00O000OO0 ,data =O0O000OOOOOOOO000 ).json ()#line:543
        except Exception as O0OOO000O0000O000 :#line:544
            print (O0OOO000O0000O000 )#line:545
    def add_clover (O00O000000OOO0O00 ):#line:548
        global golden_seed #line:549
        try :#line:550
            O0O00O00000O0O000 =f'__{timi_new()}'#line:551
            OOOOO00O00OOO0O00 ={'authorization':O00O000000OOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00000O0O000 ),'signstring':O0O00O00000O0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:560
            OOOOO0000OOOO000O =requests .request ('get',f'{host}/assets/clovers',headers =OOOOO00O00OOO0O00 ).json ()#line:561
            if 'status'in OOOOO0000OOOO000O :#line:563
                if OOOOO0000OOOO000O ['status']==200 :#line:564
                    O00OOO00000OOO000 =OOOOO0000OOOO000O ['data']['clover']#line:565
                    O0O00O00O00OOOOOO =OOOOO0000OOOO000O ['data']['used_clover']#line:566
                    OO0OO00O0O0O000O0 =float (O00OOO00000OOO000 )-float (O0O00O00O00OOOOOO )#line:567
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0O00O00O00OOOOOO}')#line:568
                    if OO0OO00O0O0O000O0 >1 :#line:569
                        O0O00O00000O0O000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0OO00O0O0O000O0)}_{timi_new()}'#line:570
                        OOOOO00O00OOO0O00 ={'authorization':O00O000000OOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00000O0O000 ),'signstring':O0O00O00000O0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:579
                        O0O00OOOO0OO0000O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0OO00O0O0O000O0 )}#line:580
                        O00O0000OO0000OO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOOO00O00OOO0O00 ,data =O0O00OOOO0OO0000O ).json ()#line:581
                        if 'status'in O00O0000OO0000OO0 :#line:583
                            if O00O0000OO0000OO0 ['status']==200 :#line:584
                                print (f'【参与抽奖】:添加三叶草:{O00O0000OO0000OO0["data"]}丨数量:{OO0OO00O0O0O000O0}')#line:585
            O0O0000OO0OOO0O00 =requests .request ('get',f'{host}/lottery',headers =OOOOO00O00OOO0O00 ).json ()#line:586
            O000OOOO00OOOOOOO =O00O000000OOO0O00 .winning_rewards ()#line:588
            if 'status'in O0O0000OO0OOO0O00 :#line:589
                if O0O0000OO0OOO0O00 ['status']==200 :#line:590
                    OOOOO0OOOOO00O0O0 =O0O0000OO0OOO0O00 ['data'][0 ]['day_get_gold_quantity']#line:591
                    golden_seed +=float (OOOOO0OOOOO00O0O0 )#line:592
                    print (f'【参与抽奖】:预计每天中{OOOOO0OOOOO00O0O0[:6]}颗金种子丨好友收益:{str(O000OOOO00OOOOOOO)[:6]}')#line:593
        except Exception as O00000OO00O00000O :#line:594
            print (O00000OO00O00000O )#line:595
    def energy (O000OO0000O00O000 ):#line:598
        OO000O00O0O0000OO =f'__{timi_new()}'#line:599
        O00OOOOOOO00O0OO0 ={'authorization':O000OO0000O00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00O0O0000OO ),'signstring':OO000O00O0O0000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:608
        OO00OO0OO0OO0O0OO =requests .request ('get',f'{host}/energy/general',headers =O00OOOOOOO00O0OO0 ).json ()#line:609
        if 'status'in OO00OO0OO0OO0O0OO :#line:611
            if OO00OO0OO0OO0O0OO ['status']==200 :#line:612
                O0O0OO0O000O0OOO0 =OO00OO0OO0OO0O0OO ['data']['ordinary_water_consumptions']#line:613
                if float (O0O0OO0O000O0OOO0 )<80 :#line:614
                    OOOO00000O0000000 =99 -float (O0O0OO0O000O0OOO0 )#line:615
                    O0O0OOO00OO0000OO ={"fertilizer":str (OOOO00000O0000000 ).split ('.')[0 ]}#line:616
                    O0O0OOO0O0OOOO000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O00OOOOOOO00O0OO0 ,data =O0O0OOO00OO0000OO ).json ()#line:617
                    if 'status'in O0O0OOO0O0OOOO000 :#line:619
                        if O0O0OOO0O0OOOO000 ['status']==200 :#line:620
                            print (f'【购买肥料】:{O0O0OOO0O0OOOO000["message"]}')#line:621
                O0O00OO0OO0000OO0 =OO00OO0OO0OO0O0OO ['data']['ordinary_water_consumptions']#line:622
                if float (O0O00OO0OO0000OO0 )<800 :#line:623
                    O0000OO0OOOO0OO00 =999 -float (O0O00OO0OO0000OO0 )#line:624
                    OO00O0OOO00000O00 ={"water":str (O0000OO0OOOO0OO00 ).split ('.')[0 ]}#line:625
                    O00O00O0O0OO0O0O0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O00OOOOOOO00O0OO0 ,data =OO00O0OOO00000O00 ).json ()#line:626
                    if 'status'in O00O00O0O0OO0O0O0 :#line:627
                        if O00O00O0O0OO0O0O0 ['status']==200 :#line:628
                            print (f'【购买水滴】:{O00O00O0O0OO0O0O0["message"]}')#line:629
def version_of_the_validation ():#line:633
    return str ((67 -56 )/10 )#line:634
def gitee_validation ():#line:637
    try :#line:638
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:639
    except Exception as OOOOOO0O00O000O00 :#line:640
        sys .exit (0 )#line:641
def update_the_validation ():#line:645
    try :#line:646
        O00O0O000O0000000 =gitee_validation ()#line:647
        if version_of_the_validation ()<O00O0O000O0000000 ['CityEarth']['edition']:#line:648
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0O000O0000000["CityEarth"]["edition"]}   ❌')#line:649
            print (f'更新内容=>>{O00O0O000O0000000["CityEarth"]["content"]}   👍')#line:650
        else :#line:651
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0O000O0000000["CityEarth"]["edition"]}   ✅')#line:652
            print (f'更新内容=>> {O00O0O000O0000000["CityEarth"]["content"]}   👍')#line:653
    except Exception as O0O00O00O0O000OO0 :#line:654
        print (O0O00O00O0O000OO0 )#line:655
def os_qinglong ():#line:658
    if application in os .environ :#line:659
        OOOOOO00O0OOOOO00 =os .environ [application ].split ('\n')#line:660
        if len (OOOOOO00O0OOOOO00 )>0 :#line:661
            return OOOOOO00O0OOOOO00 #line:662
        else :#line:663
            print (f"{application}变量未启用")#line:664
            print ('脚本退出')#line:665
            sys .exit (1 )#line:666
    else :#line:667
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:669
        return os_built ()#line:670
def os_built ():#line:673
    if token :#line:674
        OO0O00O0OOOO0000O =token .split ('\n')#line:675
        if len (OO0O00O0OOOO0000O )>0 :#line:676
            return OO0O00O0OOOO0000O #line:677
    else :#line:678
        print (f"内置变量为空")#line:679
        print ('脚本结束')#line:680
        sys .exit (0 )#line:681
if __name__ =='__main__':#line:684
    start ()#line:685
