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
@ 版本  2.9
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
        O00OO000OOO0O00OO =os_qinglong ()#line:10
        print (f"==========共找到{len(O00OO000OOO0O00OO)}个账号==========")#line:11
        for OO0OO0000O000O00O in O00OO000OOO0O00OO :#line:12
            OOO000OO0000O00OO =[]#line:13
            print (f"------------正在执行第{O00OO000OOO0O00OO.index(OO0OO0000O000O00O) + 1}个账号------------")#line:14
            OOOOOO000O0OOOOO0 =CityEarth (OO0OO0000O000O00O ,OOO000OO0000O00OO )#line:15
            def OOOO0OOOO00OOO0OO ():#line:17
                if OOOOOO000O0OOOOO0 .base_info ():#line:19
                    OOOOOO000O0OOOOO0 .sealing ()#line:21
                    OOOOOO000O0OOOOO0 .invitenum ()#line:23
                    OOOOOO000O0OOOOO0 .game_map ()#line:25
                    OOOOOO000O0OOOOO0 .friends_invitation ()#line:27
                    OOOOOO000O0OOOOO0 .propsraffle ()#line:33
                    OOOOOO000O0OOOOO0 .synthetic ()#line:35
                    OOOOOO000O0OOOOO0 .crops_illustrated ()#line:37
                    OOOOOO000O0OOOOO0 .give_gold ()#line:39
                    OOOOOO000O0OOOOO0 .withdraw ()#line:41
            O0OOO00000OO0OOOO =threading .Thread (target =OOOO0OOOO00OOO0OO )#line:43
            O0OOO00000OO0OOOO .start ()#line:44
            time .sleep (time_xx )#line:45
        print (f"------------正在处理推送通知------------")#line:46
        time .sleep (0.5 )#line:47
        O0O0OO00O00OOO00O =format_msg ()#line:48
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O0OO00O00OOO00O +' ')#line:49
    except Exception as OO00OO0O0000O00OO :#line:50
        print (OO00OO0O0000O00OO )#line:51
