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
change_nickname = False  # True 为修改昵称      False 为不修改
application = 'ce_token'  # 变量名
token = ''
time_xx = random.randint(8, 12)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
version ='3.1.4195311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        O00OOO00O00OOOO00 =os_qinglong ()#line:10
        print (f"==========共找到{len(O00OOO00O00OOOO00)}个账号==========")#line:11
        for OO0O0OOOO00OOOOO0 in O00OOO00O00OOOO00 :#line:12
            print (f"------------正在执行第{O00OOO00O00OOOO00.index(OO0O0OOOO00OOOOO0) + 1}个账号------------")#line:13
            O0O00OO0OO0O0000O =CityEarth (OO0O0OOOO00OOOOO0 )#line:14
            def OO000O00O0000O0OO ():#line:16
                if O0O00OO0OO0O0000O .base_info ():#line:18
                    O0O00OO0OO0O0000O .sealing ()#line:20
                    O0O00OO0OO0O0000O .invitenum ()#line:22
                    O0O00OO0OO0O0000O .game_map ()#line:24
                    O0O00OO0OO0O0000O .friends_invitation ()#line:26
                    O0O00OO0OO0O0000O .add_clover ()#line:28
                    O0O00OO0OO0O0000O .energy ()#line:30
                    O0O00OO0OO0O0000O .propsraffle ()#line:32
                    O0O00OO0OO0O0000O .synthetic ()#line:34
                    O0O00OO0OO0O0000O .crops_illustrated ()#line:36
                    O0O00OO0OO0O0000O .give_gold ()#line:38
                    O0O00OO0OO0O0000O .withdraw ()#line:40
                else :#line:41
                    print ('token失效')#line:42
            OOOO0OOO0000OO0OO =threading .Thread (target =OO000O00O0000O0OO )#line:44
            OOOO0OOO0000OO0OO .start ()#line:45
            time .sleep (time_xx )#line:46
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:48
        time .sleep (3 )#line:49
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:50
    except Exception as OOO0O0OOOO0O0OO0O :#line:51
        print (OOO0O0OOOO0O0OO0O )#line:52
def sign (OOO00O00000000O00 ):#line:55
    OOO0OO00O000000O0 =hashlib .md5 (OOO00O00000000O00 .encode ()).hexdigest ()#line:56
    OO0O0OOOO0OO0O00O ="scsc%^&*"+OOO0OO00O000000O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:57
    O00OOOOOO0O0O00OO =hashlib .md5 (OO0O0OOOO0OO0O00O .encode ()).hexdigest ()#line:58
    return O00OOOOOO0O0O00OO #line:59
def timi_new ():#line:62
    return str (int (time .time ()*1000 ))#line:63
