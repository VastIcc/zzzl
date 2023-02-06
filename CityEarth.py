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
        OOO0OO0O0O0OOOOO0 =os_qinglong ()#line:7
        print (f"==========共找到{len(OOO0OO0O0O0OOOOO0)}个账号==========")#line:8
        for OOOO00OOOOO0OOOOO in OOO0OO0O0O0OOOOO0 :#line:9
            print (f"------------正在执行第{OOO0OO0O0O0OOOOO0.index(OOOO00OOOOO0OOOOO) + 1}个账号------------")#line:10
            O00000000OO0OOOO0 =CityEarth (OOOO00OOOOO0OOOOO )#line:11
            def OOOOOO000O0O0O0O0 ():#line:13
                if O00000000OO0OOOO0 .base_info ():#line:15
                    O00000000OO0OOOO0 .invitenum ()#line:19
                    O00000000OO0OOOO0 .game_map ()#line:21
                    O00000000OO0OOOO0 .friends_invitation ()#line:23
                    O00000000OO0OOOO0 .add_clover ()#line:25
                    O00000000OO0OOOO0 .energy ()#line:27
                    O00000000OO0OOOO0 .propsraffle ()#line:29
                    O00000000OO0OOOO0 .synthetic ()#line:31
                    O00000000OO0OOOO0 .crops_illustrated ()#line:33
                    O00000000OO0OOOO0 .give_gold ()#line:35
                    O00000000OO0OOOO0 .withdraw ()#line:37
                else :#line:38
                    print ('token失效')#line:39
            O000OOO0O000OOOOO =threading .Thread (target =OOOOOO000O0O0O0O0 )#line:41
            O000OOO0O000OOOOO .start ()#line:42
            time .sleep (time_xx )#line:43
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:45
        time .sleep (3 )#line:46
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:47
    except Exception as O0O0O0000OOOO0O00 :#line:48
        print (O0O0O0000OOOO0O00 )#line:49
def sign (OOOOO0000O00000OO ):#line:52
    OOO0000O0O0OO00O0 =hashlib .md5 (OOOOO0000O00000OO .encode ()).hexdigest ()#line:53
    O0OOOOOO0OOOO0O0O ="scsc%^&*"+OOO0000O0O0OO00O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    OO0OOOOOOOO0O000O =hashlib .md5 (O0OOOOOO0OOOO0O0O .encode ()).hexdigest ()#line:55
    return OO0OOOOOOOO0O000O #line:56
def timi_new ():#line:59
    return str (int (time .time ()*1000 ))#line:60
