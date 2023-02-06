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
@ cron: 8 0,1,2,8,12,13,14,15,19,20,21,22 * * *
@ new Env('生城世朝')
@ 项目地址  微信打开  http://share.sc19319.com/scsc/1937553
@ 抓取  http://scsc.sc19319.com 的authorization值
@ 青龙变量  青龙配置文件 export ce_token="authorization&赠送金种子数量大于&赠送金种子id" 
@ 如果你有20金种子填10就会赠 填21就不会赠送  不赠送全填 999999     多号换行
@ 变量示范    export ce_token="557b8069-1234-4ae7-9e29-b7871f91541b&999999&999999"  用&符号分开数据
@ 版本  1.5
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
        O000O00OO00O0O00O =os_qinglong ()#line:7
        print (f"==========共找到{len(O000O00OO00O0O00O)}个账号==========")#line:8
        for O0OOOO0OO00OOO0O0 in O000O00OO00O0O00O :#line:9
            print (f"------------正在执行第{O000O00OO00O0O00O.index(O0OOOO0OO00OOO0O0) + 1}个账号------------")#line:10
            O00O0O00O000OOO00 =CityEarth (O0OOOO0OO00OOO0O0 )#line:11
            def O0OOOO0O0O00O0O00 ():#line:13
                if O00O0O00O000OOO00 .base_info ():#line:15
                    O00O0O00O000OOO00 .invitenum ()#line:19
                    O00O0O00O000OOO00 .game_map ()#line:21
                    O00O0O00O000OOO00 .friends_invitation ()#line:23
                    O00O0O00O000OOO00 .add_clover ()#line:25
                    O00O0O00O000OOO00 .energy ()#line:27
                    O00O0O00O000OOO00 .propsraffle ()#line:29
                    O00O0O00O000OOO00 .crops_illustrated ()#line:33
                    O00O0O00O000OOO00 .give_gold ()#line:35
                    O00O0O00O000OOO00 .withdraw ()#line:37
                else :#line:38
                    print ('token失效')#line:39
            OOOO0OOO0O0O00OO0 =threading .Thread (target =O0OOOO0O0O00O0O00 )#line:41
            OOOO0OOO0O0O00OO0 .start ()#line:42
            time .sleep (time_xx )#line:43
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:45
        time .sleep (3 )#line:46
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:47
    except Exception as OO0OO00OO0OO00000 :#line:48
        print (OO0OO00OO0OO00000 )#line:49
def sign (OO00O000O00O0O00O ):#line:52
    OOO0OOOOOO0O0000O =hashlib .md5 (OO00O000O00O0O00O .encode ()).hexdigest ()#line:53
    O0O000O0OOOO0O0O0 ="scsc%^&*"+OOO0OOOOOO0O0000O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    OOOO0000OO0O0O000 =hashlib .md5 (O0O000O0OOOO0O0O0 .encode ()).hexdigest ()#line:55
    return OOOO0000OO0O0O000 #line:56
def timi_new ():#line:59
    return str (int (time .time ()*1000 ))#line:60
