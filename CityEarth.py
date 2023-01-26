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
版本  0.6
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
        OO0OO00OO0O00O0O0 =os_qinglong ()#line:7
        print (f"==========共找到{len(OO0OO00OO0O00O0O0)}个账号==========")#line:8
        for OO0O000OOO0O00OO0 in OO0OO00OO0O00O0O0 :#line:9
            print (f"------------正在执行第{OO0OO00OO0O00O0O0.index(OO0O000OOO0O00OO0) + 1}个账号------------")#line:10
            O0O00OOOO0OOO000O =CityEarth (OO0O000OOO0O00OO0 )#line:11
            if O0O00OOOO0OOO000O .base_info ():#line:13
                O0O00OOOO0OOO000O .friends_invitation ()#line:18
                O0O00OOOO0OOO000O .add_clover ()#line:20
                O0O00OOOO0OOO000O .energy ()#line:22
                O0O00OOOO0OOO000O .synthetic ()#line:24
                O0O00OOOO0OOO000O .propsraffle ()#line:26
                O0O00OOOO0OOO000O .crops_illustrated ()#line:28
            else :#line:29
                print ('token失效')#line:30
            time .sleep (time_xx )#line:32
    except Exception as O00000O00000O00O0 :#line:33
        print (O00000O00000O00O0 )#line:34
def sign (OO000OOO0O0OOOOOO ):#line:36
    OOOOO0O00OOOOO00O =hashlib .md5 (OO000OOO0O0OOOOOO .encode ()).hexdigest ()#line:37
    O00O0OOO000O00O00 ="scsc%^&*"+OOOOO0O00OOOOO00O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:38
    OOOO0O00O0O0OO00O =hashlib .md5 (O00O0OOO000O00O00 .encode ()).hexdigest ()#line:39
    return OOOO0O00O0O0OO00O #line:40
def timi_new ():#line:42
    return str (int (time .time ()*1000 ))#line:43
