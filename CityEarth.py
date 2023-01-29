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
@ cron: 22 */3 * * *
@ new Env('生城世朝')
@ 项目地址  微信打开  http://share.sc19319.com/scsc/1937553
@ 抓取  http://scsc.sc19319.com 的authorization值
@ 青龙变量  青龙配置文件 export ce_token="authorization&赠送金种子数量大于&赠送金种子id" 
@ 如果你有20金种子填10就会赠 填21就不会赠送  不赠送全填 999999     多号换行
@ 变量示范    export ce_token="557b8069-1234-4ae7-9e29-b7871f91541b&999999&999999"  用&符号分开数据
@ 版本  1.1
"""

application = 'ce_token'  # 变量名
token = ''
time_xx = random.randint(8, 12)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://scsc.sc19319.com'#line:2
golden_seed =0 #line:3
def start ():#line:4
    try :#line:5
        update_the_validation ()#line:6
        O0OOO00000O0000OO =os_qinglong ()#line:7
        print (f"==========共找到{len(O0OOO00000O0000OO)}个账号==========")#line:8
        for OOO0O0OO0OO0OOO00 in O0OOO00000O0000OO :#line:9
            print (f"------------正在执行第{O0OOO00000O0000OO.index(OOO0O0OO0OO0OOO00) + 1}个账号------------")#line:10
            OOO0OOOOOOO00O000 =CityEarth (OOO0O0OO0OO0OOO00 )#line:11
            def O0OOOO00000OOOOO0 ():#line:13
                if OOO0OOOOOOO00O000 .base_info ():#line:15
                    OOO0OOOOOOO00O000 .game_map ()#line:19
                    OOO0OOOOOOO00O000 .friends_invitation ()#line:21
                    OOO0OOOOOOO00O000 .add_clover ()#line:23
                    OOO0OOOOOOO00O000 .energy ()#line:25
                    OOO0OOOOOOO00O000 .propsraffle ()#line:27
                    OOO0OOOOOOO00O000 .synthetic ()#line:29
                    OOO0OOOOOOO00O000 .crops_illustrated ()#line:31
                    OOO0OOOOOOO00O000 .give_gold ()#line:33
                else :#line:34
                    print ('token失效')#line:35
            O0OO00O0O0OOOO000 =threading .Thread (target =O0OOOO00000OOOOO0 )#line:37
            O0OO00O0O0OOOO000 .start ()#line:38
            time .sleep (time_xx )#line:39
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:41
        time .sleep (3 )#line:42
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:43
    except Exception as OO0OO0OOO000O00O0 :#line:44
        print (OO0OO0OOO000O00O0 )#line:45
def sign (O0OO0O0O0O000OOO0 ):#line:48
    O0O0O00O00O000O0O =hashlib .md5 (O0OO0O0O0O000OOO0 .encode ()).hexdigest ()#line:49
    OO0O00000O0000OO0 ="scsc%^&*"+O0O0O00O00O000O0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:50
    OO00OO00OOO0O000O =hashlib .md5 (OO0O00000O0000OO0 .encode ()).hexdigest ()#line:51
    return OO00OO00OOO0O000O #line:52
def timi_new ():#line:55
    return str (int (time .time ()*1000 ))#line:56
class CityEarth :#line:58
    def __init__ (OOO000O0000OOO00O ,OO0O0OOO000000O00 ):#line:60
        try :#line:61
            OOO000O0000OOO00O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:62
            OOO000O0000OOO00O .token =OO0O0OOO000000O00 .split ('&')[0 ]#line:63
            OOO000O0000OOO00O .innerId =OO0O0OOO000000O00 .split ('&')[1 ]#line:64
            OOO000O0000OOO00O .doneeNo =OO0O0OOO000000O00 .split ('&')[2 ]#line:65
        except :#line:66
            print ('变量格式错误')#line:67
    def base_info (OOO00O00O00000OO0 ):#line:70
        try :#line:71
            O0OOOO0OOO0O00OOO =f'__{timi_new()}'#line:72
            O0OO0O00O0O0OOO0O ={'authorization':OOO00O00O00000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OOO0O00OOO ),'signstring':O0OOOO0OOO0O00OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:81
            O0O0OO0OOO0O00O0O =requests .request ('get',f'{host}/user',headers =O0OO0O00O0O0OOO0O ).json ()#line:82
            if 'status'in O0O0OO0OOO0O00O0O :#line:84
                if O0O0OO0OOO0O00O0O ['status']==200 :#line:85
                    OOOOO00000O00O000 =O0O0OO0OOO0O00O0O ['data']['nickname']#line:86
                    OOO0OOOOO0O00OOOO =O0O0OO0OOO0O00O0O ['data']['inner_id']#line:87
                    O0OO00OO0O0O00O00 =O0O0OO0OOO0O00O0O ['data']['assets']['gold']#line:88
                    O00O000000OO00000 =O0O0OO0OOO0O00O0O ['data']['level']#line:89
                    print (f'【账号信息】:昵称:{OOOOO00000O00O000[:5]}丨ID:{str(OOO0OOOOO0O00OOOO)[:3] + "**" + str(OOO0OOOOO0O00OOOO)[5:]}丨等级:{O00O000000OO00000}丨种子:{str(O0OO00OO0O0O00O00).split(".")[0]}')#line:90
                if O0O0OO0OOO0O00O0O ['status']==401 :#line:91
                    return False #line:92
                if O0O0OO0OOO0O00O0O ['status']==500 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as OOO0O0OO0O0O0000O :#line:96
            print (OOO0O0OO0O0O0000O )#line:97
    def game_map (OOO0OOO0O00O000OO ):#line:100
        O00000000000O0O0O =f'__{timi_new()}'#line:101
        O0OO0OOOOO0O0O000 ={'authorization':OOO0OOO0O00O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000000000O0O0O ),'signstring':O00000000000O0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:110
        OO0OO00OOO0O000O0 =requests .request ('get',f'{host}/game/map',headers =O0OO0OOOOO0O0O000 ).json ()#line:111
        if 'status'in OO0OO00OOO0O000O0 :#line:113
            if OO0OO00OOO0O000O0 ['status']==200 :#line:114
                for O000OO0000O0O0OOO in OO0OO00OOO0O000O0 ['data']['list'][0 ]['crops']:#line:115
                    O00OO0O0OO00OOO0O =O000OO0000O0O0OOO ['level']#line:117
                    if O00OO0O0OO00OOO0O ==41 :#line:118
                        OOO0O0OO0O0O000OO =O000OO0000O0O0OOO ['crop_name']#line:119
                        OOO0O000O0O00OOOO =O000OO0000O0O0OOO ['count']#line:120
                        if OOO0O000O0O00OOOO >0 :#line:121
                            print (f'【农业资产】:{OOO0O0OO0O0O000OO}丨数量:{OOO0O000O0O00OOOO}')#line:122
    def give_gold (O0O00OO0O000000O0 ):#line:125
        OOO0OO0O000OOOO00 =f'__{timi_new()}'#line:126
        O00000OO0OOO0O00O ={'authorization':O0O00OO0O000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O000OOOO00 ),'signstring':OOO0OO0O000OOOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:135
        OOO0O000OO00OOO0O =requests .request ('get',f'{host}/user',headers =O00000OO0OOO0O00O ).json ()#line:136
        if 'status'in OOO0O000OO00OOO0O :#line:137
            if OOO0O000OO00OOO0O ['status']==200 :#line:138
                if float (O0O00OO0O000000O0 .doneeNo )!=0 :#line:139
                    O00OO000OOOOO000O =OOO0O000OO00OOO0O ['data']['assets']['gold']#line:140
                    if float (O00OO000OOOOO000O )>float (O0O00OO0O000000O0 .innerId ):#line:141
                        O000OOOO0OOO0O00O =int (float (O00OO000OOOOO000O )/1.1 )#line:142
                        OOO0OO0O000OOOO00 =f'_doneeNo={O0O00OO0O000000O0.doneeNo}&quantity={O000OOOO0OOO0O00O}_{timi_new()}'#line:143
                        O00000OO0OOO0O00O ={'authorization':O0O00OO0O000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O000OOOO00 ),'signstring':OOO0OO0O000OOOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:152
                        O0000O0OO000O0O00 ={"quantity":O000OOOO0OOO0O00O ,"doneeNo":O0O00OO0O000000O0 .doneeNo }#line:156
                        O0O0OOOOO00O00OOO =requests .request ('post',f'{host}/finance/give-gold',headers =O00000OO0OOO0O00O ,data =O0000O0OO000O0O00 ).json ()#line:157
                        if 'status'in O0O0OOOOO00O00OOO :#line:159
                            if O0O0OOOOO00O00OOO ['status']==200 :#line:160
                                if O0O0OOOOO00O00OOO ['data']:#line:161
                                    print (f'【赠送种子】:赠送{O000OOOO0OOO0O00O}种子给{O0O00OO0O000000O0.doneeNo}成功')#line:162
                else :#line:163
                    print (f'【赠送种子】:此账号未启动赠送功能')#line:164
    def winning_rewards (O0O000OO0OOO0OO0O ):#line:167
        O00O00O0O000O000O =f'__{timi_new()}'#line:168
        O0OO0OO0OOO000O0O ={'authorization':O0O000OO0OOO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O000O000O ),'signstring':O00O00O0O000O000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:177
        O0OO0O000000O0000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OO0OO0OOO000O0O ).json ()#line:178
        if 'status'in O0OO0O000000O0000 :#line:180
            if O0OO0O000000O0000 ['status']==200 :#line:181
                if O0OO0O000000O0000 ['data']['amount']:#line:182
                    OOO0O0O00O00OOOO0 =O0OO0O000000O0000 ['data']['amount']['gold']#line:183
                    return OOO0O0O00O00OOOO0 #line:184
                else :#line:185
                    return 0 #line:186
    def certification (O000000OO000O0O0O ):#line:189
        O0O000OO0OOO00OO0 =f'__{timi_new()}'#line:190
        O00OO0OOOOO000O00 ={'authorization':O000000OO000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OO0OOO00OO0 ),'signstring':O0O000OO0OOO00OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:199
        OO0OO00OOOOOO0O0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OO0OOOOO000O00 ).json ()#line:200
        if 'status'in OO0OO00OOOOOO0O0O :#line:202
            if OO0OO00OOOOOO0O0O ['status']==200 :#line:203
                if OO0OO00OOOOOO0O0O ['data']['result']:#line:204
                    O00O0OOOOOO0O00O0 =OO0OO00OOOOOO0O0O ['data']['nick_name']#line:205
                    return O00O0OOOOOO0O00O0 #line:206
                else :#line:207
                    return '未实名'#line:208
    def crops_illustrated (O0OOO0000000OO00O ):#line:211
        O0OO0O00O00000000 =f'__{timi_new()}'#line:212
        O0OOO0OOO0O0O00O0 ={'authorization':O0OOO0000000OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O00000000 ),'signstring':O0OO0O00O00000000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:221
        O0OO0000OO000000O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OOO0OOO0O0O00O0 ).json ()#line:222
        if 'status'in O0OO0000OO000000O :#line:224
            if O0OO0000OO000000O ['status']==200 :#line:225
                OO0000O00OOO00000 =O0OO0000OO000000O ['data'][0 ]['crops']#line:226
                for OOO0O0O00O000O000 in OO0000O00OOO00000 :#line:227
                    if OOO0O0O00O000O000 ['ill_clover_award']:#line:228
                        if float (OOO0O0O00O000O000 ['ill_clover_award'])>1 :#line:229
                            if OOO0O0O00O000O000 ['is_finish']:#line:230
                                if not OOO0O0O00O000O000 ['is_getit']:#line:231
                                    O0OO0O00O00000000 =f'_award_level={OOO0O0O00O000O000["level"]}_{timi_new()}'#line:232
                                    O0OOO0OOO0O0O00O0 ={'authorization':O0OOO0000000OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O00000000 ),'signstring':O0OO0O00O00000000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:241
                                    OOOOO00OO00OO0O0O ={"award_level":OOO0O0O00O000O000 ['level']}#line:242
                                    O00O0OOO0OOO0000O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OOO0OOO0O0O00O0 ,json =OOOOO00OO00OO0O0O ).json ()#line:244
                                    if 'status'in O00O0OOO0OOO0000O :#line:245
                                        if O00O0OOO0OOO0000O ['status']==200 :#line:246
                                            OOO0OOOO0OO0O0O0O =O00O0OOO0OOO0000O ['data']['ill_clover_award']#line:247
                                            print (f'【图鉴奖励】:领取{OOO0O0O00O000O000["crop_name"]}成就丨奖励{OOO0OOOO0OO0O0O0O}叶子成功')#line:249
                                        if O00O0OOO0OOO0000O ['status']==500 :#line:250
                                            print (f'【图鉴奖励】:{O00O0OOO0OOO0000O["message"]}')#line:251
    def watched_ad (O000O0O0000O0O00O ):#line:254
        O00O0OOOOO0000OO0 =f'__{timi_new()}'#line:255
        OO000O00O0OOOOO00 ={'authorization':O000O0O0000O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOOOO0000OO0 ),'signstring':O00O0OOOOO0000OO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:264
        O00OOOOO000OO0OO0 =requests .request ('post',f'{host}/game/watched-ad',headers =OO000O00O0OOOOO00 ).json ()#line:265
        print (O00OOOOO000OO0OO0 )#line:266
    def user_ad (OO0O0OO000O00OO00 ):#line:269
        O00O00000O00000OO =f'__{timi_new()}'#line:270
        OOO00O0OOOOO00OOO ={'authorization':OO0O0OO000O00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00000O00000OO ),'signstring':O00O00000O00000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:279
        O00OOO00OO00O0OOO =requests .request ('get',f'{host}/user/ad',headers =OOO00O0OOOOO00OOO ).json ()#line:280
        if 'status'in O00OOO00OO00O0OOO :#line:282
            if O00OOO00OO00O0OOO ['status']==200 :#line:283
                OOO00000000OO000O =O00OOO00OO00O0OOO ['data']['max_time']#line:284
                OOO0000OO0OO00OO0 =O00OOO00OO00O0OOO ['data']['watch_time']#line:285
                O0OOO00O000OO0O00 =O00OOO00OO00O0OOO ['data']['added_time']#line:286
                print (f'【获取种子】:获取种子剩余{O0OOO00O000OO0O00 + OOO00000000OO000O - OOO0000OO0OO00OO0}次丨好友提供:{O0OOO00O000OO0O00}次')#line:287
                if O0OOO00O000OO0O00 +OOO00000000OO000O -OOO0000OO0OO00OO0 >0 :#line:288
                    time .sleep (random .randint (16 ,19 ))#line:289
                    OO0OO0OO00O00OOOO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO00O0OOOOO00OOO ).json ()#line:290
                    if 'status'in OO0OO0OO00O00OOOO :#line:292
                        if OO0OO0OO00O00OOOO ['status']==200 :#line:293
                            OOO0O00OO0O0OO0OO =OO0OO0OO00O00OOOO ['data']['silver']#line:294
                            print (f'【获取种子】:获得种子:{OOO0O00OO0O0OO0OO}')#line:295
                            return True #line:296
                        if OO0OO0OO00O00OOOO ['status']==500 :#line:297
                            OO0O0O0OOOO0OO0O0 =OO0OO0OO00O00OOOO ['message']#line:298
                            print (f'【获取种子】:{OO0O0O0OOOO0OO0O0}')#line:299
                            return False #line:300
    def synthetic (OO00O0OO00OOOOO0O ):#line:303
        global id ,g #line:304
        try :#line:305
            OO00O0OO000OOO000 =OO00O0OO00OOOOO0O .level_new ()#line:306
            while True :#line:307
                O0O0000OO0OOO0O0O =f'__{timi_new()}'#line:308
                O0OOO0OO000O0O0OO ={'authorization':OO00O0OO00OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OO0OOO0O0O ),'signstring':O0O0000OO0OOO0O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:317
                OOOO000O0OOOO0O00 =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0OO000O0O0OO ).json ()#line:318
                if 'status'in OOOO000O0OOOO0O00 :#line:320
                    if OOOO000O0OOOO0O00 ['status']==200 :#line:321
                        O0OOOOO000O00O000 =OOOO000O0OOOO0O00 ['data']['cropList']#line:322
                        O00OO0OOOO00OO000 =OOOO000O0OOOO0O00 ['data']['gameCoreDataDBid']#line:323
                        O00000OOO000O0O00 =0 #line:324
                        for OOOO0OO000OO0O0OO in O0OOOOO000O00O000 :#line:325
                            if not OOOO0OO000OO0O0OO :#line:326
                                OOOOO0000O000O0O0 =f'_crop_id={O00OO0OOOO00OO000}&site={O00000OOO000O0O00}_{OO00O0OO00OOOOO0O.time}'#line:327
                                OOO000O0000O0O0OO ={'authorization':OO00O0OO00OOOOO0O .token ,'timestamp':OO00O0OO00OOOOO0O .time ,'sign':sign (OOOOO0000O000O0O0 ),'signstring':OOOOO0000O000O0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:336
                                O00O0OOOOOOOOOO00 ={"site":O00000OOO000O0O00 ,"crop_id":O00OO0OOOO00OO000 }#line:337
                                O00OO0OOO0O0O000O =requests .request ('post',f'{host}/game/crops/buy',headers =OOO000O0000O0O0OO ,data =O00O0OOOOOOOOOO00 ).json ()#line:338
                                time .sleep (random .randint (1 ,3 )/10 )#line:340
                                if 'status'in O00OO0OOO0O0O000O :#line:341
                                    if O00OO0OOO0O0O000O ['status']==200 :#line:342
                                        if O00OO0OOO0O0O000O ['message']=='种子数量不足':#line:343
                                            OO00O0OO000OOO000 =OO00O0OO00OOOOO0O .level_new ()#line:344
                                            print (f'【种植合成】:{O00OO0OOO0O0O000O["message"]}')#line:345
                                            if not OO00O0OO00OOOOO0O .user_ad ():#line:346
                                                return False #line:347
                                        print (f'【种植合成】:种植农作物,位置{O00000OOO000O0O00}')#line:348
                                    if O00OO0OOO0O0O000O ['status']==500 :#line:349
                                        print (f'【种植合成】:{O00OO0OOO0O0O000O["message"]}')#line:350
                                        return False #line:351
                            O00000OOO000O0O00 +=1 #line:352
                        O0O000OOO0OOO00O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0OO000O0O0OO ).json ()#line:353
                        O0OOOOO0000O0O00O =O0O000OOO0OOO00O0 ['data']['cropList']#line:354
                        O0OOO0OOO0OO0000O =False #line:355
                        for OOOO0OO000OO0O0OO in range (12 ):#line:356
                            id =O0OOOOO0000O0O00O [OOOO0OO000OO0O0OO ]['level']#line:357
                            if float (OO00O0OO000OOO000 )-float (id )>9 :#line:358
                                O00O0O000OO0O0OO0 =f'_site={OOOO0OO000OO0O0OO}_{timi_new()}'#line:359
                                O0O00OO0O0O0000O0 ={'accept':'application/json, text/plain, */*','authorization':OO00O0OO00OOOOO0O .token ,'timestamp':timi_new (),'sign':sign (O00O0O000OO0O0OO0 ),'signstring':O00O0O000OO0O0OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:369
                                OO0O0O0OOOO0OOO00 ={"site":OOOO0OO000OO0O0OO }#line:370
                                OOO000O00OOO00000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O00OO0O0O0000O0 ,data =OO0O0O0OOOO0OOO00 ).json ()#line:372
                                if 'status'in OOO000O00OOO00000 :#line:373
                                    if OOO000O00OOO00000 ['status']==200 :#line:374
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:375
                            if id !=0 :#line:376
                                for OOOO0OO0O0OO0000O in range (11 ):#line:377
                                    OO0O00O000000O0OO =OOOO0OO0O0OO0000O +1 #line:378
                                    g =O0OOOOO0000O0O00O [OO0O00O000000O0OO ]['level']#line:379
                                    if id ==g :#line:380
                                        OO0O000000O000OOO =OOOO0OO0O0OO0000O +2 #line:381
                                        if OO0O000000O000OOO ==OOOO0OO000OO0O0OO +1 :#line:382
                                            pass #line:383
                                        else :#line:384
                                            OOOOOO0OO00OO0OO0 =OOOO0OO000OO0O0OO +1 #line:385
                                            time .sleep (random .randint (1 ,3 )/10 )#line:387
                                            OO0OOOO0OOO0OO00O =f'_site={OOOOOO0OO00OO0OO0 - 1}&targetSite={OO0O000000O000OOO - 1}_{timi_new()}'#line:388
                                            OO0OO0O0OOO0OOOO0 ={'accept':'application/json, text/plain, */*','authorization':OO00O0OO00OOOOO0O .token ,'timestamp':timi_new (),'sign':sign (OO0OOOO0OOO0OO00O ),'signstring':OO0OOOO0OOO0OO00O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:403
                                            OO000O0O000O0OOOO ={"site":int (OOOOOO0OO00OO0OO0 -1 ),"targetSite":int (OO0O000000O000OOO -1 )}#line:404
                                            O0O000OO0O0O0O000 =requests .request ('post',f'{host}/game/crops/move',headers =OO0OO0O0OOO0OOOO0 ,json =OO000O0O000O0OOOO ).json ()#line:406
                                            if 'status'in O0O000OO0O0O0O000 :#line:407
                                                if O0O000OO0O0O0O000 ['status']==200 :#line:408
                                                    pass #line:409
                                            print ('【种植合成】:',OOOOOO0OO00OO0OO0 ,OO0O000000O000OOO ,'合成成功')#line:411
                                            O0OOO0OOO0OO0000O =True #line:412
                                    if O0OOO0OOO0OO0000O :#line:413
                                        break #line:414
                                if O0OOO0OOO0OO0000O :#line:415
                                    break #line:416
        except Exception as OOO0OO00O0000OOOO :#line:417
            OO00O0OO00OOOOO0O .synthetic ()#line:418
    def level_new (OOOO000O0O0OOO0O0 ):#line:421
        try :#line:422
            OO0000O0000O0OOO0 =f'__{timi_new()}'#line:423
            O00OO00OO0OO00O0O ={'authorization':OOOO000O0O0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O0000O0OOO0 ),'signstring':OO0000O0000O0OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:432
            O00O00O000O0O000O =requests .request ('get',f'{host}/user',headers =O00OO00OO0OO00O0O ).json ()#line:433
            if 'status'in O00O00O000O0O000O :#line:434
                if O00O00O000O0O000O ['status']==200 :#line:435
                    return float (O00O00O000O0O000O ['data']['level'])#line:436
        except Exception as OOOOOOOO0O000O00O :#line:437
            print (OOOOOOOO0O000O00O )#line:438
    def propsraffle (O0OO000OOOO0O0O00 ):#line:441
        try :#line:442
            while True :#line:443
                OO0000O00O0OOOO00 =f'__{timi_new()}'#line:444
                O0000O0O0O0OO0000 ={'authorization':O0OO000OOOO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O00O0OOOO00 ),'signstring':OO0000O00O0OOOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:453
                OOOOO00O0O0OOOO0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0000O0O0O0OO0000 ).json ()#line:454
                if 'status'in OOOOO00O0O0OOOO0O :#line:456
                    if OOOOO00O0O0OOOO0O ['status']==200 :#line:457
                        OO000O000O0OO00O0 =OOOOO00O0O0OOOO0O ['data']['rows']#line:458
                        O00O000O000O0O0O0 =OOOOO00O0O0OOOO0O ['data']['vstate']#line:459
                        if OO000O000O0OO00O0 ==5 or OO000O000O0OO00O0 ==6 or OO000O000O0OO00O0 ==7 :#line:460
                            O0OO00000O00O0O0O =OOOOO00O0O0OOOO0O ['data']['silver']#line:461
                            print (f'【转盘抽奖】:获得种子:{O0OO00000O00O0O0O}')#line:462
                        if OO000O000O0OO00O0 ==1 or OO000O000O0OO00O0 ==2 or OO000O000O0OO00O0 ==3 :#line:463
                            O0OOOO00OO0OOOO00 =OOOOO00O0O0OOOO0O ['data']['clover']#line:464
                            print (f'【转盘抽奖】:获得三叶草:{O0OOOO00OO0OOOO00}')#line:465
                        if OO000O000O0OO00O0 ==4 or OO000O000O0OO00O0 ==8 :#line:466
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:467
                        if OO000O000O0OO00O0 =='抽奖次数已用完':#line:471
                            if O00O000O000O0O0O0 :#line:472
                                OO0000O00O0OOOO00 =f'__{timi_new()}'#line:473
                                O0000O0O0O0OO0000 ={'authorization':O0OO000OOOO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O00O0OOOO00 ),'signstring':OO0000O00O0OOOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:482
                                O0000O0OOO00O0O00 =requests .request ('get',f'{host}/user',headers =O0000O0O0O0OO0000 ).json ()#line:483
                                if 'status'in O0000O0OOO00O0O00 :#line:484
                                    if O0000O0OOO00O0O00 ['status']==200 :#line:485
                                        O0OO0O0O0O00OO0O0 =O0000O0OOO00O0O00 ['data']['level']#line:486
                                        if float (O0OO0O0O0O00OO0O0 )>39 :#line:487
                                            OO0O0000OOO00O0OO =random .randint (160 ,190 )/10 #line:488
                                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{OO0O0000OOO00O0OO}秒获取抽奖机会')#line:489
                                            time .sleep (OO0O0000OOO00O0OO )#line:490
                                            OOO00O00000OO00O0 =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O0000O0O0O0OO0000 ).json ()#line:491
                                            if 'status'in OOO00O00000OO00O0 :#line:493
                                                if OOO00O00000OO00O0 ['status']==200 :#line:494
                                                    print (f'【转盘抽奖】:{OOO00O00000OO00O0["message"]}')#line:495
                                                if OOO00O00000OO00O0 ['status']==500 :#line:496
                                                    print (f'【转盘抽奖】:{OOO00O00000OO00O0["message"]}')#line:497
                                                    break #line:498
                                            time .sleep (random .randint (10 ,15 )/10 )#line:499
                                        else :#line:500
                                            break #line:501
                            else :#line:502
                                break #line:503
                time .sleep (random .randint (8 ,15 )/10 )#line:504
        except Exception as O0O0O000O00000000 :#line:505
            print (O0O0O000O00000000 )#line:506
    def friends_invitation (OOO0OO000O0O000O0 ):#line:509
        try :#line:510
            O00O0O000O0O0O000 =f'__{timi_new()}'#line:511
            O0000OO000O0000OO ={'authorization':OOO0OO000O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O000O0O0O000 ),'signstring':O00O0O000O0O0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:520
            OOOO0O000OOOO0000 =requests .request ('get',f'{host}/friends',headers =O0000OO000O0000OO ).json ()#line:521
            if 'status'in OOOO0O000OOOO0000 :#line:522
                if OOOO0O000OOOO0000 ['status']==200 :#line:523
                    OO0O00OOO0O00O00O =OOOO0O000OOOO0000 ['data']['myInviteter']#line:524
                    if OO0O00OOO0O00O00O :#line:525
                        O00O0000O000O00OO =OO0O00OOO0O00O00O ['user']['nickname']#line:526
                        OOOO0OO00OOO0O0OO =OOO0OO000O0O000O0 .certification ()#line:527
                        print (f'【查邀请人】:我的邀请人:{O00O0000O000O00OO}丨实名:{OOOO0OO00OOO0O0OO}')#line:528
                    else :#line:529
                        if OOO0OO000O0O000O0 .innerId !='0':#line:530
                            O00O0O000O0O0O000 =f'_innerId=1937553_{timi_new()}'#line:531
                            O0000OO000O0000OO ={'authorization':OOO0OO000O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O000O0O0O000 ),'signstring':O00O0O000O0O0O000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:540
                            O00O00O000O0O0O00 ={"innerId":'1937553'}#line:541
                            OO0O00O0000O0O0O0 =requests .request ('post',f'{host}/friends/my-invitation',headers =O0000OO000O0000OO ,data =O00O00O000O0O0O00 ).json ()#line:543
        except Exception as O0O0000O00O00O0O0 :#line:544
            print (O0O0000O00O00O0O0 )#line:545
    def add_clover (OOO000000OOO0OOO0 ):#line:548
        global golden_seed #line:549
        try :#line:550
            OO0O00OOO00O0O0O0 =f'__{timi_new()}'#line:551
            OO00OO00OO000OO0O ={'authorization':OOO000000OOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOO00O0O0O0 ),'signstring':OO0O00OOO00O0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:560
            O0O00000OO0O0O0O0 =requests .request ('get',f'{host}/assets/clovers',headers =OO00OO00OO000OO0O ).json ()#line:561
            if 'status'in O0O00000OO0O0O0O0 :#line:563
                if O0O00000OO0O0O0O0 ['status']==200 :#line:564
                    O0OOO0O0OOOOOO00O =O0O00000OO0O0O0O0 ['data']['clover']#line:565
                    O0O00000OO0O00OOO =O0O00000OO0O0O0O0 ['data']['used_clover']#line:566
                    OOO00O0O0OOOOO0OO =float (O0OOO0O0OOOOOO00O )-float (O0O00000OO0O00OOO )#line:567
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0O00000OO0O00OOO}')#line:568
                    if OOO00O0O0OOOOO0OO >1 :#line:569
                        OO0O00OOO00O0O0O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO00O0O0OOOOO0OO)}_{timi_new()}'#line:570
                        OO00OO00OO000OO0O ={'authorization':OOO000000OOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOO00O0O0O0 ),'signstring':OO0O00OOO00O0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:579
                        OOO0O0O0000OOOOO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO00O0O0OOOOO0OO )}#line:580
                        O0000OO0OO00O0OO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO00OO00OO000OO0O ,data =OOO0O0O0000OOOOO0 ).json ()#line:581
                        if 'status'in O0000OO0OO00O0OO0 :#line:583
                            if O0000OO0OO00O0OO0 ['status']==200 :#line:584
                                print (f'【参与抽奖】:添加三叶草:{O0000OO0OO00O0OO0["data"]}丨数量:{OOO00O0O0OOOOO0OO}')#line:585
            O0OOOO0O0O0OOOOO0 =requests .request ('get',f'{host}/lottery',headers =OO00OO00OO000OO0O ).json ()#line:586
            OO000OOO00O0000O0 =OOO000000OOO0OOO0 .winning_rewards ()#line:588
            if 'status'in O0OOOO0O0O0OOOOO0 :#line:589
                if O0OOOO0O0O0OOOOO0 ['status']==200 :#line:590
                    O0000O0O0OO00O000 =O0OOOO0O0O0OOOOO0 ['data'][0 ]['day_get_gold_quantity']#line:591
                    golden_seed +=float (O0000O0O0OO00O000 )#line:592
                    print (f'【参与抽奖】:预计每天中{O0000O0O0OO00O000[:6]}颗金种子丨好友收益:{str(OO000OOO00O0000O0)[:6]}')#line:593
        except Exception as O0O0O00OO000O0000 :#line:594
            print (O0O0O00OO000O0000 )#line:595
    def energy (OOO0O000OOO0O0O00 ):#line:598
        O0O000000O0OOO00O =f'__{timi_new()}'#line:599
        O0O00OO000OOOOOOO ={'authorization':OOO0O000OOO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000000O0OOO00O ),'signstring':O0O000000O0OOO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:608
        O00OOO0O0OO000OO0 =requests .request ('get',f'{host}/energy/general',headers =O0O00OO000OOOOOOO ).json ()#line:609
        if 'status'in O00OOO0O0OO000OO0 :#line:611
            if O00OOO0O0OO000OO0 ['status']==200 :#line:612
                OOOOOO0O0O0O0O0OO =O00OOO0O0OO000OO0 ['data']['ordinary_water_consumptions']#line:613
                if float (OOOOOO0O0O0O0O0OO )<80 :#line:614
                    OOOOO0OOOO00O00OO =99 -float (OOOOOO0O0O0O0O0OO )#line:615
                    O0O00O0O000OOO00O ={"fertilizer":str (OOOOO0OOOO00O00OO ).split ('.')[0 ]}#line:616
                    O000O00O00OOO000O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0O00OO000OOOOOOO ,data =O0O00O0O000OOO00O ).json ()#line:617
                    if 'status'in O000O00O00OOO000O :#line:619
                        if O000O00O00OOO000O ['status']==200 :#line:620
                            print (f'【购买肥料】:{O000O00O00OOO000O["message"]}')#line:621
                O0OOO0O00OO00O0OO =O00OOO0O0OO000OO0 ['data']['ordinary_water_consumptions']#line:622
                if float (O0OOO0O00OO00O0OO )<800 :#line:623
                    OO0O0OOOO0O0OOOO0 =999 -float (O0OOO0O00OO00O0OO )#line:624
                    O000O00O0OOO0OO0O ={"water":str (OO0O0OOOO0O0OOOO0 ).split ('.')[0 ]}#line:625
                    OO000OOOO000000OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O00OO000OOOOOOO ,data =O000O00O0OOO0OO0O ).json ()#line:626
                    if 'status'in OO000OOOO000000OO :#line:627
                        if OO000OOOO000000OO ['status']==200 :#line:628
                            print (f'【购买水滴】:{OO000OOOO000000OO["message"]}')#line:629
def version_of_the_validation ():#line:633
    return str ((67 -56 )/10 )#line:634
def gitee_validation ():#line:637
    try :#line:638
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:639
    except Exception as O0OO0O0OO0O000OO0 :#line:640
        sys .exit (0 )#line:641
def update_the_validation ():#line:645
    try :#line:646
        OO00O0O0O00OO0O0O =gitee_validation ()#line:647
        if version_of_the_validation ()<OO00O0O0O00OO0O0O ['CityEarth']['edition']:#line:648
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O0O0O00OO0O0O["CityEarth"]["edition"]}   ❌')#line:649
            print (f'更新内容=>>{OO00O0O0O00OO0O0O["CityEarth"]["content"]}   👍')#line:650
        else :#line:651
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O0O0O00OO0O0O["CityEarth"]["edition"]}   ✅')#line:652
            print (f'更新内容=>> {OO00O0O0O00OO0O0O["CityEarth"]["content"]}   👍')#line:653
    except Exception as OO0000000OO00OO0O :#line:654
        print (OO0000000OO00OO0O )#line:655
def os_qinglong ():#line:658
    if application in os .environ :#line:659
        OO0O0O000O000OO0O =os .environ [application ].split ('\n')#line:660
        if len (OO0O0O000O000OO0O )>0 :#line:661
            return OO0O0O000O000OO0O #line:662
        else :#line:663
            print (f"{application}变量未启用")#line:664
            print ('脚本退出')#line:665
            sys .exit (1 )#line:666
    else :#line:667
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:669
        return os_built ()#line:670
def os_built ():#line:673
    if token :#line:674
        O0O0O0OOOOO000OOO =token .split ('\n')#line:675
        if len (O0O0O0OOOOO000OOO )>0 :#line:676
            return O0O0O0OOOOO000OOO #line:677
    else :#line:678
        print (f"内置变量为空")#line:679
        print ('脚本结束')#line:680
        sys .exit (0 )#line:681
if __name__ =='__main__':#line:684
    start ()#line:685
