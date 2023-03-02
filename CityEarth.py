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
        O0OO0O00O0O000O00 =os_qinglong ()#line:10
        print (f"==========共找到{len(O0OO0O00O0O000O00)}个账号==========")#line:11
        for OO0OOOO0OO00O0OOO in O0OO0O00O0O000O00 :#line:12
            OOO00O00O0OO000O0 =[]#line:13
            print (f"------------正在执行第{O0OO0O00O0O000O00.index(OO0OOOO0OO00O0OOO) + 1}个账号------------")#line:14
            OO0OO00O000OO0O00 =CityEarth (OO0OOOO0OO00O0OOO ,OOO00O00O0OO000O0 )#line:15
            def O000O0OOO00O0O000 ():#line:17
                if OO0OO00O000OO0O00 .base_info ():#line:19
                    OO0OO00O000OO0O00 .sealing ()#line:21
                    OO0OO00O000OO0O00 .invitenum ()#line:23
                    OO0OO00O000OO0O00 .game_map ()#line:25
                    OO0OO00O000OO0O00 .friends_invitation ()#line:27
                    OO0OO00O000OO0O00 .energy ()#line:29
                    OO0OO00O000OO0O00 .add_clover ()#line:31
                    OO0OO00O000OO0O00 .propsraffle ()#line:33
                    OO0OO00O000OO0O00 .synthetic ()#line:35
                    OO0OO00O000OO0O00 .crops_illustrated ()#line:37
                    OO0OO00O000OO0O00 .give_gold ()#line:39
                    OO0OO00O000OO0O00 .withdraw ()#line:41
            O0000OO0O00O000O0 =threading .Thread (target =O000O0OOO00O0O000 )#line:43
            O0000OO0O00O000O0 .start ()#line:44
            time .sleep (time_xx )#line:45
        print (f"------------正在处理推送通知------------")#line:46
        time .sleep (0.5 )#line:47
        O0O00OOOO0OO0OO0O =format_msg ()#line:48
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O00OOOO0OO0OO0O +' ')#line:49
    except Exception as O0O0OO0OOO00O000O :#line:50
        print (O0O0OO0OOO00O000O )#line:51
def give_gold (O0O0OO00OO0O000OO ,OO0OO0OOO0OO0OO0O ):#line:54
        try :#line:55
            O0000O000O0OO0000 =f'_doneeNo={O0O0OO00OO0O000OO}&quantity={int(OO0OO0OOO0OO0OO0O)}_{timi_new()}'#line:56
            O0OOOOO00O0OOO000 ={'source':'scsc','authorization':os_qinglong ()[0 ].split ('&')[0 ],'timestamp':str (timi_new ()),'sign':sign (O0000O000O0OO0000 ),'signstring':O0000O000O0OO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:67
            O000OOOOOOO0000O0 ={"quantity":int (OO0OO0OOO0OO0OO0O ),"doneeNo":O0O0OO00OO0O000OO }#line:71
            O00O000OO000O00O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0OOOOO00O0OOO000 ,data =O000OOOOOOO0000O0 ).json ()#line:72
            if 'status'in O00O000OO000O00O0 :#line:74
                if O00O000OO000O00O0 ['status']==200 :#line:75
                    if O00O000OO000O00O0 ['data']:#line:76
                        print (f'【赠送种子】:赠送{int(OO0OO0OOO0OO0OO0O)}种子给{O0O0OO00OO0O000OO}成功')#line:77
                        return True #line:78
                if O00O000OO000O00O0 ['status']==401 :#line:79
                    print (f'【赠送种子】:{O00O000OO000O00O0["message"]}')#line:80
                    return False #line:81
                if O00O000OO000O00O0 ['status']==500 :#line:82
                    print (f'【赠送种子】:{O00O000OO000O00O0["message"]}')#line:83
                    return False #line:84
            return False #line:85
        except Exception as OOOO0O0OO0000O000 :#line:86
            print (OOOO0O0OO0000O000 )#line:87
def sign (O0O0OOOO00OOOO0OO ):#line:90
    O0OOOO0OO0OOOOOOO =hashlib .md5 (O0O0OOOO00OOOO0OO .encode ()).hexdigest ()#line:91
    O0OO00OO0OOOO000O ="scsc%^&*"+O0OOOO0OO0OOOOOOO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:92
    O00OO000000O0OOO0 =hashlib .md5 (O0OO00OO0OOOO000O .encode ()).hexdigest ()#line:93
    return O00OO000000O0OOO0 #line:94
def format_msg ():#line:96
    OO0OOO000O000OOOO =""#line:97
    for OO000O00O0OOOO0O0 in msg_list :#line:98
        OO0OOO000O000OOOO +=str (OO000O00O0OOOO0O0 )+"\r\n"#line:99
    return OO0OOO000O000OOOO #line:100
def timi_new ():#line:102
    return str (int (time .time ()*1000 ))#line:103