class CityEarth :#line:66
    def __init__ (O00OOOOO0OOO0O00O ,OOOOO0OO0O00OO0OO ):#line:68
        try :#line:69
            O00OOOOO0OOO0O00O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:70
            O00OOOOO0OOO0O00O .token =OOOOO0OO0O00OO0OO .split ('&')[0 ]#line:71
            O00OOOOO0OOO0O00O .innerId =OOOOO0OO0O00OO0OO .split ('&')[1 ]#line:72
            O00OOOOO0OOO0O00O .doneeNo =OOOOO0OO0O00OO0OO .split ('&')[2 ]#line:73
        except :#line:74
            print ('变量格式错误')#line:75
    def base_info (OO000OO00O00O0O00 ):#line:78
        try :#line:79
            OO000OO00O00O0O00 .watched_ad ()#line:81
            OO000000O0OO0O00O =f'__{timi_new()}'#line:82
            OOO0OO000OO0O00OO ={'authorization':OO000OO00O00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000O0OO0O00O ),'signstring':OO000000O0OO0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:91
            OO0O000OO00OOOOOO =requests .request ('get',f'{host}/user',headers =OOO0OO000OO0O00OO ).json ()#line:92
            if 'status'in OO0O000OO00OOOOOO :#line:94
                if OO0O000OO00OOOOOO ['status']==200 :#line:95
                    O0O0000OOO00000OO =OO0O000OO00OOOOOO ['data']['nickname']#line:96
                    O00000000000OOOOO =OO0O000OO00OOOOOO ['data']['inner_id']#line:97
                    OO00000000O000OOO =OO0O000OO00OOOOOO ['data']['assets']['gold']#line:98
                    O0O0000000000O000 =OO0O000OO00OOOOOO ['data']['level']#line:99
                    print (f'【账号信息】:昵称:{O0O0000OOO00000OO[:5]}丨ID:{O00000000000OOOOO}丨等级:{O0O0000000000O000}丨种子:{str(OO00000000O000OOO).split(".")[0]}')#line:101
                    if change_nickname :#line:102
                        OO000OO00O00O0O00 .change_nickname (O00000000000OOOOO )#line:104
                if OO0O000OO00OOOOOO ['status']==401 :#line:105
                    return False #line:106
                if OO0O000OO00OOOOOO ['status']==500 :#line:107
                    return False #line:108
            return True #line:109
        except Exception as OOO0OO0OO0000O0OO :#line:110
            print (OOO0OO0OO0000O0OO )#line:111
    def sealing (OOOOOOOO00000OO00 ):#line:114
        try :#line:115
            OO00O000OO00OO000 =f'__{timi_new()}'#line:116
            OO0OOOO0OOO00000O ={'authorization':OOOOOOOO00000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000OO00OO000 ),'signstring':OO00O000OO00OO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:125
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0OOOO0OOO00000O )#line:126
            requests .request ('get',f'{host}/packsack/list',headers =OO0OOOO0OOO00000O )#line:127
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0OOOO0OOO00000O )#line:128
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0OOOO0OOO00000O )#line:129
            requests .request ('get',f'{host}/user',headers =OO0OOOO0OOO00000O )#line:130
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0OOOO0OOO00000O )#line:131
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0OOOO0OOO00000O )#line:132
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0OOOO0OOO00000O )#line:133
            requests .request ('get',f'{host}/game/getAllData',headers =OO0OOOO0OOO00000O )#line:134
            requests .request ('get',f'{host}/assets',headers =OO0OOOO0OOO00000O )#line:135
        except Exception as O00000O00O0OOO00O :#line:136
            print (O00000O00O0OOO00O )#line:137
    def change_nickname (O00O0OOO000O0OO0O ,OOOOO00O00O00O0OO ):#line:140
        try :#line:141
            OO00OOOO0O0O0O000 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:142
            OOOOOO00OOO000OOO =requests .request ('post','https://www.qmsjmfb.com/',data =OO00OOOO0O0O0O000 ).text #line:143
            O00OOOO0OO0OOO0OO =re .findall ('<ul><li>(.*?)</li>',OOOOOO00OOO000OOO )[0 ][:3 ]+str (OOOOO00O00O00O0OO )[5 :]#line:144
            O00OO0O0OOO000000 =f'_nickname=_{timi_new()}'#line:145
            O0O00OO0000OOO0O0 ={'authorization':O00O0OOO000O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0OOO000000 ),'signstring':O00OO0O0OOO000000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:154
            O0O00OO0O0O0OOO0O ={"nickname":O00OOOO0OO0OOO0OO }#line:155
            OOO00O00OO0O0OOOO =requests .patch (f'{host}/user/nickname',headers =O0O00OO0000OOO0O0 ,json =O0O00OO0O0O0OOO0O ).json ()#line:156
            print (OOO00O00OO0O0OOOO )#line:157
        except Exception as O00O00OOOOO0O0OOO :#line:159
            print (O00O00OOOOO0O0OOO )#line:160
    def withdraw (O0OO0000OOO0OO0O0 ):#line:163
        OOOO000000OOOOO0O =f'__{timi_new()}'#line:164
        OO000OO000OOO0000 ={'authorization':O0OO0000OOO0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000000OOOOO0O ),'signstring':OOOO000000OOOOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:173
        O000OO00OO0O0OO0O =requests .request ('get',f'{host}/assets',headers =OO000OO000OOO0000 ).json ()#line:174
        if 'status'in O000OO00OO0O0OO0O :#line:176
            if O000OO00OO0O0OO0O ['status']==200 :#line:177
                O0OOO0OOOO0OOOOOO =O000OO00OO0O0OO0O ['data']['cash']#line:178
                if float (O0OOO0OOOO0OOOOOO )>20 :#line:179
                    OOOO000000OOOOO0O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:180
                    OO000OO000OOO0000 ={'authorization':O0OO0000OOO0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000000OOOOO0O ),'signstring':OOOO000000OOOOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:189
                    O000OO0O0OO000OO0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:190
                    O000OO0O00OOO0000 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO000OO000OOO0000 ,data =O000OO0O0OO000OO0 ).json ()#line:192
                    print (O000OO0O00OOO0000 )#line:193
    def invitenum (OO0O00O0OOO00O0O0 ):#line:196
        O00O0O0O0O0OOO0O0 =f'__{timi_new()}'#line:197
        OOO0OO0000O0000O0 ={'authorization':OO0O00O0OOO00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O0O0OOO0O0 ),'signstring':O00O0O0O0O0OOO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:206
        OOOOOOOO0O00O0000 =requests .request ('get',f'{host}/invite/invitenum',headers =OOO0OO0000O0000O0 ).json ()#line:207
        if 'status'in OOOOOOOO0O00O0000 :#line:209
            if OOOOOOOO0O00O0000 ['status']==200 :#line:210
                O0O0O0O0OO00O00O0 =OOOOOOOO0O00O0000 ['data']['invited_count']#line:211
                OO0O0O0OOO0OO0O0O =OOOOOOOO0O00O0000 ['data']['invited_second_count']#line:212
                print (f'【我的邀请】:直邀好友:{O0O0O0O0OO00O00O0}丨间邀好友:{OO0O0O0OOO0OO0O0O}')#line:213
    def game_map (OO0OOO0O0OO000O00 ):#line:216
        try :#line:217
            OOO00OO0000O0OOO0 =f'__{timi_new()}'#line:218
            O0O0O00OO000OO00O ={'authorization':OO0OOO0O0OO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0000O0OOO0 ),'signstring':OOO00OO0000O0OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:227
            OOO0OO0000OOOOOO0 =requests .request ('get',f'{host}/game/map',headers =O0O0O00OO000OO00O ).json ()#line:228
            if 'status'in OOO0OO0000OOOOOO0 :#line:230
                if OOO0OO0000OOOOOO0 ['status']==200 :#line:231
                    for OO00OO00OO0O0000O in OOO0OO0000OOOOOO0 ['data']['list'][0 ]['crops']:#line:232
                        OOO00O00O0OO000O0 =OO00OO00OO0O0000O ['level']#line:234
                        if OOO00O00O0OO000O0 ==41 :#line:235
                            O00O00OO00OOO000O =OO00OO00OO0O0000O ['crop_name']#line:236
                            OOO0OOO0O000OO000 =OO00OO00OO0O0000O ['count']#line:237
                            if OOO0OOO0O000OO000 >0 :#line:238
                                print (f'【农业资产】:{O00O00OO00OOO000O}丨数量:{OOO0OOO0O000OO000}')#line:239
        except Exception as OO0O0O0OO0000O000 :#line:240
            print (OO0O0O0OO0000O000 )#line:241
    def give_gold (OOOO0000O0OOO00O0 ):#line:244
        try :#line:245
            O0OOO00O00000O00O =f'__{timi_new()}'#line:246
            OOOOO00O00O00O00O ={'authorization':OOOO0000O0OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O00000O00O ),'signstring':O0OOO00O00000O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:255
            O00OO0OOO0O00O00O =requests .request ('get',f'{host}/user',headers =OOOOO00O00O00O00O ).json ()#line:256
            if 'status'in O00OO0OOO0O00O00O :#line:257
                if O00OO0OOO0O00O00O ['status']==200 :#line:258
                    if float (OOOO0000O0OOO00O0 .doneeNo )!=0 :#line:259
                        OO0OO00OOO0000O0O =O00OO0OOO0O00O00O ['data']['assets']['gold']#line:260
                        if float (OO0OO00OOO0000O0O )>float (OOOO0000O0OOO00O0 .innerId ):#line:261
                            OOO0000OOO0O00O0O =int (float (OO0OO00OOO0000O0O )/1.1 )#line:262
                            O0OOO00O00000O00O =f'_doneeNo={OOOO0000O0OOO00O0.doneeNo}&quantity={OOO0000OOO0O00O0O}_{timi_new()}'#line:263
                            OOOOO00O00O00O00O ={'authorization':OOOO0000O0OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O00000O00O ),'signstring':O0OOO00O00000O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
                            O0OOO0OOO0OOO00OO ={"quantity":OOO0000OOO0O00O0O ,"doneeNo":OOOO0000O0OOO00O0 .doneeNo }#line:276
                            OO0OOOOO000OO0O00 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOO00O00O00O00O ,data =O0OOO0OOO0OOO00OO ).json ()#line:277
                            if 'status'in OO0OOOOO000OO0O00 :#line:279
                                if OO0OOOOO000OO0O00 ['status']==200 :#line:280
                                    if OO0OOOOO000OO0O00 ['data']:#line:281
                                        print (f'【赠送种子】:赠送{OOO0000OOO0O00O0O}种子给{OOOO0000O0OOO00O0.doneeNo}成功')#line:282
                    else :#line:283
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:284
        except Exception as O00OO0O00O000000O :#line:285
            print (O00OO0O00O000000O )#line:286
    def invitation (O0000O000000OO00O ):#line:288
        try :#line:289
            _OO00O0O000O0O0O00 =float (bundled_def ())/4 #line:290
            O000O0OO0O0OO0OOO =f'_innerId={int(_OO00O0O000O0O0O00)}_{timi_new()}'#line:291
            OO0OOO0O000OO00O0 ={'authorization':O0000O000000OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO0O0OO0OOO ),'signstring':O000O0OO0O0OO0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:300
            OOOO0OOOO0OO000OO ={"innerId":int (_OO00O0O000O0O0O00 )}#line:301
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO0OOO0O000OO00O0 ,data =OOOO0OOOO0OO000OO )#line:302
        except Exception as O0O0O0OO000OO000O :#line:303
            print (O0O0O0OO000OO000O )#line:304
    def winning_rewards (OO0OO00OO0O0OO00O ):#line:307
        try :#line:308
            OOOOOOO000O00OO00 =f'__{timi_new()}'#line:309
            O0OOO00OOOO0000OO ={'authorization':OO0OO00OO0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO000O00OO00 ),'signstring':OOOOOOO000O00OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:318
            OOOO0OOOO0000000O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOO00OOOO0000OO ).json ()#line:319
            if 'status'in OOOO0OOOO0000000O :#line:321
                if OOOO0OOOO0000000O ['status']==200 :#line:322
                    if OOOO0OOOO0000000O ['data']['amount']:#line:323
                        O000O0OOO000OOO0O =OOOO0OOOO0000000O ['data']['amount']['gold']#line:324
                        return O000O0OOO000OOO0O #line:325
                    else :#line:326
                        return 0 #line:327
        except Exception as O0O000OOO00OOOOOO :#line:328
            print (O0O000OOO00OOOOOO )#line:329
    def certification (O000000OO0OO0OO00 ):#line:332
        try :#line:333
            O0OO0O0O00OOO00OO =f'__{timi_new()}'#line:334
            OO0OOO0OOO0OOO0OO ={'authorization':O000000OO0OO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O00OOO00OO ),'signstring':O0OO0O0O00OOO00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:343
            OOO0OOOO000000O00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0OOO0OOO0OOO0OO ).json ()#line:344
            if 'status'in OOO0OOOO000000O00 :#line:346
                if OOO0OOOO000000O00 ['status']==200 :#line:347
                    if OOO0OOOO000000O00 ['data']['result']:#line:348
                        OOO0O00OOOO000O00 =OOO0OOOO000000O00 ['data']['nick_name']#line:349
                        return OOO0O00OOOO000O00 #line:350
                    else :#line:351
                        return '未实名'#line:352
        except Exception as OOO0OOO00OO0O0OO0 :#line:353
            print (OOO0OOO00OO0O0OO0 )#line:354
    def crops_illustrated (OOOOO000O0000O0O0 ):#line:357
        try :#line:358
            OOO000O00000OOOOO =f'__{timi_new()}'#line:359
            O000OOOOOO0OOOOOO ={'authorization':OOOOO000O0000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O00000OOOOO ),'signstring':OOO000O00000OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:368
            O0O0O000OOO000000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O000OOOOOO0OOOOOO ).json ()#line:369
            if 'status'in O0O0O000OOO000000 :#line:371
                if O0O0O000OOO000000 ['status']==200 :#line:372
                    OO0O0OOO0OO00OOO0 =O0O0O000OOO000000 ['data'][0 ]['crops']#line:373
                    for O000O00OOO0O000O0 in OO0O0OOO0OO00OOO0 :#line:374
                        if O000O00OOO0O000O0 ['ill_clover_award']:#line:375
                            if float (O000O00OOO0O000O0 ['ill_clover_award'])>1 :#line:376
                                if O000O00OOO0O000O0 ['is_finish']:#line:377
                                    if not O000O00OOO0O000O0 ['is_getit']:#line:378
                                        if OOOOO000O0000O0O0 .certification ()!='未实名':#line:379
                                            OOO000O00000OOOOO =f'_award_level={O000O00OOO0O000O0["level"]}_{timi_new()}'#line:380
                                            O000OOOOOO0OOOOOO ={'authorization':OOOOO000O0000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O00000OOOOO ),'signstring':OOO000O00000OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:389
                                            OOO00000000000O00 ={"award_level":O000O00OOO0O000O0 ['level']}#line:390
                                            O0OO000O0O00OOOO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O000OOOOOO0OOOOOO ,json =OOO00000000000O00 ).json ()#line:392
                                            if 'status'in O0OO000O0O00OOOO0 :#line:393
                                                if O0OO000O0O00OOOO0 ['status']==200 :#line:394
                                                    O0000O0OOOOO0OO00 =O0OO000O0O00OOOO0 ['data']['ill_clover_award']#line:395
                                                    print (f'【图鉴奖励】:领取{O000O00OOO0O000O0["crop_name"]}成就丨奖励{O0000O0OOOOO0OO00}叶子成功')#line:397
                                                if O0OO000O0O00OOOO0 ['status']==500 :#line:398
                                                    print (f'【图鉴奖励】:{O0OO000O0O00OOOO0["message"]}')#line:399
        except Exception as O00OOOOOO0O0OO0O0 :#line:400
            print (O00OOOOOO0O0OO0O0 )#line:401
    def watched_ad (OOO00O00O0000OO0O ):#line:404
        try :#line:405
            O0O0OOOO00OOO0OO0 =f'__{timi_new()}'#line:406
            O00O0OO000O0OOOOO ={'authorization':OOO00O00O0000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOO00OOO0OO0 ),'signstring':O0O0OOOO00OOO0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:415
            OOOOOO00O0O0OOO00 =requests .request ('get',f'{host}/game/getAllData',headers =O00O0OO000O0OOOOO ).json ()#line:416
            if 'status'in OOOOOO00O0O0OOO00 :#line:418
                if OOOOOO00O0O0OOO00 ['status']==200 :#line:419
                    if 'offlineInfo'in OOOOOO00O0O0OOO00 ['data']:#line:420
                        O000000000OO0O000 =OOOOOO00O0O0OOO00 ['data']['offlineInfo']['off_minute']#line:421
                        O000OOOOO0OO0O0OO =float (OOOOOO00O0O0OOO00 ['data']['silver'])/1000000000000 #line:422
                        time .sleep (1 )#line:423
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00O0OO000O0OOOOO ).json ()#line:424
                        time .sleep (2 )#line:425
                        O0OOO0O0OOO0O00O0 =requests .request ('get',f'{host}/game/getAllData',headers =O00O0OO000O0OOOOO ).json ()#line:426
                        if 'status'in O0OOO0O0OOO0O00O0 :#line:428
                            if O0OOO0O0OOO0O00O0 ['status']==200 :#line:429
                                OOOOO000OOO0O0OOO =float (O0OOO0O0OOO0O00O0 ['data']['silver'])/1000000000000 #line:430
                                O0O0O0OO00O00OO00 =str (OOOOO000OOO0O0OOO -O000OOOOO0OO0O0OO )[:6 ]#line:431
                                print (f'【离线奖励】:翻倍离线{O000000000OO0O000}分钟奖励种子数量:{O0O0O0OO00O00OO00}t粒')#line:432
        except Exception as OOOO0OOO0O0OO000O :#line:433
            print (OOOO0OOO0O0OO000O )#line:434
    def user_ad (OO00OOO0OOOO0000O ):#line:437
        try :#line:438
            O00OO00O0OO00OOOO =f'__{timi_new()}'#line:439
            O0O0000OO00OOOO0O ={'authorization':OO00OOO0OOOO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00O0OO00OOOO ),'signstring':O00OO00O0OO00OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:448
            OO0OOO00OO0OO0OOO =requests .request ('get',f'{host}/user/ad',headers =O0O0000OO00OOOO0O ).json ()#line:449
            if 'status'in OO0OOO00OO0OO0OOO :#line:451
                if OO0OOO00OO0OO0OOO ['status']==200 :#line:452
                    OOOOO000OO0O0O00O =OO0OOO00OO0OO0OOO ['data']['max_time']#line:453
                    O00OOOO00O0O000O0 =OO0OOO00OO0OO0OOO ['data']['watch_time']#line:454
                    OO00OOO0O000OO0O0 =OO0OOO00OO0OO0OOO ['data']['added_time']#line:455
                    print (f'【获取种子】:获取种子剩余{OO00OOO0O000OO0O0 + OOOOO000OO0O0O00O - O00OOOO00O0O000O0}次丨好友提供:{OO00OOO0O000OO0O0}次')#line:456
                    if OO00OOO0O000OO0O0 +OOOOO000OO0O0O00O -O00OOOO00O0O000O0 >0 :#line:457
                        time .sleep (random .randint (16 ,19 ))#line:458
                        O0OOOOO0O000O0OOO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O0000OO00OOOO0O ).json ()#line:459
                        if 'status'in O0OOOOO0O000O0OOO :#line:461
                            if O0OOOOO0O000O0OOO ['status']==200 :#line:462
                                OO0OOOO0OO0O0OOOO =O0OOOOO0O000O0OOO ['data']['silver']#line:463
                                print (f'【获取种子】:获得种子:{OO0OOOO0OO0O0OOOO}')#line:464
                                return True #line:465
                            if O0OOOOO0O000O0OOO ['status']==500 :#line:466
                                O0000OOOO000OOO0O =O0OOOOO0O000O0OOO ['message']#line:467
                                print (f'【获取种子】:{O0000OOOO000OOO0O}')#line:468
                                return False #line:469
        except Exception as O0000OO0O000O000O :#line:470
            print (O0000OO0O000O000O )#line:471
    def synthetic (O000OO000OO000OO0 ):#line:474
        global id ,g #line:475
        try :#line:476
            OO0O0O0000O00O000 =O000OO000OO000OO0 .level_new ()#line:477
            while True :#line:478
                O00O000O00OOOO0O0 =f'__{timi_new()}'#line:479
                O0O00OO000O0O0000 ={'authorization':O000OO000OO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000O00OOOO0O0 ),'signstring':O00O000O00OOOO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                O000O0OOO0OOO00OO =requests .request ('get',f'{host}/game/getAllData',headers =O0O00OO000O0O0000 ).json ()#line:489
                if 'status'in O000O0OOO0OOO00OO :#line:491
                    if O000O0OOO0OOO00OO ['status']==200 :#line:492
                        OOOO0O00OO0OOO00O =O000O0OOO0OOO00OO ['data']['cropList']#line:493
                        O0OOO0O0OO0OOO0OO =O000O0OOO0OOO00OO ['data']['gameCoreDataDBid']#line:494
                        OO0OO00OO0O0000O0 =0 #line:495
                        for OO0O0O000OOO0OO0O in OOOO0O00OO0OOO00O :#line:496
                            if not OO0O0O000OOO0OO0O :#line:497
                                O000OO000OO000000 =f'_crop_id={O0OOO0O0OO0OOO0OO}&site={OO0OO00OO0O0000O0}_{O000OO000OO000OO0.time}'#line:498
                                OO00O00O000O00OO0 ={'authorization':O000OO000OO000OO0 .token ,'timestamp':O000OO000OO000OO0 .time ,'sign':sign (O000OO000OO000000 ),'signstring':O000OO000OO000000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:507
                                O0O0OOOO0O0O0OOOO ={"site":OO0OO00OO0O0000O0 ,"crop_id":O0OOO0O0OO0OOO0OO }#line:508
                                OO0OO0O0O000000OO =requests .request ('post',f'{host}/game/crops/buy',headers =OO00O00O000O00OO0 ,data =O0O0OOOO0O0O0OOOO ).json ()#line:509
                                time .sleep (random .randint (1 ,3 )/10 )#line:511
                                if 'status'in OO0OO0O0O000000OO :#line:512
                                    if OO0OO0O0O000000OO ['status']==200 :#line:513
                                        if OO0OO0O0O000000OO ['message']=='种子数量不足':#line:514
                                            OO0O0O0000O00O000 =O000OO000OO000OO0 .level_new ()#line:515
                                            print (f'【种植合成】:{OO0OO0O0O000000OO["message"]}')#line:516
                                            if not O000OO000OO000OO0 .user_ad ():#line:517
                                                return False #line:518
                                    if OO0OO0O0O000000OO ['status']==500 :#line:519
                                        print (f'【种植合成】:{OO0OO0O0O000000OO["message"]}')#line:520
                                        return False #line:521
                            OO0OO00OO0O0000O0 +=1 #line:522
                        OO0O0O0OO0O000O0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O00OO000O0O0000 ).json ()#line:523
                        O00OOOOOOO00OOOO0 =OO0O0O0OO0O000O0O ['data']['cropList']#line:524
                        O0000O0OO000O00O0 =False #line:525
                        for OO0O0O000OOO0OO0O in range (12 ):#line:526
                            id =O00OOOOOOO00OOOO0 [OO0O0O000OOO0OO0O ]['level']#line:527
                            if float (OO0O0O0000O00O000 )-float (id )>9 :#line:528
                                OOOO0O0OO0000O00O =f'_site={OO0O0O000OOO0OO0O}_{timi_new()}'#line:529
                                O0OOOO0O0O0O0OOOO ={'accept':'application/json, text/plain, */*','authorization':O000OO000OO000OO0 .token ,'timestamp':timi_new (),'sign':sign (OOOO0O0OO0000O00O ),'signstring':OOOO0O0OO0000O00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:539
                                O00O0OO0O00OOO0O0 ={"site":OO0O0O000OOO0OO0O }#line:540
                                O0OOO00000OOOOO0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OOOO0O0O0O0OOOO ,data =O00O0OO0O00OOO0O0 ).json ()#line:542
                                if 'status'in O0OOO00000OOOOO0O :#line:543
                                    if O0OOO00000OOOOO0O ['status']==200 :#line:544
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:545
                            if id !=0 :#line:546
                                for OOOO0OO0O00OO0000 in range (11 ):#line:547
                                    O00OO0O00O00O00OO =OOOO0OO0O00OO0000 +1 #line:548
                                    g =O00OOOOOOO00OOOO0 [O00OO0O00O00O00OO ]['level']#line:549
                                    if id ==g :#line:550
                                        OO0000O0OO0000000 =OOOO0OO0O00OO0000 +2 #line:551
                                        if OO0000O0OO0000000 !=OO0O0O000OOO0OO0O +1 :#line:552
                                            OO00OO0OO0OO000O0 =OO0O0O000OOO0OO0O +1 #line:553
                                            time .sleep (random .randint (1 ,3 )/10 )#line:555
                                            OOOOOO000O0OO0O00 =f'_site={OO00OO0OO0OO000O0 - 1}&targetSite={OO0000O0OO0000000 - 1}_{timi_new()}'#line:556
                                            O00O0OOOOO00OO0OO ={'accept':'application/json, text/plain, */*','authorization':O000OO000OO000OO0 .token ,'timestamp':timi_new (),'sign':sign (OOOOOO000O0OO0O00 ),'signstring':OOOOOO000O0OO0O00 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:571
                                            O0O0O000000O00OO0 ={"site":int (OO00OO0OO0OO000O0 -1 ),"targetSite":int (OO0000O0OO0000000 -1 )}#line:572
                                            O0O0O00O0OOOO0000 =requests .request ('post',f'{host}/game/crops/move',headers =O00O0OOOOO00OO0OO ,json =O0O0O000000O00OO0 ).json ()#line:574
                                            if 'status'in O0O0O00O0OOOO0000 :#line:575
                                                if O0O0O00O0OOOO0000 ['status']==200 :#line:576
                                                    pass #line:577
                                            print ('【种植合成】:',OO00OO0OO0OO000O0 ,OO0000O0OO0000000 ,'合成成功')#line:579
                                            O0000O0OO000O00O0 =True #line:580
                                    if O0000O0OO000O00O0 :#line:581
                                        break #line:582
                                if O0000O0OO000O00O0 :#line:583
                                    break #line:584
        except Exception as O00000OO0OO0O0OOO :#line:585
            O000OO000OO000OO0 .synthetic ()#line:586
    def level_new (O00OO00O0O0O00O0O ):#line:589
        try :#line:590
            O0000OOOO0OO00O0O =f'__{timi_new()}'#line:591
            O0O000OO000OOO000 ={'authorization':O00OO00O0O0O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOO0OO00O0O ),'signstring':O0000OOOO0OO00O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            O00OOOO00O0O0O00O =requests .request ('get',f'{host}/user',headers =O0O000OO000OOO000 ).json ()#line:601
            if 'status'in O00OOOO00O0O0O00O :#line:602
                if O00OOOO00O0O0O00O ['status']==200 :#line:603
                    return float (O00OOOO00O0O0O00O ['data']['level'])#line:604
        except Exception as O0O00O000OO0O0OOO :#line:605
            print (O0O00O000OO0O0OOO )#line:606
    def propsraffle (O0OO0OOOOOOO000O0 ):#line:609
        try :#line:610
            while True :#line:611
                O0O0O0OOOOOOOO000 =f'__{timi_new()}'#line:612
                O00O0OO0OOO0OO00O ={'authorization':O0OO0OOOOOOO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOOOOOO000 ),'signstring':O0O0O0OOOOOOOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:621
                OO0O00OO00OO000O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00O0OO0OOO0OO00O ).json ()#line:622
                if 'status'in OO0O00OO00OO000O0 :#line:624
                    if OO0O00OO00OO000O0 ['status']==200 :#line:625
                        OO00O00O00OOO00OO =OO0O00OO00OO000O0 ['data']['rows']#line:626
                        OOO00OO0O0OOOO0O0 =OO0O00OO00OO000O0 ['data']['vstate']#line:627
                        if OO00O00O00OOO00OO ==5 or OO00O00O00OOO00OO ==6 or OO00O00O00OOO00OO ==7 :#line:628
                            O0OO0O00O0000OOO0 =OO0O00OO00OO000O0 ['data']['silver']#line:629
                            print (f'【转盘抽奖】:获得种子:{O0OO0O00O0000OOO0}')#line:630
                        if OO00O00O00OOO00OO ==1 or OO00O00O00OOO00OO ==2 or OO00O00O00OOO00OO ==3 :#line:631
                            O0OOO00O00O0O0O0O =OO0O00OO00OO000O0 ['data']['clover']#line:632
                            print (f'【转盘抽奖】:获得三叶草:{O0OOO00O00O0O0O0O}')#line:633
                        if OO00O00O00OOO00OO ==4 or OO00O00O00OOO00OO ==8 :#line:634
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:635
                        if OO00O00O00OOO00OO =='抽奖次数已用完':#line:639
                            break #line:672
                time .sleep (random .randint (8 ,15 )/10 )#line:673
        except Exception as O00O0O0O0O0OOOOOO :#line:674
            print (O00O0O0O0O0OOOOOO )#line:675
    def friends_invitation (OOOOO0OO00O00OO0O ):#line:678
        try :#line:679
            OO0OO000O0O0OOOO0 =f'__{timi_new()}'#line:680
            OO0OO0O0O000OOO00 ={'authorization':OOOOO0OO00O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000O0O0OOOO0 ),'signstring':OO0OO000O0O0OOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:689
            O000O000OOO0OO00O =requests .request ('get',f'{host}/friends',headers =OO0OO0O0O000OOO00 ).json ()#line:690
            if 'status'in O000O000OOO0OO00O :#line:691
                if O000O000OOO0OO00O ['status']==200 :#line:692
                    OOO000OOOO0000000 =O000O000OOO0OO00O ['data']['myInviteter']#line:693
                    if OOO000OOOO0000000 :#line:694
                        OO0OO0OOO000OOO0O =OOO000OOOO0000000 ['user']['nickname']#line:695
                        OOOOOOO0O000OOOOO =OOOOO0OO00O00OO0O .certification ()#line:696
                        print (f'【查邀请人】:我的邀请人:{OO0OO0OOO000OOO0O}丨实名:{OOOOOOO0O000OOOOO}')#line:697
                    else :#line:698
                        if OOOOO0OO00O00OO0O .innerId !='0':#line:699
                            OOOOO0OO00O00OO0O .invitation ()#line:700
        except Exception as OOO0OO00O0OO00000 :#line:701
            print (OOO0OO00O0OO00000 )#line:702
    def add_clover (O00OO0O0OOO00OO00 ):#line:705
        global golden_seed #line:706
        try :#line:707
            O0OO000O0O00000O0 =f'__{timi_new()}'#line:708
            O0O00OO0OO0O00O0O ={'authorization':O00OO0O0OOO00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O0O00000O0 ),'signstring':O0OO000O0O00000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:717
            O00O00O00000OOOOO =requests .request ('get',f'{host}/assets/clovers',headers =O0O00OO0OO0O00O0O ).json ()#line:718
            if 'status'in O00O00O00000OOOOO :#line:720
                if O00O00O00000OOOOO ['status']==200 :#line:721
                    O0O00O000OO0000O0 =O00O00O00000OOOOO ['data']['clover']#line:722
                    O0OOOO000OO0O0000 =O00O00O00000OOOOO ['data']['used_clover']#line:723
                    O000O0000OOO0O0OO =float (O0O00O000OO0000O0 )-float (O0OOOO000OO0O0000 )#line:724
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0OOOO000OO0O0000}')#line:725
                    if O00OO0O0OOO00OO00 .certification ()!='未实名':#line:726
                        if O000O0000OOO0O0OO >1 :#line:727
                            O0OO000O0O00000O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O000O0000OOO0O0OO)}_{timi_new()}'#line:728
                            O0O00OO0OO0O00O0O ={'authorization':O00OO0O0OOO00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O0O00000O0 ),'signstring':O0OO000O0O00000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                            O00000000OO0O0O00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O000O0000OOO0O0OO )}#line:738
                            OOOO0O00000O00O00 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O00OO0OO0O00O0O ,data =O00000000OO0O0O00 ).json ()#line:739
                            if 'status'in OOOO0O00000O00O00 :#line:741
                                if OOOO0O00000O00O00 ['status']==200 :#line:742
                                    print (f'【参与抽奖】:添加三叶草:{OOOO0O00000O00O00["data"]}丨数量:{O000O0000OOO0O0OO}')#line:743
                                if OOOO0O00000O00O00 ['status']==500 :#line:744
                                    print (f'【参与抽奖】:添加三叶草:{OOOO0O00000O00O00["message"]}')#line:745
            OOO0O0O0OO000O0OO =requests .request ('get',f'{host}/lottery',headers =O0O00OO0OO0O00O0O ).json ()#line:746
            OO00OO0O0OOOOO0O0 =O00OO0O0OOO00OO00 .winning_rewards ()#line:748
            if 'status'in OOO0O0O0OO000O0OO :#line:749
                if OOO0O0O0OO000O0OO ['status']==200 :#line:750
                    OOO0O0OOO00OOOOOO =OOO0O0O0OO000O0OO ['data'][0 ]['day_get_gold_quantity']#line:751
                    golden_seed +=float (OOO0O0OOO00OOOOOO )#line:752
                    print (f'【参与抽奖】:预计每天中{str(OOO0O0OOO00OOOOOO)[:6]}颗金种子丨好友收益:{str(OO00OO0O0OOOOO0O0)[:6]}')#line:753
        except Exception as OO000O0OOOOOOOOO0 :#line:754
            print (OO000O0OOOOOOOOO0 )#line:755
    def energy (O0O0O0OO0O00000OO ):#line:758
        try :#line:759
            while True :#line:760
                O0O0O0OO0OO0OO00O =f'__{timi_new()}'#line:761
                O0OO0OO0OOOOO0OOO ={'authorization':O0O0O0OO0O00000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO0OO0OO00O ),'signstring':O0O0O0OO0OO0OO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:770
                O00O000O0O00O0O0O =requests .request ('get',f'{host}/energy/general',headers =O0OO0OO0OOOOO0OOO ).json ()#line:771
                if 'status'in O00O000O0O00O0O0O :#line:773
                    if O00O000O0O00O0O0O ['status']==200 :#line:774
                        O000OOO0OO0OO0O0O =O00O000O0O00O0O0O ['data']['ordinary_water']#line:775
                        O0O0OOO0OO00OO00O =O00O000O0O00O0O0O ['data']['ordinary_fertilizer']#line:776
                        print (f'【我的营养】:肥料:{str(O0O0OOO0OO00OO00O).split(".")[0]}丨水滴:{str(O000OOO0OO0OO0O0O).split(".")[0]}')#line:778
                        if float (O0O0OOO0OO00OO00O )<96 :#line:779
                            time .sleep (random .randint (160 ,180 )/10 )#line:780
                            OO0OOOO00O00O00O0 =99 -float (O0O0OOO0OO00OO00O )#line:781
                            O00O0OO00OOO0OO00 ={"fertilizer":str (OO0OOOO00O00O00O0 ).split ('.')[0 ]}#line:782
                            OOO0OOOOO0O0O0O0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0OO0OO0OOOOO0OOO ).json ()#line:783
                            if 'status'in OOO0OOOOO0O0O0O0O :#line:785
                                if OOO0OOOOO0O0O0O0O ['status']==200 :#line:786
                                    print (f'【购买肥料】:看广告获取肥料:{OOO0OOOOO0O0O0O0O["message"]}')#line:787
                        if float (O000OOO0OO0OO0O0O )<880 :#line:788
                            time .sleep (random .randint (160 ,180 )/10 )#line:789
                            OOO0OO0000O0000OO =999 -float (O000OOO0OO0OO0O0O )#line:790
                            O0OOOOOOO0O0OO000 ={"water":str (OOO0OO0000O0000OO ).split ('.')[0 ]}#line:791
                            O0OOOOOOO00O0O0OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0OO0OO0OOOOO0OOO ).json ()#line:792
                            if 'status'in O0OOOOOOO00O0O0OO :#line:794
                                if O0OOOOOOO00O0O0OO ['status']==200 :#line:795
                                    print (f'【购买水滴】:看广告获取水滴:{O0OOOOOOO00O0O0OO["message"]}')#line:796
                        if float (O0O0OOO0OO00OO00O )>96 and float (O000OOO0OO0OO0O0O )>880 :#line:797
                            break #line:798
        except Exception as OO00O0O0O0OOO0O00 :#line:800
            print (OO00O0O0O0OOO0O00 )#line:801