class CityEarth :#line:62
    def __init__ (O00OO0OO0OOO0OO0O ,OOO0OO0OO00000OO0 ):#line:64
        try :#line:65
            O00OO0OO0OOO0OO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:66
            O00OO0OO0OOO0OO0O .token =OOO0OO0OO00000OO0 .split ('&')[0 ]#line:67
            O00OO0OO0OOO0OO0O .innerId =OOO0OO0OO00000OO0 .split ('&')[1 ]#line:68
            O00OO0OO0OOO0OO0O .doneeNo =OOO0OO0OO00000OO0 .split ('&')[2 ]#line:69
        except :#line:70
            print ('变量格式错误')#line:71
    def base_info (O00O0000000O00O00 ):#line:74
        try :#line:75
            O0OO00O0OO00OO00O =f'__{timi_new()}'#line:76
            O0OO0OOO0OO0O00O0 ={'authorization':O00O0000000O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0OO00OO00O ),'signstring':O0OO00O0OO00OO00O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
            O0OOOOOO0OO0OO000 =requests .request ('get',f'{host}/user',headers =O0OO0OOO0OO0O00O0 ).json ()#line:86
            if 'status'in O0OOOOOO0OO0OO000 :#line:88
                if O0OOOOOO0OO0OO000 ['status']==200 :#line:89
                    O000O0O0000OOO0O0 =O0OOOOOO0OO0OO000 ['data']['nickname']#line:90
                    O00OO000O00OO0O0O =O0OOOOOO0OO0OO000 ['data']['inner_id']#line:91
                    OO0OO00O0O0O00O0O =O0OOOOOO0OO0OO000 ['data']['assets']['gold']#line:92
                    O00OO0OO00OO0OO0O =O0OOOOOO0OO0OO000 ['data']['level']#line:93
                    print (f'【账号信息】:昵称:{O000O0O0000OOO0O0[:5]}丨ID:{O00OO000O00OO0O0O}丨等级:{O00OO0OO00OO0OO0O}丨种子:{str(OO0OO00O0O0O00O0O).split(".")[0]}')#line:94
                if O0OOOOOO0OO0OO000 ['status']==401 :#line:95
                    return False #line:96
                if O0OOOOOO0OO0OO000 ['status']==500 :#line:97
                    return False #line:98
            return True #line:99
        except Exception as OOO0O00O0OOOOOOOO :#line:100
            print (OOO0O00O0OOOOOOOO )#line:101
    def withdraw (OO0OOOOO0O00OOO00 ):#line:104
        O00OOO000OOO00000 =f'__{timi_new()}'#line:105
        O000000OOO0OO0000 ={'authorization':OO0OOOOO0O00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO000OOO00000 ),'signstring':O00OOO000OOO00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:114
        O00O0O00OO00000O0 =requests .request ('get',f'{host}/assets',headers =O000000OOO0OO0000 ).json ()#line:115
        if 'status'in O00O0O00OO00000O0 :#line:117
            if O00O0O00OO00000O0 ['status']==200 :#line:118
                OO0OO00000OO000OO =O00O0O00OO00000O0 ['data']['cash']#line:119
                if float (OO0OO00000OO000OO )>20 :#line:120
                    O00OOO000OOO00000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:121
                    O000000OOO0OO0000 ={'authorization':OO0OOOOO0O00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO000OOO00000 ),'signstring':O00OOO000OOO00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:130
                    OOOO0OO0OOOOOO0OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:131
                    OO0000OO0OOOO0000 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O000000OOO0OO0000 ,data =OOOO0OO0OOOOOO0OO ).json ()#line:132
                    print (OO0000OO0OOOO0000 )#line:133
    def invitenum (O00OO0O0O0O0OOOOO ):#line:139
        OO0OO0O0OO0O0000O =f'__{timi_new()}'#line:140
        OOOO0OOO00OOOO0O0 ={'authorization':O00OO0O0O0O0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0OO0O0000O ),'signstring':OO0OO0O0OO0O0000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:149
        OO0O0OO0OO0OO000O =requests .request ('get',f'{host}/invite/invitenum',headers =OOOO0OOO00OOOO0O0 ).json ()#line:150
        if 'status'in OO0O0OO0OO0OO000O :#line:152
            if OO0O0OO0OO0OO000O ['status']==200 :#line:153
                O0O0O0000OO00O0O0 =OO0O0OO0OO0OO000O ['data']['invited_count']#line:154
                OOO0O0O0O0O0OO0OO =OO0O0OO0OO0OO000O ['data']['invited_second_count']#line:155
                print (f'【我的邀请】:直邀好友:{O0O0O0000OO00O0O0}丨间邀好友:{OOO0O0O0O0O0OO0OO}')#line:156
    def game_map (O0O000O000O0O0OO0 ):#line:160
        try :#line:161
            O0OO00OO00OOO0OOO =f'__{timi_new()}'#line:162
            OO000O0OOOO0O0O0O ={'authorization':O0O000O000O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO00OOO0OOO ),'signstring':O0OO00OO00OOO0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:171
            O0O0O0O0O00000OOO =requests .request ('get',f'{host}/game/map',headers =OO000O0OOOO0O0O0O ).json ()#line:172
            if 'status'in O0O0O0O0O00000OOO :#line:174
                if O0O0O0O0O00000OOO ['status']==200 :#line:175
                    for O00O0O0OO0000O000 in O0O0O0O0O00000OOO ['data']['list'][0 ]['crops']:#line:176
                        O00O0O0OO0OO00OOO =O00O0O0OO0000O000 ['level']#line:178
                        if O00O0O0OO0OO00OOO ==41 :#line:179
                            OO00000OOO0O00OO0 =O00O0O0OO0000O000 ['crop_name']#line:180
                            OO000O00O0O000O00 =O00O0O0OO0000O000 ['count']#line:181
                            if OO000O00O0O000O00 >0 :#line:182
                                print (f'【农业资产】:{OO00000OOO0O00OO0}丨数量:{OO000O00O0O000O00}')#line:183
        except Exception as OO00000OOO000O000 :#line:184
            print (OO00000OOO000O000 )#line:185
    def give_gold (OOO0OOOOO00O0OOOO ):#line:189
        try :#line:190
            OO0OO0O000000OO0O =f'__{timi_new()}'#line:191
            O0O0O0000000O0O00 ={'authorization':OOO0OOOOO00O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O000000OO0O ),'signstring':OO0OO0O000000OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:200
            O00OOOOOOOOOOO0O0 =requests .request ('get',f'{host}/user',headers =O0O0O0000000O0O00 ).json ()#line:201
            if 'status'in O00OOOOOOOOOOO0O0 :#line:202
                if O00OOOOOOOOOOO0O0 ['status']==200 :#line:203
                    if float (OOO0OOOOO00O0OOOO .doneeNo )!=0 :#line:204
                        O00O0OO0OO0O0O00O =O00OOOOOOOOOOO0O0 ['data']['assets']['gold']#line:205
                        if float (O00O0OO0OO0O0O00O )>float (OOO0OOOOO00O0OOOO .innerId ):#line:206
                            O0OOOOO0O00OOOO00 =int (float (O00O0OO0OO0O0O00O )/1.1 )#line:207
                            OO0OO0O000000OO0O =f'_doneeNo={OOO0OOOOO00O0OOOO.doneeNo}&quantity={O0OOOOO0O00OOOO00}_{timi_new()}'#line:208
                            O0O0O0000000O0O00 ={'authorization':OOO0OOOOO00O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O000000OO0O ),'signstring':OO0OO0O000000OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:217
                            OOO0OO00OO000O00O ={"quantity":O0OOOOO0O00OOOO00 ,"doneeNo":OOO0OOOOO00O0OOOO .doneeNo }#line:221
                            OOO0OO00OOO0000O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0O0000000O0O00 ,data =OOO0OO00OO000O00O ).json ()#line:222
                            if 'status'in OOO0OO00OOO0000O0 :#line:224
                                if OOO0OO00OOO0000O0 ['status']==200 :#line:225
                                    if OOO0OO00OOO0000O0 ['data']:#line:226
                                        print (f'【赠送种子】:赠送{O0OOOOO0O00OOOO00}种子给{OOO0OOOOO00O0OOOO.doneeNo}成功')#line:227
                    else :#line:228
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:229
        except Exception as OO000O0OOOO0OO00O :#line:230
            print (OO000O0OOOO0OO00O )#line:231
    def invitation (OO00000OO0O0000O0 ):#line:234
        try :#line:235
            _O0O0OO00O0000O0OO =float (bundled_def ())/4 #line:236
            OOOO00OOOOOO000O0 =f'_innerId={int(_O0O0OO00O0000O0OO)}_{timi_new()}'#line:237
            OO0OO00OO0OO00O0O ={'authorization':OO00000OO0O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOOOOO000O0 ),'signstring':OOOO00OOOOOO000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:246
            O0O000O0000OOOO00 ={"innerId":int (_O0O0OO00O0000O0OO )}#line:247
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO0OO00OO0OO00O0O ,data =O0O000O0000OOOO00 )#line:248
        except Exception as OO0O00OO0O0O00OOO :#line:249
            print (OO0O00OO0O0O00OOO )#line:250
    def winning_rewards (OO0O0O0OOO0OOO0O0 ):#line:255
        try :#line:256
            O0OO00O000000000O =f'__{timi_new()}'#line:257
            OOOO0OOOO0O0O0O0O ={'authorization':OO0O0O0OOO0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O000000000O ),'signstring':O0OO00O000000000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:266
            OOOOO0OOO0OOOO0O0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOOO0OOOO0O0O0O0O ).json ()#line:267
            if 'status'in OOOOO0OOO0OOOO0O0 :#line:269
                if OOOOO0OOO0OOOO0O0 ['status']==200 :#line:270
                    if OOOOO0OOO0OOOO0O0 ['data']['amount']:#line:271
                        O0OOOO0O0OOO0O000 =OOOOO0OOO0OOOO0O0 ['data']['amount']['gold']#line:272
                        return O0OOOO0O0OOO0O000 #line:273
                    else :#line:274
                        return 0 #line:275
        except Exception as OOO00OOO0OO0OOOOO :#line:276
            print (OOO00OOO0OO0OOOOO )#line:277
    def certification (OO0OO00OOO0O000O0 ):#line:281
        try :#line:282
            O000O0OO000O0O0O0 =f'__{timi_new()}'#line:283
            OOOOOOOOOO0OOO0O0 ={'authorization':OO0OO00OOO0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO000O0O0O0 ),'signstring':O000O0OO000O0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:292
            OOOO0O00OO0O000O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOOOOOOOOO0OOO0O0 ).json ()#line:293
            if 'status'in OOOO0O00OO0O000O0 :#line:295
                if OOOO0O00OO0O000O0 ['status']==200 :#line:296
                    if OOOO0O00OO0O000O0 ['data']['result']:#line:297
                        O0OOO0O0O00O0000O =OOOO0O00OO0O000O0 ['data']['nick_name']#line:298
                        return O0OOO0O0O00O0000O #line:299
                    else :#line:300
                        return '未实名'#line:301
        except Exception as O0OOO00OOO0OO0O00 :#line:302
            print (O0OOO00OOO0OO0O00 )#line:303
    def crops_illustrated (O00O0O0O0OOOOO0O0 ):#line:307
        try :#line:308
            O000O000OO000OO0O =f'__{timi_new()}'#line:309
            OO00000OOOO0OOO00 ={'authorization':O00O0O0O0OOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000OO000OO0O ),'signstring':O000O000OO000OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:318
            OOO0OO0OOO0OOO00O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO00000OOOO0OOO00 ).json ()#line:319
            if 'status'in OOO0OO0OOO0OOO00O :#line:321
                if OOO0OO0OOO0OOO00O ['status']==200 :#line:322
                    OO00O0O0000OOOO0O =OOO0OO0OOO0OOO00O ['data'][0 ]['crops']#line:323
                    for OO0O00OOOO0000O0O in OO00O0O0000OOOO0O :#line:324
                        if OO0O00OOOO0000O0O ['ill_clover_award']:#line:325
                            if float (OO0O00OOOO0000O0O ['ill_clover_award'])>1 :#line:326
                                if OO0O00OOOO0000O0O ['is_finish']:#line:327
                                    if not OO0O00OOOO0000O0O ['is_getit']:#line:328
                                        if O00O0O0O0OOOOO0O0 .certification ()!='未实名':#line:329
                                            O000O000OO000OO0O =f'_award_level={OO0O00OOOO0000O0O["level"]}_{timi_new()}'#line:330
                                            OO00000OOOO0OOO00 ={'authorization':O00O0O0O0OOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000OO000OO0O ),'signstring':O000O000OO000OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                                            O0OOO000OOO0O0000 ={"award_level":OO0O00OOOO0000O0O ['level']}#line:340
                                            OOO00O0OO00OOO000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO00000OOOO0OOO00 ,json =O0OOO000OOO0O0000 ).json ()#line:342
                                            if 'status'in OOO00O0OO00OOO000 :#line:343
                                                if OOO00O0OO00OOO000 ['status']==200 :#line:344
                                                    O00000OOOO0OO0O0O =OOO00O0OO00OOO000 ['data']['ill_clover_award']#line:345
                                                    print (f'【图鉴奖励】:领取{OO0O00OOOO0000O0O["crop_name"]}成就丨奖励{O00000OOOO0OO0O0O}叶子成功')#line:347
                                                if OOO00O0OO00OOO000 ['status']==500 :#line:348
                                                    print (f'【图鉴奖励】:{OOO00O0OO00OOO000["message"]}')#line:349
        except Exception as O000OO000000OO0O0 :#line:350
            print (O000OO000000OO0O0 )#line:351
    def watched_ad (OO00O0OO0OOOO0OOO ):#line:355
        try :#line:356
            O00OO0O00O0OO0OOO =f'__{timi_new()}'#line:357
            O0O0O0O00OOOOOO00 ={'authorization':OO00O0OO0OOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O00O0OO0OOO ),'signstring':O00OO0O00O0OO0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:366
            OO0OOO00O000OO000 =requests .request ('post',f'{host}/game/watched-ad',headers =O0O0O0O00OOOOOO00 ).json ()#line:367
            print (OO0OOO00O000OO000 )#line:368
        except Exception as OOOO00O0O0O0OOO0O :#line:369
            print (OOOO00O0O0O0OOO0O )#line:370
    def user_ad (OO0OOOO00OOOO0OO0 ):#line:374
        try :#line:375
            OO00OO000O00O0000 =f'__{timi_new()}'#line:376
            O00O0OOOOOO0O0OO0 ={'authorization':OO0OOOO00OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO000O00O0000 ),'signstring':OO00OO000O00O0000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:385
            OOO0O0OOOO00000O0 =requests .request ('get',f'{host}/user/ad',headers =O00O0OOOOOO0O0OO0 ).json ()#line:386
            if 'status'in OOO0O0OOOO00000O0 :#line:388
                if OOO0O0OOOO00000O0 ['status']==200 :#line:389
                    O00O00O0OO0O00O0O =OOO0O0OOOO00000O0 ['data']['max_time']#line:390
                    OOO0O00O0OOO0O000 =OOO0O0OOOO00000O0 ['data']['watch_time']#line:391
                    OOO00O0000O0O00OO =OOO0O0OOOO00000O0 ['data']['added_time']#line:392
                    print (f'【获取种子】:获取种子剩余{OOO00O0000O0O00OO + O00O00O0OO0O00O0O - OOO0O00O0OOO0O000}次丨好友提供:{OOO00O0000O0O00OO}次')#line:393
                    if OOO00O0000O0O00OO +O00O00O0OO0O00O0O -OOO0O00O0OOO0O000 >0 :#line:394
                        time .sleep (random .randint (16 ,19 ))#line:395
                        O00O0O0O000OO00OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00O0OOOOOO0O0OO0 ).json ()#line:396
                        if 'status'in O00O0O0O000OO00OO :#line:398
                            if O00O0O0O000OO00OO ['status']==200 :#line:399
                                O0O0O0000O0O0O00O =O00O0O0O000OO00OO ['data']['silver']#line:400
                                print (f'【获取种子】:获得种子:{O0O0O0000O0O0O00O}')#line:401
                                return True #line:402
                            if O00O0O0O000OO00OO ['status']==500 :#line:403
                                OOOOOO00OOOOOO0O0 =O00O0O0O000OO00OO ['message']#line:404
                                print (f'【获取种子】:{OOOOOO00OOOOOO0O0}')#line:405
                                return False #line:406
        except Exception as OO000O0OO0O0O00OO :#line:407
            print (OO000O0OO0O0O00OO )#line:408
    def synthetic (OO0OOOOOO0O00O00O ):#line:412
        global id ,g #line:413
        try :#line:414
            OO0O00000OOOOOOOO =OO0OOOOOO0O00O00O .level_new ()#line:415
            while True :#line:416
                OOO0O000O0OOOO0OO =f'__{timi_new()}'#line:417
                OO0O0O0O00OOO000O ={'authorization':OO0OOOOOO0O00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O0OOOO0OO ),'signstring':OOO0O000O0OOOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:426
                O00O00O0O0000OO0O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O0O00OOO000O ).json ()#line:427
                if 'status'in O00O00O0O0000OO0O :#line:429
                    if O00O00O0O0000OO0O ['status']==200 :#line:430
                        OOO0O00000O0OO000 =O00O00O0O0000OO0O ['data']['cropList']#line:431
                        OO00O00O00OO0OO00 =O00O00O0O0000OO0O ['data']['gameCoreDataDBid']#line:432
                        OOO0O0OO00O0OOOOO =0 #line:433
                        for OOOO0OOOO0O0OO0O0 in OOO0O00000O0OO000 :#line:434
                            if not OOOO0OOOO0O0OO0O0 :#line:435
                                O00000000OO0O000O =f'_crop_id={OO00O00O00OO0OO00}&site={OOO0O0OO00O0OOOOO}_{OO0OOOOOO0O00O00O.time}'#line:436
                                OO00OO00OO00OO000 ={'authorization':OO0OOOOOO0O00O00O .token ,'timestamp':OO0OOOOOO0O00O00O .time ,'sign':sign (O00000000OO0O000O ),'signstring':O00000000OO0O000O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:445
                                O000O00OOOO0O0O00 ={"site":OOO0O0OO00O0OOOOO ,"crop_id":OO00O00O00OO0OO00 }#line:446
                                O0000O000OO0O00O0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO00OO00OO00OO000 ,data =O000O00OOOO0O0O00 ).json ()#line:447
                                time .sleep (random .randint (1 ,3 )/10 )#line:449
                                if 'status'in O0000O000OO0O00O0 :#line:450
                                    if O0000O000OO0O00O0 ['status']==200 :#line:451
                                        if O0000O000OO0O00O0 ['message']=='种子数量不足':#line:452
                                            OO0O00000OOOOOOOO =OO0OOOOOO0O00O00O .level_new ()#line:453
                                            print (f'【种植合成】:{O0000O000OO0O00O0["message"]}')#line:454
                                            if not OO0OOOOOO0O00O00O .user_ad ():#line:455
                                                return False #line:456
                                    if O0000O000OO0O00O0 ['status']==500 :#line:457
                                        print (f'【种植合成】:{O0000O000OO0O00O0["message"]}')#line:458
                                        return False #line:459
                            OOO0O0OO00O0OOOOO +=1 #line:460
                        O00O0OO0O0O00O00O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O0O00OOO000O ).json ()#line:461
                        OO00O0000O0OOO0O0 =O00O0OO0O0O00O00O ['data']['cropList']#line:462
                        O00O00000000O00OO =False #line:463
                        for OOOO0OOOO0O0OO0O0 in range (12 ):#line:464
                            id =OO00O0000O0OOO0O0 [OOOO0OOOO0O0OO0O0 ]['level']#line:465
                            if float (OO0O00000OOOOOOOO )-float (id )>9 :#line:466
                                O000OO00OOOO0OOOO =f'_site={OOOO0OOOO0O0OO0O0}_{timi_new()}'#line:467
                                O00000000OOOO0O00 ={'accept':'application/json, text/plain, */*','authorization':OO0OOOOOO0O00O00O .token ,'timestamp':timi_new (),'sign':sign (O000OO00OOOO0OOOO ),'signstring':O000OO00OOOO0OOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:477
                                OOO0O0O00OO0O00O0 ={"site":OOOO0OOOO0O0OO0O0 }#line:478
                                OO0OO0O00O00OO0OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00000000OOOO0O00 ,data =OOO0O0O00OO0O00O0 ).json ()#line:480
                                if 'status'in OO0OO0O00O00OO0OO :#line:481
                                    if OO0OO0O00O00OO0OO ['status']==200 :#line:482
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:483
                            if id !=0 :#line:484
                                for O000O0OOOOOO0O0O0 in range (11 ):#line:485
                                    O0O0O0O0000000OO0 =O000O0OOOOOO0O0O0 +1 #line:486
                                    g =OO00O0000O0OOO0O0 [O0O0O0O0000000OO0 ]['level']#line:487
                                    if id ==g :#line:488
                                        OOOOO0OO00O0OOO0O =O000O0OOOOOO0O0O0 +2 #line:489
                                        if OOOOO0OO00O0OOO0O !=OOOO0OOOO0O0OO0O0 +1 :#line:490
                                            OOOO00O000O0O0000 =OOOO0OOOO0O0OO0O0 +1 #line:491
                                            time .sleep (random .randint (1 ,3 )/10 )#line:493
                                            OOO000O0O0O00O00O =f'_site={OOOO00O000O0O0000 - 1}&targetSite={OOOOO0OO00O0OOO0O - 1}_{timi_new()}'#line:494
                                            OOO00O0OOOO000000 ={'accept':'application/json, text/plain, */*','authorization':OO0OOOOOO0O00O00O .token ,'timestamp':timi_new (),'sign':sign (OOO000O0O0O00O00O ),'signstring':OOO000O0O0O00O00O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:509
                                            OO0O0O0O000OO0O00 ={"site":int (OOOO00O000O0O0000 -1 ),"targetSite":int (OOOOO0OO00O0OOO0O -1 )}#line:510
                                            O000OO0O00OOOO00O =requests .request ('post',f'{host}/game/crops/move',headers =OOO00O0OOOO000000 ,json =OO0O0O0O000OO0O00 ).json ()#line:512
                                            if 'status'in O000OO0O00OOOO00O :#line:513
                                                if O000OO0O00OOOO00O ['status']==200 :#line:514
                                                    pass #line:515
                                            print ('【种植合成】:',OOOO00O000O0O0000 ,OOOOO0OO00O0OOO0O ,'合成成功')#line:517
                                            O00O00000000O00OO =True #line:518
                                    if O00O00000000O00OO :#line:519
                                        break #line:520
                                if O00O00000000O00OO :#line:521
                                    break #line:522
        except Exception as O0OO0O0OO0O0O0OOO :#line:523
            OO0OOOOOO0O00O00O .synthetic ()#line:524
    def level_new (OOO0000OOO00O00O0 ):#line:527
        try :#line:528
            OO0O0O0O0OO00OOOO =f'__{timi_new()}'#line:529
            OO00OO0OO0OO00OO0 ={'authorization':OOO0000OOO00O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0O0OO00OOOO ),'signstring':OO0O0O0O0OO00OOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:538
            O00O000O00000OOO0 =requests .request ('get',f'{host}/user',headers =OO00OO0OO0OO00OO0 ).json ()#line:539
            if 'status'in O00O000O00000OOO0 :#line:540
                if O00O000O00000OOO0 ['status']==200 :#line:541
                    return float (O00O000O00000OOO0 ['data']['level'])#line:542
        except Exception as OO0OOO00O0O0OOOOO :#line:543
            print (OO0OOO00O0O0OOOOO )#line:544
    def propsraffle (O00O0OO0OOOOOO00O ):#line:547
        try :#line:548
            while True :#line:549
                OO00OOOO0OO0OOO0O =f'__{timi_new()}'#line:550
                OO0000O0OOOOO00O0 ={'authorization':O00O0OO0OOOOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOO0OO0OOO0O ),'signstring':OO00OOOO0OO0OOO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:559
                OO000OOO0O00O00OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0000O0OOOOO00O0 ).json ()#line:560
                if 'status'in OO000OOO0O00O00OO :#line:562
                    if OO000OOO0O00O00OO ['status']==200 :#line:563
                        OO000000O0O000O0O =OO000OOO0O00O00OO ['data']['rows']#line:564
                        OOO0OOOOOOO0O0OO0 =OO000OOO0O00O00OO ['data']['vstate']#line:565
                        if OO000000O0O000O0O ==5 or OO000000O0O000O0O ==6 or OO000000O0O000O0O ==7 :#line:566
                            O00O00000O0OO0O0O =OO000OOO0O00O00OO ['data']['silver']#line:567
                            print (f'【转盘抽奖】:获得种子:{O00O00000O0OO0O0O}')#line:568
                        if OO000000O0O000O0O ==1 or OO000000O0O000O0O ==2 or OO000000O0O000O0O ==3 :#line:569
                            OO0000OOOO0O00OO0 =OO000OOO0O00O00OO ['data']['clover']#line:570
                            print (f'【转盘抽奖】:获得三叶草:{OO0000OOOO0O00OO0}')#line:571
                        if OO000000O0O000O0O ==4 or OO000000O0O000O0O ==8 :#line:572
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:573
                        if OO000000O0O000O0O =='抽奖次数已用完':#line:577
                            break #line:610
                time .sleep (random .randint (8 ,15 )/10 )#line:611
        except Exception as OOO0OOOO0O00OOO0O :#line:612
            print (OOO0OOOO0O00OOO0O )#line:613
    def friends_invitation (OO00OOO000O0OOO0O ):#line:617
        try :#line:618
            O0O00O000OOO0O0O0 =f'__{timi_new()}'#line:619
            O0000O000OOOOOOO0 ={'authorization':OO00OOO000O0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O000OOO0O0O0 ),'signstring':O0O00O000OOO0O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:628
            O0OOO0O0OOO0000OO =requests .request ('get',f'{host}/friends',headers =O0000O000OOOOOOO0 ).json ()#line:629
            if 'status'in O0OOO0O0OOO0000OO :#line:630
                if O0OOO0O0OOO0000OO ['status']==200 :#line:631
                    OO000O00O0O0O0OO0 =O0OOO0O0OOO0000OO ['data']['myInviteter']#line:632
                    if OO000O00O0O0O0OO0 :#line:633
                        OO00OOO0000O0OO0O =OO000O00O0O0O0OO0 ['user']['nickname']#line:634
                        O000O0O00OOOOO000 =OO00OOO000O0OOO0O .certification ()#line:635
                        print (f'【查邀请人】:我的邀请人:{OO00OOO0000O0OO0O}丨实名:{O000O0O00OOOOO000}')#line:636
                    else :#line:637
                        if OO00OOO000O0OOO0O .innerId !='0':#line:638
                            OO00OOO000O0OOO0O .invitation ()#line:639
        except Exception as O0O0000OOO00O00OO :#line:640
            print (O0O0000OOO00O00OO )#line:641
    def add_clover (O0OOO00000000O0O0 ):#line:645
        global golden_seed #line:646
        try :#line:647
            OO0OO0O0O00O0OOO0 =f'__{timi_new()}'#line:648
            OOO000O0000000OOO ={'authorization':O0OOO00000000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0O00O0OOO0 ),'signstring':OO0OO0O0O00O0OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:657
            O0OO0O000O0000OO0 =requests .request ('get',f'{host}/assets/clovers',headers =OOO000O0000000OOO ).json ()#line:658
            if 'status'in O0OO0O000O0000OO0 :#line:660
                if O0OO0O000O0000OO0 ['status']==200 :#line:661
                    OO0OO0O0OOO0OO000 =O0OO0O000O0000OO0 ['data']['clover']#line:662
                    O0O0000OO0OOOOO00 =O0OO0O000O0000OO0 ['data']['used_clover']#line:663
                    O0OO0O000OOOO0O00 =float (OO0OO0O0OOO0OO000 )-float (O0O0000OO0OOOOO00 )#line:664
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0O0000OO0OOOOO00}')#line:665
                    if O0OOO00000000O0O0 .certification ()!='未实名':#line:666
                        if O0OO0O000OOOO0O00 >1 :#line:667
                            OO0OO0O0O00O0OOO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OO0O000OOOO0O00)}_{timi_new()}'#line:668
                            OOO000O0000000OOO ={'authorization':O0OOO00000000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0O00O0OOO0 ),'signstring':OO0OO0O0O00O0OOO0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:677
                            OOO0O00O0O00O0O00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OO0O000OOOO0O00 )}#line:678
                            OO0OO00O0OOO00O0O =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO000O0000000OOO ,data =OOO0O00O0O00O0O00 ).json ()#line:679
                            if 'status'in OO0OO00O0OOO00O0O :#line:681
                                if OO0OO00O0OOO00O0O ['status']==200 :#line:682
                                    print (f'【参与抽奖】:添加三叶草:{OO0OO00O0OOO00O0O["data"]}丨数量:{O0OO0O000OOOO0O00}')#line:683
                                if OO0OO00O0OOO00O0O ['status']==500 :#line:684
                                    print (f'【参与抽奖】:添加三叶草:{OO0OO00O0OOO00O0O["message"]}')#line:685
            O0OO0O0000OOOOOOO =requests .request ('get',f'{host}/lottery',headers =OOO000O0000000OOO ).json ()#line:686
            OO0OOO0O0OOO0OOOO =O0OOO00000000O0O0 .winning_rewards ()#line:688
            if 'status'in O0OO0O0000OOOOOOO :#line:689
                if O0OO0O0000OOOOOOO ['status']==200 :#line:690
                    O0O0OOOOO0OOO00OO =O0OO0O0000OOOOOOO ['data'][0 ]['day_get_gold_quantity']#line:691
                    golden_seed +=float (O0O0OOOOO0OOO00OO )#line:692
                    print (f'【参与抽奖】:预计每天中{str(O0O0OOOOO0OOO00OO)[:6]}颗金种子丨好友收益:{str(OO0OOO0O0OOO0OOOO)[:6]}')#line:693
        except Exception as O0OOO0OOOOOOOOO00 :#line:694
            print (O0OOO0OOOOOOOOO00 )#line:695
    def energy (OO0O0O0OOOOO0O000 ):#line:698
        O0O0OO00000O00O0O =f'__{timi_new()}'#line:699
        O0O0OOOO0OO00OOOO ={'authorization':OO0O0O0OOOOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00000O00O0O ),'signstring':O0O0OO00000O00O0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:708
        OOOO0O00OO0OOO000 =requests .request ('get',f'{host}/energy/general',headers =O0O0OOOO0OO00OOOO ).json ()#line:709
        if 'status'in OOOO0O00OO0OOO000 :#line:711
            if OOOO0O00OO0OOO000 ['status']==200 :#line:712
                O00O0OOO00000O000 =OOOO0O00OO0OOO000 ['data']['ordinary_water']#line:713
                O0OO00O0O00OOO00O =OOOO0O00OO0OOO000 ['data']['ordinary_fertilizer']#line:714
                print (f'【我的营养】:肥料:{str(O0OO00O0O00OOO00O).split(".")[0]}丨水滴:{str(O00O0OOO00000O000).split(".")[0]}')#line:715
                if float (O0OO00O0O00OOO00O )<96 :#line:716
                    time .sleep (random .randint (160 ,180 )/10 )#line:717
                    OOO00O0OO0000OOOO =99 -float (O0OO00O0O00OOO00O )#line:718
                    O0OOO0O000O00O00O ={"fertilizer":str (OOO00O0OO0000OOOO ).split ('.')[0 ]}#line:719
                    O000OOOOOOO000O0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0O0OOOO0OO00OOOO ).json ()#line:720
                    if 'status'in O000OOOOOOO000O0O :#line:722
                        if O000OOOOOOO000O0O ['status']==200 :#line:723
                            print (f'【购买肥料】:看广告获取肥料:{O000OOOOOOO000O0O["message"]}')#line:724
                if float (O00O0OOO00000O000 )<880 :#line:725
                    time .sleep (random .randint (160 ,180 )/10 )#line:726
                    OO000OOO00OO00OO0 =999 -float (O00O0OOO00000O000 )#line:727
                    O00O00OOOOO0OOOOO ={"water":str (OO000OOO00OO00OO0 ).split ('.')[0 ]}#line:728
                    OO0OO0OOO0O0000O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0O0OOOO0OO00OOOO ).json ()#line:729
                    if 'status'in OO0OO0OOO0O0000O0 :#line:731
                        if OO0OO0OOO0O0000O0 ['status']==200 :#line:732
                            print (f'【购买水滴】:看广告获取水滴:{OO0OO0OOO0O0000O0["message"]}')#line:733