class CityEarth :#line:46
    def __init__ (O000000OOO0OO0O0O ,O00OOOOO00O000OOO ):#line:48
        try :#line:49
            O000000OOO0OO0O0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:50
            O000000OOO0OO0O0O .token =O00OOOOO00O000OOO .split ('&')[0 ]#line:51
            O000000OOO0OO0O0O .innerId =O00OOOOO00O000OOO .split ('&')[1 ]#line:52
        except Exception as OOO0OO000O000OOOO :#line:53
            print ('变量格式错误')#line:54
    def base_info (OOOO0O0O000O0000O ):#line:57
        global level #line:58
        try :#line:59
            O0OOO00OOO0O0O000 =f'__{timi_new()}'#line:60
            O0OO0000O0000000O ={'authorization':OOOO0O0O000O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OOO0O0O000 ),'signstring':O0OOO00OOO0O0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:69
            OOO0OO0000OO0O00O =requests .request ('get',f'{host}/user',headers =O0OO0000O0000000O ).json ()#line:70
            if 'status'in OOO0OO0000OO0O00O :#line:71
                if OOO0OO0000OO0O00O ['status']==200 :#line:72
                    O00OOO0OOO00O0O00 =OOO0OO0000OO0O00O ['data']['nickname']#line:73
                    OOO0OO0O000O0OO00 =OOO0OO0000OO0O00O ['data']['inner_id']#line:74
                    OOOO0OO0O00OO0OO0 =OOO0OO0000OO0O00O ['data']['assets']['gold']#line:75
                    level =OOO0OO0000OO0O00O ['data']['level']#line:76
                    print (f'【账号信息】:昵称:{O00OOO0OOO00O0O00}丨ID:{str(OOO0OO0O000O0OO00)[:3] + "**"+ str(OOO0OO0O000O0OO00)[5:]}丨等级:{level}丨种子:{str(OOOO0OO0O00OO0OO0).split(".")[0]}')#line:77
                if OOO0OO0000OO0O00O ['status']==401 :#line:78
                    return False #line:79
                if OOO0OO0000OO0O00O ['status']==500 :#line:80
                    return False #line:81
            return True #line:82
        except Exception as OO0OOOOOOO0O00000 :#line:83
            print (OO0OOOOOOO0O00000 )#line:84
    def crops_illustrated (OO000OOO000O00OOO ):#line:88
        OOOO00O0000OO000O =f'__{timi_new()}'#line:89
        OOO0O00O0O0OO000O ={'authorization':OO000OOO000O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0000OO000O ),'signstring':OOOO00O0000OO000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:98
        OO0OOOO0O0000O000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO0O00O0O0OO000O ).json ()#line:99
        if 'status'in OO0OOOO0O0000O000 :#line:101
            if OO0OOOO0O0000O000 ['status']==200 :#line:102
                OOO00OO0OO000OO00 =OO0OOOO0O0000O000 ['data'][0 ]['crops']#line:103
                for O0000000OOO0O000O in OOO00OO0OO000OO00 :#line:104
                    if O0000000OOO0O000O ['ill_clover_award']:#line:105
                        if float (O0000000OOO0O000O ['ill_clover_award'])>1 :#line:106
                            if O0000000OOO0O000O ['is_finish']:#line:107
                                if not O0000000OOO0O000O ['is_getit']:#line:108
                                    OOOO00O0000OO000O =f'_award_level={O0000000OOO0O000O["level"]}_{timi_new()}'#line:109
                                    OOO0O00O0O0OO000O ={'authorization':OO000OOO000O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0000OO000O ),'signstring':OOOO00O0000OO000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:118
                                    O00OO0OOOO0OO0OO0 ={"award_level":O0000000OOO0O000O ['level']}#line:119
                                    O0OOOOO00OO00000O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO0O00O0O0OO000O ,json =O00OO0OOOO0OO0OO0 ).json ()#line:120
                                    if 'status'in O0OOOOO00OO00000O :#line:121
                                        if O0OOOOO00OO00000O ['status']==200 :#line:122
                                            O000000OOOO0OOO0O =O0OOOOO00OO00000O ['data']['ill_clover_award']#line:123
                                            print (f'【图鉴奖励】:领取{O0000000OOO0O000O["crop_name"]}成就丨奖励{O000000OOOO0OOO0O}叶子成功')#line:124
                                        if O0OOOOO00OO00000O ['status']==500 :#line:125
                                            print (f'【图鉴奖励】:{O0OOOOO00OO00000O["message"]}')#line:126
    def watched_ad (O00OO000O0O0OO000 ):#line:129
        O00OOO000OOOOOOO0 =f'__{timi_new()}'#line:130
        OO000O0000O00O00O ={'authorization':O00OO000O0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO000OOOOOOO0 ),'signstring':O00OOO000OOOOOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:139
        OOO000OO00O00O00O =requests .request ('post',f'{host}/game/watched-ad',headers =OO000O0000O00O00O ).json ()#line:140
        print (OOO000OO00O00O00O )#line:141
    def user_ad (OOOO0OOOOOOOOO000 ):#line:147
        O00O0OO00O00O0OO0 =f'__{timi_new()}'#line:148
        OOO0000O0OO00O0OO ={'authorization':OOOO0OOOOOOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO00O00O0OO0 ),'signstring':O00O0OO00O00O0OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:157
        O0O00OO0OOO0O0000 =requests .request ('get',f'{host}/user/ad',headers =OOO0000O0OO00O0OO ).json ()#line:158
        if 'status'in O0O00OO0OOO0O0000 :#line:160
            if O0O00OO0OOO0O0000 ['status']==200 :#line:161
                OO0000OOO00OO00O0 =O0O00OO0OOO0O0000 ['data']['max_time']#line:162
                OOOO00OO0000OOO00 =O0O00OO0OOO0O0000 ['data']['watch_time']#line:163
                OO0OOO0O0000O0O00 =O0O00OO0OOO0O0000 ['data']['added_time']#line:164
                print (f'【获取种子】:获取种子剩余{OO0OOO0O0000O0O00 + OO0000OOO00OO00O0 - OOOO00OO0000OOO00}次丨好友提供:{OO0OOO0O0000O0O00}次')#line:165
                if OO0OOO0O0000O0O00 +OO0000OOO00OO00O0 -OOOO00OO0000OOO00 >0 :#line:166
                    time .sleep (random .randint (16 ,19 ))#line:167
                    O0OO0O0O0OOOOOOOO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO0000O0OO00O0OO ).json ()#line:168
                    if 'status'in O0OO0O0O0OOOOOOOO :#line:170
                        if O0OO0O0O0OOOOOOOO ['status']==200 :#line:171
                            OOO0OOO0OOOO0OO0O =O0OO0O0O0OOOOOOOO ['data']['silver']#line:172
                            print (f'【获取种子】:获得种子:{OOO0OOO0OOOO0OO0O}')#line:173
                            return True #line:174
                        if O0OO0O0O0OOOOOOOO ['status']==500 :#line:175
                            O0O0000OOO00OO0OO =O0OO0O0O0OOOOOOOO ['message']#line:176
                            print (f'【获取种子】:{O0O0000OOO00OO0OO}')#line:177
                            return False #line:178
    def synthetic (OOO0OOOO0000OO00O ):#line:181
        global id ,g #line:182
        try :#line:183
            while True :#line:185
                O00OO00O0O0OO0O00 =f'__{timi_new()}'#line:186
                OO0O00OO00OOO0O0O ={'authorization':OOO0OOOO0000OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00O0O0OO0O00 ),'signstring':O00OO00O0O0OO0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:195
                O00O0000OOOO000O0 =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00OO00OOO0O0O ).json ()#line:196
                if 'status'in O00O0000OOOO000O0 :#line:198
                    if O00O0000OOOO000O0 ['status']==200 :#line:199
                        O00OO00OO00000O0O =O00O0000OOOO000O0 ['data']['cropList']#line:200
                        O00000OO000OO0O0O =O00O0000OOOO000O0 ['data']['gameCoreDataDBid']#line:201
                        O000OO00OOOOO000O =0 #line:202
                        for O000O0OO0OOO00O00 in O00OO00OO00000O0O :#line:203
                            if not O000O0OO0OOO00O00 :#line:204
                                O00OO000O0OO0O00O =f'_crop_id={O00000OO000OO0O0O}&site={O000OO00OOOOO000O}_{OOO0OOOO0000OO00O.time}'#line:205
                                O00OO00O0O0OOO0O0 ={'authorization':OOO0OOOO0000OO00O .token ,'timestamp':OOO0OOOO0000OO00O .time ,'sign':sign (O00OO000O0OO0O00O ),'signstring':O00OO000O0OO0O00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
                                O0O000OO000OOO000 ={"site":O000OO00OOOOO000O ,"crop_id":O00000OO000OO0O0O }#line:215
                                O0000OOOO000O00O0 =requests .request ('post',f'{host}/game/crops/buy',headers =O00OO00O0O0OOO0O0 ,data =O0O000OO000OOO000 ).json ()#line:216
                                if 'status'in O0000OOOO000O00O0 :#line:218
                                    if O0000OOOO000O00O0 ['status']==200 :#line:219
                                        if O0000OOOO000O00O0 ['message']=='种子数量不足':#line:220
                                            print (f'【购买合成】:{O0000OOOO000O00O0["message"]}')#line:221
                                            if not OOO0OOOO0000OO00O .user_ad ():#line:222
                                                return False #line:223
                                        print (f'【购买合成】:购买农作物,位置{O000OO00OOOOO000O}')#line:224
                                    if O0000OOOO000O00O0 ['status']==500 :#line:225
                                        print (f'【购买合成】:{O0000OOOO000O00O0["message"]}')#line:226
                                        return False #line:227
                            O000OO00OOOOO000O +=1 #line:228
                        OO0O0000O0O000O00 =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00OO00OOO0O0O ).json ()#line:229
                        O0OOO000O00OO00O0 =OO0O0000O0O000O00 ['data']['cropList']#line:230
                        OO000O000O00OO0OO =False #line:231
                        for O000O0OO0OOO00O00 in range (12 ):#line:232
                            id =O0OOO000O00OO00O0 [O000O0OO0OOO00O00 ]['level']#line:233
                            if int (level )-int (id )>9 :#line:234
                                O0O0OO00O0000O00O =f'_site={O000O0OO0OOO00O00}_{timi_new()}'#line:235
                                O00OO0OO0O000O000 ={'accept':'application/json, text/plain, */*','authorization':OOO0OOOO0000OO00O .token ,'timestamp':timi_new (),'sign':sign (O0O0OO00O0000O00O ),'signstring':O0O0OO00O0000O00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:245
                                OOOO0OO00000OOOOO ={"site":O000O0OO0OOO00O00 }#line:246
                                O0O0000OOO0O0OO0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00OO0OO0O000O000 ,data =OOOO0OO00000OOOOO ).json ()#line:247
                                if 'status'in O0O0000OOO0O0OO0O :#line:249
                                    if O0O0000OOO0O0OO0O ['status']==200 :#line:250
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:251
                            if id !=0 :#line:252
                                for OOOOOO0OO0000OO00 in range (11 ):#line:253
                                    OOO00OO0O0O0O0OOO =OOOOOO0OO0000OO00 +1 #line:254
                                    g =O0OOO000O00OO00O0 [OOO00OO0O0O0O0OOO ]['level']#line:255
                                    if id ==g :#line:256
                                        O000OO00O000000O0 =OOOOOO0OO0000OO00 +2 #line:257
                                        if O000OO00O000000O0 ==O000O0OO0OOO00O00 +1 :#line:258
                                            pass #line:259
                                        else :#line:260
                                            O0OO0O0O0O0O0000O =O000O0OO0OOO00O00 +1 #line:261
                                            OO0O00OOO0OOOO000 =f'_site={O0OO0O0O0O0O0000O-1}&targetSite={O000OO00O000000O0-1}_{timi_new()}'#line:264
                                            O0OOO0O0OO00O0O0O ={'accept':'application/json, text/plain, */*','authorization':OOO0OOOO0000OO00O .token ,'timestamp':timi_new (),'sign':sign (OO0O00OOO0OOOO000 ),'signstring':OO0O00OOO0OOOO000 ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:279
                                            O0OO0000O0O0OOOOO ={"site":int (O0OO0O0O0O0O0000O -1 ),"targetSite":int (O000OO00O000000O0 -1 )}#line:280
                                            O0O0O0OOO0OO0OO00 =requests .request ('post',f'{host}/game/crops/move',headers =O0OOO0O0OO00O0O0O ,json =O0OO0000O0O0OOOOO ).json ()#line:281
                                            if 'status'in O0O0O0OOO0OO0OO00 :#line:282
                                                if O0O0O0OOO0OO0OO00 ['status']==200 :#line:283
                                                    pass #line:284
                                            print ('【购买合成】:',O0OO0O0O0O0O0000O ,O000OO00O000000O0 ,'合成成功')#line:286
                                            OO000O000O00OO0OO =True #line:287
                                    if OO000O000O00OO0OO :#line:288
                                        break #line:289
                                if OO000O000O00OO0OO :#line:290
                                    break #line:291
        except Exception as OO0OOO0OO000O0000 :#line:292
            OOO0OOOO0000OO00O .synthetic ()#line:293
    def propsraffle (O0O0000OOOOOO0O0O ):#line:297
        try :#line:298
            while True :#line:299
                OOO000OO0O0O00OOO =f'__{timi_new()}'#line:300
                OOOOO00O0OO0O0O00 ={'authorization':O0O0000OOOOOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO0O0O00OOO ),'signstring':OOO000OO0O0O00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:309
                OO0000O0O0OO0OOO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOOO00O0OO0O0O00 ).json ()#line:310
                if 'status'in OO0000O0O0OO0OOO0 :#line:312
                    if OO0000O0O0OO0OOO0 ['status']==200 :#line:313
                        O00O00O0O0OOO000O =OO0000O0O0OO0OOO0 ['data']['rows']#line:314
                        O0OOO0OO0OOOO000O =OO0000O0O0OO0OOO0 ['data']['vstate']#line:315
                        if O00O00O0O0OOO000O ==5 or O00O00O0O0OOO000O ==6 or O00O00O0O0OOO000O ==7 :#line:316
                            OOOOOOOO0O00OO00O =OO0000O0O0OO0OOO0 ['data']['silver']#line:317
                            print (f'【转盘抽奖】:获得种子:{OOOOOOOO0O00OO00O}')#line:318
                        if O00O00O0O0OOO000O ==1 or O00O00O0O0OOO000O ==2 or O00O00O0O0OOO000O ==3 :#line:319
                            OOO000OOOOO0O0000 =OO0000O0O0OO0OOO0 ['data']['clover']#line:320
                            print (f'【转盘抽奖】:获得三叶草:{OOO000OOOOO0O0000}')#line:321
                        if O00O00O0O0OOO000O ==4 or O00O00O0O0OOO000O ==8 :#line:322
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:323
                        if O00O00O0O0OOO000O =='抽奖次数已用完':#line:327
                            if O0OOO0OO0OOOO000O :#line:328
                                OO0OO0OOO0OOOO0O0 =random .randint (160 ,190 )/10 #line:329
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{OO0OO0OOO0OOOO0O0}秒获取抽奖机会')#line:330
                                time .sleep (OO0OO0OOO0OOOO0O0 )#line:331
                                OO0OOO00O00OOO0O0 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OOOOO00O0OO0O0O00 ).json ()#line:332
                                if 'status'in OO0OOO00O00OOO0O0 :#line:334
                                    if OO0OOO00O00OOO0O0 ['status']==200 :#line:335
                                        print (f'【转盘抽奖】:{OO0OOO00O00OOO0O0["message"]}')#line:336
                                    if OO0OOO00O00OOO0O0 ['status']==500 :#line:337
                                        print (f'【转盘抽奖】:{OO0OOO00O00OOO0O0["message"]}')#line:338
                                        break #line:339
                                time .sleep (random .randint (10 ,15 )/10 )#line:340
                            else :#line:341
                                break #line:342
                time .sleep (random .randint (8 ,15 )/10 )#line:343
        except Exception as O0O0OOOOOO000000O :#line:344
            print (O0O0OOOOOO000000O )#line:345
    def friends_invitation (O0000OOO0OOO0OOO0 ):#line:348
        try :#line:349
            OO0O000000000O0OO =f'__{timi_new()}'#line:350
            O0O00OOO0O0O000O0 ={'authorization':O0000OOO0OOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000000000O0OO ),'signstring':OO0O000000000O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:359
            O0O0O0O000OO00OO0 =requests .request ('get',f'{host}/friends',headers =O0O00OOO0O0O000O0 ).json ()#line:360
            if 'status'in O0O0O0O000OO00OO0 :#line:361
                if O0O0O0O000OO00OO0 ['status']==200 :#line:362
                    OO000O0O00OO0OOOO =O0O0O0O000OO00OO0 ['data']['myInviteter']#line:363
                    if OO000O0O00OO0OOOO :#line:364
                        OO00O00O00OO0000O =OO000O0O00OO0OOOO ['user']['nickname']#line:365
                        print (f'【绑邀请码】:我的邀请人:{OO00O00O00OO0000O}')#line:366
                    else :#line:367
                        if O0000OOO0OOO0OOO0 .innerId !='0':#line:368
                            print ('【绑邀请码】:绑定邀请码')#line:369
                            O0O0O0O000OO0OO0O ={"innerId":O0000OOO0OOO0OOO0 .innerId }#line:370
                            OO00OO0000OO000OO =requests .request ('post',f'{host}/friends/my-invitation',headers =O0O00OOO0O0O000O0 ,data =O0O0O0O000OO0OO0O ).json ()#line:371
                            print (OO00OO0000OO000OO )#line:372
                        else :#line:373
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:374
        except Exception as OO0OO0OOO00O000OO :#line:375
            print (OO0OO0OOO00O000OO )#line:376
    def add_clover (O000O0OO00OO0O00O ):#line:380
        try :#line:381
            O000O0OOOO0O0OO0O =f'__{timi_new()}'#line:382
            OO0O0O0O0O0OO0000 ={'authorization':O000O0OO00OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOOO0O0OO0O ),'signstring':O000O0OOOO0O0OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:391
            OO0OOOOO000000000 =requests .request ('get',f'{host}/assets/clovers',headers =OO0O0O0O0O0OO0000 ).json ()#line:392
            if 'status'in OO0OOOOO000000000 :#line:394
                if OO0OOOOO000000000 ['status']==200 :#line:395
                    O00O00O0O00OOOO00 =OO0OOOOO000000000 ['data']['clover']#line:396
                    O00OO00OO0O0OO00O =OO0OOOOO000000000 ['data']['used_clover']#line:397
                    O00000O0000OO0O0O =float (O00O00O0O00OOOO00 )-float (O00OO00OO0O0OO00O )#line:398
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O00OO00OO0O0OO00O}')#line:399
                    if O00000O0000OO0O0O >1 :#line:400
                        O000O0OOOO0O0OO0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00000O0000OO0O0O)}_{timi_new()}'#line:401
                        OO0O0O0O0O0OO0000 ={'authorization':O000O0OO00OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOOO0O0OO0O ),'signstring':O000O0OOOO0O0OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:410
                        OO0OOOO0O000OOOOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00000O0000OO0O0O )}#line:411
                        O00O00O0O0OOO00O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0O0O0O0O0OO0000 ,data =OO0OOOO0O000OOOOO ).json ()#line:412
                        if 'status'in O00O00O0O0OOO00O0 :#line:414
                            if O00O00O0O0OOO00O0 ['status']==200 :#line:415
                                print (f'【参与抽奖】:添加三叶草:{O00O00O0O0OOO00O0["data"]}丨数量:{O00000O0000OO0O0O}')#line:416
            O00OOO00O0000000O =requests .request ('get',f'{host}/lottery',headers =OO0O0O0O0O0OO0000 ).json ()#line:417
            if 'status'in O00OOO00O0000000O :#line:419
                if O00OOO00O0000000O ['status']==200 :#line:420
                    O0O0OOO0OO0O0O0OO =O00OOO00O0000000O ['data'][0 ]['day_get_gold_quantity']#line:421
                    print (f'【参与抽奖】:预计每天中{O0O0OOO0OO0O0O0OO[:6]}种子')#line:422
        except Exception as O000O00O0OO00O0OO :#line:423
            print (O000O00O0OO00O0OO )#line:424
    def energy (OO0000000OO000OOO ):#line:427
        O0OO00000000O000O =f'__{timi_new()}'#line:428
        OOO0O00OOO00O0O00 ={'authorization':OO0000000OO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00000000O000O ),'signstring':O0OO00000000O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:437
        OOO0O00O0000OO000 =requests .request ('get',f'{host}/energy/general',headers =OOO0O00OOO00O0O00 ).json ()#line:438
        if 'status'in OOO0O00O0000OO000 :#line:440
            if OOO0O00O0000OO000 ['status']==200 :#line:441
                OO0OOO0O00OOO0OO0 =OOO0O00O0000OO000 ['data']['ordinary_water_consumptions']#line:442
                if float (OO0OOO0O00OOO0OO0 )<80 :#line:443
                    O000O00O000OOOO00 =99 -float (OO0OOO0O00OOO0OO0 )#line:444
                    O0OO00OO00OOO00O0 ={"fertilizer":str (O000O00O000OOOO00 ).split ('.')[0 ]}#line:445
                    O000000O000OO0OOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO0O00OOO00O0O00 ,data =O0OO00OO00OOO00O0 ).json ()#line:446
                    if 'status'in O000000O000OO0OOO :#line:448
                        if O000000O000OO0OOO ['status']==200 :#line:449
                            print (f'【购买肥料】:{O000000O000OO0OOO["message"]}')#line:450
                O000OO000OOOOO0OO =OOO0O00O0000OO000 ['data']['ordinary_water_consumptions']#line:451
                if float (O000OO000OOOOO0OO )<800 :#line:452
                    O00OOOOO0OOOO000O =999 -float (O000OO000OOOOO0OO )#line:453
                    OO0OO0OOO0000O0O0 ={"water":str (O00OOOOO0OOOO000O ).split ('.')[0 ]}#line:454
                    O0O0O000O0000OO0O =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO0O00OOO00O0O00 ,data =OO0OO0OOO0000O0O0 ).json ()#line:455
                    if 'status'in O0O0O000O0000OO0O :#line:456
                        if O0O0O000O0000OO0O ['status']==200 :#line:457
                            print (f'【购买水滴】:{O0O0O000O0000OO0O["message"]}')#line:458
