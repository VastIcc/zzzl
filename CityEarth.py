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
def start ():#line:3
    try :#line:4
        update_the_validation ()#line:5
        OOO0000O00O00OO00 =os_qinglong ()#line:6
        print (f"==========共找到{len(OOO0000O00O00OO00)}个账号==========")#line:7
        for O0000O00O00OOOO0O in OOO0000O00O00OO00 :#line:8
            print (f"------------正在执行第{OOO0000O00O00OO00.index(O0000O00O00OOOO0O) + 1}个账号------------")#line:9
            OO00O00O00O0O00OO =CityEarth (O0000O00O00OOOO0O )#line:10
            if OO00O00O00O0O00OO .base_info ():#line:12
                OO00O00O00O0O00OO .game_map ()#line:16
                OO00O00O00O0O00OO .friends_invitation ()#line:18
                OO00O00O00O0O00OO .add_clover ()#line:20
                OO00O00O00O0O00OO .energy ()#line:22
                OO00O00O00O0O00OO .synthetic ()#line:24
                OO00O00O00O0O00OO .propsraffle ()#line:26
                OO00O00O00O0O00OO .crops_illustrated ()#line:28
                OO00O00O00O0O00OO .give_gold ()#line:30
            else :#line:31
                print ('token失效')#line:32
            time .sleep (time_xx )#line:34
    except Exception as O0OOOOO0O000OOO00 :#line:35
        print (O0OOOOO0O000OOO00 )#line:36
def sign (O00O00OOOO00O000O ):#line:38
    OO00OOOOOOO00O0O0 =hashlib .md5 (O00O00OOOO00O000O .encode ()).hexdigest ()#line:39
    O0OOO000O0O0O0OO0 ="scsc%^&*"+OO00OOOOOOO00O0O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:40
    O00OO000OO00OOO00 =hashlib .md5 (O0OOO000O0O0O0OO0 .encode ()).hexdigest ()#line:41
    return O00OO000OO00OOO00 #line:42
def timi_new ():#line:44
    return str (int (time .time ()*1000 ))#line:45
