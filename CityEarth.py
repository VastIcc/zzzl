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
        OOO0O0000000O0O00 =os_qinglong ()#line:7
        print (f"==========共找到{len(OOO0O0000000O0O00)}个账号==========")#line:8
        for OOO0O0O00O0OOO0OO in OOO0O0000000O0O00 :#line:9
            print (f"------------正在执行第{OOO0O0000000O0O00.index(OOO0O0O00O0OOO0OO) + 1}个账号------------")#line:10
            OO0OO0O0O0O0O00OO =CityEarth (OOO0O0O00O0OOO0OO )#line:11
            if OO0OO0O0O0O0O00OO .base_info ():#line:13
                OO0OO0O0O0O0O00OO .game_map ()#line:17
                OO0OO0O0O0O0O00OO .friends_invitation ()#line:19
                OO0OO0O0O0O0O00OO .add_clover ()#line:21
                OO0OO0O0O0O0O00OO .energy ()#line:23
                OO0OO0O0O0O0O00OO .synthetic ()#line:25
                OO0OO0O0O0O0O00OO .propsraffle ()#line:27
                OO0OO0O0O0O0O00OO .crops_illustrated ()#line:29
                OO0OO0O0O0O0O00OO .give_gold ()#line:31
            else :#line:32
                print ('token失效')#line:33
            time .sleep (time_xx )#line:35
    except Exception as O0O00OOOO00OOOOOO :#line:36
        print (O0O00OOOO00OOOOOO )#line:37
def sign (OO0O0OO0OO00O0OOO ):#line:39
    O000OOO00000OO000 =hashlib .md5 (OO0O0OO0OO00O0OOO .encode ()).hexdigest ()#line:40
    OO0OOO0O00O0OOO00 ="scsc%^&*"+O000OOO00000OO000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:41
    O000O00O00O00O000 =hashlib .md5 (OO0OOO0O00O0OOO00 .encode ()).hexdigest ()#line:42
    return O000O00O00O00O000 #line:43
def timi_new ():#line:45
    return str (int (time .time ()*1000 ))#line:46
