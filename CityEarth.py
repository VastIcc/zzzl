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

leves = 0                               # 如果卡住不动就把这个设置为当前账号的等级  运行之后记得改回 0
time_xx = random.randint(2, 4)          # 秒 执行下一个号的时间  2到4秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://scsc.sc19319.com'#line:2
def start ():#line:3
    try :#line:4
        update_the_validation ()#line:5
        OO000O0O0000O000O =os_qinglong ()#line:6
        print (f"==========共找到{len(OO000O0O0000O000O)}个账号==========")#line:7
        for O0O0OO0O000OO0OO0 in OO000O0O0000O000O :#line:8
            print (f"------------正在执行第{OO000O0O0000O000O.index(O0O0OO0O000OO0OO0) + 1}个账号------------")#line:9
            O000OOO00O00OOOOO =CityEarth (O0O0OO0O000OO0OO0 )#line:10
            if O000OOO00O00OOOOO .base_info ():#line:12
                O000OOO00O00OOOOO .game_map ()#line:16
                O000OOO00O00OOOOO .friends_invitation ()#line:18
                O000OOO00O00OOOOO .add_clover ()#line:20
                O000OOO00O00OOOOO .energy ()#line:22
                O000OOO00O00OOOOO .synthetic ()#line:24
                O000OOO00O00OOOOO .propsraffle ()#line:26
                O000OOO00O00OOOOO .crops_illustrated ()#line:28
                O000OOO00O00OOOOO .give_gold ()#line:30
            else :#line:31
                print ('token失效')#line:32
            time .sleep (time_xx )#line:34
    except Exception as O00OOOOO000O000OO :#line:35
        print (O00OOOOO000O000OO )#line:36
def sign (O0000OO00O00OO00O ):#line:38
    OOO0O0000OOO0OO0O =hashlib .md5 (O0000OO00O00OO00O .encode ()).hexdigest ()#line:39
    O0O0OO0O00OO0000O ="scsc%^&*"+OOO0O0000OOO0OO0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:40
    O0O0O000000000000 =hashlib .md5 (O0O0OO0O00OO0000O .encode ()).hexdigest ()#line:41
    return O0O0O000000000000 #line:42
def timi_new ():#line:44
    return str (int (time .time ()*1000 ))#line:45