class CityEarth :#line:106
    def __init__ (OOO0OO0O0OOOO0OOO ,OOOO0O0O0OOO0O0O0 ,OO0O00O000O0OO0OO ):#line:108
        try :#line:109
            OOO0OO0O0OOOO0OOO .msg =OO0O00O000O0OO0OO #line:110
            OOO0OO0O0OOOO0OOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:111
            OOO0OO0O0OOOO0OOO .token =OOOO0O0O0OOO0O0O0 .split ('&')[0 ]#line:112
            OOO0OO0O0OOOO0OOO .innerId =OOOO0O0O0OOO0O0O0 .split ('&')[1 ]#line:113
            OOO0OO0O0OOOO0OOO .doneeNo =OOOO0O0O0OOO0O0O0 .split ('&')[2 ]#line:114
        except :#line:115
            print ('变量格式错误')#line:116
    def base_info (O00OOO0000OOOO00O ):#line:119
        try :#line:120
            O00OOO0000OOOO00O .watched_ad ()#line:122
            OOOOO0OO00OOO0O0O =f'__{timi_new()}'#line:123
            O0O0OO0000O00OOO0 ={'source':'scsc','authorization':O00OOO0000OOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OO00OOO0O0O ),'signstring':OOOOO0OO00OOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:134
            OOO0O0O0O0OOO0O0O =requests .request ('get',f'{host}/user',headers =O0O0OO0000O00OOO0 ).json ()#line:135
            if 'status'in OOO0O0O0O0OOO0O0O :#line:137
                if OOO0O0O0O0OOO0O0O ['status']==200 :#line:138
                    OOOO00OO00OO00O00 =OOO0O0O0O0OOO0O0O ['data']['nickname']#line:139
                    O00000O0O000O0O0O =OOO0O0O0O0OOO0O0O ['data']['inner_id']#line:140
                    OOOOOO0OOO0000OO0 =OOO0O0O0O0OOO0O0O ['data']['assets']['gold']#line:141
                    O00O00OOOO0O0OO0O =OOO0O0O0O0OOO0O0O ['data']['level']#line:142
                    print (f'【账号信息】:昵称:{OOOO00OO00OO00O00[:5]}丨ID:{O00000O0O000O0O0O}丨等级:{O00O00OOOO0O0OO0O}丨金种子:{str(OOOOOO0OOO0000OO0).split(".")[0]}')#line:143
                if OOO0O0O0O0OOO0O0O ['status']==401 :#line:144
                    print (OOO0O0O0O0OOO0O0O ['message'])#line:145
                    O00OOO0000OOOO00O .msg .append ('有账号失效了')#line:146
                    return False #line:147
                if OOO0O0O0O0OOO0O0O ['status']==500 :#line:148
                    return False #line:149
            return True #line:150
        except Exception as O0O0O000OO0OO0O00 :#line:151
            print (O0O0O000OO0OO0O00 )#line:152
    def sealing (O0OOO0OO0O0000000 ):#line:155
        try :#line:156
            O000000OOOO0OO000 =f'__{timi_new()}'#line:157
            O00OOOO0O00O0OO00 ={'source':'scsc','authorization':O0OOO0OO0O0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000OOOO0OO000 ),'signstring':O000000OOOO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:168
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00OOOO0O00O0OO00 )#line:169
            requests .request ('get',f'{host}/packsack/list',headers =O00OOOO0O00O0OO00 )#line:170
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00OOOO0O00O0OO00 )#line:171
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00OOOO0O00O0OO00 )#line:172
            requests .request ('get',f'{host}/user',headers =O00OOOO0O00O0OO00 )#line:173
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00OOOO0O00O0OO00 )#line:174
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00OOOO0O00O0OO00 )#line:175
            requests .request ('post',f'{host}/announcement/announcement',headers =O00OOOO0O00O0OO00 )#line:176
            requests .request ('get',f'{host}/game/getAllData',headers =O00OOOO0O00O0OO00 )#line:177
            requests .request ('get',f'{host}/assets',headers =O00OOOO0O00O0OO00 )#line:178
        except Exception as OO0000O000OOOOOO0 :#line:179
            print (OO0000O000OOOOOO0 )#line:180
    def withdraw (OO0OO000O00O0O0OO ):#line:184
        OOOO0O000O0OOO0OO =f'__{timi_new()}'#line:185
        O0O00O0000O0O0OO0 ={'source':'scsc','authorization':OO0OO000O00O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O000O0OOO0OO ),'signstring':OOOO0O000O0OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:196
        O000O0000O0O0O00O =requests .request ('get',f'{host}/assets',headers =O0O00O0000O0O0OO0 ).json ()#line:197
        if 'status'in O000O0000O0O0O00O :#line:199
            if O000O0000O0O0O00O ['status']==200 :#line:200
                O000O0OO000OOO00O =O000O0000O0O0O00O ['data']['cash']#line:201
                if float (O000O0OO000OOO00O )>20 :#line:202
                    OOOO0O000O0OOO0OO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:203
                    O0O00O0000O0O0OO0 ={'authorization':OO0OO000O00O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O000O0OOO0OO ),'signstring':OOOO0O000O0OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:213
                    O0000000O00OOO0O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:214
                    OO0000O00OO0O00O0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O00O0000O0O0OO0 ,data =O0000000O00OOO0O0 ).json ()#line:216
                    print (OO0000O00OO0O00O0 )#line:217
    def invitenum (OO00O0O000O0OOO00 ):#line:220
        O0OOOOO0OOOOOO000 =f'__{timi_new()}'#line:221
        OOO0OOO0O0OO00000 ={'source':'scsc','authorization':OO00O0O000O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0OOOOOO000 ),'signstring':O0OOOOO0OOOOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:232
        OO0OOOOOOO0OO00O0 =requests .request ('get',f'{host}/invite/invitenum',headers =OOO0OOO0O0OO00000 ).json ()#line:233
        if 'status'in OO0OOOOOOO0OO00O0 :#line:235
            if OO0OOOOOOO0OO00O0 ['status']==200 :#line:236
                O0OO0OO0O00OOOO0O =OO0OOOOOOO0OO00O0 ['data']['invited_count']#line:237
                O00O0OO00O0O00O0O =OO0OOOOOOO0OO00O0 ['data']['invited_second_count']#line:238
                print (f'【我的邀请】:直邀好友:{O0OO0OO0O00OOOO0O}丨间邀好友:{O00O0OO00O0O00O0O}')#line:239
    def game_map (OO00OOOO0O00O0OO0 ):#line:242
        try :#line:243
            O00O0OO00O0O0O000 =f'__{timi_new()}'#line:244
            O0000OO0O000O0O0O ={'source':'scsc','authorization':OO00OOOO0O00O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO00O0O0O000 ),'signstring':O00O0OO00O0O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:255
            OOO0O0O0OO00OO000 =requests .request ('get',f'{host}/game/map',headers =O0000OO0O000O0O0O ).json ()#line:256
            if 'status'in OOO0O0O0OO00OO000 :#line:258
                if OOO0O0O0OO00OO000 ['status']==200 :#line:259
                    for O0OOOOOOOOO000O00 in OOO0O0O0OO00OO000 ['data']['list'][0 ]['crops']:#line:260
                        OO0000OOOO0O0O0O0 =O0OOOOOOOOO000O00 ['level']#line:262
                        if OO0000OOOO0O0O0O0 ==41 :#line:263
                            O0OOO000OO0000O00 =O0OOOOOOOOO000O00 ['crop_name']#line:264
                            O00OO00000OOO00OO =O0OOOOOOOOO000O00 ['count']#line:265
                            if O00OO00000OOO00OO >0 :#line:266
                                print (f'【农业资产】:{O0OOO000OO0000O00}丨数量:{O00OO00000OOO00OO}')#line:267
        except Exception as OOOO0O00O000OO0O0 :#line:268
            print (OOOO0O00O000OO0O0 )#line:269
    def give_gold (OO000O000000OOO0O ):#line:272
        try :#line:273
            O00OOO0OOOOO0OO0O =f'__{timi_new()}'#line:274
            OO0O0O0O000OOO0O0 ={'source':'scsc','authorization':OO000O000000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OOOOO0OO0O ),'signstring':O00OOO0OOOOO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:285
            OOO00O00O000OOO0O =requests .request ('get',f'{host}/user',headers =OO0O0O0O000OOO0O0 ).json ()#line:286
            if 'status'in OOO00O00O000OOO0O :#line:287
                if OOO00O00O000OOO0O ['status']==200 :#line:288
                    if float (OO000O000000OOO0O .doneeNo )!=0 :#line:289
                        O0O00O0000OO0OOO0 =OOO00O00O000OOO0O ['data']['assets']['gold']#line:290
                        if float (O0O00O0000OO0OOO0 )>float (OO000O000000OOO0O .innerId ):#line:291
                            OO0O0OOOOOOOO00OO =int (float (O0O00O0000OO0OOO0 )/1.1 )#line:292
                            O00OOO0OOOOO0OO0O =f'_doneeNo={OO000O000000OOO0O.doneeNo}&quantity={OO0O0OOOOOOOO00OO}_{timi_new()}'#line:293
                            OO0O0O0O000OOO0O0 ={'source':'scsc','authorization':OO000O000000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OOOOO0OO0O ),'signstring':O00OOO0OOOOO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:304
                            OOO0O0O0OOO0O0OO0 ={"quantity":OO0O0OOOOOOOO00OO ,"doneeNo":OO000O000000OOO0O .doneeNo }#line:308
                            O0OOOOOO0O0O000O0 =requests .request ('post',f'{host}/finance/give-gold',headers =OO0O0O0O000OOO0O0 ,data =OOO0O0O0OOO0O0OO0 ).json ()#line:309
                            if 'status'in O0OOOOOO0O0O000O0 :#line:311
                                if O0OOOOOO0O0O000O0 ['status']==200 :#line:312
                                    if O0OOOOOO0O0O000O0 ['data']:#line:313
                                        print (f'【赠送种子】:赠送{OO0O0OOOOOOOO00OO}种子给{OO000O000000OOO0O.doneeNo}成功')#line:314
                    else :#line:315
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:316
        except Exception as O00O0O0OO0OO00OO0 :#line:317
            print (O00O0O0OO0OO00OO0 )#line:318
    def invitation (O00O0000O00O00O0O ):#line:320
        try :#line:321
            _O0O000OO0O0O000O0 =float (bundled_def ())/4 #line:322
            O0OO00OOOOO000000 =f'_innerId={int(_O0O000OO0O0O000O0)}_{timi_new()}'#line:323
            O00OOOOO000OO00O0 ={'source':'scsc','authorization':O00O0000O00O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OOOOO000000 ),'signstring':O0OO00OOOOO000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:334
            O0O000000OOOO0O00 ={"innerId":int (_O0O000OO0O0O000O0 )}#line:335
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00OOOOO000OO00O0 ,data =O0O000000OOOO0O00 )#line:336
        except Exception as O0O000O000O0OOO00 :#line:337
            print (O0O000O000O0OOO00 )#line:338
    def winning_rewards (OOO00OOOO00OO000O ):#line:341
        try :#line:342
            OOO0O0O000000OOO0 =f'__{timi_new()}'#line:343
            O0O0000OOOOOO0OO0 ={'source':'scsc','authorization':OOO00OOOO00OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O000000OOO0 ),'signstring':OOO0O0O000000OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:354
            OO0O0OO0OOOO0O0OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O0000OOOOOO0OO0 ).json ()#line:355
            if 'status'in OO0O0OO0OOOO0O0OO :#line:357
                if OO0O0OO0OOOO0O0OO ['status']==200 :#line:358
                    if OO0O0OO0OOOO0O0OO ['data']['amount']:#line:359
                        O000OOO00O000O000 =OO0O0OO0OOOO0O0OO ['data']['amount']['gold']#line:360
                        return O000OOO00O000O000 #line:361
                    else :#line:362
                        return 0 #line:363
        except Exception as OO0O0OO0000OOOOOO :#line:364
            print (OO0O0OO0000OOOOOO )#line:365
    def certification (O0OO00O0OO0OO0O00 ):#line:368
        try :#line:369
            OOOO0O00O0000000O =f'__{timi_new()}'#line:370
            O00000OO00O0OO0OO ={'source':'scsc','authorization':O0OO00O0OO0OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00O0000000O ),'signstring':OOOO0O00O0000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:381
            O00OOO0OOO00O0OOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00000OO00O0OO0OO ).json ()#line:382
            if 'status'in O00OOO0OOO00O0OOO :#line:384
                if O00OOO0OOO00O0OOO ['status']==200 :#line:385
                    if O00OOO0OOO00O0OOO ['data']['result']:#line:386
                        OO00O000O0O0OOO0O =O00OOO0OOO00O0OOO ['data']['nick_name']#line:387
                        return OO00O000O0O0OOO0O #line:388
                    else :#line:389
                        return '未实名'#line:390
        except Exception as O0OOOOOOOOOO00O0O :#line:391
            print (O0OOOOOOOOOO00O0O )#line:392
    def crops_illustrated (O0O0O00O0O00O0O0O ):#line:395
        try :#line:396
            OO00O0O00OO0000O0 =f'__{timi_new()}'#line:397
            OO000OO00O0O00OOO ={'source':'scsc','authorization':O0O0O00O0O00O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O00OO0000O0 ),'signstring':OO00O0O00OO0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            O00OO0O0OOOOO00O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO000OO00O0O00OOO ).json ()#line:409
            if 'status'in O00OO0O0OOOOO00O0 :#line:411
                if O00OO0O0OOOOO00O0 ['status']==200 :#line:412
                    O0OO0O00OOO0OO00O =O00OO0O0OOOOO00O0 ['data'][0 ]['crops']#line:413
                    for OO0OOOO0O0000O00O in O0OO0O00OOO0OO00O :#line:414
                        if OO0OOOO0O0000O00O ['ill_clover_award']:#line:415
                            if float (OO0OOOO0O0000O00O ['ill_clover_award'])>1 :#line:416
                                if OO0OOOO0O0000O00O ['is_finish']:#line:417
                                    if not OO0OOOO0O0000O00O ['is_getit']:#line:418
                                        if O0O0O00O0O00O0O0O .certification ()!='未实名':#line:419
                                            OO00O0O00OO0000O0 =f'_award_level={OO0OOOO0O0000O00O["level"]}_{timi_new()}'#line:420
                                            OO000OO00O0O00OOO ={'source':'scsc','authorization':O0O0O00O0O00O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O00OO0000O0 ),'signstring':OO00O0O00OO0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:431
                                            O000OO00OO0O0O0O0 ={"award_level":OO0OOOO0O0000O00O ['level']}#line:432
                                            O0000O00OO0OOOO0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO000OO00O0O00OOO ,json =O000OO00OO0O0O0O0 ).json ()#line:434
                                            if 'status'in O0000O00OO0OOOO0O :#line:435
                                                if O0000O00OO0OOOO0O ['status']==200 :#line:436
                                                    OOOOOO0OO00O0OO00 =O0000O00OO0OOOO0O ['data']['ill_clover_award']#line:437
                                                    print (f'【图鉴奖励】:领取{OO0OOOO0O0000O00O["crop_name"]}成就丨奖励{OOOOOO0OO00O0OO00}☘️')#line:439
                                                if O0000O00OO0OOOO0O ['status']==500 :#line:440
                                                    print (f'【图鉴奖励】:{O0000O00OO0OOOO0O["message"]}')#line:441
        except Exception as O0OO0O000OOOOOO00 :#line:442
            print (O0OO0O000OOOOOO00 )#line:443
    def watched_ad (O00OO0OOO0OO00000 ):#line:446
        try :#line:447
            OOO00OOOO0OOOOOOO =f'__{timi_new()}'#line:448
            OO0OOO0O0000O0O00 ={'source':'scsc','authorization':O00OO0OOO0OO00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOOO0OOOOOOO ),'signstring':OOO00OOOO0OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:459
            OOO00OO00OO0OO00O =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOO0O0000O0O00 ).json ()#line:460
            if 'status'in OOO00OO00OO0OO00O :#line:462
                if OOO00OO00OO0OO00O ['status']==200 :#line:463
                    if 'offlineInfo'in OOO00OO00OO0OO00O ['data']:#line:464
                        time .sleep (random .randint (3 ,5 ))#line:465
                        OOO0OOO00O0O000OO =OOO00OO00OO0OO00O ['data']['offlineInfo']['off_minute']#line:466
                        O0OO0OOOO00O0O000 =float (OOO00OO00OO0OO00O ['data']['silver'])/1000000000000 #line:467
                        time .sleep (1 )#line:468
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0OOO0O0000O0O00 ).json ()#line:469
                        time .sleep (2 )#line:470
                        O0OO000000000000O =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOO0O0000O0O00 ).json ()#line:471
                        if 'status'in O0OO000000000000O :#line:473
                            if O0OO000000000000O ['status']==200 :#line:474
                                OOO00OOO00O000O0O =float (O0OO000000000000O ['data']['silver'])/1000000000000 #line:475
                                O00000OOO0OO0OOO0 =str (OOO00OOO00O000O0O -O0OO0OOOO00O0O000 )[:6 ]#line:476
                                print (f'【离线奖励】:翻倍离线{OOO0OOO00O0O000OO}分钟奖励🌱数量:{O00000OOO0OO0OOO0}t粒')#line:477
        except Exception as O00000O0OOO0O00O0 :#line:478
            print (O00000O0OOO0O00O0 )#line:479
    def user_ad (OO0O000OOOOO0OOO0 ):#line:482
        try :#line:483
            OO00O00OO00OO000O =f'__{timi_new()}'#line:484
            O0O0OOOO00OO0OO00 ={'source':'scsc','authorization':OO0O000OOOOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO00OO000O ),'signstring':OO00O00OO00OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:495
            OO000O00OO0000000 =requests .request ('get',f'{host}/user/ad',headers =O0O0OOOO00OO0OO00 ).json ()#line:496
            if 'status'in OO000O00OO0000000 :#line:498
                if OO000O00OO0000000 ['status']==200 :#line:499
                    OO0O0O0O0O0OO0OO0 =OO000O00OO0000000 ['data']['max_time']#line:500
                    OOOO000OO0OOOO000 =OO000O00OO0000000 ['data']['watch_time']#line:501
                    O0O0OO0OO0O0OO0O0 =OO000O00OO0000000 ['data']['added_time']#line:502
                    print (f'【获取种子】:获取🌱剩余{O0O0OO0OO0O0OO0O0 + OO0O0O0O0O0OO0OO0 - OOOO000OO0OOOO000}次丨好友提供:{O0O0OO0OO0O0OO0O0}次')#line:503
                    if O0O0OO0OO0O0OO0O0 +OO0O0O0O0O0OO0OO0 -OOOO000OO0OOOO000 >0 :#line:504
                        time .sleep (random .randint (16 ,19 ))#line:505
                        OO0OOOOOOO00O0OO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O0OOOO00OO0OO00 ).json ()#line:506
                        if 'status'in OO0OOOOOOO00O0OO0 :#line:508
                            if OO0OOOOOOO00O0OO0 ['status']==200 :#line:509
                                O0O0O0000OOO0OO0O =float (OO0OOOOOOO00O0OO0 ['data']['silver'])/1000000000000 #line:510
                                print (f'【获取种子】:获得🌱:{int(O0O0O0000OOO0OO0O)}t粒')#line:511
                                return True #line:512
                            if OO0OOOOOOO00O0OO0 ['status']==500 :#line:513
                                O00OOOOO00O0O0000 =OO0OOOOOOO00O0OO0 ['message']#line:514
                                print (f'【获取种子】:{O00OOOOO00O0O0000}')#line:515
                                return False #line:516
        except Exception as OO00O00O0000OO0O0 :#line:517
            print (OO00O00O0000OO0O0 )#line:518
    def synthetic (O0OO00O0O0O00000O ):#line:521
        global id ,g #line:522
        try :#line:523
            OOO0O000O0O0000OO =O0OO00O0O0O00000O .level_new ()#line:524
            OO000OOO0OO000O00 =random .randint (9 ,11 )#line:525
            OO0O0O0OOO000O00O =f'_site=8&targetSite={OO000OOO0OO000O00}_{timi_new()}'#line:526
            O00O000O00OO00OO0 ={'source':'scsc','authorization':O0OO00O0O0O00000O .token ,'timestamp':timi_new (),'sign':sign (OO0O0O0OOO000O00O ),'signstring':OO0O0O0OOO000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:537
            OO0OO000OO0OOOO00 ={"site":int (8 ),"targetSite":int (OO000OOO0OO000O00 )}#line:538
            requests .request ('post',f'{host}/game/crops/move',headers =O00O000O00OO00OO0 ,json =OO0OO000OO0OOOO00 )#line:539
            while True :#line:540
                O0O0O0OO0O0O0OOOO =f'__{timi_new()}'#line:541
                O00O0OO0OOOOO0OO0 ={'source':'scsc','authorization':O0OO00O0O0O00000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO0O0O0OOOO ),'signstring':O0O0O0OO0O0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:552
                OO0O000O0O00OO00O =requests .request ('get',f'{host}/game/getAllData',headers =O00O0OO0OOOOO0OO0 ).json ()#line:553
                if 'status'in OO0O000O0O00OO00O :#line:555
                    if OO0O000O0O00OO00O ['status']==200 :#line:556
                        OO000OO0O0O0O00O0 =OO0O000O0O00OO00O ['data']['cropList']#line:557
                        OO00O0O000OO0O0OO =OO0O000O0O00OO00O ['data']['gameCoreDataDBid']#line:558
                        O0OO00O00O0O00OO0 =float (OO0O000O0O00OO00O ['data']['silver'])/1000000000000 #line:559
                        O0OO0O000O0OOO0O0 =0 #line:564
                        for OOOO0O00O00OO0000 in OO000OO0O0O0O00O0 :#line:565
                            if not OOOO0O00O00OO0000 :#line:566
                                O0O0OOOO0OOO00O00 =f'_crop_id={OO00O0O000OO0O0OO}&site={O0OO0O000O0OOO0O0}_{O0OO00O0O0O00000O.time}'#line:567
                                OO0OOO0000O0000OO ={'source':'scsc','authorization':O0OO00O0O0O00000O .token ,'timestamp':O0OO00O0O0O00000O .time ,'sign':sign (O0O0OOOO0OOO00O00 ),'signstring':O0O0OOOO0OOO00O00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:577
                                OO00OOOOO0O000OO0 ={"site":O0OO0O000O0OOO0O0 ,"crop_id":OO00O0O000OO0O0OO }#line:578
                                OOO0O000OOO0O0O0O =requests .request ('post',f'{host}/game/crops/buy',headers =OO0OOO0000O0000OO ,data =OO00OOOOO0O000OO0 ).json ()#line:579
                                time .sleep (random .randint (1 ,3 )/10 )#line:581
                                if 'status'in OOO0O000OOO0O0O0O :#line:582
                                    if OOO0O000OOO0O0O0O ['status']==200 :#line:583
                                        if OOO0O000OOO0O0O0O ['message']=='种子数量不足':#line:584
                                            OOO0O000O0O0000OO =O0OO00O0O0O00000O .level_new ()#line:585
                                            print (f'【种植合成】:{OOO0O000OOO0O0O0O["message"]}')#line:586
                                            if not O0OO00O0O0O00000O .user_ad ():#line:587
                                                return False #line:588
                                    if OOO0O000OOO0O0O0O ['status']==500 :#line:589
                                        print (f'【种植合成】:{OOO0O000OOO0O0O0O["message"]}')#line:590
                                        return False #line:591
                            O0OO0O000O0OOO0O0 +=1 #line:592
                        OO0O00O0OOOOOO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =O00O0OO0OOOOO0OO0 ).json ()#line:593
                        OO000OO0O0OOO0O0O =OO0O00O0OOOOOO0O0 ['data']['cropList']#line:594
                        O0O00OO0O00OO00O0 =False #line:595
                        for OOOO0O00O00OO0000 in range (12 ):#line:596
                            id =OO000OO0O0OOO0O0O [OOOO0O00O00OO0000 ]['level']#line:597
                            if float (OOO0O000O0O0000OO )-float (id )>9 :#line:598
                                OO0O00OO0O0OOO00O =f'_site={OOOO0O00O00OO0000}_{timi_new()}'#line:599
                                O0000O0OO00OOOOOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0OO00O0O0O00000O .token ,'timestamp':timi_new (),'sign':sign (OO0O00OO0O0OOO00O ),'signstring':OO0O00OO0O0OOO00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:610
                                OOO0OOO0OOO0O0OO0 ={"site":OOOO0O00O00OO0000 }#line:611
                                OOO00O000000O0OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0000O0OO00OOOOOO ,data =OOO0OOO0OOO0O0OO0 ).json ()#line:613
                                if 'status'in OOO00O000000O0OOO :#line:614
                                    if OOO00O000000O0OOO ['status']==200 :#line:615
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:616
                            if id !=0 :#line:617
                                for O00O0O0OOO0O00O00 in range (11 ):#line:618
                                    O00OOO0O00OOOO0OO =O00O0O0OOO0O00O00 +1 #line:619
                                    g =OO000OO0O0OOO0O0O [O00OOO0O00OOOO0OO ]['level']#line:620
                                    if id ==g :#line:621
                                        O000O0OOO0O0OOO0O =O00O0O0OOO0O00O00 +2 #line:622
                                        if O000O0OOO0O0OOO0O !=OOOO0O00O00OO0000 +1 :#line:623
                                            O0OOO0OOO0000O0O0 =OOOO0O00O00OO0000 +1 #line:624
                                            time .sleep (random .randint (1 ,3 )/10 )#line:626
                                            OO0O0O0OOO000O00O =f'_site={O0OOO0OOO0000O0O0 - 1}&targetSite={O000O0OOO0O0OOO0O - 1}_{timi_new()}'#line:627
                                            O00O000O00OO00OO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0OO00O0O0O00000O .token ,'timestamp':timi_new (),'sign':sign (OO0O0O0OOO000O00O ),'signstring':OO0O0O0OOO000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:644
                                            O000O000OOO000O0O ={"site":int (O0OOO0OOO0000O0O0 -1 ),"targetSite":int (O000O0OOO0O0OOO0O -1 )}#line:645
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00O000O00OO00OO0 ,json =O000O000OOO000O0O )#line:646
                                            O0O00OO0O00OO00O0 =True #line:648
                                    if O0O00OO0O00OO00O0 :#line:649
                                        break #line:650
                                if O0O00OO0O00OO00O0 :#line:651
                                    break #line:652
        except :#line:653
            O0OO00O0O0O00000O .synthetic ()#line:654
    def level_new (OO0OO00000OO0O00O ):#line:657
        try :#line:658
            OOOOOOOO0OOOO00OO =f'__{timi_new()}'#line:659
            OOOOOOOOOO00O0OO0 ={'source':'scsc','authorization':OO0OO00000OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO0OOOO00OO ),'signstring':OOOOOOOO0OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:670
            OO0OO0O0O0000OO0O =requests .request ('get',f'{host}/user',headers =OOOOOOOOOO00O0OO0 ).json ()#line:671
            if 'status'in OO0OO0O0O0000OO0O :#line:672
                if OO0OO0O0O0000OO0O ['status']==200 :#line:673
                    return float (OO0OO0O0O0000OO0O ['data']['level'])#line:674
        except Exception as OOOO0OO00000000O0 :#line:675
            print (OOOO0OO00000000O0 )#line:676
    def propsraffle (O0O0OO0OO00000000 ):#line:679
        try :#line:680
            while True :#line:681
                OO000O000O00OO0O0 =f'__{timi_new()}'#line:682
                O0O00OOO000O0O00O ={'source':'scsc','authorization':O0O0OO0OO00000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O000O00OO0O0 ),'signstring':OO000O000O00OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:693
                OOO000O0OOOOO0O00 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O00OOO000O0O00O ).json ()#line:694
                if 'status'in OOO000O0OOOOO0O00 :#line:696
                    if OOO000O0OOOOO0O00 ['status']==200 :#line:697
                        O0O0000OOOOOO0O0O =OOO000O0OOOOO0O00 ['data']['rows']#line:698
                        O000OO0O0OOO0O00O =OOO000O0OOOOO0O00 ['data']['vstate']#line:699
                        if O0O0000OOOOOO0O0O ==5 or O0O0000OOOOOO0O0O ==6 or O0O0000OOOOOO0O0O ==7 :#line:700
                            O00O0OO0O000O00O0 =OOO000O0OOOOO0O00 ['data']['silver']#line:701
                            print (f'【转盘抽奖】:获得种子:{O00O0OO0O000O00O0}')#line:702
                        if O0O0000OOOOOO0O0O ==1 or O0O0000OOOOOO0O0O ==2 or O0O0000OOOOOO0O0O ==3 :#line:703
                            OO00O00OO000O00OO =OOO000O0OOOOO0O00 ['data']['clover']#line:704
                            print (f'【转盘抽奖】:获得三叶草:{OO00O00OO000O00OO}')#line:705
                        if O0O0000OOOOOO0O0O ==4 or O0O0000OOOOOO0O0O ==8 :#line:706
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:707
                        if O0O0000OOOOOO0O0O =='抽奖次数已用完':#line:711
                            break #line:745
                time .sleep (random .randint (8 ,15 )/10 )#line:746
        except Exception as O0OO0O000O0O00000 :#line:747
            print (O0OO0O000O0O00000 )#line:748
    def friends_invitation (OOO000O0OOO0OO0OO ):#line:751
        try :#line:752
            O0O00O000OOOOOO0O =f'__{timi_new()}'#line:753
            O00OOO00OOO00O000 ={'source':'scsc','authorization':OOO000O0OOO0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O000OOOOOO0O ),'signstring':O0O00O000OOOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:764
            OO000OO0O0OOO0OOO =requests .request ('get',f'{host}/friends',headers =O00OOO00OOO00O000 ).json ()#line:765
            if 'status'in OO000OO0O0OOO0OOO :#line:766
                if OO000OO0O0OOO0OOO ['status']==200 :#line:767
                    OOO0O00OO0OOOO00O =OO000OO0O0OOO0OOO ['data']['myInviteter']#line:768
                    if OOO0O00OO0OOOO00O :#line:769
                        O00OOOOO0000O0OO0 =OOO0O00OO0OOOO00O ['user']['nickname']#line:770
                        O0OO000OO00O0000O =OOO000O0OOO0OO0OO .certification ()#line:771
                        print (f'【查邀请人】:我的邀请人:{O00OOOOO0000O0OO0}丨实名:{O0OO000OO00O0000O}')#line:772
                    else :#line:773
                        if OOO000O0OOO0OO0OO .innerId !='0':#line:774
                            OOO000O0OOO0OO0OO .invitation ()#line:775
        except Exception as O0000O0OO0O0O000O :#line:776
            print (O0000O0OO0O0O000O )#line:777
    def add_clover (O00OO000O00000000 ):#line:780
        global golden_seed #line:781
        try :#line:782
            O0OOO0O00O000O00O =f'__{timi_new()}'#line:783
            O0OO0O00OO0O0O000 ={'source':'scsc','authorization':O00OO000O00000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O00O000O00O ),'signstring':O0OOO0O00O000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
            OOOOO0O0OO000O000 =requests .request ('get',f'{host}/assets/clovers',headers =O0OO0O00OO0O0O000 ).json ()#line:795
            if 'status'in OOOOO0O0OO000O000 :#line:797
                if OOOOO0O0OO000O000 ['status']==200 :#line:798
                    OO00OO0O0O0OO000O =OOOOO0O0OO000O000 ['data']['clover']#line:799
                    OO00O00OO0OOO0000 =OOOOO0O0OO000O000 ['data']['used_clover']#line:800
                    OOOOOOO0OO00O0O0O =float (OO00OO0O0O0OO000O )-float (OO00O00OO0OOO0000 )#line:801
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO00O00OO0OOO0000}')#line:802
                    if O00OO000O00000000 .certification ()!='未实名':#line:803
                        if OOOOOOO0OO00O0O0O >1 :#line:804
                            O0OOO0O00O000O00O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOOOOO0OO00O0O0O)}_{timi_new()}'#line:805
                            OO0000000OOOOOO0O ={'source':'scsc','authorization':O00OO000O00000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O00O000O00O ),'signstring':O0OOO0O00O000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:816
                            OO000O0O0OOOOOOO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOOOOO0OO00O0O0O )}#line:817
                            OOO0O00OOO0OOOO00 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0000000OOOOOO0O ,data =OO000O0O0OOOOOOO0 ).json ()#line:818
                            if 'status'in OOO0O00OOO0OOOO00 :#line:820
                                if OOO0O00OOO0OOOO00 ['status']==200 :#line:821
                                    print (f'【参与抽奖】:添加☘️:{OOO0O00OOO0OOOO00["data"]}丨数量:{OOOOOOO0OO00O0O0O}')#line:822
                                if OOO0O00OOO0OOOO00 ['status']==500 :#line:823
                                    print (f'【参与抽奖】:添加☘️:{OOO0O00OOO0OOOO00["message"]}')#line:824
            OO0O0OO000OO000O0 =requests .request ('get',f'{host}/lottery',headers =O0OO0O00OO0O0O000 ).json ()#line:825
            O0OOOO0O0OOO0O0OO =O00OO000O00000000 .winning_rewards ()#line:827
            if 'status'in OO0O0OO000OO000O0 :#line:828
                if OO0O0OO000OO000O0 ['status']==200 :#line:829
                    OOO0O00OOOOOO00O0 =OO0O0OO000OO000O0 ['data'][0 ]['day_get_gold_quantity']#line:830
                    golden_seed +=float (OOO0O00OOOOOO00O0 )#line:831
                    OOOO00OOOOOOOO00O =OO0O0OO000OO000O0 ['data'][1 ]['value']#line:832
                    O00OOOO0OOOOO0O0O =OO0O0OO000OO000O0 ['data'][0 ]['join_number']#line:833
                    OO000O0O0OOO0O0O0 =int (float (OO0O0OO000OO000O0 ['data'][0 ]['totalValue']))#line:834
                    OOO0O00OOOOO0O0O0 =float (OOOO00OOOOOOOO00O /OO000O0O0OOO0O0O0 )*10000 #line:835
                    O0OOOOOOOOOOO0000 =OO000O0O0OOO0O0O0 /O00OOOO0OOOOO0O0O #line:836
                    print (f'【参与抽奖】:预计每天中{str(OOO0O00OOOOOO00O0)[:6]}颗金种子丨好友收益:{str(O0OOOO0O0OOO0O0OO)[:6]}')#line:837
                    print (f'【抽奖统计】:每1万☘️中{str(OOO0O00OOOOO0O0O0)[:6]}颗金种子丨☘️人均:{str(O0OOOOOOOOOOO0000)[:7]}️')#line:838
        except Exception as OO0OOOO00000OO0OO :#line:839
            print (OO0OOOO00000OO0OO )#line:840
    def energy (O0OOO000OOOOO0O0O ):#line:844
        try :#line:845
            while True :#line:846
                O00000O000OO0O000 =f'__{timi_new()}'#line:847
                OOO00OO0OOO0O0O00 ={'source':'scsc','authorization':O0OOO000OOOOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O000OO0O000 ),'signstring':O00000O000OO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:858
                O00000O0O0OOO00OO =requests .request ('get',f'{host}/energy/general',headers =OOO00OO0OOO0O0O00 ).json ()#line:859
                if 'status'in O00000O0O0OOO00OO :#line:861
                    if O00000O0O0OOO00OO ['status']==200 :#line:862
                        OOO0O00OOO0OO0OO0 =O00000O0O0OOO00OO ['data']['ordinary_water']#line:863
                        O0000O00OOO0OO000 =O00000O0O0OOO00OO ['data']['ordinary_fertilizer']#line:864
                        OO0OO00OOO00OOOO0 =O00000O0O0OOO00OO ['data']['videoStatus']#line:865
                        O0000000O0000O0OO =O00000O0O0OOO00OO ['data']['waterVideoKey']#line:866
                        print (f'【我的营养】:肥料:{str(O0000O00OOO0OO000).split(".")[0]}丨水滴:{str(OOO0O00OOO0OO0OO0).split(".")[0]}')#line:867
                        if float (O0000O00OOO0OO000 )<96 :#line:868
                            if OO0OO00OOO00OOOO0 :#line:869
                                time .sleep (random .randint (160 ,180 )/10 )#line:870
                                O00O00O0O0OO0OOO0 =99 -float (O0000O00OOO0OO000 )#line:871
                                OOOOO000OO0O0O0O0 ={"fertilizer":str (O00O00O0O0OO0OOO0 ).split ('.')[0 ]}#line:872
                                O0O0OOOOOO0OOOO00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOO00OO0OOO0O0O00 ).json ()#line:873
                                if 'status'in O0O0OOOOOO0OOOO00 :#line:875
                                    if O0O0OOOOOO0OOOO00 ['status']==200 :#line:876
                                        print (f'【购买肥料】:看广告获取肥料:{O0O0OOOOOO0OOOO00["message"]}')#line:877
                                    if O0O0OOOOOO0OOOO00 ['status']==500 :#line:878
                                        print (f'【购买肥料】:看广告获取肥料:{O0O0OOOOOO0OOOO00["message"]}')#line:879
                                        break #line:880
                            if energy :#line:881
                                if float (O0000O00OOO0OO000 )<81 :#line:882
                                    O00O00O0O0OO0OOO0 =80 -float (O0000O00OOO0OO000 )#line:883
                                    OO0O00OO0000OOO00 =f'_fertilizer={int(O00O00O0O0OO0OOO0)}_{timi_new()}'#line:884
                                    O00O00OO0OO0OO00O ={'source':'scsc','authorization':O0OOO000OOOOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OO0000OOO00 ),'signstring':OO0O00OO0000OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:895
                                    OO0O000OO00OOO000 ={"fertilizer":int (O00O00O0O0OO0OOO0 )}#line:896
                                    O0O0O0O00000O000O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O00O00OO0OO0OO00O ,data =OO0O000OO00OOO000 ).json ()#line:897
                                    if 'status'in O0O0O0O00000O000O :#line:899
                                        if O0O0O0O00000O000O ['status']==200 :#line:900
                                            print (f'【购买肥料】:购买肥料:{O0O0O0O00000O000O["message"]}丨数量:{int(O00O00O0O0OO0OOO0)}')#line:901
                                        if O0O0O0O00000O000O ['status']==500 :#line:902
                                            print (f'【购买肥料】:购买肥料:{O0O0O0O00000O000O["message"]}丨数量:{int(O00O00O0O0OO0OOO0)}')#line:903
                                            O0OO000OO00OOO0OO =O0O0O0O00000O000O ["message"].split ('-')[1 ]#line:904
                                            O000O0OOO00O0OO0O =f'__{timi_new()}'#line:905
                                            OO0OOOOO0O00O0OO0 ={'source':'scsc','authorization':O0OOO000OOOOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOO00O0OO0O ),'signstring':O000O0OOO00O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:916
                                            O0OO0O0OO0O00O0OO =requests .request ('get',f'{host}/user',headers =OO0OOOOO0O00O0OO0 ).json ()#line:917
                                            if 'status'in O0OO0O0OO0O00O0OO :#line:918
                                                if O0OO0O0OO0O00O0OO ['status']==200 :#line:919
                                                    O00OOOO00OO00OO0O =O0OO0O0OO0O00O0OO ['data']['inner_id']#line:920
                                                    if give_gold (O00OOOO00OO00OO0O ,float (O0OO000OO00OOO0OO )+1 ):#line:921
                                                        O0OOO000OOOOO0O0O .energy ()#line:922
                        if float (OOO0O00OOO0OO0OO0 )<880 :#line:923
                            if O0000000O0000O0OO :#line:924
                                time .sleep (random .randint (160 ,180 )/10 )#line:925
                                O00OO0O0OO0OOO00O =999 -float (OOO0O00OOO0OO0OO0 )#line:926
                                OO0O0O0OO0OO000O0 ={"water":str (O00OO0O0OO0OOO00O ).split ('.')[0 ]}#line:927
                                OOO0O00OOOO0O0O00 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOO00OO0OOO0O0O00 ).json ()#line:928
                                if 'status'in OOO0O00OOOO0O0O00 :#line:930
                                    if OOO0O00OOOO0O0O00 ['status']==200 :#line:931
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0O00OOOO0O0O00["message"]}')#line:932
                                    if OOO0O00OOOO0O0O00 ['status']==500 :#line:933
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0O00OOOO0O0O00["message"]}')#line:934
                                        break #line:935
                            if energy :#line:936
                                if float (OOO0O00OOO0OO0OO0 )<800 :#line:937
                                    O00OO0O0OO0OOO00O =800 -float (OOO0O00OOO0OO0OO0 )#line:938
                                    O0O0O0OOOOO0O00OO =f'_water={int(O00OO0O0OO0OOO00O)}_{timi_new()}'#line:939
                                    OOO0OOOOO00O000O0 ={'source':'scsc','authorization':O0OOO000OOOOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOOO0O00OO ),'signstring':O0O0O0OOOOO0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:950
                                    O0000O000000000OO ={"water":int (O00OO0O0OO0OOO00O )}#line:951
                                    O0O0OO0000OOOO00O =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO0OOOOO00O000O0 ,data =O0000O000000000OO ).json ()#line:953
                                    if 'status'in O0O0OO0000OOOO00O :#line:955
                                        if O0O0OO0000OOOO00O ['status']==200 :#line:956
                                            print (f'【购买水滴】:购买水滴:{O0O0OO0000OOOO00O["message"]}丨数量:{int(O00OO0O0OO0OOO00O)}')#line:957
                                        if O0O0OO0000OOOO00O ['status']==500 :#line:958
                                            print (f'【购买水滴】:购买水滴:{O0O0OO0000OOOO00O["message"]}丨数量:{int(O00OO0O0OO0OOO00O)}')#line:959
                                            O0OO000OO00OOO0OO =O0O0OO0000OOOO00O ["message"].split ('-')[1 ]#line:960
                                            O000O0OOO00O0OO0O =f'__{timi_new()}'#line:961
                                            OO0OOOOO0O00O0OO0 ={'source':'scsc','authorization':O0OOO000OOOOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOO00O0OO0O ),'signstring':O000O0OOO00O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:972
                                            O0OO0O0OO0O00O0OO =requests .request ('get',f'{host}/user',headers =OO0OOOOO0O00O0OO0 ).json ()#line:973
                                            if 'status'in O0OO0O0OO0O00O0OO :#line:974
                                                if O0OO0O0OO0O00O0OO ['status']==200 :#line:975
                                                    O00OOOO00OO00OO0O =O0OO0O0OO0O00O0OO ['data']['inner_id']#line:976
                                                    if give_gold (O00OOOO00OO00OO0O ,float (O0OO000OO00OOO0OO )+1 ):#line:977
                                                        O0OOO000OOOOO0O0O .energy ()#line:978
                        break #line:979
        except Exception as O0000OOOOO000OOO0 :#line:981
            print (O0000OOOOO000OOO0 )#line:982
