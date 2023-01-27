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
        O0OO00OO00000000O =os_qinglong ()#line:7
        print (f"==========共找到{len(O0OO00OO00000000O)}个账号==========")#line:8
        for OOO0OOO000O0O0O0O in O0OO00OO00000000O :#line:9
            print (f"------------正在执行第{O0OO00OO00000000O.index(OOO0OOO000O0O0O0O) + 1}个账号------------")#line:10
            O0O00O0OOOO000OOO =CityEarth (OOO0OOO000O0O0O0O )#line:11
            if O0O00O0OOOO000OOO .base_info ():#line:13
                O0O00O0OOOO000OOO .game_map ()#line:17
                O0O00O0OOOO000OOO .friends_invitation ()#line:19
                O0O00O0OOOO000OOO .add_clover ()#line:21
                O0O00O0OOOO000OOO .energy ()#line:23
                O0O00O0OOOO000OOO .synthetic ()#line:25
                O0O00O0OOOO000OOO .propsraffle ()#line:27
                O0O00O0OOOO000OOO .crops_illustrated ()#line:29
                O0O00O0OOOO000OOO .give_gold ()#line:31
            else :#line:32
                print ('token失效')#line:33
            time .sleep (time_xx )#line:35
    except Exception as O0O0O0O000O0OO0OO :#line:36
        print (O0O0O0O000O0OO0OO )#line:37
def sign (O0OO00O0OOO00OOOO ):#line:39
    O0OOOOOOO0O00O0O0 =hashlib .md5 (O0OO00O0OOO00OOOO .encode ()).hexdigest ()#line:40
    O0O00O0OOO0OOO0OO ="scsc%^&*"+O0OOOOOOO0O00O0O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:41
    OOOO0O0OOOO0O0OOO =hashlib .md5 (O0O00O0OOO0OOO0OO .encode ()).hexdigest ()#line:42
    return OOOO0O0OOOO0O0OOO #line:43
def timi_new ():#line:45
    return str (int (time .time ()*1000 ))#line:46
