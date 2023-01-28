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
@ cron: 12 */3 * * *
@ new Env('生城世朝')
@ 项目地址  微信打开  http://share.sc19319.com/scsc/1937553
@ 抓取  http://scsc.sc19319.com 的authorization值
@ 青龙变量  青龙配置文件 export ce_token="authorization&绑定邀请码&赠送金种子id"   不绑定和不赠送填 0   多号换行
@
@ 变量示范    export ce_token="557b8069-1234-4ae7-9e29-b7871f91541b&1937553&0"  用&符号分开数据
@ 我的邀请码是  1937553
@ 版本  1.0
"""
application = 'ce_token'  # 变量名
token = ''

time_xx = random.randint(8, 12)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://scsc.sc19319.com'#line:2
def start ():#line:5
    try :#line:6
        update_the_validation ()#line:7
        O0OOOOOO0OO000O00 =os_qinglong ()#line:8
        print (f"==========共找到{len(O0OOOOOO0OO000O00)}个账号==========")#line:9
        for O0OO0OO000000O00O in O0OOOOOO0OO000O00 :#line:10
            print (f"------------正在执行第{O0OOOOOO0OO000O00.index(O0OO0OO000000O00O) + 1}个账号------------")#line:11
            OOO000OOO0OOO00OO =CityEarth (O0OO0OO000000O00O )#line:12
            def OO0OOOO000OOO0O00 ():#line:14
                if OOO000OOO0OOO00OO .base_info ():#line:16
                    OOO000OOO0OOO00OO .game_map ()#line:20
                    OOO000OOO0OOO00OO .friends_invitation ()#line:22
                    OOO000OOO0OOO00OO .add_clover ()#line:24
                    OOO000OOO0OOO00OO .energy ()#line:26
                    OOO000OOO0OOO00OO .synthetic ()#line:28
                    OOO000OOO0OOO00OO .propsraffle ()#line:30
                    OOO000OOO0OOO00OO .crops_illustrated ()#line:32
                    OOO000OOO0OOO00OO .give_gold ()#line:34
                else :#line:35
                    print ('token失效')#line:36
            O0O0000O00O00000O =threading .Thread (target =OO0OOOO000OOO0O00 )#line:38
            O0O0000O00O00000O .start ()#line:39
            time .sleep (time_xx )#line:40
    except Exception as O0OO0O000O0O0OO00 :#line:41
        print (O0OO0O000O0O0OO00 )#line:42
def sign (O00OO00000000000O ):#line:45
    OO0OO000O0OO0OOOO =hashlib .md5 (O00OO00000000000O .encode ()).hexdigest ()#line:46
    OO000000O000OO0OO ="scsc%^&*"+OO0OO000O0OO0OOOO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:47
    O0O0OOO00000OOOO0 =hashlib .md5 (OO000000O000OO0OO .encode ()).hexdigest ()#line:48
    return O0O0OOO00000OOOO0 #line:49
def timi_new ():#line:52
    return str (int (time .time ()*1000 ))#line:53
class CityEarth :#line:56
    def __init__ (O00O000OOOOOOO0O0 ,OOO0O0OOO00OO0000 ):#line:58
        try :#line:59
            O00O000OOOOOOO0O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:60
            O00O000OOOOOOO0O0 .token =OOO0O0OOO00OO0000 .split ('&')[0 ]#line:61
            O00O000OOOOOOO0O0 .innerId =OOO0O0OOO00OO0000 .split ('&')[1 ]#line:62
            O00O000OOOOOOO0O0 .doneeNo =OOO0O0OOO00OO0000 .split ('&')[2 ]#line:63
        except :#line:64
            print ('变量格式错误')#line:65
    def base_info (OOO000O00000O0O0O ):#line:68
        try :#line:69
            OOO00OOO0OOOOO00O =f'__{timi_new()}'#line:70
            O0OO00O00O0OOO0O0 ={'authorization':OOO000O00000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO0OOOOO00O ),'signstring':OOO00OOO0OOOOO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:79
            O000O0OO000O00000 =requests .request ('get',f'{host}/user',headers =O0OO00O00O0OOO0O0 ).json ()#line:80
            if 'status'in O000O0OO000O00000 :#line:82
                if O000O0OO000O00000 ['status']==200 :#line:83
                    O00O000O0OO00OO0O =O000O0OO000O00000 ['data']['nickname']#line:84
                    OO000O00O000OO000 =O000O0OO000O00000 ['data']['inner_id']#line:85
                    O00OOOOO00O000000 =O000O0OO000O00000 ['data']['assets']['gold']#line:86
                    O0000O0OO0OOOO000 =O000O0OO000O00000 ['data']['level']#line:87
                    print (f'【账号信息】:昵称:{O00O000O0OO00OO0O}丨ID:{str(OO000O00O000OO000)[:3] + "**" + str(OO000O00O000OO000)[5:]}丨等级:{O0000O0OO0OOOO000}丨种子:{str(O00OOOOO00O000000).split(".")[0]}')#line:89
                if O000O0OO000O00000 ['status']==401 :#line:90
                    return False #line:91
                if O000O0OO000O00000 ['status']==500 :#line:92
                    return False #line:93
            return True #line:94
        except Exception as OO00OO0OOOO00000O :#line:95
            print (OO00OO0OOOO00000O )#line:96
    def game_map (O00O0O0OO00000OO0 ):#line:99
        OO0000O0O0OOOO0O0 =f'__{timi_new()}'#line:100
        O0O0O00OO000O00O0 ={'authorization':O00O0O0OO00000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O0O0OOOO0O0 ),'signstring':OO0000O0O0OOOO0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:109
        O0000OOOO0OO0OOOO =requests .request ('get',f'{host}/game/map',headers =O0O0O00OO000O00O0 ).json ()#line:110
        if 'status'in O0000OOOO0OO0OOOO :#line:112
            if O0000OOOO0OO0OOOO ['status']==200 :#line:113
                for OOOOOO0O000O00O00 in O0000OOOO0OO0OOOO ['data']['list'][0 ]['crops']:#line:114
                    OOO0000000OO00O0O =OOOOOO0O000O00O00 ['level']#line:116
                    if OOO0000000OO00O0O ==41 :#line:117
                        O000O0000O0000OO0 =OOOOOO0O000O00O00 ['crop_name']#line:118
                        O0000OOOOOOO000O0 =OOOOOO0O000O00O00 ['count']#line:119
                        if O0000OOOOOOO000O0 >0 :#line:120
                            print (f'【农业资产】:{O000O0000O0000OO0}丨数量:{O0000OOOOOOO000O0}')#line:121
    def give_gold (O000OOO0OO0O0OOOO ):#line:124
        O0O0OO00O0OO00OOO =f'__{timi_new()}'#line:125
        O000O0000OOO00OOO ={'authorization':O000OOO0OO0O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00O0OO00OOO ),'signstring':O0O0OO00O0OO00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:134
        O0000O0000OOO0O0O =requests .request ('get',f'{host}/user',headers =O000O0000OOO00OOO ).json ()#line:135
        if 'status'in O0000O0000OOO0O0O :#line:136
            if O0000O0000OOO0O0O ['status']==200 :#line:137
                if float (O000OOO0OO0O0OOOO .doneeNo )!=0 :#line:138
                    OO00O0OO0O00OOOOO =O0000O0000OOO0O0O ['data']['assets']['gold']#line:139
                    if float (OO00O0OO0O00OOOOO )>2 :#line:140
                        O00O00OOOO0OOOOOO =int (float (OO00O0OO0O00OOOOO )/1.1 )#line:141
                        O0O0OO00O0OO00OOO =f'_doneeNo={O000OOO0OO0O0OOOO.doneeNo}&quantity={O00O00OOOO0OOOOOO}_{timi_new()}'#line:142
                        O000O0000OOO00OOO ={'authorization':O000OOO0OO0O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00O0OO00OOO ),'signstring':O0O0OO00O0OO00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:151
                        O0OOOO0000O0OOO0O ={"quantity":O00O00OOOO0OOOOOO ,"doneeNo":O000OOO0OO0O0OOOO .doneeNo }#line:155
                        OOOOO0O0O000OO0OO =requests .request ('post',f'{host}/finance/give-gold',headers =O000O0000OOO00OOO ,data =O0OOOO0000O0OOO0O ).json ()#line:156
                        if 'status'in OOOOO0O0O000OO0OO :#line:158
                            if OOOOO0O0O000OO0OO ['status']==200 :#line:159
                                if OOOOO0O0O000OO0OO ['data']:#line:160
                                    print (f'【赠送种子】:赠送{O00O00OOOO0OOOOOO}种子给{O000OOO0OO0O0OOOO.doneeNo}成功')#line:161
                else :#line:162
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:163
    def winning_rewards (O000OO000OOOO00OO ):#line:166
        OOOO000000OO0OO00 =f'__{timi_new()}'#line:167
        OOOOOO0O0O000000O ={'authorization':O000OO000OOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000000OO0OO00 ),'signstring':OOOO000000OO0OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:176
        O0OO0OO00OOO0OO00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOOOOO0O0O000000O ).json ()#line:177
        if 'status'in O0OO0OO00OOO0OO00 :#line:179
            if O0OO0OO00OOO0OO00 ['status']==200 :#line:180
                if O0OO0OO00OOO0OO00 ['data']['amount']:#line:181
                    O00OO00O0OOO00OOO =O0OO0OO00OOO0OO00 ['data']['amount']['gold']#line:182
                    return O00OO00O0OOO00OOO #line:183
                else :#line:184
                    return 0 #line:185
    def certification (OOOO0OOO00O0O000O ):#line:188
        O0O00O0OOOOOOOOOO =f'__{timi_new()}'#line:189
        O00OO0000OOO0OO0O ={'authorization':OOOO0OOO00O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OOOOOOOOOO ),'signstring':O0O00O0OOOOOOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:198
        O00O0O0O0O00O0OO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OO0000OOO0OO0O ).json ()#line:199
        if 'status'in O00O0O0O0O00O0OO0 :#line:201
            if O00O0O0O0O00O0OO0 ['status']==200 :#line:202
                if O00O0O0O0O00O0OO0 ['data']['result']:#line:203
                    OO000000OO0OO0O00 =O00O0O0O0O00O0OO0 ['data']['nick_name']#line:204
                    return OO000000OO0OO0O00 #line:205
                else :#line:206
                    return '未实名'#line:207
    def crops_illustrated (O00OOOO000O0O00OO ):#line:210
        O000O0OO0O000000O =f'__{timi_new()}'#line:211
        OOOOOO00O00OO0000 ={'authorization':O00OOOO000O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO0O000000O ),'signstring':O000O0OO0O000000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:220
        OOOO0O0OO0OOO0000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOOOOO00O00OO0000 ).json ()#line:221
        if 'status'in OOOO0O0OO0OOO0000 :#line:223
            if OOOO0O0OO0OOO0000 ['status']==200 :#line:224
                OO00O0OOO0000O000 =OOOO0O0OO0OOO0000 ['data'][0 ]['crops']#line:225
                for OOO00O000O00O000O in OO00O0OOO0000O000 :#line:226
                    if OOO00O000O00O000O ['ill_clover_award']:#line:227
                        if float (OOO00O000O00O000O ['ill_clover_award'])>1 :#line:228
                            if OOO00O000O00O000O ['is_finish']:#line:229
                                if not OOO00O000O00O000O ['is_getit']:#line:230
                                    O000O0OO0O000000O =f'_award_level={OOO00O000O00O000O["level"]}_{timi_new()}'#line:231
                                    OOOOOO00O00OO0000 ={'authorization':O00OOOO000O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO0O000000O ),'signstring':O000O0OO0O000000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:240
                                    O0OOOOO0000OO0000 ={"award_level":OOO00O000O00O000O ['level']}#line:241
                                    O0O0000O000OOOO0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOOOOO00O00OO0000 ,json =O0OOOOO0000OO0000 ).json ()#line:243
                                    if 'status'in O0O0000O000OOOO0O :#line:244
                                        if O0O0000O000OOOO0O ['status']==200 :#line:245
                                            O0O000OOO0O0OOO0O =O0O0000O000OOOO0O ['data']['ill_clover_award']#line:246
                                            print (f'【图鉴奖励】:领取{OOO00O000O00O000O["crop_name"]}成就丨奖励{O0O000OOO0O0OOO0O}叶子成功')#line:248
                                        if O0O0000O000OOOO0O ['status']==500 :#line:249
                                            print (f'【图鉴奖励】:{O0O0000O000OOOO0O["message"]}')#line:250
    def watched_ad (O00000OO0OOOOOO00 ):#line:253
        OO000OO0OO00000OO =f'__{timi_new()}'#line:254
        OOOO0O00OO0OO00O0 ={'authorization':O00000OO0OOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0OO00000OO ),'signstring':OO000OO0OO00000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:263
        O00OO00O0OO00O00O =requests .request ('post',f'{host}/game/watched-ad',headers =OOOO0O00OO0OO00O0 ).json ()#line:264
        print (O00OO00O0OO00O00O )#line:265
    def user_ad (OO0OOOO00O00O0O0O ):#line:268
        O0000OO0O0000OO00 =f'__{timi_new()}'#line:269
        OOOO000O000OOOOOO ={'authorization':OO0OOOO00O00O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO0O0000OO00 ),'signstring':O0000OO0O0000OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
        OO00O0O0O0O0O000O =requests .request ('get',f'{host}/user/ad',headers =OOOO000O000OOOOOO ).json ()#line:279
        if 'status'in OO00O0O0O0O0O000O :#line:281
            if OO00O0O0O0O0O000O ['status']==200 :#line:282
                O00000OOO0OOO0O0O =OO00O0O0O0O0O000O ['data']['max_time']#line:283
                O0OO0O00OOO00O00O =OO00O0O0O0O0O000O ['data']['watch_time']#line:284
                OO0OOOOO0O00O0000 =OO00O0O0O0O0O000O ['data']['added_time']#line:285
                print (f'【获取种子】:获取种子剩余{OO0OOOOO0O00O0000 + O00000OOO0OOO0O0O - O0OO0O00OOO00O00O}次丨好友提供:{OO0OOOOO0O00O0000}次')#line:286
                if OO0OOOOO0O00O0000 +O00000OOO0OOO0O0O -O0OO0O00OOO00O00O >0 :#line:287
                    time .sleep (random .randint (16 ,19 ))#line:288
                    O0000OOO0O0OOOOOO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOOO000O000OOOOOO ).json ()#line:289
                    if 'status'in O0000OOO0O0OOOOOO :#line:291
                        if O0000OOO0O0OOOOOO ['status']==200 :#line:292
                            OOO0O0OO0OOO00O0O =O0000OOO0O0OOOOOO ['data']['silver']#line:293
                            print (f'【获取种子】:获得种子:{OOO0O0OO0OOO00O0O}')#line:294
                            return True #line:295
                        if O0000OOO0O0OOOOOO ['status']==500 :#line:296
                            O0000O00000O0O0O0 =O0000OOO0O0OOOOOO ['message']#line:297
                            print (f'【获取种子】:{O0000O00000O0O0O0}')#line:298
                            return False #line:299
    def synthetic (O0OOO0OOO0O00000O ):#line:302
        global id ,g #line:303
        try :#line:304
            OO0O0OOOOOOOOOOO0 =O0OOO0OOO0O00000O .level_new ()#line:305
            while True :#line:306
                O000OO000O00OO0OO =f'__{timi_new()}'#line:307
                O0O00OO0OOOOOO000 ={'authorization':O0OOO0OOO0O00000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO000O00OO0OO ),'signstring':O000OO000O00OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:316
                OO00O00OOO000OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O00OO0OOOOOO000 ).json ()#line:317
                if 'status'in OO00O00OOO000OOO0 :#line:319
                    if OO00O00OOO000OOO0 ['status']==200 :#line:320
                        O0O0O0OO0OO00OOO0 =OO00O00OOO000OOO0 ['data']['cropList']#line:321
                        O000O00OO00OOOOO0 =OO00O00OOO000OOO0 ['data']['gameCoreDataDBid']#line:322
                        OO00O00000000OO0O =0 #line:323
                        for OOOO00OOOO0O0O00O in O0O0O0OO0OO00OOO0 :#line:324
                            if not OOOO00OOOO0O0O00O :#line:325
                                OOO0O00O0OO00O00O =f'_crop_id={O000O00OO00OOOOO0}&site={OO00O00000000OO0O}_{O0OOO0OOO0O00000O.time}'#line:326
                                OOO000O00OOO0O000 ={'authorization':O0OOO0OOO0O00000O .token ,'timestamp':O0OOO0OOO0O00000O .time ,'sign':sign (OOO0O00O0OO00O00O ),'signstring':OOO0O00O0OO00O00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:335
                                OOOOO0OO000000OOO ={"site":OO00O00000000OO0O ,"crop_id":O000O00OO00OOOOO0 }#line:336
                                O00000OOOOO0O0O00 =requests .request ('post',f'{host}/game/crops/buy',headers =OOO000O00OOO0O000 ,data =OOOOO0OO000000OOO ).json ()#line:337
                                time .sleep (random .randint (1 ,3 )/10 )#line:339
                                if 'status'in O00000OOOOO0O0O00 :#line:340
                                    if O00000OOOOO0O0O00 ['status']==200 :#line:341
                                        if O00000OOOOO0O0O00 ['message']=='种子数量不足':#line:342
                                            OO0O0OOOOOOOOOOO0 =O0OOO0OOO0O00000O .level_new ()#line:343
                                            print (f'【种植合成】:{O00000OOOOO0O0O00["message"]}')#line:344
                                            if not O0OOO0OOO0O00000O .user_ad ():#line:345
                                                return False #line:346
                                        print (f'【种植合成】:种植农作物,位置{OO00O00000000OO0O}')#line:347
                                    if O00000OOOOO0O0O00 ['status']==500 :#line:348
                                        print (f'【种植合成】:{O00000OOOOO0O0O00["message"]}')#line:349
                                        return False #line:350
                            OO00O00000000OO0O +=1 #line:351
                        OO000OO00O0000OOO =requests .request ('get',f'{host}/game/getAllData',headers =O0O00OO0OOOOOO000 ).json ()#line:352
                        OO00OO000OO0O0O0O =OO000OO00O0000OOO ['data']['cropList']#line:353
                        O0O000O0OOO00O0O0 =False #line:354
                        for OOOO00OOOO0O0O00O in range (12 ):#line:355
                            id =OO00OO000OO0O0O0O [OOOO00OOOO0O0O00O ]['level']#line:356
                            if float (OO0O0OOOOOOOOOOO0 )-float (id )>9 :#line:357
                                O0O0OO0OOO0O00OO0 =f'_site={OOOO00OOOO0O0O00O}_{timi_new()}'#line:358
                                OO0OOO0O00OO0OO0O ={'accept':'application/json, text/plain, */*','authorization':O0OOO0OOO0O00000O .token ,'timestamp':timi_new (),'sign':sign (O0O0OO0OOO0O00OO0 ),'signstring':O0O0OO0OOO0O00OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:368
                                OO0O0O0OO0OO00O00 ={"site":OOOO00OOOO0O0O00O }#line:369
                                O0O0O0O0O000OOO00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0OOO0O00OO0OO0O ,data =OO0O0O0OO0OO00O00 ).json ()#line:371
                                if 'status'in O0O0O0O0O000OOO00 :#line:372
                                    if O0O0O0O0O000OOO00 ['status']==200 :#line:373
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:374
                            if id !=0 :#line:375
                                for OO0O00OO0000O00OO in range (11 ):#line:376
                                    O0OOOO00OOOO000OO =OO0O00OO0000O00OO +1 #line:377
                                    g =OO00OO000OO0O0O0O [O0OOOO00OOOO000OO ]['level']#line:378
                                    if id ==g :#line:379
                                        O0O0O0OO0O0OOOOO0 =OO0O00OO0000O00OO +2 #line:380
                                        if O0O0O0OO0O0OOOOO0 ==OOOO00OOOO0O0O00O +1 :#line:381
                                            pass #line:382
                                        else :#line:383
                                            OOOO0000O0OOO0O0O =OOOO00OOOO0O0O00O +1 #line:384
                                            time .sleep (random .randint (1 ,3 )/10 )#line:386
                                            O0OO0O00O0OO0OO0O =f'_site={OOOO0000O0OOO0O0O - 1}&targetSite={O0O0O0OO0O0OOOOO0 - 1}_{timi_new()}'#line:387
                                            O00000000000OOO0O ={'accept':'application/json, text/plain, */*','authorization':O0OOO0OOO0O00000O .token ,'timestamp':timi_new (),'sign':sign (O0OO0O00O0OO0OO0O ),'signstring':O0OO0O00O0OO0OO0O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:402
                                            O0O000O0OO0000O00 ={"site":int (OOOO0000O0OOO0O0O -1 ),"targetSite":int (O0O0O0OO0O0OOOOO0 -1 )}#line:403
                                            OO00000O0O00O00OO =requests .request ('post',f'{host}/game/crops/move',headers =O00000000000OOO0O ,json =O0O000O0OO0000O00 ).json ()#line:405
                                            if 'status'in OO00000O0O00O00OO :#line:406
                                                if OO00000O0O00O00OO ['status']==200 :#line:407
                                                    pass #line:408
                                            print ('【种植合成】:',OOOO0000O0OOO0O0O ,O0O0O0OO0O0OOOOO0 ,'合成成功')#line:410
                                            O0O000O0OOO00O0O0 =True #line:411
                                    if O0O000O0OOO00O0O0 :#line:412
                                        break #line:413
                                if O0O000O0OOO00O0O0 :#line:414
                                    break #line:415
        except Exception as O0OO000O00O00O0OO :#line:416
            O0OOO0OOO0O00000O .synthetic ()#line:417
    def level_new (OO0000O0OOO000OO0 ):#line:420
        try :#line:421
            O0O00000O000O0O0O =f'__{timi_new()}'#line:422
            OOO00OO00O0OOOOOO ={'authorization':OO0000O0OOO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000O000O0O0O ),'signstring':O0O00000O000O0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:431
            OO0OOO0OOOOOOO00O =requests .request ('get',f'{host}/user',headers =OOO00OO00O0OOOOOO ).json ()#line:432
            if 'status'in OO0OOO0OOOOOOO00O :#line:433
                if OO0OOO0OOOOOOO00O ['status']==200 :#line:434
                    return float (OO0OOO0OOOOOOO00O ['data']['level'])#line:435
        except Exception as O0000OO00O0000OO0 :#line:436
            print (O0000OO00O0000OO0 )#line:437
    def propsraffle (OOOOO0OO0O0O00O0O ):#line:440
        try :#line:441
            while True :#line:442
                O000OOO0000O000O0 =f'__{timi_new()}'#line:443
                OO0O00O000OO0OO0O ={'authorization':OOOOO0OO0O0O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0000O000O0 ),'signstring':O000OOO0000O000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:452
                OOOOOO000000OOOOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0O00O000OO0OO0O ).json ()#line:453
                if 'status'in OOOOOO000000OOOOO :#line:455
                    if OOOOOO000000OOOOO ['status']==200 :#line:456
                        OO0OO000000OO0O0O =OOOOOO000000OOOOO ['data']['rows']#line:457
                        OO000O00OO0O00000 =OOOOOO000000OOOOO ['data']['vstate']#line:458
                        if OO0OO000000OO0O0O ==5 or OO0OO000000OO0O0O ==6 or OO0OO000000OO0O0O ==7 :#line:459
                            O0O00OOOO00OOO000 =OOOOOO000000OOOOO ['data']['silver']#line:460
                            print (f'【转盘抽奖】:获得种子:{O0O00OOOO00OOO000}')#line:461
                        if OO0OO000000OO0O0O ==1 or OO0OO000000OO0O0O ==2 or OO0OO000000OO0O0O ==3 :#line:462
                            OOOO0000O00OO0OOO =OOOOOO000000OOOOO ['data']['clover']#line:463
                            print (f'【转盘抽奖】:获得三叶草:{OOOO0000O00OO0OOO}')#line:464
                        if OO0OO000000OO0O0O ==4 or OO0OO000000OO0O0O ==8 :#line:465
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:466
                        if OO0OO000000OO0O0O =='抽奖次数已用完':#line:470
                            if OO000O00OO0O00000 :#line:471
                                O000O00O0O0O0O00O =random .randint (160 ,190 )/10 #line:472
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{O000O00O0O0O0O00O}秒获取抽奖机会')#line:473
                                time .sleep (O000O00O0O0O0O00O )#line:474
                                OO0OO0O0OOO00OOO0 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OO0O00O000OO0OO0O ).json ()#line:476
                                if 'status'in OO0OO0O0OOO00OOO0 :#line:478
                                    if OO0OO0O0OOO00OOO0 ['status']==200 :#line:479
                                        print (f'【转盘抽奖】:{OO0OO0O0OOO00OOO0["message"]}')#line:480
                                    if OO0OO0O0OOO00OOO0 ['status']==500 :#line:481
                                        print (f'【转盘抽奖】:{OO0OO0O0OOO00OOO0["message"]}')#line:482
                                        break #line:483
                                time .sleep (random .randint (10 ,15 )/10 )#line:484
                            else :#line:485
                                break #line:486
                time .sleep (random .randint (8 ,15 )/10 )#line:487
        except Exception as O0O0O0OO0O0O000OO :#line:488
            print (O0O0O0OO0O0O000OO )#line:489
    def friends_invitation (O000OO0O0O0OOOO00 ):#line:492
        try :#line:493
            O000000O0OO00O00O =f'__{timi_new()}'#line:494
            OO0O0O0OOOOOOO0OO ={'authorization':O000OO0O0O0OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O0OO00O00O ),'signstring':O000000O0OO00O00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:503
            O000O00O0OO0O0O0O =requests .request ('get',f'{host}/friends',headers =OO0O0O0OOOOOOO0OO ).json ()#line:504
            if 'status'in O000O00O0OO0O0O0O :#line:505
                if O000O00O0OO0O0O0O ['status']==200 :#line:506
                    OO00O000OO000O000 =O000O00O0OO0O0O0O ['data']['myInviteter']#line:507
                    if OO00O000OO000O000 :#line:508
                        OO0O0OO00O00O0OO0 =OO00O000OO000O000 ['user']['nickname']#line:509
                        OO0OO000OOO00OOOO =O000OO0O0O0OOOO00 .certification ()#line:510
                        print (f'【绑邀请码】:我的邀请人:{OO0O0OO00O00O0OO0}丨实名:{OO0OO000OOO00OOOO}')#line:511
                    else :#line:512
                        if O000OO0O0O0OOOO00 .innerId !='0':#line:513
                            O000000O0OO00O00O =f'_innerId={O000OO0O0O0OOOO00.innerId}_{timi_new()}'#line:514
                            OO0O0O0OOOOOOO0OO ={'authorization':O000OO0O0O0OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O0OO00O00O ),'signstring':O000000O0OO00O00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:523
                            O0O00O0O00OOOO000 ={"innerId":O000OO0O0O0OOOO00 .innerId }#line:524
                            OO00O0OOO0000O00O =requests .request ('post',f'{host}/friends/my-invitation',headers =OO0O0O0OOOOOOO0OO ,data =O0O00O0O00OOOO000 ).json ()#line:526
                            if 'status'in OO00O0OOO0000O00O :#line:527
                                if OO00O0OOO0000O00O ['status']==200 :#line:528
                                    print (f'【绑邀请码】:{O000OO0O0O0OOOO00.innerId}{OO00O0OOO0000O00O["message"]}')#line:529
                        else :#line:530
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:531
        except Exception as OO0OO0O0000O0OO00 :#line:532
            print (OO0OO0O0000O0OO00 )#line:533
    def add_clover (OOO00OO0OO0000O0O ):#line:536
        try :#line:537
            O000000000OOO0OOO =f'__{timi_new()}'#line:538
            OO00OOOO00OO0OO00 ={'authorization':OOO00OO0OO0000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000000000OOO0OOO ),'signstring':O000000000OOO0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:547
            O0OOOO00O000O0O0O =requests .request ('get',f'{host}/assets/clovers',headers =OO00OOOO00OO0OO00 ).json ()#line:548
            if 'status'in O0OOOO00O000O0O0O :#line:550
                if O0OOOO00O000O0O0O ['status']==200 :#line:551
                    OOOO000OO0O0O000O =O0OOOO00O000O0O0O ['data']['clover']#line:552
                    OOO0O00OO00O000O0 =O0OOOO00O000O0O0O ['data']['used_clover']#line:553
                    O000O0OOOO00OOOO0 =float (OOOO000OO0O0O000O )-float (OOO0O00OO00O000O0 )#line:554
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OOO0O00OO00O000O0}')#line:555
                    if O000O0OOOO00OOOO0 >1 :#line:556
                        O000000000OOO0OOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O000O0OOOO00OOOO0)}_{timi_new()}'#line:557
                        OO00OOOO00OO0OO00 ={'authorization':OOO00OO0OO0000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000000000OOO0OOO ),'signstring':O000000000OOO0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:566
                        OO000OOOO000OO0OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O000O0OOOO00OOOO0 )}#line:567
                        O00O00O0OO0O0O0O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO00OOOO00OO0OO00 ,data =OO000OOOO000OO0OO ).json ()#line:568
                        if 'status'in O00O00O0OO0O0O0O0 :#line:570
                            if O00O00O0OO0O0O0O0 ['status']==200 :#line:571
                                print (f'【参与抽奖】:添加三叶草:{O00O00O0OO0O0O0O0["data"]}丨数量:{O000O0OOOO00OOOO0}')#line:572
            O0O0OOO0O0OOOO00O =requests .request ('get',f'{host}/lottery',headers =OO00OOOO00OO0OO00 ).json ()#line:573
            OO0OOO00OOO0O0000 =OOO00OO0OO0000O0O .winning_rewards ()#line:575
            if 'status'in O0O0OOO0O0OOOO00O :#line:576
                if O0O0OOO0O0OOOO00O ['status']==200 :#line:577
                    O00O000O0O0000O0O =O0O0OOO0O0OOOO00O ['data'][0 ]['day_get_gold_quantity']#line:578
                    print (f'【参与抽奖】:预计每天中{O00O000O0O0000O0O[:6]}种子丨好友收益:{OO0OOO00OOO0O0000}')#line:579
        except Exception as O0OOO000OO0O0OO0O :#line:580
            print (O0OOO000OO0O0OO0O )#line:581
    def energy (O0O0000OOO0OO0OO0 ):#line:584
        O00O0O0OO0O0O000O =f'__{timi_new()}'#line:585
        OOOO00O000000O00O ={'authorization':O0O0000OOO0OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0OO0O0O000O ),'signstring':O00O0O0OO0O0O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:594
        O0OO00O00OOOO0000 =requests .request ('get',f'{host}/energy/general',headers =OOOO00O000000O00O ).json ()#line:595
        if 'status'in O0OO00O00OOOO0000 :#line:597
            if O0OO00O00OOOO0000 ['status']==200 :#line:598
                OO0OO0OOO000O0000 =O0OO00O00OOOO0000 ['data']['ordinary_water_consumptions']#line:599
                if float (OO0OO0OOO000O0000 )<80 :#line:600
                    OOO00OOO0O0OOOO00 =99 -float (OO0OO0OOO000O0000 )#line:601
                    OO00O0O000O0O0OO0 ={"fertilizer":str (OOO00OOO0O0OOOO00 ).split ('.')[0 ]}#line:602
                    O000OO0OOOO00O0O0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOO00O000000O00O ,data =OO00O0O000O0O0OO0 ).json ()#line:604
                    if 'status'in O000OO0OOOO00O0O0 :#line:606
                        if O000OO0OOOO00O0O0 ['status']==200 :#line:607
                            print (f'【购买肥料】:{O000OO0OOOO00O0O0["message"]}')#line:608
                OOOOO0OO0000OOO0O =O0OO00O00OOOO0000 ['data']['ordinary_water_consumptions']#line:609
                if float (OOOOO0OO0000OOO0O )<800 :#line:610
                    O0O000OO0O0O00O00 =999 -float (OOOOO0OO0000OOO0O )#line:611
                    OO000000OO0O0O000 ={"water":str (O0O000OO0O0O00O00 ).split ('.')[0 ]}#line:612
                    O0OOO0O000O00000O =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOO00O000000O00O ,data =OO000000OO0O0O000 ).json ()#line:613
                    if 'status'in O0OOO0O000O00000O :#line:614
                        if O0OOO0O000O00000O ['status']==200 :#line:615
                            print (f'【购买水滴】:{O0OOO0O000O00000O["message"]}')#line:616
def version_of_the_validation ():#line:620
    return str ((66 -56 )/10 )#line:621
def gitee_validation ():#line:624
    try :#line:625
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:626
    except Exception as O000OO0OO0O00O000 :#line:627
        sys .exit (0 )#line:628
def update_the_validation ():#line:632
    try :#line:633
        OOO0OO00O0OO0O0O0 =gitee_validation ()#line:634
        if version_of_the_validation ()<OOO0OO00O0OO0O0O0 ['CityEarth']['edition']:#line:635
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OO00O0OO0O0O0["CityEarth"]["edition"]}   ❌')#line:636
            print (f'更新内容=>>{OOO0OO00O0OO0O0O0["CityEarth"]["content"]}   👍')#line:637
        else :#line:638
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OO00O0OO0O0O0["CityEarth"]["edition"]}   ✅')#line:639
            print (f'更新内容=>> {OOO0OO00O0OO0O0O0["CityEarth"]["content"]}   👍')#line:640
    except Exception as OO0OO0OOO00OO000O :#line:641
        print (OO0OO0OOO00OO000O )#line:642
def os_qinglong ():#line:645
    if application in os .environ :#line:646
        OOO0OO0000OO000O0 =os .environ [application ].split ('\n')#line:647
        if len (OOO0OO0000OO000O0 )>0 :#line:648
            return OOO0OO0000OO000O0 #line:649
        else :#line:650
            print (f"{application}变量未启用")#line:651
            print ('脚本退出')#line:652
            sys .exit (1 )#line:653
    else :#line:654
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:656
        return os_built ()#line:657
def os_built ():#line:660
    if token :#line:661
        O00O0O00OO0OO0OO0 =token .split ('\n')#line:662
        if len (O00O0O00OO0OO0OO0 )>0 :#line:663
            return O00O0O00OO0OO0OO0 #line:664
    else :#line:665
        print (f"内置变量为空")#line:666
        print ('脚本结束')#line:667
        sys .exit (0 )#line:668
if __name__ =='__main__':#line:671
    start ()#line:672
