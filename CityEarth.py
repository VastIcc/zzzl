# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import hashlib
    import json
    import urllib
    import requests
    import random
    import threading
    from notify import send
except Exception as e:
    t = re.findall("d '(.*?)'", str(e))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: 8 0,1,2,8,12,13,14,15,19,20,21,22 * * *
@ new Env('生城世朝')
@ 项目地址  https://sc19319.oss-cn-hangzhou.aliyuncs.com/scsc/prod/1.9.3.1.S4195.apk
@ 抓取  http://scsc.sc19319.com 的authorization值
@ 青龙变量  青龙配置文件 export ce_token="authorization&赠送金种子数量大于&赠送金种子id" 
@ 如果你有20金种子填10就会赠 填21就不会赠送  不赠送全填 999999     多号换行
@ 变量示范    export ce_token="557b8069-1234-4ae7-9e29-b7871f91541b&999999&999999"  用&符号分开数据
@ 版本  2.0
"""
change_nickname = False  # 
application = 'ce_token'  # 变量名
token = ''
time_xx = random.randint(8, 12)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
version ='3.1.4195311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        OOO0000O00OO000O0 =os_qinglong ()#line:10
        print (f"==========共找到{len(OOO0000O00OO000O0)}个账号==========")#line:11
        for OO0O00OOOOOO000O0 in OOO0000O00OO000O0 :#line:12
            OO0OO0OO0O000OOOO =[]#line:13
            print (f"------------正在执行第{OOO0000O00OO000O0.index(OO0O00OOOOOO000O0) + 1}个账号------------")#line:14
            O000OO0OO0000O00O =CityEarth (OO0O00OOOOOO000O0 ,OO0OO0OO0O000OOOO )#line:15
            def O0OO0O0O0O00OO0O0 ():#line:17
                if O000OO0OO0000O00O .base_info ():#line:19
                    O000OO0OO0000O00O .sealing ()#line:21
                    O000OO0OO0000O00O .invitenum ()#line:23
                    O000OO0OO0000O00O .game_map ()#line:25
                    O000OO0OO0000O00O .friends_invitation ()#line:27
                    O000OO0OO0000O00O .add_clover ()#line:29
                    O000OO0OO0000O00O .propsraffle ()#line:31
                    O000OO0OO0000O00O .synthetic ()#line:33
                    O000OO0OO0000O00O .crops_illustrated ()#line:35
                    O000OO0OO0000O00O .give_gold ()#line:37
                    O000OO0OO0000O00O .withdraw ()#line:39
                    O000OO0OO0000O00O .energy ()#line:41
            OOOO0OOOOOO0OO00O =threading .Thread (target =O0OO0O0O0O00OO0O0 )#line:43
            OOOO0OOOOOO0OO00O .start ()#line:44
            time .sleep (time_xx )#line:45
        print (f"------------正在处理推送通知------------")#line:46
        time .sleep (3 )#line:47
        O0OO0OO0OOOO0000O =format_msg ()#line:48
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0OO0OO0OOOO0000O +' ')#line:49
    except Exception as O0OOOO0OOO0O00O00 :#line:50
        print (O0OOOO0OOO0O00O00 )#line:51
def sign (OO0O000OO0O000OOO ):#line:54
    O000O0OOOOO00O0OO =hashlib .md5 (OO0O000OO0O000OOO .encode ()).hexdigest ()#line:55
    OOO0OO0OOOOOO0000 ="scsc%^&*"+O000O0OOOOO00O0OO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:56
    OOOO0OO00OO000OO0 =hashlib .md5 (OOO0OO0OOOOOO0000 .encode ()).hexdigest ()#line:57
    return OOOO0OO00OO000OO0 #line:58
def format_msg ():#line:60
    O00OOO00OOO0000O0 =""#line:61
    for OO0O0OO00O0O0OO0O in msg_list :#line:62
        O00OOO00OOO0000O0 +=str (OO0O0OO00O0O0OO0O )+"\r\n"#line:63
    return O00OOO00OOO0000O0 #line:64
def timi_new ():#line:66
    return str (int (time .time ()*1000 ))#line:67
class CityEarth :#line:70
    def __init__ (OO0O000000000000O ,O0OO00O0O0OO0OO0O ,O00O0OOO0OO00OOOO ):#line:72
        try :#line:73
            OO0O000000000000O .msg =O00O0OOO0OO00OOOO #line:74
            OO0O000000000000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:75
            OO0O000000000000O .token =O0OO00O0O0OO0OO0O .split ('&')[0 ]#line:76
            OO0O000000000000O .innerId =O0OO00O0O0OO0OO0O .split ('&')[1 ]#line:77
            OO0O000000000000O .doneeNo =O0OO00O0O0OO0OO0O .split ('&')[2 ]#line:78
        except :#line:79
            print ('变量格式错误')#line:80
    def base_info (O0000OOO0OO0O00O0 ):#line:83
        try :#line:84
            O0000OOO0OO0O00O0 .watched_ad ()#line:86
            OOO0OO0O0OO00O0O0 =f'__{timi_new()}'#line:87
            O00O0OO0OO000000O ={'authorization':O0000OOO0OO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O0OO00O0O0 ),'signstring':OOO0OO0O0OO00O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:96
            OO000O00O0O000OOO =requests .request ('get',f'{host}/user',headers =O00O0OO0OO000000O ).json ()#line:97
            if 'status'in OO000O00O0O000OOO :#line:99
                if OO000O00O0O000OOO ['status']==200 :#line:100
                    O00OOOO0OO00O00OO =OO000O00O0O000OOO ['data']['nickname']#line:101
                    O0OO0O00OO0OOOO00 =OO000O00O0O000OOO ['data']['inner_id']#line:102
                    O0O0O0O0000O0000O =OO000O00O0O000OOO ['data']['assets']['gold']#line:103
                    OO00O0OOOO00O0000 =OO000O00O0O000OOO ['data']['level']#line:104
                    print (f'【账号信息】:昵称:{O00OOOO0OO00O00OO[:5]}丨ID:{O0OO0O00OO0OOOO00}丨等级:{OO00O0OOOO00O0000}丨种子:{str(O0O0O0O0000O0000O).split(".")[0]}')#line:106
                    if change_nickname :#line:107
                        O0000OOO0OO0O00O0 .change_nickname (O0OO0O00OO0OOOO00 )#line:109
                if OO000O00O0O000OOO ['status']==401 :#line:110
                    print (OO000O00O0O000OOO ['message'])#line:111
                    O0000OOO0OO0O00O0 .msg .append ('有账号失效了')#line:112
                    return False #line:113
                if OO000O00O0O000OOO ['status']==500 :#line:114
                    return False #line:115
            return True #line:116
        except Exception as OOO00O0OOO0O00O0O :#line:117
            print (OOO00O0OOO0O00O0O )#line:118
    def sealing (O0OOO00OO0O000O00 ):#line:121
        try :#line:122
            O0OOO0OO0O000O0OO =f'__{timi_new()}'#line:123
            OO0O00OO0O0OOOOOO ={'authorization':O0OOO00OO0O000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO0O000O0OO ),'signstring':O0OOO0OO0O000O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:132
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0O00OO0O0OOOOOO )#line:133
            requests .request ('get',f'{host}/packsack/list',headers =OO0O00OO0O0OOOOOO )#line:134
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0O00OO0O0OOOOOO )#line:135
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0O00OO0O0OOOOOO )#line:136
            requests .request ('get',f'{host}/user',headers =OO0O00OO0O0OOOOOO )#line:137
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0O00OO0O0OOOOOO )#line:138
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0O00OO0O0OOOOOO )#line:139
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0O00OO0O0OOOOOO )#line:140
            requests .request ('get',f'{host}/game/getAllData',headers =OO0O00OO0O0OOOOOO )#line:141
            requests .request ('get',f'{host}/assets',headers =OO0O00OO0O0OOOOOO )#line:142
        except Exception as OO00O0O0O000OOOO0 :#line:143
            print (OO00O0O0O000OOOO0 )#line:144
    def change_nickname (OOOOO00000000O0OO ,OO0OO0O00O0O000O0 ):#line:147
        try :#line:148
            O00OOO00O0OOO0000 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:149
            OO00000OO0OO00OOO =requests .request ('post','https://www.qmsjmfb.com/',data =O00OOO00O0OOO0000 ).text #line:150
            OO0000OOOO00OO000 =re .findall ('<ul><li>(.*?)</li>',OO00000OO0OO00OOO )[0 ][:3 ]+str (OO0OO0O00O0O000O0 )[5 :]#line:151
            OO0O00OO0OO0000OO =f'_nickname=_{timi_new()}'#line:152
            O0OO00OOO00O0O0OO ={'authorization':OOOOO00000000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OO0OO0000OO ),'signstring':OO0O00OO0OO0000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:161
            O000O0O0O00O00O00 ={"nickname":str (OO0000OOOO00OO000 )}#line:163
            print (O000O0O0O00O00O00 )#line:164
            OOO000000OO0OOO0O =requests .request ('patch',f'{host}/user/nickname',headers =O0OO00OOO00O0O0OO ,data =O000O0O0O00O00O00 ).json ()#line:165
            print (OOO000000OO0OOO0O )#line:166
        except Exception as O0O0O0OO0000OO000 :#line:168
            print (O0O0O0OO0000OO000 )#line:169
    def withdraw (OO0O0O0O0O000O000 ):#line:172
        O0OOOOO0O0OO0OOO0 =f'__{timi_new()}'#line:173
        O0000OOO0O00OOO00 ={'authorization':OO0O0O0O0O000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0O0OO0OOO0 ),'signstring':O0OOOOO0O0OO0OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:182
        O00O0O000O000OOO0 =requests .request ('get',f'{host}/assets',headers =O0000OOO0O00OOO00 ).json ()#line:183
        if 'status'in O00O0O000O000OOO0 :#line:185
            if O00O0O000O000OOO0 ['status']==200 :#line:186
                O00O0O000OOO00O00 =O00O0O000O000OOO0 ['data']['cash']#line:187
                if float (O00O0O000OOO00O00 )>20 :#line:188
                    O0OOOOO0O0OO0OOO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:189
                    O0000OOO0O00OOO00 ={'authorization':OO0O0O0O0O000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0O0OO0OOO0 ),'signstring':O0OOOOO0O0OO0OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:198
                    OOOO00O000O000OOO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:199
                    OOO0O0OO0O0O0OOOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0000OOO0O00OOO00 ,data =OOOO00O000O000OOO ).json ()#line:201
                    print (OOO0O0OO0O0O0OOOO )#line:202
    def invitenum (O0OOOOOO0000O000O ):#line:205
        OOOOOO00000OO0OOO =f'__{timi_new()}'#line:206
        O0O00O000OO00O000 ={'authorization':O0OOOOOO0000O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00000OO0OOO ),'signstring':OOOOOO00000OO0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:215
        OOOO0OO0000000O0O =requests .request ('get',f'{host}/invite/invitenum',headers =O0O00O000OO00O000 ).json ()#line:216
        if 'status'in OOOO0OO0000000O0O :#line:218
            if OOOO0OO0000000O0O ['status']==200 :#line:219
                O0OO0000O0O0OOOOO =OOOO0OO0000000O0O ['data']['invited_count']#line:220
                O000000O0OO0000OO =OOOO0OO0000000O0O ['data']['invited_second_count']#line:221
                print (f'【我的邀请】:直邀好友:{O0OO0000O0O0OOOOO}丨间邀好友:{O000000O0OO0000OO}')#line:222
    def game_map (OOOOOOO0OO00O0000 ):#line:225
        try :#line:226
            OOO0OO00000O0000O =f'__{timi_new()}'#line:227
            OOO00OOO000000OO0 ={'authorization':OOOOOOO0OO00O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00000O0000O ),'signstring':OOO0OO00000O0000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:236
            O00O00O000000O0OO =requests .request ('get',f'{host}/game/map',headers =OOO00OOO000000OO0 ).json ()#line:237
            if 'status'in O00O00O000000O0OO :#line:239
                if O00O00O000000O0OO ['status']==200 :#line:240
                    for O00OO000OO00OO0OO in O00O00O000000O0OO ['data']['list'][0 ]['crops']:#line:241
                        OOOOO0000O00OO0OO =O00OO000OO00OO0OO ['level']#line:243
                        if OOOOO0000O00OO0OO ==41 :#line:244
                            O0O00OO000O0OO00O =O00OO000OO00OO0OO ['crop_name']#line:245
                            OOOOO00O00OO00OOO =O00OO000OO00OO0OO ['count']#line:246
                            if OOOOO00O00OO00OOO >0 :#line:247
                                print (f'【农业资产】:{O0O00OO000O0OO00O}丨数量:{OOOOO00O00OO00OOO}')#line:248
        except Exception as OOOO00O0OOO000O00 :#line:249
            print (OOOO00O0OOO000O00 )#line:250
    def give_gold (OO0OOOO00O000O0OO ):#line:253
        try :#line:254
            O0OOO00O0O000O000 =f'__{timi_new()}'#line:255
            O0O0OO0OO00O00000 ={'authorization':OO0OOOO00O000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0O000O000 ),'signstring':O0OOO00O0O000O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:264
            OOOOOO0OO0OOO0000 =requests .request ('get',f'{host}/user',headers =O0O0OO0OO00O00000 ).json ()#line:265
            if 'status'in OOOOOO0OO0OOO0000 :#line:266
                if OOOOOO0OO0OOO0000 ['status']==200 :#line:267
                    if float (OO0OOOO00O000O0OO .doneeNo )!=0 :#line:268
                        O0O0O0000OOO000O0 =OOOOOO0OO0OOO0000 ['data']['assets']['gold']#line:269
                        if float (O0O0O0000OOO000O0 )>float (OO0OOOO00O000O0OO .innerId ):#line:270
                            OO00OOOO000OOO0OO =int (float (O0O0O0000OOO000O0 )/1.1 )#line:271
                            O0OOO00O0O000O000 =f'_doneeNo={OO0OOOO00O000O0OO.doneeNo}&quantity={OO00OOOO000OOO0OO}_{timi_new()}'#line:272
                            O0O0OO0OO00O00000 ={'authorization':OO0OOOO00O000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0O000O000 ),'signstring':O0OOO00O0O000O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:281
                            O00O0O0O0OOO0OOOO ={"quantity":OO00OOOO000OOO0OO ,"doneeNo":OO0OOOO00O000O0OO .doneeNo }#line:285
                            O0OO0O0000O000000 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0OO0OO00O00000 ,data =O00O0O0O0OOO0OOOO ).json ()#line:286
                            if 'status'in O0OO0O0000O000000 :#line:288
                                if O0OO0O0000O000000 ['status']==200 :#line:289
                                    if O0OO0O0000O000000 ['data']:#line:290
                                        print (f'【赠送种子】:赠送{OO00OOOO000OOO0OO}种子给{OO0OOOO00O000O0OO.doneeNo}成功')#line:291
                    else :#line:292
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:293
        except Exception as O00000O00O00000OO :#line:294
            print (O00000O00O00000OO )#line:295
    def invitation (O00OO00OO00O0O00O ):#line:297
        try :#line:298
            _O0O000O000O000000 =float (bundled_def ())/4 #line:299
            OOOOO0OOO0O0OOOO0 =f'_innerId={int(_O0O000O000O000000)}_{timi_new()}'#line:300
            O0000O0O00O00OO0O ={'authorization':O00OO00OO00O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOO0O0OOOO0 ),'signstring':OOOOO0OOO0O0OOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:309
            O0O0000OO0000OOO0 ={"innerId":int (_O0O000O000O000000 )}#line:310
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0000O0O00O00OO0O ,data =O0O0000OO0000OOO0 )#line:311
        except Exception as OOOOO0OO0O0OOO00O :#line:312
            print (OOOOO0OO0O0OOO00O )#line:313
    def winning_rewards (OO00O0OOOO0O00O0O ):#line:316
        try :#line:317
            O0000O00O0OOOO0OO =f'__{timi_new()}'#line:318
            O0000O00OOO00OOO0 ={'authorization':OO00O0OOOO0O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00O0OOOO0OO ),'signstring':O0000O00O0OOOO0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:327
            OOOOOO0O00O0O0OO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0000O00OOO00OOO0 ).json ()#line:328
            if 'status'in OOOOOO0O00O0O0OO0 :#line:330
                if OOOOOO0O00O0O0OO0 ['status']==200 :#line:331
                    if OOOOOO0O00O0O0OO0 ['data']['amount']:#line:332
                        OOOOO00O0O0OOOOO0 =OOOOOO0O00O0O0OO0 ['data']['amount']['gold']#line:333
                        return OOOOO00O0O0OOOOO0 #line:334
                    else :#line:335
                        return 0 #line:336
        except Exception as OO0OOOO00O0OOO000 :#line:337
            print (OO0OOOO00O0OOO000 )#line:338
    def certification (O0O00OO0000OOOOOO ):#line:341
        try :#line:342
            OO0OO000OOOO0O0OO =f'__{timi_new()}'#line:343
            O000O0OO00OO0OO0O ={'authorization':O0O00OO0000OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OOOO0O0OO ),'signstring':OO0OO000OOOO0O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:352
            OOO00O00OO0OOOOOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O000O0OO00OO0OO0O ).json ()#line:353
            if 'status'in OOO00O00OO0OOOOOO :#line:355
                if OOO00O00OO0OOOOOO ['status']==200 :#line:356
                    if OOO00O00OO0OOOOOO ['data']['result']:#line:357
                        O0OOOOO0OO000O000 =OOO00O00OO0OOOOOO ['data']['nick_name']#line:358
                        return O0OOOOO0OO000O000 #line:359
                    else :#line:360
                        return '未实名'#line:361
        except Exception as O0OOO00OO00OOO000 :#line:362
            print (O0OOO00OO00OOO000 )#line:363
    def crops_illustrated (O0OOO000000O0O000 ):#line:366
        try :#line:367
            O0OO0O0000OOOO000 =f'__{timi_new()}'#line:368
            O0O00O000O00OO000 ={'authorization':O0OOO000000O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0000OOOO000 ),'signstring':O0OO0O0000OOOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:377
            OOO0O0O0OO00O00OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O00O000O00OO000 ).json ()#line:378
            if 'status'in OOO0O0O0OO00O00OO :#line:380
                if OOO0O0O0OO00O00OO ['status']==200 :#line:381
                    OOO0OO00O00OO0O0O =OOO0O0O0OO00O00OO ['data'][0 ]['crops']#line:382
                    for O0000O000OOO0OO00 in OOO0OO00O00OO0O0O :#line:383
                        if O0000O000OOO0OO00 ['ill_clover_award']:#line:384
                            if float (O0000O000OOO0OO00 ['ill_clover_award'])>1 :#line:385
                                if O0000O000OOO0OO00 ['is_finish']:#line:386
                                    if not O0000O000OOO0OO00 ['is_getit']:#line:387
                                        if O0OOO000000O0O000 .certification ()!='未实名':#line:388
                                            O0OO0O0000OOOO000 =f'_award_level={O0000O000OOO0OO00["level"]}_{timi_new()}'#line:389
                                            O0O00O000O00OO000 ={'authorization':O0OOO000000O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0000OOOO000 ),'signstring':O0OO0O0000OOOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:398
                                            OOO0O00000OO000OO ={"award_level":O0000O000OOO0OO00 ['level']}#line:399
                                            O00OOOOOOO00O00OO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O00O000O00OO000 ,json =OOO0O00000OO000OO ).json ()#line:401
                                            if 'status'in O00OOOOOOO00O00OO :#line:402
                                                if O00OOOOOOO00O00OO ['status']==200 :#line:403
                                                    O0000OO000OOO000O =O00OOOOOOO00O00OO ['data']['ill_clover_award']#line:404
                                                    print (f'【图鉴奖励】:领取{O0000O000OOO0OO00["crop_name"]}成就丨奖励{O0000OO000OOO000O}叶子成功')#line:406
                                                if O00OOOOOOO00O00OO ['status']==500 :#line:407
                                                    print (f'【图鉴奖励】:{O00OOOOOOO00O00OO["message"]}')#line:408
        except Exception as OO00000O0000O00OO :#line:409
            print (OO00000O0000O00OO )#line:410
    def watched_ad (OOO000OOOO000OO0O ):#line:413
        try :#line:414
            O0O00O0OO0OOOO0OO =f'__{timi_new()}'#line:415
            OO0O00OO0O00000O0 ={'authorization':OOO000OOOO000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OO0OOOO0OO ),'signstring':O0O00O0OO0OOOO0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:424
            O0000OOOO0000O0OO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00OO0O00000O0 ).json ()#line:425
            if 'status'in O0000OOOO0000O0OO :#line:427
                if O0000OOOO0000O0OO ['status']==200 :#line:428
                    if 'offlineInfo'in O0000OOOO0000O0OO ['data']:#line:429
                        OO00O0000OOOO0000 =O0000OOOO0000O0OO ['data']['offlineInfo']['off_minute']#line:430
                        O00O0O00000O0O0OO =float (O0000OOOO0000O0OO ['data']['silver'])/1000000000000 #line:431
                        time .sleep (1 )#line:432
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0O00OO0O00000O0 ).json ()#line:433
                        time .sleep (2 )#line:434
                        OOOO0O000O0OOOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00OO0O00000O0 ).json ()#line:435
                        if 'status'in OOOO0O000O0OOOOO0 :#line:437
                            if OOOO0O000O0OOOOO0 ['status']==200 :#line:438
                                OOO0000OO0OOO0OO0 =float (OOOO0O000O0OOOOO0 ['data']['silver'])/1000000000000 #line:439
                                OOOOOO0O0OO00OO00 =str (OOO0000OO0OOO0OO0 -O00O0O00000O0O0OO )[:6 ]#line:440
                                print (f'【离线奖励】:翻倍离线{OO00O0000OOOO0000}分钟奖励种子数量:{OOOOOO0O0OO00OO00}t粒')#line:441
        except Exception as OO00OOOO0O00O0OOO :#line:442
            print (OO00OOOO0O00O0OOO )#line:443
    def user_ad (OO0O0O0O000O00OOO ):#line:446
        try :#line:447
            O0000000O0000OO00 =f'__{timi_new()}'#line:448
            OOOO0O000O000O0OO ={'authorization':OO0O0O0O000O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000000O0000OO00 ),'signstring':O0000000O0000OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:457
            O0OOO0OO0OOO0O000 =requests .request ('get',f'{host}/user/ad',headers =OOOO0O000O000O0OO ).json ()#line:458
            if 'status'in O0OOO0OO0OOO0O000 :#line:460
                if O0OOO0OO0OOO0O000 ['status']==200 :#line:461
                    OO000O0000OO00OOO =O0OOO0OO0OOO0O000 ['data']['max_time']#line:462
                    OOO0O0O00O0O0O0OO =O0OOO0OO0OOO0O000 ['data']['watch_time']#line:463
                    O0O00O0OO000OOOOO =O0OOO0OO0OOO0O000 ['data']['added_time']#line:464
                    print (f'【获取种子】:获取种子剩余{O0O00O0OO000OOOOO + OO000O0000OO00OOO - OOO0O0O00O0O0O0OO}次丨好友提供:{O0O00O0OO000OOOOO}次')#line:465
                    if O0O00O0OO000OOOOO +OO000O0000OO00OOO -OOO0O0O00O0O0O0OO >0 :#line:466
                        time .sleep (random .randint (16 ,19 ))#line:467
                        O00OO0O0OO000O000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOOO0O000O000O0OO ).json ()#line:468
                        if 'status'in O00OO0O0OO000O000 :#line:470
                            if O00OO0O0OO000O000 ['status']==200 :#line:471
                                OO0O00000O0OOOO00 =O00OO0O0OO000O000 ['data']['silver']#line:472
                                print (f'【获取种子】:获得种子:{OO0O00000O0OOOO00}')#line:473
                                return True #line:474
                            if O00OO0O0OO000O000 ['status']==500 :#line:475
                                O00OO0O0OOO0OOOO0 =O00OO0O0OO000O000 ['message']#line:476
                                print (f'【获取种子】:{O00OO0O0OOO0OOOO0}')#line:477
                                return False #line:478
        except Exception as OOOOOOO000O0000O0 :#line:479
            print (OOOOOOO000O0000O0 )#line:480
    def synthetic (O0O0O000OOOOO0O00 ):#line:483
        global id ,g #line:484
        try :#line:485
            OO00O0O0O0OO0OO0O =O0O0O000OOOOO0O00 .level_new ()#line:486
            OOOOO0OOOO0OO00OO =random .randint (9 ,11 )#line:487
            OOOOOOOO0OOO0O000 =f'_site=8&targetSite={OOOOO0OOOO0OO00OO}_{timi_new()}'#line:488
            OOOO00O0000O0OO00 ={'accept':'application/json, text/plain, */*','authorization':O0O0O000OOOOO0O00 .token ,'timestamp':timi_new (),'sign':sign (OOOOOOOO0OOO0O000 ),'signstring':OOOOOOOO0OOO0O000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:503
            OOO000000O0OO00O0 ={"site":int (8 ),"targetSite":int (OOOOO0OOOO0OO00OO )}#line:504
            requests .request ('post',f'{host}/game/crops/move',headers =OOOO00O0000O0OO00 ,json =OOO000000O0OO00O0 )#line:505
            while True :#line:506
                O0OOOOO00000OO0O0 =f'__{timi_new()}'#line:507
                O0O0OO00O00O00000 ={'authorization':O0O0O000OOOOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO00000OO0O0 ),'signstring':O0OOOOO00000OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:516
                OOO0O00O00OOO0000 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO00O00O00000 ).json ()#line:517
                if 'status'in OOO0O00O00OOO0000 :#line:519
                    if OOO0O00O00OOO0000 ['status']==200 :#line:520
                        OOO00O00O0OOOOO00 =OOO0O00O00OOO0000 ['data']['cropList']#line:521
                        OO0000OO00O0OOOOO =OOO0O00O00OOO0000 ['data']['gameCoreDataDBid']#line:522
                        OOOO00O0OO0O0OO0O =0 #line:523
                        for OOO000OO0O0OO00O0 in OOO00O00O0OOOOO00 :#line:524
                            if not OOO000OO0O0OO00O0 :#line:525
                                OO0OO0O000OO000OO =f'_crop_id={OO0000OO00O0OOOOO}&site={OOOO00O0OO0O0OO0O}_{O0O0O000OOOOO0O00.time}'#line:526
                                OO0O0OOO00O00O00O ={'authorization':O0O0O000OOOOO0O00 .token ,'timestamp':O0O0O000OOOOO0O00 .time ,'sign':sign (OO0OO0O000OO000OO ),'signstring':OO0OO0O000OO000OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:535
                                O0O0OO000O0O00O00 ={"site":OOOO00O0OO0O0OO0O ,"crop_id":OO0000OO00O0OOOOO }#line:536
                                O000O00OOO000OOOO =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O0OOO00O00O00O ,data =O0O0OO000O0O00O00 ).json ()#line:537
                                time .sleep (random .randint (1 ,3 )/10 )#line:539
                                if 'status'in O000O00OOO000OOOO :#line:540
                                    if O000O00OOO000OOOO ['status']==200 :#line:541
                                        if O000O00OOO000OOOO ['message']=='种子数量不足':#line:542
                                            OO00O0O0O0OO0OO0O =O0O0O000OOOOO0O00 .level_new ()#line:543
                                            print (f'【种植合成】:{O000O00OOO000OOOO["message"]}')#line:544
                                            if not O0O0O000OOOOO0O00 .user_ad ():#line:545
                                                return False #line:546
                                    if O000O00OOO000OOOO ['status']==500 :#line:547
                                        print (f'【种植合成】:{O000O00OOO000OOOO["message"]}')#line:548
                                        return False #line:549
                            OOOO00O0OO0O0OO0O +=1 #line:550
                        O00O000O0O0OO00OO =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO00O00O00000 ).json ()#line:551
                        OO0000OOO00O00OOO =O00O000O0O0OO00OO ['data']['cropList']#line:552
                        OO000000OO0O00O0O =False #line:553
                        for OOO000OO0O0OO00O0 in range (12 ):#line:554
                            id =OO0000OOO00O00OOO [OOO000OO0O0OO00O0 ]['level']#line:555
                            if float (OO00O0O0O0OO0OO0O )-float (id )>9 :#line:556
                                O0OOOO0O0OO0O000O =f'_site={OOO000OO0O0OO00O0}_{timi_new()}'#line:557
                                OOO0O0000OO0OOOOO ={'accept':'application/json, text/plain, */*','authorization':O0O0O000OOOOO0O00 .token ,'timestamp':timi_new (),'sign':sign (O0OOOO0O0OO0O000O ),'signstring':O0OOOO0O0OO0O000O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:567
                                OOOOO0O000O0O0O0O ={"site":OOO000OO0O0OO00O0 }#line:568
                                OO00OO0000OOO0O00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO0O0000OO0OOOOO ,data =OOOOO0O000O0O0O0O ).json ()#line:570
                                if 'status'in OO00OO0000OOO0O00 :#line:571
                                    if OO00OO0000OOO0O00 ['status']==200 :#line:572
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:573
                            if id !=0 :#line:574
                                for OO0OOOO0OOO00OO0O in range (11 ):#line:575
                                    O0OO00OOO0000OOOO =OO0OOOO0OOO00OO0O +1 #line:576
                                    g =OO0000OOO00O00OOO [O0OO00OOO0000OOOO ]['level']#line:577
                                    if id ==g :#line:578
                                        O00OO0O00O000OO0O =OO0OOOO0OOO00OO0O +2 #line:579
                                        if O00OO0O00O000OO0O !=OOO000OO0O0OO00O0 +1 :#line:580
                                            O000OO0OO0O000OO0 =OOO000OO0O0OO00O0 +1 #line:581
                                            time .sleep (random .randint (1 ,3 )/10 )#line:583
                                            OOOOOOOO0OOO0O000 =f'_site={O000OO0OO0O000OO0 - 1}&targetSite={O00OO0O00O000OO0O - 1}_{timi_new()}'#line:584
                                            OOOO00O0000O0OO00 ={'accept':'application/json, text/plain, */*','authorization':O0O0O000OOOOO0O00 .token ,'timestamp':timi_new (),'sign':sign (OOOOOOOO0OOO0O000 ),'signstring':OOOOOOOO0OOO0O000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:599
                                            OOOOO00O00O0O00O0 ={"site":int (O000OO0OO0O000OO0 -1 ),"targetSite":int (O00OO0O00O000OO0O -1 )}#line:600
                                            O000OOOO00O000OOO =requests .request ('post',f'{host}/game/crops/move',headers =OOOO00O0000O0OO00 ,json =OOOOO00O00O0O00O0 ).json ()#line:602
                                            if 'status'in O000OOOO00O000OOO :#line:603
                                                if O000OOOO00O000OOO ['status']==200 :#line:604
                                                    pass #line:605
                                            print ('【种植合成】:',O000OO0OO0O000OO0 ,O00OO0O00O000OO0O ,'合成成功')#line:607
                                            OO000000OO0O00O0O =True #line:608
                                    if OO000000OO0O00O0O :#line:609
                                        break #line:610
                                if OO000000OO0O00O0O :#line:611
                                    break #line:612
        except Exception as OO0O00OO00O00OO00 :#line:613
            O0O0O000OOOOO0O00 .synthetic ()#line:614
    def level_new (OOO000O000OO00O00 ):#line:617
        try :#line:618
            O00O0OOO0O0OOOO0O =f'__{timi_new()}'#line:619
            OO00O00O00O00O0O0 ={'authorization':OOO000O000OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO0O0OOOO0O ),'signstring':O00O0OOO0O0OOOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:628
            O00O000O0OOO0OO00 =requests .request ('get',f'{host}/user',headers =OO00O00O00O00O0O0 ).json ()#line:629
            if 'status'in O00O000O0OOO0OO00 :#line:630
                if O00O000O0OOO0OO00 ['status']==200 :#line:631
                    return float (O00O000O0OOO0OO00 ['data']['level'])#line:632
        except Exception as OO0OOOO00O0OO000O :#line:633
            print (OO0OOOO00O0OO000O )#line:634
    def propsraffle (O00O0OO0O0OO000O0 ):#line:637
        try :#line:638
            while True :#line:639
                OOO0OOO0OOOOOOOOO =f'__{timi_new()}'#line:640
                O00O000O0OO0O00OO ={'authorization':O00O0OO0O0OO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OOOOOOOOO ),'signstring':OOO0OOO0OOOOOOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:649
                OOOO0O0O0O0000O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00O000O0OO0O00OO ).json ()#line:650
                if 'status'in OOOO0O0O0O0000O0O :#line:652
                    if OOOO0O0O0O0000O0O ['status']==200 :#line:653
                        O0OOO000O00OO0O00 =OOOO0O0O0O0000O0O ['data']['rows']#line:654
                        O0OOO0OOOO0000OOO =OOOO0O0O0O0000O0O ['data']['vstate']#line:655
                        if O0OOO000O00OO0O00 ==5 or O0OOO000O00OO0O00 ==6 or O0OOO000O00OO0O00 ==7 :#line:656
                            O00O0O000O00OOO00 =OOOO0O0O0O0000O0O ['data']['silver']#line:657
                            print (f'【转盘抽奖】:获得种子:{O00O0O000O00OOO00}')#line:658
                        if O0OOO000O00OO0O00 ==1 or O0OOO000O00OO0O00 ==2 or O0OOO000O00OO0O00 ==3 :#line:659
                            O0O00O00O000OOO00 =OOOO0O0O0O0000O0O ['data']['clover']#line:660
                            print (f'【转盘抽奖】:获得三叶草:{O0O00O00O000OOO00}')#line:661
                        if O0OOO000O00OO0O00 ==4 or O0OOO000O00OO0O00 ==8 :#line:662
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:663
                        if O0OOO000O00OO0O00 =='抽奖次数已用完':#line:667
                            break #line:700
                time .sleep (random .randint (8 ,15 )/10 )#line:701
        except Exception as OO00O0OOOO00OO000 :#line:702
            print (OO00O0OOOO00OO000 )#line:703
    def friends_invitation (O0OO0O0OOO00O00OO ):#line:706
        try :#line:707
            O00OO0000OO0O00O0 =f'__{timi_new()}'#line:708
            O00O0O0O00OOO0O0O ={'authorization':O0OO0O0OOO00O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0000OO0O00O0 ),'signstring':O00OO0000OO0O00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:717
            O00OO0O00O000O00O =requests .request ('get',f'{host}/friends',headers =O00O0O0O00OOO0O0O ).json ()#line:718
            if 'status'in O00OO0O00O000O00O :#line:719
                if O00OO0O00O000O00O ['status']==200 :#line:720
                    OOOOOOO000OOO0O0O =O00OO0O00O000O00O ['data']['myInviteter']#line:721
                    if OOOOOOO000OOO0O0O :#line:722
                        O00OO0OOOOOOOOOO0 =OOOOOOO000OOO0O0O ['user']['nickname']#line:723
                        O0OOOO0OOOO00OOO0 =O0OO0O0OOO00O00OO .certification ()#line:724
                        print (f'【查邀请人】:我的邀请人:{O00OO0OOOOOOOOOO0}丨实名:{O0OOOO0OOOO00OOO0}')#line:725
                    else :#line:726
                        if O0OO0O0OOO00O00OO .innerId !='0':#line:727
                            O0OO0O0OOO00O00OO .invitation ()#line:728
        except Exception as O000OO0O0O00O0OO0 :#line:729
            print (O000OO0O0O00O0OO0 )#line:730
    def add_clover (OOOO0OO000O00OOOO ):#line:733
        global golden_seed #line:734
        try :#line:735
            OO00OOOO0OO0000OO =f'__{timi_new()}'#line:736
            O0O00OOO00OOOO0O0 ={'authorization':OOOO0OO000O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOO0OO0000OO ),'signstring':OO00OOOO0OO0000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:745
            O0O0O00OOOOO00OOO =requests .request ('get',f'{host}/assets/clovers',headers =O0O00OOO00OOOO0O0 ).json ()#line:746
            if 'status'in O0O0O00OOOOO00OOO :#line:748
                if O0O0O00OOOOO00OOO ['status']==200 :#line:749
                    O00OO000O000OO000 =O0O0O00OOOOO00OOO ['data']['clover']#line:750
                    O0OO0O0O00O000000 =O0O0O00OOOOO00OOO ['data']['used_clover']#line:751
                    O0OO0O00O000O0O00 =float (O00OO000O000OO000 )-float (O0OO0O0O00O000000 )#line:752
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0OO0O0O00O000000}')#line:753
                    if OOOO0OO000O00OOOO .certification ()!='未实名':#line:754
                        if O0OO0O00O000O0O00 >1 :#line:755
                            OO00OOOO0OO0000OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OO0O00O000O0O00)}_{timi_new()}'#line:756
                            OOOOO00000OO000OO ={'authorization':OOOO0OO000O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOO0OO0000OO ),'signstring':OO00OOOO0OO0000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:765
                            O0OOO0O0O00O0000O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OO0O00O000O0O00 )}#line:766
                            O0000OOOOO0OOO00O =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOOO00000OO000OO ,data =O0OOO0O0O00O0000O ).json ()#line:767
                            if 'status'in O0000OOOOO0OOO00O :#line:769
                                if O0000OOOOO0OOO00O ['status']==200 :#line:770
                                    print (f'【参与抽奖】:添加三叶草:{O0000OOOOO0OOO00O["data"]}丨数量:{O0OO0O00O000O0O00}')#line:771
                                if O0000OOOOO0OOO00O ['status']==500 :#line:772
                                    print (f'【参与抽奖】:添加三叶草:{O0000OOOOO0OOO00O["message"]}')#line:773
            OO000OO0000OOOOOO =requests .request ('get',f'{host}/lottery',headers =O0O00OOO00OOOO0O0 ).json ()#line:774
            OOO00O0OO0O0OO000 =OOOO0OO000O00OOOO .winning_rewards ()#line:776
            if 'status'in OO000OO0000OOOOOO :#line:777
                if OO000OO0000OOOOOO ['status']==200 :#line:778
                    O00O000OOO00OO0OO =OO000OO0000OOOOOO ['data'][0 ]['day_get_gold_quantity']#line:779
                    golden_seed +=float (O00O000OOO00OO0OO )#line:780
                    print (f'【参与抽奖】:预计每天中{str(O00O000OOO00OO0OO)[:6]}颗金种子丨好友收益:{str(OOO00O0OO0O0OO000)[:6]}')#line:781
        except Exception as OO000000O0OO00000 :#line:782
            print (OO000000O0OO00000 )#line:783
    def energy (OO0000O0OOOOO00OO ):#line:787
        try :#line:788
            while True :#line:789
                OO0OO0000O0O00O0O =f'__{timi_new()}'#line:790
                O0O000OO0OO0OOOO0 ={'authorization':OO0000O0OOOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0000O0O00O0O ),'signstring':OO0OO0000O0O00O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:799
                O0000OO000OOOOO00 =requests .request ('get',f'{host}/energy/general',headers =O0O000OO0OO0OOOO0 ).json ()#line:800
                if 'status'in O0000OO000OOOOO00 :#line:802
                    if O0000OO000OOOOO00 ['status']==200 :#line:803
                        OO00OO0O0O0OOO000 =O0000OO000OOOOO00 ['data']['ordinary_water']#line:804
                        OOOOOO0O0O00O0O0O =O0000OO000OOOOO00 ['data']['ordinary_fertilizer']#line:805
                        print (f'【我的营养】:肥料:{str(OOOOOO0O0O00O0O0O).split(".")[0]}丨水滴:{str(OO00OO0O0O0OOO000).split(".")[0]}')#line:807
                        if float (OOOOOO0O0O00O0O0O )<96 :#line:808
                            time .sleep (random .randint (160 ,180 )/10 )#line:809
                            OO00OO0O0O0O0000O =99 -float (OOOOOO0O0O00O0O0O )#line:810
                            OO0000O000O000OO0 ={"fertilizer":str (OO00OO0O0O0O0000O ).split ('.')[0 ]}#line:811
                            O0OO00O0OO0000O00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0O000OO0OO0OOOO0 ).json ()#line:812
                            if 'status'in O0OO00O0OO0000O00 :#line:814
                                if O0OO00O0OO0000O00 ['status']==200 :#line:815
                                    print (f'【购买肥料】:看广告获取肥料:{O0OO00O0OO0000O00["message"]}')#line:816
                        if float (OO00OO0O0O0OOO000 )<880 :#line:817
                            time .sleep (random .randint (160 ,180 )/10 )#line:818
                            O0O000000OOOO00OO =999 -float (OO00OO0O0O0OOO000 )#line:819
                            OOO00000OOO0O0O00 ={"water":str (O0O000000OOOO00OO ).split ('.')[0 ]}#line:820
                            O00000O0OO0O0O0OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0O000OO0OO0OOOO0 ).json ()#line:821
                            if 'status'in O00000O0OO0O0O0OO :#line:823
                                if O00000O0OO0O0O0OO ['status']==200 :#line:824
                                    print (f'【购买水滴】:看广告获取水滴:{O00000O0OO0O0O0OO["message"]}')#line:825
                        if float (OOOOOO0O0O00O0O0O )>96 and float (OO00OO0O0O0OOO000 )>880 :#line:826
                            break #line:827
        except Exception as O0O00OOO00O00O0O0 :#line:829
            print (O0O00OOO00O00O0O0 )#line:830
def bundled_def ():#line:832
    OOO0O0OOOO00O0000 =['5570536','7750212','7911652','7911680','7805624']#line:833
    return OOO0O0OOOO00O0000 [random .randint (0 ,len (OOO0O0OOOO00O0000 )-1 )]#line:834
def version_of_the_validation ():#line:838
    return str ((76 -56 )/10 )#line:839
def gitee_validation ():#line:842
    try :#line:843
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:844
    except :#line:845
        sys .exit (0 )#line:846
def update_the_validation ():#line:850
    try :#line:851
        O0O0O000OOO0O0000 =gitee_validation ()#line:852
        if version_of_the_validation ()<O0O0O000OOO0O0000 ['CityEarth']['edition']:#line:853
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0O000OOO0O0000["CityEarth"]["edition"]}   ❌')#line:854
            print (f'更新内容=>>{O0O0O000OOO0O0000["CityEarth"]["content"]}   👍')#line:855
        else :#line:856
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0O000OOO0O0000["CityEarth"]["edition"]}   ✅')#line:857
            print (f'更新内容=>> {O0O0O000OOO0O0000["CityEarth"]["content"]}   👍')#line:858
    except Exception as O00000O0O0OOOO00O :#line:859
        print (O00000O0O0OOOO00O )#line:860
def os_qinglong ():#line:863
    if application in os .environ :#line:864
        O0OOOO000O0000O0O =os .environ [application ].split ('\n')#line:865
        if len (O0OOOO000O0000O0O )>0 :#line:866
            return O0OOOO000O0000O0O #line:867
        else :#line:868
            print (f"{application}变量未启用")#line:869
            print ('脚本退出')#line:870
            sys .exit (1 )#line:871
    else :#line:872
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:874
        return os_built ()#line:875
def os_built ():#line:878
    if token :#line:879
        O0OOO0OO0O0000OO0 =token .split ('\n')#line:880
        if len (O0OOO0OO0O0000OO0 )>0 :#line:881
            return O0OOO0OO0O0000OO0 #line:882
    else :#line:883
        print (f"内置变量为空")#line:884
        print ('脚本结束')#line:885
        sys .exit (0 )#line:886
if __name__ =='__main__':#line:889
    start ()#line:890
