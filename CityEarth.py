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

time_xx = random.randint(25, 45)  # 秒 执行下一个号的时间  2到4秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://scsc.sc19319.com'#line:2
def start ():#line:5
    try :#line:6
        update_the_validation ()#line:7
        OOOOOO0OOO0O0OOO0 =os_qinglong ()#line:8
        print (f"==========共找到{len(OOOOOO0OOO0O0OOO0)}个账号==========")#line:9
        for OOOO00O00OO00OO0O in OOOOOO0OOO0O0OOO0 :#line:10
            print (f"------------正在执行第{OOOOOO0OOO0O0OOO0.index(OOOO00O00OO00OO0O) + 1}个账号------------")#line:11
            O0OOOOO0O00O00000 =CityEarth (OOOO00O00OO00OO0O )#line:12
            def OO0O00OOOOOOOOO0O ():#line:14
                if O0OOOOO0O00O00000 .base_info ():#line:16
                    O0OOOOO0O00O00000 .game_map ()#line:20
                    O0OOOOO0O00O00000 .friends_invitation ()#line:22
                    O0OOOOO0O00O00000 .add_clover ()#line:24
                    O0OOOOO0O00O00000 .energy ()#line:26
                    O0OOOOO0O00O00000 .synthetic ()#line:28
                    O0OOOOO0O00O00000 .propsraffle ()#line:30
                    O0OOOOO0O00O00000 .crops_illustrated ()#line:32
                    O0OOOOO0O00O00000 .give_gold ()#line:34
                else :#line:35
                    print ('token失效')#line:36
            O00O00OO0O0000O0O =threading .Thread (target =OO0O00OOOOOOOOO0O )#line:38
            O00O00OO0O0000O0O .start ()#line:39
            time .sleep (time_xx )#line:40
    except Exception as OOO0OO00OO0OOO0OO :#line:41
        print (OOO0OO00OO0OOO0OO )#line:42
def sign (OOO000OOOOOO000OO ):#line:45
    O000O0OOO0OO00000 =hashlib .md5 (OOO000OOOOOO000OO .encode ()).hexdigest ()#line:46
    O0000OO00OO0O0OOO ="scsc%^&*"+O000O0OOO0OO00000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:47
    O00OOOO0OO0O00000 =hashlib .md5 (O0000OO00OO0O0OOO .encode ()).hexdigest ()#line:48
    return O00OOOO0OO0O00000 #line:49
def timi_new ():#line:52
    return str (int (time .time ()*1000 ))#line:53
