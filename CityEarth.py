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
        O0OO00OOO00O00O0O =os_qinglong ()#line:7
        print (f"==========共找到{len(O0OO00OOO00O00O0O)}个账号==========")#line:8
        for O00OO0OOOOO0O00O0 in O0OO00OOO00O00O0O :#line:9
            print (f"------------正在执行第{O0OO00OOO00O00O0O.index(O00OO0OOOOO0O00O0) + 1}个账号------------")#line:10
            OO0OO00O0O0OOO0OO =CityEarth (O00OO0OOOOO0O00O0 )#line:11
            if OO0OO00O0O0OOO0OO .base_info ():#line:13
                OO0OO00O0O0OOO0OO .friends_invitation ()#line:18
                OO0OO00O0O0OOO0OO .winning_rewards ()#line:20
                OO0OO00O0O0OOO0OO .add_clover ()#line:22
                OO0OO00O0O0OOO0OO .energy ()#line:24
                OO0OO00O0O0OOO0OO .synthetic ()#line:26
                OO0OO00O0O0OOO0OO .propsraffle ()#line:28
                OO0OO00O0O0OOO0OO .crops_illustrated ()#line:30
            else :#line:31
                print ('token失效')#line:32
            time .sleep (time_xx )#line:34
    except Exception as O00O000OO0000O0O0 :#line:35
        print (O00O000OO0000O0O0 )#line:36
def sign (O0OO0OOOO0O00O0O0 ):#line:38
    O00OOO0OOOO0OO0O0 =hashlib .md5 (O0OO0OOOO0O00O0O0 .encode ()).hexdigest ()#line:39
    OOOO0OO00OOO00OO0 ="scsc%^&*"+O00OOO0OOOO0OO0O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:40
    OO0O0O00OOOO0000O =hashlib .md5 (OOOO0OO00OOO00OO0 .encode ()).hexdigest ()#line:41
    return OO0O0O00OOOO0000O #line:42
def timi_new ():#line:44
    return str (int (time .time ()*1000 ))#line:45
