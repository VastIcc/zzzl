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
@ 版本  1.9
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
        O0O0O0O0O00O000OO =os_qinglong ()#line:10
        print (f"==========共找到{len(O0O0O0O0O00O000OO)}个账号==========")#line:11
        for OOO000OOOOO0O0OO0 in O0O0O0O0O00O000OO :#line:12
            print (f"------------正在执行第{O0O0O0O0O00O000OO.index(OOO000OOOOO0O0OO0) + 1}个账号------------")#line:13
            O000O00OOOO0OOOO0 =CityEarth (OOO000OOOOO0O0OO0 )#line:14
            def O0O0O000000OOOO00 ():#line:16
                if O000O00OOOO0OOOO0 .base_info ():#line:18
                    O000O00OOOO0OOOO0 .sealing ()#line:20
                    O000O00OOOO0OOOO0 .invitenum ()#line:22
                    O000O00OOOO0OOOO0 .game_map ()#line:24
                    O000O00OOOO0OOOO0 .friends_invitation ()#line:26
                    O000O00OOOO0OOOO0 .add_clover ()#line:28
                    O000O00OOOO0OOOO0 .energy ()#line:30
                    O000O00OOOO0OOOO0 .propsraffle ()#line:32
                    O000O00OOOO0OOOO0 .synthetic ()#line:34
                    O000O00OOOO0OOOO0 .crops_illustrated ()#line:36
                    O000O00OOOO0OOOO0 .give_gold ()#line:38
                    O000O00OOOO0OOOO0 .withdraw ()#line:40
                else :#line:41
                    print ('token失效')#line:42
            OO0O00OO0000OOO00 =threading .Thread (target =O0O0O000000OOOO00 )#line:44
            OO0O00OO0000OOO00 .start ()#line:45
            time .sleep (time_xx )#line:46
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:48
        time .sleep (3 )#line:49
        print (f'【每天收益】：所有账号累计每天能中:{str(golden_seed)[:6]}颗金种子')#line:50
    except Exception as OO0OO0O0OO00O0O0O :#line:51
        print (OO0OO0O0OO00O0O0O )#line:52
def sign (O0OO0O0O0O00OO00O ):#line:55
    O0O000OOO0000000O =hashlib .md5 (O0OO0O0O0O00OO00O .encode ()).hexdigest ()#line:56
    O0000OOO0O00OO0O0 ="scsc%^&*"+O0O000OOO0000000O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:57
    O0OOO000O0000000O =hashlib .md5 (O0000OOO0O00OO0O0 .encode ()).hexdigest ()#line:58
    return O0OOO000O0000000O #line:59
def timi_new ():#line:62
    return str (int (time .time ()*1000 ))#line:63
