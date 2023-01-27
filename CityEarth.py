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
@ 版本  1.0
"""
application = 'ce_token'  # 变量名
token = ''

time_xx = random.randint(2, 4)          # 秒 执行下一个号的时间  2到4秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://scsc.sc19319.com'#line:2
def start ():#line:3
    try :#line:4
        update_the_validation ()#line:5
        O0OOOO0OOOO0O0OO0 =os_qinglong ()#line:6
        print (f"==========共找到{len(O0OOOO0OOOO0O0OO0)}个账号==========")#line:7
        for OOOO0O000O0000O00 in O0OOOO0OOOO0O0OO0 :#line:8
            print (f"------------正在执行第{O0OOOO0OOOO0O0OO0.index(OOOO0O000O0000O00) + 1}个账号------------")#line:9
            OOOOOOO000OO00OOO =CityEarth (OOOO0O000O0000O00 )#line:10
            if OOOOOOO000OO00OOO .base_info ():#line:12
                OOOOOOO000OO00OOO .game_map ()#line:16
                OOOOOOO000OO00OOO .friends_invitation ()#line:18
                OOOOOOO000OO00OOO .add_clover ()#line:20
                OOOOOOO000OO00OOO .energy ()#line:22
                OOOOOOO000OO00OOO .synthetic ()#line:24
                OOOOOOO000OO00OOO .propsraffle ()#line:26
                OOOOOOO000OO00OOO .crops_illustrated ()#line:28
                OOOOOOO000OO00OOO .give_gold ()#line:30
            else :#line:31
                print ('token失效')#line:32
            time .sleep (time_xx )#line:34
    except Exception as OOO000OOO00OOO00O :#line:35
        print (OOO000OOO00OOO00O )#line:36
def sign (OOOO00OO00OOO00OO ):#line:38
    OO00000OOOO00O00O =hashlib .md5 (OOOO00OO00OOO00OO .encode ()).hexdigest ()#line:39
    O000000000000O00O ="scsc%^&*"+OO00000OOOO00O00O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:40
    OOO000O0O00O00OOO =hashlib .md5 (O000000000000O00O .encode ()).hexdigest ()#line:41
    return OOO000O0O00O00OOO #line:42
def timi_new ():#line:44
    return str (int (time .time ()*1000 ))#line:45
class CityEarth :#line:48
    def __init__ (OO0OOO0O0O0O00O00 ,O00OOO0O0O000OO00 ):#line:50
        try :#line:51
            OO0OOO0O0O0O00O00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:52
            OO0OOO0O0O0O00O00 .token =O00OOO0O0O000OO00 .split ('&')[0 ]#line:53
            OO0OOO0O0O0O00O00 .innerId =O00OOO0O0O000OO00 .split ('&')[1 ]#line:54
            OO0OOO0O0O0O00O00 .doneeNo =O00OOO0O0O000OO00 .split ('&')[2 ]#line:55
        except :#line:56
            print ('变量格式错误')#line:57
    def base_info (O00000OO00O000O00 ):#line:60
        try :#line:61
            O0OOO0OO0OO0O000O =f'__{timi_new()}'#line:62
            OO00O00O0OO0O000O ={'authorization':O00000OO00O000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO0OO0O000O ),'signstring':O0OOO0OO0OO0O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:71
            OOO0O0OOO0O000OOO =requests .request ('get',f'{host}/user',headers =OO00O00O0OO0O000O ).json ()#line:72
            if 'status'in OOO0O0OOO0O000OOO :#line:74
                if OOO0O0OOO0O000OOO ['status']==200 :#line:75
                    OO00OOOOO00OOO00O =OOO0O0OOO0O000OOO ['data']['nickname']#line:76
                    O0OOO0OOO0O000OOO =OOO0O0OOO0O000OOO ['data']['inner_id']#line:77
                    O00O0O0O000O0OOOO =OOO0O0OOO0O000OOO ['data']['assets']['gold']#line:78
                    OOOO000O0OOOO00OO =OOO0O0OOO0O000OOO ['data']['level']#line:79
                    print (f'【账号信息】:昵称:{OO00OOOOO00OOO00O}丨ID:{str(O0OOO0OOO0O000OOO)[:3] + "**"+ str(O0OOO0OOO0O000OOO)[5:]}丨等级:{OOOO000O0OOOO00OO}丨种子:{str(O00O0O0O000O0OOOO).split(".")[0]}')#line:80
                if OOO0O0OOO0O000OOO ['status']==401 :#line:81
                    return False #line:82
                if OOO0O0OOO0O000OOO ['status']==500 :#line:83
                    return False #line:84
            return True #line:85
        except Exception as O0O0O000000O00OO0 :#line:86
            print (O0O0O000000O00OO0 )#line:87
    def game_map (OOO0O000OO0OOO000 ):#line:90
        OOOO0OOOO0OO0O0OO =f'__{timi_new()}'#line:91
        OO00O0OO0O0000OO0 ={'authorization':OOO0O000OO0OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOO0OO0O0OO ),'signstring':OOOO0OOOO0OO0O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:100
        O00OOOO0O00OOO0O0 =requests .request ('get',f'{host}/game/map',headers =OO00O0OO0O0000OO0 ).json ()#line:101
        if 'status'in O00OOOO0O00OOO0O0 :#line:103
            if O00OOOO0O00OOO0O0 ['status']==200 :#line:104
                for OOO0OO0OO00000O00 in O00OOOO0O00OOO0O0 ['data']['list'][0 ]['crops']:#line:105
                    O000O00O0OO0O00O0 =OOO0OO0OO00000O00 ['level']#line:107
                    if O000O00O0OO0O00O0 ==41 :#line:108
                        O0O0OOOO0O0OO0OO0 =OOO0OO0OO00000O00 ['crop_name']#line:109
                        OO00OOOOOO0OOOO00 =OOO0OO0OO00000O00 ['count']#line:110
                        if OO00OOOOOO0OOOO00 >0 :#line:111
                            print (f'【农业资产】:{O0O0OOOO0O0OO0OO0}丨数量:{OO00OOOOOO0OOOO00}')#line:112
    def give_gold (O00000O000OO0O000 ):#line:117
        OO0O0O0OO0OO00O00 =f'__{timi_new()}'#line:118
        OO00OO00O000O000O ={'authorization':O00000O000OO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OO0OO00O00 ),'signstring':OO0O0O0OO0OO00O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
        OOO000O0O0OO00O0O =requests .request ('get',f'{host}/user',headers =OO00OO00O000O000O ).json ()#line:128
        if 'status'in OOO000O0O0OO00O0O :#line:129
            if OOO000O0O0OO00O0O ['status']==200 :#line:130
                if float (O00000O000OO0O000 .doneeNo )!=0 :#line:131
                    O0O0OO0O0OO000O00 =OOO000O0O0OO00O0O ['data']['assets']['gold']#line:132
                    if float (O0O0OO0O0OO000O00 )>2 :#line:133
                        O000OO00OO00OOO00 =int (float (O0O0OO0O0OO000O00 )/1.1 )#line:134
                        OO0O0O0OO0OO00O00 =f'_doneeNo={O00000O000OO0O000.doneeNo}&quantity={O000OO00OO00OOO00}_{timi_new()}'#line:135
                        OO00OO00O000O000O ={'authorization':O00000O000OO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OO0OO00O00 ),'signstring':OO0O0O0OO0OO00O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:144
                        O0OOOOO00OOOOOO00 ={"quantity":O000OO00OO00OOO00 ,"doneeNo":O00000O000OO0O000 .doneeNo }#line:148
                        O0O0O0000OOO000OO =requests .request ('post',f'{host}/finance/give-gold',headers =OO00OO00O000O000O ,data =O0OOOOO00OOOOOO00 ).json ()#line:149
                        if 'status'in O0O0O0000OOO000OO :#line:151
                            if O0O0O0000OOO000OO ['status']==200 :#line:152
                                if O0O0O0000OOO000OO ['data']:#line:153
                                    print (f'【赠送种子】:赠送{O000OO00OO00OOO00}种子给{O00000O000OO0O000.doneeNo}成功')#line:154
                else :#line:155
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:156
    def winning_rewards (OOO000000OOO0OO00 ):#line:158
        OO0000OOO00OOOO00 =f'__{timi_new()}'#line:159
        OO0OOOO00OOO0OO00 ={'authorization':OOO000000OOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOO00OOOO00 ),'signstring':OO0000OOO00OOOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:168
        OOO0O00OOOO00OO0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO0OOOO00OOO0OO00 ).json ()#line:169
        if 'status'in OOO0O00OOOO00OO0O :#line:171
            if OOO0O00OOOO00OO0O ['status']==200 :#line:172
                if OOO0O00OOOO00OO0O ['data']['amount']:#line:173
                    OO00O0O0O0OOO0O0O =OOO0O00OOOO00OO0O ['data']['amount']['gold']#line:174
                    return OO00O0O0O0OOO0O0O #line:175
                else :#line:176
                    return 0 #line:177
    def certification (OOOO00O000O00OO00 ):#line:179
        O0O0O00O0OO0OOO0O =f'__{timi_new()}'#line:180
        O00OO0O000000OO00 ={'authorization':OOOO00O000O00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00O0OO0OOO0O ),'signstring':O0O0O00O0OO0OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:189
        OO00OOO0000O00O0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OO0O000000OO00 ).json ()#line:190
        if 'status'in OO00OOO0000O00O0O :#line:192
            if OO00OOO0000O00O0O ['status']==200 :#line:193
                if OO00OOO0000O00O0O ['data']['result']:#line:194
                    OO00O00O0O00O00OO =OO00OOO0000O00O0O ['data']['nick_name']#line:195
                    return OO00O00O0O00O00OO #line:196
                else :#line:197
                    return '未实名'#line:198
    def crops_illustrated (O0OO00000OOO0OO00 ):#line:201
        O0OOO0O00O0O00O00 =f'__{timi_new()}'#line:202
        OO0000OO0OO0O0OOO ={'authorization':O0OO00000OOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O00O0O00O00 ),'signstring':O0OOO0O00O0O00O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:211
        O0O0OOOO00O00OOOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0000OO0OO0O0OOO ).json ()#line:212
        if 'status'in O0O0OOOO00O00OOOO :#line:214
            if O0O0OOOO00O00OOOO ['status']==200 :#line:215
                O0OO000OOO0OO0OO0 =O0O0OOOO00O00OOOO ['data'][0 ]['crops']#line:216
                for O00OO0O0OO00OOOO0 in O0OO000OOO0OO0OO0 :#line:217
                    if O00OO0O0OO00OOOO0 ['ill_clover_award']:#line:218
                        if float (O00OO0O0OO00OOOO0 ['ill_clover_award'])>1 :#line:219
                            if O00OO0O0OO00OOOO0 ['is_finish']:#line:220
                                if not O00OO0O0OO00OOOO0 ['is_getit']:#line:221
                                    O0OOO0O00O0O00O00 =f'_award_level={O00OO0O0OO00OOOO0["level"]}_{timi_new()}'#line:222
                                    OO0000OO0OO0O0OOO ={'authorization':O0OO00000OOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O00O0O00O00 ),'signstring':O0OOO0O00O0O00O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:231
                                    OO0OO0O00OO0O0OOO ={"award_level":O00OO0O0OO00OOOO0 ['level']}#line:232
                                    O0OOOO0O0OOOOOOOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0000OO0OO0O0OOO ,json =OO0OO0O00OO0O0OOO ).json ()#line:233
                                    if 'status'in O0OOOO0O0OOOOOOOO :#line:234
                                        if O0OOOO0O0OOOOOOOO ['status']==200 :#line:235
                                            O000OO0O0OO0000OO =O0OOOO0O0OOOOOOOO ['data']['ill_clover_award']#line:236
                                            print (f'【图鉴奖励】:领取{O00OO0O0OO00OOOO0["crop_name"]}成就丨奖励{O000OO0O0OO0000OO}叶子成功')#line:237
                                        if O0OOOO0O0OOOOOOOO ['status']==500 :#line:238
                                            print (f'【图鉴奖励】:{O0OOOO0O0OOOOOOOO["message"]}')#line:239
    def watched_ad (OO00OO00OO0O0000O ):#line:242
        OO000O000000O000O =f'__{timi_new()}'#line:243
        OOO0O0OO00OOOO0OO ={'authorization':OO00OO00OO0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O000000O000O ),'signstring':OO000O000000O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
        O0O0O0O0OO0OOO0OO =requests .request ('post',f'{host}/game/watched-ad',headers =OOO0O0OO00OOOO0OO ).json ()#line:253
        print (O0O0O0O0OO0OOO0OO )#line:254
    def user_ad (OO0O00000O0OO0OOO ):#line:259
        OO0OOOO0O0O00O000 =f'__{timi_new()}'#line:260
        O0OO00OO0O0OOOOO0 ={'authorization':OO0O00000O0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0O0O00O000 ),'signstring':OO0OOOO0O0O00O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:269
        O000OOO000O000O00 =requests .request ('get',f'{host}/user/ad',headers =O0OO00OO0O0OOOOO0 ).json ()#line:270
        if 'status'in O000OOO000O000O00 :#line:272
            if O000OOO000O000O00 ['status']==200 :#line:273
                O000OO0OOO0O00O00 =O000OOO000O000O00 ['data']['max_time']#line:274
                OO0O0OO00O0OOOOOO =O000OOO000O000O00 ['data']['watch_time']#line:275
                O0OO000OOO0OOO00O =O000OOO000O000O00 ['data']['added_time']#line:276
                print (f'【获取种子】:获取种子剩余{O0OO000OOO0OOO00O + O000OO0OOO0O00O00 - OO0O0OO00O0OOOOOO}次丨好友提供:{O0OO000OOO0OOO00O}次')#line:277
                if O0OO000OOO0OOO00O +O000OO0OOO0O00O00 -OO0O0OO00O0OOOOOO >0 :#line:278
                    time .sleep (random .randint (16 ,19 ))#line:279
                    O0O00OOO0O0O00O0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OO00OO0O0OOOOO0 ).json ()#line:280
                    if 'status'in O0O00OOO0O0O00O0O :#line:282
                        if O0O00OOO0O0O00O0O ['status']==200 :#line:283
                            OOOOOOO0000O0OO00 =O0O00OOO0O0O00O0O ['data']['silver']#line:284
                            print (f'【获取种子】:获得种子:{OOOOOOO0000O0OO00}')#line:285
                            return True #line:286
                        if O0O00OOO0O0O00O0O ['status']==500 :#line:287
                            O0O00OOO0OO0O0O0O =O0O00OOO0O0O00O0O ['message']#line:288
                            print (f'【获取种子】:{O0O00OOO0OO0O0O0O}')#line:289
                            return False #line:290
    def synthetic (O0OO00000OO000OOO ):#line:293
        global id ,g #line:294
        try :#line:295
            OOOOOO000O0OOOOO0 =O0OO00000OO000OOO .level_new ()#line:296
            while True :#line:297
                OO0O00OOO00OO0000 =f'__{timi_new()}'#line:298
                O0O0O0O0O000O0O00 ={'authorization':O0OO00000OO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOO00OO0000 ),'signstring':OO0O00OOO00OO0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:307
                OOOOOOOOOOOOO00OO =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0O0O000O0O00 ).json ()#line:308
                if 'status'in OOOOOOOOOOOOO00OO :#line:310
                    if OOOOOOOOOOOOO00OO ['status']==200 :#line:311
                        OO0OO00O0O0OOO0OO =OOOOOOOOOOOOO00OO ['data']['cropList']#line:312
                        O00OO0OO0OO00O00O =OOOOOOOOOOOOO00OO ['data']['gameCoreDataDBid']#line:313
                        O0OOO0O00OO0OOOOO =0 #line:314
                        for OO0O0OOO00000OO00 in OO0OO00O0O0OOO0OO :#line:315
                            if not OO0O0OOO00000OO00 :#line:316
                                O00OOO00O00O00000 =f'_crop_id={O00OO0OO0OO00O00O}&site={O0OOO0O00OO0OOOOO}_{O0OO00000OO000OOO.time}'#line:317
                                OO0000O0OOOO0O0OO ={'authorization':O0OO00000OO000OOO .token ,'timestamp':O0OO00000OO000OOO .time ,'sign':sign (O00OOO00O00O00000 ),'signstring':O00OOO00O00O00000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:326
                                O00OO00000O0O0OO0 ={"site":O0OOO0O00OO0OOOOO ,"crop_id":O00OO0OO0OO00O00O }#line:327
                                O000O000O0OOOOO00 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0000O0OOOO0O0OO ,data =O00OO00000O0O0OO0 ).json ()#line:328
                                time .sleep (random .randint (1 ,3 )/10 )#line:330
                                if 'status'in O000O000O0OOOOO00 :#line:331
                                    if O000O000O0OOOOO00 ['status']==200 :#line:332
                                        if O000O000O0OOOOO00 ['message']=='种子数量不足':#line:333
                                            OOOOOO000O0OOOOO0 =O0OO00000OO000OOO .level_new ()#line:334
                                            print (f'【种植合成】:{O000O000O0OOOOO00["message"]}')#line:335
                                            if not O0OO00000OO000OOO .user_ad ():#line:336
                                                return False #line:337
                                        print (f'【种植合成】:种植农作物,位置{O0OOO0O00OO0OOOOO}')#line:338
                                    if O000O000O0OOOOO00 ['status']==500 :#line:339
                                        print (f'【种植合成】:{O000O000O0OOOOO00["message"]}')#line:340
                                        return False #line:341
                            O0OOO0O00OO0OOOOO +=1 #line:342
                        O000OOO00OOOOOO0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0O0O000O0O00 ).json ()#line:343
                        O000O0000OO000O00 =O000OOO00OOOOOO0O ['data']['cropList']#line:344
                        OO00O000O000OOO0O =False #line:345
                        for OO0O0OOO00000OO00 in range (12 ):#line:346
                            id =O000O0000OO000O00 [OO0O0OOO00000OO00 ]['level']#line:347
                            if float (OOOOOO000O0OOOOO0 )-float (id )>9 :#line:348
                                O000O000O00OOO0O0 =f'_site={OO0O0OOO00000OO00}_{timi_new()}'#line:349
                                O000O0OOOO0O0OO0O ={'accept':'application/json, text/plain, */*','authorization':O0OO00000OO000OOO .token ,'timestamp':timi_new (),'sign':sign (O000O000O00OOO0O0 ),'signstring':O000O000O00OOO0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:359
                                O0O0O00OO0OOO0O0O ={"site":OO0O0OOO00000OO00 }#line:360
                                O0000O000OOOOOO00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000O0OOOO0O0OO0O ,data =O0O0O00OO0OOO0O0O ).json ()#line:361
                                if 'status'in O0000O000OOOOOO00 :#line:362
                                    if O0000O000OOOOOO00 ['status']==200 :#line:363
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:364
                            if id !=0 :#line:365
                                for OOO0O0O00OOOO0OO0 in range (11 ):#line:366
                                    O00O00OO00O0OO0O0 =OOO0O0O00OOOO0OO0 +1 #line:367
                                    g =O000O0000OO000O00 [O00O00OO00O0OO0O0 ]['level']#line:368
                                    if id ==g :#line:369
                                        O0O00OOO00OOOO000 =OOO0O0O00OOOO0OO0 +2 #line:370
                                        if O0O00OOO00OOOO000 ==OO0O0OOO00000OO00 +1 :#line:371
                                            pass #line:372
                                        else :#line:373
                                            O00O00O00O00OOOOO =OO0O0OOO00000OO00 +1 #line:374
                                            time .sleep (random .randint (1 ,3 )/10 )#line:376
                                            O00OO00O000OO00O0 =f'_site={O00O00O00O00OOOOO-1}&targetSite={O0O00OOO00OOOO000-1}_{timi_new()}'#line:377
                                            O0OO0O000000O000O ={'accept':'application/json, text/plain, */*','authorization':O0OO00000OO000OOO .token ,'timestamp':timi_new (),'sign':sign (O00OO00O000OO00O0 ),'signstring':O00OO00O000OO00O0 ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:392
                                            O0000O000OOO0OO0O ={"site":int (O00O00O00O00OOOOO -1 ),"targetSite":int (O0O00OOO00OOOO000 -1 )}#line:393
                                            OOO0O0O00OOOO00OO =requests .request ('post',f'{host}/game/crops/move',headers =O0OO0O000000O000O ,json =O0000O000OOO0OO0O ).json ()#line:394
                                            if 'status'in OOO0O0O00OOOO00OO :#line:395
                                                if OOO0O0O00OOOO00OO ['status']==200 :#line:396
                                                    pass #line:397
                                            print ('【种植合成】:',O00O00O00O00OOOOO ,O0O00OOO00OOOO000 ,'合成成功')#line:399
                                            OO00O000O000OOO0O =True #line:400
                                    if OO00O000O000OOO0O :#line:401
                                        break #line:402
                                if OO00O000O000OOO0O :#line:403
                                    break #line:404
        except Exception as O0OOOOO0O0O0000OO :#line:405
            O0OO00000OO000OOO .synthetic ()#line:406
    def level_new (O0OOO0OO0OOO00O0O ):#line:409
        try :#line:410
            O0O00O000OOO00O00 =f'__{timi_new()}'#line:411
            OO00000000O00O0OO ={'authorization':O0OOO0OO0OOO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O000OOO00O00 ),'signstring':O0O00O000OOO00O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:420
            O0OO000000O00OOO0 =requests .request ('get',f'{host}/user',headers =OO00000000O00O0OO ).json ()#line:421
            if 'status'in O0OO000000O00OOO0 :#line:422
                if O0OO000000O00OOO0 ['status']==200 :#line:423
                    return float (O0OO000000O00OOO0 ['data']['level'])#line:424
        except Exception as O0000O0OOO000OO00 :#line:425
            print (O0000O0OOO000OO00 )#line:426
    def propsraffle (OOO0OO0O000OO00OO ):#line:430
        try :#line:431
            while True :#line:432
                OOOOOOO0000O00OOO =f'__{timi_new()}'#line:433
                O0O000OOOOO000000 ={'authorization':OOO0OO0O000OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0000O00OOO ),'signstring':OOOOOOO0000O00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:442
                O0OO0OOO0O0OO0OOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O000OOOOO000000 ).json ()#line:443
                if 'status'in O0OO0OOO0O0OO0OOO :#line:445
                    if O0OO0OOO0O0OO0OOO ['status']==200 :#line:446
                        OO00OO0O0O00OOO0O =O0OO0OOO0O0OO0OOO ['data']['rows']#line:447
                        OO00OO000O00O000O =O0OO0OOO0O0OO0OOO ['data']['vstate']#line:448
                        if OO00OO0O0O00OOO0O ==5 or OO00OO0O0O00OOO0O ==6 or OO00OO0O0O00OOO0O ==7 :#line:449
                            O0OO0O00O0000OOO0 =O0OO0OOO0O0OO0OOO ['data']['silver']#line:450
                            print (f'【转盘抽奖】:获得种子:{O0OO0O00O0000OOO0}')#line:451
                        if OO00OO0O0O00OOO0O ==1 or OO00OO0O0O00OOO0O ==2 or OO00OO0O0O00OOO0O ==3 :#line:452
                            O0O000000O00O0000 =O0OO0OOO0O0OO0OOO ['data']['clover']#line:453
                            print (f'【转盘抽奖】:获得三叶草:{O0O000000O00O0000}')#line:454
                        if OO00OO0O0O00OOO0O ==4 or OO00OO0O0O00OOO0O ==8 :#line:455
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:456
                        if OO00OO0O0O00OOO0O =='抽奖次数已用完':#line:460
                            if OO00OO000O00O000O :#line:461
                                OO0O00000O0OOO00O =random .randint (160 ,190 )/10 #line:462
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{OO0O00000O0OOO00O}秒获取抽奖机会')#line:463
                                time .sleep (OO0O00000O0OOO00O )#line:464
                                OOO00O0OO00OOOO00 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O0O000OOOOO000000 ).json ()#line:465
                                if 'status'in OOO00O0OO00OOOO00 :#line:467
                                    if OOO00O0OO00OOOO00 ['status']==200 :#line:468
                                        print (f'【转盘抽奖】:{OOO00O0OO00OOOO00["message"]}')#line:469
                                    if OOO00O0OO00OOOO00 ['status']==500 :#line:470
                                        print (f'【转盘抽奖】:{OOO00O0OO00OOOO00["message"]}')#line:471
                                        break #line:472
                                time .sleep (random .randint (10 ,15 )/10 )#line:473
                            else :#line:474
                                break #line:475
                time .sleep (random .randint (8 ,15 )/10 )#line:476
        except Exception as O0OOOO0OOOOO0OOOO :#line:477
            print (O0OOOO0OOOOO0OOOO )#line:478
    def friends_invitation (O0OO0O0O0O000O0O0 ):#line:481
        try :#line:482
            OOO000O0O000OO0OO =f'__{timi_new()}'#line:483
            O0OO00000O00O00OO ={'authorization':O0OO0O0O0O000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0O000OO0OO ),'signstring':OOO000O0O000OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:492
            O00OO0OO00OO0000O =requests .request ('get',f'{host}/friends',headers =O0OO00000O00O00OO ).json ()#line:493
            if 'status'in O00OO0OO00OO0000O :#line:494
                if O00OO0OO00OO0000O ['status']==200 :#line:495
                    O000OOOO00OOOOO0O =O00OO0OO00OO0000O ['data']['myInviteter']#line:496
                    if O000OOOO00OOOOO0O :#line:497
                        OO000O0OO00O0OOOO =O000OOOO00OOOOO0O ['user']['nickname']#line:498
                        OOO00OOOO0000OO00 =O0OO0O0O0O000O0O0 .certification ()#line:499
                        print (f'【绑邀请码】:我的邀请人:{OO000O0OO00O0OOOO}丨实名:{OOO00OOOO0000OO00}')#line:500
                    else :#line:501
                        if O0OO0O0O0O000O0O0 .innerId !='0':#line:502
                            OOO000O0O000OO0OO =f'_innerId={O0OO0O0O0O000O0O0.innerId}_{timi_new()}'#line:503
                            O0OO00000O00O00OO ={'authorization':O0OO0O0O0O000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0O000OO0OO ),'signstring':OOO000O0O000OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
                            OOO0OOO00O0O0O0O0 ={"innerId":O0OO0O0O0O000O0O0 .innerId }#line:513
                            O0OO0OO00000OOO00 =requests .request ('post',f'{host}/friends/my-invitation',headers =O0OO00000O00O00OO ,data =OOO0OOO00O0O0O0O0 ).json ()#line:514
                            if 'status'in O0OO0OO00000OOO00 :#line:515
                                if O0OO0OO00000OOO00 ['status']==200 :#line:516
                                    print (f'【绑邀请码】:{O0OO0O0O0O000O0O0.innerId}{O0OO0OO00000OOO00["message"]}')#line:517
                        else :#line:518
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:519
        except Exception as OO00O00000O000O00 :#line:520
            print (OO00O00000O000O00 )#line:521
    def add_clover (O0000OO0O0OOOO000 ):#line:525
        try :#line:526
            O00OO0O0O00000O00 =f'__{timi_new()}'#line:527
            O000000O00O0000O0 ={'authorization':O0000OO0O0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0O00000O00 ),'signstring':O00OO0O0O00000O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:536
            OO0O00OOOOOOOO00O =requests .request ('get',f'{host}/assets/clovers',headers =O000000O00O0000O0 ).json ()#line:537
            if 'status'in OO0O00OOOOOOOO00O :#line:539
                if OO0O00OOOOOOOO00O ['status']==200 :#line:540
                    OOO0OOO00OOO00O0O =OO0O00OOOOOOOO00O ['data']['clover']#line:541
                    OO0OOO000O000O0O0 =OO0O00OOOOOOOO00O ['data']['used_clover']#line:542
                    O00O00000O000O000 =float (OOO0OOO00OOO00O0O )-float (OO0OOO000O000O0O0 )#line:543
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OO0OOO000O000O0O0}')#line:544
                    if O00O00000O000O000 >1 :#line:545
                        O00OO0O0O00000O00 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00O00000O000O000)}_{timi_new()}'#line:546
                        O000000O00O0000O0 ={'authorization':O0000OO0O0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0O00000O00 ),'signstring':O00OO0O0O00000O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:555
                        OOO000OOO0O0O0O00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00O00000O000O000 )}#line:556
                        O0O00O0OO0O00000O =requests .request ('post',f'{host}/lottery/add-stake',headers =O000000O00O0000O0 ,data =OOO000OOO0O0O0O00 ).json ()#line:557
                        if 'status'in O0O00O0OO0O00000O :#line:559
                            if O0O00O0OO0O00000O ['status']==200 :#line:560
                                print (f'【参与抽奖】:添加三叶草:{O0O00O0OO0O00000O["data"]}丨数量:{O00O00000O000O000}')#line:561
            OO000OO0O00O00O00 =requests .request ('get',f'{host}/lottery',headers =O000000O00O0000O0 ).json ()#line:562
            O0OO00OOO000O0O00 =O0000OO0O0OOOO000 .winning_rewards ()#line:564
            if 'status'in OO000OO0O00O00O00 :#line:565
                if OO000OO0O00O00O00 ['status']==200 :#line:566
                    OO0O0OO0O0OOOOOOO =OO000OO0O00O00O00 ['data'][0 ]['day_get_gold_quantity']#line:567
                    print (f'【参与抽奖】:预计每天中{OO0O0OO0O0OOOOOOO[:6]}种子丨好友收益:{O0OO00OOO000O0O00}')#line:568
        except Exception as O000O0000O00OOO00 :#line:569
            print (O000O0000O00OOO00 )#line:570
    def energy (O0OO000OOO00O0O0O ):#line:573
        OOOO0O00O00OOOO0O =f'__{timi_new()}'#line:574
        O0O0000OOOOO00OO0 ={'authorization':O0OO000OOO00O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00O00OOOO0O ),'signstring':OOOO0O00O00OOOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
        OOOO0000O0000O00O =requests .request ('get',f'{host}/energy/general',headers =O0O0000OOOOO00OO0 ).json ()#line:584
        if 'status'in OOOO0000O0000O00O :#line:586
            if OOOO0000O0000O00O ['status']==200 :#line:587
                O00O0OO0OO0O0O0OO =OOOO0000O0000O00O ['data']['ordinary_water_consumptions']#line:588
                if float (O00O0OO0OO0O0O0OO )<80 :#line:589
                    O0OOO00O0O0O00OO0 =99 -float (O00O0OO0OO0O0O0OO )#line:590
                    OO0OO0OO00OO00OOO ={"fertilizer":str (O0OOO00O0O0O00OO0 ).split ('.')[0 ]}#line:591
                    O00000O0O00OOOO0O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0O0000OOOOO00OO0 ,data =OO0OO0OO00OO00OOO ).json ()#line:592
                    if 'status'in O00000O0O00OOOO0O :#line:594
                        if O00000O0O00OOOO0O ['status']==200 :#line:595
                            print (f'【购买肥料】:{O00000O0O00OOOO0O["message"]}')#line:596
                O00O0O00O0O00OO00 =OOOO0000O0000O00O ['data']['ordinary_water_consumptions']#line:597
                if float (O00O0O00O0O00OO00 )<800 :#line:598
                    O0OOOOO0000O0O0OO =999 -float (O00O0O00O0O00OO00 )#line:599
                    O0000OO000000O0OO ={"water":str (O0OOOOO0000O0O0OO ).split ('.')[0 ]}#line:600
                    O00O00OOOO00O0OO0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O0000OOOOO00OO0 ,data =O0000OO000000O0OO ).json ()#line:601
                    if 'status'in O00O00OOOO00O0OO0 :#line:602
                        if O00O00OOOO00O0OO0 ['status']==200 :#line:603
                            print (f'【购买水滴】:{O00O00OOOO00O0OO0["message"]}')#line:604
def version_of_the_validation ():#line:610
    return str ((66 -56 )/10 )#line:611
def gitee_validation ():#line:613
    try :#line:614
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:615
    except Exception as OO0O00OOOOO00OOO0 :#line:616
        sys .exit (0 )#line:617
def update_the_validation ():#line:623
    try :#line:624
        O000O00O0O0OOOO0O =gitee_validation ()#line:625
        if version_of_the_validation ()<O000O00O0O0OOOO0O ['CityEarth']['edition']:#line:626
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000O00O0O0OOOO0O["CityEarth"]["edition"]}   ❌')#line:627
            print (f'更新内容=>>{O000O00O0O0OOOO0O["CityEarth"]["content"]}   👍')#line:628
        else :#line:629
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000O00O0O0OOOO0O["CityEarth"]["edition"]}   ✅')#line:630
            print (f'更新内容=>> {O000O00O0O0OOOO0O["CityEarth"]["content"]}   👍')#line:631
    except Exception as O0OOOOO0O000O0O00 :#line:632
        print (O0OOOOO0O000O0O00 )#line:633
def os_qinglong ():#line:636
    if application in os .environ :#line:637
        OOOO0O00OOOO0O0O0 =os .environ [application ].split ('\n')#line:638
        if len (OOOO0O00OOOO0O0O0 )>0 :#line:639
            return OOOO0O00OOOO0O0O0 #line:640
        else :#line:641
            print (f"{application}变量未启用")#line:642
            print ('脚本退出')#line:643
            sys .exit (1 )#line:644
    else :#line:645
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:646
        return os_built ()#line:647
def os_built ():#line:650
    if token :#line:651
        OO0O00O0OO0OOOO0O =token .split ('\n')#line:652
        if len (OO0O00O0OO0OOOO0O )>0 :#line:653
            return OO0O00O0OO0OOOO0O #line:654
    else :#line:655
        print (f"内置变量为空")#line:656
        print ('脚本结束')#line:657
        sys .exit (0 )#line:658
if __name__ =='__main__':#line:661
    start ()#line:662
