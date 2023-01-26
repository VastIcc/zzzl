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
        OOOOOOO0OOO00OO00 =os_qinglong ()#line:7
        print (f"==========共找到{len(OOOOOOO0OOO00OO00)}个账号==========")#line:8
        for OO00000OO0O00OO0O in OOOOOOO0OOO00OO00 :#line:9
            print (f"------------正在执行第{OOOOOOO0OOO00OO00.index(OO00000OO0O00OO0O) + 1}个账号------------")#line:10
            OOOOO0O000O00OO00 =CityEarth (OO00000OO0O00OO0O )#line:11
            if OOOOO0O000O00OO00 .base_info ():#line:13
                OOOOO0O000O00OO00 .friends_invitation ()#line:18
                OOOOO0O000O00OO00 .add_clover ()#line:20
                OOOOO0O000O00OO00 .energy ()#line:22
                OOOOO0O000O00OO00 .synthetic ()#line:24
                OOOOO0O000O00OO00 .propsraffle ()#line:26
                OOOOO0O000O00OO00 .crops_illustrated ()#line:28
            else :#line:29
                print ('token失效')#line:30
            time .sleep (time_xx )#line:32
    except Exception as O0O0OOO00OOO0OO00 :#line:33
        print (O0O0OOO00OOO0OO00 )#line:34
def sign (O0O000O00O0000000 ):#line:36
    O00OOOO00OOO0O000 =hashlib .md5 (O0O000O00O0000000 .encode ()).hexdigest ()#line:37
    O0O0O00O0O0OO0OOO ="scsc%^&*"+O00OOOO00OOO0O000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:38
    OOOO0O00O0O00O0OO =hashlib .md5 (O0O0O00O0O0OO0OOO .encode ()).hexdigest ()#line:39
    return OOOO0O00O0O00O0OO #line:40
def timi_new ():#line:42
    return str (int (time .time ()*1000 ))#line:43
