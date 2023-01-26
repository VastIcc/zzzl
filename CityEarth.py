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
项目地址  微信打开  http://share.sc19319.com/scsc/1932634
apk下载地址     https://sc19319.oss-cn-hangzhou.aliyuncs.com/scsc/test/1.9.3.1.S9.apk
抓取  http://test.scsc.sc19319.com 的authorization值
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
        O00000O00O0OO000O =os_qinglong ()#line:7
        print (f"==========共找到{len(O00000O00O0OO000O)}个账号==========")#line:8
        for OOO0O00O00OOO0O0O in O00000O00O0OO000O :#line:9
            print (f"------------正在执行第{O00000O00O0OO000O.index(OOO0O00O00OOO0O0O) + 1}个账号------------")#line:10
            O000000OO0O0OO0OO =CityEarth (OOO0O00O00OOO0O0O )#line:11
            if O000000OO0O0OO0OO .base_info ():#line:13
                O000000OO0O0OO0OO .friends_invitation ()#line:17
                O000000OO0O0OO0OO .add_clover ()#line:19
                O000000OO0O0OO0OO .energy ()#line:21
                O000000OO0O0OO0OO .synthetic ()#line:23
                O000000OO0O0OO0OO .propsraffle ()#line:25
                O000000OO0O0OO0OO .crops_illustrated ()#line:27
            else :#line:28
                print ('token失效')#line:29
            time .sleep (time_xx )#line:31
    except Exception as O0O00O000O0O00O0O :#line:32
        print (O0O00O000O0O00O0O )#line:33
def sign (OO0OOO0000000OO0O ):#line:35
    O000000O000O00OOO =hashlib .md5 (OO0OOO0000000OO0O .encode ()).hexdigest ()#line:36
    O0OO00OOO00OOO0O0 ="scsc%^&*"+O000000O000O00OOO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:37
    O0O00O0O0OO0O0OO0 =hashlib .md5 (O0OO00OOO00OOO0O0 .encode ()).hexdigest ()#line:38
    return O0O00O0O0OO0O0OO0 #line:39
def timi_new ():#line:41
    return str (int (time .time ()*1000 ))#line:42
