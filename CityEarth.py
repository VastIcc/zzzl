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
@ 版本  2.7
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
        OOOO0OOO00O00OO0O =os_qinglong ()#line:10
        print (f"==========共找到{len(OOOO0OOO00O00OO0O)}个账号==========")#line:11
        for O00O000OO0OOO000O in OOOO0OOO00O00OO0O :#line:12
            O0O0O00OO0OO0O00O =[]#line:13
            print (f"------------正在执行第{OOOO0OOO00O00OO0O.index(O00O000OO0OOO000O) + 1}个账号------------")#line:14
            OOOO00OOOO0O000O0 =CityEarth (O00O000OO0OOO000O ,O0O0O00OO0OO0O00O )#line:15
            def OO0000OOOOO0OO000 ():#line:17
                if OOOO00OOOO0O000O0 .base_info ():#line:19
                    OOOO00OOOO0O000O0 .sealing ()#line:21
                    OOOO00OOOO0O000O0 .invitenum ()#line:23
                    OOOO00OOOO0O000O0 .game_map ()#line:25
                    OOOO00OOOO0O000O0 .friends_invitation ()#line:27
                    OOOO00OOOO0O000O0 .energy ()#line:29
                    OOOO00OOOO0O000O0 .add_clover ()#line:31
                    OOOO00OOOO0O000O0 .propsraffle ()#line:33
                    OOOO00OOOO0O000O0 .synthetic ()#line:35
                    OOOO00OOOO0O000O0 .crops_illustrated ()#line:37
                    OOOO00OOOO0O000O0 .give_gold ()#line:39
                    OOOO00OOOO0O000O0 .withdraw ()#line:41
            O000OO0O0OO00O0O0 =threading .Thread (target =OO0000OOOOO0OO000 )#line:43
            O000OO0O0OO00O0O0 .start ()#line:44
            time .sleep (time_xx )#line:45
        print (f"------------正在处理推送通知------------")#line:46
        time .sleep (0.5 )#line:47
        OOOOO0O0OO00000OO =format_msg ()#line:48
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOOOO0O0OO00000OO +' ')#line:49
    except Exception as O000000000OO000OO :#line:50
        print (O000000000OO000OO )#line:51
