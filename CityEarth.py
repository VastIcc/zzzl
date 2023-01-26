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
        OO00O000OOO0O0O00 =os_qinglong ()#line:7
        print (f"==========共找到{len(OO00O000OOO0O0O00)}个账号==========")#line:8
        for OOOOOOO0OOOO000OO in OO00O000OOO0O0O00 :#line:9
            print (f"------------正在执行第{OO00O000OOO0O0O00.index(OOOOOOO0OOOO000OO) + 1}个账号------------")#line:10
            OOOOOOOO0000OOOO0 =CityEarth (OOOOOOO0OOOO000OO )#line:11
            if OOOOOOOO0000OOOO0 .base_info ():#line:13
                OOOOOOOO0000OOOO0 .friends_invitation ()#line:18
                OOOOOOOO0000OOOO0 .add_clover ()#line:20
                OOOOOOOO0000OOOO0 .energy ()#line:22
                OOOOOOOO0000OOOO0 .synthetic ()#line:24
                OOOOOOOO0000OOOO0 .propsraffle ()#line:26
                OOOOOOOO0000OOOO0 .crops_illustrated ()#line:28
            else :#line:29
                print ('token失效')#line:30
            time .sleep (time_xx )#line:32
    except Exception as OO0OOO00OO0O000OO :#line:33
        print (OO0OOO00OO0O000OO )#line:34
def sign (OOOO0OOO0O0OOOO0O ):#line:36
    O0OOOO0OO0000O0O0 =hashlib .md5 (OOOO0OOO0O0OOOO0O .encode ()).hexdigest ()#line:37
    O0OOOO00OOO0O0OOO ="scsc%^&*"+O0OOOO0OO0000O0O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:38
    OOOO0OO00OO00000O =hashlib .md5 (O0OOOO00OOO0O0OOO .encode ()).hexdigest ()#line:39
    return OOOO0OO00OO00000O #line:40
def timi_new ():#line:42
    return str (int (time .time ()*1000 ))#line:43