class CityEarth :#line:46
    def __init__ (O0OO0O000O0O000O0 ,OOOO00000O00O000O ):#line:48
        try :#line:49
            O0OO0O000O0O000O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:50
            O0OO0O000O0O000O0 .token =OOOO00000O00O000O .split ('&')[0 ]#line:51
            O0OO0O000O0O000O0 .innerId =OOOO00000O00O000O .split ('&')[1 ]#line:52
        except Exception as OO0O0OO00O00OO00O :#line:53
            print ('变量格式错误')#line:54
    def base_info (OO00OOO0OO000OOO0 ):#line:57
        global level #line:58
        try :#line:59
            O0O00OOO00OO0O0OO =f'__{timi_new()}'#line:60
            O00O00OOO0OOO000O ={'authorization':OO00OOO0OO000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO00OO0O0OO ),'signstring':O0O00OOO00OO0O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:69
            O00OO00O0O00O00OO =requests .request ('get',f'{host}/user',headers =O00O00OOO0OOO000O ).json ()#line:70
            if 'status'in O00OO00O0O00O00OO :#line:71
                if O00OO00O0O00O00OO ['status']==200 :#line:72
                    O000OO0OO0OO0OO00 =O00OO00O0O00O00OO ['data']['nickname']#line:73
                    O000O0O0OO0000O00 =O00OO00O0O00O00OO ['data']['inner_id']#line:74
                    O0OOOO0O0O0OOO0O0 =O00OO00O0O00O00OO ['data']['assets']['gold']#line:75
                    level =O00OO00O0O00O00OO ['data']['level']#line:76
                    print (f'【账号信息】:昵称:{O000OO0OO0OO0OO00}丨ID:{str(O000O0O0OO0000O00)[:3] + "**"+ str(O000O0O0OO0000O00)[5:]}丨等级:{level}丨种子:{str(O0OOOO0O0O0OOO0O0).split(".")[0]}')#line:77
                if O00OO00O0O00O00OO ['status']==401 :#line:78
                    return False #line:79
                if O00OO00O0O00O00OO ['status']==500 :#line:80
                    return False #line:81
            return True #line:82
        except Exception as O000O0OO0000000O0 :#line:83
            print (O000O0OO0000000O0 )#line:84
    def crops_illustrated (OOOO0000OOOO0O00O ):#line:88
        O00OOOOOOO0O000O0 =f'__{timi_new()}'#line:89
        O0O00O000OOO00OOO ={'authorization':OOOO0000OOOO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOOOO0O000O0 ),'signstring':O00OOOOOOO0O000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:98
        O000OOOO000OOO00O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O00O000OOO00OOO ).json ()#line:99
        if 'status'in O000OOOO000OOO00O :#line:101
            if O000OOOO000OOO00O ['status']==200 :#line:102
                OO0OO0OOOO0OOOO00 =O000OOOO000OOO00O ['data'][0 ]['crops']#line:103
                for OOO0OO000O0O0000O in OO0OO0OOOO0OOOO00 :#line:104
                    if OOO0OO000O0O0000O ['ill_clover_award']:#line:105
                        if float (OOO0OO000O0O0000O ['ill_clover_award'])>1 :#line:106
                            if OOO0OO000O0O0000O ['is_finish']:#line:107
                                if not OOO0OO000O0O0000O ['is_getit']:#line:108
                                    O00OOOOOOO0O000O0 =f'_award_level={OOO0OO000O0O0000O["level"]}_{timi_new()}'#line:109
                                    O0O00O000OOO00OOO ={'authorization':OOOO0000OOOO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOOOO0O000O0 ),'signstring':O00OOOOOOO0O000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:118
                                    OO000O0OO0OOO0O00 ={"award_level":OOO0OO000O0O0000O ['level']}#line:119
                                    OO0OO0OO000O000O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O00O000OOO00OOO ,json =OO000O0OO0OOO0O00 ).json ()#line:120
                                    if 'status'in OO0OO0OO000O000O0 :#line:121
                                        if OO0OO0OO000O000O0 ['status']==200 :#line:122
                                            OOO00O0OOOOOOO0OO =OO0OO0OO000O000O0 ['data']['ill_clover_award']#line:123
                                            print (f'【图鉴奖励】:领取{OOO0OO000O0O0000O["crop_name"]}成就丨奖励{OOO00O0OOOOOOO0OO}叶子成功')#line:124
                                        if OO0OO0OO000O000O0 ['status']==500 :#line:125
                                            print (f'【图鉴奖励】:{OO0OO0OO000O000O0["message"]}')#line:126
    def watched_ad (OOOOO0OO0000000O0 ):#line:129
        OOO0O0OOOOO000OOO =f'__{timi_new()}'#line:130
        OO0OOOOOO000O000O ={'authorization':OOOOO0OO0000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OOOOO000OOO ),'signstring':OOO0O0OOOOO000OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:139
        O00OO00OO00O0OO00 =requests .request ('post',f'{host}/game/watched-ad',headers =OO0OOOOOO000O000O ).json ()#line:140
        print (O00OO00OO00O0OO00 )#line:141
    def user_ad (O00O0O000OOO0OOOO ):#line:147
        OOOOO0O00O00O000O =f'__{timi_new()}'#line:148
        OOOO000OOOO00OOOO ={'authorization':O00O0O000OOO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O00O00O000O ),'signstring':OOOOO0O00O00O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:157
        OOOOOO0OO00OO0O00 =requests .request ('get',f'{host}/user/ad',headers =OOOO000OOOO00OOOO ).json ()#line:158
        if 'status'in OOOOOO0OO00OO0O00 :#line:160
            if OOOOOO0OO00OO0O00 ['status']==200 :#line:161
                O000O0OOO000OOOO0 =OOOOOO0OO00OO0O00 ['data']['max_time']#line:162
                O0000OO00000O0OOO =OOOOOO0OO00OO0O00 ['data']['watch_time']#line:163
                O00O000O00O0O0OOO =OOOOOO0OO00OO0O00 ['data']['added_time']#line:164
                print (f'【获取种子】:获取种子剩余{O00O000O00O0O0OOO + O000O0OOO000OOOO0 - O0000OO00000O0OOO}次丨好友提供:{O00O000O00O0O0OOO}次')#line:165
                if O00O000O00O0O0OOO +O000O0OOO000OOOO0 -O0000OO00000O0OOO >0 :#line:166
                    time .sleep (random .randint (16 ,19 ))#line:167
                    OOOO00O00O00000O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOOO000OOOO00OOOO ).json ()#line:168
                    if 'status'in OOOO00O00O00000O0 :#line:170
                        if OOOO00O00O00000O0 ['status']==200 :#line:171
                            OOO0O0OOOOOO00O00 =OOOO00O00O00000O0 ['data']['silver']#line:172
                            print (f'【获取种子】:获得种子:{OOO0O0OOOOOO00O00}')#line:173
                            return True #line:174
                        if OOOO00O00O00000O0 ['status']==500 :#line:175
                            O0O0OO0OO0000OOO0 =OOOO00O00O00000O0 ['message']#line:176
                            print (f'【获取种子】:{O0O0OO0OO0000OOO0}')#line:177
                            return False #line:178
    def synthetic (O00000OOOO0OOOOOO ):#line:181
        global id ,g #line:182
        try :#line:183
            while True :#line:185
                O0OO0O0O0OO0O0OOO =f'__{timi_new()}'#line:186
                O0O0000O00OO0OO00 ={'authorization':O00000OOOO0OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O0OO0O0OOO ),'signstring':O0OO0O0O0OO0O0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:195
                O00O0OOO0O00O0O0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O0000O00OO0OO00 ).json ()#line:196
                if 'status'in O00O0OOO0O00O0O0O :#line:198
                    if O00O0OOO0O00O0O0O ['status']==200 :#line:199
                        OOO00OOO0O000O0O0 =O00O0OOO0O00O0O0O ['data']['cropList']#line:200
                        OO0O00O0O00O0O00O =O00O0OOO0O00O0O0O ['data']['gameCoreDataDBid']#line:201
                        O0OO0OOOO000000OO =0 #line:202
                        for O0O0O0O0O00OOO00O in OOO00OOO0O000O0O0 :#line:203
                            if not O0O0O0O0O00OOO00O :#line:204
                                OOO000O000OO000O0 =f'_crop_id={OO0O00O0O00O0O00O}&site={O0OO0OOOO000000OO}_{O00000OOOO0OOOOOO.time}'#line:205
                                O0000OOOOOOOOO0O0 ={'authorization':O00000OOOO0OOOOOO .token ,'timestamp':O00000OOOO0OOOOOO .time ,'sign':sign (OOO000O000OO000O0 ),'signstring':OOO000O000OO000O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
                                O00OOO0O0000O0OOO ={"site":O0OO0OOOO000000OO ,"crop_id":OO0O00O0O00O0O00O }#line:215
                                O00000OO0O0000000 =requests .request ('post',f'{host}/game/crops/buy',headers =O0000OOOOOOOOO0O0 ,data =O00OOO0O0000O0OOO ).json ()#line:216
                                if 'status'in O00000OO0O0000000 :#line:218
                                    if O00000OO0O0000000 ['status']==200 :#line:219
                                        if O00000OO0O0000000 ['message']=='种子数量不足':#line:220
                                            print (f'【购买合成】:{O00000OO0O0000000["message"]}')#line:221
                                            if not O00000OOOO0OOOOOO .user_ad ():#line:222
                                                return False #line:223
                                        print (f'【购买合成】:购买农作物,位置{O0OO0OOOO000000OO}')#line:224
                                    if O00000OO0O0000000 ['status']==500 :#line:225
                                        print (f'【购买合成】:{O00000OO0O0000000["message"]}')#line:226
                                        return False #line:227
                                time .sleep (random .randint (3 ,5 )/10 )#line:228
                            O0OO0OOOO000000OO +=1 #line:229
                        OO0OOOO0OO0OOOO00 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0000O00OO0OO00 ).json ()#line:230
                        OO00000O00OOOOOOO =OO0OOOO0OO0OOOO00 ['data']['cropList']#line:231
                        O0O0OOOO0OO00OOOO =False #line:232
                        for O0O0O0O0O00OOO00O in range (12 ):#line:233
                            id =OO00000O00OOOOOOO [O0O0O0O0O00OOO00O ]['level']#line:234
                            if id !=0 :#line:256
                                for O00OO0O0O0OOO0000 in range (11 ):#line:257
                                    O000O00O00OOO00OO =O00OO0O0O0OOO0000 +1 #line:258
                                    g =OO00000O00OOOOOOO [O000O00O00OOO00OO ]['level']#line:259
                                    if id ==g :#line:260
                                        O0000O0OOO0OOO0OO =O00OO0O0O0OOO0000 +2 #line:261
                                        if O0000O0OOO0OOO0OO ==O0O0O0O0O00OOO00O +1 :#line:262
                                            pass #line:263
                                        else :#line:264
                                            time .sleep (random .randint (3 ,5 )/10 )#line:265
                                            O000000O0000OOO00 =O0O0O0O0O00OOO00O +1 #line:266
                                            O00000OOO0OOO0O0O =f'_site={O000000O0000OOO00-1}&targetSite={O0000O0OOO0OOO0OO-1}_{timi_new()}'#line:269
                                            OO00OO0O0OO0OOOO0 ={'accept':'application/json, text/plain, */*','authorization':O00000OOOO0OOOOOO .token ,'timestamp':timi_new (),'sign':sign (O00000OOO0OOO0O0O ),'signstring':O00000OOO0OOO0O0O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:284
                                            O0O00OO0OO0O00O0O ={"site":int (O000000O0000OOO00 -1 ),"targetSite":int (O0000O0OOO0OOO0OO -1 )}#line:285
                                            O0O0O0OO00OOO0000 =requests .request ('post',f'{host}/game/crops/move',headers =OO00OO0O0OO0OOOO0 ,json =O0O00OO0OO0O00O0O ).json ()#line:286
                                            if 'status'in O0O0O0OO00OOO0000 :#line:287
                                                if O0O0O0OO00OOO0000 ['status']==200 :#line:288
                                                    pass #line:289
                                            print ('【购买合成】:',O000000O0000OOO00 ,O0000O0OOO0OOO0OO ,'合成成功')#line:291
                                            O0O0OOOO0OO00OOOO =True #line:292
                                    if O0O0OOOO0OO00OOOO :#line:293
                                        break #line:294
                                if O0O0OOOO0OO00OOOO :#line:295
                                    break #line:296
        except Exception as O0O0O0OO000OOO0O0 :#line:297
            O00000OOOO0OOOOOO .synthetic ()#line:298
    def propsraffle (O0000OO0O00OOOO0O ):#line:302
        try :#line:303
            while True :#line:304
                O00O00O00OOOO000O =f'__{timi_new()}'#line:305
                O00OOO000O0OO0000 ={'authorization':O0000OO0O00OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O00OOOO000O ),'signstring':O00O00O00OOOO000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:314
                O0O000OO0000O0000 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00OOO000O0OO0000 ).json ()#line:315
                if 'status'in O0O000OO0000O0000 :#line:317
                    if O0O000OO0000O0000 ['status']==200 :#line:318
                        O00OO00OOO00000O0 =O0O000OO0000O0000 ['data']['rows']#line:319
                        O0000OOOO00O0000O =O0O000OO0000O0000 ['data']['vstate']#line:320
                        if O00OO00OOO00000O0 ==5 or O00OO00OOO00000O0 ==6 or O00OO00OOO00000O0 ==7 :#line:321
                            O000OO0OO00O00000 =O0O000OO0000O0000 ['data']['silver']#line:322
                            print (f'【转盘抽奖】:获得种子:{O000OO0OO00O00000}')#line:323
                        if O00OO00OOO00000O0 ==1 or O00OO00OOO00000O0 ==2 or O00OO00OOO00000O0 ==3 :#line:324
                            OOO0OO0OO0O00OOOO =O0O000OO0000O0000 ['data']['clover']#line:325
                            print (f'【转盘抽奖】:获得三叶草:{OOO0OO0OO0O00OOOO}')#line:326
                        if O00OO00OOO00000O0 ==4 or O00OO00OOO00000O0 ==8 :#line:327
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:328
                        if O00OO00OOO00000O0 =='抽奖次数已用完':#line:332
                            if O0000OOOO00O0000O :#line:333
                                OO0OOOO0O0OO000OO =random .randint (160 ,190 )/10 #line:334
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{OO0OOOO0O0OO000OO}秒获取抽奖机会')#line:335
                                time .sleep (OO0OOOO0O0OO000OO )#line:336
                                OOO00O00O00OOO0OO =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O00OOO000O0OO0000 ).json ()#line:337
                                if 'status'in OOO00O00O00OOO0OO :#line:339
                                    if OOO00O00O00OOO0OO ['status']==200 :#line:340
                                        print (f'【转盘抽奖】:{OOO00O00O00OOO0OO["message"]}')#line:341
                                    if OOO00O00O00OOO0OO ['status']==500 :#line:342
                                        print (f'【转盘抽奖】:{OOO00O00O00OOO0OO["message"]}')#line:343
                                        break #line:344
                                time .sleep (random .randint (10 ,15 )/10 )#line:345
                            else :#line:346
                                break #line:347
                time .sleep (random .randint (8 ,15 )/10 )#line:348
        except Exception as O00OO000000O0O000 :#line:349
            print (O00OO000000O0O000 )#line:350
    def friends_invitation (OO0O0000O000O0O00 ):#line:353
        try :#line:354
            OO0000OOOO00O0O0O =f'__{timi_new()}'#line:355
            O0O0O0O00000OOO0O ={'authorization':OO0O0000O000O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOOO00O0O0O ),'signstring':OO0000OOOO00O0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:364
            O0O0O00OOOOOOOOO0 =requests .request ('get',f'{host}/friends',headers =O0O0O0O00000OOO0O ).json ()#line:365
            if 'status'in O0O0O00OOOOOOOOO0 :#line:366
                if O0O0O00OOOOOOOOO0 ['status']==200 :#line:367
                    O0O0O00OO00OO0O0O =O0O0O00OOOOOOOOO0 ['data']['myInviteter']#line:368
                    if O0O0O00OO00OO0O0O :#line:369
                        O00O00OO00O00O00O =O0O0O00OO00OO0O0O ['user']['nickname']#line:370
                        print (f'【绑邀请码】:我的邀请人:{O00O00OO00O00O00O}')#line:371
                    else :#line:372
                        if OO0O0000O000O0O00 .innerId !='0':#line:373
                            print ('【绑邀请码】:绑定邀请码')#line:374
                            OO00OOOOO000000O0 ={"innerId":OO0O0000O000O0O00 .innerId }#line:375
                            O00OO0O0000OO0OO0 =requests .request ('post',f'{host}/friends/my-invitation',headers =O0O0O0O00000OOO0O ,data =OO00OOOOO000000O0 ).json ()#line:376
                            print (O00OO0O0000OO0OO0 )#line:377
                        else :#line:378
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:379
        except Exception as O0OOO0OO00O0O00OO :#line:380
            print (O0OOO0OO00O0O00OO )#line:381
    def add_clover (O00O0OO0OOO0O000O ):#line:385
        try :#line:386
            OOO0OOOO0OO0OO0OO =f'__{timi_new()}'#line:387
            O00OO00O000O0OO0O ={'authorization':O00O0OO0OOO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOO0OO0OO0OO ),'signstring':OOO0OOOO0OO0OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:396
            O0OO00000000O0O0O =requests .request ('get',f'{host}/assets/clovers',headers =O00OO00O000O0OO0O ).json ()#line:397
            if 'status'in O0OO00000000O0O0O :#line:399
                if O0OO00000000O0O0O ['status']==200 :#line:400
                    O000000OOO0O000O0 =O0OO00000000O0O0O ['data']['clover']#line:401
                    O000O0O00O00O0OO0 =O0OO00000000O0O0O ['data']['used_clover']#line:402
                    OOOO0O0O00O000O0O =float (O000000OOO0O000O0 )-float (O000O0O00O00O0OO0 )#line:403
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O000O0O00O00O0OO0}')#line:404
                    if OOOO0O0O00O000O0O >1 :#line:405
                        OOO0OOOO0OO0OO0OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOO0O0O00O000O0O)}_{timi_new()}'#line:406
                        O00OO00O000O0OO0O ={'authorization':O00O0OO0OOO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOO0OO0OO0OO ),'signstring':OOO0OOOO0OO0OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:415
                        O0O00O0O00OOOO0OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOO0O0O00O000O0O )}#line:416
                        O000000OOO0OO0O0O =requests .request ('post',f'{host}/lottery/add-stake',headers =O00OO00O000O0OO0O ,data =O0O00O0O00OOOO0OO ).json ()#line:417
                        if 'status'in O000000OOO0OO0O0O :#line:419
                            if O000000OOO0OO0O0O ['status']==200 :#line:420
                                print (f'【参与抽奖】:添加三叶草:{O000000OOO0OO0O0O["data"]}丨数量:{OOOO0O0O00O000O0O}')#line:421
            O0O0OO0O0OO00O0O0 =requests .request ('get',f'{host}/lottery',headers =O00OO00O000O0OO0O ).json ()#line:422
            if 'status'in O0O0OO0O0OO00O0O0 :#line:424
                if O0O0OO0O0OO00O0O0 ['status']==200 :#line:425
                    O00O000O0O0OO0OO0 =O0O0OO0O0OO00O0O0 ['data'][0 ]['day_get_gold_quantity']#line:426
                    print (f'【参与抽奖】:预计每天中{O00O000O0O0OO0OO0[:6]}种子')#line:427
        except Exception as OO0O000OO00O00O0O :#line:428
            print (OO0O000OO00O00O0O )#line:429
    def energy (OO00000000OOO0O0O ):#line:432
        O00O000O00O00O0O0 =f'__{timi_new()}'#line:433
        O0OO0000O000OOOO0 ={'authorization':OO00000000OOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000O00O00O0O0 ),'signstring':O00O000O00O00O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:442
        OO0000O0OOOO0O000 =requests .request ('get',f'{host}/energy/general',headers =O0OO0000O000OOOO0 ).json ()#line:443
        if 'status'in OO0000O0OOOO0O000 :#line:445
            if OO0000O0OOOO0O000 ['status']==200 :#line:446
                O0O00O000O000OO00 =OO0000O0OOOO0O000 ['data']['ordinary_water_consumptions']#line:447
                if float (O0O00O000O000OO00 )<80 :#line:448
                    O0OOOO00O0O00O0OO =99 -float (O0O00O000O000OO00 )#line:449
                    O0O00O0OOO0O00OOO ={"fertilizer":str (O0OOOO00O0O00O0OO ).split ('.')[0 ]}#line:450
                    O0OO00OO0O0OO0O0O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0OO0000O000OOOO0 ,data =O0O00O0OOO0O00OOO ).json ()#line:451
                    if 'status'in O0OO00OO0O0OO0O0O :#line:453
                        if O0OO00OO0O0OO0O0O ['status']==200 :#line:454
                            print (f'【购买肥料】:{O0OO00OO0O0OO0O0O["message"]}')#line:455
                OO00O00O0O00O0O00 =OO0000O0OOOO0O000 ['data']['ordinary_water_consumptions']#line:456
                if float (OO00O00O0O00O0O00 )<800 :#line:457
                    OOOO0000OO0O00000 =999 -float (OO00O00O0O00O0O00 )#line:458
                    OOO0O0OOOOOO00OOO ={"water":str (OOOO0000OO0O00000 ).split ('.')[0 ]}#line:459
                    O0O000O000OOO00OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0OO0000O000OOOO0 ,data =OOO0O0OOOOOO00OOO ).json ()#line:460
                    if 'status'in O0O000O000OOO00OO :#line:461
                        if O0O000O000OOO00OO ['status']==200 :#line:462
                            print (f'【购买水滴】:{O0O000O000OOO00OO["message"]}')#line:463