class CityEarth :#line:56
    def __init__ (O00O00000000OOOO0 ,OOO00OOO0O00OO00O ):#line:58
        try :#line:59
            O00O00000000OOOO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:60
            O00O00000000OOOO0 .token =OOO00OOO0O00OO00O .split ('&')[0 ]#line:61
            O00O00000000OOOO0 .innerId =OOO00OOO0O00OO00O .split ('&')[1 ]#line:62
            O00O00000000OOOO0 .doneeNo =OOO00OOO0O00OO00O .split ('&')[2 ]#line:63
        except :#line:64
            print ('变量格式错误')#line:65
    def base_info (OOOO0O000O0O0O00O ):#line:68
        try :#line:69
            OO0O00O000OO000OO =f'__{timi_new()}'#line:70
            O000000O0O00OOO00 ={'authorization':OOOO0O000O0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O000OO000OO ),'signstring':OO0O00O000OO000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:79
            OOOO0000O0OOO0OOO =requests .request ('get',f'{host}/user',headers =O000000O0O00OOO00 ).json ()#line:80
            if 'status'in OOOO0000O0OOO0OOO :#line:82
                if OOOO0000O0OOO0OOO ['status']==200 :#line:83
                    OO000OOO00000OOOO =OOOO0000O0OOO0OOO ['data']['nickname']#line:84
                    O0OOO00000000O0OO =OOOO0000O0OOO0OOO ['data']['inner_id']#line:85
                    OOO00OO00OO000OO0 =OOOO0000O0OOO0OOO ['data']['assets']['gold']#line:86
                    OO0OOOO00OOO000OO =OOOO0000O0OOO0OOO ['data']['level']#line:87
                    print (f'【账号信息】:昵称:{OO000OOO00000OOOO}丨ID:{str(O0OOO00000000O0OO)[:3] + "**" + str(O0OOO00000000O0OO)[5:]}丨等级:{OO0OOOO00OOO000OO}丨种子:{str(OOO00OO00OO000OO0).split(".")[0]}')#line:89
                if OOOO0000O0OOO0OOO ['status']==401 :#line:90
                    return False #line:91
                if OOOO0000O0OOO0OOO ['status']==500 :#line:92
                    return False #line:93
            return True #line:94
        except Exception as OOOO0OO000OOOOOO0 :#line:95
            print (OOOO0OO000OOOOOO0 )#line:96
    def game_map (OO00O000O00OOOO00 ):#line:99
        O0OOOOO000OOO000O =f'__{timi_new()}'#line:100
        OO000OO0OO00O000O ={'authorization':OO00O000O00OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO000OOO000O ),'signstring':O0OOOOO000OOO000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:109
        O0OO000O00000OOO0 =requests .request ('get',f'{host}/game/map',headers =OO000OO0OO00O000O ).json ()#line:110
        if 'status'in O0OO000O00000OOO0 :#line:112
            if O0OO000O00000OOO0 ['status']==200 :#line:113
                for OOOOO0O0OO000O00O in O0OO000O00000OOO0 ['data']['list'][0 ]['crops']:#line:114
                    OO0000OO0O00OO0O0 =OOOOO0O0OO000O00O ['level']#line:116
                    if OO0000OO0O00OO0O0 ==41 :#line:117
                        O00O0OOO00000O0OO =OOOOO0O0OO000O00O ['crop_name']#line:118
                        OOOO000OOO0OOO0O0 =OOOOO0O0OO000O00O ['count']#line:119
                        if OOOO000OOO0OOO0O0 >0 :#line:120
                            print (f'【农业资产】:{O00O0OOO00000O0OO}丨数量:{OOOO000OOO0OOO0O0}')#line:121
    def give_gold (OO0OOO0OO0O0O0OOO ):#line:124
        O00OO00O00O000O0O =f'__{timi_new()}'#line:125
        O0O0OO00O0O00O0OO ={'authorization':OO0OOO0OO0O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00O00O000O0O ),'signstring':O00OO00O00O000O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:134
        O00OOO0O0OO000000 =requests .request ('get',f'{host}/user',headers =O0O0OO00O0O00O0OO ).json ()#line:135
        if 'status'in O00OOO0O0OO000000 :#line:136
            if O00OOO0O0OO000000 ['status']==200 :#line:137
                if float (OO0OOO0OO0O0O0OOO .doneeNo )!=0 :#line:138
                    OO000OO00OO0O0000 =O00OOO0O0OO000000 ['data']['assets']['gold']#line:139
                    if float (OO000OO00OO0O0000 )>2 :#line:140
                        OO0000OOOOO00O00O =int (float (OO000OO00OO0O0000 )/1.1 )#line:141
                        O00OO00O00O000O0O =f'_doneeNo={OO0OOO0OO0O0O0OOO.doneeNo}&quantity={OO0000OOOOO00O00O}_{timi_new()}'#line:142
                        O0O0OO00O0O00O0OO ={'authorization':OO0OOO0OO0O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00O00O000O0O ),'signstring':O00OO00O00O000O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:151
                        OOO0OO0O0000O0OO0 ={"quantity":OO0000OOOOO00O00O ,"doneeNo":OO0OOO0OO0O0O0OOO .doneeNo }#line:155
                        O0OOOOO00OO00OO00 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0OO00O0O00O0OO ,data =OOO0OO0O0000O0OO0 ).json ()#line:156
                        if 'status'in O0OOOOO00OO00OO00 :#line:158
                            if O0OOOOO00OO00OO00 ['status']==200 :#line:159
                                if O0OOOOO00OO00OO00 ['data']:#line:160
                                    print (f'【赠送种子】:赠送{OO0000OOOOO00O00O}种子给{OO0OOO0OO0O0O0OOO.doneeNo}成功')#line:161
                else :#line:162
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:163
    def winning_rewards (OOO00OO0O0OO0OOOO ):#line:166
        OOO0O0OO0O00000O0 =f'__{timi_new()}'#line:167
        O00OO0000O000O0O0 ={'authorization':OOO00OO0O0OO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO0O00000O0 ),'signstring':OOO0O0OO0O00000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:176
        O0O0O00OOO00OOO0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00OO0000O000O0O0 ).json ()#line:177
        if 'status'in O0O0O00OOO00OOO0O :#line:179
            if O0O0O00OOO00OOO0O ['status']==200 :#line:180
                if O0O0O00OOO00OOO0O ['data']['amount']:#line:181
                    OO0O000O0OOO000OO =O0O0O00OOO00OOO0O ['data']['amount']['gold']#line:182
                    return OO0O000O0OOO000OO #line:183
                else :#line:184
                    return 0 #line:185
    def certification (OO00OO0OOO0O000O0 ):#line:188
        O00O00O0OO0O00O00 =f'__{timi_new()}'#line:189
        OOO00O00O0O000O00 ={'authorization':OO00OO0OOO0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0OO0O00O00 ),'signstring':O00O00O0OO0O00O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:198
        OO00OOO00O0000OO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO00O00O0O000O00 ).json ()#line:199
        if 'status'in OO00OOO00O0000OO0 :#line:201
            if OO00OOO00O0000OO0 ['status']==200 :#line:202
                if OO00OOO00O0000OO0 ['data']['result']:#line:203
                    O0O0000OO00O0000O =OO00OOO00O0000OO0 ['data']['nick_name']#line:204
                    return O0O0000OO00O0000O #line:205
                else :#line:206
                    return '未实名'#line:207
    def crops_illustrated (OOO0OOOO00000O000 ):#line:210
        OOO000OO000O00OOO =f'__{timi_new()}'#line:211
        O000O0O00O000O000 ={'authorization':OOO0OOOO00000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO000O00OOO ),'signstring':OOO000OO000O00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:220
        O0O000OOO00OO00OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =O000O0O00O000O000 ).json ()#line:221
        if 'status'in O0O000OOO00OO00OO :#line:223
            if O0O000OOO00OO00OO ['status']==200 :#line:224
                OOOOOOO0000O00OO0 =O0O000OOO00OO00OO ['data'][0 ]['crops']#line:225
                for O000O000OO00O0OOO in OOOOOOO0000O00OO0 :#line:226
                    if O000O000OO00O0OOO ['ill_clover_award']:#line:227
                        if float (O000O000OO00O0OOO ['ill_clover_award'])>1 :#line:228
                            if O000O000OO00O0OOO ['is_finish']:#line:229
                                if not O000O000OO00O0OOO ['is_getit']:#line:230
                                    OOO000OO000O00OOO =f'_award_level={O000O000OO00O0OOO["level"]}_{timi_new()}'#line:231
                                    O000O0O00O000O000 ={'authorization':OOO0OOOO00000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO000O00OOO ),'signstring':OOO000OO000O00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:240
                                    O00OOO0O0000OOOOO ={"award_level":O000O000OO00O0OOO ['level']}#line:241
                                    OOO0000O0O0O0O00O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O000O0O00O000O000 ,json =O00OOO0O0000OOOOO ).json ()#line:243
                                    if 'status'in OOO0000O0O0O0O00O :#line:244
                                        if OOO0000O0O0O0O00O ['status']==200 :#line:245
                                            O000O0OO000O0O0O0 =OOO0000O0O0O0O00O ['data']['ill_clover_award']#line:246
                                            print (f'【图鉴奖励】:领取{O000O000OO00O0OOO["crop_name"]}成就丨奖励{O000O0OO000O0O0O0}叶子成功')#line:248
                                        if OOO0000O0O0O0O00O ['status']==500 :#line:249
                                            print (f'【图鉴奖励】:{OOO0000O0O0O0O00O["message"]}')#line:250
    def watched_ad (OO0O0000O00OOO0OO ):#line:253
        O0OOO000OOOO0O000 =f'__{timi_new()}'#line:254
        OO0OOOOOOO0O0O000 ={'authorization':OO0O0000O00OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO000OOOO0O000 ),'signstring':O0OOO000OOOO0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:263
        O00OOO0OOOOO0OOO0 =requests .request ('post',f'{host}/game/watched-ad',headers =OO0OOOOOOO0O0O000 ).json ()#line:264
        print (O00OOO0OOOOO0OOO0 )#line:265
    def user_ad (OOOOOO00OO0OOO00O ):#line:268
        OOO000000O00OO0O0 =f'__{timi_new()}'#line:269
        OO0000000OOOOO00O ={'authorization':OOOOOO00OO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000000O00OO0O0 ),'signstring':OOO000000O00OO0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
        OOOO00O00O0000O00 =requests .request ('get',f'{host}/user/ad',headers =OO0000000OOOOO00O ).json ()#line:279
        if 'status'in OOOO00O00O0000O00 :#line:281
            if OOOO00O00O0000O00 ['status']==200 :#line:282
                OOOOO0OOO000O000O =OOOO00O00O0000O00 ['data']['max_time']#line:283
                OOO000O00OOOOO000 =OOOO00O00O0000O00 ['data']['watch_time']#line:284
                O0OO000000O0OOO0O =OOOO00O00O0000O00 ['data']['added_time']#line:285
                print (f'【获取种子】:获取种子剩余{O0OO000000O0OOO0O + OOOOO0OOO000O000O - OOO000O00OOOOO000}次丨好友提供:{O0OO000000O0OOO0O}次')#line:286
                if O0OO000000O0OOO0O +OOOOO0OOO000O000O -OOO000O00OOOOO000 >0 :#line:287
                    time .sleep (random .randint (16 ,19 ))#line:288
                    O0O0000000O0OO000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO0000000OOOOO00O ).json ()#line:289
                    if 'status'in O0O0000000O0OO000 :#line:291
                        if O0O0000000O0OO000 ['status']==200 :#line:292
                            OOOO00O0OO000OO00 =O0O0000000O0OO000 ['data']['silver']#line:293
                            print (f'【获取种子】:获得种子:{OOOO00O0OO000OO00}')#line:294
                            return True #line:295
                        if O0O0000000O0OO000 ['status']==500 :#line:296
                            O00OOO0OO0000OOO0 =O0O0000000O0OO000 ['message']#line:297
                            print (f'【获取种子】:{O00OOO0OO0000OOO0}')#line:298
                            return False #line:299
    def synthetic (O0OOOO0OOOO0O0O00 ):#line:302
        global id ,g #line:303
        try :#line:304
            O00OOO000OOOOOOO0 =O0OOOO0OOOO0O0O00 .level_new ()#line:305
            while True :#line:306
                OOOOO00O00000OO00 =f'__{timi_new()}'#line:307
                OO00OO0O00O00O000 ={'authorization':O0OOOO0OOOO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O00000OO00 ),'signstring':OOOOO00O00000OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:316
                OO0OO00O00OOOO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =OO00OO0O00O00O000 ).json ()#line:317
                if 'status'in OO0OO00O00OOOO0O0 :#line:319
                    if OO0OO00O00OOOO0O0 ['status']==200 :#line:320
                        OO0OO00OO00O0OOO0 =OO0OO00O00OOOO0O0 ['data']['cropList']#line:321
                        O0OOO00OOOO000OOO =OO0OO00O00OOOO0O0 ['data']['gameCoreDataDBid']#line:322
                        OO0OOO0O00000OO00 =0 #line:323
                        for O0O0O00O00OOOO0O0 in OO0OO00OO00O0OOO0 :#line:324
                            if not O0O0O00O00OOOO0O0 :#line:325
                                OO00O0O00O0O0O00O =f'_crop_id={O0OOO00OOOO000OOO}&site={OO0OOO0O00000OO00}_{O0OOOO0OOOO0O0O00.time}'#line:326
                                OO00O0OOO0O00O0O0 ={'authorization':O0OOOO0OOOO0O0O00 .token ,'timestamp':O0OOOO0OOOO0O0O00 .time ,'sign':sign (OO00O0O00O0O0O00O ),'signstring':OO00O0O00O0O0O00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:335
                                OO0O00O0O0O00OO0O ={"site":OO0OOO0O00000OO00 ,"crop_id":O0OOO00OOOO000OOO }#line:336
                                O000OO0O0OOOOOOO0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO00O0OOO0O00O0O0 ,data =OO0O00O0O0O00OO0O ).json ()#line:337
                                time .sleep (random .randint (1 ,3 )/10 )#line:339
                                if 'status'in O000OO0O0OOOOOOO0 :#line:340
                                    if O000OO0O0OOOOOOO0 ['status']==200 :#line:341
                                        if O000OO0O0OOOOOOO0 ['message']=='种子数量不足':#line:342
                                            O00OOO000OOOOOOO0 =O0OOOO0OOOO0O0O00 .level_new ()#line:343
                                            print (f'【种植合成】:{O000OO0O0OOOOOOO0["message"]}')#line:344
                                            if not O0OOOO0OOOO0O0O00 .user_ad ():#line:345
                                                return False #line:346
                                        print (f'【种植合成】:种植农作物,位置{OO0OOO0O00000OO00}')#line:347
                                    if O000OO0O0OOOOOOO0 ['status']==500 :#line:348
                                        print (f'【种植合成】:{O000OO0O0OOOOOOO0["message"]}')#line:349
                                        return False #line:350
                            OO0OOO0O00000OO00 +=1 #line:351
                        O00O0O00OOOOOO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =OO00OO0O00O00O000 ).json ()#line:352
                        O0OO0O0O0OOO0O000 =O00O0O00OOOOOO0O0 ['data']['cropList']#line:353
                        OOO0000O00OOOOO0O =False #line:354
                        for O0O0O00O00OOOO0O0 in range (12 ):#line:355
                            id =O0OO0O0O0OOO0O000 [O0O0O00O00OOOO0O0 ]['level']#line:356
                            if float (O00OOO000OOOOOOO0 )-float (id )>9 :#line:357
                                OOO0000O00OOO00OO =f'_site={O0O0O00O00OOOO0O0}_{timi_new()}'#line:358
                                OO0OO0O0OO0O000OO ={'accept':'application/json, text/plain, */*','authorization':O0OOOO0OOOO0O0O00 .token ,'timestamp':timi_new (),'sign':sign (OOO0000O00OOO00OO ),'signstring':OOO0000O00OOO00OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:368
                                OO0O0OO0OOO0000OO ={"site":O0O0O00O00OOOO0O0 }#line:369
                                OO00OO0OOO00OO0O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0OO0O0OO0O000OO ,data =OO0O0OO0OOO0000OO ).json ()#line:371
                                if 'status'in OO00OO0OOO00OO0O0 :#line:372
                                    if OO00OO0OOO00OO0O0 ['status']==200 :#line:373
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:374
                            if id !=0 :#line:375
                                for OOOO000OO0OO00OO0 in range (11 ):#line:376
                                    OO00O0OOOO0OOO000 =OOOO000OO0OO00OO0 +1 #line:377
                                    g =O0OO0O0O0OOO0O000 [OO00O0OOOO0OOO000 ]['level']#line:378
                                    if id ==g :#line:379
                                        O000OO0OO00000OOO =OOOO000OO0OO00OO0 +2 #line:380
                                        if O000OO0OO00000OOO ==O0O0O00O00OOOO0O0 +1 :#line:381
                                            pass #line:382
                                        else :#line:383
                                            O000OO00000000OOO =O0O0O00O00OOOO0O0 +1 #line:384
                                            time .sleep (random .randint (1 ,3 )/10 )#line:386
                                            OO0OOO0OO0000O00O =f'_site={O000OO00000000OOO - 1}&targetSite={O000OO0OO00000OOO - 1}_{timi_new()}'#line:387
                                            O00OO00OOO0O0000O ={'accept':'application/json, text/plain, */*','authorization':O0OOOO0OOOO0O0O00 .token ,'timestamp':timi_new (),'sign':sign (OO0OOO0OO0000O00O ),'signstring':OO0OOO0OO0000O00O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:402
                                            OOOOO0OO00OO00OOO ={"site":int (O000OO00000000OOO -1 ),"targetSite":int (O000OO0OO00000OOO -1 )}#line:403
                                            OO000000OOOO0O000 =requests .request ('post',f'{host}/game/crops/move',headers =O00OO00OOO0O0000O ,json =OOOOO0OO00OO00OOO ).json ()#line:405
                                            if 'status'in OO000000OOOO0O000 :#line:406
                                                if OO000000OOOO0O000 ['status']==200 :#line:407
                                                    pass #line:408
                                            print ('【种植合成】:',O000OO00000000OOO ,O000OO0OO00000OOO ,'合成成功')#line:410
                                            OOO0000O00OOOOO0O =True #line:411
                                    if OOO0000O00OOOOO0O :#line:412
                                        break #line:413
                                if OOO0000O00OOOOO0O :#line:414
                                    break #line:415
        except Exception as OOOO0O000OO00OOO0 :#line:416
            O0OOOO0OOOO0O0O00 .synthetic ()#line:417
    def level_new (OO00000O00O000O0O ):#line:420
        try :#line:421
            O0O0OOOOO000OO0O0 =f'__{timi_new()}'#line:422
            OOOOO00O00O00OOO0 ={'authorization':OO00000O00O000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOOO000OO0O0 ),'signstring':O0O0OOOOO000OO0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:431
            OO00OOOOOO0000OOO =requests .request ('get',f'{host}/user',headers =OOOOO00O00O00OOO0 ).json ()#line:432
            if 'status'in OO00OOOOOO0000OOO :#line:433
                if OO00OOOOOO0000OOO ['status']==200 :#line:434
                    return float (OO00OOOOOO0000OOO ['data']['level'])#line:435
        except Exception as OO0000O00000O00OO :#line:436
            print (OO0000O00000O00OO )#line:437
    def propsraffle (OOOO00OO00OO0OOOO ):#line:440
        try :#line:441
            while True :#line:442
                OO0OO0O00OOO0OO0O =f'__{timi_new()}'#line:443
                OO00OO0O000O00OOO ={'authorization':OOOO00OO00OO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O00OOO0OO0O ),'signstring':OO0OO0O00OOO0OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:452
                O00OO00O0O00000O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO00OO0O000O00OOO ).json ()#line:453
                if 'status'in O00OO00O0O00000O0 :#line:455
                    if O00OO00O0O00000O0 ['status']==200 :#line:456
                        OOO000OOOOO0OO000 =O00OO00O0O00000O0 ['data']['rows']#line:457
                        O0O0O00OO0OOOOO00 =O00OO00O0O00000O0 ['data']['vstate']#line:458
                        if OOO000OOOOO0OO000 ==5 or OOO000OOOOO0OO000 ==6 or OOO000OOOOO0OO000 ==7 :#line:459
                            OOOO000O000OO00O0 =O00OO00O0O00000O0 ['data']['silver']#line:460
                            print (f'【转盘抽奖】:获得种子:{OOOO000O000OO00O0}')#line:461
                        if OOO000OOOOO0OO000 ==1 or OOO000OOOOO0OO000 ==2 or OOO000OOOOO0OO000 ==3 :#line:462
                            OO00OOOOOOO00O0OO =O00OO00O0O00000O0 ['data']['clover']#line:463
                            print (f'【转盘抽奖】:获得三叶草:{OO00OOOOOOO00O0OO}')#line:464
                        if OOO000OOOOO0OO000 ==4 or OOO000OOOOO0OO000 ==8 :#line:465
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:466
                        if OOO000OOOOO0OO000 =='抽奖次数已用完':#line:470
                            if O0O0O00OO0OOOOO00 :#line:471
                                OO0000O00O0OO0OO0 =random .randint (160 ,190 )/10 #line:472
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{OO0000O00O0OO0OO0}秒获取抽奖机会')#line:473
                                time .sleep (OO0000O00O0OO0OO0 )#line:474
                                O0000OOO0O00000O0 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OO00OO0O000O00OOO ).json ()#line:476
                                if 'status'in O0000OOO0O00000O0 :#line:478
                                    if O0000OOO0O00000O0 ['status']==200 :#line:479
                                        print (f'【转盘抽奖】:{O0000OOO0O00000O0["message"]}')#line:480
                                    if O0000OOO0O00000O0 ['status']==500 :#line:481
                                        print (f'【转盘抽奖】:{O0000OOO0O00000O0["message"]}')#line:482
                                        break #line:483
                                time .sleep (random .randint (10 ,15 )/10 )#line:484
                            else :#line:485
                                break #line:486
                time .sleep (random .randint (8 ,15 )/10 )#line:487
        except Exception as OO000OOOO0O000O0O :#line:488
            print (OO000OOOO0O000O0O )#line:489
    def friends_invitation (O0O0O0000OO0O0O00 ):#line:492
        try :#line:493
            O0O00OO0OOOOOOOOO =f'__{timi_new()}'#line:494
            OOO0000OOO000O0O0 ={'authorization':O0O0O0000OO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0OOOOOOOOO ),'signstring':O0O00OO0OOOOOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:503
            O000O000OOOOO0OO0 =requests .request ('get',f'{host}/friends',headers =OOO0000OOO000O0O0 ).json ()#line:504
            if 'status'in O000O000OOOOO0OO0 :#line:505
                if O000O000OOOOO0OO0 ['status']==200 :#line:506
                    OOOO0O000O000O00O =O000O000OOOOO0OO0 ['data']['myInviteter']#line:507
                    if OOOO0O000O000O00O :#line:508
                        O0O00O00OOOOO000O =OOOO0O000O000O00O ['user']['nickname']#line:509
                        OO0OOOOO00OOOO000 =O0O0O0000OO0O0O00 .certification ()#line:510
                        print (f'【绑邀请码】:我的邀请人:{O0O00O00OOOOO000O}丨实名:{OO0OOOOO00OOOO000}')#line:511
                    else :#line:512
                        if O0O0O0000OO0O0O00 .innerId !='0':#line:513
                            O0O00OO0OOOOOOOOO =f'_innerId={O0O0O0000OO0O0O00.innerId}_{timi_new()}'#line:514
                            OOO0000OOO000O0O0 ={'authorization':O0O0O0000OO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0OOOOOOOOO ),'signstring':O0O00OO0OOOOOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:523
                            O000O0O0O0O0OOO00 ={"innerId":O0O0O0000OO0O0O00 .innerId }#line:524
                            O000O0000O00000O0 =requests .request ('post',f'{host}/friends/my-invitation',headers =OOO0000OOO000O0O0 ,data =O000O0O0O0O0OOO00 ).json ()#line:526
                            if 'status'in O000O0000O00000O0 :#line:527
                                if O000O0000O00000O0 ['status']==200 :#line:528
                                    print (f'【绑邀请码】:{O0O0O0000OO0O0O00.innerId}{O000O0000O00000O0["message"]}')#line:529
                        else :#line:530
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:531
        except Exception as OO00O0O00O0O00OOO :#line:532
            print (OO00O0O00O0O00OOO )#line:533
    def add_clover (OOOO00OOO0000O00O ):#line:536
        try :#line:537
            O0OOO0000OOOOO0OO =f'__{timi_new()}'#line:538
            OO0OOO0O0O0OOO00O ={'authorization':OOOO00OOO0000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000OOOOO0OO ),'signstring':O0OOO0000OOOOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:547
            O0OO00OOO0OO0O00O =requests .request ('get',f'{host}/assets/clovers',headers =OO0OOO0O0O0OOO00O ).json ()#line:548
            if 'status'in O0OO00OOO0OO0O00O :#line:550
                if O0OO00OOO0OO0O00O ['status']==200 :#line:551
                    OOO00OO0OOOO0OO0O =O0OO00OOO0OO0O00O ['data']['clover']#line:552
                    O0O0O0000OO0O00OO =O0OO00OOO0OO0O00O ['data']['used_clover']#line:553
                    O0O0O00OO0O0OOO0O =float (OOO00OO0OOOO0OO0O )-float (O0O0O0000OO0O00OO )#line:554
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0O0O0000OO0O00OO}')#line:555
                    if O0O0O00OO0O0OOO0O >1 :#line:556
                        O0OOO0000OOOOO0OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O0O00OO0O0OOO0O)}_{timi_new()}'#line:557
                        OO0OOO0O0O0OOO00O ={'authorization':OOOO00OOO0000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000OOOOO0OO ),'signstring':O0OOO0000OOOOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:566
                        OOO0OO00O0O00OO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O0O00OO0O0OOO0O )}#line:567
                        O0000000O00OO0OOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0OOO0O0O0OOO00O ,data =OOO0OO00O0O00OO00 ).json ()#line:568
                        if 'status'in O0000000O00OO0OOO :#line:570
                            if O0000000O00OO0OOO ['status']==200 :#line:571
                                print (f'【参与抽奖】:添加三叶草:{O0000000O00OO0OOO["data"]}丨数量:{O0O0O00OO0O0OOO0O}')#line:572
            OO0OO00O0O0OO0000 =requests .request ('get',f'{host}/lottery',headers =OO0OOO0O0O0OOO00O ).json ()#line:573
            O0O0OO000000O00O0 =OOOO00OOO0000O00O .winning_rewards ()#line:575
            if 'status'in OO0OO00O0O0OO0000 :#line:576
                if OO0OO00O0O0OO0000 ['status']==200 :#line:577
                    OOO0OOOOO00O000OO =OO0OO00O0O0OO0000 ['data'][0 ]['day_get_gold_quantity']#line:578
                    print (f'【参与抽奖】:预计每天中{OOO0OOOOO00O000OO[:6]}种子丨好友收益:{O0O0OO000000O00O0}')#line:579
        except Exception as O0O0OO0000OO0000O :#line:580
            print (O0O0OO0000OO0000O )#line:581
    def energy (O00OOOOOO000O00O0 ):#line:584
        OO0000OO00OO0OOO0 =f'__{timi_new()}'#line:585
        OO0O0OOO0O0O000O0 ={'authorization':O00OOOOOO000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OO00OO0OOO0 ),'signstring':OO0000OO00OO0OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:594
        O0000O000O000O00O =requests .request ('get',f'{host}/energy/general',headers =OO0O0OOO0O0O000O0 ).json ()#line:595
        if 'status'in O0000O000O000O00O :#line:597
            if O0000O000O000O00O ['status']==200 :#line:598
                O0OOOO0O000O0OO00 =O0000O000O000O00O ['data']['ordinary_water_consumptions']#line:599
                if float (O0OOOO0O000O0OO00 )<80 :#line:600
                    OO00O0000OOO0O00O =99 -float (O0OOOO0O000O0OO00 )#line:601
                    OO0O0000OO00OO00O ={"fertilizer":str (OO00O0000OOO0O00O ).split ('.')[0 ]}#line:602
                    OO00000O0OOO000O0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0O0OOO0O0O000O0 ,data =OO0O0000OO00OO00O ).json ()#line:604
                    if 'status'in OO00000O0OOO000O0 :#line:606
                        if OO00000O0OOO000O0 ['status']==200 :#line:607
                            print (f'【购买肥料】:{OO00000O0OOO000O0["message"]}')#line:608
                O000O0O0O0000O000 =O0000O000O000O00O ['data']['ordinary_water_consumptions']#line:609
                if float (O000O0O0O0000O000 )<800 :#line:610
                    OO00O00O0O0OOOO00 =999 -float (O000O0O0O0000O000 )#line:611
                    OO00OO000O0000000 ={"water":str (OO00O00O0O0OOOO00 ).split ('.')[0 ]}#line:612
                    OO0O00OO0O000O000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0O0OOO0O0O000O0 ,data =OO00OO000O0000000 ).json ()#line:613
                    if 'status'in OO0O00OO0O000O000 :#line:614
                        if OO0O00OO0O000O000 ['status']==200 :#line:615
                            print (f'【购买水滴】:{OO0O00OO0O000O000["message"]}')#line:616
