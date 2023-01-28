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

time_xx = random.randint(8, 12)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://scsc.sc19319.com'#line:2
golden_seed =0 #line:3
def start ():#line:5
    try :#line:6
        update_the_validation ()#line:7
        OOOO0OO0O000OO000 =os_qinglong ()#line:8
        print (f"==========共找到{len(OOOO0OO0O000OO000)}个账号==========")#line:9
        for O0OO0O0O0O0O00O00 in OOOO0OO0O000OO000 :#line:10
            print (f"------------正在执行第{OOOO0OO0O000OO000.index(O0OO0O0O0O0O00O00) + 1}个账号------------")#line:11
            OOOO0O0000O00O00O =CityEarth (O0OO0O0O0O0O00O00 )#line:12
            def OO0OO00OO0000O0OO ():#line:14
                if OOOO0O0000O00O00O .base_info ():#line:16
                    OOOO0O0000O00O00O .game_map ()#line:20
                    OOOO0O0000O00O00O .friends_invitation ()#line:22
                    OOOO0O0000O00O00O .add_clover ()#line:24
                    OOOO0O0000O00O00O .energy ()#line:26
                    OOOO0O0000O00O00O .synthetic ()#line:28
                    OOOO0O0000O00O00O .propsraffle ()#line:30
                    OOOO0O0000O00O00O .crops_illustrated ()#line:32
                    OOOO0O0000O00O00O .give_gold ()#line:34
                else :#line:35
                    print ('token失效')#line:36
            OOO0OO00OO0000OOO =threading .Thread (target =OO0OO00OO0000O0OO )#line:38
            OOO0OO00OO0000OOO .start ()#line:39
            time .sleep (time_xx )#line:40
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:42
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:43
    except Exception as O0O00O00O0000OOO0 :#line:44
        print (O0O00O00O0000OOO0 )#line:45
def sign (O000OOOOOOOO00O0O ):#line:48
    O000OO0O0OOO000OO =hashlib .md5 (O000OOOOOOOO00O0O .encode ()).hexdigest ()#line:49
    O0O000OOOOO0O00O0 ="scsc%^&*"+O000OO0O0OOO000OO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:50
    OO000O0OO00OO00OO =hashlib .md5 (O0O000OOOOO0O00O0 .encode ()).hexdigest ()#line:51
    return OO000O0OO00OO00OO #line:52
def timi_new ():#line:55
    return str (int (time .time ()*1000 ))#line:56
