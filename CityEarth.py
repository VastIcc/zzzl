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
        OOO00OOO0O0OO000O =os_qinglong ()#line:7
        print (f"==========共找到{len(OOO00OOO0O0OO000O)}个账号==========")#line:8
        for OOO000OO00O0OOOO0 in OOO00OOO0O0OO000O :#line:9
            print (f"------------正在执行第{OOO00OOO0O0OO000O.index(OOO000OO00O0OOOO0) + 1}个账号------------")#line:10
            O0000OOO0O0OOOO00 =CityEarth (OOO000OO00O0OOOO0 )#line:11
            if O0000OOO0O0OOOO00 .base_info ():#line:13
                O0000OOO0O0OOOO00 .friends_invitation ()#line:18
                O0000OOO0O0OOOO00 .add_clover ()#line:20
                O0000OOO0O0OOOO00 .energy ()#line:22
                O0000OOO0O0OOOO00 .synthetic ()#line:24
                O0000OOO0O0OOOO00 .propsraffle ()#line:26
                O0000OOO0O0OOOO00 .crops_illustrated ()#line:28
                O0000OOO0O0OOOO00 .give_gold ()#line:30
            else :#line:31
                print ('token失效')#line:32
            time .sleep (time_xx )#line:34
    except Exception as O0O0OOOO00O00O0O0 :#line:35
        print (O0O0OOOO00O00O0O0 )#line:36
def sign (OO0OOO0OO0OOO0000 ):#line:38
    OOOO00000OO00O00O =hashlib .md5 (OO0OOO0OO0OOO0000 .encode ()).hexdigest ()#line:39
    O00OOO000O0O0000O ="scsc%^&*"+OOOO00000OO00O00O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:40
    O00OOO00O000O0O00 =hashlib .md5 (O00OOO000O0O0000O .encode ()).hexdigest ()#line:41
    return O00OOO00O000O0O00 #line:42
def timi_new ():#line:44
    return str (int (time .time ()*1000 ))#line:45
