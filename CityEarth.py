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
        O0000O00OOOO0O0O0 =os_qinglong ()#line:10
        print (f"==========共找到{len(O0000O00OOOO0O0O0)}个账号==========")#line:11
        for O000000000O00O000 in O0000O00OOOO0O0O0 :#line:12
            O0O00OO0OOO0OO00O =[]#line:13
            print (f"------------正在执行第{O0000O00OOOO0O0O0.index(O000000000O00O000) + 1}个账号------------")#line:14
            O0O00000OO000O000 =CityEarth (O000000000O00O000 ,O0O00OO0OOO0OO00O )#line:15
            def OOO00O00OOO00OO0O ():#line:17
                if O0O00000OO000O000 .base_info ():#line:19
                    O0O00000OO000O000 .sealing ()#line:21
                    O0O00000OO000O000 .invitenum ()#line:23
                    O0O00000OO000O000 .game_map ()#line:25
                    O0O00000OO000O000 .friends_invitation ()#line:27
                    O0O00000OO000O000 .add_clover ()#line:29
                    O0O00000OO000O000 .energy ()#line:31
                    O0O00000OO000O000 .propsraffle ()#line:33
                    O0O00000OO000O000 .synthetic ()#line:35
                    O0O00000OO000O000 .crops_illustrated ()#line:37
                    O0O00000OO000O000 .give_gold ()#line:39
                    O0O00000OO000O000 .withdraw ()#line:41
            OOO000OOOOO0OO000 =threading .Thread (target =OOO00O00OOO00OO0O )#line:43
            OOO000OOOOO0OO000 .start ()#line:44
            time .sleep (time_xx )#line:45
        print (f"------------正在处理推送通知------------")#line:46
        time .sleep (3 )#line:47
        O0O0O00OO000OO0O0 =format_msg ()#line:48
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O0O00OO000OO0O0 +' ')#line:49
    except Exception as OOOO0O0OOO0O00O00 :#line:50
        print (OOOO0O0OOO0O00O00 )#line:51
def sign (O00OO0O0OO0OO0000 ):#line:54
    O0O0O000O0OO0O0O0 =hashlib .md5 (O00OO0O0OO0OO0000 .encode ()).hexdigest ()#line:55
    OOOOO0000OO0OO00O ="scsc%^&*"+O0O0O000O0OO0O0O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:56
    OOO0OO0OOOO00000O =hashlib .md5 (OOOOO0000OO0OO00O .encode ()).hexdigest ()#line:57
    return OOO0OO0OOOO00000O #line:58
def format_msg ():#line:60
    O00O0OOO0O00000O0 =""#line:61
    for O0O00O000000OOOO0 in msg_list :#line:62
        O00O0OOO0O00000O0 +=str (O0O00O000000OOOO0 )+"\r\n"#line:63
    return O00O0OOO0O00000O0 #line:64
def timi_new ():#line:66
    return str (int (time .time ()*1000 ))#line:67