class CityEarth :#line:45
    def __init__ (O00OOO0OO0OOO0OO0 ,OO000OO0OO0OO000O ):#line:47
        try :#line:48
            O00OOO0OO0OOO0OO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:49
            O00OOO0OO0OOO0OO0 .token =OO000OO0OO0OO000O .split ('&')[0 ]#line:50
            O00OOO0OO0OOO0OO0 .innerId =OO000OO0OO0OO000O .split ('&')[1 ]#line:51
        except Exception as O0000O000OOOOO00O :#line:52
            print ('变量格式错误')#line:53
    def base_info (OO00000OOOO0O0O0O ):#line:56
        global level #line:57
        try :#line:58
            O00000OOOOOOOO00O =f'__{timi_new()}'#line:59
            O0OO0OO00OOOO0OO0 ={'authorization':OO00000OOOO0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOOOOOOO00O ),'signstring':O00000OOOOOOOO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:68
            OO0O0OO00OOOOOOOO =requests .request ('get',f'{host}/user',headers =O0OO0OO00OOOO0OO0 ).json ()#line:69
            if 'status'in OO0O0OO00OOOOOOOO :#line:70
                if OO0O0OO00OOOOOOOO ['status']==200 :#line:71
                    OOOO00OO0O0O0OO00 =OO0O0OO00OOOOOOOO ['data']['nickname']#line:72
                    O0O0OOOOO0OOO0O0O =OO0O0OO00OOOOOOOO ['data']['inner_id']#line:73
                    O00OOOO00OO0000OO =OO0O0OO00OOOOOOOO ['data']['assets']['gold']#line:74
                    level =OO0O0OO00OOOOOOOO ['data']['level']#line:75
                    print (f'【账号信息】:昵称:{OOOO00OO0O0O0OO00}丨ID:{str(O0O0OOOOO0OOO0O0O)[:3] + "**"+ str(O0O0OOOOO0OOO0O0O)[5:]}丨农作物等级:{level}丨金种子:{str(O00OOOO00OO0000OO).split(".")[0]}')#line:76
                if OO0O0OO00OOOOOOOO ['status']==401 :#line:77
                    return False #line:78
                if OO0O0OO00OOOOOOOO ['status']==500 :#line:79
                    return False #line:80
            return True #line:81
        except Exception as O00O000OOO00OOO00 :#line:82
            print (O00O000OOO00OOO00 )#line:83
    def crops_illustrated (O00O0O000O0000O00 ):#line:87
        OO0OO0OO0O0OOOOOO =f'__{timi_new()}'#line:88
        O00O0O0OO000O0OOO ={'authorization':O00O0O000O0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO0O0OOOOOO ),'signstring':OO0OO0OO0O0OOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:97
        OO00O0OOOOOO0O00O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00O0O0OO000O0OOO ).json ()#line:98
        if 'status'in OO00O0OOOOOO0O00O :#line:100
            if OO00O0OOOOOO0O00O ['status']==200 :#line:101
                O0000OO000000OO0O =OO00O0OOOOOO0O00O ['data'][0 ]['crops']#line:102
                for O00000O00O0O00000 in O0000OO000000OO0O :#line:103
                    if O00000O00O0O00000 ['ill_clover_award']:#line:104
                        if float (O00000O00O0O00000 ['ill_clover_award'])>1 :#line:105
                            if O00000O00O0O00000 ['is_finish']:#line:106
                                if not O00000O00O0O00000 ['is_getit']:#line:107
                                    OO0OO0OO0O0OOOOOO =f'_award_level={O00000O00O0O00000["level"]}_{timi_new()}'#line:108
                                    O00O0O0OO000O0OOO ={'authorization':O00O0O000O0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO0O0OOOOOO ),'signstring':OO0OO0OO0O0OOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:117
                                    OOOO0O000OOO0O0OO ={"award_level":O00000O00O0O00000 ['level']}#line:118
                                    O00O0OO000000O00O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00O0O0OO000O0OOO ,json =OOOO0O000OOO0O0OO ).json ()#line:119
                                    if 'status'in O00O0OO000000O00O :#line:120
                                        if O00O0OO000000O00O ['status']==200 :#line:121
                                            OOO00000OO0OO00O0 =O00O0OO000000O00O ['data']['ill_clover_award']#line:122
                                            print (f'【图鉴奖励】:领取{O00000O00O0O00000["crop_name"]}成就丨奖励{OOO00000OO0OO00O0}种子成功')#line:123
                                        if O00O0OO000000O00O ['status']==500 :#line:124
                                            print (f'【图鉴奖励】:{O00O0OO000000O00O["message"]}')#line:125
    def watched_ad (OO00OOOO000000O00 ):#line:128
        O0O0O0OOOOOOO000O =f'__{timi_new()}'#line:129
        OOOO0O0000000OO0O ={'authorization':OO00OOOO000000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOOOOO000O ),'signstring':O0O0O0OOOOOOO000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:138
        O0OO0OOO0O000OO00 =requests .request ('post',f'{host}/game/watched-ad',headers =OOOO0O0000000OO0O ).json ()#line:139
        print (O0OO0OOO0O000OO00 )#line:140
    def user_ad (OO0000OO0O000O0O0 ):#line:146
        O000OOOOOOO0OO000 =f'__{timi_new()}'#line:147
        OO00OOOOO0O000O0O ={'authorization':OO0000OO0O000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOOOO0OO000 ),'signstring':O000OOOOOOO0OO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:156
        OO0O0OOO00OO00O0O =requests .request ('get',f'{host}/user/ad',headers =OO00OOOOO0O000O0O ).json ()#line:157
        if 'status'in OO0O0OOO00OO00O0O :#line:159
            if OO0O0OOO00OO00O0O ['status']==200 :#line:160
                O000O0OOOO00000O0 =OO0O0OOO00OO00O0O ['data']['max_time']#line:161
                OO0O00000O000OO00 =OO0O0OOO00OO00O0O ['data']['watch_time']#line:162
                O000OOOOO000O0OOO =OO0O0OOO00OO00O0O ['data']['added_time']#line:163
                print (f'【获取种子】:获取种子剩余{O000OOOOO000O0OOO + O000O0OOOO00000O0 - OO0O00000O000OO00}次丨好友提供:{O000OOOOO000O0OOO}次')#line:164
                if O000OOOOO000O0OOO +O000O0OOOO00000O0 -OO0O00000O000OO00 >0 :#line:165
                    time .sleep (random .randint (16 ,19 ))#line:166
                    O0OO00O00OOOO000O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO00OOOOO0O000O0O ).json ()#line:167
                    if 'status'in O0OO00O00OOOO000O :#line:169
                        if O0OO00O00OOOO000O ['status']==200 :#line:170
                            O0OOOOOOOOOOOO0O0 =O0OO00O00OOOO000O ['data']['silver']#line:171
                            print (f'【获取种子】:获得种子:{O0OOOOOOOOOOOO0O0}')#line:172
                            return True #line:173
                        if O0OO00O00OOOO000O ['status']==500 :#line:174
                            O0O0OO0OO0O0OOO0O =O0OO00O00OOOO000O ['message']#line:175
                            print (f'【获取种子】:{O0O0OO0OO0O0OOO0O}')#line:176
                            return False #line:177
    def synthetic (OOO0OO00OO0OOO0O0 ):#line:180
        global id ,g #line:181
        try :#line:182
            while True :#line:184
                O000OO000OO0O0O00 =f'__{timi_new()}'#line:185
                OO0OOOOOO000000OO ={'authorization':OOO0OO00OO0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO000OO0O0O00 ),'signstring':O000OO000OO0O0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:194
                OO00O0O00O0OOO0OO =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOOOOO000000OO ).json ()#line:195
                if 'status'in OO00O0O00O0OOO0OO :#line:197
                    if OO00O0O00O0OOO0OO ['status']==200 :#line:198
                        O00O0O00OOOOOOO00 =OO00O0O00O0OOO0OO ['data']['cropList']#line:199
                        OO00O00000O0O0OOO =OO00O0O00O0OOO0OO ['data']['gameCoreDataDBid']#line:200
                        O00000O000O0O00OO =0 #line:201
                        for O0OOO0OOOO0000O00 in O00O0O00OOOOOOO00 :#line:202
                            if not O0OOO0OOOO0000O00 :#line:203
                                O0000OO000OOO0O0O =f'_crop_id={OO00O00000O0O0OOO}&site={O00000O000O0O00OO}_{OOO0OO00OO0OOO0O0.time}'#line:204
                                O0O00OO0OO0OOOOOO ={'authorization':OOO0OO00OO0OOO0O0 .token ,'timestamp':OOO0OO00OO0OOO0O0 .time ,'sign':sign (O0000OO000OOO0O0O ),'signstring':O0000OO000OOO0O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:213
                                O0000O00O00OO0O0O ={"site":O00000O000O0O00OO ,"crop_id":OO00O00000O0O0OOO }#line:214
                                OOOOO0OOO00OO00O0 =requests .request ('post',f'{host}/game/crops/buy',headers =O0O00OO0OO0OOOOOO ,data =O0000O00O00OO0O0O ).json ()#line:215
                                if 'status'in OOOOO0OOO00OO00O0 :#line:217
                                    if OOOOO0OOO00OO00O0 ['status']==200 :#line:218
                                        if OOOOO0OOO00OO00O0 ['message']=='种子数量不足':#line:219
                                            print (f'【购买合成】:{OOOOO0OOO00OO00O0["message"]}')#line:220
                                            if not OOO0OO00OO0OOO0O0 .user_ad ():#line:221
                                                return False #line:222
                                        print (f'【购买合成】:购买农作物,位置{O00000O000O0O00OO}')#line:223
                                    if OOOOO0OOO00OO00O0 ['status']==500 :#line:224
                                        print (f'【购买合成】:{OOOOO0OOO00OO00O0["message"]}')#line:225
                                        return False #line:226
                                time .sleep (random .randint (3 ,5 )/10 )#line:227
                            O00000O000O0O00OO +=1 #line:228
                        OOO000O0OO000O000 =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOOOOO000000OO ).json ()#line:229
                        O0O0O00O00OO0OO00 =OOO000O0OO000O000 ['data']['cropList']#line:230
                        OO0O0O0OOO0OOOO00 =False #line:231
                        for O0OOO0OOOO0000O00 in range (12 ):#line:232
                            id =O0O0O00O00OO0OO00 [O0OOO0OOOO0000O00 ]['level']#line:233
                            if id !=0 :#line:255
                                for O00O00OOOOO0OO0OO in range (11 ):#line:256
                                    OOO00O000OO00000O =O00O00OOOOO0OO0OO +1 #line:257
                                    g =O0O0O00O00OO0OO00 [OOO00O000OO00000O ]['level']#line:258
                                    if id ==g :#line:259
                                        O00O0O00O0O000000 =O00O00OOOOO0OO0OO +2 #line:260
                                        if O00O0O00O0O000000 ==O0OOO0OOOO0000O00 +1 :#line:261
                                            pass #line:262
                                        else :#line:263
                                            time .sleep (random .randint (3 ,5 )/10 )#line:264
                                            OOOO000OOO0OO0OO0 =O0OOO0OOOO0000O00 +1 #line:265
                                            O00OO000OOO000O00 =f'_site={OOOO000OOO0OO0OO0-1}&targetSite={O00O0O00O0O000000-1}_{timi_new()}'#line:268
                                            OO0OO00OOO00OOOOO ={'accept':'application/json, text/plain, */*','authorization':OOO0OO00OO0OOO0O0 .token ,'timestamp':timi_new (),'sign':sign (O00OO000OOO000O00 ),'signstring':O00OO000OOO000O00 ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:283
                                            OOOOOO000O00000O0 ={"site":int (OOOO000OOO0OO0OO0 -1 ),"targetSite":int (O00O0O00O0O000000 -1 )}#line:284
                                            O0OOOO00O0O0O000O =requests .request ('post',f'{host}/game/crops/move',headers =OO0OO00OOO00OOOOO ,json =OOOOOO000O00000O0 ).json ()#line:285
                                            if 'status'in O0OOOO00O0O0O000O :#line:286
                                                if O0OOOO00O0O0O000O ['status']==200 :#line:287
                                                    pass #line:288
                                            print ('【购买合成】:',OOOO000OOO0OO0OO0 ,O00O0O00O0O000000 ,'合成成功')#line:290
                                            OO0O0O0OOO0OOOO00 =True #line:291
                                    if OO0O0O0OOO0OOOO00 :#line:292
                                        break #line:293
                                if OO0O0O0OOO0OOOO00 :#line:294
                                    break #line:295
        except Exception as OO0O000OO00O00OOO :#line:296
            OOO0OO00OO0OOO0O0 .synthetic ()#line:297
    def propsraffle (O00O00000OO00O000 ):#line:301
        try :#line:302
            while True :#line:303
                O0000OOO0OO000OOO =f'__{timi_new()}'#line:304
                OOO0000OOO0O000OO ={'authorization':O00O00000OO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOO0OO000OOO ),'signstring':O0000OOO0OO000OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:313
                O00O0OOOOOO00OOO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO0000OOO0O000OO ).json ()#line:314
                if 'status'in O00O0OOOOOO00OOO0 :#line:316
                    if O00O0OOOOOO00OOO0 ['status']==200 :#line:317
                        O00OOO000O0O00OO0 =O00O0OOOOOO00OOO0 ['data']['rows']#line:318
                        O00O0O00O0O0OOOO0 =O00O0OOOOOO00OOO0 ['data']['vstate']#line:319
                        if O00OOO000O0O00OO0 ==5 or O00OOO000O0O00OO0 ==6 or O00OOO000O0O00OO0 ==7 :#line:320
                            O00000OOO0OO00000 =O00O0OOOOOO00OOO0 ['data']['silver']#line:321
                            print (f'【转盘抽奖】:获得种子:{O00000OOO0OO00000}')#line:322
                        if O00OOO000O0O00OO0 ==1 or O00OOO000O0O00OO0 ==2 or O00OOO000O0O00OO0 ==3 :#line:323
                            OO0OOO0O00OO0000O =O00O0OOOOOO00OOO0 ['data']['clover']#line:324
                            print (f'【转盘抽奖】:获得三叶草:{OO0OOO0O00OO0000O}')#line:325
                        if O00OOO000O0O00OO0 ==4 or O00OOO000O0O00OO0 ==8 :#line:326
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:327
                        if O00OOO000O0O00OO0 =='抽奖次数已用完':#line:331
                            if O00O0O00O0O0OOOO0 :#line:332
                                O0000O0O0000OOO0O =random .randint (160 ,190 )/10 #line:333
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{O0000O0O0000OOO0O}秒获取抽奖机会')#line:334
                                time .sleep (O0000O0O0000OOO0O )#line:335
                                OOO00000O0O0O0O0O =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OOO0000OOO0O000OO ).json ()#line:336
                                if 'status'in OOO00000O0O0O0O0O :#line:338
                                    if OOO00000O0O0O0O0O ['status']==200 :#line:339
                                        print (f'【转盘抽奖】:{OOO00000O0O0O0O0O["message"]}')#line:340
                                    if OOO00000O0O0O0O0O ['status']==500 :#line:341
                                        print (f'【转盘抽奖】:{OOO00000O0O0O0O0O["message"]}')#line:342
                                        break #line:343
                                time .sleep (random .randint (10 ,15 )/10 )#line:344
                            else :#line:345
                                break #line:346
                time .sleep (random .randint (8 ,15 )/10 )#line:347
        except Exception as OO000OOO00OO0OO00 :#line:348
            print (OO000OOO00OO0OO00 )#line:349
    def friends_invitation (O0000OO0O0OO00OOO ):#line:352
        try :#line:353
            OO00000O0OOOOO0O0 =f'__{timi_new()}'#line:354
            OOO000OO0O000OO00 ={'authorization':O0000OO0O0OO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000O0OOOOO0O0 ),'signstring':OO00000O0OOOOO0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:363
            O00O000OO00OO0O0O =requests .request ('get',f'{host}/friends',headers =OOO000OO0O000OO00 ).json ()#line:364
            if 'status'in O00O000OO00OO0O0O :#line:365
                if O00O000OO00OO0O0O ['status']==200 :#line:366
                    OOOO000000OOO0OO0 =O00O000OO00OO0O0O ['data']['myInviteter']#line:367
                    if OOOO000000OOO0OO0 :#line:368
                        O00O00000O0O0O0O0 =OOOO000000OOO0OO0 ['user']['nickname']#line:369
                        print (f'【绑邀请码】:我的邀请人:{O00O00000O0O0O0O0}')#line:370
                    else :#line:371
                        if O0000OO0O0OO00OOO .innerId !='0':#line:372
                            print ('【绑邀请码】:绑定邀请码')#line:373
                            OOOOO0O0O00OOOOO0 ={"innerId":O0000OO0O0OO00OOO .innerId }#line:374
                            O00000O00OO000000 =requests .request ('post',f'{host}/friends/my-invitation',headers =OOO000OO0O000OO00 ,data =OOOOO0O0O00OOOOO0 ).json ()#line:375
                            print (O00000O00OO000000 )#line:376
                        else :#line:377
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:378
        except Exception as O000O0OO000000O0O :#line:379
            print (O000O0OO000000O0O )#line:380
    def add_clover (OOO00O0OO00OO0O00 ):#line:384
        try :#line:385
            O00O0OO000OO00O0O =f'__{timi_new()}'#line:386
            O0O0O00OO0O00O000 ={'authorization':OOO00O0OO00OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO000OO00O0O ),'signstring':O00O0OO000OO00O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            O000OOO0O0O0O00OO =requests .request ('get',f'{host}/assets/clovers',headers =O0O0O00OO0O00O000 ).json ()#line:396
            if 'status'in O000OOO0O0O0O00OO :#line:398
                if O000OOO0O0O0O00OO ['status']==200 :#line:399
                    OOOOO0000O0O0OOO0 =O000OOO0O0O0O00OO ['data']['clover']#line:400
                    OO0OO0O0O0O0O0000 =O000OOO0O0O0O00OO ['data']['used_clover']#line:401
                    O0O00O00O0OO000OO =float (OOOOO0000O0O0OOO0 )-float (OO0OO0O0O0O0O0000 )#line:402
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OO0OO0O0O0O0O0000}')#line:403
                    if O0O00O00O0OO000OO >1 :#line:404
                        O00O0OO000OO00O0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O00O00O0OO000OO)}_{timi_new()}'#line:405
                        O0O0O00OO0O00O000 ={'authorization':OOO00O0OO00OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO000OO00O0O ),'signstring':O00O0OO000OO00O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:414
                        O00000O0O0OO0OO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O00O00O0OO000OO )}#line:415
                        O00O00OOO0O00O000 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O0O00OO0O00O000 ,data =O00000O0O0OO0OO00 ).json ()#line:416
                        if 'status'in O00O00OOO0O00O000 :#line:418
                            if O00O00OOO0O00O000 ['status']==200 :#line:419
                                print (f'【参与抽奖】:添加三叶草:{O00O00OOO0O00O000["data"]}丨数量:{O0O00O00O0OO000OO}')#line:420
        except Exception as OOOOO0OOO0OOOO0O0 :#line:421
            print (OOOOO0OOO0OOOO0O0 )#line:422
    def energy (OOO0OO0OOOOO00000 ):#line:425
        OOOOOOO0O0O0O0O00 =f'__{timi_new()}'#line:426
        OOO0OOOO00O00O0OO ={'authorization':OOO0OO0OOOOO00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0O0O0O0O00 ),'signstring':OOOOOOO0O0O0O0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:435
        OOO00000OOO0O0O00 =requests .request ('get',f'{host}/energy/general',headers =OOO0OOOO00O00O0OO ).json ()#line:436
        if 'status'in OOO00000OOO0O0O00 :#line:438
            if OOO00000OOO0O0O00 ['status']==200 :#line:439
                OO0OO000OOOO00000 =OOO00000OOO0O0O00 ['data']['ordinary_water_consumptions']#line:440
                if float (OO0OO000OOOO00000 )<80 :#line:441
                    O0O00OOOO0OO00000 =99 -float (OO0OO000OOOO00000 )#line:442
                    OO00O00OO0O0OOO0O ={"fertilizer":str (O0O00OOOO0OO00000 ).split ('.')[0 ]}#line:443
                    OO000O000O0O0OO0O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO0OOOO00O00O0OO ,data =OO00O00OO0O0OOO0O ).json ()#line:444
                    if 'status'in OO000O000O0O0OO0O :#line:446
                        if OO000O000O0O0OO0O ['status']==200 :#line:447
                            print (f'【购买肥料】:{OO000O000O0O0OO0O["message"]}')#line:448
                OO000O0O0OO0OO00O =OOO00000OOO0O0O00 ['data']['ordinary_water_consumptions']#line:449
                if float (OO000O0O0OO0OO00O )<800 :#line:450
                    OOO000OOOOO000OOO =999 -float (OO000O0O0OO0OO00O )#line:451
                    OOO0O0000O0OO0O00 ={"water":str (OOO000OOOOO000OOO ).split ('.')[0 ]}#line:452
                    OO0O0OOOOOO0O0O00 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO0OOOO00O00O0OO ,data =OOO0O0000O0OO0O00 ).json ()#line:453
                    if 'status'in OO0O0OOOOOO0O0O00 :#line:454
                        if OO0O0OOOOOO0O0O00 ['status']==200 :#line:455
                            print (f'【购买水滴】:{OO0O0OOOOOO0O0O00["message"]}')#line:456