class CityEarth :#line:46
    def __init__ (OO0O0000OOOO00O00 ,O00OO0O0OO0O0OOO0 ):#line:48
        try :#line:49
            OO0O0000OOOO00O00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:50
            OO0O0000OOOO00O00 .token =O00OO0O0OO0O0OOO0 .split ('&')[0 ]#line:51
            OO0O0000OOOO00O00 .innerId =O00OO0O0OO0O0OOO0 .split ('&')[1 ]#line:52
        except Exception as OOO00O0O0O0OOOOO0 :#line:53
            print ('变量格式错误')#line:54
    def base_info (O0000OO000OO00O00 ):#line:57
        global level #line:58
        try :#line:59
            OO000O00OO00O0O00 =f'__{timi_new()}'#line:60
            O0O0OO0OO0OOOOO00 ={'authorization':O0000OO000OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00OO00O0O00 ),'signstring':OO000O00OO00O0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:69
            OO000OOO0OOO000O0 =requests .request ('get',f'{host}/user',headers =O0O0OO0OO0OOOOO00 ).json ()#line:70
            if 'status'in OO000OOO0OOO000O0 :#line:72
                if OO000OOO0OOO000O0 ['status']==200 :#line:73
                    O00OOO0O00O000OO0 =OO000OOO0OOO000O0 ['data']['nickname']#line:74
                    O0O0OOO0O0000OOOO =OO000OOO0OOO000O0 ['data']['inner_id']#line:75
                    O0OO00OO0O00O00OO =OO000OOO0OOO000O0 ['data']['assets']['gold']#line:76
                    level =OO000OOO0OOO000O0 ['data']['level']#line:77
                    print (f'【账号信息】:昵称:{O00OOO0O00O000OO0}丨ID:{str(O0O0OOO0O0000OOOO)[:3] + "**"+ str(O0O0OOO0O0000OOOO)[5:]}丨等级:{level}丨种子:{str(O0OO00OO0O00O00OO).split(".")[0]}')#line:78
                if OO000OOO0OOO000O0 ['status']==401 :#line:79
                    return False #line:80
                if OO000OOO0OOO000O0 ['status']==500 :#line:81
                    return False #line:82
            return True #line:83
        except Exception as O0O0OOO0O00OOO0OO :#line:84
            print (O0O0OOO0O00OOO0OO )#line:85
    def winning_rewards (OO0OOOO00O00OO0OO ):#line:88
        O00O00OOO0O00OOOO =f'__{timi_new()}'#line:89
        OOO000O00OO0OO000 ={'authorization':OO0OOOO00O00OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OOO0O00OOOO ),'signstring':O00O00OOO0O00OOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:98
        O0O00OO0OO0OO0O0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO000O00OO0OO000 ).json ()#line:99
        if 'status'in O0O00OO0OO0OO0O0O :#line:101
            if O0O00OO0OO0OO0O0O ['status']==200 :#line:102
                if O0O00OO0OO0OO0O0O ['data']['amount']:#line:103
                    OO0OOOOOOOOOO000O =O0O00OO0OO0OO0O0O ['data']['amount']['gold']#line:104
                    return OO0OOOOOOOOOO000O #line:105
                else :#line:106
                    return 0 #line:107
    def certification (OOOOOOO00O00OO000 ):#line:109
        OOOO0O0O00OO00OO0 =f'__{timi_new()}'#line:110
        OO00OO00OOO000OOO ={'authorization':OOOOOOO00O00OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O00OO00OO0 ),'signstring':OOOO0O0O00OO00OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
        O0O0O0OOO00000OO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO00OO00OOO000OOO ).json ()#line:120
        if 'status'in O0O0O0OOO00000OO0 :#line:122
            if O0O0O0OOO00000OO0 ['status']==200 :#line:123
                if O0O0O0OOO00000OO0 ['data']['result']:#line:124
                    O00O000OOO0O000O0 =O0O0O0OOO00000OO0 ['data']['nick_name']#line:125
                    return O00O000OOO0O000O0 #line:126
                else :#line:127
                    return '未实名'#line:128
    def crops_illustrated (O00O0000O00O00OO0 ):#line:131
        O0O0O0O00O0O00OOO =f'__{timi_new()}'#line:132
        O000O0OOO0000OOO0 ={'authorization':O00O0000O00O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00O0O00OOO ),'signstring':O0O0O0O00O0O00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:141
        O000OOO00O0000OO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O000O0OOO0000OOO0 ).json ()#line:142
        if 'status'in O000OOO00O0000OO0 :#line:144
            if O000OOO00O0000OO0 ['status']==200 :#line:145
                O0O0O00O00O000OOO =O000OOO00O0000OO0 ['data'][0 ]['crops']#line:146
                for OOO0O00O00OOOO0OO in O0O0O00O00O000OOO :#line:147
                    if OOO0O00O00OOOO0OO ['ill_clover_award']:#line:148
                        if float (OOO0O00O00OOOO0OO ['ill_clover_award'])>1 :#line:149
                            if OOO0O00O00OOOO0OO ['is_finish']:#line:150
                                if not OOO0O00O00OOOO0OO ['is_getit']:#line:151
                                    O0O0O0O00O0O00OOO =f'_award_level={OOO0O00O00OOOO0OO["level"]}_{timi_new()}'#line:152
                                    O000O0OOO0000OOO0 ={'authorization':O00O0000O00O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00O0O00OOO ),'signstring':O0O0O0O00O0O00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:161
                                    OOO00O00OOO0O0OOO ={"award_level":OOO0O00O00OOOO0OO ['level']}#line:162
                                    OOOO0OOO0O0000OOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O000O0OOO0000OOO0 ,json =OOO00O00OOO0O0OOO ).json ()#line:163
                                    if 'status'in OOOO0OOO0O0000OOO :#line:164
                                        if OOOO0OOO0O0000OOO ['status']==200 :#line:165
                                            OOOOO0OOO000O0OO0 =OOOO0OOO0O0000OOO ['data']['ill_clover_award']#line:166
                                            print (f'【图鉴奖励】:领取{OOO0O00O00OOOO0OO["crop_name"]}成就丨奖励{OOOOO0OOO000O0OO0}叶子成功')#line:167
                                        if OOOO0OOO0O0000OOO ['status']==500 :#line:168
                                            print (f'【图鉴奖励】:{OOOO0OOO0O0000OOO["message"]}')#line:169
    def watched_ad (O0OOOO00OOOOOO0O0 ):#line:172
        OOOO00OO000OO00OO =f'__{timi_new()}'#line:173
        OO0O0000O00OOO0O0 ={'authorization':O0OOOO00OOOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO000OO00OO ),'signstring':OOOO00OO000OO00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:182
        OOOO0OOO0O000OO0O =requests .request ('post',f'{host}/game/watched-ad',headers =OO0O0000O00OOO0O0 ).json ()#line:183
        print (OOOO0OOO0O000OO0O )#line:184
    def user_ad (O0O0OOOO00O0OO000 ):#line:190
        OO000000O0O00O000 =f'__{timi_new()}'#line:191
        O000000OOOOO0O0O0 ={'authorization':O0O0OOOO00O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000O0O00O000 ),'signstring':OO000000O0O00O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:200
        OO0OO000O0OO0O000 =requests .request ('get',f'{host}/user/ad',headers =O000000OOOOO0O0O0 ).json ()#line:201
        if 'status'in OO0OO000O0OO0O000 :#line:203
            if OO0OO000O0OO0O000 ['status']==200 :#line:204
                OOOOO00O00000O00O =OO0OO000O0OO0O000 ['data']['max_time']#line:205
                O0OO0OOO0OOOO0O0O =OO0OO000O0OO0O000 ['data']['watch_time']#line:206
                OO0O00000OO000000 =OO0OO000O0OO0O000 ['data']['added_time']#line:207
                print (f'【获取种子】:获取种子剩余{OO0O00000OO000000 + OOOOO00O00000O00O - O0OO0OOO0OOOO0O0O}次丨好友提供:{OO0O00000OO000000}次')#line:208
                if OO0O00000OO000000 +OOOOO00O00000O00O -O0OO0OOO0OOOO0O0O >0 :#line:209
                    time .sleep (random .randint (16 ,19 ))#line:210
                    OOO0OOOOOO000000O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O000000OOOOO0O0O0 ).json ()#line:211
                    if 'status'in OOO0OOOOOO000000O :#line:213
                        if OOO0OOOOOO000000O ['status']==200 :#line:214
                            O000O0OOOOO0O0OOO =OOO0OOOOOO000000O ['data']['silver']#line:215
                            print (f'【获取种子】:获得种子:{O000O0OOOOO0O0OOO}')#line:216
                            return True #line:217
                        if OOO0OOOOOO000000O ['status']==500 :#line:218
                            OOO0OO0000O000OO0 =OOO0OOOOOO000000O ['message']#line:219
                            print (f'【获取种子】:{OOO0OO0000O000OO0}')#line:220
                            return False #line:221
    def synthetic (OOOOO000O0O0O000O ):#line:224
        global id ,g #line:225
        try :#line:226
            while True :#line:228
                OOOO0O00OOO00OOOO =f'__{timi_new()}'#line:229
                OO0O0OOOOO0000O0O ={'authorization':OOOOO000O0O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00OOO00OOOO ),'signstring':OOOO0O00OOO00OOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:238
                OOO00OOO0OOO0OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0OOOOO0000O0O ).json ()#line:239
                if 'status'in OOO00OOO0OOO0OOO0 :#line:241
                    if OOO00OOO0OOO0OOO0 ['status']==200 :#line:242
                        O000000OO00O0O0OO =OOO00OOO0OOO0OOO0 ['data']['cropList']#line:243
                        O00O000OOOOO0OOOO =OOO00OOO0OOO0OOO0 ['data']['gameCoreDataDBid']#line:244
                        O00O0O0OO000OOO0O =0 #line:245
                        for OO0O0OOO0O00OO00O in O000000OO00O0O0OO :#line:246
                            if not OO0O0OOO0O00OO00O :#line:247
                                O00OOO00OO00O00OO =f'_crop_id={O00O000OOOOO0OOOO}&site={O00O0O0OO000OOO0O}_{OOOOO000O0O0O000O.time}'#line:248
                                OO00OO0O0O000O000 ={'authorization':OOOOO000O0O0O000O .token ,'timestamp':OOOOO000O0O0O000O .time ,'sign':sign (O00OOO00OO00O00OO ),'signstring':O00OOO00OO00O00OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:257
                                O0O000OO0OOO0OOOO ={"site":O00O0O0OO000OOO0O ,"crop_id":O00O000OOOOO0OOOO }#line:258
                                OOOO000O0000O0OO0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO00OO0O0O000O000 ,data =O0O000OO0OOO0OOOO ).json ()#line:259
                                if 'status'in OOOO000O0000O0OO0 :#line:261
                                    if OOOO000O0000O0OO0 ['status']==200 :#line:262
                                        if OOOO000O0000O0OO0 ['message']=='种子数量不足':#line:263
                                            print (f'【购买合成】:{OOOO000O0000O0OO0["message"]}')#line:264
                                            if not OOOOO000O0O0O000O .user_ad ():#line:265
                                                return False #line:266
                                        print (f'【购买合成】:购买农作物,位置{O00O0O0OO000OOO0O}')#line:267
                                    if OOOO000O0000O0OO0 ['status']==500 :#line:268
                                        print (f'【购买合成】:{OOOO000O0000O0OO0["message"]}')#line:269
                                        return False #line:270
                            O00O0O0OO000OOO0O +=1 #line:271
                        O0OOOOO0OO0O0OO0O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0OOOOO0000O0O ).json ()#line:272
                        OO0O0OOO0O00OO0O0 =O0OOOOO0OO0O0OO0O ['data']['cropList']#line:273
                        O0OO0OOOOOO0000OO =False #line:274
                        for OO0O0OOO0O00OO00O in range (12 ):#line:275
                            id =OO0O0OOO0O00OO0O0 [OO0O0OOO0O00OO00O ]['level']#line:276
                            if int (level )-int (id )>9 :#line:277
                                OO00OO0OO00000000 =f'_site={OO0O0OOO0O00OO00O}_{timi_new()}'#line:278
                                O0OOOOO0O0O00OO00 ={'accept':'application/json, text/plain, */*','authorization':OOOOO000O0O0O000O .token ,'timestamp':timi_new (),'sign':sign (OO00OO0OO00000000 ),'signstring':OO00OO0OO00000000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:288
                                OO0O00OO0OO00OOO0 ={"site":OO0O0OOO0O00OO00O }#line:289
                                OO00OO0OOOO0O000O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OOOOO0O0O00OO00 ,data =OO0O00OO0OO00OOO0 ).json ()#line:290
                                if 'status'in OO00OO0OOOO0O000O :#line:292
                                    if OO00OO0OOOO0O000O ['status']==200 :#line:293
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:294
                            if id !=0 :#line:295
                                for OOO0O0O0000O0OOO0 in range (11 ):#line:296
                                    OOOOO000OOOO00OO0 =OOO0O0O0000O0OOO0 +1 #line:297
                                    g =OO0O0OOO0O00OO0O0 [OOOOO000OOOO00OO0 ]['level']#line:298
                                    if id ==g :#line:299
                                        OOO0000O00OOOOOOO =OOO0O0O0000O0OOO0 +2 #line:300
                                        if OOO0000O00OOOOOOO ==OO0O0OOO0O00OO00O +1 :#line:301
                                            pass #line:302
                                        else :#line:303
                                            OOO00O000O0O0OOOO =OO0O0OOO0O00OO00O +1 #line:304
                                            O000OOO000O0000OO =f'_site={OOO00O000O0O0OOOO-1}&targetSite={OOO0000O00OOOOOOO-1}_{timi_new()}'#line:307
                                            O0000O0000OO0O00O ={'accept':'application/json, text/plain, */*','authorization':OOOOO000O0O0O000O .token ,'timestamp':timi_new (),'sign':sign (O000OOO000O0000OO ),'signstring':O000OOO000O0000OO ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:322
                                            O0OO000OO000O000O ={"site":int (OOO00O000O0O0OOOO -1 ),"targetSite":int (OOO0000O00OOOOOOO -1 )}#line:323
                                            OOO00OO00OOO0OO00 =requests .request ('post',f'{host}/game/crops/move',headers =O0000O0000OO0O00O ,json =O0OO000OO000O000O ).json ()#line:324
                                            if 'status'in OOO00OO00OOO0OO00 :#line:325
                                                if OOO00OO00OOO0OO00 ['status']==200 :#line:326
                                                    pass #line:327
                                            print ('【购买合成】:',OOO00O000O0O0OOOO ,OOO0000O00OOOOOOO ,'合成成功')#line:329
                                            O0OO0OOOOOO0000OO =True #line:330
                                    if O0OO0OOOOOO0000OO :#line:331
                                        break #line:332
                                if O0OO0OOOOOO0000OO :#line:333
                                    break #line:334
        except Exception as O0O0OOOO00OO0O000 :#line:335
            OOOOO000O0O0O000O .synthetic ()#line:336
    def propsraffle (OOO0O0O000OO0O000 ):#line:340
        try :#line:341
            while True :#line:342
                OO00O0OOOOO0O00O0 =f'__{timi_new()}'#line:343
                OOOOO0OOOO00OOO00 ={'authorization':OOO0O0O000OO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OOOOO0O00O0 ),'signstring':OO00O0OOOOO0O00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:352
                OOO00000OOOO00000 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOOO0OOOO00OOO00 ).json ()#line:353
                if 'status'in OOO00000OOOO00000 :#line:355
                    if OOO00000OOOO00000 ['status']==200 :#line:356
                        OOO00OOO00000OOO0 =OOO00000OOOO00000 ['data']['rows']#line:357
                        O00000OO000O00O0O =OOO00000OOOO00000 ['data']['vstate']#line:358
                        if OOO00OOO00000OOO0 ==5 or OOO00OOO00000OOO0 ==6 or OOO00OOO00000OOO0 ==7 :#line:359
                            OOOO000O0OOO000OO =OOO00000OOOO00000 ['data']['silver']#line:360
                            print (f'【转盘抽奖】:获得种子:{OOOO000O0OOO000OO}')#line:361
                        if OOO00OOO00000OOO0 ==1 or OOO00OOO00000OOO0 ==2 or OOO00OOO00000OOO0 ==3 :#line:362
                            OOOO000O0OO0O000O =OOO00000OOOO00000 ['data']['clover']#line:363
                            print (f'【转盘抽奖】:获得三叶草:{OOOO000O0OO0O000O}')#line:364
                        if OOO00OOO00000OOO0 ==4 or OOO00OOO00000OOO0 ==8 :#line:365
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:366
                        if OOO00OOO00000OOO0 =='抽奖次数已用完':#line:370
                            if O00000OO000O00O0O :#line:371
                                O0O0O0000OO0OOO00 =random .randint (160 ,190 )/10 #line:372
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{O0O0O0000OO0OOO00}秒获取抽奖机会')#line:373
                                time .sleep (O0O0O0000OO0OOO00 )#line:374
                                O0OO0000000O0O00O =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OOOOO0OOOO00OOO00 ).json ()#line:375
                                if 'status'in O0OO0000000O0O00O :#line:377
                                    if O0OO0000000O0O00O ['status']==200 :#line:378
                                        print (f'【转盘抽奖】:{O0OO0000000O0O00O["message"]}')#line:379
                                    if O0OO0000000O0O00O ['status']==500 :#line:380
                                        print (f'【转盘抽奖】:{O0OO0000000O0O00O["message"]}')#line:381
                                        break #line:382
                                time .sleep (random .randint (10 ,15 )/10 )#line:383
                            else :#line:384
                                break #line:385
                time .sleep (random .randint (8 ,15 )/10 )#line:386
        except Exception as OO00O0OOOOOOOOO00 :#line:387
            print (OO00O0OOOOOOOOO00 )#line:388
    def friends_invitation (OO0O0OO0OO0OOOO00 ):#line:391
        try :#line:392
            O0OOOOO00OOO0O0O0 =f'__{timi_new()}'#line:393
            O0OOO00OO00OO0OOO ={'authorization':OO0O0OO0OO0OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO00OOO0O0O0 ),'signstring':O0OOOOO00OOO0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:402
            OOOO0OO000OOOOOO0 =requests .request ('get',f'{host}/friends',headers =O0OOO00OO00OO0OOO ).json ()#line:403
            if 'status'in OOOO0OO000OOOOOO0 :#line:404
                if OOOO0OO000OOOOOO0 ['status']==200 :#line:405
                    OO0OO0OOO0OO0O0OO =OOOO0OO000OOOOOO0 ['data']['myInviteter']#line:406
                    if OO0OO0OOO0OO0O0OO :#line:407
                        O0OO0OO000O00O0O0 =OO0OO0OOO0OO0O0OO ['user']['nickname']#line:408
                        O0OO0OOO0O0OO00O0 =OO0O0OO0OO0OOOO00 .certification ()#line:409
                        print (f'【绑邀请码】:我的邀请人:{O0OO0OO000O00O0O0}丨实名:{O0OO0OOO0O0OO00O0}')#line:410
                    else :#line:411
                        if OO0O0OO0OO0OOOO00 .innerId !='0':#line:412
                            print ('【绑邀请码】:绑定邀请码')#line:413
                            OOO00OO0O00OOO0O0 ={"innerId":OO0O0OO0OO0OOOO00 .innerId }#line:414
                            OOOOO0OOO0000O0OO =requests .request ('post',f'{host}/friends/my-invitation',headers =O0OOO00OO00OO0OOO ,data =OOO00OO0O00OOO0O0 ).json ()#line:415
                            print (OOOOO0OOO0000O0OO )#line:416
                        else :#line:417
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:418
        except Exception as OO0OO0OO0O0OO0OO0 :#line:419
            print (OO0OO0OO0O0OO0OO0 )#line:420
    def add_clover (OO0OO0OO0OO000O00 ):#line:424
        try :#line:425
            OO0O0000OOO000OOO =f'__{timi_new()}'#line:426
            OO0OOO0OOOO00OOOO ={'authorization':OO0OO0OO0OO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000OOO000OOO ),'signstring':OO0O0000OOO000OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:435
            OO00OO00O0O0OO0O0 =requests .request ('get',f'{host}/assets/clovers',headers =OO0OOO0OOOO00OOOO ).json ()#line:436
            if 'status'in OO00OO00O0O0OO0O0 :#line:438
                if OO00OO00O0O0OO0O0 ['status']==200 :#line:439
                    OO0O000O0000O0OO0 =OO00OO00O0O0OO0O0 ['data']['clover']#line:440
                    O00OO0OOO000OOOOO =OO00OO00O0O0OO0O0 ['data']['used_clover']#line:441
                    OOO000OO00OOOOOO0 =float (OO0O000O0000O0OO0 )-float (O00OO0OOO000OOOOO )#line:442
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O00OO0OOO000OOOOO}')#line:443
                    if OOO000OO00OOOOOO0 >1 :#line:444
                        OO0O0000OOO000OOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO000OO00OOOOOO0)}_{timi_new()}'#line:445
                        OO0OOO0OOOO00OOOO ={'authorization':OO0OO0OO0OO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000OOO000OOO ),'signstring':OO0O0000OOO000OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:454
                        O00O000OO00O0OOO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO000OO00OOOOOO0 )}#line:455
                        O00O00OOO0OO0OO0O =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0OOO0OOOO00OOOO ,data =O00O000OO00O0OOO0 ).json ()#line:456
                        if 'status'in O00O00OOO0OO0OO0O :#line:458
                            if O00O00OOO0OO0OO0O ['status']==200 :#line:459
                                print (f'【参与抽奖】:添加三叶草:{O00O00OOO0OO0OO0O["data"]}丨数量:{OOO000OO00OOOOOO0}')#line:460
            O0OO00OO0O0OOO000 =requests .request ('get',f'{host}/lottery',headers =OO0OOO0OOOO00OOOO ).json ()#line:461
            O0O0OOOOOOOOO0OOO =OO0OO0OO0OO000O00 .winning_rewards ()#line:463
            if 'status'in O0OO00OO0O0OOO000 :#line:464
                if O0OO00OO0O0OOO000 ['status']==200 :#line:465
                    OOOO00000OOO0O00O =O0OO00OO0O0OOO000 ['data'][0 ]['day_get_gold_quantity']#line:466
                    print (f'【参与抽奖】:预计每天中{OOOO00000OOO0O00O[:6]}种子丨好友收益:{O0O0OOOOOOOOO0OOO}')#line:467
        except Exception as O00OOOO0O0OO0OOOO :#line:468
            print (O00OOOO0O0OO0OOOO )#line:469
    def energy (O00O0OO000000O0OO ):#line:472
        OO00OO000OOOOO0O0 =f'__{timi_new()}'#line:473
        OO0OOOOO000OOOOOO ={'authorization':O00O0OO000000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO000OOOOO0O0 ),'signstring':OO00OO000OOOOO0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:482
        OO0000O00O0O000OO =requests .request ('get',f'{host}/energy/general',headers =OO0OOOOO000OOOOOO ).json ()#line:483
        if 'status'in OO0000O00O0O000OO :#line:485
            if OO0000O00O0O000OO ['status']==200 :#line:486
                O0OO00OOO00OOOO0O =OO0000O00O0O000OO ['data']['ordinary_water_consumptions']#line:487
                if float (O0OO00OOO00OOOO0O )<80 :#line:488
                    OO00O00O00OO0O0O0 =99 -float (O0OO00OOO00OOOO0O )#line:489
                    O0OO0000O0OOO0O00 ={"fertilizer":str (OO00O00O00OO0O0O0 ).split ('.')[0 ]}#line:490
                    O00O0OOOO0OO0O000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0OOOOO000OOOOOO ,data =O0OO0000O0OOO0O00 ).json ()#line:491
                    if 'status'in O00O0OOOO0OO0O000 :#line:493
                        if O00O0OOOO0OO0O000 ['status']==200 :#line:494
                            print (f'【购买肥料】:{O00O0OOOO0OO0O000["message"]}')#line:495
                O0OO0O0OOOO00OO0O =OO0000O00O0O000OO ['data']['ordinary_water_consumptions']#line:496
                if float (O0OO0O0OOOO00OO0O )<800 :#line:497
                    OOOOO0000O0OOO0OO =999 -float (O0OO0O0OOOO00OO0O )#line:498
                    O00OOO0OO0000OO00 ={"water":str (OOOOO0000O0OOO0OO ).split ('.')[0 ]}#line:499
                    O0OOOOOO00OO00000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0OOOOO000OOOOOO ,data =O00OOO0OO0000OO00 ).json ()#line:500
                    if 'status'in O0OOOOOO00OO00000 :#line:501
                        if O0OOOOOO00OO00000 ['status']==200 :#line:502
                            print (f'【购买水滴】:{O0OOOOOO00OO00000["message"]}')#line:503
