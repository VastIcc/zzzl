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
@ 版本  3.0
"""
application = 'ce_token'  # 变量名
token = ''

##################################配置区##################################
energy = True              # True 为用金种子添加肥料    False 为不添加肥料和水滴
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.419541311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        OOOO0OOOO000OO000 =os_qinglong ()#line:10
        print (f"==========共找到{len(OOOO0OOOO000OO000)}个账号==========")#line:11
        for O0OOOOO00OO0O00OO in OOOO0OOOO000OO000 :#line:12
            OO0000000O0O0OO00 =[]#line:13
            print (f"------------正在执行第{OOOO0OOOO000OO000.index(O0OOOOO00OO0O00OO) + 1}个账号------------")#line:14
            O00O0OOO00O0OOOO0 =CityEarth (O0OOOOO00OO0O00OO ,OO0000000O0O0OO00 )#line:15
            def O00000O0000O00O0O ():#line:17
                if O00O0OOO00O0OOOO0 .base_info ():#line:19
                    O00O0OOO00O0OOOO0 .sealing ()#line:21
                    O00O0OOO00O0OOOO0 .invitenum ()#line:23
                    O00O0OOO00O0OOOO0 .game_map ()#line:25
                    O00O0OOO00O0OOOO0 .friends_invitation ()#line:27
                    O00O0OOO00O0OOOO0 .propsraffle ()#line:33
                    O00O0OOO00O0OOOO0 .synthetic ()#line:35
                    O00O0OOO00O0OOOO0 .crops_illustrated ()#line:37
                    O00O0OOO00O0OOOO0 .give_gold ()#line:39
                    O00O0OOO00O0OOOO0 .withdraw ()#line:41
            O0OOO00O0000O0O0O =threading .Thread (target =O00000O0000O00O0O )#line:43
            O0OOO00O0000O0O0O .start ()#line:44
            time .sleep (time_xx )#line:45
        print (f"------------正在处理推送通知------------")#line:46
        time .sleep (0.5 )#line:47
        OO0OO0O000OO0O0O0 =format_msg ()#line:48
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0OO0O000OO0O0O0 +' ')#line:49
    except Exception as OOOOO00OOO00O00O0 :#line:50
        print (OOOOO00OOO00O00O0 )#line:51
def give_gold (O00000O00OO0O0000 ,O0O00O0O0OO0O0OO0 ):#line:54
        try :#line:55
            O0O0O0O00O0OO0O00 =f'_doneeNo={O00000O00OO0O0000}&quantity={int(O0O00O0O0OO0O0OO0)}_{timi_new()}'#line:56
            O000OO000OOO0000O ={'source':'scsc','authorization':os_qinglong ()[0 ].split ('&')[0 ],'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00O0OO0O00 ),'signstring':O0O0O0O00O0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:67
            O000O0O000O0O0000 ={"quantity":int (O0O00O0O0OO0O0OO0 ),"doneeNo":O00000O00OO0O0000 }#line:71
            O00O0OOO0OOO0OOOO =requests .request ('post',f'{host}/finance/give-gold',headers =O000OO000OOO0000O ,data =O000O0O000O0O0000 ).json ()#line:72
            if 'status'in O00O0OOO0OOO0OOOO :#line:74
                if O00O0OOO0OOO0OOOO ['status']==200 :#line:75
                    if O00O0OOO0OOO0OOOO ['data']:#line:76
                        print (f'【赠送种子】:赠送{int(O0O00O0O0OO0O0OO0)}种子给{O00000O00OO0O0000}成功')#line:77
                        return True #line:78
                if O00O0OOO0OOO0OOOO ['status']==401 :#line:79
                    print (f'【赠送种子】:{O00O0OOO0OOO0OOOO["message"]}')#line:80
                    return False #line:81
                if O00O0OOO0OOO0OOOO ['status']==500 :#line:82
                    print (f'【赠送种子】:{O00O0OOO0OOO0OOOO["message"]}')#line:83
                    return False #line:84
            return False #line:85
        except Exception as O000OOO000OOO0OO0 :#line:86
            print (O000OOO000OOO0OO0 )#line:87
def sign (O0O000O0OOO0OO00O ):#line:90
    O0OOOO0O0OOO0O000 =hashlib .md5 (O0O000O0OOO0OO00O .encode ()).hexdigest ()#line:91
    O000O00OO000OO0OO =sc1 ()#line:92
    O0O0OOO00O0O00O0O =sc2 ()#line:93
    OOOO0O00O00O00000 =sc3 ()#line:94
    O0OO0000000OOO0OO =O000O00OO000OO0OO +O0OOOO0O0OOO0O000 +O0O0OOO00O0O00O0O +OOOO0O00O00O00000 #line:95
    O00000O00000000O0 =hashlib .md5 (O0OO0000000OOO0OO .encode ()).hexdigest ()#line:96
    return O00000O00000000O0 #line:97
def format_msg ():#line:101
    O000O0O0OO0O0O0OO =""#line:102
    for O00OOO000OOO0OO00 in msg_list :#line:103
        O000O0O0OO0O0O0OO +=str (O00OOO000OOO0OO00 )+"\r\n"#line:104
    return O000O0O0OO0O0O0OO #line:105
def sc1 ():#line:107
    return "scsc%^&*"#line:108
def timi_new ():#line:111
    return str (int (time .time ()*1000 ))#line:112
class CityEarth :#line:115
    def __init__ (OOOOO0O0O00O0O0O0 ,OO00000OOO0000OOO ,OOOO00000O000OOOO ):#line:117
        try :#line:118
            OOOOO0O0O00O0O0O0 .msg =OOOO00000O000OOOO #line:119
            OOOOO0O0O00O0O0O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:120
            OOOOO0O0O00O0O0O0 .token =OO00000OOO0000OOO .split ('&')[0 ]#line:121
            OOOOO0O0O00O0O0O0 .innerId =OO00000OOO0000OOO .split ('&')[1 ]#line:122
            OOOOO0O0O00O0O0O0 .doneeNo =OO00000OOO0000OOO .split ('&')[2 ]#line:123
        except :#line:124
            print ('变量格式错误')#line:125
    def base_info (OO0O000OO0O0O0OOO ):#line:128
        try :#line:129
            OO0O000OO0O0O0OOO .watched_ad ()#line:131
            O0O0OOOO0O0000000 =f'__{timi_new()}'#line:132
            OO0000OOOOO0O0OOO ={'source':'scsc','authorization':OO0O000OO0O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOO0O0000000 ),'signstring':O0O0OOOO0O0000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:143
            OOOOOOOO0000OO0O0 =requests .request ('get',f'{host}/user',headers =OO0000OOOOO0O0OOO ).json ()#line:144
            if 'status'in OOOOOOOO0000OO0O0 :#line:146
                if OOOOOOOO0000OO0O0 ['status']==200 :#line:147
                    OO0OOOO0O00OOO0O0 =OOOOOOOO0000OO0O0 ['data']['nickname']#line:148
                    OOOO000O0O00OOOO0 =OOOOOOOO0000OO0O0 ['data']['inner_id']#line:149
                    OO0OO0O00OO000000 =OOOOOOOO0000OO0O0 ['data']['assets']['gold']#line:150
                    OOOOOOOOO0O00OOO0 =OOOOOOOO0000OO0O0 ['data']['level']#line:151
                    print (f'【账号信息】:昵称:{OO0OOOO0O00OOO0O0[:5]}丨ID:{OOOO000O0O00OOOO0}丨等级:{OOOOOOOOO0O00OOO0}丨金种子:{str(OO0OO0O00OO000000).split(".")[0]}')#line:152
                if OOOOOOOO0000OO0O0 ['status']==401 :#line:153
                    print (OOOOOOOO0000OO0O0 ['message'])#line:154
                    OO0O000OO0O0O0OOO .msg .append ('有账号失效了')#line:155
                    return False #line:156
                if OOOOOOOO0000OO0O0 ['status']==500 :#line:157
                    return False #line:158
            return True #line:159
        except Exception as O00O0O0OO0O0O0OOO :#line:160
            print (O00O0O0OO0O0O0OOO )#line:161
    def sealing (O000OOO000OO00O00 ):#line:164
        try :#line:165
            OO0OOO00O00OO0O0O =f'__{timi_new()}'#line:166
            O0OO0O0OOOOO0O000 ={'source':'scsc','authorization':O000OOO000OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO00O00OO0O0O ),'signstring':OO0OOO00O00OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:177
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OO0O0OOOOO0O000 )#line:178
            requests .request ('get',f'{host}/packsack/list',headers =O0OO0O0OOOOO0O000 )#line:179
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OO0O0OOOOO0O000 )#line:180
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OO0O0OOOOO0O000 )#line:181
            requests .request ('get',f'{host}/user',headers =O0OO0O0OOOOO0O000 )#line:182
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OO0O0OOOOO0O000 )#line:183
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OO0O0OOOOO0O000 )#line:184
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OO0O0OOOOO0O000 )#line:185
            requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O0OOOOO0O000 )#line:186
            requests .request ('get',f'{host}/assets',headers =O0OO0O0OOOOO0O000 )#line:187
        except Exception as OO0O0OOO00OOOO00O :#line:188
            print (OO0O0OOO00OOOO00O )#line:189
    def withdraw (OO0OOOO00OOO0O000 ):#line:193
        O0OOO0OO00O0OOOO0 =f'__{timi_new()}'#line:194
        O000O00O0OOO0O0O0 ={'source':'scsc','authorization':OO0OOOO00OOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO00O0OOOO0 ),'signstring':O0OOO0OO00O0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:205
        O0000OOO00OO000OO =requests .request ('get',f'{host}/assets',headers =O000O00O0OOO0O0O0 ).json ()#line:206
        if 'status'in O0000OOO00OO000OO :#line:208
            if O0000OOO00OO000OO ['status']==200 :#line:209
                OO000OO00O0O0O00O =O0000OOO00OO000OO ['data']['cash']#line:210
                if float (OO000OO00O0O0O00O )>20 :#line:211
                    O0OOO0OO00O0OOOO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:212
                    O000O00O0OOO0O0O0 ={'authorization':OO0OOOO00OOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO00O0OOOO0 ),'signstring':O0OOO0OO00O0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:222
                    OOOOOOO0O0O0O00O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:223
                    O0000000000O0OOOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O000O00O0OOO0O0O0 ,data =OOOOOOO0O0O0O00O0 ).json ()#line:225
                    print (O0000000000O0OOOO )#line:226
    def invitenum (OOOO0OO0OO0OO0OOO ):#line:229
        O0OO000000O00OOOO =f'__{timi_new()}'#line:230
        OO0OO0OO0O0OOO00O ={'source':'scsc','authorization':OOOO0OO0OO0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000000O00OOOO ),'signstring':O0OO000000O00OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:241
        OO00O00OO000000OO =requests .request ('get',f'{host}/invite/invitenum',headers =OO0OO0OO0O0OOO00O ).json ()#line:242
        if 'status'in OO00O00OO000000OO :#line:244
            if OO00O00OO000000OO ['status']==200 :#line:245
                OOO0OOOO0O00OO0O0 =OO00O00OO000000OO ['data']['invited_count']#line:246
                O0O0O0OO0O0O0OO0O =OO00O00OO000000OO ['data']['invited_second_count']#line:247
                print (f'【我的邀请】:直邀好友:{OOO0OOOO0O00OO0O0}丨间邀好友:{O0O0O0OO0O0O0OO0O}')#line:248
    def game_map (O0O0000O00OO0O00O ):#line:251
        try :#line:252
            OOOO00O00OO0O0OO0 =f'__{timi_new()}'#line:253
            O00O00000O00OOO0O ={'source':'scsc','authorization':O0O0000O00OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O00OO0O0OO0 ),'signstring':OOOO00O00OO0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:264
            OOO000OOO00000O00 =requests .request ('get',f'{host}/game/map',headers =O00O00000O00OOO0O ).json ()#line:265
            if 'status'in OOO000OOO00000O00 :#line:267
                if OOO000OOO00000O00 ['status']==200 :#line:268
                    for O0000OOOOOO0O0000 in OOO000OOO00000O00 ['data']['list'][0 ]['crops']:#line:269
                        O0OOO00000O00OOO0 =O0000OOOOOO0O0000 ['level']#line:271
                        if O0OOO00000O00OOO0 ==41 :#line:272
                            O0O00OOO000OO0O00 =O0000OOOOOO0O0000 ['crop_name']#line:273
                            O0OOOO0OOO0OOOOO0 =O0000OOOOOO0O0000 ['count']#line:274
                            if O0OOOO0OOO0OOOOO0 >0 :#line:275
                                print (f'【农业资产】:{O0O00OOO000OO0O00}丨数量:{O0OOOO0OOO0OOOOO0}')#line:276
        except Exception as OOOOO0OO0OOOO0000 :#line:277
            print (OOOOO0OO0OOOO0000 )#line:278
    def give_gold (OOOO0OOOO0O000O0O ):#line:281
        try :#line:282
            OOO0000OOO00O00OO =f'__{timi_new()}'#line:283
            OOOOO0OOOO000O0O0 ={'source':'scsc','authorization':OOOO0OOOO0O000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OOO00O00OO ),'signstring':OOO0000OOO00O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:294
            OO0O0OO000OOO00OO =requests .request ('get',f'{host}/user',headers =OOOOO0OOOO000O0O0 ).json ()#line:295
            if 'status'in OO0O0OO000OOO00OO :#line:296
                if OO0O0OO000OOO00OO ['status']==200 :#line:297
                    if float (OOOO0OOOO0O000O0O .doneeNo )!=0 :#line:298
                        O00000OOO0O000000 =OO0O0OO000OOO00OO ['data']['assets']['gold']#line:299
                        if float (O00000OOO0O000000 )>float (OOOO0OOOO0O000O0O .innerId ):#line:300
                            O0000O00O0O00000O =int (float (O00000OOO0O000000 )/1.1 )#line:301
                            OOO0000OOO00O00OO =f'_doneeNo={OOOO0OOOO0O000O0O.doneeNo}&quantity={O0000O00O0O00000O}_{timi_new()}'#line:302
                            OOOOO0OOOO000O0O0 ={'source':'scsc','authorization':OOOO0OOOO0O000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OOO00O00OO ),'signstring':OOO0000OOO00O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:313
                            O0O0O0O0OOO00O0OO ={"quantity":O0000O00O0O00000O ,"doneeNo":OOOO0OOOO0O000O0O .doneeNo }#line:317
                            O0OOOOOOOO0OO0O0O =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOO0OOOO000O0O0 ,data =O0O0O0O0OOO00O0OO ).json ()#line:318
                            if 'status'in O0OOOOOOOO0OO0O0O :#line:320
                                if O0OOOOOOOO0OO0O0O ['status']==200 :#line:321
                                    if O0OOOOOOOO0OO0O0O ['data']:#line:322
                                        print (f'【赠送种子】:赠送{O0000O00O0O00000O}种子给{OOOO0OOOO0O000O0O.doneeNo}成功')#line:323
                    else :#line:324
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:325
        except Exception as O000OO00OOO0O0O00 :#line:326
            print (O000OO00OOO0O0O00 )#line:327
    def invitation (OO000O0OO00OOOO0O ):#line:329
        try :#line:330
            _O0000OOO0O00O0O0O =float (bundled_def ())/4 #line:331
            O00000O00O0OOO00O =f'_innerId={int(_O0000OOO0O00O0O0O)}_{timi_new()}'#line:332
            OO0OO0OO0O0OOOOOO ={'source':'scsc','authorization':OO000O0OO00OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O00O0OOO00O ),'signstring':O00000O00O0OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:343
            O00OO00OOOOOO0OOO ={"innerId":int (_O0000OOO0O00O0O0O )}#line:344
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO0OO0OO0O0OOOOOO ,data =O00OO00OOOOOO0OOO )#line:345
        except Exception as OOO0000OO0OOO00OO :#line:346
            print (OOO0000OO0OOO00OO )#line:347
    def winning_rewards (OOOOOOO00O00OOOO0 ):#line:350
        try :#line:351
            O0OOOO00000000000 =f'__{timi_new()}'#line:352
            O0O0O000OOOOO00OO ={'source':'scsc','authorization':OOOOOOO00O00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00000000000 ),'signstring':O0OOOO00000000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:363
            OOOOO00O0O0000000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O0O000OOOOO00OO ).json ()#line:364
            if 'status'in OOOOO00O0O0000000 :#line:366
                if OOOOO00O0O0000000 ['status']==200 :#line:367
                    if OOOOO00O0O0000000 ['data']['amount']:#line:368
                        OOOO0O00O00000O0O =OOOOO00O0O0000000 ['data']['amount']['gold']#line:369
                        return OOOO0O00O00000O0O #line:370
                    else :#line:371
                        return 0 #line:372
        except Exception as OOOO00OOO0OO0OO0O :#line:373
            print (OOOO00OOO0OO0OO0O )#line:374
    def certification (OO00OO00OOO0O0O0O ):#line:377
        try :#line:378
            O0OO0O0O0OO0OO0OO =f'__{timi_new()}'#line:379
            OO0000OO0OO000O00 ={'source':'scsc','authorization':OO00OO00OOO0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O0OO0OO0OO ),'signstring':O0OO0O0O0OO0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:390
            OOOO000O000OOOOOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0000OO0OO000O00 ).json ()#line:391
            if 'status'in OOOO000O000OOOOOO :#line:393
                if OOOO000O000OOOOOO ['status']==200 :#line:394
                    if OOOO000O000OOOOOO ['data']['result']:#line:395
                        O0000O0O0OO0OO0OO =OOOO000O000OOOOOO ['data']['nick_name']#line:396
                        return O0000O0O0OO0OO0OO #line:397
                    else :#line:398
                        return '未实名'#line:399
        except Exception as OO00O0O0000OOOO00 :#line:400
            print (OO00O0O0000OOOO00 )#line:401
    def crops_illustrated (OOO00OO000000O0OO ):#line:404
        try :#line:405
            OOOOO00OO0OOO00OO =f'__{timi_new()}'#line:406
            OO0OOO00OOO0000O0 ={'source':'scsc','authorization':OOO00OO000000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OO0OOO00OO ),'signstring':OOOOO00OO0OOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:417
            O0000O0O00OO00OOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0OOO00OOO0000O0 ).json ()#line:418
            if 'status'in O0000O0O00OO00OOO :#line:420
                if O0000O0O00OO00OOO ['status']==200 :#line:421
                    O0O000OOO00000O0O =O0000O0O00OO00OOO ['data'][0 ]['crops']#line:422
                    for O0O0000OO0O00OO0O in O0O000OOO00000O0O :#line:423
                        if O0O0000OO0O00OO0O ['ill_clover_award']:#line:424
                            if float (O0O0000OO0O00OO0O ['ill_clover_award'])>1 :#line:425
                                if O0O0000OO0O00OO0O ['is_finish']:#line:426
                                    if not O0O0000OO0O00OO0O ['is_getit']:#line:427
                                        if OOO00OO000000O0OO .certification ()!='未实名':#line:428
                                            OOOOO00OO0OOO00OO =f'_award_level={O0O0000OO0O00OO0O["level"]}_{timi_new()}'#line:429
                                            OO0OOO00OOO0000O0 ={'source':'scsc','authorization':OOO00OO000000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OO0OOO00OO ),'signstring':OOOOO00OO0OOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:440
                                            O0OOO0O0OO0O00O00 ={"award_level":O0O0000OO0O00OO0O ['level']}#line:441
                                            OO000OOOOOOO00000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0OOO00OOO0000O0 ,json =O0OOO0O0OO0O00O00 ).json ()#line:443
                                            if 'status'in OO000OOOOOOO00000 :#line:444
                                                if OO000OOOOOOO00000 ['status']==200 :#line:445
                                                    O0O000O0OOOOOOO00 =OO000OOOOOOO00000 ['data']['ill_clover_award']#line:446
                                                    print (f'【图鉴奖励】:领取{O0O0000OO0O00OO0O["crop_name"]}成就丨奖励{O0O000O0OOOOOOO00}☘️')#line:448
                                                if OO000OOOOOOO00000 ['status']==500 :#line:449
                                                    print (f'【图鉴奖励】:{OO000OOOOOOO00000["message"]}')#line:450
        except Exception as OOO0000OO0O00O0OO :#line:451
            print (OOO0000OO0O00O0OO )#line:452
    def watched_ad (OOO00O0OOOO0O0O00 ):#line:455
        try :#line:456
            O0OOOO0O000O00OOO =f'__{timi_new()}'#line:457
            O0O0OO00OO0OO00O0 ={'source':'scsc','authorization':OOO00O0OOOO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0O000O00OOO ),'signstring':O0OOOO0O000O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:468
            O0OO0OOO00OOOOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO00OO0OO00O0 ).json ()#line:469
            if 'status'in O0OO0OOO00OOOOOO0 :#line:471
                if O0OO0OOO00OOOOOO0 ['status']==200 :#line:472
                    if 'offlineInfo'in O0OO0OOO00OOOOOO0 ['data']:#line:473
                        time .sleep (random .randint (3 ,5 ))#line:474
                        OO0O0O00O00O000OO =O0OO0OOO00OOOOOO0 ['data']['offlineInfo']['off_minute']#line:475
                        O000OOO000OO0OO00 =float (O0OO0OOO00OOOOOO0 ['data']['silver'])/1000000000000 #line:476
                        time .sleep (1 )#line:477
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O0OO00OO0OO00O0 ).json ()#line:478
                        time .sleep (2 )#line:479
                        O000O0OO00OOO0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO00OO0OO00O0 ).json ()#line:480
                        if 'status'in O000O0OO00OOO0OO0 :#line:482
                            if O000O0OO00OOO0OO0 ['status']==200 :#line:483
                                OOO00O000000O00O0 =float (O000O0OO00OOO0OO0 ['data']['silver'])/1000000000000 #line:484
                                O0OOO0O0000O0O0O0 =str (OOO00O000000O00O0 -O000OOO000OO0OO00 )[:6 ]#line:485
                                print (f'【离线奖励】:翻倍离线{OO0O0O00O00O000OO}分钟奖励🌱数量:{O0OOO0O0000O0O0O0}t粒')#line:486
        except Exception as O0OO0O00O0OO00OOO :#line:487
            print (O0OO0O00O0OO00OOO )#line:488
    def user_ad (OO000OO0O000OOOO0 ):#line:491
        try :#line:492
            O0O000OO000000000 =f'__{timi_new()}'#line:493
            O0OOO000O0O000000 ={'source':'scsc','authorization':OO000OO0O000OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OO000000000 ),'signstring':O0O000OO000000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:504
            OO00OOOOO0OO0O000 =requests .request ('get',f'{host}/user/ad',headers =O0OOO000O0O000000 ).json ()#line:505
            if 'status'in OO00OOOOO0OO0O000 :#line:507
                if OO00OOOOO0OO0O000 ['status']==200 :#line:508
                    O000OO000O000OOOO =OO00OOOOO0OO0O000 ['data']['max_time']#line:509
                    OO0000O0OO000O000 =OO00OOOOO0OO0O000 ['data']['watch_time']#line:510
                    OOO0OO0OO00OOO00O =OO00OOOOO0OO0O000 ['data']['added_time']#line:511
                    print (f'【获取种子】:获取🌱剩余{OOO0OO0OO00OOO00O + O000OO000O000OOOO - OO0000O0OO000O000}次丨好友提供:{OOO0OO0OO00OOO00O}次')#line:512
                    if OOO0OO0OO00OOO00O +O000OO000O000OOOO -OO0000O0OO000O000 >0 :#line:513
                        time .sleep (random .randint (16 ,19 ))#line:514
                        O0O00O0OOOOO00OO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OOO000O0O000000 ).json ()#line:515
                        if 'status'in O0O00O0OOOOO00OO0 :#line:517
                            if O0O00O0OOOOO00OO0 ['status']==200 :#line:518
                                OO0000O0OO00000O0 =float (O0O00O0OOOOO00OO0 ['data']['silver'])/1000000000000 #line:519
                                print (f'【获取种子】:获得🌱:{int(OO0000O0OO00000O0)}t粒')#line:520
                                return True #line:521
                            if O0O00O0OOOOO00OO0 ['status']==500 :#line:522
                                OOOO000OOOO0O0000 =O0O00O0OOOOO00OO0 ['message']#line:523
                                print (f'【获取种子】:{OOOO000OOOO0O0000}')#line:524
                                return False #line:525
        except Exception as O000OO0O00O0000OO :#line:526
            print (O000OO0O00O0000OO )#line:527
    def synthetic (OO0O0O0O000OOOO0O ):#line:530
        global id ,g #line:531
        try :#line:532
            OOO00OO0OO0OO00O0 =OO0O0O0O000OOOO0O .level_new ()#line:533
            O00OOOO0OO0000000 =random .randint (9 ,11 )#line:534
            O0OOO0OO00OO0O0OO =f'_site=8&targetSite={O00OOOO0OO0000000}_{timi_new()}'#line:535
            OO00OO000OOO00000 ={'source':'scsc','authorization':OO0O0O0O000OOOO0O .token ,'timestamp':timi_new (),'sign':sign (O0OOO0OO00OO0O0OO ),'signstring':O0OOO0OO00OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:546
            OO00OOOOOO000O0O0 ={"site":int (8 ),"targetSite":int (O00OOOO0OO0000000 )}#line:547
            requests .request ('post',f'{host}/game/crops/move',headers =OO00OO000OOO00000 ,json =OO00OOOOOO000O0O0 )#line:548
            while True :#line:549
                O00OO000OOO00OO0O =f'__{timi_new()}'#line:550
                O00OOO000OO00000O ={'source':'scsc','authorization':OO0O0O0O000OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000OOO00OO0O ),'signstring':O00OO000OOO00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:561
                O0OO00000000O00O0 =requests .request ('get',f'{host}/game/getAllData',headers =O00OOO000OO00000O ).json ()#line:562
                if 'status'in O0OO00000000O00O0 :#line:564
                    if O0OO00000000O00O0 ['status']==200 :#line:565
                        OO0O00OO00OOOO0OO =O0OO00000000O00O0 ['data']['cropList']#line:566
                        O0OOOO0O0OOOO0OOO =O0OO00000000O00O0 ['data']['gameCoreDataDBid']#line:567
                        OOOO0O000O0OO000O =float (O0OO00000000O00O0 ['data']['silver'])/1000000000000 #line:568
                        O000O0O0OO00O0000 =0 #line:573
                        for OO000OOO000O00O0O in OO0O00OO00OOOO0OO :#line:574
                            if not OO000OOO000O00O0O :#line:575
                                O000000O00O0O0000 =f'_crop_id={O0OOOO0O0OOOO0OOO}&site={O000O0O0OO00O0000}_{OO0O0O0O000OOOO0O.time}'#line:576
                                OO000O000O0O00O0O ={'source':'scsc','authorization':OO0O0O0O000OOOO0O .token ,'timestamp':OO0O0O0O000OOOO0O .time ,'sign':sign (O000000O00O0O0000 ),'signstring':O000000O00O0O0000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:586
                                OOOO000O00O00OOOO ={"site":O000O0O0OO00O0000 ,"crop_id":O0OOOO0O0OOOO0OOO }#line:587
                                OOOOO0O00O000OO0O =requests .request ('post',f'{host}/game/crops/buy',headers =OO000O000O0O00O0O ,data =OOOO000O00O00OOOO ).json ()#line:588
                                time .sleep (random .randint (1 ,3 )/10 )#line:590
                                if 'status'in OOOOO0O00O000OO0O :#line:591
                                    if OOOOO0O00O000OO0O ['status']==200 :#line:592
                                        if OOOOO0O00O000OO0O ['message']=='种子数量不足':#line:593
                                            OOO00OO0OO0OO00O0 =OO0O0O0O000OOOO0O .level_new ()#line:594
                                            print (f'【种植合成】:{OOOOO0O00O000OO0O["message"]}')#line:595
                                            if not OO0O0O0O000OOOO0O .user_ad ():#line:596
                                                return False #line:597
                                    if OOOOO0O00O000OO0O ['status']==500 :#line:598
                                        print (f'【种植合成】:{OOOOO0O00O000OO0O["message"]}')#line:599
                                        return False #line:600
                            O000O0O0OO00O0000 +=1 #line:601
                        OOO0O0O0000OOOOOO =requests .request ('get',f'{host}/game/getAllData',headers =O00OOO000OO00000O ).json ()#line:602
                        O0000O0OO000OO000 =OOO0O0O0000OOOOOO ['data']['cropList']#line:603
                        O00OOOO000000O000 =False #line:604
                        for OO000OOO000O00O0O in range (12 ):#line:605
                            id =O0000O0OO000OO000 [OO000OOO000O00O0O ]['level']#line:606
                            if float (OOO00OO0OO0OO00O0 )-float (id )>9 :#line:607
                                O0000000OO0000OO0 =f'_site={OO000OOO000O00O0O}_{timi_new()}'#line:608
                                O0O00O00O0O00OOOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0O0O0O000OOOO0O .token ,'timestamp':timi_new (),'sign':sign (O0000000OO0000OO0 ),'signstring':O0000000OO0000OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:619
                                O0OO000000OOOOOOO ={"site":OO000OOO000O00O0O }#line:620
                                O0O00O0O0O0O00OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O00O00O0O00OOOO ,data =O0OO000000OOOOOOO ).json ()#line:622
                                if 'status'in O0O00O0O0O0O00OOO :#line:623
                                    if O0O00O0O0O0O00OOO ['status']==200 :#line:624
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:625
                            if id !=0 :#line:626
                                for OOOO000000O0O0O0O in range (11 ):#line:627
                                    OO0OOOO00O0O0OOOO =OOOO000000O0O0O0O +1 #line:628
                                    g =O0000O0OO000OO000 [OO0OOOO00O0O0OOOO ]['level']#line:629
                                    if id ==g :#line:630
                                        O0OOOOOOO0O0O00O0 =OOOO000000O0O0O0O +2 #line:631
                                        if O0OOOOOOO0O0O00O0 !=OO000OOO000O00O0O +1 :#line:632
                                            O000OO000O0O00O0O =OO000OOO000O00O0O +1 #line:633
                                            time .sleep (random .randint (1 ,3 )/10 )#line:635
                                            O0OOO0OO00OO0O0OO =f'_site={O000OO000O0O00O0O - 1}&targetSite={O0OOOOOOO0O0O00O0 - 1}_{timi_new()}'#line:636
                                            OO00OO000OOO00000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0O0O0O000OOOO0O .token ,'timestamp':timi_new (),'sign':sign (O0OOO0OO00OO0O0OO ),'signstring':O0OOO0OO00OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:653
                                            OOOOOO000OO0000O0 ={"site":int (O000OO000O0O00O0O -1 ),"targetSite":int (O0OOOOOOO0O0O00O0 -1 )}#line:654
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO00OO000OOO00000 ,json =OOOOOO000OO0000O0 )#line:655
                                            O00OOOO000000O000 =True #line:657
                                    if O00OOOO000000O000 :#line:658
                                        break #line:659
                                if O00OOOO000000O000 :#line:660
                                    break #line:661
        except :#line:662
            OO0O0O0O000OOOO0O .synthetic ()#line:663
    def level_new (O0OO00OOOOOO0OO0O ):#line:666
        try :#line:667
            OOOOO00O0OOO000O0 =f'__{timi_new()}'#line:668
            OOOO0O000OO0OO0OO ={'source':'scsc','authorization':O0OO00OOOOOO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0OOO000O0 ),'signstring':OOOOO00O0OOO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:679
            OO00OO00OO0OO00OO =requests .request ('get',f'{host}/user',headers =OOOO0O000OO0OO0OO ).json ()#line:680
            if 'status'in OO00OO00OO0OO00OO :#line:681
                if OO00OO00OO0OO00OO ['status']==200 :#line:682
                    return float (OO00OO00OO0OO00OO ['data']['level'])#line:683
        except Exception as O00OO00OO000O00OO :#line:684
            print (O00OO00OO000O00OO )#line:685
    def propsraffle (O0OO0OOOOO00OO000 ):#line:688
        try :#line:689
            while True :#line:690
                O0000O000O0OO00OO =f'__{timi_new()}'#line:691
                OOO0O00OOOO00OOOO ={'source':'scsc','authorization':O0OO0OOOOO00OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O000O0OO00OO ),'signstring':O0000O000O0OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:702
                O00000O0OOOOO0O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO0O00OOOO00OOOO ).json ()#line:703
                if 'status'in O00000O0OOOOO0O0O :#line:705
                    if O00000O0OOOOO0O0O ['status']==200 :#line:706
                        OOO00O00OOO00O0O0 =O00000O0OOOOO0O0O ['data']['rows']#line:707
                        OOOO00O0O00OOOO00 =O00000O0OOOOO0O0O ['data']['vstate']#line:708
                        if OOO00O00OOO00O0O0 ==5 or OOO00O00OOO00O0O0 ==6 or OOO00O00OOO00O0O0 ==7 :#line:709
                            OO0000O00000O0O0O =O00000O0OOOOO0O0O ['data']['silver']#line:710
                            print (f'【转盘抽奖】:获得种子:{OO0000O00000O0O0O}')#line:711
                        if OOO00O00OOO00O0O0 ==1 or OOO00O00OOO00O0O0 ==2 or OOO00O00OOO00O0O0 ==3 :#line:712
                            OOO0O0OOO00OO0OO0 =O00000O0OOOOO0O0O ['data']['clover']#line:713
                            print (f'【转盘抽奖】:获得三叶草:{OOO0O0OOO00OO0OO0}')#line:714
                        if OOO00O00OOO00O0O0 ==4 or OOO00O00OOO00O0O0 ==8 :#line:715
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:716
                        if OOO00O00OOO00O0O0 =='抽奖次数已用完':#line:720
                            break #line:754
                time .sleep (random .randint (8 ,15 )/10 )#line:755
        except Exception as OOO0OO00O0OOO0OO0 :#line:756
            print (OOO0OO00O0OOO0OO0 )#line:757
    def friends_invitation (OOOO000000O0000O0 ):#line:760
        try :#line:761
            O00OOOO00OO00O00O =f'__{timi_new()}'#line:762
            O0000O0OO0O00000O ={'source':'scsc','authorization':OOOO000000O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO00OO00O00O ),'signstring':O00OOOO00OO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:773
            O00OOOOOOOO0O00OO =requests .request ('get',f'{host}/friends',headers =O0000O0OO0O00000O ).json ()#line:774
            if 'status'in O00OOOOOOOO0O00OO :#line:775
                if O00OOOOOOOO0O00OO ['status']==200 :#line:776
                    O000OOO000O0O0OOO =O00OOOOOOOO0O00OO ['data']['myInviteter']#line:777
                    if O000OOO000O0O0OOO :#line:778
                        OOO0000O0OO00000O =O000OOO000O0O0OOO ['user']['nickname']#line:779
                        O00O000OOOOOOOO0O =OOOO000000O0000O0 .certification ()#line:780
                        print (f'【查邀请人】:我的邀请人:{OOO0000O0OO00000O}丨实名:{O00O000OOOOOOOO0O}')#line:781
                    else :#line:782
                        if OOOO000000O0000O0 .innerId !='0':#line:783
                            OOOO000000O0000O0 .invitation ()#line:784
        except Exception as O0O000000O0OO0O0O :#line:785
            print (O0O000000O0OO0O0O )#line:786
    def add_clover (OO000OOOO00O000O0 ):#line:789
        global golden_seed #line:790
        try :#line:791
            O000O000O00000000 =f'__{timi_new()}'#line:792
            O0O00OOO0000O000O ={'source':'scsc','authorization':OO000OOOO00O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000O00000000 ),'signstring':O000O000O00000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:803
            OOO000O00O00000O0 =requests .request ('get',f'{host}/assets/clovers',headers =O0O00OOO0000O000O ).json ()#line:804
            if 'status'in OOO000O00O00000O0 :#line:806
                if OOO000O00O00000O0 ['status']==200 :#line:807
                    O00OOOO0O0O0OOOO0 =OOO000O00O00000O0 ['data']['clover']#line:808
                    O00OOO000O0O0O0OO =OOO000O00O00000O0 ['data']['used_clover']#line:809
                    OOOO000OO000O0OOO =float (O00OOOO0O0O0OOOO0 )-float (O00OOO000O0O0O0OO )#line:810
                    print (f'【参与抽奖】:参与抽奖的☘️:{O00OOO000O0O0O0OO}')#line:811
                    if OO000OOOO00O000O0 .certification ()!='未实名':#line:812
                        if OOOO000OO000O0OOO >1 :#line:813
                            O000O000O00000000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOO000OO000O0OOO)}_{timi_new()}'#line:814
                            O00O000OO000OO00O ={'source':'scsc','authorization':OO000OOOO00O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000O00000000 ),'signstring':O000O000O00000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:825
                            O0OO0OO0OOO0O00OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOO000OO000O0OOO )}#line:826
                            O0000OO0OOOOO0OOO =requests .request ('post',f'{host}/lottery/add-stake',headers =O00O000OO000OO00O ,data =O0OO0OO0OOO0O00OO ).json ()#line:827
                            if 'status'in O0000OO0OOOOO0OOO :#line:829
                                if O0000OO0OOOOO0OOO ['status']==200 :#line:830
                                    print (f'【参与抽奖】:添加☘️:{O0000OO0OOOOO0OOO["data"]}丨数量:{OOOO000OO000O0OOO}')#line:831
                                if O0000OO0OOOOO0OOO ['status']==500 :#line:832
                                    print (f'【参与抽奖】:添加☘️:{O0000OO0OOOOO0OOO["message"]}')#line:833
            OOO000O0O00O00O00 =requests .request ('get',f'{host}/lottery',headers =O0O00OOO0000O000O ).json ()#line:834
            O0OO00O0O00O0O00O =OO000OOOO00O000O0 .winning_rewards ()#line:836
            if 'status'in OOO000O0O00O00O00 :#line:837
                if OOO000O0O00O00O00 ['status']==200 :#line:838
                    O00OOOOOO0OOO0O0O =OOO000O0O00O00O00 ['data'][0 ]['day_get_gold_quantity']#line:839
                    golden_seed +=float (O00OOOOOO0OOO0O0O )#line:840
                    O0O0O000000000O0O =OOO000O0O00O00O00 ['data'][1 ]['value']#line:841
                    O0000O00OO000O00O =OOO000O0O00O00O00 ['data'][0 ]['join_number']#line:842
                    OO0O00OOOOO000000 =int (float (OOO000O0O00O00O00 ['data'][0 ]['totalValue']))#line:843
                    OO0OO00000O00O0O0 =float (O0O0O000000000O0O /OO0O00OOOOO000000 )*10000 #line:844
                    O0OO0O0O00OOO00OO =OO0O00OOOOO000000 /O0000O00OO000O00O #line:845
                    print (f'【参与抽奖】:预计每天中{str(O00OOOOOO0OOO0O0O)[:6]}颗金种子丨好友收益:{str(O0OO00O0O00O0O00O)[:6]}')#line:846
                    print (f'【抽奖统计】:每1万☘️中{str(OO0OO00000O00O0O0)[:6]}颗金种子丨☘️人均:{str(O0OO0O0O00OOO00OO)[:7]}️')#line:847
        except Exception as O00O0O0000O00O0OO :#line:848
            print (O00O0O0000O00O0OO )#line:849
    def energy (OO00OOOO0OO0O0O00 ):#line:853
        try :#line:854
            while True :#line:855
                OOOO0000O0OO00O0O =f'__{timi_new()}'#line:856
                O00OO000OOO00O0O0 ={'source':'scsc','authorization':OO00OOOO0OO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000O0OO00O0O ),'signstring':OOOO0000O0OO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:867
                O00OOOOO0OO0O00O0 =requests .request ('get',f'{host}/energy/general',headers =O00OO000OOO00O0O0 ).json ()#line:868
                if 'status'in O00OOOOO0OO0O00O0 :#line:870
                    if O00OOOOO0OO0O00O0 ['status']==200 :#line:871
                        OO00OOOO0OO000OOO =O00OOOOO0OO0O00O0 ['data']['ordinary_water']#line:872
                        OOO0O0OOOOOO000O0 =O00OOOOO0OO0O00O0 ['data']['ordinary_fertilizer']#line:873
                        O000O00OOOOOO00O0 =O00OOOOO0OO0O00O0 ['data']['videoStatus']#line:874
                        OO00000OO0000O00O =O00OOOOO0OO0O00O0 ['data']['waterVideoKey']#line:875
                        print (f'【我的营养】:肥料:{str(OOO0O0OOOOOO000O0).split(".")[0]}丨水滴:{str(OO00OOOO0OO000OOO).split(".")[0]}')#line:876
                        if float (OOO0O0OOOOOO000O0 )<96 :#line:877
                            if O000O00OOOOOO00O0 :#line:878
                                time .sleep (random .randint (160 ,180 )/10 )#line:879
                                O0OOO0OO0O0OO000O =99 -float (OOO0O0OOOOOO000O0 )#line:880
                                O0OO00O000OO0OOOO ={"fertilizer":str (O0OOO0OO0O0OO000O ).split ('.')[0 ]}#line:881
                                OOO00000O0O00000O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00OO000OOO00O0O0 ).json ()#line:882
                                if 'status'in OOO00000O0O00000O :#line:884
                                    if OOO00000O0O00000O ['status']==200 :#line:885
                                        print (f'【购买肥料】:看广告获取肥料:{OOO00000O0O00000O["message"]}')#line:886
                                    if OOO00000O0O00000O ['status']==500 :#line:887
                                        print (f'【购买肥料】:看广告获取肥料:{OOO00000O0O00000O["message"]}')#line:888
                                        break #line:889
                            if energy :#line:890
                                if float (OOO0O0OOOOOO000O0 )<78 :#line:891
                                    O0OOO0OO0O0OO000O =80 -float (OOO0O0OOOOOO000O0 )#line:892
                                    O0O00OO000OO000O0 =f'_fertilizer={int(O0OOO0OO0O0OO000O)}_{timi_new()}'#line:893
                                    OO00O000OOOOO000O ={'source':'scsc','authorization':OO00OOOO0OO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO000OO000O0 ),'signstring':O0O00OO000OO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:904
                                    O00O0O00000OOO0OO ={"fertilizer":int (O0OOO0OO0O0OO000O )}#line:905
                                    OOO0000O0OOOOO0O0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO00O000OOOOO000O ,data =O00O0O00000OOO0OO ).json ()#line:906
                                    if 'status'in OOO0000O0OOOOO0O0 :#line:908
                                        if OOO0000O0OOOOO0O0 ['status']==200 :#line:909
                                            print (f'【购买肥料】:购买肥料:{OOO0000O0OOOOO0O0["message"]}丨数量:{int(O0OOO0OO0O0OO000O)}')#line:910
                                        if OOO0000O0OOOOO0O0 ['status']==500 :#line:911
                                            print (f'【购买肥料】:购买肥料:{OOO0000O0OOOOO0O0["message"]}丨数量:{int(O0OOO0OO0O0OO000O)}')#line:912
                                            O0000OO0O00OO0OO0 =OOO0000O0OOOOO0O0 ["message"].split ('-')[1 ]#line:913
                                            OOOO0OO00O0O0O0OO =f'__{timi_new()}'#line:914
                                            O0OOO000OOO0OO0OO ={'source':'scsc','authorization':OO00OOOO0OO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00O0O0O0OO ),'signstring':OOOO0OO00O0O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:925
                                            O0OOOO00OO000000O =requests .request ('get',f'{host}/user',headers =O0OOO000OOO0OO0OO ).json ()#line:926
                                            if 'status'in O0OOOO00OO000000O :#line:927
                                                if O0OOOO00OO000000O ['status']==200 :#line:928
                                                    OOOOO0O00OO0O0OOO =O0OOOO00OO000000O ['data']['inner_id']#line:929
                                                    if give_gold (OOOOO0O00OO0O0OOO ,float (O0000OO0O00OO0OO0 )+1 ):#line:930
                                                        OO00OOOO0OO0O0O00 .energy ()#line:931
                        if float (OO00OOOO0OO000OOO )<880 :#line:932
                            if OO00000OO0000O00O :#line:933
                                time .sleep (random .randint (160 ,180 )/10 )#line:934
                                O0O00OOOO00000OO0 =999 -float (OO00OOOO0OO000OOO )#line:935
                                OOOOO0000OO0O0O0O ={"water":str (O0O00OOOO00000OO0 ).split ('.')[0 ]}#line:936
                                O0O0O00OOO00O0OO0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00OO000OOO00O0O0 ).json ()#line:937
                                if 'status'in O0O0O00OOO00O0OO0 :#line:939
                                    if O0O0O00OOO00O0OO0 ['status']==200 :#line:940
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0O00OOO00O0OO0["message"]}')#line:941
                                    if O0O0O00OOO00O0OO0 ['status']==500 :#line:942
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0O00OOO00O0OO0["message"]}')#line:943
                                        break #line:944
                            if energy :#line:945
                                if float (OO00OOOO0OO000OOO )<780 :#line:946
                                    O0O00OOOO00000OO0 =800 -float (OO00OOOO0OO000OOO )#line:947
                                    O000O00OOO0OO00OO =f'_water={int(O0O00OOOO00000OO0)}_{timi_new()}'#line:948
                                    OOO0OO0OOOO00OO0O ={'source':'scsc','authorization':OO00OOOO0OO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00OOO0OO00OO ),'signstring':O000O00OOO0OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:959
                                    O0OO0OO00OO0OO0OO ={"water":int (O0O00OOOO00000OO0 )}#line:960
                                    OOOO00O0O00OO0OOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO0OO0OOOO00OO0O ,data =O0OO0OO00OO0OO0OO ).json ()#line:962
                                    if 'status'in OOOO00O0O00OO0OOO :#line:964
                                        if OOOO00O0O00OO0OOO ['status']==200 :#line:965
                                            print (f'【购买水滴】:购买水滴:{OOOO00O0O00OO0OOO["message"]}丨数量:{int(O0O00OOOO00000OO0)}')#line:966
                                        if OOOO00O0O00OO0OOO ['status']==500 :#line:967
                                            print (f'【购买水滴】:购买水滴:{OOOO00O0O00OO0OOO["message"]}丨数量:{int(O0O00OOOO00000OO0)}')#line:968
                                            O0000OO0O00OO0OO0 =OOOO00O0O00OO0OOO ["message"].split ('-')[1 ]#line:969
                                            OOOO0OO00O0O0O0OO =f'__{timi_new()}'#line:970
                                            O0OOO000OOO0OO0OO ={'source':'scsc','authorization':OO00OOOO0OO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00O0O0O0OO ),'signstring':OOOO0OO00O0O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:981
                                            O0OOOO00OO000000O =requests .request ('get',f'{host}/user',headers =O0OOO000OOO0OO0OO ).json ()#line:982
                                            if 'status'in O0OOOO00OO000000O :#line:983
                                                if O0OOOO00OO000000O ['status']==200 :#line:984
                                                    OOOOO0O00OO0O0OOO =O0OOOO00OO000000O ['data']['inner_id']#line:985
                                                    if give_gold (OOOOO0O00OO0O0OOO ,float (O0000OO0O00OO0OO0 )+1 ):#line:986
                                                        OO00OOOO0OO0O0O00 .energy ()#line:987
                        break #line:988
        except Exception as OO0OO00OO00O0OO0O :#line:990
            print (OO0OO00OO00O0OO0O )#line:991
def bundled_def ():#line:993
    O000OO0OO00OO0OOO =['5570536','7750212','7911652','7911680','7805624']#line:994
    return O000OO0OO00OO0OOO [random .randint (0 ,len (O000OO0OO00OO0OOO )-1 )]#line:995
def version_of_the_validation ():#line:999
    return str ((86 -56 )/10 )#line:1000
def sc2 ():#line:1002
    return "19319#$%^&*((*"#line:1003
def gitee_validation ():#line:1005
    try :#line:1006
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:1007
    except :#line:1008
        sys .exit (0 )#line:1009
def update_the_validation ():#line:1013
    try :#line:1014
        O00OOOOO0OO00O0OO =gitee_validation ()#line:1015
        if version_of_the_validation ()<O00OOOOO0OO00O0OO ['CityEarth']['edition']:#line:1016
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OOOOO0OO00O0OO["CityEarth"]["edition"]}   ❌')#line:1017
            print (f'更新内容=>>{O00OOOOO0OO00O0OO["CityEarth"]["content"]}   🎉')#line:1018
        else :#line:1019
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OOOOO0OO00O0OO["CityEarth"]["edition"]}   ✅')#line:1020
            print (f'更新内容=>> {O00OOOOO0OO00O0OO["CityEarth"]["content"]}   🎉')#line:1021
    except Exception as OO0O0OOOO0OO00OO0 :#line:1022
        print (OO0O0OOOO0OO00OO0 )#line:1023
def sc3 ():#line:1025
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1026
def os_qinglong ():#line:1028
    if application in os .environ :#line:1029
        O0OO0OO00O000OOO0 =os .environ [application ].split ('\n')#line:1030
        if len (O0OO0OO00O000OOO0 )>0 :#line:1031
            return O0OO0OO00O000OOO0 #line:1032
        else :#line:1033
            print (f"{application}变量未启用")#line:1034
            print ('脚本退出')#line:1035
            sys .exit (1 )#line:1036
    else :#line:1037
        if token :#line:1038
            O0OO0OO00O000OOO0 =token .split ('\n')#line:1039
            if len (O0OO0OO00O000OOO0 )>0 :#line:1040
                return O0OO0OO00O000OOO0 #line:1041
        else :#line:1042
            print (f"内置变量为空")#line:1043
            print ('脚本结束')#line:1044
            sys .exit (0 )#line:1045
if __name__ =='__main__':#line:1050
    start ()#line:1051