def version_of_the_validation ():#line:462
    return str ((61 -56 )/10 )#line:463
def gitee_validation ():#line:465
    try :#line:466
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:467
    except Exception as O0O00OOOOO0O0O000 :#line:468
        sys .exit (0 )#line:469
def update_the_validation ():#line:475
    try :#line:476
        OO0O00O0OOOOO0OO0 =gitee_validation ()#line:477
        if version_of_the_validation ()<OO0O00O0OOOOO0OO0 ['CityEarth']['edition']:#line:478
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O00O0OOOOO0OO0["CityEarth"]["edition"]}   ❌')#line:479
            print (f'更新内容=>>{OO0O00O0OOOOO0OO0["CityEarth"]["content"]}   👍')#line:480
        else :#line:481
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O00O0OOOOO0OO0["CityEarth"]["edition"]}   ✅')#line:482
            print (f'更新内容=>> {OO0O00O0OOOOO0OO0["CityEarth"]["content"]}   👍')#line:483
    except Exception as O00O0OOO0O00O00O0 :#line:484
        print (O00O0OOO0O00O00O0 )#line:485
def os_qinglong ():#line:488
    if application in os .environ :#line:489
        O0O0OOOOOOO00OOOO =os .environ [application ].split ('\n')#line:490
        if len (O0O0OOOOOOO00OOOO )>0 :#line:491
            return O0O0OOOOOOO00OOOO #line:492
        else :#line:493
            print (f"{application}变量未启用")#line:494
            print ('脚本退出')#line:495
            sys .exit (1 )#line:496
    else :#line:497
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:498
        return os_built ()#line:499
def os_built ():#line:502
    if token :#line:503
        OOO000OOO0O0O00OO =token .split ('\n')#line:504
        if len (OOO000OOO0O0O00OO )>0 :#line:505
            return OOO000OOO0O0O00OO #line:506
    else :#line:507
        print (f"内置变量为空")#line:508
        print ('脚本结束')#line:509
        sys .exit (0 )#line:510
if __name__ =='__main__':#line:513
    start ()#line:514