def version_of_the_validation ():#line:509
    return str ((62 -56 )/10 )#line:510
def gitee_validation ():#line:512
    try :#line:513
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:514
    except Exception as OO0OOOOOO0O000O0O :#line:515
        sys .exit (0 )#line:516
def update_the_validation ():#line:522
    try :#line:523
        OO00OOO0OO0O000OO =gitee_validation ()#line:524
        if version_of_the_validation ()<OO00OOO0OO0O000OO ['CityEarth']['edition']:#line:525
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00OOO0OO0O000OO["CityEarth"]["edition"]}   ❌')#line:526
            print (f'更新内容=>>{OO00OOO0OO0O000OO["CityEarth"]["content"]}   👍')#line:527
        else :#line:528
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00OOO0OO0O000OO["CityEarth"]["edition"]}   ✅')#line:529
            print (f'更新内容=>> {OO00OOO0OO0O000OO["CityEarth"]["content"]}   👍')#line:530
    except Exception as O0000O000000OO000 :#line:531
        print (O0000O000000OO000 )#line:532
def os_qinglong ():#line:535
    if application in os .environ :#line:536
        O00OO0OO00OO000OO =os .environ [application ].split ('\n')#line:537
        if len (O00OO0OO00OO000OO )>0 :#line:538
            return O00OO0OO00OO000OO #line:539
        else :#line:540
            print (f"{application}变量未启用")#line:541
            print ('脚本退出')#line:542
            sys .exit (1 )#line:543
    else :#line:544
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:545
        return os_built ()#line:546
def os_built ():#line:549
    if token :#line:550
        O0O0000O0OO00OOO0 =token .split ('\n')#line:551
        if len (O0O0000O0OO00OOO0 )>0 :#line:552
            return O0O0000O0OO00OOO0 #line:553
    else :#line:554
        print (f"内置变量为空")#line:555
        print ('脚本结束')#line:556
        sys .exit (0 )#line:557
if __name__ =='__main__':#line:560
    start ()#line:561
