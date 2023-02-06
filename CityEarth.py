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
@ 版本  1.6
"""
change_nickname = False     
application = 'ce_token' 
token = ''
time_xx = random.randint(8, 12)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
version ='3.1.4195'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        O000O0O0O0OO0O0OO =os_qinglong ()#line:10
        print (f"==========共找到{len(O000O0O0O0OO0O0OO)}个账号==========")#line:11
        for OOO0OOO0000000OO0 in O000O0O0O0OO0O0OO :#line:12
            print (f"------------正在执行第{O000O0O0O0OO0O0OO.index(OOO0OOO0000000OO0) + 1}个账号------------")#line:13
            O00OO00O0OOO000O0 =CityEarth (OOO0OOO0000000OO0 )#line:14
            def OO0O00O0O0OOOO00O ():#line:16
                if O00OO00O0OOO000O0 .base_info ():#line:18
                    O00OO00O0OOO000O0 .sealing ()#line:20
                    O00OO00O0OOO000O0 .watched_ad ()#line:22
                    O00OO00O0OOO000O0 .invitenum ()#line:24
                    O00OO00O0OOO000O0 .game_map ()#line:26
                    O00OO00O0OOO000O0 .friends_invitation ()#line:28
                    O00OO00O0OOO000O0 .add_clover ()#line:30
                    O00OO00O0OOO000O0 .energy ()#line:32
                    O00OO00O0OOO000O0 .propsraffle ()#line:34
                    O00OO00O0OOO000O0 .synthetic ()#line:36
                    O00OO00O0OOO000O0 .crops_illustrated ()#line:38
                    O00OO00O0OOO000O0 .give_gold ()#line:40
                    O00OO00O0OOO000O0 .withdraw ()#line:42
                else :#line:43
                    print ('token失效')#line:44
            OOO0000O0OO00O0O0 =threading .Thread (target =OO0O00O0O0OOOO00O )#line:46
            OOO0000O0OO00O0O0 .start ()#line:47
            time .sleep (time_xx )#line:48
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:50
        time .sleep (3 )#line:51
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:52
    except Exception as OO00OOO0000O0000O :#line:53
        print (OO00OOO0000O0000O )#line:54
def sign (OO0OOOOO0OOO00OOO ):#line:57
    O0OOO00O00O0O0OOO =hashlib .md5 (OO0OOOOO0OOO00OOO .encode ()).hexdigest ()#line:58
    OO0OO0OOO00O000O0 ="scsc%^&*"+O0OOO00O00O0O0OOO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:59
    OOOO0OO00O0O00OO0 =hashlib .md5 (OO0OO0OOO00O000O0 .encode ()).hexdigest ()#line:60
    return OOOO0OO00O0O00OO0 #line:61
def timi_new ():#line:64
    return str (int (time .time ()*1000 ))#line:65
class CityEarth :#line:68
    def __init__ (O0O0OOOOO000O0OO0 ,OOO000O0000OOOOO0 ):#line:70
        try :#line:71
            O0O0OOOOO000O0OO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:72
            O0O0OOOOO000O0OO0 .token =OOO000O0000OOOOO0 .split ('&')[0 ]#line:73
            O0O0OOOOO000O0OO0 .innerId =OOO000O0000OOOOO0 .split ('&')[1 ]#line:74
            O0O0OOOOO000O0OO0 .doneeNo =OOO000O0000OOOOO0 .split ('&')[2 ]#line:75
        except :#line:76
            print ('变量格式错误')#line:77
    def base_info (O0OOO0OO0O00OO00O ):#line:80
        try :#line:81
            OOOO00O0OO00O0000 =f'__{timi_new()}'#line:82
            O0O0OOO0O0000O00O ={'authorization':O0OOO0OO0O00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0OO00O0000 ),'signstring':OOOO00O0OO00O0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:91
            OO0OOOOOOO0O00O00 =requests .request ('get',f'{host}/user',headers =O0O0OOO0O0000O00O ).json ()#line:92
            if 'status'in OO0OOOOOOO0O00O00 :#line:94
                if OO0OOOOOOO0O00O00 ['status']==200 :#line:95
                    O00OOO00O0OO0OO0O =OO0OOOOOOO0O00O00 ['data']['nickname']#line:96
                    OO00OOO0OO00OOO00 =OO0OOOOOOO0O00O00 ['data']['inner_id']#line:97
                    OOO000O0OOOOOOO00 =OO0OOOOOOO0O00O00 ['data']['assets']['gold']#line:98
                    OO0O00O0O0O0O0OO0 =OO0OOOOOOO0O00O00 ['data']['level']#line:99
                    print (f'【账号信息】:昵称:{O00OOO00O0OO0OO0O[:5]}丨ID:{OO00OOO0OO00OOO00}丨等级:{OO0O00O0O0O0O0OO0}丨种子:{str(OOO000O0OOOOOOO00).split(".")[0]}')#line:101
                    if change_nickname :#line:102
                        O0OOO0OO0O00OO00O .change_nickname (OO00OOO0OO00OOO00 )#line:104
                if OO0OOOOOOO0O00O00 ['status']==401 :#line:105
                    return False #line:106
                if OO0OOOOOOO0O00O00 ['status']==500 :#line:107
                    return False #line:108
            return True #line:109
        except Exception as OO0OOO0OOO0O0000O :#line:110
            print (OO0OOO0OOO0O0000O )#line:111
    def sealing (O0O0O0O0OOOOOOOOO ):#line:114
        try :#line:115
            O00OOO0000OO0OOO0 =f'__{timi_new()}'#line:116
            O0000000OO0O0OOO0 ={'authorization':O0O0O0O0OOOOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0000OO0OOO0 ),'signstring':O00OOO0000OO0OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:125
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0000000OO0O0OOO0 )#line:126
            requests .request ('get',f'{host}/packsack/list',headers =O0000000OO0O0OOO0 )#line:127
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0000000OO0O0OOO0 )#line:128
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0000000OO0O0OOO0 )#line:129
            requests .request ('get',f'{host}/user',headers =O0000000OO0O0OOO0 )#line:130
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0000000OO0O0OOO0 )#line:131
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0000000OO0O0OOO0 )#line:132
            requests .request ('post',f'{host}/announcement/announcement',headers =O0000000OO0O0OOO0 )#line:133
            requests .request ('get',f'{host}/game/getAllData',headers =O0000000OO0O0OOO0 )#line:134
            requests .request ('get',f'{host}/assets',headers =O0000000OO0O0OOO0 )#line:135
        except Exception as O00000OO000O000OO :#line:136
            print (O00000OO000O000OO )#line:137
    def change_nickname (O00O0OOO00OO0O0OO ,OO000O00OO000000O ):#line:140
        try :#line:141
            O0OOO000OOO000OOO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:142
            O00OOO0000O0O0OOO =requests .request ('post','https://www.qmsjmfb.com/',data =O0OOO000OOO000OOO ).text #line:143
            O0O000O00O0OOOOO0 =re .findall ('<ul><li>(.*?)</li>',O00OOO0000O0O0OOO )[0 ][:3 ]+str (OO000O00OO000000O )[5 :]#line:144
            OO0O0OO0O0O0000O0 =f'_nickname=_{timi_new()}'#line:145
            OOO0O0O0O000O0O0O ={'authorization':O00O0OOO00OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO0O0O0000O0 ),'signstring':OO0O0OO0O0O0000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:154
            OO00OO000000OO000 ={"nickname":O0O000O00O0OOOOO0 }#line:155
            OO00O00000O0OO0O0 =requests .patch (f'{host}/user/nickname',headers =OOO0O0O0O000O0O0O ,json =OO00OO000000OO000 ).json ()#line:156
            print (OO00O00000O0OO0O0 )#line:157
        except Exception as O00O00000OO0O00OO :#line:159
            print (O00O00000OO0O00OO )#line:160
    def withdraw (OOO00O00O0O00OOO0 ):#line:163
        OO00O00000O00OOOO =f'__{timi_new()}'#line:164
        O00OO0OO0O00OOOOO ={'authorization':OOO00O00O0O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00000O00OOOO ),'signstring':OO00O00000O00OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:173
        O0O0OO0OOOO00O0O0 =requests .request ('get',f'{host}/assets',headers =O00OO0OO0O00OOOOO ).json ()#line:174
        if 'status'in O0O0OO0OOOO00O0O0 :#line:176
            if O0O0OO0OOOO00O0O0 ['status']==200 :#line:177
                O000O000OOO00O0OO =O0O0OO0OOOO00O0O0 ['data']['cash']#line:178
                if float (O000O000OOO00O0OO )>20 :#line:179
                    OO00O00000O00OOOO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:180
                    O00OO0OO0O00OOOOO ={'authorization':OOO00O00O0O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00000O00OOOO ),'signstring':OO00O00000O00OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:189
                    OO0O0OOO0OOOOO0OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:190
                    OO0OOO000000OO00O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00OO0OO0O00OOOOO ,data =OO0O0OOO0OOOOO0OO ).json ()#line:192
                    print (OO0OOO000000OO00O )#line:193
    def invitenum (OOOO0OO00000OOO0O ):#line:196
        OOOOO000OOOOOOOO0 =f'__{timi_new()}'#line:197
        O0O0000O000OO00OO ={'authorization':OOOO0OO00000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO000OOOOOOOO0 ),'signstring':OOOOO000OOOOOOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:206
        OOO000OO0OOO000O0 =requests .request ('get',f'{host}/invite/invitenum',headers =O0O0000O000OO00OO ).json ()#line:207
        if 'status'in OOO000OO0OOO000O0 :#line:209
            if OOO000OO0OOO000O0 ['status']==200 :#line:210
                OO00OOOOOOOOO000O =OOO000OO0OOO000O0 ['data']['invited_count']#line:211
                O0OOO0OO000O0O0O0 =OOO000OO0OOO000O0 ['data']['invited_second_count']#line:212
                print (f'【我的邀请】:直邀好友:{OO00OOOOOOOOO000O}丨间邀好友:{O0OOO0OO000O0O0O0}')#line:213
    def game_map (O0OOOOO0O00OOO0OO ):#line:216
        try :#line:217
            O0O0O0O0000OO00O0 =f'__{timi_new()}'#line:218
            O0OO00O0OO000O000 ={'authorization':O0OOOOO0O00OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0000OO00O0 ),'signstring':O0O0O0O0000OO00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:227
            OOO00O0O0OO0OO00O =requests .request ('get',f'{host}/game/map',headers =O0OO00O0OO000O000 ).json ()#line:228
            if 'status'in OOO00O0O0OO0OO00O :#line:230
                if OOO00O0O0OO0OO00O ['status']==200 :#line:231
                    for OOO0O0OOOOOO000OO in OOO00O0O0OO0OO00O ['data']['list'][0 ]['crops']:#line:232
                        O000O0OO0000OO0OO =OOO0O0OOOOOO000OO ['level']#line:234
                        if O000O0OO0000OO0OO ==41 :#line:235
                            O000O00OO00O0O0O0 =OOO0O0OOOOOO000OO ['crop_name']#line:236
                            OO00OOO0O00OO000O =OOO0O0OOOOOO000OO ['count']#line:237
                            if OO00OOO0O00OO000O >0 :#line:238
                                print (f'【农业资产】:{O000O00OO00O0O0O0}丨数量:{OO00OOO0O00OO000O}')#line:239
        except Exception as O00OO0O0OO0OOO0OO :#line:240
            print (O00OO0O0OO0OOO0OO )#line:241
    def give_gold (OOOOO0OOO00OO00O0 ):#line:244
        try :#line:245
            OOO00OO0OOO000O0O =f'__{timi_new()}'#line:246
            OOOO000O0O0OOOO0O ={'authorization':OOOOO0OOO00OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0OOO000O0O ),'signstring':OOO00OO0OOO000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:255
            OO0000O00000OOOO0 =requests .request ('get',f'{host}/user',headers =OOOO000O0O0OOOO0O ).json ()#line:256
            if 'status'in OO0000O00000OOOO0 :#line:257
                if OO0000O00000OOOO0 ['status']==200 :#line:258
                    if float (OOOOO0OOO00OO00O0 .doneeNo )!=0 :#line:259
                        OO0OO00OO000OO00O =OO0000O00000OOOO0 ['data']['assets']['gold']#line:260
                        if float (OO0OO00OO000OO00O )>float (OOOOO0OOO00OO00O0 .innerId ):#line:261
                            O000OOO0000OOO00O =int (float (OO0OO00OO000OO00O )/1.1 )#line:262
                            OOO00OO0OOO000O0O =f'_doneeNo={OOOOO0OOO00OO00O0.doneeNo}&quantity={O000OOO0000OOO00O}_{timi_new()}'#line:263
                            OOOO000O0O0OOOO0O ={'authorization':OOOOO0OOO00OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0OOO000O0O ),'signstring':OOO00OO0OOO000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
                            O0OO00OO00O000000 ={"quantity":O000OOO0000OOO00O ,"doneeNo":OOOOO0OOO00OO00O0 .doneeNo }#line:276
                            OOOOO0OO0O0O0O000 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOO000O0O0OOOO0O ,data =O0OO00OO00O000000 ).json ()#line:277
                            if 'status'in OOOOO0OO0O0O0O000 :#line:279
                                if OOOOO0OO0O0O0O000 ['status']==200 :#line:280
                                    if OOOOO0OO0O0O0O000 ['data']:#line:281
                                        print (f'【赠送种子】:赠送{O000OOO0000OOO00O}种子给{OOOOO0OOO00OO00O0.doneeNo}成功')#line:282
                    else :#line:283
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:284
        except Exception as OO0OOO00O0O0OO0OO :#line:285
            print (OO0OOO00O0O0OO0OO )#line:286
    def invitation (OOO00OOOO0O00OO0O ):#line:288
        try :#line:289
            _O0OOOOOOOOO0O0000 =float (bundled_def ())/4 #line:290
            OO0O00O0OOOOO00OO =f'_innerId={int(_O0OOOOOOOOO0O0000)}_{timi_new()}'#line:291
            OOO00OO000O00OOO0 ={'authorization':OOO00OOOO0O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O0OOOOO00OO ),'signstring':OO0O00O0OOOOO00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:300
            O00O0000OO0O0OO00 ={"innerId":int (_O0OOOOOOOOO0O0000 )}#line:301
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO00OO000O00OOO0 ,data =O00O0000OO0O0OO00 )#line:302
        except Exception as OO00OOOO0O0O0O00O :#line:303
            print (OO00OOOO0O0O0O00O )#line:304
    def winning_rewards (OO0O0OO00O0OO000O ):#line:307
        try :#line:308
            O00O00O0O0OOOOO00 =f'__{timi_new()}'#line:309
            O0OOO000O0OOOO00O ={'authorization':OO0O0OO00O0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O0OOOOO00 ),'signstring':O00O00O0O0OOOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:318
            OO00O00000O00OOO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOO000O0OOOO00O ).json ()#line:319
            if 'status'in OO00O00000O00OOO0 :#line:321
                if OO00O00000O00OOO0 ['status']==200 :#line:322
                    if OO00O00000O00OOO0 ['data']['amount']:#line:323
                        OOOO00OOOOOO0O00O =OO00O00000O00OOO0 ['data']['amount']['gold']#line:324
                        return OOOO00OOOOOO0O00O #line:325
                    else :#line:326
                        return 0 #line:327
        except Exception as O00OOOO00OOOOOO00 :#line:328
            print (O00OOOO00OOOOOO00 )#line:329
    def certification (OO0000OO00O0O0OOO ):#line:332
        try :#line:333
            O0O0O0OOOO000OO0O =f'__{timi_new()}'#line:334
            O000O0O0OO0OO000O ={'authorization':OO0000OO00O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOO000OO0O ),'signstring':O0O0O0OOOO000OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:343
            OO000OO0OO0OOO00O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O000O0O0OO0OO000O ).json ()#line:344
            if 'status'in OO000OO0OO0OOO00O :#line:346
                if OO000OO0OO0OOO00O ['status']==200 :#line:347
                    if OO000OO0OO0OOO00O ['data']['result']:#line:348
                        OOO0OO00OO00O00O0 =OO000OO0OO0OOO00O ['data']['nick_name']#line:349
                        return OOO0OO00OO00O00O0 #line:350
                    else :#line:351
                        return '未实名'#line:352
        except Exception as O0O0O0O000OOO0O0O :#line:353
            print (O0O0O0O000OOO0O0O )#line:354
    def crops_illustrated (OO0O0OOO0OO000000 ):#line:357
        try :#line:358
            O0OO0OO0OOOOO0OO0 =f'__{timi_new()}'#line:359
            OO0O0OO00O0O0000O ={'authorization':OO0O0OOO0OO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0OOOOO0OO0 ),'signstring':O0OO0OO0OOOOO0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:368
            O0O0O00O000OO00O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O0OO00O0O0000O ).json ()#line:369
            if 'status'in O0O0O00O000OO00O0 :#line:371
                if O0O0O00O000OO00O0 ['status']==200 :#line:372
                    O00OOOOO00O00000O =O0O0O00O000OO00O0 ['data'][0 ]['crops']#line:373
                    for O000O0O0O0OOO00OO in O00OOOOO00O00000O :#line:374
                        if O000O0O0O0OOO00OO ['ill_clover_award']:#line:375
                            if float (O000O0O0O0OOO00OO ['ill_clover_award'])>1 :#line:376
                                if O000O0O0O0OOO00OO ['is_finish']:#line:377
                                    if not O000O0O0O0OOO00OO ['is_getit']:#line:378
                                        if OO0O0OOO0OO000000 .certification ()!='未实名':#line:379
                                            O0OO0OO0OOOOO0OO0 =f'_award_level={O000O0O0O0OOO00OO["level"]}_{timi_new()}'#line:380
                                            OO0O0OO00O0O0000O ={'authorization':OO0O0OOO0OO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0OOOOO0OO0 ),'signstring':O0OO0OO0OOOOO0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:389
                                            OOO0O00O0O0O0O0OO ={"award_level":O000O0O0O0OOO00OO ['level']}#line:390
                                            OO0O0OOO00OOOOOOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O0OO00O0O0000O ,json =OOO0O00O0O0O0O0OO ).json ()#line:392
                                            if 'status'in OO0O0OOO00OOOOOOO :#line:393
                                                if OO0O0OOO00OOOOOOO ['status']==200 :#line:394
                                                    OOOOOOO0O00OO000O =OO0O0OOO00OOOOOOO ['data']['ill_clover_award']#line:395
                                                    print (f'【图鉴奖励】:领取{O000O0O0O0OOO00OO["crop_name"]}成就丨奖励{OOOOOOO0O00OO000O}叶子成功')#line:397
                                                if OO0O0OOO00OOOOOOO ['status']==500 :#line:398
                                                    print (f'【图鉴奖励】:{OO0O0OOO00OOOOOOO["message"]}')#line:399
        except Exception as O0000OO0OO00O0O0O :#line:400
            print (O0000OO0OO00O0O0O )#line:401
    def watched_ad (OOOO0OO0000000O00 ):#line:404
        try :#line:405
            O0OO0O00O00O00O00 =f'__{timi_new()}'#line:406
            OOOO0O0OO0OOO0OO0 ={'authorization':OOOO0OO0000000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O00O00O00 ),'signstring':O0OO0O00O00O00O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:415
            O0000OO0O0OOOOOOO =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0O0OO0OOO0OO0 ).json ()#line:416
            if 'status'in O0000OO0O0OOOOOOO :#line:418
                if O0000OO0O0OOOOOOO ['status']==200 :#line:419
                    O0O000O00O00OOOOO =O0000OO0O0OOOOOOO ['data']['silver']#line:420
                    print (f'【离线奖励】:翻倍前种子数量:{O0O000O00O00OOOOO}')#line:421
            time .sleep (1 )#line:422
            requests .request ('post',f'{host}/game/watched-ad',headers =OOOO0O0OO0OOO0OO0 ).json ()#line:423
            time .sleep (2 )#line:424
            O0O00O0O0OOOO00OO =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0O0OO0OOO0OO0 ).json ()#line:425
            if 'status'in O0O00O0O0OOOO00OO :#line:426
                if O0O00O0O0OOOO00OO ['status']==200 :#line:427
                    O0O00OO0OO00O000O =O0O00O0O0OOOO00OO ['data']['silver']#line:428
                    print (f'【离线奖励】:翻倍后种子数量"{O0O00OO0OO00O000O}')#line:429
        except Exception as O0OOOO0O0000000OO :#line:432
            print (O0OOOO0O0000000OO )#line:433
    def user_ad (O00O0000OOO0000OO ):#line:436
        try :#line:437
            OO00000O0OO00O0OO =f'__{timi_new()}'#line:438
            O0O00OOO0OOO0OOOO ={'authorization':O00O0000OOO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000O0OO00O0OO ),'signstring':OO00000O0OO00O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:447
            O00O0O0O0OOO0O0O0 =requests .request ('get',f'{host}/user/ad',headers =O0O00OOO0OOO0OOOO ).json ()#line:448
            if 'status'in O00O0O0O0OOO0O0O0 :#line:450
                if O00O0O0O0OOO0O0O0 ['status']==200 :#line:451
                    O0O00OO0O0O0000OO =O00O0O0O0OOO0O0O0 ['data']['max_time']#line:452
                    O0O0OO0OO0O0000OO =O00O0O0O0OOO0O0O0 ['data']['watch_time']#line:453
                    OO0000OO00O00O00O =O00O0O0O0OOO0O0O0 ['data']['added_time']#line:454
                    print (f'【获取种子】:获取种子剩余{OO0000OO00O00O00O + O0O00OO0O0O0000OO - O0O0OO0OO0O0000OO}次丨好友提供:{OO0000OO00O00O00O}次')#line:455
                    if OO0000OO00O00O00O +O0O00OO0O0O0000OO -O0O0OO0OO0O0000OO >0 :#line:456
                        time .sleep (random .randint (16 ,19 ))#line:457
                        O00OOOO00O0OOOOO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O00OOO0OOO0OOOO ).json ()#line:458
                        if 'status'in O00OOOO00O0OOOOO0 :#line:460
                            if O00OOOO00O0OOOOO0 ['status']==200 :#line:461
                                O0OO0OOO0O0O0OOOO =O00OOOO00O0OOOOO0 ['data']['silver']#line:462
                                print (f'【获取种子】:获得种子:{O0OO0OOO0O0O0OOOO}')#line:463
                                return True #line:464
                            if O00OOOO00O0OOOOO0 ['status']==500 :#line:465
                                O0OOOOOOO0O0O0000 =O00OOOO00O0OOOOO0 ['message']#line:466
                                print (f'【获取种子】:{O0OOOOOOO0O0O0000}')#line:467
                                return False #line:468
        except Exception as O000O000O0OOOO00O :#line:469
            print (O000O000O0OOOO00O )#line:470
    def synthetic (O00O0000OOOO0OO00 ):#line:473
        global id ,g #line:474
        try :#line:475
            OO00O0000O0OOOO00 =O00O0000OOOO0OO00 .level_new ()#line:476
            while True :#line:477
                O0O0O00OOOO0OO00O =f'__{timi_new()}'#line:478
                OO0O00O00OO0O000O ={'authorization':O00O0000OOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OOOO0OO00O ),'signstring':O0O0O00OOOO0OO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:487
                OOOO0O0OOOO00O0O0 =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00O00OO0O000O ).json ()#line:488
                if 'status'in OOOO0O0OOOO00O0O0 :#line:490
                    if OOOO0O0OOOO00O0O0 ['status']==200 :#line:491
                        OO00000O0OOO0OO0O =OOOO0O0OOOO00O0O0 ['data']['cropList']#line:492
                        OOOO0O0O0OOO0O0O0 =OOOO0O0OOOO00O0O0 ['data']['gameCoreDataDBid']#line:493
                        O0O00O0000O0O00O0 =0 #line:494
                        for OO0OO0000000O00O0 in OO00000O0OOO0OO0O :#line:495
                            if not OO0OO0000000O00O0 :#line:496
                                OOOOOOO0000000000 =f'_crop_id={OOOO0O0O0OOO0O0O0}&site={O0O00O0000O0O00O0}_{O00O0000OOOO0OO00.time}'#line:497
                                OO000O00O00000OOO ={'authorization':O00O0000OOOO0OO00 .token ,'timestamp':O00O0000OOOO0OO00 .time ,'sign':sign (OOOOOOO0000000000 ),'signstring':OOOOOOO0000000000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:506
                                OOO0O0OO00OOO0000 ={"site":O0O00O0000O0O00O0 ,"crop_id":OOOO0O0O0OOO0O0O0 }#line:507
                                O00OO0OOOOOOO00OO =requests .request ('post',f'{host}/game/crops/buy',headers =OO000O00O00000OOO ,data =OOO0O0OO00OOO0000 ).json ()#line:508
                                time .sleep (random .randint (1 ,3 )/10 )#line:510
                                if 'status'in O00OO0OOOOOOO00OO :#line:511
                                    if O00OO0OOOOOOO00OO ['status']==200 :#line:512
                                        if O00OO0OOOOOOO00OO ['message']=='种子数量不足':#line:513
                                            OO00O0000O0OOOO00 =O00O0000OOOO0OO00 .level_new ()#line:514
                                            print (f'【种植合成】:{O00OO0OOOOOOO00OO["message"]}')#line:515
                                            if not O00O0000OOOO0OO00 .user_ad ():#line:516
                                                return False #line:517
                                    if O00OO0OOOOOOO00OO ['status']==500 :#line:518
                                        print (f'【种植合成】:{O00OO0OOOOOOO00OO["message"]}')#line:519
                                        return False #line:520
                            O0O00O0000O0O00O0 +=1 #line:521
                        O00OO00000O0000OO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00O00OO0O000O ).json ()#line:522
                        OO0O0OOO00000OO00 =O00OO00000O0000OO ['data']['cropList']#line:523
                        OOOO0O0O0OO000OOO =False #line:524
                        for OO0OO0000000O00O0 in range (12 ):#line:525
                            id =OO0O0OOO00000OO00 [OO0OO0000000O00O0 ]['level']#line:526
                            if float (OO00O0000O0OOOO00 )-float (id )>9 :#line:527
                                OOOO0OO0O0O00O0O0 =f'_site={OO0OO0000000O00O0}_{timi_new()}'#line:528
                                O000OOOOO0000O0O0 ={'accept':'application/json, text/plain, */*','authorization':O00O0000OOOO0OO00 .token ,'timestamp':timi_new (),'sign':sign (OOOO0OO0O0O00O0O0 ),'signstring':OOOO0OO0O0O00O0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:538
                                OO0OOOOO0OOOOOOOO ={"site":OO0OO0000000O00O0 }#line:539
                                O0OOO0000000O0OO0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000OOOOO0000O0O0 ,data =OO0OOOOO0OOOOOOOO ).json ()#line:541
                                if 'status'in O0OOO0000000O0OO0 :#line:542
                                    if O0OOO0000000O0OO0 ['status']==200 :#line:543
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:544
                            if id !=0 :#line:545
                                for OOOO0OOOO0OO00000 in range (11 ):#line:546
                                    OOOO0OO000OO000OO =OOOO0OOOO0OO00000 +1 #line:547
                                    g =OO0O0OOO00000OO00 [OOOO0OO000OO000OO ]['level']#line:548
                                    if id ==g :#line:549
                                        OO0O000OO0O00O0OO =OOOO0OOOO0OO00000 +2 #line:550
                                        if OO0O000OO0O00O0OO !=OO0OO0000000O00O0 +1 :#line:551
                                            O00O0OOOO00O000O0 =OO0OO0000000O00O0 +1 #line:552
                                            time .sleep (random .randint (1 ,3 )/10 )#line:554
                                            O0O000O00O0OOOO00 =f'_site={O00O0OOOO00O000O0 - 1}&targetSite={OO0O000OO0O00O0OO - 1}_{timi_new()}'#line:555
                                            OOO0O0O0O0OO00OO0 ={'accept':'application/json, text/plain, */*','authorization':O00O0000OOOO0OO00 .token ,'timestamp':timi_new (),'sign':sign (O0O000O00O0OOOO00 ),'signstring':O0O000O00O0OOOO00 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:570
                                            O000OO00000OOO0O0 ={"site":int (O00O0OOOO00O000O0 -1 ),"targetSite":int (OO0O000OO0O00O0OO -1 )}#line:571
                                            O000OOO0O0OO0OOOO =requests .request ('post',f'{host}/game/crops/move',headers =OOO0O0O0O0OO00OO0 ,json =O000OO00000OOO0O0 ).json ()#line:573
                                            if 'status'in O000OOO0O0OO0OOOO :#line:574
                                                if O000OOO0O0OO0OOOO ['status']==200 :#line:575
                                                    pass #line:576
                                            print ('【种植合成】:',O00O0OOOO00O000O0 ,OO0O000OO0O00O0OO ,'合成成功')#line:578
                                            OOOO0O0O0OO000OOO =True #line:579
                                    if OOOO0O0O0OO000OOO :#line:580
                                        break #line:581
                                if OOOO0O0O0OO000OOO :#line:582
                                    break #line:583
        except Exception as OO0OOOO00OO00O0O0 :#line:584
            O00O0000OOOO0OO00 .synthetic ()#line:585
    def level_new (OO0O0000O0O00O000 ):#line:588
        try :#line:589
            O0OOOO00OOOO00OO0 =f'__{timi_new()}'#line:590
            OOO0O00O000OO000O ={'authorization':OO0O0000O0O00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00OOOO00OO0 ),'signstring':O0OOOO00OOOO00OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:599
            O00000O00OO0OOO00 =requests .request ('get',f'{host}/user',headers =OOO0O00O000OO000O ).json ()#line:600
            if 'status'in O00000O00OO0OOO00 :#line:601
                if O00000O00OO0OOO00 ['status']==200 :#line:602
                    return float (O00000O00OO0OOO00 ['data']['level'])#line:603
        except Exception as O000OO0000O0OOO00 :#line:604
            print (O000OO0000O0OOO00 )#line:605
    def propsraffle (OO0O0OOO0OOOOOOOO ):#line:608
        try :#line:609
            while True :#line:610
                OOOO0000OOO00000O =f'__{timi_new()}'#line:611
                OOO0OOOOO00O0OO00 ={'authorization':OO0O0OOO0OOOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000OOO00000O ),'signstring':OOOO0000OOO00000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:620
                O0O00OOOO00O0OO00 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO0OOOOO00O0OO00 ).json ()#line:621
                if 'status'in O0O00OOOO00O0OO00 :#line:623
                    if O0O00OOOO00O0OO00 ['status']==200 :#line:624
                        OO000O000O0OO0OO0 =O0O00OOOO00O0OO00 ['data']['rows']#line:625
                        O0000OO00OO0000OO =O0O00OOOO00O0OO00 ['data']['vstate']#line:626
                        if OO000O000O0OO0OO0 ==5 or OO000O000O0OO0OO0 ==6 or OO000O000O0OO0OO0 ==7 :#line:627
                            O000000O00O0O0O0O =O0O00OOOO00O0OO00 ['data']['silver']#line:628
                            print (f'【转盘抽奖】:获得种子:{O000000O00O0O0O0O}')#line:629
                        if OO000O000O0OO0OO0 ==1 or OO000O000O0OO0OO0 ==2 or OO000O000O0OO0OO0 ==3 :#line:630
                            OOOOO0O00O0000O0O =O0O00OOOO00O0OO00 ['data']['clover']#line:631
                            print (f'【转盘抽奖】:获得三叶草:{OOOOO0O00O0000O0O}')#line:632
                        if OO000O000O0OO0OO0 ==4 or OO000O000O0OO0OO0 ==8 :#line:633
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:634
                        if OO000O000O0OO0OO0 =='抽奖次数已用完':#line:638
                            break #line:671
                time .sleep (random .randint (8 ,15 )/10 )#line:672
        except Exception as O0OOO0O00O00OO0OO :#line:673
            print (O0OOO0O00O00OO0OO )#line:674
    def friends_invitation (O00OO00O00O0OOOO0 ):#line:677
        try :#line:678
            O0OO00O0O0OOOOO00 =f'__{timi_new()}'#line:679
            OO0O000000OOO0O00 ={'authorization':O00OO00O00O0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0O0OOOOO00 ),'signstring':O0OO00O0O0OOOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:688
            OOO0OO00O0OOO0O00 =requests .request ('get',f'{host}/friends',headers =OO0O000000OOO0O00 ).json ()#line:689
            if 'status'in OOO0OO00O0OOO0O00 :#line:690
                if OOO0OO00O0OOO0O00 ['status']==200 :#line:691
                    O0O0000O00000O000 =OOO0OO00O0OOO0O00 ['data']['myInviteter']#line:692
                    if O0O0000O00000O000 :#line:693
                        O000O0OOO0O0O0000 =O0O0000O00000O000 ['user']['nickname']#line:694
                        O0O0OOO000O000O00 =O00OO00O00O0OOOO0 .certification ()#line:695
                        print (f'【查邀请人】:我的邀请人:{O000O0OOO0O0O0000}丨实名:{O0O0OOO000O000O00}')#line:696
                    else :#line:697
                        if O00OO00O00O0OOOO0 .innerId !='0':#line:698
                            O00OO00O00O0OOOO0 .invitation ()#line:699
        except Exception as OO0OOO000OO0000OO :#line:700
            print (OO0OOO000OO0000OO )#line:701
    def add_clover (OOO0OOO000OO000O0 ):#line:704
        global golden_seed #line:705
        try :#line:706
            O0O0O0O0OO0OO00OO =f'__{timi_new()}'#line:707
            OOOOO0OOOO0OOO000 ={'authorization':OOO0OOO000OO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0OO0OO00OO ),'signstring':O0O0O0O0OO0OO00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:716
            OO0O0O0OOOO00OOO0 =requests .request ('get',f'{host}/assets/clovers',headers =OOOOO0OOOO0OOO000 ).json ()#line:717
            if 'status'in OO0O0O0OOOO00OOO0 :#line:719
                if OO0O0O0OOOO00OOO0 ['status']==200 :#line:720
                    OO00O00O00O00000O =OO0O0O0OOOO00OOO0 ['data']['clover']#line:721
                    O0OOOO000O0OOO00O =OO0O0O0OOOO00OOO0 ['data']['used_clover']#line:722
                    O0O000O00000O0000 =float (OO00O00O00O00000O )-float (O0OOOO000O0OOO00O )#line:723
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0OOOO000O0OOO00O}')#line:724
                    if OOO0OOO000OO000O0 .certification ()!='未实名':#line:725
                        if O0O000O00000O0000 >1 :#line:726
                            O0O0O0O0OO0OO00OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O000O00000O0000)}_{timi_new()}'#line:727
                            OOOOO0OOOO0OOO000 ={'authorization':OOO0OOO000OO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0OO0OO00OO ),'signstring':O0O0O0O0OO0OO00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:736
                            OOO00OOOO0O0OO000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O000O00000O0000 )}#line:737
                            O00O0OOOO0OOO00OO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOOO0OOOO0OOO000 ,data =OOO00OOOO0O0OO000 ).json ()#line:738
                            if 'status'in O00O0OOOO0OOO00OO :#line:740
                                if O00O0OOOO0OOO00OO ['status']==200 :#line:741
                                    print (f'【参与抽奖】:添加三叶草:{O00O0OOOO0OOO00OO["data"]}丨数量:{O0O000O00000O0000}')#line:742
                                if O00O0OOOO0OOO00OO ['status']==500 :#line:743
                                    print (f'【参与抽奖】:添加三叶草:{O00O0OOOO0OOO00OO["message"]}')#line:744
            OOOO00O00OO0O0000 =requests .request ('get',f'{host}/lottery',headers =OOOOO0OOOO0OOO000 ).json ()#line:745
            OOOOOOOOO00O0O0OO =OOO0OOO000OO000O0 .winning_rewards ()#line:747
            if 'status'in OOOO00O00OO0O0000 :#line:748
                if OOOO00O00OO0O0000 ['status']==200 :#line:749
                    OO00O0O00OO0O0OOO =OOOO00O00OO0O0000 ['data'][0 ]['day_get_gold_quantity']#line:750
                    golden_seed +=float (OO00O0O00OO0O0OOO )#line:751
                    print (f'【参与抽奖】:预计每天中{str(OO00O0O00OO0O0OOO)[:6]}颗金种子丨好友收益:{str(OOOOOOOOO00O0O0OO)[:6]}')#line:752
        except Exception as OOOOO0O00OO00OO0O :#line:753
            print (OOOOO0O00OO00OO0O )#line:754
    def energy (OO0O00000OOO0O0OO ):#line:757
        OOO0OO0O00OOO00OO =f'__{timi_new()}'#line:758
        OO000000OOO0000OO ={'authorization':OO0O00000OOO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O00OOO00OO ),'signstring':OOO0OO0O00OOO00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:767
        OOO00O00OO0O00O0O =requests .request ('get',f'{host}/energy/general',headers =OO000000OOO0000OO ).json ()#line:768
        if 'status'in OOO00O00OO0O00O0O :#line:770
            if OOO00O00OO0O00O0O ['status']==200 :#line:771
                OO000O0OOO0O0OO00 =OOO00O00OO0O00O0O ['data']['ordinary_water']#line:772
                OOO0O0O00OOO0O00O =OOO00O00OO0O00O0O ['data']['ordinary_fertilizer']#line:773
                print (f'【我的营养】:肥料:{str(OOO0O0O00OOO0O00O).split(".")[0]}丨水滴:{str(OO000O0OOO0O0OO00).split(".")[0]}')#line:775
                if float (OOO0O0O00OOO0O00O )<96 :#line:776
                    time .sleep (random .randint (160 ,180 )/10 )#line:777
                    O0O0OO0O00OOO00OO =99 -float (OOO0O0O00OOO0O00O )#line:778
                    O00000OOO00O0O0OO ={"fertilizer":str (O0O0OO0O00OOO00OO ).split ('.')[0 ]}#line:779
                    OO00OO0O00OOOO0O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO000000OOO0000OO ).json ()#line:780
                    if 'status'in OO00OO0O00OOOO0O0 :#line:782
                        if OO00OO0O00OOOO0O0 ['status']==200 :#line:783
                            print (f'【购买肥料】:看广告获取肥料:{OO00OO0O00OOOO0O0["message"]}')#line:784
                if float (OO000O0OOO0O0OO00 )<880 :#line:785
                    time .sleep (random .randint (160 ,180 )/10 )#line:786
                    O000OO00OOO000O00 =999 -float (OO000O0OOO0O0OO00 )#line:787
                    OOO00O0O0OO0OOO00 ={"water":str (O000OO00OOO000O00 ).split ('.')[0 ]}#line:788
                    OO0OOO0O0OO0OO000 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO000000OOO0000OO ).json ()#line:789
                    if 'status'in OO0OOO0O0OO0OO000 :#line:791
                        if OO0OOO0O0OO0OO000 ['status']==200 :#line:792
                            print (f'【购买水滴】:看广告获取水滴:{OO0OOO0O0OO0OO000["message"]}')#line:793
def bundled_def ():#line:796
    OOO00O000OO00O0OO =['5570536','7750212','7911652','7911680','7805624']#line:797
    return OOO00O000OO00O0OO [random .randint (0 ,len (OOO00O000OO00O0OO )-1 )]#line:798
def version_of_the_validation ():#line:802
    return str ((72 -56 )/10 )#line:803
def gitee_validation ():#line:806
    try :#line:807
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:808
    except :#line:809
        sys .exit (0 )#line:810
def update_the_validation ():#line:814
    try :#line:815
        O000O0OO0000O0OOO =gitee_validation ()#line:816
        if version_of_the_validation ()<O000O0OO0000O0OOO ['CityEarth']['edition']:#line:817
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000O0OO0000O0OOO["CityEarth"]["edition"]}   ❌')#line:818
            print (f'更新内容=>>{O000O0OO0000O0OOO["CityEarth"]["content"]}   👍')#line:819
        else :#line:820
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000O0OO0000O0OOO["CityEarth"]["edition"]}   ✅')#line:821
            print (f'更新内容=>> {O000O0OO0000O0OOO["CityEarth"]["content"]}   👍')#line:822
    except Exception as OOOOOO0O00OOO00OO :#line:823
        print (OOOOOO0O00OOO00OO )#line:824
def os_qinglong ():#line:827
    if application in os .environ :#line:828
        O0OO00OO000O0O00O =os .environ [application ].split ('\n')#line:829
        if len (O0OO00OO000O0O00O )>0 :#line:830
            return O0OO00OO000O0O00O #line:831
        else :#line:832
            print (f"{application}变量未启用")#line:833
            print ('脚本退出')#line:834
            sys .exit (1 )#line:835
    else :#line:836
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:838
        return os_built ()#line:839
def os_built ():#line:842
    if token :#line:843
        O00000OOO000OO00O =token .split ('\n')#line:844
        if len (O00000OOO000OO00O )>0 :#line:845
            return O00000OOO000OO00O #line:846
    else :#line:847
        print (f"内置变量为空")#line:848
        print ('脚本结束')#line:849
        sys .exit (0 )#line:850
if __name__ =='__main__':#line:853
    start ()#line:854
