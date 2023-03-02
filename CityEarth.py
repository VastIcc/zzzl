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
        OOOOOO00OO0OO0OO0 =os_qinglong ()#line:10
        print (f"==========共找到{len(OOOOOO00OO0OO0OO0)}个账号==========")#line:11
        for OO0O0000OO0O0OO00 in OOOOOO00OO0OO0OO0 :#line:12
            OOO0OOO0O00O00000 =[]#line:13
            print (f"------------正在执行第{OOOOOO00OO0OO0OO0.index(OO0O0000OO0O0OO00) + 1}个账号------------")#line:14
            O0O0O0000O0OO00O0 =CityEarth (OO0O0000OO0O0OO00 ,OOO0OOO0O00O00000 )#line:15
            def OOO00OO000O00O0O0 ():#line:17
                if O0O0O0000O0OO00O0 .base_info ():#line:19
                    O0O0O0000O0OO00O0 .sealing ()#line:21
                    O0O0O0000O0OO00O0 .invitenum ()#line:23
                    O0O0O0000O0OO00O0 .game_map ()#line:25
                    O0O0O0000O0OO00O0 .friends_invitation ()#line:27
                    O0O0O0000O0OO00O0 .energy ()#line:29
                    O0O0O0000O0OO00O0 .add_clover ()#line:31
                    O0O0O0000O0OO00O0 .propsraffle ()#line:33
                    O0O0O0000O0OO00O0 .synthetic ()#line:35
                    O0O0O0000O0OO00O0 .crops_illustrated ()#line:37
                    O0O0O0000O0OO00O0 .give_gold ()#line:39
                    O0O0O0000O0OO00O0 .withdraw ()#line:41
            OO000O0O000OOO0OO =threading .Thread (target =OOO00OO000O00O0O0 )#line:43
            OO000O0O000OOO0OO .start ()#line:44
            time .sleep (time_xx )#line:45
        print (f"------------正在处理推送通知------------")#line:46
        time .sleep (0.5 )#line:47
        O0O0OOOOO0O0O0O00 =format_msg ()#line:48
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O0OOOOO0O0O0O00 +' ')#line:49
    except Exception as O0O00OOO000O00O00 :#line:50
        print (O0O00OOO000O00O00 )#line:51
def give_gold (O0O000OO00OOO0OO0 ,OO0O00O0OO000O0O0 ):#line:54
        try :#line:55
            OOOO000000OO00000 =f'_doneeNo={O0O000OO00OOO0OO0}&quantity={int(OO0O00O0OO000O0O0)}_{timi_new()}'#line:56
            O00O00OOOO0O00000 ={'source':'scsc','authorization':os_qinglong ()[0 ].split ('&')[0 ],'timestamp':str (timi_new ()),'sign':sign (OOOO000000OO00000 ),'signstring':OOOO000000OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:67
            O00OO000000O0O00O ={"quantity":int (OO0O00O0OO000O0O0 ),"doneeNo":O0O000OO00OOO0OO0 }#line:71
            OOOO00OO00000O0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O00O00OOOO0O00000 ,data =O00OO000000O0O00O ).json ()#line:72
            if 'status'in OOOO00OO00000O0O0 :#line:74
                if OOOO00OO00000O0O0 ['status']==200 :#line:75
                    if OOOO00OO00000O0O0 ['data']:#line:76
                        print (f'【赠送种子】:赠送{int(OO0O00O0OO000O0O0)}种子给{O0O000OO00OOO0OO0}成功')#line:77
                        return True #line:78
                if OOOO00OO00000O0O0 ['status']==401 :#line:79
                    print (f'【赠送种子】:{OOOO00OO00000O0O0["message"]}')#line:80
                    return False #line:81
                if OOOO00OO00000O0O0 ['status']==500 :#line:82
                    print (f'【赠送种子】:{OOOO00OO00000O0O0["message"]}')#line:83
                    return False #line:84
            return False #line:85
        except Exception as OO0O0O0OO0O0000OO :#line:86
            print (OO0O0O0OO0O0000OO )#line:87
def sign (O0O00000OOO0O0000 ):#line:90
    OO00OO0OOO00O00O0 =hashlib .md5 (O0O00000OOO0O0000 .encode ()).hexdigest ()#line:91
    OO0OO00OOO000O00O ="scsc%^&*"+OO00OO0OOO00O00O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:92
    O000OO000O0O0O0O0 =hashlib .md5 (OO0OO00OOO000O00O .encode ()).hexdigest ()#line:93
    return O000OO000O0O0O0O0 #line:94
def format_msg ():#line:96
    O0OOOO0OO00OOOO0O =""#line:97
    for O0O0OOOO000O00OOO in msg_list :#line:98
        O0OOOO0OO00OOOO0O +=str (O0O0OOOO000O00OOO )+"\r\n"#line:99
    return O0OOOO0OO00OOOO0O #line:100
def timi_new ():#line:102
    return str (int (time .time ()*1000 ))#line:103