class CityEarth :#line:49
    def __init__ (OO00O000OO0O0OOOO ,O0000OO0O00O00OOO ):#line:51
        try :#line:52
            OO00O000OO0O0OOOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:53
            OO00O000OO0O0OOOO .token =O0000OO0O00O00OOO .split ('&')[0 ]#line:54
            OO00O000OO0O0OOOO .innerId =O0000OO0O00O00OOO .split ('&')[1 ]#line:55
            OO00O000OO0O0OOOO .doneeNo =O0000OO0O00O00OOO .split ('&')[2 ]#line:56
        except :#line:57
            print ('变量格式错误')#line:58
    def base_info (O0OO00OOOO0000OOO ):#line:61
        try :#line:62
            O0OOOOO0OO0O0O0O0 =f'__{timi_new()}'#line:63
            OOO000O0O0OO00OO0 ={'authorization':O0OO00OOOO0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0OO0O0O0O0 ),'signstring':O0OOOOO0OO0O0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:72
            OOOO000OO00O0OOOO =requests .request ('get',f'{host}/user',headers =OOO000O0O0OO00OO0 ).json ()#line:73
            if 'status'in OOOO000OO00O0OOOO :#line:75
                if OOOO000OO00O0OOOO ['status']==200 :#line:76
                    OO00O0O0O0OOO00OO =OOOO000OO00O0OOOO ['data']['nickname']#line:77
                    O0O00O0OOOO00OO00 =OOOO000OO00O0OOOO ['data']['inner_id']#line:78
                    O0OO000OOO0O0O0O0 =OOOO000OO00O0OOOO ['data']['assets']['gold']#line:79
                    O0000O0O00OOO0OOO =OOOO000OO00O0OOOO ['data']['level']#line:80
                    print (f'【账号信息】:昵称:{OO00O0O0O0OOO00OO}丨ID:{str(O0O00O0OOOO00OO00)[:3] + "**"+ str(O0O00O0OOOO00OO00)[5:]}丨等级:{O0000O0O00OOO0OOO}丨种子:{str(O0OO000OOO0O0O0O0).split(".")[0]}')#line:81
                if OOOO000OO00O0OOOO ['status']==401 :#line:82
                    return False #line:83
                if OOOO000OO00O0OOOO ['status']==500 :#line:84
                    return False #line:85
            return True #line:86
        except Exception as O0OO000O0O0OO00OO :#line:87
            print (O0OO000O0O0OO00OO )#line:88
    def game_map (O0O0000O0OO000O0O ):#line:91
        O000O00OO0O00O0O0 =f'__{timi_new()}'#line:92
        OOO0OOOO0OOO00000 ={'authorization':O0O0000O0OO000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00OO0O00O0O0 ),'signstring':O000O00OO0O00O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:101
        OO0O0OOOOOO0OO00O =requests .request ('get',f'{host}/game/map',headers =OOO0OOOO0OOO00000 ).json ()#line:102
        if 'status'in OO0O0OOOOOO0OO00O :#line:104
            if OO0O0OOOOOO0OO00O ['status']==200 :#line:105
                for OO0O0O0OOOOOO0000 in OO0O0OOOOOO0OO00O ['data']['list'][0 ]['crops']:#line:106
                    O000OOOOO0OO00O0O =OO0O0O0OOOOOO0000 ['level']#line:108
                    if O000OOOOO0OO00O0O ==41 :#line:109
                        OO0O000O00OO000O0 =OO0O0O0OOOOOO0000 ['crop_name']#line:110
                        OOOO0O00O0OO00OO0 =OO0O0O0OOOOOO0000 ['count']#line:111
                        if OOOO0O00O0OO00OO0 >0 :#line:112
                            print (f'【农业资产】:{OO0O000O00OO000O0}丨数量:{OOOO0O00O0OO00OO0}')#line:113
    def give_gold (OO00OO0OO000O0OO0 ):#line:118
        OO0O00OOOOO0O0OOO =f'__{timi_new()}'#line:119
        OO000OOO00O000000 ={'authorization':OO00OO0OO000O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOOOO0O0OOO ),'signstring':OO0O00OOOOO0O0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:128
        OO0O0000OOO0000OO =requests .request ('get',f'{host}/user',headers =OO000OOO00O000000 ).json ()#line:129
        if 'status'in OO0O0000OOO0000OO :#line:130
            if OO0O0000OOO0000OO ['status']==200 :#line:131
                if float (OO00OO0OO000O0OO0 .doneeNo )!=0 :#line:132
                    O0OO0OOO00O0000O0 =OO0O0000OOO0000OO ['data']['assets']['gold']#line:133
                    if float (O0OO0OOO00O0000O0 )>2 :#line:134
                        OO00O00OOOOOO0OOO =int (float (O0OO0OOO00O0000O0 )/1.1 )#line:135
                        OO0O00OOOOO0O0OOO =f'_doneeNo={OO00OO0OO000O0OO0.doneeNo}&quantity={OO00O00OOOOOO0OOO}_{timi_new()}'#line:136
                        OO000OOO00O000000 ={'authorization':OO00OO0OO000O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOOOO0O0OOO ),'signstring':OO0O00OOOOO0O0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:145
                        OOOO0O0OOOOOOO0O0 ={"quantity":OO00O00OOOOOO0OOO ,"doneeNo":OO00OO0OO000O0OO0 .doneeNo }#line:149
                        OO00OOO00OOO00000 =requests .request ('post',f'{host}/finance/give-gold',headers =OO000OOO00O000000 ,data =OOOO0O0OOOOOOO0O0 ).json ()#line:150
                        if 'status'in OO00OOO00OOO00000 :#line:152
                            if OO00OOO00OOO00000 ['status']==200 :#line:153
                                if OO00OOO00OOO00000 ['data']:#line:154
                                    print (f'【赠送种子】:赠送{OO00O00OOOOOO0OOO}种子给{OO00OO0OO000O0OO0.doneeNo}成功')#line:155
                else :#line:156
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:157
    def winning_rewards (OOOO00OO0O0O0000O ):#line:159
        O00OOO0O0000O00O0 =f'__{timi_new()}'#line:160
        OO000O0O000O00OOO ={'authorization':OOOO00OO0O0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0O0000O00O0 ),'signstring':O00OOO0O0000O00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
        O0O000OO000OOO0OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO000O0O000O00OOO ).json ()#line:170
        if 'status'in O0O000OO000OOO0OO :#line:172
            if O0O000OO000OOO0OO ['status']==200 :#line:173
                if O0O000OO000OOO0OO ['data']['amount']:#line:174
                    OOOOO0000O0000000 =O0O000OO000OOO0OO ['data']['amount']['gold']#line:175
                    return OOOOO0000O0000000 #line:176
                else :#line:177
                    return 0 #line:178
    def certification (OO0O0O00OOOO0O0O0 ):#line:180
        O0O00OOO0000O000O =f'__{timi_new()}'#line:181
        OO000000OOO0OOOO0 ={'authorization':OO0O0O00OOOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO0000O000O ),'signstring':O0O00OOO0000O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:190
        OO0OOOOOOOO00OOO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO000000OOO0OOOO0 ).json ()#line:191
        if 'status'in OO0OOOOOOOO00OOO0 :#line:193
            if OO0OOOOOOOO00OOO0 ['status']==200 :#line:194
                if OO0OOOOOOOO00OOO0 ['data']['result']:#line:195
                    OOOO0OO00O00O000O =OO0OOOOOOOO00OOO0 ['data']['nick_name']#line:196
                    return OOOO0OO00O00O000O #line:197
                else :#line:198
                    return '未实名'#line:199
    def crops_illustrated (O0O00O0OOO00000O0 ):#line:202
        OOO0O0O0O0OOOOO0O =f'__{timi_new()}'#line:203
        OO0000000O0O00O0O ={'authorization':O0O00O0OOO00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0O0OOOOO0O ),'signstring':OOO0O0O0O0OOOOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:212
        OO0OO000000O00O0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0000000O0O00O0O ).json ()#line:213
        if 'status'in OO0OO000000O00O0O :#line:215
            if OO0OO000000O00O0O ['status']==200 :#line:216
                O00OOO0OOO000O0OO =OO0OO000000O00O0O ['data'][0 ]['crops']#line:217
                for OOOO0000O0O00O0OO in O00OOO0OOO000O0OO :#line:218
                    if OOOO0000O0O00O0OO ['ill_clover_award']:#line:219
                        if float (OOOO0000O0O00O0OO ['ill_clover_award'])>1 :#line:220
                            if OOOO0000O0O00O0OO ['is_finish']:#line:221
                                if not OOOO0000O0O00O0OO ['is_getit']:#line:222
                                    OOO0O0O0O0OOOOO0O =f'_award_level={OOOO0000O0O00O0OO["level"]}_{timi_new()}'#line:223
                                    OO0000000O0O00O0O ={'authorization':O0O00O0OOO00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0O0OOOOO0O ),'signstring':OOO0O0O0O0OOOOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:232
                                    OOOO0OOO0OOOO0OO0 ={"award_level":OOOO0000O0O00O0OO ['level']}#line:233
                                    O0O00OOOO0OO00OOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0000000O0O00O0O ,json =OOOO0OOO0OOOO0OO0 ).json ()#line:234
                                    if 'status'in O0O00OOOO0OO00OOO :#line:235
                                        if O0O00OOOO0OO00OOO ['status']==200 :#line:236
                                            OO0O00OO000O000O0 =O0O00OOOO0OO00OOO ['data']['ill_clover_award']#line:237
                                            print (f'【图鉴奖励】:领取{OOOO0000O0O00O0OO["crop_name"]}成就丨奖励{OO0O00OO000O000O0}叶子成功')#line:238
                                        if O0O00OOOO0OO00OOO ['status']==500 :#line:239
                                            print (f'【图鉴奖励】:{O0O00OOOO0OO00OOO["message"]}')#line:240
    def watched_ad (OO0OOO00OOO0O0OO0 ):#line:243
        OOOO00O00O000000O =f'__{timi_new()}'#line:244
        OO0OOOO00O0O0OOOO ={'authorization':OO0OOO00OOO0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O00O000000O ),'signstring':OOOO00O00O000000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:253
        OO00OO0O0OOO0OOO0 =requests .request ('post',f'{host}/game/watched-ad',headers =OO0OOOO00O0O0OOOO ).json ()#line:254
        print (OO00OO0O0OOO0OOO0 )#line:255
    def user_ad (OO00OO00OOO0OO0O0 ):#line:260
        OOO000O00O00OOO00 =f'__{timi_new()}'#line:261
        OOO0OO00O00OO0000 ={'authorization':OO00OO00OOO0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O00O00OOO00 ),'signstring':OOO000O00O00OOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:270
        O000O0OOO00O00OO0 =requests .request ('get',f'{host}/user/ad',headers =OOO0OO00O00OO0000 ).json ()#line:271
        if 'status'in O000O0OOO00O00OO0 :#line:273
            if O000O0OOO00O00OO0 ['status']==200 :#line:274
                OOOOO00O0OO0O0OOO =O000O0OOO00O00OO0 ['data']['max_time']#line:275
                OO000OO00000OO00O =O000O0OOO00O00OO0 ['data']['watch_time']#line:276
                O0000OO0O00OOOO00 =O000O0OOO00O00OO0 ['data']['added_time']#line:277
                print (f'【获取种子】:获取种子剩余{O0000OO0O00OOOO00 + OOOOO00O0OO0O0OOO - OO000OO00000OO00O}次丨好友提供:{O0000OO0O00OOOO00}次')#line:278
                if O0000OO0O00OOOO00 +OOOOO00O0OO0O0OOO -OO000OO00000OO00O >0 :#line:279
                    time .sleep (random .randint (16 ,19 ))#line:280
                    O0OO00O0O00O0OO00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO0OO00O00OO0000 ).json ()#line:281
                    if 'status'in O0OO00O0O00O0OO00 :#line:283
                        if O0OO00O0O00O0OO00 ['status']==200 :#line:284
                            OO00OOO0000O0O000 =O0OO00O0O00O0OO00 ['data']['silver']#line:285
                            print (f'【获取种子】:获得种子:{OO00OOO0000O0O000}')#line:286
                            return True #line:287
                        if O0OO00O0O00O0OO00 ['status']==500 :#line:288
                            OO0OO00O000OO00OO =O0OO00O0O00O0OO00 ['message']#line:289
                            print (f'【获取种子】:{OO0OO00O000OO00OO}')#line:290
                            return False #line:291
    def synthetic (OO0O0OO0OO00O0O0O ):#line:294
        global id ,g ,level #line:295
        try :#line:296
            while True :#line:297
                O00O00O0O000O0O0O =f'__{timi_new()}'#line:298
                O00O0OOOOO00O0O00 ={'authorization':OO0O0OO0OO00O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O000O0O0O ),'signstring':O00O00O0O000O0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:307
                OOO00O00OOOOOO00O =requests .request ('get',f'{host}/game/getAllData',headers =O00O0OOOOO00O0O00 ).json ()#line:308
                if 'status'in OOO00O00OOOOOO00O :#line:310
                    if OOO00O00OOOOOO00O ['status']==200 :#line:311
                        O0OOO0000O0O0000O =OOO00O00OOOOOO00O ['data']['cropList']#line:312
                        OO00OOOO00OO0000O =OOO00O00OOOOOO00O ['data']['gameCoreDataDBid']#line:313
                        OOOOO0O000OOO0000 =0 #line:314
                        for O000O0O00OOOOOO00 in O0OOO0000O0O0000O :#line:315
                            if not O000O0O00OOOOOO00 :#line:316
                                O00O00000O0O0OO00 =f'_crop_id={OO00OOOO00OO0000O}&site={OOOOO0O000OOO0000}_{OO0O0OO0OO00O0O0O.time}'#line:317
                                OO0OOOOO0OOOOOO00 ={'authorization':OO0O0OO0OO00O0O0O .token ,'timestamp':OO0O0OO0OO00O0O0O .time ,'sign':sign (O00O00000O0O0OO00 ),'signstring':O00O00000O0O0OO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:326
                                O0OOO00O0OO00OO00 ={"site":OOOOO0O000OOO0000 ,"crop_id":OO00OOOO00OO0000O }#line:327
                                O00000OOOO000OO00 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0OOOOO0OOOOOO00 ,data =O0OOO00O0OO00OO00 ).json ()#line:328
                                time .sleep (random .randint (1 ,3 )/10 )#line:330
                                if 'status'in O00000OOOO000OO00 :#line:331
                                    if O00000OOOO000OO00 ['status']==200 :#line:332
                                        if O00000OOOO000OO00 ['message']=='种子数量不足':#line:333
                                            level =OO0O0OO0OO00O0O0O .level_new ()#line:334
                                            print (f'【购买合成】:{O00000OOOO000OO00["message"]}')#line:335
                                            if not OO0O0OO0OO00O0O0O .user_ad ():#line:336
                                                return False #line:337
                                        print (f'【购买合成】:购买农作物,位置{OOOOO0O000OOO0000}')#line:338
                                    if O00000OOOO000OO00 ['status']==500 :#line:339
                                        print (f'【购买合成】:{O00000OOOO000OO00["message"]}')#line:340
                                        return False #line:341
                            OOOOO0O000OOO0000 +=1 #line:342
                        O00000O0O0O0O00OO =requests .request ('get',f'{host}/game/getAllData',headers =O00O0OOOOO00O0O00 ).json ()#line:343
                        OOO000OOO0OOOOO00 =O00000O0O0O0O00OO ['data']['cropList']#line:344
                        O0O0O0OOO00O0O00O =False #line:345
                        for O000O0O00OOOOOO00 in range (12 ):#line:346
                            id =OOO000OOO0OOOOO00 [O000O0O00OOOOOO00 ]['level']#line:347
                            if int (level )-int (id )>9 :#line:348
                                OOOOO00O0O00OO0OO =f'_site={O000O0O00OOOOOO00}_{timi_new()}'#line:349
                                OOOOOOOO0OO0OO00O ={'accept':'application/json, text/plain, */*','authorization':OO0O0OO0OO00O0O0O .token ,'timestamp':timi_new (),'sign':sign (OOOOO00O0O00OO0OO ),'signstring':OOOOO00O0O00OO0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:359
                                OO0000OOOO00OOO00 ={"site":O000O0O00OOOOOO00 }#line:360
                                O00O0OO00O000000O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOOOOOO0OO0OO00O ,data =OO0000OOOO00OOO00 ).json ()#line:361
                                if 'status'in O00O0OO00O000000O :#line:363
                                    if O00O0OO00O000000O ['status']==200 :#line:364
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:365
                            if id !=0 :#line:366
                                for OOOO0O000O0OO00OO in range (11 ):#line:367
                                    O00OOOOO0OO0OOOO0 =OOOO0O000O0OO00OO +1 #line:368
                                    g =OOO000OOO0OOOOO00 [O00OOOOO0OO0OOOO0 ]['level']#line:369
                                    if id ==g :#line:370
                                        OO00OOOOOOO000000 =OOOO0O000O0OO00OO +2 #line:371
                                        if OO00OOOOOOO000000 ==O000O0O00OOOOOO00 +1 :#line:372
                                            pass #line:373
                                        else :#line:374
                                            OO0OOOO000OO0OOO0 =O000O0O00OOOOOO00 +1 #line:375
                                            time .sleep (random .randint (1 ,3 )/10 )#line:377
                                            OOOO0OO0OO00O00OO =f'_site={OO0OOOO000OO0OOO0-1}&targetSite={OO00OOOOOOO000000-1}_{timi_new()}'#line:378
                                            O00O000OOO00000O0 ={'accept':'application/json, text/plain, */*','authorization':OO0O0OO0OO00O0O0O .token ,'timestamp':timi_new (),'sign':sign (OOOO0OO0OO00O00OO ),'signstring':OOOO0OO0OO00O00OO ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:393
                                            O0OO0000OOOOO0000 ={"site":int (OO0OOOO000OO0OOO0 -1 ),"targetSite":int (OO00OOOOOOO000000 -1 )}#line:394
                                            OO00O000O00000O00 =requests .request ('post',f'{host}/game/crops/move',headers =O00O000OOO00000O0 ,json =O0OO0000OOOOO0000 ).json ()#line:395
                                            if 'status'in OO00O000O00000O00 :#line:396
                                                if OO00O000O00000O00 ['status']==200 :#line:397
                                                    pass #line:398
                                            print ('【购买合成】:',OO0OOOO000OO0OOO0 ,OO00OOOOOOO000000 ,'合成成功')#line:400
                                            O0O0O0OOO00O0O00O =True #line:401
                                    if O0O0O0OOO00O0O00O :#line:402
                                        break #line:403
                                if O0O0O0OOO00O0O00O :#line:404
                                    break #line:405
        except Exception as O0OOOO0OO00O0O000 :#line:406
            OO0O0OO0OO00O0O0O .synthetic ()#line:407
    def level_new (OOO00O00O0OO000O0 ):#line:410
        try :#line:411
            OOO0O000O0OOO0OOO =f'__{timi_new()}'#line:412
            OOO00O0OOO0000O00 ={'authorization':OOO00O00O0OO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O0OOO0OOO ),'signstring':OOO0O000O0OOO0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:421
            O0OOO0OO00O000O0O =requests .request ('get',f'{host}/user',headers =OOO00O0OOO0000O00 ).json ()#line:422
            if 'status'in O0OOO0OO00O000O0O :#line:423
                if O0OOO0OO00O000O0O ['status']==200 :#line:424
                    return O0OOO0OO00O000O0O ['data']['level']#line:425
        except Exception as OOOOOO0O0000O00O0 :#line:426
            print (OOOOOO0O0000O00O0 )#line:427
    def propsraffle (O000O0O0OOO00OOO0 ):#line:431
        try :#line:432
            while True :#line:433
                OO0O000OOOO0OOOOO =f'__{timi_new()}'#line:434
                O00O0000O0OO0OO0O ={'authorization':O000O0O0OOO00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000OOOO0OOOOO ),'signstring':OO0O000OOOO0OOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:443
                OO0OO000O0O00O0O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00O0000O0OO0OO0O ).json ()#line:444
                if 'status'in OO0OO000O0O00O0O0 :#line:446
                    if OO0OO000O0O00O0O0 ['status']==200 :#line:447
                        O00O0OO00000OOOOO =OO0OO000O0O00O0O0 ['data']['rows']#line:448
                        O0O00O00OOOOOOOOO =OO0OO000O0O00O0O0 ['data']['vstate']#line:449
                        if O00O0OO00000OOOOO ==5 or O00O0OO00000OOOOO ==6 or O00O0OO00000OOOOO ==7 :#line:450
                            O000OOOOOOO00O0OO =OO0OO000O0O00O0O0 ['data']['silver']#line:451
                            print (f'【转盘抽奖】:获得种子:{O000OOOOOOO00O0OO}')#line:452
                        if O00O0OO00000OOOOO ==1 or O00O0OO00000OOOOO ==2 or O00O0OO00000OOOOO ==3 :#line:453
                            OO0OOOOOOO0O00OO0 =OO0OO000O0O00O0O0 ['data']['clover']#line:454
                            print (f'【转盘抽奖】:获得三叶草:{OO0OOOOOOO0O00OO0}')#line:455
                        if O00O0OO00000OOOOO ==4 or O00O0OO00000OOOOO ==8 :#line:456
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:457
                        if O00O0OO00000OOOOO =='抽奖次数已用完':#line:461
                            if O0O00O00OOOOOOOOO :#line:462
                                O0O000O00O0O00O0O =random .randint (160 ,190 )/10 #line:463
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{O0O000O00O0O00O0O}秒获取抽奖机会')#line:464
                                time .sleep (O0O000O00O0O00O0O )#line:465
                                O000OO0OOOOOO0OOO =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O00O0000O0OO0OO0O ).json ()#line:466
                                if 'status'in O000OO0OOOOOO0OOO :#line:468
                                    if O000OO0OOOOOO0OOO ['status']==200 :#line:469
                                        print (f'【转盘抽奖】:{O000OO0OOOOOO0OOO["message"]}')#line:470
                                    if O000OO0OOOOOO0OOO ['status']==500 :#line:471
                                        print (f'【转盘抽奖】:{O000OO0OOOOOO0OOO["message"]}')#line:472
                                        break #line:473
                                time .sleep (random .randint (10 ,15 )/10 )#line:474
                            else :#line:475
                                break #line:476
                time .sleep (random .randint (8 ,15 )/10 )#line:477
        except Exception as O0O0000OO000OO000 :#line:478
            print (O0O0000OO000OO000 )#line:479
    def friends_invitation (O0OOOOOOOO000O0OO ):#line:482
        try :#line:483
            O00O00OO000O0O000 =f'__{timi_new()}'#line:484
            OO00OO0OO0000O00O ={'authorization':O0OOOOOOOO000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO000O0O000 ),'signstring':O00O00OO000O0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:493
            O0OOOOO000O0000OO =requests .request ('get',f'{host}/friends',headers =OO00OO0OO0000O00O ).json ()#line:494
            if 'status'in O0OOOOO000O0000OO :#line:495
                if O0OOOOO000O0000OO ['status']==200 :#line:496
                    O00000OO0000O0O00 =O0OOOOO000O0000OO ['data']['myInviteter']#line:497
                    if O00000OO0000O0O00 :#line:498
                        O000OO000O0O00OO0 =O00000OO0000O0O00 ['user']['nickname']#line:499
                        O0OO0O000O00OOOO0 =O0OOOOOOOO000O0OO .certification ()#line:500
                        print (f'【绑邀请码】:我的邀请人:{O000OO000O0O00OO0}丨实名:{O0OO0O000O00OOOO0}')#line:501
                    else :#line:502
                        if O0OOOOOOOO000O0OO .innerId !='0':#line:503
                            O00O00OO000O0O000 =f'_innerId={O0OOOOOOOO000O0OO.innerId}_{timi_new()}'#line:504
                            OO00OO0OO0000O00O ={'authorization':O0OOOOOOOO000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO000O0O000 ),'signstring':O00O00OO000O0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
                            O0OOOO00OO0O0000O ={"innerId":O0OOOOOOOO000O0OO .innerId }#line:514
                            OO00OOOO0OO000O00 =requests .request ('post',f'{host}/friends/my-invitation',headers =OO00OO0OO0000O00O ,data =O0OOOO00OO0O0000O ).json ()#line:515
                            if 'status'in OO00OOOO0OO000O00 :#line:516
                                if OO00OOOO0OO000O00 ['status']==200 :#line:517
                                    print (f'【绑邀请码】:{O0OOOOOOOO000O0OO.innerId}{OO00OOOO0OO000O00["message"]}')#line:518
                        else :#line:519
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:520
        except Exception as O0000O00O0000O00O :#line:521
            print (O0000O00O0000O00O )#line:522
    def add_clover (OOOO00OO00OOOO0O0 ):#line:526
        try :#line:527
            OO0OO000O0OOO0O0O =f'__{timi_new()}'#line:528
            O0OOOOO000O0OO00O ={'authorization':OOOO00OO00OOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000O0OOO0O0O ),'signstring':OO0OO000O0OOO0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:537
            OOO0O0OO00OO00O00 =requests .request ('get',f'{host}/assets/clovers',headers =O0OOOOO000O0OO00O ).json ()#line:538
            if 'status'in OOO0O0OO00OO00O00 :#line:540
                if OOO0O0OO00OO00O00 ['status']==200 :#line:541
                    O00OO00O0O0OOO000 =OOO0O0OO00OO00O00 ['data']['clover']#line:542
                    OO00O00OOO0O00O00 =OOO0O0OO00OO00O00 ['data']['used_clover']#line:543
                    OOOO00O0O0O0OOOO0 =float (O00OO00O0O0OOO000 )-float (OO00O00OOO0O00O00 )#line:544
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OO00O00OOO0O00O00}')#line:545
                    if OOOO00O0O0O0OOOO0 >1 :#line:546
                        OO0OO000O0OOO0O0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOO00O0O0O0OOOO0)}_{timi_new()}'#line:547
                        O0OOOOO000O0OO00O ={'authorization':OOOO00OO00OOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000O0OOO0O0O ),'signstring':OO0OO000O0OOO0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:556
                        O0000O0OOOOOOOO0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOO00O0O0O0OOOO0 )}#line:557
                        O0OO00OO0000O0000 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OOOOO000O0OO00O ,data =O0000O0OOOOOOOO0O ).json ()#line:558
                        if 'status'in O0OO00OO0000O0000 :#line:560
                            if O0OO00OO0000O0000 ['status']==200 :#line:561
                                print (f'【参与抽奖】:添加三叶草:{O0OO00OO0000O0000["data"]}丨数量:{OOOO00O0O0O0OOOO0}')#line:562
            OO0O0OOOOOOOO00OO =requests .request ('get',f'{host}/lottery',headers =O0OOOOO000O0OO00O ).json ()#line:563
            O00O000O000000O0O =OOOO00OO00OOOO0O0 .winning_rewards ()#line:565
            if 'status'in OO0O0OOOOOOOO00OO :#line:566
                if OO0O0OOOOOOOO00OO ['status']==200 :#line:567
                    O000OOOOO0O0000O0 =OO0O0OOOOOOOO00OO ['data'][0 ]['day_get_gold_quantity']#line:568
                    print (f'【参与抽奖】:预计每天中{O000OOOOO0O0000O0[:6]}种子丨好友收益:{O00O000O000000O0O}')#line:569
        except Exception as O00OOOOOOOOO00000 :#line:570
            print (O00OOOOOOOOO00000 )#line:571
    def energy (OOOOO0O00O0OOO0OO ):#line:574
        OOO00O0OO00O00OOO =f'__{timi_new()}'#line:575
        OO0OO00O0OO00OO0O ={'authorization':OOOOO0O00O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OO00O00OOO ),'signstring':OOO00O0OO00O00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:584
        OOOO00OOOOOO0O00O =requests .request ('get',f'{host}/energy/general',headers =OO0OO00O0OO00OO0O ).json ()#line:585
        if 'status'in OOOO00OOOOOO0O00O :#line:587
            if OOOO00OOOOOO0O00O ['status']==200 :#line:588
                O0OO000OOO00O0000 =OOOO00OOOOOO0O00O ['data']['ordinary_water_consumptions']#line:589
                if float (O0OO000OOO00O0000 )<80 :#line:590
                    OOO00OOO000OOOOOO =99 -float (O0OO000OOO00O0000 )#line:591
                    OOO0O0OO0O00O0O00 ={"fertilizer":str (OOO00OOO000OOOOOO ).split ('.')[0 ]}#line:592
                    OO0O0O000OOOO0OO0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0OO00O0OO00OO0O ,data =OOO0O0OO0O00O0O00 ).json ()#line:593
                    if 'status'in OO0O0O000OOOO0OO0 :#line:595
                        if OO0O0O000OOOO0OO0 ['status']==200 :#line:596
                            print (f'【购买肥料】:{OO0O0O000OOOO0OO0["message"]}')#line:597
                OO0OOOOOOO0000OOO =OOOO00OOOOOO0O00O ['data']['ordinary_water_consumptions']#line:598
                if float (OO0OOOOOOO0000OOO )<800 :#line:599
                    O00000OOO00OOO000 =999 -float (OO0OOOOOOO0000OOO )#line:600
                    OOO0O00O00OO00OO0 ={"water":str (O00000OOO00OOO000 ).split ('.')[0 ]}#line:601
                    OO00O000OOO0O00OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0OO00O0OO00OO0O ,data =OOO0O00O00OO00OO0 ).json ()#line:602
                    if 'status'in OO00O000OOO0O00OO :#line:603
                        if OO00O000OOO0O00OO ['status']==200 :#line:604
                            print (f'【购买水滴】:{OO00O000OOO0O00OO["message"]}')#line:605
