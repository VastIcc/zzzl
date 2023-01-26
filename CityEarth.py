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
        OOO0OOO0OO000OOO0 =os_qinglong ()#line:7
        print (f"==========共找到{len(OOO0OOO0OO000OOO0)}个账号==========")#line:8
        for OOOO0OO000OOO0O0O in OOO0OOO0OO000OOO0 :#line:9
            print (f"------------正在执行第{OOO0OOO0OO000OOO0.index(OOOO0OO000OOO0O0O) + 1}个账号------------")#line:10
            O000OOO0OO0OOO000 =CityEarth (OOOO0OO000OOO0O0O )#line:11
            if O000OOO0OO0OOO000 .base_info ():#line:13
                O000OOO0OO0OOO000 .friends_invitation ()#line:18
                O000OOO0OO0OOO000 .add_clover ()#line:20
                O000OOO0OO0OOO000 .energy ()#line:22
                O000OOO0OO0OOO000 .synthetic ()#line:24
                O000OOO0OO0OOO000 .propsraffle ()#line:26
                O000OOO0OO0OOO000 .crops_illustrated ()#line:28
            else :#line:29
                print ('token失效')#line:30
            time .sleep (time_xx )#line:32
    except Exception as O00O0O00O0000O00O :#line:33
        print (O00O0O00O0000O00O )#line:34
def sign (OOO0OOO0O0000OOO0 ):#line:36
    O00000O0OO00OO0OO =hashlib .md5 (OOO0OOO0O0000OOO0 .encode ()).hexdigest ()#line:37
    OOO000OOOO00OO0O0 ="scsc%^&*"+O00000O0OO00OO0OO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:38
    O0O00O00OO00O0000 =hashlib .md5 (OOO000OOOO00OO0O0 .encode ()).hexdigest ()#line:39
    return O0O00O00OO00O0000 #line:40
def timi_new ():#line:42
    return str (int (time .time ()*1000 ))#line:43