def version_of_the_validation ():#line:464
    return str ((62 -56 )/10 )#line:465
def gitee_validation ():#line:467
    try :#line:468
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:469
    except Exception as O0O000O000000O0O0 :#line:470
        sys .exit (0 )#line:471
def update_the_validation ():#line:477
    try :#line:478
        O00OOOOOOOOOOOOO0 =gitee_validation ()#line:479
        if version_of_the_validation ()<O00OOOOOOOOOOOOO0 ['CityEarth']['edition']:#line:480
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OOOOOOOOOOOOO0["CityEarth"]["edition"]}   ❌')#line:481
            print (f'更新内容=>>{O00OOOOOOOOOOOOO0["CityEarth"]["content"]}   👍')#line:482
        else :#line:483
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OOOOOOOOOOOOO0["CityEarth"]["edition"]}   ✅')#line:484
            print (f'更新内容=>> {O00OOOOOOOOOOOOO0["CityEarth"]["content"]}   👍')#line:485
    except Exception as OOOOO0OO00O0O0OO0 :#line:486
        print (OOOOO0OO00O0O0OO0 )#line:487
def os_qinglong ():#line:490
    if application in os .environ :#line:491
        O000000O00OOO00OO =os .environ [application ].split ('\n')#line:492
        if len (O000000O00OOO00OO )>0 :#line:493
            return O000000O00OOO00OO #line:494
        else :#line:495
            print (f"{application}变量未启用")#line:496
            print ('脚本退出')#line:497
            sys .exit (1 )#line:498
    else :#line:499
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:500
        return os_built ()#line:501
def os_built ():#line:504
    if token :#line:505
        O0OO0O00O0OO0O0O0 =token .split ('\n')#line:506
        if len (O0OO0O00O0OO0O0O0 )>0 :#line:507
            return O0OO0O00O0OO0O0O0 #line:508
    else :#line:509
        print (f"内置变量为空")#line:510
        print ('脚本结束')#line:511
        sys .exit (0 )#line:512
if __name__ =='__main__':#line:515
    start ()#line:516
