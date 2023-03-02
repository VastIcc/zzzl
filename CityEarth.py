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
    from notify import send
except Exception as E:
    t = re.findall("d '(.*?)'", str(E))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: 8 1-23/2 * * *
@ new Env('生城世朝')
@ 项目地址  https://sc19319.oss-cn-hangzhou.aliyuncs.com/scsc/prod/1.9.3.1.S4195.apk
@ 抓取  http://scsc.sc19319.com 的authorization值
@ 青龙变量  青龙配置文件 export ce_token="authorization&赠送金种子数量大于&赠送金种子id" 
@ 如果你有20金种子填10就会赠 填21就不会赠送  不赠送全填 999999     多号换行
@ 变量示范    export ce_token="557b8069-1234-4ae7-9e29-b7871f91541b&999999&999999"  用&符号分开数据
@ 版本  2.8
"""
application = 'ce_token'  # 变量名
token = ''

##################################配置区##################################
energy = True              # True 为用金种子添加肥料    False 为不添加肥料和水滴
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.41954131'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        O0O00OO0OOOOO0O0O =os_qinglong ()#line:10
        print (f"==========共找到{len(O0O00OO0OOOOO0O0O)}个账号==========")#line:11
        for O0O000O00000OOO00 in O0O00OO0OOOOO0O0O :#line:12
            OO0000OO0O0O0OOO0 =[]#line:13
            print (f"------------正在执行第{O0O00OO0OOOOO0O0O.index(O0O000O00000OOO00) + 1}个账号------------")#line:14
            OOO00OO0OO00O00O0 =CityEarth (O0O000O00000OOO00 ,OO0000OO0O0O0OOO0 )#line:15
            def OOO000000OOO00OOO ():#line:17
                if OOO00OO0OO00O00O0 .base_info ():#line:19
                    OOO00OO0OO00O00O0 .sealing ()#line:21
                    OOO00OO0OO00O00O0 .invitenum ()#line:23
                    OOO00OO0OO00O00O0 .game_map ()#line:25
                    OOO00OO0OO00O00O0 .friends_invitation ()#line:27
                    OOO00OO0OO00O00O0 .energy ()#line:29
                    OOO00OO0OO00O00O0 .add_clover ()#line:31
                    OOO00OO0OO00O00O0 .propsraffle ()#line:33
                    OOO00OO0OO00O00O0 .synthetic ()#line:35
                    OOO00OO0OO00O00O0 .crops_illustrated ()#line:37
                    OOO00OO0OO00O00O0 .give_gold ()#line:39
                    OOO00OO0OO00O00O0 .withdraw ()#line:41
            OO00O0O0O000O00OO =threading .Thread (target =OOO000000OOO00OOO )#line:43
            OO00O0O0O000O00OO .start ()#line:44
            time .sleep (time_xx )#line:45
        print (f"------------正在处理推送通知------------")#line:46
        time .sleep (0.5 )#line:47
        O0O000O0O0O000000 =format_msg ()#line:48
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O000O0O0O000000 +' ')#line:49
    except Exception as O0OO00OOO0OOOO0OO :#line:50
        print (O0OO00OOO0OOOO0OO )#line:51
def give_gold (O00OOOO0O000O00OO ,O0OO00O00O0O0O0O0 ):#line:54
        try :#line:55
            O000OOOO00OO00OO0 =f'_doneeNo={O00OOOO0O000O00OO}&quantity={int(O0OO00O00O0O0O0O0)}_{timi_new()}'#line:56
            O0OOO000OO0OO00O0 ={'source':'scsc','authorization':os_qinglong ()[0 ].split ('&')[0 ],'timestamp':str (timi_new ()),'sign':sign (O000OOOO00OO00OO0 ),'signstring':O000OOOO00OO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:67
            OOO0OOO00O000OO0O ={"quantity":int (O0OO00O00O0O0O0O0 ),"doneeNo":O00OOOO0O000O00OO }#line:71
            O0O000OO0O0O0OOOO =requests .request ('post',f'{host}/finance/give-gold',headers =O0OOO000OO0OO00O0 ,data =OOO0OOO00O000OO0O ).json ()#line:72
            if 'status'in O0O000OO0O0O0OOOO :#line:74
                if O0O000OO0O0O0OOOO ['status']==200 :#line:75
                    if O0O000OO0O0O0OOOO ['data']:#line:76
                        print (f'【赠送种子】:赠送{int(O0OO00O00O0O0O0O0)}种子给{O00OOOO0O000O00OO}成功')#line:77
                        return True #line:78
                if O0O000OO0O0O0OOOO ['status']==401 :#line:79
                    print (f'【赠送种子】:{O0O000OO0O0O0OOOO["message"]}')#line:80
                    return False #line:81
                if O0O000OO0O0O0OOOO ['status']==500 :#line:82
                    print (f'【赠送种子】:{O0O000OO0O0O0OOOO["message"]}')#line:83
                    return False #line:84
            return False #line:85
        except Exception as OOOOO00OOOOO00OO0 :#line:86
            print (OOOOO00OOOOO00OO0 )#line:87
def sign (OO000O0O0OOO00000 ):#line:90
    OO0OOO00OO0O0OO0O =hashlib .md5 (OO000O0O0OOO00000 .encode ()).hexdigest ()#line:91
    OOOOOO00OO000O000 ="scsc%^&*"+OO0OOO00OO0O0OO0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:92
    O00OO0OO0O00OOOOO =hashlib .md5 (OOOOOO00OO000O000 .encode ()).hexdigest ()#line:93
    return O00OO0OO0O00OOOOO #line:94
def format_msg ():#line:96
    O00OOO00O0OO00O0O =""#line:97
    for OOO000OO00OO0OO00 in msg_list :#line:98
        O00OOO00O0OO00O0O +=str (OOO000OO00OO0OO00 )+"\r\n"#line:99
    return O00OOO00O0OO00O0O #line:100
def timi_new ():#line:102
    return str (int (time .time ()*1000 ))#line:103
class CityEarth :#line:106
    def __init__ (OOO0O00OO000OO0O0 ,OOOO00OO0OOO0OOOO ,OOO0O00OO0000OOO0 ):#line:108
        try :#line:109
            OOO0O00OO000OO0O0 .msg =OOO0O00OO0000OOO0 #line:110
            OOO0O00OO000OO0O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:111
            OOO0O00OO000OO0O0 .token =OOOO00OO0OOO0OOOO .split ('&')[0 ]#line:112
            OOO0O00OO000OO0O0 .innerId =OOOO00OO0OOO0OOOO .split ('&')[1 ]#line:113
            OOO0O00OO000OO0O0 .doneeNo =OOOO00OO0OOO0OOOO .split ('&')[2 ]#line:114
        except :#line:115
            print ('变量格式错误')#line:116
    def base_info (OOO0OOOO000O0O0O0 ):#line:119
        try :#line:120
            OOO0OOOO000O0O0O0 .watched_ad ()#line:122
            O0O00O0O0O000OO00 =f'__{timi_new()}'#line:123
            OO0OOO00000OO0O00 ={'source':'scsc','authorization':OOO0OOOO000O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O0O000OO00 ),'signstring':O0O00O0O0O000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:134
            O0O0000O000O00O0O =requests .request ('get',f'{host}/user',headers =OO0OOO00000OO0O00 ).json ()#line:135
            if 'status'in O0O0000O000O00O0O :#line:137
                if O0O0000O000O00O0O ['status']==200 :#line:138
                    OOO0O0000OOOOOO0O =O0O0000O000O00O0O ['data']['nickname']#line:139
                    O00O0O00000O0O0O0 =O0O0000O000O00O0O ['data']['inner_id']#line:140
                    OOO0O00OOO0O000OO =O0O0000O000O00O0O ['data']['assets']['gold']#line:141
                    O0OOOO0O0O00O00O0 =O0O0000O000O00O0O ['data']['level']#line:142
                    print (f'【账号信息】:昵称:{OOO0O0000OOOOOO0O[:5]}丨ID:{O00O0O00000O0O0O0}丨等级:{O0OOOO0O0O00O00O0}丨金种子:{str(OOO0O00OOO0O000OO).split(".")[0]}')#line:143
                if O0O0000O000O00O0O ['status']==401 :#line:144
                    print (O0O0000O000O00O0O ['message'])#line:145
                    OOO0OOOO000O0O0O0 .msg .append ('有账号失效了')#line:146
                    return False #line:147
                if O0O0000O000O00O0O ['status']==500 :#line:148
                    return False #line:149
            return True #line:150
        except Exception as O00O0000OO00OOOOO :#line:151
            print (O00O0000OO00OOOOO )#line:152
    def sealing (O0OO0OOOO0O0O00O0 ):#line:155
        try :#line:156
            O000O0OO00O0O00OO =f'__{timi_new()}'#line:157
            O000OO00O00OOO000 ={'source':'scsc','authorization':O0OO0OOOO0O0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO00O0O00OO ),'signstring':O000O0OO00O0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:168
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O000OO00O00OOO000 )#line:169
            requests .request ('get',f'{host}/packsack/list',headers =O000OO00O00OOO000 )#line:170
            requests .request ('get',f'{host}/friends/invited/ad',headers =O000OO00O00OOO000 )#line:171
            requests .request ('get',f'{host}/assets/gold/rank',headers =O000OO00O00OOO000 )#line:172
            requests .request ('get',f'{host}/user',headers =O000OO00O00OOO000 )#line:173
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O000OO00O00OOO000 )#line:174
            requests .request ('get',f'{host}/finance/get-power-list',headers =O000OO00O00OOO000 )#line:175
            requests .request ('post',f'{host}/announcement/announcement',headers =O000OO00O00OOO000 )#line:176
            requests .request ('get',f'{host}/game/getAllData',headers =O000OO00O00OOO000 )#line:177
            requests .request ('get',f'{host}/assets',headers =O000OO00O00OOO000 )#line:178
        except Exception as OOOO0O0000OO00O0O :#line:179
            print (OOOO0O0000OO00O0O )#line:180
    def withdraw (O00O0O00OOO0000O0 ):#line:184
        O0O0OO00OO0000O00 =f'__{timi_new()}'#line:185
        OO0O0OO0OO0O0O000 ={'source':'scsc','authorization':O00O0O00OOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00OO0000O00 ),'signstring':O0O0OO00OO0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:196
        OOO00OOO000O0OO0O =requests .request ('get',f'{host}/assets',headers =OO0O0OO0OO0O0O000 ).json ()#line:197
        if 'status'in OOO00OOO000O0OO0O :#line:199
            if OOO00OOO000O0OO0O ['status']==200 :#line:200
                O0O0O0000OOO00O0O =OOO00OOO000O0OO0O ['data']['cash']#line:201
                if float (O0O0O0000OOO00O0O )>20 :#line:202
                    O0O0OO00OO0000O00 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:203
                    OO0O0OO0OO0O0O000 ={'authorization':O00O0O00OOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00OO0000O00 ),'signstring':O0O0OO00OO0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:213
                    O00O00O0OOO000O0O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:214
                    O0OOOOOO0OOO00O0O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO0O0OO0OO0O0O000 ,data =O00O00O0OOO000O0O ).json ()#line:216
                    print (O0OOOOOO0OOO00O0O )#line:217
    def invitenum (OO000OO00OOO00O00 ):#line:220
        O000OO00O0O0000O0 =f'__{timi_new()}'#line:221
        OO000OO00OOOOO0O0 ={'source':'scsc','authorization':OO000OO00OOO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00O0O0000O0 ),'signstring':O000OO00O0O0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:232
        O0O0OOO000OOOO000 =requests .request ('get',f'{host}/invite/invitenum',headers =OO000OO00OOOOO0O0 ).json ()#line:233
        if 'status'in O0O0OOO000OOOO000 :#line:235
            if O0O0OOO000OOOO000 ['status']==200 :#line:236
                O00OOOO00000OO0OO =O0O0OOO000OOOO000 ['data']['invited_count']#line:237
                O000OO0O0O0OOOOO0 =O0O0OOO000OOOO000 ['data']['invited_second_count']#line:238
                print (f'【我的邀请】:直邀好友:{O00OOOO00000OO0OO}丨间邀好友:{O000OO0O0O0OOOOO0}')#line:239
    def game_map (OO0O00O00O0000000 ):#line:242
        try :#line:243
            OO000OOOO00OO0O0O =f'__{timi_new()}'#line:244
            O0OOO000OOOOO00OO ={'source':'scsc','authorization':OO0O00O00O0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOO00OO0O0O ),'signstring':OO000OOOO00OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:255
            O000OOO00OO0000OO =requests .request ('get',f'{host}/game/map',headers =O0OOO000OOOOO00OO ).json ()#line:256
            if 'status'in O000OOO00OO0000OO :#line:258
                if O000OOO00OO0000OO ['status']==200 :#line:259
                    for OO0OOO0OOOO000OOO in O000OOO00OO0000OO ['data']['list'][0 ]['crops']:#line:260
                        O0O0000OOOO000O0O =OO0OOO0OOOO000OOO ['level']#line:262
                        if O0O0000OOOO000O0O ==41 :#line:263
                            OOOOO0O00OO00O00O =OO0OOO0OOOO000OOO ['crop_name']#line:264
                            OOO0O0O00O0OO0OOO =OO0OOO0OOOO000OOO ['count']#line:265
                            if OOO0O0O00O0OO0OOO >0 :#line:266
                                print (f'【农业资产】:{OOOOO0O00OO00O00O}丨数量:{OOO0O0O00O0OO0OOO}')#line:267
        except Exception as O000OOOO0O00OOOO0 :#line:268
            print (O000OOOO0O00OOOO0 )#line:269
    def give_gold (O0OOOOOOO0000O000 ):#line:272
        try :#line:273
            OOOO0000000O00O0O =f'__{timi_new()}'#line:274
            O0OOOO0O0O0OO00O0 ={'source':'scsc','authorization':O0OOOOOOO0000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000000O00O0O ),'signstring':OOOO0000000O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:285
            OO00O0OO0O0O00OOO =requests .request ('get',f'{host}/user',headers =O0OOOO0O0O0OO00O0 ).json ()#line:286
            if 'status'in OO00O0OO0O0O00OOO :#line:287
                if OO00O0OO0O0O00OOO ['status']==200 :#line:288
                    if float (O0OOOOOOO0000O000 .doneeNo )!=0 :#line:289
                        OO0O00OOO0O0OO00O =OO00O0OO0O0O00OOO ['data']['assets']['gold']#line:290
                        if float (OO0O00OOO0O0OO00O )>float (O0OOOOOOO0000O000 .innerId ):#line:291
                            O00O0O0OO000O00O0 =int (float (OO0O00OOO0O0OO00O )/1.1 )#line:292
                            OOOO0000000O00O0O =f'_doneeNo={O0OOOOOOO0000O000.doneeNo}&quantity={O00O0O0OO000O00O0}_{timi_new()}'#line:293
                            O0OOOO0O0O0OO00O0 ={'source':'scsc','authorization':O0OOOOOOO0000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000000O00O0O ),'signstring':OOOO0000000O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:304
                            OO0OO0000000OO000 ={"quantity":O00O0O0OO000O00O0 ,"doneeNo":O0OOOOOOO0000O000 .doneeNo }#line:308
                            OOOOO0OOO0O0000O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0OOOO0O0O0OO00O0 ,data =OO0OO0000000OO000 ).json ()#line:309
                            if 'status'in OOOOO0OOO0O0000O0 :#line:311
                                if OOOOO0OOO0O0000O0 ['status']==200 :#line:312
                                    if OOOOO0OOO0O0000O0 ['data']:#line:313
                                        print (f'【赠送种子】:赠送{O00O0O0OO000O00O0}种子给{O0OOOOOOO0000O000.doneeNo}成功')#line:314
                    else :#line:315
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:316
        except Exception as O00OOO0O00O00O0OO :#line:317
            print (O00OOO0O00O00O0OO )#line:318
    def invitation (OOO0O0OO00O000OOO ):#line:320
        try :#line:321
            _OOO0O0OOO0OOO0O0O =float (bundled_def ())/4 #line:322
            OO00OOO0OOOOO0O0O =f'_innerId={int(_OOO0O0OOO0OOO0O0O)}_{timi_new()}'#line:323
            OOOOO000O00OO00OO ={'source':'scsc','authorization':OOO0O0OO00O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO0OOOOO0O0O ),'signstring':OO00OOO0OOOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:334
            O0OOOOO00O00O000O ={"innerId":int (_OOO0O0OOO0OOO0O0O )}#line:335
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOOO000O00OO00OO ,data =O0OOOOO00O00O000O )#line:336
        except Exception as OO0OOO0O0OO000O00 :#line:337
            print (OO0OOO0O0OO000O00 )#line:338
    def winning_rewards (O00OO0O000OOOOOO0 ):#line:341
        try :#line:342
            O0O00000OO000OO0O =f'__{timi_new()}'#line:343
            O000O0OOO00OO0OOO ={'source':'scsc','authorization':O00OO0O000OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000OO000OO0O ),'signstring':O0O00000OO000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:354
            O000O00OO0O0O0O0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O000O0OOO00OO0OOO ).json ()#line:355
            if 'status'in O000O00OO0O0O0O0O :#line:357
                if O000O00OO0O0O0O0O ['status']==200 :#line:358
                    if O000O00OO0O0O0O0O ['data']['amount']:#line:359
                        O00O00OO0O00000OO =O000O00OO0O0O0O0O ['data']['amount']['gold']#line:360
                        return O00O00OO0O00000OO #line:361
                    else :#line:362
                        return 0 #line:363
        except Exception as OOO00OO0OO0OO00O0 :#line:364
            print (OOO00OO0OO0OO00O0 )#line:365
    def certification (OO0O0O0OO0000O0O0 ):#line:368
        try :#line:369
            O0O00O00OOO0OO0O0 =f'__{timi_new()}'#line:370
            OO0O0OOO0OO00OO0O ={'source':'scsc','authorization':OO0O0O0OO0000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00OOO0OO0O0 ),'signstring':O0O00O00OOO0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:381
            O00OOOOOO00O0O000 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0O0OOO0OO00OO0O ).json ()#line:382
            if 'status'in O00OOOOOO00O0O000 :#line:384
                if O00OOOOOO00O0O000 ['status']==200 :#line:385
                    if O00OOOOOO00O0O000 ['data']['result']:#line:386
                        O0O0O0O00OOO00O00 =O00OOOOOO00O0O000 ['data']['nick_name']#line:387
                        return O0O0O0O00OOO00O00 #line:388
                    else :#line:389
                        return '未实名'#line:390
        except Exception as OO0O000OOO00O00OO :#line:391
            print (OO0O000OOO00O00OO )#line:392
    def crops_illustrated (OO00O00O000OOO00O ):#line:395
        try :#line:396
            O0OOOOOO000O0O0O0 =f'__{timi_new()}'#line:397
            O0OOO0000O00O00O0 ={'source':'scsc','authorization':OO00O00O000OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOO000O0O0O0 ),'signstring':O0OOOOOO000O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            OOOOO000OOO00OOO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OOO0000O00O00O0 ).json ()#line:409
            if 'status'in OOOOO000OOO00OOO0 :#line:411
                if OOOOO000OOO00OOO0 ['status']==200 :#line:412
                    O00OO0O00O0OO00O0 =OOOOO000OOO00OOO0 ['data'][0 ]['crops']#line:413
                    for OOOO000O0O000OO0O in O00OO0O00O0OO00O0 :#line:414
                        if OOOO000O0O000OO0O ['ill_clover_award']:#line:415
                            if float (OOOO000O0O000OO0O ['ill_clover_award'])>1 :#line:416
                                if OOOO000O0O000OO0O ['is_finish']:#line:417
                                    if not OOOO000O0O000OO0O ['is_getit']:#line:418
                                        if OO00O00O000OOO00O .certification ()!='未实名':#line:419
                                            O0OOOOOO000O0O0O0 =f'_award_level={OOOO000O0O000OO0O["level"]}_{timi_new()}'#line:420
                                            O0OOO0000O00O00O0 ={'source':'scsc','authorization':OO00O00O000OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOO000O0O0O0 ),'signstring':O0OOOOOO000O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:431
                                            O0OOO0OO00O00O00O ={"award_level":OOOO000O0O000OO0O ['level']}#line:432
                                            O0000O0O00000OO00 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OOO0000O00O00O0 ,json =O0OOO0OO00O00O00O ).json ()#line:434
                                            if 'status'in O0000O0O00000OO00 :#line:435
                                                if O0000O0O00000OO00 ['status']==200 :#line:436
                                                    O000000OOOOO0OO0O =O0000O0O00000OO00 ['data']['ill_clover_award']#line:437
                                                    print (f'【图鉴奖励】:领取{OOOO000O0O000OO0O["crop_name"]}成就丨奖励{O000000OOOOO0OO0O}☘️')#line:439
                                                if O0000O0O00000OO00 ['status']==500 :#line:440
                                                    print (f'【图鉴奖励】:{O0000O0O00000OO00["message"]}')#line:441
        except Exception as O00OO0O0000O0OO0O :#line:442
            print (O00OO0O0000O0OO0O )#line:443
    def watched_ad (OOO0O00O0O0O000OO ):#line:446
        try :#line:447
            O0OOO0000OOO0OOOO =f'__{timi_new()}'#line:448
            OO0OOO00O000O000O ={'source':'scsc','authorization':OOO0O00O0O0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000OOO0OOOO ),'signstring':O0OOO0000OOO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:459
            O00OO0OO00OOOOO0O =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOO00O000O000O ).json ()#line:460
            if 'status'in O00OO0OO00OOOOO0O :#line:462
                if O00OO0OO00OOOOO0O ['status']==200 :#line:463
                    if 'offlineInfo'in O00OO0OO00OOOOO0O ['data']:#line:464
                        time .sleep (random .randint (3 ,5 ))#line:465
                        OOOO0O0OO00OOO000 =O00OO0OO00OOOOO0O ['data']['offlineInfo']['off_minute']#line:466
                        O0OO0OOOO0O00O0O0 =float (O00OO0OO00OOOOO0O ['data']['silver'])/1000000000000 #line:467
                        time .sleep (1 )#line:468
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0OOO00O000O000O ).json ()#line:469
                        time .sleep (2 )#line:470
                        O0O0OOOO0O0O0O00O =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOO00O000O000O ).json ()#line:471
                        if 'status'in O0O0OOOO0O0O0O00O :#line:473
                            if O0O0OOOO0O0O0O00O ['status']==200 :#line:474
                                OOOOO000OO0OOO000 =float (O0O0OOOO0O0O0O00O ['data']['silver'])/1000000000000 #line:475
                                O00O00OOOO0O0000O =str (OOOOO000OO0OOO000 -O0OO0OOOO0O00O0O0 )[:6 ]#line:476
                                print (f'【离线奖励】:翻倍离线{OOOO0O0OO00OOO000}分钟奖励🌱数量:{O00O00OOOO0O0000O}t粒')#line:477
        except Exception as OOOOO0000OOOO00OO :#line:478
            print (OOOOO0000OOOO00OO )#line:479
    def user_ad (O0O0OO0O0OOO0O000 ):#line:482
        try :#line:483
            OO0OOOO0O0OO0O00O =f'__{timi_new()}'#line:484
            O000O00O000000O0O ={'source':'scsc','authorization':O0O0OO0O0OOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0O0OO0O00O ),'signstring':OO0OOOO0O0OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:495
            OO0O00O00OO0O0O00 =requests .request ('get',f'{host}/user/ad',headers =O000O00O000000O0O ).json ()#line:496
            if 'status'in OO0O00O00OO0O0O00 :#line:498
                if OO0O00O00OO0O0O00 ['status']==200 :#line:499
                    OOO0OO000OO0O0000 =OO0O00O00OO0O0O00 ['data']['max_time']#line:500
                    OOOOOOOO0OO000OO0 =OO0O00O00OO0O0O00 ['data']['watch_time']#line:501
                    OO0O0O00OO0O00OO0 =OO0O00O00OO0O0O00 ['data']['added_time']#line:502
                    print (f'【获取种子】:获取🌱剩余{OO0O0O00OO0O00OO0 + OOO0OO000OO0O0000 - OOOOOOOO0OO000OO0}次丨好友提供:{OO0O0O00OO0O00OO0}次')#line:503
                    if OO0O0O00OO0O00OO0 +OOO0OO000OO0O0000 -OOOOOOOO0OO000OO0 >0 :#line:504
                        time .sleep (random .randint (16 ,19 ))#line:505
                        O0OO00O0OOO0OO0O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O000O00O000000O0O ).json ()#line:506
                        if 'status'in O0OO00O0OOO0OO0O0 :#line:508
                            if O0OO00O0OOO0OO0O0 ['status']==200 :#line:509
                                OOO0OO0O00OOO0O0O =float (O0OO00O0OOO0OO0O0 ['data']['silver'])/1000000000000 #line:510
                                print (f'【获取种子】:获得🌱:{int(OOO0OO0O00OOO0O0O)}t粒')#line:511
                                return True #line:512
                            if O0OO00O0OOO0OO0O0 ['status']==500 :#line:513
                                OOO0O0O0000O0OO0O =O0OO00O0OOO0OO0O0 ['message']#line:514
                                print (f'【获取种子】:{OOO0O0O0000O0OO0O}')#line:515
                                return False #line:516
        except Exception as O0OO00000OO0OOO0O :#line:517
            print (O0OO00000OO0OOO0O )#line:518
    def synthetic (OOOO000OOOO0000OO ):#line:521
        global id ,g #line:522
        try :#line:523
            O000OOOOOO0O0OOO0 =OOOO000OOOO0000OO .level_new ()#line:524
            OO000O000OOO0000O =random .randint (9 ,11 )#line:525
            O0OO0OOO0OOOO00OO =f'_site=8&targetSite={OO000O000OOO0000O}_{timi_new()}'#line:526
            O00OOO0O0OO0O0000 ={'source':'scsc','authorization':OOOO000OOOO0000OO .token ,'timestamp':timi_new (),'sign':sign (O0OO0OOO0OOOO00OO ),'signstring':O0OO0OOO0OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:537
            OO0OO00OO0000OOO0 ={"site":int (8 ),"targetSite":int (OO000O000OOO0000O )}#line:538
            requests .request ('post',f'{host}/game/crops/move',headers =O00OOO0O0OO0O0000 ,json =OO0OO00OO0000OOO0 )#line:539
            while True :#line:540
                O000000O0O0000O0O =f'__{timi_new()}'#line:541
                O00O0OOO00OOO0OOO ={'source':'scsc','authorization':OOOO000OOOO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O0O0000O0O ),'signstring':O000000O0O0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:552
                OO0000000OO0OO0OO =requests .request ('get',f'{host}/game/getAllData',headers =O00O0OOO00OOO0OOO ).json ()#line:553
                if 'status'in OO0000000OO0OO0OO :#line:555
                    if OO0000000OO0OO0OO ['status']==200 :#line:556
                        OO00O0OOO0O0OOOO0 =OO0000000OO0OO0OO ['data']['cropList']#line:557
                        O0OO0O0000O0OO000 =OO0000000OO0OO0OO ['data']['gameCoreDataDBid']#line:558
                        OO0OOO0OO00OO0000 =float (OO0000000OO0OO0OO ['data']['silver'])/1000000000000 #line:559
                        OOO0O000OOOOOOO0O =0 #line:564
                        for OO00O000000OOO000 in OO00O0OOO0O0OOOO0 :#line:565
                            if not OO00O000000OOO000 :#line:566
                                OOOOO0O0OO0O000OO =f'_crop_id={O0OO0O0000O0OO000}&site={OOO0O000OOOOOOO0O}_{OOOO000OOOO0000OO.time}'#line:567
                                OO00OOO00O0OO00O0 ={'source':'scsc','authorization':OOOO000OOOO0000OO .token ,'timestamp':OOOO000OOOO0000OO .time ,'sign':sign (OOOOO0O0OO0O000OO ),'signstring':OOOOO0O0OO0O000OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:577
                                OOOO00O0O0OOO000O ={"site":OOO0O000OOOOOOO0O ,"crop_id":O0OO0O0000O0OO000 }#line:578
                                O0OOO00O0O00000OO =requests .request ('post',f'{host}/game/crops/buy',headers =OO00OOO00O0OO00O0 ,data =OOOO00O0O0OOO000O ).json ()#line:579
                                time .sleep (random .randint (1 ,3 )/10 )#line:581
                                if 'status'in O0OOO00O0O00000OO :#line:582
                                    if O0OOO00O0O00000OO ['status']==200 :#line:583
                                        if O0OOO00O0O00000OO ['message']=='种子数量不足':#line:584
                                            O000OOOOOO0O0OOO0 =OOOO000OOOO0000OO .level_new ()#line:585
                                            print (f'【种植合成】:{O0OOO00O0O00000OO["message"]}')#line:586
                                            if not OOOO000OOOO0000OO .user_ad ():#line:587
                                                return False #line:588
                                    if O0OOO00O0O00000OO ['status']==500 :#line:589
                                        print (f'【种植合成】:{O0OOO00O0O00000OO["message"]}')#line:590
                                        return False #line:591
                            OOO0O000OOOOOOO0O +=1 #line:592
                        OOO0OOO00OO00000O =requests .request ('get',f'{host}/game/getAllData',headers =O00O0OOO00OOO0OOO ).json ()#line:593
                        OO0OOO00OOO00O0OO =OOO0OOO00OO00000O ['data']['cropList']#line:594
                        OOOOO0OO0OO0OO000 =False #line:595
                        for OO00O000000OOO000 in range (12 ):#line:596
                            id =OO0OOO00OOO00O0OO [OO00O000000OOO000 ]['level']#line:597
                            if float (O000OOOOOO0O0OOO0 )-float (id )>9 :#line:598
                                O00O00O00OO00000O =f'_site={OO00O000000OOO000}_{timi_new()}'#line:599
                                OOO0O0OO00OOO0OOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOO000OOOO0000OO .token ,'timestamp':timi_new (),'sign':sign (O00O00O00OO00000O ),'signstring':O00O00O00OO00000O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:610
                                OO00O000000O0OOO0 ={"site":OO00O000000OOO000 }#line:611
                                OOO0O0O0O0OO00OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO0O0OO00OOO0OOO ,data =OO00O000000O0OOO0 ).json ()#line:613
                                if 'status'in OOO0O0O0O0OO00OOO :#line:614
                                    if OOO0O0O0O0OO00OOO ['status']==200 :#line:615
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:616
                            if id !=0 :#line:617
                                for OOO0OO0OO0OO000O0 in range (11 ):#line:618
                                    OO0O0OOOO000O0OO0 =OOO0OO0OO0OO000O0 +1 #line:619
                                    g =OO0OOO00OOO00O0OO [OO0O0OOOO000O0OO0 ]['level']#line:620
                                    if id ==g :#line:621
                                        O0O0OOO0O00O00OO0 =OOO0OO0OO0OO000O0 +2 #line:622
                                        if O0O0OOO0O00O00OO0 !=OO00O000000OOO000 +1 :#line:623
                                            O0O00OO0OOO0OOOO0 =OO00O000000OOO000 +1 #line:624
                                            time .sleep (random .randint (1 ,3 )/10 )#line:626
                                            O0OO0OOO0OOOO00OO =f'_site={O0O00OO0OOO0OOOO0 - 1}&targetSite={O0O0OOO0O00O00OO0 - 1}_{timi_new()}'#line:627
                                            O00OOO0O0OO0O0000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOO000OOOO0000OO .token ,'timestamp':timi_new (),'sign':sign (O0OO0OOO0OOOO00OO ),'signstring':O0OO0OOO0OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:644
                                            O00OO00000000OO00 ={"site":int (O0O00OO0OOO0OOOO0 -1 ),"targetSite":int (O0O0OOO0O00O00OO0 -1 )}#line:645
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00OOO0O0OO0O0000 ,json =O00OO00000000OO00 )#line:646
                                            OOOOO0OO0OO0OO000 =True #line:648
                                    if OOOOO0OO0OO0OO000 :#line:649
                                        break #line:650
                                if OOOOO0OO0OO0OO000 :#line:651
                                    break #line:652
        except :#line:653
            OOOO000OOOO0000OO .synthetic ()#line:654
    def level_new (O0000OOO0OOO0O0OO ):#line:657
        try :#line:658
            O00OO0O00OOOO00O0 =f'__{timi_new()}'#line:659
            OO0O0O0OOO00O0O0O ={'source':'scsc','authorization':O0000OOO0OOO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O00OOOO00O0 ),'signstring':O00OO0O00OOOO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:670
            OOOOO0O00OOO000O0 =requests .request ('get',f'{host}/user',headers =OO0O0O0OOO00O0O0O ).json ()#line:671
            if 'status'in OOOOO0O00OOO000O0 :#line:672
                if OOOOO0O00OOO000O0 ['status']==200 :#line:673
                    return float (OOOOO0O00OOO000O0 ['data']['level'])#line:674
        except Exception as OO0O0O000OO00OO0O :#line:675
            print (OO0O0O000OO00OO0O )#line:676
    def propsraffle (OO00O0OOO00O00OOO ):#line:679
        try :#line:680
            while True :#line:681
                OO0OOOO0O0000OOOO =f'__{timi_new()}'#line:682
                O0OOO00O00O0O00OO ={'source':'scsc','authorization':OO00O0OOO00O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0O0000OOOO ),'signstring':OO0OOOO0O0000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:693
                O0O000OOOO0O0O0OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OOO00O00O0O00OO ).json ()#line:694
                if 'status'in O0O000OOOO0O0O0OO :#line:696
                    if O0O000OOOO0O0O0OO ['status']==200 :#line:697
                        OOOO0000OOOOOOOOO =O0O000OOOO0O0O0OO ['data']['rows']#line:698
                        OO0O0OOOOOOOOOO00 =O0O000OOOO0O0O0OO ['data']['vstate']#line:699
                        if OOOO0000OOOOOOOOO ==5 or OOOO0000OOOOOOOOO ==6 or OOOO0000OOOOOOOOO ==7 :#line:700
                            OO0O00OOOO00OO000 =O0O000OOOO0O0O0OO ['data']['silver']#line:701
                            print (f'【转盘抽奖】:获得种子:{OO0O00OOOO00OO000}')#line:702
                        if OOOO0000OOOOOOOOO ==1 or OOOO0000OOOOOOOOO ==2 or OOOO0000OOOOOOOOO ==3 :#line:703
                            OO000OO0O000O0O00 =O0O000OOOO0O0O0OO ['data']['clover']#line:704
                            print (f'【转盘抽奖】:获得三叶草:{OO000OO0O000O0O00}')#line:705
                        if OOOO0000OOOOOOOOO ==4 or OOOO0000OOOOOOOOO ==8 :#line:706
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:707
                        if OOOO0000OOOOOOOOO =='抽奖次数已用完':#line:711
                            break #line:745
                time .sleep (random .randint (8 ,15 )/10 )#line:746
        except Exception as OOO0OOOOOO0O00OOO :#line:747
            print (OOO0OOOOOO0O00OOO )#line:748
    def friends_invitation (O00O0000OO00OO000 ):#line:751
        try :#line:752
            OO0OO0O000O0O00O0 =f'__{timi_new()}'#line:753
            O0O00OO0OOOOO00O0 ={'source':'scsc','authorization':O00O0000OO00OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O000O0O00O0 ),'signstring':OO0OO0O000O0O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:764
            O0OOOO0O000O0OOO0 =requests .request ('get',f'{host}/friends',headers =O0O00OO0OOOOO00O0 ).json ()#line:765
            if 'status'in O0OOOO0O000O0OOO0 :#line:766
                if O0OOOO0O000O0OOO0 ['status']==200 :#line:767
                    OO0O0O0OOOO0O0O00 =O0OOOO0O000O0OOO0 ['data']['myInviteter']#line:768
                    if OO0O0O0OOOO0O0O00 :#line:769
                        O0OOO0OO0OOO00OO0 =OO0O0O0OOOO0O0O00 ['user']['nickname']#line:770
                        OO000000O000OOO00 =O00O0000OO00OO000 .certification ()#line:771
                        print (f'【查邀请人】:我的邀请人:{O0OOO0OO0OOO00OO0}丨实名:{OO000000O000OOO00}')#line:772
                    else :#line:773
                        if O00O0000OO00OO000 .innerId !='0':#line:774
                            O00O0000OO00OO000 .invitation ()#line:775
        except Exception as OOOOOO00000O0O0OO :#line:776
            print (OOOOOO00000O0O0OO )#line:777
    def add_clover (O0O00O000OO0O0000 ):#line:780
        global golden_seed #line:781
        try :#line:782
            O00O00OOO0OOO0000 =f'__{timi_new()}'#line:783
            O0O000O0OO000O000 ={'source':'scsc','authorization':O0O00O000OO0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OOO0OOO0000 ),'signstring':O00O00OOO0OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
            O0OOOOO000OOO0000 =requests .request ('get',f'{host}/assets/clovers',headers =O0O000O0OO000O000 ).json ()#line:795
            if 'status'in O0OOOOO000OOO0000 :#line:797
                if O0OOOOO000OOO0000 ['status']==200 :#line:798
                    O0OOO00OO0OO0OOOO =O0OOOOO000OOO0000 ['data']['clover']#line:799
                    O000O00000OO00OO0 =O0OOOOO000OOO0000 ['data']['used_clover']#line:800
                    O0O00O000OO0OOO0O =float (O0OOO00OO0OO0OOOO )-float (O000O00000OO00OO0 )#line:801
                    print (f'【参与抽奖】:参与抽奖的☘️:{O000O00000OO00OO0}')#line:802
                    if O0O00O000OO0O0000 .certification ()!='未实名':#line:803
                        if O0O00O000OO0OOO0O >1 :#line:804
                            O00O00OOO0OOO0000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O00O000OO0OOO0O)}_{timi_new()}'#line:805
                            OOOO00O0OOOOO0000 ={'source':'scsc','authorization':O0O00O000OO0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OOO0OOO0000 ),'signstring':O00O00OOO0OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:816
                            O000OOO0OOOO0O00O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O00O000OO0OOO0O )}#line:817
                            OO0OO0O0O00O0000O =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOO00O0OOOOO0000 ,data =O000OOO0OOOO0O00O ).json ()#line:818
                            if 'status'in OO0OO0O0O00O0000O :#line:820
                                if OO0OO0O0O00O0000O ['status']==200 :#line:821
                                    print (f'【参与抽奖】:添加☘️:{OO0OO0O0O00O0000O["data"]}丨数量:{O0O00O000OO0OOO0O}')#line:822
                                if OO0OO0O0O00O0000O ['status']==500 :#line:823
                                    print (f'【参与抽奖】:添加☘️:{OO0OO0O0O00O0000O["message"]}')#line:824
            O0OO0OO0OO00OO0OO =requests .request ('get',f'{host}/lottery',headers =O0O000O0OO000O000 ).json ()#line:825
            OO0O00OO0O0O00000 =O0O00O000OO0O0000 .winning_rewards ()#line:827
            if 'status'in O0OO0OO0OO00OO0OO :#line:828
                if O0OO0OO0OO00OO0OO ['status']==200 :#line:829
                    O0OOOOOO0OOOOOO0O =O0OO0OO0OO00OO0OO ['data'][0 ]['day_get_gold_quantity']#line:830
                    golden_seed +=float (O0OOOOOO0OOOOOO0O )#line:831
                    O0O0000OOOOOO0OO0 =O0OO0OO0OO00OO0OO ['data'][1 ]['value']#line:832
                    OO0OOO0OO0O0O0O00 =O0OO0OO0OO00OO0OO ['data'][0 ]['join_number']#line:833
                    O000000O00OO0OOO0 =int (float (O0OO0OO0OO00OO0OO ['data'][0 ]['totalValue']))#line:834
                    OOOO00OO0O0OO0OO0 =float (O0O0000OOOOOO0OO0 /O000000O00OO0OOO0 )*10000 #line:835
                    O00O00OO0OO00O00O =O000000O00OO0OOO0 /OO0OOO0OO0O0O0O00 #line:836
                    print (f'【参与抽奖】:预计每天中{str(O0OOOOOO0OOOOOO0O)[:6]}颗金种子丨好友收益:{str(OO0O00OO0O0O00000)[:6]}')#line:837
                    print (f'【抽奖统计】:每1万☘️中{str(OOOO00OO0O0OO0OO0)[:6]}颗金种子丨☘️人均:{str(O00O00OO0OO00O00O)[:7]}️')#line:838
        except Exception as O0000OO000O0000OO :#line:839
            print (O0000OO000O0000OO )#line:840
    def energy (O0OOO00OO0O0O00OO ):#line:844
        try :#line:845
            while True :#line:846
                O0O0OO000OO0O0OO0 =f'__{timi_new()}'#line:847
                OO00O0O0OOOOO0O00 ={'source':'scsc','authorization':O0OOO00OO0O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO000OO0O0OO0 ),'signstring':O0O0OO000OO0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:858
                O00000OOO00OO00OO =requests .request ('get',f'{host}/energy/general',headers =OO00O0O0OOOOO0O00 ).json ()#line:859
                if 'status'in O00000OOO00OO00OO :#line:861
                    if O00000OOO00OO00OO ['status']==200 :#line:862
                        O0000O0O00000OO0O =O00000OOO00OO00OO ['data']['ordinary_water']#line:863
                        O00O0O0OOO0OOO000 =O00000OOO00OO00OO ['data']['ordinary_fertilizer']#line:864
                        OO00O00O000O00O00 =O00000OOO00OO00OO ['data']['videoStatus']#line:865
                        O000OOOOOOO0OOOO0 =O00000OOO00OO00OO ['data']['waterVideoKey']#line:866
                        print (f'【我的营养】:肥料:{str(O00O0O0OOO0OOO000).split(".")[0]}丨水滴:{str(O0000O0O00000OO0O).split(".")[0]}')#line:867
                        if float (O00O0O0OOO0OOO000 )<96 :#line:868
                            if OO00O00O000O00O00 :#line:869
                                time .sleep (random .randint (160 ,180 )/10 )#line:870
                                OO0000000000OOO0O =99 -float (O00O0O0OOO0OOO000 )#line:871
                                OO0O000OO0OOOO00O ={"fertilizer":str (OO0000000000OOO0O ).split ('.')[0 ]}#line:872
                                O0O0OO0O0OO000O00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO00O0O0OOOOO0O00 ).json ()#line:873
                                if 'status'in O0O0OO0O0OO000O00 :#line:875
                                    if O0O0OO0O0OO000O00 ['status']==200 :#line:876
                                        print (f'【购买肥料】:看广告获取肥料:{O0O0OO0O0OO000O00["message"]}')#line:877
                                    if O0O0OO0O0OO000O00 ['status']==500 :#line:878
                                        print (f'【购买肥料】:看广告获取肥料:{O0O0OO0O0OO000O00["message"]}')#line:879
                                        break #line:880
                            if energy :#line:881
                                if float (O00O0O0OOO0OOO000 )<78 :#line:882
                                    OO0000000000OOO0O =80 -float (O00O0O0OOO0OOO000 )#line:883
                                    O0OO0O00O0OO0O00O =f'_fertilizer={int(OO0000000000OOO0O)}_{timi_new()}'#line:884
                                    O00O0O00OO00OOO00 ={'source':'scsc','authorization':O0OOO00OO0O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O0OO0O00O ),'signstring':O0OO0O00O0OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:895
                                    OO0OOO0OO0OO0O0O0 ={"fertilizer":int (OO0000000000OOO0O )}#line:896
                                    O00OOOO0OOOOOOOO0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O00O0O00OO00OOO00 ,data =OO0OOO0OO0OO0O0O0 ).json ()#line:897
                                    if 'status'in O00OOOO0OOOOOOOO0 :#line:899
                                        if O00OOOO0OOOOOOOO0 ['status']==200 :#line:900
                                            print (f'【购买肥料】:购买肥料:{O00OOOO0OOOOOOOO0["message"]}丨数量:{int(OO0000000000OOO0O)}')#line:901
                                        if O00OOOO0OOOOOOOO0 ['status']==500 :#line:902
                                            print (f'【购买肥料】:购买肥料:{O00OOOO0OOOOOOOO0["message"]}丨数量:{int(OO0000000000OOO0O)}')#line:903
                                            OOOOOOO00O00OOO0O =O00OOOO0OOOOOOOO0 ["message"].split ('-')[1 ]#line:904
                                            O0000OOOOO0OOO00O =f'__{timi_new()}'#line:905
                                            OO00OO0OOOO0O00O0 ={'source':'scsc','authorization':O0OOO00OO0O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOOO0OOO00O ),'signstring':O0000OOOOO0OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:916
                                            OO0OOO0000OOOOOO0 =requests .request ('get',f'{host}/user',headers =OO00OO0OOOO0O00O0 ).json ()#line:917
                                            if 'status'in OO0OOO0000OOOOOO0 :#line:918
                                                if OO0OOO0000OOOOOO0 ['status']==200 :#line:919
                                                    OOOO00O0O0OO00O00 =OO0OOO0000OOOOOO0 ['data']['inner_id']#line:920
                                                    if give_gold (OOOO00O0O0OO00O00 ,float (OOOOOOO00O00OOO0O )+1 ):#line:921
                                                        O0OOO00OO0O0O00OO .energy ()#line:922
                        if float (O0000O0O00000OO0O )<880 :#line:923
                            if O000OOOOOOO0OOOO0 :#line:924
                                time .sleep (random .randint (160 ,180 )/10 )#line:925
                                O00O0OO0O00OO0O0O =999 -float (O0000O0O00000OO0O )#line:926
                                O000O0O00O0O0O0OO ={"water":str (O00O0OO0O00OO0O0O ).split ('.')[0 ]}#line:927
                                OOO000O000OOO00O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO00O0O0OOOOO0O00 ).json ()#line:928
                                if 'status'in OOO000O000OOO00O0 :#line:930
                                    if OOO000O000OOO00O0 ['status']==200 :#line:931
                                        print (f'【购买水滴】:看广告获取水滴:{OOO000O000OOO00O0["message"]}')#line:932
                                    if OOO000O000OOO00O0 ['status']==500 :#line:933
                                        print (f'【购买水滴】:看广告获取水滴:{OOO000O000OOO00O0["message"]}')#line:934
                                        break #line:935
                            if energy :#line:936
                                if float (O0000O0O00000OO0O )<780 :#line:937
                                    O00O0OO0O00OO0O0O =800 -float (O0000O0O00000OO0O )#line:938
                                    OOO0OO00O0O00O000 =f'_water={int(O00O0OO0O00OO0O0O)}_{timi_new()}'#line:939
                                    O0OOOOOO0OOOO00OO ={'source':'scsc','authorization':O0OOO00OO0O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00O0O00O000 ),'signstring':OOO0OO00O0O00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:950
                                    OOO0OOO0O0O0O0OO0 ={"water":int (O00O0OO0O00OO0O0O )}#line:951
                                    O000O0OOO0O00O000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0OOOOOO0OOOO00OO ,data =OOO0OOO0O0O0O0OO0 ).json ()#line:953
                                    if 'status'in O000O0OOO0O00O000 :#line:955
                                        if O000O0OOO0O00O000 ['status']==200 :#line:956
                                            print (f'【购买水滴】:购买水滴:{O000O0OOO0O00O000["message"]}丨数量:{int(O00O0OO0O00OO0O0O)}')#line:957
                                        if O000O0OOO0O00O000 ['status']==500 :#line:958
                                            print (f'【购买水滴】:购买水滴:{O000O0OOO0O00O000["message"]}丨数量:{int(O00O0OO0O00OO0O0O)}')#line:959
                                            OOOOOOO00O00OOO0O =O000O0OOO0O00O000 ["message"].split ('-')[1 ]#line:960
                                            O0000OOOOO0OOO00O =f'__{timi_new()}'#line:961
                                            OO00OO0OOOO0O00O0 ={'source':'scsc','authorization':O0OOO00OO0O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOOO0OOO00O ),'signstring':O0000OOOOO0OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:972
                                            OO0OOO0000OOOOOO0 =requests .request ('get',f'{host}/user',headers =OO00OO0OOOO0O00O0 ).json ()#line:973
                                            if 'status'in OO0OOO0000OOOOOO0 :#line:974
                                                if OO0OOO0000OOOOOO0 ['status']==200 :#line:975
                                                    OOOO00O0O0OO00O00 =OO0OOO0000OOOOOO0 ['data']['inner_id']#line:976
                                                    if give_gold (OOOO00O0O0OO00O00 ,float (OOOOOOO00O00OOO0O )+1 ):#line:977
                                                        O0OOO00OO0O0O00OO .energy ()#line:978
                        break #line:979
        except Exception as O000000O0000OO000 :#line:981
            print (O000000O0000OO000 )#line:982
def bundled_def ():#line:984
    OO0000OOO0O0OOOO0 =['5570536','7750212','7911652','7911680','7805624']#line:985
    return OO0000OOO0O0OOOO0 [random .randint (0 ,len (OO0000OOO0O0OOOO0 )-1 )]#line:986
def version_of_the_validation ():#line:990
    return str ((84 -56 )/10 )#line:991
def gitee_validation ():#line:994
    try :#line:995
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:996
    except :#line:997
        sys .exit (0 )#line:998
def update_the_validation ():#line:1002
    try :#line:1003
        O00OOO0O0OO00O0O0 =gitee_validation ()#line:1004
        if version_of_the_validation ()<O00OOO0O0OO00O0O0 ['CityEarth']['edition']:#line:1005
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OOO0O0OO00O0O0["CityEarth"]["edition"]}   ❌')#line:1006
            print (f'更新内容=>>{O00OOO0O0OO00O0O0["CityEarth"]["content"]}   🎉')#line:1007
        else :#line:1008
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OOO0O0OO00O0O0["CityEarth"]["edition"]}   ✅')#line:1009
            print (f'更新内容=>> {O00OOO0O0OO00O0O0["CityEarth"]["content"]}   🎉')#line:1010
    except Exception as O0OO00O00OOO000O0 :#line:1011
        print (O0OO00O00OOO000O0 )#line:1012
def os_qinglong ():#line:1015
    if application in os .environ :#line:1016
        OOOO00OOOOO00000O =os .environ [application ].split ('\n')#line:1017
        if len (OOOO00OOOOO00000O )>0 :#line:1018
            return OOOO00OOOOO00000O #line:1019
        else :#line:1020
            print (f"{application}变量未启用")#line:1021
            print ('脚本退出')#line:1022
            sys .exit (1 )#line:1023
    else :#line:1024
        if token :#line:1025
            OOOO00OOOOO00000O =token .split ('\n')#line:1026
            if len (OOOO00OOOOO00000O )>0 :#line:1027
                return OOOO00OOOOO00000O #line:1028
        else :#line:1029
            print (f"内置变量为空")#line:1030
            print ('脚本结束')#line:1031
            sys .exit (0 )#line:1032
if __name__ =='__main__':#line:1037
    start ()#line:1038
