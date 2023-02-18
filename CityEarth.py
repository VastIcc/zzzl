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
@ 版本  2.4
"""
application = 'ce_token'  # 变量名
token = ''''''
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
        O00OO0O00O000O0O0 =os_qinglong ()#line:10
        print (f"==========共找到{len(O00OO0O00O000O0O0)}个账号==========")#line:11
        for OO0OO00OOO0OOOOO0 in O00OO0O00O000O0O0 :#line:12
            OO00O0OOO0O00OO0O =[]#line:13
            print (f"------------正在执行第{O00OO0O00O000O0O0.index(OO0OO00OOO0OOOOO0) + 1}个账号------------")#line:14
            OO000000OO0OO0OOO =CityEarth (OO0OO00OOO0OOOOO0 ,OO00O0OOO0O00OO0O )#line:15
            def OOO0O0O0O0000OOOO ():#line:17
                if OO000000OO0OO0OOO .base_info ():#line:19
                    OO000000OO0OO0OOO .sealing ()#line:21
                    OO000000OO0OO0OOO .invitenum ()#line:23
                    OO000000OO0OO0OOO .game_map ()#line:25
                    OO000000OO0OO0OOO .friends_invitation ()#line:27
                    OO000000OO0OO0OOO .add_clover ()#line:29
                    OO000000OO0OO0OOO .propsraffle ()#line:31
                    OO000000OO0OO0OOO .synthetic ()#line:33
                    OO000000OO0OO0OOO .crops_illustrated ()#line:35
                    OO000000OO0OO0OOO .give_gold ()#line:37
                    OO000000OO0OO0OOO .withdraw ()#line:39
                    OO000000OO0OO0OOO .energy ()#line:41
            OO0000000OOOOO0O0 =threading .Thread (target =OOO0O0O0O0000OOOO )#line:42
            OO0000000OOOOO0O0 .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        OOO0O0O0O0OO000O0 =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOO0O0O0O0OO000O0 +' ')#line:48
    except Exception as O0O0O0OO000000OO0 :#line:49
        print (O0O0O0OO000000OO0 )#line:50
def sign (OO000OO0OO0OOOOO0 ):#line:53
    O0000000OO0000OOO =hashlib .md5 (OO000OO0OO0OOOOO0 .encode ()).hexdigest ()#line:54
    O00O000000OOO00OO ="scsc%^&*"+O0000000OO0000OOO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    O000O000OOO00OOOO =hashlib .md5 (O00O000000OOO00OO .encode ()).hexdigest ()#line:56
    return O000O000OOO00OOOO #line:57
def format_msg ():#line:59
    O0O0O0000OOO000OO =""#line:60
    for OOOOO000000OOO0OO in msg_list :#line:61
        O0O0O0000OOO000OO +=str (OOOOO000000OOO0OO )+"\r\n"#line:62
    return O0O0O0000OOO000OO #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (O00000O00OOO0OO0O ,O0O0O000000OO0OOO ,OOOOO00OO00OO0000 ):#line:71
        try :#line:72
            O00000O00OOO0OO0O .msg =OOOOO00OO00OO0000 #line:73
            O00000O00OOO0OO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            O00000O00OOO0OO0O .token =O0O0O000000OO0OOO .split ('&')[0 ]#line:75
            O00000O00OOO0OO0O .innerId =O0O0O000000OO0OOO .split ('&')[1 ]#line:76
            O00000O00OOO0OO0O .doneeNo =O0O0O000000OO0OOO .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (O0OO0O0O0000OOOOO ):#line:82
        try :#line:83
            O0OO0O0O0000OOOOO .watched_ad ()#line:85
            O0OOO0O0000OO0O0O =f'__{timi_new()}'#line:86
            OOO0O00OO000OOO0O ={'authorization':O0OO0O0O0000OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O0000OO0O0O ),'signstring':O0OOO0O0000OO0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            O0OOO0O0OO00OOO00 =requests .request ('get',f'{host}/user',headers =OOO0O00OO000OOO0O ).json ()#line:96
            if 'status'in O0OOO0O0OO00OOO00 :#line:98
                if O0OOO0O0OO00OOO00 ['status']==200 :#line:99
                    O0O000OOO0O0O0000 =O0OOO0O0OO00OOO00 ['data']['nickname']#line:100
                    O00OOOO0OO00OOOOO =O0OOO0O0OO00OOO00 ['data']['inner_id']#line:101
                    OO0OOOO0OO0000O00 =O0OOO0O0OO00OOO00 ['data']['assets']['gold']#line:102
                    OO0O0000O00000OO0 =O0OOO0O0OO00OOO00 ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{O0O000OOO0O0O0000[:5]}丨ID:{O00OOOO0OO00OOOOO}丨等级:{OO0O0000O00000OO0}丨金种子:{str(OO0OOOO0OO0000O00).split(".")[0]}')#line:104
                if O0OOO0O0OO00OOO00 ['status']==401 :#line:105
                    print (O0OOO0O0OO00OOO00 ['message'])#line:106
                    O0OO0O0O0000OOOOO .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if O0OOO0O0OO00OOO00 ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as O0O0OO0O0OO000O0O :#line:112
            print (O0O0OO0O0OO000O0O )#line:113
    def sealing (OOOO00000O0000OOO ):#line:116
        try :#line:117
            OO000OO0O0O000O0O =f'__{timi_new()}'#line:118
            OO0O00O0O000O0OOO ={'authorization':OOOO00000O0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0O0O000O0O ),'signstring':OO000OO0O0O000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0O00O0O000O0OOO )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =OO0O00O0O000O0OOO )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0O00O0O000O0OOO )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0O00O0O000O0OOO )#line:131
            requests .request ('get',f'{host}/user',headers =OO0O00O0O000O0OOO )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0O00O0O000O0OOO )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0O00O0O000O0OOO )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0O00O0O000O0OOO )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =OO0O00O0O000O0OOO )#line:136
            requests .request ('get',f'{host}/assets',headers =OO0O00O0O000O0OOO )#line:137
        except Exception as OO00O00OO00O0OOO0 :#line:138
            print (OO00O00OO00O0OOO0 )#line:139
    def withdraw (OO000OO0OOOOO00OO ):#line:143
        O0OO0OOO000OO0000 =f'__{timi_new()}'#line:144
        OO0OOO00OOOOOO000 ={'authorization':OO000OO0OOOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO000OO0000 ),'signstring':O0OO0OOO000OO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        OOO0O000O00OOO0O0 =requests .request ('get',f'{host}/assets',headers =OO0OOO00OOOOOO000 ).json ()#line:154
        if 'status'in OOO0O000O00OOO0O0 :#line:156
            if OOO0O000O00OOO0O0 ['status']==200 :#line:157
                O0OO000O000O00OOO =OOO0O000O00OOO0O0 ['data']['cash']#line:158
                if float (O0OO000O000O00OOO )>20 :#line:159
                    O0OO0OOO000OO0000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    OO0OOO00OOOOOO000 ={'authorization':OO000OO0OOOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO000OO0000 ),'signstring':O0OO0OOO000OO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    OO0OO0O000O00O00O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    OO000O00O0OOO0OO0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO0OOO00OOOOOO000 ,data =OO0OO0O000O00O00O ).json ()#line:172
                    print (OO000O00O0OOO0OO0 )#line:173
    def invitenum (OOO00O0OO0000OO0O ):#line:176
        O000OO0O000OOOOOO =f'__{timi_new()}'#line:177
        O000OO00O00O000O0 ={'authorization':OOO00O0OO0000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O000OOOOOO ),'signstring':O000OO0O000OOOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O0O00OOO00O0OOOO0 =requests .request ('get',f'{host}/invite/invitenum',headers =O000OO00O00O000O0 ).json ()#line:187
        if 'status'in O0O00OOO00O0OOOO0 :#line:189
            if O0O00OOO00O0OOOO0 ['status']==200 :#line:190
                OO00OOO0OO000OO0O =O0O00OOO00O0OOOO0 ['data']['invited_count']#line:191
                OO00O00O0OO00O000 =O0O00OOO00O0OOOO0 ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OO00OOO0OO000OO0O}丨间邀好友:{OO00O00O0OO00O000}')#line:193
    def game_map (O00OO0000O000O00O ):#line:196
        try :#line:197
            O0OOOO000OOO00O0O =f'__{timi_new()}'#line:198
            O000O00O000O000OO ={'authorization':O00OO0000O000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO000OOO00O0O ),'signstring':O0OOOO000OOO00O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            OO0OOOOOO00O00O0O =requests .request ('get',f'{host}/game/map',headers =O000O00O000O000OO ).json ()#line:208
            if 'status'in OO0OOOOOO00O00O0O :#line:210
                if OO0OOOOOO00O00O0O ['status']==200 :#line:211
                    for OO00O00OOO00O0OOO in OO0OOOOOO00O00O0O ['data']['list'][0 ]['crops']:#line:212
                        O000O0OOOO00O0O0O =OO00O00OOO00O0OOO ['level']#line:214
                        if O000O0OOOO00O0O0O ==41 :#line:215
                            O00OO0O0000O0O0OO =OO00O00OOO00O0OOO ['crop_name']#line:216
                            OO0OO00O000O00O0O =OO00O00OOO00O0OOO ['count']#line:217
                            if OO0OO00O000O00O0O >0 :#line:218
                                print (f'【农业资产】:{O00OO0O0000O0O0OO}丨数量:{OO0OO00O000O00O0O}')#line:219
        except Exception as OOO000O0OOOO0O0O0 :#line:220
            print (OOO000O0OOOO0O0O0 )#line:221
    def give_gold (O000OOO000000O00O ):#line:224
        try :#line:225
            O000OO00O00000O0O =f'__{timi_new()}'#line:226
            OO0OOOOO0OOO0OOO0 ={'authorization':O000OOO000000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00O00000O0O ),'signstring':O000OO00O00000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            OO0OOO0OO00OOO0OO =requests .request ('get',f'{host}/user',headers =OO0OOOOO0OOO0OOO0 ).json ()#line:236
            if 'status'in OO0OOO0OO00OOO0OO :#line:237
                if OO0OOO0OO00OOO0OO ['status']==200 :#line:238
                    if float (O000OOO000000O00O .doneeNo )!=0 :#line:239
                        OO00O0000O0OOO00O =OO0OOO0OO00OOO0OO ['data']['assets']['gold']#line:240
                        if float (OO00O0000O0OOO00O )>float (O000OOO000000O00O .innerId ):#line:241
                            O0O0OO0000OO0O0O0 =int (float (OO00O0000O0OOO00O )/1.1 )#line:242
                            O000OO00O00000O0O =f'_doneeNo={O000OOO000000O00O.doneeNo}&quantity={O0O0OO0000OO0O0O0}_{timi_new()}'#line:243
                            OO0OOOOO0OOO0OOO0 ={'authorization':O000OOO000000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00O00000O0O ),'signstring':O000OO00O00000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            O0O0OOOOOO0OO000O ={"quantity":O0O0OO0000OO0O0O0 ,"doneeNo":O000OOO000000O00O .doneeNo }#line:256
                            O000OO00O0OOOOOOO =requests .request ('post',f'{host}/finance/give-gold',headers =OO0OOOOO0OOO0OOO0 ,data =O0O0OOOOOO0OO000O ).json ()#line:257
                            if 'status'in O000OO00O0OOOOOOO :#line:259
                                if O000OO00O0OOOOOOO ['status']==200 :#line:260
                                    if O000OO00O0OOOOOOO ['data']:#line:261
                                        print (f'【赠送种子】:赠送{O0O0OO0000OO0O0O0}种子给{O000OOO000000O00O.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as OO0OOOOO000OO0000 :#line:265
            print (OO0OOOOO000OO0000 )#line:266
    def invitation (O000OO00OO00O0O00 ):#line:268
        try :#line:269
            _OO0OO000O0000OOO0 =float (bundled_def ())/4 #line:270
            OO00000O0OO0O0000 =f'_innerId={int(_OO0OO000O0000OOO0)}_{timi_new()}'#line:271
            OOOOOO0O000OO00O0 ={'authorization':O000OO00OO00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000O0OO0O0000 ),'signstring':OO00000O0OO0O0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            O00000O000OOO0000 ={"innerId":int (_OO0OO000O0000OOO0 )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOOOO0O000OO00O0 ,data =O00000O000OOO0000 )#line:282
        except Exception as O00O0O0O0OOO0O000 :#line:283
            print (O00O0O0O0OOO0O000 )#line:284
    def winning_rewards (OO00OOOOOO0O000O0 ):#line:287
        try :#line:288
            OO0OOOOO0O0000O0O =f'__{timi_new()}'#line:289
            O000OO0OOO0OOOO0O ={'authorization':OO00OOOOOO0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO0O0000O0O ),'signstring':OO0OOOOO0O0000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            O0O00OO00OOOOO00O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O000OO0OOO0OOOO0O ).json ()#line:299
            if 'status'in O0O00OO00OOOOO00O :#line:301
                if O0O00OO00OOOOO00O ['status']==200 :#line:302
                    if O0O00OO00OOOOO00O ['data']['amount']:#line:303
                        OO00000O000OOOO0O =O0O00OO00OOOOO00O ['data']['amount']['gold']#line:304
                        return OO00000O000OOOO0O #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as O00O00000O00OOOOO :#line:308
            print (O00O00000O00OOOOO )#line:309
    def certification (O0OO0OO00O0O000OO ):#line:312
        try :#line:313
            OOO0O000OO00OOO00 =f'__{timi_new()}'#line:314
            OO0OOOOOOOOO00O00 ={'authorization':O0OO0OO00O0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000OO00OOO00 ),'signstring':OOO0O000OO00OOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OO00OOO000O000O0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0OOOOOOOOO00O00 ).json ()#line:324
            if 'status'in OO00OOO000O000O0O :#line:326
                if OO00OOO000O000O0O ['status']==200 :#line:327
                    if OO00OOO000O000O0O ['data']['result']:#line:328
                        O00O0000OO000OOOO =OO00OOO000O000O0O ['data']['nick_name']#line:329
                        return O00O0000OO000OOOO #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as O00O0OO0O0OOO000O :#line:333
            print (O00O0OO0O0OOO000O )#line:334
    def crops_illustrated (OO0OOOO0O000OOOOO ):#line:337
        try :#line:338
            OOOOO0OOO000O0OO0 =f'__{timi_new()}'#line:339
            O0O0OOOOO000OO0O0 ={'authorization':OO0OOOO0O000OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOO000O0OO0 ),'signstring':OOOOO0OOO000O0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            OO0OOOOOO0OO00OO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O0OOOOO000OO0O0 ).json ()#line:349
            if 'status'in OO0OOOOOO0OO00OO0 :#line:351
                if OO0OOOOOO0OO00OO0 ['status']==200 :#line:352
                    OO000O0OO000000OO =OO0OOOOOO0OO00OO0 ['data'][0 ]['crops']#line:353
                    for O0OOOO0OOO0O00OO0 in OO000O0OO000000OO :#line:354
                        if O0OOOO0OOO0O00OO0 ['ill_clover_award']:#line:355
                            if float (O0OOOO0OOO0O00OO0 ['ill_clover_award'])>1 :#line:356
                                if O0OOOO0OOO0O00OO0 ['is_finish']:#line:357
                                    if not O0OOOO0OOO0O00OO0 ['is_getit']:#line:358
                                        if OO0OOOO0O000OOOOO .certification ()!='未实名':#line:359
                                            OOOOO0OOO000O0OO0 =f'_award_level={O0OOOO0OOO0O00OO0["level"]}_{timi_new()}'#line:360
                                            O0O0OOOOO000OO0O0 ={'authorization':OO0OOOO0O000OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOO000O0OO0 ),'signstring':OOOOO0OOO000O0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            OO0OO00O0OOO00000 ={"award_level":O0OOOO0OOO0O00OO0 ['level']}#line:370
                                            OOO0O0O00OO00O00O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O0OOOOO000OO0O0 ,json =OO0OO00O0OOO00000 ).json ()#line:372
                                            if 'status'in OOO0O0O00OO00O00O :#line:373
                                                if OOO0O0O00OO00O00O ['status']==200 :#line:374
                                                    O0OO0OO0OO0OO0000 =OOO0O0O00OO00O00O ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{O0OOOO0OOO0O00OO0["crop_name"]}成就丨奖励{O0OO0OO0OO0OO0000}☘️')#line:377
                                                if OOO0O0O00OO00O00O ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{OOO0O0O00OO00O00O["message"]}')#line:379
        except Exception as OOO00OOO0OOOO000O :#line:380
            print (OOO00OOO0OOOO000O )#line:381
    def watched_ad (O00OOO00O0O00OO00 ):#line:384
        try :#line:385
            O0O000O00OOOO0O00 =f'__{timi_new()}'#line:386
            OOOO0O00OOO0O0O00 ={'authorization':O00OOO00O0O00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000O00OOOO0O00 ),'signstring':O0O000O00OOOO0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            OOO0O000O0OO0OOOO =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0O00OOO0O0O00 ).json ()#line:396
            if 'status'in OOO0O000O0OO0OOOO :#line:398
                if OOO0O000O0OO0OOOO ['status']==200 :#line:399
                    if 'offlineInfo'in OOO0O000O0OO0OOOO ['data']:#line:400
                        time .sleep (random .randint (5 ,8 ))#line:401
                        O00O00OOO000O000O =OOO0O000O0OO0OOOO ['data']['offlineInfo']['off_minute']#line:402
                        O00O000O00O0O0O0O =float (OOO0O000O0OO0OOOO ['data']['silver'])/1000000000000 #line:403
                        time .sleep (1 )#line:404
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOOO0O00OOO0O0O00 ).json ()#line:405
                        time .sleep (2 )#line:406
                        OO000OOO0O0O0OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0O00OOO0O0O00 ).json ()#line:407
                        if 'status'in OO000OOO0O0O0OOO0 :#line:409
                            if OO000OOO0O0O0OOO0 ['status']==200 :#line:410
                                O00OO00O0OOOO0O0O =float (OO000OOO0O0O0OOO0 ['data']['silver'])/1000000000000 #line:411
                                O000O00000OO00OO0 =str (O00OO00O0OOOO0O0O -O00O000O00O0O0O0O )[:6 ]#line:412
                                print (f'【离线奖励】:翻倍离线{O00O00OOO000O000O}分钟奖励🌱数量:{O000O00000OO00OO0}t粒')#line:413
        except Exception as O0OOO00OO0OOO00OO :#line:414
            print (O0OOO00OO0OOO00OO )#line:415
    def user_ad (O0O0O0000OO000O0O ):#line:418
        try :#line:419
            OOO00O0O00O0OOOOO =f'__{timi_new()}'#line:420
            O0O000O0O0O0O0O00 ={'authorization':O0O0O0000OO000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0O00O0OOOOO ),'signstring':OOO00O0O00O0OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:429
            O00OO000O000OO0OO =requests .request ('get',f'{host}/user/ad',headers =O0O000O0O0O0O0O00 ).json ()#line:430
            if 'status'in O00OO000O000OO0OO :#line:432
                if O00OO000O000OO0OO ['status']==200 :#line:433
                    OO0OO0OO000OO0OOO =O00OO000O000OO0OO ['data']['max_time']#line:434
                    O00000O00O0OO00O0 =O00OO000O000OO0OO ['data']['watch_time']#line:435
                    OOOOOO0OOO0O00000 =O00OO000O000OO0OO ['data']['added_time']#line:436
                    print (f'【获取种子】:获取🌱剩余{OOOOOO0OOO0O00000 + OO0OO0OO000OO0OOO - O00000O00O0OO00O0}次丨好友提供:{OOOOOO0OOO0O00000}次')#line:437
                    if OOOOOO0OOO0O00000 +OO0OO0OO000OO0OOO -O00000O00O0OO00O0 >0 :#line:438
                        time .sleep (random .randint (16 ,19 ))#line:439
                        OO0O0O0OO0O00OO0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O000O0O0O0O0O00 ).json ()#line:440
                        if 'status'in OO0O0O0OO0O00OO0O :#line:442
                            if OO0O0O0OO0O00OO0O ['status']==200 :#line:443
                                O00OO00O0O0000OO0 =float (OO0O0O0OO0O00OO0O ['data']['silver'])/1000000000000 #line:444
                                print (f'【获取种子】:获得🌱:{int(O00OO00O0O0000OO0)}t粒')#line:445
                                return True #line:446
                            if OO0O0O0OO0O00OO0O ['status']==500 :#line:447
                                OOOO0O00O00OOOO0O =OO0O0O0OO0O00OO0O ['message']#line:448
                                print (f'【获取种子】:{OOOO0O00O00OOOO0O}')#line:449
                                return False #line:450
        except Exception as O0O00000O0O000OOO :#line:451
            print (O0O00000O0O000OOO )#line:452
    def synthetic (OO0OOO00O00OOO0OO ):#line:455
        global id ,g #line:456
        try :#line:457
            OO0000O0O00O0O0O0 =OO0OOO00O00OOO0OO .level_new ()#line:458
            OO000O0000OO0O00O =random .randint (9 ,11 )#line:459
            O0O0OO0O00O00O0OO =f'_site=8&targetSite={OO000O0000OO0O00O}_{timi_new()}'#line:460
            OOO0O000000OOO000 ={'accept':'application/json, text/plain, */*','authorization':OO0OOO00O00OOO0OO .token ,'timestamp':timi_new (),'sign':sign (O0O0OO0O00O00O0OO ),'signstring':O0O0OO0O00O00O0OO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:475
            OO0OO0000OO00OO0O ={"site":int (8 ),"targetSite":int (OO000O0000OO0O00O )}#line:476
            requests .request ('post',f'{host}/game/crops/move',headers =OOO0O000000OOO000 ,json =OO0OO0000OO00OO0O )#line:477
            while True :#line:478
                O0000OO0OOO0OOOO0 =f'__{timi_new()}'#line:479
                O0O0OOOOOOOO0OOOO ={'authorization':OO0OOO00O00OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO0OOO0OOOO0 ),'signstring':O0000OO0OOO0OOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                OOOO0OOOOOO0OO0OO =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OOOOOOOO0OOOO ).json ()#line:489
                if 'status'in OOOO0OOOOOO0OO0OO :#line:491
                    if OOOO0OOOOOO0OO0OO ['status']==200 :#line:492
                        O0OOO0O0OOOO000OO =OOOO0OOOOOO0OO0OO ['data']['cropList']#line:493
                        OO0O000OOO0O0O0OO =OOOO0OOOOOO0OO0OO ['data']['gameCoreDataDBid']#line:494
                        OOOO0O0O0O0O00O00 =float (OOOO0OOOOOO0OO0OO ['data']['silver'])/1000000000000 #line:495
                        O0O0000000OOOO00O =0 #line:500
                        for OO000OO0O000O000O in O0OOO0O0OOOO000OO :#line:501
                            if not OO000OO0O000O000O :#line:502
                                OO0OOOO000OO000OO =f'_crop_id={OO0O000OOO0O0O0OO}&site={O0O0000000OOOO00O}_{OO0OOO00O00OOO0OO.time}'#line:503
                                OOO00OOO0O0O0OOO0 ={'authorization':OO0OOO00O00OOO0OO .token ,'timestamp':OO0OOO00O00OOO0OO .time ,'sign':sign (OO0OOOO000OO000OO ),'signstring':OO0OOOO000OO000OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
                                O00O000O00O0O00OO ={"site":O0O0000000OOOO00O ,"crop_id":OO0O000OOO0O0O0OO }#line:513
                                O0OO000OOO0O00000 =requests .request ('post',f'{host}/game/crops/buy',headers =OOO00OOO0O0O0OOO0 ,data =O00O000O00O0O00OO ).json ()#line:514
                                time .sleep (random .randint (1 ,3 )/10 )#line:516
                                if 'status'in O0OO000OOO0O00000 :#line:517
                                    if O0OO000OOO0O00000 ['status']==200 :#line:518
                                        if O0OO000OOO0O00000 ['message']=='种子数量不足':#line:519
                                            OO0000O0O00O0O0O0 =OO0OOO00O00OOO0OO .level_new ()#line:520
                                            print (f'【种植合成】:{O0OO000OOO0O00000["message"]}')#line:521
                                            if not OO0OOO00O00OOO0OO .user_ad ():#line:522
                                                return False #line:523
                                    if O0OO000OOO0O00000 ['status']==500 :#line:524
                                        print (f'【种植合成】:{O0OO000OOO0O00000["message"]}')#line:525
                                        return False #line:526
                            O0O0000000OOOO00O +=1 #line:527
                        O0O0O0000O0O00OOO =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OOOOOOOO0OOOO ).json ()#line:528
                        O0000OOOO0000OOOO =O0O0O0000O0O00OOO ['data']['cropList']#line:529
                        O00OOOOOOOO000OOO =False #line:530
                        for OO000OO0O000O000O in range (12 ):#line:531
                            id =O0000OOOO0000OOOO [OO000OO0O000O000O ]['level']#line:532
                            if float (OO0000O0O00O0O0O0 )-float (id )>9 :#line:533
                                O000O00OOOOO000OO =f'_site={OO000OO0O000O000O}_{timi_new()}'#line:534
                                O00O0O0000000O0OO ={'accept':'application/json, text/plain, */*','authorization':OO0OOO00O00OOO0OO .token ,'timestamp':timi_new (),'sign':sign (O000O00OOOOO000OO ),'signstring':O000O00OOOOO000OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:544
                                OOOOO0O0OO0000O0O ={"site":OO000OO0O000O000O }#line:545
                                O00OO00OO0OO0OOOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00O0O0000000O0OO ,data =OOOOO0O0OO0000O0O ).json ()#line:547
                                if 'status'in O00OO00OO0OO0OOOO :#line:548
                                    if O00OO00OO0OO0OOOO ['status']==200 :#line:549
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:550
                            if id !=0 :#line:551
                                for O00O0O00OOO00O0O0 in range (11 ):#line:552
                                    O00O00O000O00O0OO =O00O0O00OOO00O0O0 +1 #line:553
                                    g =O0000OOOO0000OOOO [O00O00O000O00O0OO ]['level']#line:554
                                    if id ==g :#line:555
                                        O0O0OOOO0O00O0O00 =O00O0O00OOO00O0O0 +2 #line:556
                                        if O0O0OOOO0O00O0O00 !=OO000OO0O000O000O +1 :#line:557
                                            O0OO0O00000000OO0 =OO000OO0O000O000O +1 #line:558
                                            time .sleep (random .randint (1 ,3 )/10 )#line:560
                                            O0O0OO0O00O00O0OO =f'_site={O0OO0O00000000OO0 - 1}&targetSite={O0O0OOOO0O00O0O00 - 1}_{timi_new()}'#line:561
                                            OOO0O000000OOO000 ={'accept':'application/json, text/plain, */*','authorization':OO0OOO00O00OOO0OO .token ,'timestamp':timi_new (),'sign':sign (O0O0OO0O00O00O0OO ),'signstring':O0O0OO0O00O00O0OO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:576
                                            O0O00OO00OO000O0O ={"site":int (O0OO0O00000000OO0 -1 ),"targetSite":int (O0O0OOOO0O00O0O00 -1 )}#line:577
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOO0O000000OOO000 ,json =O0O00OO00OO000O0O )#line:578
                                            print (f'【种植合成】:位置{O0OO0O00000000OO0}和位置{O0O0OOOO0O00O0O00}合出{int(id) + 1}级农作物')#line:579
                                            O00OOOOOOOO000OOO =True #line:580
                                    if O00OOOOOOOO000OOO :#line:581
                                        break #line:582
                                if O00OOOOOOOO000OOO :#line:583
                                    break #line:584
        except :#line:585
            OO0OOO00O00OOO0OO .synthetic ()#line:586
    def level_new (O0000OOOO0OOO00O0 ):#line:589
        try :#line:590
            O0OOO0OO00OOO0O0O =f'__{timi_new()}'#line:591
            O0OO0O00000O00O00 ={'authorization':O0000OOOO0OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO00OOO0O0O ),'signstring':O0OOO0OO00OOO0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            OO0OOOO0O0OOO0OO0 =requests .request ('get',f'{host}/user',headers =O0OO0O00000O00O00 ).json ()#line:601
            if 'status'in OO0OOOO0O0OOO0OO0 :#line:602
                if OO0OOOO0O0OOO0OO0 ['status']==200 :#line:603
                    return float (OO0OOOO0O0OOO0OO0 ['data']['level'])#line:604
        except Exception as OOO0OO0O0OOO00O00 :#line:605
            print (OOO0OO0O0OOO00O00 )#line:606
    def propsraffle (O0O0OO000O000OO00 ):#line:609
        try :#line:610
            while True :#line:611
                OO0OO00O00O00O000 =f'__{timi_new()}'#line:612
                O00OO0O0OOO0O000O ={'authorization':O0O0OO000O000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00O00O00O000 ),'signstring':OO0OO00O00O00O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:621
                OOO0OO00O0O0OO0OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00OO0O0OOO0O000O ).json ()#line:622
                if 'status'in OOO0OO00O0O0OO0OO :#line:624
                    if OOO0OO00O0O0OO0OO ['status']==200 :#line:625
                        OO000OOOO00O0O0O0 =OOO0OO00O0O0OO0OO ['data']['rows']#line:626
                        O0OO00O0OO0OO0O00 =OOO0OO00O0O0OO0OO ['data']['vstate']#line:627
                        if OO000OOOO00O0O0O0 ==5 or OO000OOOO00O0O0O0 ==6 or OO000OOOO00O0O0O0 ==7 :#line:628
                            O0OO000OOOOOOOOO0 =OOO0OO00O0O0OO0OO ['data']['silver']#line:629
                            print (f'【转盘抽奖】:获得种子:{O0OO000OOOOOOOOO0}')#line:630
                        if OO000OOOO00O0O0O0 ==1 or OO000OOOO00O0O0O0 ==2 or OO000OOOO00O0O0O0 ==3 :#line:631
                            O00O0O0OO0O00OO00 =OOO0OO00O0O0OO0OO ['data']['clover']#line:632
                            print (f'【转盘抽奖】:获得三叶草:{O00O0O0OO0O00OO00}')#line:633
                        if OO000OOOO00O0O0O0 ==4 or OO000OOOO00O0O0O0 ==8 :#line:634
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:635
                        if OO000OOOO00O0O0O0 =='抽奖次数已用完':#line:639
                            break #line:672
                time .sleep (random .randint (8 ,15 )/10 )#line:673
        except Exception as OO0OOO0OOOOO000OO :#line:674
            print (OO0OOO0OOOOO000OO )#line:675
    def friends_invitation (O0OO00OOO0OOOOO00 ):#line:678
        try :#line:679
            OOO00OOO0O0O00OOO =f'__{timi_new()}'#line:680
            OO00O00O00O0O0000 ={'authorization':O0OO00OOO0OOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO0O0O00OOO ),'signstring':OOO00OOO0O0O00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:689
            O000OO000O000OOO0 =requests .request ('get',f'{host}/friends',headers =OO00O00O00O0O0000 ).json ()#line:690
            if 'status'in O000OO000O000OOO0 :#line:691
                if O000OO000O000OOO0 ['status']==200 :#line:692
                    OOOO00000OO0OO0O0 =O000OO000O000OOO0 ['data']['myInviteter']#line:693
                    if OOOO00000OO0OO0O0 :#line:694
                        OOO00O0OO000000O0 =OOOO00000OO0OO0O0 ['user']['nickname']#line:695
                        O00O0O0OOOO0O0O00 =O0OO00OOO0OOOOO00 .certification ()#line:696
                        print (f'【查邀请人】:我的邀请人:{OOO00O0OO000000O0}丨实名:{O00O0O0OOOO0O0O00}')#line:697
                    else :#line:698
                        if O0OO00OOO0OOOOO00 .innerId !='0':#line:699
                            O0OO00OOO0OOOOO00 .invitation ()#line:700
        except Exception as O0O00OOO00O00OOO0 :#line:701
            print (O0O00OOO00O00OOO0 )#line:702
    def add_clover (OOOO000000OO000OO ):#line:705
        global golden_seed #line:706
        try :#line:707
            O00000O0O0OOOO0O0 =f'__{timi_new()}'#line:708
            O0O000OOOOOO00OOO ={'authorization':OOOO000000OO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0O0OOOO0O0 ),'signstring':O00000O0O0OOOO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:717
            OOOOOO00OO00OOOOO =requests .request ('get',f'{host}/assets/clovers',headers =O0O000OOOOOO00OOO ).json ()#line:718
            if 'status'in OOOOOO00OO00OOOOO :#line:720
                if OOOOOO00OO00OOOOO ['status']==200 :#line:721
                    OO0000OOO0OOO0OOO =OOOOOO00OO00OOOOO ['data']['clover']#line:722
                    OOOOOOO000O00OO0O =OOOOOO00OO00OOOOO ['data']['used_clover']#line:723
                    OOO00O0O0000O0O0O =float (OO0000OOO0OOO0OOO )-float (OOOOOOO000O00OO0O )#line:724
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOOOOOO000O00OO0O}')#line:725
                    if OOOO000000OO000OO .certification ()!='未实名':#line:726
                        if OOO00O0O0000O0O0O >1 :#line:727
                            O00000O0O0OOOO0O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO00O0O0000O0O0O)}_{timi_new()}'#line:728
                            OO00OO0OOOO0O000O ={'authorization':OOOO000000OO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0O0OOOO0O0 ),'signstring':O00000O0O0OOOO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                            O0O000O0OOO0O00OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO00O0O0000O0O0O )}#line:738
                            OOOO0OOO0OOO0OOO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO00OO0OOOO0O000O ,data =O0O000O0OOO0O00OO ).json ()#line:739
                            if 'status'in OOOO0OOO0OOO0OOO0 :#line:741
                                if OOOO0OOO0OOO0OOO0 ['status']==200 :#line:742
                                    print (f'【参与抽奖】:添加☘️:{OOOO0OOO0OOO0OOO0["data"]}丨数量:{OOO00O0O0000O0O0O}')#line:743
                                if OOOO0OOO0OOO0OOO0 ['status']==500 :#line:744
                                    print (f'【参与抽奖】:添加☘️:{OOOO0OOO0OOO0OOO0["message"]}')#line:745
            O0O0OOO0O00OO00OO =requests .request ('get',f'{host}/lottery',headers =O0O000OOOOOO00OOO ).json ()#line:746
            O000OOO00O000000O =OOOO000000OO000OO .winning_rewards ()#line:748
            if 'status'in O0O0OOO0O00OO00OO :#line:749
                if O0O0OOO0O00OO00OO ['status']==200 :#line:750
                    O0O0O000O0OOO0OO0 =O0O0OOO0O00OO00OO ['data'][0 ]['day_get_gold_quantity']#line:751
                    golden_seed +=float (O0O0O000O0OOO0OO0 )#line:752
                    OO0OOOO0O000O0OOO =O0O0OOO0O00OO00OO ['data'][1 ]['value']#line:753
                    O00OOO00O0000OOO0 =O0O0OOO0O00OO00OO ['data'][0 ]['join_number']#line:754
                    O0O000O00O0O0OOO0 =int (float (O0O0OOO0O00OO00OO ['data'][0 ]['totalValue']))#line:755
                    O0O0000O0OOOOO00O =float (OO0OOOO0O000O0OOO /O0O000O00O0O0OOO0 )*10000 #line:756
                    OOOO0OO0OOO00000O =O0O000O00O0O0OOO0 /O00OOO00O0000OOO0 #line:757
                    print (f'【参与抽奖】:预计每天中{str(O0O0O000O0OOO0OO0)[:6]}颗金种子丨好友收益:{str(O000OOO00O000000O)[:6]}')#line:758
                    print (f'【抽奖统计】:每1万☘️中{str(O0O0000O0OOOOO00O)[:6]}颗金种子丨☘️人均:{str(OOOO0OO0OOO00000O)[:7]}️')#line:759
        except Exception as OO0OO00OOO00O0OOO :#line:760
            print (OO0OO00OOO00O0OOO )#line:761
    def energy (OOOO000OOO00000OO ):#line:765
        try :#line:766
            while True :#line:767
                OOO00OO0000OOO0O0 =f'__{timi_new()}'#line:768
                O00000O00O0O0OOO0 ={'authorization':OOOO000OOO00000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0000OOO0O0 ),'signstring':OOO00OO0000OOO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:777
                O0O0O0O00O0O0OOO0 =requests .request ('get',f'{host}/energy/general',headers =O00000O00O0O0OOO0 ).json ()#line:778
                if 'status'in O0O0O0O00O0O0OOO0 :#line:780
                    if O0O0O0O00O0O0OOO0 ['status']==200 :#line:781
                        O0O00OO00OO0000O0 =O0O0O0O00O0O0OOO0 ['data']['ordinary_water']#line:782
                        O0000OO000OOOOOO0 =O0O0O0O00O0O0OOO0 ['data']['ordinary_fertilizer']#line:783
                        print (f'【我的营养】:肥料:{str(O0000OO000OOOOOO0).split(".")[0]}丨水滴:{str(O0O00OO00OO0000O0).split(".")[0]}')#line:785
                        if float (O0000OO000OOOOOO0 )<96 :#line:786
                            time .sleep (random .randint (160 ,180 )/10 )#line:787
                            O0OO0000OO00OOO00 =99 -float (O0000OO000OOOOOO0 )#line:788
                            OOO00OO0O000O0O0O ={"fertilizer":str (O0OO0000OO00OOO00 ).split ('.')[0 ]}#line:789
                            O00OOO0000OO0O000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00000O00O0O0OOO0 ).json ()#line:790
                            if 'status'in O00OOO0000OO0O000 :#line:792
                                if O00OOO0000OO0O000 ['status']==200 :#line:793
                                    print (f'【购买肥料】:看广告获取肥料:{O00OOO0000OO0O000["message"]}')#line:794
                                if O00OOO0000OO0O000 ['status']==500 :#line:795
                                    print (f'【购买肥料】:看广告获取肥料:{O00OOO0000OO0O000["message"]}')#line:796
                                    break #line:797
                        if float (O0O00OO00OO0000O0 )<880 :#line:798
                            time .sleep (random .randint (160 ,180 )/10 )#line:799
                            OOO0O0000OO00O0O0 =999 -float (O0O00OO00OO0000O0 )#line:800
                            O0O00O00000O0OOO0 ={"water":str (OOO0O0000OO00O0O0 ).split ('.')[0 ]}#line:801
                            O0O0OOO0O00O00O0O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00000O00O0O0OOO0 ).json ()#line:802
                            if 'status'in O0O0OOO0O00O00O0O :#line:804
                                if O0O0OOO0O00O00O0O ['status']==200 :#line:805
                                    print (f'【购买水滴】:看广告获取水滴:{O0O0OOO0O00O00O0O["message"]}')#line:806
                                if O0O0OOO0O00O00O0O ['status']==500 :#line:807
                                    print (f'【购买水滴】:看广告获取水滴:{O0O0OOO0O00O00O0O["message"]}')#line:808
                                    break #line:809
                        if float (O0000OO000OOOOOO0 )>96 and float (O0O00OO00OO0000O0 )>880 :#line:810
                            break #line:811
        except Exception as OOOO0O0OOO00O00O0 :#line:813
            print (OOOO0O0OOO00O00O0 )#line:814
def bundled_def ():#line:816
    OOO0O00OOOOOO0O00 =['5570536','7750212','7911652','7911680','7805624']#line:817
    return OOO0O00OOOOOO0O00 [random .randint (0 ,len (OOO0O00OOOOOO0O00 )-1 )]#line:818
def version_of_the_validation ():#line:822
    return str ((80 -56 )/10 )#line:823
def gitee_validation ():#line:826
    try :#line:827
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:828
    except :#line:829
        sys .exit (0 )#line:830
def update_the_validation ():#line:834
    try :#line:835
        OO000OO0000OO00O0 =gitee_validation ()#line:836
        if version_of_the_validation ()<OO000OO0000OO00O0 ['CityEarth']['edition']:#line:837
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO000OO0000OO00O0["CityEarth"]["edition"]}   ❌')#line:838
            print (f'更新内容=>>{OO000OO0000OO00O0["CityEarth"]["content"]}   🎉')#line:839
        else :#line:840
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO000OO0000OO00O0["CityEarth"]["edition"]}   ✅')#line:841
            print (f'更新内容=>> {OO000OO0000OO00O0["CityEarth"]["content"]}   🎉')#line:842
    except Exception as OOO0O0000O0000O0O :#line:843
        print (OOO0O0000O0000O0O )#line:844
def os_qinglong ():#line:847
    if application in os .environ :#line:848
        OO00OO0OO000OOOO0 =os .environ [application ].split ('\n')#line:849
        if len (OO00OO0OO000OOOO0 )>0 :#line:850
            return OO00OO0OO000OOOO0 #line:851
        else :#line:852
            print (f"{application}变量未启用")#line:853
            print ('脚本退出')#line:854
            sys .exit (1 )#line:855
    else :#line:856
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:858
        return os_built ()#line:859
def os_built ():#line:862
    if token :#line:863
        O00O0OO00O0000OO0 =token .split ('\n')#line:864
        if len (O00O0OO00O0000OO0 )>0 :#line:865
            return O00O0OO00O0000OO0 #line:866
    else :#line:867
        print (f"内置变量为空")#line:868
        print ('脚本结束')#line:869
        sys .exit (0 )#line:870
if __name__ =='__main__':#line:873
    start ()#line:874
