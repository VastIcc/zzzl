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
@ cron: 8 1-23/2 * * *
@ new Env('生城世朝')
@ 项目地址  https://sc19319.oss-cn-hangzhou.aliyuncs.com/scsc/prod/1.9.3.1.S4195.apk
@ 抓取  http://scsc.sc19319.com 的authorization值
@ 青龙变量  青龙配置文件 export ce_token="authorization&赠送金种子数量大于&赠送金种子id" 
@ 如果你有20金种子填10就会赠 填21就不会赠送  不赠送全填 999999     多号换行
@ 变量示范    export ce_token="557b8069-1234-4ae7-9e29-b7871f91541b&999999&999999"  用&符号分开数据
@ 版本  2.1
"""
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
        O000O00OOO0000OO0 =os_qinglong ()#line:10
        print (f"==========共找到{len(O000O00OOO0000OO0)}个账号==========")#line:11
        for OOOO0O000O0O0OO0O in O000O00OOO0000OO0 :#line:12
            O00OOO0OOO0000OOO =[]#line:13
            print (f"------------正在执行第{O000O00OOO0000OO0.index(OOOO0O000O0O0OO0O) + 1}个账号------------")#line:14
            OO00OO000000O0000 =CityEarth (OOOO0O000O0O0OO0O ,O00OOO0OOO0000OOO )#line:15
            def O000O0O0OOOOOO000 ():#line:17
                if OO00OO000000O0000 .base_info ():#line:19
                    OO00OO000000O0000 .sealing ()#line:21
                    OO00OO000000O0000 .invitenum ()#line:23
                    OO00OO000000O0000 .game_map ()#line:25
                    OO00OO000000O0000 .friends_invitation ()#line:27
                    OO00OO000000O0000 .add_clover ()#line:29
                    OO00OO000000O0000 .propsraffle ()#line:31
                    OO00OO000000O0000 .synthetic ()#line:33
                    OO00OO000000O0000 .crops_illustrated ()#line:35
                    OO00OO000000O0000 .give_gold ()#line:37
                    OO00OO000000O0000 .withdraw ()#line:39
                    OO00OO000000O0000 .energy ()#line:41
            OOOOOOOO0OO000O0O =threading .Thread (target =O000O0O0OOOOOO000 )#line:42
            OOOOOOOO0OO000O0O .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        O0OO0OO000O0O0OOO =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0OO0OO000O0O0OOO +' ')#line:48
    except Exception as O0O0OO0O00O0OO0O0 :#line:49
        print (O0O0OO0O00O0OO0O0 )#line:50
def sign (OOO0O0000OOOOO000 ):#line:53
    O00O0OO0O00O0000O =hashlib .md5 (OOO0O0000OOOOO000 .encode ()).hexdigest ()#line:54
    OOOOOO0000O00OOO0 ="scsc%^&*"+O00O0OO0O00O0000O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    OOOOO0OOO00O0000O =hashlib .md5 (OOOOOO0000O00OOO0 .encode ()).hexdigest ()#line:56
    return OOOOO0OOO00O0000O #line:57
def format_msg ():#line:59
    O00OOOO0OO0OOO000 =""#line:60
    for OO00O0OO000O0OO00 in msg_list :#line:61
        O00OOOO0OO0OOO000 +=str (OO00O0OO000O0OO00 )+"\r\n"#line:62
    return O00OOOO0OO0OOO000 #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (OOO0OO0O0O0OOO00O ,OOO0OO0OOO0OOO000 ,OO00OOO0000000OO0 ):#line:71
        try :#line:72
            OOO0OO0O0O0OOO00O .msg =OO00OOO0000000OO0 #line:73
            OOO0OO0O0O0OOO00O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            OOO0OO0O0O0OOO00O .token =OOO0OO0OOO0OOO000 .split ('&')[0 ]#line:75
            OOO0OO0O0O0OOO00O .innerId =OOO0OO0OOO0OOO000 .split ('&')[1 ]#line:76
            OOO0OO0O0O0OOO00O .doneeNo =OOO0OO0OOO0OOO000 .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (O0O00O0O0OO0000OO ):#line:82
        try :#line:83
            O0O00O0O0OO0000OO .watched_ad ()#line:85
            OO0000O0OOO0000O0 =f'__{timi_new()}'#line:86
            O00O00000O0O0O00O ={'authorization':O0O00O0O0OO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O0OOO0000O0 ),'signstring':OO0000O0OOO0000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            O0000OO00O0O00OOO =requests .request ('get',f'{host}/user',headers =O00O00000O0O0O00O ).json ()#line:96
            if 'status'in O0000OO00O0O00OOO :#line:98
                if O0000OO00O0O00OOO ['status']==200 :#line:99
                    O00OO0O0000OOOOO0 =O0000OO00O0O00OOO ['data']['nickname']#line:100
                    O0OOOOOO00O00O00O =O0000OO00O0O00OOO ['data']['inner_id']#line:101
                    OO00OO00O0000000O =O0000OO00O0O00OOO ['data']['assets']['gold']#line:102
                    OOO0OOO000OOOOO00 =O0000OO00O0O00OOO ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{O00OO0O0000OOOOO0[:5]}丨ID:{O0OOOOOO00O00O00O}丨等级:{OOO0OOO000OOOOO00}丨种子:{str(OO00OO00O0000000O).split(".")[0]}')#line:104
                if O0000OO00O0O00OOO ['status']==401 :#line:105
                    print (O0000OO00O0O00OOO ['message'])#line:106
                    O0O00O0O0OO0000OO .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if O0000OO00O0O00OOO ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as OOOOOOOO0OO0O0O0O :#line:112
            print (OOOOOOOO0OO0O0O0O )#line:113
    def sealing (OOO0OO0OOOO00OO0O ):#line:116
        try :#line:117
            O000O00OOO00000OO =f'__{timi_new()}'#line:118
            O00OO0OO0OO0OO00O ={'authorization':OOO0OO0OOOO00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00OOO00000OO ),'signstring':O000O00OOO00000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00OO0OO0OO0OO00O )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =O00OO0OO0OO0OO00O )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00OO0OO0OO0OO00O )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00OO0OO0OO0OO00O )#line:131
            requests .request ('get',f'{host}/user',headers =O00OO0OO0OO0OO00O )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00OO0OO0OO0OO00O )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00OO0OO0OO0OO00O )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =O00OO0OO0OO0OO00O )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =O00OO0OO0OO0OO00O )#line:136
            requests .request ('get',f'{host}/assets',headers =O00OO0OO0OO0OO00O )#line:137
        except Exception as OO0OO0OO0000OOOO0 :#line:138
            print (OO0OO0OO0000OOOO0 )#line:139
    def withdraw (O0O00O000000O000O ):#line:143
        OO00OOOOO0OOOOO00 =f'__{timi_new()}'#line:144
        OO0O0OOOO0OOOO0OO ={'authorization':O0O00O000000O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOOO0OOOOO00 ),'signstring':OO00OOOOO0OOOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        O0OOOOOO000OOOO00 =requests .request ('get',f'{host}/assets',headers =OO0O0OOOO0OOOO0OO ).json ()#line:154
        if 'status'in O0OOOOOO000OOOO00 :#line:156
            if O0OOOOOO000OOOO00 ['status']==200 :#line:157
                O0OOOO000OO0O00O0 =O0OOOOOO000OOOO00 ['data']['cash']#line:158
                if float (O0OOOO000OO0O00O0 )>20 :#line:159
                    OO00OOOOO0OOOOO00 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    OO0O0OOOO0OOOO0OO ={'authorization':O0O00O000000O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOOO0OOOOO00 ),'signstring':OO00OOOOO0OOOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    O0O0O0O0OOO0O0O00 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    OOOOOOO00OOOO0O0O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO0O0OOOO0OOOO0OO ,data =O0O0O0O0OOO0O0O00 ).json ()#line:172
                    print (OOOOOOO00OOOO0O0O )#line:173
    def invitenum (OOO0O0O0OO00OOOO0 ):#line:176
        O0OO0OO0O0000OO00 =f'__{timi_new()}'#line:177
        OO00O00000OO000O0 ={'authorization':OOO0O0O0OO00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0O0000OO00 ),'signstring':O0OO0OO0O0000OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O0OO0OOOO000000O0 =requests .request ('get',f'{host}/invite/invitenum',headers =OO00O00000OO000O0 ).json ()#line:187
        if 'status'in O0OO0OOOO000000O0 :#line:189
            if O0OO0OOOO000000O0 ['status']==200 :#line:190
                O000O00OOO00O0O00 =O0OO0OOOO000000O0 ['data']['invited_count']#line:191
                O000000OO000O00OO =O0OO0OOOO000000O0 ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{O000O00OOO00O0O00}丨间邀好友:{O000000OO000O00OO}')#line:193
    def game_map (O0O0O00OO00OO0O0O ):#line:196
        try :#line:197
            OOO00000O00000OOO =f'__{timi_new()}'#line:198
            OOO00O0O00O00OOOO ={'authorization':O0O0O00OO00OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00000O00000OOO ),'signstring':OOO00000O00000OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            OO00OOOO000OO0O0O =requests .request ('get',f'{host}/game/map',headers =OOO00O0O00O00OOOO ).json ()#line:208
            if 'status'in OO00OOOO000OO0O0O :#line:210
                if OO00OOOO000OO0O0O ['status']==200 :#line:211
                    for O0000OO0O000O00OO in OO00OOOO000OO0O0O ['data']['list'][0 ]['crops']:#line:212
                        OO0O000O00OO000OO =O0000OO0O000O00OO ['level']#line:214
                        if OO0O000O00OO000OO ==41 :#line:215
                            OOOO0O0OOOO00O000 =O0000OO0O000O00OO ['crop_name']#line:216
                            O000O00O0OO00O0O0 =O0000OO0O000O00OO ['count']#line:217
                            if O000O00O0OO00O0O0 >0 :#line:218
                                print (f'【农业资产】:{OOOO0O0OOOO00O000}丨数量:{O000O00O0OO00O0O0}')#line:219
        except Exception as O0000OOOOO000O0OO :#line:220
            print (O0000OOOOO000O0OO )#line:221
    def give_gold (O0O0O00O0O000O0O0 ):#line:224
        try :#line:225
            O0O000OO0O00OOOOO =f'__{timi_new()}'#line:226
            OO0000OO00O00O0O0 ={'authorization':O0O0O00O0O000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OO0O00OOOOO ),'signstring':O0O000OO0O00OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            O0OO000O0O0O0O0OO =requests .request ('get',f'{host}/user',headers =OO0000OO00O00O0O0 ).json ()#line:236
            if 'status'in O0OO000O0O0O0O0OO :#line:237
                if O0OO000O0O0O0O0OO ['status']==200 :#line:238
                    if float (O0O0O00O0O000O0O0 .doneeNo )!=0 :#line:239
                        O0000OOOOO00OO00O =O0OO000O0O0O0O0OO ['data']['assets']['gold']#line:240
                        if float (O0000OOOOO00OO00O )>float (O0O0O00O0O000O0O0 .innerId ):#line:241
                            O0000OO0OO000OOO0 =int (float (O0000OOOOO00OO00O )/1.1 )#line:242
                            O0O000OO0O00OOOOO =f'_doneeNo={O0O0O00O0O000O0O0.doneeNo}&quantity={O0000OO0OO000OOO0}_{timi_new()}'#line:243
                            OO0000OO00O00O0O0 ={'authorization':O0O0O00O0O000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OO0O00OOOOO ),'signstring':O0O000OO0O00OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            OO0O00O00O00OOOO0 ={"quantity":O0000OO0OO000OOO0 ,"doneeNo":O0O0O00O0O000O0O0 .doneeNo }#line:256
                            OO0OOO00O0OOOOOO0 =requests .request ('post',f'{host}/finance/give-gold',headers =OO0000OO00O00O0O0 ,data =OO0O00O00O00OOOO0 ).json ()#line:257
                            if 'status'in OO0OOO00O0OOOOOO0 :#line:259
                                if OO0OOO00O0OOOOOO0 ['status']==200 :#line:260
                                    if OO0OOO00O0OOOOOO0 ['data']:#line:261
                                        print (f'【赠送种子】:赠送{O0000OO0OO000OOO0}种子给{O0O0O00O0O000O0O0.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as OO0OOO0000000O000 :#line:265
            print (OO0OOO0000000O000 )#line:266
    def invitation (O0O00O000O0O0OOOO ):#line:268
        try :#line:269
            _OO000OO00O000O000 =float (bundled_def ())/4 #line:270
            OO0000O0O0000O000 =f'_innerId={int(_OO000OO00O000O000)}_{timi_new()}'#line:271
            OOOO00OO0OO000O0O ={'authorization':O0O00O000O0O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O0O0000O000 ),'signstring':OO0000O0O0000O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            O000OO0O00O0OO0O0 ={"innerId":int (_OO000OO00O000O000 )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOO00OO0OO000O0O ,data =O000OO0O00O0OO0O0 )#line:282
        except Exception as O000O00OO0OOOOO0O :#line:283
            print (O000O00OO0OOOOO0O )#line:284
    def winning_rewards (O000OO0O0OOOO00OO ):#line:287
        try :#line:288
            OOOOOOOO000O00000 =f'__{timi_new()}'#line:289
            OOOO000OOO0OO00O0 ={'authorization':O000OO0O0OOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO000O00000 ),'signstring':OOOOOOOO000O00000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            OOOOOO000000O0O0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOOO000OOO0OO00O0 ).json ()#line:299
            if 'status'in OOOOOO000000O0O0O :#line:301
                if OOOOOO000000O0O0O ['status']==200 :#line:302
                    if OOOOOO000000O0O0O ['data']['amount']:#line:303
                        OOO0O0OO0000O000O =OOOOOO000000O0O0O ['data']['amount']['gold']#line:304
                        return OOO0O0OO0000O000O #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as O000OOOOOOO00O0OO :#line:308
            print (O000OOOOOOO00O0OO )#line:309
    def certification (O0O00OOOO000000O0 ):#line:312
        try :#line:313
            OO0000O0O00000O0O =f'__{timi_new()}'#line:314
            O0O0OOO00OO000OOO ={'authorization':O0O00OOOO000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O0O00000O0O ),'signstring':OO0000O0O00000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OO00O00OO0O0OOOOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0O0OOO00OO000OOO ).json ()#line:324
            if 'status'in OO00O00OO0O0OOOOO :#line:326
                if OO00O00OO0O0OOOOO ['status']==200 :#line:327
                    if OO00O00OO0O0OOOOO ['data']['result']:#line:328
                        OOO0OOO000OO00O00 =OO00O00OO0O0OOOOO ['data']['nick_name']#line:329
                        return OOO0OOO000OO00O00 #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as O00OOOOOOO00000OO :#line:333
            print (O00OOOOOOO00000OO )#line:334
    def crops_illustrated (O00OOOO00OOOOO000 ):#line:337
        try :#line:338
            O0O0000O000OOOOOO =f'__{timi_new()}'#line:339
            O0O0OOO00OOO000O0 ={'authorization':O00OOOO00OOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000O000OOOOOO ),'signstring':O0O0000O000OOOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            OOO0000000O0O000O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O0OOO00OOO000O0 ).json ()#line:349
            if 'status'in OOO0000000O0O000O :#line:351
                if OOO0000000O0O000O ['status']==200 :#line:352
                    O00OOO0000OOO0O00 =OOO0000000O0O000O ['data'][0 ]['crops']#line:353
                    for OO0OOOOOO00OOOO0O in O00OOO0000OOO0O00 :#line:354
                        if OO0OOOOOO00OOOO0O ['ill_clover_award']:#line:355
                            if float (OO0OOOOOO00OOOO0O ['ill_clover_award'])>1 :#line:356
                                if OO0OOOOOO00OOOO0O ['is_finish']:#line:357
                                    if not OO0OOOOOO00OOOO0O ['is_getit']:#line:358
                                        if O00OOOO00OOOOO000 .certification ()!='未实名':#line:359
                                            O0O0000O000OOOOOO =f'_award_level={OO0OOOOOO00OOOO0O["level"]}_{timi_new()}'#line:360
                                            O0O0OOO00OOO000O0 ={'authorization':O00OOOO00OOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000O000OOOOOO ),'signstring':O0O0000O000OOOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            OO0000OO00000000O ={"award_level":OO0OOOOOO00OOOO0O ['level']}#line:370
                                            OOO000OOOOOOOO0OO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O0OOO00OOO000O0 ,json =OO0000OO00000000O ).json ()#line:372
                                            if 'status'in OOO000OOOOOOOO0OO :#line:373
                                                if OOO000OOOOOOOO0OO ['status']==200 :#line:374
                                                    O00OO0OOOO0O0O00O =OOO000OOOOOOOO0OO ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{OO0OOOOOO00OOOO0O["crop_name"]}成就丨奖励{O00OO0OOOO0O0O00O}叶子成功')#line:377
                                                if OOO000OOOOOOOO0OO ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{OOO000OOOOOOOO0OO["message"]}')#line:379
        except Exception as O000OOOOO0O0O00O0 :#line:380
            print (O000OOOOO0O0O00O0 )#line:381
    def watched_ad (O0OO0O00OO0OO0000 ):#line:384
        try :#line:385
            OO0OOOOOOOO0O0000 =f'__{timi_new()}'#line:386
            O00O0OOOO00OO0OO0 ={'authorization':O0OO0O00OO0OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOOOOO0O0000 ),'signstring':OO0OOOOOOOO0O0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            OOOOO0O0O0OOOOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O00O0OOOO00OO0OO0 ).json ()#line:396
            if 'status'in OOOOO0O0O0OOOOOO0 :#line:398
                if OOOOO0O0O0OOOOOO0 ['status']==200 :#line:399
                    if 'offlineInfo'in OOOOO0O0O0OOOOOO0 ['data']:#line:400
                        OOOO0OO000000000O =OOOOO0O0O0OOOOOO0 ['data']['offlineInfo']['off_minute']#line:401
                        O000O0O0000OOO000 =float (OOOOO0O0O0OOOOOO0 ['data']['silver'])/1000000000000 #line:402
                        time .sleep (1 )#line:403
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00O0OOOO00OO0OO0 ).json ()#line:404
                        time .sleep (2 )#line:405
                        OO0O0000O0OOO0O00 =requests .request ('get',f'{host}/game/getAllData',headers =O00O0OOOO00OO0OO0 ).json ()#line:406
                        if 'status'in OO0O0000O0OOO0O00 :#line:408
                            if OO0O0000O0OOO0O00 ['status']==200 :#line:409
                                O0O0O000O00OOOOO0 =float (OO0O0000O0OOO0O00 ['data']['silver'])/1000000000000 #line:410
                                OO0OO0000000O00OO =str (O0O0O000O00OOOOO0 -O000O0O0000OOO000 )[:6 ]#line:411
                                print (f'【离线奖励】:翻倍离线{OOOO0OO000000000O}分钟奖励种子数量:{OO0OO0000000O00OO}t粒')#line:412
        except Exception as OO00000OOO00O000O :#line:413
            print (OO00000OOO00O000O )#line:414
    def user_ad (O0OOOO0OO000000OO ):#line:417
        try :#line:418
            OOOO0O0O0OO00000O =f'__{timi_new()}'#line:419
            O00OO0OOOOOO00O0O ={'authorization':O0OOOO0OO000000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O0OO00000O ),'signstring':OOOO0O0O0OO00000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:428
            O00OOOO00OOO0OO00 =requests .request ('get',f'{host}/user/ad',headers =O00OO0OOOOOO00O0O ).json ()#line:429
            if 'status'in O00OOOO00OOO0OO00 :#line:431
                if O00OOOO00OOO0OO00 ['status']==200 :#line:432
                    OOOOO00O00OO00OO0 =O00OOOO00OOO0OO00 ['data']['max_time']#line:433
                    OOOOO0O0O00000000 =O00OOOO00OOO0OO00 ['data']['watch_time']#line:434
                    OO00O00000O0OO0OO =O00OOOO00OOO0OO00 ['data']['added_time']#line:435
                    print (f'【获取种子】:获取种子剩余{OO00O00000O0OO0OO + OOOOO00O00OO00OO0 - OOOOO0O0O00000000}次丨好友提供:{OO00O00000O0OO0OO}次')#line:436
                    if OO00O00000O0OO0OO +OOOOO00O00OO00OO0 -OOOOO0O0O00000000 >0 :#line:437
                        time .sleep (random .randint (16 ,19 ))#line:438
                        OO0O00O0O0O00O0O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00OO0OOOOOO00O0O ).json ()#line:439
                        if 'status'in OO0O00O0O0O00O0O0 :#line:441
                            if OO0O00O0O0O00O0O0 ['status']==200 :#line:442
                                OOO0000OOO0O00O00 =float (OO0O00O0O0O00O0O0 ['data']['silver'])/1000000000000 #line:443
                                print (f'【获取种子】:获得种子:{OOO0000OOO0O00O00}t粒')#line:444
                                return True #line:445
                            if OO0O00O0O0O00O0O0 ['status']==500 :#line:446
                                O00O0OOOOOO0O00OO =OO0O00O0O0O00O0O0 ['message']#line:447
                                print (f'【获取种子】:{O00O0OOOOOO0O00OO}')#line:448
                                return False #line:449
        except Exception as O0OOO0000O00000O0 :#line:450
            print (O0OOO0000O00000O0 )#line:451
    def synthetic (OOOOO000OO0O0000O ):#line:454
        global id ,g #line:455
        try :#line:456
            OOO000O00OOO000O0 =OOOOO000OO0O0000O .level_new ()#line:457
            O00O000OOOOO000O0 =random .randint (9 ,11 )#line:458
            OO0O00OOOO00000OO =f'_site=8&targetSite={O00O000OOOOO000O0}_{timi_new()}'#line:459
            O000O00OO00O0OOO0 ={'accept':'application/json, text/plain, */*','authorization':OOOOO000OO0O0000O .token ,'timestamp':timi_new (),'sign':sign (OO0O00OOOO00000OO ),'signstring':OO0O00OOOO00000OO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:474
            O0O00OOOO00OO0OO0 ={"site":int (8 ),"targetSite":int (O00O000OOOOO000O0 )}#line:475
            requests .request ('post',f'{host}/game/crops/move',headers =O000O00OO00O0OOO0 ,json =O0O00OOOO00OO0OO0 )#line:476
            while True :#line:477
                O00O00O0O0OOO0OO0 =f'__{timi_new()}'#line:478
                OO0OOO00O0O000O0O ={'authorization':OOOOO000OO0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O0OOO0OO0 ),'signstring':O00O00O0O0OOO0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:487
                O0O0O00OOO00OOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOO00O0O000O0O ).json ()#line:488
                if 'status'in O0O0O00OOO00OOOO0 :#line:490
                    if O0O0O00OOO00OOOO0 ['status']==200 :#line:491
                        OO0OO0000000OO0OO =O0O0O00OOO00OOOO0 ['data']['cropList']#line:492
                        OO0OOO0O0OOO000OO =O0O0O00OOO00OOOO0 ['data']['gameCoreDataDBid']#line:493
                        O0OOO0OO0O0OO0O00 =0 #line:494
                        for O000000OO0O0O0OO0 in OO0OO0000000OO0OO :#line:495
                            if not O000000OO0O0O0OO0 :#line:496
                                OO000OO0O00O0O0OO =f'_crop_id={OO0OOO0O0OOO000OO}&site={O0OOO0OO0O0OO0O00}_{OOOOO000OO0O0000O.time}'#line:497
                                OOO00OOOO0000OO00 ={'authorization':OOOOO000OO0O0000O .token ,'timestamp':OOOOO000OO0O0000O .time ,'sign':sign (OO000OO0O00O0O0OO ),'signstring':OO000OO0O00O0O0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:506
                                O000O000OO0O0OOOO ={"site":O0OOO0OO0O0OO0O00 ,"crop_id":OO0OOO0O0OOO000OO }#line:507
                                OO0OOOOO000OO0000 =requests .request ('post',f'{host}/game/crops/buy',headers =OOO00OOOO0000OO00 ,data =O000O000OO0O0OOOO ).json ()#line:508
                                time .sleep (random .randint (1 ,3 )/10 )#line:510
                                if 'status'in OO0OOOOO000OO0000 :#line:511
                                    if OO0OOOOO000OO0000 ['status']==200 :#line:512
                                        if OO0OOOOO000OO0000 ['message']=='种子数量不足':#line:513
                                            OOO000O00OOO000O0 =OOOOO000OO0O0000O .level_new ()#line:514
                                            print (f'【种植合成】:{OO0OOOOO000OO0000["message"]}')#line:515
                                            if not OOOOO000OO0O0000O .user_ad ():#line:516
                                                return False #line:517
                                    if OO0OOOOO000OO0000 ['status']==500 :#line:518
                                        print (f'【种植合成】:{OO0OOOOO000OO0000["message"]}')#line:519
                                        return False #line:520
                            O0OOO0OO0O0OO0O00 +=1 #line:521
                        OOO00O0OOO0O0OO0O =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOO00O0O000O0O ).json ()#line:522
                        O00O000OO00OOOOOO =OOO00O0OOO0O0OO0O ['data']['cropList']#line:523
                        O00O0OO0OO00000OO =False #line:524
                        for O000000OO0O0O0OO0 in range (12 ):#line:525
                            id =O00O000OO00OOOOOO [O000000OO0O0O0OO0 ]['level']#line:526
                            if float (OOO000O00OOO000O0 )-float (id )>9 :#line:527
                                OOO00O0OO0000OO00 =f'_site={O000000OO0O0O0OO0}_{timi_new()}'#line:528
                                O000O0O0O00OO0O00 ={'accept':'application/json, text/plain, */*','authorization':OOOOO000OO0O0000O .token ,'timestamp':timi_new (),'sign':sign (OOO00O0OO0000OO00 ),'signstring':OOO00O0OO0000OO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:538
                                O00OO0OOOO00OOOOO ={"site":O000000OO0O0O0OO0 }#line:539
                                O0O0OOOOOOO00OOOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000O0O0O00OO0O00 ,data =O00OO0OOOO00OOOOO ).json ()#line:541
                                if 'status'in O0O0OOOOOOO00OOOO :#line:542
                                    if O0O0OOOOOOO00OOOO ['status']==200 :#line:543
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:544
                            if id !=0 :#line:545
                                for O00O0OOOO0O00OOO0 in range (11 ):#line:546
                                    O0O0O0OOOO0OO000O =O00O0OOOO0O00OOO0 +1 #line:547
                                    g =O00O000OO00OOOOOO [O0O0O0OOOO0OO000O ]['level']#line:548
                                    if id ==g :#line:549
                                        O0OO00OOOO0000O00 =O00O0OOOO0O00OOO0 +2 #line:550
                                        if O0OO00OOOO0000O00 !=O000000OO0O0O0OO0 +1 :#line:551
                                            OO00O00OOO00O00O0 =O000000OO0O0O0OO0 +1 #line:552
                                            time .sleep (random .randint (1 ,3 )/10 )#line:554
                                            OO0O00OOOO00000OO =f'_site={OO00O00OOO00O00O0 - 1}&targetSite={O0OO00OOOO0000O00 - 1}_{timi_new()}'#line:555
                                            O000O00OO00O0OOO0 ={'accept':'application/json, text/plain, */*','authorization':OOOOO000OO0O0000O .token ,'timestamp':timi_new (),'sign':sign (OO0O00OOOO00000OO ),'signstring':OO0O00OOOO00000OO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:570
                                            O000OO00O000O0000 ={"site":int (OO00O00OOO00O00O0 -1 ),"targetSite":int (O0OO00OOOO0000O00 -1 )}#line:571
                                            requests .request ('post',f'{host}/game/crops/move',headers =O000O00OO00O0OOO0 ,json =O000OO00O000O0000 )#line:572
                                            print (f'【种植合成】:位置{OO00O00OOO00O00O0}和位置{O0OO00OOOO0000O00}合出{int(id) + 1}级农作物')#line:573
                                            O00O0OO0OO00000OO =True #line:574
                                    if O00O0OO0OO00000OO :#line:575
                                        break #line:576
                                if O00O0OO0OO00000OO :#line:577
                                    break #line:578
        except :#line:579
            OOOOO000OO0O0000O .synthetic ()#line:580
    def level_new (OOOO0O0OO000OO000 ):#line:583
        try :#line:584
            OOOO0O0OOOO0OO00O =f'__{timi_new()}'#line:585
            OO0O0000O000OOO00 ={'authorization':OOOO0O0OO000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0OOOO0OO00O ),'signstring':OOOO0O0OOOO0OO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:594
            OO00OO000OO00000O =requests .request ('get',f'{host}/user',headers =OO0O0000O000OOO00 ).json ()#line:595
            if 'status'in OO00OO000OO00000O :#line:596
                if OO00OO000OO00000O ['status']==200 :#line:597
                    return float (OO00OO000OO00000O ['data']['level'])#line:598
        except Exception as O00OO00OOO00O000O :#line:599
            print (O00OO00OOO00O000O )#line:600
    def propsraffle (OO0000OOO00OOOOOO ):#line:603
        try :#line:604
            while True :#line:605
                OOOO000O00OOOOO00 =f'__{timi_new()}'#line:606
                O00000O0O000OOOO0 ={'authorization':OO0000OOO00OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O00OOOOO00 ),'signstring':OOOO000O00OOOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:615
                OO0000O0OO000O00O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00000O0O000OOOO0 ).json ()#line:616
                if 'status'in OO0000O0OO000O00O :#line:618
                    if OO0000O0OO000O00O ['status']==200 :#line:619
                        OO0O0000O0OO0OO00 =OO0000O0OO000O00O ['data']['rows']#line:620
                        OOO0OOO000O0OO000 =OO0000O0OO000O00O ['data']['vstate']#line:621
                        if OO0O0000O0OO0OO00 ==5 or OO0O0000O0OO0OO00 ==6 or OO0O0000O0OO0OO00 ==7 :#line:622
                            OO0O000OO0O000OOO =OO0000O0OO000O00O ['data']['silver']#line:623
                            print (f'【转盘抽奖】:获得种子:{OO0O000OO0O000OOO}')#line:624
                        if OO0O0000O0OO0OO00 ==1 or OO0O0000O0OO0OO00 ==2 or OO0O0000O0OO0OO00 ==3 :#line:625
                            OO0OOO0O0O00O0O00 =OO0000O0OO000O00O ['data']['clover']#line:626
                            print (f'【转盘抽奖】:获得三叶草:{OO0OOO0O0O00O0O00}')#line:627
                        if OO0O0000O0OO0OO00 ==4 or OO0O0000O0OO0OO00 ==8 :#line:628
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:629
                        if OO0O0000O0OO0OO00 =='抽奖次数已用完':#line:633
                            break #line:666
                time .sleep (random .randint (8 ,15 )/10 )#line:667
        except Exception as O0O0OOO0OOOO000OO :#line:668
            print (O0O0OOO0OOOO000OO )#line:669
    def friends_invitation (O0O000O000O00OO0O ):#line:672
        try :#line:673
            O00OO000OOOO0O00O =f'__{timi_new()}'#line:674
            OOOOOO0OOO0OOO00O ={'authorization':O0O000O000O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000OOOO0O00O ),'signstring':O00OO000OOOO0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:683
            O0OO000OO00000OOO =requests .request ('get',f'{host}/friends',headers =OOOOOO0OOO0OOO00O ).json ()#line:684
            if 'status'in O0OO000OO00000OOO :#line:685
                if O0OO000OO00000OOO ['status']==200 :#line:686
                    O000OOO0000OOOOO0 =O0OO000OO00000OOO ['data']['myInviteter']#line:687
                    if O000OOO0000OOOOO0 :#line:688
                        OOOO0O0OO0OOO0O00 =O000OOO0000OOOOO0 ['user']['nickname']#line:689
                        O000O00O000OO0O00 =O0O000O000O00OO0O .certification ()#line:690
                        print (f'【查邀请人】:我的邀请人:{OOOO0O0OO0OOO0O00}丨实名:{O000O00O000OO0O00}')#line:691
                    else :#line:692
                        if O0O000O000O00OO0O .innerId !='0':#line:693
                            O0O000O000O00OO0O .invitation ()#line:694
        except Exception as OOOO0O0000O00OO00 :#line:695
            print (OOOO0O0000O00OO00 )#line:696
    def add_clover (OOOO00OOO00OO0000 ):#line:699
        global golden_seed #line:700
        try :#line:701
            O000000O000O0O00O =f'__{timi_new()}'#line:702
            OOO0O000O0OO000O0 ={'authorization':OOOO00OOO00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O000O0O00O ),'signstring':O000000O000O0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:711
            OOO0O00O000O0OO0O =requests .request ('get',f'{host}/assets/clovers',headers =OOO0O000O0OO000O0 ).json ()#line:712
            if 'status'in OOO0O00O000O0OO0O :#line:714
                if OOO0O00O000O0OO0O ['status']==200 :#line:715
                    OO0OOO0000O0O00O0 =OOO0O00O000O0OO0O ['data']['clover']#line:716
                    OOO0OOO0O0O0OO000 =OOO0O00O000O0OO0O ['data']['used_clover']#line:717
                    OOOOOO0O0O00OO0O0 =float (OO0OOO0000O0O00O0 )-float (OOO0OOO0O0O0OO000 )#line:718
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OOO0OOO0O0O0OO000}')#line:719
                    if OOOO00OOO00OO0000 .certification ()!='未实名':#line:720
                        if OOOOOO0O0O00OO0O0 >1 :#line:721
                            O000000O000O0O00O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOOOO0O0O00OO0O0)}_{timi_new()}'#line:722
                            O00OOO0O0OOO000OO ={'authorization':OOOO00OOO00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O000O0O00O ),'signstring':O000000O000O0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:731
                            O0000OOOOOOOO0000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOOOO0O0O00OO0O0 )}#line:732
                            OOOOO000OOOO0OO00 =requests .request ('post',f'{host}/lottery/add-stake',headers =O00OOO0O0OOO000OO ,data =O0000OOOOOOOO0000 ).json ()#line:733
                            if 'status'in OOOOO000OOOO0OO00 :#line:735
                                if OOOOO000OOOO0OO00 ['status']==200 :#line:736
                                    print (f'【参与抽奖】:添加三叶草:{OOOOO000OOOO0OO00["data"]}丨数量:{OOOOOO0O0O00OO0O0}')#line:737
                                if OOOOO000OOOO0OO00 ['status']==500 :#line:738
                                    print (f'【参与抽奖】:添加三叶草:{OOOOO000OOOO0OO00["message"]}')#line:739
            O0O0O00OOO0OOOOOO =requests .request ('get',f'{host}/lottery',headers =OOO0O000O0OO000O0 ).json ()#line:740
            O0OO00O0000000O00 =OOOO00OOO00OO0000 .winning_rewards ()#line:742
            if 'status'in O0O0O00OOO0OOOOOO :#line:743
                if O0O0O00OOO0OOOOOO ['status']==200 :#line:744
                    O00O00000O00O00O0 =O0O0O00OOO0OOOOOO ['data'][0 ]['day_get_gold_quantity']#line:745
                    golden_seed +=float (O00O00000O00O00O0 )#line:746
                    print (f'【参与抽奖】:预计每天中{str(O00O00000O00O00O0)[:6]}颗金种子丨好友收益:{str(O0OO00O0000000O00)[:6]}')#line:747
        except Exception as OO000OO00O000000O :#line:748
            print (OO000OO00O000000O )#line:749
    def energy (OO0O0OOO0OO0OOO0O ):#line:753
        try :#line:754
            while True :#line:755
                OOOOO0OO0OOOOOOOO =f'__{timi_new()}'#line:756
                OO0OOOOOO00O000OO ={'authorization':OO0O0OOO0OO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OO0OOOOOOOO ),'signstring':OOOOO0OO0OOOOOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:765
                OOOOOO000OO0O0O0O =requests .request ('get',f'{host}/energy/general',headers =OO0OOOOOO00O000OO ).json ()#line:766
                if 'status'in OOOOOO000OO0O0O0O :#line:768
                    if OOOOOO000OO0O0O0O ['status']==200 :#line:769
                        O00OOOOOOOOO00O00 =OOOOOO000OO0O0O0O ['data']['ordinary_water']#line:770
                        O000OOO000OO00O00 =OOOOOO000OO0O0O0O ['data']['ordinary_fertilizer']#line:771
                        print (f'【我的营养】:肥料:{str(O000OOO000OO00O00).split(".")[0]}丨水滴:{str(O00OOOOOOOOO00O00).split(".")[0]}')#line:773
                        if float (O000OOO000OO00O00 )<96 :#line:774
                            time .sleep (random .randint (160 ,180 )/10 )#line:775
                            O0O0OO00OOO00O0O0 =99 -float (O000OOO000OO00O00 )#line:776
                            O00OOO0O0OO00000O ={"fertilizer":str (O0O0OO00OOO00O0O0 ).split ('.')[0 ]}#line:777
                            OOOO0OOOO00OO0000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0OOOOOO00O000OO ).json ()#line:778
                            if 'status'in OOOO0OOOO00OO0000 :#line:780
                                if OOOO0OOOO00OO0000 ['status']==200 :#line:781
                                    print (f'【购买肥料】:看广告获取肥料:{OOOO0OOOO00OO0000["message"]}')#line:782
                        if float (O00OOOOOOOOO00O00 )<880 :#line:783
                            time .sleep (random .randint (160 ,180 )/10 )#line:784
                            O0OO0O0OOOO0000OO =999 -float (O00OOOOOOOOO00O00 )#line:785
                            O000O00OOOOOOO00O ={"water":str (O0OO0O0OOOO0000OO ).split ('.')[0 ]}#line:786
                            O0000OO0OOO0OO0O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0OOOOOO00O000OO ).json ()#line:787
                            if 'status'in O0000OO0OOO0OO0O0 :#line:789
                                if O0000OO0OOO0OO0O0 ['status']==200 :#line:790
                                    print (f'【购买水滴】:看广告获取水滴:{O0000OO0OOO0OO0O0["message"]}')#line:791
                        if float (O000OOO000OO00O00 )>96 and float (O00OOOOOOOOO00O00 )>880 :#line:792
                            break #line:793
        except Exception as O0O0O0O0OOOO00OOO :#line:795
            print (O0O0O0O0OOOO00OOO )#line:796
def bundled_def ():#line:798
    O0O0O0OO0OOO000O0 =['5570536','7750212','7911652','7911680','7805624']#line:799
    return O0O0O0OO0OOO000O0 [random .randint (0 ,len (O0O0O0OO0OOO000O0 )-1 )]#line:800
def version_of_the_validation ():#line:804
    return str ((77 -56 )/10 )#line:805
def gitee_validation ():#line:808
    try :#line:809
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:810
    except :#line:811
        sys .exit (0 )#line:812
def update_the_validation ():#line:816
    try :#line:817
        O00OO000O00O0OO00 =gitee_validation ()#line:818
        if version_of_the_validation ()<O00OO000O00O0OO00 ['CityEarth']['edition']:#line:819
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OO000O00O0OO00["CityEarth"]["edition"]}   ❌')#line:820
            print (f'更新内容=>>{O00OO000O00O0OO00["CityEarth"]["content"]}   👍')#line:821
        else :#line:822
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OO000O00O0OO00["CityEarth"]["edition"]}   ✅')#line:823
            print (f'更新内容=>> {O00OO000O00O0OO00["CityEarth"]["content"]}   👍')#line:824
    except Exception as O0OO0O0000O0O000O :#line:825
        print (O0OO0O0000O0O000O )#line:826
def os_qinglong ():#line:829
    if application in os .environ :#line:830
        OOO0000OO000OOOOO =os .environ [application ].split ('\n')#line:831
        if len (OOO0000OO000OOOOO )>0 :#line:832
            return OOO0000OO000OOOOO #line:833
        else :#line:834
            print (f"{application}变量未启用")#line:835
            print ('脚本退出')#line:836
            sys .exit (1 )#line:837
    else :#line:838
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:840
        return os_built ()#line:841
def os_built ():#line:844
    if token :#line:845
        OO00O00O00O00O0OO =token .split ('\n')#line:846
        if len (OO00O00O00O00O0OO )>0 :#line:847
            return OO00O00O00O00O0OO #line:848
    else :#line:849
        print (f"内置变量为空")#line:850
        print ('脚本结束')#line:851
        sys .exit (0 )#line:852
if __name__ =='__main__':#line:855
    start ()#line:856
