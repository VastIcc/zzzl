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
token = ''
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
version ='3.1.4195311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
def start ():#line:7
    try :#line:8
        update_the_validation ()#line:9
        OOO00OO00O0O00000 =os_qinglong ()#line:10
        print (f"==========共找到{len(OOO00OO00O0O00000)}个账号==========")#line:11
        for OO0OO000O0000000O in OOO00OO00O0O00000 :#line:12
            OO00OOOO0000OO0OO =[]#line:13
            print (f"------------正在执行第{OOO00OO00O0O00000.index(OO0OO000O0000000O) + 1}个账号------------")#line:14
            OOO00000000OOOO00 =CityEarth (OO0OO000O0000000O ,OO00OOOO0000OO0OO )#line:15
            def OOO0O00O0OOO00OOO ():#line:17
                if OOO00000000OOOO00 .base_info ():#line:19
                    OOO00000000OOOO00 .sealing ()#line:21
                    OOO00000000OOOO00 .invitenum ()#line:23
                    OOO00000000OOOO00 .game_map ()#line:25
                    OOO00000000OOOO00 .friends_invitation ()#line:27
                    OOO00000000OOOO00 .add_clover ()#line:29
                    OOO00000000OOOO00 .propsraffle ()#line:31
                    OOO00000000OOOO00 .synthetic ()#line:33
                    OOO00000000OOOO00 .crops_illustrated ()#line:35
                    OOO00000000OOOO00 .give_gold ()#line:37
                    OOO00000000OOOO00 .withdraw ()#line:39
                    OOO00000000OOOO00 .energy ()#line:41
            O0O0O0000O0000OO0 =threading .Thread (target =OOO0O00O0OOO00OOO )#line:42
            O0O0O0000O0000OO0 .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        O0O0O0O0OOO00OOO0 =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O0O0O0OOO00OOO0 +' ')#line:48
    except Exception as O0OO0000OO0000O00 :#line:49
        print (O0OO0000OO0000O00 )#line:50
def sign (OO00OOO00O00OOOO0 ):#line:53
    OOO0O000OOO0OO0OO =hashlib .md5 (OO00OOO00O00OOOO0 .encode ()).hexdigest ()#line:54
    O00O000OOOOO00000 ="scsc%^&*"+OOO0O000OOO0OO0OO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    OO00OO00OOOO00OOO =hashlib .md5 (O00O000OOOOO00000 .encode ()).hexdigest ()#line:56
    return OO00OO00OOOO00OOO #line:57
