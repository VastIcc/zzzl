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
        OO00O00O0O0OOO000 =os_qinglong ()#line:10
        print (f"==========共找到{len(OO00O00O0O0OOO000)}个账号==========")#line:11
        for O0000O00O00000000 in OO00O00O0O0OOO000 :#line:12
            O0OO000O00000OOOO =[]#line:13
            print (f"------------正在执行第{OO00O00O0O0OOO000.index(O0000O00O00000000) + 1}个账号------------")#line:14
            O0O0OOOO0O0OOOOO0 =CityEarth (O0000O00O00000000 ,O0OO000O00000OOOO )#line:15
            def O0OOO0000OO00O0O0 ():#line:17
                if O0O0OOOO0O0OOOOO0 .base_info ():#line:19
                    O0O0OOOO0O0OOOOO0 .sealing ()#line:21
                    O0O0OOOO0O0OOOOO0 .invitenum ()#line:23
                    O0O0OOOO0O0OOOOO0 .game_map ()#line:25
                    O0O0OOOO0O0OOOOO0 .friends_invitation ()#line:27
                    O0O0OOOO0O0OOOOO0 .add_clover ()#line:29
                    O0O0OOOO0O0OOOOO0 .propsraffle ()#line:31
                    O0O0OOOO0O0OOOOO0 .synthetic ()#line:33
                    O0O0OOOO0O0OOOOO0 .crops_illustrated ()#line:35
                    O0O0OOOO0O0OOOOO0 .give_gold ()#line:37
                    O0O0OOOO0O0OOOOO0 .withdraw ()#line:39
                    O0O0OOOO0O0OOOOO0 .energy ()#line:41
            OO0O0O00OOOO0O000 =threading .Thread (target =O0OOO0000OO00O0O0 )#line:42
            OO0O0O00OOOO0O000 .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        O000000OOO0000O0O =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O000000OOO0000O0O +' ')#line:48
    except Exception as O0O000OOOOOO000O0 :#line:49
        print (O0O000OOOOOO000O0 )#line:50
def sign (OO0OO0OO0O00000OO ):#line:53
    O0OOOOOOO0000OOO0 =hashlib .md5 (OO0OO0OO0O00000OO .encode ()).hexdigest ()#line:54
    O0OO0OOO00OOOOOOO ="scsc%^&*"+O0OOOOOOO0000OOO0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    O0O0O00OO0OO0OO0O =hashlib .md5 (O0OO0OOO00OOOOOOO .encode ()).hexdigest ()#line:56
    return O0O0O00OO0OO0OO0O #line:57