class CityEarth :#line:46
    def __init__ (OO0000000O00O0OO0 ,OO0OOOO0O0OOOO0O0 ):#line:48
        try :#line:49
            OO0000000O00O0OO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:50
            OO0000000O00O0OO0 .token =OO0OOOO0O0OOOO0O0 .split ('&')[0 ]#line:51
            OO0000000O00O0OO0 .innerId =OO0OOOO0O0OOOO0O0 .split ('&')[1 ]#line:52
        except Exception as O000O00O00OOO00O0 :#line:53
            print ('变量格式错误')#line:54
    def base_info (O0000OO00O00O0O00 ):#line:57
        global level #line:58
        try :#line:59
            O0O00000OOOOO00OO =f'__{timi_new()}'#line:60
            OO0OOO0O00OOO0OOO ={'authorization':O0000OO00O00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000OOOOO00OO ),'signstring':O0O00000OOOOO00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:69
            O0000O000OO00OO0O =requests .request ('get',f'{host}/user',headers =OO0OOO0O00OOO0OOO ).json ()#line:70
            if 'status'in O0000O000OO00OO0O :#line:72
                if O0000O000OO00OO0O ['status']==200 :#line:73
                    O0O0OOO00000OOOO0 =O0000O000OO00OO0O ['data']['nickname']#line:74
                    OOO00O0OOOOO00O0O =O0000O000OO00OO0O ['data']['inner_id']#line:75
                    O0O000OOO0OOO0OO0 =O0000O000OO00OO0O ['data']['assets']['gold']#line:76
                    level =O0000O000OO00OO0O ['data']['level']#line:77
                    print (f'【账号信息】:昵称:{O0O0OOO00000OOOO0}丨ID:{str(OOO00O0OOOOO00O0O)[:3] + "**"+ str(OOO00O0OOOOO00O0O)[5:]}丨等级:{level}丨种子:{str(O0O000OOO0OOO0OO0).split(".")[0]}')#line:78
                if O0000O000OO00OO0O ['status']==401 :#line:79
                    return False #line:80
                if O0000O000OO00OO0O ['status']==500 :#line:81
                    return False #line:82
            return True #line:83
        except Exception as OOO00OOO0OOOO00OO :#line:84
            print (OOO00OOO0OOOO00OO )#line:85
    def winning_rewards (OO0OO0O00OO0O00OO ):#line:88
        OO0OO0O0OO00OOO0O =f'__{timi_new()}'#line:89
        O0OO0OO00O0OOOO0O ={'authorization':OO0OO0O00OO0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0OO00OOO0O ),'signstring':OO0OO0O0OO00OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:98
        O0OO00O000OOO0O0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OO0OO00O0OOOO0O ).json ()#line:99
        if 'status'in O0OO00O000OOO0O0O :#line:101
            if O0OO00O000OOO0O0O ['status']==200 :#line:102
                if O0OO00O000OOO0O0O ['data']['amount']:#line:103
                    OOOO0O0000O000O0O =O0OO00O000OOO0O0O ['data']['amount']['gold']#line:104
                    return OOOO0O0000O000O0O #line:105
                else :#line:106
                    return 0 #line:107
    def certification (OO00O0OOOOO0O0OO0 ):#line:109
        O0O000OOOOO0000O0 =f'__{timi_new()}'#line:110
        OOO00OO0O0O0O000O ={'authorization':OO00O0OOOOO0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOOOO0000O0 ),'signstring':O0O000OOOOO0000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
        OOOO000000OOOO0O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO00OO0O0O0O000O ).json ()#line:120
        if 'status'in OOOO000000OOOO0O0 :#line:122
            if OOOO000000OOOO0O0 ['status']==200 :#line:123
                if OOOO000000OOOO0O0 ['data']['result']:#line:124
                    OOOO0O0OOOO00OOOO =OOOO000000OOOO0O0 ['data']['nick_name']#line:125
                    return OOOO0O0OOOO00OOOO #line:126
                else :#line:127
                    return '未实名'#line:128
    def crops_illustrated (O000O0O00OO0O00O0 ):#line:131
        O000OOO0O00O0OO0O =f'__{timi_new()}'#line:132
        OOOO000O0OOOO0O00 ={'authorization':O000O0O00OO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0O00O0OO0O ),'signstring':O000OOO0O00O0OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:141
        O0OOO0OO0OOO0O0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOOO000O0OOOO0O00 ).json ()#line:142
        if 'status'in O0OOO0OO0OOO0O0O0 :#line:144
            if O0OOO0OO0OOO0O0O0 ['status']==200 :#line:145
                O0O00O00O0OOOOO00 =O0OOO0OO0OOO0O0O0 ['data'][0 ]['crops']#line:146
                for O00O0OO000OOOOO0O in O0O00O00O0OOOOO00 :#line:147
                    if O00O0OO000OOOOO0O ['ill_clover_award']:#line:148
                        if float (O00O0OO000OOOOO0O ['ill_clover_award'])>1 :#line:149
                            if O00O0OO000OOOOO0O ['is_finish']:#line:150
                                if not O00O0OO000OOOOO0O ['is_getit']:#line:151
                                    O000OOO0O00O0OO0O =f'_award_level={O00O0OO000OOOOO0O["level"]}_{timi_new()}'#line:152
                                    OOOO000O0OOOO0O00 ={'authorization':O000O0O00OO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0O00O0OO0O ),'signstring':O000OOO0O00O0OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:161
                                    O0OOOO0O0OO0O0O0O ={"award_level":O00O0OO000OOOOO0O ['level']}#line:162
                                    OO0O0O0O0OOO00000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOOO000O0OOOO0O00 ,json =O0OOOO0O0OO0O0O0O ).json ()#line:163
                                    if 'status'in OO0O0O0O0OOO00000 :#line:164
                                        if OO0O0O0O0OOO00000 ['status']==200 :#line:165
                                            OOOOOO0O0OOOO0O00 =OO0O0O0O0OOO00000 ['data']['ill_clover_award']#line:166
                                            print (f'【图鉴奖励】:领取{O00O0OO000OOOOO0O["crop_name"]}成就丨奖励{OOOOOO0O0OOOO0O00}叶子成功')#line:167
                                        if OO0O0O0O0OOO00000 ['status']==500 :#line:168
                                            print (f'【图鉴奖励】:{OO0O0O0O0OOO00000["message"]}')#line:169
    def watched_ad (O0OO0OO000O0O0O00 ):#line:172
        OOO00OO0OOOOOOOO0 =f'__{timi_new()}'#line:173
        O0O0OO00O0O0O00OO ={'authorization':O0OO0OO000O0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0OOOOOOOO0 ),'signstring':OOO00OO0OOOOOOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:182
        O000OOOOOOO00OOO0 =requests .request ('post',f'{host}/game/watched-ad',headers =O0O0OO00O0O0O00OO ).json ()#line:183
        print (O000OOOOOOO00OOO0 )#line:184
    def user_ad (OOO0O000OOO0OO00O ):#line:190
        OO0O0O00O00O00OOO =f'__{timi_new()}'#line:191
        OOO00O00000O00OO0 ={'authorization':OOO0O000OOO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O00O00O00OOO ),'signstring':OO0O0O00O00O00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:200
        O000O0O0O0OOO000O =requests .request ('get',f'{host}/user/ad',headers =OOO00O00000O00OO0 ).json ()#line:201
        if 'status'in O000O0O0O0OOO000O :#line:203
            if O000O0O0O0OOO000O ['status']==200 :#line:204
                O00000OOOO0OOO000 =O000O0O0O0OOO000O ['data']['max_time']#line:205
                O0O00O00O0OO0OOOO =O000O0O0O0OOO000O ['data']['watch_time']#line:206
                OO0O0000O0O0O0OO0 =O000O0O0O0OOO000O ['data']['added_time']#line:207
                print (f'【获取种子】:获取种子剩余{OO0O0000O0O0O0OO0 + O00000OOOO0OOO000 - O0O00O00O0OO0OOOO}次丨好友提供:{OO0O0000O0O0O0OO0}次')#line:208
                if OO0O0000O0O0O0OO0 +O00000OOOO0OOO000 -O0O00O00O0OO0OOOO >0 :#line:209
                    time .sleep (random .randint (16 ,19 ))#line:210
                    O0OO0000O0O000O0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO00O00000O00OO0 ).json ()#line:211
                    if 'status'in O0OO0000O0O000O0O :#line:213
                        if O0OO0000O0O000O0O ['status']==200 :#line:214
                            OOOO000OOOO0O0OOO =O0OO0000O0O000O0O ['data']['silver']#line:215
                            print (f'【获取种子】:获得种子:{OOOO000OOOO0O0OOO}')#line:216
                            return True #line:217
                        if O0OO0000O0O000O0O ['status']==500 :#line:218
                            OO0OOOO0O0OOO0O00 =O0OO0000O0O000O0O ['message']#line:219
                            print (f'【获取种子】:{OO0OOOO0O0OOO0O00}')#line:220
                            return False #line:221
    def synthetic (OOO0OO0O0000O0OOO ):#line:224
        global id ,g #line:225
        try :#line:226
            while True :#line:228
                O00O00OO000O0O0O0 =f'__{timi_new()}'#line:229
                O0O0O0O0O00OOOOOO ={'authorization':OOO0OO0O0000O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO000O0O0O0 ),'signstring':O00O00OO000O0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:238
                OO00O00O0000O0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0O0O00OOOOOO ).json ()#line:239
                if 'status'in OO00O00O0000O0OO0 :#line:241
                    if OO00O00O0000O0OO0 ['status']==200 :#line:242
                        OOO0OO0000OOOO0O0 =OO00O00O0000O0OO0 ['data']['cropList']#line:243
                        OO00O0O0O0OOO00OO =OO00O00O0000O0OO0 ['data']['gameCoreDataDBid']#line:244
                        O00O000OO00OOOO00 =0 #line:245
                        for O00OO00OO00OOO0O0 in OOO0OO0000OOOO0O0 :#line:246
                            if not O00OO00OO00OOO0O0 :#line:247
                                OO0O0OOO00O0O00OO =f'_crop_id={OO00O0O0O0OOO00OO}&site={O00O000OO00OOOO00}_{OOO0OO0O0000O0OOO.time}'#line:248
                                OOO00O0OOOOO0O00O ={'authorization':OOO0OO0O0000O0OOO .token ,'timestamp':OOO0OO0O0000O0OOO .time ,'sign':sign (OO0O0OOO00O0O00OO ),'signstring':OO0O0OOO00O0O00OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:257
                                OO0OOO00O000O00OO ={"site":O00O000OO00OOOO00 ,"crop_id":OO00O0O0O0OOO00OO }#line:258
                                OOO0OOO0O00OOO000 =requests .request ('post',f'{host}/game/crops/buy',headers =OOO00O0OOOOO0O00O ,data =OO0OOO00O000O00OO ).json ()#line:259
                                if 'status'in OOO0OOO0O00OOO000 :#line:261
                                    if OOO0OOO0O00OOO000 ['status']==200 :#line:262
                                        if OOO0OOO0O00OOO000 ['message']=='种子数量不足':#line:263
                                            print (f'【购买合成】:{OOO0OOO0O00OOO000["message"]}')#line:264
                                            if not OOO0OO0O0000O0OOO .user_ad ():#line:265
                                                return False #line:266
                                        print (f'【购买合成】:购买农作物,位置{O00O000OO00OOOO00}')#line:267
                                    if OOO0OOO0O00OOO000 ['status']==500 :#line:268
                                        print (f'【购买合成】:{OOO0OOO0O00OOO000["message"]}')#line:269
                                        return False #line:270
                            O00O000OO00OOOO00 +=1 #line:271
                        OOOOOO000O000OO0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0O0O00OOOOOO ).json ()#line:272
                        O0O0O0OO0O0O0O0O0 =OOOOOO000O000OO0O ['data']['cropList']#line:273
                        OO0O0O00OO0O00O0O =False #line:274
                        for O00OO00OO00OOO0O0 in range (12 ):#line:275
                            id =O0O0O0OO0O0O0O0O0 [O00OO00OO00OOO0O0 ]['level']#line:276
                            if int (level )-int (id )>9 :#line:277
                                O00OOOO000000O00O =f'_site={O00OO00OO00OOO0O0}_{timi_new()}'#line:278
                                O0O0OOOOOO000OO00 ={'accept':'application/json, text/plain, */*','authorization':OOO0OO0O0000O0OOO .token ,'timestamp':timi_new (),'sign':sign (O00OOOO000000O00O ),'signstring':O00OOOO000000O00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:288
                                OO000O0OOO0OO0000 ={"site":O00OO00OO00OOO0O0 }#line:289
                                O00O0O0OOOOO00O0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O0OOOOOO000OO00 ,data =OO000O0OOO0OO0000 ).json ()#line:290
                                if 'status'in O00O0O0OOOOO00O0O :#line:292
                                    if O00O0O0OOOOO00O0O ['status']==200 :#line:293
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:294
                            if id !=0 :#line:295
                                for OOO000O00O0OOOOO0 in range (11 ):#line:296
                                    OOOO000O0OOO0000O =OOO000O00O0OOOOO0 +1 #line:297
                                    g =O0O0O0OO0O0O0O0O0 [OOOO000O0OOO0000O ]['level']#line:298
                                    if id ==g :#line:299
                                        OO000OO0O0OO00OO0 =OOO000O00O0OOOOO0 +2 #line:300
                                        if OO000OO0O0OO00OO0 ==O00OO00OO00OOO0O0 +1 :#line:301
                                            pass #line:302
                                        else :#line:303
                                            O0O0OOOOO00O0OOO0 =O00OO00OO00OOO0O0 +1 #line:304
                                            O0000OO0OOO0O0O00 =f'_site={O0O0OOOOO00O0OOO0-1}&targetSite={OO000OO0O0OO00OO0-1}_{timi_new()}'#line:307
                                            OOO0OOO0O00O0O000 ={'accept':'application/json, text/plain, */*','authorization':OOO0OO0O0000O0OOO .token ,'timestamp':timi_new (),'sign':sign (O0000OO0OOO0O0O00 ),'signstring':O0000OO0OOO0O0O00 ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:322
                                            OO0OOO00O0O000OO0 ={"site":int (O0O0OOOOO00O0OOO0 -1 ),"targetSite":int (OO000OO0O0OO00OO0 -1 )}#line:323
                                            O00O00O0O0O000O00 =requests .request ('post',f'{host}/game/crops/move',headers =OOO0OOO0O00O0O000 ,json =OO0OOO00O0O000OO0 ).json ()#line:324
                                            if 'status'in O00O00O0O0O000O00 :#line:325
                                                if O00O00O0O0O000O00 ['status']==200 :#line:326
                                                    pass #line:327
                                            print ('【购买合成】:',O0O0OOOOO00O0OOO0 ,OO000OO0O0OO00OO0 ,'合成成功')#line:329
                                            OO0O0O00OO0O00O0O =True #line:330
                                    if OO0O0O00OO0O00O0O :#line:331
                                        break #line:332
                                if OO0O0O00OO0O00O0O :#line:333
                                    break #line:334
        except Exception as O0OOOO000O0000000 :#line:335
            OOO0OO0O0000O0OOO .synthetic ()#line:336
    def propsraffle (OOO00OOOO0O0000O0 ):#line:340
        try :#line:341
            while True :#line:342
                O0OO0O00O0OOO00O0 =f'__{timi_new()}'#line:343
                O0O00O0OO00OO00O0 ={'authorization':OOO00OOOO0O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O0OOO00O0 ),'signstring':O0OO0O00O0OOO00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:352
                OO00O00O00O00OO0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O00O0OO00OO00O0 ).json ()#line:353
                if 'status'in OO00O00O00O00OO0O :#line:355
                    if OO00O00O00O00OO0O ['status']==200 :#line:356
                        OO00OO0000O0000O0 =OO00O00O00O00OO0O ['data']['rows']#line:357
                        OO000OO0O0OO0000O =OO00O00O00O00OO0O ['data']['vstate']#line:358
                        if OO00OO0000O0000O0 ==5 or OO00OO0000O0000O0 ==6 or OO00OO0000O0000O0 ==7 :#line:359
                            O0O0O0O0O000OOO00 =OO00O00O00O00OO0O ['data']['silver']#line:360
                            print (f'【转盘抽奖】:获得种子:{O0O0O0O0O000OOO00}')#line:361
                        if OO00OO0000O0000O0 ==1 or OO00OO0000O0000O0 ==2 or OO00OO0000O0000O0 ==3 :#line:362
                            O0OOO00000OOOO000 =OO00O00O00O00OO0O ['data']['clover']#line:363
                            print (f'【转盘抽奖】:获得三叶草:{O0OOO00000OOOO000}')#line:364
                        if OO00OO0000O0000O0 ==4 or OO00OO0000O0000O0 ==8 :#line:365
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:366
                        if OO00OO0000O0000O0 =='抽奖次数已用完':#line:370
                            if OO000OO0O0OO0000O :#line:371
                                OOO00O00O0OOOO000 =random .randint (160 ,190 )/10 #line:372
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{OOO00O00O0OOOO000}秒获取抽奖机会')#line:373
                                time .sleep (OOO00O00O0OOOO000 )#line:374
                                O00OO0OOO0OOO00O0 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O0O00O0OO00OO00O0 ).json ()#line:375
                                if 'status'in O00OO0OOO0OOO00O0 :#line:377
                                    if O00OO0OOO0OOO00O0 ['status']==200 :#line:378
                                        print (f'【转盘抽奖】:{O00OO0OOO0OOO00O0["message"]}')#line:379
                                    if O00OO0OOO0OOO00O0 ['status']==500 :#line:380
                                        print (f'【转盘抽奖】:{O00OO0OOO0OOO00O0["message"]}')#line:381
                                        break #line:382
                                time .sleep (random .randint (10 ,15 )/10 )#line:383
                            else :#line:384
                                break #line:385
                time .sleep (random .randint (8 ,15 )/10 )#line:386
        except Exception as OO0O000000000000O :#line:387
            print (OO0O000000000000O )#line:388
    def friends_invitation (OO0OOOO0OO0O00O00 ):#line:391
        try :#line:392
            OO00O0000O0O00000 =f'__{timi_new()}'#line:393
            O000O0OOO000OO00O ={'authorization':OO0OOOO0OO0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0000O0O00000 ),'signstring':OO00O0000O0O00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:402
            OOO0OOO0OOO0OO0OO =requests .request ('get',f'{host}/friends',headers =O000O0OOO000OO00O ).json ()#line:403
            if 'status'in OOO0OOO0OOO0OO0OO :#line:404
                if OOO0OOO0OOO0OO0OO ['status']==200 :#line:405
                    OOO0000O00000OOOO =OOO0OOO0OOO0OO0OO ['data']['myInviteter']#line:406
                    if OOO0000O00000OOOO :#line:407
                        OO0OOOO0OOO000O0O =OOO0000O00000OOOO ['user']['nickname']#line:408
                        OO00O00OOOO0O00O0 =OO0OOOO0OO0O00O00 .certification ()#line:409
                        print (f'【绑邀请码】:我的邀请人:{OO0OOOO0OOO000O0O}丨实名:{OO00O00OOOO0O00O0}')#line:410
                    else :#line:411
                        if OO0OOOO0OO0O00O00 .innerId !='0':#line:412
                            OO00O0000O0O00000 =f'_innerId={OO0OOOO0OO0O00O00.innerId}_{timi_new()}'#line:413
                            O000O0OOO000OO00O ={'authorization':OO0OOOO0OO0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0000O0O00000 ),'signstring':OO00O0000O0O00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:422
                            O0O0000O000OOO000 ={"innerId":OO0OOOO0OO0O00O00 .innerId }#line:423
                            OO000000OO0000O0O =requests .request ('post',f'{host}/friends/my-invitation',headers =O000O0OOO000OO00O ,data =O0O0000O000OOO000 ).json ()#line:424
                            if 'status'in OO000000OO0000O0O :#line:425
                                if OO000000OO0000O0O ['status']==200 :#line:426
                                    print (f'【绑邀请码】:{OO0OOOO0OO0O00O00.innerId}{OO000000OO0000O0O["message"]}')#line:427
                        else :#line:428
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:429
        except Exception as O00O0000OOOOO0000 :#line:430
            print (O00O0000OOOOO0000 )#line:431
    def add_clover (O0OO0O0OO000OOOOO ):#line:435
        try :#line:436
            O0O0O0OO0000O00O0 =f'__{timi_new()}'#line:437
            O00000O0OOOO0OOO0 ={'authorization':O0OO0O0OO000OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO0000O00O0 ),'signstring':O0O0O0OO0000O00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:446
            O000000OO000000OO =requests .request ('get',f'{host}/assets/clovers',headers =O00000O0OOOO0OOO0 ).json ()#line:447
            if 'status'in O000000OO000000OO :#line:449
                if O000000OO000000OO ['status']==200 :#line:450
                    O000O0OOOOOO00OOO =O000000OO000000OO ['data']['clover']#line:451
                    O0OO0O000O0OO0O0O =O000000OO000000OO ['data']['used_clover']#line:452
                    O000000O0O00000OO =float (O000O0OOOOOO00OOO )-float (O0OO0O000O0OO0O0O )#line:453
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0OO0O000O0OO0O0O}')#line:454
                    if O000000O0O00000OO >1 :#line:455
                        O0O0O0OO0000O00O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O000000O0O00000OO)}_{timi_new()}'#line:456
                        O00000O0OOOO0OOO0 ={'authorization':O0OO0O0OO000OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO0000O00O0 ),'signstring':O0O0O0OO0000O00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:465
                        OO00000OO0O0O0O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O000000O0O00000OO )}#line:466
                        OO00O00O000O00000 =requests .request ('post',f'{host}/lottery/add-stake',headers =O00000O0OOOO0OOO0 ,data =OO00000OO0O0O0O0O ).json ()#line:467
                        if 'status'in OO00O00O000O00000 :#line:469
                            if OO00O00O000O00000 ['status']==200 :#line:470
                                print (f'【参与抽奖】:添加三叶草:{OO00O00O000O00000["data"]}丨数量:{O000000O0O00000OO}')#line:471
            OO0O0O0OO0O00OO0O =requests .request ('get',f'{host}/lottery',headers =O00000O0OOOO0OOO0 ).json ()#line:472
            O0000O00O00000OOO =O0OO0O0OO000OOOOO .winning_rewards ()#line:474
            if 'status'in OO0O0O0OO0O00OO0O :#line:475
                if OO0O0O0OO0O00OO0O ['status']==200 :#line:476
                    O0O0000OO00000O00 =OO0O0O0OO0O00OO0O ['data'][0 ]['day_get_gold_quantity']#line:477
                    print (f'【参与抽奖】:预计每天中{O0O0000OO00000O00[:6]}种子丨好友收益:{O0000O00O00000OOO}')#line:478
        except Exception as OOO00OOOO00O0OO00 :#line:479
            print (OOO00OOOO00O0OO00 )#line:480
    def energy (O0O0O0OOOO000OO00 ):#line:483
        OO000OO0000O00OOO =f'__{timi_new()}'#line:484
        OO00O00O00O00O00O ={'authorization':O0O0O0OOOO000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0000O00OOO ),'signstring':OO000OO0000O00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:493
        OOO0OO0000OOO0OO0 =requests .request ('get',f'{host}/energy/general',headers =OO00O00O00O00O00O ).json ()#line:494
        if 'status'in OOO0OO0000OOO0OO0 :#line:496
            if OOO0OO0000OOO0OO0 ['status']==200 :#line:497
                OO0OOOO0OOO0000OO =OOO0OO0000OOO0OO0 ['data']['ordinary_water_consumptions']#line:498
                if float (OO0OOOO0OOO0000OO )<80 :#line:499
                    OOO00000OO000OO00 =99 -float (OO0OOOO0OOO0000OO )#line:500
                    O000O0OO000OOO000 ={"fertilizer":str (OOO00000OO000OO00 ).split ('.')[0 ]}#line:501
                    OOO0OOOO0O0O0000O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO00O00O00O00O00O ,data =O000O0OO000OOO000 ).json ()#line:502
                    if 'status'in OOO0OOOO0O0O0000O :#line:504
                        if OOO0OOOO0O0O0000O ['status']==200 :#line:505
                            print (f'【购买肥料】:{OOO0OOOO0O0O0000O["message"]}')#line:506
                OO0OOOOOO0O0O0O0O =OOO0OO0000OOO0OO0 ['data']['ordinary_water_consumptions']#line:507
                if float (OO0OOOOOO0O0O0O0O )<800 :#line:508
                    O00O0OOO0O0000OO0 =999 -float (OO0OOOOOO0O0O0O0O )#line:509
                    OOOO0OO0O000OO000 ={"water":str (O00O0OOO0O0000OO0 ).split ('.')[0 ]}#line:510
                    OOOOOOOO0O0OOO0OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO00O00O00O00O00O ,data =OOOO0OO0O000OO000 ).json ()#line:511
                    if 'status'in OOOOOOOO0O0OOO0OO :#line:512
                        if OOOOOOOO0O0OOO0OO ['status']==200 :#line:513
                            print (f'【购买水滴】:{OOOOOOOO0O0OOO0OO["message"]}')#line:514