class CityEarth :#line:59
    def __init__ (OOO000OO0OO00OO00 ,O000O0OOO0000OOO0 ):#line:61
        try :#line:62
            OOO000OO0OO00OO00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:63
            OOO000OO0OO00OO00 .token =O000O0OOO0000OOO0 .split ('&')[0 ]#line:64
            OOO000OO0OO00OO00 .innerId =O000O0OOO0000OOO0 .split ('&')[1 ]#line:65
            OOO000OO0OO00OO00 .doneeNo =O000O0OOO0000OOO0 .split ('&')[2 ]#line:66
        except :#line:67
            print ('变量格式错误')#line:68
    def base_info (OOO000OOO00O000O0 ):#line:71
        try :#line:72
            O0OO00O00O0O000OO =f'__{timi_new()}'#line:73
            OOOO0O00OO0O0OOO0 ={'authorization':OOO000OOO00O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O00O0O000OO ),'signstring':O0OO00O00O0O000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:82
            O0OO0O0O0000O0OO0 =requests .request ('get',f'{host}/user',headers =OOOO0O00OO0O0OOO0 ).json ()#line:83
            if 'status'in O0OO0O0O0000O0OO0 :#line:85
                if O0OO0O0O0000O0OO0 ['status']==200 :#line:86
                    OO0000O0O00OO00O0 =O0OO0O0O0000O0OO0 ['data']['nickname']#line:87
                    O000OOOO0OO00O00O =O0OO0O0O0000O0OO0 ['data']['inner_id']#line:88
                    OO0OOO0OOOOO00O0O =O0OO0O0O0000O0OO0 ['data']['assets']['gold']#line:89
                    O000OO0O0OOO00OO0 =O0OO0O0O0000O0OO0 ['data']['level']#line:90
                    print (f'【账号信息】:昵称:{OO0000O0O00OO00O0[:5]}丨ID:{str(O000OOOO0OO00O00O)[:3] + "**" + str(O000OOOO0OO00O00O)[5:]}丨等级:{O000OO0O0OOO00OO0}丨种子:{str(OO0OOO0OOOOO00O0O).split(".")[0]}')#line:91
                if O0OO0O0O0000O0OO0 ['status']==401 :#line:92
                    return False #line:93
                if O0OO0O0O0000O0OO0 ['status']==500 :#line:94
                    return False #line:95
            return True #line:96
        except Exception as OOO00O0OOOO0OOOOO :#line:97
            print (OOO00O0OOOO0OOOOO )#line:98
    def game_map (O0O0OO00O0O000000 ):#line:101
        O0000000OOO00O00O =f'__{timi_new()}'#line:102
        OOO0OO0OOOOO0O00O ={'authorization':O0O0OO00O0O000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000000OOO00O00O ),'signstring':O0000000OOO00O00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:111
        O0OOOOO0O0OO00000 =requests .request ('get',f'{host}/game/map',headers =OOO0OO0OOOOO0O00O ).json ()#line:112
        if 'status'in O0OOOOO0O0OO00000 :#line:114
            if O0OOOOO0O0OO00000 ['status']==200 :#line:115
                for O000O00O0OOOOO000 in O0OOOOO0O0OO00000 ['data']['list'][0 ]['crops']:#line:116
                    O000OO0OOOOO0O0OO =O000O00O0OOOOO000 ['level']#line:118
                    if O000OO0OOOOO0O0OO ==41 :#line:119
                        OOO000OOOO0000000 =O000O00O0OOOOO000 ['crop_name']#line:120
                        O00O0OO0OOO00O000 =O000O00O0OOOOO000 ['count']#line:121
                        if O00O0OO0OOO00O000 >0 :#line:122
                            print (f'【农业资产】:{OOO000OOOO0000000}丨数量:{O00O0OO0OOO00O000}')#line:123
    def give_gold (OOOO0OOOOOO0OO00O ):#line:126
        O0O0O0O0O000O000O =f'__{timi_new()}'#line:127
        O0000O0O0OO00000O ={'authorization':OOOO0OOOOOO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0O000O000O ),'signstring':O0O0O0O0O000O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:136
        OO0O00OOO0OOOOOO0 =requests .request ('get',f'{host}/user',headers =O0000O0O0OO00000O ).json ()#line:137
        if 'status'in OO0O00OOO0OOOOOO0 :#line:138
            if OO0O00OOO0OOOOOO0 ['status']==200 :#line:139
                if float (OOOO0OOOOOO0OO00O .doneeNo )!=0 :#line:140
                    O00000O000OOOOO00 =OO0O00OOO0OOOOOO0 ['data']['assets']['gold']#line:141
                    if float (O00000O000OOOOO00 )>2 :#line:142
                        OOO000000OOOOOO00 =int (float (O00000O000OOOOO00 )/1.1 )#line:143
                        O0O0O0O0O000O000O =f'_doneeNo={OOOO0OOOOOO0OO00O.doneeNo}&quantity={OOO000000OOOOOO00}_{timi_new()}'#line:144
                        O0000O0O0OO00000O ={'authorization':OOOO0OOOOOO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0O000O000O ),'signstring':O0O0O0O0O000O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
                        O0OOOOO00000OOOO0 ={"quantity":OOO000000OOOOOO00 ,"doneeNo":OOOO0OOOOOO0OO00O .doneeNo }#line:157
                        O0O0OOOO0OO0O000O =requests .request ('post',f'{host}/finance/give-gold',headers =O0000O0O0OO00000O ,data =O0OOOOO00000OOOO0 ).json ()#line:158
                        if 'status'in O0O0OOOO0OO0O000O :#line:160
                            if O0O0OOOO0OO0O000O ['status']==200 :#line:161
                                if O0O0OOOO0OO0O000O ['data']:#line:162
                                    print (f'【赠送种子】:赠送{OOO000000OOOOOO00}种子给{OOOO0OOOOOO0OO00O.doneeNo}成功')#line:163
                else :#line:164
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:165
    def winning_rewards (OOOO00OOOOO0O0OO0 ):#line:168
        O0OOOO0OO0O00OO0O =f'__{timi_new()}'#line:169
        OO00OO0O000OOO00O ={'authorization':OOOO00OOOOO0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OO0O00OO0O ),'signstring':O0OOOO0OO0O00OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:178
        OOOOOO0OO0OO00O0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO00OO0O000OOO00O ).json ()#line:179
        if 'status'in OOOOOO0OO0OO00O0O :#line:181
            if OOOOOO0OO0OO00O0O ['status']==200 :#line:182
                if OOOOOO0OO0OO00O0O ['data']['amount']:#line:183
                    O0000OO00O0OOOO0O =OOOOOO0OO0OO00O0O ['data']['amount']['gold']#line:184
                    return O0000OO00O0OOOO0O #line:185
                else :#line:186
                    return 0 #line:187
    def certification (O00O0OOOOO0000O00 ):#line:190
        O00000O0OO00000O0 =f'__{timi_new()}'#line:191
        OO0OO0OO000OO000O ={'authorization':O00O0OOOOO0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0OO00000O0 ),'signstring':O00000O0OO00000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:200
        O0OOO0O0O0000O00O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0OO0OO000OO000O ).json ()#line:201
        if 'status'in O0OOO0O0O0000O00O :#line:203
            if O0OOO0O0O0000O00O ['status']==200 :#line:204
                if O0OOO0O0O0000O00O ['data']['result']:#line:205
                    O0O0OO0OO0O0O0O0O =O0OOO0O0O0000O00O ['data']['nick_name']#line:206
                    return O0O0OO0OO0O0O0O0O #line:207
                else :#line:208
                    return '未实名'#line:209
    def crops_illustrated (O0O000000O00O0OOO ):#line:212
        OOO000OOO000OOOO0 =f'__{timi_new()}'#line:213
        O0OOOOOO000OO00OO ={'authorization':O0O000000O00O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOO000OOOO0 ),'signstring':OOO000OOO000OOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:222
        O0O0OO000OO00O000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OOOOOO000OO00OO ).json ()#line:223
        if 'status'in O0O0OO000OO00O000 :#line:225
            if O0O0OO000OO00O000 ['status']==200 :#line:226
                O000000OOO000OOO0 =O0O0OO000OO00O000 ['data'][0 ]['crops']#line:227
                for O00000O00O00O00O0 in O000000OOO000OOO0 :#line:228
                    if O00000O00O00O00O0 ['ill_clover_award']:#line:229
                        if float (O00000O00O00O00O0 ['ill_clover_award'])>1 :#line:230
                            if O00000O00O00O00O0 ['is_finish']:#line:231
                                if not O00000O00O00O00O0 ['is_getit']:#line:232
                                    OOO000OOO000OOOO0 =f'_award_level={O00000O00O00O00O0["level"]}_{timi_new()}'#line:233
                                    O0OOOOOO000OO00OO ={'authorization':O0O000000O00O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOO000OOOO0 ),'signstring':OOO000OOO000OOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:242
                                    O00O00000000O00O0 ={"award_level":O00000O00O00O00O0 ['level']}#line:243
                                    O0O0OOO0O0000O0O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OOOOOO000OO00OO ,json =O00O00000000O00O0 ).json ()#line:245
                                    if 'status'in O0O0OOO0O0000O0O0 :#line:246
                                        if O0O0OOO0O0000O0O0 ['status']==200 :#line:247
                                            O0OO00O0000OO00O0 =O0O0OOO0O0000O0O0 ['data']['ill_clover_award']#line:248
                                            print (f'【图鉴奖励】:领取{O00000O00O00O00O0["crop_name"]}成就丨奖励{O0OO00O0000OO00O0}叶子成功')#line:250
                                        if O0O0OOO0O0000O0O0 ['status']==500 :#line:251
                                            print (f'【图鉴奖励】:{O0O0OOO0O0000O0O0["message"]}')#line:252
    def watched_ad (O00O0O00O000O0O0O ):#line:255
        O00O0OOO00O0OO00O =f'__{timi_new()}'#line:256
        O00OO0000O0O0OO00 ={'authorization':O00O0O00O000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO00O0OO00O ),'signstring':O00O0OOO00O0OO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:265
        OO0OOOO000OOOO000 =requests .request ('post',f'{host}/game/watched-ad',headers =O00OO0000O0O0OO00 ).json ()#line:266
        print (OO0OOOO000OOOO000 )#line:267
    def user_ad (O000OO0OO0OOO0OO0 ):#line:270
        OOO0OOOO00OO00O00 =f'__{timi_new()}'#line:271
        OOO0000OOOO0000OO ={'authorization':O000OO0OO0OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOO00OO00O00 ),'signstring':OOO0OOOO00OO00O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
        O000OOO0OO00OO0OO =requests .request ('get',f'{host}/user/ad',headers =OOO0000OOOO0000OO ).json ()#line:281
        if 'status'in O000OOO0OO00OO0OO :#line:283
            if O000OOO0OO00OO0OO ['status']==200 :#line:284
                OOO0O0O0O00O0OOO0 =O000OOO0OO00OO0OO ['data']['max_time']#line:285
                O0O0OOO00O000O0OO =O000OOO0OO00OO0OO ['data']['watch_time']#line:286
                OOO0OOOO0OOO0O00O =O000OOO0OO00OO0OO ['data']['added_time']#line:287
                print (f'【获取种子】:获取种子剩余{OOO0OOOO0OOO0O00O + OOO0O0O0O00O0OOO0 - O0O0OOO00O000O0OO}次丨好友提供:{OOO0OOOO0OOO0O00O}次')#line:288
                if OOO0OOOO0OOO0O00O +OOO0O0O0O00O0OOO0 -O0O0OOO00O000O0OO >0 :#line:289
                    time .sleep (random .randint (16 ,19 ))#line:290
                    O0000O00OO00O0OOO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO0000OOOO0000OO ).json ()#line:291
                    if 'status'in O0000O00OO00O0OOO :#line:293
                        if O0000O00OO00O0OOO ['status']==200 :#line:294
                            OO000000O0000OOO0 =O0000O00OO00O0OOO ['data']['silver']#line:295
                            print (f'【获取种子】:获得种子:{OO000000O0000OOO0}')#line:296
                            return True #line:297
                        if O0000O00OO00O0OOO ['status']==500 :#line:298
                            OO00OO0O00O000OO0 =O0000O00OO00O0OOO ['message']#line:299
                            print (f'【获取种子】:{OO00OO0O00O000OO0}')#line:300
                            return False #line:301
    def synthetic (OO000000O0OO0O000 ):#line:304
        global id ,g #line:305
        try :#line:306
            OO0OOO00O0000OOOO =OO000000O0OO0O000 .level_new ()#line:307
            while True :#line:308
                OO00000O00O0O000O =f'__{timi_new()}'#line:309
                O0OOO00OOOOOO0OOO ={'authorization':OO000000O0OO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000O00O0O000O ),'signstring':OO00000O00O0O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:318
                O00OO00OO0OOO0OOO =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO00OOOOOO0OOO ).json ()#line:319
                if 'status'in O00OO00OO0OOO0OOO :#line:321
                    if O00OO00OO0OOO0OOO ['status']==200 :#line:322
                        OOO0OO000O0O0OO0O =O00OO00OO0OOO0OOO ['data']['cropList']#line:323
                        OO00O000O0O00O0O0 =O00OO00OO0OOO0OOO ['data']['gameCoreDataDBid']#line:324
                        O0O000O000O0O0000 =0 #line:325
                        for OO0O0OO0O00O000O0 in OOO0OO000O0O0OO0O :#line:326
                            if not OO0O0OO0O00O000O0 :#line:327
                                OO0O00O0O0O000000 =f'_crop_id={OO00O000O0O00O0O0}&site={O0O000O000O0O0000}_{OO000000O0OO0O000.time}'#line:328
                                O0000000OOO0OO0OO ={'authorization':OO000000O0OO0O000 .token ,'timestamp':OO000000O0OO0O000 .time ,'sign':sign (OO0O00O0O0O000000 ),'signstring':OO0O00O0O0O000000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:337
                                O000OOOOO0OO0OO00 ={"site":O0O000O000O0O0000 ,"crop_id":OO00O000O0O00O0O0 }#line:338
                                O00O0O00O0000OO00 =requests .request ('post',f'{host}/game/crops/buy',headers =O0000000OOO0OO0OO ,data =O000OOOOO0OO0OO00 ).json ()#line:339
                                time .sleep (random .randint (1 ,3 )/10 )#line:341
                                if 'status'in O00O0O00O0000OO00 :#line:342
                                    if O00O0O00O0000OO00 ['status']==200 :#line:343
                                        if O00O0O00O0000OO00 ['message']=='种子数量不足':#line:344
                                            OO0OOO00O0000OOOO =OO000000O0OO0O000 .level_new ()#line:345
                                            print (f'【种植合成】:{O00O0O00O0000OO00["message"]}')#line:346
                                            if not OO000000O0OO0O000 .user_ad ():#line:347
                                                return False #line:348
                                        print (f'【种植合成】:种植农作物,位置{O0O000O000O0O0000}')#line:349
                                    if O00O0O00O0000OO00 ['status']==500 :#line:350
                                        print (f'【种植合成】:{O00O0O00O0000OO00["message"]}')#line:351
                                        return False #line:352
                            O0O000O000O0O0000 +=1 #line:353
                        OOO0OO0OOOO00O0OO =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO00OOOOOO0OOO ).json ()#line:354
                        O0OO0OOO0OOO00OO0 =OOO0OO0OOOO00O0OO ['data']['cropList']#line:355
                        O000O0000OO00OO00 =False #line:356
                        for OO0O0OO0O00O000O0 in range (12 ):#line:357
                            id =O0OO0OOO0OOO00OO0 [OO0O0OO0O00O000O0 ]['level']#line:358
                            if float (OO0OOO00O0000OOOO )-float (id )>9 :#line:359
                                OO00O0OO000OO0OO0 =f'_site={OO0O0OO0O00O000O0}_{timi_new()}'#line:360
                                O0OOO0OOO00OOOOOO ={'accept':'application/json, text/plain, */*','authorization':OO000000O0OO0O000 .token ,'timestamp':timi_new (),'sign':sign (OO00O0OO000OO0OO0 ),'signstring':OO00O0OO000OO0OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:370
                                O00OOOO000O0OOO00 ={"site":OO0O0OO0O00O000O0 }#line:371
                                OOO000O0OO00O0O0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OOO0OOO00OOOOOO ,data =O00OOOO000O0OOO00 ).json ()#line:373
                                if 'status'in OOO000O0OO00O0O0O :#line:374
                                    if OOO000O0OO00O0O0O ['status']==200 :#line:375
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:376
                            if id !=0 :#line:377
                                for O0O0O00000O0OOOO0 in range (11 ):#line:378
                                    OOO00O0OOO0OOO000 =O0O0O00000O0OOOO0 +1 #line:379
                                    g =O0OO0OOO0OOO00OO0 [OOO00O0OOO0OOO000 ]['level']#line:380
                                    if id ==g :#line:381
                                        OOOOOO0OO0O00O0OO =O0O0O00000O0OOOO0 +2 #line:382
                                        if OOOOOO0OO0O00O0OO ==OO0O0OO0O00O000O0 +1 :#line:383
                                            pass #line:384
                                        else :#line:385
                                            OO0OOO000O00O000O =OO0O0OO0O00O000O0 +1 #line:386
                                            time .sleep (random .randint (1 ,3 )/10 )#line:388
                                            OOO00O000O000000O =f'_site={OO0OOO000O00O000O - 1}&targetSite={OOOOOO0OO0O00O0OO - 1}_{timi_new()}'#line:389
                                            OOO0OOO00O00000O0 ={'accept':'application/json, text/plain, */*','authorization':OO000000O0OO0O000 .token ,'timestamp':timi_new (),'sign':sign (OOO00O000O000000O ),'signstring':OOO00O000O000000O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:404
                                            O00OOOO0O00O00OO0 ={"site":int (OO0OOO000O00O000O -1 ),"targetSite":int (OOOOOO0OO0O00O0OO -1 )}#line:405
                                            O00OO0000000O0OOO =requests .request ('post',f'{host}/game/crops/move',headers =OOO0OOO00O00000O0 ,json =O00OOOO0O00O00OO0 ).json ()#line:407
                                            if 'status'in O00OO0000000O0OOO :#line:408
                                                if O00OO0000000O0OOO ['status']==200 :#line:409
                                                    pass #line:410
                                            print ('【种植合成】:',OO0OOO000O00O000O ,OOOOOO0OO0O00O0OO ,'合成成功')#line:412
                                            O000O0000OO00OO00 =True #line:413
                                    if O000O0000OO00OO00 :#line:414
                                        break #line:415
                                if O000O0000OO00OO00 :#line:416
                                    break #line:417
        except Exception as O0000OOOO0OOO00O0 :#line:418
            OO000000O0OO0O000 .synthetic ()#line:419
    def level_new (OOO00O0O00OO0OOO0 ):#line:422
        try :#line:423
            O0O0O0O00OO00000O =f'__{timi_new()}'#line:424
            O00O00OOOO0OO0O0O ={'authorization':OOO00O0O00OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00OO00000O ),'signstring':O0O0O0O00OO00000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:433
            O000O000O00OOO000 =requests .request ('get',f'{host}/user',headers =O00O00OOOO0OO0O0O ).json ()#line:434
            if 'status'in O000O000O00OOO000 :#line:435
                if O000O000O00OOO000 ['status']==200 :#line:436
                    return float (O000O000O00OOO000 ['data']['level'])#line:437
        except Exception as OOOOOOO00O00OOOO0 :#line:438
            print (OOOOOOO00O00OOOO0 )#line:439
    def propsraffle (OOO0O000O0O0000OO ):#line:442
        try :#line:443
            while True :#line:444
                OOOO00OOOO000O00O =f'__{timi_new()}'#line:445
                OO00O0OO000O0O00O ={'authorization':OOO0O000O0O0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOOO000O00O ),'signstring':OOOO00OOOO000O00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:454
                O0OOOOO00O00O000O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO00O0OO000O0O00O ).json ()#line:455
                if 'status'in O0OOOOO00O00O000O :#line:457
                    if O0OOOOO00O00O000O ['status']==200 :#line:458
                        O0O0OOOOOOOO0OO0O =O0OOOOO00O00O000O ['data']['rows']#line:459
                        OOO0O00OOOOOOOO0O =O0OOOOO00O00O000O ['data']['vstate']#line:460
                        if O0O0OOOOOOOO0OO0O ==5 or O0O0OOOOOOOO0OO0O ==6 or O0O0OOOOOOOO0OO0O ==7 :#line:461
                            O0OO0OOOO0O000O0O =O0OOOOO00O00O000O ['data']['silver']#line:462
                            print (f'【转盘抽奖】:获得种子:{O0OO0OOOO0O000O0O}')#line:463
                        if O0O0OOOOOOOO0OO0O ==1 or O0O0OOOOOOOO0OO0O ==2 or O0O0OOOOOOOO0OO0O ==3 :#line:464
                            OOO00OOOO0OOOOO0O =O0OOOOO00O00O000O ['data']['clover']#line:465
                            print (f'【转盘抽奖】:获得三叶草:{OOO00OOOO0OOOOO0O}')#line:466
                        if O0O0OOOOOOOO0OO0O ==4 or O0O0OOOOOOOO0OO0O ==8 :#line:467
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:468
                        if O0O0OOOOOOOO0OO0O =='抽奖次数已用完':#line:472
                            if OOO0O00OOOOOOOO0O :#line:473
                                O0OO0OO0000000000 =random .randint (160 ,190 )/10 #line:474
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{O0OO0OO0000000000}秒获取抽奖机会')#line:475
                                time .sleep (O0OO0OO0000000000 )#line:476
                                O000O0000OO0OOOOO =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OO00O0OO000O0O00O ).json ()#line:478
                                if 'status'in O000O0000OO0OOOOO :#line:480
                                    if O000O0000OO0OOOOO ['status']==200 :#line:481
                                        print (f'【转盘抽奖】:{O000O0000OO0OOOOO["message"]}')#line:482
                                    if O000O0000OO0OOOOO ['status']==500 :#line:483
                                        print (f'【转盘抽奖】:{O000O0000OO0OOOOO["message"]}')#line:484
                                        break #line:485
                                time .sleep (random .randint (10 ,15 )/10 )#line:486
                            else :#line:487
                                break #line:488
                time .sleep (random .randint (8 ,15 )/10 )#line:489
        except Exception as O0O0OOO00OO00O0OO :#line:490
            print (O0O0OOO00OO00O0OO )#line:491
    def friends_invitation (OOOOO00000O0O0OOO ):#line:494
        try :#line:495
            OO0OOO0000OOOO0OO =f'__{timi_new()}'#line:496
            O00O00OO0O0O000O0 ={'authorization':OOOOO00000O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0000OOOO0OO ),'signstring':OO0OOO0000OOOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:505
            OO0OOO000O0000O00 =requests .request ('get',f'{host}/friends',headers =O00O00OO0O0O000O0 ).json ()#line:506
            if 'status'in OO0OOO000O0000O00 :#line:507
                if OO0OOO000O0000O00 ['status']==200 :#line:508
                    O00O00O0000O0OOOO =OO0OOO000O0000O00 ['data']['myInviteter']#line:509
                    if O00O00O0000O0OOOO :#line:510
                        OO00000O00O00000O =O00O00O0000O0OOOO ['user']['nickname']#line:511
                        O0O00OOOO00OOOO0O =OOOOO00000O0O0OOO .certification ()#line:512
                        print (f'【绑邀请码】:我的邀请人:{OO00000O00O00000O}丨实名:{O0O00OOOO00OOOO0O}')#line:513
                    else :#line:514
                        if OOOOO00000O0O0OOO .innerId !='0':#line:515
                            OO0OOO0000OOOO0OO =f'_innerId={OOOOO00000O0O0OOO.innerId}_{timi_new()}'#line:516
                            O00O00OO0O0O000O0 ={'authorization':OOOOO00000O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0000OOOO0OO ),'signstring':OO0OOO0000OOOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:525
                            O0000OOO000000O0O ={"innerId":OOOOO00000O0O0OOO .innerId }#line:526
                            O0O000O0000O0O00O =requests .request ('post',f'{host}/friends/my-invitation',headers =O00O00OO0O0O000O0 ,data =O0000OOO000000O0O ).json ()#line:528
                            if 'status'in O0O000O0000O0O00O :#line:529
                                if O0O000O0000O0O00O ['status']==200 :#line:530
                                    print (f'【绑邀请码】:{OOOOO00000O0O0OOO.innerId}{O0O000O0000O0O00O["message"]}')#line:531
                        else :#line:532
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:533
        except Exception as O0O0OOO00000O00O0 :#line:534
            print (O0O0OOO00000O00O0 )#line:535
    def add_clover (OOO000O0OOO000O00 ):#line:538
        global golden_seed #line:539
        try :#line:540
            O0O0O0OO0000OO000 =f'__{timi_new()}'#line:541
            OO00O0OOOOOO0OO0O ={'authorization':OOO000O0OOO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO0000OO000 ),'signstring':O0O0O0OO0000OO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:550
            O0O0OOOO0OOOO0OO0 =requests .request ('get',f'{host}/assets/clovers',headers =OO00O0OOOOOO0OO0O ).json ()#line:551
            if 'status'in O0O0OOOO0OOOO0OO0 :#line:553
                if O0O0OOOO0OOOO0OO0 ['status']==200 :#line:554
                    OOOO0O0OOOOO00000 =O0O0OOOO0OOOO0OO0 ['data']['clover']#line:555
                    O0O00OOOOOO0O00O0 =O0O0OOOO0OOOO0OO0 ['data']['used_clover']#line:556
                    O0OO00OO000OOOO0O =float (OOOO0O0OOOOO00000 )-float (O0O00OOOOOO0O00O0 )#line:557
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0O00OOOOOO0O00O0}')#line:558
                    if O0OO00OO000OOOO0O >1 :#line:559
                        O0O0O0OO0000OO000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OO00OO000OOOO0O)}_{timi_new()}'#line:560
                        OO00O0OOOOOO0OO0O ={'authorization':OOO000O0OOO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO0000OO000 ),'signstring':O0O0O0OO0000OO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:569
                        OO00O0000O0O00O00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OO00OO000OOOO0O )}#line:570
                        OOO00OOOOOOOO0OO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO00O0OOOOOO0OO0O ,data =OO00O0000O0O00O00 ).json ()#line:571
                        if 'status'in OOO00OOOOOOOO0OO0 :#line:573
                            if OOO00OOOOOOOO0OO0 ['status']==200 :#line:574
                                print (f'【参与抽奖】:添加三叶草:{OOO00OOOOOOOO0OO0["data"]}丨数量:{O0OO00OO000OOOO0O}')#line:575
            O0O0OO0O00OO0O0O0 =requests .request ('get',f'{host}/lottery',headers =OO00O0OOOOOO0OO0O ).json ()#line:576
            OO00000OO00000OOO =OOO000O0OOO000O00 .winning_rewards ()#line:578
            if 'status'in O0O0OO0O00OO0O0O0 :#line:579
                if O0O0OO0O00OO0O0O0 ['status']==200 :#line:580
                    O0000O000O00OO0OO =O0O0OO0O00OO0O0O0 ['data'][0 ]['day_get_gold_quantity']#line:581
                    golden_seed +=float (O0000O000O00OO0OO )#line:582
                    print (f'【参与抽奖】:预计每天中{O0000O000O00OO0OO[:6]}颗金种子丨好友收益:{str(OO00000OO00000OOO)[:6]}')#line:583
        except Exception as OO0O00OO0O00O0OOO :#line:584
            print (OO0O00OO0O00O0OOO )#line:585
    def energy (O0OOOO0OO000O00OO ):#line:588
        OOO0O00OO000O0O00 =f'__{timi_new()}'#line:589
        O0O000O0O0OO0O0O0 ={'authorization':O0OOOO0OO000O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00OO000O0O00 ),'signstring':OOO0O00OO000O0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:598
        O0O0000O0O00OOO00 =requests .request ('get',f'{host}/energy/general',headers =O0O000O0O0OO0O0O0 ).json ()#line:599
        if 'status'in O0O0000O0O00OOO00 :#line:601
            if O0O0000O0O00OOO00 ['status']==200 :#line:602
                OO0OOO000O0O0O0O0 =O0O0000O0O00OOO00 ['data']['ordinary_water_consumptions']#line:603
                if float (OO0OOO000O0O0O0O0 )<80 :#line:604
                    OOOO0O0OO0O000OOO =99 -float (OO0OOO000O0O0O0O0 )#line:605
                    OO0000O0O000OOO00 ={"fertilizer":str (OOOO0O0OO0O000OOO ).split ('.')[0 ]}#line:606
                    O0OOO0OO0OOOOOO00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0O000O0O0OO0O0O0 ,data =OO0000O0O000OOO00 ).json ()#line:608
                    if 'status'in O0OOO0OO0OOOOOO00 :#line:610
                        if O0OOO0OO0OOOOOO00 ['status']==200 :#line:611
                            print (f'【购买肥料】:{O0OOO0OO0OOOOOO00["message"]}')#line:612
                O00O0O000OOOO0OO0 =O0O0000O0O00OOO00 ['data']['ordinary_water_consumptions']#line:613
                if float (O00O0O000OOOO0OO0 )<800 :#line:614
                    O000OOOO0OO000OOO =999 -float (O00O0O000OOOO0OO0 )#line:615
                    O00OOOOO000O0O0OO ={"water":str (O000OOOO0OO000OOO ).split ('.')[0 ]}#line:616
                    OO0OOOOO00000O0OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O000O0O0OO0O0O0 ,data =O00OOOOO000O0O0OO ).json ()#line:617
                    if 'status'in OO0OOOOO00000O0OO :#line:618
                        if OO0OOOOO00000O0OO ['status']==200 :#line:619
                            print (f'【购买水滴】:{OO0OOOOO00000O0OO["message"]}')#line:620
