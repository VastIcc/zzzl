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
@ 版本  2.2
"""
application = 'ce_token'  # 变量名
token = ''
time_xx = random.randint(23, 28)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
version ='3.1.4195311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        O00OOO0OOO0OOO00O =os_qinglong ()#line:10
        print (f"==========共找到{len(O00OOO0OOO0OOO00O)}个账号==========")#line:11
        for O00OO0OO00OOO00OO in O00OOO0OOO0OOO00O :#line:12
            OO0OO00O00OO0O0OO =[]#line:13
            print (f"------------正在执行第{O00OOO0OOO0OOO00O.index(O00OO0OO00OOO00OO) + 1}个账号------------")#line:14
            O0O00O00O0OOO00OO =CityEarth (O00OO0OO00OOO00OO ,OO0OO00O00OO0O0OO )#line:15
            def OO0OOO0OOOOO0O0O0 ():#line:17
                if O0O00O00O0OOO00OO .base_info ():#line:19
                    O0O00O00O0OOO00OO .sealing ()#line:21
                    O0O00O00O0OOO00OO .invitenum ()#line:23
                    O0O00O00O0OOO00OO .game_map ()#line:25
                    O0O00O00O0OOO00OO .friends_invitation ()#line:27
                    O0O00O00O0OOO00OO .add_clover ()#line:29
                    O0O00O00O0OOO00OO .propsraffle ()#line:31
                    O0O00O00O0OOO00OO .synthetic ()#line:33
                    O0O00O00O0OOO00OO .crops_illustrated ()#line:35
                    O0O00O00O0OOO00OO .give_gold ()#line:37
                    O0O00O00O0OOO00OO .withdraw ()#line:39
                    O0O00O00O0OOO00OO .energy ()#line:41
            OO00OOOOOO00O0000 =threading .Thread (target =OO0OOO0OOOOO0O0O0 )#line:42
            OO00OOOOOO00O0000 .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        O00O0OO0O0O0OOO00 =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00O0OO0O0O0OOO00 +' ')#line:48
    except Exception as O0OO000O0OO0OO000 :#line:49
        print (O0OO000O0OO0OO000 )#line:50
def sign (OOOO000000O0OO0OO ):#line:53
    O00OOOOO0000OO0O0 =hashlib .md5 (OOOO000000O0OO0OO .encode ()).hexdigest ()#line:54
    OOO0OOO0OOO0OO0OO ="scsc%^&*"+O00OOOOO0000OO0O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    O0000OOO0O0OOO00O =hashlib .md5 (OOO0OOO0OOO0OO0OO .encode ()).hexdigest ()#line:56
    return O0000OOO0O0OOO00O #line:57
def format_msg ():#line:59
    OO0O0OO00OOO0OOOO =""#line:60
    for OO0OOOOO00O0O000O in msg_list :#line:61
        OO0O0OO00OOO0OOOO +=str (OO0OOOOO00O0O000O )+"\r\n"#line:62
    return OO0O0OO00OOO0OOOO #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (OO0OO00OOOO0OO0OO ,O0O0OO0000000O000 ,OOO0O0O0O0O00OO0O ):#line:71
        try :#line:72
            OO0OO00OOOO0OO0OO .msg =OOO0O0O0O0O00OO0O #line:73
            OO0OO00OOOO0OO0OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            OO0OO00OOOO0OO0OO .token =O0O0OO0000000O000 .split ('&')[0 ]#line:75
            OO0OO00OOOO0OO0OO .innerId =O0O0OO0000000O000 .split ('&')[1 ]#line:76
            OO0OO00OOOO0OO0OO .doneeNo =O0O0OO0000000O000 .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (OO0O0O00O0O0OOO00 ):#line:82
        try :#line:83
            OO0O0O00O0O0OOO00 .watched_ad ()#line:85
            OOO00O0OOOOOOOOOO =f'__{timi_new()}'#line:86
            OOOOOO0000OOO0O0O ={'authorization':OO0O0O00O0O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OOOOOOOOOO ),'signstring':OOO00O0OOOOOOOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            OOO0OO0O0O0O0OO00 =requests .request ('get',f'{host}/user',headers =OOOOOO0000OOO0O0O ).json ()#line:96
            if 'status'in OOO0OO0O0O0O0OO00 :#line:98
                if OOO0OO0O0O0O0OO00 ['status']==200 :#line:99
                    O000O0OOO00000OOO =OOO0OO0O0O0O0OO00 ['data']['nickname']#line:100
                    O00OOO00OO0OOOO0O =OOO0OO0O0O0O0OO00 ['data']['inner_id']#line:101
                    OO000000OO0O0OO00 =OOO0OO0O0O0O0OO00 ['data']['assets']['gold']#line:102
                    OO00O000O000000O0 =OOO0OO0O0O0O0OO00 ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{O000O0OOO00000OOO[:5]}丨ID:{O00OOO00OO0OOOO0O}丨等级:{OO00O000O000000O0}丨金种子:{str(OO000000OO0O0OO00).split(".")[0]}')#line:104
                if OOO0OO0O0O0O0OO00 ['status']==401 :#line:105
                    print (OOO0OO0O0O0O0OO00 ['message'])#line:106
                    OO0O0O00O0O0OOO00 .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if OOO0OO0O0O0O0OO00 ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as O0OOO00O00OOO0O0O :#line:112
            print (O0OOO00O00OOO0O0O )#line:113
    def sealing (O0OO00OO0OOO0OOO0 ):#line:116
        try :#line:117
            OOOOOO00O0OOO0O0O =f'__{timi_new()}'#line:118
            OOO0O00000O000O00 ={'authorization':O0OO00OO0OOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00O0OOO0O0O ),'signstring':OOOOOO00O0OOO0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO0O00000O000O00 )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =OOO0O00000O000O00 )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO0O00000O000O00 )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO0O00000O000O00 )#line:131
            requests .request ('get',f'{host}/user',headers =OOO0O00000O000O00 )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO0O00000O000O00 )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO0O00000O000O00 )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO0O00000O000O00 )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =OOO0O00000O000O00 )#line:136
            requests .request ('get',f'{host}/assets',headers =OOO0O00000O000O00 )#line:137
        except Exception as O0O0O00O00000O0O0 :#line:138
            print (O0O0O00O00000O0O0 )#line:139
    def withdraw (O00OO0O0000000OO0 ):#line:143
        OOO0O0OOO0OO0O00O =f'__{timi_new()}'#line:144
        O00O0O000O0000000 ={'authorization':O00OO0O0000000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OOO0OO0O00O ),'signstring':OOO0O0OOO0OO0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        OO0OOOOOO000OOOOO =requests .request ('get',f'{host}/assets',headers =O00O0O000O0000000 ).json ()#line:154
        if 'status'in OO0OOOOOO000OOOOO :#line:156
            if OO0OOOOOO000OOOOO ['status']==200 :#line:157
                OOOO0O000000O0OOO =OO0OOOOOO000OOOOO ['data']['cash']#line:158
                if float (OOOO0O000000O0OOO )>20 :#line:159
                    OOO0O0OOO0OO0O00O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    O00O0O000O0000000 ={'authorization':O00OO0O0000000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OOO0OO0O00O ),'signstring':OOO0O0OOO0OO0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    O00O0O00O000OO00O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    OOO0OO000O0OOO0OO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00O0O000O0000000 ,data =O00O0O00O000OO00O ).json ()#line:172
                    print (OOO0OO000O0OOO0OO )#line:173
    def invitenum (OOO00O0OOO00OOOOO ):#line:176
        OO0O000O0OO00OOO0 =f'__{timi_new()}'#line:177
        O0OO0O00O00OO0O0O ={'authorization':OOO00O0OOO00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000O0OO00OOO0 ),'signstring':OO0O000O0OO00OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O00000OO00OO0O00O =requests .request ('get',f'{host}/invite/invitenum',headers =O0OO0O00O00OO0O0O ).json ()#line:187
        if 'status'in O00000OO00OO0O00O :#line:189
            if O00000OO00OO0O00O ['status']==200 :#line:190
                OOOOO000O0OO0OO0O =O00000OO00OO0O00O ['data']['invited_count']#line:191
                O0O0O00OOO0O000O0 =O00000OO00OO0O00O ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OOOOO000O0OO0OO0O}丨间邀好友:{O0O0O00OOO0O000O0}')#line:193
    def game_map (O00OO0OOOO0O0O0OO ):#line:196
        try :#line:197
            O000O0O0OO0000O00 =f'__{timi_new()}'#line:198
            O00OO0O0OOOO00O00 ={'authorization':O00OO0OOOO0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O0OO0000O00 ),'signstring':O000O0O0OO0000O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            O0O0O0OO00000O00O =requests .request ('get',f'{host}/game/map',headers =O00OO0O0OOOO00O00 ).json ()#line:208
            if 'status'in O0O0O0OO00000O00O :#line:210
                if O0O0O0OO00000O00O ['status']==200 :#line:211
                    for O0OOOOOOO0O0OOO00 in O0O0O0OO00000O00O ['data']['list'][0 ]['crops']:#line:212
                        O0OOO00O0O0O0OOO0 =O0OOOOOOO0O0OOO00 ['level']#line:214
                        if O0OOO00O0O0O0OOO0 ==41 :#line:215
                            OOO00000O000O0OOO =O0OOOOOOO0O0OOO00 ['crop_name']#line:216
                            O00O00O0OOO0000O0 =O0OOOOOOO0O0OOO00 ['count']#line:217
                            if O00O00O0OOO0000O0 >0 :#line:218
                                print (f'【农业资产】:{OOO00000O000O0OOO}丨数量:{O00O00O0OOO0000O0}')#line:219
        except Exception as O000OO0OO00O0O0OO :#line:220
            print (O000OO0OO00O0O0OO )#line:221
    def give_gold (O0O0O000O00OOOO00 ):#line:224
        try :#line:225
            O000O000O0OOO0O00 =f'__{timi_new()}'#line:226
            O0O000OOOOO0000OO ={'authorization':O0O0O000O00OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000O0OOO0O00 ),'signstring':O000O000O0OOO0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            O00O0O0000O00O000 =requests .request ('get',f'{host}/user',headers =O0O000OOOOO0000OO ).json ()#line:236
            if 'status'in O00O0O0000O00O000 :#line:237
                if O00O0O0000O00O000 ['status']==200 :#line:238
                    if float (O0O0O000O00OOOO00 .doneeNo )!=0 :#line:239
                        O00OOO0O0O0OO000O =O00O0O0000O00O000 ['data']['assets']['gold']#line:240
                        if float (O00OOO0O0O0OO000O )>float (O0O0O000O00OOOO00 .innerId ):#line:241
                            O00OO0OO0O000OO0O =int (float (O00OOO0O0O0OO000O )/1.1 )#line:242
                            O000O000O0OOO0O00 =f'_doneeNo={O0O0O000O00OOOO00.doneeNo}&quantity={O00OO0OO0O000OO0O}_{timi_new()}'#line:243
                            O0O000OOOOO0000OO ={'authorization':O0O0O000O00OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000O0OOO0O00 ),'signstring':O000O000O0OOO0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            O000OO0O0OO000000 ={"quantity":O00OO0OO0O000OO0O ,"doneeNo":O0O0O000O00OOOO00 .doneeNo }#line:256
                            O0OO00OO0OO00O000 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O000OOOOO0000OO ,data =O000OO0O0OO000000 ).json ()#line:257
                            if 'status'in O0OO00OO0OO00O000 :#line:259
                                if O0OO00OO0OO00O000 ['status']==200 :#line:260
                                    if O0OO00OO0OO00O000 ['data']:#line:261
                                        print (f'【赠送种子】:赠送{O00OO0OO0O000OO0O}种子给{O0O0O000O00OOOO00.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as O0OO0O0O0O0OO00O0 :#line:265
            print (O0OO0O0O0O0OO00O0 )#line:266
    def invitation (O0000O000OOOOOOO0 ):#line:268
        try :#line:269
            _OOO0O000OOO0OOOOO =float (bundled_def ())/4 #line:270
            O0OO0O00O0OO000O0 =f'_innerId={int(_OOO0O000OOO0OOOOO)}_{timi_new()}'#line:271
            O000000O0O000O00O ={'authorization':O0000O000OOOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O0OO000O0 ),'signstring':O0OO0O00O0OO000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            OO00O00000OO0O00O ={"innerId":int (_OOO0O000OOO0OOOOO )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =O000000O0O000O00O ,data =OO00O00000OO0O00O )#line:282
        except Exception as O0OO0O0O00O0OO000 :#line:283
            print (O0OO0O0O00O0OO000 )#line:284
    def winning_rewards (O0OOO0O00OO0OO000 ):#line:287
        try :#line:288
            O0O0O0O0O0OOOO000 =f'__{timi_new()}'#line:289
            O0O0000O0OOOOOO00 ={'authorization':O0OOO0O00OO0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0O0OOOO000 ),'signstring':O0O0O0O0O0OOOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            OO0OOO0O000O0O0O0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O0000O0OOOOOO00 ).json ()#line:299
            if 'status'in OO0OOO0O000O0O0O0 :#line:301
                if OO0OOO0O000O0O0O0 ['status']==200 :#line:302
                    if OO0OOO0O000O0O0O0 ['data']['amount']:#line:303
                        O0OO0OOO000O00O00 =OO0OOO0O000O0O0O0 ['data']['amount']['gold']#line:304
                        return O0OO0OOO000O00O00 #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as O0O00OO0O00O0000O :#line:308
            print (O0O00OO0O00O0000O )#line:309
    def certification (OOO0O0000OO00000O ):#line:312
        try :#line:313
            OOOOOO0O0000O00OO =f'__{timi_new()}'#line:314
            O0000O00O0OO00OO0 ={'authorization':OOO0O0000OO00000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O0000O00OO ),'signstring':OOOOOO0O0000O00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OO0OOOOO0000000OO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0000O00O0OO00OO0 ).json ()#line:324
            if 'status'in OO0OOOOO0000000OO :#line:326
                if OO0OOOOO0000000OO ['status']==200 :#line:327
                    if OO0OOOOO0000000OO ['data']['result']:#line:328
                        O00O00000O0000O00 =OO0OOOOO0000000OO ['data']['nick_name']#line:329
                        return O00O00000O0000O00 #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as O0O0OOO000O0OOOO0 :#line:333
            print (O0O0OOO000O0OOOO0 )#line:334
    def crops_illustrated (OOOO0OO000OOOOOO0 ):#line:337
        try :#line:338
            OOO0OO000O000O000 =f'__{timi_new()}'#line:339
            OO000OOO0OOO000O0 ={'authorization':OOOO0OO000OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO000O000O000 ),'signstring':OOO0OO000O000O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            O0O0OO000OO0OOO00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO000OOO0OOO000O0 ).json ()#line:349
            if 'status'in O0O0OO000OO0OOO00 :#line:351
                if O0O0OO000OO0OOO00 ['status']==200 :#line:352
                    O0OOO0O00OO0OO0O0 =O0O0OO000OO0OOO00 ['data'][0 ]['crops']#line:353
                    for OO00OOOOOOOOO00OO in O0OOO0O00OO0OO0O0 :#line:354
                        if OO00OOOOOOOOO00OO ['ill_clover_award']:#line:355
                            if float (OO00OOOOOOOOO00OO ['ill_clover_award'])>1 :#line:356
                                if OO00OOOOOOOOO00OO ['is_finish']:#line:357
                                    if not OO00OOOOOOOOO00OO ['is_getit']:#line:358
                                        if OOOO0OO000OOOOOO0 .certification ()!='未实名':#line:359
                                            OOO0OO000O000O000 =f'_award_level={OO00OOOOOOOOO00OO["level"]}_{timi_new()}'#line:360
                                            OO000OOO0OOO000O0 ={'authorization':OOOO0OO000OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO000O000O000 ),'signstring':OOO0OO000O000O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            O0O0O00OOOO0O00OO ={"award_level":OO00OOOOOOOOO00OO ['level']}#line:370
                                            O0O00O000OO0O0O00 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO000OOO0OOO000O0 ,json =O0O0O00OOOO0O00OO ).json ()#line:372
                                            if 'status'in O0O00O000OO0O0O00 :#line:373
                                                if O0O00O000OO0O0O00 ['status']==200 :#line:374
                                                    O00O000O0O0O0O00O =O0O00O000OO0O0O00 ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{OO00OOOOOOOOO00OO["crop_name"]}成就丨奖励{O00O000O0O0O0O00O}☘️')#line:377
                                                if O0O00O000OO0O0O00 ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{O0O00O000OO0O0O00["message"]}')#line:379
        except Exception as O00O0OOOOO0O00O00 :#line:380
            print (O00O0OOOOO0O00O00 )#line:381
    def watched_ad (OO0O0O00OO0O0000O ):#line:384
        try :#line:385
            OO00O00OOOOOO00O0 =f'__{timi_new()}'#line:386
            O0O000000OOOOO0OO ={'authorization':OO0O0O00OO0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OOOOOO00O0 ),'signstring':OO00O00OOOOOO00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            OO0O00O0O000OOOOO =requests .request ('get',f'{host}/game/getAllData',headers =O0O000000OOOOO0OO ).json ()#line:396
            if 'status'in OO0O00O0O000OOOOO :#line:398
                if OO0O00O0O000OOOOO ['status']==200 :#line:399
                    if 'offlineInfo'in OO0O00O0O000OOOOO ['data']:#line:400
                        time .sleep (random .randint (16 ,18 ))#line:401
                        OOOOOOOO0000O0OO0 =OO0O00O0O000OOOOO ['data']['offlineInfo']['off_minute']#line:402
                        OOOO00000OOO00000 =float (OO0O00O0O000OOOOO ['data']['silver'])/1000000000000 #line:403
                        time .sleep (1 )#line:404
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O000000OOOOO0OO ).json ()#line:405
                        time .sleep (2 )#line:406
                        OOOOOO00OO0O0O00O =requests .request ('get',f'{host}/game/getAllData',headers =O0O000000OOOOO0OO ).json ()#line:407
                        if 'status'in OOOOOO00OO0O0O00O :#line:409
                            if OOOOOO00OO0O0O00O ['status']==200 :#line:410
                                O00O00OOO00O0O0O0 =float (OOOOOO00OO0O0O00O ['data']['silver'])/1000000000000 #line:411
                                O0000OOOOOO00OO0O =str (O00O00OOO00O0O0O0 -OOOO00000OOO00000 )[:6 ]#line:412
                                print (f'【离线奖励】:翻倍离线{OOOOOOOO0000O0OO0}分钟奖励🌱数量:{O0000OOOOOO00OO0O}t粒')#line:413
        except Exception as OOO0OOO0OOO0OOO00 :#line:414
            print (OOO0OOO0OOO0OOO00 )#line:415
    def user_ad (O000O0OOO0O0O0OO0 ):#line:418
        try :#line:419
            O0O0O00OO000O000O =f'__{timi_new()}'#line:420
            O000O0O000OO0000O ={'authorization':O000O0OOO0O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OO000O000O ),'signstring':O0O0O00OO000O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:429
            OOOO0OOOOOOO0O0OO =requests .request ('get',f'{host}/user/ad',headers =O000O0O000OO0000O ).json ()#line:430
            if 'status'in OOOO0OOOOOOO0O0OO :#line:432
                if OOOO0OOOOOOO0O0OO ['status']==200 :#line:433
                    O000O0000OOO0O000 =OOOO0OOOOOOO0O0OO ['data']['max_time']#line:434
                    O0O0O0OO0O0000O0O =OOOO0OOOOOOO0O0OO ['data']['watch_time']#line:435
                    OO0OOOO00OOO0OO0O =OOOO0OOOOOOO0O0OO ['data']['added_time']#line:436
                    print (f'【获取种子】:获取🌱剩余{OO0OOOO00OOO0OO0O + O000O0000OOO0O000 - O0O0O0OO0O0000O0O}次丨好友提供:{OO0OOOO00OOO0OO0O}次')#line:437
                    if OO0OOOO00OOO0OO0O +O000O0000OOO0O000 -O0O0O0OO0O0000O0O >0 :#line:438
                        time .sleep (random .randint (16 ,19 ))#line:439
                        O0OO0O00000O00000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O000O0O000OO0000O ).json ()#line:440
                        if 'status'in O0OO0O00000O00000 :#line:442
                            if O0OO0O00000O00000 ['status']==200 :#line:443
                                OO000OO00O0000OO0 =float (O0OO0O00000O00000 ['data']['silver'])/1000000000000 #line:444
                                print (f'【获取种子】:获得🌱:{int(OO000OO00O0000OO0)}t粒')#line:445
                                return True #line:446
                            if O0OO0O00000O00000 ['status']==500 :#line:447
                                OO0O00O00OO00OOOO =O0OO0O00000O00000 ['message']#line:448
                                print (f'【获取种子】:{OO0O00O00OO00OOOO}')#line:449
                                return False #line:450
        except Exception as OO0000O0OO0OO000O :#line:451
            print (OO0000O0OO0OO000O )#line:452
    def synthetic (O0OOOOO0O0000OOO0 ):#line:455
        global id ,g #line:456
        try :#line:457
            O00O0OOO0O000O0OO =O0OOOOO0O0000OOO0 .level_new ()#line:458
            OOOOOOOOOOOOO0000 =random .randint (9 ,11 )#line:459
            O00OO0OO0OO000OO0 =f'_site=8&targetSite={OOOOOOOOOOOOO0000}_{timi_new()}'#line:460
            O0O00OOOOOOO0OOO0 ={'accept':'application/json, text/plain, */*','authorization':O0OOOOO0O0000OOO0 .token ,'timestamp':timi_new (),'sign':sign (O00OO0OO0OO000OO0 ),'signstring':O00OO0OO0OO000OO0 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:475
            OOOOO0OOO0O00O000 ={"site":int (8 ),"targetSite":int (OOOOOOOOOOOOO0000 )}#line:476
            requests .request ('post',f'{host}/game/crops/move',headers =O0O00OOOOOOO0OOO0 ,json =OOOOO0OOO0O00O000 )#line:477
            while True :#line:478
                O0OOOOO0OOO00OO00 =f'__{timi_new()}'#line:479
                OO0O0OO0OO00000O0 ={'authorization':O0OOOOO0O0000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0OOO00OO00 ),'signstring':O0OOOOO0OOO00OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                O000OOO0O0OOOOO00 =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0OO0OO00000O0 ).json ()#line:489
                if 'status'in O000OOO0O0OOOOO00 :#line:491
                    if O000OOO0O0OOOOO00 ['status']==200 :#line:492
                        O00OO0O0OO0O0O0OO =O000OOO0O0OOOOO00 ['data']['cropList']#line:493
                        OO00OOOO000O0O000 =O000OOO0O0OOOOO00 ['data']['gameCoreDataDBid']#line:494
                        O0OO0O0OO00O0OOO0 =float (O000OOO0O0OOOOO00 ['data']['silver'])/1000000000000 #line:495
                        if O0OO0O0OO00O0OOO0 <6750 :#line:496
                            print (f'【种植合成】:🌱不足6750t')#line:497
                            if not O0OOOOO0O0000OOO0 .user_ad ():#line:498
                                return False #line:499
                        O00OOOOOO0O0O00OO =0 #line:500
                        for O0OO00000O0OO0000 in O00OO0O0OO0O0O0OO :#line:501
                            if not O0OO00000O0OO0000 :#line:502
                                O00000OO000OOOO00 =f'_crop_id={OO00OOOO000O0O000}&site={O00OOOOOO0O0O00OO}_{O0OOOOO0O0000OOO0.time}'#line:503
                                OOO00O000O0OOO0O0 ={'authorization':O0OOOOO0O0000OOO0 .token ,'timestamp':O0OOOOO0O0000OOO0 .time ,'sign':sign (O00000OO000OOOO00 ),'signstring':O00000OO000OOOO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
                                O0O0O00O000O0OO00 ={"site":O00OOOOOO0O0O00OO ,"crop_id":OO00OOOO000O0O000 }#line:513
                                OO00O00OO0O0O0OOO =requests .request ('post',f'{host}/game/crops/buy',headers =OOO00O000O0OOO0O0 ,data =O0O0O00O000O0OO00 ).json ()#line:514
                                time .sleep (random .randint (1 ,3 )/10 )#line:516
                                if 'status'in OO00O00OO0O0O0OOO :#line:517
                                    if OO00O00OO0O0O0OOO ['status']==200 :#line:518
                                        if OO00O00OO0O0O0OOO ['message']=='种子数量不足':#line:519
                                            O00O0OOO0O000O0OO =O0OOOOO0O0000OOO0 .level_new ()#line:520
                                            print (f'【种植合成】:{OO00O00OO0O0O0OOO["message"]}')#line:521
                                            if not O0OOOOO0O0000OOO0 .user_ad ():#line:522
                                                return False #line:523
                                    if OO00O00OO0O0O0OOO ['status']==500 :#line:524
                                        print (f'【种植合成】:{OO00O00OO0O0O0OOO["message"]}')#line:525
                                        return False #line:526
                            O00OOOOOO0O0O00OO +=1 #line:527
                        OO0OO0OOO00OOOOOO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0OO0OO00000O0 ).json ()#line:528
                        OO0OOOO0O00O000O0 =OO0OO0OOO00OOOOOO ['data']['cropList']#line:529
                        OO0O0000OO0OO0OO0 =False #line:530
                        for O0OO00000O0OO0000 in range (12 ):#line:531
                            id =OO0OOOO0O00O000O0 [O0OO00000O0OO0000 ]['level']#line:532
                            if float (O00O0OOO0O000O0OO )-float (id )>9 :#line:533
                                OOO0O0OOO000000OO =f'_site={O0OO00000O0OO0000}_{timi_new()}'#line:534
                                OOOO000O0000O0OOO ={'accept':'application/json, text/plain, */*','authorization':O0OOOOO0O0000OOO0 .token ,'timestamp':timi_new (),'sign':sign (OOO0O0OOO000000OO ),'signstring':OOO0O0OOO000000OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:544
                                O0OOO0000O0OOOO00 ={"site":O0OO00000O0OO0000 }#line:545
                                OOOO0OO0O0OOO0OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOO000O0000O0OOO ,data =O0OOO0000O0OOOO00 ).json ()#line:547
                                if 'status'in OOOO0OO0O0OOO0OOO :#line:548
                                    if OOOO0OO0O0OOO0OOO ['status']==200 :#line:549
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:550
                            if id !=0 :#line:551
                                for OO0OO0O000O0O0OOO in range (11 ):#line:552
                                    O0OO0O0O000O00O00 =OO0OO0O000O0O0OOO +1 #line:553
                                    g =OO0OOOO0O00O000O0 [O0OO0O0O000O00O00 ]['level']#line:554
                                    if id ==g :#line:555
                                        OOO0OO000O0O0OOO0 =OO0OO0O000O0O0OOO +2 #line:556
                                        if OOO0OO000O0O0OOO0 !=O0OO00000O0OO0000 +1 :#line:557
                                            O0OO00OOO00O0O000 =O0OO00000O0OO0000 +1 #line:558
                                            time .sleep (random .randint (1 ,3 )/10 )#line:560
                                            O00OO0OO0OO000OO0 =f'_site={O0OO00OOO00O0O000 - 1}&targetSite={OOO0OO000O0O0OOO0 - 1}_{timi_new()}'#line:561
                                            O0O00OOOOOOO0OOO0 ={'accept':'application/json, text/plain, */*','authorization':O0OOOOO0O0000OOO0 .token ,'timestamp':timi_new (),'sign':sign (O00OO0OO0OO000OO0 ),'signstring':O00OO0OO0OO000OO0 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:576
                                            O0O0O00000OO00O00 ={"site":int (O0OO00OOO00O0O000 -1 ),"targetSite":int (OOO0OO000O0O0OOO0 -1 )}#line:577
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0O00OOOOOOO0OOO0 ,json =O0O0O00000OO00O00 )#line:578
                                            print (f'【种植合成】:位置{O0OO00OOO00O0O000}和位置{OOO0OO000O0O0OOO0}合出{int(id) + 1}级农作物')#line:579
                                            OO0O0000OO0OO0OO0 =True #line:580
                                    if OO0O0000OO0OO0OO0 :#line:581
                                        break #line:582
                                if OO0O0000OO0OO0OO0 :#line:583
                                    break #line:584
        except :#line:585
            O0OOOOO0O0000OOO0 .synthetic ()#line:586
    def level_new (OOOO000OO00OOOOOO ):#line:589
        try :#line:590
            OOO0000O0OO00OO0O =f'__{timi_new()}'#line:591
            OO0OOOO0OO0O00OO0 ={'authorization':OOOO000OO00OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O0OO00OO0O ),'signstring':OOO0000O0OO00OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            OOOO0OO0OOOOO00OO =requests .request ('get',f'{host}/user',headers =OO0OOOO0OO0O00OO0 ).json ()#line:601
            if 'status'in OOOO0OO0OOOOO00OO :#line:602
                if OOOO0OO0OOOOO00OO ['status']==200 :#line:603
                    return float (OOOO0OO0OOOOO00OO ['data']['level'])#line:604
        except Exception as OOO00OO00000OOOOO :#line:605
            print (OOO00OO00000OOOOO )#line:606
    def propsraffle (OOO0OO00OO0000O0O ):#line:609
        try :#line:610
            while True :#line:611
                OOO000O0O0OOO0O0O =f'__{timi_new()}'#line:612
                OOO00000OO000O00O ={'authorization':OOO0OO00OO0000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0O0OOO0O0O ),'signstring':OOO000O0O0OOO0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:621
                OO0O0O0OOO0O00000 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO00000OO000O00O ).json ()#line:622
                if 'status'in OO0O0O0OOO0O00000 :#line:624
                    if OO0O0O0OOO0O00000 ['status']==200 :#line:625
                        OOOO0000OOO0000OO =OO0O0O0OOO0O00000 ['data']['rows']#line:626
                        O00OO00OOOO00O000 =OO0O0O0OOO0O00000 ['data']['vstate']#line:627
                        if OOOO0000OOO0000OO ==5 or OOOO0000OOO0000OO ==6 or OOOO0000OOO0000OO ==7 :#line:628
                            OO0OOOOO0O0OOOOOO =OO0O0O0OOO0O00000 ['data']['silver']#line:629
                            print (f'【转盘抽奖】:获得种子:{OO0OOOOO0O0OOOOOO}')#line:630
                        if OOOO0000OOO0000OO ==1 or OOOO0000OOO0000OO ==2 or OOOO0000OOO0000OO ==3 :#line:631
                            OOOOOOO00000OOOOO =OO0O0O0OOO0O00000 ['data']['clover']#line:632
                            print (f'【转盘抽奖】:获得三叶草:{OOOOOOO00000OOOOO}')#line:633
                        if OOOO0000OOO0000OO ==4 or OOOO0000OOO0000OO ==8 :#line:634
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:635
                        if OOOO0000OOO0000OO =='抽奖次数已用完':#line:639
                            break #line:672
                time .sleep (random .randint (8 ,15 )/10 )#line:673
        except Exception as O0OO0O00O00000OOO :#line:674
            print (O0OO0O00O00000OOO )#line:675
    def friends_invitation (O000OO00O000O0O0O ):#line:678
        try :#line:679
            O0O0OO0000O0OOO00 =f'__{timi_new()}'#line:680
            OO00O0OOO000OOOOO ={'authorization':O000OO00O000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0000O0OOO00 ),'signstring':O0O0OO0000O0OOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:689
            O000O0OO0OOOO0OO0 =requests .request ('get',f'{host}/friends',headers =OO00O0OOO000OOOOO ).json ()#line:690
            if 'status'in O000O0OO0OOOO0OO0 :#line:691
                if O000O0OO0OOOO0OO0 ['status']==200 :#line:692
                    OO00OOO0O00O00O00 =O000O0OO0OOOO0OO0 ['data']['myInviteter']#line:693
                    if OO00OOO0O00O00O00 :#line:694
                        O00OOOOOO0OO0O0OO =OO00OOO0O00O00O00 ['user']['nickname']#line:695
                        O0O0O000O0O0O000O =O000OO00O000O0O0O .certification ()#line:696
                        print (f'【查邀请人】:我的邀请人:{O00OOOOOO0OO0O0OO}丨实名:{O0O0O000O0O0O000O}')#line:697
                    else :#line:698
                        if O000OO00O000O0O0O .innerId !='0':#line:699
                            O000OO00O000O0O0O .invitation ()#line:700
        except Exception as OOO000OO000O000OO :#line:701
            print (OOO000OO000O000OO )#line:702
    def add_clover (O000000000O0OO00O ):#line:705
        global golden_seed #line:706
        try :#line:707
            OO000O00O00OO0OOO =f'__{timi_new()}'#line:708
            OOO00O0OOOO0000OO ={'authorization':O000000000O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00O00OO0OOO ),'signstring':OO000O00O00OO0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:717
            OOOO000O0O00OOOO0 =requests .request ('get',f'{host}/assets/clovers',headers =OOO00O0OOOO0000OO ).json ()#line:718
            if 'status'in OOOO000O0O00OOOO0 :#line:720
                if OOOO000O0O00OOOO0 ['status']==200 :#line:721
                    O0OOOOOO0O0OO0O0O =OOOO000O0O00OOOO0 ['data']['clover']#line:722
                    O0OO000OO000O0OOO =OOOO000O0O00OOOO0 ['data']['used_clover']#line:723
                    OOOO000OOO0OO000O =float (O0OOOOOO0O0OO0O0O )-float (O0OO000OO000O0OOO )#line:724
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OO000OO000O0OOO}')#line:725
                    if O000000000O0OO00O .certification ()!='未实名':#line:726
                        if OOOO000OOO0OO000O >1 :#line:727
                            OO000O00O00OO0OOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOO000OOO0OO000O)}_{timi_new()}'#line:728
                            OOOO00O000OO0OOOO ={'authorization':O000000000O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00O00OO0OOO ),'signstring':OO000O00O00OO0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                            O0OOOOO00OOO00000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOO000OOO0OO000O )}#line:738
                            OO00OOO000OOOO00O =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOO00O000OO0OOOO ,data =O0OOOOO00OOO00000 ).json ()#line:739
                            if 'status'in OO00OOO000OOOO00O :#line:741
                                if OO00OOO000OOOO00O ['status']==200 :#line:742
                                    print (f'【参与抽奖】:添加☘️:{OO00OOO000OOOO00O["data"]}丨数量:{OOOO000OOO0OO000O}')#line:743
                                if OO00OOO000OOOO00O ['status']==500 :#line:744
                                    print (f'【参与抽奖】:添加☘️:{OO00OOO000OOOO00O["message"]}')#line:745
            OO00OO00000O0O0O0 =requests .request ('get',f'{host}/lottery',headers =OOO00O0OOOO0000OO ).json ()#line:746
            O0OOO000OOO00OO0O =O000000000O0OO00O .winning_rewards ()#line:748
            if 'status'in OO00OO00000O0O0O0 :#line:749
                if OO00OO00000O0O0O0 ['status']==200 :#line:750
                    O0000O00O000O0O00 =OO00OO00000O0O0O0 ['data'][0 ]['day_get_gold_quantity']#line:751
                    golden_seed +=float (O0000O00O000O0O00 )#line:752
                    OOO0O0OOOOO00O000 =OO00OO00000O0O0O0 ['data'][1 ]['value']#line:753
                    O0000OOO00OO0OO00 =OO00OO00000O0O0O0 ['data'][0 ]['join_number']#line:754
                    OO00OO0O0O00OOOOO =int (float (OO00OO00000O0O0O0 ['data'][0 ]['totalValue']))#line:755
                    OOOOO0O000O0O0000 =float (OOO0O0OOOOO00O000 /OO00OO0O0O00OOOOO )*10000 #line:756
                    O000O0OO00O0OO00O =OO00OO0O0O00OOOOO /O0000OOO00OO0OO00 #line:757
                    print (f'【参与抽奖】:预计每天中{str(O0000O00O000O0O00)[:6]}颗金种子丨好友收益:{str(O0OOO000OOO00OO0O)[:6]}')#line:758
                    print (f'【抽奖统计】:每1万☘️中{str(OOOOO0O000O0O0000)[:6]}颗金种子丨☘️人均:{str(O000O0OO00O0OO00O)[:7]}️')#line:759
        except Exception as OO0OO0OOO0OOOO0OO :#line:760
            print (OO0OO0OOO0OOOO0OO )#line:761
    def energy (OO0OOOOO0OOO0O000 ):#line:765
        try :#line:766
            while True :#line:767
                O0O0O0OOOOO0OOO0O =f'__{timi_new()}'#line:768
                O0O0OO000OO00OOO0 ={'authorization':OO0OOOOO0OOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOOO0OOO0O ),'signstring':O0O0O0OOOOO0OOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:777
                OOO0O0000OO0O0O0O =requests .request ('get',f'{host}/energy/general',headers =O0O0OO000OO00OOO0 ).json ()#line:778
                if 'status'in OOO0O0000OO0O0O0O :#line:780
                    if OOO0O0000OO0O0O0O ['status']==200 :#line:781
                        OO00OOOO0O0O00O0O =OOO0O0000OO0O0O0O ['data']['ordinary_water']#line:782
                        OO00O0000O00O00O0 =OOO0O0000OO0O0O0O ['data']['ordinary_fertilizer']#line:783
                        print (f'【我的营养】:肥料:{str(OO00O0000O00O00O0).split(".")[0]}丨水滴:{str(OO00OOOO0O0O00O0O).split(".")[0]}')#line:785
                        if float (OO00O0000O00O00O0 )<96 :#line:786
                            time .sleep (random .randint (160 ,180 )/10 )#line:787
                            O0O000O0OOOOO0OOO =99 -float (OO00O0000O00O00O0 )#line:788
                            O0OOOO00000OOO0O0 ={"fertilizer":str (O0O000O0OOOOO0OOO ).split ('.')[0 ]}#line:789
                            O0OOOOO0OO0OOOO0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0O0OO000OO00OOO0 ).json ()#line:790
                            if 'status'in O0OOOOO0OO0OOOO0O :#line:792
                                if O0OOOOO0OO0OOOO0O ['status']==200 :#line:793
                                    print (f'【购买肥料】:看广告获取肥料:{O0OOOOO0OO0OOOO0O["message"]}')#line:794
                        if float (OO00OOOO0O0O00O0O )<880 :#line:795
                            time .sleep (random .randint (160 ,180 )/10 )#line:796
                            OOO0O0OOOOOO0OO00 =999 -float (OO00OOOO0O0O00O0O )#line:797
                            OO0O000O00000OO0O ={"water":str (OOO0O0OOOOOO0OO00 ).split ('.')[0 ]}#line:798
                            OO0OOO0O00OO0OOO0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0O0OO000OO00OOO0 ).json ()#line:799
                            if 'status'in OO0OOO0O00OO0OOO0 :#line:801
                                if OO0OOO0O00OO0OOO0 ['status']==200 :#line:802
                                    print (f'【购买水滴】:看广告获取水滴:{OO0OOO0O00OO0OOO0["message"]}')#line:803
                        if float (OO00O0000O00O00O0 )>96 and float (OO00OOOO0O0O00O0O )>880 :#line:804
                            break #line:805
        except Exception as OOOOO0O0OO0OOO00O :#line:807
            print (OOOOO0O0OO0OOO00O )#line:808
def bundled_def ():#line:810
    OOOO00OOO000O0000 =['5570536','7750212','7911652','7911680','7805624']#line:811
    return OOOO00OOO000O0000 [random .randint (0 ,len (OOOO00OOO000O0000 )-1 )]#line:812
def version_of_the_validation ():#line:816
    return str ((78 -56 )/10 )#line:817
def gitee_validation ():#line:820
    try :#line:821
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:822
    except :#line:823
        sys .exit (0 )#line:824
def update_the_validation ():#line:828
    try :#line:829
        O0OOOO000000O0OOO =gitee_validation ()#line:830
        if version_of_the_validation ()<O0OOOO000000O0OOO ['CityEarth']['edition']:#line:831
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOO000000O0OOO["CityEarth"]["edition"]}   ❌')#line:832
            print (f'更新内容=>>{O0OOOO000000O0OOO["CityEarth"]["content"]}   🎉')#line:833
        else :#line:834
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOO000000O0OOO["CityEarth"]["edition"]}   ✅')#line:835
            print (f'更新内容=>> {O0OOOO000000O0OOO["CityEarth"]["content"]}   🎉')#line:836
    except Exception as OOO00OO00O0000000 :#line:837
        print (OOO00OO00O0000000 )#line:838
def os_qinglong ():#line:841
    if application in os .environ :#line:842
        OO00000000OOO0O0O =os .environ [application ].split ('\n')#line:843
        if len (OO00000000OOO0O0O )>0 :#line:844
            return OO00000000OOO0O0O #line:845
        else :#line:846
            print (f"{application}变量未启用")#line:847
            print ('脚本退出')#line:848
            sys .exit (1 )#line:849
    else :#line:850
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:852
        return os_built ()#line:853
def os_built ():#line:856
    if token :#line:857
        OOOOOOOOOO0O0OOOO =token .split ('\n')#line:858
        if len (OOOOOOOOOO0O0OOOO )>0 :#line:859
            return OOOOOOOOOO0O0OOOO #line:860
    else :#line:861
        print (f"内置变量为空")#line:862
        print ('脚本结束')#line:863
        sys .exit (0 )#line:864
if __name__ =='__main__':#line:867
    start ()#line:868
