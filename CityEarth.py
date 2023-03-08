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
        O000OO00000O00000 =os_qinglong ()#line:10
        print (f"==========共找到{len(O000OO00000O00000)}个账号==========")#line:11
        for OOO0OO0O0O00OOOOO in O000OO00000O00000 :#line:12
            O00OOOOO00OOOO0O0 =[]#line:13
            print (f"------------正在执行第{O000OO00000O00000.index(OOO0OO0O0O00OOOOO) + 1}个账号------------")#line:14
            OO0OOOO000OO0OOOO =CityEarth (OOO0OO0O0O00OOOOO ,O00OOOOO00OOOO0O0 )#line:15
            def O00OO0OOOOO0000OO ():#line:17
                if OO0OOOO000OO0OOOO .base_info ():#line:19
                    OO0OOOO000OO0OOOO .sealing ()#line:21
                    OO0OOOO000OO0OOOO .invitenum ()#line:23
                    OO0OOOO000OO0OOOO .game_map ()#line:25
                    OO0OOOO000OO0OOOO .friends_invitation ()#line:27
                    OO0OOOO000OO0OOOO .energy ()#line:29
                    OO0OOOO000OO0OOOO .add_clover ()#line:31
                    OO0OOOO000OO0OOOO .propsraffle ()#line:33
                    OO0OOOO000OO0OOOO .synthetic ()#line:35
                    OO0OOOO000OO0OOOO .crops_illustrated ()#line:37
                    OO0OOOO000OO0OOOO .give_gold ()#line:39
                    OO0OOOO000OO0OOOO .withdraw ()#line:41
            OO0O00O0OOOO0O000 =threading .Thread (target =O00OO0OOOOO0000OO )#line:43
            OO0O00O0OOOO0O000 .start ()#line:44
            time .sleep (time_xx )#line:45
        print (f"------------正在处理推送通知------------")#line:46
        time .sleep (0.5 )#line:47
        O000O00OOOO000000 =format_msg ()#line:48
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O000O00OOOO000000 +' ')#line:49
    except Exception as OO0O00O0OOO0000OO :#line:50
        print (OO0O00O0OOO0000OO )#line:51