def format_msg ():#line:59
    OO0OO0O000O0OOOO0 =""#line:60
    for O0OO0OOOOO0O0O00O in msg_list :#line:61
        OO0OO0O000O0OOOO0 +=str (O0OO0OOOOO0O0O00O )+"\r\n"#line:62
    return OO0OO0O000O0OOOO0 #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (O00000OO0O0O0OOO0 ,OOOOOO0O0OO00O0O0 ,OOO0O0O0000O0OO0O ):#line:71
        try :#line:72
            O00000OO0O0O0OOO0 .msg =OOO0O0O0000O0OO0O #line:73
            O00000OO0O0O0OOO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            O00000OO0O0O0OOO0 .token =OOOOOO0O0OO00O0O0 .split ('&')[0 ]#line:75
            O00000OO0O0O0OOO0 .innerId =OOOOOO0O0OO00O0O0 .split ('&')[1 ]#line:76
            O00000OO0O0O0OOO0 .doneeNo =OOOOOO0O0OO00O0O0 .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (OOO0O0OO00O0OOO00 ):#line:82
        try :#line:83
            OOO0O0OO00O0OOO00 .watched_ad ()#line:85
            OO000OOO0OOO0O00O =f'__{timi_new()}'#line:86
            O0O0O0000O0O000OO ={'authorization':OOO0O0OO00O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOO0OOO0O00O ),'signstring':OO000OOO0OOO0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            O00OOO0OOOOO00OOO =requests .request ('get',f'{host}/user',headers =O0O0O0000O0O000OO ).json ()#line:96
            if 'status'in O00OOO0OOOOO00OOO :#line:98
                if O00OOO0OOOOO00OOO ['status']==200 :#line:99
                    OOOO000O0O0O00OO0 =O00OOO0OOOOO00OOO ['data']['nickname']#line:100
                    OOOOOOO0O00O0OO0O =O00OOO0OOOOO00OOO ['data']['inner_id']#line:101
                    O0O0OO00000O0OO0O =O00OOO0OOOOO00OOO ['data']['assets']['gold']#line:102
                    OO0OOO0000OO00O0O =O00OOO0OOOOO00OOO ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{OOOO000O0O0O00OO0[:5]}丨ID:{OOOOOOO0O00O0OO0O}丨等级:{OO0OOO0000OO00O0O}丨金种子:{str(O0O0OO00000O0OO0O).split(".")[0]}')#line:104
                if O00OOO0OOOOO00OOO ['status']==401 :#line:105
                    print (O00OOO0OOOOO00OOO ['message'])#line:106
                    OOO0O0OO00O0OOO00 .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if O00OOO0OOOOO00OOO ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as O00O0000O00O00O0O :#line:112
            print (O00O0000O00O00O0O )#line:113
    def sealing (O00OO0OO00OOO0O00 ):#line:116
        try :#line:117
            OOOOO0O00000OO0O0 =f'__{timi_new()}'#line:118
            OOOOOO0O00O00000O ={'authorization':O00OO0OO00OOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O00000OO0O0 ),'signstring':OOOOO0O00000OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOOOO0O00O00000O )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =OOOOOO0O00O00000O )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOOOO0O00O00000O )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOOOO0O00O00000O )#line:131
            requests .request ('get',f'{host}/user',headers =OOOOOO0O00O00000O )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOOOO0O00O00000O )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOOOO0O00O00000O )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOOOO0O00O00000O )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =OOOOOO0O00O00000O )#line:136
            requests .request ('get',f'{host}/assets',headers =OOOOOO0O00O00000O )#line:137
        except Exception as O0000000OOO0O0OOO :#line:138
            print (O0000000OOO0O0OOO )#line:139
    def withdraw (OO0O000000000O0OO ):#line:143
        OOO0OOO0OOO000OOO =f'__{timi_new()}'#line:144
        OOOO0OOOO0OO0O00O ={'authorization':OO0O000000000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OOO000OOO ),'signstring':OOO0OOO0OOO000OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        O0O0OO00000OOOO0O =requests .request ('get',f'{host}/assets',headers =OOOO0OOOO0OO0O00O ).json ()#line:154
        if 'status'in O0O0OO00000OOOO0O :#line:156
            if O0O0OO00000OOOO0O ['status']==200 :#line:157
                O00O0O0000OO00000 =O0O0OO00000OOOO0O ['data']['cash']#line:158
                if float (O00O0O0000OO00000 )>20 :#line:159
                    OOO0OOO0OOO000OOO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    OOOO0OOOO0OO0O00O ={'authorization':OO0O000000000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OOO000OOO ),'signstring':OOO0OOO0OOO000OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    OOO00OO0000O00O00 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    OOOOOOOO00OOOOO00 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOO0OOOO0OO0O00O ,data =OOO00OO0000O00O00 ).json ()#line:172
                    print (OOOOOOOO00OOOOO00 )#line:173
    def invitenum (OOO0000OO00O0OO00 ):#line:176
        OO00O0O00OO00O000 =f'__{timi_new()}'#line:177
        O0OOO0O0O000OOOO0 ={'authorization':OOO0000OO00O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O00OO00O000 ),'signstring':OO00O0O00OO00O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O0000OOO0000O0O0O =requests .request ('get',f'{host}/invite/invitenum',headers =O0OOO0O0O000OOOO0 ).json ()#line:187
        if 'status'in O0000OOO0000O0O0O :#line:189
            if O0000OOO0000O0O0O ['status']==200 :#line:190
                O000000OOOO00OOO0 =O0000OOO0000O0O0O ['data']['invited_count']#line:191
                O0O0O00O00O0000O0 =O0000OOO0000O0O0O ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{O000000OOOO00OOO0}丨间邀好友:{O0O0O00O00O0000O0}')#line:193
    def game_map (O000O0O0OO0O0000O ):#line:196
        try :#line:197
            O0OO00OO0OOO0000O =f'__{timi_new()}'#line:198
            OOO0OOO0OO000OOO0 ={'authorization':O000O0O0OO0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO0OOO0000O ),'signstring':O0OO00OO0OOO0000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            OOOOOOO0O00O0O00O =requests .request ('get',f'{host}/game/map',headers =OOO0OOO0OO000OOO0 ).json ()#line:208
            if 'status'in OOOOOOO0O00O0O00O :#line:210
                if OOOOOOO0O00O0O00O ['status']==200 :#line:211
                    for OO00OO00OO0O0OOOO in OOOOOOO0O00O0O00O ['data']['list'][0 ]['crops']:#line:212
                        O00OO000000OO0000 =OO00OO00OO0O0OOOO ['level']#line:214
                        if O00OO000000OO0000 ==41 :#line:215
                            OO0O000OOOO0O00O0 =OO00OO00OO0O0OOOO ['crop_name']#line:216
                            O0OO0OO000O000OO0 =OO00OO00OO0O0OOOO ['count']#line:217
                            if O0OO0OO000O000OO0 >0 :#line:218
                                print (f'【农业资产】:{OO0O000OOOO0O00O0}丨数量:{O0OO0OO000O000OO0}')#line:219
        except Exception as O00000O0O0OOOOO0O :#line:220
            print (O00000O0O0OOOOO0O )#line:221
    def give_gold (O00OO0O0O0O00OOO0 ):#line:224
        try :#line:225
            OOO0O0O000O0O0OO0 =f'__{timi_new()}'#line:226
            O000O0OO00000OOO0 ={'authorization':O00OO0O0O0O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O000O0O0OO0 ),'signstring':OOO0O0O000O0O0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            OO0OOO0O0OO0O0000 =requests .request ('get',f'{host}/user',headers =O000O0OO00000OOO0 ).json ()#line:236
            if 'status'in OO0OOO0O0OO0O0000 :#line:237
                if OO0OOO0O0OO0O0000 ['status']==200 :#line:238
                    if float (O00OO0O0O0O00OOO0 .doneeNo )!=0 :#line:239
                        O0O000O0OOO00OOO0 =OO0OOO0O0OO0O0000 ['data']['assets']['gold']#line:240
                        if float (O0O000O0OOO00OOO0 )>float (O00OO0O0O0O00OOO0 .innerId ):#line:241
                            OO00O0OO0OO0000OO =int (float (O0O000O0OOO00OOO0 )/1.1 )#line:242
                            OOO0O0O000O0O0OO0 =f'_doneeNo={O00OO0O0O0O00OOO0.doneeNo}&quantity={OO00O0OO0OO0000OO}_{timi_new()}'#line:243
                            O000O0OO00000OOO0 ={'authorization':O00OO0O0O0O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O000O0O0OO0 ),'signstring':OOO0O0O000O0O0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            OO000OOO0OOO00O0O ={"quantity":OO00O0OO0OO0000OO ,"doneeNo":O00OO0O0O0O00OOO0 .doneeNo }#line:256
                            OO0OO0OO00O0O0O00 =requests .request ('post',f'{host}/finance/give-gold',headers =O000O0OO00000OOO0 ,data =OO000OOO0OOO00O0O ).json ()#line:257
                            if 'status'in OO0OO0OO00O0O0O00 :#line:259
                                if OO0OO0OO00O0O0O00 ['status']==200 :#line:260
                                    if OO0OO0OO00O0O0O00 ['data']:#line:261
                                        print (f'【赠送种子】:赠送{OO00O0OO0OO0000OO}种子给{O00OO0O0O0O00OOO0.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as OOO0OO00OO0OOO0OO :#line:265
            print (OOO0OO00OO0OOO0OO )#line:266
    def invitation (O00OO00OOO000OO00 ):#line:268
        try :#line:269
            _O0O0O0O0000O00O00 =float (bundled_def ())/4 #line:270
            O0O0OOO0000OOOO00 =f'_innerId={int(_O0O0O0O0000O00O00)}_{timi_new()}'#line:271
            OOOO0O0O0O0OO0O00 ={'authorization':O00OO00OOO000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO0000OOOO00 ),'signstring':O0O0OOO0000OOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            O0OO000O00000000O ={"innerId":int (_O0O0O0O0000O00O00 )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOO0O0O0O0OO0O00 ,data =O0OO000O00000000O )#line:282
        except Exception as OO0OO0O0OO00OO0O0 :#line:283
            print (OO0OO0O0OO00OO0O0 )#line:284
    def winning_rewards (O00O0OO00O0O0OO00 ):#line:287
        try :#line:288
            O00OO0O0O0OO00OOO =f'__{timi_new()}'#line:289
            O00O000O0OOOOOOO0 ={'authorization':O00O0OO00O0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0O0OO00OOO ),'signstring':O00OO0O0O0OO00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            OO000O00OOOO000OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00O000O0OOOOOOO0 ).json ()#line:299
            if 'status'in OO000O00OOOO000OO :#line:301
                if OO000O00OOOO000OO ['status']==200 :#line:302
                    if OO000O00OOOO000OO ['data']['amount']:#line:303
                        O0OO00OOO0OOOO0OO =OO000O00OOOO000OO ['data']['amount']['gold']#line:304
                        return O0OO00OOO0OOOO0OO #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as OO0OO00OOOOO0O000 :#line:308
            print (OO0OO00OOOOO0O000 )#line:309
    def certification (OO00O00O000O0O0OO ):#line:312
        try :#line:313
            OOO000O0O0O00OO0O =f'__{timi_new()}'#line:314
            OO0OOO0O0O00O00O0 ={'authorization':OO00O00O000O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0O0O00OO0O ),'signstring':OOO000O0O0O00OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OOO0O000OO00OO0O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0OOO0O0O00O00O0 ).json ()#line:324
            if 'status'in OOO0O000OO00OO0O0 :#line:326
                if OOO0O000OO00OO0O0 ['status']==200 :#line:327
                    if OOO0O000OO00OO0O0 ['data']['result']:#line:328
                        OOO000000O00O00O0 =OOO0O000OO00OO0O0 ['data']['nick_name']#line:329
                        return OOO000000O00O00O0 #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as OO0O0O0OO00OOO000 :#line:333
            print (OO0O0O0OO00OOO000 )#line:334
    def crops_illustrated (O0O0O0OOOO0OO0O00 ):#line:337
        try :#line:338
            OO0OO00000OOOO000 =f'__{timi_new()}'#line:339
            OO00OOO0000000O0O ={'authorization':O0O0O0OOOO0OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00000OOOO000 ),'signstring':OO0OO00000OOOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            O00OO00OO000O0O0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO00OOO0000000O0O ).json ()#line:349
            if 'status'in O00OO00OO000O0O0O :#line:351
                if O00OO00OO000O0O0O ['status']==200 :#line:352
                    OOOO00O0O0O00O0OO =O00OO00OO000O0O0O ['data'][0 ]['crops']#line:353
                    for O00O00OOOOO0OOO0O in OOOO00O0O0O00O0OO :#line:354
                        if O00O00OOOOO0OOO0O ['ill_clover_award']:#line:355
                            if float (O00O00OOOOO0OOO0O ['ill_clover_award'])>1 :#line:356
                                if O00O00OOOOO0OOO0O ['is_finish']:#line:357
                                    if not O00O00OOOOO0OOO0O ['is_getit']:#line:358
                                        if O0O0O0OOOO0OO0O00 .certification ()!='未实名':#line:359
                                            OO0OO00000OOOO000 =f'_award_level={O00O00OOOOO0OOO0O["level"]}_{timi_new()}'#line:360
                                            OO00OOO0000000O0O ={'authorization':O0O0O0OOOO0OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00000OOOO000 ),'signstring':OO0OO00000OOOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            OO000OOOOO0OOOOOO ={"award_level":O00O00OOOOO0OOO0O ['level']}#line:370
                                            O000O0OOO00OOO00O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO00OOO0000000O0O ,json =OO000OOOOO0OOOOOO ).json ()#line:372
                                            if 'status'in O000O0OOO00OOO00O :#line:373
                                                if O000O0OOO00OOO00O ['status']==200 :#line:374
                                                    O0OOOO000O0O0OO0O =O000O0OOO00OOO00O ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{O00O00OOOOO0OOO0O["crop_name"]}成就丨奖励{O0OOOO000O0O0OO0O}☘️')#line:377
                                                if O000O0OOO00OOO00O ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{O000O0OOO00OOO00O["message"]}')#line:379
        except Exception as O000OOO0O00O0OOOO :#line:380
            print (O000OOO0O00O0OOOO )#line:381
    def watched_ad (OOOOO00OOO000OO00 ):#line:384
        try :#line:385
            OOOOO0OO000O0OOOO =f'__{timi_new()}'#line:386
            OOOO000O0OO0O0OOO ={'authorization':OOOOO00OOO000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OO000O0OOOO ),'signstring':OOOOO0OO000O0OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            O0OOOO00OO00O0O0O =requests .request ('get',f'{host}/game/getAllData',headers =OOOO000O0OO0O0OOO ).json ()#line:396
            if 'status'in O0OOOO00OO00O0O0O :#line:398
                if O0OOOO00OO00O0O0O ['status']==200 :#line:399
                    if 'offlineInfo'in O0OOOO00OO00O0O0O ['data']:#line:400
                        time .sleep (random .randint (3 ,5 ))#line:401
                        O00000O00O00OO000 =O0OOOO00OO00O0O0O ['data']['offlineInfo']['off_minute']#line:402
                        O0O0O0O000OO00000 =float (O0OOOO00OO00O0O0O ['data']['silver'])/1000000000000 #line:403
                        time .sleep (1 )#line:404
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOOO000O0OO0O0OOO ).json ()#line:405
                        time .sleep (2 )#line:406
                        O00OO00000O0O000O =requests .request ('get',f'{host}/game/getAllData',headers =OOOO000O0OO0O0OOO ).json ()#line:407
                        if 'status'in O00OO00000O0O000O :#line:409
                            if O00OO00000O0O000O ['status']==200 :#line:410
                                OOOOO0O00O0OOOOOO =float (O00OO00000O0O000O ['data']['silver'])/1000000000000 #line:411
                                OOO00000O0000O0O0 =str (OOOOO0O00O0OOOOOO -O0O0O0O000OO00000 )[:6 ]#line:412
                                print (f'【离线奖励】:翻倍离线{O00000O00O00OO000}分钟奖励🌱数量:{OOO00000O0000O0O0}t粒')#line:413
        except Exception as O0O0OOO000OOO0000 :#line:414
            print (O0O0OOO000OOO0000 )#line:415
    def user_ad (O0O0OOO000OOOO0OO ):#line:418
        try :#line:419
            O00O00OO00000OOOO =f'__{timi_new()}'#line:420
            O000O0000OO0OOOO0 ={'authorization':O0O0OOO000OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO00000OOOO ),'signstring':O00O00OO00000OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:429
            O000O0OOO0O00O00O =requests .request ('get',f'{host}/user/ad',headers =O000O0000OO0OOOO0 ).json ()#line:430
            if 'status'in O000O0OOO0O00O00O :#line:432
                if O000O0OOO0O00O00O ['status']==200 :#line:433
                    O0000OO000OO0OOO0 =O000O0OOO0O00O00O ['data']['max_time']#line:434
                    OOO0O0OO0OO0000O0 =O000O0OOO0O00O00O ['data']['watch_time']#line:435
                    O00OOOO0OO0O0O0O0 =O000O0OOO0O00O00O ['data']['added_time']#line:436
                    print (f'【获取种子】:获取🌱剩余{O00OOOO0OO0O0O0O0 + O0000OO000OO0OOO0 - OOO0O0OO0OO0000O0}次丨好友提供:{O00OOOO0OO0O0O0O0}次')#line:437
                    if O00OOOO0OO0O0O0O0 +O0000OO000OO0OOO0 -OOO0O0OO0OO0000O0 >0 :#line:438
                        time .sleep (random .randint (16 ,19 ))#line:439
                        OOO00000O00OO0O0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O000O0000OO0OOOO0 ).json ()#line:440
                        if 'status'in OOO00000O00OO0O0O :#line:442
                            if OOO00000O00OO0O0O ['status']==200 :#line:443
                                O0O000OO0000000O0 =float (OOO00000O00OO0O0O ['data']['silver'])/1000000000000 #line:444
                                print (f'【获取种子】:获得🌱:{int(O0O000OO0000000O0)}t粒')#line:445
                                return True #line:446
                            if OOO00000O00OO0O0O ['status']==500 :#line:447
                                O00OOO0OOOO000O00 =OOO00000O00OO0O0O ['message']#line:448
                                print (f'【获取种子】:{O00OOO0OOOO000O00}')#line:449
                                return False #line:450
        except Exception as OO0OOO000OOOO000O :#line:451
            print (OO0OOO000OOOO000O )#line:452
    def synthetic (O0OO00OOOO0OOO0O0 ):#line:455
        global id ,g #line:456
        try :#line:457
            OO000OOOOO0O00000 =O0OO00OOOO0OOO0O0 .level_new ()#line:458
            O00000O0O00000O0O =random .randint (9 ,11 )#line:459
            OOOO0O000000OOOOO =f'_site=8&targetSite={O00000O0O00000O0O}_{timi_new()}'#line:460
            OO000OO00OOO0O000 ={'accept':'application/json, text/plain, */*','authorization':O0OO00OOOO0OOO0O0 .token ,'timestamp':timi_new (),'sign':sign (OOOO0O000000OOOOO ),'signstring':OOOO0O000000OOOOO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:475
            OO00O0O00O0O0OOOO ={"site":int (8 ),"targetSite":int (O00000O0O00000O0O )}#line:476
            requests .request ('post',f'{host}/game/crops/move',headers =OO000OO00OOO0O000 ,json =OO00O0O00O0O0OOOO )#line:477
            while True :#line:478
                O000O0OOOOO00OOO0 =f'__{timi_new()}'#line:479
                OO0O0O00O0O000O00 ={'authorization':O0OO00OOOO0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOOOO00OOO0 ),'signstring':O000O0OOOOO00OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:488
                O0000000O00O0OOOO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O00O0O000O00 ).json ()#line:489
                if 'status'in O0000000O00O0OOOO :#line:491
                    if O0000000O00O0OOOO ['status']==200 :#line:492
                        OO0000OOOOO0O00O0 =O0000000O00O0OOOO ['data']['cropList']#line:493
                        O0O0000OOO0O00O0O =O0000000O00O0OOOO ['data']['gameCoreDataDBid']#line:494
                        O0OOOOOO0OOOOO0O0 =float (O0000000O00O0OOOO ['data']['silver'])/1000000000000 #line:495
                        OO0OOO0O00OO0O0OO =0 #line:500
                        for O00O00OOOO0O000OO in OO0000OOOOO0O00O0 :#line:501
                            if not O00O00OOOO0O000OO :#line:502
                                O0O00OOOO000000OO =f'_crop_id={O0O0000OOO0O00O0O}&site={OO0OOO0O00OO0O0OO}_{O0OO00OOOO0OOO0O0.time}'#line:503
                                OOOO0OOO00OOOO0OO ={'authorization':O0OO00OOOO0OOO0O0 .token ,'timestamp':O0OO00OOOO0OOO0O0 .time ,'sign':sign (O0O00OOOO000000OO ),'signstring':O0O00OOOO000000OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
                                OO00O0000000O0OO0 ={"site":OO0OOO0O00OO0O0OO ,"crop_id":O0O0000OOO0O00O0O }#line:513
                                O000000OOOO000O00 =requests .request ('post',f'{host}/game/crops/buy',headers =OOOO0OOO00OOOO0OO ,data =OO00O0000000O0OO0 ).json ()#line:514
                                time .sleep (random .randint (1 ,3 )/10 )#line:516
                                if 'status'in O000000OOOO000O00 :#line:517
                                    if O000000OOOO000O00 ['status']==200 :#line:518
                                        if O000000OOOO000O00 ['message']=='种子数量不足':#line:519
                                            OO000OOOOO0O00000 =O0OO00OOOO0OOO0O0 .level_new ()#line:520
                                            print (f'【种植合成】:{O000000OOOO000O00["message"]}')#line:521
                                            if not O0OO00OOOO0OOO0O0 .user_ad ():#line:522
                                                return False #line:523
                                    if O000000OOOO000O00 ['status']==500 :#line:524
                                        print (f'【种植合成】:{O000000OOOO000O00["message"]}')#line:525
                                        return False #line:526
                            OO0OOO0O00OO0O0OO +=1 #line:527
                        O0OO00OOOOOOO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O00O0O000O00 ).json ()#line:528
                        O00O0OO0000O00O00 =O0OO00OOOOOOO0O0O ['data']['cropList']#line:529
                        O0O00O0OO000O0OOO =False #line:530
                        for O00O00OOOO0O000OO in range (12 ):#line:531
                            id =O00O0OO0000O00O00 [O00O00OOOO0O000OO ]['level']#line:532
                            if float (OO000OOOOO0O00000 )-float (id )>9 :#line:533
                                OOOO0OOOOOOO0OOOO =f'_site={O00O00OOOO0O000OO}_{timi_new()}'#line:534
                                OO0O000OOO000O0OO ={'accept':'application/json, text/plain, */*','authorization':O0OO00OOOO0OOO0O0 .token ,'timestamp':timi_new (),'sign':sign (OOOO0OOOOOOO0OOOO ),'signstring':OOOO0OOOOOOO0OOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:544
                                OO0O0O0O0OOO0OOO0 ={"site":O00O00OOOO0O000OO }#line:545
                                OOOOO0OOO00O00OO0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0O000OOO000O0OO ,data =OO0O0O0O0OOO0OOO0 ).json ()#line:547
                                if 'status'in OOOOO0OOO00O00OO0 :#line:548
                                    if OOOOO0OOO00O00OO0 ['status']==200 :#line:549
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:550
                            if id !=0 :#line:551
                                for OO00OOOO0O00OOO0O in range (11 ):#line:552
                                    OO0OOOO0O0OOO0000 =OO00OOOO0O00OOO0O +1 #line:553
                                    g =O00O0OO0000O00O00 [OO0OOOO0O0OOO0000 ]['level']#line:554
                                    if id ==g :#line:555
                                        OO00000OO000OO000 =OO00OOOO0O00OOO0O +2 #line:556
                                        if OO00000OO000OO000 !=O00O00OOOO0O000OO +1 :#line:557
                                            O0O0OOOO0OO00OOO0 =O00O00OOOO0O000OO +1 #line:558
                                            time .sleep (random .randint (1 ,3 )/10 )#line:560
                                            OOOO0O000000OOOOO =f'_site={O0O0OOOO0OO00OOO0 - 1}&targetSite={OO00000OO000OO000 - 1}_{timi_new()}'#line:561
                                            OO000OO00OOO0O000 ={'accept':'application/json, text/plain, */*','authorization':O0OO00OOOO0OOO0O0 .token ,'timestamp':timi_new (),'sign':sign (OOOO0O000000OOOOO ),'signstring':OOOO0O000000OOOOO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:576
                                            O0OO00O0OOO0OO000 ={"site":int (O0O0OOOO0OO00OOO0 -1 ),"targetSite":int (OO00000OO000OO000 -1 )}#line:577
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO000OO00OOO0O000 ,json =O0OO00O0OOO0OO000 )#line:578
                                            O0O00O0OO000O0OOO =True #line:580
                                    if O0O00O0OO000O0OOO :#line:581
                                        break #line:582
                                if O0O00O0OO000O0OOO :#line:583
                                    break #line:584
        except :#line:585
            O0OO00OOOO0OOO0O0 .synthetic ()#line:586
    def level_new (OO0OO000OO0OO00OO ):#line:589
        try :#line:590
            OO00000OOO00O0O0O =f'__{timi_new()}'#line:591
            OOOOO0O0O0OO000O0 ={'authorization':OO0OO000OO0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OOO00O0O0O ),'signstring':OO00000OOO00O0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            OOO0OO0OO0O0O0OOO =requests .request ('get',f'{host}/user',headers =OOOOO0O0O0OO000O0 ).json ()#line:601
            if 'status'in OOO0OO0OO0O0O0OOO :#line:602
                if OOO0OO0OO0O0O0OOO ['status']==200 :#line:603
                    return float (OOO0OO0OO0O0O0OOO ['data']['level'])#line:604
        except Exception as OO000O00OO0OOO0O0 :#line:605
            print (OO000O00OO0OOO0O0 )#line:606
    def propsraffle (OO0O0O0OO00OOO0OO ):#line:609
        try :#line:610
            while True :#line:611
                O000OOO0O000O0O0O =f'__{timi_new()}'#line:612
                O000O0000000O00OO ={'authorization':OO0O0O0OO00OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0O000O0O0O ),'signstring':O000OOO0O000O0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:621
                O0O00O000O0O0O0OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O000O0000000O00OO ).json ()#line:622
                if 'status'in O0O00O000O0O0O0OO :#line:624
                    if O0O00O000O0O0O0OO ['status']==200 :#line:625
                        OO0O00OOO00OOO00O =O0O00O000O0O0O0OO ['data']['rows']#line:626
                        O0OO0OOOO0000O00O =O0O00O000O0O0O0OO ['data']['vstate']#line:627
                        if OO0O00OOO00OOO00O ==5 or OO0O00OOO00OOO00O ==6 or OO0O00OOO00OOO00O ==7 :#line:628
                            O000000O0OO0OOOOO =O0O00O000O0O0O0OO ['data']['silver']#line:629
                            print (f'【转盘抽奖】:获得种子:{O000000O0OO0OOOOO}')#line:630
                        if OO0O00OOO00OOO00O ==1 or OO0O00OOO00OOO00O ==2 or OO0O00OOO00OOO00O ==3 :#line:631
                            O00OOOOOOOOO00OOO =O0O00O000O0O0O0OO ['data']['clover']#line:632
                            print (f'【转盘抽奖】:获得三叶草:{O00OOOOOOOOO00OOO}')#line:633
                        if OO0O00OOO00OOO00O ==4 or OO0O00OOO00OOO00O ==8 :#line:634
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:635
                        if OO0O00OOO00OOO00O =='抽奖次数已用完':#line:639
                            break #line:672
                time .sleep (random .randint (8 ,15 )/10 )#line:673
        except Exception as O0OO000OOO00OO0OO :#line:674
            print (O0OO000OOO00OO0OO )#line:675
    def friends_invitation (O0OO00OOO0000000O ):#line:678
        try :#line:679
            OO00OO0O00OOO00O0 =f'__{timi_new()}'#line:680
            O00O000OO0OOO00O0 ={'authorization':O0OO00OOO0000000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0O00OOO00O0 ),'signstring':OO00OO0O00OOO00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:689
            OOO0000OO0OOO0O0O =requests .request ('get',f'{host}/friends',headers =O00O000OO0OOO00O0 ).json ()#line:690
            if 'status'in OOO0000OO0OOO0O0O :#line:691
                if OOO0000OO0OOO0O0O ['status']==200 :#line:692
                    OOO0OOO0O0000OOOO =OOO0000OO0OOO0O0O ['data']['myInviteter']#line:693
                    if OOO0OOO0O0000OOOO :#line:694
                        O0OO00OOO00OOOO00 =OOO0OOO0O0000OOOO ['user']['nickname']#line:695
                        OO0OO0O0O000OOO00 =O0OO00OOO0000000O .certification ()#line:696
                        print (f'【查邀请人】:我的邀请人:{O0OO00OOO00OOOO00}丨实名:{OO0OO0O0O000OOO00}')#line:697
                    else :#line:698
                        if O0OO00OOO0000000O .innerId !='0':#line:699
                            O0OO00OOO0000000O .invitation ()#line:700
        except Exception as OOOOOOO000OOO000O :#line:701
            print (OOOOOOO000OOO000O )#line:702
    def add_clover (OO000OOOOO0OOO00O ):#line:705
        global golden_seed #line:706
        try :#line:707
            O0O0O0O0OO00OO000 =f'__{timi_new()}'#line:708
            OO0000000OOOOOO0O ={'authorization':OO000OOOOO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0OO00OO000 ),'signstring':O0O0O0O0OO00OO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:717
            OO000O0OOO00O0000 =requests .request ('get',f'{host}/assets/clovers',headers =OO0000000OOOOOO0O ).json ()#line:718
            if 'status'in OO000O0OOO00O0000 :#line:720
                if OO000O0OOO00O0000 ['status']==200 :#line:721
                    OOOOOO000O0OO000O =OO000O0OOO00O0000 ['data']['clover']#line:722
                    O0OOO000O0000000O =OO000O0OOO00O0000 ['data']['used_clover']#line:723
                    OOOO000O0O0OO0000 =float (OOOOOO000O0OO000O )-float (O0OOO000O0000000O )#line:724
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OOO000O0000000O}')#line:725
                    if OO000OOOOO0OOO00O .certification ()!='未实名':#line:726
                        if OOOO000O0O0OO0000 >1 :#line:727
                            O0O0O0O0OO00OO000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOO000O0O0OO0000)}_{timi_new()}'#line:728
                            OO0O00OO000OO0000 ={'authorization':OO000OOOOO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0OO00OO000 ),'signstring':O0O0O0O0OO00OO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                            O00O0OOOO0O0OOO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOO000O0O0OO0000 )}#line:738
                            O00OOO000O0O0000O =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0O00OO000OO0000 ,data =O00O0OOOO0O0OOO00 ).json ()#line:739
                            if 'status'in O00OOO000O0O0000O :#line:741
                                if O00OOO000O0O0000O ['status']==200 :#line:742
                                    print (f'【参与抽奖】:添加☘️:{O00OOO000O0O0000O["data"]}丨数量:{OOOO000O0O0OO0000}')#line:743
                                if O00OOO000O0O0000O ['status']==500 :#line:744
                                    print (f'【参与抽奖】:添加☘️:{O00OOO000O0O0000O["message"]}')#line:745
            O0OOOOOO0000OO000 =requests .request ('get',f'{host}/lottery',headers =OO0000000OOOOOO0O ).json ()#line:746
            OOO0OO0O000000O0O =OO000OOOOO0OOO00O .winning_rewards ()#line:748
            if 'status'in O0OOOOOO0000OO000 :#line:749
                if O0OOOOOO0000OO000 ['status']==200 :#line:750
                    OOOOOO0O0OOO0O00O =O0OOOOOO0000OO000 ['data'][0 ]['day_get_gold_quantity']#line:751
                    golden_seed +=float (OOOOOO0O0OOO0O00O )#line:752
                    OOO0OO0O00000O00O =O0OOOOOO0000OO000 ['data'][1 ]['value']#line:753
                    OO00O0O0O0OOOO000 =O0OOOOOO0000OO000 ['data'][0 ]['join_number']#line:754
                    O000OO0000OO00O0O =int (float (O0OOOOOO0000OO000 ['data'][0 ]['totalValue']))#line:755
                    O00O0OOOOO0O0OOO0 =float (OOO0OO0O00000O00O /O000OO0000OO00O0O )*10000 #line:756
                    OOOOO0000O0O00OOO =O000OO0000OO00O0O /OO00O0O0O0OOOO000 #line:757
                    print (f'【参与抽奖】:预计每天中{str(OOOOOO0O0OOO0O00O)[:6]}颗金种子丨好友收益:{str(OOO0OO0O000000O0O)[:6]}')#line:758
                    print (f'【抽奖统计】:每1万☘️中{str(O00O0OOOOO0O0OOO0)[:6]}颗金种子丨☘️人均:{str(OOOOO0000O0O00OOO)[:7]}️')#line:759
        except Exception as OO0000O0O0O0O0O0O :#line:760
            print (OO0000O0O0O0O0O0O )#line:761
    def energy (OOO0O0OOO0O000OO0 ):#line:765
        try :#line:766
            while True :#line:767
                OOO00O00OO000O0O0 =f'__{timi_new()}'#line:768
                OO0OO00000O00O000 ={'authorization':OOO0O0OOO0O000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00OO000O0O0 ),'signstring':OOO00O00OO000O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:777
                OO000OO0OOOO000OO =requests .request ('get',f'{host}/energy/general',headers =OO0OO00000O00O000 ).json ()#line:778
                if 'status'in OO000OO0OOOO000OO :#line:780
                    if OO000OO0OOOO000OO ['status']==200 :#line:781
                        OOOOOO00O0OO0OOO0 =OO000OO0OOOO000OO ['data']['ordinary_water']#line:782
                        OOO0OOO0OO00OO0O0 =OO000OO0OOOO000OO ['data']['ordinary_fertilizer']#line:783
                        OO000OO00OO0OO00O =OO000OO0OOOO000OO ['data']['videoStatus']#line:784
                        print (f'【我的营养】:肥料:{str(OOO0OOO0OO00OO0O0).split(".")[0]}丨水滴:{str(OOOOOO00O0OO0OOO0).split(".")[0]}')#line:785
                        if float (OOO0OOO0OO00OO0O0 )<96 :#line:786
                            if OO000OO00OO0OO00O :#line:787
                                time .sleep (random .randint (160 ,180 )/10 )#line:788
                                OO0OO0OO00OOO000O =99 -float (OOO0OOO0OO00OO0O0 )#line:789
                                O000O0O00OOO00000 ={"fertilizer":str (OO0OO0OO00OOO000O ).split ('.')[0 ]}#line:790
                                O0OOOOO00O00O00O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0OO00000O00O000 ).json ()#line:791
                                if 'status'in O0OOOOO00O00O00O0 :#line:793
                                    if O0OOOOO00O00O00O0 ['status']==200 :#line:794
                                        print (f'【购买肥料】:看广告获取肥料:{O0OOOOO00O00O00O0["message"]}')#line:795
                                    if O0OOOOO00O00O00O0 ['status']==500 :#line:796
                                        print (f'【购买肥料】:看广告获取肥料:{O0OOOOO00O00O00O0["message"]}')#line:797
                                        break #line:798
                        if float (OOOOOO00O0OO0OOO0 )<880 :#line:799
                            time .sleep (random .randint (160 ,180 )/10 )#line:800
                            O0000000O00OO0OO0 =999 -float (OOOOOO00O0OO0OOO0 )#line:801
                            OO00OOOOO00OO0O00 ={"water":str (O0000000O00OO0OO0 ).split ('.')[0 ]}#line:802
                            OO000000OOOOO00OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0OO00000O00O000 ).json ()#line:803
                            if 'status'in OO000000OOOOO00OO :#line:805
                                if OO000000OOOOO00OO ['status']==200 :#line:806
                                    print (f'【购买水滴】:看广告获取水滴:{OO000000OOOOO00OO["message"]}')#line:807
                                if OO000000OOOOO00OO ['status']==500 :#line:808
                                    print (f'【购买水滴】:看广告获取水滴:{OO000000OOOOO00OO["message"]}')#line:809
                                    break #line:810
                        break #line:812
        except Exception as O000000OOO0O000O0 :#line:814
            print (O000000OOO0O000O0 )#line:815
