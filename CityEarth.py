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
@ 版本  0.7
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
        O00O000OOO0000OOO =os_qinglong ()#line:7
        print (f"==========共找到{len(O00O000OOO0000OOO)}个账号==========")#line:8
        for O00OOOOOOOO000OOO in O00O000OOO0000OOO :#line:9
            print (f"------------正在执行第{O00O000OOO0000OOO.index(O00OOOOOOOO000OOO) + 1}个账号------------")#line:10
            O0O0OO00OOOO00000 =CityEarth (O00OOOOOOOO000OOO )#line:11
            if O0O0OO00OOOO00000 .base_info ():#line:13
                O0O0OO00OOOO00000 .friends_invitation ()#line:18
                O0O0OO00OOOO00000 .add_clover ()#line:20
                O0O0OO00OOOO00000 .energy ()#line:22
                O0O0OO00OOOO00000 .synthetic ()#line:24
                O0O0OO00OOOO00000 .propsraffle ()#line:26
                O0O0OO00OOOO00000 .crops_illustrated ()#line:28
                O0O0OO00OOOO00000 .give_gold ()#line:30
            else :#line:31
                print ('token失效')#line:32
            time .sleep (time_xx )#line:34
    except Exception as OOO0O0O00OO0O00O0 :#line:35
        print (OOO0O0O00OO0O00O0 )#line:36
def sign (O000000OOO0OO0O00 ):#line:38
    O000OOO00000O0000 =hashlib .md5 (O000000OOO0OO0O00 .encode ()).hexdigest ()#line:39
    OO00O00O0000OOO00 ="scsc%^&*"+O000OOO00000O0000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:40
    OOO00O00OOOO0OOO0 =hashlib .md5 (OO00O00O0000OOO00 .encode ()).hexdigest ()#line:41
    return OOO00O00OOOO0OOO0 #line:42
def timi_new ():#line:44
    return str (int (time .time ()*1000 ))#line:45