class CityEarth :#line:106
    def __init__ (OOOOO00OO000000OO ,O0OOOOOOO00OOO000 ,O0O000O0000000O0O ):#line:108
        try :#line:109
            OOOOO00OO000000OO .msg =O0O000O0000000O0O #line:110
            OOOOO00OO000000OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:111
            OOOOO00OO000000OO .token =O0OOOOOOO00OOO000 .split ('&')[0 ]#line:112
            OOOOO00OO000000OO .innerId =O0OOOOOOO00OOO000 .split ('&')[1 ]#line:113
            OOOOO00OO000000OO .doneeNo =O0OOOOOOO00OOO000 .split ('&')[2 ]#line:114
        except :#line:115
            print ('变量格式错误')#line:116
    def base_info (OOOOOO0O0OO0O0O0O ):#line:119
        try :#line:120
            OOOOOO0O0OO0O0O0O .watched_ad ()#line:122
            O00O00O0OOOOOO00O =f'__{timi_new()}'#line:123
            O000OO0OO0OO0OO00 ={'source':'scsc','authorization':OOOOOO0O0OO0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0OOOOOO00O ),'signstring':O00O00O0OOOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:134
            O0O00O00000OOO000 =requests .request ('get',f'{host}/user',headers =O000OO0OO0OO0OO00 ).json ()#line:135
            if 'status'in O0O00O00000OOO000 :#line:137
                if O0O00O00000OOO000 ['status']==200 :#line:138
                    O0O0OOO0OO0O00OO0 =O0O00O00000OOO000 ['data']['nickname']#line:139
                    OOO00OOOO00OOO0O0 =O0O00O00000OOO000 ['data']['inner_id']#line:140
                    OOOOO0000OOO0000O =O0O00O00000OOO000 ['data']['assets']['gold']#line:141
                    OOOOO00000O0OOO00 =O0O00O00000OOO000 ['data']['level']#line:142
                    print (f'【账号信息】:昵称:{O0O0OOO0OO0O00OO0[:5]}丨ID:{OOO00OOOO00OOO0O0}丨等级:{OOOOO00000O0OOO00}丨金种子:{str(OOOOO0000OOO0000O).split(".")[0]}')#line:143
                if O0O00O00000OOO000 ['status']==401 :#line:144
                    print (O0O00O00000OOO000 ['message'])#line:145
                    OOOOOO0O0OO0O0O0O .msg .append ('有账号失效了')#line:146
                    return False #line:147
                if O0O00O00000OOO000 ['status']==500 :#line:148
                    return False #line:149
            return True #line:150
        except Exception as OO0O0O0OO0O0OO000 :#line:151
            print (OO0O0O0OO0O0OO000 )#line:152
    def sealing (O00OOOOO0OO0OOO00 ):#line:155
        try :#line:156
            O0O0O00OOOOOO0OOO =f'__{timi_new()}'#line:157
            OOOOO00000O000000 ={'source':'scsc','authorization':O00OOOOO0OO0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OOOOOO0OOO ),'signstring':O0O0O00OOOOOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:168
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOOO00000O000000 )#line:169
            requests .request ('get',f'{host}/packsack/list',headers =OOOOO00000O000000 )#line:170
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOOO00000O000000 )#line:171
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOOO00000O000000 )#line:172
            requests .request ('get',f'{host}/user',headers =OOOOO00000O000000 )#line:173
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOOO00000O000000 )#line:174
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOOO00000O000000 )#line:175
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOOO00000O000000 )#line:176
            requests .request ('get',f'{host}/game/getAllData',headers =OOOOO00000O000000 )#line:177
            requests .request ('get',f'{host}/assets',headers =OOOOO00000O000000 )#line:178
        except Exception as OO0O00O0OO00OO0OO :#line:179
            print (OO0O00O0OO00OO0OO )#line:180
    def withdraw (O000OO00OOO000OO0 ):#line:184
        OO0OO0O0O00O000O0 =f'__{timi_new()}'#line:185
        O0OOOO0OOO00O00OO ={'source':'scsc','authorization':O000OO00OOO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0O00O000O0 ),'signstring':OO0OO0O0O00O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:196
        OOOO00000O0OO0O0O =requests .request ('get',f'{host}/assets',headers =O0OOOO0OOO00O00OO ).json ()#line:197
        if 'status'in OOOO00000O0OO0O0O :#line:199
            if OOOO00000O0OO0O0O ['status']==200 :#line:200
                O00O0O0OOOO0O0OO0 =OOOO00000O0OO0O0O ['data']['cash']#line:201
                if float (O00O0O0OOOO0O0OO0 )>20 :#line:202
                    OO0OO0O0O00O000O0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:203
                    O0OOOO0OOO00O00OO ={'authorization':O000OO00OOO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0O00O000O0 ),'signstring':OO0OO0O0O00O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:213
                    O0O0O00OOO000O00O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:214
                    O0O0O0OOOOOO0O0O0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0OOOO0OOO00O00OO ,data =O0O0O00OOO000O00O ).json ()#line:216
                    print (O0O0O0OOOOOO0O0O0 )#line:217
    def invitenum (O0O0000000OOO0OOO ):#line:220
        O00O0OOOOO00O0O0O =f'__{timi_new()}'#line:221
        O000OOO00OO0O00O0 ={'source':'scsc','authorization':O0O0000000OOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOOOO00O0O0O ),'signstring':O00O0OOOOO00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:232
        OOO0O0O00OOO0O000 =requests .request ('get',f'{host}/invite/invitenum',headers =O000OOO00OO0O00O0 ).json ()#line:233
        if 'status'in OOO0O0O00OOO0O000 :#line:235
            if OOO0O0O00OOO0O000 ['status']==200 :#line:236
                OOO0OO0O00O00OOO0 =OOO0O0O00OOO0O000 ['data']['invited_count']#line:237
                O0OOO0O0OO0O00O0O =OOO0O0O00OOO0O000 ['data']['invited_second_count']#line:238
                print (f'【我的邀请】:直邀好友:{OOO0OO0O00O00OOO0}丨间邀好友:{O0OOO0O0OO0O00O0O}')#line:239
    def game_map (OO0OO0OOO00O0O0OO ):#line:242
        try :#line:243
            OOOO0O0O0O00OO0OO =f'__{timi_new()}'#line:244
            OOOOOO00OOO00OOO0 ={'source':'scsc','authorization':OO0OO0OOO00O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O0O00OO0OO ),'signstring':OOOO0O0O0O00OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:255
            OOO00OO000OO0OO00 =requests .request ('get',f'{host}/game/map',headers =OOOOOO00OOO00OOO0 ).json ()#line:256
            if 'status'in OOO00OO000OO0OO00 :#line:258
                if OOO00OO000OO0OO00 ['status']==200 :#line:259
                    for OOOO00O0OOO00OOO0 in OOO00OO000OO0OO00 ['data']['list'][0 ]['crops']:#line:260
                        O0O000OO00O0O00OO =OOOO00O0OOO00OOO0 ['level']#line:262
                        if O0O000OO00O0O00OO ==41 :#line:263
                            O0000O0O00OO00000 =OOOO00O0OOO00OOO0 ['crop_name']#line:264
                            OOOO0OO0O000000OO =OOOO00O0OOO00OOO0 ['count']#line:265
                            if OOOO0OO0O000000OO >0 :#line:266
                                print (f'【农业资产】:{O0000O0O00OO00000}丨数量:{OOOO0OO0O000000OO}')#line:267
        except Exception as O0O0OO0O0000O0000 :#line:268
            print (O0O0OO0O0000O0000 )#line:269
    def give_gold (OOO0OOOOOO0O00OOO ):#line:272
        try :#line:273
            O00O00O000OO0OO00 =f'__{timi_new()}'#line:274
            OOOOO000O000O000O ={'source':'scsc','authorization':OOO0OOOOOO0O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O000OO0OO00 ),'signstring':O00O00O000OO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:285
            O0OO0OOOOO000OO0O =requests .request ('get',f'{host}/user',headers =OOOOO000O000O000O ).json ()#line:286
            if 'status'in O0OO0OOOOO000OO0O :#line:287
                if O0OO0OOOOO000OO0O ['status']==200 :#line:288
                    if float (OOO0OOOOOO0O00OOO .doneeNo )!=0 :#line:289
                        O0O0OO000O0O00O0O =O0OO0OOOOO000OO0O ['data']['assets']['gold']#line:290
                        if float (O0O0OO000O0O00O0O )>float (OOO0OOOOOO0O00OOO .innerId ):#line:291
                            O0OOO0O000OO00000 =int (float (O0O0OO000O0O00O0O )/1.1 )#line:292
                            O00O00O000OO0OO00 =f'_doneeNo={OOO0OOOOOO0O00OOO.doneeNo}&quantity={O0OOO0O000OO00000}_{timi_new()}'#line:293
                            OOOOO000O000O000O ={'source':'scsc','authorization':OOO0OOOOOO0O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O000OO0OO00 ),'signstring':O00O00O000OO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:304
                            OO00O0OOO00OO0OOO ={"quantity":O0OOO0O000OO00000 ,"doneeNo":OOO0OOOOOO0O00OOO .doneeNo }#line:308
                            O000000000OOOOO0O =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOO000O000O000O ,data =OO00O0OOO00OO0OOO ).json ()#line:309
                            if 'status'in O000000000OOOOO0O :#line:311
                                if O000000000OOOOO0O ['status']==200 :#line:312
                                    if O000000000OOOOO0O ['data']:#line:313
                                        print (f'【赠送种子】:赠送{O0OOO0O000OO00000}种子给{OOO0OOOOOO0O00OOO.doneeNo}成功')#line:314
                    else :#line:315
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:316
        except Exception as OO0000O00000O00O0 :#line:317
            print (OO0000O00000O00O0 )#line:318
    def invitation (O0OO0OOO0OOO00000 ):#line:320
        try :#line:321
            _O00O0000O0OOOOO00 =float (bundled_def ())/4 #line:322
            OO0OOO000000O0O0O =f'_innerId={int(_O00O0000O0OOOOO00)}_{timi_new()}'#line:323
            O0OOO0O000OO000O0 ={'source':'scsc','authorization':O0OO0OOO0OOO00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO000000O0O0O ),'signstring':OO0OOO000000O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:334
            O0OO0OOOOOOO00OO0 ={"innerId":int (_O00O0000O0OOOOO00 )}#line:335
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0OOO0O000OO000O0 ,data =O0OO0OOOOOOO00OO0 )#line:336
        except Exception as OO0000O0OO000OO0O :#line:337
            print (OO0000O0OO000OO0O )#line:338
    def winning_rewards (OO0000O0OO0O0000O ):#line:341
        try :#line:342
            O000OOOOO0O00O0O0 =f'__{timi_new()}'#line:343
            O00OOO00O00000O00 ={'source':'scsc','authorization':OO0000O0OO0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOO0O00O0O0 ),'signstring':O000OOOOO0O00O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:354
            OOO00OO00OO0O0O0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00OOO00O00000O00 ).json ()#line:355
            if 'status'in OOO00OO00OO0O0O0O :#line:357
                if OOO00OO00OO0O0O0O ['status']==200 :#line:358
                    if OOO00OO00OO0O0O0O ['data']['amount']:#line:359
                        O00OOO00OOO00O0O0 =OOO00OO00OO0O0O0O ['data']['amount']['gold']#line:360
                        return O00OOO00OOO00O0O0 #line:361
                    else :#line:362
                        return 0 #line:363
        except Exception as O0OO0O0O00OOO0O00 :#line:364
            print (O0OO0O0O00OOO0O00 )#line:365
    def certification (O0OO0O00OO0OO0OO0 ):#line:368
        try :#line:369
            O000OOO0OO0O0OOOO =f'__{timi_new()}'#line:370
            OOO000OOO0O0O0O00 ={'source':'scsc','authorization':O0OO0O00OO0OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0OO0O0OOOO ),'signstring':O000OOO0OO0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:381
            OOO000O00O0O00OO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO000OOO0O0O0O00 ).json ()#line:382
            if 'status'in OOO000O00O0O00OO0 :#line:384
                if OOO000O00O0O00OO0 ['status']==200 :#line:385
                    if OOO000O00O0O00OO0 ['data']['result']:#line:386
                        OO000O0O0OO00000O =OOO000O00O0O00OO0 ['data']['nick_name']#line:387
                        return OO000O0O0OO00000O #line:388
                    else :#line:389
                        return '未实名'#line:390
        except Exception as O0000OOO00OOOOOOO :#line:391
            print (O0000OOO00OOOOOOO )#line:392
    def crops_illustrated (O000OO00OOO0O0000 ):#line:395
        try :#line:396
            O00OOOO000OO00000 =f'__{timi_new()}'#line:397
            O0O0O0OOOOOOO0000 ={'source':'scsc','authorization':O000OO00OOO0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO000OO00000 ),'signstring':O00OOOO000OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            OO0O0000OO0OO00OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O0O0OOOOOOO0000 ).json ()#line:409
            if 'status'in OO0O0000OO0OO00OO :#line:411
                if OO0O0000OO0OO00OO ['status']==200 :#line:412
                    OO0O00OO00O000000 =OO0O0000OO0OO00OO ['data'][0 ]['crops']#line:413
                    for OO0OO0OOOOO0O0OO0 in OO0O00OO00O000000 :#line:414
                        if OO0OO0OOOOO0O0OO0 ['ill_clover_award']:#line:415
                            if float (OO0OO0OOOOO0O0OO0 ['ill_clover_award'])>1 :#line:416
                                if OO0OO0OOOOO0O0OO0 ['is_finish']:#line:417
                                    if not OO0OO0OOOOO0O0OO0 ['is_getit']:#line:418
                                        if O000OO00OOO0O0000 .certification ()!='未实名':#line:419
                                            O00OOOO000OO00000 =f'_award_level={OO0OO0OOOOO0O0OO0["level"]}_{timi_new()}'#line:420
                                            O0O0O0OOOOOOO0000 ={'source':'scsc','authorization':O000OO00OOO0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO000OO00000 ),'signstring':O00OOOO000OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:431
                                            O00O00O0000O000OO ={"award_level":OO0OO0OOOOO0O0OO0 ['level']}#line:432
                                            OO00O0000OO0OOO0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O0O0OOOOOOO0000 ,json =O00O00O0000O000OO ).json ()#line:434
                                            if 'status'in OO00O0000OO0OOO0O :#line:435
                                                if OO00O0000OO0OOO0O ['status']==200 :#line:436
                                                    OO0OO000O0000OO0O =OO00O0000OO0OOO0O ['data']['ill_clover_award']#line:437
                                                    print (f'【图鉴奖励】:领取{OO0OO0OOOOO0O0OO0["crop_name"]}成就丨奖励{OO0OO000O0000OO0O}☘️')#line:439
                                                if OO00O0000OO0OOO0O ['status']==500 :#line:440
                                                    print (f'【图鉴奖励】:{OO00O0000OO0OOO0O["message"]}')#line:441
        except Exception as O0OO000OO0OO00OO0 :#line:442
            print (O0OO000OO0OO00OO0 )#line:443
    def watched_ad (O00O00000000000O0 ):#line:446
        try :#line:447
            OOOOOOO0000OO000O =f'__{timi_new()}'#line:448
            OOO00000O00O0OO0O ={'source':'scsc','authorization':O00O00000000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0000OO000O ),'signstring':OOOOOOO0000OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:459
            OOOOO0OO00OOO0O00 =requests .request ('get',f'{host}/game/getAllData',headers =OOO00000O00O0OO0O ).json ()#line:460
            if 'status'in OOOOO0OO00OOO0O00 :#line:462
                if OOOOO0OO00OOO0O00 ['status']==200 :#line:463
                    if 'offlineInfo'in OOOOO0OO00OOO0O00 ['data']:#line:464
                        time .sleep (random .randint (3 ,5 ))#line:465
                        O0000O0000OOOO0O0 =OOOOO0OO00OOO0O00 ['data']['offlineInfo']['off_minute']#line:466
                        OOO00OOOO0O0OO00O =float (OOOOO0OO00OOO0O00 ['data']['silver'])/1000000000000 #line:467
                        time .sleep (1 )#line:468
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO00000O00O0OO0O ).json ()#line:469
                        time .sleep (2 )#line:470
                        O0O0OOOOOOOO0O0O0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO00000O00O0OO0O ).json ()#line:471
                        if 'status'in O0O0OOOOOOOO0O0O0 :#line:473
                            if O0O0OOOOOOOO0O0O0 ['status']==200 :#line:474
                                O00OO00O0OOOOO0OO =float (O0O0OOOOOOOO0O0O0 ['data']['silver'])/1000000000000 #line:475
                                O000OOO00O00O0O00 =str (O00OO00O0OOOOO0OO -OOO00OOOO0O0OO00O )[:6 ]#line:476
                                print (f'【离线奖励】:翻倍离线{O0000O0000OOOO0O0}分钟奖励🌱数量:{O000OOO00O00O0O00}t粒')#line:477
        except Exception as O00OOOOOO0OO0O0O0 :#line:478
            print (O00OOOOOO0OO0O0O0 )#line:479
    def user_ad (O0O00O00O000000O0 ):#line:482
        try :#line:483
            OOO0OO0000OO00O0O =f'__{timi_new()}'#line:484
            O0O000O00000O0OO0 ={'source':'scsc','authorization':O0O00O00O000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0000OO00O0O ),'signstring':OOO0OO0000OO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:495
            O000O00O00OOO00O0 =requests .request ('get',f'{host}/user/ad',headers =O0O000O00000O0OO0 ).json ()#line:496
            if 'status'in O000O00O00OOO00O0 :#line:498
                if O000O00O00OOO00O0 ['status']==200 :#line:499
                    O0OO0O000O0O000O0 =O000O00O00OOO00O0 ['data']['max_time']#line:500
                    OOOO0O0O00O000O00 =O000O00O00OOO00O0 ['data']['watch_time']#line:501
                    OO0O00O0O00OO0OO0 =O000O00O00OOO00O0 ['data']['added_time']#line:502
                    print (f'【获取种子】:获取🌱剩余{OO0O00O0O00OO0OO0 + O0OO0O000O0O000O0 - OOOO0O0O00O000O00}次丨好友提供:{OO0O00O0O00OO0OO0}次')#line:503
                    if OO0O00O0O00OO0OO0 +O0OO0O000O0O000O0 -OOOO0O0O00O000O00 >0 :#line:504
                        time .sleep (random .randint (16 ,19 ))#line:505
                        O000OO00O00O00O0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O000O00000O0OO0 ).json ()#line:506
                        if 'status'in O000OO00O00O00O0O :#line:508
                            if O000OO00O00O00O0O ['status']==200 :#line:509
                                O00OOO00000000O0O =float (O000OO00O00O00O0O ['data']['silver'])/1000000000000 #line:510
                                print (f'【获取种子】:获得🌱:{int(O00OOO00000000O0O)}t粒')#line:511
                                return True #line:512
                            if O000OO00O00O00O0O ['status']==500 :#line:513
                                OO00OO0OOOO000OOO =O000OO00O00O00O0O ['message']#line:514
                                print (f'【获取种子】:{OO00OO0OOOO000OOO}')#line:515
                                return False #line:516
        except Exception as O00000O00O00O00O0 :#line:517
            print (O00000O00O00O00O0 )#line:518
    def synthetic (O0O000OO000O000OO ):#line:521
        global id ,g #line:522
        try :#line:523
            O0O00O00O0000OOO0 =O0O000OO000O000OO .level_new ()#line:524
            O000O0OOOOOOOOO00 =random .randint (9 ,11 )#line:525
            OOOOOO0O0O0O000O0 =f'_site=8&targetSite={O000O0OOOOOOOOO00}_{timi_new()}'#line:526
            OOO00OO0000OOOOO0 ={'source':'scsc','authorization':O0O000OO000O000OO .token ,'timestamp':timi_new (),'sign':sign (OOOOOO0O0O0O000O0 ),'signstring':OOOOOO0O0O0O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:537
            O0O0OO00O0OOOOOO0 ={"site":int (8 ),"targetSite":int (O000O0OOOOOOOOO00 )}#line:538
            requests .request ('post',f'{host}/game/crops/move',headers =OOO00OO0000OOOOO0 ,json =O0O0OO00O0OOOOOO0 )#line:539
            while True :#line:540
                OOOOOO00O0OO0O00O =f'__{timi_new()}'#line:541
                O0O0OOO00O0OO0OO0 ={'source':'scsc','authorization':O0O000OO000O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00O0OO0O00O ),'signstring':OOOOOO00O0OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:552
                O00O0000O0OO00O00 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OOO00O0OO0OO0 ).json ()#line:553
                if 'status'in O00O0000O0OO00O00 :#line:555
                    if O00O0000O0OO00O00 ['status']==200 :#line:556
                        O00O0OO00O0O00OOO =O00O0000O0OO00O00 ['data']['cropList']#line:557
                        O000000O0000O0OO0 =O00O0000O0OO00O00 ['data']['gameCoreDataDBid']#line:558
                        O0OOOOO000OO00O00 =float (O00O0000O0OO00O00 ['data']['silver'])/1000000000000 #line:559
                        O0O00OOOO000OO0OO =0 #line:564
                        for OOO0OO00O00000000 in O00O0OO00O0O00OOO :#line:565
                            if not OOO0OO00O00000000 :#line:566
                                OOO0O0O00O0000000 =f'_crop_id={O000000O0000O0OO0}&site={O0O00OOOO000OO0OO}_{O0O000OO000O000OO.time}'#line:567
                                OO00OOOO0O0000000 ={'source':'scsc','authorization':O0O000OO000O000OO .token ,'timestamp':O0O000OO000O000OO .time ,'sign':sign (OOO0O0O00O0000000 ),'signstring':OOO0O0O00O0000000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:577
                                O0OO000OOO0OOOOOO ={"site":O0O00OOOO000OO0OO ,"crop_id":O000000O0000O0OO0 }#line:578
                                O00O0OOO0O00OOOO0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO00OOOO0O0000000 ,data =O0OO000OOO0OOOOOO ).json ()#line:579
                                time .sleep (random .randint (1 ,3 )/10 )#line:581
                                if 'status'in O00O0OOO0O00OOOO0 :#line:582
                                    if O00O0OOO0O00OOOO0 ['status']==200 :#line:583
                                        if O00O0OOO0O00OOOO0 ['message']=='种子数量不足':#line:584
                                            O0O00O00O0000OOO0 =O0O000OO000O000OO .level_new ()#line:585
                                            print (f'【种植合成】:{O00O0OOO0O00OOOO0["message"]}')#line:586
                                            if not O0O000OO000O000OO .user_ad ():#line:587
                                                return False #line:588
                                    if O00O0OOO0O00OOOO0 ['status']==500 :#line:589
                                        print (f'【种植合成】:{O00O0OOO0O00OOOO0["message"]}')#line:590
                                        return False #line:591
                            O0O00OOOO000OO0OO +=1 #line:592
                        OO0O00OO0OOO000O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OOO00O0OO0OO0 ).json ()#line:593
                        O000O0O0000O0O00O =OO0O00OO0OOO000O0 ['data']['cropList']#line:594
                        OO0O0O000O00OO00O =False #line:595
                        for OOO0OO00O00000000 in range (12 ):#line:596
                            id =O000O0O0000O0O00O [OOO0OO00O00000000 ]['level']#line:597
                            if float (O0O00O00O0000OOO0 )-float (id )>9 :#line:598
                                O0000OOOO000OO000 =f'_site={OOO0OO00O00000000}_{timi_new()}'#line:599
                                O0000O0OO0OO00OOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O000OO000O000OO .token ,'timestamp':timi_new (),'sign':sign (O0000OOOO000OO000 ),'signstring':O0000OOOO000OO000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:610
                                OOOOO0OOO000000OO ={"site":OOO0OO00O00000000 }#line:611
                                O0OO0O00O00O0O0O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0000O0OO0OO00OOO ,data =OOOOO0OOO000000OO ).json ()#line:613
                                if 'status'in O0OO0O00O00O0O0O0 :#line:614
                                    if O0OO0O00O00O0O0O0 ['status']==200 :#line:615
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:616
                            if id !=0 :#line:617
                                for OO00OO00OO00OO0OO in range (11 ):#line:618
                                    O0O00O00000O0OOOO =OO00OO00OO00OO0OO +1 #line:619
                                    g =O000O0O0000O0O00O [O0O00O00000O0OOOO ]['level']#line:620
                                    if id ==g :#line:621
                                        OO00O0OOOOO000O00 =OO00OO00OO00OO0OO +2 #line:622
                                        if OO00O0OOOOO000O00 !=OOO0OO00O00000000 +1 :#line:623
                                            O0OO00O0000O0O00O =OOO0OO00O00000000 +1 #line:624
                                            time .sleep (random .randint (1 ,3 )/10 )#line:626
                                            OOOOOO0O0O0O000O0 =f'_site={O0OO00O0000O0O00O - 1}&targetSite={OO00O0OOOOO000O00 - 1}_{timi_new()}'#line:627
                                            OOO00OO0000OOOOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O000OO000O000OO .token ,'timestamp':timi_new (),'sign':sign (OOOOOO0O0O0O000O0 ),'signstring':OOOOOO0O0O0O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:644
                                            OO00O0O0O0O0O0O0O ={"site":int (O0OO00O0000O0O00O -1 ),"targetSite":int (OO00O0OOOOO000O00 -1 )}#line:645
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOO00OO0000OOOOO0 ,json =OO00O0O0O0O0O0O0O )#line:646
                                            OO0O0O000O00OO00O =True #line:648
                                    if OO0O0O000O00OO00O :#line:649
                                        break #line:650
                                if OO0O0O000O00OO00O :#line:651
                                    break #line:652
        except :#line:653
            O0O000OO000O000OO .synthetic ()#line:654
    def level_new (O0O0OOOOOOOOOO00O ):#line:657
        try :#line:658
            OOO00OO0000000OO0 =f'__{timi_new()}'#line:659
            O0O000OOO000OO0O0 ={'source':'scsc','authorization':O0O0OOOOOOOOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0000000OO0 ),'signstring':OOO00OO0000000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:670
            O00OO0OO00OO0OOO0 =requests .request ('get',f'{host}/user',headers =O0O000OOO000OO0O0 ).json ()#line:671
            if 'status'in O00OO0OO00OO0OOO0 :#line:672
                if O00OO0OO00OO0OOO0 ['status']==200 :#line:673
                    return float (O00OO0OO00OO0OOO0 ['data']['level'])#line:674
        except Exception as O000OOO0OOO0OO000 :#line:675
            print (O000OOO0OOO0OO000 )#line:676
    def propsraffle (OOOO0000OOOO00OO0 ):#line:679
        try :#line:680
            while True :#line:681
                OOOOOO0000OO0000O =f'__{timi_new()}'#line:682
                OOOO0O00O0O000OO0 ={'source':'scsc','authorization':OOOO0000OOOO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0000OO0000O ),'signstring':OOOOOO0000OO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:693
                OO0OO00OO0O000O00 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOO0O00O0O000OO0 ).json ()#line:694
                if 'status'in OO0OO00OO0O000O00 :#line:696
                    if OO0OO00OO0O000O00 ['status']==200 :#line:697
                        OOO0000OO00OOOO0O =OO0OO00OO0O000O00 ['data']['rows']#line:698
                        OOOO0000O0OOO00OO =OO0OO00OO0O000O00 ['data']['vstate']#line:699
                        if OOO0000OO00OOOO0O ==5 or OOO0000OO00OOOO0O ==6 or OOO0000OO00OOOO0O ==7 :#line:700
                            OO00OO0OO0O0O00OO =OO0OO00OO0O000O00 ['data']['silver']#line:701
                            print (f'【转盘抽奖】:获得种子:{OO00OO0OO0O0O00OO}')#line:702
                        if OOO0000OO00OOOO0O ==1 or OOO0000OO00OOOO0O ==2 or OOO0000OO00OOOO0O ==3 :#line:703
                            OO0OO0OO0000O0000 =OO0OO00OO0O000O00 ['data']['clover']#line:704
                            print (f'【转盘抽奖】:获得三叶草:{OO0OO0OO0000O0000}')#line:705
                        if OOO0000OO00OOOO0O ==4 or OOO0000OO00OOOO0O ==8 :#line:706
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:707
                        if OOO0000OO00OOOO0O =='抽奖次数已用完':#line:711
                            break #line:745
                time .sleep (random .randint (8 ,15 )/10 )#line:746
        except Exception as OOOO0OO0OO0000OO0 :#line:747
            print (OOOO0OO0OO0000OO0 )#line:748
    def friends_invitation (OOOOO000OO000O0OO ):#line:751
        try :#line:752
            O0OO000O000OO0O0O =f'__{timi_new()}'#line:753
            OO0OOOOOO0OO0O000 ={'source':'scsc','authorization':OOOOO000OO000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O000OO0O0O ),'signstring':O0OO000O000OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:764
            O0O0O0000O0OO0O00 =requests .request ('get',f'{host}/friends',headers =OO0OOOOOO0OO0O000 ).json ()#line:765
            if 'status'in O0O0O0000O0OO0O00 :#line:766
                if O0O0O0000O0OO0O00 ['status']==200 :#line:767
                    O00O0OO0000O0OOO0 =O0O0O0000O0OO0O00 ['data']['myInviteter']#line:768
                    if O00O0OO0000O0OOO0 :#line:769
                        OOOO0000O0OOOOOO0 =O00O0OO0000O0OOO0 ['user']['nickname']#line:770
                        O000OO000OOO0000O =OOOOO000OO000O0OO .certification ()#line:771
                        print (f'【查邀请人】:我的邀请人:{OOOO0000O0OOOOOO0}丨实名:{O000OO000OOO0000O}')#line:772
                    else :#line:773
                        if OOOOO000OO000O0OO .innerId !='0':#line:774
                            OOOOO000OO000O0OO .invitation ()#line:775
        except Exception as O0O0000OO00000OOO :#line:776
            print (O0O0000OO00000OOO )#line:777
    def add_clover (OO00O0OOO0O0O0OO0 ):#line:780
        global golden_seed #line:781
        try :#line:782
            OOOO0O0O0OO0O0OO0 =f'__{timi_new()}'#line:783
            O0O0O0O0000OOO0OO ={'source':'scsc','authorization':OO00O0OOO0O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O0OO0O0OO0 ),'signstring':OOOO0O0O0OO0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
            O0O0000OOO0O0O000 =requests .request ('get',f'{host}/assets/clovers',headers =O0O0O0O0000OOO0OO ).json ()#line:795
            if 'status'in O0O0000OOO0O0O000 :#line:797
                if O0O0000OOO0O0O000 ['status']==200 :#line:798
                    O0O00OOOO00O0O000 =O0O0000OOO0O0O000 ['data']['clover']#line:799
                    O0OO00OO0OO0000O0 =O0O0000OOO0O0O000 ['data']['used_clover']#line:800
                    O000OOOOOOO0O00O0 =float (O0O00OOOO00O0O000 )-float (O0OO00OO0OO0000O0 )#line:801
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OO00OO0OO0000O0}')#line:802
                    if OO00O0OOO0O0O0OO0 .certification ()!='未实名':#line:803
                        if O000OOOOOOO0O00O0 >1 :#line:804
                            OOOO0O0O0OO0O0OO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O000OOOOOOO0O00O0)}_{timi_new()}'#line:805
                            OO00O000000O00000 ={'source':'scsc','authorization':OO00O0OOO0O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O0OO0O0OO0 ),'signstring':OOOO0O0O0OO0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:816
                            O00O000OOOO0O00O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O000OOOOOOO0O00O0 )}#line:817
                            O0O0O000000O0OO00 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO00O000000O00000 ,data =O00O000OOOO0O00O0 ).json ()#line:818
                            if 'status'in O0O0O000000O0OO00 :#line:820
                                if O0O0O000000O0OO00 ['status']==200 :#line:821
                                    print (f'【参与抽奖】:添加☘️:{O0O0O000000O0OO00["data"]}丨数量:{O000OOOOOOO0O00O0}')#line:822
                                if O0O0O000000O0OO00 ['status']==500 :#line:823
                                    print (f'【参与抽奖】:添加☘️:{O0O0O000000O0OO00["message"]}')#line:824
            OO0000O00OO0O000O =requests .request ('get',f'{host}/lottery',headers =O0O0O0O0000OOO0OO ).json ()#line:825
            OO0OOOO0O0OOOOOOO =OO00O0OOO0O0O0OO0 .winning_rewards ()#line:827
            if 'status'in OO0000O00OO0O000O :#line:828
                if OO0000O00OO0O000O ['status']==200 :#line:829
                    O0O0O000O000O0O00 =OO0000O00OO0O000O ['data'][0 ]['day_get_gold_quantity']#line:830
                    golden_seed +=float (O0O0O000O000O0O00 )#line:831
                    O0O00O00OO0OOO00O =OO0000O00OO0O000O ['data'][1 ]['value']#line:832
                    O00O0OO0OO0OOOOOO =OO0000O00OO0O000O ['data'][0 ]['join_number']#line:833
                    O0O000OOO0000O0O0 =int (float (OO0000O00OO0O000O ['data'][0 ]['totalValue']))#line:834
                    O0000O0O0OO0O00O0 =float (O0O00O00OO0OOO00O /O0O000OOO0000O0O0 )*10000 #line:835
                    O0000O000OO0OOOOO =O0O000OOO0000O0O0 /O00O0OO0OO0OOOOOO #line:836
                    print (f'【参与抽奖】:预计每天中{str(O0O0O000O000O0O00)[:6]}颗金种子丨好友收益:{str(OO0OOOO0O0OOOOOOO)[:6]}')#line:837
                    print (f'【抽奖统计】:每1万☘️中{str(O0000O0O0OO0O00O0)[:6]}颗金种子丨☘️人均:{str(O0000O000OO0OOOOO)[:7]}️')#line:838
        except Exception as OO0OOOOO0O0O0O00O :#line:839
            print (OO0OOOOO0O0O0O00O )#line:840
    def energy (O000O0OO0O00O0O00 ):#line:844
        try :#line:845
            while True :#line:846
                OO00000O0O0O0OO00 =f'__{timi_new()}'#line:847
                OO00O00000O000O00 ={'source':'scsc','authorization':O000O0OO0O00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000O0O0O0OO00 ),'signstring':OO00000O0O0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:858
                OOO00OO0O00O0OOOO =requests .request ('get',f'{host}/energy/general',headers =OO00O00000O000O00 ).json ()#line:859
                if 'status'in OOO00OO0O00O0OOOO :#line:861
                    if OOO00OO0O00O0OOOO ['status']==200 :#line:862
                        OO0O0OOO000OO00OO =OOO00OO0O00O0OOOO ['data']['ordinary_water']#line:863
                        OOOOO0OOOO00000O0 =OOO00OO0O00O0OOOO ['data']['ordinary_fertilizer']#line:864
                        OOOO00OOOO0O0O0O0 =OOO00OO0O00O0OOOO ['data']['videoStatus']#line:865
                        O00OOO0OO0O0000O0 =OOO00OO0O00O0OOOO ['data']['waterVideoKey']#line:866
                        print (f'【我的营养】:肥料:{str(OOOOO0OOOO00000O0).split(".")[0]}丨水滴:{str(OO0O0OOO000OO00OO).split(".")[0]}')#line:867
                        if float (OOOOO0OOOO00000O0 )<96 :#line:868
                            if OOOO00OOOO0O0O0O0 :#line:869
                                time .sleep (random .randint (160 ,180 )/10 )#line:870
                                O00O0OO0OO0O0O0O0 =99 -float (OOOOO0OOOO00000O0 )#line:871
                                OO000O000O00O0O0O ={"fertilizer":str (O00O0OO0OO0O0O0O0 ).split ('.')[0 ]}#line:872
                                O0O000O0OO00OOOO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO00O00000O000O00 ).json ()#line:873
                                if 'status'in O0O000O0OO00OOOO0 :#line:875
                                    if O0O000O0OO00OOOO0 ['status']==200 :#line:876
                                        print (f'【购买肥料】:看广告获取肥料:{O0O000O0OO00OOOO0["message"]}')#line:877
                                    if O0O000O0OO00OOOO0 ['status']==500 :#line:878
                                        print (f'【购买肥料】:看广告获取肥料:{O0O000O0OO00OOOO0["message"]}')#line:879
                                        break #line:880
                            if energy :#line:881
                                O00O0OO0OO0O0O0O0 =80 -float (OOOOO0OOOO00000O0 )#line:882
                                OO0OOOO00OO0OO000 =f'_fertilizer={int(O00O0OO0OO0O0O0O0)}_{timi_new()}'#line:883
                                OO0OOOO000OO0OOOO ={'source':'scsc','authorization':O000O0OO0O00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO00OO0OO000 ),'signstring':OO0OOOO00OO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:894
                                OO0OO0OOO0O00000O ={"fertilizer":int (O00O0OO0OO0O0O0O0 )}#line:895
                                OO00OO00OOO00OOO0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0OOOO000OO0OOOO ,data =OO0OO0OOO0O00000O ).json ()#line:896
                                if 'status'in OO00OO00OOO00OOO0 :#line:898
                                    if OO00OO00OOO00OOO0 ['status']==200 :#line:899
                                        print (f'【购买肥料】:购买肥料:{OO00OO00OOO00OOO0["message"]}丨数量:{int(O00O0OO0OO0O0O0O0)}')#line:900
                                    if OO00OO00OOO00OOO0 ['status']==500 :#line:901
                                        print (f'【购买肥料】:购买肥料:{OO00OO00OOO00OOO0["message"]}丨数量:{int(O00O0OO0OO0O0O0O0)}')#line:902
                                        OO0OO0OO0OOO00O00 =OO00OO00OOO00OOO0 ["message"].split ('-')[1 ]#line:903
                                        O0O0O000OOOOO0O0O =f'__{timi_new()}'#line:904
                                        O000O00000OO0O000 ={'source':'scsc','authorization':O000O0OO0O00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000OOOOO0O0O ),'signstring':O0O0O000OOOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:915
                                        OO000OOO000O0OOO0 =requests .request ('get',f'{host}/user',headers =O000O00000OO0O000 ).json ()#line:916
                                        if 'status'in OO000OOO000O0OOO0 :#line:917
                                            if OO000OOO000O0OOO0 ['status']==200 :#line:918
                                                OOO00000OO0O0O00O =OO000OOO000O0OOO0 ['data']['inner_id']#line:919
                                                if give_gold (OOO00000OO0O0O00O ,float (OO0OO0OO0OOO00O00 )+1 ):#line:920
                                                    O000O0OO0O00O0O00 .energy ()#line:921
                        if float (OO0O0OOO000OO00OO )<880 :#line:922
                            if O00OOO0OO0O0000O0 :#line:923
                                time .sleep (random .randint (160 ,180 )/10 )#line:924
                                O0000O00O0O0OO0OO =999 -float (OO0O0OOO000OO00OO )#line:925
                                OO0000OOOOO00OOOO ={"water":str (O0000O00O0O0OO0OO ).split ('.')[0 ]}#line:926
                                O0OOO00OOOO00O000 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO00O00000O000O00 ).json ()#line:927
                                if 'status'in O0OOO00OOOO00O000 :#line:929
                                    if O0OOO00OOOO00O000 ['status']==200 :#line:930
                                        print (f'【购买水滴】:看广告获取水滴:{O0OOO00OOOO00O000["message"]}')#line:931
                                    if O0OOO00OOOO00O000 ['status']==500 :#line:932
                                        print (f'【购买水滴】:看广告获取水滴:{O0OOO00OOOO00O000["message"]}')#line:933
                                        break #line:934
                            if energy :#line:935
                                O0000O00O0O0OO0OO =800 -float (OO0O0OOO000OO00OO )#line:936
                                O0OO00OO0000000O0 =f'_water={int(O0000O00O0O0OO0OO)}_{timi_new()}'#line:937
                                OO0OO00OOOOOO000O ={'source':'scsc','authorization':O000O0OO0O00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO0000000O0 ),'signstring':O0OO00OO0000000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:948
                                OOOO00OO0O00O00OO ={"water":int (O0000O00O0O0OO0OO )}#line:949
                                O0OO00O0OOO000OOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0OO00OOOOOO000O ,data =OOOO00OO0O00O00OO ).json ()#line:951
                                if 'status'in O0OO00O0OOO000OOO :#line:953
                                    if O0OO00O0OOO000OOO ['status']==200 :#line:954
                                        print (f'【购买水滴】:购买水滴:{O0OO00O0OOO000OOO["message"]}丨数量:{int(O0000O00O0O0OO0OO)}')#line:955
                                    if O0OO00O0OOO000OOO ['status']==500 :#line:956
                                        print (f'【购买水滴】:购买水滴:{O0OO00O0OOO000OOO["message"]}丨数量:{int(O0000O00O0O0OO0OO)}')#line:957
                                        OO0OO0OO0OOO00O00 =O0OO00O0OOO000OOO ["message"].split ('-')[1 ]#line:958
                                        O0O0O000OOOOO0O0O =f'__{timi_new()}'#line:959
                                        O000O00000OO0O000 ={'source':'scsc','authorization':O000O0OO0O00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000OOOOO0O0O ),'signstring':O0O0O000OOOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:970
                                        OO000OOO000O0OOO0 =requests .request ('get',f'{host}/user',headers =O000O00000OO0O000 ).json ()#line:971
                                        if 'status'in OO000OOO000O0OOO0 :#line:972
                                            if OO000OOO000O0OOO0 ['status']==200 :#line:973
                                                OOO00000OO0O0O00O =OO000OOO000O0OOO0 ['data']['inner_id']#line:974
                                                if give_gold (OOO00000OO0O0O00O ,float (OO0OO0OO0OOO00O00 )+1 ):#line:975
                                                    O000O0OO0O00O0O00 .energy ()#line:976
                        break #line:977
        except Exception as O0000O0O0O0O00O00 :#line:979
            print (O0000O0O0O0O00O00 )#line:980