def give_gold (O0O0OO00OOOO0OO00 ,O0O0000000OOOOOOO ):#line:54
        try :#line:55
            OOO00O00O000OOOOO =f'_doneeNo={O0O0OO00OOOO0OO00}&quantity={int(O0O0000000OOOOOOO)}_{timi_new()}'#line:56
            OOO00OOO0000O00OO ={'source':'scsc','authorization':os_qinglong ()[0 ].split ('&')[0 ],'timestamp':str (timi_new ()),'sign':sign (OOO00O00O000OOOOO ),'signstring':OOO00O00O000OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:67
            O00OOOOOO000O00O0 ={"quantity":int (O0O0000000OOOOOOO ),"doneeNo":O0O0OO00OOOO0OO00 }#line:71
            OOO00O0OOO00O0O0O =requests .request ('post',f'{host}/finance/give-gold',headers =OOO00OOO0000O00OO ,data =O00OOOOOO000O00O0 ).json ()#line:72
            if 'status'in OOO00O0OOO00O0O0O :#line:74
                if OOO00O0OOO00O0O0O ['status']==200 :#line:75
                    if OOO00O0OOO00O0O0O ['data']:#line:76
                        print (f'【赠送种子】:赠送{int(O0O0000000OOOOOOO)}种子给{O0O0OO00OOOO0OO00}成功')#line:77
                if OOO00O0OOO00O0O0O ['status']==401 :#line:78
                    print (f'【赠送种子】:{OOO00O0OOO00O0O0O["message"]}')#line:79
                if OOO00O0OOO00O0O0O ['status']==500 :#line:80
                    print (f'【赠送种子】:{OOO00O0OOO00O0O0O["message"]}')#line:81
        except Exception as OOO0OO0O0OOO0OO0O :#line:82
            print (OOO0OO0O0OOO0OO0O )#line:83
def sign (OOOOOOOO0OO0O0OOO ):#line:86
    O00O0000O00OO0O0O =hashlib .md5 (OOOOOOOO0OO0O0OOO .encode ()).hexdigest ()#line:87
    OOOOOO0OOOOO0O000 ="scsc%^&*"+O00O0000O00OO0O0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:88
    OOOOO0OOO0OOO0O0O =hashlib .md5 (OOOOOO0OOOOO0O000 .encode ()).hexdigest ()#line:89
    return OOOOO0OOO0OOO0O0O #line:90
def format_msg ():#line:92
    OO00O00O00OOOO00O =""#line:93
    for OO0OOO0OO0000O0OO in msg_list :#line:94
        OO00O00O00OOOO00O +=str (OO0OOO0OO0000O0OO )+"\r\n"#line:95
    return OO00O00O00OOOO00O #line:96
def timi_new ():#line:98
    return str (int (time .time ()*1000 ))#line:99
class CityEarth :#line:102
    def __init__ (OO0O00OO0OOO0OO00 ,O000O00O00000O00O ,O000OOOOO0OO00O0O ):#line:104
        try :#line:105
            OO0O00OO0OOO0OO00 .msg =O000OOOOO0OO00O0O #line:106
            OO0O00OO0OOO0OO00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:107
            OO0O00OO0OOO0OO00 .token =O000O00O00000O00O .split ('&')[0 ]#line:108
            OO0O00OO0OOO0OO00 .innerId =O000O00O00000O00O .split ('&')[1 ]#line:109
            OO0O00OO0OOO0OO00 .doneeNo =O000O00O00000O00O .split ('&')[2 ]#line:110
        except :#line:111
            print ('变量格式错误')#line:112
    def base_info (O00O0O0000OOO0O00 ):#line:115
        try :#line:116
            O00O0O0000OOO0O00 .watched_ad ()#line:118
            O000OOOO0O0OO00OO =f'__{timi_new()}'#line:119
            OOOO00000O0000O0O ={'source':'scsc','authorization':O00O0O0000OOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOO0O0OO00OO ),'signstring':O000OOOO0O0OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:130
            O0OOOO0O0O00OOO0O =requests .request ('get',f'{host}/user',headers =OOOO00000O0000O0O ).json ()#line:131
            if 'status'in O0OOOO0O0O00OOO0O :#line:133
                if O0OOOO0O0O00OOO0O ['status']==200 :#line:134
                    OOO0000OOO0OOOO00 =O0OOOO0O0O00OOO0O ['data']['nickname']#line:135
                    OO0000O0OOO000000 =O0OOOO0O0O00OOO0O ['data']['inner_id']#line:136
                    O0O00OOOO0OO0O000 =O0OOOO0O0O00OOO0O ['data']['assets']['gold']#line:137
                    OO000OOOO00OO00O0 =O0OOOO0O0O00OOO0O ['data']['level']#line:138
                    print (f'【账号信息】:昵称:{OOO0000OOO0OOOO00[:5]}丨ID:{OO0000O0OOO000000}丨等级:{OO000OOOO00OO00O0}丨金种子:{str(O0O00OOOO0OO0O000).split(".")[0]}')#line:139
                if O0OOOO0O0O00OOO0O ['status']==401 :#line:140
                    print (O0OOOO0O0O00OOO0O ['message'])#line:141
                    O00O0O0000OOO0O00 .msg .append ('有账号失效了')#line:142
                    return False #line:143
                if O0OOOO0O0O00OOO0O ['status']==500 :#line:144
                    return False #line:145
            return True #line:146
        except Exception as O000OO000OO0O0OOO :#line:147
            print (O000OO000OO0O0OOO )#line:148
    def sealing (OOO0O0O0OO0OOOO0O ):#line:151
        try :#line:152
            O0O0O0O0O0O0O0000 =f'__{timi_new()}'#line:153
            OOO000OO0O0OO00OO ={'source':'scsc','authorization':OOO0O0O0OO0OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0O0O0O0000 ),'signstring':O0O0O0O0O0O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:164
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO000OO0O0OO00OO )#line:165
            requests .request ('get',f'{host}/packsack/list',headers =OOO000OO0O0OO00OO )#line:166
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO000OO0O0OO00OO )#line:167
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO000OO0O0OO00OO )#line:168
            requests .request ('get',f'{host}/user',headers =OOO000OO0O0OO00OO )#line:169
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO000OO0O0OO00OO )#line:170
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO000OO0O0OO00OO )#line:171
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO000OO0O0OO00OO )#line:172
            requests .request ('get',f'{host}/game/getAllData',headers =OOO000OO0O0OO00OO )#line:173
            requests .request ('get',f'{host}/assets',headers =OOO000OO0O0OO00OO )#line:174
        except Exception as OO00OO0O0OO00O00O :#line:175
            print (OO00OO0O0OO00O00O )#line:176
    def withdraw (OOO00OOOOOOOOO0O0 ):#line:180
        O0O0OOOOO0O0OO00O =f'__{timi_new()}'#line:181
        O00000000O0OO00O0 ={'source':'scsc','authorization':OOO00OOOOOOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOOO0O0OO00O ),'signstring':O0O0OOOOO0O0OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:192
        OO0O0O0OOO00000OO =requests .request ('get',f'{host}/assets',headers =O00000000O0OO00O0 ).json ()#line:193
        if 'status'in OO0O0O0OOO00000OO :#line:195
            if OO0O0O0OOO00000OO ['status']==200 :#line:196
                OOOO00OOO00OOO000 =OO0O0O0OOO00000OO ['data']['cash']#line:197
                if float (OOOO00OOO00OOO000 )>20 :#line:198
                    O0O0OOOOO0O0OO00O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:199
                    O00000000O0OO00O0 ={'authorization':OOO00OOOOOOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOOO0O0OO00O ),'signstring':O0O0OOOOO0O0OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:209
                    O000O000O0000000O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:210
                    OOOO0O000O000O0OO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00000000O0OO00O0 ,data =O000O000O0000000O ).json ()#line:212
                    print (OOOO0O000O000O0OO )#line:213
    def invitenum (OO0O00O0OO0O0OOOO ):#line:216
        O0OO0OO00O0O00000 =f'__{timi_new()}'#line:217
        O0OOOO0000O0OOO0O ={'source':'scsc','authorization':OO0O00O0OO0O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO00O0O00000 ),'signstring':O0OO0OO00O0O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:228
        OO0O00O0000O000O0 =requests .request ('get',f'{host}/invite/invitenum',headers =O0OOOO0000O0OOO0O ).json ()#line:229
        if 'status'in OO0O00O0000O000O0 :#line:231
            if OO0O00O0000O000O0 ['status']==200 :#line:232
                O00OOO0O00000OO00 =OO0O00O0000O000O0 ['data']['invited_count']#line:233
                OOOOO0OOO000OOOOO =OO0O00O0000O000O0 ['data']['invited_second_count']#line:234
                print (f'【我的邀请】:直邀好友:{O00OOO0O00000OO00}丨间邀好友:{OOOOO0OOO000OOOOO}')#line:235
    def game_map (O0O0OOOOO000O0OO0 ):#line:238
        try :#line:239
            O00O00O0OOO00O000 =f'__{timi_new()}'#line:240
            O00O000OO00OO0OOO ={'source':'scsc','authorization':O0O0OOOOO000O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0OOO00O000 ),'signstring':O00O00O0OOO00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:251
            OO0OO000O00OOOO0O =requests .request ('get',f'{host}/game/map',headers =O00O000OO00OO0OOO ).json ()#line:252
            if 'status'in OO0OO000O00OOOO0O :#line:254
                if OO0OO000O00OOOO0O ['status']==200 :#line:255
                    for OOOOOO00O0OOOO0O0 in OO0OO000O00OOOO0O ['data']['list'][0 ]['crops']:#line:256
                        OOOOO0O0O000OOOO0 =OOOOOO00O0OOOO0O0 ['level']#line:258
                        if OOOOO0O0O000OOOO0 ==41 :#line:259
                            O0000OO0OOO0OO0OO =OOOOOO00O0OOOO0O0 ['crop_name']#line:260
                            O0O0O000OO00O0O00 =OOOOOO00O0OOOO0O0 ['count']#line:261
                            if O0O0O000OO00O0O00 >0 :#line:262
                                print (f'【农业资产】:{O0000OO0OOO0OO0OO}丨数量:{O0O0O000OO00O0O00}')#line:263
        except Exception as OOOOO00O00OO00O00 :#line:264
            print (OOOOO00O00OO00O00 )#line:265
    def give_gold (O0OOOO000OO00O000 ):#line:268
        try :#line:269
            OO00O0OO00OOOOOO0 =f'__{timi_new()}'#line:270
            OOOOOO0O00OO00OO0 ={'source':'scsc','authorization':O0OOOO000OO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OO00OOOOOO0 ),'signstring':OO00O0OO00OOOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:281
            OO00O0O0OO0O00OOO =requests .request ('get',f'{host}/user',headers =OOOOOO0O00OO00OO0 ).json ()#line:282
            if 'status'in OO00O0O0OO0O00OOO :#line:283
                if OO00O0O0OO0O00OOO ['status']==200 :#line:284
                    if float (O0OOOO000OO00O000 .doneeNo )!=0 :#line:285
                        O00OO0O00O000O0OO =OO00O0O0OO0O00OOO ['data']['assets']['gold']#line:286
                        if float (O00OO0O00O000O0OO )>float (O0OOOO000OO00O000 .innerId ):#line:287
                            O000OO0OOOO00OOOO =int (float (O00OO0O00O000O0OO )/1.1 )#line:288
                            OO00O0OO00OOOOOO0 =f'_doneeNo={O0OOOO000OO00O000.doneeNo}&quantity={O000OO0OOOO00OOOO}_{timi_new()}'#line:289
                            OOOOOO0O00OO00OO0 ={'source':'scsc','authorization':O0OOOO000OO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OO00OOOOOO0 ),'signstring':OO00O0OO00OOOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:300
                            O000000000O000OO0 ={"quantity":O000OO0OOOO00OOOO ,"doneeNo":O0OOOO000OO00O000 .doneeNo }#line:304
                            O0OOO0OO00000OOOO =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOOO0O00OO00OO0 ,data =O000000000O000OO0 ).json ()#line:305
                            if 'status'in O0OOO0OO00000OOOO :#line:307
                                if O0OOO0OO00000OOOO ['status']==200 :#line:308
                                    if O0OOO0OO00000OOOO ['data']:#line:309
                                        print (f'【赠送种子】:赠送{O000OO0OOOO00OOOO}种子给{O0OOOO000OO00O000.doneeNo}成功')#line:310
                    else :#line:311
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:312
        except Exception as OOO0OOO000O00000O :#line:313
            print (OOO0OOO000O00000O )#line:314
    def invitation (OOOO0OOO0O0OO000O ):#line:316
        try :#line:317
            _OO0O00OO000OOO000 =float (bundled_def ())/4 #line:318
            O0O0O00O0OO0OOOO0 =f'_innerId={int(_OO0O00OO000OOO000)}_{timi_new()}'#line:319
            OO0OO00OO00000O0O ={'source':'scsc','authorization':OOOO0OOO0O0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00O0OO0OOOO0 ),'signstring':O0O0O00O0OO0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:330
            OOO0O0O00O00O00O0 ={"innerId":int (_OO0O00OO000OOO000 )}#line:331
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO0OO00OO00000O0O ,data =OOO0O0O00O00O00O0 )#line:332
        except Exception as O00000O0OO0OO0OO0 :#line:333
            print (O00000O0OO0OO0OO0 )#line:334
    def winning_rewards (O0OO00O00OO0O0OOO ):#line:337
        try :#line:338
            OO00OOO0OOO00OOO0 =f'__{timi_new()}'#line:339
            OO0000O0OOOOO0OO0 ={'source':'scsc','authorization':O0OO00O00OO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO0OOO00OOO0 ),'signstring':OO00OOO0OOO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
            OOOOOO0O000OOOO00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO0000O0OOOOO0OO0 ).json ()#line:351
            if 'status'in OOOOOO0O000OOOO00 :#line:353
                if OOOOOO0O000OOOO00 ['status']==200 :#line:354
                    if OOOOOO0O000OOOO00 ['data']['amount']:#line:355
                        OOOO00OOOO0OO0OO0 =OOOOOO0O000OOOO00 ['data']['amount']['gold']#line:356
                        return OOOO00OOOO0OO0OO0 #line:357
                    else :#line:358
                        return 0 #line:359
        except Exception as O0OO0O00OOO00O0OO :#line:360
            print (O0OO0O00OOO00O0OO )#line:361
    def certification (O00000000O0O0000O ):#line:364
        try :#line:365
            OO000000OO0O00OOO =f'__{timi_new()}'#line:366
            OOOO0O000O0O000OO ={'source':'scsc','authorization':O00000000O0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000OO0O00OOO ),'signstring':OO000000OO0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:377
            O00OO0OO00O00OO0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOOO0O000O0O000OO ).json ()#line:378
            if 'status'in O00OO0OO00O00OO0O :#line:380
                if O00OO0OO00O00OO0O ['status']==200 :#line:381
                    if O00OO0OO00O00OO0O ['data']['result']:#line:382
                        O0OOOOO0O0000O00O =O00OO0OO00O00OO0O ['data']['nick_name']#line:383
                        return O0OOOOO0O0000O00O #line:384
                    else :#line:385
                        return '未实名'#line:386
        except Exception as O00OO0O0OO0O000OO :#line:387
            print (O00OO0O0OO0O000OO )#line:388
    def crops_illustrated (O0OO000000O0O0O0O ):#line:391
        try :#line:392
            O0OO0000O00O0O00O =f'__{timi_new()}'#line:393
            OO0OO00OO000000O0 ={'source':'scsc','authorization':O0OO000000O0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0000O00O0O00O ),'signstring':O0OO0000O00O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:404
            O0O00O0000OOO0O00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0OO00OO000000O0 ).json ()#line:405
            if 'status'in O0O00O0000OOO0O00 :#line:407
                if O0O00O0000OOO0O00 ['status']==200 :#line:408
                    OOO00000O000OOOO0 =O0O00O0000OOO0O00 ['data'][0 ]['crops']#line:409
                    for O0000OO0000OOO0O0 in OOO00000O000OOOO0 :#line:410
                        if O0000OO0000OOO0O0 ['ill_clover_award']:#line:411
                            if float (O0000OO0000OOO0O0 ['ill_clover_award'])>1 :#line:412
                                if O0000OO0000OOO0O0 ['is_finish']:#line:413
                                    if not O0000OO0000OOO0O0 ['is_getit']:#line:414
                                        if O0OO000000O0O0O0O .certification ()!='未实名':#line:415
                                            O0OO0000O00O0O00O =f'_award_level={O0000OO0000OOO0O0["level"]}_{timi_new()}'#line:416
                                            OO0OO00OO000000O0 ={'source':'scsc','authorization':O0OO000000O0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0000O00O0O00O ),'signstring':O0OO0000O00O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:427
                                            O0OOOO00O00000OOO ={"award_level":O0000OO0000OOO0O0 ['level']}#line:428
                                            O0O000O00O00OO0O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0OO00OO000000O0 ,json =O0OOOO00O00000OOO ).json ()#line:430
                                            if 'status'in O0O000O00O00OO0O0 :#line:431
                                                if O0O000O00O00OO0O0 ['status']==200 :#line:432
                                                    OO000O000OO00OO00 =O0O000O00O00OO0O0 ['data']['ill_clover_award']#line:433
                                                    print (f'【图鉴奖励】:领取{O0000OO0000OOO0O0["crop_name"]}成就丨奖励{OO000O000OO00OO00}☘️')#line:435
                                                if O0O000O00O00OO0O0 ['status']==500 :#line:436
                                                    print (f'【图鉴奖励】:{O0O000O00O00OO0O0["message"]}')#line:437
        except Exception as OO0OO00000O0OOO0O :#line:438
            print (OO0OO00000O0OOO0O )#line:439
    def watched_ad (O0000000O0O0OO000 ):#line:442
        try :#line:443
            OOO000OO00O000000 =f'__{timi_new()}'#line:444
            O000O0OOOOOO0O000 ={'source':'scsc','authorization':O0000000O0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO00O000000 ),'signstring':OOO000OO00O000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:455
            O00O00OOOOOOO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =O000O0OOOOOO0O000 ).json ()#line:456
            if 'status'in O00O00OOOOOOO0O0O :#line:458
                if O00O00OOOOOOO0O0O ['status']==200 :#line:459
                    if 'offlineInfo'in O00O00OOOOOOO0O0O ['data']:#line:460
                        time .sleep (random .randint (3 ,5 ))#line:461
                        O0O0O00O0000000O0 =O00O00OOOOOOO0O0O ['data']['offlineInfo']['off_minute']#line:462
                        OOOO0OOO000000O00 =float (O00O00OOOOOOO0O0O ['data']['silver'])/1000000000000 #line:463
                        time .sleep (1 )#line:464
                        requests .request ('post',f'{host}/game/watched-ad',headers =O000O0OOOOOO0O000 ).json ()#line:465
                        time .sleep (2 )#line:466
                        O000OOO0OOOO0OO0O =requests .request ('get',f'{host}/game/getAllData',headers =O000O0OOOOOO0O000 ).json ()#line:467
                        if 'status'in O000OOO0OOOO0OO0O :#line:469
                            if O000OOO0OOOO0OO0O ['status']==200 :#line:470
                                OOOO000OO0000OO0O =float (O000OOO0OOOO0OO0O ['data']['silver'])/1000000000000 #line:471
                                O00O000O000OO0O00 =str (OOOO000OO0000OO0O -OOOO0OOO000000O00 )[:6 ]#line:472
                                print (f'【离线奖励】:翻倍离线{O0O0O00O0000000O0}分钟奖励🌱数量:{O00O000O000OO0O00}t粒')#line:473
        except Exception as O000O00OO000OOOO0 :#line:474
            print (O000O00OO000OOOO0 )#line:475
    def user_ad (O00O00000OO00OO0O ):#line:478
        try :#line:479
            OOOOOO00O0000O000 =f'__{timi_new()}'#line:480
            OO000OO000000O0OO ={'source':'scsc','authorization':O00O00000OO00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00O0000O000 ),'signstring':OOOOOO00O0000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:491
            O0O000O0O0OO0OO00 =requests .request ('get',f'{host}/user/ad',headers =OO000OO000000O0OO ).json ()#line:492
            if 'status'in O0O000O0O0OO0OO00 :#line:494
                if O0O000O0O0OO0OO00 ['status']==200 :#line:495
                    OO0O0OO00O0OO0OOO =O0O000O0O0OO0OO00 ['data']['max_time']#line:496
                    O000OOOO0OOO00O00 =O0O000O0O0OO0OO00 ['data']['watch_time']#line:497
                    OOO0OOO00O0OOO0O0 =O0O000O0O0OO0OO00 ['data']['added_time']#line:498
                    print (f'【获取种子】:获取🌱剩余{OOO0OOO00O0OOO0O0 + OO0O0OO00O0OO0OOO - O000OOOO0OOO00O00}次丨好友提供:{OOO0OOO00O0OOO0O0}次')#line:499
                    if OOO0OOO00O0OOO0O0 +OO0O0OO00O0OO0OOO -O000OOOO0OOO00O00 >0 :#line:500
                        time .sleep (random .randint (16 ,19 ))#line:501
                        OO000OOO000000OO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO000OO000000O0OO ).json ()#line:502
                        if 'status'in OO000OOO000000OO0 :#line:504
                            if OO000OOO000000OO0 ['status']==200 :#line:505
                                O00O00OOO0O0O0OO0 =float (OO000OOO000000OO0 ['data']['silver'])/1000000000000 #line:506
                                print (f'【获取种子】:获得🌱:{int(O00O00OOO0O0O0OO0)}t粒')#line:507
                                return True #line:508
                            if OO000OOO000000OO0 ['status']==500 :#line:509
                                O0O00O00O00OOOOO0 =OO000OOO000000OO0 ['message']#line:510
                                print (f'【获取种子】:{O0O00O00O00OOOOO0}')#line:511
                                return False #line:512
        except Exception as OO0OO0000000OOO00 :#line:513
            print (OO0OO0000000OOO00 )#line:514
    def synthetic (O0000OO0000OOOOOO ):#line:517
        global id ,g #line:518
        try :#line:519
            OO0OO0O0O00O0000O =O0000OO0000OOOOOO .level_new ()#line:520
            O0O000OOOO00O0O00 =random .randint (9 ,11 )#line:521
            O0OO0000000O0OO00 =f'_site=8&targetSite={O0O000OOOO00O0O00}_{timi_new()}'#line:522
            O0OO00OO00OOO0000 ={'source':'scsc','authorization':O0000OO0000OOOOOO .token ,'timestamp':timi_new (),'sign':sign (O0OO0000000O0OO00 ),'signstring':O0OO0000000O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:533
            O0O0O0OO0000O0OO0 ={"site":int (8 ),"targetSite":int (O0O000OOOO00O0O00 )}#line:534
            requests .request ('post',f'{host}/game/crops/move',headers =O0OO00OO00OOO0000 ,json =O0O0O0OO0000O0OO0 )#line:535
            while True :#line:536
                O0OO00O000OOOO000 =f'__{timi_new()}'#line:537
                OOOOOOO0O0OOO0O00 ={'source':'scsc','authorization':O0000OO0000OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O000OOOO000 ),'signstring':O0OO00O000OOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:548
                O0OOO0000OO0O0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOOOOOO0O0OOO0O00 ).json ()#line:549
                if 'status'in O0OOO0000OO0O0OO0 :#line:551
                    if O0OOO0000OO0O0OO0 ['status']==200 :#line:552
                        OOO00000O000O0000 =O0OOO0000OO0O0OO0 ['data']['cropList']#line:553
                        OO0000OO00O0O00O0 =O0OOO0000OO0O0OO0 ['data']['gameCoreDataDBid']#line:554
                        OOOOOOO0000O00000 =float (O0OOO0000OO0O0OO0 ['data']['silver'])/1000000000000 #line:555
                        O000OO0OOOOO0O0O0 =0 #line:560
                        for O00OOOO0O0O000OO0 in OOO00000O000O0000 :#line:561
                            if not O00OOOO0O0O000OO0 :#line:562
                                OOO0O0OOOOO000O0O =f'_crop_id={OO0000OO00O0O00O0}&site={O000OO0OOOOO0O0O0}_{O0000OO0000OOOOOO.time}'#line:563
                                O0O0OOOOO000O000O ={'source':'scsc','authorization':O0000OO0000OOOOOO .token ,'timestamp':O0000OO0000OOOOOO .time ,'sign':sign (OOO0O0OOOOO000O0O ),'signstring':OOO0O0OOOOO000O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:573
                                OOO00O0O0O00OOO00 ={"site":O000OO0OOOOO0O0O0 ,"crop_id":OO0000OO00O0O00O0 }#line:574
                                O0OOOOO0000000000 =requests .request ('post',f'{host}/game/crops/buy',headers =O0O0OOOOO000O000O ,data =OOO00O0O0O00OOO00 ).json ()#line:575
                                time .sleep (random .randint (1 ,3 )/10 )#line:577
                                if 'status'in O0OOOOO0000000000 :#line:578
                                    if O0OOOOO0000000000 ['status']==200 :#line:579
                                        if O0OOOOO0000000000 ['message']=='种子数量不足':#line:580
                                            OO0OO0O0O00O0000O =O0000OO0000OOOOOO .level_new ()#line:581
                                            print (f'【种植合成】:{O0OOOOO0000000000["message"]}')#line:582
                                            if not O0000OO0000OOOOOO .user_ad ():#line:583
                                                return False #line:584
                                    if O0OOOOO0000000000 ['status']==500 :#line:585
                                        print (f'【种植合成】:{O0OOOOO0000000000["message"]}')#line:586
                                        return False #line:587
                            O000OO0OOOOO0O0O0 +=1 #line:588
                        OO0O0O00OO0O0OOOO =requests .request ('get',f'{host}/game/getAllData',headers =OOOOOOO0O0OOO0O00 ).json ()#line:589
                        OO00O0OOO0OO0OOOO =OO0O0O00OO0O0OOOO ['data']['cropList']#line:590
                        OOO0OOOOO00OO0O00 =False #line:591
                        for O00OOOO0O0O000OO0 in range (12 ):#line:592
                            id =OO00O0OOO0OO0OOOO [O00OOOO0O0O000OO0 ]['level']#line:593
                            if float (OO0OO0O0O00O0000O )-float (id )>9 :#line:594
                                OOO0OOOO0OOOOOO0O =f'_site={O00OOOO0O0O000OO0}_{timi_new()}'#line:595
                                OOOOO0O0O0O00OO00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0000OO0000OOOOOO .token ,'timestamp':timi_new (),'sign':sign (OOO0OOOO0OOOOOO0O ),'signstring':OOO0OOOO0OOOOOO0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:606
                                OOO0OOOO0OOO0O0O0 ={"site":O00OOOO0O0O000OO0 }#line:607
                                OO0000OOO0O0OOO00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOOO0O0O0O00OO00 ,data =OOO0OOOO0OOO0O0O0 ).json ()#line:609
                                if 'status'in OO0000OOO0O0OOO00 :#line:610
                                    if OO0000OOO0O0OOO00 ['status']==200 :#line:611
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:612
                            if id !=0 :#line:613
                                for OOO00O00O0OO0OOOO in range (11 ):#line:614
                                    OO00O0OO0OOO00OOO =OOO00O00O0OO0OOOO +1 #line:615
                                    g =OO00O0OOO0OO0OOOO [OO00O0OO0OOO00OOO ]['level']#line:616
                                    if id ==g :#line:617
                                        OOO0OO00O000OO000 =OOO00O00O0OO0OOOO +2 #line:618
                                        if OOO0OO00O000OO000 !=O00OOOO0O0O000OO0 +1 :#line:619
                                            OOO000O0OOO0OOOOO =O00OOOO0O0O000OO0 +1 #line:620
                                            time .sleep (random .randint (1 ,3 )/10 )#line:622
                                            O0OO0000000O0OO00 =f'_site={OOO000O0OOO0OOOOO - 1}&targetSite={OOO0OO00O000OO000 - 1}_{timi_new()}'#line:623
                                            O0OO00OO00OOO0000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0000OO0000OOOOOO .token ,'timestamp':timi_new (),'sign':sign (O0OO0000000O0OO00 ),'signstring':O0OO0000000O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:640
                                            O00OO00OO0OOOO000 ={"site":int (OOO000O0OOO0OOOOO -1 ),"targetSite":int (OOO0OO00O000OO000 -1 )}#line:641
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0OO00OO00OOO0000 ,json =O00OO00OO0OOOO000 )#line:642
                                            OOO0OOOOO00OO0O00 =True #line:644
                                    if OOO0OOOOO00OO0O00 :#line:645
                                        break #line:646
                                if OOO0OOOOO00OO0O00 :#line:647
                                    break #line:648
        except :#line:649
            O0000OO0000OOOOOO .synthetic ()#line:650
    def level_new (OO0O00O0O0OOOOO0O ):#line:653
        try :#line:654
            O0OOO00O0000O0O0O =f'__{timi_new()}'#line:655
            OO00OOO000000O0OO ={'source':'scsc','authorization':OO0O00O0O0OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0000O0O0O ),'signstring':O0OOO00O0000O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:666
            O000OOO000O00OOO0 =requests .request ('get',f'{host}/user',headers =OO00OOO000000O0OO ).json ()#line:667
            if 'status'in O000OOO000O00OOO0 :#line:668
                if O000OOO000O00OOO0 ['status']==200 :#line:669
                    return float (O000OOO000O00OOO0 ['data']['level'])#line:670
        except Exception as OOO000OOO0000OOO0 :#line:671
            print (OOO000OOO0000OOO0 )#line:672
    def propsraffle (OO0OOO0O000O00O00 ):#line:675
        try :#line:676
            while True :#line:677
                O00O000000000OOO0 =f'__{timi_new()}'#line:678
                O000OO00000OOO00O ={'source':'scsc','authorization':OO0OOO0O000O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000000000OOO0 ),'signstring':O00O000000000OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:689
                O000O00O0O0000OO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O000OO00000OOO00O ).json ()#line:690
                if 'status'in O000O00O0O0000OO0 :#line:692
                    if O000O00O0O0000OO0 ['status']==200 :#line:693
                        OO0000O00O0O000O0 =O000O00O0O0000OO0 ['data']['rows']#line:694
                        O0O00OO0OO0O00000 =O000O00O0O0000OO0 ['data']['vstate']#line:695
                        if OO0000O00O0O000O0 ==5 or OO0000O00O0O000O0 ==6 or OO0000O00O0O000O0 ==7 :#line:696
                            OO00O00OOO0O0O000 =O000O00O0O0000OO0 ['data']['silver']#line:697
                            print (f'【转盘抽奖】:获得种子:{OO00O00OOO0O0O000}')#line:698
                        if OO0000O00O0O000O0 ==1 or OO0000O00O0O000O0 ==2 or OO0000O00O0O000O0 ==3 :#line:699
                            OOOOO00OOO00O0O0O =O000O00O0O0000OO0 ['data']['clover']#line:700
                            print (f'【转盘抽奖】:获得三叶草:{OOOOO00OOO00O0O0O}')#line:701
                        if OO0000O00O0O000O0 ==4 or OO0000O00O0O000O0 ==8 :#line:702
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:703
                        if OO0000O00O0O000O0 =='抽奖次数已用完':#line:707
                            break #line:741
                time .sleep (random .randint (8 ,15 )/10 )#line:742
        except Exception as OOOOO0OOOOOOOO00O :#line:743
            print (OOOOO0OOOOOOOO00O )#line:744
    def friends_invitation (OOO0OO0O00O000O0O ):#line:747
        try :#line:748
            OO00O000OO0O0OO00 =f'__{timi_new()}'#line:749
            OO0OOO00O000O0OOO ={'source':'scsc','authorization':OOO0OO0O00O000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000OO0O0OO00 ),'signstring':OO00O000OO0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:760
            O0O0O0OO00OOO0O00 =requests .request ('get',f'{host}/friends',headers =OO0OOO00O000O0OOO ).json ()#line:761
            if 'status'in O0O0O0OO00OOO0O00 :#line:762
                if O0O0O0OO00OOO0O00 ['status']==200 :#line:763
                    OO0OO0O0000O0OOOO =O0O0O0OO00OOO0O00 ['data']['myInviteter']#line:764
                    if OO0OO0O0000O0OOOO :#line:765
                        OO0O0OO0O000OO0O0 =OO0OO0O0000O0OOOO ['user']['nickname']#line:766
                        O0O0OO0OO00O0O0OO =OOO0OO0O00O000O0O .certification ()#line:767
                        print (f'【查邀请人】:我的邀请人:{OO0O0OO0O000OO0O0}丨实名:{O0O0OO0OO00O0O0OO}')#line:768
                    else :#line:769
                        if OOO0OO0O00O000O0O .innerId !='0':#line:770
                            OOO0OO0O00O000O0O .invitation ()#line:771
        except Exception as O0OO000OO00O0OOO0 :#line:772
            print (O0OO000OO00O0OOO0 )#line:773
    def add_clover (O00OOOOO0OO0000O0 ):#line:776
        global golden_seed #line:777
        try :#line:778
            OOO0OO0OOO000OO0O =f'__{timi_new()}'#line:779
            OO00OOO0OOOOO00OO ={'source':'scsc','authorization':O00OOOOO0OO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OOO000OO0O ),'signstring':OOO0OO0OOO000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:790
            O00OO00O0O000O0OO =requests .request ('get',f'{host}/assets/clovers',headers =OO00OOO0OOOOO00OO ).json ()#line:791
            if 'status'in O00OO00O0O000O0OO :#line:793
                if O00OO00O0O000O0OO ['status']==200 :#line:794
                    OO000O0O00OOOOO00 =O00OO00O0O000O0OO ['data']['clover']#line:795
                    O0O0O0O0000OO0OO0 =O00OO00O0O000O0OO ['data']['used_clover']#line:796
                    OOOO0OO000OOOO0O0 =float (OO000O0O00OOOOO00 )-float (O0O0O0O0000OO0OO0 )#line:797
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0O0O0O0000OO0OO0}')#line:798
                    if O00OOOOO0OO0000O0 .certification ()!='未实名':#line:799
                        if OOOO0OO000OOOO0O0 >1 :#line:800
                            OOO0OO0OOO000OO0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOO0OO000OOOO0O0)}_{timi_new()}'#line:801
                            O0OO0O0000O000OO0 ={'source':'scsc','authorization':O00OOOOO0OO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OOO000OO0O ),'signstring':OOO0OO0OOO000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:812
                            OOO0000O00O0O0OOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOO0OO000OOOO0O0 )}#line:813
                            OOOO0OO00OO0O000O =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OO0O0000O000OO0 ,data =OOO0000O00O0O0OOO ).json ()#line:814
                            if 'status'in OOOO0OO00OO0O000O :#line:816
                                if OOOO0OO00OO0O000O ['status']==200 :#line:817
                                    print (f'【参与抽奖】:添加☘️:{OOOO0OO00OO0O000O["data"]}丨数量:{OOOO0OO000OOOO0O0}')#line:818
                                if OOOO0OO00OO0O000O ['status']==500 :#line:819
                                    print (f'【参与抽奖】:添加☘️:{OOOO0OO00OO0O000O["message"]}')#line:820
            O0OOOO00000O0O0OO =requests .request ('get',f'{host}/lottery',headers =OO00OOO0OOOOO00OO ).json ()#line:821
            O0O00O0OOO00OO000 =O00OOOOO0OO0000O0 .winning_rewards ()#line:823
            if 'status'in O0OOOO00000O0O0OO :#line:824
                if O0OOOO00000O0O0OO ['status']==200 :#line:825
                    O0O00O00O0OO0OOO0 =O0OOOO00000O0O0OO ['data'][0 ]['day_get_gold_quantity']#line:826
                    golden_seed +=float (O0O00O00O0OO0OOO0 )#line:827
                    O00OOO0O0OOO0O00O =O0OOOO00000O0O0OO ['data'][1 ]['value']#line:828
                    O0OOOOO0OOOO00OOO =O0OOOO00000O0O0OO ['data'][0 ]['join_number']#line:829
                    OOOO00O000OO0O0OO =int (float (O0OOOO00000O0O0OO ['data'][0 ]['totalValue']))#line:830
                    OO0OO00O000OOO000 =float (O00OOO0O0OOO0O00O /OOOO00O000OO0O0OO )*10000 #line:831
                    OO0O0OO0O0OO0O0OO =OOOO00O000OO0O0OO /O0OOOOO0OOOO00OOO #line:832
                    print (f'【参与抽奖】:预计每天中{str(O0O00O00O0OO0OOO0)[:6]}颗金种子丨好友收益:{str(O0O00O0OOO00OO000)[:6]}')#line:833
                    print (f'【抽奖统计】:每1万☘️中{str(OO0OO00O000OOO000)[:6]}颗金种子丨☘️人均:{str(OO0O0OO0O0OO0O0OO)[:7]}️')#line:834
        except Exception as O00O0OOOOO000O0O0 :#line:835
            print (O00O0OOOOO000O0O0 )#line:836
    def energy (O0O0OOO0OO0OOO0O0 ):#line:840
        try :#line:841
            while True :#line:842
                OOOOOOOO0O0OO0OO0 =f'__{timi_new()}'#line:843
                OO000OOO00O00OOOO ={'source':'scsc','authorization':O0O0OOO0OO0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO0O0OO0OO0 ),'signstring':OOOOOOOO0O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:854
                OO0000O0OOO0O00O0 =requests .request ('get',f'{host}/energy/general',headers =OO000OOO00O00OOOO ).json ()#line:855
                if 'status'in OO0000O0OOO0O00O0 :#line:857
                    if OO0000O0OOO0O00O0 ['status']==200 :#line:858
                        O0O00OOO00O00OOO0 =OO0000O0OOO0O00O0 ['data']['ordinary_water']#line:859
                        OO0OOO0O0OOO00000 =OO0000O0OOO0O00O0 ['data']['ordinary_fertilizer']#line:860
                        OOOOO0OO0000O0OO0 =OO0000O0OOO0O00O0 ['data']['videoStatus']#line:861
                        O00OO0O0000O00OOO =OO0000O0OOO0O00O0 ['data']['waterVideoKey']#line:862
                        print (f'【我的营养】:肥料:{str(OO0OOO0O0OOO00000).split(".")[0]}丨水滴:{str(O0O00OOO00O00OOO0).split(".")[0]}')#line:863
                        if float (OO0OOO0O0OOO00000 )<96 :#line:864
                            if OOOOO0OO0000O0OO0 :#line:865
                                time .sleep (random .randint (160 ,180 )/10 )#line:866
                                O0000000OO0000000 =99 -float (OO0OOO0O0OOO00000 )#line:867
                                OOOO0OO0OOO0OOO0O ={"fertilizer":str (O0000000OO0000000 ).split ('.')[0 ]}#line:868
                                OO0OO0O0OO00O000O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO000OOO00O00OOOO ).json ()#line:869
                                if 'status'in OO0OO0O0OO00O000O :#line:871
                                    if OO0OO0O0OO00O000O ['status']==200 :#line:872
                                        print (f'【购买肥料】:看广告获取肥料:{OO0OO0O0OO00O000O["message"]}')#line:873
                                    if OO0OO0O0OO00O000O ['status']==500 :#line:874
                                        print (f'【购买肥料】:看广告获取肥料:{OO0OO0O0OO00O000O["message"]}')#line:875
                                        break #line:876
                            if energy :#line:877
                                O0000000OO0000000 =99 -float (OO0OOO0O0OOO00000 )#line:878
                                OOO0000OO00O0O0OO =f'_fertilizer={O0000000OO0000000}_{timi_new()}'#line:879
                                O0OO000O0OOOOOOOO ={'source':'scsc','authorization':O0O0OOO0OO0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OO00O0O0OO ),'signstring':OOO0000OO00O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:890
                                OOO0000O00OO00OO0 ={"fertilizer":O0000000OO0000000 }#line:891
                                O0O00O0O0OO000OOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0OO000O0OOOOOOOO ,data =OOO0000O00OO00OO0 ).json ()#line:892
                                if 'status'in O0O00O0O0OO000OOO :#line:894
                                    if O0O00O0O0OO000OOO ['status']==200 :#line:895
                                        print (f'【购买肥料】:购买肥料:{O0O00O0O0OO000OOO["message"]}丨数量:{O0000000OO0000000}')#line:896
                                    if O0O00O0O0OO000OOO ['status']==500 :#line:897
                                        print (f'【购买肥料】:购买肥料:{O0O00O0O0OO000OOO["message"]}丨数量:{O0000000OO0000000}')#line:898
                                        O0O0OOO0000O0O0O0 =O0O00O0O0OO000OOO ["message"].split ('-')[1 ]#line:899
                                        O0000O000OOO0OOO0 =f'__{timi_new()}'#line:900
                                        OO00OOOO0O0O000OO ={'source':'scsc','authorization':O0O0OOO0OO0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O000OOO0OOO0 ),'signstring':O0000O000OOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:911
                                        O000O0O000OOO0OOO =requests .request ('get',f'{host}/user',headers =OO00OOOO0O0O000OO ).json ()#line:912
                                        if 'status'in O000O0O000OOO0OOO :#line:913
                                            if O000O0O000OOO0OOO ['status']==200 :#line:914
                                                O00O00O0O0O00OOOO =O000O0O000OOO0OOO ['data']['inner_id']#line:915
                                                give_gold (O00O00O0O0O00OOOO ,float (O0O0OOO0000O0O0O0 )+1 )#line:916
                                                O0O0OOO0OO0OOO0O0 .energy ()#line:917
                        if float (O0O00OOO00O00OOO0 )<880 :#line:918
                            if O00OO0O0000O00OOO :#line:919
                                time .sleep (random .randint (160 ,180 )/10 )#line:920
                                O0OO00O0000O000OO =999 -float (O0O00OOO00O00OOO0 )#line:921
                                O0O0O00OOO000000O ={"water":str (O0OO00O0000O000OO ).split ('.')[0 ]}#line:922
                                O0OOO000O0000O000 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO000OOO00O00OOOO ).json ()#line:923
                                if 'status'in O0OOO000O0000O000 :#line:925
                                    if O0OOO000O0000O000 ['status']==200 :#line:926
                                        print (f'【购买水滴】:看广告获取水滴:{O0OOO000O0000O000["message"]}')#line:927
                                    if O0OOO000O0000O000 ['status']==500 :#line:928
                                        print (f'【购买水滴】:看广告获取水滴:{O0OOO000O0000O000["message"]}')#line:929
                                        break #line:930
                            if energy :#line:931
                                O0OO00O0000O000OO =999 -float (O0O00OOO00O00OOO0 )#line:932
                                OOO0O000000OO0OOO =f'_water={O0OO00O0000O000OO}_{timi_new()}'#line:933
                                OO00O00O0O000O00O ={'source':'scsc','authorization':O0O0OOO0OO0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000000OO0OOO ),'signstring':OOO0O000000OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:944
                                O0O00000O00OO0O0O ={"water":O0OO00O0000O000OO }#line:945
                                O00O00OOOOOO0OOO0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO00O00O0O000O00O ,data =O0O00000O00OO0O0O ).json ()#line:947
                                if 'status'in O00O00OOOOOO0OOO0 :#line:949
                                    if O00O00OOOOOO0OOO0 ['status']==200 :#line:950
                                        print (f'【购买水滴】:购买水滴:{O00O00OOOOOO0OOO0["message"]}丨数量:{O0OO00O0000O000OO}')#line:951
                                    if O00O00OOOOOO0OOO0 ['status']==500 :#line:952
                                        print (f'【购买水滴】:购买水滴:{O00O00OOOOOO0OOO0["message"]}丨数量:{O0OO00O0000O000OO}')#line:953
                                        O0O0OOO0000O0O0O0 =O00O00OOOOOO0OOO0 ["message"].split ('-')[1 ]#line:954
                                        O0000O000OOO0OOO0 =f'__{timi_new()}'#line:955
                                        OO00OOOO0O0O000OO ={'source':'scsc','authorization':O0O0OOO0OO0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O000OOO0OOO0 ),'signstring':O0000O000OOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:966
                                        O000O0O000OOO0OOO =requests .request ('get',f'{host}/user',headers =OO00OOOO0O0O000OO ).json ()#line:967
                                        if 'status'in O000O0O000OOO0OOO :#line:968
                                            if O000O0O000OOO0OOO ['status']==200 :#line:969
                                                O00O00O0O0O00OOOO =O000O0O000OOO0OOO ['data']['inner_id']#line:970
                                                give_gold (O00O00O0O0O00OOOO ,float (O0O0OOO0000O0O0O0 )+1 )#line:971
                                                O0O0OOO0OO0OOO0O0 .energy ()#line:972
                        break #line:973
        except Exception as O00OOOO0O0OO000OO :#line:975
            print (O00OOOO0O0OO000OO )#line:976