class CityEarth :#line:48
    def __init__ (O0OOO0O0O000O0OO0 ,O0O0OOOOO0OO00OO0 ):#line:50
        try :#line:51
            O0OOO0O0O000O0OO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:52
            O0OOO0O0O000O0OO0 .token =O0O0OOOOO0OO00OO0 .split ('&')[0 ]#line:53
            O0OOO0O0O000O0OO0 .innerId =O0O0OOOOO0OO00OO0 .split ('&')[1 ]#line:54
        except Exception as O0O00O0O0O0O00O0O :#line:55
            print ('变量格式错误')#line:56
    def base_info (O0O00O0O00OOO0OOO ):#line:59
        global level #line:60
        try :#line:61
            O0O0OO0O0OOO0O0O0 =f'__{timi_new()}'#line:62
            O000O00O00O0O00OO ={'authorization':O0O00O0O00OOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0OOO0O0O0 ),'signstring':O0O0OO0O0OOO0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:71
            OOO0O00O00OO000O0 =requests .request ('get',f'{host}/user',headers =O000O00O00O0O00OO ).json ()#line:72
            if 'status'in OOO0O00O00OO000O0 :#line:74
                if OOO0O00O00OO000O0 ['status']==200 :#line:75
                    O000O0000OOO0000O =OOO0O00O00OO000O0 ['data']['nickname']#line:76
                    O000000OOOOO00000 =OOO0O00O00OO000O0 ['data']['inner_id']#line:77
                    OO0OO0O0OO0O000O0 =OOO0O00O00OO000O0 ['data']['assets']['gold']#line:78
                    level =OOO0O00O00OO000O0 ['data']['level']#line:79
                    print (f'【账号信息】:昵称:{O000O0000OOO0000O}丨ID:{str(O000000OOOOO00000)[:3] + "**"+ str(O000000OOOOO00000)[5:]}丨等级:{level}丨种子:{str(OO0OO0O0OO0O000O0).split(".")[0]}')#line:80
                if OOO0O00O00OO000O0 ['status']==401 :#line:81
                    return False #line:82
                if OOO0O00O00OO000O0 ['status']==500 :#line:83
                    return False #line:84
            return True #line:85
        except Exception as O0O000OO0OOO000OO :#line:86
            print (O0O000OO0OOO000OO )#line:87
    def winning_rewards (O0OOOO000O000O000 ):#line:90
        O0O00O0O0OO00O0OO =f'__{timi_new()}'#line:91
        O0O0O000O0OOO00O0 ={'authorization':O0OOOO000O000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O0OO00O0OO ),'signstring':O0O00O0O0OO00O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:100
        O00OOO0O00000OOOO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O0O000O0OOO00O0 ).json ()#line:101
        if 'status'in O00OOO0O00000OOOO :#line:103
            if O00OOO0O00000OOOO ['status']==200 :#line:104
                O00000O0O00000OO0 =O00OOO0O00000OOOO ['data']['amount']['gold']#line:105
                return O00000O0O00000OO0 #line:106
    def certification (OOO0O0OOO0OOOOO0O ):#line:109
        OOOOO00OOOO000O00 =f'__{timi_new()}'#line:110
        O00OOO000O0O0O0OO ={'authorization':OOO0O0OOO0OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OOOO000O00 ),'signstring':OOOOO00OOOO000O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
        OO00OOOO0OO0OOOO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OOO000O0O0O0OO ).json ()#line:120
        if 'status'in OO00OOOO0OO0OOOO0 :#line:122
            if OO00OOOO0OO0OOOO0 ['status']==200 :#line:123
                if OO00OOOO0OO0OOOO0 ['data']['result']:#line:124
                    OO000OO0O0OOOO000 =OO00OOOO0OO0OOOO0 ['data']['nick_name']#line:125
                    return OO000OO0O0OOOO000 #line:126
                else :#line:127
                    return '未实名'#line:128
    def crops_illustrated (OO0000O0OO0OO0OO0 ):#line:131
        O0O0OO0O0000OO000 =f'__{timi_new()}'#line:132
        O0O0OO0000000OO0O ={'authorization':OO0000O0OO0OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0000OO000 ),'signstring':O0O0OO0O0000OO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:141
        OO00O0O0O0OOO00O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O0OO0000000OO0O ).json ()#line:142
        if 'status'in OO00O0O0O0OOO00O0 :#line:144
            if OO00O0O0O0OOO00O0 ['status']==200 :#line:145
                O0O0OOOO00O00OO00 =OO00O0O0O0OOO00O0 ['data'][0 ]['crops']#line:146
                for O00OO0O0OO0OO0OO0 in O0O0OOOO00O00OO00 :#line:147
                    if O00OO0O0OO0OO0OO0 ['ill_clover_award']:#line:148
                        if float (O00OO0O0OO0OO0OO0 ['ill_clover_award'])>1 :#line:149
                            if O00OO0O0OO0OO0OO0 ['is_finish']:#line:150
                                if not O00OO0O0OO0OO0OO0 ['is_getit']:#line:151
                                    O0O0OO0O0000OO000 =f'_award_level={O00OO0O0OO0OO0OO0["level"]}_{timi_new()}'#line:152
                                    O0O0OO0000000OO0O ={'authorization':OO0000O0OO0OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0000OO000 ),'signstring':O0O0OO0O0000OO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:161
                                    OOOOO0O00000O0000 ={"award_level":O00OO0O0OO0OO0OO0 ['level']}#line:162
                                    OO00OO00O00O00000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O0OO0000000OO0O ,json =OOOOO0O00000O0000 ).json ()#line:163
                                    if 'status'in OO00OO00O00O00000 :#line:164
                                        if OO00OO00O00O00000 ['status']==200 :#line:165
                                            O0OO0000O000O0000 =OO00OO00O00O00000 ['data']['ill_clover_award']#line:166
                                            print (f'【图鉴奖励】:领取{O00OO0O0OO0OO0OO0["crop_name"]}成就丨奖励{O0OO0000O000O0000}叶子成功')#line:167
                                        if OO00OO00O00O00000 ['status']==500 :#line:168
                                            print (f'【图鉴奖励】:{OO00OO00O00O00000["message"]}')#line:169
    def watched_ad (OO0O0O0OOOO0O0O0O ):#line:172
        O0000O0O0OOOOO000 =f'__{timi_new()}'#line:173
        O0O00O0O0O00OOO00 ={'authorization':OO0O0O0OOOO0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0O0OOOOO000 ),'signstring':O0000O0O0OOOOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:182
        O0OO000OOOO000000 =requests .request ('post',f'{host}/game/watched-ad',headers =O0O00O0O0O00OOO00 ).json ()#line:183
        print (O0OO000OOOO000000 )#line:184
    def user_ad (OO0O0O00O00O00000 ):#line:190
        OOOO0000O0OO00OO0 =f'__{timi_new()}'#line:191
        O000O00O00O00OOOO ={'authorization':OO0O0O00O00O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000O0OO00OO0 ),'signstring':OOOO0000O0OO00OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:200
        O0OOO00OOOO0000OO =requests .request ('get',f'{host}/user/ad',headers =O000O00O00O00OOOO ).json ()#line:201
        if 'status'in O0OOO00OOOO0000OO :#line:203
            if O0OOO00OOOO0000OO ['status']==200 :#line:204
                OO0O0O0O000OOO000 =O0OOO00OOOO0000OO ['data']['max_time']#line:205
                O0O000000O00O0OO0 =O0OOO00OOOO0000OO ['data']['watch_time']#line:206
                O0O0OOOOO000OO0O0 =O0OOO00OOOO0000OO ['data']['added_time']#line:207
                print (f'【获取种子】:获取种子剩余{O0O0OOOOO000OO0O0 + OO0O0O0O000OOO000 - O0O000000O00O0OO0}次丨好友提供:{O0O0OOOOO000OO0O0}次')#line:208
                if O0O0OOOOO000OO0O0 +OO0O0O0O000OOO000 -O0O000000O00O0OO0 >0 :#line:209
                    time .sleep (random .randint (16 ,19 ))#line:210
                    O0000OO0000O000O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O000O00O00O00OOOO ).json ()#line:211
                    if 'status'in O0000OO0000O000O0 :#line:213
                        if O0000OO0000O000O0 ['status']==200 :#line:214
                            OO0O00O0OOOOO0O00 =O0000OO0000O000O0 ['data']['silver']#line:215
                            print (f'【获取种子】:获得种子:{OO0O00O0OOOOO0O00}')#line:216
                            return True #line:217
                        if O0000OO0000O000O0 ['status']==500 :#line:218
                            OOO0OO0OOOO00000O =O0000OO0000O000O0 ['message']#line:219
                            print (f'【获取种子】:{OOO0OO0OOOO00000O}')#line:220
                            return False #line:221
    def synthetic (O0O0OOOOO00O000OO ):#line:224
        global id ,g #line:225
        try :#line:226
            while True :#line:228
                O0O00OOO00O0O000O =f'__{timi_new()}'#line:229
                OOOOO0O0O00OO0OOO ={'authorization':O0O0OOOOO00O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO00O0O000O ),'signstring':O0O00OOO00O0O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:238
                OOOOOO00OO000OO0O =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO0O0O00OO0OOO ).json ()#line:239
                if 'status'in OOOOOO00OO000OO0O :#line:241
                    if OOOOOO00OO000OO0O ['status']==200 :#line:242
                        O0O0O000000O00000 =OOOOOO00OO000OO0O ['data']['cropList']#line:243
                        O0000O00000O00OO0 =OOOOOO00OO000OO0O ['data']['gameCoreDataDBid']#line:244
                        O0000OO0O00OO00O0 =0 #line:245
                        for O0OOOOO00OO0OO0O0 in O0O0O000000O00000 :#line:246
                            if not O0OOOOO00OO0OO0O0 :#line:247
                                O0O000OO0OO000O0O =f'_crop_id={O0000O00000O00OO0}&site={O0000OO0O00OO00O0}_{O0O0OOOOO00O000OO.time}'#line:248
                                OOO0O0O0OO0OOO000 ={'authorization':O0O0OOOOO00O000OO .token ,'timestamp':O0O0OOOOO00O000OO .time ,'sign':sign (O0O000OO0OO000O0O ),'signstring':O0O000OO0OO000O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:257
                                OO0O0OOO0O00O0OOO ={"site":O0000OO0O00OO00O0 ,"crop_id":O0000O00000O00OO0 }#line:258
                                O0000OO0OOOOOO0OO =requests .request ('post',f'{host}/game/crops/buy',headers =OOO0O0O0OO0OOO000 ,data =OO0O0OOO0O00O0OOO ).json ()#line:259
                                if 'status'in O0000OO0OOOOOO0OO :#line:261
                                    if O0000OO0OOOOOO0OO ['status']==200 :#line:262
                                        if O0000OO0OOOOOO0OO ['message']=='种子数量不足':#line:263
                                            print (f'【购买合成】:{O0000OO0OOOOOO0OO["message"]}')#line:264
                                            if not O0O0OOOOO00O000OO .user_ad ():#line:265
                                                return False #line:266
                                        print (f'【购买合成】:购买农作物,位置{O0000OO0O00OO00O0}')#line:267
                                    if O0000OO0OOOOOO0OO ['status']==500 :#line:268
                                        print (f'【购买合成】:{O0000OO0OOOOOO0OO["message"]}')#line:269
                                        return False #line:270
                            O0000OO0O00OO00O0 +=1 #line:271
                        O00OOOO00O0OOO00O =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO0O0O00OO0OOO ).json ()#line:272
                        O0O00O00O0OO0O00O =O00OOOO00O0OOO00O ['data']['cropList']#line:273
                        O0000OOOO00O0OO00 =False #line:274
                        for O0OOOOO00OO0OO0O0 in range (12 ):#line:275
                            id =O0O00O00O0OO0O00O [O0OOOOO00OO0OO0O0 ]['level']#line:276
                            if int (level )-int (id )>9 :#line:277
                                O0OOOOOOO00OO00OO =f'_site={O0OOOOO00OO0OO0O0}_{timi_new()}'#line:278
                                O0OOO0O00OO0000O0 ={'accept':'application/json, text/plain, */*','authorization':O0O0OOOOO00O000OO .token ,'timestamp':timi_new (),'sign':sign (O0OOOOOOO00OO00OO ),'signstring':O0OOOOOOO00OO00OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:288
                                OO0O00OO000OOOO0O ={"site":O0OOOOO00OO0OO0O0 }#line:289
                                OO000O00O0O0OO0O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OOO0O00OO0000O0 ,data =OO0O00OO000OOOO0O ).json ()#line:290
                                if 'status'in OO000O00O0O0OO0O0 :#line:292
                                    if OO000O00O0O0OO0O0 ['status']==200 :#line:293
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:294
                            if id !=0 :#line:295
                                for O000OO0000O00000O in range (11 ):#line:296
                                    OOOOO0OO0O00O000O =O000OO0000O00000O +1 #line:297
                                    g =O0O00O00O0OO0O00O [OOOOO0OO0O00O000O ]['level']#line:298
                                    if id ==g :#line:299
                                        OOOO0OOOO0O00O00O =O000OO0000O00000O +2 #line:300
                                        if OOOO0OOOO0O00O00O ==O0OOOOO00OO0OO0O0 +1 :#line:301
                                            pass #line:302
                                        else :#line:303
                                            O0O00O00OO000O0OO =O0OOOOO00OO0OO0O0 +1 #line:304
                                            O000OOO0O00O000OO =f'_site={O0O00O00OO000O0OO-1}&targetSite={OOOO0OOOO0O00O00O-1}_{timi_new()}'#line:307
                                            OOO00O0OO0OO0OO00 ={'accept':'application/json, text/plain, */*','authorization':O0O0OOOOO00O000OO .token ,'timestamp':timi_new (),'sign':sign (O000OOO0O00O000OO ),'signstring':O000OOO0O00O000OO ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:322
                                            O0O00OO00O00OOO00 ={"site":int (O0O00O00OO000O0OO -1 ),"targetSite":int (OOOO0OOOO0O00O00O -1 )}#line:323
                                            O0OO0O0O0OOOO0OO0 =requests .request ('post',f'{host}/game/crops/move',headers =OOO00O0OO0OO0OO00 ,json =O0O00OO00O00OOO00 ).json ()#line:324
                                            if 'status'in O0OO0O0O0OOOO0OO0 :#line:325
                                                if O0OO0O0O0OOOO0OO0 ['status']==200 :#line:326
                                                    pass #line:327
                                            print ('【购买合成】:',O0O00O00OO000O0OO ,OOOO0OOOO0O00O00O ,'合成成功')#line:329
                                            O0000OOOO00O0OO00 =True #line:330
                                    if O0000OOOO00O0OO00 :#line:331
                                        break #line:332
                                if O0000OOOO00O0OO00 :#line:333
                                    break #line:334
        except Exception as O0O0000O0O0O0OOOO :#line:335
            O0O0OOOOO00O000OO .synthetic ()#line:336
    def propsraffle (OO0OO00O0OOOOO0O0 ):#line:340
        try :#line:341
            while True :#line:342
                O000000O0OOO0O0OO =f'__{timi_new()}'#line:343
                O0OO0O0O000OO0OO0 ={'authorization':OO0OO00O0OOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O0OOO0O0OO ),'signstring':O000000O0OOO0O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:352
                OOO0OO0OOO0O0OO0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OO0O0O000OO0OO0 ).json ()#line:353
                if 'status'in OOO0OO0OOO0O0OO0O :#line:355
                    if OOO0OO0OOO0O0OO0O ['status']==200 :#line:356
                        O00000OO00OOOO0O0 =OOO0OO0OOO0O0OO0O ['data']['rows']#line:357
                        O0O000OO00O00OO00 =OOO0OO0OOO0O0OO0O ['data']['vstate']#line:358
                        if O00000OO00OOOO0O0 ==5 or O00000OO00OOOO0O0 ==6 or O00000OO00OOOO0O0 ==7 :#line:359
                            O0O0OOO0O00OOO0OO =OOO0OO0OOO0O0OO0O ['data']['silver']#line:360
                            print (f'【转盘抽奖】:获得种子:{O0O0OOO0O00OOO0OO}')#line:361
                        if O00000OO00OOOO0O0 ==1 or O00000OO00OOOO0O0 ==2 or O00000OO00OOOO0O0 ==3 :#line:362
                            O0O00O0OOOOO0OO0O =OOO0OO0OOO0O0OO0O ['data']['clover']#line:363
                            print (f'【转盘抽奖】:获得三叶草:{O0O00O0OOOOO0OO0O}')#line:364
                        if O00000OO00OOOO0O0 ==4 or O00000OO00OOOO0O0 ==8 :#line:365
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:366
                        if O00000OO00OOOO0O0 =='抽奖次数已用完':#line:370
                            if O0O000OO00O00OO00 :#line:371
                                OOO0000O0OO0O0OOO =random .randint (160 ,190 )/10 #line:372
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{OOO0000O0OO0O0OOO}秒获取抽奖机会')#line:373
                                time .sleep (OOO0000O0OO0O0OOO )#line:374
                                O0OOO0OO0O00O000O =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O0OO0O0O000OO0OO0 ).json ()#line:375
                                if 'status'in O0OOO0OO0O00O000O :#line:377
                                    if O0OOO0OO0O00O000O ['status']==200 :#line:378
                                        print (f'【转盘抽奖】:{O0OOO0OO0O00O000O["message"]}')#line:379
                                    if O0OOO0OO0O00O000O ['status']==500 :#line:380
                                        print (f'【转盘抽奖】:{O0OOO0OO0O00O000O["message"]}')#line:381
                                        break #line:382
                                time .sleep (random .randint (10 ,15 )/10 )#line:383
                            else :#line:384
                                break #line:385
                time .sleep (random .randint (8 ,15 )/10 )#line:386
        except Exception as OO00O0000OOO00O00 :#line:387
            print (OO00O0000OOO00O00 )#line:388
    def friends_invitation (OOOO0O0OOOOOO0O00 ):#line:391
        try :#line:392
            OO000OOO0000OOOO0 =f'__{timi_new()}'#line:393
            OO0OOOO0OO00OO0O0 ={'authorization':OOOO0O0OOOOOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOO0000OOOO0 ),'signstring':OO000OOO0000OOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:402
            O0O0O0O00OOO0O00O =requests .request ('get',f'{host}/friends',headers =OO0OOOO0OO00OO0O0 ).json ()#line:403
            if 'status'in O0O0O0O00OOO0O00O :#line:404
                if O0O0O0O00OOO0O00O ['status']==200 :#line:405
                    OOOOO0O00O00OOOOO =O0O0O0O00OOO0O00O ['data']['myInviteter']#line:406
                    if OOOOO0O00O00OOOOO :#line:407
                        O0OO0OOOO0000O000 =OOOOO0O00O00OOOOO ['user']['nickname']#line:408
                        OOOO0O0OOOOO00O00 =OOOO0O0OOOOOO0O00 .certification ()#line:409
                        print (f'【绑邀请码】:我的邀请人:{O0OO0OOOO0000O000}丨实名:{OOOO0O0OOOOO00O00}')#line:410
                    else :#line:411
                        if OOOO0O0OOOOOO0O00 .innerId !='0':#line:412
                            print ('【绑邀请码】:绑定邀请码')#line:413
                            OO000O00OO0OOO0OO ={"innerId":OOOO0O0OOOOOO0O00 .innerId }#line:414
                            OOO000O0OO0OOO0OO =requests .request ('post',f'{host}/friends/my-invitation',headers =OO0OOOO0OO00OO0O0 ,data =OO000O00OO0OOO0OO ).json ()#line:415
                            print (OOO000O0OO0OOO0OO )#line:416
                        else :#line:417
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:418
        except Exception as OOOOOO0O00OOOO000 :#line:419
            print (OOOOOO0O00OOOO000 )#line:420
    def add_clover (O00O00O0000OOOOO0 ):#line:424
        try :#line:425
            O0000O00OOOOOO0OO =f'__{timi_new()}'#line:426
            OO0000O0OO000O0O0 ={'authorization':O00O00O0000OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00OOOOOO0OO ),'signstring':O0000O00OOOOOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:435
            O0OOO0O0OO0OOO0O0 =requests .request ('get',f'{host}/assets/clovers',headers =OO0000O0OO000O0O0 ).json ()#line:436
            if 'status'in O0OOO0O0OO0OOO0O0 :#line:438
                if O0OOO0O0OO0OOO0O0 ['status']==200 :#line:439
                    O0OOO00OO00OOOO00 =O0OOO0O0OO0OOO0O0 ['data']['clover']#line:440
                    OOOOOOO000OO0OO00 =O0OOO0O0OO0OOO0O0 ['data']['used_clover']#line:441
                    O0000O0O0OO00OO0O =float (O0OOO00OO00OOOO00 )-float (OOOOOOO000OO0OO00 )#line:442
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OOOOOOO000OO0OO00}')#line:443
                    if O0000O0O0OO00OO0O >1 :#line:444
                        O0000O00OOOOOO0OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0000O0O0OO00OO0O)}_{timi_new()}'#line:445
                        OO0000O0OO000O0O0 ={'authorization':O00O00O0000OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00OOOOOO0OO ),'signstring':O0000O00OOOOOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:454
                        O000OO00O000O0OO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0000O0O0OO00OO0O )}#line:455
                        O0O0OO0O0OOOOOO00 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0000O0OO000O0O0 ,data =O000OO00O000O0OO0 ).json ()#line:456
                        if 'status'in O0O0OO0O0OOOOOO00 :#line:458
                            if O0O0OO0O0OOOOOO00 ['status']==200 :#line:459
                                print (f'【参与抽奖】:添加三叶草:{O0O0OO0O0OOOOOO00["data"]}丨数量:{O0000O0O0OO00OO0O}')#line:460
            OO000O00OO0OO00O0 =requests .request ('get',f'{host}/lottery',headers =OO0000O0OO000O0O0 ).json ()#line:461
            O00O0OO0O0O0OO0OO =O00O00O0000OOOOO0 .winning_rewards ()#line:463
            if 'status'in OO000O00OO0OO00O0 :#line:464
                if OO000O00OO0OO00O0 ['status']==200 :#line:465
                    O0OOOO0000000OOO0 =OO000O00OO0OO00O0 ['data'][0 ]['day_get_gold_quantity']#line:466
                    print (f'【参与抽奖】:预计每天中{O0OOOO0000000OOO0[:6]}种子丨好友收益:{O00O0OO0O0O0OO0OO}')#line:467
        except Exception as O000O000O00O0OOOO :#line:468
            print (O000O000O00O0OOOO )#line:469
    def energy (OO0OO00O00O000000 ):#line:472
        O0OOO0000O0O00000 =f'__{timi_new()}'#line:473
        OO0O0O0000OO00OOO ={'authorization':OO0OO00O00O000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000O0O00000 ),'signstring':O0OOO0000O0O00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:482
        O000O0OOOO0O00000 =requests .request ('get',f'{host}/energy/general',headers =OO0O0O0000OO00OOO ).json ()#line:483
        if 'status'in O000O0OOOO0O00000 :#line:485
            if O000O0OOOO0O00000 ['status']==200 :#line:486
                OO0OOO0O00OOOOO0O =O000O0OOOO0O00000 ['data']['ordinary_water_consumptions']#line:487
                if float (OO0OOO0O00OOOOO0O )<80 :#line:488
                    OOOOOO00OOOO00OOO =99 -float (OO0OOO0O00OOOOO0O )#line:489
                    O00O00O0OO00000O0 ={"fertilizer":str (OOOOOO00OOOO00OOO ).split ('.')[0 ]}#line:490
                    O00O0OOO00OOO0O0O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0O0O0000OO00OOO ,data =O00O00O0OO00000O0 ).json ()#line:491
                    if 'status'in O00O0OOO00OOO0O0O :#line:493
                        if O00O0OOO00OOO0O0O ['status']==200 :#line:494
                            print (f'【购买肥料】:{O00O0OOO00OOO0O0O["message"]}')#line:495
                OOOO0O0O0OO0OO00O =O000O0OOOO0O00000 ['data']['ordinary_water_consumptions']#line:496
                if float (OOOO0O0O0OO0OO00O )<800 :#line:497
                    OO00OO0000O000O00 =999 -float (OOOO0O0O0OO0OO00O )#line:498
                    O0O0O0OOO0OOOOO00 ={"water":str (OO00OO0000O000O00 ).split ('.')[0 ]}#line:499
                    O0OOO0O0000OOOOOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0O0O0000OO00OOO ,data =O0O0O0OOO0OOOOO00 ).json ()#line:500
                    if 'status'in O0OOO0O0000OOOOOO :#line:501
                        if O0OOO0O0000OOOOOO ['status']==200 :#line:502
                            print (f'【购买水滴】:{O0OOO0O0000OOOOOO["message"]}')#line:503
