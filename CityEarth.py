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
        O0000O00O0O0O0O00 =os_qinglong ()#line:10
        print (f"==========共找到{len(O0000O00O0O0O0O00)}个账号==========")#line:11
        for OOOO0OO0OO0O000O0 in O0000O00O0O0O0O00 :#line:12
            O00OO0OOO000O0OOO =[]#line:13
            print (f"------------正在执行第{O0000O00O0O0O0O00.index(OOOO0OO0OO0O000O0) + 1}个账号------------")#line:14
            OO0O0000O0OO000O0 =CityEarth (OOOO0OO0OO0O000O0 ,O00OO0OOO000O0OOO )#line:15
            def OO0000OOOOOO0OO0O ():#line:17
                if OO0O0000O0OO000O0 .base_info ():#line:19
                    OO0O0000O0OO000O0 .sealing ()#line:21
                    OO0O0000O0OO000O0 .invitenum ()#line:23
                    OO0O0000O0OO000O0 .game_map ()#line:25
                    OO0O0000O0OO000O0 .friends_invitation ()#line:27
                    OO0O0000O0OO000O0 .energy ()#line:29
                    OO0O0000O0OO000O0 .add_clover ()#line:31
                    OO0O0000O0OO000O0 .propsraffle ()#line:33
                    OO0O0000O0OO000O0 .synthetic ()#line:35
                    OO0O0000O0OO000O0 .crops_illustrated ()#line:37
                    OO0O0000O0OO000O0 .give_gold ()#line:39
                    OO0O0000O0OO000O0 .withdraw ()#line:41
            OO00OO000000OOOOO =threading .Thread (target =OO0000OOOOOO0OO0O )#line:43
            OO00OO000000OOOOO .start ()#line:44
            time .sleep (time_xx )#line:45
        print (f"------------正在处理推送通知------------")#line:46
        time .sleep (0.5 )#line:47
        OOO0OOO000000OOOO =format_msg ()#line:48
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOO0OOO000000OOOO +' ')#line:49
    except Exception as O00O0OOO0O0O0000O :#line:50
        print (O00O0OOO0O0O0000O )#line:51