class CityEarth :#line:49
    def __init__ (OOO00OO0OO0OOOO0O ,O0OOO0O0OO0O0OOOO ):#line:51
        try :#line:52
            OOO00OO0OO0OOOO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:53
            OOO00OO0OO0OOOO0O .token =O0OOO0O0OO0O0OOOO .split ('&')[0 ]#line:54
            OOO00OO0OO0OOOO0O .innerId =O0OOO0O0OO0O0OOOO .split ('&')[1 ]#line:55
            OOO00OO0OO0OOOO0O .doneeNo =O0OOO0O0OO0O0OOOO .split ('&')[2 ]#line:56
        except :#line:57
            print ('变量格式错误')#line:58
    def base_info (OO0O000OO0000O0O0 ):#line:61
        try :#line:62
            O00OOO0OOO0OO0O00 =f'__{timi_new()}'#line:63
            O00O0O0O00000OOOO ={'authorization':OO0O000OO0000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OOO0OO0O00 ),'signstring':O00OOO0OOO0OO0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:72
            OO0O000OO00OO0OO0 =requests .request ('get',f'{host}/user',headers =O00O0O0O00000OOOO ).json ()#line:73
            if 'status'in OO0O000OO00OO0OO0 :#line:75
                if OO0O000OO00OO0OO0 ['status']==200 :#line:76
                    OO00OO00O0O00OOO0 =OO0O000OO00OO0OO0 ['data']['nickname']#line:77
                    OOO0OO00O00O00OO0 =OO0O000OO00OO0OO0 ['data']['inner_id']#line:78
                    O0000O000O0O0000O =OO0O000OO00OO0OO0 ['data']['assets']['gold']#line:79
                    O0O00OO00000000O0 =OO0O000OO00OO0OO0 ['data']['level']#line:80
                    print (f'【账号信息】:昵称:{OO00OO00O0O00OOO0}丨ID:{str(OOO0OO00O00O00OO0)[:3] + "**"+ str(OOO0OO00O00O00OO0)[5:]}丨等级:{O0O00OO00000000O0}丨种子:{str(O0000O000O0O0000O).split(".")[0]}')#line:81
                if OO0O000OO00OO0OO0 ['status']==401 :#line:82
                    return False #line:83
                if OO0O000OO00OO0OO0 ['status']==500 :#line:84
                    return False #line:85
            return True #line:86
        except Exception as OO000O0OO0OOO00OO :#line:87
            print (OO000O0OO0OOO00OO )#line:88
    def game_map (O00O00O0OO0O00OOO ):#line:91
        O000000OOOO0OO0OO =f'__{timi_new()}'#line:92
        OOO00O0OO0O000O00 ={'authorization':O00O00O0OO0O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000000OOOO0OO0OO ),'signstring':O000000OOOO0OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:101
        OO0OOO000O0OO00O0 =requests .request ('get',f'{host}/game/map',headers =OOO00O0OO0O000O00 ).json ()#line:102
        if 'status'in OO0OOO000O0OO00O0 :#line:104
            if OO0OOO000O0OO00O0 ['status']==200 :#line:105
                for O0OOO00O00OO0O000 in OO0OOO000O0OO00O0 ['data']['list'][0 ]['crops']:#line:106
                    O0O0OOOO00O000O0O =O0OOO00O00OO0O000 ['level']#line:108
                    if O0O0OOOO00O000O0O ==41 :#line:109
                        OOOO000OOO000O000 =O0OOO00O00OO0O000 ['crop_name']#line:110
                        O0O0O0OO0O00OOOO0 =O0OOO00O00OO0O000 ['count']#line:111
                        if O0O0O0OO0O00OOOO0 >0 :#line:112
                            print (f'【农业资产】:{OOOO000OOO000O000}丨数量:{O0O0O0OO0O00OOOO0}')#line:113
    def give_gold (O0O0000OO00OO0000 ):#line:118
        OO000O00OOOOOOO00 =f'__{timi_new()}'#line:119
        O0O0OOOOO0OO0OO0O ={'authorization':O0O0000OO00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00OOOOOOO00 ),'signstring':OO000O00OOOOOOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:128
        O0OO0O0OOOOOO00OO =requests .request ('get',f'{host}/user',headers =O0O0OOOOO0OO0OO0O ).json ()#line:129
        if 'status'in O0OO0O0OOOOOO00OO :#line:130
            if O0OO0O0OOOOOO00OO ['status']==200 :#line:131
                if float (O0O0000OO00OO0000 .doneeNo )!=0 :#line:132
                    OO0OO000000OO000O =O0OO0O0OOOOOO00OO ['data']['assets']['gold']#line:133
                    if float (OO0OO000000OO000O )>2 :#line:134
                        O0O0OOO0O0000OOOO =int (float (OO0OO000000OO000O )/1.1 )#line:135
                        OO000O00OOOOOOO00 =f'_doneeNo={O0O0000OO00OO0000.doneeNo}&quantity={O0O0OOO0O0000OOOO}_{timi_new()}'#line:136
                        O0O0OOOOO0OO0OO0O ={'authorization':O0O0000OO00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00OOOOOOO00 ),'signstring':OO000O00OOOOOOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:145
                        OOOOO000OOO0O0OOO ={"quantity":O0O0OOO0O0000OOOO ,"doneeNo":O0O0000OO00OO0000 .doneeNo }#line:149
                        O0OOO0000000OO0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0OOOOO0OO0OO0O ,data =OOOOO000OOO0O0OOO ).json ()#line:150
                        if 'status'in O0OOO0000000OO0O0 :#line:152
                            if O0OOO0000000OO0O0 ['status']==200 :#line:153
                                if O0OOO0000000OO0O0 ['data']:#line:154
                                    print (f'【赠送种子】:赠送{O0O0OOO0O0000OOOO}种子给{O0O0000OO00OO0000.doneeNo}成功')#line:155
                else :#line:156
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:157
    def winning_rewards (OO00O0OOOOO0O000O ):#line:159
        O0O00OO0OO0OOOO00 =f'__{timi_new()}'#line:160
        O00OOOOO00O00O000 ={'authorization':OO00O0OOOOO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0OO0OOOO00 ),'signstring':O0O00OO0OO0OOOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
        OO000OO0O0OOO000O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00OOOOO00O00O000 ).json ()#line:170
        if 'status'in OO000OO0O0OOO000O :#line:172
            if OO000OO0O0OOO000O ['status']==200 :#line:173
                if OO000OO0O0OOO000O ['data']['amount']:#line:174
                    O00O0O0O0O0O00OOO =OO000OO0O0OOO000O ['data']['amount']['gold']#line:175
                    return O00O0O0O0O0O00OOO #line:176
                else :#line:177
                    return 0 #line:178
    def certification (O00000OO000OOOO00 ):#line:180
        O0O0O000OO0O0OOOO =f'__{timi_new()}'#line:181
        OO00O00OO0000OO00 ={'authorization':O00000OO000OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000OO0O0OOOO ),'signstring':O0O0O000OO0O0OOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:190
        OOO0OO0O00O0OOO0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO00O00OO0000OO00 ).json ()#line:191
        if 'status'in OOO0OO0O00O0OOO0O :#line:193
            if OOO0OO0O00O0OOO0O ['status']==200 :#line:194
                if OOO0OO0O00O0OOO0O ['data']['result']:#line:195
                    OOOO00O0O0O000O00 =OOO0OO0O00O0OOO0O ['data']['nick_name']#line:196
                    return OOOO00O0O0O000O00 #line:197
                else :#line:198
                    return '未实名'#line:199
    def crops_illustrated (O000O00O0O0OO0O00 ):#line:202
        O00O00000OOOOO000 =f'__{timi_new()}'#line:203
        OO0O0000O00OOO00O ={'authorization':O000O00O0O0OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00000OOOOO000 ),'signstring':O00O00000OOOOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:212
        OOO00O0OOOOO0OO00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O0000O00OOO00O ).json ()#line:213
        if 'status'in OOO00O0OOOOO0OO00 :#line:215
            if OOO00O0OOOOO0OO00 ['status']==200 :#line:216
                O000O0O0OOO00O0O0 =OOO00O0OOOOO0OO00 ['data'][0 ]['crops']#line:217
                for O0O00OO0000O0OO0O in O000O0O0OOO00O0O0 :#line:218
                    if O0O00OO0000O0OO0O ['ill_clover_award']:#line:219
                        if float (O0O00OO0000O0OO0O ['ill_clover_award'])>1 :#line:220
                            if O0O00OO0000O0OO0O ['is_finish']:#line:221
                                if not O0O00OO0000O0OO0O ['is_getit']:#line:222
                                    O00O00000OOOOO000 =f'_award_level={O0O00OO0000O0OO0O["level"]}_{timi_new()}'#line:223
                                    OO0O0000O00OOO00O ={'authorization':O000O00O0O0OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00000OOOOO000 ),'signstring':O00O00000OOOOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:232
                                    O0O00O0O0000OO0OO ={"award_level":O0O00OO0000O0OO0O ['level']}#line:233
                                    OO0OO0OO00O00O00O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O0000O00OOO00O ,json =O0O00O0O0000OO0OO ).json ()#line:234
                                    if 'status'in OO0OO0OO00O00O00O :#line:235
                                        if OO0OO0OO00O00O00O ['status']==200 :#line:236
                                            OOOOOO00OOOOOO00O =OO0OO0OO00O00O00O ['data']['ill_clover_award']#line:237
                                            print (f'【图鉴奖励】:领取{O0O00OO0000O0OO0O["crop_name"]}成就丨奖励{OOOOOO00OOOOOO00O}叶子成功')#line:238
                                        if OO0OO0OO00O00O00O ['status']==500 :#line:239
                                            print (f'【图鉴奖励】:{OO0OO0OO00O00O00O["message"]}')#line:240
    def watched_ad (O0OOO00O0O0OOO0O0 ):#line:243
        OOOO0O0OOO0O00OO0 =f'__{timi_new()}'#line:244
        OOOOO00O00OO00OO0 ={'authorization':O0OOO00O0O0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0OOO0O00OO0 ),'signstring':OOOO0O0OOO0O00OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:253
        O00000O00O0O0O00O =requests .request ('post',f'{host}/game/watched-ad',headers =OOOOO00O00OO00OO0 ).json ()#line:254
        print (O00000O00O0O0O00O )#line:255
    def user_ad (OOOO0OOOO0OOO0OOO ):#line:260
        O00OO000OOO000OO0 =f'__{timi_new()}'#line:261
        O00O000O000O000O0 ={'authorization':OOOO0OOOO0OOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000OOO000OO0 ),'signstring':O00OO000OOO000OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:270
        OOOOOOOOOOOO0O0OO =requests .request ('get',f'{host}/user/ad',headers =O00O000O000O000O0 ).json ()#line:271
        if 'status'in OOOOOOOOOOOO0O0OO :#line:273
            if OOOOOOOOOOOO0O0OO ['status']==200 :#line:274
                O00OOO0O0OO0O0OOO =OOOOOOOOOOOO0O0OO ['data']['max_time']#line:275
                OO00O0OOO000OOO00 =OOOOOOOOOOOO0O0OO ['data']['watch_time']#line:276
                O0OOOOO0000O000OO =OOOOOOOOOOOO0O0OO ['data']['added_time']#line:277
                print (f'【获取种子】:获取种子剩余{O0OOOOO0000O000OO + O00OOO0O0OO0O0OOO - OO00O0OOO000OOO00}次丨好友提供:{O0OOOOO0000O000OO}次')#line:278
                if O0OOOOO0000O000OO +O00OOO0O0OO0O0OOO -OO00O0OOO000OOO00 >0 :#line:279
                    time .sleep (random .randint (16 ,19 ))#line:280
                    OO000OOOOO0O0OOO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00O000O000O000O0 ).json ()#line:281
                    if 'status'in OO000OOOOO0O0OOO0 :#line:283
                        if OO000OOOOO0O0OOO0 ['status']==200 :#line:284
                            O0O0O0OOO000O00OO =OO000OOOOO0O0OOO0 ['data']['silver']#line:285
                            print (f'【获取种子】:获得种子:{O0O0O0OOO000O00OO}')#line:286
                            return True #line:287
                        if OO000OOOOO0O0OOO0 ['status']==500 :#line:288
                            OOO00000O0OOOOO0O =OO000OOOOO0O0OOO0 ['message']#line:289
                            print (f'【获取种子】:{OOO00000O0OOOOO0O}')#line:290
                            return False #line:291
    def synthetic (O00000OO0OOOOOOO0 ):#line:294
        global id ,g ,level #line:295
        try :#line:296
            while True :#line:297
                OOOOO0O0O000OO00O =f'__{timi_new()}'#line:298
                O00OO00O000O0OO0O ={'authorization':O00000OO0OOOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O0O000OO00O ),'signstring':OOOOO0O0O000OO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:307
                OOO000OOO0O00O0O0 =requests .request ('get',f'{host}/game/getAllData',headers =O00OO00O000O0OO0O ).json ()#line:308
                if 'status'in OOO000OOO0O00O0O0 :#line:310
                    if OOO000OOO0O00O0O0 ['status']==200 :#line:311
                        O000OO0O0OOOOOOOO =OOO000OOO0O00O0O0 ['data']['cropList']#line:312
                        O00O0O0OOO0O00OOO =OOO000OOO0O00O0O0 ['data']['gameCoreDataDBid']#line:313
                        O0O0OO0000OO0OOO0 =0 #line:314
                        for O0000O00000OO0O00 in O000OO0O0OOOOOOOO :#line:315
                            if not O0000O00000OO0O00 :#line:316
                                OOOO00OO00O0OO0OO =f'_crop_id={O00O0O0OOO0O00OOO}&site={O0O0OO0000OO0OOO0}_{O00000OO0OOOOOOO0.time}'#line:317
                                O000000O0OO00OOO0 ={'authorization':O00000OO0OOOOOOO0 .token ,'timestamp':O00000OO0OOOOOOO0 .time ,'sign':sign (OOOO00OO00O0OO0OO ),'signstring':OOOO00OO00O0OO0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:326
                                OO00000O0OOO000OO ={"site":O0O0OO0000OO0OOO0 ,"crop_id":O00O0O0OOO0O00OOO }#line:327
                                O0OOOOO0OOOOO0000 =requests .request ('post',f'{host}/game/crops/buy',headers =O000000O0OO00OOO0 ,data =OO00000O0OOO000OO ).json ()#line:328
                                time .sleep (random .randint (1 ,3 )/10 )#line:330
                                if 'status'in O0OOOOO0OOOOO0000 :#line:331
                                    if O0OOOOO0OOOOO0000 ['status']==200 :#line:332
                                        if O0OOOOO0OOOOO0000 ['message']=='种子数量不足':#line:333
                                            level =O00000OO0OOOOOOO0 .level_new ()#line:334
                                            print (f'【购买合成】:{O0OOOOO0OOOOO0000["message"]}')#line:335
                                            if not O00000OO0OOOOOOO0 .user_ad ():#line:336
                                                return False #line:337
                                        print (f'【购买合成】:购买农作物,位置{O0O0OO0000OO0OOO0}')#line:338
                                    if O0OOOOO0OOOOO0000 ['status']==500 :#line:339
                                        print (f'【购买合成】:{O0OOOOO0OOOOO0000["message"]}')#line:340
                                        return False #line:341
                            O0O0OO0000OO0OOO0 +=1 #line:342
                        OO00OOO00OOO000O0 =requests .request ('get',f'{host}/game/getAllData',headers =O00OO00O000O0OO0O ).json ()#line:343
                        O000000OO0000O000 =OO00OOO00OOO000O0 ['data']['cropList']#line:344
                        O0O00OO00OO0OOO0O =False #line:345
                        for O0000O00000OO0O00 in range (12 ):#line:346
                            id =O000000OO0000O000 [O0000O00000OO0O00 ]['level']#line:347
                            if float (level )-float (id )>9 :#line:348
                                OO0O0OO000O0OO000 =f'_site={O0000O00000OO0O00}_{timi_new()}'#line:349
                                O00O000O0000OO00O ={'accept':'application/json, text/plain, */*','authorization':O00000OO0OOOOOOO0 .token ,'timestamp':timi_new (),'sign':sign (OO0O0OO000O0OO000 ),'signstring':OO0O0OO000O0OO000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:359
                                OO0O0O000O000000O ={"site":O0000O00000OO0O00 }#line:360
                                OOO000OOOO000OO00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00O000O0000OO00O ,data =OO0O0O000O000000O ).json ()#line:361
                                if 'status'in OOO000OOOO000OO00 :#line:363
                                    if OOO000OOOO000OO00 ['status']==200 :#line:364
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:365
                            if id !=0 :#line:366
                                for O0O00000OOOO00O00 in range (11 ):#line:367
                                    O0OO000O0O0O00O0O =O0O00000OOOO00O00 +1 #line:368
                                    g =O000000OO0000O000 [O0OO000O0O0O00O0O ]['level']#line:369
                                    if id ==g :#line:370
                                        OOOO0OO00OO0O0000 =O0O00000OOOO00O00 +2 #line:371
                                        if OOOO0OO00OO0O0000 ==O0000O00000OO0O00 +1 :#line:372
                                            pass #line:373
                                        else :#line:374
                                            OOO0O0O0O0OO00000 =O0000O00000OO0O00 +1 #line:375
                                            time .sleep (random .randint (1 ,3 )/10 )#line:377
                                            O00O00O0O0O00O0OO =f'_site={OOO0O0O0O0OO00000-1}&targetSite={OOOO0OO00OO0O0000-1}_{timi_new()}'#line:378
                                            OOO00OO0OOO000000 ={'accept':'application/json, text/plain, */*','authorization':O00000OO0OOOOOOO0 .token ,'timestamp':timi_new (),'sign':sign (O00O00O0O0O00O0OO ),'signstring':O00O00O0O0O00O0OO ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:393
                                            OOO00O0OOO000O000 ={"site":int (OOO0O0O0O0OO00000 -1 ),"targetSite":int (OOOO0OO00OO0O0000 -1 )}#line:394
                                            O0OOO00000O0OO000 =requests .request ('post',f'{host}/game/crops/move',headers =OOO00OO0OOO000000 ,json =OOO00O0OOO000O000 ).json ()#line:395
                                            if 'status'in O0OOO00000O0OO000 :#line:396
                                                if O0OOO00000O0OO000 ['status']==200 :#line:397
                                                    pass #line:398
                                            print ('【购买合成】:',OOO0O0O0O0OO00000 ,OOOO0OO00OO0O0000 ,'合成成功')#line:400
                                            O0O00OO00OO0OOO0O =True #line:401
                                    if O0O00OO00OO0OOO0O :#line:402
                                        break #line:403
                                if O0O00OO00OO0OOO0O :#line:404
                                    break #line:405
        except Exception as O0OOOOO00OOO0O0O0 :#line:406
            O00000OO0OOOOOOO0 .synthetic ()#line:407
    def level_new (OO0O0O0O0OOOO0OO0 ):#line:410
        try :#line:411
            OO0O0O0O00OOO00O0 =f'__{timi_new()}'#line:412
            O0000OO0O0OO0OO00 ={'authorization':OO0O0O0O0OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0O00OOO00O0 ),'signstring':OO0O0O0O00OOO00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:421
            O000OO000OOO000OO =requests .request ('get',f'{host}/user',headers =O0000OO0O0OO0OO00 ).json ()#line:422
            if 'status'in O000OO000OOO000OO :#line:423
                if O000OO000OOO000OO ['status']==200 :#line:424
                    return float (O000OO000OOO000OO ['data']['level'])#line:425
        except Exception as OOO0O0OO00OO000OO :#line:426
            print (OOO0O0OO00OO000OO )#line:427
    def propsraffle (OO00000000OO000OO ):#line:431
        try :#line:432
            while True :#line:433
                OO000OO00O00OO00O =f'__{timi_new()}'#line:434
                OO00000O00OO00000 ={'authorization':OO00000000OO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO00O00OO00O ),'signstring':OO000OO00O00OO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:443
                O00O0000O0O00O0O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO00000O00OO00000 ).json ()#line:444
                if 'status'in O00O0000O0O00O0O0 :#line:446
                    if O00O0000O0O00O0O0 ['status']==200 :#line:447
                        OO0000OO0OO0OO0OO =O00O0000O0O00O0O0 ['data']['rows']#line:448
                        OOO00OOO00O0O0OO0 =O00O0000O0O00O0O0 ['data']['vstate']#line:449
                        if OO0000OO0OO0OO0OO ==5 or OO0000OO0OO0OO0OO ==6 or OO0000OO0OO0OO0OO ==7 :#line:450
                            OO0O0OOOOO0000O0O =O00O0000O0O00O0O0 ['data']['silver']#line:451
                            print (f'【转盘抽奖】:获得种子:{OO0O0OOOOO0000O0O}')#line:452
                        if OO0000OO0OO0OO0OO ==1 or OO0000OO0OO0OO0OO ==2 or OO0000OO0OO0OO0OO ==3 :#line:453
                            OO0OO000O0O0OO000 =O00O0000O0O00O0O0 ['data']['clover']#line:454
                            print (f'【转盘抽奖】:获得三叶草:{OO0OO000O0O0OO000}')#line:455
                        if OO0000OO0OO0OO0OO ==4 or OO0000OO0OO0OO0OO ==8 :#line:456
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:457
                        if OO0000OO0OO0OO0OO =='抽奖次数已用完':#line:461
                            if OOO00OOO00O0O0OO0 :#line:462
                                OO000OOOO0OO00OOO =random .randint (160 ,190 )/10 #line:463
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{OO000OOOO0OO00OOO}秒获取抽奖机会')#line:464
                                time .sleep (OO000OOOO0OO00OOO )#line:465
                                OOOOOOOO0OOOO0O0O =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OO00000O00OO00000 ).json ()#line:466
                                if 'status'in OOOOOOOO0OOOO0O0O :#line:468
                                    if OOOOOOOO0OOOO0O0O ['status']==200 :#line:469
                                        print (f'【转盘抽奖】:{OOOOOOOO0OOOO0O0O["message"]}')#line:470
                                    if OOOOOOOO0OOOO0O0O ['status']==500 :#line:471
                                        print (f'【转盘抽奖】:{OOOOOOOO0OOOO0O0O["message"]}')#line:472
                                        break #line:473
                                time .sleep (random .randint (10 ,15 )/10 )#line:474
                            else :#line:475
                                break #line:476
                time .sleep (random .randint (8 ,15 )/10 )#line:477
        except Exception as O0OOO00O0O000OO0O :#line:478
            print (O0OOO00O0O000OO0O )#line:479
    def friends_invitation (OO00000OO00OOOOOO ):#line:482
        try :#line:483
            OOO00O0OOOO0OOO0O =f'__{timi_new()}'#line:484
            OO000000O0OOO0OO0 ={'authorization':OO00000OO00OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OOOO0OOO0O ),'signstring':OOO00O0OOOO0OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:493
            O00000O0OO000OOOO =requests .request ('get',f'{host}/friends',headers =OO000000O0OOO0OO0 ).json ()#line:494
            if 'status'in O00000O0OO000OOOO :#line:495
                if O00000O0OO000OOOO ['status']==200 :#line:496
                    O000OO00O0OOOOOOO =O00000O0OO000OOOO ['data']['myInviteter']#line:497
                    if O000OO00O0OOOOOOO :#line:498
                        OOOO0OO00OO0OO0O0 =O000OO00O0OOOOOOO ['user']['nickname']#line:499
                        O0O0O0O00O0O000O0 =OO00000OO00OOOOOO .certification ()#line:500
                        print (f'【绑邀请码】:我的邀请人:{OOOO0OO00OO0OO0O0}丨实名:{O0O0O0O00O0O000O0}')#line:501
                    else :#line:502
                        if OO00000OO00OOOOOO .innerId !='0':#line:503
                            OOO00O0OOOO0OOO0O =f'_innerId={OO00000OO00OOOOOO.innerId}_{timi_new()}'#line:504
                            OO000000O0OOO0OO0 ={'authorization':OO00000OO00OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OOOO0OOO0O ),'signstring':OOO00O0OOOO0OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
                            OO0OOOO0OOOO00OOO ={"innerId":OO00000OO00OOOOOO .innerId }#line:514
                            OO0OOO0OOOO0OO00O =requests .request ('post',f'{host}/friends/my-invitation',headers =OO000000O0OOO0OO0 ,data =OO0OOOO0OOOO00OOO ).json ()#line:515
                            if 'status'in OO0OOO0OOOO0OO00O :#line:516
                                if OO0OOO0OOOO0OO00O ['status']==200 :#line:517
                                    print (f'【绑邀请码】:{OO00000OO00OOOOOO.innerId}{OO0OOO0OOOO0OO00O["message"]}')#line:518
                        else :#line:519
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:520
        except Exception as O0O0O0OO0OOOO00O0 :#line:521
            print (O0O0O0OO0OOOO00O0 )#line:522
    def add_clover (OOOO0000000O00OOO ):#line:526
        try :#line:527
            OO0O00O00000OO0OO =f'__{timi_new()}'#line:528
            O000O0O0O0O00O00O ={'authorization':OOOO0000000O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O00000OO0OO ),'signstring':OO0O00O00000OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:537
            OOO00O00O00OO0000 =requests .request ('get',f'{host}/assets/clovers',headers =O000O0O0O0O00O00O ).json ()#line:538
            if 'status'in OOO00O00O00OO0000 :#line:540
                if OOO00O00O00OO0000 ['status']==200 :#line:541
                    O0OO00O000O00O000 =OOO00O00O00OO0000 ['data']['clover']#line:542
                    O00O0O0OOO000O00O =OOO00O00O00OO0000 ['data']['used_clover']#line:543
                    O000O00000OOO0OOO =float (O0OO00O000O00O000 )-float (O00O0O0OOO000O00O )#line:544
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O00O0O0OOO000O00O}')#line:545
                    if O000O00000OOO0OOO >1 :#line:546
                        OO0O00O00000OO0OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O000O00000OOO0OOO)}_{timi_new()}'#line:547
                        O000O0O0O0O00O00O ={'authorization':OOOO0000000O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O00000OO0OO ),'signstring':OO0O00O00000OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:556
                        OO000OO000O0O0OOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O000O00000OOO0OOO )}#line:557
                        OOOO0O00OOOO00O00 =requests .request ('post',f'{host}/lottery/add-stake',headers =O000O0O0O0O00O00O ,data =OO000OO000O0O0OOO ).json ()#line:558
                        if 'status'in OOOO0O00OOOO00O00 :#line:560
                            if OOOO0O00OOOO00O00 ['status']==200 :#line:561
                                print (f'【参与抽奖】:添加三叶草:{OOOO0O00OOOO00O00["data"]}丨数量:{O000O00000OOO0OOO}')#line:562
            O00O000O00OO0OO0O =requests .request ('get',f'{host}/lottery',headers =O000O0O0O0O00O00O ).json ()#line:563
            O0OOOOOOO00OOO0OO =OOOO0000000O00OOO .winning_rewards ()#line:565
            if 'status'in O00O000O00OO0OO0O :#line:566
                if O00O000O00OO0OO0O ['status']==200 :#line:567
                    OOO000O00OOOO0O0O =O00O000O00OO0OO0O ['data'][0 ]['day_get_gold_quantity']#line:568
                    print (f'【参与抽奖】:预计每天中{OOO000O00OOOO0O0O[:6]}种子丨好友收益:{O0OOOOOOO00OOO0OO}')#line:569
        except Exception as O0OOO00O0OO00OO0O :#line:570
            print (O0OOO00O0OO00OO0O )#line:571
    def energy (OO0OOO0O0000OO0OO ):#line:574
        O0OO0OOO00000O0OO =f'__{timi_new()}'#line:575
        OO0OO0OO00OOOOOO0 ={'authorization':OO0OOO0O0000OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO00000O0OO ),'signstring':O0OO0OOO00000O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:584
        O00O0OO000O000O0O =requests .request ('get',f'{host}/energy/general',headers =OO0OO0OO00OOOOOO0 ).json ()#line:585
        if 'status'in O00O0OO000O000O0O :#line:587
            if O00O0OO000O000O0O ['status']==200 :#line:588
                OO00OO00O000O00O0 =O00O0OO000O000O0O ['data']['ordinary_water_consumptions']#line:589
                if float (OO00OO00O000O00O0 )<80 :#line:590
                    O0OOOOOOOOOOOOO0O =99 -float (OO00OO00O000O00O0 )#line:591
                    O00O000000OO0O00O ={"fertilizer":str (O0OOOOOOOOOOOOO0O ).split ('.')[0 ]}#line:592
                    OOO0O0O00OOOOOO00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0OO0OO00OOOOOO0 ,data =O00O000000OO0O00O ).json ()#line:593
                    if 'status'in OOO0O0O00OOOOOO00 :#line:595
                        if OOO0O0O00OOOOOO00 ['status']==200 :#line:596
                            print (f'【购买肥料】:{OOO0O0O00OOOOOO00["message"]}')#line:597
                O000O00OO0OOOO0O0 =O00O0OO000O000O0O ['data']['ordinary_water_consumptions']#line:598
                if float (O000O00OO0OOOO0O0 )<800 :#line:599
                    O00OO0O00000OOOOO =999 -float (O000O00OO0OOOO0O0 )#line:600
                    OOOOOO0O00OO00OO0 ={"water":str (O00OO0O00000OOOOO ).split ('.')[0 ]}#line:601
                    OOO0OO00O00OO0OOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0OO0OO00OOOOOO0 ,data =OOOOOO0O00OO00OO0 ).json ()#line:602
                    if 'status'in OOO0OO00O00OO0OOO :#line:603
                        if OOO0OO00O00OO0OOO ['status']==200 :#line:604
                            print (f'【购买水滴】:{OOO0OO00O00OO0OOO["message"]}')#line:605