def bundled_def ():#line:803
    OOO0O000O0OOO0OO0 =['5570536','7750212','7911652','7911680','7805624']#line:804
    return OOO0O000O0OOO0OO0 [random .randint (0 ,len (OOO0O000O0OOO0OO0 )-1 )]#line:805
def version_of_the_validation ():#line:809
    return str ((74 -56 )/10 )#line:810
def gitee_validation ():#line:813
    try :#line:814
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:815
    except :#line:816
        sys .exit (0 )#line:817
def update_the_validation ():#line:821
    try :#line:822
        OO00000000OO00000 =gitee_validation ()#line:823
        if version_of_the_validation ()<OO00000000OO00000 ['CityEarth']['edition']:#line:824
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00000000OO00000["CityEarth"]["edition"]}   ❌')#line:825
            print (f'更新内容=>>{OO00000000OO00000["CityEarth"]["content"]}   👍')#line:826
        else :#line:827
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00000000OO00000["CityEarth"]["edition"]}   ✅')#line:828
            print (f'更新内容=>> {OO00000000OO00000["CityEarth"]["content"]}   👍')#line:829
    except Exception as O0000000O00O0OO00 :#line:830
        print (O0000000O00O0OO00 )#line:831
def os_qinglong ():#line:834
    if application in os .environ :#line:835
        O0000O0OOOO000O00 =os .environ [application ].split ('\n')#line:836
        if len (O0000O0OOOO000O00 )>0 :#line:837
            return O0000O0OOOO000O00 #line:838
        else :#line:839
            print (f"{application}变量未启用")#line:840
            print ('脚本退出')#line:841
            sys .exit (1 )#line:842
    else :#line:843
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:845
        return os_built ()#line:846
def os_built ():#line:849
    if token :#line:850
        OO00OO00OO0000OOO =token .split ('\n')#line:851
        if len (OO00OO00OO0000OOO )>0 :#line:852
            return OO00OO00OO0000OOO #line:853
    else :#line:854
        print (f"内置变量为空")#line:855
        print ('脚本结束')#line:856
        sys .exit (0 )#line:857
if __name__ =='__main__':#line:860
    start ()#line:861