def version_of_the_validation ():#line:624
    return str ((66 -56 )/10 )#line:625
def gitee_validation ():#line:628
    try :#line:629
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:630
    except Exception as O0O00O0000OO0OOOO :#line:631
        sys .exit (0 )#line:632
def update_the_validation ():#line:636
    try :#line:637
        O0OOO000000OO00O0 =gitee_validation ()#line:638
        if version_of_the_validation ()<O0OOO000000OO00O0 ['CityEarth']['edition']:#line:639
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOO000000OO00O0["CityEarth"]["edition"]}   ❌')#line:640
            print (f'更新内容=>>{O0OOO000000OO00O0["CityEarth"]["content"]}   👍')#line:641
        else :#line:642
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOO000000OO00O0["CityEarth"]["edition"]}   ✅')#line:643
            print (f'更新内容=>> {O0OOO000000OO00O0["CityEarth"]["content"]}   👍')#line:644
    except Exception as O00O00O0O000O0OO0 :#line:645
        print (O00O00O0O000O0OO0 )#line:646
def os_qinglong ():#line:649
    if application in os .environ :#line:650
        OO00O0000O0OOOO0O =os .environ [application ].split ('\n')#line:651
        if len (OO00O0000O0OOOO0O )>0 :#line:652
            return OO00O0000O0OOOO0O #line:653
        else :#line:654
            print (f"{application}变量未启用")#line:655
            print ('脚本退出')#line:656
            sys .exit (1 )#line:657
    else :#line:658
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:660
        return os_built ()#line:661
def os_built ():#line:664
    if token :#line:665
        O0OO000O00OO0O0O0 =token .split ('\n')#line:666
        if len (O0OO000O00OO0O0O0 )>0 :#line:667
            return O0OO000O00OO0O0O0 #line:668
    else :#line:669
        print (f"内置变量为空")#line:670
        print ('脚本结束')#line:671
        sys .exit (0 )#line:672
if __name__ =='__main__':#line:675
    start ()#line:676