def version_of_the_validation ():#line:520
    return str ((62 -56 )/10 )#line:521
def gitee_validation ():#line:523
    try :#line:524
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:525
    except Exception as O00OO0O000OO0O00O :#line:526
        sys .exit (0 )#line:527
def update_the_validation ():#line:533
    try :#line:534
        OO0OOO0O0OOO0OO00 =gitee_validation ()#line:535
        if version_of_the_validation ()<OO0OOO0O0OOO0OO00 ['CityEarth']['edition']:#line:536
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OOO0O0OOO0OO00["CityEarth"]["edition"]}   ❌')#line:537
            print (f'更新内容=>>{OO0OOO0O0OOO0OO00["CityEarth"]["content"]}   👍')#line:538
        else :#line:539
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OOO0O0OOO0OO00["CityEarth"]["edition"]}   ✅')#line:540
            print (f'更新内容=>> {OO0OOO0O0OOO0OO00["CityEarth"]["content"]}   👍')#line:541
    except Exception as O000OOOOO000O0O0O :#line:542
        print (O000OOOOO000O0O0O )#line:543
def os_qinglong ():#line:546
    if application in os .environ :#line:547
        O0OO0OOOO00O0O000 =os .environ [application ].split ('\n')#line:548
        if len (O0OO0OOOO00O0O000 )>0 :#line:549
            return O0OO0OOOO00O0O000 #line:550
        else :#line:551
            print (f"{application}变量未启用")#line:552
            print ('脚本退出')#line:553
            sys .exit (1 )#line:554
    else :#line:555
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:556
        return os_built ()#line:557
def os_built ():#line:560
    if token :#line:561
        OOOOOOO00O000OOO0 =token .split ('\n')#line:562
        if len (OOOOOOO00O000OOO0 )>0 :#line:563
            return OOOOOOO00O000OOO0 #line:564
    else :#line:565
        print (f"内置变量为空")#line:566
        print ('脚本结束')#line:567
        sys .exit (0 )#line:568
if __name__ =='__main__':#line:571
    start ()#line:572