class CityEarth :#line:62
    def __init__ (O00000OO0O0O00OOO ,O00O0O0OOOO0OO000 ):#line:64
        try :#line:65
            O00000OO0O0O00OOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:66
            O00000OO0O0O00OOO .token =O00O0O0OOOO0OO000 .split ('&')[0 ]#line:67
            O00000OO0O0O00OOO .innerId =O00O0O0OOOO0OO000 .split ('&')[1 ]#line:68
            O00000OO0O0O00OOO .doneeNo =O00O0O0OOOO0OO000 .split ('&')[2 ]#line:69
        except :#line:70
            print ('变量格式错误')#line:71
    def base_info (OO00O00O00O00O0OO ):#line:74
        try :#line:75
            OOOO00O00OOOOO0O0 =f'__{timi_new()}'#line:76
            O0O0OO000OOOO00O0 ={'authorization':OO00O00O00O00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O00OOOOO0O0 ),'signstring':OOOO00O00OOOOO0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
            O0O00OOO0OO00OOO0 =requests .request ('get',f'{host}/user',headers =O0O0OO000OOOO00O0 ).json ()#line:86
            if 'status'in O0O00OOO0OO00OOO0 :#line:88
                if O0O00OOO0OO00OOO0 ['status']==200 :#line:89
                    OO000000OO0O0O00O =O0O00OOO0OO00OOO0 ['data']['nickname']#line:90
                    O0OOO00O00O0O0O00 =O0O00OOO0OO00OOO0 ['data']['inner_id']#line:91
                    OO000OOOOOO0OOOOO =O0O00OOO0OO00OOO0 ['data']['assets']['gold']#line:92
                    O00O00O000O0OO0OO =O0O00OOO0OO00OOO0 ['data']['level']#line:93
                    print (f'【账号信息】:昵称:{OO000000OO0O0O00O[:5]}丨ID:{O0OOO00O00O0O0O00}丨等级:{O00O00O000O0OO0OO}丨种子:{str(OO000OOOOOO0OOOOO).split(".")[0]}')#line:94
                if O0O00OOO0OO00OOO0 ['status']==401 :#line:95
                    return False #line:96
                if O0O00OOO0OO00OOO0 ['status']==500 :#line:97
                    return False #line:98
            return True #line:99
        except Exception as OOO0OOO00O00O0000 :#line:100
            print (OOO0OOO00O00O0000 )#line:101
    def withdraw (OOOOOOOO0O00OO00O ):#line:104
        O000O0000OOOO000O =f'__{timi_new()}'#line:105
        OO00OOOO0O0000OOO ={'authorization':OOOOOOOO0O00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0000OOOO000O ),'signstring':O000O0000OOOO000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:114
        OOO0000O00OO00OO0 =requests .request ('get',f'{host}/assets',headers =OO00OOOO0O0000OOO ).json ()#line:115
        if 'status'in OOO0000O00OO00OO0 :#line:117
            if OOO0000O00OO00OO0 ['status']==200 :#line:118
                OO0OO0O00O00OO0OO =OOO0000O00OO00OO0 ['data']['cash']#line:119
                if float (OO0OO0O00O00OO0OO )>20 :#line:120
                    O000O0000OOOO000O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:121
                    OO00OOOO0O0000OOO ={'authorization':OOOOOOOO0O00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0000OOOO000O ),'signstring':O000O0000OOOO000O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:130
                    O0OOOOO0000OO0000 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:131
                    OOO0OOO00O000OOOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO00OOOO0O0000OOO ,data =O0OOOOO0000OO0000 ).json ()#line:132
                    print (OOO0OOO00O000OOOO )#line:133
    def invitenum (O000OO0000OO0OO00 ):#line:139
        OOOO0O0OOOO0O0OOO =f'__{timi_new()}'#line:140
        OOOOOO0OO000O0000 ={'authorization':O000OO0000OO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0OOOO0O0OOO ),'signstring':OOOO0O0OOOO0O0OOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:149
        O00OOOO000O00O0O0 =requests .request ('get',f'{host}/invite/invitenum',headers =OOOOOO0OO000O0000 ).json ()#line:150
        if 'status'in O00OOOO000O00O0O0 :#line:152
            if O00OOOO000O00O0O0 ['status']==200 :#line:153
                O00OOOO00O000O0OO =O00OOOO000O00O0O0 ['data']['invited_count']#line:154
                O0OO0OO0OOO00OO00 =O00OOOO000O00O0O0 ['data']['invited_second_count']#line:155
                print (f'【我的邀请】:直邀好友:{O00OOOO00O000O0OO}丨间邀好友:{O0OO0OO0OOO00OO00}')#line:156
    def game_map (OOOO00OO0OO0OO000 ):#line:160
        try :#line:161
            O0O0O0000O0O000OO =f'__{timi_new()}'#line:162
            OO0O0O000O00O000O ={'authorization':OOOO00OO0OO0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0000O0O000OO ),'signstring':O0O0O0000O0O000OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:171
            O00000O00OO0OOOO0 =requests .request ('get',f'{host}/game/map',headers =OO0O0O000O00O000O ).json ()#line:172
            if 'status'in O00000O00OO0OOOO0 :#line:174
                if O00000O00OO0OOOO0 ['status']==200 :#line:175
                    for OO0O00O0000000OOO in O00000O00OO0OOOO0 ['data']['list'][0 ]['crops']:#line:176
                        O0OO0OOO00OOOOO00 =OO0O00O0000000OOO ['level']#line:178
                        if O0OO0OOO00OOOOO00 ==41 :#line:179
                            OOO0O0000O0OO0O00 =OO0O00O0000000OOO ['crop_name']#line:180
                            O0O00O0OO00000000 =OO0O00O0000000OOO ['count']#line:181
                            if O0O00O0OO00000000 >0 :#line:182
                                print (f'【农业资产】:{OOO0O0000O0OO0O00}丨数量:{O0O00O0OO00000000}')#line:183
        except Exception as OOOOO0OO0O0000OOO :#line:184
            print (OOOOO0OO0O0000OOO )#line:185
    def give_gold (OOO000O00O0O0OO00 ):#line:189
        try :#line:190
            OO0O0OO000000OOOO =f'__{timi_new()}'#line:191
            O00O000O0000O0O0O ={'authorization':OOO000O00O0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO000000OOOO ),'signstring':OO0O0OO000000OOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:200
            O000000OOO0O00O0O =requests .request ('get',f'{host}/user',headers =O00O000O0000O0O0O ).json ()#line:201
            if 'status'in O000000OOO0O00O0O :#line:202
                if O000000OOO0O00O0O ['status']==200 :#line:203
                    if float (OOO000O00O0O0OO00 .doneeNo )!=0 :#line:204
                        O0O0O0O0OO0OOO0OO =O000000OOO0O00O0O ['data']['assets']['gold']#line:205
                        if float (O0O0O0O0OO0OOO0OO )>float (OOO000O00O0O0OO00 .innerId ):#line:206
                            OOOO00OOO00O000O0 =int (float (O0O0O0O0OO0OOO0OO )/1.1 )#line:207
                            OO0O0OO000000OOOO =f'_doneeNo={OOO000O00O0O0OO00.doneeNo}&quantity={OOOO00OOO00O000O0}_{timi_new()}'#line:208
                            O00O000O0000O0O0O ={'authorization':OOO000O00O0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO000000OOOO ),'signstring':OO0O0OO000000OOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:217
                            O00O0O00O00O00O0O ={"quantity":OOOO00OOO00O000O0 ,"doneeNo":OOO000O00O0O0OO00 .doneeNo }#line:221
                            O0O0O00OO0OOO00OO =requests .request ('post',f'{host}/finance/give-gold',headers =O00O000O0000O0O0O ,data =O00O0O00O00O00O0O ).json ()#line:222
                            if 'status'in O0O0O00OO0OOO00OO :#line:224
                                if O0O0O00OO0OOO00OO ['status']==200 :#line:225
                                    if O0O0O00OO0OOO00OO ['data']:#line:226
                                        print (f'【赠送种子】:赠送{OOOO00OOO00O000O0}种子给{OOO000O00O0O0OO00.doneeNo}成功')#line:227
                    else :#line:228
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:229
        except Exception as O00OO00O0O000OO0O :#line:230
            print (O00OO00O0O000OO0O )#line:231
    def invitation (O0OOO0O000OOO0OOO ):#line:234
        try :#line:235
            _O00O00OOOO000O00O =float (bundled_def ())/4 #line:236
            O0OO0O00OO000O0O0 =f'_innerId={int(_O00O00OOOO000O00O)}_{timi_new()}'#line:237
            O000O0OO00OOO0000 ={'authorization':O0OOO0O000OOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00OO000O0O0 ),'signstring':O0OO0O00OO000O0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:246
            O000OOOOOO000O00O ={"innerId":int (_O00O00OOOO000O00O )}#line:247
            requests .request ('post',f'{host}/friends/my-invitation',headers =O000O0OO00OOO0000 ,data =O000OOOOOO000O00O )#line:248
        except Exception as OO000O0000O0OO000 :#line:249
            print (OO000O0000O0OO000 )#line:250
    def winning_rewards (O0000O0000O00O0OO ):#line:255
        try :#line:256
            O0OO00O0O00O0OO0O =f'__{timi_new()}'#line:257
            O0000OO0OOO000O0O ={'authorization':O0000O0000O00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0O00O0OO0O ),'signstring':O0OO00O0O00O0OO0O ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:266
            OO0OOOOOO0O0O0O0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0000OO0OOO000O0O ).json ()#line:267
            if 'status'in OO0OOOOOO0O0O0O0O :#line:269
                if OO0OOOOOO0O0O0O0O ['status']==200 :#line:270
                    if OO0OOOOOO0O0O0O0O ['data']['amount']:#line:271
                        O0OOO0OOO0000OO00 =OO0OOOOOO0O0O0O0O ['data']['amount']['gold']#line:272
                        return O0OOO0OOO0000OO00 #line:273
                    else :#line:274
                        return 0 #line:275
        except Exception as O0OOOOOOOO0OOO0OO :#line:276
            print (O0OOOOOOOO0OOO0OO )#line:277
    def certification (O0O000O0O0OO00O00 ):#line:281
        try :#line:282
            OOOO00000O0O0OO00 =f'__{timi_new()}'#line:283
            O00O000O000O00OO0 ={'authorization':O0O000O0O0OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00000O0O0OO00 ),'signstring':OOOO00000O0O0OO00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:292
            OO0OO00O000O0O00O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00O000O000O00OO0 ).json ()#line:293
            if 'status'in OO0OO00O000O0O00O :#line:295
                if OO0OO00O000O0O00O ['status']==200 :#line:296
                    if OO0OO00O000O0O00O ['data']['result']:#line:297
                        OOO0O0O000O0000OO =OO0OO00O000O0O00O ['data']['nick_name']#line:298
                        return OOO0O0O000O0000OO #line:299
                    else :#line:300
                        return '未实名'#line:301
        except Exception as O00OOO0OOO000O000 :#line:302
            print (O00OOO0OOO000O000 )#line:303
    def crops_illustrated (O0000O0OO0O0OO0OO ):#line:307
        try :#line:308
            O00OO00O0OO0OO0O0 =f'__{timi_new()}'#line:309
            OOO000O0O000OO0O0 ={'authorization':O0000O0OO0O0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00O0OO0OO0O0 ),'signstring':O00OO00O0OO0OO0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:318
            O0O0OO0O0OOO000OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO000O0O000OO0O0 ).json ()#line:319
            if 'status'in O0O0OO0O0OOO000OO :#line:321
                if O0O0OO0O0OOO000OO ['status']==200 :#line:322
                    OO0OOOO000O0OOO0O =O0O0OO0O0OOO000OO ['data'][0 ]['crops']#line:323
                    for O0O0O000OO0OOO000 in OO0OOOO000O0OOO0O :#line:324
                        if O0O0O000OO0OOO000 ['ill_clover_award']:#line:325
                            if float (O0O0O000OO0OOO000 ['ill_clover_award'])>1 :#line:326
                                if O0O0O000OO0OOO000 ['is_finish']:#line:327
                                    if not O0O0O000OO0OOO000 ['is_getit']:#line:328
                                        if O0000O0OO0O0OO0OO .certification ()!='未实名':#line:329
                                            O00OO00O0OO0OO0O0 =f'_award_level={O0O0O000OO0OOO000["level"]}_{timi_new()}'#line:330
                                            OOO000O0O000OO0O0 ={'authorization':O0000O0OO0O0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00O0OO0OO0O0 ),'signstring':O00OO00O0OO0OO0O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                                            O0OOOOO0O0OOOO0O0 ={"award_level":O0O0O000OO0OOO000 ['level']}#line:340
                                            OO0O0OO0000OOO000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO000O0O000OO0O0 ,json =O0OOOOO0O0OOOO0O0 ).json ()#line:342
                                            if 'status'in OO0O0OO0000OOO000 :#line:343
                                                if OO0O0OO0000OOO000 ['status']==200 :#line:344
                                                    O0O0OO00O00OOO0OO =OO0O0OO0000OOO000 ['data']['ill_clover_award']#line:345
                                                    print (f'【图鉴奖励】:领取{O0O0O000OO0OOO000["crop_name"]}成就丨奖励{O0O0OO00O00OOO0OO}叶子成功')#line:347
                                                if OO0O0OO0000OOO000 ['status']==500 :#line:348
                                                    print (f'【图鉴奖励】:{OO0O0OO0000OOO000["message"]}')#line:349
        except Exception as OOOO0O000OOO0O0OO :#line:350
            print (OOOO0O000OOO0O0OO )#line:351
    def watched_ad (OO0000OO0OOOOOOOO ):#line:355
        try :#line:356
            OOOO0OO00O0OOO0OO =f'__{timi_new()}'#line:357
            OO0000OOOOOOO0OO0 ={'authorization':OO0000OO0OOOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00O0OOO0OO ),'signstring':OOOO0OO00O0OOO0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:366
            OO0O0OOOOO0OOOO0O =requests .request ('post',f'{host}/game/watched-ad',headers =OO0000OOOOOOO0OO0 ).json ()#line:367
            print (OO0O0OOOOO0OOOO0O )#line:368
        except Exception as O00O0O0OOO00O0OOO :#line:369
            print (O00O0O0OOO00O0OOO )#line:370
    def user_ad (OO0OO0OOO00OO00OO ):#line:374
        try :#line:375
            O0000O0O000O000O0 =f'__{timi_new()}'#line:376
            OO0O00OO0O000OO00 ={'authorization':OO0OO0OOO00OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0O000O000O0 ),'signstring':O0000O0O000O000O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:385
            O0O000OO00O0O0O00 =requests .request ('get',f'{host}/user/ad',headers =OO0O00OO0O000OO00 ).json ()#line:386
            if 'status'in O0O000OO00O0O0O00 :#line:388
                if O0O000OO00O0O0O00 ['status']==200 :#line:389
                    O0OOO00000O0OO000 =O0O000OO00O0O0O00 ['data']['max_time']#line:390
                    O0O0O00000000O00O =O0O000OO00O0O0O00 ['data']['watch_time']#line:391
                    O0OO00OO000O0OOOO =O0O000OO00O0O0O00 ['data']['added_time']#line:392
                    print (f'【获取种子】:获取种子剩余{O0OO00OO000O0OOOO + O0OOO00000O0OO000 - O0O0O00000000O00O}次丨好友提供:{O0OO00OO000O0OOOO}次')#line:393
                    if O0OO00OO000O0OOOO +O0OOO00000O0OO000 -O0O0O00000000O00O >0 :#line:394
                        time .sleep (random .randint (16 ,19 ))#line:395
                        OO00OOOO0000OOO0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO0O00OO0O000OO00 ).json ()#line:396
                        if 'status'in OO00OOOO0000OOO0O :#line:398
                            if OO00OOOO0000OOO0O ['status']==200 :#line:399
                                O0O00OOO0O0O0O00O =OO00OOOO0000OOO0O ['data']['silver']#line:400
                                print (f'【获取种子】:获得种子:{O0O00OOO0O0O0O00O}')#line:401
                                return True #line:402
                            if OO00OOOO0000OOO0O ['status']==500 :#line:403
                                OOO0OO00OOOOO00OO =OO00OOOO0000OOO0O ['message']#line:404
                                print (f'【获取种子】:{OOO0OO00OOOOO00OO}')#line:405
                                return False #line:406
        except Exception as OOO0OOOO0OOO00OO0 :#line:407
            print (OOO0OOOO0OOO00OO0 )#line:408
    def synthetic (OOOO0O00O00OOOOO0 ):#line:412
        global id ,g #line:413
        try :#line:414
            O00O000000OOOOOOO =OOOO0O00O00OOOOO0 .level_new ()#line:415
            while True :#line:416
                O00O0OO0O0000OOOO =f'__{timi_new()}'#line:417
                OOOOO0OOO00000000 ={'authorization':OOOO0O00O00OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO0O0000OOOO ),'signstring':O00O0OO0O0000OOOO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:426
                O00O00O00O0OO0O00 =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO0OOO00000000 ).json ()#line:427
                if 'status'in O00O00O00O0OO0O00 :#line:429
                    if O00O00O00O0OO0O00 ['status']==200 :#line:430
                        O0O0OO000OOOOO000 =O00O00O00O0OO0O00 ['data']['cropList']#line:431
                        O000O0O00O0O0000O =O00O00O00O0OO0O00 ['data']['gameCoreDataDBid']#line:432
                        OO0OOOO00OOOOOO0O =0 #line:433
                        for OO000O0OOOOOOO00O in O0O0OO000OOOOO000 :#line:434
                            if not OO000O0OOOOOOO00O :#line:435
                                O0O000O000OOO0O00 =f'_crop_id={O000O0O00O0O0000O}&site={OO0OOOO00OOOOOO0O}_{OOOO0O00O00OOOOO0.time}'#line:436
                                OOOO00OOO0OO0OO00 ={'authorization':OOOO0O00O00OOOOO0 .token ,'timestamp':OOOO0O00O00OOOOO0 .time ,'sign':sign (O0O000O000OOO0O00 ),'signstring':O0O000O000OOO0O00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:445
                                OOOO0O0000000OOOO ={"site":OO0OOOO00OOOOOO0O ,"crop_id":O000O0O00O0O0000O }#line:446
                                OO0O00OO0000O000O =requests .request ('post',f'{host}/game/crops/buy',headers =OOOO00OOO0OO0OO00 ,data =OOOO0O0000000OOOO ).json ()#line:447
                                time .sleep (random .randint (1 ,3 )/10 )#line:449
                                if 'status'in OO0O00OO0000O000O :#line:450
                                    if OO0O00OO0000O000O ['status']==200 :#line:451
                                        if OO0O00OO0000O000O ['message']=='种子数量不足':#line:452
                                            O00O000000OOOOOOO =OOOO0O00O00OOOOO0 .level_new ()#line:453
                                            print (f'【种植合成】:{OO0O00OO0000O000O["message"]}')#line:454
                                            if not OOOO0O00O00OOOOO0 .user_ad ():#line:455
                                                return False #line:456
                                    if OO0O00OO0000O000O ['status']==500 :#line:457
                                        print (f'【种植合成】:{OO0O00OO0000O000O["message"]}')#line:458
                                        return False #line:459
                            OO0OOOO00OOOOOO0O +=1 #line:460
                        O000000O0O0O0OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO0OOO00000000 ).json ()#line:461
                        O00OOOOO00O0O0000 =O000000O0O0O0OOO0 ['data']['cropList']#line:462
                        O00O00O0O0OOO0O0O =False #line:463
                        for OO000O0OOOOOOO00O in range (12 ):#line:464
                            id =O00OOOOO00O0O0000 [OO000O0OOOOOOO00O ]['level']#line:465
                            if float (O00O000000OOOOOOO )-float (id )>9 :#line:466
                                OOOOO0OO000000OO0 =f'_site={OO000O0OOOOOOO00O}_{timi_new()}'#line:467
                                O0O0000O0O00O0OOO ={'accept':'application/json, text/plain, */*','authorization':OOOO0O00O00OOOOO0 .token ,'timestamp':timi_new (),'sign':sign (OOOOO0OO000000OO0 ),'signstring':OOOOO0OO000000OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:477
                                OOO00O0OOO0000O0O ={"site":OO000O0OOOOOOO00O }#line:478
                                O000O0O00O000OO00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O0000O0O00O0OOO ,data =OOO00O0OOO0000O0O ).json ()#line:480
                                if 'status'in O000O0O00O000OO00 :#line:481
                                    if O000O0O00O000OO00 ['status']==200 :#line:482
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:483
                            if id !=0 :#line:484
                                for O00000O000OOO00OO in range (11 ):#line:485
                                    O00O000OOOO000O0O =O00000O000OOO00OO +1 #line:486
                                    g =O00OOOOO00O0O0000 [O00O000OOOO000O0O ]['level']#line:487
                                    if id ==g :#line:488
                                        OOOO0OOO00OO0O000 =O00000O000OOO00OO +2 #line:489
                                        if OOOO0OOO00OO0O000 !=OO000O0OOOOOOO00O +1 :#line:490
                                            O0OOOO0OOOO0O0000 =OO000O0OOOOOOO00O +1 #line:491
                                            time .sleep (random .randint (1 ,3 )/10 )#line:493
                                            O00OOOOO00O0OOO0O =f'_site={O0OOOO0OOOO0O0000 - 1}&targetSite={OOOO0OOO00OO0O000 - 1}_{timi_new()}'#line:494
                                            OO0000000OOOOO000 ={'accept':'application/json, text/plain, */*','authorization':OOOO0O00O00OOOOO0 .token ,'timestamp':timi_new (),'sign':sign (O00OOOOO00O0OOO0O ),'signstring':O00OOOOO00O0OOO0O ,'version':'3.1.4191','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:509
                                            OOOOO00000OO0OOO0 ={"site":int (O0OOOO0OOOO0O0000 -1 ),"targetSite":int (OOOO0OOO00OO0O000 -1 )}#line:510
                                            OO000000O0O0O0OOO =requests .request ('post',f'{host}/game/crops/move',headers =OO0000000OOOOO000 ,json =OOOOO00000OO0OOO0 ).json ()#line:512
                                            if 'status'in OO000000O0O0O0OOO :#line:513
                                                if OO000000O0O0O0OOO ['status']==200 :#line:514
                                                    pass #line:515
                                            print ('【种植合成】:',O0OOOO0OOOO0O0000 ,OOOO0OOO00OO0O000 ,'合成成功')#line:517
                                            O00O00O0O0OOO0O0O =True #line:518
                                    if O00O00O0O0OOO0O0O :#line:519
                                        break #line:520
                                if O00O00O0O0OOO0O0O :#line:521
                                    break #line:522
        except Exception as O0000OOOOOOOO0000 :#line:523
            OOOO0O00O00OOOOO0 .synthetic ()#line:524
    def level_new (OOO0OOOO0OOOOO000 ):#line:527
        try :#line:528
            O0O00O0O00OO0O0OO =f'__{timi_new()}'#line:529
            OO000000OOOO0OO0O ={'authorization':OOO0OOOO0OOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O00OO0O0OO ),'signstring':O0O00O0O00OO0O0OO ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:538
            OO00OOO0O0OO0O00O =requests .request ('get',f'{host}/user',headers =OO000000OOOO0OO0O ).json ()#line:539
            if 'status'in OO00OOO0O0OO0O00O :#line:540
                if OO00OOO0O0OO0O00O ['status']==200 :#line:541
                    return float (OO00OOO0O0OO0O00O ['data']['level'])#line:542
        except Exception as O00OOO0O000OO0O0O :#line:543
            print (O00OOO0O000OO0O0O )#line:544
    def propsraffle (OO0O00OO0O0OOOO00 ):#line:547
        try :#line:548
            while True :#line:549
                O0OOO0000OO0O00O0 =f'__{timi_new()}'#line:550
                O00OO0OOO0O0OOOO0 ={'authorization':OO0O00OO0O0OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000OO0O00O0 ),'signstring':O0OOO0000OO0O00O0 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:559
                O0OOOOOO0O0OO00O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00OO0OOO0O0OOOO0 ).json ()#line:560
                if 'status'in O0OOOOOO0O0OO00O0 :#line:562
                    if O0OOOOOO0O0OO00O0 ['status']==200 :#line:563
                        OOO00OO000OOOOO0O =O0OOOOOO0O0OO00O0 ['data']['rows']#line:564
                        OO0OOOO00O0OOOO0O =O0OOOOOO0O0OO00O0 ['data']['vstate']#line:565
                        if OOO00OO000OOOOO0O ==5 or OOO00OO000OOOOO0O ==6 or OOO00OO000OOOOO0O ==7 :#line:566
                            OOO0O000O0O000O00 =O0OOOOOO0O0OO00O0 ['data']['silver']#line:567
                            print (f'【转盘抽奖】:获得种子:{OOO0O000O0O000O00}')#line:568
                        if OOO00OO000OOOOO0O ==1 or OOO00OO000OOOOO0O ==2 or OOO00OO000OOOOO0O ==3 :#line:569
                            O00O000O00OO0OOO0 =O0OOOOOO0O0OO00O0 ['data']['clover']#line:570
                            print (f'【转盘抽奖】:获得三叶草:{O00O000O00OO0OOO0}')#line:571
                        if OOO00OO000OOOOO0O ==4 or OOO00OO000OOOOO0O ==8 :#line:572
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:573
                        if OOO00OO000OOOOO0O =='抽奖次数已用完':#line:577
                            break #line:610
                time .sleep (random .randint (8 ,15 )/10 )#line:611
        except Exception as O000OO000O0O0OO00 :#line:612
            print (O000OO000O0O0OO00 )#line:613
    def friends_invitation (O00000OOO00OO000O ):#line:617
        try :#line:618
            OO00OOOO0O00O0O00 =f'__{timi_new()}'#line:619
            O0OO00OOO00O000OO ={'authorization':O00000OOO00OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOO0O00O0O00 ),'signstring':OO00OOOO0O00O0O00 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:628
            OOOO0O00OOOO0O00O =requests .request ('get',f'{host}/friends',headers =O0OO00OOO00O000OO ).json ()#line:629
            if 'status'in OOOO0O00OOOO0O00O :#line:630
                if OOOO0O00OOOO0O00O ['status']==200 :#line:631
                    O0000OOOOOOO00000 =OOOO0O00OOOO0O00O ['data']['myInviteter']#line:632
                    if O0000OOOOOOO00000 :#line:633
                        OOOO000O000O0O00O =O0000OOOOOOO00000 ['user']['nickname']#line:634
                        OOOOOOOO0O00OO0OO =O00000OOO00OO000O .certification ()#line:635
                        print (f'【查邀请人】:我的邀请人:{OOOO000O000O0O00O}丨实名:{OOOOOOOO0O00OO0OO}')#line:636
                    else :#line:637
                        if O00000OOO00OO000O .innerId !='0':#line:638
                            O00000OOO00OO000O .invitation ()#line:639
        except Exception as O000OO000OOO00O00 :#line:640
            print (O000OO000OOO00O00 )#line:641
    def add_clover (OOOOOO0O0OOOOOOO0 ):#line:645
        global golden_seed #line:646
        try :#line:647
            OO00O000000OOO000 =f'__{timi_new()}'#line:648
            O00O0O00OO000O000 ={'authorization':OOOOOO0O0OOOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000000OOO000 ),'signstring':OO00O000000OOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:657
            O000OOOOOOOOOO000 =requests .request ('get',f'{host}/assets/clovers',headers =O00O0O00OO000O000 ).json ()#line:658
            if 'status'in O000OOOOOOOOOO000 :#line:660
                if O000OOOOOOOOOO000 ['status']==200 :#line:661
                    O00000OO0OOO0O0OO =O000OOOOOOOOOO000 ['data']['clover']#line:662
                    O0OOOOOO0O000000O =O000OOOOOOOOOO000 ['data']['used_clover']#line:663
                    O0OO0OO0O00OO0000 =float (O00000OO0OOO0O0OO )-float (O0OOOOOO0O000000O )#line:664
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0OOOOOO0O000000O}')#line:665
                    if OOOOOO0O0OOOOOOO0 .certification ()!='未实名':#line:666
                        if O0OO0OO0O00OO0000 >1 :#line:667
                            OO00O000000OOO000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OO0OO0O00OO0000)}_{timi_new()}'#line:668
                            O00O0O00OO000O000 ={'authorization':OOOOOO0O0OOOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000000OOO000 ),'signstring':OO00O000000OOO000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:677
                            O0O0OOO0O0O00O0OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OO0OO0O00OO0000 )}#line:678
                            O00OO0000000OO0OO =requests .request ('post',f'{host}/lottery/add-stake',headers =O00O0O00OO000O000 ,data =O0O0OOO0O0O00O0OO ).json ()#line:679
                            if 'status'in O00OO0000000OO0OO :#line:681
                                if O00OO0000000OO0OO ['status']==200 :#line:682
                                    print (f'【参与抽奖】:添加三叶草:{O00OO0000000OO0OO["data"]}丨数量:{O0OO0OO0O00OO0000}')#line:683
                                if O00OO0000000OO0OO ['status']==500 :#line:684
                                    print (f'【参与抽奖】:添加三叶草:{O00OO0000000OO0OO["message"]}')#line:685
            OOOOO000OO0OOOOOO =requests .request ('get',f'{host}/lottery',headers =O00O0O00OO000O000 ).json ()#line:686
            O00O0000O0O00OOOO =OOOOOO0O0OOOOOOO0 .winning_rewards ()#line:688
            if 'status'in OOOOO000OO0OOOOOO :#line:689
                if OOOOO000OO0OOOOOO ['status']==200 :#line:690
                    O000OO00OO000O00O =OOOOO000OO0OOOOOO ['data'][0 ]['day_get_gold_quantity']#line:691
                    golden_seed +=float (O000OO00OO000O00O )#line:692
                    print (f'【参与抽奖】:预计每天中{str(O000OO00OO000O00O)[:6]}颗金种子丨好友收益:{str(O00O0000O0O00OOOO)[:6]}')#line:693
        except Exception as OOOO0OOO0000O00OO :#line:694
            print (OOOO0OOO0000O00OO )#line:695
    def energy (OOO0O00OOOO00OO0O ):#line:698
        O0OO0O00O00O00000 =f'__{timi_new()}'#line:699
        OOO00O00OO00O0O0O ={'authorization':OOO0O00OOOO00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O00O00000 ),'signstring':O0OO0O00O00O00000 ,'version':'3.1.4191','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:708
        OOO00OOOOO0000O00 =requests .request ('get',f'{host}/energy/general',headers =OOO00O00OO00O0O0O ).json ()#line:709
        if 'status'in OOO00OOOOO0000O00 :#line:711
            if OOO00OOOOO0000O00 ['status']==200 :#line:712
                O00OO000OOOO0OOO0 =OOO00OOOOO0000O00 ['data']['ordinary_water']#line:713
                OOO00OO0OO00OO000 =OOO00OOOOO0000O00 ['data']['ordinary_fertilizer']#line:714
                print (f'【我的营养】:肥料:{str(OOO00OO0OO00OO000).split(".")[0]}丨水滴:{str(O00OO000OOOO0OOO0).split(".")[0]}')#line:715
                if float (OOO00OO0OO00OO000 )<96 :#line:716
                    time .sleep (random .randint (160 ,180 )/10 )#line:717
                    OOO0O0O00O00O00O0 =99 -float (OOO00OO0OO00OO000 )#line:718
                    OO000OO00OO000OO0 ={"fertilizer":str (OOO0O0O00O00O00O0 ).split ('.')[0 ]}#line:719
                    O0000000OO00O00O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOO00O00OO00O0O0O ).json ()#line:720
                    if 'status'in O0000000OO00O00O0 :#line:722
                        if O0000000OO00O00O0 ['status']==200 :#line:723
                            print (f'【购买肥料】:看广告获取肥料:{O0000000OO00O00O0["message"]}')#line:724
                if float (O00OO000OOOO0OOO0 )<880 :#line:725
                    time .sleep (random .randint (160 ,180 )/10 )#line:726
                    OOOOOO0000OOO00O0 =999 -float (O00OO000OOOO0OOO0 )#line:727
                    O0O0O00OO00O000OO ={"water":str (OOOOOO0000OOO00O0 ).split ('.')[0 ]}#line:728
                    O0O000O0OOO00OO00 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOO00O00OO00O0O0O ).json ()#line:729
                    if 'status'in O0O000O0OOO00OO00 :#line:731
                        if O0O000O0OOO00OO00 ['status']==200 :#line:732
                            print (f'【购买水滴】:看广告获取水滴:{O0O000O0OOO00OO00["message"]}')#line:733