class CityEarth :#line:70
    def __init__ (OOO0O00OOOO0O00OO ,O00000OO00O00OO00 ,OO0O0OOO0OOO00O00 ):#line:72
        try :#line:73
            OOO0O00OOOO0O00OO .msg =OO0O0OOO0OOO00O00 #line:74
            OOO0O00OOOO0O00OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:75
            OOO0O00OOOO0O00OO .token =O00000OO00O00OO00 .split ('&')[0 ]#line:76
            OOO0O00OOOO0O00OO .innerId =O00000OO00O00OO00 .split ('&')[1 ]#line:77
            OOO0O00OOOO0O00OO .doneeNo =O00000OO00O00OO00 .split ('&')[2 ]#line:78
        except :#line:79
            print ('变量格式错误')#line:80
    def base_info (O00O0000O0000000O ):#line:83
        try :#line:84
            O00O0000O0000000O .watched_ad ()#line:86
            OOO00OOOO0O0OOOOO =f'__{timi_new()}'#line:87
            OO00OOO0O00O0OO0O ={'authorization':O00O0000O0000000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOOO0O0OOOOO ),'signstring':OOO00OOOO0O0OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:96
            OOOOOO00O0OO00OOO =requests .request ('get',f'{host}/user',headers =OO00OOO0O00O0OO0O ).json ()#line:97
            if 'status'in OOOOOO00O0OO00OOO :#line:99
                if OOOOOO00O0OO00OOO ['status']==200 :#line:100
                    OO0O00OOO000OOOO0 =OOOOOO00O0OO00OOO ['data']['nickname']#line:101
                    O0OOOO00000OO000O =OOOOOO00O0OO00OOO ['data']['inner_id']#line:102
                    O0O0O00O0OO0OO0OO =OOOOOO00O0OO00OOO ['data']['assets']['gold']#line:103
                    O00OO0000O00000OO =OOOOOO00O0OO00OOO ['data']['level']#line:104
                    print (f'【账号信息】:昵称:{OO0O00OOO000OOOO0[:5]}丨ID:{O0OOOO00000OO000O}丨等级:{O00OO0000O00000OO}丨种子:{str(O0O0O00O0OO0OO0OO).split(".")[0]}')#line:106
                    if change_nickname :#line:107
                        O00O0000O0000000O .change_nickname (O0OOOO00000OO000O )#line:109
                if OOOOOO00O0OO00OOO ['status']==401 :#line:110
                    print (OOOOOO00O0OO00OOO ['message'])#line:111
                    O00O0000O0000000O .msg .append ('有账号失效了')#line:112
                    return False #line:113
                if OOOOOO00O0OO00OOO ['status']==500 :#line:114
                    return False #line:115
            return True #line:116
        except Exception as OO0OO00OOO0O0OOOO :#line:117
            print (OO0OO00OOO0O0OOOO )#line:118
    def sealing (O0OOO0OO000OOO00O ):#line:121
        try :#line:122
            O0000000OOOOOOO00 =f'__{timi_new()}'#line:123
            OOOOOOOOOO0OOOO00 ={'authorization':O0OOO0OO000OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000000OOOOOOO00 ),'signstring':O0000000OOOOOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:132
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOOOOOOOO0OOOO00 )#line:133
            requests .request ('get',f'{host}/packsack/list',headers =OOOOOOOOOO0OOOO00 )#line:134
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOOOOOOOO0OOOO00 )#line:135
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOOOOOOOO0OOOO00 )#line:136
            requests .request ('get',f'{host}/user',headers =OOOOOOOOOO0OOOO00 )#line:137
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOOOOOOOO0OOOO00 )#line:138
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOOOOOOOO0OOOO00 )#line:139
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOOOOOOOO0OOOO00 )#line:140
            requests .request ('get',f'{host}/game/getAllData',headers =OOOOOOOOOO0OOOO00 )#line:141
            requests .request ('get',f'{host}/assets',headers =OOOOOOOOOO0OOOO00 )#line:142
        except Exception as OO00000OOOOO000OO :#line:143
            print (OO00000OOOOO000OO )#line:144
    def change_nickname (O00OOO0OOOOOO0OOO ,OO000O000OO000OO0 ):#line:147
        try :#line:148
            OOOO0O0OOOO0O0OOO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:149
            OO00OOOO000OO0O0O =requests .request ('post','https://www.qmsjmfb.com/',data =OOOO0O0OOOO0O0OOO ).text #line:150
            OO0OO00000O00O000 =re .findall ('<ul><li>(.*?)</li>',OO00OOOO000OO0O0O )[0 ][:3 ]+str (OO000O000OO000OO0 )[5 :]#line:151
            O000OOO0OO00O00O0 =f'_nickname=_{timi_new()}'#line:152
            OO00000O00O0OO0O0 ={'authorization':O00OOO0OOOOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0OO00O00O0 ),'signstring':O000OOO0OO00O00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:161
            O0OO0OO00O0OO0000 ={"nickname":OO0OO00000O00O000 }#line:162
            O000O0OO00O00OOOO =requests .patch (f'{host}/user/nickname',headers =OO00000O00O0OO0O0 ,json =O0OO0OO00O0OO0000 ).json ()#line:163
            print (O000O0OO00O00OOOO )#line:164
        except Exception as OO000OOO00OO000OO :#line:166
            print (OO000OOO00OO000OO )#line:167
    def withdraw (OO00OO0O0O0000O00 ):#line:170
        O0OO00OO0O0OOOOO0 =f'__{timi_new()}'#line:171
        OO0OO000OOO0OOO0O ={'authorization':OO00OO0O0O0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO0O0OOOOO0 ),'signstring':O0OO00OO0O0OOOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:180
        OOOOOO0000OOOOOO0 =requests .request ('get',f'{host}/assets',headers =OO0OO000OOO0OOO0O ).json ()#line:181
        if 'status'in OOOOOO0000OOOOOO0 :#line:183
            if OOOOOO0000OOOOOO0 ['status']==200 :#line:184
                O000OOO000O0O0O0O =OOOOOO0000OOOOOO0 ['data']['cash']#line:185
                if float (O000OOO000O0O0O0O )>20 :#line:186
                    O0OO00OO0O0OOOOO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:187
                    OO0OO000OOO0OOO0O ={'authorization':OO00OO0O0O0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO0O0OOOOO0 ),'signstring':O0OO00OO0O0OOOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:196
                    O0000000OOO00OOO0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:197
                    O00OO00O0OO0OOO00 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO0OO000OOO0OOO0O ,data =O0000000OOO00OOO0 ).json ()#line:199
                    print (O00OO00O0OO0OOO00 )#line:200
    def invitenum (O00O00O00OO00000O ):#line:203
        O0OO00O0O0000OOOO =f'__{timi_new()}'#line:204
        O00OO0000O0O0OOO0 ={'authorization':O00O00O00OO00000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0O0000OOOO ),'signstring':O0OO00O0O0000OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:213
        OOOO0O0O0OOO000O0 =requests .request ('get',f'{host}/invite/invitenum',headers =O00OO0000O0O0OOO0 ).json ()#line:214
        if 'status'in OOOO0O0O0OOO000O0 :#line:216
            if OOOO0O0O0OOO000O0 ['status']==200 :#line:217
                OO00O000O000000O0 =OOOO0O0O0OOO000O0 ['data']['invited_count']#line:218
                O00OO0OO0OO0O0OO0 =OOOO0O0O0OOO000O0 ['data']['invited_second_count']#line:219
                print (f'【我的邀请】:直邀好友:{OO00O000O000000O0}丨间邀好友:{O00OO0OO0OO0O0OO0}')#line:220
    def game_map (O00OOOOO000O00OO0 ):#line:223
        try :#line:224
            O00O0OO00OOOOO000 =f'__{timi_new()}'#line:225
            OOOO00OO00O0O00O0 ={'authorization':O00OOOOO000O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO00OOOOO000 ),'signstring':O00O0OO00OOOOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:234
            OO0000O0OO0OO0O00 =requests .request ('get',f'{host}/game/map',headers =OOOO00OO00O0O00O0 ).json ()#line:235
            if 'status'in OO0000O0OO0OO0O00 :#line:237
                if OO0000O0OO0OO0O00 ['status']==200 :#line:238
                    for O0O000000OO0O0000 in OO0000O0OO0OO0O00 ['data']['list'][0 ]['crops']:#line:239
                        OOO0000OO0O0000OO =O0O000000OO0O0000 ['level']#line:241
                        if OOO0000OO0O0000OO ==41 :#line:242
                            O0O0OO0O0O0OO0O00 =O0O000000OO0O0000 ['crop_name']#line:243
                            O00000OOO000OO00O =O0O000000OO0O0000 ['count']#line:244
                            if O00000OOO000OO00O >0 :#line:245
                                print (f'【农业资产】:{O0O0OO0O0O0OO0O00}丨数量:{O00000OOO000OO00O}')#line:246
        except Exception as O000000O00O0O0O0O :#line:247
            print (O000000O00O0O0O0O )#line:248
    def give_gold (O0O0000O000OOO0O0 ):#line:251
        try :#line:252
            OO00O000O0O00O00O =f'__{timi_new()}'#line:253
            O0O0OO0O0O00OO0O0 ={'authorization':O0O0000O000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000O0O00O00O ),'signstring':OO00O000O0O00O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:262
            OO0OOOOO00O000OOO =requests .request ('get',f'{host}/user',headers =O0O0OO0O0O00OO0O0 ).json ()#line:263
            if 'status'in OO0OOOOO00O000OOO :#line:264
                if OO0OOOOO00O000OOO ['status']==200 :#line:265
                    if float (O0O0000O000OOO0O0 .doneeNo )!=0 :#line:266
                        OOO0O0OO00OO0O0O0 =OO0OOOOO00O000OOO ['data']['assets']['gold']#line:267
                        if float (OOO0O0OO00OO0O0O0 )>float (O0O0000O000OOO0O0 .innerId ):#line:268
                            OO0O0O000O000OOO0 =int (float (OOO0O0OO00OO0O0O0 )/1.1 )#line:269
                            OO00O000O0O00O00O =f'_doneeNo={O0O0000O000OOO0O0.doneeNo}&quantity={OO0O0O000O000OOO0}_{timi_new()}'#line:270
                            O0O0OO0O0O00OO0O0 ={'authorization':O0O0000O000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000O0O00O00O ),'signstring':OO00O000O0O00O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:279
                            OOO00O000OOO00OOO ={"quantity":OO0O0O000O000OOO0 ,"doneeNo":O0O0000O000OOO0O0 .doneeNo }#line:283
                            OO000O0O00000O00O =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0OO0O0O00OO0O0 ,data =OOO00O000OOO00OOO ).json ()#line:284
                            if 'status'in OO000O0O00000O00O :#line:286
                                if OO000O0O00000O00O ['status']==200 :#line:287
                                    if OO000O0O00000O00O ['data']:#line:288
                                        print (f'【赠送种子】:赠送{OO0O0O000O000OOO0}种子给{O0O0000O000OOO0O0.doneeNo}成功')#line:289
                    else :#line:290
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:291
        except Exception as O0OOOO0O0OO00OOOO :#line:292
            print (O0OOOO0O0OO00OOOO )#line:293
    def invitation (OO0000000O00OO0O0 ):#line:295
        try :#line:296
            _OOO0OOO0OOOOOO0OO =float (bundled_def ())/4 #line:297
            OO000OOO0O000O0OO =f'_innerId={int(_OOO0OOO0OOOOOO0OO)}_{timi_new()}'#line:298
            O00OOO00000O00O0O ={'authorization':OO0000000O00OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOO0O000O0OO ),'signstring':OO000OOO0O000O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:307
            O0O0OO00000OO0OOO ={"innerId":int (_OOO0OOO0OOOOOO0OO )}#line:308
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00OOO00000O00O0O ,data =O0O0OO00000OO0OOO )#line:309
        except Exception as OO0O0O0O00OO00O00 :#line:310
            print (OO0O0O0O00OO00O00 )#line:311
    def winning_rewards (OOOO0O0O0OOOO0OO0 ):#line:314
        try :#line:315
            OO000O000000O0OO0 =f'__{timi_new()}'#line:316
            O00OO0O00O0O00O0O ={'authorization':OOOO0O0O0OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O000000O0OO0 ),'signstring':OO000O000000O0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:325
            O0000O0O0O000OOOO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00OO0O00O0O00O0O ).json ()#line:326
            if 'status'in O0000O0O0O000OOOO :#line:328
                if O0000O0O0O000OOOO ['status']==200 :#line:329
                    if O0000O0O0O000OOOO ['data']['amount']:#line:330
                        OOO0OOO000O0000OO =O0000O0O0O000OOOO ['data']['amount']['gold']#line:331
                        return OOO0OOO000O0000OO #line:332
                    else :#line:333
                        return 0 #line:334
        except Exception as O0OOOO0O0O0OOOOO0 :#line:335
            print (O0OOOO0O0O0OOOOO0 )#line:336
    def certification (OO0OO0O000OO0OOO0 ):#line:339
        try :#line:340
            O000OO0O0O000OOOO =f'__{timi_new()}'#line:341
            O00O000O0O00000OO ={'authorization':OO0OO0O000OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O0O000OOOO ),'signstring':O000OO0O0O000OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
            OO000OO0O0O0000O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00O000O0O00000OO ).json ()#line:351
            if 'status'in OO000OO0O0O0000O0 :#line:353
                if OO000OO0O0O0000O0 ['status']==200 :#line:354
                    if OO000OO0O0O0000O0 ['data']['result']:#line:355
                        O0OOO00O0O0000OO0 =OO000OO0O0O0000O0 ['data']['nick_name']#line:356
                        return O0OOO00O0O0000OO0 #line:357
                    else :#line:358
                        return '未实名'#line:359
        except Exception as OOO00OOO0O0OO0000 :#line:360
            print (OOO00OOO0O0OO0000 )#line:361
    def crops_illustrated (OOO000OO0OO00OOOO ):#line:364
        try :#line:365
            OOOOO0OOOOOO0OO00 =f'__{timi_new()}'#line:366
            OO0O00O0O0OOOOO0O ={'authorization':OOO000OO0OO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOOOOO0OO00 ),'signstring':OOOOO0OOOOOO0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:375
            OOOO000OOO0O0OOOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O00O0O0OOOOO0O ).json ()#line:376
            if 'status'in OOOO000OOO0O0OOOO :#line:378
                if OOOO000OOO0O0OOOO ['status']==200 :#line:379
                    O00000OOO00OO000O =OOOO000OOO0O0OOOO ['data'][0 ]['crops']#line:380
                    for OOOOO00O0OOOOOO00 in O00000OOO00OO000O :#line:381
                        if OOOOO00O0OOOOOO00 ['ill_clover_award']:#line:382
                            if float (OOOOO00O0OOOOOO00 ['ill_clover_award'])>1 :#line:383
                                if OOOOO00O0OOOOOO00 ['is_finish']:#line:384
                                    if not OOOOO00O0OOOOOO00 ['is_getit']:#line:385
                                        if OOO000OO0OO00OOOO .certification ()!='未实名':#line:386
                                            OOOOO0OOOOOO0OO00 =f'_award_level={OOOOO00O0OOOOOO00["level"]}_{timi_new()}'#line:387
                                            OO0O00O0O0OOOOO0O ={'authorization':OOO000OO0OO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOOOOO0OO00 ),'signstring':OOOOO0OOOOOO0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:396
                                            OOO0000OO00OOO0O0 ={"award_level":OOOOO00O0OOOOOO00 ['level']}#line:397
                                            OOO0000OOO0OOOO0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O00O0O0OOOOO0O ,json =OOO0000OO00OOO0O0 ).json ()#line:399
                                            if 'status'in OOO0000OOO0OOOO0O :#line:400
                                                if OOO0000OOO0OOOO0O ['status']==200 :#line:401
                                                    OO000OOO0000OO0O0 =OOO0000OOO0OOOO0O ['data']['ill_clover_award']#line:402
                                                    print (f'【图鉴奖励】:领取{OOOOO00O0OOOOOO00["crop_name"]}成就丨奖励{OO000OOO0000OO0O0}叶子成功')#line:404
                                                if OOO0000OOO0OOOO0O ['status']==500 :#line:405
                                                    print (f'【图鉴奖励】:{OOO0000OOO0OOOO0O["message"]}')#line:406
        except Exception as OO0OO0OO0O0OOOOOO :#line:407
            print (OO0OO0OO0O0OOOOOO )#line:408
    def watched_ad (O0O0O000OOO00OO0O ):#line:411
        try :#line:412
            OOO0O000O00O0O0O0 =f'__{timi_new()}'#line:413
            O0OOOO00OOO0O0OO0 ={'authorization':O0O0O000OOO00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O00O0O0O0 ),'signstring':OOO0O000O00O0O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:422
            OOOO0OO000000O000 =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOO00OOO0O0OO0 ).json ()#line:423
            if 'status'in OOOO0OO000000O000 :#line:425
                if OOOO0OO000000O000 ['status']==200 :#line:426
                    if 'offlineInfo'in OOOO0OO000000O000 ['data']:#line:427
                        OOO0OO0O0000OOOO0 =OOOO0OO000000O000 ['data']['offlineInfo']['off_minute']#line:428
                        OOO0O00O0O00O0OO0 =float (OOOO0OO000000O000 ['data']['silver'])/1000000000000 #line:429
                        time .sleep (1 )#line:430
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0OOOO00OOO0O0OO0 ).json ()#line:431
                        time .sleep (2 )#line:432
                        OO0OO00OO0O0O0000 =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOO00OOO0O0OO0 ).json ()#line:433
                        if 'status'in OO0OO00OO0O0O0000 :#line:435
                            if OO0OO00OO0O0O0000 ['status']==200 :#line:436
                                O0000OO00OO000O0O =float (OO0OO00OO0O0O0000 ['data']['silver'])/1000000000000 #line:437
                                O0OO0O000000OOOO0 =str (O0000OO00OO000O0O -OOO0O00O0O00O0OO0 )[:6 ]#line:438
                                print (f'【离线奖励】:翻倍离线{OOO0OO0O0000OOOO0}分钟奖励种子数量:{O0OO0O000000OOOO0}t粒')#line:439
        except Exception as O0OOOO0OOO000O000 :#line:440
            print (O0OOOO0OOO000O000 )#line:441
    def user_ad (OO0OO000OO0OO0O0O ):#line:444
        try :#line:445
            OOOO0OO000O00000O =f'__{timi_new()}'#line:446
            OOO0OOOOO0OO0O0OO ={'authorization':OO0OO000OO0OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO000O00000O ),'signstring':OOOO0OO000O00000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:455
            OO00OOOOOO0O0OOOO =requests .request ('get',f'{host}/user/ad',headers =OOO0OOOOO0OO0O0OO ).json ()#line:456
            if 'status'in OO00OOOOOO0O0OOOO :#line:458
                if OO00OOOOOO0O0OOOO ['status']==200 :#line:459
                    O0OO00O000O00OOO0 =OO00OOOOOO0O0OOOO ['data']['max_time']#line:460
                    O0O0OO000O0O00O0O =OO00OOOOOO0O0OOOO ['data']['watch_time']#line:461
                    O00O0OO00OOO0OO00 =OO00OOOOOO0O0OOOO ['data']['added_time']#line:462
                    print (f'【获取种子】:获取种子剩余{O00O0OO00OOO0OO00 + O0OO00O000O00OOO0 - O0O0OO000O0O00O0O}次丨好友提供:{O00O0OO00OOO0OO00}次')#line:463
                    if O00O0OO00OOO0OO00 +O0OO00O000O00OOO0 -O0O0OO000O0O00O0O >0 :#line:464
                        time .sleep (random .randint (16 ,19 ))#line:465
                        O00O00O0O0OO0O00O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO0OOOOO0OO0O0OO ).json ()#line:466
                        if 'status'in O00O00O0O0OO0O00O :#line:468
                            if O00O00O0O0OO0O00O ['status']==200 :#line:469
                                OO00OO00O0OO0OO00 =O00O00O0O0OO0O00O ['data']['silver']#line:470
                                print (f'【获取种子】:获得种子:{OO00OO00O0OO0OO00}')#line:471
                                return True #line:472
                            if O00O00O0O0OO0O00O ['status']==500 :#line:473
                                OOOOOO0O0OOO000OO =O00O00O0O0OO0O00O ['message']#line:474
                                print (f'【获取种子】:{OOOOOO0O0OOO000OO}')#line:475
                                return False #line:476
        except Exception as O00O0OO0O0OOOO0O0 :#line:477
            print (O00O0OO0O0OOOO0O0 )#line:478
    def synthetic (O00OO0OOOOO0OOO0O ):#line:481
        global id ,g #line:482
        try :#line:483
            O000OOOOO0O0OOOO0 =O00OO0OOOOO0OOO0O .level_new ()#line:484
            O0OO000OO0OOOO0OO =random .randint (9 ,11 )#line:485
            OOO0OO00OOOOOO00O =f'_site=8&targetSite={O0OO000OO0OOOO0OO}_{timi_new()}'#line:486
            O0OOOOO0O0000OO00 ={'accept':'application/json, text/plain, */*','authorization':O00OO0OOOOO0OOO0O .token ,'timestamp':timi_new (),'sign':sign (OOO0OO00OOOOOO00O ),'signstring':OOO0OO00OOOOOO00O ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:501
            OO0OO000O0OO00OOO ={"site":int (8 ),"targetSite":int (O0OO000OO0OOOO0OO )}#line:502
            requests .request ('post',f'{host}/game/crops/move',headers =O0OOOOO0O0000OO00 ,json =OO0OO000O0OO00OOO )#line:503
            while True :#line:504
                OOO00000O0O0OOOO0 =f'__{timi_new()}'#line:505
                OOOO0O0OOO0OO0OO0 ={'authorization':O00OO0OOOOO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00000O0O0OOOO0 ),'signstring':OOO00000O0O0OOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:514
                OOOO00O000OO0OO00 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0O0OOO0OO0OO0 ).json ()#line:515
                if 'status'in OOOO00O000OO0OO00 :#line:517
                    if OOOO00O000OO0OO00 ['status']==200 :#line:518
                        OOOOOO0000O0O00OO =OOOO00O000OO0OO00 ['data']['cropList']#line:519
                        OO00O00OOO0OOO0OO =OOOO00O000OO0OO00 ['data']['gameCoreDataDBid']#line:520
                        OO0O00OOO00OOO0O0 =0 #line:521
                        for OO0OOOOO000OOOOO0 in OOOOOO0000O0O00OO :#line:522
                            if not OO0OOOOO000OOOOO0 :#line:523
                                O0OO0OOOO0O0OOO00 =f'_crop_id={OO00O00OOO0OOO0OO}&site={OO0O00OOO00OOO0O0}_{O00OO0OOOOO0OOO0O.time}'#line:524
                                OO0O000OO0000O0OO ={'authorization':O00OO0OOOOO0OOO0O .token ,'timestamp':O00OO0OOOOO0OOO0O .time ,'sign':sign (O0OO0OOOO0O0OOO00 ),'signstring':O0OO0OOOO0O0OOO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:533
                                OO00O0O0000O000OO ={"site":OO0O00OOO00OOO0O0 ,"crop_id":OO00O00OOO0OOO0OO }#line:534
                                OOOO00000O0000000 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O000OO0000O0OO ,data =OO00O0O0000O000OO ).json ()#line:535
                                time .sleep (random .randint (1 ,3 )/10 )#line:537
                                if 'status'in OOOO00000O0000000 :#line:538
                                    if OOOO00000O0000000 ['status']==200 :#line:539
                                        if OOOO00000O0000000 ['message']=='种子数量不足':#line:540
                                            O000OOOOO0O0OOOO0 =O00OO0OOOOO0OOO0O .level_new ()#line:541
                                            print (f'【种植合成】:{OOOO00000O0000000["message"]}')#line:542
                                            if not O00OO0OOOOO0OOO0O .user_ad ():#line:543
                                                return False #line:544
                                    if OOOO00000O0000000 ['status']==500 :#line:545
                                        print (f'【种植合成】:{OOOO00000O0000000["message"]}')#line:546
                                        return False #line:547
                            OO0O00OOO00OOO0O0 +=1 #line:548
                        OO0O0O000OOOOOO00 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0O0OOO0OO0OO0 ).json ()#line:549
                        OOO0OO0000OO000O0 =OO0O0O000OOOOOO00 ['data']['cropList']#line:550
                        OOOOOOO000000OOOO =False #line:551
                        for OO0OOOOO000OOOOO0 in range (12 ):#line:552
                            id =OOO0OO0000OO000O0 [OO0OOOOO000OOOOO0 ]['level']#line:553
                            if float (O000OOOOO0O0OOOO0 )-float (id )>9 :#line:554
                                O000OO0000OOO000O =f'_site={OO0OOOOO000OOOOO0}_{timi_new()}'#line:555
                                OOOO000OOOOOOO0OO ={'accept':'application/json, text/plain, */*','authorization':O00OO0OOOOO0OOO0O .token ,'timestamp':timi_new (),'sign':sign (O000OO0000OOO000O ),'signstring':O000OO0000OOO000O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:565
                                OO000OOOO0O000O00 ={"site":OO0OOOOO000OOOOO0 }#line:566
                                O00000OO00OOOOO0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOO000OOOOOOO0OO ,data =OO000OOOO0O000O00 ).json ()#line:568
                                if 'status'in O00000OO00OOOOO0O :#line:569
                                    if O00000OO00OOOOO0O ['status']==200 :#line:570
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:571
                            if id !=0 :#line:572
                                for O00O0OO000O000OOO in range (11 ):#line:573
                                    OOOO0O0O0OOOO0O0O =O00O0OO000O000OOO +1 #line:574
                                    g =OOO0OO0000OO000O0 [OOOO0O0O0OOOO0O0O ]['level']#line:575
                                    if id ==g :#line:576
                                        O0O0OO00OOOO00O0O =O00O0OO000O000OOO +2 #line:577
                                        if O0O0OO00OOOO00O0O !=OO0OOOOO000OOOOO0 +1 :#line:578
                                            OO0OOOO00O00O0000 =OO0OOOOO000OOOOO0 +1 #line:579
                                            time .sleep (random .randint (1 ,3 )/10 )#line:581
                                            OOO0OO00OOOOOO00O =f'_site={OO0OOOO00O00O0000 - 1}&targetSite={O0O0OO00OOOO00O0O - 1}_{timi_new()}'#line:582
                                            O0OOOOO0O0000OO00 ={'accept':'application/json, text/plain, */*','authorization':O00OO0OOOOO0OOO0O .token ,'timestamp':timi_new (),'sign':sign (OOO0OO00OOOOOO00O ),'signstring':OOO0OO00OOOOOO00O ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:597
                                            OO0O00000OOOO00O0 ={"site":int (OO0OOOO00O00O0000 -1 ),"targetSite":int (O0O0OO00OOOO00O0O -1 )}#line:598
                                            OOO000O00OO0O00O0 =requests .request ('post',f'{host}/game/crops/move',headers =O0OOOOO0O0000OO00 ,json =OO0O00000OOOO00O0 ).json ()#line:600
                                            if 'status'in OOO000O00OO0O00O0 :#line:601
                                                if OOO000O00OO0O00O0 ['status']==200 :#line:602
                                                    pass #line:603
                                            print ('【种植合成】:',OO0OOOO00O00O0000 ,O0O0OO00OOOO00O0O ,'合成成功')#line:605
                                            OOOOOOO000000OOOO =True #line:606
                                    if OOOOOOO000000OOOO :#line:607
                                        break #line:608
                                if OOOOOOO000000OOOO :#line:609
                                    break #line:610
        except Exception as O0OOOO0000OOOOO0O :#line:611
            O00OO0OOOOO0OOO0O .synthetic ()#line:612
    def level_new (O00000000O0OO0O0O ):#line:615
        try :#line:616
            O0OO00OOOO000OOO0 =f'__{timi_new()}'#line:617
            OOOOOO00OO000OO0O ={'authorization':O00000000O0OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OOOO000OOO0 ),'signstring':O0OO00OOOO000OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:626
            O0OOOOOO00OO0000O =requests .request ('get',f'{host}/user',headers =OOOOOO00OO000OO0O ).json ()#line:627
            if 'status'in O0OOOOOO00OO0000O :#line:628
                if O0OOOOOO00OO0000O ['status']==200 :#line:629
                    return float (O0OOOOOO00OO0000O ['data']['level'])#line:630
        except Exception as O0OOO0O0OO0000OO0 :#line:631
            print (O0OOO0O0OO0000OO0 )#line:632
    def propsraffle (OO0000OO00OO0000O ):#line:635
        try :#line:636
            while True :#line:637
                O0O00000OOOO00OO0 =f'__{timi_new()}'#line:638
                OOOOO0O000O0O000O ={'authorization':OO0000OO00OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000OOOO00OO0 ),'signstring':O0O00000OOOO00OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:647
                O0O000OOO00O0O0O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOOO0O000O0O000O ).json ()#line:648
                if 'status'in O0O000OOO00O0O0O0 :#line:650
                    if O0O000OOO00O0O0O0 ['status']==200 :#line:651
                        OO0O0OO0OO0O00OOO =O0O000OOO00O0O0O0 ['data']['rows']#line:652
                        OO0O0O0OO00O00000 =O0O000OOO00O0O0O0 ['data']['vstate']#line:653
                        if OO0O0OO0OO0O00OOO ==5 or OO0O0OO0OO0O00OOO ==6 or OO0O0OO0OO0O00OOO ==7 :#line:654
                            O000OOOOOOOOO00OO =O0O000OOO00O0O0O0 ['data']['silver']#line:655
                            print (f'【转盘抽奖】:获得种子:{O000OOOOOOOOO00OO}')#line:656
                        if OO0O0OO0OO0O00OOO ==1 or OO0O0OO0OO0O00OOO ==2 or OO0O0OO0OO0O00OOO ==3 :#line:657
                            OOOOOOOO0O000O000 =O0O000OOO00O0O0O0 ['data']['clover']#line:658
                            print (f'【转盘抽奖】:获得三叶草:{OOOOOOOO0O000O000}')#line:659
                        if OO0O0OO0OO0O00OOO ==4 or OO0O0OO0OO0O00OOO ==8 :#line:660
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:661
                        if OO0O0OO0OO0O00OOO =='抽奖次数已用完':#line:665
                            break #line:698
                time .sleep (random .randint (8 ,15 )/10 )#line:699
        except Exception as O000000OO0OO0000O :#line:700
            print (O000000OO0OO0000O )#line:701
    def friends_invitation (OO000O0000OOOO0OO ):#line:704
        try :#line:705
            O0000OOOO000OO0O0 =f'__{timi_new()}'#line:706
            OOO0OOO0000OO00O0 ={'authorization':OO000O0000OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOO000OO0O0 ),'signstring':O0000OOOO000OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:715
            O0O0O0OOO0O000000 =requests .request ('get',f'{host}/friends',headers =OOO0OOO0000OO00O0 ).json ()#line:716
            if 'status'in O0O0O0OOO0O000000 :#line:717
                if O0O0O0OOO0O000000 ['status']==200 :#line:718
                    OO000O000O0O000O0 =O0O0O0OOO0O000000 ['data']['myInviteter']#line:719
                    if OO000O000O0O000O0 :#line:720
                        O0OOO0OO0OO00O0OO =OO000O000O0O000O0 ['user']['nickname']#line:721
                        O0OO00O0OOOO00O0O =OO000O0000OOOO0OO .certification ()#line:722
                        print (f'【查邀请人】:我的邀请人:{O0OOO0OO0OO00O0OO}丨实名:{O0OO00O0OOOO00O0O}')#line:723
                    else :#line:724
                        if OO000O0000OOOO0OO .innerId !='0':#line:725
                            OO000O0000OOOO0OO .invitation ()#line:726
        except Exception as O00O0O000OO00OO00 :#line:727
            print (O00O0O000OO00OO00 )#line:728
    def add_clover (O0OOOO0OOO0O00OOO ):#line:731
        global golden_seed #line:732
        try :#line:733
            OOOOOOOOO0OO0OO00 =f'__{timi_new()}'#line:734
            O00O0000O0O00O0OO ={'authorization':O0OOOO0OOO0O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOOO0OO0OO00 ),'signstring':OOOOOOOOO0OO0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:743
            OOO0OOO00O000O0OO =requests .request ('get',f'{host}/assets/clovers',headers =O00O0000O0O00O0OO ).json ()#line:744
            if 'status'in OOO0OOO00O000O0OO :#line:746
                if OOO0OOO00O000O0OO ['status']==200 :#line:747
                    O0O0O0OOO00OOO000 =OOO0OOO00O000O0OO ['data']['clover']#line:748
                    OOO000O0O0O0OO00O =OOO0OOO00O000O0OO ['data']['used_clover']#line:749
                    OOO0000O00000000O =float (O0O0O0OOO00OOO000 )-float (OOO000O0O0O0OO00O )#line:750
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OOO000O0O0O0OO00O}')#line:751
                    if O0OOOO0OOO0O00OOO .certification ()!='未实名':#line:752
                        if OOO0000O00000000O >1 :#line:753
                            OOOOOOOOO0OO0OO00 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO0000O00000000O)}_{timi_new()}'#line:754
                            OOOO0O0OO0O0O0O0O ={'authorization':O0OOOO0OOO0O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOOO0OO0OO00 ),'signstring':OOOOOOOOO0OO0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:763
                            OOOOO000000O0O000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO0000O00000000O )}#line:764
                            OO00O00OO0000O0O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOO0O0OO0O0O0O0O ,data =OOOOO000000O0O000 ).json ()#line:765
                            if 'status'in OO00O00OO0000O0O0 :#line:767
                                if OO00O00OO0000O0O0 ['status']==200 :#line:768
                                    print (f'【参与抽奖】:添加三叶草:{OO00O00OO0000O0O0["data"]}丨数量:{OOO0000O00000000O}')#line:769
                                if OO00O00OO0000O0O0 ['status']==500 :#line:770
                                    print (f'【参与抽奖】:添加三叶草:{OO00O00OO0000O0O0["message"]}')#line:771
            O00O0OO000O000OO0 =requests .request ('get',f'{host}/lottery',headers =O00O0000O0O00O0OO ).json ()#line:772
            OO00000OO0OOOOOOO =O0OOOO0OOO0O00OOO .winning_rewards ()#line:774
            if 'status'in O00O0OO000O000OO0 :#line:775
                if O00O0OO000O000OO0 ['status']==200 :#line:776
                    OOO00O0O0OOOOOOOO =O00O0OO000O000OO0 ['data'][0 ]['day_get_gold_quantity']#line:777
                    golden_seed +=float (OOO00O0O0OOOOOOOO )#line:778
                    print (f'【参与抽奖】:预计每天中{str(OOO00O0O0OOOOOOOO)[:6]}颗金种子丨好友收益:{str(OO00000OO0OOOOOOO)[:6]}')#line:779
        except Exception as OO0O0O00OOOO0OOO0 :#line:780
            print (OO0O0O00OOOO0OOO0 )#line:781
    def energy (O0O00OO0OOOO0OO00 ):#line:785
        try :#line:786
            while True :#line:787
                OO0OOOOOOOOOOO00O =f'__{timi_new()}'#line:788
                O0OO0O00OO00000OO ={'authorization':O0O00OO0OOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOOOOOOOO00O ),'signstring':OO0OOOOOOOOOOO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:797
                O0OOO0O00OOO0OOOO =requests .request ('get',f'{host}/energy/general',headers =O0OO0O00OO00000OO ).json ()#line:798
                if 'status'in O0OOO0O00OOO0OOOO :#line:800
                    if O0OOO0O00OOO0OOOO ['status']==200 :#line:801
                        OO00OOO000OOO0O00 =O0OOO0O00OOO0OOOO ['data']['ordinary_water']#line:802
                        O0OO0OOOOOOO00000 =O0OOO0O00OOO0OOOO ['data']['ordinary_fertilizer']#line:803
                        print (f'【我的营养】:肥料:{str(O0OO0OOOOOOO00000).split(".")[0]}丨水滴:{str(OO00OOO000OOO0O00).split(".")[0]}')#line:805
                        if float (O0OO0OOOOOOO00000 )<96 :#line:806
                            time .sleep (random .randint (160 ,180 )/10 )#line:807
                            OOOO00O0O00000000 =99 -float (O0OO0OOOOOOO00000 )#line:808
                            OO00O00OOO0OO0000 ={"fertilizer":str (OOOO00O0O00000000 ).split ('.')[0 ]}#line:809
                            O00O0OOOOOO0OOOO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0OO0O00OO00000OO ).json ()#line:810
                            if 'status'in O00O0OOOOOO0OOOO0 :#line:812
                                if O00O0OOOOOO0OOOO0 ['status']==200 :#line:813
                                    print (f'【购买肥料】:看广告获取肥料:{O00O0OOOOOO0OOOO0["message"]}')#line:814
                        if float (OO00OOO000OOO0O00 )<880 :#line:815
                            time .sleep (random .randint (160 ,180 )/10 )#line:816
                            OOO0OO0O0O0O00O0O =999 -float (OO00OOO000OOO0O00 )#line:817
                            O0000O000000O00O0 ={"water":str (OOO0OO0O0O0O00O0O ).split ('.')[0 ]}#line:818
                            OO0O00OOO0O0O0000 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0OO0O00OO00000OO ).json ()#line:819
                            if 'status'in OO0O00OOO0O0O0000 :#line:821
                                if OO0O00OOO0O0O0000 ['status']==200 :#line:822
                                    print (f'【购买水滴】:看广告获取水滴:{OO0O00OOO0O0O0000["message"]}')#line:823
                        if float (O0OO0OOOOOOO00000 )>96 and float (OO00OOO000OOO0O00 )>880 :#line:824
                            break #line:825
        except Exception as O0O0OOOO0O0O0O0OO :#line:827
            print (O0O0OOOO0O0O0O0OO )#line:828
