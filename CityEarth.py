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
token = 'f6502cb2-73a7-456b-a1aa-12ecb65c3c26&5000&1951406'

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
        O000OO0O0O0O00OO0 =os_qinglong ()#line:10
        print (f"==========共找到{len(O000OO0O0O0O00OO0)}个账号==========")#line:11
        for OOOO0O0OO0OO000OO in O000OO0O0O0O00OO0 :#line:12
            OOO00OOO00OO000OO =[]#line:13
            print (f"------------正在执行第{O000OO0O0O0O00OO0.index(OOOO0O0OO0OO000OO) + 1}个账号------------")#line:14
            OO0O000OOOOOO0O0O =CityEarth (OOOO0O0OO0OO000OO ,OOO00OOO00OO000OO )#line:15
            def O0O0OOOOO0OO0OOOO ():#line:17
                if OO0O000OOOOOO0O0O .base_info ():#line:19
                    OO0O000OOOOOO0O0O .sealing ()#line:21
                    OO0O000OOOOOO0O0O .invitenum ()#line:23
                    OO0O000OOOOOO0O0O .game_map ()#line:25
                    OO0O000OOOOOO0O0O .friends_invitation ()#line:27
                    OO0O000OOOOOO0O0O .energy ()#line:29
                    OO0O000OOOOOO0O0O .add_clover ()#line:31
                    OO0O000OOOOOO0O0O .propsraffle ()#line:33
                    OO0O000OOOOOO0O0O .synthetic ()#line:35
                    OO0O000OOOOOO0O0O .crops_illustrated ()#line:37
                    OO0O000OOOOOO0O0O .give_gold ()#line:39
                    OO0O000OOOOOO0O0O .withdraw ()#line:41
            OOOO0OOO0O00O0O00 =threading .Thread (target =O0O0OOOOO0OO0OOOO )#line:43
            OOOO0OOO0O00O0O00 .start ()#line:44
            time .sleep (time_xx )#line:45
        print (f"------------正在处理推送通知------------")#line:46
        time .sleep (0.5 )#line:47
        OOOO0O00OO00O00OO =format_msg ()#line:48
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOOO0O00OO00O00OO +' ')#line:49
    except Exception as OOOOOOO0OO00OOOOO :#line:50
        print (OOOOOOO0OO00OOOOO )#line:51
def give_gold (OO00OOOOOO00O000O ,OO0O00O00O0000OOO ):#line:54
        try :#line:55
            O00O0000OOO000O00 =f'_doneeNo={OO00OOOOOO00O000O}&quantity={int(OO0O00O00O0000OOO)}_{timi_new()}'#line:56
            O0O0OOOO000O00000 ={'source':'scsc','authorization':os_qinglong ()[0 ].split ('&')[0 ],'timestamp':str (timi_new ()),'sign':sign (O00O0000OOO000O00 ),'signstring':O00O0000OOO000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:67
            O0O00000O00O00OO0 ={"quantity":int (OO0O00O00O0000OOO ),"doneeNo":OO00OOOOOO00O000O }#line:71
            O0OOO0O0O000O0O0O =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0OOOO000O00000 ,data =O0O00000O00O00OO0 ).json ()#line:72
            if 'status'in O0OOO0O0O000O0O0O :#line:74
                if O0OOO0O0O000O0O0O ['status']==200 :#line:75
                    if O0OOO0O0O000O0O0O ['data']:#line:76
                        print (f'【赠送种子】:赠送{int(OO0O00O00O0000OOO)}种子给{OO00OOOOOO00O000O}成功')#line:77
                        return True #line:78
                if O0OOO0O0O000O0O0O ['status']==401 :#line:79
                    print (f'【赠送种子】:{O0OOO0O0O000O0O0O["message"]}')#line:80
                    return False #line:81
                if O0OOO0O0O000O0O0O ['status']==500 :#line:82
                    print (f'【赠送种子】:{O0OOO0O0O000O0O0O["message"]}')#line:83
                    return False #line:84
            return False #line:85
        except Exception as OO00OOO0000000OOO :#line:86
            print (OO00OOO0000000OOO )#line:87
def sign (OOOO000O0000O0O00 ):#line:90
    O0O0OOOO0O0OOOO00 =hashlib .md5 (OOOO000O0000O0O00 .encode ()).hexdigest ()#line:91
    O000OO00O00OO000O =sc1 ()#line:92
    OOOOO0O00O000OOOO =sc2 ()#line:93
    OO000OOOO00OOOOOO =sc3 ()#line:94
    O0O00OOO0OOO00000 =O000OO00O00OO000O +O0O0OOOO0O0OOOO00 +OOOOO0O00O000OOOO +OO000OOOO00OOOOOO #line:95
    O0OO000OOOO0OO000 =hashlib .md5 (O0O00OOO0OOO00000 .encode ()).hexdigest ()#line:96
    return O0OO000OOOO0OO000 #line:97
def format_msg ():#line:101
    O0OO000OO00O0O0O0 =""#line:102
    for OOO00O0OO00O0O000 in msg_list :#line:103
        O0OO000OO00O0O0O0 +=str (OOO00O0OO00O0O000 )+"\r\n"#line:104
    return O0OO000OO00O0O0O0 #line:105
def sc1 ():#line:107
    return "scsc%^&*"#line:108
def timi_new ():#line:111
    return str (int (time .time ()*1000 ))#line:112
