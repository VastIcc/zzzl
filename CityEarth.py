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
cron: 12 */3 * * *
new Env('生城世朝')
项目地址  微信打开  http://share.sc19319.com/scsc/1937553
抓取  http://scsc.sc19319.com 的authorization值
青龙变量 export ce_token="authorization&绑定邀请码"   不绑定填 0   多号换行
我的邀请码是  1937553
版本  0.5
"""
application = 'ce_token'  # 变量名
token = ''


time_xx = random.randint(8, 12)          # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://scsc.sc19319.com'#line:2
level =1 #line:3
def start ():#line:4
    try :#line:5
        update_the_validation ()#line:6
        O0OO00OO000O000OO =os_qinglong ()#line:7
        print (f"==========共找到{len(O0OO00OO000O000OO)}个账号==========")#line:8
        for OO0000O00O0OOOOOO in O0OO00OO000O000OO :#line:9
            print (f"------------正在执行第{O0OO00OO000O000OO.index(OO0000O00O0OOOOOO) + 1}个账号------------")#line:10
            OOOOOO000O0OOO000 =CityEarth (OO0000O00O0OOOOOO )#line:11
            if OOOOOO000O0OOO000 .base_info ():#line:13
                OOOOOO000O0OOO000 .friends_invitation ()#line:18
                OOOOOO000O0OOO000 .add_clover ()#line:20
                OOOOOO000O0OOO000 .energy ()#line:22
                OOOOOO000O0OOO000 .synthetic ()#line:24
                OOOOOO000O0OOO000 .propsraffle ()#line:26
                OOOOOO000O0OOO000 .crops_illustrated ()#line:28
            else :#line:29
                print ('token失效')#line:30
            time .sleep (time_xx )#line:32
    except Exception as OOO000000O0OOO000 :#line:33
        print (OOO000000O0OOO000 )#line:34
def sign (O0O0O0O000OOO0O00 ):#line:36
    OO0OO0O0OOOO0O000 =hashlib .md5 (O0O0O0O000OOO0O00 .encode ()).hexdigest ()#line:37
    OO0O0O00OO0O0OOO0 ="scsc%^&*"+OO0OO0O0OOOO0O000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:38
    O00OOOO0OOO000O0O =hashlib .md5 (OO0O0O00OO0O0OOO0 .encode ()).hexdigest ()#line:39
    return O00OOOO0OOO000O0O #line:40
def timi_new ():#line:42
    return str (int (time .time ()*1000 ))#line:43
class CityEarth :#line:46
    def __init__ (O0O0000O00O00O0O0 ,OOOO00OOOOOO0OOOO ):#line:48
        try :#line:49
            O0O0000O00O00O0O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:50
            O0O0000O00O00O0O0 .token =OOOO00OOOOOO0OOOO .split ('&')[0 ]#line:51
            O0O0000O00O00O0O0 .innerId =OOOO00OOOOOO0OOOO .split ('&')[1 ]#line:52
        except Exception as OO00O0O0OO0O00O0O :#line:53
            print ('变量格式错误')#line:54
    def base_info (O0000OOOO0OOOO0OO ):#line:57
        global level #line:58
        try :#line:59
            O0O0O0OOOOOO00000 =f'__{timi_new()}'#line:60
            OOO0OOOOO00O00000 ={'authorization':O0000OOOO0OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOOOO00000 ),'signstring':O0O0O0OOOOOO00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:69
            OO00000O00OOOO000 =requests .request ('get',f'{host}/user',headers =OOO0OOOOO00O00000 ).json ()#line:70
            if 'status'in OO00000O00OOOO000 :#line:71
                if OO00000O00OOOO000 ['status']==200 :#line:72
                    OO00O00000OO00000 =OO00000O00OOOO000 ['data']['nickname']#line:73
                    OOO0O0000000O00O0 =OO00000O00OOOO000 ['data']['inner_id']#line:74
                    OOO00O0000O00OO00 =OO00000O00OOOO000 ['data']['assets']['gold']#line:75
                    level =OO00000O00OOOO000 ['data']['level']#line:76
                    print (f'【账号信息】:昵称:{OO00O00000OO00000}丨ID:{str(OOO0O0000000O00O0)[:3] + "**"+ str(OOO0O0000000O00O0)[5:]}丨等级:{level}丨种子:{str(OOO00O0000O00OO00).split(".")[0]}')#line:77
                if OO00000O00OOOO000 ['status']==401 :#line:78
                    return False #line:79
                if OO00000O00OOOO000 ['status']==500 :#line:80
                    return False #line:81
            return True #line:82
        except Exception as O00O000OOOOOOOOO0 :#line:83
            print (O00O000OOOOOOOOO0 )#line:84
    def crops_illustrated (O0O00OOO000OOO0O0 ):#line:88
        O0O0000OOOO000OO0 =f'__{timi_new()}'#line:89
        OO0O00O0OO0O0OOO0 ={'authorization':O0O00OOO000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OOOO000OO0 ),'signstring':O0O0000OOOO000OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:98
        O000O000O0O000000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O00O0OO0O0OOO0 ).json ()#line:99
        if 'status'in O000O000O0O000000 :#line:101
            if O000O000O0O000000 ['status']==200 :#line:102
                OOOO00OOOOOOOO00O =O000O000O0O000000 ['data'][0 ]['crops']#line:103
                for O00O000OO000O0O0O in OOOO00OOOOOOOO00O :#line:104
                    if O00O000OO000O0O0O ['ill_clover_award']:#line:105
                        if float (O00O000OO000O0O0O ['ill_clover_award'])>1 :#line:106
                            if O00O000OO000O0O0O ['is_finish']:#line:107
                                if not O00O000OO000O0O0O ['is_getit']:#line:108
                                    O0O0000OOOO000OO0 =f'_award_level={O00O000OO000O0O0O["level"]}_{timi_new()}'#line:109
                                    OO0O00O0OO0O0OOO0 ={'authorization':O0O00OOO000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OOOO000OO0 ),'signstring':O0O0000OOOO000OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:118
                                    O00OOOO00OOO000O0 ={"award_level":O00O000OO000O0O0O ['level']}#line:119
                                    O00O0OO0OOOO0O00O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O00O0OO0O0OOO0 ,json =O00OOOO00OOO000O0 ).json ()#line:120
                                    if 'status'in O00O0OO0OOOO0O00O :#line:121
                                        if O00O0OO0OOOO0O00O ['status']==200 :#line:122
                                            OOOOO0O000O00OOO0 =O00O0OO0OOOO0O00O ['data']['ill_clover_award']#line:123
                                            print (f'【图鉴奖励】:领取{O00O000OO000O0O0O["crop_name"]}成就丨奖励{OOOOO0O000O00OOO0}叶子成功')#line:124
                                        if O00O0OO0OOOO0O00O ['status']==500 :#line:125
                                            print (f'【图鉴奖励】:{O00O0OO0OOOO0O00O["message"]}')#line:126
    def watched_ad (OO0O0OO0000O00OOO ):#line:129
        O0OO00OOOO0OOO000 =f'__{timi_new()}'#line:130
        OOO0OOOO00OO0OO0O ={'authorization':OO0O0OO0000O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OOOO0OOO000 ),'signstring':O0OO00OOOO0OOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:139
        OO0OOOOOOOOO000OO =requests .request ('post',f'{host}/game/watched-ad',headers =OOO0OOOO00OO0OO0O ).json ()#line:140
        print (OO0OOOOOOOOO000OO )#line:141
    def user_ad (OOO0O0OO0OOOO0OOO ):#line:147
        OOO0O00000OOOO0OO =f'__{timi_new()}'#line:148
        O0OO0O0O00OO0000O ={'authorization':OOO0O0OO0OOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00000OOOO0OO ),'signstring':OOO0O00000OOOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:157
        OO0OOOOOOO0O00OOO =requests .request ('get',f'{host}/user/ad',headers =O0OO0O0O00OO0000O ).json ()#line:158
        if 'status'in OO0OOOOOOO0O00OOO :#line:160
            if OO0OOOOOOO0O00OOO ['status']==200 :#line:161
                O00O000OOO00O0000 =OO0OOOOOOO0O00OOO ['data']['max_time']#line:162
                O00O0000000OOO00O =OO0OOOOOOO0O00OOO ['data']['watch_time']#line:163
                O0000O0O000OOO00O =OO0OOOOOOO0O00OOO ['data']['added_time']#line:164
                print (f'【获取种子】:获取种子剩余{O0000O0O000OOO00O + O00O000OOO00O0000 - O00O0000000OOO00O}次丨好友提供:{O0000O0O000OOO00O}次')#line:165
                if O0000O0O000OOO00O +O00O000OOO00O0000 -O00O0000000OOO00O >0 :#line:166
                    time .sleep (random .randint (16 ,19 ))#line:167
                    OO0OOOO0O0O0O0000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OO0O0O00OO0000O ).json ()#line:168
                    if 'status'in OO0OOOO0O0O0O0000 :#line:170
                        if OO0OOOO0O0O0O0000 ['status']==200 :#line:171
                            OOO0O00O000O0OOOO =OO0OOOO0O0O0O0000 ['data']['silver']#line:172
                            print (f'【获取种子】:获得种子:{OOO0O00O000O0OOOO}')#line:173
                            return True #line:174
                        if OO0OOOO0O0O0O0000 ['status']==500 :#line:175
                            OOOOOOOOOOOOOOOOO =OO0OOOO0O0O0O0000 ['message']#line:176
                            print (f'【获取种子】:{OOOOOOOOOOOOOOOOO}')#line:177
                            return False #line:178
    def synthetic (O0O0O0O0O00O0OO0O ):#line:181
        global id ,g #line:182
        try :#line:183
            while True :#line:185
                OO0O00OO00O0OO0OO =f'__{timi_new()}'#line:186
                OO0OO000OOO0O0O0O ={'authorization':O0O0O0O0O00O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OO00O0OO0OO ),'signstring':OO0O00OO00O0OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:195
                OOO0OOOOO00OO000O =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO000OOO0O0O0O ).json ()#line:196
                if 'status'in OOO0OOOOO00OO000O :#line:198
                    if OOO0OOOOO00OO000O ['status']==200 :#line:199
                        O00O0OO0OO0O0OO00 =OOO0OOOOO00OO000O ['data']['cropList']#line:200
                        OO0OOO0OOOOOOO00O =OOO0OOOOO00OO000O ['data']['gameCoreDataDBid']#line:201
                        O00OOO0OOO00000OO =0 #line:202
                        for OO000O00OO00O000O in O00O0OO0OO0O0OO00 :#line:203
                            if not OO000O00OO00O000O :#line:204
                                O00O0O0O0O0000OOO =f'_crop_id={OO0OOO0OOOOOOO00O}&site={O00OOO0OOO00000OO}_{O0O0O0O0O00O0OO0O.time}'#line:205
                                OO0OOOO00OOOO000O ={'authorization':O0O0O0O0O00O0OO0O .token ,'timestamp':O0O0O0O0O00O0OO0O .time ,'sign':sign (O00O0O0O0O0000OOO ),'signstring':O00O0O0O0O0000OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
                                O0O0OOOOOO0OO0OO0 ={"site":O00OOO0OOO00000OO ,"crop_id":OO0OOO0OOOOOOO00O }#line:215
                                O000OOO0O0O0O0O00 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0OOOO00OOOO000O ,data =O0O0OOOOOO0OO0OO0 ).json ()#line:216
                                if 'status'in O000OOO0O0O0O0O00 :#line:218
                                    if O000OOO0O0O0O0O00 ['status']==200 :#line:219
                                        if O000OOO0O0O0O0O00 ['message']=='种子数量不足':#line:220
                                            print (f'【购买合成】:{O000OOO0O0O0O0O00["message"]}')#line:221
                                            if not O0O0O0O0O00O0OO0O .user_ad ():#line:222
                                                return False #line:223
                                        print (f'【购买合成】:购买农作物,位置{O00OOO0OOO00000OO}')#line:224
                                    if O000OOO0O0O0O0O00 ['status']==500 :#line:225
                                        print (f'【购买合成】:{O000OOO0O0O0O0O00["message"]}')#line:226
                                        return False #line:227
                                time .sleep (random .randint (3 ,5 )/10 )#line:228
                            O00OOO0OOO00000OO +=1 #line:229
                        O00OOO0O000000O00 =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO000OOO0O0O0O ).json ()#line:230
                        OOO0O0OOOO00OOOO0 =O00OOO0O000000O00 ['data']['cropList']#line:231
                        O0OOO000O000O000O =False #line:232
                        for OO000O00OO00O000O in range (12 ):#line:233
                            id =OOO0O0OOOO00OOOO0 [OO000O00OO00O000O ]['level']#line:234
                            if int (level )-int (id )>8 :#line:235
                                OOOOO0000O0O0O000 =f'_site={OO000O00OO00O000O}_{timi_new()}'#line:236
                                O0OO00OOO0O0O000O ={'accept':'application/json, text/plain, */*','authorization':O0O0O0O0O00O0OO0O .token ,'timestamp':timi_new (),'sign':sign (OOOOO0000O0O0O000 ),'signstring':OOOOO0000O0O0O000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:246
                                O00O0OO000O0O0OO0 ={"site":OO000O00OO00O000O }#line:247
                                O0O00OOO0OOOOOOOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OO00OOO0O0O000O ,data =O00O0OO000O0O0OO0 ).json ()#line:248
                                if 'status'in O0O00OOO0OOOOOOOO :#line:250
                                    if O0O00OOO0OOOOOOOO ['status']==200 :#line:251
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:252
                            if id !=0 :#line:253
                                for O00O000OOOOO0OO0O in range (11 ):#line:254
                                    OO00000000O0OOOOO =O00O000OOOOO0OO0O +1 #line:255
                                    g =OOO0O0OOOO00OOOO0 [OO00000000O0OOOOO ]['level']#line:256
                                    if id ==g :#line:257
                                        OOOO00OOO0000O0OO =O00O000OOOOO0OO0O +2 #line:258
                                        if OOOO00OOO0000O0OO ==OO000O00OO00O000O +1 :#line:259
                                            pass #line:260
                                        else :#line:261
                                            time .sleep (random .randint (3 ,5 )/10 )#line:262
                                            O0O0O00O000O0OO0O =OO000O00OO00O000O +1 #line:263
                                            O000OO0O0O0OO0000 =f'_site={O0O0O00O000O0OO0O-1}&targetSite={OOOO00OOO0000O0OO-1}_{timi_new()}'#line:266
                                            OO00O0O0OOOO00O00 ={'accept':'application/json, text/plain, */*','authorization':O0O0O0O0O00O0OO0O .token ,'timestamp':timi_new (),'sign':sign (O000OO0O0O0OO0000 ),'signstring':O000OO0O0O0OO0000 ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:281
                                            O000OOOO00OOOOO00 ={"site":int (O0O0O00O000O0OO0O -1 ),"targetSite":int (OOOO00OOO0000O0OO -1 )}#line:282
                                            O00O00O0O00O0O000 =requests .request ('post',f'{host}/game/crops/move',headers =OO00O0O0OOOO00O00 ,json =O000OOOO00OOOOO00 ).json ()#line:283
                                            if 'status'in O00O00O0O00O0O000 :#line:284
                                                if O00O00O0O00O0O000 ['status']==200 :#line:285
                                                    pass #line:286
                                            print ('【购买合成】:',O0O0O00O000O0OO0O ,OOOO00OOO0000O0OO ,'合成成功')#line:288
                                            O0OOO000O000O000O =True #line:289
                                    if O0OOO000O000O000O :#line:290
                                        break #line:291
                                if O0OOO000O000O000O :#line:292
                                    break #line:293
        except Exception as O0000OO00OO0OO0O0 :#line:294
            O0O0O0O0O00O0OO0O .synthetic ()#line:295
    def propsraffle (O0OOOO0OOOO00OO00 ):#line:299
        try :#line:300
            while True :#line:301
                OO0O0OO0OOO0OOOO0 =f'__{timi_new()}'#line:302
                OOOOO0OOOO0O0O0OO ={'authorization':O0OOOO0OOOO00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO0OOO0OOOO0 ),'signstring':OO0O0OO0OOO0OOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:311
                OOOOOO00OO000OOO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOOO0OOOO0O0O0OO ).json ()#line:312
                if 'status'in OOOOOO00OO000OOO0 :#line:314
                    if OOOOOO00OO000OOO0 ['status']==200 :#line:315
                        O0O0000OO000O0OOO =OOOOOO00OO000OOO0 ['data']['rows']#line:316
                        OO0000O0OO0OOOO0O =OOOOOO00OO000OOO0 ['data']['vstate']#line:317
                        if O0O0000OO000O0OOO ==5 or O0O0000OO000O0OOO ==6 or O0O0000OO000O0OOO ==7 :#line:318
                            O0O00O00O000000O0 =OOOOOO00OO000OOO0 ['data']['silver']#line:319
                            print (f'【转盘抽奖】:获得种子:{O0O00O00O000000O0}')#line:320
                        if O0O0000OO000O0OOO ==1 or O0O0000OO000O0OOO ==2 or O0O0000OO000O0OOO ==3 :#line:321
                            O00OOO0000000O000 =OOOOOO00OO000OOO0 ['data']['clover']#line:322
                            print (f'【转盘抽奖】:获得三叶草:{O00OOO0000000O000}')#line:323
                        if O0O0000OO000O0OOO ==4 or O0O0000OO000O0OOO ==8 :#line:324
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:325
                        if O0O0000OO000O0OOO =='抽奖次数已用完':#line:329
                            if OO0000O0OO0OOOO0O :#line:330
                                OO0OOOOO0OO000O00 =random .randint (160 ,190 )/10 #line:331
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{OO0OOOOO0OO000O00}秒获取抽奖机会')#line:332
                                time .sleep (OO0OOOOO0OO000O00 )#line:333
                                O0O00OO00O00OOOO0 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OOOOO0OOOO0O0O0OO ).json ()#line:334
                                if 'status'in O0O00OO00O00OOOO0 :#line:336
                                    if O0O00OO00O00OOOO0 ['status']==200 :#line:337
                                        print (f'【转盘抽奖】:{O0O00OO00O00OOOO0["message"]}')#line:338
                                    if O0O00OO00O00OOOO0 ['status']==500 :#line:339
                                        print (f'【转盘抽奖】:{O0O00OO00O00OOOO0["message"]}')#line:340
                                        break #line:341
                                time .sleep (random .randint (10 ,15 )/10 )#line:342
                            else :#line:343
                                break #line:344
                time .sleep (random .randint (8 ,15 )/10 )#line:345
        except Exception as O0O0OOOOO00O00OOO :#line:346
            print (O0O0OOOOO00O00OOO )#line:347
    def friends_invitation (OO0O0O00OOOOO000O ):#line:350
        try :#line:351
            OOOO0OOOO0O000000 =f'__{timi_new()}'#line:352
            OO0OOOOOOOO00OOO0 ={'authorization':OO0O0O00OOOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOO0O000000 ),'signstring':OOOO0OOOO0O000000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:361
            O0O0O00000OO0O00O =requests .request ('get',f'{host}/friends',headers =OO0OOOOOOOO00OOO0 ).json ()#line:362
            if 'status'in O0O0O00000OO0O00O :#line:363
                if O0O0O00000OO0O00O ['status']==200 :#line:364
                    OOOOO0000OO0OO0O0 =O0O0O00000OO0O00O ['data']['myInviteter']#line:365
                    if OOOOO0000OO0OO0O0 :#line:366
                        OO0O0OO00OOO00O00 =OOOOO0000OO0OO0O0 ['user']['nickname']#line:367
                        print (f'【绑邀请码】:我的邀请人:{OO0O0OO00OOO00O00}')#line:368
                    else :#line:369
                        if OO0O0O00OOOOO000O .innerId !='0':#line:370
                            print ('【绑邀请码】:绑定邀请码')#line:371
                            O000O0O00000OO000 ={"innerId":OO0O0O00OOOOO000O .innerId }#line:372
                            O0OO000O0OO0OO00O =requests .request ('post',f'{host}/friends/my-invitation',headers =OO0OOOOOOOO00OOO0 ,data =O000O0O00000OO000 ).json ()#line:373
                            print (O0OO000O0OO0OO00O )#line:374
                        else :#line:375
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:376
        except Exception as O0O0OO000O00OO0O0 :#line:377
            print (O0O0OO000O00OO0O0 )#line:378
    def add_clover (OOOO0OO0OOOO00000 ):#line:382
        try :#line:383
            OO0OO0000OO0O00OO =f'__{timi_new()}'#line:384
            OOO00OOOO0O00O0OO ={'authorization':OOOO0OO0OOOO00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0000OO0O00OO ),'signstring':OO0OO0000OO0O00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:393
            OOO0O0O0000O0OOOO =requests .request ('get',f'{host}/assets/clovers',headers =OOO00OOOO0O00O0OO ).json ()#line:394
            if 'status'in OOO0O0O0000O0OOOO :#line:396
                if OOO0O0O0000O0OOOO ['status']==200 :#line:397
                    OOOOO000O000O00O0 =OOO0O0O0000O0OOOO ['data']['clover']#line:398
                    O00OOOOOOO0OO000O =OOO0O0O0000O0OOOO ['data']['used_clover']#line:399
                    OOOO00O000O00OO0O =float (OOOOO000O000O00O0 )-float (O00OOOOOOO0OO000O )#line:400
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O00OOOOOOO0OO000O}')#line:401
                    if OOOO00O000O00OO0O >1 :#line:402
                        OO0OO0000OO0O00OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOO00O000O00OO0O)}_{timi_new()}'#line:403
                        OOO00OOOO0O00O0OO ={'authorization':OOOO0OO0OOOO00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0000OO0O00OO ),'signstring':OO0OO0000OO0O00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:412
                        OOO0O000000OO00OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOO00O000O00OO0O )}#line:413
                        O0O00OO00OOO00OOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO00OOOO0O00O0OO ,data =OOO0O000000OO00OO ).json ()#line:414
                        if 'status'in O0O00OO00OOO00OOO :#line:416
                            if O0O00OO00OOO00OOO ['status']==200 :#line:417
                                print (f'【参与抽奖】:添加三叶草:{O0O00OO00OOO00OOO["data"]}丨数量:{OOOO00O000O00OO0O}')#line:418
            O0OOOO0O0O0O00O0O =requests .request ('get',f'{host}/lottery',headers =OOO00OOOO0O00O0OO ).json ()#line:419
            if 'status'in O0OOOO0O0O0O00O0O :#line:421
                if O0OOOO0O0O0O00O0O ['status']==200 :#line:422
                    OOO00O0000OOO0OOO =O0OOOO0O0O0O00O0O ['data'][0 ]['day_get_gold_quantity']#line:423
                    print (f'【参与抽奖】:预计每天中{OOO00O0000OOO0OOO[:6]}种子')#line:424
        except Exception as OO0OO0OO00O0O00O0 :#line:425
            print (OO0OO0OO00O0O00O0 )#line:426
    def energy (O00O0O0O0O0O0O000 ):#line:429
        O0OO0OOOOO0OOO0O0 =f'__{timi_new()}'#line:430
        O00O0OOOOO000O0O0 ={'authorization':O00O0O0O0O0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOOOO0OOO0O0 ),'signstring':O0OO0OOOOO0OOO0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:439
        OO0OO0O000O0OOOOO =requests .request ('get',f'{host}/energy/general',headers =O00O0OOOOO000O0O0 ).json ()#line:440
        if 'status'in OO0OO0O000O0OOOOO :#line:442
            if OO0OO0O000O0OOOOO ['status']==200 :#line:443
                OO0O0OOO00O00OOO0 =OO0OO0O000O0OOOOO ['data']['ordinary_water_consumptions']#line:444
                if float (OO0O0OOO00O00OOO0 )<80 :#line:445
                    OO00000OOO0OO0000 =99 -float (OO0O0OOO00O00OOO0 )#line:446
                    O00OOO0000OOOOO00 ={"fertilizer":str (OO00000OOO0OO0000 ).split ('.')[0 ]}#line:447
                    OOOOOOOOO00000OOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O00O0OOOOO000O0O0 ,data =O00OOO0000OOOOO00 ).json ()#line:448
                    if 'status'in OOOOOOOOO00000OOO :#line:450
                        if OOOOOOOOO00000OOO ['status']==200 :#line:451
                            print (f'【购买肥料】:{OOOOOOOOO00000OOO["message"]}')#line:452
                OOO0OOOOO0O0OO0O0 =OO0OO0O000O0OOOOO ['data']['ordinary_water_consumptions']#line:453
                if float (OOO0OOOOO0O0OO0O0 )<800 :#line:454
                    O0OO0O0O0OO0OO00O =999 -float (OOO0OOOOO0O0OO0O0 )#line:455
                    O0OOOOO00O0O0OOOO ={"water":str (O0OO0O0O0OO0OO00O ).split ('.')[0 ]}#line:456
                    OO00OOOOO0OOO00OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O00O0OOOOO000O0O0 ,data =O0OOOOO00O0O0OOOO ).json ()#line:457
                    if 'status'in OO00OOOOO0OOO00OO :#line:458
                        if OO00OOOOO0OOO00OO ['status']==200 :#line:459
                            print (f'【购买水滴】:{OO00OOOOO0OOO00OO["message"]}')#line:460
def version_of_the_validation ():#line:466
    return str ((61 -56 )/10 )#line:467
def gitee_validation ():#line:469
    try :#line:470
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:471
    except Exception as OOOO0OOO000OO0000 :#line:472
        sys .exit (0 )#line:473
def update_the_validation ():#line:479
    try :#line:480
        OOOO0000000OO00O0 =gitee_validation ()#line:481
        if version_of_the_validation ()<OOOO0000000OO00O0 ['CityEarth']['edition']:#line:482
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO0000000OO00O0["CityEarth"]["edition"]}   ❌')#line:483
            print (f'更新内容=>>{OOOO0000000OO00O0["CityEarth"]["content"]}   👍')#line:484
        else :#line:485
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO0000000OO00O0["CityEarth"]["edition"]}   ✅')#line:486
            print (f'更新内容=>> {OOOO0000000OO00O0["CityEarth"]["content"]}   👍')#line:487
    except Exception as O0O00OO000OOOOOOO :#line:488
        print (O0O00OO000OOOOOOO )#line:489
def os_qinglong ():#line:492
    if application in os .environ :#line:493
        O00OO00000OOO00O0 =os .environ [application ].split ('\n')#line:494
        if len (O00OO00000OOO00O0 )>0 :#line:495
            return O00OO00000OOO00O0 #line:496
        else :#line:497
            print (f"{application}变量未启用")#line:498
            print ('脚本退出')#line:499
            sys .exit (1 )#line:500
    else :#line:501
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:502
        return os_built ()#line:503
def os_built ():#line:506
    if token :#line:507
        O000OOOO0OOOO0O0O =token .split ('\n')#line:508
        if len (O000OOOO0OOOO0O0O )>0 :#line:509
            return O000OOOO0OOOO0O0O #line:510
    else :#line:511
        print (f"内置变量为空")#line:512
        print ('脚本结束')#line:513
        sys .exit (0 )#line:514
if __name__ =='__main__':#line:517
    start ()#line:518
