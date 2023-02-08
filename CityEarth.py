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
@ 版本  1.8
"""
change_nickname = False  # 
application = 'ce_token'  # 变量名
token = ''
time_xx = random.randint(8, 12)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
version ='3.1.419531'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        O0OO00O000O0O0000 =os_qinglong ()#line:10
        print (f"==========共找到{len(O0OO00O000O0O0000)}个账号==========")#line:11
        for O0O00000O00O00OO0 in O0OO00O000O0O0000 :#line:12
            print (f"------------正在执行第{O0OO00O000O0O0000.index(O0O00000O00O00OO0) + 1}个账号------------")#line:13
            O0O0OOOOO0OOOOOOO =CityEarth (O0O00000O00O00OO0 )#line:14
            def O0O0O0O00O0O000OO ():#line:16
                if O0O0OOOOO0OOOOOOO .base_info ():#line:18
                    O0O0OOOOO0OOOOOOO .sealing ()#line:20
                    O0O0OOOOO0OOOOOOO .invitenum ()#line:22
                    O0O0OOOOO0OOOOOOO .game_map ()#line:24
                    O0O0OOOOO0OOOOOOO .friends_invitation ()#line:26
                    O0O0OOOOO0OOOOOOO .add_clover ()#line:28
                    O0O0OOOOO0OOOOOOO .energy ()#line:30
                    O0O0OOOOO0OOOOOOO .propsraffle ()#line:32
                    O0O0OOOOO0OOOOOOO .synthetic ()#line:34
                    O0O0OOOOO0OOOOOOO .crops_illustrated ()#line:36
                    O0O0OOOOO0OOOOOOO .give_gold ()#line:38
                    O0O0OOOOO0OOOOOOO .withdraw ()#line:40
                else :#line:41
                    print ('token失效')#line:42
            O00000O000O0O00OO =threading .Thread (target =O0O0O0O00O0O000OO )#line:44
            O00000O000O0O00OO .start ()#line:45
            time .sleep (time_xx )#line:46
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:48
        time .sleep (3 )#line:49
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:50
    except Exception as O0O0OOOO0O000O0O0 :#line:51
        print (O0O0OOOO0O000O0O0 )#line:52
def sign (O0O000O0O00O0O0OO ):#line:55
    O0OO0O0OOOOO0OO00 =hashlib .md5 (O0O000O0O00O0O0OO .encode ()).hexdigest ()#line:56
    OO0000OO000O00OOO ="scsc%^&*"+O0OO0O0OOOOO0OO00 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:57
    O0OO000OO0000OO0O =hashlib .md5 (OO0000OO000O00OOO .encode ()).hexdigest ()#line:58
    return O0OO000OO0000OO0O #line:59
def timi_new ():#line:62
    return str (int (time .time ()*1000 ))#line:63
class CityEarth :#line:66
    def __init__ (OO00O0OO000O0000O ,O0OO000000000000O ):#line:68
        try :#line:69
            OO00O0OO000O0000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:70
            OO00O0OO000O0000O .token =O0OO000000000000O .split ('&')[0 ]#line:71
            OO00O0OO000O0000O .innerId =O0OO000000000000O .split ('&')[1 ]#line:72
            OO00O0OO000O0000O .doneeNo =O0OO000000000000O .split ('&')[2 ]#line:73
        except :#line:74
            print ('变量格式错误')#line:75
    def base_info (O00000OOO0O000OO0 ):#line:78
        try :#line:79
            O00000OOO0O000OO0 .watched_ad ()#line:81
            OOO000OO0OO00OOO0 =f'__{timi_new()}'#line:82
            OO0O000O0O0OOOOO0 ={'authorization':O00000OOO0O000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO0OO00OOO0 ),'signstring':OOO000OO0OO00OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:91
            OO0000O0O0OO00000 =requests .request ('get',f'{host}/user',headers =OO0O000O0O0OOOOO0 ).json ()#line:92
            if 'status'in OO0000O0O0OO00000 :#line:94
                if OO0000O0O0OO00000 ['status']==200 :#line:95
                    O00OO00OO0OOOOO00 =OO0000O0O0OO00000 ['data']['nickname']#line:96
                    OO000OO0OOOO0OOOO =OO0000O0O0OO00000 ['data']['inner_id']#line:97
                    OO0000O000OO0O0OO =OO0000O0O0OO00000 ['data']['assets']['gold']#line:98
                    OOOO0O0O0OO00OOOO =OO0000O0O0OO00000 ['data']['level']#line:99
                    print (f'【账号信息】:昵称:{O00OO00OO0OOOOO00[:5]}丨ID:{OO000OO0OOOO0OOOO}丨等级:{OOOO0O0O0OO00OOOO}丨种子:{str(OO0000O000OO0O0OO).split(".")[0]}')#line:101
                    if change_nickname :#line:102
                        O00000OOO0O000OO0 .change_nickname (OO000OO0OOOO0OOOO )#line:104
                if OO0000O0O0OO00000 ['status']==401 :#line:105
                    return False #line:106
                if OO0000O0O0OO00000 ['status']==500 :#line:107
                    return False #line:108
            return True #line:109
        except Exception as O0O0O00OOO000O0O0 :#line:110
            print (O0O0O00OOO000O0O0 )#line:111
    def sealing (OO000OOO0000OOOO0 ):#line:114
        try :#line:115
            O00O00O0O0OO000O0 =f'__{timi_new()}'#line:116
            O00OO00000OOOOO00 ={'authorization':OO000OOO0000OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O0OO000O0 ),'signstring':O00O00O0O0OO000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:125
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00OO00000OOOOO00 )#line:126
            requests .request ('get',f'{host}/packsack/list',headers =O00OO00000OOOOO00 )#line:127
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00OO00000OOOOO00 )#line:128
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00OO00000OOOOO00 )#line:129
            requests .request ('get',f'{host}/user',headers =O00OO00000OOOOO00 )#line:130
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00OO00000OOOOO00 )#line:131
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00OO00000OOOOO00 )#line:132
            requests .request ('post',f'{host}/announcement/announcement',headers =O00OO00000OOOOO00 )#line:133
            requests .request ('get',f'{host}/game/getAllData',headers =O00OO00000OOOOO00 )#line:134
            requests .request ('get',f'{host}/assets',headers =O00OO00000OOOOO00 )#line:135
        except Exception as OO0000O00O0O0OOO0 :#line:136
            print (OO0000O00O0O0OOO0 )#line:137
    def change_nickname (OOOO0OOO0OOO0O00O ,OO00000000OO00OO0 ):#line:140
        try :#line:141
            OO00O00OOO0OO0OO0 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:142
            O0O0O0O0OOO0OOO00 =requests .request ('post','https://www.qmsjmfb.com/',data =OO00O00OOO0OO0OO0 ).text #line:143
            OO0O00OO00OO00OO0 =re .findall ('<ul><li>(.*?)</li>',O0O0O0O0OOO0OOO00 )[0 ][:3 ]+str (OO00000000OO00OO0 )[5 :]#line:144
            OO0OO0O00O0O0OO00 =f'_nickname=_{timi_new()}'#line:145
            OOOOO00OOO00OO00O ={'authorization':OOOO0OOO0OOO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O00O0O0OO00 ),'signstring':OO0OO0O00O0O0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:154
            OO0O00OOO00OOO00O ={"nickname":OO0O00OO00OO00OO0 }#line:155
            OO0OOOO000O0O0OO0 =requests .patch (f'{host}/user/nickname',headers =OOOOO00OOO00OO00O ,json =OO0O00OOO00OOO00O ).json ()#line:156
            print (OO0OOOO000O0O0OO0 )#line:157
        except Exception as OOO000O00OOOOO0OO :#line:159
            print (OOO000O00OOOOO0OO )#line:160
    def withdraw (O000O00OO0O0000O0 ):#line:163
        O0000O00O00OO0OO0 =f'__{timi_new()}'#line:164
        OOOO0OOO0OOOOO0OO ={'authorization':O000O00OO0O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00O00OO0OO0 ),'signstring':O0000O00O00OO0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:173
        OO0OO0OOO00O0O0O0 =requests .request ('get',f'{host}/assets',headers =OOOO0OOO0OOOOO0OO ).json ()#line:174
        if 'status'in OO0OO0OOO00O0O0O0 :#line:176
            if OO0OO0OOO00O0O0O0 ['status']==200 :#line:177
                O00OO0OO0OO0OOOOO =OO0OO0OOO00O0O0O0 ['data']['cash']#line:178
                if float (O00OO0OO0OO0OOOOO )>20 :#line:179
                    O0000O00O00OO0OO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:180
                    OOOO0OOO0OOOOO0OO ={'authorization':O000O00OO0O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00O00OO0OO0 ),'signstring':O0000O00O00OO0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:189
                    OOOO0OO0000O00O00 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:190
                    O00OOOOOO00O00O0O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOO0OOO0OOOOO0OO ,data =OOOO0OO0000O00O00 ).json ()#line:192
                    print (O00OOOOOO00O00O0O )#line:193
    def invitenum (O0O0O0OOO00000O0O ):#line:196
        OO000OO0OO00OOOOO =f'__{timi_new()}'#line:197
        O000000OOOOO0O000 ={'authorization':O0O0O0OOO00000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0OO00OOOOO ),'signstring':OO000OO0OO00OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:206
        O0OO0000O00O0O000 =requests .request ('get',f'{host}/invite/invitenum',headers =O000000OOOOO0O000 ).json ()#line:207
        if 'status'in O0OO0000O00O0O000 :#line:209
            if O0OO0000O00O0O000 ['status']==200 :#line:210
                O000O00O0OOO00O0O =O0OO0000O00O0O000 ['data']['invited_count']#line:211
                O00OO0O0OOO0OO0O0 =O0OO0000O00O0O000 ['data']['invited_second_count']#line:212
                print (f'【我的邀请】:直邀好友:{O000O00O0OOO00O0O}丨间邀好友:{O00OO0O0OOO0OO0O0}')#line:213
    def game_map (OO0OOO00OOO00OOO0 ):#line:216
        try :#line:217
            OO0OOOO0O00O0OOOO =f'__{timi_new()}'#line:218
            O000OOO0OOO00OO0O ={'authorization':OO0OOO00OOO00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0O00O0OOOO ),'signstring':OO0OOOO0O00O0OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:227
            O0OO0OO00OO0OO000 =requests .request ('get',f'{host}/game/map',headers =O000OOO0OOO00OO0O ).json ()#line:228
            if 'status'in O0OO0OO00OO0OO000 :#line:230
                if O0OO0OO00OO0OO000 ['status']==200 :#line:231
                    for O00O0OO00O0O00O0O in O0OO0OO00OO0OO000 ['data']['list'][0 ]['crops']:#line:232
                        O00OO0000O000OOOO =O00O0OO00O0O00O0O ['level']#line:234
                        if O00OO0000O000OOOO ==41 :#line:235
                            O0OOO0000O0OOO00O =O00O0OO00O0O00O0O ['crop_name']#line:236
                            O0OOO0O0O00OO0000 =O00O0OO00O0O00O0O ['count']#line:237
                            if O0OOO0O0O00OO0000 >0 :#line:238
                                print (f'【农业资产】:{O0OOO0000O0OOO00O}丨数量:{O0OOO0O0O00OO0000}')#line:239
        except Exception as O0OO0000OOO0OOOOO :#line:240
            print (O0OO0000OOO0OOOOO )#line:241
    def give_gold (OO0O0OOO0O0OO0OOO ):#line:244
        try :#line:245
            OO000O0O0OOO00000 =f'__{timi_new()}'#line:246
            OO0O000O000O0O00O ={'authorization':OO0O0OOO0O0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O0OOO00000 ),'signstring':OO000O0O0OOO00000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:255
            O0OO000OO0OOOOOO0 =requests .request ('get',f'{host}/user',headers =OO0O000O000O0O00O ).json ()#line:256
            if 'status'in O0OO000OO0OOOOOO0 :#line:257
                if O0OO000OO0OOOOOO0 ['status']==200 :#line:258
                    if float (OO0O0OOO0O0OO0OOO .doneeNo )!=0 :#line:259
                        O0O0O0O0000000000 =O0OO000OO0OOOOOO0 ['data']['assets']['gold']#line:260
                        if float (O0O0O0O0000000000 )>float (OO0O0OOO0O0OO0OOO .innerId ):#line:261
                            OOOOO0O000O0OO00O =int (float (O0O0O0O0000000000 )/1.1 )#line:262
                            OO000O0O0OOO00000 =f'_doneeNo={OO0O0OOO0O0OO0OOO.doneeNo}&quantity={OOOOO0O000O0OO00O}_{timi_new()}'#line:263
                            OO0O000O000O0O00O ={'authorization':OO0O0OOO0O0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O0OOO00000 ),'signstring':OO000O0O0OOO00000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
                            OOO0O000OO00O00OO ={"quantity":OOOOO0O000O0OO00O ,"doneeNo":OO0O0OOO0O0OO0OOO .doneeNo }#line:276
                            OOOO00000OOOOO000 =requests .request ('post',f'{host}/finance/give-gold',headers =OO0O000O000O0O00O ,data =OOO0O000OO00O00OO ).json ()#line:277
                            if 'status'in OOOO00000OOOOO000 :#line:279
                                if OOOO00000OOOOO000 ['status']==200 :#line:280
                                    if OOOO00000OOOOO000 ['data']:#line:281
                                        print (f'【赠送种子】:赠送{OOOOO0O000O0OO00O}种子给{OO0O0OOO0O0OO0OOO.doneeNo}成功')#line:282
                    else :#line:283
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:284
        except Exception as OOOO00000O00OO0O0 :#line:285
            print (OOOO00000O00OO0O0 )#line:286
    def invitation (O00O0O00000000O0O ):#line:288
        try :#line:289
            _OO00O00O0OO000OOO =float (bundled_def ())/4 #line:290
            O0OOOOOO0O0O00000 =f'_innerId={int(_OO00O00O0OO000OOO)}_{timi_new()}'#line:291
            OOO0000O00OOOO000 ={'authorization':O00O0O00000000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOO0O0O00000 ),'signstring':O0OOOOOO0O0O00000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:300
            O000O0OOOO0OO00OO ={"innerId":int (_OO00O00O0OO000OOO )}#line:301
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO0000O00OOOO000 ,data =O000O0OOOO0OO00OO )#line:302
        except Exception as O00O0O0OO0OO00O0O :#line:303
            print (O00O0O0OO0OO00O0O )#line:304
    def winning_rewards (O0OO0OOOOOO0O0OOO ):#line:307
        try :#line:308
            OO0OO00000O0OOO0O =f'__{timi_new()}'#line:309
            O0OO0OOOOOO00O000 ={'authorization':O0OO0OOOOOO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00000O0OOO0O ),'signstring':OO0OO00000O0OOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:318
            O0OOOOOO0OO00OO0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OO0OOOOOO00O000 ).json ()#line:319
            if 'status'in O0OOOOOO0OO00OO0O :#line:321
                if O0OOOOOO0OO00OO0O ['status']==200 :#line:322
                    if O0OOOOOO0OO00OO0O ['data']['amount']:#line:323
                        O00O0O0OO0OOO0O00 =O0OOOOOO0OO00OO0O ['data']['amount']['gold']#line:324
                        return O00O0O0OO0OOO0O00 #line:325
                    else :#line:326
                        return 0 #line:327
        except Exception as O00O00OOOO0O000O0 :#line:328
            print (O00O00OOOO0O000O0 )#line:329
    def certification (OO00O0O000O0OOO0O ):#line:332
        try :#line:333
            OO0000O00O000O00O =f'__{timi_new()}'#line:334
            OOOOO00OOO00OOO00 ={'authorization':OO00O0O000O0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O00O000O00O ),'signstring':OO0000O00O000O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:343
            OOO0O000O00OO0OO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOOOO00OOO00OOO00 ).json ()#line:344
            if 'status'in OOO0O000O00OO0OO0 :#line:346
                if OOO0O000O00OO0OO0 ['status']==200 :#line:347
                    if OOO0O000O00OO0OO0 ['data']['result']:#line:348
                        O0OO0OO0OO0OOO0OO =OOO0O000O00OO0OO0 ['data']['nick_name']#line:349
                        return O0OO0OO0OO0OOO0OO #line:350
                    else :#line:351
                        return '未实名'#line:352
        except Exception as OO0OOO0O0OO00000O :#line:353
            print (OO0OOO0O0OO00000O )#line:354
    def crops_illustrated (OO000OOO00OO0OOO0 ):#line:357
        try :#line:358
            O0OOO00OO0000O00O =f'__{timi_new()}'#line:359
            O000O0000O000O000 ={'authorization':OO000OOO00OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OO0000O00O ),'signstring':O0OOO00OO0000O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:368
            O00O0O0O0000OO0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O000O0000O000O000 ).json ()#line:369
            if 'status'in O00O0O0O0000OO0O0 :#line:371
                if O00O0O0O0000OO0O0 ['status']==200 :#line:372
                    O00000O0O0O00O0O0 =O00O0O0O0000OO0O0 ['data'][0 ]['crops']#line:373
                    for OO0OOOOO0O00OO000 in O00000O0O0O00O0O0 :#line:374
                        if OO0OOOOO0O00OO000 ['ill_clover_award']:#line:375
                            if float (OO0OOOOO0O00OO000 ['ill_clover_award'])>1 :#line:376
                                if OO0OOOOO0O00OO000 ['is_finish']:#line:377
                                    if not OO0OOOOO0O00OO000 ['is_getit']:#line:378
                                        if OO000OOO00OO0OOO0 .certification ()!='未实名':#line:379
                                            O0OOO00OO0000O00O =f'_award_level={OO0OOOOO0O00OO000["level"]}_{timi_new()}'#line:380
                                            O000O0000O000O000 ={'authorization':OO000OOO00OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OO0000O00O ),'signstring':O0OOO00OO0000O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:389
                                            O000OOO00OOOOO0O0 ={"award_level":OO0OOOOO0O00OO000 ['level']}#line:390
                                            OOOOOO0OO0O00OO00 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O000O0000O000O000 ,json =O000OOO00OOOOO0O0 ).json ()#line:392
                                            if 'status'in OOOOOO0OO0O00OO00 :#line:393
                                                if OOOOOO0OO0O00OO00 ['status']==200 :#line:394
                                                    OOOO0OOO0OO0000O0 =OOOOOO0OO0O00OO00 ['data']['ill_clover_award']#line:395
                                                    print (f'【图鉴奖励】:领取{OO0OOOOO0O00OO000["crop_name"]}成就丨奖励{OOOO0OOO0OO0000O0}叶子成功')#line:397
                                                if OOOOOO0OO0O00OO00 ['status']==500 :#line:398
                                                    print (f'【图鉴奖励】:{OOOOOO0OO0O00OO00["message"]}')#line:399
        except Exception as OOOO000OO0O0OOO00 :#line:400
            print (OOOO000OO0O0OOO00 )#line:401
    def watched_ad (OO000000OOO0O0O0O ):#line:404
        try :#line:405
            O0O000OOO00OOO0O0 =f'__{timi_new()}'#line:406
            O0O0OO0OO000OOOO0 ={'authorization':OO000000OOO0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOO00OOO0O0 ),'signstring':O0O000OOO00OOO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:415
            O0000O0000OOO0OOO =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO0OO000OOOO0 ).json ()#line:416
            if 'status'in O0000O0000OOO0OOO :#line:418
                if O0000O0000OOO0OOO ['status']==200 :#line:419
                    if 'offlineInfo'in O0000O0000OOO0OOO ['data']:#line:420
                        OOOOO00O0OO0O000O =O0000O0000OOO0OOO ['data']['offlineInfo']['off_minute']#line:421
                        OO0O0OOO0000OOOO0 =float (O0000O0000OOO0OOO ['data']['silver'])/1000000000000 #line:422
                        time .sleep (1 )#line:423
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O0OO0OO000OOOO0 ).json ()#line:424
                        time .sleep (2 )#line:425
                        O0O0OOOO0000O0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO0OO000OOOO0 ).json ()#line:426
                        if 'status'in O0O0OOOO0000O0OO0 :#line:428
                            if O0O0OOOO0000O0OO0 ['status']==200 :#line:429
                                OO0O0OOO000OO0O00 =float (O0O0OOOO0000O0OO0 ['data']['silver'])/1000000000000 #line:430
                                OOOO0OOOO0OO0O000 =str (OO0O0OOO000OO0O00 -OO0O0OOO0000OOOO0 )[:6 ]#line:431
                                print (f'【离线奖励】:翻倍离线{OOOOO00O0OO0O000O}分钟奖励种子数量:{OOOO0OOOO0OO0O000}t粒')#line:432
        except Exception as O0000O00OO000OO00 :#line:433
            print (O0000O00OO000OO00 )#line:434
    def user_ad (O0O00OO0OOOO000OO ):#line:437
        try :#line:438
            OO00000OO00O00O00 =f'__{timi_new()}'#line:439
            O0O0OOOOO0O0OO00O ={'authorization':O0O00OO0OOOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OO00O00O00 ),'signstring':OO00000OO00O00O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:448
            O0O000O00O0OO0O00 =requests .request ('get',f'{host}/user/ad',headers =O0O0OOOOO0O0OO00O ).json ()#line:449
            if 'status'in O0O000O00O0OO0O00 :#line:451
                if O0O000O00O0OO0O00 ['status']==200 :#line:452
                    O0O000O00O0000O00 =O0O000O00O0OO0O00 ['data']['max_time']#line:453
                    OO000O0O0O00OO0OO =O0O000O00O0OO0O00 ['data']['watch_time']#line:454
                    OO0OOO0O00O0OOOOO =O0O000O00O0OO0O00 ['data']['added_time']#line:455
                    print (f'【获取种子】:获取种子剩余{OO0OOO0O00O0OOOOO + O0O000O00O0000O00 - OO000O0O0O00OO0OO}次丨好友提供:{OO0OOO0O00O0OOOOO}次')#line:456
                    if OO0OOO0O00O0OOOOO +O0O000O00O0000O00 -OO000O0O0O00OO0OO >0 :#line:457
                        time .sleep (random .randint (16 ,19 ))#line:458
                        OOO00O0OO0O000OO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O0OOOOO0O0OO00O ).json ()#line:459
                        if 'status'in OOO00O0OO0O000OO0 :#line:461
                            if OOO00O0OO0O000OO0 ['status']==200 :#line:462
                                O00OOOOOO0O0O0OOO =OOO00O0OO0O000OO0 ['data']['silver']#line:463
                                print (f'【获取种子】:获得种子:{O00OOOOOO0O0O0OOO}')#line:464
                                return True #line:465
                            if OOO00O0OO0O000OO0 ['status']==500 :#line:466
                                OOO00OO00OO000OO0 =OOO00O0OO0O000OO0 ['message']#line:467
                                print (f'【获取种子】:{OOO00OO00OO000OO0}')#line:468
                                return False #line:469
        except Exception as OO00000OOOO00OO00 :#line:470
            print (OO00000OOOO00OO00 )#line:471
    def synthetic (OO0OOOOO0OO0OOO0O ):#line:474
        global id ,g #line:475
        try :#line:476
            O00O00O0OO0OO000O =OO0OOOOO0OO0OOO0O .level_new ()#line:477
            while True :#line:478
                O0OO00O0OO0OOOOO0 =f'__{timi_new()}'#line:479
                OO0O0O0O000000O00 ={'authorization':OO0OOOOO0OO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0OO0OOOOO0 ),'signstring':O0OO00O0OO0OOOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                OO0O0OO0OO0O0O00O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O0O000000O00 ).json ()#line:489
                if 'status'in OO0O0OO0OO0O0O00O :#line:491
                    if OO0O0OO0OO0O0O00O ['status']==200 :#line:492
                        O0OOO0O000O0O0O00 =OO0O0OO0OO0O0O00O ['data']['cropList']#line:493
                        O000O00OOO0OOOO00 =OO0O0OO0OO0O0O00O ['data']['gameCoreDataDBid']#line:494
                        OOO0O000O000O00O0 =0 #line:495
                        for O00OOO00O00000O00 in O0OOO0O000O0O0O00 :#line:496
                            if not O00OOO00O00000O00 :#line:497
                                OOO00O00OOOOO0000 =f'_crop_id={O000O00OOO0OOOO00}&site={OOO0O000O000O00O0}_{OO0OOOOO0OO0OOO0O.time}'#line:498
                                O0O0000OO0O0O00OO ={'authorization':OO0OOOOO0OO0OOO0O .token ,'timestamp':OO0OOOOO0OO0OOO0O .time ,'sign':sign (OOO00O00OOOOO0000 ),'signstring':OOO00O00OOOOO0000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:507
                                O00OO0000O0OO00OO ={"site":OOO0O000O000O00O0 ,"crop_id":O000O00OOO0OOOO00 }#line:508
                                OO0000OOO00OOO00O =requests .request ('post',f'{host}/game/crops/buy',headers =O0O0000OO0O0O00OO ,data =O00OO0000O0OO00OO ).json ()#line:509
                                time .sleep (random .randint (1 ,3 )/10 )#line:511
                                if 'status'in OO0000OOO00OOO00O :#line:512
                                    if OO0000OOO00OOO00O ['status']==200 :#line:513
                                        if OO0000OOO00OOO00O ['message']=='种子数量不足':#line:514
                                            O00O00O0OO0OO000O =OO0OOOOO0OO0OOO0O .level_new ()#line:515
                                            print (f'【种植合成】:{OO0000OOO00OOO00O["message"]}')#line:516
                                            if not OO0OOOOO0OO0OOO0O .user_ad ():#line:517
                                                return False #line:518
                                    if OO0000OOO00OOO00O ['status']==500 :#line:519
                                        print (f'【种植合成】:{OO0000OOO00OOO00O["message"]}')#line:520
                                        return False #line:521
                            OOO0O000O000O00O0 +=1 #line:522
                        O0O0OO0OO000OO0OO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O0O000000O00 ).json ()#line:523
                        OOO0OOO00OOOOOOOO =O0O0OO0OO000OO0OO ['data']['cropList']#line:524
                        OO00OOOOOO0OOO000 =False #line:525
                        for O00OOO00O00000O00 in range (12 ):#line:526
                            id =OOO0OOO00OOOOOOOO [O00OOO00O00000O00 ]['level']#line:527
                            if float (O00O00O0OO0OO000O )-float (id )>9 :#line:528
                                O0OO0OOOOOO0O0O0O =f'_site={O00OOO00O00000O00}_{timi_new()}'#line:529
                                O000OO0000O00000O ={'accept':'application/json, text/plain, */*','authorization':OO0OOOOO0OO0OOO0O .token ,'timestamp':timi_new (),'sign':sign (O0OO0OOOOOO0O0O0O ),'signstring':O0OO0OOOOOO0O0O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:539
                                OOOO0O0OOO00O00OO ={"site":O00OOO00O00000O00 }#line:540
                                OO00000OOO0OOO0OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000OO0000O00000O ,data =OOOO0O0OOO00O00OO ).json ()#line:542
                                if 'status'in OO00000OOO0OOO0OO :#line:543
                                    if OO00000OOO0OOO0OO ['status']==200 :#line:544
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:545
                            if id !=0 :#line:546
                                for OOO0O0O00OOOOO000 in range (11 ):#line:547
                                    O00000OO0OOOO000O =OOO0O0O00OOOOO000 +1 #line:548
                                    g =OOO0OOO00OOOOOOOO [O00000OO0OOOO000O ]['level']#line:549
                                    if id ==g :#line:550
                                        O0000000O000OO0OO =OOO0O0O00OOOOO000 +2 #line:551
                                        if O0000000O000OO0OO !=O00OOO00O00000O00 +1 :#line:552
                                            OO00O00OOOOOO00OO =O00OOO00O00000O00 +1 #line:553
                                            time .sleep (random .randint (1 ,3 )/10 )#line:555
                                            O0O00O0O000O0OO0O =f'_site={OO00O00OOOOOO00OO - 1}&targetSite={O0000000O000OO0OO - 1}_{timi_new()}'#line:556
                                            OO0000OO0O00O0000 ={'accept':'application/json, text/plain, */*','authorization':OO0OOOOO0OO0OOO0O .token ,'timestamp':timi_new (),'sign':sign (O0O00O0O000O0OO0O ),'signstring':O0O00O0O000O0OO0O ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:571
                                            O0O000OO0O0O00000 ={"site":int (OO00O00OOOOOO00OO -1 ),"targetSite":int (O0000000O000OO0OO -1 )}#line:572
                                            OO000000O0O00000O =requests .request ('post',f'{host}/game/crops/move',headers =OO0000OO0O00O0000 ,json =O0O000OO0O0O00000 ).json ()#line:574
                                            if 'status'in OO000000O0O00000O :#line:575
                                                if OO000000O0O00000O ['status']==200 :#line:576
                                                    pass #line:577
                                            print ('【种植合成】:',OO00O00OOOOOO00OO ,O0000000O000OO0OO ,'合成成功')#line:579
                                            OO00OOOOOO0OOO000 =True #line:580
                                    if OO00OOOOOO0OOO000 :#line:581
                                        break #line:582
                                if OO00OOOOOO0OOO000 :#line:583
                                    break #line:584
        except Exception as O00O0O0OOOO00OOO0 :#line:585
            OO0OOOOO0OO0OOO0O .synthetic ()#line:586
    def level_new (OOO00O0000O0O0O0O ):#line:589
        try :#line:590
            O000O0O000OO0O0O0 =f'__{timi_new()}'#line:591
            O0OO0O000OO0O0O00 ={'authorization':OOO00O0000O0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O000OO0O0O0 ),'signstring':O000O0O000OO0O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            O0O000O00OO000OO0 =requests .request ('get',f'{host}/user',headers =O0OO0O000OO0O0O00 ).json ()#line:601
            if 'status'in O0O000O00OO000OO0 :#line:602
                if O0O000O00OO000OO0 ['status']==200 :#line:603
                    return float (O0O000O00OO000OO0 ['data']['level'])#line:604
        except Exception as OOOOO00OO0000OO0O :#line:605
            print (OOOOO00OO0000OO0O )#line:606
    def propsraffle (OO0OO00OOO00OO0O0 ):#line:609
        try :#line:610
            while True :#line:611
                OO00O00O000OOOO00 =f'__{timi_new()}'#line:612
                O0OOOOO00O00O0O0O ={'authorization':OO0OO00OOO00OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00O000OOOO00 ),'signstring':OO00O00O000OOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:621
                O0OOO0OOO00O00O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OOOOO00O00O0O0O ).json ()#line:622
                if 'status'in O0OOO0OOO00O00O0O :#line:624
                    if O0OOO0OOO00O00O0O ['status']==200 :#line:625
                        OO0OOO00O0000000O =O0OOO0OOO00O00O0O ['data']['rows']#line:626
                        O00O0O0O000000OOO =O0OOO0OOO00O00O0O ['data']['vstate']#line:627
                        if OO0OOO00O0000000O ==5 or OO0OOO00O0000000O ==6 or OO0OOO00O0000000O ==7 :#line:628
                            O000OOO00000O0O0O =O0OOO0OOO00O00O0O ['data']['silver']#line:629
                            print (f'【转盘抽奖】:获得种子:{O000OOO00000O0O0O}')#line:630
                        if OO0OOO00O0000000O ==1 or OO0OOO00O0000000O ==2 or OO0OOO00O0000000O ==3 :#line:631
                            O00O00OOO0O0000O0 =O0OOO0OOO00O00O0O ['data']['clover']#line:632
                            print (f'【转盘抽奖】:获得三叶草:{O00O00OOO0O0000O0}')#line:633
                        if OO0OOO00O0000000O ==4 or OO0OOO00O0000000O ==8 :#line:634
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:635
                        if OO0OOO00O0000000O =='抽奖次数已用完':#line:639
                            break #line:672
                time .sleep (random .randint (8 ,15 )/10 )#line:673
        except Exception as O0OOOO0O0O0OOOOO0 :#line:674
            print (O0OOOO0O0O0OOOOO0 )#line:675
    def friends_invitation (O0OOO0OO0OO00OOO0 ):#line:678
        try :#line:679
            OO0O00OOOO00000OO =f'__{timi_new()}'#line:680
            OO00OO0OO000OOO00 ={'authorization':O0OOO0OO0OO00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOOO00000OO ),'signstring':OO0O00OOOO00000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:689
            O00OO0000O000OO00 =requests .request ('get',f'{host}/friends',headers =OO00OO0OO000OOO00 ).json ()#line:690
            if 'status'in O00OO0000O000OO00 :#line:691
                if O00OO0000O000OO00 ['status']==200 :#line:692
                    OO0O0O000O00OOO0O =O00OO0000O000OO00 ['data']['myInviteter']#line:693
                    if OO0O0O000O00OOO0O :#line:694
                        OOO0OO0O0O0OO00O0 =OO0O0O000O00OOO0O ['user']['nickname']#line:695
                        O0OOOOOOOOO00O000 =O0OOO0OO0OO00OOO0 .certification ()#line:696
                        print (f'【查邀请人】:我的邀请人:{OOO0OO0O0O0OO00O0}丨实名:{O0OOOOOOOOO00O000}')#line:697
                    else :#line:698
                        if O0OOO0OO0OO00OOO0 .innerId !='0':#line:699
                            O0OOO0OO0OO00OOO0 .invitation ()#line:700
        except Exception as OOOO0OO0OO00000OO :#line:701
            print (OOOO0OO0OO00000OO )#line:702
    def add_clover (O000O0000OOO000O0 ):#line:705
        global golden_seed #line:706
        try :#line:707
            O000O00OOO0OOO0O0 =f'__{timi_new()}'#line:708
            OOO00O000OOO0O00O ={'authorization':O000O0000OOO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00OOO0OOO0O0 ),'signstring':O000O00OOO0OOO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:717
            OO000OO0OO0O0O0O0 =requests .request ('get',f'{host}/assets/clovers',headers =OOO00O000OOO0O00O ).json ()#line:718
            if 'status'in OO000OO0OO0O0O0O0 :#line:720
                if OO000OO0OO0O0O0O0 ['status']==200 :#line:721
                    OOO000O00OOOO0O00 =OO000OO0OO0O0O0O0 ['data']['clover']#line:722
                    OOOOO00OOO00O0OOO =OO000OO0OO0O0O0O0 ['data']['used_clover']#line:723
                    OOO0O000O0O000O00 =float (OOO000O00OOOO0O00 )-float (OOOOO00OOO00O0OOO )#line:724
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OOOOO00OOO00O0OOO}')#line:725
                    if O000O0000OOO000O0 .certification ()!='未实名':#line:726
                        if OOO0O000O0O000O00 >1 :#line:727
                            O000O00OOO0OOO0O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO0O000O0O000O00)}_{timi_new()}'#line:728
                            OOO00O000OOO0O00O ={'authorization':O000O0000OOO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00OOO0OOO0O0 ),'signstring':O000O00OOO0OOO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                            OO0OOO00O00000O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO0O000O0O000O00 )}#line:738
                            O00OOO00000OO0OO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO00O000OOO0O00O ,data =OO0OOO00O00000O0O ).json ()#line:739
                            if 'status'in O00OOO00000OO0OO0 :#line:741
                                if O00OOO00000OO0OO0 ['status']==200 :#line:742
                                    print (f'【参与抽奖】:添加三叶草:{O00OOO00000OO0OO0["data"]}丨数量:{OOO0O000O0O000O00}')#line:743
                                if O00OOO00000OO0OO0 ['status']==500 :#line:744
                                    print (f'【参与抽奖】:添加三叶草:{O00OOO00000OO0OO0["message"]}')#line:745
            O000000OOOO000OOO =requests .request ('get',f'{host}/lottery',headers =OOO00O000OOO0O00O ).json ()#line:746
            OO0OOOOOOOOO0O00O =O000O0000OOO000O0 .winning_rewards ()#line:748
            if 'status'in O000000OOOO000OOO :#line:749
                if O000000OOOO000OOO ['status']==200 :#line:750
                    O000OOOOO00OO0OOO =O000000OOOO000OOO ['data'][0 ]['day_get_gold_quantity']#line:751
                    golden_seed +=float (O000OOOOO00OO0OOO )#line:752
                    print (f'【参与抽奖】:预计每天中{str(O000OOOOO00OO0OOO)[:6]}颗金种子丨好友收益:{str(OO0OOOOOOOOO0O00O)[:6]}')#line:753
        except Exception as OOO00O0O00O000OO0 :#line:754
            print (OOO00O0O00O000OO0 )#line:755
    def energy (O000000OOOOO000OO ):#line:758
        try :#line:759
            while True :#line:760
                O00OO000OO00O0OO0 =f'__{timi_new()}'#line:761
                O00OOOOOO0OOO000O ={'authorization':O000000OOOOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000OO00O0OO0 ),'signstring':O00OO000OO00O0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:770
                OOO00O00OO0OOO0OO =requests .request ('get',f'{host}/energy/general',headers =O00OOOOOO0OOO000O ).json ()#line:771
                if 'status'in OOO00O00OO0OOO0OO :#line:773
                    if OOO00O00OO0OOO0OO ['status']==200 :#line:774
                        OO0O000OO00O0O00O =OOO00O00OO0OOO0OO ['data']['ordinary_water']#line:775
                        O0OOOO0OOO000OOOO =OOO00O00OO0OOO0OO ['data']['ordinary_fertilizer']#line:776
                        print (f'【我的营养】:肥料:{str(O0OOOO0OOO000OOOO).split(".")[0]}丨水滴:{str(OO0O000OO00O0O00O).split(".")[0]}')#line:778
                        if float (O0OOOO0OOO000OOOO )<96 :#line:779
                            time .sleep (random .randint (160 ,180 )/10 )#line:780
                            OOOO0OOO0OO0OOO0O =99 -float (O0OOOO0OOO000OOOO )#line:781
                            OOO0O0OOOOO0O0O0O ={"fertilizer":str (OOOO0OOO0OO0OOO0O ).split ('.')[0 ]}#line:782
                            OOOOOOO0OO00OO000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00OOOOOO0OOO000O ).json ()#line:783
                            if 'status'in OOOOOOO0OO00OO000 :#line:785
                                if OOOOOOO0OO00OO000 ['status']==200 :#line:786
                                    print (f'【购买肥料】:看广告获取肥料:{OOOOOOO0OO00OO000["message"]}')#line:787
                        if float (OO0O000OO00O0O00O )<880 :#line:788
                            time .sleep (random .randint (160 ,180 )/10 )#line:789
                            O00OOOOO00O000O00 =999 -float (OO0O000OO00O0O00O )#line:790
                            OOOO00O00OOOOO0OO ={"water":str (O00OOOOO00O000O00 ).split ('.')[0 ]}#line:791
                            O000O0OO000OO0OO0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00OOOOOO0OOO000O ).json ()#line:792
                            if 'status'in O000O0OO000OO0OO0 :#line:794
                                if O000O0OO000OO0OO0 ['status']==200 :#line:795
                                    print (f'【购买水滴】:看广告获取水滴:{O000O0OO000OO0OO0["message"]}')#line:796
                        if float (O0OOOO0OOO000OOOO )>96 and float (OO0O000OO00O0O00O )>880 :#line:797
                            break #line:798
        except Exception as OO0OO00000O0OOOO0 :#line:800
            print (OO0OO00000O0OOOO0 )#line:801
def bundled_def ():#line:803
    O0O0O0000O00OO0O0 =['5570536','7750212','7911652','7911680','7805624']#line:804
    return O0O0O0000O00OO0O0 [random .randint (0 ,len (O0O0O0000O00OO0O0 )-1 )]#line:805
def version_of_the_validation ():#line:809
    return str ((74 -56 )/10 )#line:810
def gitee_validation ():#line:813
    try :#line:814
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:815
    except :#line:816
        sys .exit (0 )#line:817
def update_the_validation ():#line:821
    try :#line:822
        O0O000000OO00000O =gitee_validation ()#line:823
        if version_of_the_validation ()<O0O000000OO00000O ['CityEarth']['edition']:#line:824
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O000000OO00000O["CityEarth"]["edition"]}   ❌')#line:825
            print (f'更新内容=>>{O0O000000OO00000O["CityEarth"]["content"]}   👍')#line:826
        else :#line:827
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O000000OO00000O["CityEarth"]["edition"]}   ✅')#line:828
            print (f'更新内容=>> {O0O000000OO00000O["CityEarth"]["content"]}   👍')#line:829
    except Exception as O00OOOO00OOOO000O :#line:830
        print (O00OOOO00OOOO000O )#line:831
def os_qinglong ():#line:834
    if application in os .environ :#line:835
        O0O0000000O00O0OO =os .environ [application ].split ('\n')#line:836
        if len (O0O0000000O00O0OO )>0 :#line:837
            return O0O0000000O00O0OO #line:838
        else :#line:839
            print (f"{application}变量未启用")#line:840
            print ('脚本退出')#line:841
            sys .exit (1 )#line:842
    else :#line:843
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:845
        return os_built ()#line:846
def os_built ():#line:849
    if token :#line:850
        OOOO0000O00O0OO0O =token .split ('\n')#line:851
        if len (OOOO0000O00O0OO0O )>0 :#line:852
            return OOOO0000O00O0OO0O #line:853
    else :#line:854
        print (f"内置变量为空")#line:855
        print ('脚本结束')#line:856
        sys .exit (0 )#line:857
if __name__ =='__main__':#line:860
    start ()#line:861