class CityEarth :#line:48
    def __init__ (O000OO00O0O00OO0O ,O0OOO0O000OOO00OO ):#line:50
        try :#line:51
            O000OO00O0O00OO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:52
            O000OO00O0O00OO0O .token =O0OOO0O000OOO00OO .split ('&')[0 ]#line:53
            O000OO00O0O00OO0O .innerId =O0OOO0O000OOO00OO .split ('&')[1 ]#line:54
            O000OO00O0O00OO0O .doneeNo =O0OOO0O000OOO00OO .split ('&')[2 ]#line:55
        except :#line:56
            print ('变量格式错误')#line:57
    def base_info (O0O00O0000000O00O ):#line:60
        try :#line:61
            O00O0O0O0O0OOO000 =f'__{timi_new()}'#line:62
            OO0000O0O0OOO000O ={'authorization':O0O00O0000000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O0O0OOO000 ),'signstring':O00O0O0O0O0OOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:71
            O00OOOOO00OO0OOOO =requests .request ('get',f'{host}/user',headers =OO0000O0O0OOO000O ).json ()#line:72
            if 'status'in O00OOOOO00OO0OOOO :#line:74
                if O00OOOOO00OO0OOOO ['status']==200 :#line:75
                    O0OO000OOOOO000OO =O00OOOOO00OO0OOOO ['data']['nickname']#line:76
                    OOOO00O0O00000OO0 =O00OOOOO00OO0OOOO ['data']['inner_id']#line:77
                    OO0OOO0OOOO00O000 =O00OOOOO00OO0OOOO ['data']['assets']['gold']#line:78
                    OOOOO0000O0O00000 =O00OOOOO00OO0OOOO ['data']['level']#line:79
                    print (f'【账号信息】:昵称:{O0OO000OOOOO000OO}丨ID:{str(OOOO00O0O00000OO0)[:3] + "**"+ str(OOOO00O0O00000OO0)[5:]}丨等级:{OOOOO0000O0O00000}丨种子:{str(OO0OOO0OOOO00O000).split(".")[0]}')#line:80
                if O00OOOOO00OO0OOOO ['status']==401 :#line:81
                    return False #line:82
                if O00OOOOO00OO0OOOO ['status']==500 :#line:83
                    return False #line:84
            return True #line:85
        except Exception as OOO0O00OOO0OOO0OO :#line:86
            print (OOO0O00OOO0OOO0OO )#line:87
    def game_map (OO0OOOOO00OOO00OO ):#line:90
        O0O000OO0O0OOOOOO =f'__{timi_new()}'#line:91
        O0O0OO0O000OOO00O ={'authorization':OO0OOOOO00OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OO0O0OOOOOO ),'signstring':O0O000OO0O0OOOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:100
        OOOO0OOOOO0OO0000 =requests .request ('get',f'{host}/game/map',headers =O0O0OO0O000OOO00O ).json ()#line:101
        if 'status'in OOOO0OOOOO0OO0000 :#line:103
            if OOOO0OOOOO0OO0000 ['status']==200 :#line:104
                for OO000O00O0O000OOO in OOOO0OOOOO0OO0000 ['data']['list'][0 ]['crops']:#line:105
                    O00OO00OOO0000000 =OO000O00O0O000OOO ['level']#line:107
                    if O00OO00OOO0000000 ==41 :#line:108
                        OOO0OOOOOO00OOO00 =OO000O00O0O000OOO ['crop_name']#line:109
                        O0OOOOO0OO0OOOOO0 =OO000O00O0O000OOO ['count']#line:110
                        if O0OOOOO0OO0OOOOO0 >0 :#line:111
                            print (f'【农业资产】:{OOO0OOOOOO00OOO00}丨数量:{O0OOOOO0OO0OOOOO0}')#line:112
    def give_gold (OOO0O00000OO0O0O0 ):#line:117
        OOOOO00O000O0O0OO =f'__{timi_new()}'#line:118
        O0OOOOO00O00O0000 ={'authorization':OOO0O00000OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O000O0O0OO ),'signstring':OOOOO00O000O0O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
        OO0OO0000O00O00O0 =requests .request ('get',f'{host}/user',headers =O0OOOOO00O00O0000 ).json ()#line:128
        if 'status'in OO0OO0000O00O00O0 :#line:129
            if OO0OO0000O00O00O0 ['status']==200 :#line:130
                if float (OOO0O00000OO0O0O0 .doneeNo )!=0 :#line:131
                    O0OOO0OO0000OOO00 =OO0OO0000O00O00O0 ['data']['assets']['gold']#line:132
                    if float (O0OOO0OO0000OOO00 )>2 :#line:133
                        OOO000OOO000O00O0 =int (float (O0OOO0OO0000OOO00 )/1.1 )#line:134
                        OOOOO00O000O0O0OO =f'_doneeNo={OOO0O00000OO0O0O0.doneeNo}&quantity={OOO000OOO000O00O0}_{timi_new()}'#line:135
                        O0OOOOO00O00O0000 ={'authorization':OOO0O00000OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O000O0O0OO ),'signstring':OOOOO00O000O0O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:144
                        OO0OOOOOO0O000000 ={"quantity":OOO000OOO000O00O0 ,"doneeNo":OOO0O00000OO0O0O0 .doneeNo }#line:148
                        OOO0OO000OOOO0000 =requests .request ('post',f'{host}/finance/give-gold',headers =O0OOOOO00O00O0000 ,data =OO0OOOOOO0O000000 ).json ()#line:149
                        if 'status'in OOO0OO000OOOO0000 :#line:151
                            if OOO0OO000OOOO0000 ['status']==200 :#line:152
                                if OOO0OO000OOOO0000 ['data']:#line:153
                                    print (f'【赠送种子】:赠送{OOO000OOO000O00O0}种子给{OOO0O00000OO0O0O0.doneeNo}成功')#line:154
                else :#line:155
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:156
    def winning_rewards (OOOO00O0O00O00000 ):#line:158
        O00OO000O000OOOO0 =f'__{timi_new()}'#line:159
        OO0O0OO00OOOO00OO ={'authorization':OOOO00O0O00O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000O000OOOO0 ),'signstring':O00OO000O000OOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:168
        O000O000OO0000000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO0O0OO00OOOO00OO ).json ()#line:169
        if 'status'in O000O000OO0000000 :#line:171
            if O000O000OO0000000 ['status']==200 :#line:172
                if O000O000OO0000000 ['data']['amount']:#line:173
                    O00000OOOOO0O0OO0 =O000O000OO0000000 ['data']['amount']['gold']#line:174
                    return O00000OOOOO0O0OO0 #line:175
                else :#line:176
                    return 0 #line:177
    def certification (O0OO0000OO000O0OO ):#line:179
        OO0O0OO0O0OOO00OO =f'__{timi_new()}'#line:180
        OO0000O0O0O0000O0 ={'authorization':O0OO0000OO000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO0O0OOO00OO ),'signstring':OO0O0OO0O0OOO00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:189
        O0OO0O0000O0000O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0000O0O0O0000O0 ).json ()#line:190
        if 'status'in O0OO0O0000O0000O0 :#line:192
            if O0OO0O0000O0000O0 ['status']==200 :#line:193
                if O0OO0O0000O0000O0 ['data']['result']:#line:194
                    O00OOO00O00OO0OO0 =O0OO0O0000O0000O0 ['data']['nick_name']#line:195
                    return O00OOO00O00OO0OO0 #line:196
                else :#line:197
                    return '未实名'#line:198
    def crops_illustrated (OO00O0O0OOO0000O0 ):#line:201
        OO000000000O0O000 =f'__{timi_new()}'#line:202
        O00OOOO0O00O00000 ={'authorization':OO00O0O0OOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000000O0O000 ),'signstring':OO000000000O0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:211
        OOOO000O0O0O000O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00OOOO0O00O00000 ).json ()#line:212
        if 'status'in OOOO000O0O0O000O0 :#line:214
            if OOOO000O0O0O000O0 ['status']==200 :#line:215
                OOOOO000OO00O0000 =OOOO000O0O0O000O0 ['data'][0 ]['crops']#line:216
                for O00000O0O00OO0OO0 in OOOOO000OO00O0000 :#line:217
                    if O00000O0O00OO0OO0 ['ill_clover_award']:#line:218
                        if float (O00000O0O00OO0OO0 ['ill_clover_award'])>1 :#line:219
                            if O00000O0O00OO0OO0 ['is_finish']:#line:220
                                if not O00000O0O00OO0OO0 ['is_getit']:#line:221
                                    OO000000000O0O000 =f'_award_level={O00000O0O00OO0OO0["level"]}_{timi_new()}'#line:222
                                    O00OOOO0O00O00000 ={'authorization':OO00O0O0OOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000000O0O000 ),'signstring':OO000000000O0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:231
                                    OOOO00OOOOO000O00 ={"award_level":O00000O0O00OO0OO0 ['level']}#line:232
                                    OOOOO000O0O00OO0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00OOOO0O00O00000 ,json =OOOO00OOOOO000O00 ).json ()#line:233
                                    if 'status'in OOOOO000O0O00OO0O :#line:234
                                        if OOOOO000O0O00OO0O ['status']==200 :#line:235
                                            O0OO0O00000OOO0OO =OOOOO000O0O00OO0O ['data']['ill_clover_award']#line:236
                                            print (f'【图鉴奖励】:领取{O00000O0O00OO0OO0["crop_name"]}成就丨奖励{O0OO0O00000OOO0OO}叶子成功')#line:237
                                        if OOOOO000O0O00OO0O ['status']==500 :#line:238
                                            print (f'【图鉴奖励】:{OOOOO000O0O00OO0O["message"]}')#line:239
    def watched_ad (O0OOO000000O0OOO0 ):#line:242
        O00OOO00OOOOO0O0O =f'__{timi_new()}'#line:243
        OO0000O0O00OOO0O0 ={'authorization':O0OOO000000O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO00OOOOO0O0O ),'signstring':O00OOO00OOOOO0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
        O0O00OOO0O00OOOOO =requests .request ('post',f'{host}/game/watched-ad',headers =OO0000O0O00OOO0O0 ).json ()#line:253
        print (O0O00OOO0O00OOOOO )#line:254
    def user_ad (O0O0OOOO0000OOOOO ):#line:259
        O0O0OOOOOO000O0O0 =f'__{timi_new()}'#line:260
        O0000O00O0O0O0O0O ={'authorization':O0O0OOOO0000OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOOOO000O0O0 ),'signstring':O0O0OOOOOO000O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:269
        OO00000OO0O0OOO00 =requests .request ('get',f'{host}/user/ad',headers =O0000O00O0O0O0O0O ).json ()#line:270
        if 'status'in OO00000OO0O0OOO00 :#line:272
            if OO00000OO0O0OOO00 ['status']==200 :#line:273
                OOO0OOO0OO0000O00 =OO00000OO0O0OOO00 ['data']['max_time']#line:274
                OO000O0OOO0OO0000 =OO00000OO0O0OOO00 ['data']['watch_time']#line:275
                O000O0O0000O0OOO0 =OO00000OO0O0OOO00 ['data']['added_time']#line:276
                print (f'【获取种子】:获取种子剩余{O000O0O0000O0OOO0 + OOO0OOO0OO0000O00 - OO000O0OOO0OO0000}次丨好友提供:{O000O0O0000O0OOO0}次')#line:277
                if O000O0O0000O0OOO0 +OOO0OOO0OO0000O00 -OO000O0OOO0OO0000 >0 :#line:278
                    time .sleep (random .randint (16 ,19 ))#line:279
                    O0O0000000OO00OO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0000O00O0O0O0O0O ).json ()#line:280
                    if 'status'in O0O0000000OO00OO0 :#line:282
                        if O0O0000000OO00OO0 ['status']==200 :#line:283
                            OO0000OO00O00O0OO =O0O0000000OO00OO0 ['data']['silver']#line:284
                            print (f'【获取种子】:获得种子:{OO0000OO00O00O0OO}')#line:285
                            return True #line:286
                        if O0O0000000OO00OO0 ['status']==500 :#line:287
                            O0O00O000OO00OO00 =O0O0000000OO00OO0 ['message']#line:288
                            print (f'【获取种子】:{O0O00O000OO00OO00}')#line:289
                            return False #line:290
    def synthetic (O0O0000OO00OO0O00 ):#line:293
        global id ,g #line:294
        try :#line:295
            OO0OO0000OO00OO00 =leves #line:296
            while True :#line:297
                OOO00000O0OOOOOO0 =f'__{timi_new()}'#line:298
                OOOO00OOO0OO0OOO0 ={'authorization':O0O0000OO00OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00000O0OOOOOO0 ),'signstring':OOO00000O0OOOOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:307
                OOO00O0OOOOOOOOOO =requests .request ('get',f'{host}/game/getAllData',headers =OOOO00OOO0OO0OOO0 ).json ()#line:308
                if 'status'in OOO00O0OOOOOOOOOO :#line:310
                    if OOO00O0OOOOOOOOOO ['status']==200 :#line:311
                        O0O00000000OO000O =OOO00O0OOOOOOOOOO ['data']['cropList']#line:312
                        OO00O0OOOO0OOOOO0 =OOO00O0OOOOOOOOOO ['data']['gameCoreDataDBid']#line:313
                        OOO0000OOO0000OO0 =0 #line:314
                        for OOO0OOO000OOOOOO0 in O0O00000000OO000O :#line:315
                            if not OOO0OOO000OOOOOO0 :#line:316
                                O0O0O0OO000O0O000 =f'_crop_id={OO00O0OOOO0OOOOO0}&site={OOO0000OOO0000OO0}_{O0O0000OO00OO0O00.time}'#line:317
                                OO0O0OO0OOOOOO0O0 ={'authorization':O0O0000OO00OO0O00 .token ,'timestamp':O0O0000OO00OO0O00 .time ,'sign':sign (O0O0O0OO000O0O000 ),'signstring':O0O0O0OO000O0O000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:326
                                O000OO0OOO0OO0OOO ={"site":OOO0000OOO0000OO0 ,"crop_id":OO00O0OOOO0OOOOO0 }#line:327
                                O0OO00O0O0OOO00O0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O0OO0OOOOOO0O0 ,data =O000OO0OOO0OO0OOO ).json ()#line:328
                                time .sleep (random .randint (1 ,3 )/10 )#line:330
                                if 'status'in O0OO00O0O0OOO00O0 :#line:331
                                    if O0OO00O0O0OOO00O0 ['status']==200 :#line:332
                                        if O0OO00O0O0OOO00O0 ['message']=='种子数量不足':#line:333
                                            OO0OO0000OO00OO00 =O0O0000OO00OO0O00 .level_new ()#line:334
                                            print (f'【种植合成】:{O0OO00O0O0OOO00O0["message"]}')#line:335
                                            if not O0O0000OO00OO0O00 .user_ad ():#line:336
                                                return False #line:337
                                        print (f'【种植合成】:种植农作物,位置{OOO0000OOO0000OO0}')#line:338
                                    if O0OO00O0O0OOO00O0 ['status']==500 :#line:339
                                        print (f'【种植合成】:{O0OO00O0O0OOO00O0["message"]}')#line:340
                                        return False #line:341
                            OOO0000OOO0000OO0 +=1 #line:342
                        O00OO00O0O00O0O0O =requests .request ('get',f'{host}/game/getAllData',headers =OOOO00OOO0OO0OOO0 ).json ()#line:343
                        OOOO0O000OOOOOO00 =O00OO00O0O00O0O0O ['data']['cropList']#line:344
                        O0OO0OOOO0OOO00OO =False #line:345
                        for OOO0OOO000OOOOOO0 in range (12 ):#line:346
                            id =OOOO0O000OOOOOO00 [OOO0OOO000OOOOOO0 ]['level']#line:347
                            if float (OO0OO0000OO00OO00 )-float (id )>9 :#line:348
                                OOOO0OOO000O000O0 =f'_site={OOO0OOO000OOOOOO0}_{timi_new()}'#line:349
                                O0OO00O00O00O0000 ={'accept':'application/json, text/plain, */*','authorization':O0O0000OO00OO0O00 .token ,'timestamp':timi_new (),'sign':sign (OOOO0OOO000O000O0 ),'signstring':OOOO0OOO000O000O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:359
                                O0000OOO00O0OOO0O ={"site":OOO0OOO000OOOOOO0 }#line:360
                                OO00O00OOOOOOO000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OO00O00O00O0000 ,data =O0000OOO00O0OOO0O ).json ()#line:361
                                if 'status'in OO00O00OOOOOOO000 :#line:362
                                    if OO00O00OOOOOOO000 ['status']==200 :#line:363
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:364
                            if id !=0 :#line:365
                                for O0000O0O00O0OO000 in range (11 ):#line:366
                                    O00O0O00000OO00OO =O0000O0O00O0OO000 +1 #line:367
                                    g =OOOO0O000OOOOOO00 [O00O0O00000OO00OO ]['level']#line:368
                                    if id ==g :#line:369
                                        O00OOOOOO000O00OO =O0000O0O00O0OO000 +2 #line:370
                                        if O00OOOOOO000O00OO ==OOO0OOO000OOOOOO0 +1 :#line:371
                                            pass #line:372
                                        else :#line:373
                                            O000O000O00O0OO0O =OOO0OOO000OOOOOO0 +1 #line:374
                                            time .sleep (random .randint (1 ,3 )/10 )#line:376
                                            OO00OOO0O0OO0O000 =f'_site={O000O000O00O0OO0O-1}&targetSite={O00OOOOOO000O00OO-1}_{timi_new()}'#line:377
                                            OO00O0O0OO0OOO0O0 ={'accept':'application/json, text/plain, */*','authorization':O0O0000OO00OO0O00 .token ,'timestamp':timi_new (),'sign':sign (OO00OOO0O0OO0O000 ),'signstring':OO00OOO0O0OO0O000 ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:392
                                            OOOOO0O0OO00O00OO ={"site":int (O000O000O00O0OO0O -1 ),"targetSite":int (O00OOOOOO000O00OO -1 )}#line:393
                                            O00O00O0000O000O0 =requests .request ('post',f'{host}/game/crops/move',headers =OO00O0O0OO0OOO0O0 ,json =OOOOO0O0OO00O00OO ).json ()#line:394
                                            if 'status'in O00O00O0000O000O0 :#line:395
                                                if O00O00O0000O000O0 ['status']==200 :#line:396
                                                    pass #line:397
                                                    print ('交换位置')#line:398
                                            print ('【种植合成】:',O000O000O00O0OO0O ,O00OOOOOO000O00OO ,'合成成功')#line:399
                                            O0OO0OOOO0OOO00OO =True #line:400
                                    if O0OO0OOOO0OOO00OO :#line:401
                                        break #line:402
                                if O0OO0OOOO0OOO00OO :#line:403
                                    break #line:404
        except Exception as O00O0O0O0O000OO0O :#line:405
            O0O0000OO00OO0O00 .synthetic ()#line:406
    def level_new (O0000OO00000OO000 ):#line:409
        try :#line:410
            OOOOOOOO0O00O00OO =f'__{timi_new()}'#line:411
            O000OOO000O0O0O00 ={'authorization':O0000OO00000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO0O00O00OO ),'signstring':OOOOOOOO0O00O00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:420
            OOO0O0OOO000O00O0 =requests .request ('get',f'{host}/user',headers =O000OOO000O0O0O00 ).json ()#line:421
            if 'status'in OOO0O0OOO000O00O0 :#line:422
                if OOO0O0OOO000O00O0 ['status']==200 :#line:423
                    return float (OOO0O0OOO000O00O0 ['data']['level'])#line:424
        except Exception as OOO00OOOO00O00O0O :#line:425
            print (OOO00OOOO00O00O0O )#line:426
    def propsraffle (O000O0O000O0OOO00 ):#line:430
        try :#line:431
            while True :#line:432
                OOO0000OO0O0OO0OO =f'__{timi_new()}'#line:433
                OOOO0000O00O000O0 ={'authorization':O000O0O000O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OO0O0OO0OO ),'signstring':OOO0000OO0O0OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:442
                O0000O0O0OO000OOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOO0000O00O000O0 ).json ()#line:443
                if 'status'in O0000O0O0OO000OOO :#line:445
                    if O0000O0O0OO000OOO ['status']==200 :#line:446
                        O0O00O000O00O00O0 =O0000O0O0OO000OOO ['data']['rows']#line:447
                        OOOO0O0O000000000 =O0000O0O0OO000OOO ['data']['vstate']#line:448
                        if O0O00O000O00O00O0 ==5 or O0O00O000O00O00O0 ==6 or O0O00O000O00O00O0 ==7 :#line:449
                            OO00O00O0OOO0OOOO =O0000O0O0OO000OOO ['data']['silver']#line:450
                            print (f'【转盘抽奖】:获得种子:{OO00O00O0OOO0OOOO}')#line:451
                        if O0O00O000O00O00O0 ==1 or O0O00O000O00O00O0 ==2 or O0O00O000O00O00O0 ==3 :#line:452
                            O00OO00O0O00OO00O =O0000O0O0OO000OOO ['data']['clover']#line:453
                            print (f'【转盘抽奖】:获得三叶草:{O00OO00O0O00OO00O}')#line:454
                        if O0O00O000O00O00O0 ==4 or O0O00O000O00O00O0 ==8 :#line:455
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:456
                        if O0O00O000O00O00O0 =='抽奖次数已用完':#line:460
                            if OOOO0O0O000000000 :#line:461
                                OO0000O0000OO000O =random .randint (160 ,190 )/10 #line:462
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{OO0000O0000OO000O}秒获取抽奖机会')#line:463
                                time .sleep (OO0000O0000OO000O )#line:464
                                O0000000000O0OO00 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OOOO0000O00O000O0 ).json ()#line:465
                                if 'status'in O0000000000O0OO00 :#line:467
                                    if O0000000000O0OO00 ['status']==200 :#line:468
                                        print (f'【转盘抽奖】:{O0000000000O0OO00["message"]}')#line:469
                                    if O0000000000O0OO00 ['status']==500 :#line:470
                                        print (f'【转盘抽奖】:{O0000000000O0OO00["message"]}')#line:471
                                        break #line:472
                                time .sleep (random .randint (10 ,15 )/10 )#line:473
                            else :#line:474
                                break #line:475
                time .sleep (random .randint (8 ,15 )/10 )#line:476
        except Exception as O0OOOOOO0OO0O0OOO :#line:477
            print (O0OOOOOO0OO0O0OOO )#line:478
    def friends_invitation (O00O0O0OOOOO0000O ):#line:481
        try :#line:482
            OO0OOO0O0OO0OOO00 =f'__{timi_new()}'#line:483
            OO0OOOO000O0O0OOO ={'authorization':O00O0O0OOOOO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O0OO0OOO00 ),'signstring':OO0OOO0O0OO0OOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:492
            OO00OOOOO0O00OOO0 =requests .request ('get',f'{host}/friends',headers =OO0OOOO000O0O0OOO ).json ()#line:493
            if 'status'in OO00OOOOO0O00OOO0 :#line:494
                if OO00OOOOO0O00OOO0 ['status']==200 :#line:495
                    O0OOOOOOO0OO0O00O =OO00OOOOO0O00OOO0 ['data']['myInviteter']#line:496
                    if O0OOOOOOO0OO0O00O :#line:497
                        OOOO0OOO00000O00O =O0OOOOOOO0OO0O00O ['user']['nickname']#line:498
                        OOO0OO0O0O0O0OO00 =O00O0O0OOOOO0000O .certification ()#line:499
                        print (f'【绑邀请码】:我的邀请人:{OOOO0OOO00000O00O}丨实名:{OOO0OO0O0O0O0OO00}')#line:500
                    else :#line:501
                        if O00O0O0OOOOO0000O .innerId !='0':#line:502
                            OO0OOO0O0OO0OOO00 =f'_innerId={O00O0O0OOOOO0000O.innerId}_{timi_new()}'#line:503
                            OO0OOOO000O0O0OOO ={'authorization':O00O0O0OOOOO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O0OO0OOO00 ),'signstring':OO0OOO0O0OO0OOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
                            OOOOOOO0OOO0OO000 ={"innerId":O00O0O0OOOOO0000O .innerId }#line:513
                            O0O00OO000O0O000O =requests .request ('post',f'{host}/friends/my-invitation',headers =OO0OOOO000O0O0OOO ,data =OOOOOOO0OOO0OO000 ).json ()#line:514
                            if 'status'in O0O00OO000O0O000O :#line:515
                                if O0O00OO000O0O000O ['status']==200 :#line:516
                                    print (f'【绑邀请码】:{O00O0O0OOOOO0000O.innerId}{O0O00OO000O0O000O["message"]}')#line:517
                        else :#line:518
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:519
        except Exception as O0O00000O0O0O0O0O :#line:520
            print (O0O00000O0O0O0O0O )#line:521
    def add_clover (O00000O00O0O0O00O ):#line:525
        try :#line:526
            O0OOO0000OO00O0O0 =f'__{timi_new()}'#line:527
            OO000OO0OOOOO000O ={'authorization':O00000O00O0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000OO00O0O0 ),'signstring':O0OOO0000OO00O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:536
            OO00OOO0O0OO0OO0O =requests .request ('get',f'{host}/assets/clovers',headers =OO000OO0OOOOO000O ).json ()#line:537
            if 'status'in OO00OOO0O0OO0OO0O :#line:539
                if OO00OOO0O0OO0OO0O ['status']==200 :#line:540
                    OOOO0OO0O0OO000O0 =OO00OOO0O0OO0OO0O ['data']['clover']#line:541
                    OOO0OOOOOO000O0OO =OO00OOO0O0OO0OO0O ['data']['used_clover']#line:542
                    O000000OOO00O00OO =float (OOOO0OO0O0OO000O0 )-float (OOO0OOOOOO000O0OO )#line:543
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OOO0OOOOOO000O0OO}')#line:544
                    if O000000OOO00O00OO >1 :#line:545
                        O0OOO0000OO00O0O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O000000OOO00O00OO)}_{timi_new()}'#line:546
                        OO000OO0OOOOO000O ={'authorization':O00000O00O0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000OO00O0O0 ),'signstring':O0OOO0000OO00O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:555
                        OOO000OOOO000000O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O000000OOO00O00OO )}#line:556
                        O0OO00000OOO0OOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OO000OO0OOOOO000O ,data =OOO000OOOO000000O ).json ()#line:557
                        if 'status'in O0OO00000OOO0OOOO :#line:559
                            if O0OO00000OOO0OOOO ['status']==200 :#line:560
                                print (f'【参与抽奖】:添加三叶草:{O0OO00000OOO0OOOO["data"]}丨数量:{O000000OOO00O00OO}')#line:561
            OOOO0OO00O0O0O0O0 =requests .request ('get',f'{host}/lottery',headers =OO000OO0OOOOO000O ).json ()#line:562
            OO0O000O0O0O0O000 =O00000O00O0O0O00O .winning_rewards ()#line:564
            if 'status'in OOOO0OO00O0O0O0O0 :#line:565
                if OOOO0OO00O0O0O0O0 ['status']==200 :#line:566
                    OOO0O0OOOO0OO000O =OOOO0OO00O0O0O0O0 ['data'][0 ]['day_get_gold_quantity']#line:567
                    print (f'【参与抽奖】:预计每天中{OOO0O0OOOO0OO000O[:6]}种子丨好友收益:{OO0O000O0O0O0O000}')#line:568
        except Exception as O0OO0O0O00OO0OOO0 :#line:569
            print (O0OO0O0O00OO0OOO0 )#line:570
    def energy (O0O000OO00OO000O0 ):#line:573
        O000O000OOO00000O =f'__{timi_new()}'#line:574
        OO0OOOOOOOOO00O0O ={'authorization':O0O000OO00OO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000OOO00000O ),'signstring':O000O000OOO00000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
        O0OO0OOO0000O000O =requests .request ('get',f'{host}/energy/general',headers =OO0OOOOOOOOO00O0O ).json ()#line:584
        if 'status'in O0OO0OOO0000O000O :#line:586
            if O0OO0OOO0000O000O ['status']==200 :#line:587
                OO00OO0O0OO0OOO0O =O0OO0OOO0000O000O ['data']['ordinary_water_consumptions']#line:588
                if float (OO00OO0O0OO0OOO0O )<80 :#line:589
                    OOOO00OOO0O00O0O0 =99 -float (OO00OO0O0OO0OOO0O )#line:590
                    OO0O000OO00OOO000 ={"fertilizer":str (OOOO00OOO0O00O0O0 ).split ('.')[0 ]}#line:591
                    O00OO00O0OOO000OO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0OOOOOOOOO00O0O ,data =OO0O000OO00OOO000 ).json ()#line:592
                    if 'status'in O00OO00O0OOO000OO :#line:594
                        if O00OO00O0OOO000OO ['status']==200 :#line:595
                            print (f'【购买肥料】:{O00OO00O0OOO000OO["message"]}')#line:596
                OO0OO0OOO00000O0O =O0OO0OOO0000O000O ['data']['ordinary_water_consumptions']#line:597
                if float (OO0OO0OOO00000O0O )<800 :#line:598
                    O000OO0O00OO0OO00 =999 -float (OO0OO0OOO00000O0O )#line:599
                    O00O00000O0O00000 ={"water":str (O000OO0O00OO0OO00 ).split ('.')[0 ]}#line:600
                    OO00O000OO00OOOOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0OOOOOOOOO00O0O ,data =O00O00000O0O00000 ).json ()#line:601
                    if 'status'in OO00O000OO00OOOOO :#line:602
                        if OO00O000OO00OOOOO ['status']==200 :#line:603
                            print (f'【购买水滴】:{OO00O000OO00OOOOO["message"]}')#line:604