class CityEarth :#line:66
    def __init__ (O0OOO0OOO0OOOO0OO ,O00OO00OOO00000O0 ):#line:68
        try :#line:69
            O0OOO0OOO0OOOO0OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:70
            O0OOO0OOO0OOOO0OO .token =O00OO00OOO00000O0 .split ('&')[0 ]#line:71
            O0OOO0OOO0OOOO0OO .innerId =O00OO00OOO00000O0 .split ('&')[1 ]#line:72
            O0OOO0OOO0OOOO0OO .doneeNo =O00OO00OOO00000O0 .split ('&')[2 ]#line:73
        except :#line:74
            print ('变量格式错误')#line:75
    def base_info (OO0OOO0OOOO00OOOO ):#line:78
        try :#line:79
            OO0OOO0OOOO00OOOO .watched_ad ()#line:81
            OOO0OO0O0OO000OO0 =f'__{timi_new()}'#line:82
            O00O00O00O0OOOOO0 ={'authorization':OO0OOO0OOOO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O0OO000OO0 ),'signstring':OOO0OO0O0OO000OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:91
            O0O00000OOO00O00O =requests .request ('get',f'{host}/user',headers =O00O00O00O0OOOOO0 ).json ()#line:92
            if 'status'in O0O00000OOO00O00O :#line:94
                if O0O00000OOO00O00O ['status']==200 :#line:95
                    O0OO0OOO00O00O000 =O0O00000OOO00O00O ['data']['nickname']#line:96
                    O00OOO000000000OO =O0O00000OOO00O00O ['data']['inner_id']#line:97
                    OO0OOO00000O0O0O0 =O0O00000OOO00O00O ['data']['assets']['gold']#line:98
                    OO0O000OOO0O0OOOO =O0O00000OOO00O00O ['data']['level']#line:99
                    print (f'【账号信息】:昵称:{O0OO0OOO00O00O000[:5]}丨ID:{O00OOO000000000OO}丨等级:{OO0O000OOO0O0OOOO}丨种子:{str(OO0OOO00000O0O0O0).split(".")[0]}')#line:101
                    if change_nickname :#line:102
                        OO0OOO0OOOO00OOOO .change_nickname (O00OOO000000000OO )#line:104
                if O0O00000OOO00O00O ['status']==401 :#line:105
                    return False #line:106
                if O0O00000OOO00O00O ['status']==500 :#line:107
                    return False #line:108
            return True #line:109
        except Exception as OOO0O0OOOOOO00O00 :#line:110
            print (OOO0O0OOOOOO00O00 )#line:111
    def sealing (OO0O00O00O000O000 ):#line:114
        try :#line:115
            OO0OO0OO000O0000O =f'__{timi_new()}'#line:116
            OOO000OOO0OOOOO0O ={'authorization':OO0O00O00O000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO000O0000O ),'signstring':OO0OO0OO000O0000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:125
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO000OOO0OOOOO0O )#line:126
            requests .request ('get',f'{host}/packsack/list',headers =OOO000OOO0OOOOO0O )#line:127
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO000OOO0OOOOO0O )#line:128
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO000OOO0OOOOO0O )#line:129
            requests .request ('get',f'{host}/user',headers =OOO000OOO0OOOOO0O )#line:130
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO000OOO0OOOOO0O )#line:131
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO000OOO0OOOOO0O )#line:132
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO000OOO0OOOOO0O )#line:133
            requests .request ('get',f'{host}/game/getAllData',headers =OOO000OOO0OOOOO0O )#line:134
            requests .request ('get',f'{host}/assets',headers =OOO000OOO0OOOOO0O )#line:135
        except Exception as O00000O00O00000O0 :#line:136
            print (O00000O00O00000O0 )#line:137
    def change_nickname (OOO0O0OOO0OOO0O00 ,OOO0O000OOOO0O00O ):#line:140
        try :#line:141
            OOOO0O0OOOO00O00O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:142
            O0O0000OO000OO0OO =requests .request ('post','https://www.qmsjmfb.com/',data =OOOO0O0OOOO00O00O ).text #line:143
            O0O0O0OO0OOO0O00O =re .findall ('<ul><li>(.*?)</li>',O0O0000OO000OO0OO )[0 ][:3 ]+str (OOO0O000OOOO0O00O )[5 :]#line:144
            OO000O0O000O00OO0 =f'_nickname=_{timi_new()}'#line:145
            O00OO000OO00O000O ={'authorization':OOO0O0OOO0OOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O000O00OO0 ),'signstring':OO000O0O000O00OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:154
            OOOOO0OOOO00O0O0O ={"nickname":O0O0O0OO0OOO0O00O }#line:155
            O0000O0000OOOO0OO =requests .patch (f'{host}/user/nickname',headers =O00OO000OO00O000O ,json =OOOOO0OOOO00O0O0O ).json ()#line:156
            print (O0000O0000OOOO0OO )#line:157
        except Exception as OOO00000O0OO0O00O :#line:159
            print (OOO00000O0OO0O00O )#line:160
    def withdraw (OOOO00000000OOOO0 ):#line:163
        O00OO0OOO0OOO00O0 =f'__{timi_new()}'#line:164
        O0O0OO00O0OOOOOOO ={'authorization':OOOO00000000OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OOO0OOO00O0 ),'signstring':O00OO0OOO0OOO00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:173
        OO0O00O00OOOO00OO =requests .request ('get',f'{host}/assets',headers =O0O0OO00O0OOOOOOO ).json ()#line:174
        if 'status'in OO0O00O00OOOO00OO :#line:176
            if OO0O00O00OOOO00OO ['status']==200 :#line:177
                O0O0O0OO00OO0O00O =OO0O00O00OOOO00OO ['data']['cash']#line:178
                if float (O0O0O0OO00OO0O00O )>20 :#line:179
                    O00OO0OOO0OOO00O0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:180
                    O0O0OO00O0OOOOOOO ={'authorization':OOOO00000000OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OOO0OOO00O0 ),'signstring':O00OO0OOO0OOO00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:189
                    OO0OOO00OOO00OOOO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:190
                    OOOOOOO00000O0O0O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O0OO00O0OOOOOOO ,data =OO0OOO00OOO00OOOO ).json ()#line:192
                    print (OOOOOOO00000O0O0O )#line:193
    def invitenum (O0OO000O0O00OOOOO ):#line:196
        O000OOO0000OOO00O =f'__{timi_new()}'#line:197
        O00OOOOO0O0O0O00O ={'authorization':O0OO000O0O00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0000OOO00O ),'signstring':O000OOO0000OOO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:206
        O00OOO000OO00OO0O =requests .request ('get',f'{host}/invite/invitenum',headers =O00OOOOO0O0O0O00O ).json ()#line:207
        if 'status'in O00OOO000OO00OO0O :#line:209
            if O00OOO000OO00OO0O ['status']==200 :#line:210
                O00OOO0O000O0O000 =O00OOO000OO00OO0O ['data']['invited_count']#line:211
                O00O0000O0000OO0O =O00OOO000OO00OO0O ['data']['invited_second_count']#line:212
                print (f'【我的邀请】:直邀好友:{O00OOO0O000O0O000}丨间邀好友:{O00O0000O0000OO0O}')#line:213
    def game_map (O00OOOOO0O0OOOOO0 ):#line:216
        try :#line:217
            OO00O0000O0OOOO0O =f'__{timi_new()}'#line:218
            OO0O0OO0OO000OO0O ={'authorization':O00OOOOO0O0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0000O0OOOO0O ),'signstring':OO00O0000O0OOOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:227
            OO0000000OO0OOO0O =requests .request ('get',f'{host}/game/map',headers =OO0O0OO0OO000OO0O ).json ()#line:228
            if 'status'in OO0000000OO0OOO0O :#line:230
                if OO0000000OO0OOO0O ['status']==200 :#line:231
                    for O00OO0O0000OO0O00 in OO0000000OO0OOO0O ['data']['list'][0 ]['crops']:#line:232
                        OO000O000OO00OO00 =O00OO0O0000OO0O00 ['level']#line:234
                        if OO000O000OO00OO00 ==41 :#line:235
                            O0O00O00OOOO000OO =O00OO0O0000OO0O00 ['crop_name']#line:236
                            OO0O0O0O00O0OOO0O =O00OO0O0000OO0O00 ['count']#line:237
                            if OO0O0O0O00O0OOO0O >0 :#line:238
                                print (f'【农业资产】:{O0O00O00OOOO000OO}丨数量:{OO0O0O0O00O0OOO0O}')#line:239
        except Exception as O0OO0OO00000O0O00 :#line:240
            print (O0OO0OO00000O0O00 )#line:241
    def give_gold (OOOO0OO0O0O0OO00O ):#line:244
        try :#line:245
            O0O0O000OO00OOO00 =f'__{timi_new()}'#line:246
            OO00O0OO00O00OOOO ={'authorization':OOOO0OO0O0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000OO00OOO00 ),'signstring':O0O0O000OO00OOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:255
            OOOOOOOO0O000OO00 =requests .request ('get',f'{host}/user',headers =OO00O0OO00O00OOOO ).json ()#line:256
            if 'status'in OOOOOOOO0O000OO00 :#line:257
                if OOOOOOOO0O000OO00 ['status']==200 :#line:258
                    if float (OOOO0OO0O0O0OO00O .doneeNo )!=0 :#line:259
                        OO0O00O0OO00OOOOO =OOOOOOOO0O000OO00 ['data']['assets']['gold']#line:260
                        if float (OO0O00O0OO00OOOOO )>float (OOOO0OO0O0O0OO00O .innerId ):#line:261
                            O0OO0O0000OOO0OO0 =int (float (OO0O00O0OO00OOOOO )/1.1 )#line:262
                            O0O0O000OO00OOO00 =f'_doneeNo={OOOO0OO0O0O0OO00O.doneeNo}&quantity={O0OO0O0000OOO0OO0}_{timi_new()}'#line:263
                            OO00O0OO00O00OOOO ={'authorization':OOOO0OO0O0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000OO00OOO00 ),'signstring':O0O0O000OO00OOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
                            O000OOO0000000OOO ={"quantity":O0OO0O0000OOO0OO0 ,"doneeNo":OOOO0OO0O0O0OO00O .doneeNo }#line:276
                            O0000000O0OOOO0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =OO00O0OO00O00OOOO ,data =O000OOO0000000OOO ).json ()#line:277
                            if 'status'in O0000000O0OOOO0O0 :#line:279
                                if O0000000O0OOOO0O0 ['status']==200 :#line:280
                                    if O0000000O0OOOO0O0 ['data']:#line:281
                                        print (f'【赠送种子】:赠送{O0OO0O0000OOO0OO0}种子给{OOOO0OO0O0O0OO00O.doneeNo}成功')#line:282
                    else :#line:283
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:284
        except Exception as O00OOO000000O0O00 :#line:285
            print (O00OOO000000O0O00 )#line:286
    def invitation (OOOOOOO0O0OOOO0OO ):#line:288
        try :#line:289
            _OOOOO0OOO00000O0O =float (bundled_def ())/4 #line:290
            OOOO00OOO0OO00OOO =f'_innerId={int(_OOOOO0OOO00000O0O)}_{timi_new()}'#line:291
            O000O00O0O00OOOO0 ={'authorization':OOOOOOO0O0OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOO0OO00OOO ),'signstring':OOOO00OOO0OO00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:300
            OOOO0O0OOO00OO0O0 ={"innerId":int (_OOOOO0OOO00000O0O )}#line:301
            requests .request ('post',f'{host}/friends/my-invitation',headers =O000O00O0O00OOOO0 ,data =OOOO0O0OOO00OO0O0 )#line:302
        except Exception as OOO00O0OO000O0OOO :#line:303
            print (OOO00O0OO000O0OOO )#line:304
    def winning_rewards (O00OO0OOO0OO000O0 ):#line:307
        try :#line:308
            OOO000O0O0OOOOO00 =f'__{timi_new()}'#line:309
            O0000O0O00OOO00OO ={'authorization':O00OO0OOO0OO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0O0OOOOO00 ),'signstring':OOO000O0O0OOOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:318
            O00O00O00OO0OO000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0000O0O00OOO00OO ).json ()#line:319
            if 'status'in O00O00O00OO0OO000 :#line:321
                if O00O00O00OO0OO000 ['status']==200 :#line:322
                    if O00O00O00OO0OO000 ['data']['amount']:#line:323
                        OOO0OOOO00OO00OOO =O00O00O00OO0OO000 ['data']['amount']['gold']#line:324
                        return OOO0OOOO00OO00OOO #line:325
                    else :#line:326
                        return 0 #line:327
        except Exception as OOOOO0OOO000O0000 :#line:328
            print (OOOOO0OOO000O0000 )#line:329
    def certification (OO0O0OOOO0OO0OO0O ):#line:332
        try :#line:333
            O0OOO0O0O0OOO0O0O =f'__{timi_new()}'#line:334
            OOO0O0OOOO000000O ={'authorization':OO0O0OOOO0OO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O0O0OOO0O0O ),'signstring':O0OOO0O0O0OOO0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:343
            O00OO0OO0OOOOOOOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO0O0OOOO000000O ).json ()#line:344
            if 'status'in O00OO0OO0OOOOOOOO :#line:346
                if O00OO0OO0OOOOOOOO ['status']==200 :#line:347
                    if O00OO0OO0OOOOOOOO ['data']['result']:#line:348
                        OOO00OOOOO0O0OOO0 =O00OO0OO0OOOOOOOO ['data']['nick_name']#line:349
                        return OOO00OOOOO0O0OOO0 #line:350
                    else :#line:351
                        return '未实名'#line:352
        except Exception as OOO00O0OO0OO0O000 :#line:353
            print (OOO00O0OO0OO0O000 )#line:354
    def crops_illustrated (OO000OO0OOO0OOO00 ):#line:357
        try :#line:358
            O00O00O0O00OO0000 =f'__{timi_new()}'#line:359
            O0OO0OO0O0O00O0OO ={'authorization':OO000OO0OOO0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O00OO0000 ),'signstring':O00O00O0O00OO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:368
            O0O0O0000O00O0000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OO0OO0O0O00O0OO ).json ()#line:369
            if 'status'in O0O0O0000O00O0000 :#line:371
                if O0O0O0000O00O0000 ['status']==200 :#line:372
                    OO00O0O0O0000O000 =O0O0O0000O00O0000 ['data'][0 ]['crops']#line:373
                    for OOO0000O00000000O in OO00O0O0O0000O000 :#line:374
                        if OOO0000O00000000O ['ill_clover_award']:#line:375
                            if float (OOO0000O00000000O ['ill_clover_award'])>1 :#line:376
                                if OOO0000O00000000O ['is_finish']:#line:377
                                    if not OOO0000O00000000O ['is_getit']:#line:378
                                        if OO000OO0OOO0OOO00 .certification ()!='未实名':#line:379
                                            O00O00O0O00OO0000 =f'_award_level={OOO0000O00000000O["level"]}_{timi_new()}'#line:380
                                            O0OO0OO0O0O00O0OO ={'authorization':OO000OO0OOO0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O00OO0000 ),'signstring':O00O00O0O00OO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:389
                                            O00O0O0OO00O0OOO0 ={"award_level":OOO0000O00000000O ['level']}#line:390
                                            O00O0OOO0OO0O0000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OO0OO0O0O00O0OO ,json =O00O0O0OO00O0OOO0 ).json ()#line:392
                                            if 'status'in O00O0OOO0OO0O0000 :#line:393
                                                if O00O0OOO0OO0O0000 ['status']==200 :#line:394
                                                    OOOO0O0OOOOOOO0O0 =O00O0OOO0OO0O0000 ['data']['ill_clover_award']#line:395
                                                    print (f'【图鉴奖励】:领取{OOO0000O00000000O["crop_name"]}成就丨奖励{OOOO0O0OOOOOOO0O0}叶子成功')#line:397
                                                if O00O0OOO0OO0O0000 ['status']==500 :#line:398
                                                    print (f'【图鉴奖励】:{O00O0OOO0OO0O0000["message"]}')#line:399
        except Exception as O00OOOO00OO00O0O0 :#line:400
            print (O00OOOO00OO00O0O0 )#line:401
    def watched_ad (OO000O0O00O00O000 ):#line:404
        try :#line:405
            O0OO00000OOO00OOO =f'__{timi_new()}'#line:406
            OO00000OO0OOOO0O0 ={'authorization':OO000O0O00O00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00000OOO00OOO ),'signstring':O0OO00000OOO00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:415
            OO000O000O00O0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =OO00000OO0OOOO0O0 ).json ()#line:416
            if 'status'in OO000O000O00O0OO0 :#line:418
                if OO000O000O00O0OO0 ['status']==200 :#line:419
                    if 'offlineInfo'in OO000O000O00O0OO0 ['data']:#line:420
                        O0O0000O000O0OO00 =OO000O000O00O0OO0 ['data']['offlineInfo']['off_minute']#line:421
                        OO0O00O0O0000OO0O =float (OO000O000O00O0OO0 ['data']['silver'])/1000000000000 #line:422
                        time .sleep (1 )#line:423
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO00000OO0OOOO0O0 ).json ()#line:424
                        time .sleep (2 )#line:425
                        OO0OO000O0OOOO00O =requests .request ('get',f'{host}/game/getAllData',headers =OO00000OO0OOOO0O0 ).json ()#line:426
                        if 'status'in OO0OO000O0OOOO00O :#line:428
                            if OO0OO000O0OOOO00O ['status']==200 :#line:429
                                OOO000000OO0OOO00 =float (OO0OO000O0OOOO00O ['data']['silver'])/1000000000000 #line:430
                                O0OOOO00000OOO00O =str (OOO000000OO0OOO00 -OO0O00O0O0000OO0O )[:6 ]#line:431
                                print (f'【离线奖励】:翻倍离线{O0O0000O000O0OO00}分钟奖励种子数量:{O0OOOO00000OOO00O}t粒')#line:432
        except Exception as O0OOOO0OOOOOO0O00 :#line:433
            print (O0OOOO0OOOOOO0O00 )#line:434
    def user_ad (O0O000OOOOO000OOO ):#line:437
        try :#line:438
            OO0OOOOO0O00O0OO0 =f'__{timi_new()}'#line:439
            O0O0O0O0OO000OO0O ={'authorization':O0O000OOOOO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO0O00O0OO0 ),'signstring':OO0OOOOO0O00O0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:448
            OO00O00OO0O0OO000 =requests .request ('get',f'{host}/user/ad',headers =O0O0O0O0OO000OO0O ).json ()#line:449
            if 'status'in OO00O00OO0O0OO000 :#line:451
                if OO00O00OO0O0OO000 ['status']==200 :#line:452
                    OO0OO0O00O0OO0O0O =OO00O00OO0O0OO000 ['data']['max_time']#line:453
                    O0OOOOO0O0OO00OOO =OO00O00OO0O0OO000 ['data']['watch_time']#line:454
                    OOO000O0O00OOOO0O =OO00O00OO0O0OO000 ['data']['added_time']#line:455
                    print (f'【获取种子】:获取种子剩余{OOO000O0O00OOOO0O + OO0OO0O00O0OO0O0O - O0OOOOO0O0OO00OOO}次丨好友提供:{OOO000O0O00OOOO0O}次')#line:456
                    if OOO000O0O00OOOO0O +OO0OO0O00O0OO0O0O -O0OOOOO0O0OO00OOO >0 :#line:457
                        time .sleep (random .randint (16 ,19 ))#line:458
                        O00OO0OO0OOOO00OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O0O0O0OO000OO0O ).json ()#line:459
                        if 'status'in O00OO0OO0OOOO00OO :#line:461
                            if O00OO0OO0OOOO00OO ['status']==200 :#line:462
                                O0OOO000OO0000000 =O00OO0OO0OOOO00OO ['data']['silver']#line:463
                                print (f'【获取种子】:获得种子:{O0OOO000OO0000000}')#line:464
                                return True #line:465
                            if O00OO0OO0OOOO00OO ['status']==500 :#line:466
                                OOOO00OOOO0O00O00 =O00OO0OO0OOOO00OO ['message']#line:467
                                print (f'【获取种子】:{OOOO00OOOO0O00O00}')#line:468
                                return False #line:469
        except Exception as O0000OOO000OOO000 :#line:470
            print (O0000OOO000OOO000 )#line:471
    def synthetic (O0O0OO0OO00000O0O ):#line:474
        global id ,g #line:475
        try :#line:476
            OO000O000OOOO0O0O =O0O0OO0OO00000O0O .level_new ()#line:477
            OOO000000O00O00O0 =random .randint (9 ,11 )#line:478
            OO0O000O0O0OO0O00 =f'_site=8&targetSite={OOO000000O00O00O0}_{timi_new()}'#line:479
            O0O0O00O0O000000O ={'accept':'application/json, text/plain, */*','authorization':O0O0OO0OO00000O0O .token ,'timestamp':timi_new (),'sign':sign (OO0O000O0O0OO0O00 ),'signstring':OO0O000O0O0OO0O00 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:494
            O000OOO00OOOO0O0O ={"site":int (8 ),"targetSite":int (OOO000000O00O00O0 )}#line:495
            requests .request ('post',f'{host}/game/crops/move',headers =O0O0O00O0O000000O ,json =O000OOO00OOOO0O0O )#line:496
            while True :#line:497
                OO00OOO0O0OOO00OO =f'__{timi_new()}'#line:498
                O000000000O0O00OO ={'authorization':O0O0OO0OO00000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO0O0OOO00OO ),'signstring':OO00OOO0O0OOO00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:507
                OO0OO0O00O0O0O0O0 =requests .request ('get',f'{host}/game/getAllData',headers =O000000000O0O00OO ).json ()#line:508
                if 'status'in OO0OO0O00O0O0O0O0 :#line:510
                    if OO0OO0O00O0O0O0O0 ['status']==200 :#line:511
                        O00000O00OO0O00OO =OO0OO0O00O0O0O0O0 ['data']['cropList']#line:512
                        OOO0OOOOO0OOOO00O =OO0OO0O00O0O0O0O0 ['data']['gameCoreDataDBid']#line:513
                        OOO0OOOOOOOOOOOOO =0 #line:514
                        for O0OO0OOO00OOO0000 in O00000O00OO0O00OO :#line:515
                            if not O0OO0OOO00OOO0000 :#line:516
                                OOO0O00O0OOO0000O =f'_crop_id={OOO0OOOOO0OOOO00O}&site={OOO0OOOOOOOOOOOOO}_{O0O0OO0OO00000O0O.time}'#line:517
                                O00O00O0OO0O000OO ={'authorization':O0O0OO0OO00000O0O .token ,'timestamp':O0O0OO0OO00000O0O .time ,'sign':sign (OOO0O00O0OOO0000O ),'signstring':OOO0O00O0OOO0000O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:526
                                OO000O0O00OO0O0O0 ={"site":OOO0OOOOOOOOOOOOO ,"crop_id":OOO0OOOOO0OOOO00O }#line:527
                                O0O0000OOO00O0OOO =requests .request ('post',f'{host}/game/crops/buy',headers =O00O00O0OO0O000OO ,data =OO000O0O00OO0O0O0 ).json ()#line:528
                                time .sleep (random .randint (1 ,3 )/10 )#line:530
                                if 'status'in O0O0000OOO00O0OOO :#line:531
                                    if O0O0000OOO00O0OOO ['status']==200 :#line:532
                                        if O0O0000OOO00O0OOO ['message']=='种子数量不足':#line:533
                                            OO000O000OOOO0O0O =O0O0OO0OO00000O0O .level_new ()#line:534
                                            print (f'【种植合成】:{O0O0000OOO00O0OOO["message"]}')#line:535
                                            if not O0O0OO0OO00000O0O .user_ad ():#line:536
                                                return False #line:537
                                    if O0O0000OOO00O0OOO ['status']==500 :#line:538
                                        print (f'【种植合成】:{O0O0000OOO00O0OOO["message"]}')#line:539
                                        return False #line:540
                            OOO0OOOOOOOOOOOOO +=1 #line:541
                        O0O0OO0O000O00O00 =requests .request ('get',f'{host}/game/getAllData',headers =O000000000O0O00OO ).json ()#line:542
                        OO00000O00OO00O00 =O0O0OO0O000O00O00 ['data']['cropList']#line:543
                        O000OOOO0OO0000OO =False #line:544
                        for O0OO0OOO00OOO0000 in range (12 ):#line:545
                            id =OO00000O00OO00O00 [O0OO0OOO00OOO0000 ]['level']#line:546
                            if float (OO000O000OOOO0O0O )-float (id )>9 :#line:547
                                O0OO0OO00O00000O0 =f'_site={O0OO0OOO00OOO0000}_{timi_new()}'#line:548
                                O00000O0OOOOO000O ={'accept':'application/json, text/plain, */*','authorization':O0O0OO0OO00000O0O .token ,'timestamp':timi_new (),'sign':sign (O0OO0OO00O00000O0 ),'signstring':O0OO0OO00O00000O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:558
                                OO0OOOO000OO0O000 ={"site":O0OO0OOO00OOO0000 }#line:559
                                O0OO0O000O00OO0OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00000O0OOOOO000O ,data =OO0OOOO000OO0O000 ).json ()#line:561
                                if 'status'in O0OO0O000O00OO0OO :#line:562
                                    if O0OO0O000O00OO0OO ['status']==200 :#line:563
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:564
                            if id !=0 :#line:565
                                for O000O0O0000OOO0OO in range (11 ):#line:566
                                    OO0O0OO0O0OOOO0OO =O000O0O0000OOO0OO +1 #line:567
                                    g =OO00000O00OO00O00 [OO0O0OO0O0OOOO0OO ]['level']#line:568
                                    if id ==g :#line:569
                                        O00OO0O0O00O0O00O =O000O0O0000OOO0OO +2 #line:570
                                        if O00OO0O0O00O0O00O !=O0OO0OOO00OOO0000 +1 :#line:571
                                            OO000000OOOOOO000 =O0OO0OOO00OOO0000 +1 #line:572
                                            time .sleep (random .randint (1 ,3 )/10 )#line:574
                                            OO0O000O0O0OO0O00 =f'_site={OO000000OOOOOO000 - 1}&targetSite={O00OO0O0O00O0O00O - 1}_{timi_new()}'#line:575
                                            O0O0O00O0O000000O ={'accept':'application/json, text/plain, */*','authorization':O0O0OO0OO00000O0O .token ,'timestamp':timi_new (),'sign':sign (OO0O000O0O0OO0O00 ),'signstring':OO0O000O0O0OO0O00 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:590
                                            OOO000OOOO0O0O00O ={"site":int (OO000000OOOOOO000 -1 ),"targetSite":int (O00OO0O0O00O0O00O -1 )}#line:591
                                            O00O0OO0OO0OOOOOO =requests .request ('post',f'{host}/game/crops/move',headers =O0O0O00O0O000000O ,json =OOO000OOOO0O0O00O ).json ()#line:593
                                            if 'status'in O00O0OO0OO0OOOOOO :#line:594
                                                if O00O0OO0OO0OOOOOO ['status']==200 :#line:595
                                                    pass #line:596
                                            print ('【种植合成】:',OO000000OOOOOO000 ,O00OO0O0O00O0O00O ,'合成成功')#line:598
                                            O000OOOO0OO0000OO =True #line:599
                                    if O000OOOO0OO0000OO :#line:600
                                        break #line:601
                                if O000OOOO0OO0000OO :#line:602
                                    break #line:603
        except Exception as O0OO0O00000O0O000 :#line:604
            O0O0OO0OO00000O0O .synthetic ()#line:605
    def level_new (OOO00OOO00OOO00OO ):#line:608
        try :#line:609
            OO0OOO0OO000OOOOO =f'__{timi_new()}'#line:610
            OO000O0OO0O0OO000 ={'authorization':OOO00OOO00OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0OO000OOOOO ),'signstring':OO0OOO0OO000OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:619
            OO0OOOO00OO0O0OO0 =requests .request ('get',f'{host}/user',headers =OO000O0OO0O0OO000 ).json ()#line:620
            if 'status'in OO0OOOO00OO0O0OO0 :#line:621
                if OO0OOOO00OO0O0OO0 ['status']==200 :#line:622
                    return float (OO0OOOO00OO0O0OO0 ['data']['level'])#line:623
        except Exception as O0OOOO00O0O000OO0 :#line:624
            print (O0OOOO00O0O000OO0 )#line:625
    def propsraffle (OOO0O00OOOOOO0000 ):#line:628
        try :#line:629
            while True :#line:630
                OO00000OO000OO000 =f'__{timi_new()}'#line:631
                O0O000O000O00OOOO ={'authorization':OOO0O00OOOOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OO000OO000 ),'signstring':OO00000OO000OO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:640
                O0O0OO00OOOOOOO0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O000O000O00OOOO ).json ()#line:641
                if 'status'in O0O0OO00OOOOOOO0O :#line:643
                    if O0O0OO00OOOOOOO0O ['status']==200 :#line:644
                        O00OOOO0OO0OOO0O0 =O0O0OO00OOOOOOO0O ['data']['rows']#line:645
                        OOO00000O000OOO00 =O0O0OO00OOOOOOO0O ['data']['vstate']#line:646
                        if O00OOOO0OO0OOO0O0 ==5 or O00OOOO0OO0OOO0O0 ==6 or O00OOOO0OO0OOO0O0 ==7 :#line:647
                            O00OOO0O00OO0OO00 =O0O0OO00OOOOOOO0O ['data']['silver']#line:648
                            print (f'【转盘抽奖】:获得种子:{O00OOO0O00OO0OO00}')#line:649
                        if O00OOOO0OO0OOO0O0 ==1 or O00OOOO0OO0OOO0O0 ==2 or O00OOOO0OO0OOO0O0 ==3 :#line:650
                            OOOO0OOO0O000O0OO =O0O0OO00OOOOOOO0O ['data']['clover']#line:651
                            print (f'【转盘抽奖】:获得三叶草:{OOOO0OOO0O000O0OO}')#line:652
                        if O00OOOO0OO0OOO0O0 ==4 or O00OOOO0OO0OOO0O0 ==8 :#line:653
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:654
                        if O00OOOO0OO0OOO0O0 =='抽奖次数已用完':#line:658
                            break #line:691
                time .sleep (random .randint (8 ,15 )/10 )#line:692
        except Exception as O00OOOOOO00O0000O :#line:693
            print (O00OOOOOO00O0000O )#line:694
    def friends_invitation (O00OOOO0O00000000 ):#line:697
        try :#line:698
            OOO00OO000O0O00O0 =f'__{timi_new()}'#line:699
            OO000OOO0000OOO00 ={'authorization':O00OOOO0O00000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO000O0O00O0 ),'signstring':OOO00OO000O0O00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:708
            O00OOOOO000OOOOO0 =requests .request ('get',f'{host}/friends',headers =OO000OOO0000OOO00 ).json ()#line:709
            if 'status'in O00OOOOO000OOOOO0 :#line:710
                if O00OOOOO000OOOOO0 ['status']==200 :#line:711
                    OOOO0000OO0O00OO0 =O00OOOOO000OOOOO0 ['data']['myInviteter']#line:712
                    if OOOO0000OO0O00OO0 :#line:713
                        O0OOO0O0O00OOO00O =OOOO0000OO0O00OO0 ['user']['nickname']#line:714
                        O00O00OOOO000OO0O =O00OOOO0O00000000 .certification ()#line:715
                        print (f'【查邀请人】:我的邀请人:{O0OOO0O0O00OOO00O}丨实名:{O00O00OOOO000OO0O}')#line:716
                    else :#line:717
                        if O00OOOO0O00000000 .innerId !='0':#line:718
                            O00OOOO0O00000000 .invitation ()#line:719
        except Exception as O0OOOO000OOO00O0O :#line:720
            print (O0OOOO000OOO00O0O )#line:721
    def add_clover (OOOOOO0O0OO0OO0OO ):#line:724
        global golden_seed #line:725
        try :#line:726
            O0O0000000OO000O0 =f'__{timi_new()}'#line:727
            O00O0OOOOO0OO0OO0 ={'authorization':OOOOOO0O0OO0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000000OO000O0 ),'signstring':O0O0000000OO000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:736
            OOO0O0OOO00OO0O0O =requests .request ('get',f'{host}/assets/clovers',headers =O00O0OOOOO0OO0OO0 ).json ()#line:737
            if 'status'in OOO0O0OOO00OO0O0O :#line:739
                if OOO0O0OOO00OO0O0O ['status']==200 :#line:740
                    OO000O0O0000O0OO0 =OOO0O0OOO00OO0O0O ['data']['clover']#line:741
                    O0O000OO00O0OOOO0 =OOO0O0OOO00OO0O0O ['data']['used_clover']#line:742
                    OO0O0O0O0OO0O0OOO =float (OO000O0O0000O0OO0 )-float (O0O000OO00O0OOOO0 )#line:743
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0O000OO00O0OOOO0}')#line:744
                    if OOOOOO0O0OO0OO0OO .certification ()!='未实名':#line:745
                        if OO0O0O0O0OO0O0OOO >1 :#line:746
                            O0O0000000OO000O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0O0O0O0OO0O0OOO)}_{timi_new()}'#line:747
                            O00O0OOOOO0OO0OO0 ={'authorization':OOOOOO0O0OO0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000000OO000O0 ),'signstring':O0O0000000OO000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:756
                            O000OOO00OO0000OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0O0O0O0OO0O0OOO )}#line:757
                            O0O00OO0OO0OOOOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =O00O0OOOOO0OO0OO0 ,data =O000OOO00OO0000OO ).json ()#line:758
                            if 'status'in O0O00OO0OO0OOOOOO :#line:760
                                if O0O00OO0OO0OOOOOO ['status']==200 :#line:761
                                    print (f'【参与抽奖】:添加三叶草:{O0O00OO0OO0OOOOOO["data"]}丨数量:{OO0O0O0O0OO0O0OOO}')#line:762
                                if O0O00OO0OO0OOOOOO ['status']==500 :#line:763
                                    print (f'【参与抽奖】:添加三叶草:{O0O00OO0OO0OOOOOO["message"]}')#line:764
            O000O00OOOO00OOO0 =requests .request ('get',f'{host}/lottery',headers =O00O0OOOOO0OO0OO0 ).json ()#line:765
            O0OOOOO000O0OOO0O =OOOOOO0O0OO0OO0OO .winning_rewards ()#line:767
            if 'status'in O000O00OOOO00OOO0 :#line:768
                if O000O00OOOO00OOO0 ['status']==200 :#line:769
                    OO00O00OO0OOOO00O =O000O00OOOO00OOO0 ['data'][0 ]['day_get_gold_quantity']#line:770
                    golden_seed +=float (OO00O00OO0OOOO00O )#line:771
                    print (f'【参与抽奖】:预计每天中{str(OO00O00OO0OOOO00O)[:6]}颗金种子丨好友收益:{str(O0OOOOO000O0OOO0O)[:6]}')#line:772
        except Exception as OOOO00OO00O0O0O0O :#line:773
            print (OOOO00OO00O0O0O0O )#line:774
    def energy (OO0O0O0O00O00OOO0 ):#line:777
        try :#line:778
            while True :#line:779
                O00OO0OO0OO0000OO =f'__{timi_new()}'#line:780
                O00O000000OOOOOO0 ={'authorization':OO0O0O0O00O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OO0OO0000OO ),'signstring':O00OO0OO0OO0000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:789
                O000000OOOO00O0OO =requests .request ('get',f'{host}/energy/general',headers =O00O000000OOOOOO0 ).json ()#line:790
                if 'status'in O000000OOOO00O0OO :#line:792
                    if O000000OOOO00O0OO ['status']==200 :#line:793
                        OOO00O0OOO00OO0OO =O000000OOOO00O0OO ['data']['ordinary_water']#line:794
                        O0OO000OO0OO0OO00 =O000000OOOO00O0OO ['data']['ordinary_fertilizer']#line:795
                        print (f'【我的营养】:肥料:{str(O0OO000OO0OO0OO00).split(".")[0]}丨水滴:{str(OOO00O0OOO00OO0OO).split(".")[0]}')#line:797
                        if float (O0OO000OO0OO0OO00 )<96 :#line:798
                            time .sleep (random .randint (160 ,180 )/10 )#line:799
                            OOOOOO00O0O00OO0O =99 -float (O0OO000OO0OO0OO00 )#line:800
                            OO0OOOO0000O00000 ={"fertilizer":str (OOOOOO00O0O00OO0O ).split ('.')[0 ]}#line:801
                            O00OO00000O0OO0OO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00O000000OOOOOO0 ).json ()#line:802
                            if 'status'in O00OO00000O0OO0OO :#line:804
                                if O00OO00000O0OO0OO ['status']==200 :#line:805
                                    print (f'【购买肥料】:看广告获取肥料:{O00OO00000O0OO0OO["message"]}')#line:806
                        if float (OOO00O0OOO00OO0OO )<880 :#line:807
                            time .sleep (random .randint (160 ,180 )/10 )#line:808
                            OO000OOOOOOOO0OOO =999 -float (OOO00O0OOO00OO0OO )#line:809
                            O00OO0OO00OO0OOOO ={"water":str (OO000OOOOOOOO0OOO ).split ('.')[0 ]}#line:810
                            O00OOO0O00O00OO0O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00O000000OOOOOO0 ).json ()#line:811
                            if 'status'in O00OOO0O00O00OO0O :#line:813
                                if O00OOO0O00O00OO0O ['status']==200 :#line:814
                                    print (f'【购买水滴】:看广告获取水滴:{O00OOO0O00O00OO0O["message"]}')#line:815
                        if float (O0OO000OO0OO0OO00 )>96 and float (OOO00O0OOO00OO0OO )>880 :#line:816
                            break #line:817
        except Exception as OO000000OOO0O00O0 :#line:819
            print (OO000000OOO0O00O0 )#line:820
