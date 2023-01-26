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
        O0OO00O0000O00O00 =os_qinglong ()#line:7
        print (f"==========共找到{len(O0OO00O0000O00O00)}个账号==========")#line:8
        for O0O0O0O0O0OOO0O00 in O0OO00O0000O00O00 :#line:9
            print (f"------------正在执行第{O0OO00O0000O00O00.index(O0O0O0O0O0OOO0O00) + 1}个账号------------")#line:10
            O0O00O0O0000O00O0 =CityEarth (O0O0O0O0O0OOO0O00 )#line:11
            if O0O00O0O0000O00O0 .base_info ():#line:13
                O0O00O0O0000O00O0 .friends_invitation ()#line:18
                O0O00O0O0000O00O0 .add_clover ()#line:20
                O0O00O0O0000O00O0 .energy ()#line:22
                O0O00O0O0000O00O0 .synthetic ()#line:24
                O0O00O0O0000O00O0 .propsraffle ()#line:26
                O0O00O0O0000O00O0 .crops_illustrated ()#line:28
            else :#line:29
                print ('token失效')#line:30
            time .sleep (time_xx )#line:32
    except Exception as O0OOO00OO0O00OO0O :#line:33
        print (O0OOO00OO0O00OO0O )#line:34
def sign (O000O0OOO00OOO00O ):#line:36
    OOOOOOO0O00OOOO0O =hashlib .md5 (O000O0OOO00OOO00O .encode ()).hexdigest ()#line:37
    O00OO0OO0O00O00OO ="scsc%^&*"+OOOOOOO0O00OOOO0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:38
    O0000O0OO000OOOOO =hashlib .md5 (O00OO0OO0O00O00OO .encode ()).hexdigest ()#line:39
    return O0000O0OO000OOOOO #line:40
def timi_new ():#line:42
    return str (int (time .time ()*1000 ))#line:43