def give_gold (OOOO000O00OO00OO0 ,OOOOOO0OOO0O0OO00 ):#line:54
        try :#line:55
            OOOO0O00OOOOO0OOO =f'_doneeNo={OOOO000O00OO00OO0}&quantity={int(OOOOOO0OOO0O0OO00)}_{timi_new()}'#line:56
            OOO00OOO00OOOOO00 ={'source':'scsc','authorization':os_qinglong ()[0 ].split ('&')[0 ],'timestamp':str (timi_new ()),'sign':sign (OOOO0O00OOOOO0OOO ),'signstring':OOOO0O00OOOOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:67
            O00000O0O00O0OO0O ={"quantity":int (OOOOOO0OOO0O0OO00 ),"doneeNo":OOOO000O00OO00OO0 }#line:71
            OOO00OO0OOO0OO00O =requests .request ('post',f'{host}/finance/give-gold',headers =OOO00OOO00OOOOO00 ,data =O00000O0O00O0OO0O ).json ()#line:72
            if 'status'in OOO00OO0OOO0OO00O :#line:74
                if OOO00OO0OOO0OO00O ['status']==200 :#line:75
                    if OOO00OO0OOO0OO00O ['data']:#line:76
                        print (f'【赠送种子】:赠送{int(OOOOOO0OOO0O0OO00)}种子给{OOOO000O00OO00OO0}成功')#line:77
                        return True #line:78
                if OOO00OO0OOO0OO00O ['status']==401 :#line:79
                    print (f'【赠送种子】:{OOO00OO0OOO0OO00O["message"]}')#line:80
                    return False #line:81
                if OOO00OO0OOO0OO00O ['status']==500 :#line:82
                    print (f'【赠送种子】:{OOO00OO0OOO0OO00O["message"]}')#line:83
                    return False #line:84
            return False #line:85
        except Exception as O00OO000OO000OOOO :#line:86
            print (O00OO000OO000OOOO )#line:87
def sign (O00O0OO0OOO00O0O0 ):#line:90
    OO0OO00OOO0O0O0O0 =hashlib .md5 (O00O0OO0OOO00O0O0 .encode ()).hexdigest ()#line:91
    O000O00OO00O0O0O0 =sc1 ()#line:92
    O000O0O0O0OO00OO0 =sc2 ()#line:93
    OO0OOO000O000OO0O =sc3 ()#line:94
    O0O000000O00OO000 =O000O00OO00O0O0O0 +OO0OO00OOO0O0O0O0 +O000O0O0O0OO00OO0 +OO0OOO000O000OO0O #line:95
    O0O0O0O0O0O000OOO =hashlib .md5 (O0O000000O00OO000 .encode ()).hexdigest ()#line:96
    return O0O0O0O0O0O000OOO #line:97
def format_msg ():#line:101
    OOO0O00O0000000OO =""#line:102
    for O00O000OOOOO0OOOO in msg_list :#line:103
        OOO0O00O0000000OO +=str (O00O000OOOOO0OOOO )+"\r\n"#line:104
    return OOO0O00O0000000OO #line:105
def sc1 ():#line:107
    return "scsc%^&*"#line:108
def timi_new ():#line:111
    return str (int (time .time ()*1000 ))#line:112
class CityEarth :#line:115
    def __init__ (OOO00OO00OO00000O ,O0O0OO0O00000OO00 ,O00O0O0O0O00O000O ):#line:117
        try :#line:118
            OOO00OO00OO00000O .msg =O00O0O0O0O00O000O #line:119
            OOO00OO00OO00000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:120
            OOO00OO00OO00000O .token =O0O0OO0O00000OO00 .split ('&')[0 ]#line:121
            OOO00OO00OO00000O .innerId =O0O0OO0O00000OO00 .split ('&')[1 ]#line:122
            OOO00OO00OO00000O .doneeNo =O0O0OO0O00000OO00 .split ('&')[2 ]#line:123
        except :#line:124
            print ('变量格式错误')#line:125
    def base_info (O0O0000O0O000O0OO ):#line:128
        try :#line:129
            O0O0000O0O000O0OO .watched_ad ()#line:131
            OOOO00000OOOO00OO =f'__{timi_new()}'#line:132
            OO0O00O0OO0O0O000 ={'source':'scsc','authorization':O0O0000O0O000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00000OOOO00OO ),'signstring':OOOO00000OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:143
            OO0OO00OOO0OOO00O =requests .request ('get',f'{host}/user',headers =OO0O00O0OO0O0O000 ).json ()#line:144
            if 'status'in OO0OO00OOO0OOO00O :#line:146
                if OO0OO00OOO0OOO00O ['status']==200 :#line:147
                    OO0O0OOOOOO0OOO0O =OO0OO00OOO0OOO00O ['data']['nickname']#line:148
                    O0O0000O0O0O0OO00 =OO0OO00OOO0OOO00O ['data']['inner_id']#line:149
                    O0OO000OO0OOO00OO =OO0OO00OOO0OOO00O ['data']['assets']['gold']#line:150
                    OOOO0OO000000OO00 =OO0OO00OOO0OOO00O ['data']['level']#line:151
                    print (f'【账号信息】:昵称:{OO0O0OOOOOO0OOO0O[:5]}丨ID:{O0O0000O0O0O0OO00}丨等级:{OOOO0OO000000OO00}丨金种子:{str(O0OO000OO0OOO00OO).split(".")[0]}')#line:152
                if OO0OO00OOO0OOO00O ['status']==401 :#line:153
                    print (OO0OO00OOO0OOO00O ['message'])#line:154
                    O0O0000O0O000O0OO .msg .append ('有账号失效了')#line:155
                    return False #line:156
                if OO0OO00OOO0OOO00O ['status']==500 :#line:157
                    return False #line:158
            return True #line:159
        except Exception as O0OOOOO0O0O0O0O0O :#line:160
            print (O0OOOOO0O0O0O0O0O )#line:161
    def sealing (OOO0O0OO0O0000000 ):#line:164
        try :#line:165
            O0000OO000OOOOOOO =f'__{timi_new()}'#line:166
            O00O0O0OO0O0OO0O0 ={'source':'scsc','authorization':OOO0O0OO0O0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO000OOOOOOO ),'signstring':O0000OO000OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:177
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00O0O0OO0O0OO0O0 )#line:178
            requests .request ('get',f'{host}/packsack/list',headers =O00O0O0OO0O0OO0O0 )#line:179
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00O0O0OO0O0OO0O0 )#line:180
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00O0O0OO0O0OO0O0 )#line:181
            requests .request ('get',f'{host}/user',headers =O00O0O0OO0O0OO0O0 )#line:182
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00O0O0OO0O0OO0O0 )#line:183
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00O0O0OO0O0OO0O0 )#line:184
            requests .request ('post',f'{host}/announcement/announcement',headers =O00O0O0OO0O0OO0O0 )#line:185
            requests .request ('get',f'{host}/game/getAllData',headers =O00O0O0OO0O0OO0O0 )#line:186
            requests .request ('get',f'{host}/assets',headers =O00O0O0OO0O0OO0O0 )#line:187
        except Exception as OO00O00O0OOOO0OOO :#line:188
            print (OO00O00O0OOOO0OOO )#line:189
    def withdraw (O0O00OOOO00OOO000 ):#line:193
        OOOO00O0O00O000OO =f'__{timi_new()}'#line:194
        OOO00OO00O000OO00 ={'source':'scsc','authorization':O0O00OOOO00OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0O00O000OO ),'signstring':OOOO00O0O00O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:205
        OOO0000O00OOOO000 =requests .request ('get',f'{host}/assets',headers =OOO00OO00O000OO00 ).json ()#line:206
        if 'status'in OOO0000O00OOOO000 :#line:208
            if OOO0000O00OOOO000 ['status']==200 :#line:209
                O0O0OOO00OOOOO000 =OOO0000O00OOOO000 ['data']['cash']#line:210
                if float (O0O0OOO00OOOOO000 )>20 :#line:211
                    OOOO00O0O00O000OO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:212
                    OOO00OO00O000OO00 ={'authorization':O0O00OOOO00OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0O00O000OO ),'signstring':OOOO00O0O00O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:222
                    OO000O00O0O0OO0O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:223
                    OO0OOOOOOOO00OO00 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOO00OO00O000OO00 ,data =OO000O00O0O0OO0O0 ).json ()#line:225
                    print (OO0OOOOOOOO00OO00 )#line:226
    def invitenum (O0OO0O00000O0000O ):#line:229
        OOO00OO00O0OO0O0O =f'__{timi_new()}'#line:230
        O0OO000OO0OOO0OO0 ={'source':'scsc','authorization':O0OO0O00000O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO00O0OO0O0O ),'signstring':OOO00OO00O0OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:241
        O0OO00OO000OO000O =requests .request ('get',f'{host}/invite/invitenum',headers =O0OO000OO0OOO0OO0 ).json ()#line:242
        if 'status'in O0OO00OO000OO000O :#line:244
            if O0OO00OO000OO000O ['status']==200 :#line:245
                O0OO000000000OO0O =O0OO00OO000OO000O ['data']['invited_count']#line:246
                OO0O000OO0O0000O0 =O0OO00OO000OO000O ['data']['invited_second_count']#line:247
                print (f'【我的邀请】:直邀好友:{O0OO000000000OO0O}丨间邀好友:{OO0O000OO0O0000O0}')#line:248
    def game_map (OO0OOO00OO0000OOO ):#line:251
        try :#line:252
            O0O0OOO0OO0OOOOO0 =f'__{timi_new()}'#line:253
            OOOO0OO0O0OO00O0O ={'source':'scsc','authorization':OO0OOO00OO0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO0OO0OOOOO0 ),'signstring':O0O0OOO0OO0OOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:264
            O00O000OOOOOO0O0O =requests .request ('get',f'{host}/game/map',headers =OOOO0OO0O0OO00O0O ).json ()#line:265
            if 'status'in O00O000OOOOOO0O0O :#line:267
                if O00O000OOOOOO0O0O ['status']==200 :#line:268
                    for O0000OO0O00OO00OO in O00O000OOOOOO0O0O ['data']['list'][0 ]['crops']:#line:269
                        O0O0O0O0O0OOOOO00 =O0000OO0O00OO00OO ['level']#line:271
                        if O0O0O0O0O0OOOOO00 ==41 :#line:272
                            OOO0OO0O0000OOOOO =O0000OO0O00OO00OO ['crop_name']#line:273
                            OOO000OOO0OO0OOO0 =O0000OO0O00OO00OO ['count']#line:274
                            if OOO000OOO0OO0OOO0 >0 :#line:275
                                print (f'【农业资产】:{OOO0OO0O0000OOOOO}丨数量:{OOO000OOO0OO0OOO0}')#line:276
        except Exception as O0O0O0OO00O0O0OOO :#line:277
            print (O0O0O0OO00O0O0OOO )#line:278
    def give_gold (O0OOOO00OO0O0OO0O ):#line:281
        try :#line:282
            OOOO00O0O00O0O0OO =f'__{timi_new()}'#line:283
            O0O0O00OOOO0O0OOO ={'source':'scsc','authorization':O0OOOO00OO0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0O00O0O0OO ),'signstring':OOOO00O0O00O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:294
            O000OO0OO0O0O00O0 =requests .request ('get',f'{host}/user',headers =O0O0O00OOOO0O0OOO ).json ()#line:295
            if 'status'in O000OO0OO0O0O00O0 :#line:296
                if O000OO0OO0O0O00O0 ['status']==200 :#line:297
                    if float (O0OOOO00OO0O0OO0O .doneeNo )!=0 :#line:298
                        OO0OO0OOO0OOOO00O =O000OO0OO0O0O00O0 ['data']['assets']['gold']#line:299
                        if float (OO0OO0OOO0OOOO00O )>float (O0OOOO00OO0O0OO0O .innerId ):#line:300
                            O000000000OO0OOOO =int (float (OO0OO0OOO0OOOO00O )/1.1 )#line:301
                            OOOO00O0O00O0O0OO =f'_doneeNo={O0OOOO00OO0O0OO0O.doneeNo}&quantity={O000000000OO0OOOO}_{timi_new()}'#line:302
                            O0O0O00OOOO0O0OOO ={'source':'scsc','authorization':O0OOOO00OO0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0O00O0O0OO ),'signstring':OOOO00O0O00O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:313
                            O0OO0OO0O0OO00000 ={"quantity":O000000000OO0OOOO ,"doneeNo":O0OOOO00OO0O0OO0O .doneeNo }#line:317
                            OOOOO00O0OOO0O0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0O00OOOO0O0OOO ,data =O0OO0OO0O0OO00000 ).json ()#line:318
                            if 'status'in OOOOO00O0OOO0O0O0 :#line:320
                                if OOOOO00O0OOO0O0O0 ['status']==200 :#line:321
                                    if OOOOO00O0OOO0O0O0 ['data']:#line:322
                                        print (f'【赠送种子】:赠送{O000000000OO0OOOO}种子给{O0OOOO00OO0O0OO0O.doneeNo}成功')#line:323
                    else :#line:324
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:325
        except Exception as OO0000OOOO00O0O00 :#line:326
            print (OO0000OOOO00O0O00 )#line:327
    def invitation (OO0OOOOOO00OOO000 ):#line:329
        try :#line:330
            _OO0OOOO0000O0O000 =float (bundled_def ())/4 #line:331
            O0O0000O0OOO0O000 =f'_innerId={int(_OO0OOOO0000O0O000)}_{timi_new()}'#line:332
            O00O000OO0O0000O0 ={'source':'scsc','authorization':OO0OOOOOO00OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000O0OOO0O000 ),'signstring':O0O0000O0OOO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:343
            OO0O0000OO0O000OO ={"innerId":int (_OO0OOOO0000O0O000 )}#line:344
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00O000OO0O0000O0 ,data =OO0O0000OO0O000OO )#line:345
        except Exception as O00OOOOOOOOOO00OO :#line:346
            print (O00OOOOOOOOOO00OO )#line:347
    def winning_rewards (OOOOOO0O000O00O00 ):#line:350
        try :#line:351
            O00O0OO0O0O00O0OO =f'__{timi_new()}'#line:352
            O0O0O0000O00OOOO0 ={'source':'scsc','authorization':OOOOOO0O000O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO0O0O00O0OO ),'signstring':O00O0OO0O0O00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:363
            OOO0OOOOO000O0OOO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O0O0000O00OOOO0 ).json ()#line:364
            if 'status'in OOO0OOOOO000O0OOO :#line:366
                if OOO0OOOOO000O0OOO ['status']==200 :#line:367
                    if OOO0OOOOO000O0OOO ['data']['amount']:#line:368
                        O000OOO0O0OOOO000 =OOO0OOOOO000O0OOO ['data']['amount']['gold']#line:369
                        return O000OOO0O0OOOO000 #line:370
                    else :#line:371
                        return 0 #line:372
        except Exception as OO00O00O0OOO00O00 :#line:373
            print (OO00O00O0OOO00O00 )#line:374
    def certification (O00000O000000OOOO ):#line:377
        try :#line:378
            OOO0O00OOOOO00O00 =f'__{timi_new()}'#line:379
            O0000O00OOO0000O0 ={'source':'scsc','authorization':O00000O000000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00OOOOO00O00 ),'signstring':OOO0O00OOOOO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:390
            OOO00OO000OOO0O00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0000O00OOO0000O0 ).json ()#line:391
            if 'status'in OOO00OO000OOO0O00 :#line:393
                if OOO00OO000OOO0O00 ['status']==200 :#line:394
                    if OOO00OO000OOO0O00 ['data']['result']:#line:395
                        O0O0OOOOOOOOO0OO0 =OOO00OO000OOO0O00 ['data']['nick_name']#line:396
                        return O0O0OOOOOOOOO0OO0 #line:397
                    else :#line:398
                        return '未实名'#line:399
        except Exception as OOOO0OO000OO00O0O :#line:400
            print (OOOO0OO000OO00O0O )#line:401
    def crops_illustrated (OO00OO0O000OO0000 ):#line:404
        try :#line:405
            O0000OO00OOOO0O00 =f'__{timi_new()}'#line:406
            OO0O00O000OO00OOO ={'source':'scsc','authorization':OO00OO0O000OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO00OOOO0O00 ),'signstring':O0000OO00OOOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:417
            O0O0O0O0O00O00O0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O00O000OO00OOO ).json ()#line:418
            if 'status'in O0O0O0O0O00O00O0O :#line:420
                if O0O0O0O0O00O00O0O ['status']==200 :#line:421
                    O00OOO000000OOO00 =O0O0O0O0O00O00O0O ['data'][0 ]['crops']#line:422
                    for O0O0000OO0O0O0OO0 in O00OOO000000OOO00 :#line:423
                        if O0O0000OO0O0O0OO0 ['ill_clover_award']:#line:424
                            if float (O0O0000OO0O0O0OO0 ['ill_clover_award'])>1 :#line:425
                                if O0O0000OO0O0O0OO0 ['is_finish']:#line:426
                                    if not O0O0000OO0O0O0OO0 ['is_getit']:#line:427
                                        if OO00OO0O000OO0000 .certification ()!='未实名':#line:428
                                            O0000OO00OOOO0O00 =f'_award_level={O0O0000OO0O0O0OO0["level"]}_{timi_new()}'#line:429
                                            OO0O00O000OO00OOO ={'source':'scsc','authorization':OO00OO0O000OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO00OOOO0O00 ),'signstring':O0000OO00OOOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:440
                                            OOO0O0000000O0O0O ={"award_level":O0O0000OO0O0O0OO0 ['level']}#line:441
                                            OOOO0O0OOOOO000O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O00O000OO00OOO ,json =OOO0O0000000O0O0O ).json ()#line:443
                                            if 'status'in OOOO0O0OOOOO000O0 :#line:444
                                                if OOOO0O0OOOOO000O0 ['status']==200 :#line:445
                                                    OO0OOOO0O0OOOOOOO =OOOO0O0OOOOO000O0 ['data']['ill_clover_award']#line:446
                                                    print (f'【图鉴奖励】:领取{O0O0000OO0O0O0OO0["crop_name"]}成就丨奖励{OO0OOOO0O0OOOOOOO}☘️')#line:448
                                                if OOOO0O0OOOOO000O0 ['status']==500 :#line:449
                                                    print (f'【图鉴奖励】:{OOOO0O0OOOOO000O0["message"]}')#line:450
        except Exception as OO0000O0OOOO0O0O0 :#line:451
            print (OO0000O0OOOO0O0O0 )#line:452
    def watched_ad (OOO00OO0O0000OOOO ):#line:455
        try :#line:456
            OO0OO00OOO000OOOO =f'__{timi_new()}'#line:457
            OO0OOOOO0O00O0O00 ={'source':'scsc','authorization':OOO00OO0O0000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00OOO000OOOO ),'signstring':OO0OO00OOO000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:468
            O0OO0000OO00O0OOO =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOOOO0O00O0O00 ).json ()#line:469
            if 'status'in O0OO0000OO00O0OOO :#line:471
                if O0OO0000OO00O0OOO ['status']==200 :#line:472
                    if 'offlineInfo'in O0OO0000OO00O0OOO ['data']:#line:473
                        time .sleep (random .randint (3 ,5 ))#line:474
                        OO0O0O0O0OOOO0OO0 =O0OO0000OO00O0OOO ['data']['offlineInfo']['off_minute']#line:475
                        OOOOOO000OOO0O000 =float (O0OO0000OO00O0OOO ['data']['silver'])/1000000000000 #line:476
                        time .sleep (1 )#line:477
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0OOOOO0O00O0O00 ).json ()#line:478
                        time .sleep (2 )#line:479
                        O00O00O00OO0OO000 =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOOOO0O00O0O00 ).json ()#line:480
                        if 'status'in O00O00O00OO0OO000 :#line:482
                            if O00O00O00OO0OO000 ['status']==200 :#line:483
                                O0OOOOO000O0O0OOO =float (O00O00O00OO0OO000 ['data']['silver'])/1000000000000 #line:484
                                OO0OO00O0OOO00O0O =str (O0OOOOO000O0O0OOO -OOOOOO000OOO0O000 )[:6 ]#line:485
                                print (f'【离线奖励】:翻倍离线{OO0O0O0O0OOOO0OO0}分钟奖励🌱数量:{OO0OO00O0OOO00O0O}t粒')#line:486
        except Exception as O0OO000000O000O00 :#line:487
            print (O0OO000000O000O00 )#line:488
    def user_ad (O0OOO0OOO0O00O0OO ):#line:491
        try :#line:492
            OOOOO0OOOO00000OO =f'__{timi_new()}'#line:493
            O0O0OOO00O0000O0O ={'source':'scsc','authorization':O0OOO0OOO0O00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOOO00000OO ),'signstring':OOOOO0OOOO00000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:504
            OO0O0OOO0OO0OOO0O =requests .request ('get',f'{host}/user/ad',headers =O0O0OOO00O0000O0O ).json ()#line:505
            if 'status'in OO0O0OOO0OO0OOO0O :#line:507
                if OO0O0OOO0OO0OOO0O ['status']==200 :#line:508
                    OOOOOOO0O0000OOOO =OO0O0OOO0OO0OOO0O ['data']['max_time']#line:509
                    O0O0OO0OO000OO00O =OO0O0OOO0OO0OOO0O ['data']['watch_time']#line:510
                    O0000OOO0OOOO00OO =OO0O0OOO0OO0OOO0O ['data']['added_time']#line:511
                    print (f'【获取种子】:获取🌱剩余{O0000OOO0OOOO00OO + OOOOOOO0O0000OOOO - O0O0OO0OO000OO00O}次丨好友提供:{O0000OOO0OOOO00OO}次')#line:512
                    if O0000OOO0OOOO00OO +OOOOOOO0O0000OOOO -O0O0OO0OO000OO00O >0 :#line:513
                        time .sleep (random .randint (16 ,19 ))#line:514
                        OOO0O000OO0OOO0OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O0OOO00O0000O0O ).json ()#line:515
                        if 'status'in OOO0O000OO0OOO0OO :#line:517
                            if OOO0O000OO0OOO0OO ['status']==200 :#line:518
                                OO00OOOO00O000000 =float (OOO0O000OO0OOO0OO ['data']['silver'])/1000000000000 #line:519
                                print (f'【获取种子】:获得🌱:{int(OO00OOOO00O000000)}t粒')#line:520
                                return True #line:521
                            if OOO0O000OO0OOO0OO ['status']==500 :#line:522
                                OO00O0OOO0O00O0O0 =OOO0O000OO0OOO0OO ['message']#line:523
                                print (f'【获取种子】:{OO00O0OOO0O00O0O0}')#line:524
                                return False #line:525
        except Exception as OO0000OO0O00OOOO0 :#line:526
            print (OO0000OO0O00OOOO0 )#line:527
    def synthetic (O0O00O0OO00O000OO ):#line:530
        global id ,g #line:531
        try :#line:532
            OO000O000000OOOOO =O0O00O0OO00O000OO .level_new ()#line:533
            O00OO00O000O0O00O =random .randint (9 ,11 )#line:534
            O0OO00O0000OOO000 =f'_site=8&targetSite={O00OO00O000O0O00O}_{timi_new()}'#line:535
            O00O0OOO000O0O0O0 ={'source':'scsc','authorization':O0O00O0OO00O000OO .token ,'timestamp':timi_new (),'sign':sign (O0OO00O0000OOO000 ),'signstring':O0OO00O0000OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:546
            OOO00OO0O00O0O00O ={"site":int (8 ),"targetSite":int (O00OO00O000O0O00O )}#line:547
            requests .request ('post',f'{host}/game/crops/move',headers =O00O0OOO000O0O0O0 ,json =OOO00OO0O00O0O00O )#line:548
            while True :#line:549
                O0OO0O0OOOO0OOO00 =f'__{timi_new()}'#line:550
                O0OOO0OOO00O0OOO0 ={'source':'scsc','authorization':O0O00O0OO00O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0OOOO0OOO00 ),'signstring':O0OO0O0OOOO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:561
                OOO0O0O00OO0OOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0OOO00O0OOO0 ).json ()#line:562
                if 'status'in OOO0O0O00OO0OOOO0 :#line:564
                    if OOO0O0O00OO0OOOO0 ['status']==200 :#line:565
                        O0OO00OOO0000O0O0 =OOO0O0O00OO0OOOO0 ['data']['cropList']#line:566
                        OOO0OO00OOOOOOO00 =OOO0O0O00OO0OOOO0 ['data']['gameCoreDataDBid']#line:567
                        OOO0O0OOO0O00O00O =float (OOO0O0O00OO0OOOO0 ['data']['silver'])/1000000000000 #line:568
                        OO0OOO00OO0O00O0O =0 #line:573
                        for OO0OO0O0OOOO0OO0O in O0OO00OOO0000O0O0 :#line:574
                            if not OO0OO0O0OOOO0OO0O :#line:575
                                O0O000O00OOOO0O00 =f'_crop_id={OOO0OO00OOOOOOO00}&site={OO0OOO00OO0O00O0O}_{O0O00O0OO00O000OO.time}'#line:576
                                O0OOOOO00O00O000O ={'source':'scsc','authorization':O0O00O0OO00O000OO .token ,'timestamp':O0O00O0OO00O000OO .time ,'sign':sign (O0O000O00OOOO0O00 ),'signstring':O0O000O00OOOO0O00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:586
                                OO000OOOO000000OO ={"site":OO0OOO00OO0O00O0O ,"crop_id":OOO0OO00OOOOOOO00 }#line:587
                                O0O0OOO0O00OOOOOO =requests .request ('post',f'{host}/game/crops/buy',headers =O0OOOOO00O00O000O ,data =OO000OOOO000000OO ).json ()#line:588
                                time .sleep (random .randint (1 ,3 )/10 )#line:590
                                if 'status'in O0O0OOO0O00OOOOOO :#line:591
                                    if O0O0OOO0O00OOOOOO ['status']==200 :#line:592
                                        if O0O0OOO0O00OOOOOO ['message']=='种子数量不足':#line:593
                                            OO000O000000OOOOO =O0O00O0OO00O000OO .level_new ()#line:594
                                            print (f'【种植合成】:{O0O0OOO0O00OOOOOO["message"]}')#line:595
                                            if not O0O00O0OO00O000OO .user_ad ():#line:596
                                                return False #line:597
                                    if O0O0OOO0O00OOOOOO ['status']==500 :#line:598
                                        print (f'【种植合成】:{O0O0OOO0O00OOOOOO["message"]}')#line:599
                                        return False #line:600
                            OO0OOO00OO0O00O0O +=1 #line:601
                        O0OO00000OOOOOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0OOO00O0OOO0 ).json ()#line:602
                        OOO0000OOOOOO00OO =O0OO00000OOOOOOO0 ['data']['cropList']#line:603
                        O00OOOO000O00O0O0 =False #line:604
                        for OO0OO0O0OOOO0OO0O in range (12 ):#line:605
                            id =OOO0000OOOOOO00OO [OO0OO0O0OOOO0OO0O ]['level']#line:606
                            if float (OO000O000000OOOOO )-float (id )>9 :#line:607
                                O00O0O0O0OO00000O =f'_site={OO0OO0O0OOOO0OO0O}_{timi_new()}'#line:608
                                OO00OO0OO00OOO00O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00O0OO00O000OO .token ,'timestamp':timi_new (),'sign':sign (O00O0O0O0OO00000O ),'signstring':O00O0O0O0OO00000O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:619
                                OO0OO00O00OOO0OOO ={"site":OO0OO0O0OOOO0OO0O }#line:620
                                O00O00OOOOO000OO0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO00OO0OO00OOO00O ,data =OO0OO00O00OOO0OOO ).json ()#line:622
                                if 'status'in O00O00OOOOO000OO0 :#line:623
                                    if O00O00OOOOO000OO0 ['status']==200 :#line:624
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:625
                            if id !=0 :#line:626
                                for OO00O0O0O00000O00 in range (11 ):#line:627
                                    OOO0OO0O0O000O000 =OO00O0O0O00000O00 +1 #line:628
                                    g =OOO0000OOOOOO00OO [OOO0OO0O0O000O000 ]['level']#line:629
                                    if id ==g :#line:630
                                        OO0000OOO0O00O000 =OO00O0O0O00000O00 +2 #line:631
                                        if OO0000OOO0O00O000 !=OO0OO0O0OOOO0OO0O +1 :#line:632
                                            OOO0000OO0O0O00OO =OO0OO0O0OOOO0OO0O +1 #line:633
                                            time .sleep (random .randint (1 ,3 )/10 )#line:635
                                            O0OO00O0000OOO000 =f'_site={OOO0000OO0O0O00OO - 1}&targetSite={OO0000OOO0O00O000 - 1}_{timi_new()}'#line:636
                                            O00O0OOO000O0O0O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00O0OO00O000OO .token ,'timestamp':timi_new (),'sign':sign (O0OO00O0000OOO000 ),'signstring':O0OO00O0000OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:653
                                            O0O0O00OOOOO00OO0 ={"site":int (OOO0000OO0O0O00OO -1 ),"targetSite":int (OO0000OOO0O00O000 -1 )}#line:654
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00O0OOO000O0O0O0 ,json =O0O0O00OOOOO00OO0 )#line:655
                                            O00OOOO000O00O0O0 =True #line:657
                                    if O00OOOO000O00O0O0 :#line:658
                                        break #line:659
                                if O00OOOO000O00O0O0 :#line:660
                                    break #line:661
        except :#line:662
            O0O00O0OO00O000OO .synthetic ()#line:663
    def level_new (OO00O00000000OO00 ):#line:666
        try :#line:667
            OOOOOOOO0O000O00O =f'__{timi_new()}'#line:668
            O0O00O00OOO000000 ={'source':'scsc','authorization':OO00O00000000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO0O000O00O ),'signstring':OOOOOOOO0O000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:679
            O000O000O0OO00000 =requests .request ('get',f'{host}/user',headers =O0O00O00OOO000000 ).json ()#line:680
            if 'status'in O000O000O0OO00000 :#line:681
                if O000O000O0OO00000 ['status']==200 :#line:682
                    return float (O000O000O0OO00000 ['data']['level'])#line:683
        except Exception as OOOO000O0O0OOOO0O :#line:684
            print (OOOO000O0O0OOOO0O )#line:685
    def propsraffle (OO0O0OO00O0O00O00 ):#line:688
        try :#line:689
            while True :#line:690
                O00000O00OOOOOO00 =f'__{timi_new()}'#line:691
                OOOOOOOOOOO0O0OO0 ={'source':'scsc','authorization':OO0O0OO00O0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O00OOOOOO00 ),'signstring':O00000O00OOOOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:702
                OO0O0OOO0OOO0O0OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOOOOOOOOO0O0OO0 ).json ()#line:703
                if 'status'in OO0O0OOO0OOO0O0OO :#line:705
                    if OO0O0OOO0OOO0O0OO ['status']==200 :#line:706
                        OOOOOOOO0OO00O000 =OO0O0OOO0OOO0O0OO ['data']['rows']#line:707
                        O00000000O00O0OOO =OO0O0OOO0OOO0O0OO ['data']['vstate']#line:708
                        if OOOOOOOO0OO00O000 ==5 or OOOOOOOO0OO00O000 ==6 or OOOOOOOO0OO00O000 ==7 :#line:709
                            O00O0OO0O00OOO00O =OO0O0OOO0OOO0O0OO ['data']['silver']#line:710
                            print (f'【转盘抽奖】:获得种子:{O00O0OO0O00OOO00O}')#line:711
                        if OOOOOOOO0OO00O000 ==1 or OOOOOOOO0OO00O000 ==2 or OOOOOOOO0OO00O000 ==3 :#line:712
                            OOO000OOOO0OO00OO =OO0O0OOO0OOO0O0OO ['data']['clover']#line:713
                            print (f'【转盘抽奖】:获得三叶草:{OOO000OOOO0OO00OO}')#line:714
                        if OOOOOOOO0OO00O000 ==4 or OOOOOOOO0OO00O000 ==8 :#line:715
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:716
                        if OOOOOOOO0OO00O000 =='抽奖次数已用完':#line:720
                            break #line:754
                time .sleep (random .randint (8 ,15 )/10 )#line:755
        except Exception as OOOOOOOOOOO0O0000 :#line:756
            print (OOOOOOOOOOO0O0000 )#line:757
    def friends_invitation (O0O0OOO000O0O0O00 ):#line:760
        try :#line:761
            O00OOOO0O0O000OO0 =f'__{timi_new()}'#line:762
            O0O0O0O0OOO00OOOO ={'source':'scsc','authorization':O0O0OOO000O0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0O0O000OO0 ),'signstring':O00OOOO0O0O000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:773
            OO0O0000O000OOO00 =requests .request ('get',f'{host}/friends',headers =O0O0O0O0OOO00OOOO ).json ()#line:774
            if 'status'in OO0O0000O000OOO00 :#line:775
                if OO0O0000O000OOO00 ['status']==200 :#line:776
                    O0OOOOO0OO00000OO =OO0O0000O000OOO00 ['data']['myInviteter']#line:777
                    if O0OOOOO0OO00000OO :#line:778
                        OOO00O0O0OO0O00OO =O0OOOOO0OO00000OO ['user']['nickname']#line:779
                        O00000OOO0OOOO0OO =O0O0OOO000O0O0O00 .certification ()#line:780
                        print (f'【查邀请人】:我的邀请人:{OOO00O0O0OO0O00OO}丨实名:{O00000OOO0OOOO0OO}')#line:781
                    else :#line:782
                        if O0O0OOO000O0O0O00 .innerId !='0':#line:783
                            O0O0OOO000O0O0O00 .invitation ()#line:784
        except Exception as OOOOOOOOOOOOO0O00 :#line:785
            print (OOOOOOOOOOOOO0O00 )#line:786
    def add_clover (OOO00OOOOO0OO0000 ):#line:789
        global golden_seed #line:790
        try :#line:791
            O00000O00OOOO00OO =f'__{timi_new()}'#line:792
            O0000O0OOOOOOOOOO ={'source':'scsc','authorization':OOO00OOOOO0OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O00OOOO00OO ),'signstring':O00000O00OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:803
            OOO00OO00O0OO0OO0 =requests .request ('get',f'{host}/assets/clovers',headers =O0000O0OOOOOOOOOO ).json ()#line:804
            if 'status'in OOO00OO00O0OO0OO0 :#line:806
                if OOO00OO00O0OO0OO0 ['status']==200 :#line:807
                    OO00OO00O0000O000 =OOO00OO00O0OO0OO0 ['data']['clover']#line:808
                    O0OO00OOO00000OOO =OOO00OO00O0OO0OO0 ['data']['used_clover']#line:809
                    OOO0OO000OOO0O00O =float (OO00OO00O0000O000 )-float (O0OO00OOO00000OOO )#line:810
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OO00OOO00000OOO}')#line:811
                    if OOO00OOOOO0OO0000 .certification ()!='未实名':#line:812
                        if OOO0OO000OOO0O00O >1 :#line:813
                            O00000O00OOOO00OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO0OO000OOO0O00O)}_{timi_new()}'#line:814
                            OOOOOOOOO00OO0OO0 ={'source':'scsc','authorization':OOO00OOOOO0OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O00OOOO00OO ),'signstring':O00000O00OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:825
                            OO00000000OOOO00O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO0OO000OOO0O00O )}#line:826
                            OO0O00OOO0OO000OO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOOOOOOO00OO0OO0 ,data =OO00000000OOOO00O ).json ()#line:827
                            if 'status'in OO0O00OOO0OO000OO :#line:829
                                if OO0O00OOO0OO000OO ['status']==200 :#line:830
                                    print (f'【参与抽奖】:添加☘️:{OO0O00OOO0OO000OO["data"]}丨数量:{OOO0OO000OOO0O00O}')#line:831
                                if OO0O00OOO0OO000OO ['status']==500 :#line:832
                                    print (f'【参与抽奖】:添加☘️:{OO0O00OOO0OO000OO["message"]}')#line:833
            OOOO0O00OOOO00000 =requests .request ('get',f'{host}/lottery',headers =O0000O0OOOOOOOOOO ).json ()#line:834
            O0O00O00O00OOO0OO =OOO00OOOOO0OO0000 .winning_rewards ()#line:836
            if 'status'in OOOO0O00OOOO00000 :#line:837
                if OOOO0O00OOOO00000 ['status']==200 :#line:838
                    OO0O00O0O0OO00000 =OOOO0O00OOOO00000 ['data'][0 ]['day_get_gold_quantity']#line:839
                    golden_seed +=float (OO0O00O0O0OO00000 )#line:840
                    O0OOO0O0O0O0OOO00 =OOOO0O00OOOO00000 ['data'][1 ]['value']#line:841
                    OO0O0O0OO000O0OO0 =OOOO0O00OOOO00000 ['data'][0 ]['join_number']#line:842
                    OOO0O00O000OOOOOO =int (float (OOOO0O00OOOO00000 ['data'][0 ]['totalValue']))#line:843
                    OO00000OOOO00OOOO =float (O0OOO0O0O0O0OOO00 /OOO0O00O000OOOOOO )*10000 #line:844
                    O00O00OOOO00O0OOO =OOO0O00O000OOOOOO /OO0O0O0OO000O0OO0 #line:845
                    print (f'【参与抽奖】:预计每天中{str(OO0O00O0O0OO00000)[:6]}颗金种子丨好友收益:{str(O0O00O00O00OOO0OO)[:6]}')#line:846
                    print (f'【抽奖统计】:每1万☘️中{str(OO00000OOOO00OOOO)[:6]}颗金种子丨☘️人均:{str(O00O00OOOO00O0OOO)[:7]}️')#line:847
        except Exception as OO00O0OO00OO00OO0 :#line:848
            print (OO00O0OO00OO00OO0 )#line:849
    def energy (OOO000000OO00O000 ):#line:853
        try :#line:854
            while True :#line:855
                O0O00O00OO0OO00O0 =f'__{timi_new()}'#line:856
                O0O0OOOO0O000O0OO ={'source':'scsc','authorization':OOO000000OO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00OO0OO00O0 ),'signstring':O0O00O00OO0OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:867
                OO0O0O000O00O00OO =requests .request ('get',f'{host}/energy/general',headers =O0O0OOOO0O000O0OO ).json ()#line:868
                if 'status'in OO0O0O000O00O00OO :#line:870
                    if OO0O0O000O00O00OO ['status']==200 :#line:871
                        O00O0000O000OOO00 =OO0O0O000O00O00OO ['data']['ordinary_water']#line:872
                        O000000OOOOO0OO0O =OO0O0O000O00O00OO ['data']['ordinary_fertilizer']#line:873
                        OO00O000O0OOOOOOO =OO0O0O000O00O00OO ['data']['videoStatus']#line:874
                        O0000O0OO0000O000 =OO0O0O000O00O00OO ['data']['waterVideoKey']#line:875
                        print (f'【我的营养】:肥料:{str(O000000OOOOO0OO0O).split(".")[0]}丨水滴:{str(O00O0000O000OOO00).split(".")[0]}')#line:876
                        if float (O000000OOOOO0OO0O )<96 :#line:877
                            if OO00O000O0OOOOOOO :#line:878
                                time .sleep (random .randint (160 ,180 )/10 )#line:879
                                OOO0O00O0O00O0OOO =99 -float (O000000OOOOO0OO0O )#line:880
                                O00O0O00O00O0O00O ={"fertilizer":str (OOO0O00O0O00O0OOO ).split ('.')[0 ]}#line:881
                                O000000O0O0O00OOO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0O0OOOO0O000O0OO ).json ()#line:882
                                if 'status'in O000000O0O0O00OOO :#line:884
                                    if O000000O0O0O00OOO ['status']==200 :#line:885
                                        print (f'【购买肥料】:看广告获取肥料:{O000000O0O0O00OOO["message"]}')#line:886
                                    if O000000O0O0O00OOO ['status']==500 :#line:887
                                        print (f'【购买肥料】:看广告获取肥料:{O000000O0O0O00OOO["message"]}')#line:888
                                        break #line:889
                            if energy :#line:890
                                if float (O000000OOOOO0OO0O )<78 :#line:891
                                    OOO0O00O0O00O0OOO =80 -float (O000000OOOOO0OO0O )#line:892
                                    O000O0O0O00O0O000 =f'_fertilizer={int(OOO0O00O0O00O0OOO)}_{timi_new()}'#line:893
                                    O0000O0OO0OO0O0O0 ={'source':'scsc','authorization':OOO000000OO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O0O00O0O000 ),'signstring':O000O0O0O00O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:904
                                    OO00O0OOO000OOOOO ={"fertilizer":int (OOO0O00O0O00O0OOO )}#line:905
                                    O0O0OOOO0OO0OO000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0000O0OO0OO0O0O0 ,data =OO00O0OOO000OOOOO ).json ()#line:906
                                    if 'status'in O0O0OOOO0OO0OO000 :#line:908
                                        if O0O0OOOO0OO0OO000 ['status']==200 :#line:909
                                            print (f'【购买肥料】:购买肥料:{O0O0OOOO0OO0OO000["message"]}丨数量:{int(OOO0O00O0O00O0OOO)}')#line:910
                                        if O0O0OOOO0OO0OO000 ['status']==500 :#line:911
                                            print (f'【购买肥料】:购买肥料:{O0O0OOOO0OO0OO000["message"]}丨数量:{int(OOO0O00O0O00O0OOO)}')#line:912
                                            OOO000OOO00OO000O =O0O0OOOO0OO0OO000 ["message"].split ('-')[1 ]#line:913
                                            O0O0000OO0OO0000O =f'__{timi_new()}'#line:914
                                            OOO0OOO00O0O0O000 ={'source':'scsc','authorization':OOO000000OO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OO0OO0000O ),'signstring':O0O0000OO0OO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:925
                                            OO0O0O0OOOOOO000O =requests .request ('get',f'{host}/user',headers =OOO0OOO00O0O0O000 ).json ()#line:926
                                            if 'status'in OO0O0O0OOOOOO000O :#line:927
                                                if OO0O0O0OOOOOO000O ['status']==200 :#line:928
                                                    OO00O00OOO0O0OO00 =OO0O0O0OOOOOO000O ['data']['inner_id']#line:929
                                                    if give_gold (OO00O00OOO0O0OO00 ,float (OOO000OOO00OO000O )+1 ):#line:930
                                                        OOO000000OO00O000 .energy ()#line:931
                        if float (O00O0000O000OOO00 )<880 :#line:932
                            if O0000O0OO0000O000 :#line:933
                                time .sleep (random .randint (160 ,180 )/10 )#line:934
                                O0000OOOOOOOOOOO0 =999 -float (O00O0000O000OOO00 )#line:935
                                OO00O0O000O0O000O ={"water":str (O0000OOOOOOOOOOO0 ).split ('.')[0 ]}#line:936
                                OOOOO00000OOO0O00 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0O0OOOO0O000O0OO ).json ()#line:937
                                if 'status'in OOOOO00000OOO0O00 :#line:939
                                    if OOOOO00000OOO0O00 ['status']==200 :#line:940
                                        print (f'【购买水滴】:看广告获取水滴:{OOOOO00000OOO0O00["message"]}')#line:941
                                    if OOOOO00000OOO0O00 ['status']==500 :#line:942
                                        print (f'【购买水滴】:看广告获取水滴:{OOOOO00000OOO0O00["message"]}')#line:943
                                        break #line:944
                            if energy :#line:945
                                if float (O00O0000O000OOO00 )<780 :#line:946
                                    O0000OOOOOOOOOOO0 =800 -float (O00O0000O000OOO00 )#line:947
                                    O00O00OO000OO0000 =f'_water={int(O0000OOOOOOOOOOO0)}_{timi_new()}'#line:948
                                    O0OOO0OO0000OO0O0 ={'source':'scsc','authorization':OOO000000OO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO000OO0000 ),'signstring':O00O00OO000OO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:959
                                    O000OO0OOOO00OO00 ={"water":int (O0000OOOOOOOOOOO0 )}#line:960
                                    O0O00000OOOO0OOOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0OOO0OO0000OO0O0 ,data =O000OO0OOOO00OO00 ).json ()#line:962
                                    if 'status'in O0O00000OOOO0OOOO :#line:964
                                        if O0O00000OOOO0OOOO ['status']==200 :#line:965
                                            print (f'【购买水滴】:购买水滴:{O0O00000OOOO0OOOO["message"]}丨数量:{int(O0000OOOOOOOOOOO0)}')#line:966
                                        if O0O00000OOOO0OOOO ['status']==500 :#line:967
                                            print (f'【购买水滴】:购买水滴:{O0O00000OOOO0OOOO["message"]}丨数量:{int(O0000OOOOOOOOOOO0)}')#line:968
                                            OOO000OOO00OO000O =O0O00000OOOO0OOOO ["message"].split ('-')[1 ]#line:969
                                            O0O0000OO0OO0000O =f'__{timi_new()}'#line:970
                                            OOO0OOO00O0O0O000 ={'source':'scsc','authorization':OOO000000OO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OO0OO0000O ),'signstring':O0O0000OO0OO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:981
                                            OO0O0O0OOOOOO000O =requests .request ('get',f'{host}/user',headers =OOO0OOO00O0O0O000 ).json ()#line:982
                                            if 'status'in OO0O0O0OOOOOO000O :#line:983
                                                if OO0O0O0OOOOOO000O ['status']==200 :#line:984
                                                    OO00O00OOO0O0OO00 =OO0O0O0OOOOOO000O ['data']['inner_id']#line:985
                                                    if give_gold (OO00O00OOO0O0OO00 ,float (OOO000OOO00OO000O )+1 ):#line:986
                                                        OOO000000OO00O000 .energy ()#line:987
                        break #line:988
        except Exception as O000O0O0O0OOOOO00 :#line:990
            print (O000O0O0O0OOOOO00 )#line:991