class CityEarth :#line:115
    def __init__ (OOOOO0OOOO0OOO000 ,O000O0O00O0OO0000 ,OOOO0OOOOO0O0O00O ):#line:117
        try :#line:118
            OOOOO0OOOO0OOO000 .msg =OOOO0OOOOO0O0O00O #line:119
            OOOOO0OOOO0OOO000 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:120
            OOOOO0OOOO0OOO000 .token =O000O0O00O0OO0000 .split ('&')[0 ]#line:121
            OOOOO0OOOO0OOO000 .innerId =O000O0O00O0OO0000 .split ('&')[1 ]#line:122
            OOOOO0OOOO0OOO000 .doneeNo =O000O0O00O0OO0000 .split ('&')[2 ]#line:123
        except :#line:124
            print ('变量格式错误')#line:125
    def base_info (O00O000O00000OOO0 ):#line:128
        try :#line:129
            O00O000O00000OOO0 .watched_ad ()#line:131
            O000O0O0O000OO0OO =f'__{timi_new()}'#line:132
            O000O0O0OO0OO0OOO ={'source':'scsc','authorization':O00O000O00000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O0O000OO0OO ),'signstring':O000O0O0O000OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:143
            O0OOOO00OO0OO000O =requests .request ('get',f'{host}/user',headers =O000O0O0OO0OO0OOO ).json ()#line:144
            if 'status'in O0OOOO00OO0OO000O :#line:146
                if O0OOOO00OO0OO000O ['status']==200 :#line:147
                    O00O000000OOO00O0 =O0OOOO00OO0OO000O ['data']['nickname']#line:148
                    O000OO00O0O00O00O =O0OOOO00OO0OO000O ['data']['inner_id']#line:149
                    O0O0O0O0O0OO0OO00 =O0OOOO00OO0OO000O ['data']['assets']['gold']#line:150
                    OO0000OOO000O0OO0 =O0OOOO00OO0OO000O ['data']['level']#line:151
                    print (f'【账号信息】:昵称:{O00O000000OOO00O0[:5]}丨ID:{O000OO00O0O00O00O}丨等级:{OO0000OOO000O0OO0}丨金种子:{str(O0O0O0O0O0OO0OO00).split(".")[0]}')#line:152
                if O0OOOO00OO0OO000O ['status']==401 :#line:153
                    print (O0OOOO00OO0OO000O ['message'])#line:154
                    O00O000O00000OOO0 .msg .append ('有账号失效了')#line:155
                    return False #line:156
                if O0OOOO00OO0OO000O ['status']==500 :#line:157
                    return False #line:158
            return True #line:159
        except Exception as O0000O00OO0OOOOOO :#line:160
            print (O0000O00OO0OOOOOO )#line:161
    def sealing (OOOO0OOO0000OOOO0 ):#line:164
        try :#line:165
            OOO0OO00OOO0OO00O =f'__{timi_new()}'#line:166
            OO0O0O000000OO0OO ={'source':'scsc','authorization':OOOO0OOO0000OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00OOO0OO00O ),'signstring':OOO0OO00OOO0OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:177
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0O0O000000OO0OO )#line:178
            requests .request ('get',f'{host}/packsack/list',headers =OO0O0O000000OO0OO )#line:179
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0O0O000000OO0OO )#line:180
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0O0O000000OO0OO )#line:181
            requests .request ('get',f'{host}/user',headers =OO0O0O000000OO0OO )#line:182
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0O0O000000OO0OO )#line:183
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0O0O000000OO0OO )#line:184
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0O0O000000OO0OO )#line:185
            requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O000000OO0OO )#line:186
            requests .request ('get',f'{host}/assets',headers =OO0O0O000000OO0OO )#line:187
        except Exception as O000OO000OO0O00OO :#line:188
            print (O000OO000OO0O00OO )#line:189
    def withdraw (OO00O0O00OO0OO000 ):#line:193
        OOO0OOOOOOO000O00 =f'__{timi_new()}'#line:194
        OOO0OO000OO00O0O0 ={'source':'scsc','authorization':OO00O0O00OO0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOOOO000O00 ),'signstring':OOO0OOOOOOO000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:205
        O000O0O0000OO0OOO =requests .request ('get',f'{host}/assets',headers =OOO0OO000OO00O0O0 ).json ()#line:206
        if 'status'in O000O0O0000OO0OOO :#line:208
            if O000O0O0000OO0OOO ['status']==200 :#line:209
                OO000OOOO0O0OO00O =O000O0O0000OO0OOO ['data']['cash']#line:210
                if float (OO000OOOO0O0OO00O )>20 :#line:211
                    OOO0OOOOOOO000O00 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:212
                    OOO0OO000OO00O0O0 ={'authorization':OO00O0O00OO0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOOOO000O00 ),'signstring':OOO0OOOOOOO000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:222
                    O0000OO0OO00000OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:223
                    OOO000OO00O0OOO0O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOO0OO000OO00O0O0 ,data =O0000OO0OO00000OO ).json ()#line:225
                    print (OOO000OO00O0OOO0O )#line:226
    def invitenum (O0O000OOOOOO00O0O ):#line:229
        O000O0OOO0O0000OO =f'__{timi_new()}'#line:230
        O0000O0O0OOO0OOOO ={'source':'scsc','authorization':O0O000OOOOOO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOO0O0000OO ),'signstring':O000O0OOO0O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:241
        OO000O0O0OOO0OOOO =requests .request ('get',f'{host}/invite/invitenum',headers =O0000O0O0OOO0OOOO ).json ()#line:242
        if 'status'in OO000O0O0OOO0OOOO :#line:244
            if OO000O0O0OOO0OOOO ['status']==200 :#line:245
                OOO00O0OO000OO00O =OO000O0O0OOO0OOOO ['data']['invited_count']#line:246
                O0O0O0O000OOO0OO0 =OO000O0O0OOO0OOOO ['data']['invited_second_count']#line:247
                print (f'【我的邀请】:直邀好友:{OOO00O0OO000OO00O}丨间邀好友:{O0O0O0O000OOO0OO0}')#line:248
    def game_map (OOO000OOO0OOOO000 ):#line:251
        try :#line:252
            OO00OO0OO0000O0O0 =f'__{timi_new()}'#line:253
            O0O000O00O0OO000O ={'source':'scsc','authorization':OOO000OOO0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OO0000O0O0 ),'signstring':OO00OO0OO0000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:264
            O0O0O0O0OO0OOOO00 =requests .request ('get',f'{host}/game/map',headers =O0O000O00O0OO000O ).json ()#line:265
            if 'status'in O0O0O0O0OO0OOOO00 :#line:267
                if O0O0O0O0OO0OOOO00 ['status']==200 :#line:268
                    for O000O0OOO000OOO00 in O0O0O0O0OO0OOOO00 ['data']['list'][0 ]['crops']:#line:269
                        OO0OOOO0OOO0O0000 =O000O0OOO000OOO00 ['level']#line:271
                        if OO0OOOO0OOO0O0000 ==41 :#line:272
                            OO00000OOO0000O0O =O000O0OOO000OOO00 ['crop_name']#line:273
                            O0O00OOO00000OO00 =O000O0OOO000OOO00 ['count']#line:274
                            if O0O00OOO00000OO00 >0 :#line:275
                                print (f'【农业资产】:{OO00000OOO0000O0O}丨数量:{O0O00OOO00000OO00}')#line:276
        except Exception as O00OOO00O000OOO0O :#line:277
            print (O00OOO00O000OOO0O )#line:278
    def give_gold (O000OOOOO0O0000O0 ):#line:281
        try :#line:282
            OOOOOO0O0O0000OO0 =f'__{timi_new()}'#line:283
            OOOOO00OO0OO0O0OO ={'source':'scsc','authorization':O000OOOOO0O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O0O0000OO0 ),'signstring':OOOOOO0O0O0000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:294
            OO0000O0O00OOOOOO =requests .request ('get',f'{host}/user',headers =OOOOO00OO0OO0O0OO ).json ()#line:295
            if 'status'in OO0000O0O00OOOOOO :#line:296
                if OO0000O0O00OOOOOO ['status']==200 :#line:297
                    if float (O000OOOOO0O0000O0 .doneeNo )!=0 :#line:298
                        O0O00000000000000 =OO0000O0O00OOOOOO ['data']['assets']['gold']#line:299
                        if float (O0O00000000000000 )>float (O000OOOOO0O0000O0 .innerId ):#line:300
                            O0O00000OOOOO0OOO =int (float (O0O00000000000000 )/1.1 )#line:301
                            OOOOOO0O0O0000OO0 =f'_doneeNo={O000OOOOO0O0000O0.doneeNo}&quantity={O0O00000OOOOO0OOO}_{timi_new()}'#line:302
                            OOOOO00OO0OO0O0OO ={'source':'scsc','authorization':O000OOOOO0O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O0O0000OO0 ),'signstring':OOOOOO0O0O0000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:313
                            O00000OOOO0O0OOOO ={"quantity":O0O00000OOOOO0OOO ,"doneeNo":O000OOOOO0O0000O0 .doneeNo }#line:317
                            O000O0O0O00O000O0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOO00OO0OO0O0OO ,data =O00000OOOO0O0OOOO ).json ()#line:318
                            if 'status'in O000O0O0O00O000O0 :#line:320
                                if O000O0O0O00O000O0 ['status']==200 :#line:321
                                    if O000O0O0O00O000O0 ['data']:#line:322
                                        print (f'【赠送种子】:赠送{O0O00000OOOOO0OOO}种子给{O000OOOOO0O0000O0.doneeNo}成功')#line:323
                    else :#line:324
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:325
        except Exception as O000000OO0000O0O0 :#line:326
            print (O000000OO0000O0O0 )#line:327
    def invitation (OO0O0OO0O00OOOO0O ):#line:329
        try :#line:330
            _OOOOOO0OO0000O0O0 =float (bundled_def ())/4 #line:331
            O0OO000O0O0OOOOOO =f'_innerId={int(_OOOOOO0OO0000O0O0)}_{timi_new()}'#line:332
            O000O0000O0O0OO00 ={'source':'scsc','authorization':OO0O0OO0O00OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O0O0OOOOOO ),'signstring':O0OO000O0O0OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:343
            O0O0OO000OO000O0O ={"innerId":int (_OOOOOO0OO0000O0O0 )}#line:344
            requests .request ('post',f'{host}/friends/my-invitation',headers =O000O0000O0O0OO00 ,data =O0O0OO000OO000O0O )#line:345
        except Exception as O0OOOO0OOO00OOOO0 :#line:346
            print (O0OOOO0OOO00OOOO0 )#line:347
    def winning_rewards (O0O0O0OO00O0OO00O ):#line:350
        try :#line:351
            O0OOO00OOOO0O00OO =f'__{timi_new()}'#line:352
            OOOO00O0OOO0000O0 ={'source':'scsc','authorization':O0O0O0OO00O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OOOO0O00OO ),'signstring':O0OOO00OOOO0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:363
            OO00OO0O0OO00000O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOOO00O0OOO0000O0 ).json ()#line:364
            if 'status'in OO00OO0O0OO00000O :#line:366
                if OO00OO0O0OO00000O ['status']==200 :#line:367
                    if OO00OO0O0OO00000O ['data']['amount']:#line:368
                        O0O000O00OOO0OOO0 =OO00OO0O0OO00000O ['data']['amount']['gold']#line:369
                        return O0O000O00OOO0OOO0 #line:370
                    else :#line:371
                        return 0 #line:372
        except Exception as OO00OOOO00OOOOOOO :#line:373
            print (OO00OOOO00OOOOOOO )#line:374
    def certification (OO0O00000OOO0O00O ):#line:377
        try :#line:378
            OOOO0O0OOOOOO0OOO =f'__{timi_new()}'#line:379
            O0OO0OO000O0O0O00 ={'source':'scsc','authorization':OO0O00000OOO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0OOOOOO0OOO ),'signstring':OOOO0O0OOOOOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:390
            OO0O0OOOO0000OO0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0OO0OO000O0O0O00 ).json ()#line:391
            if 'status'in OO0O0OOOO0000OO0O :#line:393
                if OO0O0OOOO0000OO0O ['status']==200 :#line:394
                    if OO0O0OOOO0000OO0O ['data']['result']:#line:395
                        OO0000OO00000OOO0 =OO0O0OOOO0000OO0O ['data']['nick_name']#line:396
                        return OO0000OO00000OOO0 #line:397
                    else :#line:398
                        return '未实名'#line:399
        except Exception as OO0OOO0OO0O00OO0O :#line:400
            print (OO0OOO0OO0O00OO0O )#line:401
    def crops_illustrated (O0OO0OO0O00000000 ):#line:404
        try :#line:405
            OO000OOO00O00OOO0 =f'__{timi_new()}'#line:406
            OO00000OOOOOO0000 ={'source':'scsc','authorization':O0OO0OO0O00000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOO00O00OOO0 ),'signstring':OO000OOO00O00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:417
            OOOO0OOO00O0O0000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO00000OOOOOO0000 ).json ()#line:418
            if 'status'in OOOO0OOO00O0O0000 :#line:420
                if OOOO0OOO00O0O0000 ['status']==200 :#line:421
                    OO0OOOOO0O0O0O0OO =OOOO0OOO00O0O0000 ['data'][0 ]['crops']#line:422
                    for OO0OOO000O0OO000O in OO0OOOOO0O0O0O0OO :#line:423
                        if OO0OOO000O0OO000O ['ill_clover_award']:#line:424
                            if float (OO0OOO000O0OO000O ['ill_clover_award'])>1 :#line:425
                                if OO0OOO000O0OO000O ['is_finish']:#line:426
                                    if not OO0OOO000O0OO000O ['is_getit']:#line:427
                                        if O0OO0OO0O00000000 .certification ()!='未实名':#line:428
                                            OO000OOO00O00OOO0 =f'_award_level={OO0OOO000O0OO000O["level"]}_{timi_new()}'#line:429
                                            OO00000OOOOOO0000 ={'source':'scsc','authorization':O0OO0OO0O00000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOO00O00OOO0 ),'signstring':OO000OOO00O00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:440
                                            O000O0O0OO0O0OOO0 ={"award_level":OO0OOO000O0OO000O ['level']}#line:441
                                            OOOOO0O0O0O000000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO00000OOOOOO0000 ,json =O000O0O0OO0O0OOO0 ).json ()#line:443
                                            if 'status'in OOOOO0O0O0O000000 :#line:444
                                                if OOOOO0O0O0O000000 ['status']==200 :#line:445
                                                    O00000O0O000000OO =OOOOO0O0O0O000000 ['data']['ill_clover_award']#line:446
                                                    print (f'【图鉴奖励】:领取{OO0OOO000O0OO000O["crop_name"]}成就丨奖励{O00000O0O000000OO}☘️')#line:448
                                                if OOOOO0O0O0O000000 ['status']==500 :#line:449
                                                    print (f'【图鉴奖励】:{OOOOO0O0O0O000000["message"]}')#line:450
        except Exception as OO00OO0000OO0O0OO :#line:451
            print (OO00OO0000OO0O0OO )#line:452
    def watched_ad (O0O000OOOO00000OO ):#line:455
        try :#line:456
            OO0OO0OOOO000OOOO =f'__{timi_new()}'#line:457
            O00OOOOO0O0OOO0O0 ={'source':'scsc','authorization':O0O000OOOO00000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OOOO000OOOO ),'signstring':OO0OO0OOOO000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:468
            O0O0OO0OO0OOOO00O =requests .request ('get',f'{host}/game/getAllData',headers =O00OOOOO0O0OOO0O0 ).json ()#line:469
            if 'status'in O0O0OO0OO0OOOO00O :#line:471
                if O0O0OO0OO0OOOO00O ['status']==200 :#line:472
                    if 'offlineInfo'in O0O0OO0OO0OOOO00O ['data']:#line:473
                        time .sleep (random .randint (3 ,5 ))#line:474
                        OOO0O0O00OO0O0O00 =O0O0OO0OO0OOOO00O ['data']['offlineInfo']['off_minute']#line:475
                        O000OOOO0O0O0O000 =float (O0O0OO0OO0OOOO00O ['data']['silver'])/1000000000000 #line:476
                        time .sleep (1 )#line:477
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00OOOOO0O0OOO0O0 ).json ()#line:478
                        time .sleep (2 )#line:479
                        O00OO0000O0O0OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O00OOOOO0O0OOO0O0 ).json ()#line:480
                        if 'status'in O00OO0000O0O0OOO0 :#line:482
                            if O00OO0000O0O0OOO0 ['status']==200 :#line:483
                                OO0000O0OOO0OOOOO =float (O00OO0000O0O0OOO0 ['data']['silver'])/1000000000000 #line:484
                                O000O00O00OO000OO =str (OO0000O0OOO0OOOOO -O000OOOO0O0O0O000 )[:6 ]#line:485
                                print (f'【离线奖励】:翻倍离线{OOO0O0O00OO0O0O00}分钟奖励🌱数量:{O000O00O00OO000OO}t粒')#line:486
        except Exception as OOO00000O0O00OOOO :#line:487
            print (OOO00000O0O00OOOO )#line:488
    def user_ad (OOOO00OO000OOO000 ):#line:491
        try :#line:492
            OOOOOOOOOO000OO0O =f'__{timi_new()}'#line:493
            O00OOO0O000OO0OOO ={'source':'scsc','authorization':OOOO00OO000OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOOOO000OO0O ),'signstring':OOOOOOOOOO000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:504
            OO0O00000000O0O00 =requests .request ('get',f'{host}/user/ad',headers =O00OOO0O000OO0OOO ).json ()#line:505
            if 'status'in OO0O00000000O0O00 :#line:507
                if OO0O00000000O0O00 ['status']==200 :#line:508
                    OOO0O0O0O0O0O0000 =OO0O00000000O0O00 ['data']['max_time']#line:509
                    O0O0OO00OOOO00OOO =OO0O00000000O0O00 ['data']['watch_time']#line:510
                    O0OO0000OOO0000OO =OO0O00000000O0O00 ['data']['added_time']#line:511
                    print (f'【获取种子】:获取🌱剩余{O0OO0000OOO0000OO + OOO0O0O0O0O0O0000 - O0O0OO00OOOO00OOO}次丨好友提供:{O0OO0000OOO0000OO}次')#line:512
                    if O0OO0000OOO0000OO +OOO0O0O0O0O0O0000 -O0O0OO00OOOO00OOO >0 :#line:513
                        time .sleep (random .randint (16 ,19 ))#line:514
                        OOOO0O0O000OOOO00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00OOO0O000OO0OOO ).json ()#line:515
                        if 'status'in OOOO0O0O000OOOO00 :#line:517
                            if OOOO0O0O000OOOO00 ['status']==200 :#line:518
                                OOOOOOOOO00OOO0O0 =float (OOOO0O0O000OOOO00 ['data']['silver'])/1000000000000 #line:519
                                print (f'【获取种子】:获得🌱:{int(OOOOOOOOO00OOO0O0)}t粒')#line:520
                                return True #line:521
                            if OOOO0O0O000OOOO00 ['status']==500 :#line:522
                                OOOOO0OOOOO00OOOO =OOOO0O0O000OOOO00 ['message']#line:523
                                print (f'【获取种子】:{OOOOO0OOOOO00OOOO}')#line:524
                                return False #line:525
        except Exception as OO0OO00O000OO0O00 :#line:526
            print (OO0OO00O000OO0O00 )#line:527
    def synthetic (O0O0O0OOO0O0OO0O0 ):#line:530
        global id ,g #line:531
        try :#line:532
            OO000OOOOOOOO0OO0 =O0O0O0OOO0O0OO0O0 .level_new ()#line:533
            OO00OOOO0OO0OO0O0 =random .randint (9 ,11 )#line:534
            O0OOO00OO0O00OOOO =f'_site=8&targetSite={OO00OOOO0OO0OO0O0}_{timi_new()}'#line:535
            OO0OO000O0O0OO0O0 ={'source':'scsc','authorization':O0O0O0OOO0O0OO0O0 .token ,'timestamp':timi_new (),'sign':sign (O0OOO00OO0O00OOOO ),'signstring':O0OOO00OO0O00OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:546
            O00O00OO0O0OO0000 ={"site":int (8 ),"targetSite":int (OO00OOOO0OO0OO0O0 )}#line:547
            requests .request ('post',f'{host}/game/crops/move',headers =OO0OO000O0O0OO0O0 ,json =O00O00OO0O0OO0000 )#line:548
            while True :#line:549
                O0O00000O0OO0OO00 =f'__{timi_new()}'#line:550
                OOO0OOO0000O0000O ={'source':'scsc','authorization':O0O0O0OOO0O0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000O0OO0OO00 ),'signstring':O0O00000O0OO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:561
                O0000OOOO00000OO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OOO0000O0000O ).json ()#line:562
                if 'status'in O0000OOOO00000OO0 :#line:564
                    if O0000OOOO00000OO0 ['status']==200 :#line:565
                        OO0OOOO00O000OOO0 =O0000OOOO00000OO0 ['data']['cropList']#line:566
                        O00OO000O00OO00O0 =O0000OOOO00000OO0 ['data']['gameCoreDataDBid']#line:567
                        O0OOO0000O000O0O0 =float (O0000OOOO00000OO0 ['data']['silver'])/1000000000000 #line:568
                        O0OO00OOO0O0OO0OO =0 #line:573
                        for O00O0OO0OO0O00OOO in OO0OOOO00O000OOO0 :#line:574
                            if not O00O0OO0OO0O00OOO :#line:575
                                OO0OO0OO0OOOO00O0 =f'_crop_id={O00OO000O00OO00O0}&site={O0OO00OOO0O0OO0OO}_{O0O0O0OOO0O0OO0O0.time}'#line:576
                                O0O0O0OOO0OO00O0O ={'source':'scsc','authorization':O0O0O0OOO0O0OO0O0 .token ,'timestamp':O0O0O0OOO0O0OO0O0 .time ,'sign':sign (OO0OO0OO0OOOO00O0 ),'signstring':OO0OO0OO0OOOO00O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:586
                                O0OOO00O0O00OOO00 ={"site":O0OO00OOO0O0OO0OO ,"crop_id":O00OO000O00OO00O0 }#line:587
                                OOOOO000OOO000O00 =requests .request ('post',f'{host}/game/crops/buy',headers =O0O0O0OOO0OO00O0O ,data =O0OOO00O0O00OOO00 ).json ()#line:588
                                time .sleep (random .randint (1 ,3 )/10 )#line:590
                                if 'status'in OOOOO000OOO000O00 :#line:591
                                    if OOOOO000OOO000O00 ['status']==200 :#line:592
                                        if OOOOO000OOO000O00 ['message']=='种子数量不足':#line:593
                                            OO000OOOOOOOO0OO0 =O0O0O0OOO0O0OO0O0 .level_new ()#line:594
                                            print (f'【种植合成】:{OOOOO000OOO000O00["message"]}')#line:595
                                            if not O0O0O0OOO0O0OO0O0 .user_ad ():#line:596
                                                return False #line:597
                                    if OOOOO000OOO000O00 ['status']==500 :#line:598
                                        print (f'【种植合成】:{OOOOO000OOO000O00["message"]}')#line:599
                                        return False #line:600
                            O0OO00OOO0O0OO0OO +=1 #line:601
                        OO0OOO0O0O0OO00OO =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OOO0000O0000O ).json ()#line:602
                        O0O0OO0O00O00O0O0 =OO0OOO0O0O0OO00OO ['data']['cropList']#line:603
                        OO000OOO00OOOO000 =False #line:604
                        for O00O0OO0OO0O00OOO in range (12 ):#line:605
                            id =O0O0OO0O00O00O0O0 [O00O0OO0OO0O00OOO ]['level']#line:606
                            if float (OO000OOOOOOOO0OO0 )-float (id )>9 :#line:607
                                O000OO0O000O00OO0 =f'_site={O00O0OO0OO0O00OOO}_{timi_new()}'#line:608
                                O0000000O0O0OO0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O0O0OOO0O0OO0O0 .token ,'timestamp':timi_new (),'sign':sign (O000OO0O000O00OO0 ),'signstring':O000OO0O000O00OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:619
                                OO00O0O0O00OO00OO ={"site":O00O0OO0OO0O00OOO }#line:620
                                O000O0O000OO00OO0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0000000O0O0OO0OO ,data =OO00O0O0O00OO00OO ).json ()#line:622
                                if 'status'in O000O0O000OO00OO0 :#line:623
                                    if O000O0O000OO00OO0 ['status']==200 :#line:624
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:625
                            if id !=0 :#line:626
                                for O000O0O0O0000O00O in range (11 ):#line:627
                                    O00O00000O0O0OOOO =O000O0O0O0000O00O +1 #line:628
                                    g =O0O0OO0O00O00O0O0 [O00O00000O0O0OOOO ]['level']#line:629
                                    if id ==g :#line:630
                                        O0OO0OO0OOO0O0OO0 =O000O0O0O0000O00O +2 #line:631
                                        if O0OO0OO0OOO0O0OO0 !=O00O0OO0OO0O00OOO +1 :#line:632
                                            O00O0O0O000OO00O0 =O00O0OO0OO0O00OOO +1 #line:633
                                            time .sleep (random .randint (1 ,3 )/10 )#line:635
                                            O0OOO00OO0O00OOOO =f'_site={O00O0O0O000OO00O0 - 1}&targetSite={O0OO0OO0OOO0O0OO0 - 1}_{timi_new()}'#line:636
                                            OO0OO000O0O0OO0O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O0O0OOO0O0OO0O0 .token ,'timestamp':timi_new (),'sign':sign (O0OOO00OO0O00OOOO ),'signstring':O0OOO00OO0O00OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:653
                                            O0000OO0O0O00OO00 ={"site":int (O00O0O0O000OO00O0 -1 ),"targetSite":int (O0OO0OO0OOO0O0OO0 -1 )}#line:654
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0OO000O0O0OO0O0 ,json =O0000OO0O0O00OO00 )#line:655
                                            OO000OOO00OOOO000 =True #line:657
                                    if OO000OOO00OOOO000 :#line:658
                                        break #line:659
                                if OO000OOO00OOOO000 :#line:660
                                    break #line:661
        except :#line:662
            O0O0O0OOO0O0OO0O0 .synthetic ()#line:663
    def level_new (OOOO0O00OOO0O0O00 ):#line:666
        try :#line:667
            O0OO0000OOO00O0O0 =f'__{timi_new()}'#line:668
            O000OOOOO0000O0O0 ={'source':'scsc','authorization':OOOO0O00OOO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0000OOO00O0O0 ),'signstring':O0OO0000OOO00O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:679
            O00O00O0OOOO0O0O0 =requests .request ('get',f'{host}/user',headers =O000OOOOO0000O0O0 ).json ()#line:680
            if 'status'in O00O00O0OOOO0O0O0 :#line:681
                if O00O00O0OOOO0O0O0 ['status']==200 :#line:682
                    return float (O00O00O0OOOO0O0O0 ['data']['level'])#line:683
        except Exception as OO0O0OO0O0O00O000 :#line:684
            print (OO0O0OO0O0O00O000 )#line:685
    def propsraffle (OOOOO0O00O00O00O0 ):#line:688
        try :#line:689
            while True :#line:690
                O0O0OO00000OO0OOO =f'__{timi_new()}'#line:691
                OOO00OOOO0O00OO0O ={'source':'scsc','authorization':OOOOO0O00O00O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00000OO0OOO ),'signstring':O0O0OO00000OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:702
                OOO00OOOOOO0OOO00 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO00OOOO0O00OO0O ).json ()#line:703
                if 'status'in OOO00OOOOOO0OOO00 :#line:705
                    if OOO00OOOOOO0OOO00 ['status']==200 :#line:706
                        OOO0O00O0O00000O0 =OOO00OOOOOO0OOO00 ['data']['rows']#line:707
                        OOOOO0O00O0OOOO00 =OOO00OOOOOO0OOO00 ['data']['vstate']#line:708
                        if OOO0O00O0O00000O0 ==5 or OOO0O00O0O00000O0 ==6 or OOO0O00O0O00000O0 ==7 :#line:709
                            OO0O00O0000O0OO00 =OOO00OOOOOO0OOO00 ['data']['silver']#line:710
                            print (f'【转盘抽奖】:获得种子:{OO0O00O0000O0OO00}')#line:711
                        if OOO0O00O0O00000O0 ==1 or OOO0O00O0O00000O0 ==2 or OOO0O00O0O00000O0 ==3 :#line:712
                            OO000OOO0000O0000 =OOO00OOOOOO0OOO00 ['data']['clover']#line:713
                            print (f'【转盘抽奖】:获得三叶草:{OO000OOO0000O0000}')#line:714
                        if OOO0O00O0O00000O0 ==4 or OOO0O00O0O00000O0 ==8 :#line:715
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:716
                        if OOO0O00O0O00000O0 =='抽奖次数已用完':#line:720
                            break #line:754
                time .sleep (random .randint (8 ,15 )/10 )#line:755
        except Exception as OO0OO0O00000O0O0O :#line:756
            print (OO0OO0O00000O0O0O )#line:757
    def friends_invitation (O00O000O000O000O0 ):#line:760
        try :#line:761
            O0OO0000OO00000O0 =f'__{timi_new()}'#line:762
            OO00000OOOO0OO000 ={'source':'scsc','authorization':O00O000O000O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0000OO00000O0 ),'signstring':O0OO0000OO00000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:773
            O000OO00O0O0O0OOO =requests .request ('get',f'{host}/friends',headers =OO00000OOOO0OO000 ).json ()#line:774
            if 'status'in O000OO00O0O0O0OOO :#line:775
                if O000OO00O0O0O0OOO ['status']==200 :#line:776
                    OOO0OOO0O000O000O =O000OO00O0O0O0OOO ['data']['myInviteter']#line:777
                    if OOO0OOO0O000O000O :#line:778
                        OO0OO0O0OO0O0OOOO =OOO0OOO0O000O000O ['user']['nickname']#line:779
                        OOOOO000OO0O00O0O =O00O000O000O000O0 .certification ()#line:780
                        print (f'【查邀请人】:我的邀请人:{OO0OO0O0OO0O0OOOO}丨实名:{OOOOO000OO0O00O0O}')#line:781
                    else :#line:782
                        if O00O000O000O000O0 .innerId !='0':#line:783
                            O00O000O000O000O0 .invitation ()#line:784
        except Exception as O000O0OOO00O0OOOO :#line:785
            print (O000O0OOO00O0OOOO )#line:786
    def add_clover (O00O0OOO00O000OOO ):#line:789
        global golden_seed #line:790
        try :#line:791
            OO00OOOOOO000O0O0 =f'__{timi_new()}'#line:792
            OO0O00OOO00O0OOOO ={'source':'scsc','authorization':O00O0OOO00O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOOOO000O0O0 ),'signstring':OO00OOOOOO000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:803
            OOO0O0O0O00OOO00O =requests .request ('get',f'{host}/assets/clovers',headers =OO0O00OOO00O0OOOO ).json ()#line:804
            if 'status'in OOO0O0O0O00OOO00O :#line:806
                if OOO0O0O0O00OOO00O ['status']==200 :#line:807
                    O0O00O00OOO0O00OO =OOO0O0O0O00OOO00O ['data']['clover']#line:808
                    OOO00OOOOO0O0OOOO =OOO0O0O0O00OOO00O ['data']['used_clover']#line:809
                    O0O0OO00O0000OO00 =float (O0O00O00OOO0O00OO )-float (OOO00OOOOO0O0OOOO )#line:810
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOO00OOOOO0O0OOOO}')#line:811
                    if O00O0OOO00O000OOO .certification ()!='未实名':#line:812
                        if O0O0OO00O0000OO00 >1 :#line:813
                            OO00OOOOOO000O0O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O0OO00O0000OO00)}_{timi_new()}'#line:814
                            OO000OOOO0OO000OO ={'source':'scsc','authorization':O00O0OOO00O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOOOO000O0O0 ),'signstring':OO00OOOOOO000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:825
                            OOO0O0O0OOO0OOOO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O0OO00O0000OO00 )}#line:826
                            O00O00O0O000OOO0O =requests .request ('post',f'{host}/lottery/add-stake',headers =OO000OOOO0OO000OO ,data =OOO0O0O0OOO0OOOO0 ).json ()#line:827
                            if 'status'in O00O00O0O000OOO0O :#line:829
                                if O00O00O0O000OOO0O ['status']==200 :#line:830
                                    print (f'【参与抽奖】:添加☘️:{O00O00O0O000OOO0O["data"]}丨数量:{O0O0OO00O0000OO00}')#line:831
                                if O00O00O0O000OOO0O ['status']==500 :#line:832
                                    print (f'【参与抽奖】:添加☘️:{O00O00O0O000OOO0O["message"]}')#line:833
            OOO000O0O00000OOO =requests .request ('get',f'{host}/lottery',headers =OO0O00OOO00O0OOOO ).json ()#line:834
            OO0O0OO0OOOOO00O0 =O00O0OOO00O000OOO .winning_rewards ()#line:836
            if 'status'in OOO000O0O00000OOO :#line:837
                if OOO000O0O00000OOO ['status']==200 :#line:838
                    OOO0OOOO00OO0OO0O =OOO000O0O00000OOO ['data'][0 ]['day_get_gold_quantity']#line:839
                    golden_seed +=float (OOO0OOOO00OO0OO0O )#line:840
                    O0OO00OOO00O0O0OO =OOO000O0O00000OOO ['data'][1 ]['value']#line:841
                    OOO000O0O0O00O000 =OOO000O0O00000OOO ['data'][0 ]['join_number']#line:842
                    O0O00000OOOOOOOOO =int (float (OOO000O0O00000OOO ['data'][0 ]['totalValue']))#line:843
                    OOO0OOOOOO00O0O0O =float (O0OO00OOO00O0O0OO /O0O00000OOOOOOOOO )*10000 #line:844
                    OOO00O0O0OOO0OOOO =O0O00000OOOOOOOOO /OOO000O0O0O00O000 #line:845
                    print (f'【参与抽奖】:预计每天中{str(OOO0OOOO00OO0OO0O)[:6]}颗金种子丨好友收益:{str(OO0O0OO0OOOOO00O0)[:6]}')#line:846
                    print (f'【抽奖统计】:每1万☘️中{str(OOO0OOOOOO00O0O0O)[:6]}颗金种子丨☘️人均:{str(OOO00O0O0OOO0OOOO)[:7]}️')#line:847
        except Exception as O00OOOO0O0OO000OO :#line:848
            print (O00OOOO0O0OO000OO )#line:849
    def energy (O0O000O0O00OO0OO0 ):#line:853
        try :#line:854
            while True :#line:855
                O0O00O0OOO0OO00O0 =f'__{timi_new()}'#line:856
                OO00O0O000O0O0OOO ={'source':'scsc','authorization':O0O000O0O00OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OOO0OO00O0 ),'signstring':O0O00O0OOO0OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:867
                O00O0OOO00OOO0O00 =requests .request ('get',f'{host}/energy/general',headers =OO00O0O000O0O0OOO ).json ()#line:868
                if 'status'in O00O0OOO00OOO0O00 :#line:870
                    if O00O0OOO00OOO0O00 ['status']==200 :#line:871
                        O0O0OO0OO0O0OO000 =O00O0OOO00OOO0O00 ['data']['ordinary_water']#line:872
                        OO0O00O00000OOOOO =O00O0OOO00OOO0O00 ['data']['ordinary_fertilizer']#line:873
                        OO0OOO0OO0OO0OO00 =O00O0OOO00OOO0O00 ['data']['videoStatus']#line:874
                        OO000000000000O0O =O00O0OOO00OOO0O00 ['data']['waterVideoKey']#line:875
                        print (f'【我的营养】:肥料:{str(OO0O00O00000OOOOO).split(".")[0]}丨水滴:{str(O0O0OO0OO0O0OO000).split(".")[0]}')#line:876
                        if float (OO0O00O00000OOOOO )<96 :#line:877
                            if OO0OOO0OO0OO0OO00 :#line:878
                                time .sleep (random .randint (160 ,180 )/10 )#line:879
                                OO0O0OO0O000O000O =99 -float (OO0O00O00000OOOOO )#line:880
                                O0OO00000OO0000O0 ={"fertilizer":str (OO0O0OO0O000O000O ).split ('.')[0 ]}#line:881
                                OO000O00O0000OOO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO00O0O000O0O0OOO ).json ()#line:882
                                if 'status'in OO000O00O0000OOO0 :#line:884
                                    if OO000O00O0000OOO0 ['status']==200 :#line:885
                                        print (f'【购买肥料】:看广告获取肥料:{OO000O00O0000OOO0["message"]}')#line:886
                                    if OO000O00O0000OOO0 ['status']==500 :#line:887
                                        print (f'【购买肥料】:看广告获取肥料:{OO000O00O0000OOO0["message"]}')#line:888
                                        break #line:889
                            if energy :#line:890
                                if float (OO0O00O00000OOOOO )<78 :#line:891
                                    OO0O0OO0O000O000O =80 -float (OO0O00O00000OOOOO )#line:892
                                    OOO000OO0OOOO0O0O =f'_fertilizer={int(OO0O0OO0O000O000O)}_{timi_new()}'#line:893
                                    OO00OOO000O0O0O00 ={'source':'scsc','authorization':O0O000O0O00OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO0OOOO0O0O ),'signstring':OOO000OO0OOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:904
                                    OOOOOO0OOOO0O0OOO ={"fertilizer":int (OO0O0OO0O000O000O )}#line:905
                                    OO00000OOO0OOO00O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO00OOO000O0O0O00 ,data =OOOOOO0OOOO0O0OOO ).json ()#line:906
                                    if 'status'in OO00000OOO0OOO00O :#line:908
                                        if OO00000OOO0OOO00O ['status']==200 :#line:909
                                            print (f'【购买肥料】:购买肥料:{OO00000OOO0OOO00O["message"]}丨数量:{int(OO0O0OO0O000O000O)}')#line:910
                                        if OO00000OOO0OOO00O ['status']==500 :#line:911
                                            print (f'【购买肥料】:购买肥料:{OO00000OOO0OOO00O["message"]}丨数量:{int(OO0O0OO0O000O000O)}')#line:912
                                            O0O0O000OOOO000OO =OO00000OOO0OOO00O ["message"].split ('-')[1 ]#line:913
                                            O0OOO00OO0O0OO0OO =f'__{timi_new()}'#line:914
                                            OOOOO0O0O0O0O0000 ={'source':'scsc','authorization':O0O000O0O00OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OO0O0OO0OO ),'signstring':O0OOO00OO0O0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:925
                                            OO000OO0O0O0OO0OO =requests .request ('get',f'{host}/user',headers =OOOOO0O0O0O0O0000 ).json ()#line:926
                                            if 'status'in OO000OO0O0O0OO0OO :#line:927
                                                if OO000OO0O0O0OO0OO ['status']==200 :#line:928
                                                    O0O00O00OO000O00O =OO000OO0O0O0OO0OO ['data']['inner_id']#line:929
                                                    if give_gold (O0O00O00OO000O00O ,float (O0O0O000OOOO000OO )+1 ):#line:930
                                                        O0O000O0O00OO0OO0 .energy ()#line:931
                        if float (O0O0OO0OO0O0OO000 )<880 :#line:932
                            if OO000000000000O0O :#line:933
                                time .sleep (random .randint (160 ,180 )/10 )#line:934
                                OOO00OO00O00OOOOO =999 -float (O0O0OO0OO0O0OO000 )#line:935
                                OOOOOO00O0O0O00OO ={"water":str (OOO00OO00O00OOOOO ).split ('.')[0 ]}#line:936
                                OO00OOOOO00OOO0OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO00O0O000O0O0OOO ).json ()#line:937
                                if 'status'in OO00OOOOO00OOO0OO :#line:939
                                    if OO00OOOOO00OOO0OO ['status']==200 :#line:940
                                        print (f'【购买水滴】:看广告获取水滴:{OO00OOOOO00OOO0OO["message"]}')#line:941
                                    if OO00OOOOO00OOO0OO ['status']==500 :#line:942
                                        print (f'【购买水滴】:看广告获取水滴:{OO00OOOOO00OOO0OO["message"]}')#line:943
                                        break #line:944
                            if energy :#line:945
                                if float (O0O0OO0OO0O0OO000 )<780 :#line:946
                                    OOO00OO00O00OOOOO =800 -float (O0O0OO0OO0O0OO000 )#line:947
                                    OOOO000O00OO000OO =f'_water={int(OOO00OO00O00OOOOO)}_{timi_new()}'#line:948
                                    OO0000OO000O0OO0O ={'source':'scsc','authorization':O0O000O0O00OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O00OO000OO ),'signstring':OOOO000O00OO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:959
                                    OO0O00O0OOO0O000O ={"water":int (OOO00OO00O00OOOOO )}#line:960
                                    OOOOOO0O0OOOOOOO0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0000OO000O0OO0O ,data =OO0O00O0OOO0O000O ).json ()#line:962
                                    if 'status'in OOOOOO0O0OOOOOOO0 :#line:964
                                        if OOOOOO0O0OOOOOOO0 ['status']==200 :#line:965
                                            print (f'【购买水滴】:购买水滴:{OOOOOO0O0OOOOOOO0["message"]}丨数量:{int(OOO00OO00O00OOOOO)}')#line:966
                                        if OOOOOO0O0OOOOOOO0 ['status']==500 :#line:967
                                            print (f'【购买水滴】:购买水滴:{OOOOOO0O0OOOOOOO0["message"]}丨数量:{int(OOO00OO00O00OOOOO)}')#line:968
                                            O0O0O000OOOO000OO =OOOOOO0O0OOOOOOO0 ["message"].split ('-')[1 ]#line:969
                                            O0OOO00OO0O0OO0OO =f'__{timi_new()}'#line:970
                                            OOOOO0O0O0O0O0000 ={'source':'scsc','authorization':O0O000O0O00OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OO0O0OO0OO ),'signstring':O0OOO00OO0O0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:981
                                            OO000OO0O0O0OO0OO =requests .request ('get',f'{host}/user',headers =OOOOO0O0O0O0O0000 ).json ()#line:982
                                            if 'status'in OO000OO0O0O0OO0OO :#line:983
                                                if OO000OO0O0O0OO0OO ['status']==200 :#line:984
                                                    O0O00O00OO000O00O =OO000OO0O0O0OO0OO ['data']['inner_id']#line:985
                                                    if give_gold (O0O00O00OO000O00O ,float (O0O0O000OOOO000OO )+1 ):#line:986
                                                        O0O000O0O00OO0OO0 .energy ()#line:987
                        break #line:988
        except Exception as O0O0O0OOO0OOOO000 :#line:990
            print (O0O0O0OOO0OOOO000 )#line:991
