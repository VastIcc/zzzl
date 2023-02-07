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
@ 版本  1.7
"""
change_nickname = False  # True 为修改昵称      False 为不修改
application = 'ce_token'  # 变量名
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
        O0OOO0OO00OOO00OO =os_qinglong ()#line:10
        print (f"==========共找到{len(O0OOO0OO00OOO00OO)}个账号==========")#line:11
        for OOO0O00OOOOO00OO0 in O0OOO0OO00OOO00OO :#line:12
            print (f"------------正在执行第{O0OOO0OO00OOO00OO.index(OOO0O00OOOOO00OO0) + 1}个账号------------")#line:13
            OOOO0OOO0O0000OOO =CityEarth (OOO0O00OOOOO00OO0 )#line:14
            def O0OOO000O00OO00OO ():#line:16
                if OOOO0OOO0O0000OOO .base_info ():#line:18
                    OOOO0OOO0O0000OOO .sealing ()#line:20
                    OOOO0OOO0O0000OOO .invitenum ()#line:22
                    OOOO0OOO0O0000OOO .game_map ()#line:24
                    OOOO0OOO0O0000OOO .friends_invitation ()#line:26
                    OOOO0OOO0O0000OOO .add_clover ()#line:28
                    OOOO0OOO0O0000OOO .energy ()#line:30
                    OOOO0OOO0O0000OOO .propsraffle ()#line:32
                    OOOO0OOO0O0000OOO .synthetic ()#line:34
                    OOOO0OOO0O0000OOO .crops_illustrated ()#line:36
                    OOOO0OOO0O0000OOO .give_gold ()#line:38
                    OOOO0OOO0O0000OOO .withdraw ()#line:40
                else :#line:41
                    print ('token失效')#line:42
            O0O0000OO000O00O0 =threading .Thread (target =O0OOO000O00OO00OO )#line:44
            O0O0000OO000O00O0 .start ()#line:45
            time .sleep (time_xx )#line:46
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:48
        time .sleep (3 )#line:49
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:50
    except Exception as O0OOOOOO000O000O0 :#line:51
        print (O0OOOOOO000O000O0 )#line:52
def sign (O00000O00O0O00OO0 ):#line:55
    OO00OOOOOO00O0OO0 =hashlib .md5 (O00000O00O0O00OO0 .encode ()).hexdigest ()#line:56
    O00O00OO00000O00O ="scsc%^&*"+OO00OOOOOO00O0OO0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:57
    OO0OOOOOOO00OO000 =hashlib .md5 (O00O00OO00000O00O .encode ()).hexdigest ()#line:58
    return OO0OOOOOOO00OO000 #line:59
def timi_new ():#line:62
    return str (int (time .time ()*1000 ))#line:63
class CityEarth :#line:66
    def __init__ (OOO00O000O00OO00O ,OOO0O000OOOOO0O0O ):#line:68
        try :#line:69
            OOO00O000O00OO00O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:70
            OOO00O000O00OO00O .token =OOO0O000OOOOO0O0O .split ('&')[0 ]#line:71
            OOO00O000O00OO00O .innerId =OOO0O000OOOOO0O0O .split ('&')[1 ]#line:72
            OOO00O000O00OO00O .doneeNo =OOO0O000OOOOO0O0O .split ('&')[2 ]#line:73
        except :#line:74
            print ('变量格式错误')#line:75
    def base_info (O000OO00OOO0O000O ):#line:78
        try :#line:79
            O000OO00OOO0O000O .watched_ad ()#line:81
            O0OOOO000O00O00O0 =f'__{timi_new()}'#line:82
            OOO0OOOOOO00OOOO0 ={'authorization':O000OO00OOO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO000O00O00O0 ),'signstring':O0OOOO000O00O00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:91
            OOOOOOO000OO00000 =requests .request ('get',f'{host}/user',headers =OOO0OOOOOO00OOOO0 ).json ()#line:92
            if 'status'in OOOOOOO000OO00000 :#line:94
                if OOOOOOO000OO00000 ['status']==200 :#line:95
                    OO0OO000O0O0OOOOO =OOOOOOO000OO00000 ['data']['nickname']#line:96
                    OO000OO000OOO00OO =OOOOOOO000OO00000 ['data']['inner_id']#line:97
                    OOOOO0000OOOOO0OO =OOOOOOO000OO00000 ['data']['assets']['gold']#line:98
                    O000O00OO0OO00O0O =OOOOOOO000OO00000 ['data']['level']#line:99
                    print (f'【账号信息】:昵称:{OO0OO000O0O0OOOOO[:5]}丨ID:{OO000OO000OOO00OO}丨等级:{O000O00OO0OO00O0O}丨种子:{str(OOOOO0000OOOOO0OO).split(".")[0]}')#line:101
                    if change_nickname :#line:102
                        O000OO00OOO0O000O .change_nickname (OO000OO000OOO00OO )#line:104
                if OOOOOOO000OO00000 ['status']==401 :#line:105
                    return False #line:106
                if OOOOOOO000OO00000 ['status']==500 :#line:107
                    return False #line:108
            return True #line:109
        except Exception as OOOOOO00OO00O00O0 :#line:110
            print (OOOOOO00OO00O00O0 )#line:111
    def sealing (O000000OOO00OOO00 ):#line:114
        try :#line:115
            OO0OO00OOO0O00OOO =f'__{timi_new()}'#line:116
            O0OOOOOO000OOOOOO ={'authorization':O000000OOO00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00OOO0O00OOO ),'signstring':OO0OO00OOO0O00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:125
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OOOOOO000OOOOOO )#line:126
            requests .request ('get',f'{host}/packsack/list',headers =O0OOOOOO000OOOOOO )#line:127
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OOOOOO000OOOOOO )#line:128
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OOOOOO000OOOOOO )#line:129
            requests .request ('get',f'{host}/user',headers =O0OOOOOO000OOOOOO )#line:130
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OOOOOO000OOOOOO )#line:131
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OOOOOO000OOOOOO )#line:132
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OOOOOO000OOOOOO )#line:133
            requests .request ('get',f'{host}/game/getAllData',headers =O0OOOOOO000OOOOOO )#line:134
            requests .request ('get',f'{host}/assets',headers =O0OOOOOO000OOOOOO )#line:135
        except Exception as O0O0O0O00000OOOO0 :#line:136
            print (O0O0O0O00000OOOO0 )#line:137
    def change_nickname (O00O0O00OOO00O0O0 ,O00O0O0OO0OO0O0OO ):#line:140
        try :#line:141
            O000OO0O000O00OOO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:142
            O0O0OO0OOO00O0000 =requests .request ('post','https://www.qmsjmfb.com/',data =O000OO0O000O00OOO ).text #line:143
            OO0O00OO0O000OOO0 =re .findall ('<ul><li>(.*?)</li>',O0O0OO0OOO00O0000 )[0 ][:3 ]+str (O00O0O0OO0OO0O0OO )[5 :]#line:144
            O000OOOO0OO0O0OOO =f'_nickname=_{timi_new()}'#line:145
            OO0OOO00OO0OOOO0O ={'authorization':O00O0O00OOO00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOO0OO0O0OOO ),'signstring':O000OOOO0OO0O0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:154
            O000O00O0O0OO00OO ={"nickname":OO0O00OO0O000OOO0 }#line:155
            O0OOOO0OOO0O0O0OO =requests .patch (f'{host}/user/nickname',headers =OO0OOO00OO0OOOO0O ,json =O000O00O0O0OO00OO ).json ()#line:156
            print (O0OOOO0OOO0O0O0OO )#line:157
        except Exception as OO00O0OOOO0OO0OOO :#line:159
            print (OO00O0OOOO0OO0OOO )#line:160
    def withdraw (O00O0O0OO000OO000 ):#line:163
        OOO00OO00000OOOOO =f'__{timi_new()}'#line:164
        O00OO0OO0OOO0OOO0 ={'authorization':O00O0O0OO000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO00000OOOOO ),'signstring':OOO00OO00000OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:173
        O0O00OOO000OO0O0O =requests .request ('get',f'{host}/assets',headers =O00OO0OO0OOO0OOO0 ).json ()#line:174
        if 'status'in O0O00OOO000OO0O0O :#line:176
            if O0O00OOO000OO0O0O ['status']==200 :#line:177
                OOOOOO000OO0OO0OO =O0O00OOO000OO0O0O ['data']['cash']#line:178
                if float (OOOOOO000OO0OO0OO )>20 :#line:179
                    OOO00OO00000OOOOO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:180
                    O00OO0OO0OOO0OOO0 ={'authorization':O00O0O0OO000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO00000OOOOO ),'signstring':OOO00OO00000OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:189
                    OOO0O000000O0O0OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:190
                    OO0O00O0OO00O0000 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00OO0OO0OOO0OOO0 ,data =OOO0O000000O0O0OO ).json ()#line:192
                    print (OO0O00O0OO00O0000 )#line:193
    def invitenum (OO00000OO0O00OO00 ):#line:196
        OOO000O0O0O0O000O =f'__{timi_new()}'#line:197
        OO00OO0OO0OOOO0OO ={'authorization':OO00000OO0O00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0O0O0O000O ),'signstring':OOO000O0O0O0O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:206
        OO00O0OO00O0OO0OO =requests .request ('get',f'{host}/invite/invitenum',headers =OO00OO0OO0OOOO0OO ).json ()#line:207
        if 'status'in OO00O0OO00O0OO0OO :#line:209
            if OO00O0OO00O0OO0OO ['status']==200 :#line:210
                OO0OOO00O00O0O00O =OO00O0OO00O0OO0OO ['data']['invited_count']#line:211
                O00O0O000O0O0O00O =OO00O0OO00O0OO0OO ['data']['invited_second_count']#line:212
                print (f'【我的邀请】:直邀好友:{OO0OOO00O00O0O00O}丨间邀好友:{O00O0O000O0O0O00O}')#line:213
    def game_map (OOOOOO000OOO0OOO0 ):#line:216
        try :#line:217
            OOOO00OOOO00000O0 =f'__{timi_new()}'#line:218
            O0OO0O0000OOO0OOO ={'authorization':OOOOOO000OOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOOO00000O0 ),'signstring':OOOO00OOOO00000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:227
            O00OO0O00OOOOOOO0 =requests .request ('get',f'{host}/game/map',headers =O0OO0O0000OOO0OOO ).json ()#line:228
            if 'status'in O00OO0O00OOOOOOO0 :#line:230
                if O00OO0O00OOOOOOO0 ['status']==200 :#line:231
                    for OO0OO00OO0OOOOOO0 in O00OO0O00OOOOOOO0 ['data']['list'][0 ]['crops']:#line:232
                        OO00O0O000O0OOO0O =OO0OO00OO0OOOOOO0 ['level']#line:234
                        if OO00O0O000O0OOO0O ==41 :#line:235
                            OO0O00000000000O0 =OO0OO00OO0OOOOOO0 ['crop_name']#line:236
                            O0O0000OOOO0OOOO0 =OO0OO00OO0OOOOOO0 ['count']#line:237
                            if O0O0000OOOO0OOOO0 >0 :#line:238
                                print (f'【农业资产】:{OO0O00000000000O0}丨数量:{O0O0000OOOO0OOOO0}')#line:239
        except Exception as OO00OO000O000OO0O :#line:240
            print (OO00OO000O000OO0O )#line:241
    def give_gold (O0000OOO0O0O00OO0 ):#line:244
        try :#line:245
            O0O00O0OO0OOOOO0O =f'__{timi_new()}'#line:246
            OOO0OO0OOOOOOOOO0 ={'authorization':O0000OOO0O0O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OO0OOOOO0O ),'signstring':O0O00O0OO0OOOOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:255
            O0O000000O00O0OOO =requests .request ('get',f'{host}/user',headers =OOO0OO0OOOOOOOOO0 ).json ()#line:256
            if 'status'in O0O000000O00O0OOO :#line:257
                if O0O000000O00O0OOO ['status']==200 :#line:258
                    if float (O0000OOO0O0O00OO0 .doneeNo )!=0 :#line:259
                        OOOO0O0O0OOOOOO00 =O0O000000O00O0OOO ['data']['assets']['gold']#line:260
                        if float (OOOO0O0O0OOOOOO00 )>float (O0000OOO0O0O00OO0 .innerId ):#line:261
                            O00O0O0000000OOO0 =int (float (OOOO0O0O0OOOOOO00 )/1.1 )#line:262
                            O0O00O0OO0OOOOO0O =f'_doneeNo={O0000OOO0O0O00OO0.doneeNo}&quantity={O00O0O0000000OOO0}_{timi_new()}'#line:263
                            OOO0OO0OOOOOOOOO0 ={'authorization':O0000OOO0O0O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OO0OOOOO0O ),'signstring':O0O00O0OO0OOOOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
                            OO0OO0O000OOO000O ={"quantity":O00O0O0000000OOO0 ,"doneeNo":O0000OOO0O0O00OO0 .doneeNo }#line:276
                            OOOO00O0OOO0OO0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0OO0OOOOOOOOO0 ,data =OO0OO0O000OOO000O ).json ()#line:277
                            if 'status'in OOOO00O0OOO0OO0O0 :#line:279
                                if OOOO00O0OOO0OO0O0 ['status']==200 :#line:280
                                    if OOOO00O0OOO0OO0O0 ['data']:#line:281
                                        print (f'【赠送种子】:赠送{O00O0O0000000OOO0}种子给{O0000OOO0O0O00OO0.doneeNo}成功')#line:282
                    else :#line:283
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:284
        except Exception as O0OOOOO00OOOOO0O0 :#line:285
            print (O0OOOOO00OOOOO0O0 )#line:286
    def invitation (O0OOOO000OO0OOO0O ):#line:288
        try :#line:289
            _O000000O0OO0000O0 =float (bundled_def ())/4 #line:290
            OOOOOOOOO0O0O0000 =f'_innerId={int(_O000000O0OO0000O0)}_{timi_new()}'#line:291
            O0OO0OOOOO00OOOOO ={'authorization':O0OOOO000OO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOOO0O0O0000 ),'signstring':OOOOOOOOO0O0O0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:300
            OO0OOO0O000O0OO00 ={"innerId":int (_O000000O0OO0000O0 )}#line:301
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0OO0OOOOO00OOOOO ,data =OO0OOO0O000O0OO00 )#line:302
        except Exception as OOO000OO0O0OOO0O0 :#line:303
            print (OOO000OO0O0OOO0O0 )#line:304
    def winning_rewards (OO000000O0000O0O0 ):#line:307
        try :#line:308
            O00O0OOO0O000O0OO =f'__{timi_new()}'#line:309
            O0OO0000O0O00OOO0 ={'authorization':OO000000O0000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO0O000O0OO ),'signstring':O00O0OOO0O000O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:318
            OOOOOOO0O00OO0000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OO0000O0O00OOO0 ).json ()#line:319
            if 'status'in OOOOOOO0O00OO0000 :#line:321
                if OOOOOOO0O00OO0000 ['status']==200 :#line:322
                    if OOOOOOO0O00OO0000 ['data']['amount']:#line:323
                        OO000O0000O0O0000 =OOOOOOO0O00OO0000 ['data']['amount']['gold']#line:324
                        return OO000O0000O0O0000 #line:325
                    else :#line:326
                        return 0 #line:327
        except Exception as OOOOO0O00O0O00000 :#line:328
            print (OOOOO0O00O0O00000 )#line:329
    def certification (OOO0O00OO0O00O0O0 ):#line:332
        try :#line:333
            O00OOO00OO00000O0 =f'__{timi_new()}'#line:334
            OO0O00O00O000O000 ={'authorization':OOO0O00OO0O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO00OO00000O0 ),'signstring':O00OOO00OO00000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:343
            O0O00O000000OOOO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0O00O00O000O000 ).json ()#line:344
            if 'status'in O0O00O000000OOOO0 :#line:346
                if O0O00O000000OOOO0 ['status']==200 :#line:347
                    if O0O00O000000OOOO0 ['data']['result']:#line:348
                        O0O000OOO0OOO0O00 =O0O00O000000OOOO0 ['data']['nick_name']#line:349
                        return O0O000OOO0OOO0O00 #line:350
                    else :#line:351
                        return '未实名'#line:352
        except Exception as O000OO00OO0OO00O0 :#line:353
            print (O000OO00OO0OO00O0 )#line:354
    def crops_illustrated (O0OOOO0000OOOOOO0 ):#line:357
        try :#line:358
            OO0O0O0O0O0OO0OOO =f'__{timi_new()}'#line:359
            OO00O0O00000OOO0O ={'authorization':O0OOOO0000OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0O0O0OO0OOO ),'signstring':OO0O0O0O0O0OO0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:368
            O0O0OOOO0O00OO0OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO00O0O00000OOO0O ).json ()#line:369
            if 'status'in O0O0OOOO0O00OO0OO :#line:371
                if O0O0OOOO0O00OO0OO ['status']==200 :#line:372
                    O00OO00O00O0O000O =O0O0OOOO0O00OO0OO ['data'][0 ]['crops']#line:373
                    for OOO00OO0000O00OO0 in O00OO00O00O0O000O :#line:374
                        if OOO00OO0000O00OO0 ['ill_clover_award']:#line:375
                            if float (OOO00OO0000O00OO0 ['ill_clover_award'])>1 :#line:376
                                if OOO00OO0000O00OO0 ['is_finish']:#line:377
                                    if not OOO00OO0000O00OO0 ['is_getit']:#line:378
                                        if O0OOOO0000OOOOOO0 .certification ()!='未实名':#line:379
                                            OO0O0O0O0O0OO0OOO =f'_award_level={OOO00OO0000O00OO0["level"]}_{timi_new()}'#line:380
                                            OO00O0O00000OOO0O ={'authorization':O0OOOO0000OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0O0O0OO0OOO ),'signstring':OO0O0O0O0O0OO0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:389
                                            O0O0OO0OOO0000OOO ={"award_level":OOO00OO0000O00OO0 ['level']}#line:390
                                            O0O0O0000000O0OO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO00O0O00000OOO0O ,json =O0O0OO0OOO0000OOO ).json ()#line:392
                                            if 'status'in O0O0O0000000O0OO0 :#line:393
                                                if O0O0O0000000O0OO0 ['status']==200 :#line:394
                                                    OOO0O0OOO00OOOO00 =O0O0O0000000O0OO0 ['data']['ill_clover_award']#line:395
                                                    print (f'【图鉴奖励】:领取{OOO00OO0000O00OO0["crop_name"]}成就丨奖励{OOO0O0OOO00OOOO00}叶子成功')#line:397
                                                if O0O0O0000000O0OO0 ['status']==500 :#line:398
                                                    print (f'【图鉴奖励】:{O0O0O0000000O0OO0["message"]}')#line:399
        except Exception as OO0OO0000OO00O00O :#line:400
            print (OO0OO0000OO00O00O )#line:401
    def watched_ad (O0OO000OOO0000OO0 ):#line:404
        try :#line:405
            O000O0OO00O00OO0O =f'__{timi_new()}'#line:406
            O0O0O0O00OOOO0O0O ={'authorization':O0OO000OOO0000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO00O00OO0O ),'signstring':O000O0OO00O00OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:415
            OOOO0O000O0OOOOOO =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0O00OOOO0O0O ).json ()#line:416
            if 'status'in OOOO0O000O0OOOOOO :#line:418
                if OOOO0O000O0OOOOOO ['status']==200 :#line:419
                    if 'offlineInfo'in OOOO0O000O0OOOOOO ['data']:#line:420
                        O0O0000O0OOO0O000 =OOOO0O000O0OOOOOO ['data']['offlineInfo']['off_minute']#line:421
                        OOO0OOOO0000O000O =float (OOOO0O000O0OOOOOO ['data']['silver'])/1000000000000 #line:422
                        time .sleep (1 )#line:423
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O0O0O00OOOO0O0O ).json ()#line:424
                        time .sleep (2 )#line:425
                        OO0O00O0OO0O0OO00 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0O00OOOO0O0O ).json ()#line:426
                        if 'status'in OO0O00O0OO0O0OO00 :#line:428
                            if OO0O00O0OO0O0OO00 ['status']==200 :#line:429
                                OOO0OO0OO000OO000 =float (OO0O00O0OO0O0OO00 ['data']['silver'])/1000000000000 #line:430
                                OOOO0O0O0OO0O00O0 =str (OOO0OO0OO000OO000 -OOO0OOOO0000O000O )[:6 ]#line:431
                                print (f'【离线奖励】:翻倍离线{O0O0000O0OOO0O000}分钟奖励种子数量:{OOOO0O0O0OO0O00O0}t粒')#line:432
        except Exception as O0OO0000O0O0OO0OO :#line:433
            print (O0OO0000O0O0OO0OO )#line:434
    def user_ad (O0OOOO0OOO0OO00OO ):#line:437
        try :#line:438
            O00OO0O0O0O00O00O =f'__{timi_new()}'#line:439
            O0OO00O0000O0OO0O ={'authorization':O0OOOO0OOO0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0O0O00O00O ),'signstring':O00OO0O0O0O00O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:448
            OO00OO0000O0OOO00 =requests .request ('get',f'{host}/user/ad',headers =O0OO00O0000O0OO0O ).json ()#line:449
            if 'status'in OO00OO0000O0OOO00 :#line:451
                if OO00OO0000O0OOO00 ['status']==200 :#line:452
                    OOO0O0OO0O00OOOO0 =OO00OO0000O0OOO00 ['data']['max_time']#line:453
                    O0O0000OO00O0OOOO =OO00OO0000O0OOO00 ['data']['watch_time']#line:454
                    OOOO0OOO0O0OO0O00 =OO00OO0000O0OOO00 ['data']['added_time']#line:455
                    print (f'【获取种子】:获取种子剩余{OOOO0OOO0O0OO0O00 + OOO0O0OO0O00OOOO0 - O0O0000OO00O0OOOO}次丨好友提供:{OOOO0OOO0O0OO0O00}次')#line:456
                    if OOOO0OOO0O0OO0O00 +OOO0O0OO0O00OOOO0 -O0O0000OO00O0OOOO >0 :#line:457
                        time .sleep (random .randint (16 ,19 ))#line:458
                        OO00O0OOO0O0O00OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OO00O0000O0OO0O ).json ()#line:459
                        if 'status'in OO00O0OOO0O0O00OO :#line:461
                            if OO00O0OOO0O0O00OO ['status']==200 :#line:462
                                O00000OOO00O0OOOO =OO00O0OOO0O0O00OO ['data']['silver']#line:463
                                print (f'【获取种子】:获得种子:{O00000OOO00O0OOOO}')#line:464
                                return True #line:465
                            if OO00O0OOO0O0O00OO ['status']==500 :#line:466
                                O0OOOO0OOO000000O =OO00O0OOO0O0O00OO ['message']#line:467
                                print (f'【获取种子】:{O0OOOO0OOO000000O}')#line:468
                                return False #line:469
        except Exception as OOOO0OOOOOO0000O0 :#line:470
            print (OOOO0OOOOOO0000O0 )#line:471
    def synthetic (OO000OOO000O00OOO ):#line:474
        global id ,g #line:475
        try :#line:476
            OOOOOO0O0OO00O0OO =OO000OOO000O00OOO .level_new ()#line:477
            while True :#line:478
                O0OOO00O0000O00O0 =f'__{timi_new()}'#line:479
                OO00O0OO0000O0OO0 ={'authorization':OO000OOO000O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0000O00O0 ),'signstring':O0OOO00O0000O00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                O0OO00OOO0O0OOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0OO0000O0OO0 ).json ()#line:489
                if 'status'in O0OO00OOO0O0OOOO0 :#line:491
                    if O0OO00OOO0O0OOOO0 ['status']==200 :#line:492
                        OOOO0OOO0O0O000OO =O0OO00OOO0O0OOOO0 ['data']['cropList']#line:493
                        OOOOO000OO00OO00O =O0OO00OOO0O0OOOO0 ['data']['gameCoreDataDBid']#line:494
                        O0O000O00OOO0O0OO =0 #line:495
                        for O0OO0O0OO0O0O00O0 in OOOO0OOO0O0O000OO :#line:496
                            if not O0OO0O0OO0O0O00O0 :#line:497
                                OOOOOO0OOOO00O00O =f'_crop_id={OOOOO000OO00OO00O}&site={O0O000O00OOO0O0OO}_{OO000OOO000O00OOO.time}'#line:498
                                O000O000OO00O00O0 ={'authorization':OO000OOO000O00OOO .token ,'timestamp':OO000OOO000O00OOO .time ,'sign':sign (OOOOOO0OOOO00O00O ),'signstring':OOOOOO0OOOO00O00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:507
                                O000000O00OO00OOO ={"site":O0O000O00OOO0O0OO ,"crop_id":OOOOO000OO00OO00O }#line:508
                                O00O0OOO0O0OOOO00 =requests .request ('post',f'{host}/game/crops/buy',headers =O000O000OO00O00O0 ,data =O000000O00OO00OOO ).json ()#line:509
                                time .sleep (random .randint (1 ,3 )/10 )#line:511
                                if 'status'in O00O0OOO0O0OOOO00 :#line:512
                                    if O00O0OOO0O0OOOO00 ['status']==200 :#line:513
                                        if O00O0OOO0O0OOOO00 ['message']=='种子数量不足':#line:514
                                            OOOOOO0O0OO00O0OO =OO000OOO000O00OOO .level_new ()#line:515
                                            print (f'【种植合成】:{O00O0OOO0O0OOOO00["message"]}')#line:516
                                            if not OO000OOO000O00OOO .user_ad ():#line:517
                                                return False #line:518
                                    if O00O0OOO0O0OOOO00 ['status']==500 :#line:519
                                        print (f'【种植合成】:{O00O0OOO0O0OOOO00["message"]}')#line:520
                                        return False #line:521
                            O0O000O00OOO0O0OO +=1 #line:522
                        O0000OOO000OOO0OO =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0OO0000O0OO0 ).json ()#line:523
                        OO0OO0O00O000O0O0 =O0000OOO000OOO0OO ['data']['cropList']#line:524
                        OOO0OO0O0OOOOO00O =False #line:525
                        for O0OO0O0OO0O0O00O0 in range (12 ):#line:526
                            id =OO0OO0O00O000O0O0 [O0OO0O0OO0O0O00O0 ]['level']#line:527
                            if float (OOOOOO0O0OO00O0OO )-float (id )>9 :#line:528
                                O000O00O00O00OOOO =f'_site={O0OO0O0OO0O0O00O0}_{timi_new()}'#line:529
                                O0OO000O0OO0O0O0O ={'accept':'application/json, text/plain, */*','authorization':OO000OOO000O00OOO .token ,'timestamp':timi_new (),'sign':sign (O000O00O00O00OOOO ),'signstring':O000O00O00O00OOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:539
                                O00000OOO0000OOO0 ={"site":O0OO0O0OO0O0O00O0 }#line:540
                                OOOO00O0O0OOO00OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OO000O0OO0O0O0O ,data =O00000OOO0000OOO0 ).json ()#line:542
                                if 'status'in OOOO00O0O0OOO00OO :#line:543
                                    if OOOO00O0O0OOO00OO ['status']==200 :#line:544
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:545
                            if id !=0 :#line:546
                                for OO0OOO00O0O00O00O in range (11 ):#line:547
                                    O00OOO000000O00O0 =OO0OOO00O0O00O00O +1 #line:548
                                    g =OO0OO0O00O000O0O0 [O00OOO000000O00O0 ]['level']#line:549
                                    if id ==g :#line:550
                                        OOO000OOO0O000OOO =OO0OOO00O0O00O00O +2 #line:551
                                        if OOO000OOO0O000OOO !=O0OO0O0OO0O0O00O0 +1 :#line:552
                                            OOOOO0OOO00000O0O =O0OO0O0OO0O0O00O0 +1 #line:553
                                            time .sleep (random .randint (1 ,3 )/10 )#line:555
                                            OOOOOOO0O000O0OOO =f'_site={OOOOO0OOO00000O0O - 1}&targetSite={OOO000OOO0O000OOO - 1}_{timi_new()}'#line:556
                                            OO00O000OOO0000OO ={'accept':'application/json, text/plain, */*','authorization':OO000OOO000O00OOO .token ,'timestamp':timi_new (),'sign':sign (OOOOOOO0O000O0OOO ),'signstring':OOOOOOO0O000O0OOO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:571
                                            O0OO0OOO00O000O0O ={"site":int (OOOOO0OOO00000O0O -1 ),"targetSite":int (OOO000OOO0O000OOO -1 )}#line:572
                                            OOOO0O0OO000O0O00 =requests .request ('post',f'{host}/game/crops/move',headers =OO00O000OOO0000OO ,json =O0OO0OOO00O000O0O ).json ()#line:574
                                            if 'status'in OOOO0O0OO000O0O00 :#line:575
                                                if OOOO0O0OO000O0O00 ['status']==200 :#line:576
                                                    pass #line:577
                                            print ('【种植合成】:',OOOOO0OOO00000O0O ,OOO000OOO0O000OOO ,'合成成功')#line:579
                                            OOO0OO0O0OOOOO00O =True #line:580
                                    if OOO0OO0O0OOOOO00O :#line:581
                                        break #line:582
                                if OOO0OO0O0OOOOO00O :#line:583
                                    break #line:584
        except Exception as O00OOOO000OOO0O00 :#line:585
            OO000OOO000O00OOO .synthetic ()#line:586
    def level_new (OOOO00OOOO000OO0O ):#line:589
        try :#line:590
            OOO00O0O00O0O00OO =f'__{timi_new()}'#line:591
            OO00O00OO000OOO00 ={'authorization':OOOO00OOOO000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0O00O0O00OO ),'signstring':OOO00O0O00O0O00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            OOO00000OOOOOOOOO =requests .request ('get',f'{host}/user',headers =OO00O00OO000OOO00 ).json ()#line:601
            if 'status'in OOO00000OOOOOOOOO :#line:602
                if OOO00000OOOOOOOOO ['status']==200 :#line:603
                    return float (OOO00000OOOOOOOOO ['data']['level'])#line:604
        except Exception as O0OO0OOO0O0O0O0OO :#line:605
            print (O0OO0OOO0O0O0O0OO )#line:606
    def propsraffle (OOO0OOOO0OO0O0000 ):#line:609
        try :#line:610
            while True :#line:611
                O0O0O0OO00OO0OO00 =f'__{timi_new()}'#line:612
                O00O0000O0OO0O000 ={'authorization':OOO0OOOO0OO0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO00OO0OO00 ),'signstring':O0O0O0OO00OO0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:621
                O0O000OOO00O0O0OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00O0000O0OO0O000 ).json ()#line:622
                if 'status'in O0O000OOO00O0O0OO :#line:624
                    if O0O000OOO00O0O0OO ['status']==200 :#line:625
                        O000O000OO0000O00 =O0O000OOO00O0O0OO ['data']['rows']#line:626
                        O0O00OOO000OO00O0 =O0O000OOO00O0O0OO ['data']['vstate']#line:627
                        if O000O000OO0000O00 ==5 or O000O000OO0000O00 ==6 or O000O000OO0000O00 ==7 :#line:628
                            OO00O000O00O0OOO0 =O0O000OOO00O0O0OO ['data']['silver']#line:629
                            print (f'【转盘抽奖】:获得种子:{OO00O000O00O0OOO0}')#line:630
                        if O000O000OO0000O00 ==1 or O000O000OO0000O00 ==2 or O000O000OO0000O00 ==3 :#line:631
                            O0O0OO00OO0OO00OO =O0O000OOO00O0O0OO ['data']['clover']#line:632
                            print (f'【转盘抽奖】:获得三叶草:{O0O0OO00OO0OO00OO}')#line:633
                        if O000O000OO0000O00 ==4 or O000O000OO0000O00 ==8 :#line:634
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:635
                        if O000O000OO0000O00 =='抽奖次数已用完':#line:639
                            break #line:672
                time .sleep (random .randint (8 ,15 )/10 )#line:673
        except Exception as OOOO0O0OO00000O00 :#line:674
            print (OOOO0O0OO00000O00 )#line:675
    def friends_invitation (O0OOO0O000000OOO0 ):#line:678
        try :#line:679
            OOO0O0O0OO0OO0OOO =f'__{timi_new()}'#line:680
            O00OO00000O00O0O0 ={'authorization':O0OOO0O000000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OO0OO0OOO ),'signstring':OOO0O0O0OO0OO0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:689
            OO0O0OO0O0OO00OOO =requests .request ('get',f'{host}/friends',headers =O00OO00000O00O0O0 ).json ()#line:690
            if 'status'in OO0O0OO0O0OO00OOO :#line:691
                if OO0O0OO0O0OO00OOO ['status']==200 :#line:692
                    OOOO00OOO00OOOO0O =OO0O0OO0O0OO00OOO ['data']['myInviteter']#line:693
                    if OOOO00OOO00OOOO0O :#line:694
                        O0OOOO000OO0O00O0 =OOOO00OOO00OOOO0O ['user']['nickname']#line:695
                        O0O00OO0OOOOO00OO =O0OOO0O000000OOO0 .certification ()#line:696
                        print (f'【查邀请人】:我的邀请人:{O0OOOO000OO0O00O0}丨实名:{O0O00OO0OOOOO00OO}')#line:697
                    else :#line:698
                        if O0OOO0O000000OOO0 .innerId !='0':#line:699
                            O0OOO0O000000OOO0 .invitation ()#line:700
        except Exception as OO000OOOO00OO0O0O :#line:701
            print (OO000OOOO00OO0O0O )#line:702
    def add_clover (OO00O00OOO0O000O0 ):#line:705
        global golden_seed #line:706
        try :#line:707
            O0O000OOOOO0O000O =f'__{timi_new()}'#line:708
            O00OO0O0OOOO0OO00 ={'authorization':OO00O00OOO0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOOOO0O000O ),'signstring':O0O000OOOOO0O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:717
            O00000O0000OOO0O0 =requests .request ('get',f'{host}/assets/clovers',headers =O00OO0O0OOOO0OO00 ).json ()#line:718
            if 'status'in O00000O0000OOO0O0 :#line:720
                if O00000O0000OOO0O0 ['status']==200 :#line:721
                    OO0O0OO0O00O00O0O =O00000O0000OOO0O0 ['data']['clover']#line:722
                    O0O0OO0O0OOOO00OO =O00000O0000OOO0O0 ['data']['used_clover']#line:723
                    O0000000OOO00O00O =float (OO0O0OO0O00O00O0O )-float (O0O0OO0O0OOOO00OO )#line:724
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0O0OO0O0OOOO00OO}')#line:725
                    if OO00O00OOO0O000O0 .certification ()!='未实名':#line:726
                        if O0000000OOO00O00O >1 :#line:727
                            O0O000OOOOO0O000O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0000000OOO00O00O)}_{timi_new()}'#line:728
                            O00OO0O0OOOO0OO00 ={'authorization':OO00O00OOO0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOOOO0O000O ),'signstring':O0O000OOOOO0O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                            O0O00OOO0000OOOOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0000000OOO00O00O )}#line:738
                            OO00O00OOOOOOOO00 =requests .request ('post',f'{host}/lottery/add-stake',headers =O00OO0O0OOOO0OO00 ,data =O0O00OOO0000OOOOO ).json ()#line:739
                            if 'status'in OO00O00OOOOOOOO00 :#line:741
                                if OO00O00OOOOOOOO00 ['status']==200 :#line:742
                                    print (f'【参与抽奖】:添加三叶草:{OO00O00OOOOOOOO00["data"]}丨数量:{O0000000OOO00O00O}')#line:743
                                if OO00O00OOOOOOOO00 ['status']==500 :#line:744
                                    print (f'【参与抽奖】:添加三叶草:{OO00O00OOOOOOOO00["message"]}')#line:745
            O0O00OO0OO0OO00O0 =requests .request ('get',f'{host}/lottery',headers =O00OO0O0OOOO0OO00 ).json ()#line:746
            OO0000OO000OO0O00 =OO00O00OOO0O000O0 .winning_rewards ()#line:748
            if 'status'in O0O00OO0OO0OO00O0 :#line:749
                if O0O00OO0OO0OO00O0 ['status']==200 :#line:750
                    O00O0O00OO00O00O0 =O0O00OO0OO0OO00O0 ['data'][0 ]['day_get_gold_quantity']#line:751
                    golden_seed +=float (O00O0O00OO00O00O0 )#line:752
                    print (f'【参与抽奖】:预计每天中{str(O00O0O00OO00O00O0)[:6]}颗金种子丨好友收益:{str(OO0000OO000OO0O00)[:6]}')#line:753
        except Exception as O0O000OOO0OO000O0 :#line:754
            print (O0O000OOO0OO000O0 )#line:755
    def energy (O0OOOO0OO000OO0OO ):#line:758
        O000O000OOO0000O0 =f'__{timi_new()}'#line:759
        OOOOO0O00OOOOOOO0 ={'authorization':O0OOOO0OO000OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000OOO0000O0 ),'signstring':O000O000OOO0000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:768
        O00OOOO0OO0000O00 =requests .request ('get',f'{host}/energy/general',headers =OOOOO0O00OOOOOOO0 ).json ()#line:769
        if 'status'in O00OOOO0OO0000O00 :#line:771
            if O00OOOO0OO0000O00 ['status']==200 :#line:772
                O0O00O000OO0OOO00 =O00OOOO0OO0000O00 ['data']['ordinary_water']#line:773
                O0O0O0O0O00O00O00 =O00OOOO0OO0000O00 ['data']['ordinary_fertilizer']#line:774
                print (f'【我的营养】:肥料:{str(O0O0O0O0O00O00O00).split(".")[0]}丨水滴:{str(O0O00O000OO0OOO00).split(".")[0]}')#line:776
                if float (O0O0O0O0O00O00O00 )<96 :#line:777
                    time .sleep (random .randint (160 ,180 )/10 )#line:778
                    O00000000OO0000OO =99 -float (O0O0O0O0O00O00O00 )#line:779
                    OO00OO0OOO0000O0O ={"fertilizer":str (O00000000OO0000OO ).split ('.')[0 ]}#line:780
                    O0O00OO000OOOO0O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOOO0O00OOOOOOO0 ).json ()#line:781
                    if 'status'in O0O00OO000OOOO0O0 :#line:783
                        if O0O00OO000OOOO0O0 ['status']==200 :#line:784
                            print (f'【购买肥料】:看广告获取肥料:{O0O00OO000OOOO0O0["message"]}')#line:785
                if float (O0O00O000OO0OOO00 )<880 :#line:786
                    time .sleep (random .randint (160 ,180 )/10 )#line:787
                    O00O000OO0O0OOOO0 =999 -float (O0O00O000OO0OOO00 )#line:788
                    OOOOO0OO00O00O0O0 ={"water":str (O00O000OO0O0OOOO0 ).split ('.')[0 ]}#line:789
                    O0000OOOOOOO0O0OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOOO0O00OOOOOOO0 ).json ()#line:790
                    if 'status'in O0000OOOOOOO0O0OO :#line:792
                        if O0000OOOOOOO0O0OO ['status']==200 :#line:793
                            print (f'【购买水滴】:看广告获取水滴:{O0000OOOOOOO0O0OO["message"]}')#line:794
def bundled_def ():#line:797
    O0OO000O0O0O0OO00 =['5570536','7750212','7911652','7911680','7805624']#line:798
    return O0OO000O0O0O0OO00 [random .randint (0 ,len (O0OO000O0O0O0OO00 )-1 )]#line:799
def version_of_the_validation ():#line:803
    return str ((73 -56 )/10 )#line:804
def gitee_validation ():#line:807
    try :#line:808
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:809
    except :#line:810
        sys .exit (0 )#line:811
def update_the_validation ():#line:815
    try :#line:816
        O00OOO00OO0OOOO0O =gitee_validation ()#line:817
        if version_of_the_validation ()<O00OOO00OO0OOOO0O ['CityEarth']['edition']:#line:818
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OOO00OO0OOOO0O["CityEarth"]["edition"]}   ❌')#line:819
            print (f'更新内容=>>{O00OOO00OO0OOOO0O["CityEarth"]["content"]}   👍')#line:820
        else :#line:821
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OOO00OO0OOOO0O["CityEarth"]["edition"]}   ✅')#line:822
            print (f'更新内容=>> {O00OOO00OO0OOOO0O["CityEarth"]["content"]}   👍')#line:823
    except Exception as OOOO0O0O000O0OO0O :#line:824
        print (OOOO0O0O000O0OO0O )#line:825
def os_qinglong ():#line:828
    if application in os .environ :#line:829
        OO000OOOO000O0OO0 =os .environ [application ].split ('\n')#line:830
        if len (OO000OOOO000O0OO0 )>0 :#line:831
            return OO000OOOO000O0OO0 #line:832
        else :#line:833
            print (f"{application}变量未启用")#line:834
            print ('脚本退出')#line:835
            sys .exit (1 )#line:836
    else :#line:837
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:839
        return os_built ()#line:840
def os_built ():#line:843
    if token :#line:844
        OOO0OOOO0O0O00OOO =token .split ('\n')#line:845
        if len (OOO0OOOO0O0O00OOO )>0 :#line:846
            return OOO0OOOO0O0O00OOO #line:847
    else :#line:848
        print (f"内置变量为空")#line:849
        print ('脚本结束')#line:850
        sys .exit (0 )#line:851
if __name__ =='__main__':#line:854
    start ()#line:855