def bundled_def ():#line:993
    O0OOOO00O0OO0O00O =['5570536','7750212','7911652','7911680','7805624']#line:994
    return O0OOOO00O0OO0O00O [random .randint (0 ,len (O0OOOO00O0OO0O00O )-1 )]#line:995
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
        O0000OO0OO00O0O00 =gitee_validation ()#line:1015
        if version_of_the_validation ()<O0000OO0OO00O0O00 ['CityEarth']['edition']:#line:1016
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0000OO0OO00O0O00["CityEarth"]["edition"]}   ❌')#line:1017
            print (f'更新内容=>>{O0000OO0OO00O0O00["CityEarth"]["content"]}   🎉')#line:1018
        else :#line:1019
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0000OO0OO00O0O00["CityEarth"]["edition"]}   ✅')#line:1020
            print (f'更新内容=>> {O0000OO0OO00O0O00["CityEarth"]["content"]}   🎉')#line:1021
    except Exception as O0OO000O000OO0O00 :#line:1022
        print (O0OO000O000OO0O00 )#line:1023
def sc3 ():#line:1025
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1026
def os_qinglong ():#line:1028
    if application in os .environ :#line:1029
        OO0000OOOO0OOOO0O =os .environ [application ].split ('\n')#line:1030
        if len (OO0000OOOO0OOOO0O )>0 :#line:1031
            return OO0000OOOO0OOOO0O #line:1032
        else :#line:1033
            print (f"{application}变量未启用")#line:1034
            print ('脚本退出')#line:1035
            sys .exit (1 )#line:1036
    else :#line:1037
        if token :#line:1038
            OO0000OOOO0OOOO0O =token .split ('\n')#line:1039
            if len (OO0000OOOO0OOOO0O )>0 :#line:1040
                return OO0000OOOO0OOOO0O #line:1041
        else :#line:1042
            print (f"内置变量为空")#line:1043
            print ('脚本结束')#line:1044
            sys .exit (0 )#line:1045
if __name__ =='__main__':#line:1050
    start ()#line:1051