def bundled_def ():#line:982
    OO0OOOOOO0OOOOO0O =['5570536','7750212','7911652','7911680','7805624']#line:983
    return OO0OOOOOO0OOOOO0O [random .randint (0 ,len (OO0OOOOOO0OOOOO0O )-1 )]#line:984
def version_of_the_validation ():#line:988
    return str ((84 -56 )/10 )#line:989
def gitee_validation ():#line:992
    try :#line:993
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:994
    except :#line:995
        sys .exit (0 )#line:996
def update_the_validation ():#line:1000
    try :#line:1001
        OO0O0O0000O000OOO =gitee_validation ()#line:1002
        if version_of_the_validation ()<OO0O0O0000O000OOO ['CityEarth']['edition']:#line:1003
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0O0000O000OOO["CityEarth"]["edition"]}   ❌')#line:1004
            print (f'更新内容=>>{OO0O0O0000O000OOO["CityEarth"]["content"]}   🎉')#line:1005
        else :#line:1006
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0O0000O000OOO["CityEarth"]["edition"]}   ✅')#line:1007
            print (f'更新内容=>> {OO0O0O0000O000OOO["CityEarth"]["content"]}   🎉')#line:1008
    except Exception as O0OOOO000O00O0OOO :#line:1009
        print (O0OOOO000O00O0OOO )#line:1010
def os_qinglong ():#line:1013
    if application in os .environ :#line:1014
        OOO0000OO0OO00O00 =os .environ [application ].split ('\n')#line:1015
        if len (OOO0000OO0OO00O00 )>0 :#line:1016
            return OOO0000OO0OO00O00 #line:1017
        else :#line:1018
            print (f"{application}变量未启用")#line:1019
            print ('脚本退出')#line:1020
            sys .exit (1 )#line:1021
    else :#line:1022
        if token :#line:1023
            OOO0000OO0OO00O00 =token .split ('\n')#line:1024
            if len (OOO0000OO0OO00O00 )>0 :#line:1025
                return OOO0000OO0OO00O00 #line:1026
        else :#line:1027
            print (f"内置变量为空")#line:1028
            print ('脚本结束')#line:1029
            sys .exit (0 )#line:1030
if __name__ =='__main__':#line:1035
    start ()#line:1036