def bundled_def ():#line:736
    O00O000O0OOOO00OO =['5570536','7750212','7911652','7911680','7805624']#line:737
    return O00O000O0OOOO00OO [random .randint (0 ,len (O00O000O0OOOO00OO )-1 )]#line:738
def version_of_the_validation ():#line:742
    return str ((71 -56 )/10 )#line:743
def gitee_validation ():#line:746
    try :#line:747
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:748
    except :#line:749
        sys .exit (0 )#line:750
def update_the_validation ():#line:754
    try :#line:755
        O0O0000OOO0000O0O =gitee_validation ()#line:756
        if version_of_the_validation ()<O0O0000OOO0000O0O ['CityEarth']['edition']:#line:757
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0000OOO0000O0O["CityEarth"]["edition"]}   ❌')#line:758
            print (f'更新内容=>>{O0O0000OOO0000O0O["CityEarth"]["content"]}   👍')#line:759
        else :#line:760
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0000OOO0000O0O["CityEarth"]["edition"]}   ✅')#line:761
            print (f'更新内容=>> {O0O0000OOO0000O0O["CityEarth"]["content"]}   👍')#line:762
    except Exception as O0OOOOOO00OOOOO00 :#line:763
        print (O0OOOOOO00OOOOO00 )#line:764
def os_qinglong ():#line:767
    if application in os .environ :#line:768
        O0OOO0OO000O0O00O =os .environ [application ].split ('\n')#line:769
        if len (O0OOO0OO000O0O00O )>0 :#line:770
            return O0OOO0OO000O0O00O #line:771
        else :#line:772
            print (f"{application}变量未启用")#line:773
            print ('脚本退出')#line:774
            sys .exit (1 )#line:775
    else :#line:776
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:778
        return os_built ()#line:779
def os_built ():#line:782
    if token :#line:783
        OOOO0OOOOO0O00O0O =token .split ('\n')#line:784
        if len (OOOO0OOOOO0O00O0O )>0 :#line:785
            return OOOO0OOOOO0O00O0O #line:786
    else :#line:787
        print (f"内置变量为空")#line:788
        print ('脚本结束')#line:789
        sys .exit (0 )#line:790
if __name__ =='__main__':#line:793
    start ()#line:794