def bundled_def ():#line:984
    O000OOOO00O00OO00 =['5570536','7750212','7911652','7911680','7805624']#line:985
    return O000OOOO00O00OO00 [random .randint (0 ,len (O000OOOO00O00OO00 )-1 )]#line:986
def version_of_the_validation ():#line:990
    return str ((84 -56 )/10 )#line:991
def gitee_validation ():#line:994
    try :#line:995
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:996
    except :#line:997
        sys .exit (0 )#line:998
def update_the_validation ():#line:1002
    try :#line:1003
        OO0O0O0O000OO0000 =gitee_validation ()#line:1004
        if version_of_the_validation ()<OO0O0O0O000OO0000 ['CityEarth']['edition']:#line:1005
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0O0O000OO0000["CityEarth"]["edition"]}   ❌')#line:1006
            print (f'更新内容=>>{OO0O0O0O000OO0000["CityEarth"]["content"]}   🎉')#line:1007
        else :#line:1008
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0O0O000OO0000["CityEarth"]["edition"]}   ✅')#line:1009
            print (f'更新内容=>> {OO0O0O0O000OO0000["CityEarth"]["content"]}   🎉')#line:1010
    except Exception as OO0O0OOOO0OOO000O :#line:1011
        print (OO0O0OOOO0OOO000O )#line:1012
def os_qinglong ():#line:1015
    if application in os .environ :#line:1016
        O0O0OO0OOO0O00OOO =os .environ [application ].split ('\n')#line:1017
        if len (O0O0OO0OOO0O00OOO )>0 :#line:1018
            return O0O0OO0OOO0O00OOO #line:1019
        else :#line:1020
            print (f"{application}变量未启用")#line:1021
            print ('脚本退出')#line:1022
            sys .exit (1 )#line:1023
    else :#line:1024
        if token :#line:1025
            O0O0OO0OOO0O00OOO =token .split ('\n')#line:1026
            if len (O0O0OO0OOO0O00OOO )>0 :#line:1027
                return O0O0OO0OOO0O00OOO #line:1028
        else :#line:1029
            print (f"内置变量为空")#line:1030
            print ('脚本结束')#line:1031
            sys .exit (0 )#line:1032
if __name__ =='__main__':#line:1037
    start ()#line:1038