def bundled_def ():#line:736
    O0O000000O00O00OO =['5570536','7750212','7911652','7911680','7805624']#line:737
    return O0O000000O00O00OO [random .randint (0 ,len (O0O000000O00O00OO )-1 )]#line:738
def version_of_the_validation ():#line:742
    return str ((71 -56 )/10 )#line:743
def gitee_validation ():#line:746
    try :#line:747
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:748
    except :#line:749
        sys .exit (0 )#line:750
def update_the_validation ():#line:754
    try :#line:755
        OOO00O0OO0OOOO000 =gitee_validation ()#line:756
        if version_of_the_validation ()<OOO00O0OO0OOOO000 ['CityEarth']['edition']:#line:757
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO00O0OO0OOOO000["CityEarth"]["edition"]}   ❌')#line:758
            print (f'更新内容=>>{OOO00O0OO0OOOO000["CityEarth"]["content"]}   👍')#line:759
        else :#line:760
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO00O0OO0OOOO000["CityEarth"]["edition"]}   ✅')#line:761
            print (f'更新内容=>> {OOO00O0OO0OOOO000["CityEarth"]["content"]}   👍')#line:762
    except Exception as O00OO0O00OOOOOOOO :#line:763
        print (O00OO0O00OOOOOOOO )#line:764
def os_qinglong ():#line:767
    if application in os .environ :#line:768
        O000O00OOOOO0OO0O =os .environ [application ].split ('\n')#line:769
        if len (O000O00OOOOO0OO0O )>0 :#line:770
            return O000O00OOOOO0OO0O #line:771
        else :#line:772
            print (f"{application}变量未启用")#line:773
            print ('脚本退出')#line:774
            sys .exit (1 )#line:775
    else :#line:776
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:778
        return os_built ()#line:779
def os_built ():#line:782
    if token :#line:783
        OO00O00O0O00OOO0O =token .split ('\n')#line:784
        if len (OO00O00O0O00OOO0O )>0 :#line:785
            return OO00O00O0O00OOO0O #line:786
    else :#line:787
        print (f"内置变量为空")#line:788
        print ('脚本结束')#line:789
        sys .exit (0 )#line:790
if __name__ =='__main__':#line:793
    start ()#line:794