def version_of_the_validation ():#line:469
    return str ((61 -56 )/10 )#line:470
def gitee_validation ():#line:472
    try :#line:473
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:474
    except Exception as OOO00OOO00O000000 :#line:475
        sys .exit (0 )#line:476
def update_the_validation ():#line:482
    try :#line:483
        OO0O000O00000OOO0 =gitee_validation ()#line:484
        if version_of_the_validation ()<OO0O000O00000OOO0 ['CityEarth']['edition']:#line:485
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O000O00000OOO0["CityEarth"]["edition"]}   ❌')#line:486
            print (f'更新内容=>>{OO0O000O00000OOO0["CityEarth"]["content"]}   👍')#line:487
        else :#line:488
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O000O00000OOO0["CityEarth"]["edition"]}   ✅')#line:489
            print (f'更新内容=>> {OO0O000O00000OOO0["CityEarth"]["content"]}   👍')#line:490
    except Exception as O0O0OO000OOO00000 :#line:491
        print (O0O0OO000OOO00000 )#line:492
def os_qinglong ():#line:495
    if application in os .environ :#line:496
        O0000O000OO0OOO00 =os .environ [application ].split ('\n')#line:497
        if len (O0000O000OO0OOO00 )>0 :#line:498
            return O0000O000OO0OOO00 #line:499
        else :#line:500
            print (f"{application}变量未启用")#line:501
            print ('脚本退出')#line:502
            sys .exit (1 )#line:503
    else :#line:504
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:505
        return os_built ()#line:506
def os_built ():#line:509
    if token :#line:510
        OOOO0O0OOOO0OOO0O =token .split ('\n')#line:511
        if len (OOOO0O0OOOO0OOO0O )>0 :#line:512
            return OOOO0O0OOOO0OOO0O #line:513
    else :#line:514
        print (f"内置变量为空")#line:515
        print ('脚本结束')#line:516
        sys .exit (0 )#line:517
if __name__ =='__main__':#line:520
    start ()#line:521