class CityEarth :#line:46
    def __init__ (OOO0000O00OO0OOOO ,O000O00O00OO0OO0O ):#line:48
        try :#line:49
            OOO0000O00OO0OOOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:50
            OOO0000O00OO0OOOO .token =O000O00O00OO0OO0O .split ('&')[0 ]#line:51
            OOO0000O00OO0OOOO .innerId =O000O00O00OO0OO0O .split ('&')[1 ]#line:52
        except Exception as O0OOOOOOOOO00O00O :#line:53
            print ('变量格式错误')#line:54
    def base_info (OOOO0O0OOO0OO000O ):#line:57
        global level #line:58
        try :#line:59
            OOOOOO0O000OOO0OO =f'__{timi_new()}'#line:60
            OO00OO0O0OO000OOO ={'authorization':OOOO0O0OOO0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O000OOO0OO ),'signstring':OOOOOO0O000OOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:69
            OO00000OO00O0OO00 =requests .request ('get',f'{host}/user',headers =OO00OO0O0OO000OOO ).json ()#line:70
            if 'status'in OO00000OO00O0OO00 :#line:71
                if OO00000OO00O0OO00 ['status']==200 :#line:72
                    O0OOO0000000O0O0O =OO00000OO00O0OO00 ['data']['nickname']#line:73
                    O0O0O00O00OOO0000 =OO00000OO00O0OO00 ['data']['inner_id']#line:74
                    O00O0O0OO0000OO00 =OO00000OO00O0OO00 ['data']['assets']['gold']#line:75
                    level =OO00000OO00O0OO00 ['data']['level']#line:76
                    print (f'【账号信息】:昵称:{O0OOO0000000O0O0O}丨ID:{str(O0O0O00O00OOO0000)[:3] + "**"+ str(O0O0O00O00OOO0000)[5:]}丨等级:{level}丨种子:{str(O00O0O0OO0000OO00).split(".")[0]}')#line:77
                if OO00000OO00O0OO00 ['status']==401 :#line:78
                    return False #line:79
                if OO00000OO00O0OO00 ['status']==500 :#line:80
                    return False #line:81
            return True #line:82
        except Exception as OO00O000OO000OOOO :#line:83
            print (OO00O000OO000OOOO )#line:84
    def crops_illustrated (O0O0000O0OOOO000O ):#line:88
        O0OOOO00O0OO00000 =f'__{timi_new()}'#line:89
        O0OO0OO000OO00OOO ={'authorization':O0O0000O0OOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00O0OO00000 ),'signstring':O0OOOO00O0OO00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:98
        OOO0O00000000O00O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OO0OO000OO00OOO ).json ()#line:99
        if 'status'in OOO0O00000000O00O :#line:101
            if OOO0O00000000O00O ['status']==200 :#line:102
                O0OO0OO0O0O0OOOOO =OOO0O00000000O00O ['data'][0 ]['crops']#line:103
                for OOOO0OO000OO0OOOO in O0OO0OO0O0O0OOOOO :#line:104
                    if OOOO0OO000OO0OOOO ['ill_clover_award']:#line:105
                        if float (OOOO0OO000OO0OOOO ['ill_clover_award'])>1 :#line:106
                            if OOOO0OO000OO0OOOO ['is_finish']:#line:107
                                if not OOOO0OO000OO0OOOO ['is_getit']:#line:108
                                    O0OOOO00O0OO00000 =f'_award_level={OOOO0OO000OO0OOOO["level"]}_{timi_new()}'#line:109
                                    O0OO0OO000OO00OOO ={'authorization':O0O0000O0OOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00O0OO00000 ),'signstring':O0OOOO00O0OO00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:118
                                    O0O000000O000OOOO ={"award_level":OOOO0OO000OO0OOOO ['level']}#line:119
                                    O0O0OOOOOO00OOO00 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OO0OO000OO00OOO ,json =O0O000000O000OOOO ).json ()#line:120
                                    if 'status'in O0O0OOOOOO00OOO00 :#line:121
                                        if O0O0OOOOOO00OOO00 ['status']==200 :#line:122
                                            O000O00O00O00OOO0 =O0O0OOOOOO00OOO00 ['data']['ill_clover_award']#line:123
                                            print (f'【图鉴奖励】:领取{OOOO0OO000OO0OOOO["crop_name"]}成就丨奖励{O000O00O00O00OOO0}叶子成功')#line:124
                                        if O0O0OOOOOO00OOO00 ['status']==500 :#line:125
                                            print (f'【图鉴奖励】:{O0O0OOOOOO00OOO00["message"]}')#line:126
    def watched_ad (OO0O0000O0000O0OO ):#line:129
        OOOO000OOO00000O0 =f'__{timi_new()}'#line:130
        OOOOOOO00OOOOO0O0 ={'authorization':OO0O0000O0000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000OOO00000O0 ),'signstring':OOOO000OOO00000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:139
        OOOOOOO0O000OOOOO =requests .request ('post',f'{host}/game/watched-ad',headers =OOOOOOO00OOOOO0O0 ).json ()#line:140
        print (OOOOOOO0O000OOOOO )#line:141
    def user_ad (OOO0OOOO00O00O00O ):#line:147
        OOO0000000O000OO0 =f'__{timi_new()}'#line:148
        OOOO000000OOO00O0 ={'authorization':OOO0OOOO00O00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000000O000OO0 ),'signstring':OOO0000000O000OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:157
        O0OO0O00O0O00OO00 =requests .request ('get',f'{host}/user/ad',headers =OOOO000000OOO00O0 ).json ()#line:158
        if 'status'in O0OO0O00O0O00OO00 :#line:160
            if O0OO0O00O0O00OO00 ['status']==200 :#line:161
                OOOOO0OO0O00OO000 =O0OO0O00O0O00OO00 ['data']['max_time']#line:162
                O000OOO00O000OOO0 =O0OO0O00O0O00OO00 ['data']['watch_time']#line:163
                OO000000OO00OO00O =O0OO0O00O0O00OO00 ['data']['added_time']#line:164
                print (f'【获取种子】:获取种子剩余{OO000000OO00OO00O + OOOOO0OO0O00OO000 - O000OOO00O000OOO0}次丨好友提供:{OO000000OO00OO00O}次')#line:165
                if OO000000OO00OO00O +OOOOO0OO0O00OO000 -O000OOO00O000OOO0 >0 :#line:166
                    time .sleep (random .randint (16 ,19 ))#line:167
                    OOO0000OO0O0OO0O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOOO000000OOO00O0 ).json ()#line:168
                    if 'status'in OOO0000OO0O0OO0O0 :#line:170
                        if OOO0000OO0O0OO0O0 ['status']==200 :#line:171
                            O0OOO0O0O0000OO00 =OOO0000OO0O0OO0O0 ['data']['silver']#line:172
                            print (f'【获取种子】:获得种子:{O0OOO0O0O0000OO00}')#line:173
                            return True #line:174
                        if OOO0000OO0O0OO0O0 ['status']==500 :#line:175
                            OO0OOO0O0OO000O0O =OOO0000OO0O0OO0O0 ['message']#line:176
                            print (f'【获取种子】:{OO0OOO0O0OO000O0O}')#line:177
                            return False #line:178
    def synthetic (OOO0O0OOOO000OO0O ):#line:181
        global id ,g #line:182
        try :#line:183
            while True :#line:185
                OOOOOO0OO0O0OO00O =f'__{timi_new()}'#line:186
                OO00O0OO00O0OO0O0 ={'authorization':OOO0O0OOOO000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OO0O0OO00O ),'signstring':OOOOOO0OO0O0OO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:195
                OOO0OO00000000O00 =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0OO00O0OO0O0 ).json ()#line:196
                if 'status'in OOO0OO00000000O00 :#line:198
                    if OOO0OO00000000O00 ['status']==200 :#line:199
                        O00000OOO00OO000O =OOO0OO00000000O00 ['data']['cropList']#line:200
                        O0O000O0OO0O00000 =OOO0OO00000000O00 ['data']['gameCoreDataDBid']#line:201
                        OOOOO0OO0OOO0O0O0 =0 #line:202
                        for OOOO0000O0O0OO000 in O00000OOO00OO000O :#line:203
                            if not OOOO0000O0O0OO000 :#line:204
                                OO00O000O00O00O0O =f'_crop_id={O0O000O0OO0O00000}&site={OOOOO0OO0OOO0O0O0}_{OOO0O0OOOO000OO0O.time}'#line:205
                                O00OO0O0O0OOOO000 ={'authorization':OOO0O0OOOO000OO0O .token ,'timestamp':OOO0O0OOOO000OO0O .time ,'sign':sign (OO00O000O00O00O0O ),'signstring':OO00O000O00O00O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
                                O0O0OOOO00O0OOOOO ={"site":OOOOO0OO0OOO0O0O0 ,"crop_id":O0O000O0OO0O00000 }#line:215
                                OOO0O0OO0000OOO0O =requests .request ('post',f'{host}/game/crops/buy',headers =O00OO0O0O0OOOO000 ,data =O0O0OOOO00O0OOOOO ).json ()#line:216
                                if 'status'in OOO0O0OO0000OOO0O :#line:218
                                    if OOO0O0OO0000OOO0O ['status']==200 :#line:219
                                        if OOO0O0OO0000OOO0O ['message']=='种子数量不足':#line:220
                                            print (f'【购买合成】:{OOO0O0OO0000OOO0O["message"]}')#line:221
                                            if not OOO0O0OOOO000OO0O .user_ad ():#line:222
                                                return False #line:223
                                        print (f'【购买合成】:购买农作物,位置{OOOOO0OO0OOO0O0O0}')#line:224
                                    if OOO0O0OO0000OOO0O ['status']==500 :#line:225
                                        print (f'【购买合成】:{OOO0O0OO0000OOO0O["message"]}')#line:226
                                        return False #line:227
                            OOOOO0OO0OOO0O0O0 +=1 #line:228
                        OOO0OO0O0O0O0OO0O =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0OO00O0OO0O0 ).json ()#line:229
                        O0OO0000OO00OOO0O =OOO0OO0O0O0O0OO0O ['data']['cropList']#line:230
                        OOOOO0O0O0O0OO000 =False #line:231
                        for OOOO0000O0O0OO000 in range (12 ):#line:232
                            id =O0OO0000OO00OOO0O [OOOO0000O0O0OO000 ]['level']#line:233
                            if int (level )-int (id )>8 :#line:234
                                OO0O0O000000OOOOO =f'_site={OOOO0000O0O0OO000}_{timi_new()}'#line:235
                                OOOO00OO0OO0O0OOO ={'accept':'application/json, text/plain, */*','authorization':OOO0O0OOOO000OO0O .token ,'timestamp':timi_new (),'sign':sign (OO0O0O000000OOOOO ),'signstring':OO0O0O000000OOOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:245
                                O0OOOOO0OOO0O0O00 ={"site":OOOO0000O0O0OO000 }#line:246
                                OOO0O000O0OO00000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOO00OO0OO0O0OOO ,data =O0OOOOO0OOO0O0O00 ).json ()#line:247
                                if 'status'in OOO0O000O0OO00000 :#line:249
                                    if OOO0O000O0OO00000 ['status']==200 :#line:250
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:251
                            if id !=0 :#line:252
                                for O0OO000O0OO0000OO in range (11 ):#line:253
                                    OO00OOO0000O0000O =O0OO000O0OO0000OO +1 #line:254
                                    g =O0OO0000OO00OOO0O [OO00OOO0000O0000O ]['level']#line:255
                                    if id ==g :#line:256
                                        O00O0O0OO00OO00O0 =O0OO000O0OO0000OO +2 #line:257
                                        if O00O0O0OO00OO00O0 ==OOOO0000O0O0OO000 +1 :#line:258
                                            pass #line:259
                                        else :#line:260
                                            OO0000O00OO0O0000 =OOOO0000O0O0OO000 +1 #line:261
                                            O0O0O0OOO0O0O00OO =f'_site={OO0000O00OO0O0000-1}&targetSite={O00O0O0OO00OO00O0-1}_{timi_new()}'#line:264
                                            O00OO00O0000O00O0 ={'accept':'application/json, text/plain, */*','authorization':OOO0O0OOOO000OO0O .token ,'timestamp':timi_new (),'sign':sign (O0O0O0OOO0O0O00OO ),'signstring':O0O0O0OOO0O0O00OO ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:279
                                            O000000O00O0OO0O0 ={"site":int (OO0000O00OO0O0000 -1 ),"targetSite":int (O00O0O0OO00OO00O0 -1 )}#line:280
                                            O0O0O0OOO0OOO00OO =requests .request ('post',f'{host}/game/crops/move',headers =O00OO00O0000O00O0 ,json =O000000O00O0OO0O0 ).json ()#line:281
                                            if 'status'in O0O0O0OOO0OOO00OO :#line:282
                                                if O0O0O0OOO0OOO00OO ['status']==200 :#line:283
                                                    pass #line:284
                                            print ('【购买合成】:',OO0000O00OO0O0000 ,O00O0O0OO00OO00O0 ,'合成成功')#line:286
                                            OOOOO0O0O0O0OO000 =True #line:287
                                    if OOOOO0O0O0O0OO000 :#line:288
                                        break #line:289
                                if OOOOO0O0O0O0OO000 :#line:290
                                    break #line:291
        except Exception as OOOO000O000OO00O0 :#line:292
            OOO0O0OOOO000OO0O .synthetic ()#line:293
    def propsraffle (OOOOOOO0OOO0OOOOO ):#line:297
        try :#line:298
            while True :#line:299
                OOO0OOO0O00O0O000 =f'__{timi_new()}'#line:300
                O0O0000O0OO0OO000 ={'authorization':OOOOOOO0OOO0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0O00O0O000 ),'signstring':OOO0OOO0O00O0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:309
                OO00OOO0O0O0OOOOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O0000O0OO0OO000 ).json ()#line:310
                if 'status'in OO00OOO0O0O0OOOOO :#line:312
                    if OO00OOO0O0O0OOOOO ['status']==200 :#line:313
                        O000OO0OOO0000000 =OO00OOO0O0O0OOOOO ['data']['rows']#line:314
                        OOO0O0OOO00OOO0OO =OO00OOO0O0O0OOOOO ['data']['vstate']#line:315
                        if O000OO0OOO0000000 ==5 or O000OO0OOO0000000 ==6 or O000OO0OOO0000000 ==7 :#line:316
                            OOOOO000OOO00000O =OO00OOO0O0O0OOOOO ['data']['silver']#line:317
                            print (f'【转盘抽奖】:获得种子:{OOOOO000OOO00000O}')#line:318
                        if O000OO0OOO0000000 ==1 or O000OO0OOO0000000 ==2 or O000OO0OOO0000000 ==3 :#line:319
                            O0OOO000OO0000OOO =OO00OOO0O0O0OOOOO ['data']['clover']#line:320
                            print (f'【转盘抽奖】:获得三叶草:{O0OOO000OO0000OOO}')#line:321
                        if O000OO0OOO0000000 ==4 or O000OO0OOO0000000 ==8 :#line:322
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:323
                        if O000OO0OOO0000000 =='抽奖次数已用完':#line:327
                            if OOO0O0OOO00OOO0OO :#line:328
                                O0000O000000O00O0 =random .randint (160 ,190 )/10 #line:329
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{O0000O000000O00O0}秒获取抽奖机会')#line:330
                                time .sleep (O0000O000000O00O0 )#line:331
                                O0OO00O000OO00O00 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O0O0000O0OO0OO000 ).json ()#line:332
                                if 'status'in O0OO00O000OO00O00 :#line:334
                                    if O0OO00O000OO00O00 ['status']==200 :#line:335
                                        print (f'【转盘抽奖】:{O0OO00O000OO00O00["message"]}')#line:336
                                    if O0OO00O000OO00O00 ['status']==500 :#line:337
                                        print (f'【转盘抽奖】:{O0OO00O000OO00O00["message"]}')#line:338
                                        break #line:339
                                time .sleep (random .randint (10 ,15 )/10 )#line:340
                            else :#line:341
                                break #line:342
                time .sleep (random .randint (8 ,15 )/10 )#line:343
        except Exception as O00OO0O0000O00000 :#line:344
            print (O00OO0O0000O00000 )#line:345
    def friends_invitation (OOO0OOO00O0O00O0O ):#line:348
        try :#line:349
            O0OOO00O0O00O0O0O =f'__{timi_new()}'#line:350
            OO0O00OO0OOOOO0O0 ={'authorization':OOO0OOO00O0O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0O00O0O0O ),'signstring':O0OOO00O0O00O0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:359
            OO000O0O0OOOOOOO0 =requests .request ('get',f'{host}/friends',headers =OO0O00OO0OOOOO0O0 ).json ()#line:360
            if 'status'in OO000O0O0OOOOOOO0 :#line:361
                if OO000O0O0OOOOOOO0 ['status']==200 :#line:362
                    O0OOOO0O00OO00OO0 =OO000O0O0OOOOOOO0 ['data']['myInviteter']#line:363
                    if O0OOOO0O00OO00OO0 :#line:364
                        OO00OO0O0OO0000O0 =O0OOOO0O00OO00OO0 ['user']['nickname']#line:365
                        print (f'【绑邀请码】:我的邀请人:{OO00OO0O0OO0000O0}')#line:366
                    else :#line:367
                        if OOO0OOO00O0O00O0O .innerId !='0':#line:368
                            print ('【绑邀请码】:绑定邀请码')#line:369
                            O0O0OO000O0000O0O ={"innerId":OOO0OOO00O0O00O0O .innerId }#line:370
                            OOO00O00OOO000000 =requests .request ('post',f'{host}/friends/my-invitation',headers =OO0O00OO0OOOOO0O0 ,data =O0O0OO000O0000O0O ).json ()#line:371
                            print (OOO00O00OOO000000 )#line:372
                        else :#line:373
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:374
        except Exception as O0OO0OOOOO0O0000O :#line:375
            print (O0OO0OOOOO0O0000O )#line:376
    def add_clover (O0O0OO00O0OOO0OO0 ):#line:380
        try :#line:381
            OO000O00O0OOO0O0O =f'__{timi_new()}'#line:382
            OO0OO00000O000OOO ={'authorization':O0O0OO00O0OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00O0OOO0O0O ),'signstring':OO000O00O0OOO0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:391
            OO00OO0O00OOOOO0O =requests .request ('get',f'{host}/assets/clovers',headers =OO0OO00000O000OOO ).json ()#line:392
            if 'status'in OO00OO0O00OOOOO0O :#line:394
                if OO00OO0O00OOOOO0O ['status']==200 :#line:395
                    OO0O0000O0O00OO0O =OO00OO0O00OOOOO0O ['data']['clover']#line:396
                    OO00OOO0O0O0OO000 =OO00OO0O00OOOOO0O ['data']['used_clover']#line:397
                    O0OOOO0O0OOOOOOOO =float (OO0O0000O0O00OO0O )-float (OO00OOO0O0O0OO000 )#line:398
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OO00OOO0O0O0OO000}')#line:399
                    if O0OOOO0O0OOOOOOOO >1 :#line:400
                        OO000O00O0OOO0O0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OOOO0O0OOOOOOOO)}_{timi_new()}'#line:401
                        OO0OO00000O000OOO ={'authorization':O0O0OO00O0OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00O0OOO0O0O ),'signstring':OO000O00O0OOO0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:410
                        OO0O0000O0OO0O000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OOOO0O0OOOOOOOO )}#line:411
                        OOOO00OOO000OO0O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0OO00000O000OOO ,data =OO0O0000O0OO0O000 ).json ()#line:412
                        if 'status'in OOOO00OOO000OO0O0 :#line:414
                            if OOOO00OOO000OO0O0 ['status']==200 :#line:415
                                print (f'【参与抽奖】:添加三叶草:{OOOO00OOO000OO0O0["data"]}丨数量:{O0OOOO0O0OOOOOOOO}')#line:416
            OO000OO000OO000OO =requests .request ('get',f'{host}/lottery',headers =OO0OO00000O000OOO ).json ()#line:417
            if 'status'in OO000OO000OO000OO :#line:419
                if OO000OO000OO000OO ['status']==200 :#line:420
                    O00OOOO00O0000OOO =OO000OO000OO000OO ['data'][0 ]['day_get_gold_quantity']#line:421
                    print (f'【参与抽奖】:预计每天中{O00OOOO00O0000OOO[:6]}种子')#line:422
        except Exception as OOOOO0OO0O0O0OOOO :#line:423
            print (OOOOO0OO0O0O0OOOO )#line:424
    def energy (O0O0OO000O0O00OOO ):#line:427
        OO0OOOO00OO0OO0OO =f'__{timi_new()}'#line:428
        OOO0OO0O0000O00OO ={'authorization':O0O0OO000O0O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO00OO0OO0OO ),'signstring':OO0OOOO00OO0OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:437
        O000OO0OO0O0000O0 =requests .request ('get',f'{host}/energy/general',headers =OOO0OO0O0000O00OO ).json ()#line:438
        if 'status'in O000OO0OO0O0000O0 :#line:440
            if O000OO0OO0O0000O0 ['status']==200 :#line:441
                O0OO0O00O0OO0O0OO =O000OO0OO0O0000O0 ['data']['ordinary_water_consumptions']#line:442
                if float (O0OO0O00O0OO0O0OO )<80 :#line:443
                    OOOO0O00O000O0O0O =99 -float (O0OO0O00O0OO0O0OO )#line:444
                    OO00OOOO00OO0000O ={"fertilizer":str (OOOO0O00O000O0O0O ).split ('.')[0 ]}#line:445
                    OO0000O00O0O00OO0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO0OO0O0000O00OO ,data =OO00OOOO00OO0000O ).json ()#line:446
                    if 'status'in OO0000O00O0O00OO0 :#line:448
                        if OO0000O00O0O00OO0 ['status']==200 :#line:449
                            print (f'【购买肥料】:{OO0000O00O0O00OO0["message"]}')#line:450
                OOO000O0OO0O00OOO =O000OO0OO0O0000O0 ['data']['ordinary_water_consumptions']#line:451
                if float (OOO000O0OO0O00OOO )<800 :#line:452
                    OOOOO00O0O0O0OOOO =999 -float (OOO000O0OO0O00OOO )#line:453
                    O0OO0OOOO0O000OOO ={"water":str (OOOOO00O0O0O0OOOO ).split ('.')[0 ]}#line:454
                    O0OO00O0OOOO0OO00 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO0OO0O0000O00OO ,data =O0OO0OOOO0O000OOO ).json ()#line:455
                    if 'status'in O0OO00O0OOOO0OO00 :#line:456
                        if O0OO00O0OOOO0OO00 ['status']==200 :#line:457
                            print (f'【购买水滴】:{O0OO00O0OOOO0OO00["message"]}')#line:458