def format_msg ():#line:59
    O00O00O00OOO0O0OO =""#line:60
    for OO0OOOO0O00O00OO0 in msg_list :#line:61
        O00O00O00OOO0O0OO +=str (OO0OOOO0O00O00OO0 )+"\r\n"#line:62
    return O00O00O00OOO0O0OO #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (OOO000O0O0OO0000O ,OO0000OO0O0O000OO ,OO0O0OOOOOOOOOO0O ):#line:71
        try :#line:72
            OOO000O0O0OO0000O .msg =OO0O0OOOOOOOOOO0O #line:73
            OOO000O0O0OO0000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            OOO000O0O0OO0000O .token =OO0000OO0O0O000OO .split ('&')[0 ]#line:75
            OOO000O0O0OO0000O .innerId =OO0000OO0O0O000OO .split ('&')[1 ]#line:76
            OOO000O0O0OO0000O .doneeNo =OO0000OO0O0O000OO .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (OOOO00OOOO0O000OO ):#line:82
        try :#line:83
            OOOO00OOOO0O000OO .watched_ad ()#line:85
            OO00000OOO00OO0O0 =f'__{timi_new()}'#line:86
            O0OOO0O00O0OO0OOO ={'authorization':OOOO00OOOO0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OOO00OO0O0 ),'signstring':OO00000OOO00OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            O0OO00O0O00OO000O =requests .request ('get',f'{host}/user',headers =O0OOO0O00O0OO0OOO ).json ()#line:96
            if 'status'in O0OO00O0O00OO000O :#line:98
                if O0OO00O0O00OO000O ['status']==200 :#line:99
                    O0O0O00OOO0OOO000 =O0OO00O0O00OO000O ['data']['nickname']#line:100
                    OO0OO0OOO0O0OO00O =O0OO00O0O00OO000O ['data']['inner_id']#line:101
                    OO0OO0OOOO000O00O =O0OO00O0O00OO000O ['data']['assets']['gold']#line:102
                    OOOO00OOO0O00OOO0 =O0OO00O0O00OO000O ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{O0O0O00OOO0OOO000[:5]}丨ID:{OO0OO0OOO0O0OO00O}丨等级:{OOOO00OOO0O00OOO0}丨金种子:{str(OO0OO0OOOO000O00O).split(".")[0]}')#line:104
                if O0OO00O0O00OO000O ['status']==401 :#line:105
                    print (O0OO00O0O00OO000O ['message'])#line:106
                    OOOO00OOOO0O000OO .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if O0OO00O0O00OO000O ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as OO00OOO00O0O00000 :#line:112
            print (OO00OOO00O0O00000 )#line:113
    def sealing (O000O0OO00OO0OOOO ):#line:116
        try :#line:117
            OO0OO0O00000O00OO =f'__{timi_new()}'#line:118
            O00000000OOOOOO00 ={'authorization':O000O0OO00OO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O00000O00OO ),'signstring':OO0OO0O00000O00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00000000OOOOOO00 )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =O00000000OOOOOO00 )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00000000OOOOOO00 )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00000000OOOOOO00 )#line:131
            requests .request ('get',f'{host}/user',headers =O00000000OOOOOO00 )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00000000OOOOOO00 )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00000000OOOOOO00 )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =O00000000OOOOOO00 )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =O00000000OOOOOO00 )#line:136
            requests .request ('get',f'{host}/assets',headers =O00000000OOOOOO00 )#line:137
        except Exception as O00O00OOOO00000OO :#line:138
            print (O00O00OOOO00000OO )#line:139
    def withdraw (OO00O000O000O0OO0 ):#line:143
        O00OO0O0OOOO0O000 =f'__{timi_new()}'#line:144
        O0OOOOOO0O0O00000 ={'authorization':OO00O000O000O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0OOOO0O000 ),'signstring':O00OO0O0OOOO0O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        O0OO0O0OOO0000OO0 =requests .request ('get',f'{host}/assets',headers =O0OOOOOO0O0O00000 ).json ()#line:154
        if 'status'in O0OO0O0OOO0000OO0 :#line:156
            if O0OO0O0OOO0000OO0 ['status']==200 :#line:157
                O0OOO0OO0O000OOO0 =O0OO0O0OOO0000OO0 ['data']['cash']#line:158
                if float (O0OOO0OO0O000OOO0 )>20 :#line:159
                    O00OO0O0OOOO0O000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    O0OOOOOO0O0O00000 ={'authorization':OO00O000O000O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0OOOO0O000 ),'signstring':O00OO0O0OOOO0O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    OO0OOO00O0OOOO0O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    OOO0O0000O00O000O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0OOOOOO0O0O00000 ,data =OO0OOO00O0OOOO0O0 ).json ()#line:172
                    print (OOO0O0000O00O000O )#line:173
    def invitenum (OOO0O00OOOO00O000 ):#line:176
        OO0O00OOO0OO000OO =f'__{timi_new()}'#line:177
        O0OO00OO0O00O0O00 ={'authorization':OOO0O00OOOO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOO0OO000OO ),'signstring':OO0O00OOO0OO000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        OOO000O000O0O0OO0 =requests .request ('get',f'{host}/invite/invitenum',headers =O0OO00OO0O00O0O00 ).json ()#line:187
        if 'status'in OOO000O000O0O0OO0 :#line:189
            if OOO000O000O0O0OO0 ['status']==200 :#line:190
                OO00O000O0OOO0O00 =OOO000O000O0O0OO0 ['data']['invited_count']#line:191
                O0O00OO00OOOOO0O0 =OOO000O000O0O0OO0 ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OO00O000O0OOO0O00}丨间邀好友:{O0O00OO00OOOOO0O0}')#line:193
    def game_map (OO00O000000OOO00O ):#line:196
        try :#line:197
            O0OOOOO0O000OOOOO =f'__{timi_new()}'#line:198
            O0000OOO00OO0O000 ={'authorization':OO00O000000OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0O000OOOOO ),'signstring':O0OOOOO0O000OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            O0O0O00OO00OO0000 =requests .request ('get',f'{host}/game/map',headers =O0000OOO00OO0O000 ).json ()#line:208
            if 'status'in O0O0O00OO00OO0000 :#line:210
                if O0O0O00OO00OO0000 ['status']==200 :#line:211
                    for O0OOO0O0OO00O0OO0 in O0O0O00OO00OO0000 ['data']['list'][0 ]['crops']:#line:212
                        O0OOOOO00O0OOO0OO =O0OOO0O0OO00O0OO0 ['level']#line:214
                        if O0OOOOO00O0OOO0OO ==41 :#line:215
                            OOO00OOOOOO0O0O0O =O0OOO0O0OO00O0OO0 ['crop_name']#line:216
                            OO000OOOOOO0OO000 =O0OOO0O0OO00O0OO0 ['count']#line:217
                            if OO000OOOOOO0OO000 >0 :#line:218
                                print (f'【农业资产】:{OOO00OOOOOO0O0O0O}丨数量:{OO000OOOOOO0OO000}')#line:219
        except Exception as OOO000OOOOO00000O :#line:220
            print (OOO000OOOOO00000O )#line:221
    def give_gold (O0OOOO0OO0O0O00OO ):#line:224
        try :#line:225
            OO0OO0O0000O0OO0O =f'__{timi_new()}'#line:226
            O0OOO0000O000OOOO ={'authorization':O0OOOO0OO0O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0000O0OO0O ),'signstring':OO0OO0O0000O0OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            OO0O0OOOO0O000OO0 =requests .request ('get',f'{host}/user',headers =O0OOO0000O000OOOO ).json ()#line:236
            if 'status'in OO0O0OOOO0O000OO0 :#line:237
                if OO0O0OOOO0O000OO0 ['status']==200 :#line:238
                    if float (O0OOOO0OO0O0O00OO .doneeNo )!=0 :#line:239
                        OO0OOO0O00OO000O0 =OO0O0OOOO0O000OO0 ['data']['assets']['gold']#line:240
                        if float (OO0OOO0O00OO000O0 )>float (O0OOOO0OO0O0O00OO .innerId ):#line:241
                            O0O0OOOO00O0O00O0 =int (float (OO0OOO0O00OO000O0 )/1.1 )#line:242
                            OO0OO0O0000O0OO0O =f'_doneeNo={O0OOOO0OO0O0O00OO.doneeNo}&quantity={O0O0OOOO00O0O00O0}_{timi_new()}'#line:243
                            O0OOO0000O000OOOO ={'authorization':O0OOOO0OO0O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0000O0OO0O ),'signstring':OO0OO0O0000O0OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            O0O0O0O00O0O0OO00 ={"quantity":O0O0OOOO00O0O00O0 ,"doneeNo":O0OOOO0OO0O0O00OO .doneeNo }#line:256
                            O00OOO0000OOO0O00 =requests .request ('post',f'{host}/finance/give-gold',headers =O0OOO0000O000OOOO ,data =O0O0O0O00O0O0OO00 ).json ()#line:257
                            if 'status'in O00OOO0000OOO0O00 :#line:259
                                if O00OOO0000OOO0O00 ['status']==200 :#line:260
                                    if O00OOO0000OOO0O00 ['data']:#line:261
                                        print (f'【赠送种子】:赠送{O0O0OOOO00O0O00O0}种子给{O0OOOO0OO0O0O00OO.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as O0O00O00OO0O0OOOO :#line:265
            print (O0O00O00OO0O0OOOO )#line:266
    def invitation (O0O0OO0O0OOO0O0O0 ):#line:268
        try :#line:269
            _O000OO00O000OOO00 =float (bundled_def ())/4 #line:270
            O0O00O0O000OO00O0 =f'_innerId={int(_O000OO00O000OOO00)}_{timi_new()}'#line:271
            O00O00OO0000OO00O ={'authorization':O0O0OO0O0OOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O000OO00O0 ),'signstring':O0O00O0O000OO00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            O00OO000O00O0O0OO ={"innerId":int (_O000OO00O000OOO00 )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00O00OO0000OO00O ,data =O00OO000O00O0O0OO )#line:282
        except Exception as O0O0OO0O00OO0OO00 :#line:283
            print (O0O0OO0O00OO0OO00 )#line:284
    def winning_rewards (OO0O0OO0O0OOO0O0O ):#line:287
        try :#line:288
            O000O00O00OOO0OOO =f'__{timi_new()}'#line:289
            OO00O0O0O00OO000O ={'authorization':OO0O0OO0O0OOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00O00OOO0OOO ),'signstring':O000O00O00OOO0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            OOOOOO0OOOO0000OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO00O0O0O00OO000O ).json ()#line:299
            if 'status'in OOOOOO0OOOO0000OO :#line:301
                if OOOOOO0OOOO0000OO ['status']==200 :#line:302
                    if OOOOOO0OOOO0000OO ['data']['amount']:#line:303
                        O0O0OO00O000OO000 =OOOOOO0OOOO0000OO ['data']['amount']['gold']#line:304
                        return O0O0OO00O000OO000 #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as OOOOO0OO0O0OO000O :#line:308
            print (OOOOO0OO0O0OO000O )#line:309
    def certification (O0OO0O00OOO00O00O ):#line:312
        try :#line:313
            O00OO000O000O00O0 =f'__{timi_new()}'#line:314
            OO0O00O0OOO00OO00 ={'authorization':O0OO0O00OOO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000O000O00O0 ),'signstring':O00OO000O000O00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OO0O0000O00OOOO00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0O00O0OOO00OO00 ).json ()#line:324
            if 'status'in OO0O0000O00OOOO00 :#line:326
                if OO0O0000O00OOOO00 ['status']==200 :#line:327
                    if OO0O0000O00OOOO00 ['data']['result']:#line:328
                        OO0O0OO00O0000OOO =OO0O0000O00OOOO00 ['data']['nick_name']#line:329
                        return OO0O0OO00O0000OOO #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as OOO00O00O0O0OO0OO :#line:333
            print (OOO00O00O0O0OO0OO )#line:334
    def crops_illustrated (O000OOOOOO0O0O000 ):#line:337
        try :#line:338
            O0OO0O00O0OO0O000 =f'__{timi_new()}'#line:339
            OOOOO0OO00OOO00OO ={'authorization':O000OOOOOO0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O0OO0O000 ),'signstring':O0OO0O00O0OO0O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            OO0O0OOO0O0O00000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOOOO0OO00OOO00OO ).json ()#line:349
            if 'status'in OO0O0OOO0O0O00000 :#line:351
                if OO0O0OOO0O0O00000 ['status']==200 :#line:352
                    OOOOOO0OO00OOOOOO =OO0O0OOO0O0O00000 ['data'][0 ]['crops']#line:353
                    for O0OOO0O0000OO0000 in OOOOOO0OO00OOOOOO :#line:354
                        if O0OOO0O0000OO0000 ['ill_clover_award']:#line:355
                            if float (O0OOO0O0000OO0000 ['ill_clover_award'])>1 :#line:356
                                if O0OOO0O0000OO0000 ['is_finish']:#line:357
                                    if not O0OOO0O0000OO0000 ['is_getit']:#line:358
                                        if O000OOOOOO0O0O000 .certification ()!='未实名':#line:359
                                            O0OO0O00O0OO0O000 =f'_award_level={O0OOO0O0000OO0000["level"]}_{timi_new()}'#line:360
                                            OOOOO0OO00OOO00OO ={'authorization':O000OOOOOO0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O0OO0O000 ),'signstring':O0OO0O00O0OO0O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            OOOOOOO0O00OO00OO ={"award_level":O0OOO0O0000OO0000 ['level']}#line:370
                                            OO0OO0OOOO0OO0O0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOOOO0OO00OOO00OO ,json =OOOOOOO0O00OO00OO ).json ()#line:372
                                            if 'status'in OO0OO0OOOO0OO0O0O :#line:373
                                                if OO0OO0OOOO0OO0O0O ['status']==200 :#line:374
                                                    O000O0OOOOO000OO0 =OO0OO0OOOO0OO0O0O ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{O0OOO0O0000OO0000["crop_name"]}成就丨奖励{O000O0OOOOO000OO0}☘️')#line:377
                                                if OO0OO0OOOO0OO0O0O ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{OO0OO0OOOO0OO0O0O["message"]}')#line:379
        except Exception as OO0O0OO0OOOOO0OO0 :#line:380
            print (OO0O0OO0OOOOO0OO0 )#line:381
    def watched_ad (OO0O0OO000OO0OO00 ):#line:384
        try :#line:385
            O0OO0OOO0OOO0O00O =f'__{timi_new()}'#line:386
            O0O0O0OOO000OOO00 ={'authorization':OO0O0OO000OO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO0OOO0O00O ),'signstring':O0OO0OOO0OOO0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            O000OO00O0O00OO0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0OOO000OOO00 ).json ()#line:396
            if 'status'in O000OO00O0O00OO0O :#line:398
                if O000OO00O0O00OO0O ['status']==200 :#line:399
                    if 'offlineInfo'in O000OO00O0O00OO0O ['data']:#line:400
                        time .sleep (random .randint (16 ,18 ))#line:401
                        O0OO00O0OO0OO000O =O000OO00O0O00OO0O ['data']['offlineInfo']['off_minute']#line:402
                        OO00O00000OOOOOOO =float (O000OO00O0O00OO0O ['data']['silver'])/1000000000000 #line:403
                        time .sleep (1 )#line:404
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O0O0OOO000OOO00 ).json ()#line:405
                        time .sleep (2 )#line:406
                        O0O0000OOOO00OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0OOO000OOO00 ).json ()#line:407
                        if 'status'in O0O0000OOOO00OOO0 :#line:409
                            if O0O0000OOOO00OOO0 ['status']==200 :#line:410
                                O00O0000O0OOO0OOO =float (O0O0000OOOO00OOO0 ['data']['silver'])/1000000000000 #line:411
                                OOO0OOO0O0O0O00OO =str (O00O0000O0OOO0OOO -OO00O00000OOOOOOO )[:6 ]#line:412
                                print (f'【离线奖励】:翻倍离线{O0OO00O0OO0OO000O}分钟奖励🌱数量:{OOO0OOO0O0O0O00OO}t粒')#line:413
        except Exception as OOOOOO00O0OO0O00O :#line:414
            print (OOOOOO00O0OO0O00O )#line:415
    def user_ad (O00000OO0O000O000 ):#line:418
        try :#line:419
            OOO00O00OOO0OO00O =f'__{timi_new()}'#line:420
            O00O0O0O0OOOO000O ={'authorization':O00000OO0O000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00OOO0OO00O ),'signstring':OOO00O00OOO0OO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:429
            OOO0O0OO000OO00O0 =requests .request ('get',f'{host}/user/ad',headers =O00O0O0O0OOOO000O ).json ()#line:430
            if 'status'in OOO0O0OO000OO00O0 :#line:432
                if OOO0O0OO000OO00O0 ['status']==200 :#line:433
                    OOOO0O00000000O0O =OOO0O0OO000OO00O0 ['data']['max_time']#line:434
                    OO0O00O0000OO0OOO =OOO0O0OO000OO00O0 ['data']['watch_time']#line:435
                    O00O0OO000OOOO0OO =OOO0O0OO000OO00O0 ['data']['added_time']#line:436
                    print (f'【获取种子】:获取🌱剩余{O00O0OO000OOOO0OO + OOOO0O00000000O0O - OO0O00O0000OO0OOO}次丨好友提供:{O00O0OO000OOOO0OO}次')#line:437
                    if O00O0OO000OOOO0OO +OOOO0O00000000O0O -OO0O00O0000OO0OOO >0 :#line:438
                        time .sleep (random .randint (16 ,19 ))#line:439
                        O0O0O0OO0000OO000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00O0O0O0OOOO000O ).json ()#line:440
                        if 'status'in O0O0O0OO0000OO000 :#line:442
                            if O0O0O0OO0000OO000 ['status']==200 :#line:443
                                OO00OO000OO0OO0OO =float (O0O0O0OO0000OO000 ['data']['silver'])/1000000000000 #line:444
                                print (f'【获取种子】:获得🌱:{int(OO00OO000OO0OO0OO)}t粒')#line:445
                                return True #line:446
                            if O0O0O0OO0000OO000 ['status']==500 :#line:447
                                O0OOOO000000OO0OO =O0O0O0OO0000OO000 ['message']#line:448
                                print (f'【获取种子】:{O0OOOO000000OO0OO}')#line:449
                                return False #line:450
        except Exception as OOOO0OO00OO00O0O0 :#line:451
            print (OOOO0OO00OO00O0O0 )#line:452
    def synthetic (O000O00OOOO0000OO ):#line:455
        global id ,g #line:456
        try :#line:457
            O0OOOO0000OOOOO00 =O000O00OOOO0000OO .level_new ()#line:458
            OO00O0OO00OOO0O0O =random .randint (9 ,11 )#line:459
            O0OOO0O0O0O0OO000 =f'_site=8&targetSite={OO00O0OO00OOO0O0O}_{timi_new()}'#line:460
            O00OO000OOO0OO00O ={'accept':'application/json, text/plain, */*','authorization':O000O00OOOO0000OO .token ,'timestamp':timi_new (),'sign':sign (O0OOO0O0O0O0OO000 ),'signstring':O0OOO0O0O0O0OO000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:475
            O0O0OOOO0OO0OO000 ={"site":int (8 ),"targetSite":int (OO00O0OO00OOO0O0O )}#line:476
            requests .request ('post',f'{host}/game/crops/move',headers =O00OO000OOO0OO00O ,json =O0O0OOOO0OO0OO000 )#line:477
            while True :#line:478
                OO00000000O0OOOO0 =f'__{timi_new()}'#line:479
                O0OO0O0O000O0O0O0 ={'authorization':O000O00OOOO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000000O0OOOO0 ),'signstring':OO00000000O0OOOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                OOOOO000O0O00OO0O =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O0O000O0O0O0 ).json ()#line:489
                if 'status'in OOOOO000O0O00OO0O :#line:491
                    if OOOOO000O0O00OO0O ['status']==200 :#line:492
                        OO00000OO00OOOOO0 =OOOOO000O0O00OO0O ['data']['cropList']#line:493
                        OO00O00O00OO0O0O0 =OOOOO000O0O00OO0O ['data']['gameCoreDataDBid']#line:494
                        O0O000O0O00000OO0 =float (OOOOO000O0O00OO0O ['data']['silver'])/1000000000000 #line:495
                        if O0O000O0O00000OO0 <6750 :#line:496
                            print (f'【种植合成】:🌱不足6750t')#line:497
                            if O000O00OOOO0000OO .user_ad ():#line:498
                                return False #line:499
                        OOOO00O0O0O0OOO00 =0 #line:500
                        for OO00O000000OOO0O0 in OO00000OO00OOOOO0 :#line:501
                            if not OO00O000000OOO0O0 :#line:502
                                O00O0OO0O0OO0OOO0 =f'_crop_id={OO00O00O00OO0O0O0}&site={OOOO00O0O0O0OOO00}_{O000O00OOOO0000OO.time}'#line:503
                                OOOO0O000O00000OO ={'authorization':O000O00OOOO0000OO .token ,'timestamp':O000O00OOOO0000OO .time ,'sign':sign (O00O0OO0O0OO0OOO0 ),'signstring':O00O0OO0O0OO0OOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
                                O00000000OO000000 ={"site":OOOO00O0O0O0OOO00 ,"crop_id":OO00O00O00OO0O0O0 }#line:513
                                OO00OOO00O00O00OO =requests .request ('post',f'{host}/game/crops/buy',headers =OOOO0O000O00000OO ,data =O00000000OO000000 ).json ()#line:514
                                time .sleep (random .randint (1 ,3 )/10 )#line:516
                                if 'status'in OO00OOO00O00O00OO :#line:517
                                    if OO00OOO00O00O00OO ['status']==200 :#line:518
                                        if OO00OOO00O00O00OO ['message']=='种子数量不足':#line:519
                                            O0OOOO0000OOOOO00 =O000O00OOOO0000OO .level_new ()#line:520
                                            print (f'【种植合成】:{OO00OOO00O00O00OO["message"]}')#line:521
                                            if not O000O00OOOO0000OO .user_ad ():#line:522
                                                return False #line:523
                                    if OO00OOO00O00O00OO ['status']==500 :#line:524
                                        print (f'【种植合成】:{OO00OOO00O00O00OO["message"]}')#line:525
                                        return False #line:526
                            OOOO00O0O0O0OOO00 +=1 #line:527
                        O0O0OO0OOOO0O00O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O0O000O0O0O0 ).json ()#line:528
                        OO0OOO0O00OO00OOO =O0O0OO0OOOO0O00O0 ['data']['cropList']#line:529
                        OO0O000OO0OOO0O0O =False #line:530
                        for OO00O000000OOO0O0 in range (12 ):#line:531
                            id =OO0OOO0O00OO00OOO [OO00O000000OOO0O0 ]['level']#line:532
                            if float (O0OOOO0000OOOOO00 )-float (id )>9 :#line:533
                                O0O00O000O0OOO00O =f'_site={OO00O000000OOO0O0}_{timi_new()}'#line:534
                                O00O00O0O000O000O ={'accept':'application/json, text/plain, */*','authorization':O000O00OOOO0000OO .token ,'timestamp':timi_new (),'sign':sign (O0O00O000O0OOO00O ),'signstring':O0O00O000O0OOO00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:544
                                O0O0OO0OOO000OO00 ={"site":OO00O000000OOO0O0 }#line:545
                                O0OO0000O00OO0OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00O00O0O000O000O ,data =O0O0OO0OOO000OO00 ).json ()#line:547
                                if 'status'in O0OO0000O00OO0OOO :#line:548
                                    if O0OO0000O00OO0OOO ['status']==200 :#line:549
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:550
                            if id !=0 :#line:551
                                for OOOOO0000OOOO0O0O in range (11 ):#line:552
                                    O0O0OOOOOO00OO00O =OOOOO0000OOOO0O0O +1 #line:553
                                    g =OO0OOO0O00OO00OOO [O0O0OOOOOO00OO00O ]['level']#line:554
                                    if id ==g :#line:555
                                        OO0OOOOOOO0O0OOOO =OOOOO0000OOOO0O0O +2 #line:556
                                        if OO0OOOOOOO0O0OOOO !=OO00O000000OOO0O0 +1 :#line:557
                                            OOOO000O0000000OO =OO00O000000OOO0O0 +1 #line:558
                                            time .sleep (random .randint (1 ,3 )/10 )#line:560
                                            O0OOO0O0O0O0OO000 =f'_site={OOOO000O0000000OO - 1}&targetSite={OO0OOOOOOO0O0OOOO - 1}_{timi_new()}'#line:561
                                            O00OO000OOO0OO00O ={'accept':'application/json, text/plain, */*','authorization':O000O00OOOO0000OO .token ,'timestamp':timi_new (),'sign':sign (O0OOO0O0O0O0OO000 ),'signstring':O0OOO0O0O0O0OO000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:576
                                            O00OOO000OOOOOO00 ={"site":int (OOOO000O0000000OO -1 ),"targetSite":int (OO0OOOOOOO0O0OOOO -1 )}#line:577
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00OO000OOO0OO00O ,json =O00OOO000OOOOOO00 )#line:578
                                            print (f'【种植合成】:位置{OOOO000O0000000OO}和位置{OO0OOOOOOO0O0OOOO}合出{int(id) + 1}级农作物')#line:579
                                            OO0O000OO0OOO0O0O =True #line:580
                                    if OO0O000OO0OOO0O0O :#line:581
                                        break #line:582
                                if OO0O000OO0OOO0O0O :#line:583
                                    break #line:584
        except :#line:585
            O000O00OOOO0000OO .synthetic ()#line:586
    def level_new (OOOO0OOO0OO0O0OOO ):#line:589
        try :#line:590
            OOOOO0O00OO0O0O0O =f'__{timi_new()}'#line:591
            OO00O0OO0000OOO00 ={'authorization':OOOO0OOO0OO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O00OO0O0O0O ),'signstring':OOOOO0O00OO0O0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            OO0OOO0O0O0O0OO00 =requests .request ('get',f'{host}/user',headers =OO00O0OO0000OOO00 ).json ()#line:601
            if 'status'in OO0OOO0O0O0O0OO00 :#line:602
                if OO0OOO0O0O0O0OO00 ['status']==200 :#line:603
                    return float (OO0OOO0O0O0O0OO00 ['data']['level'])#line:604
        except Exception as O0O0O000O00OO00O0 :#line:605
            print (O0O0O000O00OO00O0 )#line:606
    def propsraffle (OO00OO0OOOO00OOOO ):#line:609
        try :#line:610
            while True :#line:611
                O0OO0OO0000O0000O =f'__{timi_new()}'#line:612
                OO0OOOOO0O000OO00 ={'authorization':OO00OO0OOOO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0000O0000O ),'signstring':O0OO0OO0000O0000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:621
                OOOOO0OOO0O0OO000 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0OOOOO0O000OO00 ).json ()#line:622
                if 'status'in OOOOO0OOO0O0OO000 :#line:624
                    if OOOOO0OOO0O0OO000 ['status']==200 :#line:625
                        O00O0O0O0000000OO =OOOOO0OOO0O0OO000 ['data']['rows']#line:626
                        O000OO000OOO0OO00 =OOOOO0OOO0O0OO000 ['data']['vstate']#line:627
                        if O00O0O0O0000000OO ==5 or O00O0O0O0000000OO ==6 or O00O0O0O0000000OO ==7 :#line:628
                            OOO0O000O00OOOOOO =OOOOO0OOO0O0OO000 ['data']['silver']#line:629
                            print (f'【转盘抽奖】:获得种子:{OOO0O000O00OOOOOO}')#line:630
                        if O00O0O0O0000000OO ==1 or O00O0O0O0000000OO ==2 or O00O0O0O0000000OO ==3 :#line:631
                            OO000O00O0O0O0O00 =OOOOO0OOO0O0OO000 ['data']['clover']#line:632
                            print (f'【转盘抽奖】:获得三叶草:{OO000O00O0O0O0O00}')#line:633
                        if O00O0O0O0000000OO ==4 or O00O0O0O0000000OO ==8 :#line:634
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:635
                        if O00O0O0O0000000OO =='抽奖次数已用完':#line:639
                            break #line:672
                time .sleep (random .randint (8 ,15 )/10 )#line:673
        except Exception as O0OOOOOO0OOO00OOO :#line:674
            print (O0OOOOOO0OOO00OOO )#line:675
    def friends_invitation (O0O0000OOOO00O000 ):#line:678
        try :#line:679
            O0O00OO00OO00OO0O =f'__{timi_new()}'#line:680
            OO0000OO00000OOO0 ={'authorization':O0O0000OOOO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO00OO00OO0O ),'signstring':O0O00OO00OO00OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:689
            O0OO000OOOOO000OO =requests .request ('get',f'{host}/friends',headers =OO0000OO00000OOO0 ).json ()#line:690
            if 'status'in O0OO000OOOOO000OO :#line:691
                if O0OO000OOOOO000OO ['status']==200 :#line:692
                    OOOOO00O000OO0O00 =O0OO000OOOOO000OO ['data']['myInviteter']#line:693
                    if OOOOO00O000OO0O00 :#line:694
                        O0000O000OO00OOOO =OOOOO00O000OO0O00 ['user']['nickname']#line:695
                        OO0OO000O0OO0000O =O0O0000OOOO00O000 .certification ()#line:696
                        print (f'【查邀请人】:我的邀请人:{O0000O000OO00OOOO}丨实名:{OO0OO000O0OO0000O}')#line:697
                    else :#line:698
                        if O0O0000OOOO00O000 .innerId !='0':#line:699
                            O0O0000OOOO00O000 .invitation ()#line:700
        except Exception as O0O000OOOOOO0O0OO :#line:701
            print (O0O000OOOOOO0O0OO )#line:702
    def add_clover (OO0O000OO0O0O0OOO ):#line:705
        global golden_seed #line:706
        try :#line:707
            OOO0O0OOO0O00O000 =f'__{timi_new()}'#line:708
            O00OO00O0OOO00000 ={'authorization':OO0O000OO0O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OOO0O00O000 ),'signstring':OOO0O0OOO0O00O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:717
            O0O0O0000OO0O00OO =requests .request ('get',f'{host}/assets/clovers',headers =O00OO00O0OOO00000 ).json ()#line:718
            if 'status'in O0O0O0000OO0O00OO :#line:720
                if O0O0O0000OO0O00OO ['status']==200 :#line:721
                    O0O00OO00O000O0O0 =O0O0O0000OO0O00OO ['data']['clover']#line:722
                    O0OO0O00OOO00O0OO =O0O0O0000OO0O00OO ['data']['used_clover']#line:723
                    OO0OOOOO00O0000O0 =float (O0O00OO00O000O0O0 )-float (O0OO0O00OOO00O0OO )#line:724
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OO0O00OOO00O0OO}')#line:725
                    if OO0O000OO0O0O0OOO .certification ()!='未实名':#line:726
                        if OO0OOOOO00O0000O0 >1 :#line:727
                            OOO0O0OOO0O00O000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0OOOOO00O0000O0)}_{timi_new()}'#line:728
                            O0000OO00000OOOO0 ={'authorization':OO0O000OO0O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OOO0O00O000 ),'signstring':OOO0O0OOO0O00O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                            OOO0O000OO0OOOOOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0OOOOO00O0000O0 )}#line:738
                            O0OOO0OOOO0OOO0O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0000OO00000OOOO0 ,data =OOO0O000OO0OOOOOO ).json ()#line:739
                            if 'status'in O0OOO0OOOO0OOO0O0 :#line:741
                                if O0OOO0OOOO0OOO0O0 ['status']==200 :#line:742
                                    print (f'【参与抽奖】:添加☘️:{O0OOO0OOOO0OOO0O0["data"]}丨数量:{OO0OOOOO00O0000O0}')#line:743
                                if O0OOO0OOOO0OOO0O0 ['status']==500 :#line:744
                                    print (f'【参与抽奖】:添加☘️:{O0OOO0OOOO0OOO0O0["message"]}')#line:745
            OOOOO0OO0OOOOOO0O =requests .request ('get',f'{host}/lottery',headers =O00OO00O0OOO00000 ).json ()#line:746
            O000O0000OO00OO00 =OO0O000OO0O0O0OOO .winning_rewards ()#line:748
            if 'status'in OOOOO0OO0OOOOOO0O :#line:749
                if OOOOO0OO0OOOOOO0O ['status']==200 :#line:750
                    OOO000O0OO0O000O0 =OOOOO0OO0OOOOOO0O ['data'][0 ]['day_get_gold_quantity']#line:751
                    golden_seed +=float (OOO000O0OO0O000O0 )#line:752
                    OOO00OOOOOO0OO0OO =OOOOO0OO0OOOOOO0O ['data'][1 ]['value']#line:753
                    O0OOO0OOOOO0OOO00 =OOOOO0OO0OOOOOO0O ['data'][0 ]['join_number']#line:754
                    OOOOO0O0OO000OO0O =int (float (OOOOO0OO0OOOOOO0O ['data'][0 ]['totalValue']))#line:755
                    OOO00O0O0OO0O000O =float (OOO00OOOOOO0OO0OO /OOOOO0O0OO000OO0O )*10000 #line:756
                    O0OO0000O0OOO0000 =OOOOO0O0OO000OO0O /O0OOO0OOOOO0OOO00 #line:757
                    print (f'【参与抽奖】:预计每天中{str(OOO000O0OO0O000O0)[:6]}颗金种子丨好友收益:{str(O000O0000OO00OO00)[:6]}')#line:758
                    print (f'【抽奖统计】:每1万☘️中{str(OOO00O0O0OO0O000O)[:6]}颗金种子丨☘️人均:{str(O0OO0000O0OOO0000)[:7]}️')#line:759
        except Exception as OO0O00OOO0OOO0OOO :#line:760
            print (OO0O00OOO0OOO0OOO )#line:761
    def energy (O0O0OOOO0O0O0O0OO ):#line:765
        try :#line:766
            while True :#line:767
                OO0OOOOOO000OOOOO =f'__{timi_new()}'#line:768
                OOO000O0O000OOOOO ={'authorization':O0O0OOOO0O0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOOO000OOOOO ),'signstring':OO0OOOOOO000OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:777
                O00O0000OO0OO0OO0 =requests .request ('get',f'{host}/energy/general',headers =OOO000O0O000OOOOO ).json ()#line:778
                if 'status'in O00O0000OO0OO0OO0 :#line:780
                    if O00O0000OO0OO0OO0 ['status']==200 :#line:781
                        OO00OOOO00000O000 =O00O0000OO0OO0OO0 ['data']['ordinary_water']#line:782
                        O0O00000OO0OO00O0 =O00O0000OO0OO0OO0 ['data']['ordinary_fertilizer']#line:783
                        print (f'【我的营养】:肥料:{str(O0O00000OO0OO00O0).split(".")[0]}丨水滴:{str(OO00OOOO00000O000).split(".")[0]}')#line:785
                        if float (O0O00000OO0OO00O0 )<96 :#line:786
                            time .sleep (random .randint (160 ,180 )/10 )#line:787
                            OO00OO000OO000O00 =99 -float (O0O00000OO0OO00O0 )#line:788
                            OO0O0OOO0O0OOO00O ={"fertilizer":str (OO00OO000OO000O00 ).split ('.')[0 ]}#line:789
                            OOO0O0000000OO000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOO000O0O000OOOOO ).json ()#line:790
                            if 'status'in OOO0O0000000OO000 :#line:792
                                if OOO0O0000000OO000 ['status']==200 :#line:793
                                    print (f'【购买肥料】:看广告获取肥料:{OOO0O0000000OO000["message"]}')#line:794
                        if float (OO00OOOO00000O000 )<880 :#line:795
                            time .sleep (random .randint (160 ,180 )/10 )#line:796
                            OOOOO0OOOOO0OOOOO =999 -float (OO00OOOO00000O000 )#line:797
                            O00OO00O00O00OO00 ={"water":str (OOOOO0OOOOO0OOOOO ).split ('.')[0 ]}#line:798
                            O0O0O00O00OOO0OOO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOO000O0O000OOOOO ).json ()#line:799
                            if 'status'in O0O0O00O00OOO0OOO :#line:801
                                if O0O0O00O00OOO0OOO ['status']==200 :#line:802
                                    print (f'【购买水滴】:看广告获取水滴:{O0O0O00O00OOO0OOO["message"]}')#line:803
                        if float (O0O00000OO0OO00O0 )>96 and float (OO00OOOO00000O000 )>880 :#line:804
                            break #line:805
        except Exception as OOOO0O0OOO0O00OO0 :#line:807
            print (OOOO0O0OOO0O00OO0 )#line:808