def version_of_the_validation ():#line:610
    return str ((66 -56 )/10 )#line:611
def gitee_validation ():#line:613
    try :#line:614
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:615
    except Exception as OO0000000000O00O0 :#line:616
        sys .exit (0 )#line:617
def update_the_validation ():#line:623
    try :#line:624
        OOOOO00000OOO00OO =gitee_validation ()#line:625
        if version_of_the_validation ()<OOOOO00000OOO00OO ['CityEarth']['edition']:#line:626
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOO00000OOO00OO["CityEarth"]["edition"]}   ❌')#line:627
            print (f'更新内容=>>{OOOOO00000OOO00OO["CityEarth"]["content"]}   👍')#line:628
        else :#line:629
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOO00000OOO00OO["CityEarth"]["edition"]}   ✅')#line:630
            print (f'更新内容=>> {OOOOO00000OOO00OO["CityEarth"]["content"]}   👍')#line:631
    except Exception as OO00OO0OO000O00OO :#line:632
        print (OO00OO0OO000O00OO )#line:633
def os_qinglong ():#line:636
    if application in os .environ :#line:637
        OOO0O00O000000O0O =os .environ [application ].split ('\n')#line:638
        if len (OOO0O00O000000O0O )>0 :#line:639
            return OOO0O00O000000O0O #line:640
        else :#line:641
            print (f"{application}变量未启用")#line:642
            print ('脚本退出')#line:643
            sys .exit (1 )#line:644
    else :#line:645
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:646
        return os_built ()#line:647
def os_built ():#line:650
    if token :#line:651
        O000OO0O00000O0OO =token .split ('\n')#line:652
        if len (O000OO0O00000O0OO )>0 :#line:653
            return O000OO0O00000O0OO #line:654
    else :#line:655
        print (f"内置变量为空")#line:656
        print ('脚本结束')#line:657
        sys .exit (0 )#line:658
if __name__ =='__main__':#line:661
    start ()#line:662