def version_of_the_validation ():#line:509
    return str ((62 -56 )/10 )#line:510
def gitee_validation ():#line:512
    try :#line:513
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:514
    except Exception as O000O0OOO0OOO0OOO :#line:515
        sys .exit (0 )#line:516
def update_the_validation ():#line:522
    try :#line:523
        O0O00OO00OO0O0OO0 =gitee_validation ()#line:524
        if version_of_the_validation ()<O0O00OO00OO0O0OO0 ['CityEarth']['edition']:#line:525
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O00OO00OO0O0OO0["CityEarth"]["edition"]}   ❌')#line:526
            print (f'更新内容=>>{O0O00OO00OO0O0OO0["CityEarth"]["content"]}   👍')#line:527
        else :#line:528
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O00OO00OO0O0OO0["CityEarth"]["edition"]}   ✅')#line:529
            print (f'更新内容=>> {O0O00OO00OO0O0OO0["CityEarth"]["content"]}   👍')#line:530
    except Exception as OO00000O0O00O00OO :#line:531
        print (OO00000O0O00O00OO )#line:532
def os_qinglong ():#line:535
    if application in os .environ :#line:536
        O0O0OO000O0O00000 =os .environ [application ].split ('\n')#line:537
        if len (O0O0OO000O0O00000 )>0 :#line:538
            return O0O0OO000O0O00000 #line:539
        else :#line:540
            print (f"{application}变量未启用")#line:541
            print ('脚本退出')#line:542
            sys .exit (1 )#line:543
    else :#line:544
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:545
        return os_built ()#line:546
def os_built ():#line:549
    if token :#line:550
        OOO00O00O0OOOO00O =token .split ('\n')#line:551
        if len (OOO00O00O0OOOO00O )>0 :#line:552
            return OOO00O00O0OOOO00O #line:553
    else :#line:554
        print (f"内置变量为空")#line:555
        print ('脚本结束')#line:556
        sys .exit (0 )#line:557
if __name__ =='__main__':#line:560
    start ()#line:561