def version_of_the_validation ():#line:464
    return str ((61 -56 )/10 )#line:465
def gitee_validation ():#line:467
    try :#line:468
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:469
    except Exception as OOO0000O0OOO0OO00 :#line:470
        sys .exit (0 )#line:471
def update_the_validation ():#line:477
    try :#line:478
        OOO0OO000O0OO0000 =gitee_validation ()#line:479
        if version_of_the_validation ()<OOO0OO000O0OO0000 ['CityEarth']['edition']:#line:480
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OO000O0OO0000["CityEarth"]["edition"]}   ❌')#line:481
            print (f'更新内容=>>{OOO0OO000O0OO0000["CityEarth"]["content"]}   👍')#line:482
        else :#line:483
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OO000O0OO0000["CityEarth"]["edition"]}   ✅')#line:484
            print (f'更新内容=>> {OOO0OO000O0OO0000["CityEarth"]["content"]}   👍')#line:485
    except Exception as OOOO0O000OOO0OOOO :#line:486
        print (OOOO0O000OOO0OOOO )#line:487
def os_qinglong ():#line:490
    if application in os .environ :#line:491
        OO0000OO0O00O0OOO =os .environ [application ].split ('\n')#line:492
        if len (OO0000OO0O00O0OOO )>0 :#line:493
            return OO0000OO0O00O0OOO #line:494
        else :#line:495
            print (f"{application}变量未启用")#line:496
            print ('脚本退出')#line:497
            sys .exit (1 )#line:498
    else :#line:499
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:500
        return os_built ()#line:501
def os_built ():#line:504
    if token :#line:505
        O0O0O0000OO000O00 =token .split ('\n')#line:506
        if len (O0O0O0000OO000O00 )>0 :#line:507
            return O0O0O0000OO000O00 #line:508
    else :#line:509
        print (f"内置变量为空")#line:510
        print ('脚本结束')#line:511
        sys .exit (0 )#line:512
if __name__ =='__main__':#line:515
    start ()#line:516