def give_gold (OO0O00O000OO00000 ,O0000OOO0O00OOO00 ):#line:54
        try :#line:55
            OOO0OO0O0OOO00O00 =f'_doneeNo={OO0O00O000OO00000}&quantity={int(O0000OOO0O00OOO00)}_{timi_new()}'#line:56
            OO0O00O0OOO0O0000 ={'source':'scsc','authorization':os_qinglong ()[0 ].split ('&')[0 ],'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O0OOO00O00 ),'signstring':OOO0OO0O0OOO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:67
            O0OOO0OOOOO000O0O ={"quantity":int (O0000OOO0O00OOO00 ),"doneeNo":OO0O00O000OO00000 }#line:71
            OO0O0000O0OOO0000 =requests .request ('post',f'{host}/finance/give-gold',headers =OO0O00O0OOO0O0000 ,data =O0OOO0OOOOO000O0O ).json ()#line:72
            if 'status'in OO0O0000O0OOO0000 :#line:74
                if OO0O0000O0OOO0000 ['status']==200 :#line:75
                    if OO0O0000O0OOO0000 ['data']:#line:76
                        print (f'【赠送种子】:赠送{int(O0000OOO0O00OOO00)}种子给{OO0O00O000OO00000}成功')#line:77
                        return True #line:78
                if OO0O0000O0OOO0000 ['status']==401 :#line:79
                    print (f'【赠送种子】:{OO0O0000O0OOO0000["message"]}')#line:80
                    return False #line:81
                if OO0O0000O0OOO0000 ['status']==500 :#line:82
                    print (f'【赠送种子】:{OO0O0000O0OOO0000["message"]}')#line:83
                    return False #line:84
            return False #line:85
        except Exception as O0OO0OOO000OO0OO0 :#line:86
            print (O0OO0OOO000OO0OO0 )#line:87
def sign (O0O00O0OOO000O00O ):#line:90
    OO000O0O0O000O00O =hashlib .md5 (O0O00O0OOO000O00O .encode ()).hexdigest ()#line:91
    OO00OO0OO0O0OO0O0 =sc1 ()#line:92
    OOO000O000OO00OOO =sc2 ()#line:93
    O0000O0O00OOO0O00 =sc3 ()#line:94
    O0OO000000OOOOO00 =OO00OO0OO0O0OO0O0 +OO000O0O0O000O00O +OOO000O000OO00OOO +O0000O0O00OOO0O00 #line:95
    O0OOO0000O00OO00O =hashlib .md5 (O0OO000000OOOOO00 .encode ()).hexdigest ()#line:96
    return O0OOO0000O00OO00O #line:97
def format_msg ():#line:101
    O0000O00000O0OOO0 =""#line:102
    for OOO0OO0OOO0O00000 in msg_list :#line:103
        O0000O00000O0OOO0 +=str (OOO0OO0OOO0O00000 )+"\r\n"#line:104
    return O0000O00000O0OOO0 #line:105
def sc1 ():#line:107
    return "scsc%^&*"#line:108
def timi_new ():#line:111
    return str (int (time .time ()*1000 ))#line:112
class CityEarth :#line:115
    def __init__ (O00OO0OO000O00OO0 ,O000OOOO0O0O0O0O0 ,OOOO00OO000O00O0O ):#line:117
        try :#line:118
            O00OO0OO000O00OO0 .msg =OOOO00OO000O00O0O #line:119
            O00OO0OO000O00OO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:120
            O00OO0OO000O00OO0 .token =O000OOOO0O0O0O0O0 .split ('&')[0 ]#line:121
            O00OO0OO000O00OO0 .innerId =O000OOOO0O0O0O0O0 .split ('&')[1 ]#line:122
            O00OO0OO000O00OO0 .doneeNo =O000OOOO0O0O0O0O0 .split ('&')[2 ]#line:123
        except :#line:124
            print ('变量格式错误')#line:125
    def base_info (OOO000O0O0OOOO0O0 ):#line:128
        try :#line:129
            OOO000O0O0OOOO0O0 .watched_ad ()#line:131
            OOOOOO00OOOO0O0OO =f'__{timi_new()}'#line:132
            O0000OOOOO0O00O0O ={'source':'scsc','authorization':OOO000O0O0OOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00OOOO0O0OO ),'signstring':OOOOOO00OOOO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:143
            O0O0000O0O0OOOO0O =requests .request ('get',f'{host}/user',headers =O0000OOOOO0O00O0O ).json ()#line:144
            if 'status'in O0O0000O0O0OOOO0O :#line:146
                if O0O0000O0O0OOOO0O ['status']==200 :#line:147
                    OOOO000OOO0O00OO0 =O0O0000O0O0OOOO0O ['data']['nickname']#line:148
                    O0O0OOO000OO0OOO0 =O0O0000O0O0OOOO0O ['data']['inner_id']#line:149
                    OO0OOO00O0000O00O =O0O0000O0O0OOOO0O ['data']['assets']['gold']#line:150
                    O000OO000OOOOOOO0 =O0O0000O0O0OOOO0O ['data']['level']#line:151
                    print (f'【账号信息】:昵称:{OOOO000OOO0O00OO0[:5]}丨ID:{O0O0OOO000OO0OOO0}丨等级:{O000OO000OOOOOOO0}丨金种子:{str(OO0OOO00O0000O00O).split(".")[0]}')#line:152
                if O0O0000O0O0OOOO0O ['status']==401 :#line:153
                    print (O0O0000O0O0OOOO0O ['message'])#line:154
                    OOO000O0O0OOOO0O0 .msg .append ('有账号失效了')#line:155
                    return False #line:156
                if O0O0000O0O0OOOO0O ['status']==500 :#line:157
                    return False #line:158
            return True #line:159
        except Exception as O00O000OOOOO0O000 :#line:160
            print (O00O000OOOOO0O000 )#line:161
    def sealing (OOO0OOOO0O0O0OOO0 ):#line:164
        try :#line:165
            O00000OO000OO0O0O =f'__{timi_new()}'#line:166
            OOOO0O00OOOO0O0O0 ={'source':'scsc','authorization':OOO0OOOO0O0O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO000OO0O0O ),'signstring':O00000OO000OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:177
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOO0O00OOOO0O0O0 )#line:178
            requests .request ('get',f'{host}/packsack/list',headers =OOOO0O00OOOO0O0O0 )#line:179
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOO0O00OOOO0O0O0 )#line:180
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOO0O00OOOO0O0O0 )#line:181
            requests .request ('get',f'{host}/user',headers =OOOO0O00OOOO0O0O0 )#line:182
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOO0O00OOOO0O0O0 )#line:183
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOO0O00OOOO0O0O0 )#line:184
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOO0O00OOOO0O0O0 )#line:185
            requests .request ('get',f'{host}/game/getAllData',headers =OOOO0O00OOOO0O0O0 )#line:186
            requests .request ('get',f'{host}/assets',headers =OOOO0O00OOOO0O0O0 )#line:187
        except Exception as OOOO0OOO00OOOOOOO :#line:188
            print (OOOO0OOO00OOOOOOO )#line:189
    def withdraw (OO0OO00O0000OOO0O ):#line:193
        OOO0O0O0O0O0000OO =f'__{timi_new()}'#line:194
        OOOO00OOO00O00OOO ={'source':'scsc','authorization':OO0OO00O0000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0O0O0000OO ),'signstring':OOO0O0O0O0O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:205
        O0OO0000OOO0000O0 =requests .request ('get',f'{host}/assets',headers =OOOO00OOO00O00OOO ).json ()#line:206
        if 'status'in O0OO0000OOO0000O0 :#line:208
            if O0OO0000OOO0000O0 ['status']==200 :#line:209
                O0O0OOOOO00OOO0OO =O0OO0000OOO0000O0 ['data']['cash']#line:210
                if float (O0O0OOOOO00OOO0OO )>20 :#line:211
                    OOO0O0O0O0O0000OO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:212
                    OOOO00OOO00O00OOO ={'authorization':OO0OO00O0000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0O0O0000OO ),'signstring':OOO0O0O0O0O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:222
                    OOO0000OOOOOOOO0O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:223
                    OOO00O000OOO0O000 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOO00OOO00O00OOO ,data =OOO0000OOOOOOOO0O ).json ()#line:225
                    print (OOO00O000OOO0O000 )#line:226
    def invitenum (OO0OOO0OOO0O00O00 ):#line:229
        OO0O00O0OOO0000OO =f'__{timi_new()}'#line:230
        OO000OOOOOOO0OOOO ={'source':'scsc','authorization':OO0OOO0OOO0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O0OOO0000OO ),'signstring':OO0O00O0OOO0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:241
        O0000OO0O0O0O00O0 =requests .request ('get',f'{host}/invite/invitenum',headers =OO000OOOOOOO0OOOO ).json ()#line:242
        if 'status'in O0000OO0O0O0O00O0 :#line:244
            if O0000OO0O0O0O00O0 ['status']==200 :#line:245
                OOO000000OO000O0O =O0000OO0O0O0O00O0 ['data']['invited_count']#line:246
                O0O00O0OOO00OOO0O =O0000OO0O0O0O00O0 ['data']['invited_second_count']#line:247
                print (f'【我的邀请】:直邀好友:{OOO000000OO000O0O}丨间邀好友:{O0O00O0OOO00OOO0O}')#line:248
    def game_map (OO0OOO0000OOO0O0O ):#line:251
        try :#line:252
            OO00000OOO0OOO000 =f'__{timi_new()}'#line:253
            OOO0OOOO000O00000 ={'source':'scsc','authorization':OO0OOO0000OOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OOO0OOO000 ),'signstring':OO00000OOO0OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:264
            OO0OO0OOOOOO0OO00 =requests .request ('get',f'{host}/game/map',headers =OOO0OOOO000O00000 ).json ()#line:265
            if 'status'in OO0OO0OOOOOO0OO00 :#line:267
                if OO0OO0OOOOOO0OO00 ['status']==200 :#line:268
                    for OOO0OOO0OO0O00OO0 in OO0OO0OOOOOO0OO00 ['data']['list'][0 ]['crops']:#line:269
                        O0O00OOOO0000OOO0 =OOO0OOO0OO0O00OO0 ['level']#line:271
                        if O0O00OOOO0000OOO0 ==41 :#line:272
                            O00OO00O0OO00O000 =OOO0OOO0OO0O00OO0 ['crop_name']#line:273
                            O0OOOOOO0O000OO0O =OOO0OOO0OO0O00OO0 ['count']#line:274
                            if O0OOOOOO0O000OO0O >0 :#line:275
                                print (f'【农业资产】:{O00OO00O0OO00O000}丨数量:{O0OOOOOO0O000OO0O}')#line:276
        except Exception as O00OOOO0OOO00O00O :#line:277
            print (O00OOOO0OOO00O00O )#line:278
    def give_gold (O00OOO000O0O0OO00 ):#line:281
        try :#line:282
            OOOO00OOO0OO0OOO0 =f'__{timi_new()}'#line:283
            OO0OO0O0O0OO0O000 ={'source':'scsc','authorization':O00OOO000O0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOO0OO0OOO0 ),'signstring':OOOO00OOO0OO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:294
            O00O00OOO0O0O0OOO =requests .request ('get',f'{host}/user',headers =OO0OO0O0O0OO0O000 ).json ()#line:295
            if 'status'in O00O00OOO0O0O0OOO :#line:296
                if O00O00OOO0O0O0OOO ['status']==200 :#line:297
                    if float (O00OOO000O0O0OO00 .doneeNo )!=0 :#line:298
                        OOO0OO0O000O0OOOO =O00O00OOO0O0O0OOO ['data']['assets']['gold']#line:299
                        if float (OOO0OO0O000O0OOOO )>float (O00OOO000O0O0OO00 .innerId ):#line:300
                            OO0O00000O0OOO00O =int (float (OOO0OO0O000O0OOOO )/1.1 )#line:301
                            OOOO00OOO0OO0OOO0 =f'_doneeNo={O00OOO000O0O0OO00.doneeNo}&quantity={OO0O00000O0OOO00O}_{timi_new()}'#line:302
                            OO0OO0O0O0OO0O000 ={'source':'scsc','authorization':O00OOO000O0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOO0OO0OOO0 ),'signstring':OOOO00OOO0OO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:313
                            O00O00000OOOO000O ={"quantity":OO0O00000O0OOO00O ,"doneeNo":O00OOO000O0O0OO00 .doneeNo }#line:317
                            O0OOOOOOOO0O00OOO =requests .request ('post',f'{host}/finance/give-gold',headers =OO0OO0O0O0OO0O000 ,data =O00O00000OOOO000O ).json ()#line:318
                            if 'status'in O0OOOOOOOO0O00OOO :#line:320
                                if O0OOOOOOOO0O00OOO ['status']==200 :#line:321
                                    if O0OOOOOOOO0O00OOO ['data']:#line:322
                                        print (f'【赠送种子】:赠送{OO0O00000O0OOO00O}种子给{O00OOO000O0O0OO00.doneeNo}成功')#line:323
                    else :#line:324
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:325
        except Exception as OOO0OOOOOO0000000 :#line:326
            print (OOO0OOOOOO0000000 )#line:327
    def invitation (OO00OO0OOOO0OOO0O ):#line:329
        try :#line:330
            _O0000OOOO00OO0O00 =float (bundled_def ())/4 #line:331
            OOOO0O00O00O0O00O =f'_innerId={int(_O0000OOOO00OO0O00)}_{timi_new()}'#line:332
            O00O0000OO00O0O0O ={'source':'scsc','authorization':OO00OO0OOOO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00O00O0O00O ),'signstring':OOOO0O00O00O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:343
            OO0O0O00O00OO00OO ={"innerId":int (_O0000OOOO00OO0O00 )}#line:344
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00O0000OO00O0O0O ,data =OO0O0O00O00OO00OO )#line:345
        except Exception as O0O0OOO0OO000O000 :#line:346
            print (O0O0OOO0OO000O000 )#line:347
    def winning_rewards (OO0O000OOO0O0O00O ):#line:350
        try :#line:351
            O0OO00OO0O000O0O0 =f'__{timi_new()}'#line:352
            OOO00O0OOO0OO000O ={'source':'scsc','authorization':OO0O000OOO0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO0O000O0O0 ),'signstring':O0OO00OO0O000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:363
            OOOOOOO0OOOOOOOOO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO00O0OOO0OO000O ).json ()#line:364
            if 'status'in OOOOOOO0OOOOOOOOO :#line:366
                if OOOOOOO0OOOOOOOOO ['status']==200 :#line:367
                    if OOOOOOO0OOOOOOOOO ['data']['amount']:#line:368
                        O0O0O000O000OOO0O =OOOOOOO0OOOOOOOOO ['data']['amount']['gold']#line:369
                        return O0O0O000O000OOO0O #line:370
                    else :#line:371
                        return 0 #line:372
        except Exception as O0000000OO00O00O0 :#line:373
            print (O0000000OO00O00O0 )#line:374
    def certification (O0OOO00O0OOO00OOO ):#line:377
        try :#line:378
            OOO0O0OOO00O0000O =f'__{timi_new()}'#line:379
            O0OO0OO0O0O0O00OO ={'source':'scsc','authorization':O0OOO00O0OOO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OOO00O0000O ),'signstring':OOO0O0OOO00O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:390
            O0OO00O00O0OOOO00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0OO0OO0O0O0O00OO ).json ()#line:391
            if 'status'in O0OO00O00O0OOOO00 :#line:393
                if O0OO00O00O0OOOO00 ['status']==200 :#line:394
                    if O0OO00O00O0OOOO00 ['data']['result']:#line:395
                        O0O0O00000OOOOO0O =O0OO00O00O0OOOO00 ['data']['nick_name']#line:396
                        return O0O0O00000OOOOO0O #line:397
                    else :#line:398
                        return '未实名'#line:399
        except Exception as OO0OO00O000OO0000 :#line:400
            print (OO0OO00O000OO0000 )#line:401
    def crops_illustrated (OOOO0OO00O000O0O0 ):#line:404
        try :#line:405
            O0000OOO0OOOOO000 =f'__{timi_new()}'#line:406
            OO0OO00OOOO0O00OO ={'source':'scsc','authorization':OOOO0OO00O000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOO0OOOOO000 ),'signstring':O0000OOO0OOOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:417
            OOOO000OO00O0OOO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0OO00OOOO0O00OO ).json ()#line:418
            if 'status'in OOOO000OO00O0OOO0 :#line:420
                if OOOO000OO00O0OOO0 ['status']==200 :#line:421
                    O0OOO000OOOO000OO =OOOO000OO00O0OOO0 ['data'][0 ]['crops']#line:422
                    for OOO00OO0OO0OOOOO0 in O0OOO000OOOO000OO :#line:423
                        if OOO00OO0OO0OOOOO0 ['ill_clover_award']:#line:424
                            if float (OOO00OO0OO0OOOOO0 ['ill_clover_award'])>1 :#line:425
                                if OOO00OO0OO0OOOOO0 ['is_finish']:#line:426
                                    if not OOO00OO0OO0OOOOO0 ['is_getit']:#line:427
                                        if OOOO0OO00O000O0O0 .certification ()!='未实名':#line:428
                                            O0000OOO0OOOOO000 =f'_award_level={OOO00OO0OO0OOOOO0["level"]}_{timi_new()}'#line:429
                                            OO0OO00OOOO0O00OO ={'source':'scsc','authorization':OOOO0OO00O000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOO0OOOOO000 ),'signstring':O0000OOO0OOOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:440
                                            OOO000000O0O0OO0O ={"award_level":OOO00OO0OO0OOOOO0 ['level']}#line:441
                                            OO00OOOOO0OOO00O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0OO00OOOO0O00OO ,json =OOO000000O0O0OO0O ).json ()#line:443
                                            if 'status'in OO00OOOOO0OOO00O0 :#line:444
                                                if OO00OOOOO0OOO00O0 ['status']==200 :#line:445
                                                    OOO0O0OO0O00OOO0O =OO00OOOOO0OOO00O0 ['data']['ill_clover_award']#line:446
                                                    print (f'【图鉴奖励】:领取{OOO00OO0OO0OOOOO0["crop_name"]}成就丨奖励{OOO0O0OO0O00OOO0O}☘️')#line:448
                                                if OO00OOOOO0OOO00O0 ['status']==500 :#line:449
                                                    print (f'【图鉴奖励】:{OO00OOOOO0OOO00O0["message"]}')#line:450
        except Exception as OO00O0OOO0OO0O0O0 :#line:451
            print (OO00O0OOO0OO0O0O0 )#line:452
    def watched_ad (O0OOO00OOOOOO0OOO ):#line:455
        try :#line:456
            O00O00OO0O0O000OO =f'__{timi_new()}'#line:457
            OOO000OOO000O00OO ={'source':'scsc','authorization':O0OOO00OOOOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO0O0O000OO ),'signstring':O00O00OO0O0O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:468
            O0OO0OOOOOO0OOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OOO000O00OO ).json ()#line:469
            if 'status'in O0OO0OOOOOO0OOOO0 :#line:471
                if O0OO0OOOOOO0OOOO0 ['status']==200 :#line:472
                    if 'offlineInfo'in O0OO0OOOOOO0OOOO0 ['data']:#line:473
                        time .sleep (random .randint (3 ,5 ))#line:474
                        OO0OO00OOOO0O0OOO =O0OO0OOOOOO0OOOO0 ['data']['offlineInfo']['off_minute']#line:475
                        O0O000O00O0O0OOOO =float (O0OO0OOOOOO0OOOO0 ['data']['silver'])/1000000000000 #line:476
                        time .sleep (1 )#line:477
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO000OOO000O00OO ).json ()#line:478
                        time .sleep (2 )#line:479
                        OOOO0O0O00OOO000O =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OOO000O00OO ).json ()#line:480
                        if 'status'in OOOO0O0O00OOO000O :#line:482
                            if OOOO0O0O00OOO000O ['status']==200 :#line:483
                                OOO00OOOO00OO0000 =float (OOOO0O0O00OOO000O ['data']['silver'])/1000000000000 #line:484
                                O0000OO00OOOOO000 =str (OOO00OOOO00OO0000 -O0O000O00O0O0OOOO )[:6 ]#line:485
                                print (f'【离线奖励】:翻倍离线{OO0OO00OOOO0O0OOO}分钟奖励🌱数量:{O0000OO00OOOOO000}t粒')#line:486
        except Exception as O0O0O0OO0O0OO0O00 :#line:487
            print (O0O0O0OO0O0OO0O00 )#line:488
    def user_ad (OO00OOOO000OOO0O0 ):#line:491
        try :#line:492
            O000OOO00OOO00000 =f'__{timi_new()}'#line:493
            OO00OOOO0O00OO000 ={'source':'scsc','authorization':OO00OOOO000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO00OOO00000 ),'signstring':O000OOO00OOO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:504
            O0O0OO0OOO00O00O0 =requests .request ('get',f'{host}/user/ad',headers =OO00OOOO0O00OO000 ).json ()#line:505
            if 'status'in O0O0OO0OOO00O00O0 :#line:507
                if O0O0OO0OOO00O00O0 ['status']==200 :#line:508
                    O000O0O0O00OOOO00 =O0O0OO0OOO00O00O0 ['data']['max_time']#line:509
                    O0O00O000OO00OO00 =O0O0OO0OOO00O00O0 ['data']['watch_time']#line:510
                    O00OO0OOOOO00O0O0 =O0O0OO0OOO00O00O0 ['data']['added_time']#line:511
                    print (f'【获取种子】:获取🌱剩余{O00OO0OOOOO00O0O0 + O000O0O0O00OOOO00 - O0O00O000OO00OO00}次丨好友提供:{O00OO0OOOOO00O0O0}次')#line:512
                    if O00OO0OOOOO00O0O0 +O000O0O0O00OOOO00 -O0O00O000OO00OO00 >0 :#line:513
                        time .sleep (random .randint (16 ,19 ))#line:514
                        O00000000OO0OOO00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO00OOOO0O00OO000 ).json ()#line:515
                        if 'status'in O00000000OO0OOO00 :#line:517
                            if O00000000OO0OOO00 ['status']==200 :#line:518
                                O0000O00OOO000O0O =float (O00000000OO0OOO00 ['data']['silver'])/1000000000000 #line:519
                                print (f'【获取种子】:获得🌱:{int(O0000O00OOO000O0O)}t粒')#line:520
                                return True #line:521
                            if O00000000OO0OOO00 ['status']==500 :#line:522
                                OO0O0O000OO0O0OOO =O00000000OO0OOO00 ['message']#line:523
                                print (f'【获取种子】:{OO0O0O000OO0O0OOO}')#line:524
                                return False #line:525
        except Exception as OOOO0O00OO0O00OOO :#line:526
            print (OOOO0O00OO0O00OOO )#line:527
    def synthetic (O00O000O00O000000 ):#line:530
        global id ,g #line:531
        try :#line:532
            O0OO00O000000O0OO =O00O000O00O000000 .level_new ()#line:533
            O0OOO0OOOO00OOOOO =random .randint (9 ,11 )#line:534
            O000O00O0OOO0O0O0 =f'_site=8&targetSite={O0OOO0OOOO00OOOOO}_{timi_new()}'#line:535
            OOO00000000OOOOO0 ={'source':'scsc','authorization':O00O000O00O000000 .token ,'timestamp':timi_new (),'sign':sign (O000O00O0OOO0O0O0 ),'signstring':O000O00O0OOO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:546
            OOO00OOOO00O00000 ={"site":int (8 ),"targetSite":int (O0OOO0OOOO00OOOOO )}#line:547
            requests .request ('post',f'{host}/game/crops/move',headers =OOO00000000OOOOO0 ,json =OOO00OOOO00O00000 )#line:548
            while True :#line:549
                OOO000OOOOO00OOO0 =f'__{timi_new()}'#line:550
                OO0O0OO0OO0OOO00O ={'source':'scsc','authorization':O00O000O00O000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOOOO00OOO0 ),'signstring':OOO000OOOOO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:561
                O0OO0OO0O0000OO0O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0OO0OO0OOO00O ).json ()#line:562
                if 'status'in O0OO0OO0O0000OO0O :#line:564
                    if O0OO0OO0O0000OO0O ['status']==200 :#line:565
                        OO00O00O00O0OO0O0 =O0OO0OO0O0000OO0O ['data']['cropList']#line:566
                        O0O00OOOO00OOOO00 =O0OO0OO0O0000OO0O ['data']['gameCoreDataDBid']#line:567
                        OO000O0O00O000O00 =float (O0OO0OO0O0000OO0O ['data']['silver'])/1000000000000 #line:568
                        OO000OO000OOOO00O =0 #line:573
                        for O0O00O0OO0000O0OO in OO00O00O00O0OO0O0 :#line:574
                            if not O0O00O0OO0000O0OO :#line:575
                                OO000OOO0O0OO0000 =f'_crop_id={O0O00OOOO00OOOO00}&site={OO000OO000OOOO00O}_{O00O000O00O000000.time}'#line:576
                                OO00OO00000OOOOOO ={'source':'scsc','authorization':O00O000O00O000000 .token ,'timestamp':O00O000O00O000000 .time ,'sign':sign (OO000OOO0O0OO0000 ),'signstring':OO000OOO0O0OO0000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:586
                                O00O0OOO0000OOO0O ={"site":OO000OO000OOOO00O ,"crop_id":O0O00OOOO00OOOO00 }#line:587
                                O000OO00000O0OO00 =requests .request ('post',f'{host}/game/crops/buy',headers =OO00OO00000OOOOOO ,data =O00O0OOO0000OOO0O ).json ()#line:588
                                time .sleep (random .randint (1 ,3 )/10 )#line:590
                                if 'status'in O000OO00000O0OO00 :#line:591
                                    if O000OO00000O0OO00 ['status']==200 :#line:592
                                        if O000OO00000O0OO00 ['message']=='种子数量不足':#line:593
                                            O0OO00O000000O0OO =O00O000O00O000000 .level_new ()#line:594
                                            print (f'【种植合成】:{O000OO00000O0OO00["message"]}')#line:595
                                            if not O00O000O00O000000 .user_ad ():#line:596
                                                return False #line:597
                                    if O000OO00000O0OO00 ['status']==500 :#line:598
                                        print (f'【种植合成】:{O000OO00000O0OO00["message"]}')#line:599
                                        return False #line:600
                            OO000OO000OOOO00O +=1 #line:601
                        O0OO00O0000OO0OOO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0OO0OO0OOO00O ).json ()#line:602
                        O000000O0O000OOOO =O0OO00O0000OO0OOO ['data']['cropList']#line:603
                        OO0000OO0OO000OOO =False #line:604
                        for O0O00O0OO0000O0OO in range (12 ):#line:605
                            id =O000000O0O000OOOO [O0O00O0OO0000O0OO ]['level']#line:606
                            if float (O0OO00O000000O0OO )-float (id )>9 :#line:607
                                O0000O000OO0OO0OO =f'_site={O0O00O0OO0000O0OO}_{timi_new()}'#line:608
                                O0OOOO0OOOO0OO000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00O000O00O000000 .token ,'timestamp':timi_new (),'sign':sign (O0000O000OO0OO0OO ),'signstring':O0000O000OO0OO0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:619
                                OOOOOOOO0OOO00O0O ={"site":O0O00O0OO0000O0OO }#line:620
                                OOO000O0OOOOO00O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OOOO0OOOO0OO000 ,data =OOOOOOOO0OOO00O0O ).json ()#line:622
                                if 'status'in OOO000O0OOOOO00O0 :#line:623
                                    if OOO000O0OOOOO00O0 ['status']==200 :#line:624
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:625
                            if id !=0 :#line:626
                                for OOOOOOO000O00000O in range (11 ):#line:627
                                    O0O0O00000O000000 =OOOOOOO000O00000O +1 #line:628
                                    g =O000000O0O000OOOO [O0O0O00000O000000 ]['level']#line:629
                                    if id ==g :#line:630
                                        OO0O000OO0OO0O00O =OOOOOOO000O00000O +2 #line:631
                                        if OO0O000OO0OO0O00O !=O0O00O0OO0000O0OO +1 :#line:632
                                            O0OO0000O0OO000O0 =O0O00O0OO0000O0OO +1 #line:633
                                            time .sleep (random .randint (1 ,3 )/10 )#line:635
                                            O000O00O0OOO0O0O0 =f'_site={O0OO0000O0OO000O0 - 1}&targetSite={OO0O000OO0OO0O00O - 1}_{timi_new()}'#line:636
                                            OOO00000000OOOOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00O000O00O000000 .token ,'timestamp':timi_new (),'sign':sign (O000O00O0OOO0O0O0 ),'signstring':O000O00O0OOO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:653
                                            OOOO0OO00OOOO0OO0 ={"site":int (O0OO0000O0OO000O0 -1 ),"targetSite":int (OO0O000OO0OO0O00O -1 )}#line:654
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOO00000000OOOOO0 ,json =OOOO0OO00OOOO0OO0 )#line:655
                                            OO0000OO0OO000OOO =True #line:657
                                    if OO0000OO0OO000OOO :#line:658
                                        break #line:659
                                if OO0000OO0OO000OOO :#line:660
                                    break #line:661
        except :#line:662
            O00O000O00O000000 .synthetic ()#line:663
    def level_new (OOO000OO0O0O0OO00 ):#line:666
        try :#line:667
            O000O0OOOOOO0OOOO =f'__{timi_new()}'#line:668
            O00OOOOOOOOO00O00 ={'source':'scsc','authorization':OOO000OO0O0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOOOOO0OOOO ),'signstring':O000O0OOOOOO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:679
            O0O0OOO000OO000O0 =requests .request ('get',f'{host}/user',headers =O00OOOOOOOOO00O00 ).json ()#line:680
            if 'status'in O0O0OOO000OO000O0 :#line:681
                if O0O0OOO000OO000O0 ['status']==200 :#line:682
                    return float (O0O0OOO000OO000O0 ['data']['level'])#line:683
        except Exception as OO0OOOOOO0OOO0O00 :#line:684
            print (OO0OOOOOO0OOO0O00 )#line:685
    def propsraffle (O00OOO0OO0O0O00OO ):#line:688
        try :#line:689
            while True :#line:690
                OO0000OOOO00O0OOO =f'__{timi_new()}'#line:691
                OO0OO00O0OOO00OOO ={'source':'scsc','authorization':O00OOO0OO0O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOOO00O0OOO ),'signstring':OO0000OOOO00O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:702
                O0OO0OOO0O0000OOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0OO00O0OOO00OOO ).json ()#line:703
                if 'status'in O0OO0OOO0O0000OOO :#line:705
                    if O0OO0OOO0O0000OOO ['status']==200 :#line:706
                        O0O0OOO000O0O0O0O =O0OO0OOO0O0000OOO ['data']['rows']#line:707
                        O00OOO00O0O0OOO00 =O0OO0OOO0O0000OOO ['data']['vstate']#line:708
                        if O0O0OOO000O0O0O0O ==5 or O0O0OOO000O0O0O0O ==6 or O0O0OOO000O0O0O0O ==7 :#line:709
                            OO0O0OOOO0O0O0OO0 =O0OO0OOO0O0000OOO ['data']['silver']#line:710
                            print (f'【转盘抽奖】:获得种子:{OO0O0OOOO0O0O0OO0}')#line:711
                        if O0O0OOO000O0O0O0O ==1 or O0O0OOO000O0O0O0O ==2 or O0O0OOO000O0O0O0O ==3 :#line:712
                            O0O00OO0O0O0OO0OO =O0OO0OOO0O0000OOO ['data']['clover']#line:713
                            print (f'【转盘抽奖】:获得三叶草:{O0O00OO0O0O0OO0OO}')#line:714
                        if O0O0OOO000O0O0O0O ==4 or O0O0OOO000O0O0O0O ==8 :#line:715
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:716
                        if O0O0OOO000O0O0O0O =='抽奖次数已用完':#line:720
                            break #line:754
                time .sleep (random .randint (8 ,15 )/10 )#line:755
        except Exception as O0O00O000OO0O0OOO :#line:756
            print (O0O00O000OO0O0OOO )#line:757
    def friends_invitation (OOOO0OO0O000O0OOO ):#line:760
        try :#line:761
            OO0OO00O0000O0O0O =f'__{timi_new()}'#line:762
            OO0OO0O000OO00OO0 ={'source':'scsc','authorization':OOOO0OO0O000O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00O0000O0O0O ),'signstring':OO0OO00O0000O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:773
            OO0OO000OO0O0OOOO =requests .request ('get',f'{host}/friends',headers =OO0OO0O000OO00OO0 ).json ()#line:774
            if 'status'in OO0OO000OO0O0OOOO :#line:775
                if OO0OO000OO0O0OOOO ['status']==200 :#line:776
                    O0OO000OOO00O0O0O =OO0OO000OO0O0OOOO ['data']['myInviteter']#line:777
                    if O0OO000OOO00O0O0O :#line:778
                        O000O00O00OOOOO0O =O0OO000OOO00O0O0O ['user']['nickname']#line:779
                        O000OOOOOOO0OO0OO =OOOO0OO0O000O0OOO .certification ()#line:780
                        print (f'【查邀请人】:我的邀请人:{O000O00O00OOOOO0O}丨实名:{O000OOOOOOO0OO0OO}')#line:781
                    else :#line:782
                        if OOOO0OO0O000O0OOO .innerId !='0':#line:783
                            OOOO0OO0O000O0OOO .invitation ()#line:784
        except Exception as O0OOOOOO0O0OO0O00 :#line:785
            print (O0OOOOOO0O0OO0O00 )#line:786
    def add_clover (OO000O00O000OO000 ):#line:789
        global golden_seed #line:790
        try :#line:791
            O0O00OOOOOO0OO000 =f'__{timi_new()}'#line:792
            O000O0O000O0OO00O ={'source':'scsc','authorization':OO000O00O000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOOOOO0OO000 ),'signstring':O0O00OOOOOO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:803
            O0OO0OOOOO00OOOOO =requests .request ('get',f'{host}/assets/clovers',headers =O000O0O000O0OO00O ).json ()#line:804
            if 'status'in O0OO0OOOOO00OOOOO :#line:806
                if O0OO0OOOOO00OOOOO ['status']==200 :#line:807
                    OOOOOO0000OO00OOO =O0OO0OOOOO00OOOOO ['data']['clover']#line:808
                    O00000O0OOOOO0O0O =O0OO0OOOOO00OOOOO ['data']['used_clover']#line:809
                    OO00O0O000000OOO0 =float (OOOOOO0000OO00OOO )-float (O00000O0OOOOO0O0O )#line:810
                    print (f'【参与抽奖】:参与抽奖的☘️:{O00000O0OOOOO0O0O}')#line:811
                    if OO000O00O000OO000 .certification ()!='未实名':#line:812
                        if OO00O0O000000OOO0 >1 :#line:813
                            O0O00OOOOOO0OO000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO00O0O000000OOO0)}_{timi_new()}'#line:814
                            O00000O00OO00O000 ={'source':'scsc','authorization':OO000O00O000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOOOOO0OO000 ),'signstring':O0O00OOOOOO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:825
                            O00O0O0O0O0OOO000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO00O0O000000OOO0 )}#line:826
                            O0OOO00OO0OOOOOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =O00000O00OO00O000 ,data =O00O0O0O0O0OOO000 ).json ()#line:827
                            if 'status'in O0OOO00OO0OOOOOOO :#line:829
                                if O0OOO00OO0OOOOOOO ['status']==200 :#line:830
                                    print (f'【参与抽奖】:添加☘️:{O0OOO00OO0OOOOOOO["data"]}丨数量:{OO00O0O000000OOO0}')#line:831
                                if O0OOO00OO0OOOOOOO ['status']==500 :#line:832
                                    print (f'【参与抽奖】:添加☘️:{O0OOO00OO0OOOOOOO["message"]}')#line:833
            OOOOO0OO0OOOOOOO0 =requests .request ('get',f'{host}/lottery',headers =O000O0O000O0OO00O ).json ()#line:834
            O00O000O0O0O000O0 =OO000O00O000OO000 .winning_rewards ()#line:836
            if 'status'in OOOOO0OO0OOOOOOO0 :#line:837
                if OOOOO0OO0OOOOOOO0 ['status']==200 :#line:838
                    O00OOO000O00OOO00 =OOOOO0OO0OOOOOOO0 ['data'][0 ]['day_get_gold_quantity']#line:839
                    golden_seed +=float (O00OOO000O00OOO00 )#line:840
                    O0O00OOOOO00O0OO0 =OOOOO0OO0OOOOOOO0 ['data'][1 ]['value']#line:841
                    O000000O00OO0000O =OOOOO0OO0OOOOOOO0 ['data'][0 ]['join_number']#line:842
                    O0OOOOOOO0O0O0O0O =int (float (OOOOO0OO0OOOOOOO0 ['data'][0 ]['totalValue']))#line:843
                    O0O0OO0OO0OOOOO0O =float (O0O00OOOOO00O0OO0 /O0OOOOOOO0O0O0O0O )*10000 #line:844
                    O00000O0000000OOO =O0OOOOOOO0O0O0O0O /O000000O00OO0000O #line:845
                    print (f'【参与抽奖】:预计每天中{str(O00OOO000O00OOO00)[:6]}颗金种子丨好友收益:{str(O00O000O0O0O000O0)[:6]}')#line:846
                    print (f'【抽奖统计】:每1万☘️中{str(O0O0OO0OO0OOOOO0O)[:6]}颗金种子丨☘️人均:{str(O00000O0000000OOO)[:7]}️')#line:847
        except Exception as OO0O000OO0OOO0000 :#line:848
            print (OO0O000OO0OOO0000 )#line:849
    def energy (O0000000000OO0OOO ):#line:853
        try :#line:854
            while True :#line:855
                OOO0000OOOO0O000O =f'__{timi_new()}'#line:856
                OO0000OOO0OOO0OO0 ={'source':'scsc','authorization':O0000000000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OOOO0O000O ),'signstring':OOO0000OOOO0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:867
                OO0OOO00O000OOOOO =requests .request ('get',f'{host}/energy/general',headers =OO0000OOO0OOO0OO0 ).json ()#line:868
                if 'status'in OO0OOO00O000OOOOO :#line:870
                    if OO0OOO00O000OOOOO ['status']==200 :#line:871
                        O00O0OOOOO0000O0O =OO0OOO00O000OOOOO ['data']['ordinary_water']#line:872
                        OO0000OO00OOO0OOO =OO0OOO00O000OOOOO ['data']['ordinary_fertilizer']#line:873
                        O00O0O00O000O0OOO =OO0OOO00O000OOOOO ['data']['videoStatus']#line:874
                        O0000OOOO0O0O0OOO =OO0OOO00O000OOOOO ['data']['waterVideoKey']#line:875
                        print (f'【我的营养】:肥料:{str(OO0000OO00OOO0OOO).split(".")[0]}丨水滴:{str(O00O0OOOOO0000O0O).split(".")[0]}')#line:876
                        if float (OO0000OO00OOO0OOO )<96 :#line:877
                            if O00O0O00O000O0OOO :#line:878
                                time .sleep (random .randint (160 ,180 )/10 )#line:879
                                O000OOO000O00OOOO =99 -float (OO0000OO00OOO0OOO )#line:880
                                O0O0OOOOOOO00O0O0 ={"fertilizer":str (O000OOO000O00OOOO ).split ('.')[0 ]}#line:881
                                O00O0O00O00OOO000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0000OOO0OOO0OO0 ).json ()#line:882
                                if 'status'in O00O0O00O00OOO000 :#line:884
                                    if O00O0O00O00OOO000 ['status']==200 :#line:885
                                        print (f'【购买肥料】:看广告获取肥料:{O00O0O00O00OOO000["message"]}')#line:886
                                    if O00O0O00O00OOO000 ['status']==500 :#line:887
                                        print (f'【购买肥料】:看广告获取肥料:{O00O0O00O00OOO000["message"]}')#line:888
                                        break #line:889
                            if energy :#line:890
                                if float (OO0000OO00OOO0OOO )<78 :#line:891
                                    O000OOO000O00OOOO =80 -float (OO0000OO00OOO0OOO )#line:892
                                    O00O00OOO00OO000O =f'_fertilizer={int(O000OOO000O00OOOO)}_{timi_new()}'#line:893
                                    OOOOO0000OOO00O0O ={'source':'scsc','authorization':O0000000000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OOO00OO000O ),'signstring':O00O00OOO00OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:904
                                    OOO000O00O00OOO0O ={"fertilizer":int (O000OOO000O00OOOO )}#line:905
                                    OO00O00OOOO0O0O0O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOOO0000OOO00O0O ,data =OOO000O00O00OOO0O ).json ()#line:906
                                    if 'status'in OO00O00OOOO0O0O0O :#line:908
                                        if OO00O00OOOO0O0O0O ['status']==200 :#line:909
                                            print (f'【购买肥料】:购买肥料:{OO00O00OOOO0O0O0O["message"]}丨数量:{int(O000OOO000O00OOOO)}')#line:910
                                        if OO00O00OOOO0O0O0O ['status']==500 :#line:911
                                            print (f'【购买肥料】:购买肥料:{OO00O00OOOO0O0O0O["message"]}丨数量:{int(O000OOO000O00OOOO)}')#line:912
                                            OOOOO0O0O00000000 =OO00O00OOOO0O0O0O ["message"].split ('-')[1 ]#line:913
                                            O0OO00O00OOOO00OO =f'__{timi_new()}'#line:914
                                            OO0O00OO00000OOOO ={'source':'scsc','authorization':O0000000000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O00OOOO00OO ),'signstring':O0OO00O00OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:925
                                            OO00O00OOO0OO000O =requests .request ('get',f'{host}/user',headers =OO0O00OO00000OOOO ).json ()#line:926
                                            if 'status'in OO00O00OOO0OO000O :#line:927
                                                if OO00O00OOO0OO000O ['status']==200 :#line:928
                                                    OO0OOO0OOOOO0OO00 =OO00O00OOO0OO000O ['data']['inner_id']#line:929
                                                    if give_gold (OO0OOO0OOOOO0OO00 ,float (OOOOO0O0O00000000 )+1 ):#line:930
                                                        O0000000000OO0OOO .energy ()#line:931
                        if float (O00O0OOOOO0000O0O )<880 :#line:932
                            if O0000OOOO0O0O0OOO :#line:933
                                time .sleep (random .randint (160 ,180 )/10 )#line:934
                                OO0OOOO00O00O00OO =999 -float (O00O0OOOOO0000O0O )#line:935
                                OO00O0000O0000000 ={"water":str (OO0OOOO00O00O00OO ).split ('.')[0 ]}#line:936
                                OOOO00O000000OO0O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0000OOO0OOO0OO0 ).json ()#line:937
                                if 'status'in OOOO00O000000OO0O :#line:939
                                    if OOOO00O000000OO0O ['status']==200 :#line:940
                                        print (f'【购买水滴】:看广告获取水滴:{OOOO00O000000OO0O["message"]}')#line:941
                                    if OOOO00O000000OO0O ['status']==500 :#line:942
                                        print (f'【购买水滴】:看广告获取水滴:{OOOO00O000000OO0O["message"]}')#line:943
                                        break #line:944
                            if energy :#line:945
                                if float (O00O0OOOOO0000O0O )<780 :#line:946
                                    OO0OOOO00O00O00OO =800 -float (O00O0OOOOO0000O0O )#line:947
                                    OOOO00OOOOO0OO0OO =f'_water={int(OO0OOOO00O00O00OO)}_{timi_new()}'#line:948
                                    OOO0OO0OO000OOO00 ={'source':'scsc','authorization':O0000000000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOOOO0OO0OO ),'signstring':OOOO00OOOOO0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:959
                                    O0OO0OOO0OO00OOOO ={"water":int (OO0OOOO00O00O00OO )}#line:960
                                    O000000OO0OOO0000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO0OO0OO000OOO00 ,data =O0OO0OOO0OO00OOOO ).json ()#line:962
                                    if 'status'in O000000OO0OOO0000 :#line:964
                                        if O000000OO0OOO0000 ['status']==200 :#line:965
                                            print (f'【购买水滴】:购买水滴:{O000000OO0OOO0000["message"]}丨数量:{int(OO0OOOO00O00O00OO)}')#line:966
                                        if O000000OO0OOO0000 ['status']==500 :#line:967
                                            print (f'【购买水滴】:购买水滴:{O000000OO0OOO0000["message"]}丨数量:{int(OO0OOOO00O00O00OO)}')#line:968
                                            OOOOO0O0O00000000 =O000000OO0OOO0000 ["message"].split ('-')[1 ]#line:969
                                            O0OO00O00OOOO00OO =f'__{timi_new()}'#line:970
                                            OO0O00OO00000OOOO ={'source':'scsc','authorization':O0000000000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O00OOOO00OO ),'signstring':O0OO00O00OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:981
                                            OO00O00OOO0OO000O =requests .request ('get',f'{host}/user',headers =OO0O00OO00000OOOO ).json ()#line:982
                                            if 'status'in OO00O00OOO0OO000O :#line:983
                                                if OO00O00OOO0OO000O ['status']==200 :#line:984
                                                    OO0OOO0OOOOO0OO00 =OO00O00OOO0OO000O ['data']['inner_id']#line:985
                                                    if give_gold (OO0OOO0OOOOO0OO00 ,float (OOOOO0O0O00000000 )+1 ):#line:986
                                                        O0000000000OO0OOO .energy ()#line:987
                        break #line:988
        except Exception as O0O000OOO0O000OO0 :#line:990
            print (O0O000OOO0O000OO0 )#line:991