class CityEarth :#line:48
    def __init__ (O0O0O0O0OO0O0O000 ,OO0O00000O0000000 ):#line:50
        try :#line:51
            O0O0O0O0OO0O0O000 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:52
            O0O0O0O0OO0O0O000 .token =OO0O00000O0000000 .split ('&')[0 ]#line:53
            O0O0O0O0OO0O0O000 .innerId =OO0O00000O0000000 .split ('&')[1 ]#line:54
            O0O0O0O0OO0O0O000 .doneeNo =OO0O00000O0000000 .split ('&')[2 ]#line:55
        except :#line:56
            print ('变量格式错误')#line:57
    def base_info (O00O0OOO0O00O00OO ):#line:60
        global level #line:61
        try :#line:62
            O00O0O000OOOOO000 =f'__{timi_new()}'#line:63
            OO000O0O00OOOOOO0 ={'authorization':O00O0OOO0O00O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O000OOOOO000 ),'signstring':O00O0O000OOOOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:72
            O0O0OO00000O00OOO =requests .request ('get',f'{host}/user',headers =OO000O0O00OOOOOO0 ).json ()#line:73
            if 'status'in O0O0OO00000O00OOO :#line:75
                if O0O0OO00000O00OOO ['status']==200 :#line:76
                    OOOOOOO000OOO0O0O =O0O0OO00000O00OOO ['data']['nickname']#line:77
                    O000000OO0OOOO0OO =O0O0OO00000O00OOO ['data']['inner_id']#line:78
                    OO0OOOO000000OO00 =O0O0OO00000O00OOO ['data']['assets']['gold']#line:79
                    level =O0O0OO00000O00OOO ['data']['level']#line:80
                    print (f'【账号信息】:昵称:{OOOOOOO000OOO0O0O}丨ID:{str(O000000OO0OOOO0OO)[:3] + "**"+ str(O000000OO0OOOO0OO)[5:]}丨等级:{level}丨种子:{str(OO0OOOO000000OO00).split(".")[0]}')#line:81
                if O0O0OO00000O00OOO ['status']==401 :#line:82
                    return False #line:83
                if O0O0OO00000O00OOO ['status']==500 :#line:84
                    return False #line:85
            return True #line:86
        except Exception as OOOOOO0O0OO00O0O0 :#line:87
            print (OOOOOO0O0OO00O0O0 )#line:88
    def give_gold (O00OOO0O0O0O0O0OO ):#line:91
        OOOOO00OO0OOOO000 =f'__{timi_new()}'#line:92
        O0O000000O0OO0OOO ={'authorization':O00OOO0O0O0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OO0OOOO000 ),'signstring':OOOOO00OO0OOOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:101
        OO000OO00O00O00O0 =requests .request ('get',f'{host}/user',headers =O0O000000O0OO0OOO ).json ()#line:102
        if 'status'in OO000OO00O00O00O0 :#line:103
            if OO000OO00O00O00O0 ['status']==200 :#line:104
                print (O00OOO0O0O0O0O0OO .doneeNo )#line:105
                if float (O00OOO0O0O0O0O0OO .doneeNo )!=0 :#line:106
                    OO0O00OO0O00O00OO =OO000OO00O00O00O0 ['data']['assets']['gold']#line:107
                    if float (OO0O00OO0O00O00OO )>2 :#line:108
                        O000OO00000OOO0O0 =int (float (OO0O00OO0O00O00OO )/1.1 )#line:109
                        OOOOO00OO0OOOO000 =f'_doneeNo={O00OOO0O0O0O0O0OO.doneeNo}&quantity={O000OO00000OOO0O0}_{timi_new()}'#line:110
                        O0O000000O0OO0OOO ={'authorization':O00OOO0O0O0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OO0OOOO000 ),'signstring':OOOOO00OO0OOOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
                        OOO00O000O0000OO0 ={"quantity":O000OO00000OOO0O0 ,"doneeNo":O00OOO0O0O0O0O0OO .doneeNo }#line:123
                        O000OOOO0000OOO00 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O000000O0OO0OOO ,data =OOO00O000O0000OO0 ).json ()#line:124
                        print (O000OOOO0000OOO00 )#line:125
                        if 'status'in O000OOOO0000OOO00 :#line:126
                            if O000OOOO0000OOO00 ['status']==200 :#line:127
                                if O000OOOO0000OOO00 ['data']:#line:128
                                    print (f'【赠送种子】:赠送{O000OO00000OOO0O0}种子给{O00OOO0O0O0O0O0OO.doneeNo}成功')#line:129
                    print (f'【赠送种子】:余额不足未启动赠送功能')#line:130
                else :#line:131
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:132
    def winning_rewards (OO0000O0O0O00O0OO ):#line:134
        O000O00O000OO0O0O =f'__{timi_new()}'#line:135
        OOO0O0OOO000OO0OO ={'authorization':OO0000O0O0O00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00O000OO0O0O ),'signstring':O000O00O000OO0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:144
        O00OOO00000OO0O00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO0O0OOO000OO0OO ).json ()#line:145
        if 'status'in O00OOO00000OO0O00 :#line:147
            if O00OOO00000OO0O00 ['status']==200 :#line:148
                if O00OOO00000OO0O00 ['data']['amount']:#line:149
                    O00O0OO00OO0OO00O =O00OOO00000OO0O00 ['data']['amount']['gold']#line:150
                    return O00O0OO00OO0OO00O #line:151
                else :#line:152
                    return 0 #line:153
    def certification (OO0O000OOOOOOOO00 ):#line:155
        OO0OO0000O000O0O0 =f'__{timi_new()}'#line:156
        O0OO0OO00O00OOO0O ={'authorization':OO0O000OOOOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0000O000O0O0 ),'signstring':OO0OO0000O000O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:165
        O000O0000O0O00O0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0OO0OO00O00OOO0O ).json ()#line:166
        if 'status'in O000O0000O0O00O0O :#line:168
            if O000O0000O0O00O0O ['status']==200 :#line:169
                if O000O0000O0O00O0O ['data']['result']:#line:170
                    OOOOO00O00O0O000O =O000O0000O0O00O0O ['data']['nick_name']#line:171
                    return OOOOO00O00O0O000O #line:172
                else :#line:173
                    return '未实名'#line:174
    def crops_illustrated (OO0O0OOO0OOO000O0 ):#line:177
        O0000O00O00OOO00O =f'__{timi_new()}'#line:178
        O0OO0OOOO0O0O00OO ={'authorization':OO0O0OOO0OOO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00O00OOO00O ),'signstring':O0000O00O00OOO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:187
        OOOO0O0OO0O0OO0OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OO0OOOO0O0O00OO ).json ()#line:188
        if 'status'in OOOO0O0OO0O0OO0OO :#line:190
            if OOOO0O0OO0O0OO0OO ['status']==200 :#line:191
                OO0O0OOOOOOOOOO00 =OOOO0O0OO0O0OO0OO ['data'][0 ]['crops']#line:192
                for O0OOOO000O0O00O0O in OO0O0OOOOOOOOOO00 :#line:193
                    if O0OOOO000O0O00O0O ['ill_clover_award']:#line:194
                        if float (O0OOOO000O0O00O0O ['ill_clover_award'])>1 :#line:195
                            if O0OOOO000O0O00O0O ['is_finish']:#line:196
                                if not O0OOOO000O0O00O0O ['is_getit']:#line:197
                                    O0000O00O00OOO00O =f'_award_level={O0OOOO000O0O00O0O["level"]}_{timi_new()}'#line:198
                                    O0OO0OOOO0O0O00OO ={'authorization':OO0O0OOO0OOO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00O00OOO00O ),'signstring':O0000O00O00OOO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
                                    O00O0000O0O0OO00O ={"award_level":O0OOOO000O0O00O0O ['level']}#line:208
                                    OO0O0OOO0OOOOO000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OO0OOOO0O0O00OO ,json =O00O0000O0O0OO00O ).json ()#line:209
                                    if 'status'in OO0O0OOO0OOOOO000 :#line:210
                                        if OO0O0OOO0OOOOO000 ['status']==200 :#line:211
                                            OOO0OOO00O00O000O =OO0O0OOO0OOOOO000 ['data']['ill_clover_award']#line:212
                                            print (f'【图鉴奖励】:领取{O0OOOO000O0O00O0O["crop_name"]}成就丨奖励{OOO0OOO00O00O000O}叶子成功')#line:213
                                        if OO0O0OOO0OOOOO000 ['status']==500 :#line:214
                                            print (f'【图鉴奖励】:{OO0O0OOO0OOOOO000["message"]}')#line:215
    def watched_ad (O0OOO0O0O00O0OOO0 ):#line:218
        OO000O00O00O0O000 =f'__{timi_new()}'#line:219
        OOO0000O0O00OO00O ={'authorization':O0OOO0O0O00O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00O00O0O000 ),'signstring':OO000O00O00O0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:228
        O000O00O0O00OOOOO =requests .request ('post',f'{host}/game/watched-ad',headers =OOO0000O0O00OO00O ).json ()#line:229
        print (O000O00O0O00OOOOO )#line:230
    def user_ad (O0O0O0OOOOOOO00O0 ):#line:236
        OO00O0OO0O00O000O =f'__{timi_new()}'#line:237
        O0O000O0OOO000000 ={'authorization':O0O0O0OOOOOOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OO0O00O000O ),'signstring':OO00O0OO0O00O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:246
        OOO00OOOOOO0O00OO =requests .request ('get',f'{host}/user/ad',headers =O0O000O0OOO000000 ).json ()#line:247
        if 'status'in OOO00OOOOOO0O00OO :#line:249
            if OOO00OOOOOO0O00OO ['status']==200 :#line:250
                OO00OOO00O000OO0O =OOO00OOOOOO0O00OO ['data']['max_time']#line:251
                OOOOO0O0OO00O0O00 =OOO00OOOOOO0O00OO ['data']['watch_time']#line:252
                OOOO000000O0O0O0O =OOO00OOOOOO0O00OO ['data']['added_time']#line:253
                print (f'【获取种子】:获取种子剩余{OOOO000000O0O0O0O + OO00OOO00O000OO0O - OOOOO0O0OO00O0O00}次丨好友提供:{OOOO000000O0O0O0O}次')#line:254
                if OOOO000000O0O0O0O +OO00OOO00O000OO0O -OOOOO0O0OO00O0O00 >0 :#line:255
                    time .sleep (random .randint (16 ,19 ))#line:256
                    OOO00O0O0O0OOO0O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O000O0OOO000000 ).json ()#line:257
                    if 'status'in OOO00O0O0O0OOO0O0 :#line:259
                        if OOO00O0O0O0OOO0O0 ['status']==200 :#line:260
                            OOOOO0000O0OOO000 =OOO00O0O0O0OOO0O0 ['data']['silver']#line:261
                            print (f'【获取种子】:获得种子:{OOOOO0000O0OOO000}')#line:262
                            return True #line:263
                        if OOO00O0O0O0OOO0O0 ['status']==500 :#line:264
                            OOOOO0O0OO00OO00O =OOO00O0O0O0OOO0O0 ['message']#line:265
                            print (f'【获取种子】:{OOOOO0O0OO00OO00O}')#line:266
                            return False #line:267
    def synthetic (OOOO00O0OOO0000OO ):#line:270
        global id ,g #line:271
        try :#line:272
            while True :#line:274
                OO00O0O00OO0OOOO0 =f'__{timi_new()}'#line:275
                O0O00OO00O00O0OO0 ={'authorization':OOOO00O0OOO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O00OO0OOOO0 ),'signstring':OO00O0O00OO0OOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:284
                O0OOOO0O0OOOOOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O00OO00O00O0OO0 ).json ()#line:285
                if 'status'in O0OOOO0O0OOOOOOO0 :#line:287
                    if O0OOOO0O0OOOOOOO0 ['status']==200 :#line:288
                        O0O000O00O0O0O0O0 =O0OOOO0O0OOOOOOO0 ['data']['cropList']#line:289
                        O0O0O000OO00O00OO =O0OOOO0O0OOOOOOO0 ['data']['gameCoreDataDBid']#line:290
                        O0O0O0OOO0OOO0OO0 =0 #line:291
                        for OO0O0OOO000O00OOO in O0O000O00O0O0O0O0 :#line:292
                            if not OO0O0OOO000O00OOO :#line:293
                                O0O000OOOO0000000 =f'_crop_id={O0O0O000OO00O00OO}&site={O0O0O0OOO0OOO0OO0}_{OOOO00O0OOO0000OO.time}'#line:294
                                OO00OO0OO00O00OOO ={'authorization':OOOO00O0OOO0000OO .token ,'timestamp':OOOO00O0OOO0000OO .time ,'sign':sign (O0O000OOOO0000000 ),'signstring':O0O000OOOO0000000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:303
                                O000OO000O0OO0OO0 ={"site":O0O0O0OOO0OOO0OO0 ,"crop_id":O0O0O000OO00O00OO }#line:304
                                OO0000OOO0OOO0O0O =requests .request ('post',f'{host}/game/crops/buy',headers =OO00OO0OO00O00OOO ,data =O000OO000O0OO0OO0 ).json ()#line:305
                                time .sleep (random .randint (1 ,3 )/10 )#line:307
                                if 'status'in OO0000OOO0OOO0O0O :#line:308
                                    if OO0000OOO0OOO0O0O ['status']==200 :#line:309
                                        if OO0000OOO0OOO0O0O ['message']=='种子数量不足':#line:310
                                            print (f'【购买合成】:{OO0000OOO0OOO0O0O["message"]}')#line:311
                                            if not OOOO00O0OOO0000OO .user_ad ():#line:312
                                                return False #line:313
                                        print (f'【购买合成】:购买农作物,位置{O0O0O0OOO0OOO0OO0}')#line:314
                                    if OO0000OOO0OOO0O0O ['status']==500 :#line:315
                                        print (f'【购买合成】:{OO0000OOO0OOO0O0O["message"]}')#line:316
                                        return False #line:317
                            O0O0O0OOO0OOO0OO0 +=1 #line:318
                        O0000OO0O0OO0O000 =requests .request ('get',f'{host}/game/getAllData',headers =O0O00OO00O00O0OO0 ).json ()#line:319
                        O0O00O00OOO00OO00 =O0000OO0O0OO0O000 ['data']['cropList']#line:320
                        OOOOO0O00OO00O00O =False #line:321
                        for OO0O0OOO000O00OOO in range (12 ):#line:322
                            id =O0O00O00OOO00OO00 [OO0O0OOO000O00OOO ]['level']#line:323
                            if int (level )-int (id )>9 :#line:324
                                OOOOOO0O0O00000OO =f'_site={OO0O0OOO000O00OOO}_{timi_new()}'#line:325
                                OO00OO00000O0OOOO ={'accept':'application/json, text/plain, */*','authorization':OOOO00O0OOO0000OO .token ,'timestamp':timi_new (),'sign':sign (OOOOOO0O0O00000OO ),'signstring':OOOOOO0O0O00000OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:335
                                O00OO0OO00O000OO0 ={"site":OO0O0OOO000O00OOO }#line:336
                                OO000OOOO0000OOOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO00OO00000O0OOOO ,data =O00OO0OO00O000OO0 ).json ()#line:337
                                if 'status'in OO000OOOO0000OOOO :#line:339
                                    if OO000OOOO0000OOOO ['status']==200 :#line:340
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:341
                            if id !=0 :#line:342
                                for OOOOOOO0OOO0O0O00 in range (11 ):#line:343
                                    OO0O000O0O0000O0O =OOOOOOO0OOO0O0O00 +1 #line:344
                                    g =O0O00O00OOO00OO00 [OO0O000O0O0000O0O ]['level']#line:345
                                    if id ==g :#line:346
                                        O0OO00OOO0O00O000 =OOOOOOO0OOO0O0O00 +2 #line:347
                                        if O0OO00OOO0O00O000 ==OO0O0OOO000O00OOO +1 :#line:348
                                            pass #line:349
                                        else :#line:350
                                            O0O0O00O00O0OOOOO =OO0O0OOO000O00OOO +1 #line:351
                                            time .sleep (random .randint (1 ,3 )/10 )#line:353
                                            O0O0OO0OOOO0O0OOO =f'_site={O0O0O00O00O0OOOOO-1}&targetSite={O0OO00OOO0O00O000-1}_{timi_new()}'#line:354
                                            OO000O000OOO0OO0O ={'accept':'application/json, text/plain, */*','authorization':OOOO00O0OOO0000OO .token ,'timestamp':timi_new (),'sign':sign (O0O0OO0OOOO0O0OOO ),'signstring':O0O0OO0OOOO0O0OOO ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:369
                                            O0OOO0O0OOOOO0O0O ={"site":int (O0O0O00O00O0OOOOO -1 ),"targetSite":int (O0OO00OOO0O00O000 -1 )}#line:370
                                            O0O0O0O00O0O00O00 =requests .request ('post',f'{host}/game/crops/move',headers =OO000O000OOO0OO0O ,json =O0OOO0O0OOOOO0O0O ).json ()#line:371
                                            if 'status'in O0O0O0O00O0O00O00 :#line:372
                                                if O0O0O0O00O0O00O00 ['status']==200 :#line:373
                                                    pass #line:374
                                            print ('【购买合成】:',O0O0O00O00O0OOOOO ,O0OO00OOO0O00O000 ,'合成成功')#line:376
                                            OOOOO0O00OO00O00O =True #line:377
                                    if OOOOO0O00OO00O00O :#line:378
                                        break #line:379
                                if OOOOO0O00OO00O00O :#line:380
                                    break #line:381
        except Exception as OOO0O0OO00O0O0OOO :#line:382
            OOOO00O0OOO0000OO .synthetic ()#line:383
    def propsraffle (OOOO0OOO000000000 ):#line:387
        try :#line:388
            while True :#line:389
                OO00OO000000O0000 =f'__{timi_new()}'#line:390
                O00O0OOO000O0O000 ={'authorization':OOOO0OOO000000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO000000O0000 ),'signstring':OO00OO000000O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:399
                OO000O0OOO0O000O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00O0OOO000O0O000 ).json ()#line:400
                if 'status'in OO000O0OOO0O000O0 :#line:402
                    if OO000O0OOO0O000O0 ['status']==200 :#line:403
                        OOO0O000O00O0OO00 =OO000O0OOO0O000O0 ['data']['rows']#line:404
                        O00O000OO00O0O0OO =OO000O0OOO0O000O0 ['data']['vstate']#line:405
                        if OOO0O000O00O0OO00 ==5 or OOO0O000O00O0OO00 ==6 or OOO0O000O00O0OO00 ==7 :#line:406
                            OO0OOO0O000O0000O =OO000O0OOO0O000O0 ['data']['silver']#line:407
                            print (f'【转盘抽奖】:获得种子:{OO0OOO0O000O0000O}')#line:408
                        if OOO0O000O00O0OO00 ==1 or OOO0O000O00O0OO00 ==2 or OOO0O000O00O0OO00 ==3 :#line:409
                            O00O0OOOO000O0O0O =OO000O0OOO0O000O0 ['data']['clover']#line:410
                            print (f'【转盘抽奖】:获得三叶草:{O00O0OOOO000O0O0O}')#line:411
                        if OOO0O000O00O0OO00 ==4 or OOO0O000O00O0OO00 ==8 :#line:412
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:413
                        if OOO0O000O00O0OO00 =='抽奖次数已用完':#line:417
                            if O00O000OO00O0O0OO :#line:418
                                OOOOOOOOO00OO00O0 =random .randint (160 ,190 )/10 #line:419
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{OOOOOOOOO00OO00O0}秒获取抽奖机会')#line:420
                                time .sleep (OOOOOOOOO00OO00O0 )#line:421
                                OO0O0OO00OOOOO0OO =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O00O0OOO000O0O000 ).json ()#line:422
                                if 'status'in OO0O0OO00OOOOO0OO :#line:424
                                    if OO0O0OO00OOOOO0OO ['status']==200 :#line:425
                                        print (f'【转盘抽奖】:{OO0O0OO00OOOOO0OO["message"]}')#line:426
                                    if OO0O0OO00OOOOO0OO ['status']==500 :#line:427
                                        print (f'【转盘抽奖】:{OO0O0OO00OOOOO0OO["message"]}')#line:428
                                        break #line:429
                                time .sleep (random .randint (10 ,15 )/10 )#line:430
                            else :#line:431
                                break #line:432
                time .sleep (random .randint (8 ,15 )/10 )#line:433
        except Exception as OOO00O0OOO0O0O000 :#line:434
            print (OOO00O0OOO0O0O000 )#line:435
    def friends_invitation (OO0O00000O000O000 ):#line:438
        try :#line:439
            O00OO0OOO0000000O =f'__{timi_new()}'#line:440
            O00O00OOO0O0OOO00 ={'authorization':OO0O00000O000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OOO0000000O ),'signstring':O00OO0OOO0000000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:449
            OOO000OOOO0O000OO =requests .request ('get',f'{host}/friends',headers =O00O00OOO0O0OOO00 ).json ()#line:450
            if 'status'in OOO000OOOO0O000OO :#line:451
                if OOO000OOOO0O000OO ['status']==200 :#line:452
                    O00OOO0O00OOOO0OO =OOO000OOOO0O000OO ['data']['myInviteter']#line:453
                    if O00OOO0O00OOOO0OO :#line:454
                        OO0OOOOO00OOO0OOO =O00OOO0O00OOOO0OO ['user']['nickname']#line:455
                        OO0OO0OOO0OO000O0 =OO0O00000O000O000 .certification ()#line:456
                        print (f'【绑邀请码】:我的邀请人:{OO0OOOOO00OOO0OOO}丨实名:{OO0OO0OOO0OO000O0}')#line:457
                    else :#line:458
                        if OO0O00000O000O000 .innerId !='0':#line:459
                            O00OO0OOO0000000O =f'_innerId={OO0O00000O000O000.innerId}_{timi_new()}'#line:460
                            O00O00OOO0O0OOO00 ={'authorization':OO0O00000O000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OOO0000000O ),'signstring':O00OO0OOO0000000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:469
                            O000OO0OOO0O0O0O0 ={"innerId":OO0O00000O000O000 .innerId }#line:470
                            O0O00OO000O0OOO00 =requests .request ('post',f'{host}/friends/my-invitation',headers =O00O00OOO0O0OOO00 ,data =O000OO0OOO0O0O0O0 ).json ()#line:471
                            if 'status'in O0O00OO000O0OOO00 :#line:472
                                if O0O00OO000O0OOO00 ['status']==200 :#line:473
                                    print (f'【绑邀请码】:{OO0O00000O000O000.innerId}{O0O00OO000O0OOO00["message"]}')#line:474
                        else :#line:475
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:476
        except Exception as O0OO0000OOO0O000O :#line:477
            print (O0OO0000OOO0O000O )#line:478
    def add_clover (O000OOO000O00OOOO ):#line:482
        try :#line:483
            O0O0O0000OO0OO000 =f'__{timi_new()}'#line:484
            OO0OO0O00O00O00O0 ={'authorization':O000OOO000O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0000OO0OO000 ),'signstring':O0O0O0000OO0OO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:493
            OOOO00O000000O000 =requests .request ('get',f'{host}/assets/clovers',headers =OO0OO0O00O00O00O0 ).json ()#line:494
            if 'status'in OOOO00O000000O000 :#line:496
                if OOOO00O000000O000 ['status']==200 :#line:497
                    OOO0O000O0O0OO0OO =OOOO00O000000O000 ['data']['clover']#line:498
                    OO000OOO00000OO0O =OOOO00O000000O000 ['data']['used_clover']#line:499
                    O00000O0O0O0O00O0 =float (OOO0O000O0O0OO0OO )-float (OO000OOO00000OO0O )#line:500
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OO000OOO00000OO0O}')#line:501
                    if O00000O0O0O0O00O0 >1 :#line:502
                        O0O0O0000OO0OO000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00000O0O0O0O00O0)}_{timi_new()}'#line:503
                        OO0OO0O00O00O00O0 ={'authorization':O000OOO000O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0000OO0OO000 ),'signstring':O0O0O0000OO0OO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
                        OOOOO0O0000O00O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00000O0O0O0O00O0 )}#line:513
                        OOOO0OO00O000OO00 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0OO0O00O00O00O0 ,data =OOOOO0O0000O00O0O ).json ()#line:514
                        if 'status'in OOOO0OO00O000OO00 :#line:516
                            if OOOO0OO00O000OO00 ['status']==200 :#line:517
                                print (f'【参与抽奖】:添加三叶草:{OOOO0OO00O000OO00["data"]}丨数量:{O00000O0O0O0O00O0}')#line:518
            O0000OO0OOOO0O00O =requests .request ('get',f'{host}/lottery',headers =OO0OO0O00O00O00O0 ).json ()#line:519
            OO0O00OO0O0OO0O00 =O000OOO000O00OOOO .winning_rewards ()#line:521
            if 'status'in O0000OO0OOOO0O00O :#line:522
                if O0000OO0OOOO0O00O ['status']==200 :#line:523
                    O0OO00O0O0O0OO0OO =O0000OO0OOOO0O00O ['data'][0 ]['day_get_gold_quantity']#line:524
                    print (f'【参与抽奖】:预计每天中{O0OO00O0O0O0OO0OO[:6]}种子丨好友收益:{OO0O00OO0O0OO0O00}')#line:525
        except Exception as OO0O0000OOO0O0O00 :#line:526
            print (OO0O0000OOO0O0O00 )#line:527
    def energy (OO00O00OO0O00O000 ):#line:530
        O000OOO0OOOO000OO =f'__{timi_new()}'#line:531
        OOOO00O0OOOO0000O ={'authorization':OO00O00OO0O00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0OOOO000OO ),'signstring':O000OOO0OOOO000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:540
        O0O0O0OOO00O0O0O0 =requests .request ('get',f'{host}/energy/general',headers =OOOO00O0OOOO0000O ).json ()#line:541
        if 'status'in O0O0O0OOO00O0O0O0 :#line:543
            if O0O0O0OOO00O0O0O0 ['status']==200 :#line:544
                O0O0OO00OO00O0000 =O0O0O0OOO00O0O0O0 ['data']['ordinary_water_consumptions']#line:545
                if float (O0O0OO00OO00O0000 )<80 :#line:546
                    O0000000000000O0O =99 -float (O0O0OO00OO00O0000 )#line:547
                    O000OO0O0O0OOO000 ={"fertilizer":str (O0000000000000O0O ).split ('.')[0 ]}#line:548
                    OOOO00OO00O0O0O00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOO00O0OOOO0000O ,data =O000OO0O0O0OOO000 ).json ()#line:549
                    if 'status'in OOOO00OO00O0O0O00 :#line:551
                        if OOOO00OO00O0O0O00 ['status']==200 :#line:552
                            print (f'【购买肥料】:{OOOO00OO00O0O0O00["message"]}')#line:553
                OO0O00OOO0OO00OO0 =O0O0O0OOO00O0O0O0 ['data']['ordinary_water_consumptions']#line:554
                if float (OO0O00OOO0OO00OO0 )<800 :#line:555
                    O0000O00OO0OOO00O =999 -float (OO0O00OOO0OO00OO0 )#line:556
                    O0O0O0000OO0O0OO0 ={"water":str (O0000O00OO0OOO00O ).split ('.')[0 ]}#line:557
                    O0OOOOO00O0000O00 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOO00O0OOOO0000O ,data =O0O0O0000OO0O0OO0 ).json ()#line:558
                    if 'status'in O0OOOOO00O0000O00 :#line:559
                        if O0OOOOO00O0000O00 ['status']==200 :#line:560
                            print (f'【购买水滴】:{O0OOOOO00O0000O00["message"]}')#line:561
