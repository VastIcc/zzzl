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
@ 青龙变量 export ce_token="authorization&绑定邀请码&赠送金种子id"   
@ 变量示范    export ce_token="557b8069-1234-4ae7-9e29-b7871f91541b&1937553&0"
@ 不绑定和不赠送填 0   多号换行
@ 我的邀请码是  1937553
@ 版本  0.8
"""
application = 'ce_token'  # 变量名
token = ''


time_xx = random.randint(2, 4)          # 秒 执行下一个号的时间  2到4秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://scsc.sc19319.com'#line:2
level =1 #line:3
def start ():#line:4
    try :#line:5
        update_the_validation ()#line:6
        O00O0O000OO000OOO =os_qinglong ()#line:7
        print (f"==========共找到{len(O00O0O000OO000OOO)}个账号==========")#line:8
        for O00O0000OO0O000OO in O00O0O000OO000OOO :#line:9
            print (f"------------正在执行第{O00O0O000OO000OOO.index(O00O0000OO0O000OO) + 1}个账号------------")#line:10
            OO0000O000OO0OO0O =CityEarth (O00O0000OO0O000OO )#line:11
            if OO0000O000OO0OO0O .base_info ():#line:13
                OO0000O000OO0OO0O .game_map ()#line:17
                OO0000O000OO0OO0O .friends_invitation ()#line:19
                OO0000O000OO0OO0O .add_clover ()#line:21
                OO0000O000OO0OO0O .energy ()#line:23
                OO0000O000OO0OO0O .synthetic ()#line:25
                OO0000O000OO0OO0O .propsraffle ()#line:27
                OO0000O000OO0OO0O .crops_illustrated ()#line:29
                OO0000O000OO0OO0O .give_gold ()#line:31
            else :#line:32
                print ('token失效')#line:33
            time .sleep (time_xx )#line:35
    except Exception as O00000O0O0OOOO0OO :#line:36
        print (O00000O0O0OOOO0OO )#line:37
def sign (OO000O00OO0O00OOO ):#line:39
    O0OO000OO0OO00O0O =hashlib .md5 (OO000O00OO0O00OOO .encode ()).hexdigest ()#line:40
    O0OO0O0O0O0OO0O0O ="scsc%^&*"+O0OO000OO0OO00O0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:41
    OOOOO000O00O0O000 =hashlib .md5 (O0OO0O0O0O0OO0O0O .encode ()).hexdigest ()#line:42
    return OOOOO000O00O0O000 #line:43
def timi_new ():#line:45
    return str (int (time .time ()*1000 ))#line:46
class CityEarth :#line:49
    def __init__ (OOOOO00OOOOO0000O ,OOO000OO0OO0O0000 ):#line:51
        try :#line:52
            OOOOO00OOOOO0000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:53
            OOOOO00OOOOO0000O .token =OOO000OO0OO0O0000 .split ('&')[0 ]#line:54
            OOOOO00OOOOO0000O .innerId =OOO000OO0OO0O0000 .split ('&')[1 ]#line:55
            OOOOO00OOOOO0000O .doneeNo =OOO000OO0OO0O0000 .split ('&')[2 ]#line:56
        except :#line:57
            print ('变量格式错误')#line:58
    def base_info (OO00000O0OO00O00O ):#line:61
        global level #line:62
        try :#line:63
            O0O00O0000OO00000 =f'__{timi_new()}'#line:64
            OO00000000O0OO0O0 ={'authorization':OO00000O0OO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0000OO00000 ),'signstring':O0O00O0000OO00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:73
            O000O0OOO00OOO000 =requests .request ('get',f'{host}/user',headers =OO00000000O0OO0O0 ).json ()#line:74
            if 'status'in O000O0OOO00OOO000 :#line:76
                if O000O0OOO00OOO000 ['status']==200 :#line:77
                    OOO0OO0OO00O00O0O =O000O0OOO00OOO000 ['data']['nickname']#line:78
                    O0OO0O0O00O00000O =O000O0OOO00OOO000 ['data']['inner_id']#line:79
                    OOOO0000O00OOO00O =O000O0OOO00OOO000 ['data']['assets']['gold']#line:80
                    level =O000O0OOO00OOO000 ['data']['level']#line:81
                    print (f'【账号信息】:昵称:{OOO0OO0OO00O00O0O}丨ID:{str(O0OO0O0O00O00000O)[:3] + "**"+ str(O0OO0O0O00O00000O)[5:]}丨等级:{level}丨种子:{str(OOOO0000O00OOO00O).split(".")[0]}')#line:82
                if O000O0OOO00OOO000 ['status']==401 :#line:83
                    return False #line:84
                if O000O0OOO00OOO000 ['status']==500 :#line:85
                    return False #line:86
            return True #line:87
        except Exception as O0000O0OOOOOOOO0O :#line:88
            print (O0000O0OOOOOOOO0O )#line:89
    def game_map (O0O00O00O00O00000 ):#line:92
        OOOO0000000OO0O00 =f'__{timi_new()}'#line:93
        OOOO0O0OOO0O00OO0 ={'authorization':O0O00O00O00O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000000OO0O00 ),'signstring':OOOO0000000OO0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:102
        OOOOO0O00OOO0OO00 =requests .request ('get',f'{host}/game/map',headers =OOOO0O0OOO0O00OO0 ).json ()#line:103
        if 'status'in OOOOO0O00OOO0OO00 :#line:105
            if OOOOO0O00OOO0OO00 ['status']==200 :#line:106
                for OOOO0OOO0O00OO0OO in OOOOO0O00OOO0OO00 ['data']['list'][0 ]['crops']:#line:107
                    OOOO0OOO0O0O00O0O =OOOO0OOO0O00OO0OO ['level']#line:109
                    if OOOO0OOO0O0O00O0O ==41 :#line:110
                        OOO00O0OOO0O0O000 =OOOO0OOO0O00OO0OO ['crop_name']#line:111
                        OO00O000000OOOO00 =OOOO0OOO0O00OO0OO ['count']#line:112
                        if OO00O000000OOOO00 >0 :#line:113
                            print (f'【农业资产】:{OOO00O0OOO0O0O000}丨数量:{OO00O000000OOOO00}')#line:114
    def give_gold (O0O0OO0O0OOOOOO0O ):#line:121
        OOOOO0OOO00000000 =f'__{timi_new()}'#line:122
        O0O000OO0OO0O0O00 ={'authorization':O0O0OO0O0OOOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOO00000000 ),'signstring':OOOOO0OOO00000000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:131
        OO00O00O0OO000O0O =requests .request ('get',f'{host}/user',headers =O0O000OO0OO0O0O00 ).json ()#line:132
        if 'status'in OO00O00O0OO000O0O :#line:133
            if OO00O00O0OO000O0O ['status']==200 :#line:134
                if float (O0O0OO0O0OOOOOO0O .doneeNo )!=0 :#line:135
                    OO00OO00O0OOOOOOO =OO00O00O0OO000O0O ['data']['assets']['gold']#line:136
                    if float (OO00OO00O0OOOOOOO )>2 :#line:137
                        OO000OOOOOO0OO00O =int (float (OO00OO00O0OOOOOOO )/1.1 )#line:138
                        OOOOO0OOO00000000 =f'_doneeNo={O0O0OO0O0OOOOOO0O.doneeNo}&quantity={OO000OOOOOO0OO00O}_{timi_new()}'#line:139
                        O0O000OO0OO0O0O00 ={'authorization':O0O0OO0O0OOOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOO00000000 ),'signstring':OOOOO0OOO00000000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:148
                        O000O0OO00OO0OOOO ={"quantity":OO000OOOOOO0OO00O ,"doneeNo":O0O0OO0O0OOOOOO0O .doneeNo }#line:152
                        O0O0OO00O0O0OOO0O =requests .request ('post',f'{host}/finance/give-gold',headers =O0O000OO0OO0O0O00 ,data =O000O0OO00OO0OOOO ).json ()#line:153
                        if 'status'in O0O0OO00O0O0OOO0O :#line:155
                            if O0O0OO00O0O0OOO0O ['status']==200 :#line:156
                                if O0O0OO00O0O0OOO0O ['data']:#line:157
                                    print (f'【赠送种子】:赠送{OO000OOOOOO0OO00O}种子给{O0O0OO0O0OOOOOO0O.doneeNo}成功')#line:158
                else :#line:159
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:160
    def winning_rewards (O00000O0000O00O0O ):#line:162
        O0OO0O00O0OO00O00 =f'__{timi_new()}'#line:163
        OO0OOO0O0000O00O0 ={'authorization':O00000O0000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O0OO00O00 ),'signstring':O0OO0O00O0OO00O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:172
        O00OOO0000O000O00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO0OOO0O0000O00O0 ).json ()#line:173
        if 'status'in O00OOO0000O000O00 :#line:175
            if O00OOO0000O000O00 ['status']==200 :#line:176
                if O00OOO0000O000O00 ['data']['amount']:#line:177
                    O0OO0OO00O00000O0 =O00OOO0000O000O00 ['data']['amount']['gold']#line:178
                    return O0OO0OO00O00000O0 #line:179
                else :#line:180
                    return 0 #line:181
    def certification (O00O00O00O0000O00 ):#line:183
        OO0O0O0000O0OO0OO =f'__{timi_new()}'#line:184
        O00O0000O0O000O00 ={'authorization':O00O00O00O0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0000O0OO0OO ),'signstring':OO0O0O0000O0OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:193
        O000O0O00O0OO0000 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00O0000O0O000O00 ).json ()#line:194
        if 'status'in O000O0O00O0OO0000 :#line:196
            if O000O0O00O0OO0000 ['status']==200 :#line:197
                if O000O0O00O0OO0000 ['data']['result']:#line:198
                    O0O0O0OO0OO00OO00 =O000O0O00O0OO0000 ['data']['nick_name']#line:199
                    return O0O0O0OO0OO00OO00 #line:200
                else :#line:201
                    return '未实名'#line:202
    def crops_illustrated (OO0OOO0OO00O0OO0O ):#line:205
        OO0O000OOOOOOOOOO =f'__{timi_new()}'#line:206
        O0O000OOO0O000O00 ={'authorization':OO0OOO0OO00O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000OOOOOOOOOO ),'signstring':OO0O000OOOOOOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:215
        OOO00O000OOO000O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O000OOO0O000O00 ).json ()#line:216
        if 'status'in OOO00O000OOO000O0 :#line:218
            if OOO00O000OOO000O0 ['status']==200 :#line:219
                O00OOOO0OOOO00OOO =OOO00O000OOO000O0 ['data'][0 ]['crops']#line:220
                for OOOO00OOO00O0000O in O00OOOO0OOOO00OOO :#line:221
                    if OOOO00OOO00O0000O ['ill_clover_award']:#line:222
                        if float (OOOO00OOO00O0000O ['ill_clover_award'])>1 :#line:223
                            if OOOO00OOO00O0000O ['is_finish']:#line:224
                                if not OOOO00OOO00O0000O ['is_getit']:#line:225
                                    OO0O000OOOOOOOOOO =f'_award_level={OOOO00OOO00O0000O["level"]}_{timi_new()}'#line:226
                                    O0O000OOO0O000O00 ={'authorization':OO0OOO0OO00O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000OOOOOOOOOO ),'signstring':OO0O000OOOOOOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
                                    OO0O0O0OO00O0O0OO ={"award_level":OOOO00OOO00O0000O ['level']}#line:236
                                    O0OO0OO0000OOO00O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O000OOO0O000O00 ,json =OO0O0O0OO00O0O0OO ).json ()#line:237
                                    if 'status'in O0OO0OO0000OOO00O :#line:238
                                        if O0OO0OO0000OOO00O ['status']==200 :#line:239
                                            OO0000OO0O0OO00OO =O0OO0OO0000OOO00O ['data']['ill_clover_award']#line:240
                                            print (f'【图鉴奖励】:领取{OOOO00OOO00O0000O["crop_name"]}成就丨奖励{OO0000OO0O0OO00OO}叶子成功')#line:241
                                        if O0OO0OO0000OOO00O ['status']==500 :#line:242
                                            print (f'【图鉴奖励】:{O0OO0OO0000OOO00O["message"]}')#line:243
    def watched_ad (O00O0OOO000O00000 ):#line:246
        O000O0O0O00O00OOO =f'__{timi_new()}'#line:247
        O00000O0OO0O0O0O0 ={'authorization':O00O0OOO000O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O0O00O00OOO ),'signstring':O000O0O0O00O00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:256
        O0O0O0O00OO0OO00O =requests .request ('post',f'{host}/game/watched-ad',headers =O00000O0OO0O0O0O0 ).json ()#line:257
        print (O0O0O0O00OO0OO00O )#line:258
    def user_ad (OOOOOO000000OOO0O ):#line:264
        OO0OOOO00O00OOO0O =f'__{timi_new()}'#line:265
        OO0O000000OO0OO0O ={'authorization':OOOOOO000000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO00O00OOO0O ),'signstring':OO0OOOO00O00OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:274
        O0OOOOOOOOO0O0OO0 =requests .request ('get',f'{host}/user/ad',headers =OO0O000000OO0OO0O ).json ()#line:275
        if 'status'in O0OOOOOOOOO0O0OO0 :#line:277
            if O0OOOOOOOOO0O0OO0 ['status']==200 :#line:278
                O00O0OOO000OOOO00 =O0OOOOOOOOO0O0OO0 ['data']['max_time']#line:279
                O0O00OO0OOOOOOO0O =O0OOOOOOOOO0O0OO0 ['data']['watch_time']#line:280
                O0O00O0000OOOOOO0 =O0OOOOOOOOO0O0OO0 ['data']['added_time']#line:281
                print (f'【获取种子】:获取种子剩余{O0O00O0000OOOOOO0 + O00O0OOO000OOOO00 - O0O00OO0OOOOOOO0O}次丨好友提供:{O0O00O0000OOOOOO0}次')#line:282
                if O0O00O0000OOOOOO0 +O00O0OOO000OOOO00 -O0O00OO0OOOOOOO0O >0 :#line:283
                    time .sleep (random .randint (16 ,19 ))#line:284
                    O0OOO0OOO00OO0OO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO0O000000OO0OO0O ).json ()#line:285
                    if 'status'in O0OOO0OOO00OO0OO0 :#line:287
                        if O0OOO0OOO00OO0OO0 ['status']==200 :#line:288
                            OOO0O0O000OO000OO =O0OOO0OOO00OO0OO0 ['data']['silver']#line:289
                            print (f'【获取种子】:获得种子:{OOO0O0O000OO000OO}')#line:290
                            return True #line:291
                        if O0OOO0OOO00OO0OO0 ['status']==500 :#line:292
                            O0OOO00O00000O0O0 =O0OOO0OOO00OO0OO0 ['message']#line:293
                            print (f'【获取种子】:{O0OOO00O00000O0O0}')#line:294
                            return False #line:295
    def synthetic (O0OO00O00OOOO00OO ):#line:298
        global id ,g #line:299
        try :#line:300
            while True :#line:302
                O000OOOOO0000OOO0 =f'__{timi_new()}'#line:303
                O0OO0O000OOOO00OO ={'authorization':O0OO00O00OOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOO0000OOO0 ),'signstring':O000OOOOO0000OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:312
                OO0OO00OO000OO000 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O000OOOO00OO ).json ()#line:313
                if 'status'in OO0OO00OO000OO000 :#line:315
                    if OO0OO00OO000OO000 ['status']==200 :#line:316
                        O0OOOO00OOOOOOOOO =OO0OO00OO000OO000 ['data']['cropList']#line:317
                        OOO0O0OOO0O0OO0O0 =OO0OO00OO000OO000 ['data']['gameCoreDataDBid']#line:318
                        OO0OO0OO000OOO0OO =0 #line:319
                        for O0OOOOO00O0OO00OO in O0OOOO00OOOOOOOOO :#line:320
                            if not O0OOOOO00O0OO00OO :#line:321
                                O00000O0O0O000O0O =f'_crop_id={OOO0O0OOO0O0OO0O0}&site={OO0OO0OO000OOO0OO}_{O0OO00O00OOOO00OO.time}'#line:322
                                O0000O0000O0OOO0O ={'authorization':O0OO00O00OOOO00OO .token ,'timestamp':O0OO00O00OOOO00OO .time ,'sign':sign (O00000O0O0O000O0O ),'signstring':O00000O0O0O000O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:331
                                OOOOOOOOO000O00OO ={"site":OO0OO0OO000OOO0OO ,"crop_id":OOO0O0OOO0O0OO0O0 }#line:332
                                OO0OOO0OOOOO0000O =requests .request ('post',f'{host}/game/crops/buy',headers =O0000O0000O0OOO0O ,data =OOOOOOOOO000O00OO ).json ()#line:333
                                time .sleep (random .randint (1 ,3 )/10 )#line:335
                                if 'status'in OO0OOO0OOOOO0000O :#line:336
                                    if OO0OOO0OOOOO0000O ['status']==200 :#line:337
                                        if OO0OOO0OOOOO0000O ['message']=='种子数量不足':#line:338
                                            print (f'【购买合成】:{OO0OOO0OOOOO0000O["message"]}')#line:339
                                            if not O0OO00O00OOOO00OO .user_ad ():#line:340
                                                return False #line:341
                                        print (f'【购买合成】:购买农作物,位置{OO0OO0OO000OOO0OO}')#line:342
                                    if OO0OOO0OOOOO0000O ['status']==500 :#line:343
                                        print (f'【购买合成】:{OO0OOO0OOOOO0000O["message"]}')#line:344
                                        return False #line:345
                            OO0OO0OO000OOO0OO +=1 #line:346
                        OOOOO0OO00O000000 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O000OOOO00OO ).json ()#line:347
                        OO0O0OO0OOO000000 =OOOOO0OO00O000000 ['data']['cropList']#line:348
                        OO00O0OOOO00OOOO0 =False #line:349
                        for O0OOOOO00O0OO00OO in range (12 ):#line:350
                            id =OO0O0OO0OOO000000 [O0OOOOO00O0OO00OO ]['level']#line:351
                            if int (level )-int (id )>9 :#line:352
                                O0OO00O0OOO0OO00O =f'_site={O0OOOOO00O0OO00OO}_{timi_new()}'#line:353
                                OOO000O00O0OOOOO0 ={'accept':'application/json, text/plain, */*','authorization':O0OO00O00OOOO00OO .token ,'timestamp':timi_new (),'sign':sign (O0OO00O0OOO0OO00O ),'signstring':O0OO00O0OOO0OO00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:363
                                OO0O0O00OOO0O000O ={"site":O0OOOOO00O0OO00OO }#line:364
                                O00O000O0OOOO0OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO000O00O0OOOOO0 ,data =OO0O0O00OOO0O000O ).json ()#line:365
                                if 'status'in O00O000O0OOOO0OOO :#line:367
                                    if O00O000O0OOOO0OOO ['status']==200 :#line:368
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:369
                            if id !=0 :#line:370
                                for O0OOO00O0OOOO0O0O in range (11 ):#line:371
                                    O00OOOO0000OO0OO0 =O0OOO00O0OOOO0O0O +1 #line:372
                                    g =OO0O0OO0OOO000000 [O00OOOO0000OO0OO0 ]['level']#line:373
                                    if id ==g :#line:374
                                        O0OO0O00OOO000OOO =O0OOO00O0OOOO0O0O +2 #line:375
                                        if O0OO0O00OOO000OOO ==O0OOOOO00O0OO00OO +1 :#line:376
                                            pass #line:377
                                        else :#line:378
                                            OO00OO000OO00OOOO =O0OOOOO00O0OO00OO +1 #line:379
                                            time .sleep (random .randint (1 ,3 )/10 )#line:381
                                            OO0OOOO00OOO0OOO0 =f'_site={OO00OO000OO00OOOO-1}&targetSite={O0OO0O00OOO000OOO-1}_{timi_new()}'#line:382
                                            O0OOOOO00O000OOO0 ={'accept':'application/json, text/plain, */*','authorization':O0OO00O00OOOO00OO .token ,'timestamp':timi_new (),'sign':sign (OO0OOOO00OOO0OOO0 ),'signstring':OO0OOOO00OOO0OOO0 ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:397
                                            OO0OOO0OOO0OOOO0O ={"site":int (OO00OO000OO00OOOO -1 ),"targetSite":int (O0OO0O00OOO000OOO -1 )}#line:398
                                            OOO0O0O0OOOO00000 =requests .request ('post',f'{host}/game/crops/move',headers =O0OOOOO00O000OOO0 ,json =OO0OOO0OOO0OOOO0O ).json ()#line:399
                                            if 'status'in OOO0O0O0OOOO00000 :#line:400
                                                if OOO0O0O0OOOO00000 ['status']==200 :#line:401
                                                    pass #line:402
                                            print ('【购买合成】:',OO00OO000OO00OOOO ,O0OO0O00OOO000OOO ,'合成成功')#line:404
                                            OO00O0OOOO00OOOO0 =True #line:405
                                    if OO00O0OOOO00OOOO0 :#line:406
                                        break #line:407
                                if OO00O0OOOO00OOOO0 :#line:408
                                    break #line:409
        except Exception as OOOO00O0OOO0OO00O :#line:410
            O0OO00O00OOOO00OO .synthetic ()#line:411
    def propsraffle (OO0O0O0O0OO0OOO0O ):#line:415
        try :#line:416
            while True :#line:417
                O0O0OO00OOOO000O0 =f'__{timi_new()}'#line:418
                OOO0O00O0OOOOOOOO ={'authorization':OO0O0O0O0OO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00OOOO000O0 ),'signstring':O0O0OO00OOOO000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:427
                OOO0000OO0OO00000 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO0O00O0OOOOOOOO ).json ()#line:428
                if 'status'in OOO0000OO0OO00000 :#line:430
                    if OOO0000OO0OO00000 ['status']==200 :#line:431
                        OO0OO000OOOO0000O =OOO0000OO0OO00000 ['data']['rows']#line:432
                        OOOO000O0O00O000O =OOO0000OO0OO00000 ['data']['vstate']#line:433
                        if OO0OO000OOOO0000O ==5 or OO0OO000OOOO0000O ==6 or OO0OO000OOOO0000O ==7 :#line:434
                            OO0OOO0O00OO0OO00 =OOO0000OO0OO00000 ['data']['silver']#line:435
                            print (f'【转盘抽奖】:获得种子:{OO0OOO0O00OO0OO00}')#line:436
                        if OO0OO000OOOO0000O ==1 or OO0OO000OOOO0000O ==2 or OO0OO000OOOO0000O ==3 :#line:437
                            OOO0000OO00OOOO00 =OOO0000OO0OO00000 ['data']['clover']#line:438
                            print (f'【转盘抽奖】:获得三叶草:{OOO0000OO00OOOO00}')#line:439
                        if OO0OO000OOOO0000O ==4 or OO0OO000OOOO0000O ==8 :#line:440
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:441
                        if OO0OO000OOOO0000O =='抽奖次数已用完':#line:445
                            if OOOO000O0O00O000O :#line:446
                                O0OOOOOO0O0OOOOO0 =random .randint (160 ,190 )/10 #line:447
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{O0OOOOOO0O0OOOOO0}秒获取抽奖机会')#line:448
                                time .sleep (O0OOOOOO0O0OOOOO0 )#line:449
                                OO0O0000OO0O0O000 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OOO0O00O0OOOOOOOO ).json ()#line:450
                                if 'status'in OO0O0000OO0O0O000 :#line:452
                                    if OO0O0000OO0O0O000 ['status']==200 :#line:453
                                        print (f'【转盘抽奖】:{OO0O0000OO0O0O000["message"]}')#line:454
                                    if OO0O0000OO0O0O000 ['status']==500 :#line:455
                                        print (f'【转盘抽奖】:{OO0O0000OO0O0O000["message"]}')#line:456
                                        break #line:457
                                time .sleep (random .randint (10 ,15 )/10 )#line:458
                            else :#line:459
                                break #line:460
                time .sleep (random .randint (8 ,15 )/10 )#line:461
        except Exception as OOOOO0OOO0OOO000O :#line:462
            print (OOOOO0OOO0OOO000O )#line:463
    def friends_invitation (OO00O0OO0O000OO0O ):#line:466
        try :#line:467
            O0O0OO000OO0OO00O =f'__{timi_new()}'#line:468
            O00OO000OO0O0O0OO ={'authorization':OO00O0OO0O000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO000OO0OO00O ),'signstring':O0O0OO000OO0OO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:477
            O00O00O0OO0OO00O0 =requests .request ('get',f'{host}/friends',headers =O00OO000OO0O0O0OO ).json ()#line:478
            if 'status'in O00O00O0OO0OO00O0 :#line:479
                if O00O00O0OO0OO00O0 ['status']==200 :#line:480
                    OO0OOO0O0OO0000O0 =O00O00O0OO0OO00O0 ['data']['myInviteter']#line:481
                    if OO0OOO0O0OO0000O0 :#line:482
                        O0OOO00O00OO0O000 =OO0OOO0O0OO0000O0 ['user']['nickname']#line:483
                        OOO0O000OOOOO00OO =OO00O0OO0O000OO0O .certification ()#line:484
                        print (f'【绑邀请码】:我的邀请人:{O0OOO00O00OO0O000}丨实名:{OOO0O000OOOOO00OO}')#line:485
                    else :#line:486
                        if OO00O0OO0O000OO0O .innerId !='0':#line:487
                            O0O0OO000OO0OO00O =f'_innerId={OO00O0OO0O000OO0O.innerId}_{timi_new()}'#line:488
                            O00OO000OO0O0O0OO ={'authorization':OO00O0OO0O000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO000OO0OO00O ),'signstring':O0O0OO000OO0OO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:497
                            OO00O00O0O0OO0OO0 ={"innerId":OO00O0OO0O000OO0O .innerId }#line:498
                            O0OOO0OO00O000OO0 =requests .request ('post',f'{host}/friends/my-invitation',headers =O00OO000OO0O0O0OO ,data =OO00O00O0O0OO0OO0 ).json ()#line:499
                            if 'status'in O0OOO0OO00O000OO0 :#line:500
                                if O0OOO0OO00O000OO0 ['status']==200 :#line:501
                                    print (f'【绑邀请码】:{OO00O0OO0O000OO0O.innerId}{O0OOO0OO00O000OO0["message"]}')#line:502
                        else :#line:503
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:504
        except Exception as O0OOO0O00O0OO00OO :#line:505
            print (O0OOO0O00O0OO00OO )#line:506
    def add_clover (OO0O00OO0000O0000 ):#line:510
        try :#line:511
            O0OOOOO000OOO0OO0 =f'__{timi_new()}'#line:512
            OOO0OOO000O0OOO0O ={'authorization':OO0O00OO0000O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO000OOO0OO0 ),'signstring':O0OOOOO000OOO0OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:521
            OOO000OOO0O0O0OOO =requests .request ('get',f'{host}/assets/clovers',headers =OOO0OOO000O0OOO0O ).json ()#line:522
            if 'status'in OOO000OOO0O0O0OOO :#line:524
                if OOO000OOO0O0O0OOO ['status']==200 :#line:525
                    O00OOOO00O00O0OOO =OOO000OOO0O0O0OOO ['data']['clover']#line:526
                    OO0O0O00OOO000O0O =OOO000OOO0O0O0OOO ['data']['used_clover']#line:527
                    O0000000OOOO0OOOO =float (O00OOOO00O00O0OOO )-float (OO0O0O00OOO000O0O )#line:528
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OO0O0O00OOO000O0O}')#line:529
                    if O0000000OOOO0OOOO >1 :#line:530
                        O0OOOOO000OOO0OO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0000000OOOO0OOOO)}_{timi_new()}'#line:531
                        OOO0OOO000O0OOO0O ={'authorization':OO0O00OO0000O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO000OOO0OO0 ),'signstring':O0OOOOO000OOO0OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:540
                        O0OO0O000OO0OOO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0000000OOOO0OOOO )}#line:541
                        O0000O0000000O00O =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO0OOO000O0OOO0O ,data =O0OO0O000OO0OOO00 ).json ()#line:542
                        if 'status'in O0000O0000000O00O :#line:544
                            if O0000O0000000O00O ['status']==200 :#line:545
                                print (f'【参与抽奖】:添加三叶草:{O0000O0000000O00O["data"]}丨数量:{O0000000OOOO0OOOO}')#line:546
            O0O0OO000O0OOO0OO =requests .request ('get',f'{host}/lottery',headers =OOO0OOO000O0OOO0O ).json ()#line:547
            O000O00O0OO000O00 =OO0O00OO0000O0000 .winning_rewards ()#line:549
            if 'status'in O0O0OO000O0OOO0OO :#line:550
                if O0O0OO000O0OOO0OO ['status']==200 :#line:551
                    O000O000O0O00OOO0 =O0O0OO000O0OOO0OO ['data'][0 ]['day_get_gold_quantity']#line:552
                    print (f'【参与抽奖】:预计每天中{O000O000O0O00OOO0[:6]}种子丨好友收益:{O000O00O0OO000O00}')#line:553
        except Exception as O0OO00OOOO0O0OOOO :#line:554
            print (O0OO00OOOO0O0OOOO )#line:555
    def energy (O0OO000OO000O00OO ):#line:558
        OOOOO00000000O0OO =f'__{timi_new()}'#line:559
        O0OOOO00OO0O0OO0O ={'authorization':O0OO000OO000O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00000000O0OO ),'signstring':OOOOO00000000O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:568
        O0000O00O00O00O00 =requests .request ('get',f'{host}/energy/general',headers =O0OOOO00OO0O0OO0O ).json ()#line:569
        if 'status'in O0000O00O00O00O00 :#line:571
            if O0000O00O00O00O00 ['status']==200 :#line:572
                O0OOO00OO0OOO00O0 =O0000O00O00O00O00 ['data']['ordinary_water_consumptions']#line:573
                if float (O0OOO00OO0OOO00O0 )<80 :#line:574
                    OOOO0O0OO00OOOOO0 =99 -float (O0OOO00OO0OOO00O0 )#line:575
                    OOO0O000O000O0OO0 ={"fertilizer":str (OOOO0O0OO00OOOOO0 ).split ('.')[0 ]}#line:576
                    O00O0O0OOO00000OO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0OOOO00OO0O0OO0O ,data =OOO0O000O000O0OO0 ).json ()#line:577
                    if 'status'in O00O0O0OOO00000OO :#line:579
                        if O00O0O0OOO00000OO ['status']==200 :#line:580
                            print (f'【购买肥料】:{O00O0O0OOO00000OO["message"]}')#line:581
                OO00OOOOO0OO00O00 =O0000O00O00O00O00 ['data']['ordinary_water_consumptions']#line:582
                if float (OO00OOOOO0OO00O00 )<800 :#line:583
                    OOO0000O0OOO000O0 =999 -float (OO00OOOOO0OO00O00 )#line:584
                    O0O0OO0O000O0OOO0 ={"water":str (OOO0000O0OOO000O0 ).split ('.')[0 ]}#line:585
                    O000OO0OOO0O0O000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0OOOO00OO0O0OO0O ,data =O0O0OO0O000O0OOO0 ).json ()#line:586
                    if 'status'in O000OO0OOO0O0O000 :#line:587
                        if O000OO0OOO0O0O000 ['status']==200 :#line:588
                            print (f'【购买水滴】:{O000OO0OOO0O0O000["message"]}')#line:589
def version_of_the_validation ():#line:595
    return str ((64 -56 )/10 )#line:596
def gitee_validation ():#line:598
    try :#line:599
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:600
    except Exception as O00O00000O00OOOO0 :#line:601
        sys .exit (0 )#line:602
def update_the_validation ():#line:608
    try :#line:609
        O00O000O00OO0OOO0 =gitee_validation ()#line:610
        if version_of_the_validation ()<O00O000O00OO0OOO0 ['CityEarth']['edition']:#line:611
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O000O00OO0OOO0["CityEarth"]["edition"]}   ❌')#line:612
            print (f'更新内容=>>{O00O000O00OO0OOO0["CityEarth"]["content"]}   👍')#line:613
        else :#line:614
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O000O00OO0OOO0["CityEarth"]["edition"]}   ✅')#line:615
            print (f'更新内容=>> {O00O000O00OO0OOO0["CityEarth"]["content"]}   👍')#line:616
    except Exception as OOO0O000OOOO00OOO :#line:617
        print (OOO0O000OOOO00OOO )#line:618
def os_qinglong ():#line:621
    if application in os .environ :#line:622
        OOO00O00000OOOOO0 =os .environ [application ].split ('\n')#line:623
        if len (OOO00O00000OOOOO0 )>0 :#line:624
            return OOO00O00000OOOOO0 #line:625
        else :#line:626
            print (f"{application}变量未启用")#line:627
            print ('脚本退出')#line:628
            sys .exit (1 )#line:629
    else :#line:630
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:631
        return os_built ()#line:632
def os_built ():#line:635
    if token :#line:636
        OO0000O00O0OOO0O0 =token .split ('\n')#line:637
        if len (OO0000O00O0OOO0O0 )>0 :#line:638
            return OO0000O00O0OOO0O0 #line:639
    else :#line:640
        print (f"内置变量为空")#line:641
        print ('脚本结束')#line:642
        sys .exit (0 )#line:643
if __name__ =='__main__':#line:646
    start ()#line:647