def bundled_def ():#line:993
    O0O0O0O00OO0OOOOO =['5570536','7750212','7911652','7911680','7805624']#line:994
    return O0O0O0O00OO0OOOOO [random .randint (0 ,len (O0O0O0O00OO0OOOOO )-1 )]#line:995
def version_of_the_validation ():#line:999
    return str ((84 -56 )/10 )#line:1000
def sc2 ():#line:1002
    return "19319#$%^&*((*"#line:1003
def gitee_validation ():#line:1005
    try :#line:1006
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:1007
    except :#line:1008
        sys .exit (0 )#line:1009
def update_the_validation ():#line:1013
    try :#line:1014
        O0OO000O00OO0O0O0 =gitee_validation ()#line:1015
        if version_of_the_validation ()<O0OO000O00OO0O0O0 ['CityEarth']['edition']:#line:1016
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO000O00OO0O0O0["CityEarth"]["edition"]}   ❌')#line:1017
            print (f'更新内容=>>{O0OO000O00OO0O0O0["CityEarth"]["content"]}   🎉')#line:1018
        else :#line:1019
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO000O00OO0O0O0["CityEarth"]["edition"]}   ✅')#line:1020
            print (f'更新内容=>> {O0OO000O00OO0O0O0["CityEarth"]["content"]}   🎉')#line:1021
    except Exception as O0OOOO0OOO00O000O :#line:1022
        print (O0OOOO0OOO00O000O )#line:1023
def sc3 ():#line:1025
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1026
def os_qinglong ():#line:1028
    if application in os .environ :#line:1029
        OOO00O0O0O00OO000 =os .environ [application ].split ('\n')#line:1030
        if len (OOO00O0O0O00OO000 )>0 :#line:1031
            return OOO00O0O0O00OO000 #line:1032
        else :#line:1033
            print (f"{application}变量未启用")#line:1034
            print ('脚本退出')#line:1035
            sys .exit (1 )#line:1036
    else :#line:1037
        if token :#line:1038
            OOO00O0O0O00OO000 =token .split ('\n')#line:1039
            if len (OOO00O0O0O00OO000 )>0 :#line:1040
                return OOO00O0O0O00OO000 #line:1041
        else :#line:1042
            print (f"内置变量为空")#line:1043
            print ('脚本结束')#line:1044
            sys .exit (0 )#line:1045
if __name__ =='__main__':#line:1050
    start ()#line:1051