class CityEarth :#line:48
    def __init__ (O000O00000O0000O0 ,OO0000000O0O000O0 ):#line:50
        try :#line:51
            O000O00000O0000O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:52
            O000O00000O0000O0 .token =OO0000000O0O000O0 .split ('&')[0 ]#line:53
            O000O00000O0000O0 .innerId =OO0000000O0O000O0 .split ('&')[1 ]#line:54
            O000O00000O0000O0 .doneeNo =OO0000000O0O000O0 .split ('&')[2 ]#line:55
        except :#line:56
            print ('变量格式错误')#line:57
    def base_info (OO00OOOOO000O00O0 ):#line:60
        try :#line:61
            OO0OOO0O0OOO00O00 =f'__{timi_new()}'#line:62
            O000000OO0000OO00 ={'authorization':OO00OOOOO000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O0OOO00O00 ),'signstring':OO0OOO0O0OOO00O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:71
            OOO0OO0OOOOO0OOO0 =requests .request ('get',f'{host}/user',headers =O000000OO0000OO00 ).json ()#line:72
            if 'status'in OOO0OO0OOOOO0OOO0 :#line:74
                if OOO0OO0OOOOO0OOO0 ['status']==200 :#line:75
                    O00OOOOOOOO0O0O00 =OOO0OO0OOOOO0OOO0 ['data']['nickname']#line:76
                    OO0O0O00OOOO00O0O =OOO0OO0OOOOO0OOO0 ['data']['inner_id']#line:77
                    O0O0O0O00O0O00O0O =OOO0OO0OOOOO0OOO0 ['data']['assets']['gold']#line:78
                    OOOOOO00O000O00OO =OOO0OO0OOOOO0OOO0 ['data']['level']#line:79
                    print (f'【账号信息】:昵称:{O00OOOOOOOO0O0O00}丨ID:{str(OO0O0O00OOOO00O0O)[:3] + "**"+ str(OO0O0O00OOOO00O0O)[5:]}丨等级:{OOOOOO00O000O00OO}丨种子:{str(O0O0O0O00O0O00O0O).split(".")[0]}')#line:80
                if OOO0OO0OOOOO0OOO0 ['status']==401 :#line:81
                    return False #line:82
                if OOO0OO0OOOOO0OOO0 ['status']==500 :#line:83
                    return False #line:84
            return True #line:85
        except Exception as O00OOOOOOO00OO0O0 :#line:86
            print (O00OOOOOOO00OO0O0 )#line:87
    def game_map (O0OO000O00000OOO0 ):#line:90
        OO0O000OO0O0000O0 =f'__{timi_new()}'#line:91
        OOOOO00OO0000O0OO ={'authorization':O0OO000O00000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000OO0O0000O0 ),'signstring':OO0O000OO0O0000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:100
        OOOO000O0OOO00000 =requests .request ('get',f'{host}/game/map',headers =OOOOO00OO0000O0OO ).json ()#line:101
        if 'status'in OOOO000O0OOO00000 :#line:103
            if OOOO000O0OOO00000 ['status']==200 :#line:104
                for OO0O00OOO000O0OOO in OOOO000O0OOO00000 ['data']['list'][0 ]['crops']:#line:105
                    OO0OO0O0O00O0O0OO =OO0O00OOO000O0OOO ['level']#line:107
                    if OO0OO0O0O00O0O0OO ==41 :#line:108
                        OOO00O000000O0000 =OO0O00OOO000O0OOO ['crop_name']#line:109
                        O0OO00O0000O0O00O =OO0O00OOO000O0OOO ['count']#line:110
                        if O0OO00O0000O0O00O >0 :#line:111
                            print (f'【农业资产】:{OOO00O000000O0000}丨数量:{O0OO00O0000O0O00O}')#line:112
    def give_gold (O000000O00OO0OOO0 ):#line:117
        O000O000OO000O0OO =f'__{timi_new()}'#line:118
        O00OOO00O0O000000 ={'authorization':O000000O00OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000OO000O0OO ),'signstring':O000O000OO000O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
        OOO0O0OO00OOO0OO0 =requests .request ('get',f'{host}/user',headers =O00OOO00O0O000000 ).json ()#line:128
        if 'status'in OOO0O0OO00OOO0OO0 :#line:129
            if OOO0O0OO00OOO0OO0 ['status']==200 :#line:130
                if float (O000000O00OO0OOO0 .doneeNo )!=0 :#line:131
                    O0000O00OO0OOOOO0 =OOO0O0OO00OOO0OO0 ['data']['assets']['gold']#line:132
                    if float (O0000O00OO0OOOOO0 )>2 :#line:133
                        O0OOOO0O00OOO0OO0 =int (float (O0000O00OO0OOOOO0 )/1.1 )#line:134
                        O000O000OO000O0OO =f'_doneeNo={O000000O00OO0OOO0.doneeNo}&quantity={O0OOOO0O00OOO0OO0}_{timi_new()}'#line:135
                        O00OOO00O0O000000 ={'authorization':O000000O00OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000OO000O0OO ),'signstring':O000O000OO000O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:144
                        OOO0O00OOO000O0O0 ={"quantity":O0OOOO0O00OOO0OO0 ,"doneeNo":O000000O00OO0OOO0 .doneeNo }#line:148
                        O000O0OO000OOO0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O00OOO00O0O000000 ,data =OOO0O00OOO000O0O0 ).json ()#line:149
                        if 'status'in O000O0OO000OOO0O0 :#line:151
                            if O000O0OO000OOO0O0 ['status']==200 :#line:152
                                if O000O0OO000OOO0O0 ['data']:#line:153
                                    print (f'【赠送种子】:赠送{O0OOOO0O00OOO0OO0}种子给{O000000O00OO0OOO0.doneeNo}成功')#line:154
                else :#line:155
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:156
    def winning_rewards (OO000O0O0OOO0000O ):#line:158
        O0OO0O0OO0O0OOO0O =f'__{timi_new()}'#line:159
        O0OOO000000OO0O0O ={'authorization':OO000O0O0OOO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0OO0O0OOO0O ),'signstring':O0OO0O0OO0O0OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:168
        O00OOO00O0O00OO00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOO000000OO0O0O ).json ()#line:169
        if 'status'in O00OOO00O0O00OO00 :#line:171
            if O00OOO00O0O00OO00 ['status']==200 :#line:172
                if O00OOO00O0O00OO00 ['data']['amount']:#line:173
                    O00OOO00O00O0OOO0 =O00OOO00O0O00OO00 ['data']['amount']['gold']#line:174
                    return O00OOO00O00O0OOO0 #line:175
                else :#line:176
                    return 0 #line:177
    def certification (O00OOOO00000O0OO0 ):#line:179
        O00OO00OO0000OO00 =f'__{timi_new()}'#line:180
        O000O0O00O00OO000 ={'authorization':O00OOOO00000O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00OO0000OO00 ),'signstring':O00OO00OO0000OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:189
        O0O000OOO00OOO00O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O000O0O00O00OO000 ).json ()#line:190
        if 'status'in O0O000OOO00OOO00O :#line:192
            if O0O000OOO00OOO00O ['status']==200 :#line:193
                if O0O000OOO00OOO00O ['data']['result']:#line:194
                    O000OOO000O000OO0 =O0O000OOO00OOO00O ['data']['nick_name']#line:195
                    return O000OOO000O000OO0 #line:196
                else :#line:197
                    return '未实名'#line:198
    def crops_illustrated (O0O000O00O00O0000 ):#line:201
        O00000O00000O00O0 =f'__{timi_new()}'#line:202
        OOO0O000O00OO0O00 ={'authorization':O0O000O00O00O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O00000O00O0 ),'signstring':O00000O00000O00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:211
        OO00O000000000OOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO0O000O00OO0O00 ).json ()#line:212
        if 'status'in OO00O000000000OOO :#line:214
            if OO00O000000000OOO ['status']==200 :#line:215
                OO00OO0OO0O00O0OO =OO00O000000000OOO ['data'][0 ]['crops']#line:216
                for O0000000OOOOOOO0O in OO00OO0OO0O00O0OO :#line:217
                    if O0000000OOOOOOO0O ['ill_clover_award']:#line:218
                        if float (O0000000OOOOOOO0O ['ill_clover_award'])>1 :#line:219
                            if O0000000OOOOOOO0O ['is_finish']:#line:220
                                if not O0000000OOOOOOO0O ['is_getit']:#line:221
                                    O00000O00000O00O0 =f'_award_level={O0000000OOOOOOO0O["level"]}_{timi_new()}'#line:222
                                    OOO0O000O00OO0O00 ={'authorization':O0O000O00O00O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O00000O00O0 ),'signstring':O00000O00000O00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:231
                                    OOO0000O0O0000O0O ={"award_level":O0000000OOOOOOO0O ['level']}#line:232
                                    O0O00OO00O0O0000O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO0O000O00OO0O00 ,json =OOO0000O0O0000O0O ).json ()#line:233
                                    if 'status'in O0O00OO00O0O0000O :#line:234
                                        if O0O00OO00O0O0000O ['status']==200 :#line:235
                                            OOO00OOOO000O0O0O =O0O00OO00O0O0000O ['data']['ill_clover_award']#line:236
                                            print (f'【图鉴奖励】:领取{O0000000OOOOOOO0O["crop_name"]}成就丨奖励{OOO00OOOO000O0O0O}叶子成功')#line:237
                                        if O0O00OO00O0O0000O ['status']==500 :#line:238
                                            print (f'【图鉴奖励】:{O0O00OO00O0O0000O["message"]}')#line:239
    def watched_ad (OOOOO0O00OO00O0OO ):#line:242
        OO0O00000OO0OOOOO =f'__{timi_new()}'#line:243
        O0O0O0OO0OO00OO0O ={'authorization':OOOOO0O00OO00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00000OO0OOOOO ),'signstring':OO0O00000OO0OOOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
        O0OOO0O0000OOOOOO =requests .request ('post',f'{host}/game/watched-ad',headers =O0O0O0OO0OO00OO0O ).json ()#line:253
        print (O0OOO0O0000OOOOOO )#line:254
    def user_ad (O00000000OOO000O0 ):#line:259
        OOOOOOO0OOOO00OOO =f'__{timi_new()}'#line:260
        OOO00O00000OOO0OO ={'authorization':O00000000OOO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0OOOO00OOO ),'signstring':OOOOOOO0OOOO00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:269
        OOO00O00OO00O00OO =requests .request ('get',f'{host}/user/ad',headers =OOO00O00000OOO0OO ).json ()#line:270
        if 'status'in OOO00O00OO00O00OO :#line:272
            if OOO00O00OO00O00OO ['status']==200 :#line:273
                OOO0OOO0OOOO0OOOO =OOO00O00OO00O00OO ['data']['max_time']#line:274
                O000O0OOOOO0OO0OO =OOO00O00OO00O00OO ['data']['watch_time']#line:275
                O00O00OOO000O000O =OOO00O00OO00O00OO ['data']['added_time']#line:276
                print (f'【获取种子】:获取种子剩余{O00O00OOO000O000O + OOO0OOO0OOOO0OOOO - O000O0OOOOO0OO0OO}次丨好友提供:{O00O00OOO000O000O}次')#line:277
                if O00O00OOO000O000O +OOO0OOO0OOOO0OOOO -O000O0OOOOO0OO0OO >0 :#line:278
                    time .sleep (random .randint (16 ,19 ))#line:279
                    O0O0O0OOOOOOOOOO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO00O00000OOO0OO ).json ()#line:280
                    if 'status'in O0O0O0OOOOOOOOOO0 :#line:282
                        if O0O0O0OOOOOOOOOO0 ['status']==200 :#line:283
                            OO00OOO0000OOOOOO =O0O0O0OOOOOOOOOO0 ['data']['silver']#line:284
                            print (f'【获取种子】:获得种子:{OO00OOO0000OOOOOO}')#line:285
                            return True #line:286
                        if O0O0O0OOOOOOOOOO0 ['status']==500 :#line:287
                            O0O000O0O000O0000 =O0O0O0OOOOOOOOOO0 ['message']#line:288
                            print (f'【获取种子】:{O0O000O0O000O0000}')#line:289
                            return False #line:290
    def synthetic (OO0O0O000O000O0OO ):#line:293
        global id ,g #line:294
        try :#line:295
            while True :#line:296
                O0O0O0000O0OOOO0O =OO0O0O000O000O0OO .level_new ()#line:297
                OO0O0O000OO0OO0OO =f'__{timi_new()}'#line:298
                O0000O0OO0O0O0O0O ={'authorization':OO0O0O000O000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O000OO0OO0OO ),'signstring':OO0O0O000OO0OO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:307
                O0O0OOO0OO0O00OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0000O0OO0O0O0O0O ).json ()#line:308
                if 'status'in O0O0OOO0OO0O00OO0 :#line:310
                    if O0O0OOO0OO0O00OO0 ['status']==200 :#line:311
                        OO0O00OO000OOOO00 =O0O0OOO0OO0O00OO0 ['data']['cropList']#line:312
                        O00OO000O00O0OOO0 =O0O0OOO0OO0O00OO0 ['data']['gameCoreDataDBid']#line:313
                        O0OO00O00O00000OO =0 #line:314
                        for OOOO00000O0OOOO0O in OO0O00OO000OOOO00 :#line:315
                            if not OOOO00000O0OOOO0O :#line:316
                                OOOO00O00O00OOO0O =f'_crop_id={O00OO000O00O0OOO0}&site={O0OO00O00O00000OO}_{OO0O0O000O000O0OO.time}'#line:317
                                OO000000OO0000OOO ={'authorization':OO0O0O000O000O0OO .token ,'timestamp':OO0O0O000O000O0OO .time ,'sign':sign (OOOO00O00O00OOO0O ),'signstring':OOOO00O00O00OOO0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:326
                                OOOOOOO000O00OO00 ={"site":O0OO00O00O00000OO ,"crop_id":O00OO000O00O0OOO0 }#line:327
                                O00O0O0OO0OOOOOOO =requests .request ('post',f'{host}/game/crops/buy',headers =OO000000OO0000OOO ,data =OOOOOOO000O00OO00 ).json ()#line:328
                                time .sleep (random .randint (1 ,3 )/10 )#line:330
                                if 'status'in O00O0O0OO0OOOOOOO :#line:331
                                    if O00O0O0OO0OOOOOOO ['status']==200 :#line:332
                                        if O00O0O0OO0OOOOOOO ['message']=='种子数量不足':#line:333
                                            print (f'【购买合成】:{O00O0O0OO0OOOOOOO["message"]}')#line:334
                                            if not OO0O0O000O000O0OO .user_ad ():#line:335
                                                return False #line:336
                                        print (f'【购买合成】:购买农作物,位置{O0OO00O00O00000OO}')#line:337
                                    if O00O0O0OO0OOOOOOO ['status']==500 :#line:338
                                        print (f'【购买合成】:{O00O0O0OO0OOOOOOO["message"]}')#line:339
                                        return False #line:340
                            O0OO00O00O00000OO +=1 #line:341
                        O0OOOO00OO000O0O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0000O0OO0O0O0O0O ).json ()#line:342
                        OOOOOOO000OO0000O =O0OOOO00OO000O0O0 ['data']['cropList']#line:343
                        O000OOOO00000OOO0 =False #line:344
                        for OOOO00000O0OOOO0O in range (12 ):#line:345
                            id =OOOOOOO000OO0000O [OOOO00000O0OOOO0O ]['level']#line:346
                            if int (O0O0O0000O0OOOO0O )-int (id )>9 :#line:347
                                O00OO0OOO0OOO00OO =f'_site={OOOO00000O0OOOO0O}_{timi_new()}'#line:348
                                OO0O0OO0OOO0O0000 ={'accept':'application/json, text/plain, */*','authorization':OO0O0O000O000O0OO .token ,'timestamp':timi_new (),'sign':sign (O00OO0OOO0OOO00OO ),'signstring':O00OO0OOO0OOO00OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:358
                                OOO00OOOO0OOOO0OO ={"site":OOOO00000O0OOOO0O }#line:359
                                OO0O0O0OOOOOOO00O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0O0OO0OOO0O0000 ,data =OOO00OOOO0OOOO0OO ).json ()#line:360
                                if 'status'in OO0O0O0OOOOOOO00O :#line:362
                                    if OO0O0O0OOOOOOO00O ['status']==200 :#line:363
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:364
                            if id !=0 :#line:365
                                for OOO0O0OO0O00000O0 in range (11 ):#line:366
                                    OOO0O0OOOO0000O0O =OOO0O0OO0O00000O0 +1 #line:367
                                    g =OOOOOOO000OO0000O [OOO0O0OOOO0000O0O ]['level']#line:368
                                    if id ==g :#line:369
                                        O0OOOOO0O00O0O0O0 =OOO0O0OO0O00000O0 +2 #line:370
                                        if O0OOOOO0O00O0O0O0 ==OOOO00000O0OOOO0O +1 :#line:371
                                            pass #line:372
                                        else :#line:373
                                            O000O000OOO0O0OO0 =OOOO00000O0OOOO0O +1 #line:374
                                            time .sleep (random .randint (1 ,3 )/10 )#line:376
                                            OOOOOOO0OO00O0O00 =f'_site={O000O000OOO0O0OO0-1}&targetSite={O0OOOOO0O00O0O0O0-1}_{timi_new()}'#line:377
                                            OO0O00O00O0OO00OO ={'accept':'application/json, text/plain, */*','authorization':OO0O0O000O000O0OO .token ,'timestamp':timi_new (),'sign':sign (OOOOOOO0OO00O0O00 ),'signstring':OOOOOOO0OO00O0O00 ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:392
                                            OO0OOO00O0OO0O00O ={"site":int (O000O000OOO0O0OO0 -1 ),"targetSite":int (O0OOOOO0O00O0O0O0 -1 )}#line:393
                                            OO0000O0OO0000OO0 =requests .request ('post',f'{host}/game/crops/move',headers =OO0O00O00O0OO00OO ,json =OO0OOO00O0OO0O00O ).json ()#line:394
                                            if 'status'in OO0000O0OO0000OO0 :#line:395
                                                if OO0000O0OO0000OO0 ['status']==200 :#line:396
                                                    pass #line:397
                                            print ('【购买合成】:',O000O000OOO0O0OO0 ,O0OOOOO0O00O0O0O0 ,'合成成功')#line:399
                                            O000OOOO00000OOO0 =True #line:400
                                    if O000OOOO00000OOO0 :#line:401
                                        break #line:402
                                if O000OOOO00000OOO0 :#line:403
                                    break #line:404
        except Exception as O0000OO0OOO0OOOOO :#line:405
            OO0O0O000O000O0OO .synthetic ()#line:406
    def level_new (OO000000O0O00OOOO ):#line:409
        try :#line:410
            O0O0O0OO00O00OOO0 =f'__{timi_new()}'#line:411
            OOO0OO0OO0OOOO0OO ={'authorization':OO000000O0O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO00O00OOO0 ),'signstring':O0O0O0OO00O00OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:420
            OO00OO0O0OO000O00 =requests .request ('get',f'{host}/user',headers =OOO0OO0OO0OOOO0OO ).json ()#line:421
            if 'status'in OO00OO0O0OO000O00 :#line:422
                if OO00OO0O0OO000O00 ['status']==200 :#line:423
                    return OO00OO0O0OO000O00 ['data']['level']#line:424
        except Exception as OO0OO0OOOO0O0OOO0 :#line:425
            print (OO0OO0OOOO0O0OOO0 )#line:426
    def propsraffle (OOO00O0OOOO0O000O ):#line:430
        try :#line:431
            while True :#line:432
                O00000OOOO000O0O0 =f'__{timi_new()}'#line:433
                O00O0OOO0000OOO0O ={'authorization':OOO00O0OOOO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOOO000O0O0 ),'signstring':O00000OOOO000O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:442
                O0O0O0OO00OO0OOO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00O0OOO0000OOO0O ).json ()#line:443
                if 'status'in O0O0O0OO00OO0OOO0 :#line:445
                    if O0O0O0OO00OO0OOO0 ['status']==200 :#line:446
                        OO00O00OO0O0O000O =O0O0O0OO00OO0OOO0 ['data']['rows']#line:447
                        OO0000O0OOO0000OO =O0O0O0OO00OO0OOO0 ['data']['vstate']#line:448
                        if OO00O00OO0O0O000O ==5 or OO00O00OO0O0O000O ==6 or OO00O00OO0O0O000O ==7 :#line:449
                            O00000O000O00O0OO =O0O0O0OO00OO0OOO0 ['data']['silver']#line:450
                            print (f'【转盘抽奖】:获得种子:{O00000O000O00O0OO}')#line:451
                        if OO00O00OO0O0O000O ==1 or OO00O00OO0O0O000O ==2 or OO00O00OO0O0O000O ==3 :#line:452
                            OOO0OO0000OO0O00O =O0O0O0OO00OO0OOO0 ['data']['clover']#line:453
                            print (f'【转盘抽奖】:获得三叶草:{OOO0OO0000OO0O00O}')#line:454
                        if OO00O00OO0O0O000O ==4 or OO00O00OO0O0O000O ==8 :#line:455
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:456
                        if OO00O00OO0O0O000O =='抽奖次数已用完':#line:460
                            if OO0000O0OOO0000OO :#line:461
                                OOOO00O0O0O0OOOO0 =random .randint (160 ,190 )/10 #line:462
                                print (f'【转盘抽奖】:抽奖次数已用完丨等待{OOOO00O0O0O0OOOO0}秒获取抽奖机会')#line:463
                                time .sleep (OOOO00O0O0O0OOOO0 )#line:464
                                O000OO0000O000000 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O00O0OOO0000OOO0O ).json ()#line:465
                                if 'status'in O000OO0000O000000 :#line:467
                                    if O000OO0000O000000 ['status']==200 :#line:468
                                        print (f'【转盘抽奖】:{O000OO0000O000000["message"]}')#line:469
                                    if O000OO0000O000000 ['status']==500 :#line:470
                                        print (f'【转盘抽奖】:{O000OO0000O000000["message"]}')#line:471
                                        break #line:472
                                time .sleep (random .randint (10 ,15 )/10 )#line:473
                            else :#line:474
                                break #line:475
                time .sleep (random .randint (8 ,15 )/10 )#line:476
        except Exception as OO0O00OO000OO0OO0 :#line:477
            print (OO0O00OO000OO0OO0 )#line:478
    def friends_invitation (O00O00O0OOOO0O00O ):#line:481
        try :#line:482
            O0OOO0OOO000O0OO0 =f'__{timi_new()}'#line:483
            OO00O0O00000O0O0O ={'authorization':O00O00O0OOOO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OOO000O0OO0 ),'signstring':O0OOO0OOO000O0OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:492
            OO0O00OOO00O0OO00 =requests .request ('get',f'{host}/friends',headers =OO00O0O00000O0O0O ).json ()#line:493
            if 'status'in OO0O00OOO00O0OO00 :#line:494
                if OO0O00OOO00O0OO00 ['status']==200 :#line:495
                    O000OO000000O0OOO =OO0O00OOO00O0OO00 ['data']['myInviteter']#line:496
                    if O000OO000000O0OOO :#line:497
                        O0000O0O00O0O0OOO =O000OO000000O0OOO ['user']['nickname']#line:498
                        O00OO0O0OO0O000O0 =O00O00O0OOOO0O00O .certification ()#line:499
                        print (f'【绑邀请码】:我的邀请人:{O0000O0O00O0O0OOO}丨实名:{O00OO0O0OO0O000O0}')#line:500
                    else :#line:501
                        if O00O00O0OOOO0O00O .innerId !='0':#line:502
                            O0OOO0OOO000O0OO0 =f'_innerId={O00O00O0OOOO0O00O.innerId}_{timi_new()}'#line:503
                            OO00O0O00000O0O0O ={'authorization':O00O00O0OOOO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OOO000O0OO0 ),'signstring':O0OOO0OOO000O0OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
                            OO00O00OOO0OO00OO ={"innerId":O00O00O0OOOO0O00O .innerId }#line:513
                            O000OO0000OOOO000 =requests .request ('post',f'{host}/friends/my-invitation',headers =OO00O0O00000O0O0O ,data =OO00O00OOO0OO00OO ).json ()#line:514
                            if 'status'in O000OO0000OOOO000 :#line:515
                                if O000OO0000OOOO000 ['status']==200 :#line:516
                                    print (f'【绑邀请码】:{O00O00O0OOOO0O00O.innerId}{O000OO0000OOOO000["message"]}')#line:517
                        else :#line:518
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:519
        except Exception as OOOO0OOO0O00OO00O :#line:520
            print (OOOO0OOO0O00OO00O )#line:521
    def add_clover (OO00O0OOO0OOOOOO0 ):#line:525
        try :#line:526
            O000O0O0OOOOO0OO0 =f'__{timi_new()}'#line:527
            OOOOOOO00000O0OOO ={'authorization':OO00O0OOO0OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O0OOOOO0OO0 ),'signstring':O000O0O0OOOOO0OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:536
            O00OO00O0O0O000O0 =requests .request ('get',f'{host}/assets/clovers',headers =OOOOOOO00000O0OOO ).json ()#line:537
            if 'status'in O00OO00O0O0O000O0 :#line:539
                if O00OO00O0O0O000O0 ['status']==200 :#line:540
                    O0O0OO0OO0OO00OOO =O00OO00O0O0O000O0 ['data']['clover']#line:541
                    O000O00OOOOO00000 =O00OO00O0O0O000O0 ['data']['used_clover']#line:542
                    O0O000O0000OO0O0O =float (O0O0OO0OO0OO00OOO )-float (O000O00OOOOO00000 )#line:543
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O000O00OOOOO00000}')#line:544
                    if O0O000O0000OO0O0O >1 :#line:545
                        O000O0O0OOOOO0OO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O000O0000OO0O0O)}_{timi_new()}'#line:546
                        OOOOOOO00000O0OOO ={'authorization':OO00O0OOO0OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O0OOOOO0OO0 ),'signstring':O000O0O0OOOOO0OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:555
                        OO00OOOOOOO0O000O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O000O0000OO0O0O )}#line:556
                        OO00O0OOO0OOOOO00 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOOOOO00000O0OOO ,data =OO00OOOOOOO0O000O ).json ()#line:557
                        if 'status'in OO00O0OOO0OOOOO00 :#line:559
                            if OO00O0OOO0OOOOO00 ['status']==200 :#line:560
                                print (f'【参与抽奖】:添加三叶草:{OO00O0OOO0OOOOO00["data"]}丨数量:{O0O000O0000OO0O0O}')#line:561
            OOO0O0OOOOO0O0O00 =requests .request ('get',f'{host}/lottery',headers =OOOOOOO00000O0OOO ).json ()#line:562
            OOO0O00000O00OOOO =OO00O0OOO0OOOOOO0 .winning_rewards ()#line:564
            if 'status'in OOO0O0OOOOO0O0O00 :#line:565
                if OOO0O0OOOOO0O0O00 ['status']==200 :#line:566
                    O00OOOOOO000OO00O =OOO0O0OOOOO0O0O00 ['data'][0 ]['day_get_gold_quantity']#line:567
                    print (f'【参与抽奖】:预计每天中{O00OOOOOO000OO00O[:6]}种子丨好友收益:{OOO0O00000O00OOOO}')#line:568
        except Exception as O0O0O000OOO0O0O00 :#line:569
            print (O0O0O000OOO0O0O00 )#line:570
    def energy (O000OO00O000OOOOO ):#line:573
        OO0OO0OO0OOO000O0 =f'__{timi_new()}'#line:574
        OOOO0O0OOOOOO000O ={'authorization':O000OO00O000OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO0OOO000O0 ),'signstring':OO0OO0OO0OOO000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
        OO0O000OO000O0O00 =requests .request ('get',f'{host}/energy/general',headers =OOOO0O0OOOOOO000O ).json ()#line:584
        if 'status'in OO0O000OO000O0O00 :#line:586
            if OO0O000OO000O0O00 ['status']==200 :#line:587
                O000OOOOO0O0OO000 =OO0O000OO000O0O00 ['data']['ordinary_water_consumptions']#line:588
                if float (O000OOOOO0O0OO000 )<80 :#line:589
                    O0OOOOOOO00OOOO0O =99 -float (O000OOOOO0O0OO000 )#line:590
                    OOOOOO000000OO00O ={"fertilizer":str (O0OOOOOOO00OOOO0O ).split ('.')[0 ]}#line:591
                    OO0OO0OO0OO00O000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOO0O0OOOOOO000O ,data =OOOOOO000000OO00O ).json ()#line:592
                    if 'status'in OO0OO0OO0OO00O000 :#line:594
                        if OO0OO0OO0OO00O000 ['status']==200 :#line:595
                            print (f'【购买肥料】:{OO0OO0OO0OO00O000["message"]}')#line:596
                OOO0000OOO0O00O00 =OO0O000OO000O0O00 ['data']['ordinary_water_consumptions']#line:597
                if float (OOO0000OOO0O00O00 )<800 :#line:598
                    O000O00O0O00OOOO0 =999 -float (OOO0000OOO0O00O00 )#line:599
                    OOO00OO00O0OOO0O0 ={"water":str (O000O00O0O00OOOO0 ).split ('.')[0 ]}#line:600
                    OO0O0O0OOO0OOOO0O =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOO0O0OOOOOO000O ,data =OOO00OO00O0OOO0O0 ).json ()#line:601
                    if 'status'in OO0O0O0OOO0OOOO0O :#line:602
                        if OO0O0O0OOO0OOOO0O ['status']==200 :#line:603
                            print (f'【购买水滴】:{OO0O0O0OOO0OOOO0O["message"]}')#line:604