def bundled_def ():#line:978
    O0OOO0O0O0OO0OO0O =['5570536','7750212','7911652','7911680','7805624']#line:979
    return O0OOO0O0O0OO0OO0O [random .randint (0 ,len (O0OOO0O0O0OO0OO0O )-1 )]#line:980
def version_of_the_validation ():#line:984
    return str ((83 -56 )/10 )#line:985
def gitee_validation ():#line:988
    try :#line:989
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:990
    except :#line:991
        sys .exit (0 )#line:992
def update_the_validation ():#line:996
    try :#line:997
        O0OO0O0OOO00O0000 =gitee_validation ()#line:998
        if version_of_the_validation ()<O0OO0O0OOO00O0000 ['CityEarth']['edition']:#line:999
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO0O0OOO00O0000["CityEarth"]["edition"]}   ❌')#line:1000
            print (f'更新内容=>>{O0OO0O0OOO00O0000["CityEarth"]["content"]}   🎉')#line:1001
        else :#line:1002
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO0O0OOO00O0000["CityEarth"]["edition"]}   ✅')#line:1003
            print (f'更新内容=>> {O0OO0O0OOO00O0000["CityEarth"]["content"]}   🎉')#line:1004
    except Exception as O0OOOOOO0OOO0O0O0 :#line:1005
        print (O0OOOOOO0OOO0O0O0 )#line:1006
def os_qinglong ():#line:1009
    if application in os .environ :#line:1010
        OOO0O000OO00O0OOO =os .environ [application ].split ('\n')#line:1011
        if len (OOO0O000OO00O0OOO )>0 :#line:1012
            return OOO0O000OO00O0OOO #line:1013
        else :#line:1014
            print (f"{application}变量未启用")#line:1015
            print ('脚本退出')#line:1016
            sys .exit (1 )#line:1017
    else :#line:1018
        if token :#line:1019
            OOO0O000OO00O0OOO =token .split ('\n')#line:1020
            if len (OOO0O000OO00O0OOO )>0 :#line:1021
                return OOO0O000OO00O0OOO #line:1022
        else :#line:1023
            print (f"内置变量为空")#line:1024
            print ('脚本结束')#line:1025
            sys .exit (0 )#line:1026
if __name__ =='__main__':#line:1031
    start ()#line:1032
