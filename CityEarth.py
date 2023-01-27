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
@ 青龙变量  青龙配置文件 export ce_token="authorization&绑定邀请码&赠送金种子id"   不绑定和不赠送填 0   多号换行
@
@ 变量示范    export ce_token="557b8069-1234-4ae7-9e29-b7871f91541b&1937553&0"  用&符号分开数据
@ 我的邀请码是  1937553
@ 版本  0.9
"""
application = 'ce_token'  # 变量名
token = ''


time_xx = random.randint(2, 4)          # 秒 执行下一个号的时间  2到4秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://scsc.sc19319.com'#line:2
level =0 #line:3
def start ():#line:4
    try :#line:5
        update_the_validation ()#line:6
        OOO0O00000000O000 =os_qinglong ()#line:7
        print (f"==========共找到{len(OOO0O00000000O000)}个账号==========")#line:8
        for O0O00OO0000O0O000 in OOO0O00000000O000 :#line:9
            print (f"------------正在执行第{OOO0O00000000O000.index(O0O00OO0000O0O000) + 1}个账号------------")#line:10
            OO0OOO00O00OOOOOO =CityEarth (O0O00OO0000O0O000 )#line:11
            if OO0OOO00O00OOOOOO .base_info ():#line:13
                OO0OOO00O00OOOOOO .game_map ()#line:17
                OO0OOO00O00OOOOOO .friends_invitation ()#line:19
                OO0OOO00O00OOOOOO .add_clover ()#line:21
                OO0OOO00O00OOOOOO .energy ()#line:23
                OO0OOO00O00OOOOOO .synthetic ()#line:25
                OO0OOO00O00OOOOOO .propsraffle ()#line:27
                OO0OOO00O00OOOOOO .crops_illustrated ()#line:29
                OO0OOO00O00OOOOOO .give_gold ()#line:31
            else :#line:32
                print ('token失效')#line:33
            time .sleep (time_xx )#line:35
    except Exception as OO00OOO0OOO0OOO0O :#line:36
        print (OO00OOO0OOO0OOO0O )#line:37
def sign (O0OO0O000OO0O00O0 ):#line:39
    O0OOO00OO0OO0OOOO =hashlib .md5 (O0OO0O000OO0O00O0 .encode ()).hexdigest ()#line:40
    OOOOO0O00O000OOO0 ="scsc%^&*"+O0OOO00OO0OO0OOOO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:41
    O000OOO00O0O000OO =hashlib .md5 (OOOOO0O00O000OOO0 .encode ()).hexdigest ()#line:42
    return O000OOO00O0O000OO #line:43
def timi_new ():#line:45
    return str (int (time .time ()*1000 ))#line:46
class CityEarth :#line:49
    def __init__ (OO00O0O00OOOO0000 ,OOO00O0O0O0O00O00 ):#line:51
        try :#line:52
            OO00O0O00OOOO0000 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:53
            OO00O0O00OOOO0000 .token =OOO00O0O0O0O00O00 .split ('&')[0 ]#line:54
            OO00O0O00OOOO0000 .innerId =OOO00O0O0O0O00O00 .split ('&')[1 ]#line:55
            OO00O0O00OOOO0000 .doneeNo =OOO00O0O0O0O00O00 .split ('&')[2 ]#line:56
        except :#line:57
            print ('变量格式错误')#line:58
    def base_info (OOO00O000OO0O00O0 ):#line:61
        try :#line:62
            O0O0O0O00O00O0OO0 =f'__{timi_new()}'#line:63
            OO0OO0OOO00000O00 ={'authorization':OOO00O000OO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00O00O0OO0 ),'signstring':O0O0O0O00O00O0OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:72
            O000O0OOOOOOOO0OO =requests .request ('get',f'{host}/user',headers =OO0OO0OOO00000O00 ).json ()#line:73
            if 'status'in O000O0OOOOOOOO0OO :#line:75
                if O000O0OOOOOOOO0OO ['status']==200 :#line:76
                    OOO0000OO000O0OOO =O000O0OOOOOOOO0OO ['data']['nickname']#line:77
                    OOOOOO00OOO0O0O00 =O000O0OOOOOOOO0OO ['data']['inner_id']#line:78
                    OO0O0OO0OOO00O0OO =O000O0OOOOOOOO0OO ['data']['assets']['gold']#line:79
                    O00O000OOOOOOO00O =O000O0OOOOOOOO0OO ['data']['level']#line:80
                    print (f'【账号信息】:昵称:{OOO0000OO000O0OOO}丨ID:{str(OOOOOO00OOO0O0O00)[:3] + "**"+ str(OOOOOO00OOO0O0O00)[5:]}丨等级:{O00O000OOOOOOO00O}丨种子:{str(OO0O0OO0OOO00O0OO).split(".")[0]}')#line:81
                if O000O0OOOOOOOO0OO ['status']==401 :#line:82
                    return False #line:83
                if O000O0OOOOOOOO0OO ['status']==500 :#line:84
                    return False #line:85
            return True #line:86
        except Exception as OOO0O00O0O0O000OO :#line:87
            print (OOO0O00O0O0O000OO )#line:88
    def game_map (O0O00OO0000OOOOO0 ):#line:91
        O000000000OOOOOO0 =f'__{timi_new()}'#line:92
        OO0OO0000OO0O0O0O ={'authorization':O0O00OO0000OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000000OOOOOO0 ),'signstring':O000000000OOOOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:101
        OOO00OO0OOOO00O00 =requests .request ('get',f'{host}/game/map',headers =OO0OO0000OO0O0O0O ).json ()#line:102
        if 'status'in OOO00OO0OOOO00O00 :#line:104
            if OOO00OO0OOOO00O00 ['status']==200 :#line:105
                for O0O00O000OOOO0O0O in OOO00OO0OOOO00O00 ['data']['list'][0 ]['crops']:#line:106
                    O0000O0OOOOOOOOOO =O0O00O000OOOO0O0O ['level']#line:108
                    if O0000O0OOOOOOOOOO ==41 :#line:109
                        OOO0OO0OOO0OOO0O0 =O0O00O000OOOO0O0O ['crop_name']#line:110
                        OO0OO0OOO00O0000O =O0O00O000OOOO0O0O ['count']#line:111
                        if OO0OO0OOO00O0000O >0 :#line:112
                            print (f'【农业资产】:{OOO0OO0OOO0OOO0O0}丨数量:{OO0OO0OOO00O0000O}')#line:113
    def give_gold (OOOO0O0OO00OO0OOO ):#line:118
        OOO000OOO0OOO0O00 =f'__{timi_new()}'#line:119
        O00OO0000O0000O0O ={'authorization':OOOO0O0OO00OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOO0OOO0O00 ),'signstring':OOO000OOO0OOO0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:128
        OO0OOOOOOO0OO000O =requests .request ('get',f'{host}/user',headers =O00OO0000O0000O0O ).json ()#line:129
        if 'status'in OO0OOOOOOO0OO000O :#line:130
            if OO0OOOOOOO0OO000O ['status']==200 :#line:131
                if float (OOOO0O0OO00OO0OOO .doneeNo )!=0 :#line:132
                    O0OO00OOO000O0OOO =OO0OOOOOOO0OO000O ['data']['assets']['gold']#line:133
                    if float (O0OO00OOO000O0OOO )>2 :#line:134
                        OOO0OO0O00O0OO0OO =int (float (O0OO00OOO000O0OOO )/1.1 )#line:135
                        OOO000OOO0OOO0O00 =f'_doneeNo={OOOO0O0OO00OO0OOO.doneeNo}&quantity={OOO0OO0O00O0OO0OO}_{timi_new()}'#line:136
                        O00OO0000O0000O0O ={'authorization':OOOO0O0OO00OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOO0OOO0O00 ),'signstring':OOO000OOO0OOO0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:145
                        O0O0OOOO0O00O0O0O ={"quantity":OOO0OO0O00O0OO0OO ,"doneeNo":OOOO0O0OO00OO0OOO .doneeNo }#line:149
                        OOOOOO0O0000OO00O =requests .request ('post',f'{host}/finance/give-gold',headers =O00OO0000O0000O0O ,data =O0O0OOOO0O00O0O0O ).json ()#line:150
                        if 'status'in OOOOOO0O0000OO00O :#line:152
                            if OOOOOO0O0000OO00O ['status']==200 :#line:153
                                if OOOOOO0O0000OO00O ['data']:#line:154
                                    print (f'【赠送种子】:赠送{OOO0OO0O00O0OO0OO}种子给{OOOO0O0OO00OO0OOO.doneeNo}成功')#line:155
                else :#line:156
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:157
    def winning_rewards (O00O00OO00O0000O0 ):#line:159
        O0O00000O00OO000O =f'__{timi_new()}'#line:160
        OOO0O0OOOO00O0OO0 ={'authorization':O00O00OO00O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000O00OO000O ),'signstring':O0O00000O00OO000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
        O00OOO0OOO0O00OOO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO0O0OOOO00O0OO0 ).json ()#line:170
        if 'status'in O00OOO0OOO0O00OOO :#line:172
            if O00OOO0OOO0O00OOO ['status']==200 :#line:173
                if O00OOO0OOO0O00OOO ['data']['amount']:#line:174
                    O0OO000000000O0O0 =O00OOO0OOO0O00OOO ['data']['amount']['gold']#line:175
                    return O0OO000000000O0O0 #line:176
                else :#line:177
                    return 0 #line:178
    def certification (OOO00OOO0OO000OOO ):#line:180
        OOO0O00OO0O000O00 =f'__{timi_new()}'#line:181
        OO000O0O0O000OO0O ={'authorization':OOO00OOO0OO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00OO0O000O00 ),'signstring':OOO0O00OO0O000O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:190
        O0OO0O0OOOOOOOO00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO000O0O0O000OO0O ).json ()#line:191
        if 'status'in O0OO0O0OOOOOOOO00 :#line:193
            if O0OO0O0OOOOOOOO00 ['status']==200 :#line:194
                if O0OO0O0OOOOOOOO00 ['data']['result']:#line:195
                    O0OO00O000O0O0OO0 =O0OO0O0OOOOOOOO00 ['data']['nick_name']#line:196
                    return O0OO00O000O0O0OO0 #line:197
                else :#line:198
                    return '未实名'#line:199
    def crops_illustrated (O0O0OOOO00OOOO0O0 ):#line:202
        OOO0OO0OO00O000OO =f'__{timi_new()}'#line:203
        OOOO0O000OO000O00 ={'authorization':O0O0OOOO00OOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OO00O000OO ),'signstring':OOO0OO0OO00O000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:212
        O0OOOOOO0OO0000OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOOO0O000OO000O00 ).json ()#line:213
        if 'status'in O0OOOOOO0OO0000OO :#line:215
            if O0OOOOOO0OO0000OO ['status']==200 :#line:216
                O00O000OOOOO00OO0 =O0OOOOOO0OO0000OO ['data'][0 ]['crops']#line:217
                for O00O0OOO00000OOO0 in O00O000OOOOO00OO0 :#line:218
                    if O00O0OOO00000OOO0 ['ill_clover_award']:#line:219
                        if float (O00O0OOO00000OOO0 ['ill_clover_award'])>1 :#line:220
                            if O00O0OOO00000OOO0 ['is_finish']:#line:221
                                if not O00O0OOO00000OOO0 ['is_getit']:#line:222
                                    OOO0OO0OO00O000OO =f'_award_level={O00O0OOO00000OOO0["level"]}_{timi_new()}'#line:223
                                    OOOO0O000OO000O00 ={'authorization':O0O0OOOO00OOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OO00O000OO ),'signstring':OOO0OO0OO00O000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:232
                                    OO0OO0OOO00000OOO ={"award_level":O00O0OOO00000OOO0 ['level']}#line:233
                                    O00OOO0OOO00O00O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOOO0O000OO000O00 ,json =OO0OO0OOO00000OOO ).json ()#line:234
                                    if 'status'in O00OOO0OOO00O00O0 :#line:235
                                        if O00OOO0OOO00O00O0 ['status']==200 :#line:236
                                            OO0O00OOOO00OOOOO =O00OOO0OOO00O00O0 ['data']['ill_clover_award']#line:237
                                            print (f'【图鉴奖励】:领取{O00O0OOO00000OOO0["crop_name"]}成就丨奖励{OO0O00OOOO00OOOOO}叶子成功')#line:238
                                        if O00OOO0OOO00O00O0 ['status']==500 :#line:239
                                            print (f'【图鉴奖励】:{O00OOO0OOO00O00O0["message"]}')#line:240
    def watched_ad (O000OO0O00OOO0OOO ):#line:243
        OOOO0O0O0OOOO0O00 =f'__{timi_new()}'#line:244
        O000O0OOOOOOOO00O ={'authorization':O000OO0O00OOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O0OOOO0O00 ),'signstring':OOOO0O0O0OOOO0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:253
        OO0OOO0OOO00O0OO0 =requests .request ('post',f'{host}/game/watched-ad',headers =O000O0OOOOOOOO00O ).json ()#line:254
        print (OO0OOO0OOO00O0OO0 )#line:255
    def user_ad (O00O00000O00OO0OO ):#line:260
        O0OOO0OO0O0OOO000 =f'__{timi_new()}'#line:261
        O00OO00OO0000O000 ={'authorization':O00O00000O00OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO0O0OOO000 ),'signstring':O0OOO0OO0O0OOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:270
        O0O0OOOO0O00O00OO =requests .request ('get',f'{host}/user/ad',headers =O00OO00OO0000O000 ).json ()#line:271
        if 'status'in O0O0OOOO0O00O00OO :#line:273
            if O0O0OOOO0O00O00OO ['status']==200 :#line:274
                OO0O00OO00OOO000O =O0O0OOOO0O00O00OO ['data']['max_time']#line:275
                O0OOO00OOOO0O0OO0 =O0O0OOOO0O00O00OO ['data']['watch_time']#line:276
                OOOO0O0O0O00OOO00 =O0O0OOOO0O00O00OO ['data']['added_time']#line:277
                print (f'【获取种子】:获取种子剩余{OOOO0O0O0O00OOO00 + OO0O00OO00OOO000O - O0OOO00OOOO0O0OO0}次丨好友提供:{OOOO0O0O0O00OOO00}次')#line:278
                if OOOO0O0O0O00OOO00 +OO0O00OO00OOO000O -O0OOO00OOOO0O0OO0 >0 :#line:279
                    time .sleep (random .randint (16 ,19 ))#line:280
                    OOOOO00O0000OO00O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00OO00OO0000O000 ).json ()#line:281
                    if 'status'in OOOOO00O0000OO00O :#line:283
                        if OOOOO00O0000OO00O ['status']==200 :#line:284
                            OOOO0OOO000O0O00O =OOOOO00O0000OO00O ['data']['silver']#line:285
                            print (f'【获取种子】:获得种子:{OOOO0OOO000O0O00O}')#line:286
                            return True #line:287
                        if OOOOO00O0000OO00O ['status']==500 :#line:288
                            OO0OO000O00000OO0 =OOOOO00O0000OO00O ['message']#line:289
                            print (f'【获取种子】:{OO0OO000O00000OO0}')#line:290
                            return False #line:291
    def synthetic (OOOOO0O0OOOO00O00 ):#line:294
        global id ,g ,level #line:295
        try :#line:296
            level =0 #line:297
            while True :#line:298
                O0000O0O00OOO00OO =f'__{timi_new()}'#line:299
                O0000OO00O000OOO0 ={'authorization':OOOOO0O0OOOO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0O00OOO00OO ),'signstring':O0000O0O00OOO00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:308
                O00O000OOO0O00O00 =requests .request ('get',f'{host}/game/getAllData',headers =O0000OO00O000OOO0 ).json ()#line:309
                if 'status'in O00O000OOO0O00O00 :#line:311
                    if O00O000OOO0O00O00 ['status']==200 :#line:312
                        OOO0O0000O0O0OO00 =O00O000OOO0O00O00 ['data']['cropList']#line:313
                        O00OO00O00OO00OOO =O00O000OOO0O00O00 ['data']['gameCoreDataDBid']#line:314
                        O00OOOOOOOOOOO000 =0 #line:315
                        for O0O0OOO00O000O0O0 in OOO0O0000O0O0OO00 :#line:316
                            if not O0O0OOO00O000O0O0 :#line:317
                                O00000OO000O0000O =f'_crop_id={O00OO00O00OO00OOO}&site={O00OOOOOOOOOOO000}_{OOOOO0O0OOOO00O00.time}'#line:318
                                OO0000O000OOOOOOO ={'authorization':OOOOO0O0OOOO00O00 .token ,'timestamp':OOOOO0O0OOOO00O00 .time ,'sign':sign (O00000OO000O0000O ),'signstring':O00000OO000O0000O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:327
                                OO0O0O0000O00OO0O ={"site":O00OOOOOOOOOOO000 ,"crop_id":O00OO00O00OO00OOO }#line:328
                                O0000000O0000OOOO =requests .request ('post',f'{host}/game/crops/buy',headers =OO0000O000OOOOOOO ,data =OO0O0O0000O00OO0O ).json ()#line:329
                                time .sleep (random .randint (1 ,3 )/10 )#line:331
                                if 'status'in O0000000O0000OOOO :#line:332
                                    if O0000000O0000OOOO ['status']==200 :#line:333
                                        if O0000000O0000OOOO ['message']=='种子数量不足':#line:334
                                            level =OOOOO0O0OOOO00O00 .level_new ()#line:335
                                            print (f'【购买合成】:{O0000000O0000OOOO["message"]}')#line:336
                                            if not OOOOO0O0OOOO00O00 .user_ad ():#line:337
                                                return False #line:338
                                        print (f'【购买合成】:购买农作物,位置{O00OOOOOOOOOOO000}')#line:339
                                    if O0000000O0000OOOO ['status']==500 :#line:340
                                        print (f'【购买合成】:{O0000000O0000OOOO["message"]}')#line:341
                                        return False #line:342
                            O00OOOOOOOOOOO000 +=1 #line:343
                        O00OOOOO00OOOOOOO =requests .request ('get',f'{host}/game/getAllData',headers =O0000OO00O000OOO0 ).json ()#line:344
                        OOO000O000000OO00 =O00OOOOO00OOOOOOO ['data']['cropList']#line:345
                        O0OOO000O0000OO00 =False #line:346
                        for O0O0OOO00O000O0O0 in range (12 ):#line:347
                            id =OOO000O000000OO00 [O0O0OOO00O000O0O0 ]['level']#line:348
                            if float (level )-float (id )>9 :#line:349
                                OOOO0OOO00OO0OOO0 =f'_site={O0O0OOO00O000O0O0}_{timi_new()}'#line:350
                                O000OOOOOOO00O000 ={'accept':'application/json, text/plain, */*','authorization':OOOOO0O0OOOO00O00 .token ,'timestamp':timi_new (),'sign':sign (OOOO0OOO00OO0OOO0 ),'signstring':OOOO0OOO00OO0OOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:360
                                O0OO000OO0O000O00 ={"site":O0O0OOO00O000O0O0 }#line:361
                                O0OOOOOOO0OOOOO00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000OOOOOOO00O000 ,data =O0OO000OO0O000O00 ).json ()#line:362
                                if 'status'in O0OOOOOOO0OOOOO00 :#line:364
                                    if O0OOOOOOO0OOOOO00 ['status']==200 :#line:365
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:366
                            if id !=0 :#line:367
                                for OO0O0000OO00000OO in range (11 ):#line:368
                                    O00O00O0OOO0O00OO =OO0O0000OO00000OO +1 #line:369
                                    g =OOO000O000000OO00 [O00O00O0OOO0O00OO ]['level']#line:370
                                    if id ==g :#line:371
                                        O0O00OOO00O00OO0O =OO0O0000OO00000OO +2 #line:372
                                        if O0O00OOO00O00OO0O ==O0O0OOO00O000O0O0 +1 :#line:373
                                            pass #line:374
                                        else :#line:375
                                            O0OOO0OOO00O0OOOO =O0O0OOO00O000O0O0 +1 #line:376
                                            time .sleep (random .randint (1 ,3 )/10 )#line:378
                                            OOOO0O0000OOOO00O =f'_site={O0OOO0OOO00O0OOOO-1}&targetSite={O0O00OOO00O00OO0O-1}_{timi_new()}'#line:379
                                            OOO0O00O0OO0O0OOO ={'accept':'application/json, text/plain, */*','authorization':OOOOO0O0OOOO00O00 .token ,'timestamp':timi_new (),'sign':sign (OOOO0O0000OOOO00O ),'signstring':OOOO0O0000OOOO00O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:394
                                            O0O0O000OOOO00O0O ={"site":int (O0OOO0OOO00O0OOOO -1 ),"targetSite":int (O0O00OOO00O00OO0O -1 )}#line:395
                                            O0O0O00OO0OOOO0OO =requests .request ('post',f'{host}/game/crops/move',headers =OOO0O00O0OO0O0OOO ,json =O0O0O000OOOO00O0O ).json ()#line:396
                                            if 'status'in O0O0O00OO0OOOO0OO :#line:397
                                                if O0O0O00OO0OOOO0OO ['status']==200 :#line:398
                                                    pass #line:399
                                            print ('【购买合成】:',O0OOO0OOO00O0OOOO ,O0O00OOO00O00OO0O ,'合成成功')#line:401
                                            O0OOO000O0000OO00 =True #line:402
                                    if O0OOO000O0000OO00 :#line:403
                                        break #line:404
                                if O0OOO000O0000OO00 :#line:405
                                    break #line:406
        except Exception as O0O000OOOO0000O0O :#line:407
            OOOOO0O0OOOO00O00 .synthetic ()#line:408
    def level_new (O00O0O00OOO0O00OO ):#line:411
        try :#line:412
            OO0O0O0O0OO0O0000 =f'__{timi_new()}'#line:413
            O000OO0O0OOOO000O ={'authorization':O00O0O00OOO0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0O0OO0O0000 ),'signstring':OO0O0O0O0OO0O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:422
            OOO0000OO000000O0 =requests .request ('get',f'{host}/user',headers =O000OO0O0OOOO000O ).json ()#line:423
            if 'status'in OOO0000OO000000O0 :#line:424
                if OOO0000OO000000O0 ['status']==200 :#line:425
                    return float (OOO0000OO000000O0 ['data']['level'])#line:426
        except Exception as OOO0O0OOO00O0O00O :#line:427
            print (OOO0O0OOO00O0O00O )#line:428
    def propsraffle (O0O0000000OOO00O0 ):#line:432
        try :#line:433
            while True :#line:434
                O00000OO0OOO00O0O =f'__{timi_new()}'#line:435
                O0O000O00O0O0OO0O ={'authorization':O0O0000000OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO0OOO00O0O ),'signstring':O00000OO0OOO00O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:444
                OOO00OO0O00OO0OO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O000O00O0O0OO0O ).json ()#line:445
                if 'status'in OOO00OO0O00OO0OO0 :#line:447
                    if OOO00OO0O00OO0OO0 ['status']==200 :#line:448
                        O000O0000O0OOOO0O =OOO00OO0O00OO0OO0 ['data']['rows']#line:449
                        O0O0000O0O0O0OO0O =OOO00OO0O00OO0OO0 ['data']['vstate']#line:450
                        if O000O0000O0OOOO0O ==5 or O000O0000O0OOOO0O ==6 or O000O0000O0OOOO0O ==7 :#line:451
                            OOOO0000OOOO00O0O =OOO00OO0O00OO0OO0 ['data']['silver']#line:452
                            print (f'【转盘抽奖】:获得种子:{OOOO0000OOOO00O0O}')#line:453
                        if O000O0000O0OOOO0O ==1 or O000O0000O0OOOO0O ==2 or O000O0000O0OOOO0O ==3 :#line:454
                            O000O0O0OOOO0000O =OOO00OO0O00OO0OO0 ['data']['clover']#line:455
                            print (f'【转盘抽奖】:获得三叶草:{O000O0O0OOOO0000O}')#line:456
                        if O000O0000O0OOOO0O ==4 or O000O0000O0OOOO0O ==8 :#line:457
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:458
                        if O000O0000O0OOOO0O =='抽奖次数已用完':#line:462
                            if O0O0000O0O0O0OO0O :#line:463
                                O0OOO0O0000OO00O0 =random .randint (160 ,190 )/10 #line:464
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{O0OOO0O0000OO00O0}秒获取抽奖机会')#line:465
                                time .sleep (O0OOO0O0000OO00O0 )#line:466
                                OO00OO0O0OO0OO0O0 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O0O000O00O0O0OO0O ).json ()#line:467
                                if 'status'in OO00OO0O0OO0OO0O0 :#line:469
                                    if OO00OO0O0OO0OO0O0 ['status']==200 :#line:470
                                        print (f'【转盘抽奖】:{OO00OO0O0OO0OO0O0["message"]}')#line:471
                                    if OO00OO0O0OO0OO0O0 ['status']==500 :#line:472
                                        print (f'【转盘抽奖】:{OO00OO0O0OO0OO0O0["message"]}')#line:473
                                        break #line:474
                                time .sleep (random .randint (10 ,15 )/10 )#line:475
                            else :#line:476
                                break #line:477
                time .sleep (random .randint (8 ,15 )/10 )#line:478
        except Exception as OO00OO0000OOOO000 :#line:479
            print (OO00OO0000OOOO000 )#line:480
    def friends_invitation (OOO000O00O000OO0O ):#line:483
        try :#line:484
            OOO00O00OO0000OOO =f'__{timi_new()}'#line:485
            OOO0O000O0OO0OO0O ={'authorization':OOO000O00O000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00OO0000OOO ),'signstring':OOO00O00OO0000OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:494
            OO0OOOOOO0OO000OO =requests .request ('get',f'{host}/friends',headers =OOO0O000O0OO0OO0O ).json ()#line:495
            if 'status'in OO0OOOOOO0OO000OO :#line:496
                if OO0OOOOOO0OO000OO ['status']==200 :#line:497
                    OO0O00O0O0O00O00O =OO0OOOOOO0OO000OO ['data']['myInviteter']#line:498
                    if OO0O00O0O0O00O00O :#line:499
                        OO000OO0O0O0OO0OO =OO0O00O0O0O00O00O ['user']['nickname']#line:500
                        OOOOOOO0OOOOOOO0O =OOO000O00O000OO0O .certification ()#line:501
                        print (f'【绑邀请码】:我的邀请人:{OO000OO0O0O0OO0OO}丨实名:{OOOOOOO0OOOOOOO0O}')#line:502
                    else :#line:503
                        if OOO000O00O000OO0O .innerId !='0':#line:504
                            OOO00O00OO0000OOO =f'_innerId={OOO000O00O000OO0O.innerId}_{timi_new()}'#line:505
                            OOO0O000O0OO0OO0O ={'authorization':OOO000O00O000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00OO0000OOO ),'signstring':OOO00O00OO0000OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:514
                            O000000O000OOOO00 ={"innerId":OOO000O00O000OO0O .innerId }#line:515
                            O00OO00OOOOOO000O =requests .request ('post',f'{host}/friends/my-invitation',headers =OOO0O000O0OO0OO0O ,data =O000000O000OOOO00 ).json ()#line:516
                            if 'status'in O00OO00OOOOOO000O :#line:517
                                if O00OO00OOOOOO000O ['status']==200 :#line:518
                                    print (f'【绑邀请码】:{OOO000O00O000OO0O.innerId}{O00OO00OOOOOO000O["message"]}')#line:519
                        else :#line:520
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:521
        except Exception as O00O000OOOO00O0O0 :#line:522
            print (O00O000OOOO00O0O0 )#line:523
    def add_clover (O00OO0O000000O00O ):#line:527
        try :#line:528
            OOOO0OOOOO000OOO0 =f'__{timi_new()}'#line:529
            O0OOOOO0OOO0O00O0 ={'authorization':O00OO0O000000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOOO000OOO0 ),'signstring':OOOO0OOOOO000OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:538
            O0O0O000O00O0OO00 =requests .request ('get',f'{host}/assets/clovers',headers =O0OOOOO0OOO0O00O0 ).json ()#line:539
            if 'status'in O0O0O000O00O0OO00 :#line:541
                if O0O0O000O00O0OO00 ['status']==200 :#line:542
                    OO0O0O000O0OOOOOO =O0O0O000O00O0OO00 ['data']['clover']#line:543
                    OOOOO00O0OOO0O00O =O0O0O000O00O0OO00 ['data']['used_clover']#line:544
                    OOOO0OO0000O0OOO0 =float (OO0O0O000O0OOOOOO )-float (OOOOO00O0OOO0O00O )#line:545
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OOOOO00O0OOO0O00O}')#line:546
                    if OOOO0OO0000O0OOO0 >1 :#line:547
                        OOOO0OOOOO000OOO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOO0OO0000O0OOO0)}_{timi_new()}'#line:548
                        O0OOOOO0OOO0O00O0 ={'authorization':O00OO0O000000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOOO000OOO0 ),'signstring':OOOO0OOOOO000OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:557
                        O000O00OO000OOO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOO0OO0000O0OOO0 )}#line:558
                        OO0000OOOO00OO0O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OOOOO0OOO0O00O0 ,data =O000O00OO000OOO00 ).json ()#line:559
                        if 'status'in OO0000OOOO00OO0O0 :#line:561
                            if OO0000OOOO00OO0O0 ['status']==200 :#line:562
                                print (f'【参与抽奖】:添加三叶草:{OO0000OOOO00OO0O0["data"]}丨数量:{OOOO0OO0000O0OOO0}')#line:563
            OO000O00O000O0000 =requests .request ('get',f'{host}/lottery',headers =O0OOOOO0OOO0O00O0 ).json ()#line:564
            O0OOOO0O000OO00OO =O00OO0O000000O00O .winning_rewards ()#line:566
            if 'status'in OO000O00O000O0000 :#line:567
                if OO000O00O000O0000 ['status']==200 :#line:568
                    O00O0O0O0OOO0O0O0 =OO000O00O000O0000 ['data'][0 ]['day_get_gold_quantity']#line:569
                    print (f'【参与抽奖】:预计每天中{O00O0O0O0OOO0O0O0[:6]}种子丨好友收益:{O0OOOO0O000OO00OO}')#line:570
        except Exception as OOO00OO00O00OO0O0 :#line:571
            print (OOO00OO00O00OO0O0 )#line:572
    def energy (O00O0OOOO000000O0 ):#line:575
        O00OOOOO0O000O00O =f'__{timi_new()}'#line:576
        OOO0000O00000OOO0 ={'authorization':O00O0OOOO000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOO0O000O00O ),'signstring':O00OOOOO0O000O00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:585
        O0O0OOOOOO0O00O00 =requests .request ('get',f'{host}/energy/general',headers =OOO0000O00000OOO0 ).json ()#line:586
        if 'status'in O0O0OOOOOO0O00O00 :#line:588
            if O0O0OOOOOO0O00O00 ['status']==200 :#line:589
                OO0000OOO0000000O =O0O0OOOOOO0O00O00 ['data']['ordinary_water_consumptions']#line:590
                if float (OO0000OOO0000000O )<80 :#line:591
                    OO0000OO000O0OOOO =99 -float (OO0000OOO0000000O )#line:592
                    OOO0OOOOO00O0OO00 ={"fertilizer":str (OO0000OO000O0OOOO ).split ('.')[0 ]}#line:593
                    OOOO0OO0O0O0O0OOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO0000O00000OOO0 ,data =OOO0OOOOO00O0OO00 ).json ()#line:594
                    if 'status'in OOOO0OO0O0O0O0OOO :#line:596
                        if OOOO0OO0O0O0O0OOO ['status']==200 :#line:597
                            print (f'【购买肥料】:{OOOO0OO0O0O0O0OOO["message"]}')#line:598
                OO0000OOO00O0O0O0 =O0O0OOOOOO0O00O00 ['data']['ordinary_water_consumptions']#line:599
                if float (OO0000OOO00O0O0O0 )<800 :#line:600
                    O0OO0000OO00OO000 =999 -float (OO0000OOO00O0O0O0 )#line:601
                    OO0O0O0OOO00000OO ={"water":str (O0OO0000OO00OO000 ).split ('.')[0 ]}#line:602
                    OOOOO0O0O000O0000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO0000O00000OOO0 ,data =OO0O0O0OOO00000OO ).json ()#line:603
                    if 'status'in OOOOO0O0O000O0000 :#line:604
                        if OOOOO0O0O000O0000 ['status']==200 :#line:605
                            print (f'【购买水滴】:{OOOOO0O0O000O0000["message"]}')#line:606
def version_of_the_validation ():#line:612
    return str ((65 -56 )/10 )#line:613
def gitee_validation ():#line:615
    try :#line:616
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:617
    except Exception as OOOOO00O00O0O00OO :#line:618
        sys .exit (0 )#line:619
def update_the_validation ():#line:625
    try :#line:626
        O0O0O0O0000OOO0OO =gitee_validation ()#line:627
        if version_of_the_validation ()<O0O0O0O0000OOO0OO ['CityEarth']['edition']:#line:628
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0O0O0000OOO0OO["CityEarth"]["edition"]}   ❌')#line:629
            print (f'更新内容=>>{O0O0O0O0000OOO0OO["CityEarth"]["content"]}   👍')#line:630
        else :#line:631
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0O0O0000OOO0OO["CityEarth"]["edition"]}   ✅')#line:632
            print (f'更新内容=>> {O0O0O0O0000OOO0OO["CityEarth"]["content"]}   👍')#line:633
    except Exception as OO000OO00OO00OOOO :#line:634
        print (OO000OO00OO00OOOO )#line:635
def os_qinglong ():#line:638
    if application in os .environ :#line:639
        O0O0O0OO0O000OOOO =os .environ [application ].split ('\n')#line:640
        if len (O0O0O0OO0O000OOOO )>0 :#line:641
            return O0O0O0OO0O000OOOO #line:642
        else :#line:643
            print (f"{application}变量未启用")#line:644
            print ('脚本退出')#line:645
            sys .exit (1 )#line:646
    else :#line:647
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:648
        return os_built ()#line:649
def os_built ():#line:652
    if token :#line:653
        OOO000O0OO0000OOO =token .split ('\n')#line:654
        if len (OOO000O0OO0000OOO )>0 :#line:655
            return OOO000O0OO0000OOO #line:656
    else :#line:657
        print (f"内置变量为空")#line:658
        print ('脚本结束')#line:659
        sys .exit (0 )#line:660
if __name__ =='__main__':#line:663
    start ()#line:664
