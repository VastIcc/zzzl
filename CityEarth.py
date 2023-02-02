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
@ 版本  1.4
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
        O000O00O000OOOO0O =os_qinglong ()#line:7
        print (f"==========共找到{len(O000O00O000OOOO0O)}个账号==========")#line:8
        for O000O000O000000OO in O000O00O000OOOO0O :#line:9
            print (f"------------正在执行第{O000O00O000OOOO0O.index(O000O000O000000OO) + 1}个账号------------")#line:10
            OOOO0O00OOOOOO0OO =CityEarth (O000O000O000000OO )#line:11
            def OO0000OOOO0000000 ():#line:13
                if OOOO0O00OOOOOO0OO .base_info ():#line:15
                    OOOO0O00OOOOOO0OO .game_map ()#line:19
                    OOOO0O00OOOOOO0OO .friends_invitation ()#line:21
                    OOOO0O00OOOOOO0OO .add_clover ()#line:23
                    OOOO0O00OOOOOO0OO .energy ()#line:25
                    OOOO0O00OOOOOO0OO .propsraffle ()#line:27
                    OOOO0O00OOOOOO0OO .synthetic ()#line:29
                    OOOO0O00OOOOOO0OO .crops_illustrated ()#line:31
                    OOOO0O00OOOOOO0OO .give_gold ()#line:33
                else :#line:34
                    print ('token失效')#line:35
            OOO00000OOOO00OOO =threading .Thread (target =OO0000OOOO0000000 )#line:37
            OOO00000OOOO00OOO .start ()#line:38
            time .sleep (time_xx )#line:39
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:41
        time .sleep (3 )#line:42
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:43
    except Exception as OOO0000O0OOO0OOO0 :#line:44
        print (OOO0000O0OOO0OOO0 )#line:45
def sign (OO0O0000OOO0OOOO0 ):#line:48
    OO000O0O0O00OO000 =hashlib .md5 (OO0O0000OOO0OOOO0 .encode ()).hexdigest ()#line:49
    OO000OOO0O0OO00O0 ="scsc%^&*"+OO000O0O0O00OO000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:50
    OOO0O0OOO000000OO =hashlib .md5 (OO000OOO0O0OO00O0 .encode ()).hexdigest ()#line:51
    return OOO0O0OOO000000OO #line:52
def timi_new ():#line:55
    return str (int (time .time ()*1000 ))#line:56