def bundled_def ():#line:817
    OOO00000OOO00O0O0 =['5570536','7750212','7911652','7911680','7805624']#line:818
    return OOO00000OOO00O0O0 [random .randint (0 ,len (OOO00000OOO00O0O0 )-1 )]#line:819
def version_of_the_validation ():#line:823
    return str ((80 -56 )/10 )#line:824
def gitee_validation ():#line:827
    try :#line:828
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:829
    except :#line:830
        sys .exit (0 )#line:831
def update_the_validation ():#line:835
    try :#line:836
        OOO0OO00O0O0OOOOO =gitee_validation ()#line:837
        if version_of_the_validation ()<OOO0OO00O0O0OOOOO ['CityEarth']['edition']:#line:838
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OO00O0O0OOOOO["CityEarth"]["edition"]}   ❌')#line:839
            print (f'更新内容=>>{OOO0OO00O0O0OOOOO["CityEarth"]["content"]}   🎉')#line:840
        else :#line:841
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OO00O0O0OOOOO["CityEarth"]["edition"]}   ✅')#line:842
            print (f'更新内容=>> {OOO0OO00O0O0OOOOO["CityEarth"]["content"]}   🎉')#line:843
    except Exception as O0O00O0OO0OOOOOOO :#line:844
        print (O0O00O0OO0OOOOOOO )#line:845
def os_qinglong ():#line:848
    if application in os .environ :#line:849
        O0000O0000O0OOOOO =os .environ [application ].split ('\n')#line:850
        if len (O0000O0000O0OOOOO )>0 :#line:851
            return O0000O0000O0OOOOO #line:852
        else :#line:853
            print (f"{application}变量未启用")#line:854
            print ('脚本退出')#line:855
            sys .exit (1 )#line:856
    else :#line:857
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:859
        return os_built ()#line:860
def os_built ():#line:863
    if token :#line:864
        OOO00000000000000 =token .split ('\n')#line:865
        if len (OOO00000000000000 )>0 :#line:866
            return OOO00000000000000 #line:867
    else :#line:868
        print (f"内置变量为空")#line:869
        print ('脚本结束')#line:870
        sys .exit (0 )#line:871
if __name__ =='__main__':#line:874
    start ()#line:875