def give_gold (O0OOOOO0OOOO0OO0O ,OO00O0OO0OO00OOOO ):#line:54
        try :#line:55
            OO0OOOO0000O0OOOO =f'_doneeNo={O0OOOOO0OOOO0OO0O}&quantity={int(OO00O0OO0OO00OOOO)}_{timi_new()}'#line:56
            O000OOOO00OO000O0 ={'source':'scsc','authorization':os_qinglong ()[0 ].split ('&')[0 ],'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0000O0OOOO ),'signstring':OO0OOOO0000O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:67
            OOOOOOOO0OO000OOO ={"quantity":int (OO00O0OO0OO00OOOO ),"doneeNo":O0OOOOO0OOOO0OO0O }#line:71
            O0OO0O0O00OOOOOOO =requests .request ('post',f'{host}/finance/give-gold',headers =O000OOOO00OO000O0 ,data =OOOOOOOO0OO000OOO ).json ()#line:72
            if 'status'in O0OO0O0O00OOOOOOO :#line:74
                if O0OO0O0O00OOOOOOO ['status']==200 :#line:75
                    if O0OO0O0O00OOOOOOO ['data']:#line:76
                        print (f'【赠送种子】:赠送{int(OO00O0OO0OO00OOOO)}种子给{O0OOOOO0OOOO0OO0O}成功')#line:77
                if O0OO0O0O00OOOOOOO ['status']==401 :#line:78
                    print (f'【赠送种子】:{O0OO0O0O00OOOOOOO["message"]}')#line:79
                if O0OO0O0O00OOOOOOO ['status']==500 :#line:80
                    print (f'【赠送种子】:{O0OO0O0O00OOOOOOO["message"]}')#line:81
        except Exception as OO0OOO000O0OOO000 :#line:82
            print (OO0OOO000O0OOO000 )#line:83
def sign (O0OOO000O0OO0OOO0 ):#line:86
    OOO0000OO000OO0O0 =hashlib .md5 (O0OOO000O0OO0OOO0 .encode ()).hexdigest ()#line:87
    OOOO0O0O0O00O0O0O ="scsc%^&*"+OOO0000OO000OO0O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:88
    OO000O0O0O00O0OOO =hashlib .md5 (OOOO0O0O0O00O0O0O .encode ()).hexdigest ()#line:89
    return OO000O0O0O00O0OOO #line:90
def format_msg ():#line:92
    O0OO000O000OO0OOO =""#line:93
    for OOO00O00OO000OO00 in msg_list :#line:94
        O0OO000O000OO0OOO +=str (OOO00O00OO000OO00 )+"\r\n"#line:95
    return O0OO000O000OO0OOO #line:96
def timi_new ():#line:98
    return str (int (time .time ()*1000 ))#line:99
class CityEarth :#line:102
    def __init__ (O00OO0OO0OOOO00OO ,O0OO0O0OOO0O00OO0 ,OOOOO00000OO0O00O ):#line:104
        try :#line:105
            O00OO0OO0OOOO00OO .msg =OOOOO00000OO0O00O #line:106
            O00OO0OO0OOOO00OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:107
            O00OO0OO0OOOO00OO .token =O0OO0O0OOO0O00OO0 .split ('&')[0 ]#line:108
            O00OO0OO0OOOO00OO .innerId =O0OO0O0OOO0O00OO0 .split ('&')[1 ]#line:109
            O00OO0OO0OOOO00OO .doneeNo =O0OO0O0OOO0O00OO0 .split ('&')[2 ]#line:110
        except :#line:111
            print ('变量格式错误')#line:112
    def base_info (OOO00OOO00O0O0O00 ):#line:115
        try :#line:116
            OOO00OOO00O0O0O00 .watched_ad ()#line:118
            O0OO0000000O0O0O0 =f'__{timi_new()}'#line:119
            OOO0000000OOO0O00 ={'source':'scsc','authorization':OOO00OOO00O0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0000000O0O0O0 ),'signstring':O0OO0000000O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:130
            O00OOO00O0O0OOO00 =requests .request ('get',f'{host}/user',headers =OOO0000000OOO0O00 ).json ()#line:131
            if 'status'in O00OOO00O0O0OOO00 :#line:133
                if O00OOO00O0O0OOO00 ['status']==200 :#line:134
                    OOOO0O000OOOOOO00 =O00OOO00O0O0OOO00 ['data']['nickname']#line:135
                    O00O00O000000O00O =O00OOO00O0O0OOO00 ['data']['inner_id']#line:136
                    O000OOOOOO00O0OO0 =O00OOO00O0O0OOO00 ['data']['assets']['gold']#line:137
                    OO00O00O0OO0O0O0O =O00OOO00O0O0OOO00 ['data']['level']#line:138
                    print (f'【账号信息】:昵称:{OOOO0O000OOOOOO00[:5]}丨ID:{O00O00O000000O00O}丨等级:{OO00O00O0OO0O0O0O}丨金种子:{str(O000OOOOOO00O0OO0).split(".")[0]}')#line:139
                if O00OOO00O0O0OOO00 ['status']==401 :#line:140
                    print (O00OOO00O0O0OOO00 ['message'])#line:141
                    OOO00OOO00O0O0O00 .msg .append ('有账号失效了')#line:142
                    return False #line:143
                if O00OOO00O0O0OOO00 ['status']==500 :#line:144
                    return False #line:145
            return True #line:146
        except Exception as OOO0000OO0OOOOOOO :#line:147
            print (OOO0000OO0OOOOOOO )#line:148
    def sealing (O000OOOOOO0OO00O0 ):#line:151
        try :#line:152
            O0O0O0O000000O0O0 =f'__{timi_new()}'#line:153
            OOO000OO0O0O0OO0O ={'source':'scsc','authorization':O000OOOOOO0OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O000000O0O0 ),'signstring':O0O0O0O000000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:164
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO000OO0O0O0OO0O )#line:165
            requests .request ('get',f'{host}/packsack/list',headers =OOO000OO0O0O0OO0O )#line:166
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO000OO0O0O0OO0O )#line:167
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO000OO0O0O0OO0O )#line:168
            requests .request ('get',f'{host}/user',headers =OOO000OO0O0O0OO0O )#line:169
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO000OO0O0O0OO0O )#line:170
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO000OO0O0O0OO0O )#line:171
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO000OO0O0O0OO0O )#line:172
            requests .request ('get',f'{host}/game/getAllData',headers =OOO000OO0O0O0OO0O )#line:173
            requests .request ('get',f'{host}/assets',headers =OOO000OO0O0O0OO0O )#line:174
        except Exception as O00O00O000000OO0O :#line:175
            print (O00O00O000000OO0O )#line:176
    def withdraw (O00OOOOOOO00OOOO0 ):#line:180
        O00O0O0O0OOOO0000 =f'__{timi_new()}'#line:181
        OOOOOO0O000O0OO0O ={'source':'scsc','authorization':O00OOOOOOO00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O0OOOO0000 ),'signstring':O00O0O0O0OOOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:192
        OO00O00000O0OOO0O =requests .request ('get',f'{host}/assets',headers =OOOOOO0O000O0OO0O ).json ()#line:193
        if 'status'in OO00O00000O0OOO0O :#line:195
            if OO00O00000O0OOO0O ['status']==200 :#line:196
                OO000OO0O0OOOOOOO =OO00O00000O0OOO0O ['data']['cash']#line:197
                if float (OO000OO0O0OOOOOOO )>20 :#line:198
                    O00O0O0O0OOOO0000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:199
                    OOOOOO0O000O0OO0O ={'authorization':O00OOOOOOO00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O0OOOO0000 ),'signstring':O00O0O0O0OOOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:209
                    O000OO0OOOO0OO0O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:210
                    O00OOOO0OOOO0OOO0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOOOO0O000O0OO0O ,data =O000OO0OOOO0OO0O0 ).json ()#line:212
                    print (O00OOOO0OOOO0OOO0 )#line:213
    def invitenum (OO0OOO0O00OO0OO0O ):#line:216
        OO0O0O00OO0OOOO0O =f'__{timi_new()}'#line:217
        O00OOOOOO00OOOOO0 ={'source':'scsc','authorization':OO0OOO0O00OO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O00OO0OOOO0O ),'signstring':OO0O0O00OO0OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:228
        OO0OO0O000O00O0O0 =requests .request ('get',f'{host}/invite/invitenum',headers =O00OOOOOO00OOOOO0 ).json ()#line:229
        if 'status'in OO0OO0O000O00O0O0 :#line:231
            if OO0OO0O000O00O0O0 ['status']==200 :#line:232
                O000O0OO00000O0O0 =OO0OO0O000O00O0O0 ['data']['invited_count']#line:233
                O0O0O00O0O000O0OO =OO0OO0O000O00O0O0 ['data']['invited_second_count']#line:234
                print (f'【我的邀请】:直邀好友:{O000O0OO00000O0O0}丨间邀好友:{O0O0O00O0O000O0OO}')#line:235
    def game_map (O000000OOOOO00O0O ):#line:238
        try :#line:239
            O0OO0O00O0000OOO0 =f'__{timi_new()}'#line:240
            O00OOOOO00O00O0O0 ={'source':'scsc','authorization':O000000OOOOO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O0000OOO0 ),'signstring':O0OO0O00O0000OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:251
            O0O0O000OOOOO00O0 =requests .request ('get',f'{host}/game/map',headers =O00OOOOO00O00O0O0 ).json ()#line:252
            if 'status'in O0O0O000OOOOO00O0 :#line:254
                if O0O0O000OOOOO00O0 ['status']==200 :#line:255
                    for OOOOOOO00OO00OOOO in O0O0O000OOOOO00O0 ['data']['list'][0 ]['crops']:#line:256
                        O0O0O0OO00OO0OOO0 =OOOOOOO00OO00OOOO ['level']#line:258
                        if O0O0O0OO00OO0OOO0 ==41 :#line:259
                            O00OOOOOOO0O00OO0 =OOOOOOO00OO00OOOO ['crop_name']#line:260
                            O00O0OOO00OOOOOO0 =OOOOOOO00OO00OOOO ['count']#line:261
                            if O00O0OOO00OOOOOO0 >0 :#line:262
                                print (f'【农业资产】:{O00OOOOOOO0O00OO0}丨数量:{O00O0OOO00OOOOOO0}')#line:263
        except Exception as OO0O00O00O0000OOO :#line:264
            print (OO0O00O00O0000OOO )#line:265
    def give_gold (O00OO0OOOO00OO0OO ):#line:268
        try :#line:269
            O0O000OOO0OOOO0O0 =f'__{timi_new()}'#line:270
            OOOOOO0O00OO0O0OO ={'source':'scsc','authorization':O00OO0OOOO00OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOO0OOOO0O0 ),'signstring':O0O000OOO0OOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:281
            O00OOOOOOOOOOO00O =requests .request ('get',f'{host}/user',headers =OOOOOO0O00OO0O0OO ).json ()#line:282
            if 'status'in O00OOOOOOOOOOO00O :#line:283
                if O00OOOOOOOOOOO00O ['status']==200 :#line:284
                    if float (O00OO0OOOO00OO0OO .doneeNo )!=0 :#line:285
                        O0O00O00OO0O00000 =O00OOOOOOOOOOO00O ['data']['assets']['gold']#line:286
                        if float (O0O00O00OO0O00000 )>float (O00OO0OOOO00OO0OO .innerId ):#line:287
                            O00OO0O0000O000OO =int (float (O0O00O00OO0O00000 )/1.1 )#line:288
                            O0O000OOO0OOOO0O0 =f'_doneeNo={O00OO0OOOO00OO0OO.doneeNo}&quantity={O00OO0O0000O000OO}_{timi_new()}'#line:289
                            OOOOOO0O00OO0O0OO ={'source':'scsc','authorization':O00OO0OOOO00OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOO0OOOO0O0 ),'signstring':O0O000OOO0OOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:300
                            OO000OOOOOO000OOO ={"quantity":O00OO0O0000O000OO ,"doneeNo":O00OO0OOOO00OO0OO .doneeNo }#line:304
                            OOOOO0000OOOO0000 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOOO0O00OO0O0OO ,data =OO000OOOOOO000OOO ).json ()#line:305
                            if 'status'in OOOOO0000OOOO0000 :#line:307
                                if OOOOO0000OOOO0000 ['status']==200 :#line:308
                                    if OOOOO0000OOOO0000 ['data']:#line:309
                                        print (f'【赠送种子】:赠送{O00OO0O0000O000OO}种子给{O00OO0OOOO00OO0OO.doneeNo}成功')#line:310
                    else :#line:311
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:312
        except Exception as O00OO00OO00000O00 :#line:313
            print (O00OO00OO00000O00 )#line:314
    def invitation (O0OO000OOOOOOOO00 ):#line:316
        try :#line:317
            _O00OO00O00OO00000 =float (bundled_def ())/4 #line:318
            O000O00O00O0O0O00 =f'_innerId={int(_O00OO00O00OO00000)}_{timi_new()}'#line:319
            O000000O0O000OO00 ={'source':'scsc','authorization':O0OO000OOOOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00O00O0O0O00 ),'signstring':O000O00O00O0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:330
            OO0O0OOOOO0000000 ={"innerId":int (_O00OO00O00OO00000 )}#line:331
            requests .request ('post',f'{host}/friends/my-invitation',headers =O000000O0O000OO00 ,data =OO0O0OOOOO0000000 )#line:332
        except Exception as OO0OO0O0O0OO0OOOO :#line:333
            print (OO0OO0O0O0OO0OOOO )#line:334
    def winning_rewards (O0O0OOO0OO0O0O0O0 ):#line:337
        try :#line:338
            O00OOO0OO0OOOO0OO =f'__{timi_new()}'#line:339
            O00000O0O0O0OO0OO ={'source':'scsc','authorization':O0O0OOO0OO0O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OO0OOOO0OO ),'signstring':O00OOO0OO0OOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
            O0O00000OOO00O0OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00000O0O0O0OO0OO ).json ()#line:351
            if 'status'in O0O00000OOO00O0OO :#line:353
                if O0O00000OOO00O0OO ['status']==200 :#line:354
                    if O0O00000OOO00O0OO ['data']['amount']:#line:355
                        O0OOOOO0000OO0OO0 =O0O00000OOO00O0OO ['data']['amount']['gold']#line:356
                        return O0OOOOO0000OO0OO0 #line:357
                    else :#line:358
                        return 0 #line:359
        except Exception as OOO0O0OO00O0O0000 :#line:360
            print (OOO0O0OO00O0O0000 )#line:361
    def certification (OO0000O0O000000OO ):#line:364
        try :#line:365
            OOO0OO0000OO00OO0 =f'__{timi_new()}'#line:366
            OOO0OOO000O0O0OOO ={'source':'scsc','authorization':OO0000O0O000000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0000OO00OO0 ),'signstring':OOO0OO0000OO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:377
            OO0OOOOO0OOOOO0O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO0OOO000O0O0OOO ).json ()#line:378
            if 'status'in OO0OOOOO0OOOOO0O0 :#line:380
                if OO0OOOOO0OOOOO0O0 ['status']==200 :#line:381
                    if OO0OOOOO0OOOOO0O0 ['data']['result']:#line:382
                        OO00O000O000OO0O0 =OO0OOOOO0OOOOO0O0 ['data']['nick_name']#line:383
                        return OO00O000O000OO0O0 #line:384
                    else :#line:385
                        return '未实名'#line:386
        except Exception as O00000O0O0O0O0O0O :#line:387
            print (O00000O0O0O0O0O0O )#line:388
    def crops_illustrated (O0OO0000000O0OO0O ):#line:391
        try :#line:392
            OOOOO0OOOO0O0OO00 =f'__{timi_new()}'#line:393
            O00000O0OO000O0O0 ={'source':'scsc','authorization':O0OO0000000O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOOO0O0OO00 ),'signstring':OOOOO0OOOO0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:404
            O0O0O0OOO00OOOOOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00000O0OO000O0O0 ).json ()#line:405
            if 'status'in O0O0O0OOO00OOOOOO :#line:407
                if O0O0O0OOO00OOOOOO ['status']==200 :#line:408
                    O0OO00000000OOOOO =O0O0O0OOO00OOOOOO ['data'][0 ]['crops']#line:409
                    for OO0OO0000000O0O00 in O0OO00000000OOOOO :#line:410
                        if OO0OO0000000O0O00 ['ill_clover_award']:#line:411
                            if float (OO0OO0000000O0O00 ['ill_clover_award'])>1 :#line:412
                                if OO0OO0000000O0O00 ['is_finish']:#line:413
                                    if not OO0OO0000000O0O00 ['is_getit']:#line:414
                                        if O0OO0000000O0OO0O .certification ()!='未实名':#line:415
                                            OOOOO0OOOO0O0OO00 =f'_award_level={OO0OO0000000O0O00["level"]}_{timi_new()}'#line:416
                                            O00000O0OO000O0O0 ={'source':'scsc','authorization':O0OO0000000O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOOO0O0OO00 ),'signstring':OOOOO0OOOO0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:427
                                            O0OOOO00O000O0O00 ={"award_level":OO0OO0000000O0O00 ['level']}#line:428
                                            OO0OO0O0O0OO00OO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00000O0OO000O0O0 ,json =O0OOOO00O000O0O00 ).json ()#line:430
                                            if 'status'in OO0OO0O0O0OO00OO0 :#line:431
                                                if OO0OO0O0O0OO00OO0 ['status']==200 :#line:432
                                                    O00OO0O000OOO0O0O =OO0OO0O0O0OO00OO0 ['data']['ill_clover_award']#line:433
                                                    print (f'【图鉴奖励】:领取{OO0OO0000000O0O00["crop_name"]}成就丨奖励{O00OO0O000OOO0O0O}☘️')#line:435
                                                if OO0OO0O0O0OO00OO0 ['status']==500 :#line:436
                                                    print (f'【图鉴奖励】:{OO0OO0O0O0OO00OO0["message"]}')#line:437
        except Exception as O0O0OOO00OO0000OO :#line:438
            print (O0O0OOO00OO0000OO )#line:439
    def watched_ad (OO00OO00OO00OO0O0 ):#line:442
        try :#line:443
            OOO0O000O0OOO0O00 =f'__{timi_new()}'#line:444
            OO0O0O00OOOOO0OO0 ={'source':'scsc','authorization':OO00OO00OO00OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O0OOO0O00 ),'signstring':OOO0O000O0OOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:455
            O0O00OO00O0000O0O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O00OOOOO0OO0 ).json ()#line:456
            if 'status'in O0O00OO00O0000O0O :#line:458
                if O0O00OO00O0000O0O ['status']==200 :#line:459
                    if 'offlineInfo'in O0O00OO00O0000O0O ['data']:#line:460
                        time .sleep (random .randint (3 ,5 ))#line:461
                        O0O000OOOO0OOO00O =O0O00OO00O0000O0O ['data']['offlineInfo']['off_minute']#line:462
                        OOOO000000O00O00O =float (O0O00OO00O0000O0O ['data']['silver'])/1000000000000 #line:463
                        time .sleep (1 )#line:464
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0O0O00OOOOO0OO0 ).json ()#line:465
                        time .sleep (2 )#line:466
                        O00OOO0O00OO0O0OO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O00OOOOO0OO0 ).json ()#line:467
                        if 'status'in O00OOO0O00OO0O0OO :#line:469
                            if O00OOO0O00OO0O0OO ['status']==200 :#line:470
                                OO0O000O00OO0000O =float (O00OOO0O00OO0O0OO ['data']['silver'])/1000000000000 #line:471
                                O0O00O000000O00OO =str (OO0O000O00OO0000O -OOOO000000O00O00O )[:6 ]#line:472
                                print (f'【离线奖励】:翻倍离线{O0O000OOOO0OOO00O}分钟奖励🌱数量:{O0O00O000000O00OO}t粒')#line:473
        except Exception as O00OO00OOO0OOOO0O :#line:474
            print (O00OO00OOO0OOOO0O )#line:475
    def user_ad (OO0OO000OO0000OOO ):#line:478
        try :#line:479
            OOO0000O0O00000OO =f'__{timi_new()}'#line:480
            O000OOO00OOOO0000 ={'source':'scsc','authorization':OO0OO000OO0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O0O00000OO ),'signstring':OOO0000O0O00000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:491
            O00O000OOOO00OO0O =requests .request ('get',f'{host}/user/ad',headers =O000OOO00OOOO0000 ).json ()#line:492
            if 'status'in O00O000OOOO00OO0O :#line:494
                if O00O000OOOO00OO0O ['status']==200 :#line:495
                    OO0O00O0O000O0O0O =O00O000OOOO00OO0O ['data']['max_time']#line:496
                    OOO000OOOOO00O000 =O00O000OOOO00OO0O ['data']['watch_time']#line:497
                    OO0000OO0OO0000O0 =O00O000OOOO00OO0O ['data']['added_time']#line:498
                    print (f'【获取种子】:获取🌱剩余{OO0000OO0OO0000O0 + OO0O00O0O000O0O0O - OOO000OOOOO00O000}次丨好友提供:{OO0000OO0OO0000O0}次')#line:499
                    if OO0000OO0OO0000O0 +OO0O00O0O000O0O0O -OOO000OOOOO00O000 >0 :#line:500
                        time .sleep (random .randint (16 ,19 ))#line:501
                        OO000OO0OOOOO0O00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O000OOO00OOOO0000 ).json ()#line:502
                        if 'status'in OO000OO0OOOOO0O00 :#line:504
                            if OO000OO0OOOOO0O00 ['status']==200 :#line:505
                                O0OO00OO0OO000O0O =float (OO000OO0OOOOO0O00 ['data']['silver'])/1000000000000 #line:506
                                print (f'【获取种子】:获得🌱:{int(O0OO00OO0OO000O0O)}t粒')#line:507
                                return True #line:508
                            if OO000OO0OOOOO0O00 ['status']==500 :#line:509
                                OO0OOOO00000O0O00 =OO000OO0OOOOO0O00 ['message']#line:510
                                print (f'【获取种子】:{OO0OOOO00000O0O00}')#line:511
                                return False #line:512
        except Exception as OOOO00O0OO00OO0OO :#line:513
            print (OOOO00O0OO00OO0OO )#line:514
    def synthetic (OO000000OO000OO00 ):#line:517
        global id ,g #line:518
        try :#line:519
            O00O0O0OOOOO0O000 =OO000000OO000OO00 .level_new ()#line:520
            OOO00O0OOOO000OO0 =random .randint (9 ,11 )#line:521
            OO0OOO000O0O0OOOO =f'_site=8&targetSite={OOO00O0OOOO000OO0}_{timi_new()}'#line:522
            OOOOO0O0O0O0OO000 ={'source':'scsc','authorization':OO000000OO000OO00 .token ,'timestamp':timi_new (),'sign':sign (OO0OOO000O0O0OOOO ),'signstring':OO0OOO000O0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:533
            OO00O000O000OO00O ={"site":int (8 ),"targetSite":int (OOO00O0OOOO000OO0 )}#line:534
            requests .request ('post',f'{host}/game/crops/move',headers =OOOOO0O0O0O0OO000 ,json =OO00O000O000OO00O )#line:535
            while True :#line:536
                OO000O00000O0000O =f'__{timi_new()}'#line:537
                OOOOOOO00OO0OOO0O ={'source':'scsc','authorization':OO000000OO000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00000O0000O ),'signstring':OO000O00000O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:548
                O0O0O0O0OOOOO00OO =requests .request ('get',f'{host}/game/getAllData',headers =OOOOOOO00OO0OOO0O ).json ()#line:549
                if 'status'in O0O0O0O0OOOOO00OO :#line:551
                    if O0O0O0O0OOOOO00OO ['status']==200 :#line:552
                        OOO0OOOO000000000 =O0O0O0O0OOOOO00OO ['data']['cropList']#line:553
                        OO0000000O0O0000O =O0O0O0O0OOOOO00OO ['data']['gameCoreDataDBid']#line:554
                        OO0O000O0OOO00O00 =float (O0O0O0O0OOOOO00OO ['data']['silver'])/1000000000000 #line:555
                        OOOO00O0O0OO00OOO =0 #line:560
                        for OOO0OOOOOOOO0O000 in OOO0OOOO000000000 :#line:561
                            if not OOO0OOOOOOOO0O000 :#line:562
                                OOOO0O00O0000000O =f'_crop_id={OO0000000O0O0000O}&site={OOOO00O0O0OO00OOO}_{OO000000OO000OO00.time}'#line:563
                                O0O0OO000OO0OO000 ={'source':'scsc','authorization':OO000000OO000OO00 .token ,'timestamp':OO000000OO000OO00 .time ,'sign':sign (OOOO0O00O0000000O ),'signstring':OOOO0O00O0000000O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:573
                                O00000OO0OO00O00O ={"site":OOOO00O0O0OO00OOO ,"crop_id":OO0000000O0O0000O }#line:574
                                OOOOOO00O0000O000 =requests .request ('post',f'{host}/game/crops/buy',headers =O0O0OO000OO0OO000 ,data =O00000OO0OO00O00O ).json ()#line:575
                                time .sleep (random .randint (1 ,3 )/10 )#line:577
                                if 'status'in OOOOOO00O0000O000 :#line:578
                                    if OOOOOO00O0000O000 ['status']==200 :#line:579
                                        if OOOOOO00O0000O000 ['message']=='种子数量不足':#line:580
                                            O00O0O0OOOOO0O000 =OO000000OO000OO00 .level_new ()#line:581
                                            print (f'【种植合成】:{OOOOOO00O0000O000["message"]}')#line:582
                                            if not OO000000OO000OO00 .user_ad ():#line:583
                                                return False #line:584
                                    if OOOOOO00O0000O000 ['status']==500 :#line:585
                                        print (f'【种植合成】:{OOOOOO00O0000O000["message"]}')#line:586
                                        return False #line:587
                            OOOO00O0O0OO00OOO +=1 #line:588
                        OOOO0OO0OOO0O0O0O =requests .request ('get',f'{host}/game/getAllData',headers =OOOOOOO00OO0OOO0O ).json ()#line:589
                        OO00OO0OOOO0OO00O =OOOO0OO0OOO0O0O0O ['data']['cropList']#line:590
                        O00O000O0O00O0O0O =False #line:591
                        for OOO0OOOOOOOO0O000 in range (12 ):#line:592
                            id =OO00OO0OOOO0OO00O [OOO0OOOOOOOO0O000 ]['level']#line:593
                            if float (O00O0O0OOOOO0O000 )-float (id )>9 :#line:594
                                O00O000O0O0OOO0OO =f'_site={OOO0OOOOOOOO0O000}_{timi_new()}'#line:595
                                O0O0000O00OO000O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO000000OO000OO00 .token ,'timestamp':timi_new (),'sign':sign (O00O000O0O0OOO0OO ),'signstring':O00O000O0O0OOO0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:606
                                OOO0OOOOO00OOO000 ={"site":OOO0OOOOOOOO0O000 }#line:607
                                OOOOO000O00O0O0OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O0000O00OO000O0 ,data =OOO0OOOOO00OOO000 ).json ()#line:609
                                if 'status'in OOOOO000O00O0O0OO :#line:610
                                    if OOOOO000O00O0O0OO ['status']==200 :#line:611
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:612
                            if id !=0 :#line:613
                                for OO0OO0000OOOO0OOO in range (11 ):#line:614
                                    O00O0OO000OO00O0O =OO0OO0000OOOO0OOO +1 #line:615
                                    g =OO00OO0OOOO0OO00O [O00O0OO000OO00O0O ]['level']#line:616
                                    if id ==g :#line:617
                                        O0O0O0OOO00OO000O =OO0OO0000OOOO0OOO +2 #line:618
                                        if O0O0O0OOO00OO000O !=OOO0OOOOOOOO0O000 +1 :#line:619
                                            OO00OOO0OOO0O00O0 =OOO0OOOOOOOO0O000 +1 #line:620
                                            time .sleep (random .randint (1 ,3 )/10 )#line:622
                                            OO0OOO000O0O0OOOO =f'_site={OO00OOO0OOO0O00O0 - 1}&targetSite={O0O0O0OOO00OO000O - 1}_{timi_new()}'#line:623
                                            OOOOO0O0O0O0OO000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO000000OO000OO00 .token ,'timestamp':timi_new (),'sign':sign (OO0OOO000O0O0OOOO ),'signstring':OO0OOO000O0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:640
                                            O0000O000OOOO0000 ={"site":int (OO00OOO0OOO0O00O0 -1 ),"targetSite":int (O0O0O0OOO00OO000O -1 )}#line:641
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOOOO0O0O0O0OO000 ,json =O0000O000OOOO0000 )#line:642
                                            O00O000O0O00O0O0O =True #line:644
                                    if O00O000O0O00O0O0O :#line:645
                                        break #line:646
                                if O00O000O0O00O0O0O :#line:647
                                    break #line:648
        except :#line:649
            OO000000OO000OO00 .synthetic ()#line:650
    def level_new (O0O0O000O0O000000 ):#line:653
        try :#line:654
            O0OOO0OO00O00O00O =f'__{timi_new()}'#line:655
            O0000000OO000O000 ={'source':'scsc','authorization':O0O0O000O0O000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO00O00O00O ),'signstring':O0OOO0OO00O00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:666
            O0O0O0O000O0OOOO0 =requests .request ('get',f'{host}/user',headers =O0000000OO000O000 ).json ()#line:667
            if 'status'in O0O0O0O000O0OOOO0 :#line:668
                if O0O0O0O000O0OOOO0 ['status']==200 :#line:669
                    return float (O0O0O0O000O0OOOO0 ['data']['level'])#line:670
        except Exception as OOOOOOOO00O0O0O0O :#line:671
            print (OOOOOOOO00O0O0O0O )#line:672
    def propsraffle (OOO0OOOO000O00O00 ):#line:675
        try :#line:676
            while True :#line:677
                O00OOO00000OOOO00 =f'__{timi_new()}'#line:678
                O0OO00O0O00O0O000 ={'source':'scsc','authorization':OOO0OOOO000O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO00000OOOO00 ),'signstring':O00OOO00000OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:689
                OO0O00OO00O00O0O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OO00O0O00O0O000 ).json ()#line:690
                if 'status'in OO0O00OO00O00O0O0 :#line:692
                    if OO0O00OO00O00O0O0 ['status']==200 :#line:693
                        O0OOOOO0OO0O000OO =OO0O00OO00O00O0O0 ['data']['rows']#line:694
                        OOOOOOO0OO000OO0O =OO0O00OO00O00O0O0 ['data']['vstate']#line:695
                        if O0OOOOO0OO0O000OO ==5 or O0OOOOO0OO0O000OO ==6 or O0OOOOO0OO0O000OO ==7 :#line:696
                            OO0O00OO0O00000OO =OO0O00OO00O00O0O0 ['data']['silver']#line:697
                            print (f'【转盘抽奖】:获得种子:{OO0O00OO0O00000OO}')#line:698
                        if O0OOOOO0OO0O000OO ==1 or O0OOOOO0OO0O000OO ==2 or O0OOOOO0OO0O000OO ==3 :#line:699
                            O00OOOO0OO0OO0OO0 =OO0O00OO00O00O0O0 ['data']['clover']#line:700
                            print (f'【转盘抽奖】:获得三叶草:{O00OOOO0OO0OO0OO0}')#line:701
                        if O0OOOOO0OO0O000OO ==4 or O0OOOOO0OO0O000OO ==8 :#line:702
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:703
                        if O0OOOOO0OO0O000OO =='抽奖次数已用完':#line:707
                            break #line:741
                time .sleep (random .randint (8 ,15 )/10 )#line:742
        except Exception as OOOO000O0OOO000OO :#line:743
            print (OOOO000O0OOO000OO )#line:744
    def friends_invitation (OO0OO0000OO0OOOOO ):#line:747
        try :#line:748
            O0OOO0OO0O00O0OOO =f'__{timi_new()}'#line:749
            OOOO0O0OO0000O00O ={'source':'scsc','authorization':OO0OO0000OO0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO0O00O0OOO ),'signstring':O0OOO0OO0O00O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:760
            O0OO0O0OO00O0O0OO =requests .request ('get',f'{host}/friends',headers =OOOO0O0OO0000O00O ).json ()#line:761
            if 'status'in O0OO0O0OO00O0O0OO :#line:762
                if O0OO0O0OO00O0O0OO ['status']==200 :#line:763
                    O000O0OO0O0OOO00O =O0OO0O0OO00O0O0OO ['data']['myInviteter']#line:764
                    if O000O0OO0O0OOO00O :#line:765
                        OOO0O00O00O000OOO =O000O0OO0O0OOO00O ['user']['nickname']#line:766
                        O00OOO0OO0O0OOO00 =OO0OO0000OO0OOOOO .certification ()#line:767
                        print (f'【查邀请人】:我的邀请人:{OOO0O00O00O000OOO}丨实名:{O00OOO0OO0O0OOO00}')#line:768
                    else :#line:769
                        if OO0OO0000OO0OOOOO .innerId !='0':#line:770
                            OO0OO0000OO0OOOOO .invitation ()#line:771
        except Exception as OOO0OO0OOOO0O000O :#line:772
            print (OOO0OO0OOOO0O000O )#line:773
    def add_clover (OO00000O0OOOO000O ):#line:776
        global golden_seed #line:777
        try :#line:778
            O0OOO00O0OOO000O0 =f'__{timi_new()}'#line:779
            OO000O000O0O0O0OO ={'source':'scsc','authorization':OO00000O0OOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0OOO000O0 ),'signstring':O0OOO00O0OOO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:790
            OO0OOOOO000O000OO =requests .request ('get',f'{host}/assets/clovers',headers =OO000O000O0O0O0OO ).json ()#line:791
            if 'status'in OO0OOOOO000O000OO :#line:793
                if OO0OOOOO000O000OO ['status']==200 :#line:794
                    OOOO000000000O000 =OO0OOOOO000O000OO ['data']['clover']#line:795
                    OO0O00OO0OOOOO0O0 =OO0OOOOO000O000OO ['data']['used_clover']#line:796
                    O0O0O0O0OOO000O0O =float (OOOO000000000O000 )-float (OO0O00OO0OOOOO0O0 )#line:797
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO0O00OO0OOOOO0O0}')#line:798
                    if OO00000O0OOOO000O .certification ()!='未实名':#line:799
                        if O0O0O0O0OOO000O0O >1 :#line:800
                            O0OOO00O0OOO000O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O0O0O0OOO000O0O)}_{timi_new()}'#line:801
                            O0OOO00OOO0000O0O ={'source':'scsc','authorization':OO00000O0OOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0OOO000O0 ),'signstring':O0OOO00O0OOO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:812
                            O0O000000O00OO0O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O0O0O0OOO000O0O )}#line:813
                            O00OOO000O0OOO0OO =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OOO00OOO0000O0O ,data =O0O000000O00OO0O0 ).json ()#line:814
                            if 'status'in O00OOO000O0OOO0OO :#line:816
                                if O00OOO000O0OOO0OO ['status']==200 :#line:817
                                    print (f'【参与抽奖】:添加☘️:{O00OOO000O0OOO0OO["data"]}丨数量:{O0O0O0O0OOO000O0O}')#line:818
                                if O00OOO000O0OOO0OO ['status']==500 :#line:819
                                    print (f'【参与抽奖】:添加☘️:{O00OOO000O0OOO0OO["message"]}')#line:820
            O000000O0OOOO0OOO =requests .request ('get',f'{host}/lottery',headers =OO000O000O0O0O0OO ).json ()#line:821
            OOOOOOOO0OO000O00 =OO00000O0OOOO000O .winning_rewards ()#line:823
            if 'status'in O000000O0OOOO0OOO :#line:824
                if O000000O0OOOO0OOO ['status']==200 :#line:825
                    O0OOOOO00O000000O =O000000O0OOOO0OOO ['data'][0 ]['day_get_gold_quantity']#line:826
                    golden_seed +=float (O0OOOOO00O000000O )#line:827
                    O0O0OOOO0OO00O00O =O000000O0OOOO0OOO ['data'][1 ]['value']#line:828
                    O0O00OOOO0000000O =O000000O0OOOO0OOO ['data'][0 ]['join_number']#line:829
                    OO00OO000000O00OO =int (float (O000000O0OOOO0OOO ['data'][0 ]['totalValue']))#line:830
                    O0O0O00OO00OOOO0O =float (O0O0OOOO0OO00O00O /OO00OO000000O00OO )*10000 #line:831
                    O0OOOOOO0OOO00000 =OO00OO000000O00OO /O0O00OOOO0000000O #line:832
                    print (f'【参与抽奖】:预计每天中{str(O0OOOOO00O000000O)[:6]}颗金种子丨好友收益:{str(OOOOOOOO0OO000O00)[:6]}')#line:833
                    print (f'【抽奖统计】:每1万☘️中{str(O0O0O00OO00OOOO0O)[:6]}颗金种子丨☘️人均:{str(O0OOOOOO0OOO00000)[:7]}️')#line:834
        except Exception as O0O000000000O000O :#line:835
            print (O0O000000000O000O )#line:836
    def energy (O0OO0000000O0OOO0 ):#line:840
        try :#line:841
            while True :#line:842
                O0O0O00O0OO00OO00 =f'__{timi_new()}'#line:843
                OOOOOOOOO0OO0000O ={'source':'scsc','authorization':O0OO0000000O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00O0OO00OO00 ),'signstring':O0O0O00O0OO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:854
                O00O0OOO0000OOOOO =requests .request ('get',f'{host}/energy/general',headers =OOOOOOOOO0OO0000O ).json ()#line:855
                if 'status'in O00O0OOO0000OOOOO :#line:857
                    if O00O0OOO0000OOOOO ['status']==200 :#line:858
                        OOOO00O000O0OOOOO =O00O0OOO0000OOOOO ['data']['ordinary_water']#line:859
                        O0OOOOO0O00O0O000 =O00O0OOO0000OOOOO ['data']['ordinary_fertilizer']#line:860
                        OO00O0000O0000OOO =O00O0OOO0000OOOOO ['data']['videoStatus']#line:861
                        OOO000O00O00O0O00 =O00O0OOO0000OOOOO ['data']['waterVideoKey']#line:862
                        print (f'【我的营养】:肥料:{str(O0OOOOO0O00O0O000).split(".")[0]}丨水滴:{str(OOOO00O000O0OOOOO).split(".")[0]}')#line:863
                        if float (O0OOOOO0O00O0O000 )<96 :#line:864
                            if OO00O0000O0000OOO :#line:865
                                time .sleep (random .randint (160 ,180 )/10 )#line:866
                                OO00OOO0O0OO0OO00 =99 -float (O0OOOOO0O00O0O000 )#line:867
                                O00OOO00O00O0OOOO ={"fertilizer":str (OO00OOO0O0OO0OO00 ).split ('.')[0 ]}#line:868
                                OOO000O00O0OOO0O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOOOOOOO0OO0000O ).json ()#line:869
                                if 'status'in OOO000O00O0OOO0O0 :#line:871
                                    if OOO000O00O0OOO0O0 ['status']==200 :#line:872
                                        print (f'【购买肥料】:看广告获取肥料:{OOO000O00O0OOO0O0["message"]}')#line:873
                                    if OOO000O00O0OOO0O0 ['status']==500 :#line:874
                                        print (f'【购买肥料】:看广告获取肥料:{OOO000O00O0OOO0O0["message"]}')#line:875
                                        break #line:876
                            if energy :#line:877
                                OO00OOO0O0OO0OO00 =80 -float (O0OOOOO0O00O0O000 )#line:878
                                O0OOO0O00O0O0O000 =f'_fertilizer={int(OO00OOO0O0OO0OO00)}_{timi_new()}'#line:879
                                OOOO00O00OOOOO0OO ={'source':'scsc','authorization':O0OO0000000O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O00O0O0O000 ),'signstring':O0OOO0O00O0O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:890
                                OO00000OO0000OO00 ={"fertilizer":int (OO00OOO0O0OO0OO00 )}#line:891
                                OO0OO0OOO000O00O0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOO00O00OOOOO0OO ,data =OO00000OO0000OO00 ).json ()#line:892
                                if 'status'in OO0OO0OOO000O00O0 :#line:894
                                    if OO0OO0OOO000O00O0 ['status']==200 :#line:895
                                        print (f'【购买肥料】:购买肥料:{OO0OO0OOO000O00O0["message"]}丨数量:{int(OO00OOO0O0OO0OO00)}')#line:896
                                    if OO0OO0OOO000O00O0 ['status']==500 :#line:897
                                        print (f'【购买肥料】:购买肥料:{OO0OO0OOO000O00O0["message"]}丨数量:{int(OO00OOO0O0OO0OO00)}')#line:898
                                        OOOOOO00OO0O0OOOO =OO0OO0OOO000O00O0 ["message"].split ('-')[1 ]#line:899
                                        O0OO000O0OOO0O0OO =f'__{timi_new()}'#line:900
                                        O0O0OOOOO00OOO0OO ={'source':'scsc','authorization':O0OO0000000O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O0OOO0O0OO ),'signstring':O0OO000O0OOO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:911
                                        O000OOO00O0O0O000 =requests .request ('get',f'{host}/user',headers =O0O0OOOOO00OOO0OO ).json ()#line:912
                                        if 'status'in O000OOO00O0O0O000 :#line:913
                                            if O000OOO00O0O0O000 ['status']==200 :#line:914
                                                O000OOOOO00O00OOO =O000OOO00O0O0O000 ['data']['inner_id']#line:915
                                                give_gold (O000OOOOO00O00OOO ,float (OOOOOO00OO0O0OOOO )+1 )#line:916
                                                O0OO0000000O0OOO0 .energy ()#line:917
                        if float (OOOO00O000O0OOOOO )<880 :#line:918
                            if OOO000O00O00O0O00 :#line:919
                                time .sleep (random .randint (160 ,180 )/10 )#line:920
                                O0OOO0OO0OO000OO0 =999 -float (OOOO00O000O0OOOOO )#line:921
                                O0000O0OOOO0OOO00 ={"water":str (O0OOO0OO0OO000OO0 ).split ('.')[0 ]}#line:922
                                OO0OOOOO0000OO00O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOOOOOOO0OO0000O ).json ()#line:923
                                if 'status'in OO0OOOOO0000OO00O :#line:925
                                    if OO0OOOOO0000OO00O ['status']==200 :#line:926
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OOOOO0000OO00O["message"]}')#line:927
                                    if OO0OOOOO0000OO00O ['status']==500 :#line:928
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OOOOO0000OO00O["message"]}')#line:929
                                        break #line:930
                            if energy :#line:931
                                O0OOO0OO0OO000OO0 =800 -float (OOOO00O000O0OOOOO )#line:932
                                O0O0OOO00OOOOO0OO =f'_water={int(O0OOO0OO0OO000OO0)}_{timi_new()}'#line:933
                                OOO0O0000OOO0OO00 ={'source':'scsc','authorization':O0OO0000000O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO00OOOOO0OO ),'signstring':O0O0OOO00OOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:944
                                OO000O0OO00OO00OO ={"water":int (O0OOO0OO0OO000OO0 )}#line:945
                                OOO0000OOOOO0000O =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO0O0000OOO0OO00 ,data =OO000O0OO00OO00OO ).json ()#line:947
                                if 'status'in OOO0000OOOOO0000O :#line:949
                                    if OOO0000OOOOO0000O ['status']==200 :#line:950
                                        print (f'【购买水滴】:购买水滴:{OOO0000OOOOO0000O["message"]}丨数量:{int(O0OOO0OO0OO000OO0)}')#line:951
                                    if OOO0000OOOOO0000O ['status']==500 :#line:952
                                        print (f'【购买水滴】:购买水滴:{OOO0000OOOOO0000O["message"]}丨数量:{int(O0OOO0OO0OO000OO0)}')#line:953
                                        OOOOOO00OO0O0OOOO =OOO0000OOOOO0000O ["message"].split ('-')[1 ]#line:954
                                        O0OO000O0OOO0O0OO =f'__{timi_new()}'#line:955
                                        O0O0OOOOO00OOO0OO ={'source':'scsc','authorization':O0OO0000000O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O0OOO0O0OO ),'signstring':O0OO000O0OOO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:966
                                        O000OOO00O0O0O000 =requests .request ('get',f'{host}/user',headers =O0O0OOOOO00OOO0OO ).json ()#line:967
                                        if 'status'in O000OOO00O0O0O000 :#line:968
                                            if O000OOO00O0O0O000 ['status']==200 :#line:969
                                                O000OOOOO00O00OOO =O000OOO00O0O0O000 ['data']['inner_id']#line:970
                                                give_gold (O000OOOOO00O00OOO ,float (OOOOOO00OO0O0OOOO )+1 )#line:971
                                                O0OO0000000O0OOO0 .energy ()#line:972
                        break #line:973
        except Exception as O0OOO00000OO00O0O :#line:975
            print (O0OOO00000OO00O0O )#line:976