class CityEarth :#line:58
    def __init__ (OO000OOO0O00O000O ,OOO00OO0O0OOO0OO0 ):#line:60
        try :#line:61
            OO000OOO0O00O000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:62
            OO000OOO0O00O000O .token =OOO00OO0O0OOO0OO0 .split ('&')[0 ]#line:63
            OO000OOO0O00O000O .innerId =OOO00OO0O0OOO0OO0 .split ('&')[1 ]#line:64
            OO000OOO0O00O000O .doneeNo =OOO00OO0O0OOO0OO0 .split ('&')[2 ]#line:65
        except :#line:66
            print ('变量格式错误')#line:67
    def base_info (O0OOO0OOOOOOO0000 ):#line:70
        try :#line:71
            O00O0O0O0OOO0OOOO =f'__{timi_new()}'#line:72
            O0OOOOOO00OO00OO0 ={'authorization':O0OOO0OOOOOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O0OOO0OOOO ),'signstring':O00O0O0O0OOO0OOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:81
            OOO00OO0OOOO00O0O =requests .request ('get',f'{host}/user',headers =O0OOOOOO00OO00OO0 ).json ()#line:82
            if 'status'in OOO00OO0OOOO00O0O :#line:84
                if OOO00OO0OOOO00O0O ['status']==200 :#line:85
                    O0OOO00O0OO0OO000 =OOO00OO0OOOO00O0O ['data']['nickname']#line:86
                    OOOOO0OOOO0OOOOO0 =OOO00OO0OOOO00O0O ['data']['inner_id']#line:87
                    OO000O000OOO0OOOO =OOO00OO0OOOO00O0O ['data']['assets']['gold']#line:88
                    O00OO00OOO0000O00 =OOO00OO0OOOO00O0O ['data']['level']#line:89
                    print (f'【账号信息】:昵称:{O0OOO00O0OO0OO000[:5]}丨ID:{OOOOO0OOOO0OOOOO0}丨等级:{O00OO00OOO0000O00}丨种子:{str(OO000O000OOO0OOOO).split(".")[0]}')#line:90
                if OOO00OO0OOOO00O0O ['status']==401 :#line:91
                    return False #line:92
                if OOO00OO0OOOO00O0O ['status']==500 :#line:93
                    return False #line:94
            return True #line:95
        except Exception as O000O00O0000O0O0O :#line:96
            print (O000O00O0000O0O0O )#line:97
    def game_map (OOOO0OOOO00O0OO00 ):#line:100
        try :#line:101
            OOOO00OOOO0OOOO00 =f'__{timi_new()}'#line:102
            OOOO0O0OOOO00OO0O ={'authorization':OOOO0OOOO00O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOOO0OOOO00 ),'signstring':OOOO00OOOO0OOOO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:111
            OO0OO0OO0OO0O0OOO =requests .request ('get',f'{host}/game/map',headers =OOOO0O0OOOO00OO0O ).json ()#line:112
            if 'status'in OO0OO0OO0OO0O0OOO :#line:114
                if OO0OO0OO0OO0O0OOO ['status']==200 :#line:115
                    for O000O0O0OOOO0OOO0 in OO0OO0OO0OO0O0OOO ['data']['list'][0 ]['crops']:#line:116
                        O0000O0O00000O00O =O000O0O0OOOO0OOO0 ['level']#line:118
                        if O0000O0O00000O00O ==41 :#line:119
                            OOOOO00O000O0O0O0 =O000O0O0OOOO0OOO0 ['crop_name']#line:120
                            OOOO0O0OO00OO0O00 =O000O0O0OOOO0OOO0 ['count']#line:121
                            if OOOO0O0OO00OO0O00 >0 :#line:122
                                print (f'【农业资产】:{OOOOO00O000O0O0O0}丨数量:{OOOO0O0OO00OO0O00}')#line:123
        except Exception as O00O0O0OOOOOOOOOO :#line:124
            print (O00O0O0OOOOOOOOOO )#line:125
    def give_gold (O0O00OOOO0OOOOO0O ):#line:129
        try :#line:130
            OOOO00OOOOOO0OOO0 =f'__{timi_new()}'#line:131
            OOO0000OOO00O00OO ={'authorization':O0O00OOOO0OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOOOOO0OOO0 ),'signstring':OOOO00OOOOOO0OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:140
            OO00OOO0O00OO000O =requests .request ('get',f'{host}/user',headers =OOO0000OOO00O00OO ).json ()#line:141
            if 'status'in OO00OOO0O00OO000O :#line:142
                if OO00OOO0O00OO000O ['status']==200 :#line:143
                    if float (O0O00OOOO0OOOOO0O .doneeNo )!=0 :#line:144
                        OO0OO0OOOOOOO0OO0 =OO00OOO0O00OO000O ['data']['assets']['gold']#line:145
                        if float (OO0OO0OOOOOOO0OO0 )>float (O0O00OOOO0OOOOO0O .innerId ):#line:146
                            OOO00O0000O0O0OO0 =int (float (OO0OO0OOOOOOO0OO0 )/1.1 )#line:147
                            OOOO00OOOOOO0OOO0 =f'_doneeNo={O0O00OOOO0OOOOO0O.doneeNo}&quantity={OOO00O0000O0O0OO0}_{timi_new()}'#line:148
                            OOO0000OOO00O00OO ={'authorization':O0O00OOOO0OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOOOOO0OOO0 ),'signstring':OOOO00OOOOOO0OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:157
                            OOO000OO0OO00O000 ={"quantity":OOO00O0000O0O0OO0 ,"doneeNo":O0O00OOOO0OOOOO0O .doneeNo }#line:161
                            OO00O00O000O0OO00 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0000OOO00O00OO ,data =OOO000OO0OO00O000 ).json ()#line:162
                            if 'status'in OO00O00O000O0OO00 :#line:164
                                if OO00O00O000O0OO00 ['status']==200 :#line:165
                                    if OO00O00O000O0OO00 ['data']:#line:166
                                        print (f'【赠送种子】:赠送{OOO00O0000O0O0OO0}种子给{O0O00OOOO0OOOOO0O.doneeNo}成功')#line:167
                    else :#line:168
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:169
        except Exception as OOOO00OOOOO0O000O :#line:170
            print (OOOO00OOOOO0O000O )#line:171
    def invitation (O0O000O0O000000OO ):#line:174
        try :#line:175
            _O00O00OOOOO00O000 =float (bundled_def ())/4 #line:176
            OO00OOO0O00O0OO00 =f'_innerId={int(_O00O00OOOOO00O000)}_{timi_new()}'#line:177
            O0OO0OO0000000OO0 ={'authorization':O0O000O0O000000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO0O00O0OO00 ),'signstring':OO00OOO0O00O0OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
            OOOOOOOOO0OO0O00O ={"innerId":int (_O00O00OOOOO00O000 )}#line:187
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0OO0OO0000000OO0 ,data =OOOOOOOOO0OO0O00O )#line:188
        except Exception as O00OOOO00OOO00O0O :#line:189
            print (O00OOOO00OOO00O0O )#line:190
    def winning_rewards (O0O0OO0O00OOO0O00 ):#line:195
        try :#line:196
            O000OO00O00O00O00 =f'__{timi_new()}'#line:197
            OOO0000OO0O0OO0O0 ={'authorization':O0O0OO0O00OOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00O00O00O00 ),'signstring':O000OO00O00O00O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:206
            O00OO0OOOO0OO00OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO0000OO0O0OO0O0 ).json ()#line:207
            if 'status'in O00OO0OOOO0OO00OO :#line:209
                if O00OO0OOOO0OO00OO ['status']==200 :#line:210
                    if O00OO0OOOO0OO00OO ['data']['amount']:#line:211
                        OOOO00OO0O0O000O0 =O00OO0OOOO0OO00OO ['data']['amount']['gold']#line:212
                        return OOOO00OO0O0O000O0 #line:213
                    else :#line:214
                        return 0 #line:215
        except Exception as O0O00OOOO00O00O0O :#line:216
            print (O0O00OOOO00O00O0O )#line:217
    def certification (O0O0O000OO0O0O00O ):#line:221
        try :#line:222
            OOO0O00O0OO000OOO =f'__{timi_new()}'#line:223
            O00000O00O00OOO0O ={'authorization':O0O0O000OO0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00O0OO000OOO ),'signstring':OOO0O00O0OO000OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:232
            OOO000000O00O0O00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00000O00O00OOO0O ).json ()#line:233
            if 'status'in OOO000000O00O0O00 :#line:235
                if OOO000000O00O0O00 ['status']==200 :#line:236
                    if OOO000000O00O0O00 ['data']['result']:#line:237
                        O00O0OOOOOO000000 =OOO000000O00O0O00 ['data']['nick_name']#line:238
                        return O00O0OOOOOO000000 #line:239
                    else :#line:240
                        return '未实名'#line:241
        except Exception as O00O000OO000OO00O :#line:242
            print (O00O000OO000OO00O )#line:243
    def crops_illustrated (OOO00OOO0OO0O000O ):#line:247
        try :#line:248
            O000OOO00O00OOOO0 =f'__{timi_new()}'#line:249
            OO0O0O0OO0OOOO0O0 ={'authorization':OOO00OOO0OO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO00O00OOOO0 ),'signstring':O000OOO00O00OOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:258
            OOO0O00OO00000000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O0O0OO0OOOO0O0 ).json ()#line:259
            if 'status'in OOO0O00OO00000000 :#line:261
                if OOO0O00OO00000000 ['status']==200 :#line:262
                    O00OOOOOO000O0OO0 =OOO0O00OO00000000 ['data'][0 ]['crops']#line:263
                    for O000000O0O0OO00OO in O00OOOOOO000O0OO0 :#line:264
                        if O000000O0O0OO00OO ['ill_clover_award']:#line:265
                            if float (O000000O0O0OO00OO ['ill_clover_award'])>1 :#line:266
                                if O000000O0O0OO00OO ['is_finish']:#line:267
                                    if not O000000O0O0OO00OO ['is_getit']:#line:268
                                        if OOO00OOO0OO0O000O .certification ()!='未实名':#line:269
                                            O000OOO00O00OOOO0 =f'_award_level={O000000O0O0OO00OO["level"]}_{timi_new()}'#line:270
                                            OO0O0O0OO0OOOO0O0 ={'authorization':OOO00OOO0OO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO00O00OOOO0 ),'signstring':O000OOO00O00OOOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:279
                                            O0000O0OOOO00000O ={"award_level":O000000O0O0OO00OO ['level']}#line:280
                                            O0O00O00O00000O0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O0O0OO0OOOO0O0 ,json =O0000O0OOOO00000O ).json ()#line:282
                                            if 'status'in O0O00O00O00000O0O :#line:283
                                                if O0O00O00O00000O0O ['status']==200 :#line:284
                                                    O00000000O000OO0O =O0O00O00O00000O0O ['data']['ill_clover_award']#line:285
                                                    print (f'【图鉴奖励】:领取{O000000O0O0OO00OO["crop_name"]}成就丨奖励{O00000000O000OO0O}叶子成功')#line:287
                                                if O0O00O00O00000O0O ['status']==500 :#line:288
                                                    print (f'【图鉴奖励】:{O0O00O00O00000O0O["message"]}')#line:289
        except Exception as O00O0OOO0O000OOOO :#line:290
            print (O00O0OOO0O000OOOO )#line:291
    def watched_ad (OOO00O0O00O0OOOOO ):#line:295
        try :#line:296
            O00OOOO000O000OOO =f'__{timi_new()}'#line:297
            OO000O0O0O00O0OOO ={'authorization':OOO00O0O00O0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO000O000OOO ),'signstring':O00OOOO000O000OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:306
            O0O000000OOO0OOO0 =requests .request ('post',f'{host}/game/watched-ad',headers =OO000O0O0O00O0OOO ).json ()#line:307
            print (O0O000000OOO0OOO0 )#line:308
        except Exception as OOOOOOOOO0O0OO00O :#line:309
            print (OOOOOOOOO0O0OO00O )#line:310
    def user_ad (OO000OOOOOO0OO000 ):#line:314
        try :#line:315
            OOO0OO000O0OO00OO =f'__{timi_new()}'#line:316
            OO00O00O0O0O00O0O ={'authorization':OO000OOOOOO0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO000O0OO00OO ),'signstring':OOO0OO000O0OO00OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:325
            O0O0OOO0OOOO0O0O0 =requests .request ('get',f'{host}/user/ad',headers =OO00O00O0O0O00O0O ).json ()#line:326
            if 'status'in O0O0OOO0OOOO0O0O0 :#line:328
                if O0O0OOO0OOOO0O0O0 ['status']==200 :#line:329
                    O0000OO0OO00O000O =O0O0OOO0OOOO0O0O0 ['data']['max_time']#line:330
                    OO0O0O0OO0OOOOOO0 =O0O0OOO0OOOO0O0O0 ['data']['watch_time']#line:331
                    O00O0O000OOOOO0OO =O0O0OOO0OOOO0O0O0 ['data']['added_time']#line:332
                    print (f'【获取种子】:获取种子剩余{O00O0O000OOOOO0OO + O0000OO0OO00O000O - OO0O0O0OO0OOOOOO0}次丨好友提供:{O00O0O000OOOOO0OO}次')#line:333
                    if O00O0O000OOOOO0OO +O0000OO0OO00O000O -OO0O0O0OO0OOOOOO0 >0 :#line:334
                        time .sleep (random .randint (16 ,19 ))#line:335
                        O0O000000OOO0O0O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO00O00O0O0O00O0O ).json ()#line:336
                        if 'status'in O0O000000OOO0O0O0 :#line:338
                            if O0O000000OOO0O0O0 ['status']==200 :#line:339
                                OOO0O0O0000OO00OO =O0O000000OOO0O0O0 ['data']['silver']#line:340
                                print (f'【获取种子】:获得种子:{OOO0O0O0000OO00OO}')#line:341
                                return True #line:342
                            if O0O000000OOO0O0O0 ['status']==500 :#line:343
                                OOO0O0O00O0O000OO =O0O000000OOO0O0O0 ['message']#line:344
                                print (f'【获取种子】:{OOO0O0O00O0O000OO}')#line:345
                                return False #line:346
        except Exception as O00O0OO000OOO00OO :#line:347
            print (O00O0OO000OOO00OO )#line:348
    def synthetic (OOO00OO0OO0OOOOO0 ):#line:352
        global id ,g #line:353
        try :#line:354
            OOO0O000000O0O000 =OOO00OO0OO0OOOOO0 .level_new ()#line:355
            while True :#line:356
                OO0000OO000O0OOO0 =f'__{timi_new()}'#line:357
                O0OOO0000OO0O0000 ={'authorization':OOO00OO0OO0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OO000O0OOO0 ),'signstring':OO0000OO000O0OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:366
                O0O000O00OOOOO000 =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0000OO0O0000 ).json ()#line:367
                if 'status'in O0O000O00OOOOO000 :#line:369
                    if O0O000O00OOOOO000 ['status']==200 :#line:370
                        OOOO0O0O0O0OO00OO =O0O000O00OOOOO000 ['data']['cropList']#line:371
                        OO0OOOOOO0O00O00O =O0O000O00OOOOO000 ['data']['gameCoreDataDBid']#line:372
                        O0O0O0OOOOO000OOO =0 #line:373
                        for OO00000O000O000OO in OOOO0O0O0O0OO00OO :#line:374
                            if not OO00000O000O000OO :#line:375
                                OOOOO0OO00O0OOOOO =f'_crop_id={OO0OOOOOO0O00O00O}&site={O0O0O0OOOOO000OOO}_{OOO00OO0OO0OOOOO0.time}'#line:376
                                O000OO00O0OOOO0O0 ={'authorization':OOO00OO0OO0OOOOO0 .token ,'timestamp':OOO00OO0OO0OOOOO0 .time ,'sign':sign (OOOOO0OO00O0OOOOO ),'signstring':OOOOO0OO00O0OOOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:385
                                O0O0O0OOO0OOOOO00 ={"site":O0O0O0OOOOO000OOO ,"crop_id":OO0OOOOOO0O00O00O }#line:386
                                O0O0OOO00OO0O0OO0 =requests .request ('post',f'{host}/game/crops/buy',headers =O000OO00O0OOOO0O0 ,data =O0O0O0OOO0OOOOO00 ).json ()#line:387
                                time .sleep (random .randint (1 ,3 )/10 )#line:389
                                if 'status'in O0O0OOO00OO0O0OO0 :#line:390
                                    if O0O0OOO00OO0O0OO0 ['status']==200 :#line:391
                                        if O0O0OOO00OO0O0OO0 ['message']=='种子数量不足':#line:392
                                            OOO0O000000O0O000 =OOO00OO0OO0OOOOO0 .level_new ()#line:393
                                            print (f'【种植合成】:{O0O0OOO00OO0O0OO0["message"]}')#line:394
                                            if not OOO00OO0OO0OOOOO0 .user_ad ():#line:395
                                                return False #line:396
                                        print (f'【种植合成】:种植农作物,位置{O0O0O0OOOOO000OOO}')#line:397
                                    if O0O0OOO00OO0O0OO0 ['status']==500 :#line:398
                                        print (f'【种植合成】:{O0O0OOO00OO0O0OO0["message"]}')#line:399
                                        return False #line:400
                            O0O0O0OOOOO000OOO +=1 #line:401
                        OOOOO0OO0O000OO0O =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0000OO0O0000 ).json ()#line:402
                        OO0OO0OOOOO00OOO0 =OOOOO0OO0O000OO0O ['data']['cropList']#line:403
                        OO000OOOOO000OO0O =False #line:404
                        for OO00000O000O000OO in range (12 ):#line:405
                            id =OO0OO0OOOOO00OOO0 [OO00000O000O000OO ]['level']#line:406
                            if float (OOO0O000000O0O000 )-float (id )>9 :#line:407
                                O0OO00OOO00O00O00 =f'_site={OO00000O000O000OO}_{timi_new()}'#line:408
                                O0000O00OO0000OO0 ={'accept':'application/json, text/plain, */*','authorization':OOO00OO0OO0OOOOO0 .token ,'timestamp':timi_new (),'sign':sign (O0OO00OOO00O00O00 ),'signstring':O0OO00OOO00O00O00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:418
                                O0000O000OOO00OOO ={"site":OO00000O000O000OO }#line:419
                                O00OOO0OOO00OO000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0000O00OO0000OO0 ,data =O0000O000OOO00OOO ).json ()#line:421
                                if 'status'in O00OOO0OOO00OO000 :#line:422
                                    if O00OOO0OOO00OO000 ['status']==200 :#line:423
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:424
                            if id !=0 :#line:425
                                for OO0O0OOOO0O000O0O in range (11 ):#line:426
                                    OO0000O0000000000 =OO0O0OOOO0O000O0O +1 #line:427
                                    g =OO0OO0OOOOO00OOO0 [OO0000O0000000000 ]['level']#line:428
                                    if id ==g :#line:429
                                        OO0000O000OOO0O00 =OO0O0OOOO0O000O0O +2 #line:430
                                        if OO0000O000OOO0O00 ==OO00000O000O000OO +1 :#line:431
                                            pass #line:432
                                        else :#line:433
                                            O00O0O0000000000O =OO00000O000O000OO +1 #line:434
                                            time .sleep (random .randint (1 ,3 )/10 )#line:436
                                            OO0O0OO00O0O0000O =f'_site={O00O0O0000000000O - 1}&targetSite={OO0000O000OOO0O00 - 1}_{timi_new()}'#line:437
                                            O00OOOOOO000OO000 ={'accept':'application/json, text/plain, */*','authorization':OOO00OO0OO0OOOOO0 .token ,'timestamp':timi_new (),'sign':sign (OO0O0OO00O0O0000O ),'signstring':OO0O0OO00O0O0000O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:452
                                            O0OO0OOO000OO0000 ={"site":int (O00O0O0000000000O -1 ),"targetSite":int (OO0000O000OOO0O00 -1 )}#line:453
                                            OOOO0OO00O000OOO0 =requests .request ('post',f'{host}/game/crops/move',headers =O00OOOOOO000OO000 ,json =O0OO0OOO000OO0000 ).json ()#line:455
                                            if 'status'in OOOO0OO00O000OOO0 :#line:456
                                                if OOOO0OO00O000OOO0 ['status']==200 :#line:457
                                                    pass #line:458
                                            print ('【种植合成】:',O00O0O0000000000O ,OO0000O000OOO0O00 ,'合成成功')#line:460
                                            OO000OOOOO000OO0O =True #line:461
                                    if OO000OOOOO000OO0O :#line:462
                                        break #line:463
                                if OO000OOOOO000OO0O :#line:464
                                    break #line:465
        except Exception as O0OOO00OO0OOO000O :#line:466
            OOO00OO0OO0OOOOO0 .synthetic ()#line:467
    def level_new (O00O00000O0OO000O ):#line:470
        try :#line:471
            OO0OOO0O0OOO000O0 =f'__{timi_new()}'#line:472
            OOO00OO0OO0OOO0OO ={'authorization':O00O00000O0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O0OOO000O0 ),'signstring':OO0OOO0O0OOO000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:481
            O0O0OOOO00O00000O =requests .request ('get',f'{host}/user',headers =OOO00OO0OO0OOO0OO ).json ()#line:482
            if 'status'in O0O0OOOO00O00000O :#line:483
                if O0O0OOOO00O00000O ['status']==200 :#line:484
                    return float (O0O0OOOO00O00000O ['data']['level'])#line:485
        except Exception as OOOO0O0OOOO00OOOO :#line:486
            print (OOOO0O0OOOO00OOOO )#line:487
    def propsraffle (O0OO0O000OOO0O00O ):#line:490
        try :#line:491
            while True :#line:492
                O0OOO0OOO000O0OOO =f'__{timi_new()}'#line:493
                O0O0000000O0O0O00 ={'authorization':O0OO0O000OOO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OOO000O0OOO ),'signstring':O0OOO0OOO000O0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:502
                OO00O0O0OOO00O0OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O0000000O0O0O00 ).json ()#line:503
                if 'status'in OO00O0O0OOO00O0OO :#line:505
                    if OO00O0O0OOO00O0OO ['status']==200 :#line:506
                        OOO0O0O0OOOOOO0OO =OO00O0O0OOO00O0OO ['data']['rows']#line:507
                        OO000000O0OOO0O00 =OO00O0O0OOO00O0OO ['data']['vstate']#line:508
                        if OOO0O0O0OOOOOO0OO ==5 or OOO0O0O0OOOOOO0OO ==6 or OOO0O0O0OOOOOO0OO ==7 :#line:509
                            OOO0OO000O0000OO0 =OO00O0O0OOO00O0OO ['data']['silver']#line:510
                            print (f'【转盘抽奖】:获得种子:{OOO0OO000O0000OO0}')#line:511
                        if OOO0O0O0OOOOOO0OO ==1 or OOO0O0O0OOOOOO0OO ==2 or OOO0O0O0OOOOOO0OO ==3 :#line:512
                            OO0O0O000O00OO0O0 =OO00O0O0OOO00O0OO ['data']['clover']#line:513
                            print (f'【转盘抽奖】:获得三叶草:{OO0O0O000O00OO0O0}')#line:514
                        if OOO0O0O0OOOOOO0OO ==4 or OOO0O0O0OOOOOO0OO ==8 :#line:515
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:516
                        if OOO0O0O0OOOOOO0OO =='抽奖次数已用完':#line:520
                            break #line:553
                time .sleep (random .randint (8 ,15 )/10 )#line:554
        except Exception as OO0OOOOOO00O0OOO0 :#line:555
            print (OO0OOOOOO00O0OOO0 )#line:556
    def friends_invitation (OOOOOOO0O00OO0O0O ):#line:560
        try :#line:561
            O0O00O0000O0O0000 =f'__{timi_new()}'#line:562
            OO0OO00O0OOOO0OO0 ={'authorization':OOOOOOO0O00OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0000O0O0000 ),'signstring':O0O00O0000O0O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:571
            O0OOO00000OOO0OOO =requests .request ('get',f'{host}/friends',headers =OO0OO00O0OOOO0OO0 ).json ()#line:572
            if 'status'in O0OOO00000OOO0OOO :#line:573
                if O0OOO00000OOO0OOO ['status']==200 :#line:574
                    O00O0OOOOO0O000OO =O0OOO00000OOO0OOO ['data']['myInviteter']#line:575
                    if O00O0OOOOO0O000OO :#line:576
                        OO0000O0OOO000000 =O00O0OOOOO0O000OO ['user']['nickname']#line:577
                        OO000OOO0OO0O000O =OOOOOOO0O00OO0O0O .certification ()#line:578
                        print (f'【查邀请人】:我的邀请人:{OO0000O0OOO000000}丨实名:{OO000OOO0OO0O000O}')#line:579
                    else :#line:580
                        if OOOOOOO0O00OO0O0O .innerId !='0':#line:581
                            OOOOOOO0O00OO0O0O .invitation ()#line:582
        except Exception as OO0OO0O0O00OO0OOO :#line:583
            print (OO0OO0O0O00OO0OOO )#line:584
    def add_clover (OO00O00O0O0O000O0 ):#line:588
        global golden_seed #line:589
        try :#line:590
            OO0OO0O000O0O0000 =f'__{timi_new()}'#line:591
            O0OOOO0OOOO00O0O0 ={'authorization':OO00O00O0O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O000O0O0000 ),'signstring':OO0OO0O000O0O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            O0O000OO00O0O00O0 =requests .request ('get',f'{host}/assets/clovers',headers =O0OOOO0OOOO00O0O0 ).json ()#line:601
            if 'status'in O0O000OO00O0O00O0 :#line:603
                if O0O000OO00O0O00O0 ['status']==200 :#line:604
                    O0O0O0OO000O00O00 =O0O000OO00O0O00O0 ['data']['clover']#line:605
                    O000O0OOOO0OO0OOO =O0O000OO00O0O00O0 ['data']['used_clover']#line:606
                    OO00OOO000O00O000 =float (O0O0O0OO000O00O00 )-float (O000O0OOOO0OO0OOO )#line:607
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O000O0OOOO0OO0OOO}')#line:608
                    if OO00O00O0O0O000O0 .certification ()!='未实名':#line:609
                        if OO00OOO000O00O000 >1 :#line:610
                            OO0OO0O000O0O0000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO00OOO000O00O000)}_{timi_new()}'#line:611
                            O0OOOO0OOOO00O0O0 ={'authorization':OO00O00O0O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O000O0O0000 ),'signstring':OO0OO0O000O0O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:620
                            OOOOOO0O0OO0O00OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO00OOO000O00O000 )}#line:621
                            O000000O00OO0O0O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OOOO0OOOO00O0O0 ,data =OOOOOO0O0OO0O00OO ).json ()#line:622
                            if 'status'in O000000O00OO0O0O0 :#line:624
                                if O000000O00OO0O0O0 ['status']==200 :#line:625
                                    print (f'【参与抽奖】:添加三叶草:{O000000O00OO0O0O0["data"]}丨数量:{OO00OOO000O00O000}')#line:626
                                if O000000O00OO0O0O0 ['status']==500 :#line:627
                                    print (f'【参与抽奖】:添加三叶草:{O000000O00OO0O0O0["message"]}')#line:628
            O00OO0O0OO00OOOOO =requests .request ('get',f'{host}/lottery',headers =O0OOOO0OOOO00O0O0 ).json ()#line:629
            O0OO0OO00OOOO000O =OO00O00O0O0O000O0 .winning_rewards ()#line:631
            if 'status'in O00OO0O0OO00OOOOO :#line:632
                if O00OO0O0OO00OOOOO ['status']==200 :#line:633
                    OOOO00O000OOO00O0 =O00OO0O0OO00OOOOO ['data'][0 ]['day_get_gold_quantity']#line:634
                    golden_seed +=float (OOOO00O000OOO00O0 )#line:635
                    print (f'【参与抽奖】:预计每天中{str(OOOO00O000OOO00O0)[:6]}颗金种子丨好友收益:{str(O0OO0OO00OOOO000O)[:6]}')#line:636
        except Exception as OO00O0OO0O0OOO0OO :#line:637
            print (OO00O0OO0O0OOO0OO )#line:638
    def energy (OO000OO0000OO0OOO ):#line:641
        OO00O0O0OO00000O0 =f'__{timi_new()}'#line:642
        OO00O00OO000O0O0O ={'authorization':OO000OO0000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0OO00000O0 ),'signstring':OO00O0O0OO00000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:651
        OOO00O0000O0O0O0O =requests .request ('get',f'{host}/energy/general',headers =OO00O00OO000O0O0O ).json ()#line:652
        if 'status'in OOO00O0000O0O0O0O :#line:654
            if OOO00O0000O0O0O0O ['status']==200 :#line:655
                OO00OO00OOO0OOOOO =OOO00O0000O0O0O0O ['data']['ordinary_water']#line:656
                OOO0000OOOO00OO0O =OOO00O0000O0O0O0O ['data']['ordinary_fertilizer']#line:657
                print (f'【我的营养】:肥料:{str(OOO0000OOOO00OO0O).split(".")[0]}丨水滴:{str(OO00OO00OOO0OOOOO).split(".")[0]}')#line:658
                if float (OOO0000OOOO00OO0O )<96 :#line:659
                    time .sleep (random .randint (160 ,180 )/10 )#line:660
                    O0000O0O000O0O0OO =99 -float (OOO0000OOOO00OO0O )#line:661
                    OO0O000OO0OO0O00O ={"fertilizer":str (O0000O0O000O0O0OO ).split ('.')[0 ]}#line:662
                    OO0O0000O00O0OO00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO00O00OO000O0O0O ).json ()#line:663
                    if 'status'in OO0O0000O00O0OO00 :#line:665
                        if OO0O0000O00O0OO00 ['status']==200 :#line:666
                            print (f'【购买肥料】:看广告获取肥料:{OO0O0000O00O0OO00["message"]}')#line:667
                if float (OO00OO00OOO0OOOOO )<880 :#line:668
                    time .sleep (random .randint (160 ,180 )/10 )#line:669
                    OO0O00OOOO00OOO00 =999 -float (OO00OO00OOO0OOOOO )#line:670
                    O0OOO00O0O0O00000 ={"water":str (OO0O00OOOO00OOO00 ).split ('.')[0 ]}#line:671
                    O0O0O000OOO0O0OO0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO00O00OO000O0O0O ).json ()#line:672
                    if 'status'in O0O0O000OOO0O0OO0 :#line:674
                        if O0O0O000OOO0O0OO0 ['status']==200 :#line:675
                            print (f'【购买水滴】:看广告获取水滴:{O0O0O000OOO0O0OO0["message"]}')#line:676