def version_of_the_validation ():#line:567
    return str ((63 -56 )/10 )#line:568
def gitee_validation ():#line:570
    try :#line:571
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:572
    except Exception as OOO00O00O000O00OO :#line:573
        sys .exit (0 )#line:574
def update_the_validation ():#line:580
    try :#line:581
        O0O0O00OO0000OOOO =gitee_validation ()#line:582
        if version_of_the_validation ()<O0O0O00OO0000OOOO ['CityEarth']['edition']:#line:583
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0O00OO0000OOOO["CityEarth"]["edition"]}   ❌')#line:584
            print (f'更新内容=>>{O0O0O00OO0000OOOO["CityEarth"]["content"]}   👍')#line:585
        else :#line:586
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0O00OO0000OOOO["CityEarth"]["edition"]}   ✅')#line:587
            print (f'更新内容=>> {O0O0O00OO0000OOOO["CityEarth"]["content"]}   👍')#line:588
    except Exception as OO0O0000O0000O000 :#line:589
        print (OO0O0000O0000O000 )#line:590
def os_qinglong ():#line:593
    if application in os .environ :#line:594
        OOOO000OO0OOOOO0O =os .environ [application ].split ('\n')#line:595
        if len (OOOO000OO0OOOOO0O )>0 :#line:596
            return OOOO000OO0OOOOO0O #line:597
        else :#line:598
            print (f"{application}变量未启用")#line:599
            print ('脚本退出')#line:600
            sys .exit (1 )#line:601
    else :#line:602
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:603
        return os_built ()#line:604
def os_built ():#line:607
    if token :#line:608
        OOOO0O0OOO0OOOO00 =token .split ('\n')#line:609
        if len (OOOO0O0OOO0OOOO00 )>0 :#line:610
            return OOOO0O0OOO0OOOO00 #line:611
    else :#line:612
        print (f"内置变量为空")#line:613
        print ('脚本结束')#line:614
        sys .exit (0 )#line:615
if __name__ =='__main__':#line:618
    start ()#line:619