def version_of_the_validation ():#line:611
    return str ((65 -56 )/10 )#line:612
def gitee_validation ():#line:614
    try :#line:615
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:616
    except Exception as OO000O0OO00O0O0O0 :#line:617
        sys .exit (0 )#line:618
def update_the_validation ():#line:624
    try :#line:625
        O0OO000OO0O0OO0OO =gitee_validation ()#line:626
        if version_of_the_validation ()<O0OO000OO0O0OO0OO ['CityEarth']['edition']:#line:627
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO000OO0O0OO0OO["CityEarth"]["edition"]}   ❌')#line:628
            print (f'更新内容=>>{O0OO000OO0O0OO0OO["CityEarth"]["content"]}   👍')#line:629
        else :#line:630
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO000OO0O0OO0OO["CityEarth"]["edition"]}   ✅')#line:631
            print (f'更新内容=>> {O0OO000OO0O0OO0OO["CityEarth"]["content"]}   👍')#line:632
    except Exception as O00OOOOO0OO000O00 :#line:633
        print (O00OOOOO0OO000O00 )#line:634
def os_qinglong ():#line:637
    if application in os .environ :#line:638
        OO00O0O0O0OOOOOOO =os .environ [application ].split ('\n')#line:639
        if len (OO00O0O0O0OOOOOOO )>0 :#line:640
            return OO00O0O0O0OOOOOOO #line:641
        else :#line:642
            print (f"{application}变量未启用")#line:643
            print ('脚本退出')#line:644
            sys .exit (1 )#line:645
    else :#line:646
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:647
        return os_built ()#line:648
def os_built ():#line:651
    if token :#line:652
        OO0000000OOO0000O =token .split ('\n')#line:653
        if len (OO0000000OOO0000O )>0 :#line:654
            return OO0000000OOO0000O #line:655
    else :#line:656
        print (f"内置变量为空")#line:657
        print ('脚本结束')#line:658
        sys .exit (0 )#line:659
if __name__ =='__main__':#line:662
    start ()#line:663