def bundled_def ():#line:679
    OOOOO00OO000OOO0O =['5570536','7750212','7911652','7911680','7805624']#line:680
    return OOOOO00OO000OOO0O [random .randint (0 ,len (OOOOO00OO000OOO0O )-1 )]#line:681
def version_of_the_validation ():#line:685
    return str ((70 -56 )/10 )#line:686
def gitee_validation ():#line:689
    try :#line:690
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:691
    except :#line:692
        sys .exit (0 )#line:693
def update_the_validation ():#line:697
    try :#line:698
        OO0000OOO0OO0OO00 =gitee_validation ()#line:699
        if version_of_the_validation ()<OO0000OOO0OO0OO00 ['CityEarth']['edition']:#line:700
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0000OOO0OO0OO00["CityEarth"]["edition"]}   ❌')#line:701
            print (f'更新内容=>>{OO0000OOO0OO0OO00["CityEarth"]["content"]}   👍')#line:702
        else :#line:703
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0000OOO0OO0OO00["CityEarth"]["edition"]}   ✅')#line:704
            print (f'更新内容=>> {OO0000OOO0OO0OO00["CityEarth"]["content"]}   👍')#line:705
    except Exception as O0OO000OO00OOO0OO :#line:706
        print (O0OO000OO00OOO0OO )#line:707
def os_qinglong ():#line:710
    if application in os .environ :#line:711
        OOO0O0O00000O0000 =os .environ [application ].split ('\n')#line:712
        if len (OOO0O0O00000O0000 )>0 :#line:713
            return OOO0O0O00000O0000 #line:714
        else :#line:715
            print (f"{application}变量未启用")#line:716
            print ('脚本退出')#line:717
            sys .exit (1 )#line:718
    else :#line:719
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:721
        return os_built ()#line:722
def os_built ():#line:725
    if token :#line:726
        OOOOOOOOOOO00000O =token .split ('\n')#line:727
        if len (OOOOOOOOOOO00000O )>0 :#line:728
            return OOOOOOOOOOO00000O #line:729
    else :#line:730
        print (f"内置变量为空")#line:731
        print ('脚本结束')#line:732
        sys .exit (0 )#line:733
if __name__ =='__main__':#line:736
    start ()#line:737