def version_of_the_validation ():#line:611
    return str ((65 -56 )/10 )#line:612
def gitee_validation ():#line:614
    try :#line:615
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:616
    except Exception as O0OOOO0O0O00OO000 :#line:617
        sys .exit (0 )#line:618
def update_the_validation ():#line:624
    try :#line:625
        OOOOOO000O000000O =gitee_validation ()#line:626
        if version_of_the_validation ()<OOOOOO000O000000O ['CityEarth']['edition']:#line:627
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOOO000O000000O["CityEarth"]["edition"]}   ❌')#line:628
            print (f'更新内容=>>{OOOOOO000O000000O["CityEarth"]["content"]}   👍')#line:629
        else :#line:630
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOOO000O000000O["CityEarth"]["edition"]}   ✅')#line:631
            print (f'更新内容=>> {OOOOOO000O000000O["CityEarth"]["content"]}   👍')#line:632
    except Exception as OO0O0OOO0OO0O000O :#line:633
        print (OO0O0OOO0OO0O000O )#line:634
def os_qinglong ():#line:637
    if application in os .environ :#line:638
        OO0O0O00000OOO000 =os .environ [application ].split ('\n')#line:639
        if len (OO0O0O00000OOO000 )>0 :#line:640
            return OO0O0O00000OOO000 #line:641
        else :#line:642
            print (f"{application}变量未启用")#line:643
            print ('脚本退出')#line:644
            sys .exit (1 )#line:645
    else :#line:646
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:647
        return os_built ()#line:648
def os_built ():#line:651
    if token :#line:652
        OOO00OO0O0O0OOOO0 =token .split ('\n')#line:653
        if len (OOO00OO0O0O0OOOO0 )>0 :#line:654
            return OOO00OO0O0O0OOOO0 #line:655
    else :#line:656
        print (f"内置变量为空")#line:657
        print ('脚本结束')#line:658
        sys .exit (0 )#line:659
if __name__ =='__main__':#line:662
    start ()#line:663