def bundled_def ():#line:810
    O0OO0000OO0000OOO =['5570536','7750212','7911652','7911680','7805624']#line:811
    return O0OO0000OO0000OOO [random .randint (0 ,len (O0OO0000OO0000OOO )-1 )]#line:812
def version_of_the_validation ():#line:816
    return str ((78 -56 )/10 )#line:817
def gitee_validation ():#line:820
    try :#line:821
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:822
    except :#line:823
        sys .exit (0 )#line:824
def update_the_validation ():#line:828
    try :#line:829
        OO00O000OOOOOOO00 =gitee_validation ()#line:830
        if version_of_the_validation ()<OO00O000OOOOOOO00 ['CityEarth']['edition']:#line:831
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O000OOOOOOO00["CityEarth"]["edition"]}   ❌')#line:832
            print (f'更新内容=>>{OO00O000OOOOOOO00["CityEarth"]["content"]}   🎉')#line:833
        else :#line:834
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O000OOOOOOO00["CityEarth"]["edition"]}   ✅')#line:835
            print (f'更新内容=>> {OO00O000OOOOOOO00["CityEarth"]["content"]}   🎉')#line:836
    except Exception as OOO0O00OO0OO00O0O :#line:837
        print (OOO0O00OO0OO00O0O )#line:838
def os_qinglong ():#line:841
    if application in os .environ :#line:842
        O0OO00O0O00O000O0 =os .environ [application ].split ('\n')#line:843
        if len (O0OO00O0O00O000O0 )>0 :#line:844
            return O0OO00O0O00O000O0 #line:845
        else :#line:846
            print (f"{application}变量未启用")#line:847
            print ('脚本退出')#line:848
            sys .exit (1 )#line:849
    else :#line:850
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:852
        return os_built ()#line:853
def os_built ():#line:856
    if token :#line:857
        OO0OO00OO000OOO00 =token .split ('\n')#line:858
        if len (OO0OO00OO000OOO00 )>0 :#line:859
            return OO0OO00OO000OOO00 #line:860
    else :#line:861
        print (f"内置变量为空")#line:862
        print ('脚本结束')#line:863
        sys .exit (0 )#line:864
if __name__ =='__main__':#line:867
    start ()#line:868