def version_of_the_validation ():#line:610
    return str ((65 -56 )/10 )#line:611
def gitee_validation ():#line:613
    try :#line:614
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:615
    except Exception as O0OO0O000OOO000OO :#line:616
        sys .exit (0 )#line:617
def update_the_validation ():#line:623
    try :#line:624
        O00O00OOO000O0OOO =gitee_validation ()#line:625
        if version_of_the_validation ()<O00O00OOO000O0OOO ['CityEarth']['edition']:#line:626
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O00OOO000O0OOO["CityEarth"]["edition"]}   ❌')#line:627
            print (f'更新内容=>>{O00O00OOO000O0OOO["CityEarth"]["content"]}   👍')#line:628
        else :#line:629
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O00OOO000O0OOO["CityEarth"]["edition"]}   ✅')#line:630
            print (f'更新内容=>> {O00O00OOO000O0OOO["CityEarth"]["content"]}   👍')#line:631
    except Exception as OOO0OO0OOO0O00000 :#line:632
        print (OOO0OO0OOO0O00000 )#line:633
def os_qinglong ():#line:636
    if application in os .environ :#line:637
        O000OOOO00O000O0O =os .environ [application ].split ('\n')#line:638
        if len (O000OOOO00O000O0O )>0 :#line:639
            return O000OOOO00O000O0O #line:640
        else :#line:641
            print (f"{application}变量未启用")#line:642
            print ('脚本退出')#line:643
            sys .exit (1 )#line:644
    else :#line:645
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:646
        return os_built ()#line:647
def os_built ():#line:650
    if token :#line:651
        O0OOO0OOOO00O0OOO =token .split ('\n')#line:652
        if len (O0OOO0OOOO00O0OOO )>0 :#line:653
            return O0OOO0OOOO00O0OOO #line:654
    else :#line:655
        print (f"内置变量为空")#line:656
        print ('脚本结束')#line:657
        sys .exit (0 )#line:658
if __name__ =='__main__':#line:661
    start ()#line:662