class CityEarth :#line:48
    def __init__ (O0OO00O00OOOOOO00 ,OO00OO0OOOOO000OO ):#line:50
        try :#line:51
            O0OO00O00OOOOOO00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:52
            O0OO00O00OOOOOO00 .token =OO00OO0OOOOO000OO .split ('&')[0 ]#line:53
            O0OO00O00OOOOOO00 .innerId =OO00OO0OOOOO000OO .split ('&')[1 ]#line:54
            O0OO00O00OOOOOO00 .doneeNo =OO00OO0OOOOO000OO .split ('&')[2 ]#line:55
        except :#line:56
            print ('变量格式错误')#line:57
    def base_info (O0OOO0O00O000000O ):#line:60
        global level #line:61
        try :#line:62
            O000O0O0OOO0OOO0O =f'__{timi_new()}'#line:63
            O000O0O0000OO0O0O ={'authorization':O0OOO0O00O000000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O0OOO0OOO0O ),'signstring':O000O0O0OOO0OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:72
            O0OOO0O0OO00OOOOO =requests .request ('get',f'{host}/user',headers =O000O0O0000OO0O0O ).json ()#line:73
            if 'status'in O0OOO0O0OO00OOOOO :#line:75
                if O0OOO0O0OO00OOOOO ['status']==200 :#line:76
                    OOO0000000000OO0O =O0OOO0O0OO00OOOOO ['data']['nickname']#line:77
                    OO0OO000O0O00OOO0 =O0OOO0O0OO00OOOOO ['data']['inner_id']#line:78
                    OOOO0OO000OOOO00O =O0OOO0O0OO00OOOOO ['data']['assets']['gold']#line:79
                    level =O0OOO0O0OO00OOOOO ['data']['level']#line:80
                    print (f'【账号信息】:昵称:{OOO0000000000OO0O}丨ID:{str(OO0OO000O0O00OOO0)[:3] + "**"+ str(OO0OO000O0O00OOO0)[5:]}丨等级:{level}丨种子:{str(OOOO0OO000OOOO00O).split(".")[0]}')#line:81
                if O0OOO0O0OO00OOOOO ['status']==401 :#line:82
                    return False #line:83
                if O0OOO0O0OO00OOOOO ['status']==500 :#line:84
                    return False #line:85
            return True #line:86
        except Exception as O0OOOOO000O00OO0O :#line:87
            print (O0OOOOO000O00OO0O )#line:88
    def give_gold (O0O0O00OOO0O0O000 ):#line:91
        OO000OO0OO0O0OO00 =f'__{timi_new()}'#line:92
        O0OOO0O0OO00O00O0 ={'authorization':O0O0O00OOO0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0OO0O0OO00 ),'signstring':OO000OO0OO0O0OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:101
        O00OO0OO00O0O0OOO =requests .request ('get',f'{host}/user',headers =O0OOO0O0OO00O00O0 ).json ()#line:102
        if 'status'in O00OO0OO00O0O0OOO :#line:103
            if O00OO0OO00O0O0OOO ['status']==200 :#line:104
                if float (O0O0O00OOO0O0O000 .doneeNo )!=0 :#line:105
                    OOO00O0000OO0OOO0 =O00OO0OO00O0O0OOO ['data']['assets']['gold']#line:106
                    if float (OOO00O0000OO0OOO0 )>2 :#line:107
                        O0000O000O0OOO000 =int (float (OOO00O0000OO0OOO0 )/1.1 )#line:108
                        OO000OO0OO0O0OO00 =f'_doneeNo={O0O0O00OOO0O0O000.doneeNo}&quantity={O0000O000O0OOO000}_{timi_new()}'#line:109
                        O0OOO0O0OO00O00O0 ={'authorization':O0O0O00OOO0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0OO0O0OO00 ),'signstring':OO000OO0OO0O0OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:118
                        O00O00OO000O00OO0 ={"quantity":O0000O000O0OOO000 ,"doneeNo":O0O0O00OOO0O0O000 .doneeNo }#line:122
                        OOO00O0O000000000 =requests .request ('post',f'{host}/finance/give-gold',headers =O0OOO0O0OO00O00O0 ,data =O00O00OO000O00OO0 ).json ()#line:123
                        if 'status'in OOO00O0O000000000 :#line:125
                            if OOO00O0O000000000 ['status']==200 :#line:126
                                if OOO00O0O000000000 ['data']:#line:127
                                    print (f'【赠送种子】:赠送{O0000O000O0OOO000}种子给{O0O0O00OOO0O0O000.doneeNo}成功')#line:128
                else :#line:129
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:130
    def winning_rewards (OOO0O0O000OO0O0OO ):#line:132
        OO0OOOO000000OO00 =f'__{timi_new()}'#line:133
        OOOO0OO00O0O00000 ={'authorization':OOO0O0O000OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO000000OO00 ),'signstring':OO0OOOO000000OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:142
        OOOOOOO00O000O0O0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOOO0OO00O0O00000 ).json ()#line:143
        if 'status'in OOOOOOO00O000O0O0 :#line:145
            if OOOOOOO00O000O0O0 ['status']==200 :#line:146
                if OOOOOOO00O000O0O0 ['data']['amount']:#line:147
                    O0O0000OO0OOOOO0O =OOOOOOO00O000O0O0 ['data']['amount']['gold']#line:148
                    return O0O0000OO0OOOOO0O #line:149
                else :#line:150
                    return 0 #line:151
    def certification (OO00OOO0O000O0O00 ):#line:153
        OOOO0O0OO000000O0 =f'__{timi_new()}'#line:154
        OO0000OO0O00OO0O0 ={'authorization':OO00OOO0O000O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0OO000000O0 ),'signstring':OOOO0O0OO000000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:163
        O00OO000OO0OOOOO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0000OO0O00OO0O0 ).json ()#line:164
        if 'status'in O00OO000OO0OOOOO0 :#line:166
            if O00OO000OO0OOOOO0 ['status']==200 :#line:167
                if O00OO000OO0OOOOO0 ['data']['result']:#line:168
                    O0000OO00O0OO00OO =O00OO000OO0OOOOO0 ['data']['nick_name']#line:169
                    return O0000OO00O0OO00OO #line:170
                else :#line:171
                    return '未实名'#line:172
    def crops_illustrated (O00O00OO000000000 ):#line:175
        OOO000O000O0O0O00 =f'__{timi_new()}'#line:176
        O0O0OO0O000OO00O0 ={'authorization':O00O00OO000000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O000O0O0O00 ),'signstring':OOO000O000O0O0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:185
        O0OOO0OO000OOO00O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O0OO0O000OO00O0 ).json ()#line:186
        if 'status'in O0OOO0OO000OOO00O :#line:188
            if O0OOO0OO000OOO00O ['status']==200 :#line:189
                OOOOO0O000O0O0000 =O0OOO0OO000OOO00O ['data'][0 ]['crops']#line:190
                for O0OOO0OOO00OOO00O in OOOOO0O000O0O0000 :#line:191
                    if O0OOO0OOO00OOO00O ['ill_clover_award']:#line:192
                        if float (O0OOO0OOO00OOO00O ['ill_clover_award'])>1 :#line:193
                            if O0OOO0OOO00OOO00O ['is_finish']:#line:194
                                if not O0OOO0OOO00OOO00O ['is_getit']:#line:195
                                    OOO000O000O0O0O00 =f'_award_level={O0OOO0OOO00OOO00O["level"]}_{timi_new()}'#line:196
                                    O0O0OO0O000OO00O0 ={'authorization':O00O00OO000000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O000O0O0O00 ),'signstring':OOO000O000O0O0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:205
                                    O00OOO0OO0OOOOO0O ={"award_level":O0OOO0OOO00OOO00O ['level']}#line:206
                                    OO0O000O0O0O00O0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O0OO0O000OO00O0 ,json =O00OOO0OO0OOOOO0O ).json ()#line:207
                                    if 'status'in OO0O000O0O0O00O0O :#line:208
                                        if OO0O000O0O0O00O0O ['status']==200 :#line:209
                                            O0000O0O0000O0OOO =OO0O000O0O0O00O0O ['data']['ill_clover_award']#line:210
                                            print (f'【图鉴奖励】:领取{O0OOO0OOO00OOO00O["crop_name"]}成就丨奖励{O0000O0O0000O0OOO}叶子成功')#line:211
                                        if OO0O000O0O0O00O0O ['status']==500 :#line:212
                                            print (f'【图鉴奖励】:{OO0O000O0O0O00O0O["message"]}')#line:213
    def watched_ad (O0000O0OOOOO0OO00 ):#line:216
        O00OOO000O00O0O00 =f'__{timi_new()}'#line:217
        O0000O00OO000OOOO ={'authorization':O0000O0OOOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO000O00O0O00 ),'signstring':O00OOO000O00O0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:226
        OOO0OOOO0O0OOOOO0 =requests .request ('post',f'{host}/game/watched-ad',headers =O0000O00OO000OOOO ).json ()#line:227
        print (OOO0OOOO0O0OOOOO0 )#line:228
    def user_ad (OO0OOOOO000O000OO ):#line:234
        OOOO00O000O00O0O0 =f'__{timi_new()}'#line:235
        OO00O0OOOO000O0OO ={'authorization':OO0OOOOO000O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O000O00O0O0 ),'signstring':OOOO00O000O00O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:244
        O000O00000000000O =requests .request ('get',f'{host}/user/ad',headers =OO00O0OOOO000O0OO ).json ()#line:245
        if 'status'in O000O00000000000O :#line:247
            if O000O00000000000O ['status']==200 :#line:248
                O00O00O00000O00O0 =O000O00000000000O ['data']['max_time']#line:249
                O000OO00OOO00OO00 =O000O00000000000O ['data']['watch_time']#line:250
                OO0OO0OOO0O0OO0O0 =O000O00000000000O ['data']['added_time']#line:251
                print (f'【获取种子】:获取种子剩余{OO0OO0OOO0O0OO0O0 + O00O00O00000O00O0 - O000OO00OOO00OO00}次丨好友提供:{OO0OO0OOO0O0OO0O0}次')#line:252
                if OO0OO0OOO0O0OO0O0 +O00O00O00000O00O0 -O000OO00OOO00OO00 >0 :#line:253
                    time .sleep (random .randint (16 ,19 ))#line:254
                    O0000O00OOOO000OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO00O0OOOO000O0OO ).json ()#line:255
                    if 'status'in O0000O00OOOO000OO :#line:257
                        if O0000O00OOOO000OO ['status']==200 :#line:258
                            OO0O0000O00OOO0O0 =O0000O00OOOO000OO ['data']['silver']#line:259
                            print (f'【获取种子】:获得种子:{OO0O0000O00OOO0O0}')#line:260
                            return True #line:261
                        if O0000O00OOOO000OO ['status']==500 :#line:262
                            O00OOO0OOO0000O0O =O0000O00OOOO000OO ['message']#line:263
                            print (f'【获取种子】:{O00OOO0OOO0000O0O}')#line:264
                            return False #line:265
    def synthetic (OO00O0O000O0O0OO0 ):#line:268
        global id ,g #line:269
        try :#line:270
            while True :#line:272
                OOOO0OO0O0000OOO0 =f'__{timi_new()}'#line:273
                O000OOO00OOOO0OO0 ={'authorization':OO00O0O000O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO0O0000OOO0 ),'signstring':OOOO0OO0O0000OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:282
                OO00OOO00O0OOOO00 =requests .request ('get',f'{host}/game/getAllData',headers =O000OOO00OOOO0OO0 ).json ()#line:283
                if 'status'in OO00OOO00O0OOOO00 :#line:285
                    if OO00OOO00O0OOOO00 ['status']==200 :#line:286
                        O0O0OO00O0O0OOOO0 =OO00OOO00O0OOOO00 ['data']['cropList']#line:287
                        O00OO0O0O0O0O0O0O =OO00OOO00O0OOOO00 ['data']['gameCoreDataDBid']#line:288
                        OOO000O0OOO000O00 =0 #line:289
                        for OO00O00O00O0OOOO0 in O0O0OO00O0O0OOOO0 :#line:290
                            if not OO00O00O00O0OOOO0 :#line:291
                                O0OOO0O00O0OO0OO0 =f'_crop_id={O00OO0O0O0O0O0O0O}&site={OOO000O0OOO000O00}_{OO00O0O000O0O0OO0.time}'#line:292
                                O00OO0OOOO00OOO0O ={'authorization':OO00O0O000O0O0OO0 .token ,'timestamp':OO00O0O000O0O0OO0 .time ,'sign':sign (O0OOO0O00O0OO0OO0 ),'signstring':O0OOO0O00O0OO0OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:301
                                O0O00O00OO00O0O0O ={"site":OOO000O0OOO000O00 ,"crop_id":O00OO0O0O0O0O0O0O }#line:302
                                OOOO00O000O00000O =requests .request ('post',f'{host}/game/crops/buy',headers =O00OO0OOOO00OOO0O ,data =O0O00O00OO00O0O0O ).json ()#line:303
                                time .sleep (random .randint (1 ,3 )/10 )#line:305
                                if 'status'in OOOO00O000O00000O :#line:306
                                    if OOOO00O000O00000O ['status']==200 :#line:307
                                        if OOOO00O000O00000O ['message']=='种子数量不足':#line:308
                                            print (f'【购买合成】:{OOOO00O000O00000O["message"]}')#line:309
                                            if not OO00O0O000O0O0OO0 .user_ad ():#line:310
                                                return False #line:311
                                        print (f'【购买合成】:购买农作物,位置{OOO000O0OOO000O00}')#line:312
                                    if OOOO00O000O00000O ['status']==500 :#line:313
                                        print (f'【购买合成】:{OOOO00O000O00000O["message"]}')#line:314
                                        return False #line:315
                            OOO000O0OOO000O00 +=1 #line:316
                        O0O0O00000O000OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O000OOO00OOOO0OO0 ).json ()#line:317
                        OOO0OO0OO0O0OOO00 =O0O0O00000O000OO0 ['data']['cropList']#line:318
                        OO0O0O0OO0OO0O00O =False #line:319
                        for OO00O00O00O0OOOO0 in range (12 ):#line:320
                            id =OOO0OO0OO0O0OOO00 [OO00O00O00O0OOOO0 ]['level']#line:321
                            if int (level )-int (id )>9 :#line:322
                                O00O0O0OO0O000OOO =f'_site={OO00O00O00O0OOOO0}_{timi_new()}'#line:323
                                OO0O0OO0OOO0O0O00 ={'accept':'application/json, text/plain, */*','authorization':OO00O0O000O0O0OO0 .token ,'timestamp':timi_new (),'sign':sign (O00O0O0OO0O000OOO ),'signstring':O00O0O0OO0O000OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:333
                                OOOOOO00O0O0OOO0O ={"site":OO00O00O00O0OOOO0 }#line:334
                                O0O0OO000OOOOO0OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0O0OO0OOO0O0O00 ,data =OOOOOO00O0O0OOO0O ).json ()#line:335
                                if 'status'in O0O0OO000OOOOO0OO :#line:337
                                    if O0O0OO000OOOOO0OO ['status']==200 :#line:338
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:339
                            if id !=0 :#line:340
                                for OO0O0OO0O0OO0OO00 in range (11 ):#line:341
                                    OO0OOOOO000OO00O0 =OO0O0OO0O0OO0OO00 +1 #line:342
                                    g =OOO0OO0OO0O0OOO00 [OO0OOOOO000OO00O0 ]['level']#line:343
                                    if id ==g :#line:344
                                        OOO00OOO000OO0O00 =OO0O0OO0O0OO0OO00 +2 #line:345
                                        if OOO00OOO000OO0O00 ==OO00O00O00O0OOOO0 +1 :#line:346
                                            pass #line:347
                                        else :#line:348
                                            OOO00O0OOOO0OOOOO =OO00O00O00O0OOOO0 +1 #line:349
                                            time .sleep (random .randint (1 ,3 )/10 )#line:351
                                            O0OO0OO000OOO00OO =f'_site={OOO00O0OOOO0OOOOO-1}&targetSite={OOO00OOO000OO0O00-1}_{timi_new()}'#line:352
                                            OOO0O0OO00O00OO00 ={'accept':'application/json, text/plain, */*','authorization':OO00O0O000O0O0OO0 .token ,'timestamp':timi_new (),'sign':sign (O0OO0OO000OOO00OO ),'signstring':O0OO0OO000OOO00OO ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:367
                                            OOO00O0OOO000O0OO ={"site":int (OOO00O0OOOO0OOOOO -1 ),"targetSite":int (OOO00OOO000OO0O00 -1 )}#line:368
                                            OO0000OOOO0OO00O0 =requests .request ('post',f'{host}/game/crops/move',headers =OOO0O0OO00O00OO00 ,json =OOO00O0OOO000O0OO ).json ()#line:369
                                            if 'status'in OO0000OOOO0OO00O0 :#line:370
                                                if OO0000OOOO0OO00O0 ['status']==200 :#line:371
                                                    pass #line:372
                                            print ('【购买合成】:',OOO00O0OOOO0OOOOO ,OOO00OOO000OO0O00 ,'合成成功')#line:374
                                            OO0O0O0OO0OO0O00O =True #line:375
                                    if OO0O0O0OO0OO0O00O :#line:376
                                        break #line:377
                                if OO0O0O0OO0OO0O00O :#line:378
                                    break #line:379
        except Exception as O00000O00O0OOOOO0 :#line:380
            OO00O0O000O0O0OO0 .synthetic ()#line:381
    def propsraffle (OO0O00OOO0OO0OOOO ):#line:385
        try :#line:386
            while True :#line:387
                O0O00000OO0OOO000 =f'__{timi_new()}'#line:388
                OO00O0O0O00OO00O0 ={'authorization':OO0O00OOO0OO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000OO0OOO000 ),'signstring':O0O00000OO0OOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:397
                O0OOOO0O0O0O0000O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO00O0O0O00OO00O0 ).json ()#line:398
                if 'status'in O0OOOO0O0O0O0000O :#line:400
                    if O0OOOO0O0O0O0000O ['status']==200 :#line:401
                        OOO0O00OOO000OO00 =O0OOOO0O0O0O0000O ['data']['rows']#line:402
                        OOOO000O0OOOOO000 =O0OOOO0O0O0O0000O ['data']['vstate']#line:403
                        if OOO0O00OOO000OO00 ==5 or OOO0O00OOO000OO00 ==6 or OOO0O00OOO000OO00 ==7 :#line:404
                            O000OO0O00000OOO0 =O0OOOO0O0O0O0000O ['data']['silver']#line:405
                            print (f'【转盘抽奖】:获得种子:{O000OO0O00000OOO0}')#line:406
                        if OOO0O00OOO000OO00 ==1 or OOO0O00OOO000OO00 ==2 or OOO0O00OOO000OO00 ==3 :#line:407
                            OO00OO00O000OOOOO =O0OOOO0O0O0O0000O ['data']['clover']#line:408
                            print (f'【转盘抽奖】:获得三叶草:{OO00OO00O000OOOOO}')#line:409
                        if OOO0O00OOO000OO00 ==4 or OOO0O00OOO000OO00 ==8 :#line:410
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:411
                        if OOO0O00OOO000OO00 =='抽奖次数已用完':#line:415
                            if OOOO000O0OOOOO000 :#line:416
                                O000OOO0O0OO0000O =random .randint (160 ,190 )/10 #line:417
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{O000OOO0O0OO0000O}秒获取抽奖机会')#line:418
                                time .sleep (O000OOO0O0OO0000O )#line:419
                                O0O0O0O0O0000O0O0 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OO00O0O0O00OO00O0 ).json ()#line:420
                                if 'status'in O0O0O0O0O0000O0O0 :#line:422
                                    if O0O0O0O0O0000O0O0 ['status']==200 :#line:423
                                        print (f'【转盘抽奖】:{O0O0O0O0O0000O0O0["message"]}')#line:424
                                    if O0O0O0O0O0000O0O0 ['status']==500 :#line:425
                                        print (f'【转盘抽奖】:{O0O0O0O0O0000O0O0["message"]}')#line:426
                                        break #line:427
                                time .sleep (random .randint (10 ,15 )/10 )#line:428
                            else :#line:429
                                break #line:430
                time .sleep (random .randint (8 ,15 )/10 )#line:431
        except Exception as O00OO000O0OOO000O :#line:432
            print (O00OO000O0OOO000O )#line:433
    def friends_invitation (O000OOOOO0O0O0OOO ):#line:436
        try :#line:437
            OOOOO0OO0O00O0000 =f'__{timi_new()}'#line:438
            O0OO0000OO0O00OO0 ={'authorization':O000OOOOO0O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OO0O00O0000 ),'signstring':OOOOO0OO0O00O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:447
            O0O00000O0OOO0000 =requests .request ('get',f'{host}/friends',headers =O0OO0000OO0O00OO0 ).json ()#line:448
            if 'status'in O0O00000O0OOO0000 :#line:449
                if O0O00000O0OOO0000 ['status']==200 :#line:450
                    O0OOOOO0OOO0OO0OO =O0O00000O0OOO0000 ['data']['myInviteter']#line:451
                    if O0OOOOO0OOO0OO0OO :#line:452
                        O0OOOOOOOOOO0OOOO =O0OOOOO0OOO0OO0OO ['user']['nickname']#line:453
                        OOOO0OOO0OO0O00OO =O000OOOOO0O0O0OOO .certification ()#line:454
                        print (f'【绑邀请码】:我的邀请人:{O0OOOOOOOOOO0OOOO}丨实名:{OOOO0OOO0OO0O00OO}')#line:455
                    else :#line:456
                        if O000OOOOO0O0O0OOO .innerId !='0':#line:457
                            OOOOO0OO0O00O0000 =f'_innerId={O000OOOOO0O0O0OOO.innerId}_{timi_new()}'#line:458
                            O0OO0000OO0O00OO0 ={'authorization':O000OOOOO0O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OO0O00O0000 ),'signstring':OOOOO0OO0O00O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:467
                            O00O000O0OOO00O0O ={"innerId":O000OOOOO0O0O0OOO .innerId }#line:468
                            O00O0OO0O0OOOO0O0 =requests .request ('post',f'{host}/friends/my-invitation',headers =O0OO0000OO0O00OO0 ,data =O00O000O0OOO00O0O ).json ()#line:469
                            if 'status'in O00O0OO0O0OOOO0O0 :#line:470
                                if O00O0OO0O0OOOO0O0 ['status']==200 :#line:471
                                    print (f'【绑邀请码】:{O000OOOOO0O0O0OOO.innerId}{O00O0OO0O0OOOO0O0["message"]}')#line:472
                        else :#line:473
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:474
        except Exception as OO0OOO000OO0O0000 :#line:475
            print (OO0OOO000OO0O0000 )#line:476
    def add_clover (OO0000OOOOO0OO0O0 ):#line:480
        try :#line:481
            OO00OO0OO0OOO00O0 =f'__{timi_new()}'#line:482
            OOO00O00OOOO0O000 ={'authorization':OO0000OOOOO0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OO0OOO00O0 ),'signstring':OO00OO0OO0OOO00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:491
            O0O0OOO00OOOO0OO0 =requests .request ('get',f'{host}/assets/clovers',headers =OOO00O00OOOO0O000 ).json ()#line:492
            if 'status'in O0O0OOO00OOOO0OO0 :#line:494
                if O0O0OOO00OOOO0OO0 ['status']==200 :#line:495
                    O00O00OOOOO00OO00 =O0O0OOO00OOOO0OO0 ['data']['clover']#line:496
                    O00O0O0000OOOO000 =O0O0OOO00OOOO0OO0 ['data']['used_clover']#line:497
                    OO00O00OO0O000O00 =float (O00O00OOOOO00OO00 )-float (O00O0O0000OOOO000 )#line:498
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O00O0O0000OOOO000}')#line:499
                    if OO00O00OO0O000O00 >1 :#line:500
                        OO00OO0OO0OOO00O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO00O00OO0O000O00)}_{timi_new()}'#line:501
                        OOO00O00OOOO0O000 ={'authorization':OO0000OOOOO0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OO0OOO00O0 ),'signstring':OO00OO0OO0OOO00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:510
                        OOO0O0O0O0OOO00OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO00O00OO0O000O00 )}#line:511
                        O00OOOO00OOO0O000 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO00O00OOOO0O000 ,data =OOO0O0O0O0OOO00OO ).json ()#line:512
                        if 'status'in O00OOOO00OOO0O000 :#line:514
                            if O00OOOO00OOO0O000 ['status']==200 :#line:515
                                print (f'【参与抽奖】:添加三叶草:{O00OOOO00OOO0O000["data"]}丨数量:{OO00O00OO0O000O00}')#line:516
            OOOOO000OO0O0OO0O =requests .request ('get',f'{host}/lottery',headers =OOO00O00OOOO0O000 ).json ()#line:517
            OOOOOOO00O0OOO0O0 =OO0000OOOOO0OO0O0 .winning_rewards ()#line:519
            if 'status'in OOOOO000OO0O0OO0O :#line:520
                if OOOOO000OO0O0OO0O ['status']==200 :#line:521
                    OOOOOO0O0OOOOOO00 =OOOOO000OO0O0OO0O ['data'][0 ]['day_get_gold_quantity']#line:522
                    print (f'【参与抽奖】:预计每天中{OOOOOO0O0OOOOOO00[:6]}种子丨好友收益:{OOOOOOO00O0OOO0O0}')#line:523
        except Exception as O00O00O00OO0O00O0 :#line:524
            print (O00O00O00OO0O00O0 )#line:525
    def energy (O0OOOOOO0000000OO ):#line:528
        OOOOO00OO0000OO00 =f'__{timi_new()}'#line:529
        O0O00O00OOOO000OO ={'authorization':O0OOOOOO0000000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OO0000OO00 ),'signstring':OOOOO00OO0000OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:538
        OOO00OO0O0OO00000 =requests .request ('get',f'{host}/energy/general',headers =O0O00O00OOOO000OO ).json ()#line:539
        if 'status'in OOO00OO0O0OO00000 :#line:541
            if OOO00OO0O0OO00000 ['status']==200 :#line:542
                OO000O0OO0OO00OO0 =OOO00OO0O0OO00000 ['data']['ordinary_water_consumptions']#line:543
                if float (OO000O0OO0OO00OO0 )<80 :#line:544
                    O00O0000O00OOO0O0 =99 -float (OO000O0OO0OO00OO0 )#line:545
                    OOOOOO0O00O0OO0OO ={"fertilizer":str (O00O0000O00OOO0O0 ).split ('.')[0 ]}#line:546
                    O0O0O0OO00O00O0OO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0O00O00OOOO000OO ,data =OOOOOO0O00O0OO0OO ).json ()#line:547
                    if 'status'in O0O0O0OO00O00O0OO :#line:549
                        if O0O0O0OO00O00O0OO ['status']==200 :#line:550
                            print (f'【购买肥料】:{O0O0O0OO00O00O0OO["message"]}')#line:551
                O0O00OO000O0OOOOO =OOO00OO0O0OO00000 ['data']['ordinary_water_consumptions']#line:552
                if float (O0O00OO000O0OOOOO )<800 :#line:553
                    O0000000OOOO0OOO0 =999 -float (O0O00OO000O0OOOOO )#line:554
                    O000OOOO0OO0OOO00 ={"water":str (O0000000OOOO0OOO0 ).split ('.')[0 ]}#line:555
                    O00O0OOO0OOOOO0OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O00O00OOOO000OO ,data =O000OOOO0OO0OOO00 ).json ()#line:556
                    if 'status'in O00O0OOO0OOOOO0OO :#line:557
                        if O00O0OOO0OOOOO0OO ['status']==200 :#line:558
                            print (f'【购买水滴】:{O00O0OOO0OOOOO0OO["message"]}')#line:559