def version_of_the_validation ():#line:620
    return str ((66 -56 )/10 )#line:621
def gitee_validation ():#line:624
    try :#line:625
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:626
    except Exception as O00OOOO00O0O00OOO :#line:627
        sys .exit (0 )#line:628
def update_the_validation ():#line:632
    try :#line:633
        O0000O00OOO00OOOO =gitee_validation ()#line:634
        if version_of_the_validation ()<O0000O00OOO00OOOO ['CityEarth']['edition']:#line:635
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0000O00OOO00OOOO["CityEarth"]["edition"]}   ❌')#line:636
            print (f'更新内容=>>{O0000O00OOO00OOOO["CityEarth"]["content"]}   👍')#line:637
        else :#line:638
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0000O00OOO00OOOO["CityEarth"]["edition"]}   ✅')#line:639
            print (f'更新内容=>> {O0000O00OOO00OOOO["CityEarth"]["content"]}   👍')#line:640
    except Exception as O00OOOOOOOOO00OOO :#line:641
        print (O00OOOOOOOOO00OOO )#line:642
def os_qinglong ():#line:645
    if application in os .environ :#line:646
        O00OOOO00OO0O00O0 =os .environ [application ].split ('\n')#line:647
        if len (O00OOOO00OO0O00O0 )>0 :#line:648
            return O00OOOO00OO0O00O0 #line:649
        else :#line:650
            print (f"{application}变量未启用")#line:651
            print ('脚本退出')#line:652
            sys .exit (1 )#line:653
    else :#line:654
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:656
        return os_built ()#line:657
def os_built ():#line:660
    if token :#line:661
        OO0OO0000OO00OOO0 =token .split ('\n')#line:662
        if len (OO0OO0000OO00OOO0 )>0 :#line:663
            return OO0OO0000OO00OOO0 #line:664
    else :#line:665
        print (f"内置变量为空")#line:666
        print ('脚本结束')#line:667
        sys .exit (0 )#line:668
if __name__ =='__main__':#line:671
    start ()#line:672