def bundled_def ():#line:993
    OOO000O00O0OO0O00 =['5570536','7750212','7911652','7911680','7805624']#line:994
    return OOO000O00O0OO0O00 [random .randint (0 ,len (OOO000O00O0OO0O00 )-1 )]#line:995
def version_of_the_validation ():#line:999
    return str ((85 -56 )/10 )#line:1000
def sc2 ():#line:1002
    return "19319#$%^&*((*"#line:1003
def gitee_validation ():#line:1005
    try :#line:1006
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:1007
    except :#line:1008
        sys .exit (0 )#line:1009
def update_the_validation ():#line:1013
    try :#line:1014
        OO00O0O0000OO0O00 =gitee_validation ()#line:1015
        if version_of_the_validation ()<OO00O0O0000OO0O00 ['CityEarth']['edition']:#line:1016
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O0O0000OO0O00["CityEarth"]["edition"]}   ❌')#line:1017
            print (f'更新内容=>>{OO00O0O0000OO0O00["CityEarth"]["content"]}   🎉')#line:1018
        else :#line:1019
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O0O0000OO0O00["CityEarth"]["edition"]}   ✅')#line:1020
            print (f'更新内容=>> {OO00O0O0000OO0O00["CityEarth"]["content"]}   🎉')#line:1021
    except Exception as O00O0000O00O000O0 :#line:1022
        print (O00O0000O00O000O0 )#line:1023
def sc3 ():#line:1025
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1026
def os_qinglong ():#line:1028
    if application in os .environ :#line:1029
        O0000OO00OOOOO00O =os .environ [application ].split ('\n')#line:1030
        if len (O0000OO00OOOOO00O )>0 :#line:1031
            return O0000OO00OOOOO00O #line:1032
        else :#line:1033
            print (f"{application}变量未启用")#line:1034
            print ('脚本退出')#line:1035
            sys .exit (1 )#line:1036
    else :#line:1037
        if token :#line:1038
            O0000OO00OOOOO00O =token .split ('\n')#line:1039
            if len (O0000OO00OOOOO00O )>0 :#line:1040
                return O0000OO00OOOOO00O #line:1041
        else :#line:1042
            print (f"内置变量为空")#line:1043
            print ('脚本结束')#line:1044
            sys .exit (0 )#line:1045
if __name__ =='__main__':#line:1050
    start ()#line:1051