def bundled_def ():#line:830
    OOOO0OO0OOO0OOO00 =['5570536','7750212','7911652','7911680','7805624']#line:831
    return OOOO0OO0OOO0OOO00 [random .randint (0 ,len (OOOO0OO0OOO0OOO00 )-1 )]#line:832
def version_of_the_validation ():#line:836
    return str ((76 -56 )/10 )#line:837
def gitee_validation ():#line:840
    try :#line:841
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:842
    except :#line:843
        sys .exit (0 )#line:844
def update_the_validation ():#line:848
    try :#line:849
        OOOO00OO00OOO00O0 =gitee_validation ()#line:850
        if version_of_the_validation ()<OOOO00OO00OOO00O0 ['CityEarth']['edition']:#line:851
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO00OO00OOO00O0["CityEarth"]["edition"]}   ❌')#line:852
            print (f'更新内容=>>{OOOO00OO00OOO00O0["CityEarth"]["content"]}   👍')#line:853
        else :#line:854
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO00OO00OOO00O0["CityEarth"]["edition"]}   ✅')#line:855
            print (f'更新内容=>> {OOOO00OO00OOO00O0["CityEarth"]["content"]}   👍')#line:856
    except Exception as OOOO00000OOOO0000 :#line:857
        print (OOOO00000OOOO0000 )#line:858
def os_qinglong ():#line:861
    if application in os .environ :#line:862
        OO0OO0000OO0OOOO0 =os .environ [application ].split ('\n')#line:863
        if len (OO0OO0000OO0OOOO0 )>0 :#line:864
            return OO0OO0000OO0OOOO0 #line:865
        else :#line:866
            print (f"{application}变量未启用")#line:867
            print ('脚本退出')#line:868
            sys .exit (1 )#line:869
    else :#line:870
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:872
        return os_built ()#line:873
def os_built ():#line:876
    if token :#line:877
        O00OO000OOOO0O0OO =token .split ('\n')#line:878
        if len (O00OO000OOOO0O0OO )>0 :#line:879
            return O00OO000OOOO0O0OO #line:880
    else :#line:881
        print (f"内置变量为空")#line:882
        print ('脚本结束')#line:883
        sys .exit (0 )#line:884
if __name__ =='__main__':#line:887
    start ()#line:888