def bundled_def ():#line:978
    OO00O0OO00000O00O =['5570536','7750212','7911652','7911680','7805624']#line:979
    return OO00O0OO00000O00O [random .randint (0 ,len (OO00O0OO00000O00O )-1 )]#line:980
def version_of_the_validation ():#line:984
    return str ((83 -56 )/10 )#line:985
def gitee_validation ():#line:988
    try :#line:989
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:990
    except :#line:991
        sys .exit (0 )#line:992
def update_the_validation ():#line:996
    try :#line:997
        O000OOOO0O0O000O0 =gitee_validation ()#line:998
        if version_of_the_validation ()<O000OOOO0O0O000O0 ['CityEarth']['edition']:#line:999
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOOO0O0O000O0["CityEarth"]["edition"]}   ❌')#line:1000
            print (f'更新内容=>>{O000OOOO0O0O000O0["CityEarth"]["content"]}   🎉')#line:1001
        else :#line:1002
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOOO0O0O000O0["CityEarth"]["edition"]}   ✅')#line:1003
            print (f'更新内容=>> {O000OOOO0O0O000O0["CityEarth"]["content"]}   🎉')#line:1004
    except Exception as OO00OOO000000O000 :#line:1005
        print (OO00OOO000000O000 )#line:1006
def os_qinglong ():#line:1009
    if application in os .environ :#line:1010
        OO00OO0OO00OO00OO =os .environ [application ].split ('\n')#line:1011
        if len (OO00OO0OO00OO00OO )>0 :#line:1012
            return OO00OO0OO00OO00OO #line:1013
        else :#line:1014
            print (f"{application}变量未启用")#line:1015
            print ('脚本退出')#line:1016
            sys .exit (1 )#line:1017
    else :#line:1018
        if token :#line:1019
            OO00OO0OO00OO00OO =token .split ('\n')#line:1020
            if len (OO00OO0OO00OO00OO )>0 :#line:1021
                return OO00OO0OO00OO00OO #line:1022
        else :#line:1023
            print (f"内置变量为空")#line:1024
            print ('脚本结束')#line:1025
            sys .exit (0 )#line:1026
if __name__ =='__main__':#line:1031
    start ()#line:1032