def version_of_the_validation ():#line:565
    return str ((63 -56 )/10 )#line:566
def gitee_validation ():#line:568
    try :#line:569
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:570
    except Exception as OO000O00OOO000O00 :#line:571
        sys .exit (0 )#line:572
def update_the_validation ():#line:578
    try :#line:579
        OO0O00OOOOOO0OOO0 =gitee_validation ()#line:580
        if version_of_the_validation ()<OO0O00OOOOOO0OOO0 ['CityEarth']['edition']:#line:581
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O00OOOOOO0OOO0["CityEarth"]["edition"]}   ❌')#line:582
            print (f'更新内容=>>{OO0O00OOOOOO0OOO0["CityEarth"]["content"]}   👍')#line:583
        else :#line:584
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O00OOOOOO0OOO0["CityEarth"]["edition"]}   ✅')#line:585
            print (f'更新内容=>> {OO0O00OOOOOO0OOO0["CityEarth"]["content"]}   👍')#line:586
    except Exception as OOO0OO00OOOOO0O00 :#line:587
        print (OOO0OO00OOOOO0O00 )#line:588
def os_qinglong ():#line:591
    if application in os .environ :#line:592
        O00OOO000O00O00O0 =os .environ [application ].split ('\n')#line:593
        if len (O00OOO000O00O00O0 )>0 :#line:594
            return O00OOO000O00O00O0 #line:595
        else :#line:596
            print (f"{application}变量未启用")#line:597
            print ('脚本退出')#line:598
            sys .exit (1 )#line:599
    else :#line:600
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:601
        return os_built ()#line:602
def os_built ():#line:605
    if token :#line:606
        OO000O0O00O0O0OOO =token .split ('\n')#line:607
        if len (OO000O0O00O0O0OOO )>0 :#line:608
            return OO000O0O00O0O0OOO #line:609
    else :#line:610
        print (f"内置变量为空")#line:611
        print ('脚本结束')#line:612
        sys .exit (0 )#line:613
if __name__ =='__main__':#line:616
    start ()#line:617