def bundled_def ():#line:822
    OO000OO00O00OO0OO =['5570536','7750212','7911652','7911680','7805624']#line:823
    return OO000OO00O00OO0OO [random .randint (0 ,len (OO000OO00O00OO0OO )-1 )]#line:824
def version_of_the_validation ():#line:828
    return str ((75 -56 )/10 )#line:829
def gitee_validation ():#line:832
    try :#line:833
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:834
    except :#line:835
        sys .exit (0 )#line:836
def update_the_validation ():#line:840
    try :#line:841
        O00O0OOOOOO00O00O =gitee_validation ()#line:842
        if version_of_the_validation ()<O00O0OOOOOO00O00O ['CityEarth']['edition']:#line:843
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0OOOOOO00O00O["CityEarth"]["edition"]}   ❌')#line:844
            print (f'更新内容=>>{O00O0OOOOOO00O00O["CityEarth"]["content"]}   👍')#line:845
        else :#line:846
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0OOOOOO00O00O["CityEarth"]["edition"]}   ✅')#line:847
            print (f'更新内容=>> {O00O0OOOOOO00O00O["CityEarth"]["content"]}   👍')#line:848
    except Exception as OO0000OO0OOO000O0 :#line:849
        print (OO0000OO0OOO000O0 )#line:850
def os_qinglong ():#line:853
    if application in os .environ :#line:854
        O00O00O00O00OO0O0 =os .environ [application ].split ('\n')#line:855
        if len (O00O00O00O00OO0O0 )>0 :#line:856
            return O00O00O00O00OO0O0 #line:857
        else :#line:858
            print (f"{application}变量未启用")#line:859
            print ('脚本退出')#line:860
            sys .exit (1 )#line:861
    else :#line:862
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:864
        return os_built ()#line:865
def os_built ():#line:868
    if token :#line:869
        O0O000O00OOOOO0OO =token .split ('\n')#line:870
        if len (O0O000O00OOOOO0OO )>0 :#line:871
            return O0O000O00OOOOO0OO #line:872
    else :#line:873
        print (f"内置变量为空")#line:874
        print ('脚本结束')#line:875
        sys .exit (0 )#line:876
if __name__ =='__main__':#line:879
    start ()#line:880
