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
        OO00O0OO00O0OOO0O =os_qinglong ()#line:10
        print (f"==========共找到{len(OO00O0OO00O0OOO0O)}个账号==========")#line:11
        for OOO0OOOOO0O00O0O0 in OO00O0OO00O0OOO0O :#line:12
            OOOO00OO0O0O0O00O =[]#line:13
            print (f"------------正在执行第{OO00O0OO00O0OOO0O.index(OOO0OOOOO0O00O0O0) + 1}个账号------------")#line:14
            O0O00O00O00O00O00 =CityEarth (OOO0OOOOO0O00O0O0 ,OOOO00OO0O0O0O00O )#line:15
            def O0OO000O000OOO000 ():#line:17
                if O0O00O00O00O00O00 .base_info ():#line:19
                    O0O00O00O00O00O00 .sealing ()#line:21
                    O0O00O00O00O00O00 .invitenum ()#line:23
                    O0O00O00O00O00O00 .game_map ()#line:25
                    O0O00O00O00O00O00 .friends_invitation ()#line:27
                    O0O00O00O00O00O00 .add_clover ()#line:29
                    O0O00O00O00O00O00 .propsraffle ()#line:31
                    O0O00O00O00O00O00 .synthetic ()#line:33
                    O0O00O00O00O00O00 .crops_illustrated ()#line:35
                    O0O00O00O00O00O00 .give_gold ()#line:37
                    O0O00O00O00O00O00 .withdraw ()#line:39
                    O0O00O00O00O00O00 .energy ()#line:41
            OO0OO000000OOO000 =threading .Thread (target =O0OO000O000OOO000 )#line:42
            OO0OO000000OOO000 .start ()#line:43
            time .sleep (time_xx )#line:44
        print (f"------------正在处理推送通知------------")#line:45
        time .sleep (0.5 )#line:46
        OO0O00O0000OO0OO0 =format_msg ()#line:47
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0O00O0000OO0OO0 +' ')#line:48
    except Exception as OO00O00OO000OO0OO :#line:49
        print (OO00O00OO000OO0OO )#line:50
def sign (OO00OOO00O0O000O0 ):#line:53
    O00OOO000O0O00O00 =hashlib .md5 (OO00OOO00O0O000O0 .encode ()).hexdigest ()#line:54
    OO0O0000OOO000OOO ="scsc%^&*"+O00OOO000O0O00O00 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    OOOOOOO0OO0000O0O =hashlib .md5 (OO0O0000OOO000OOO .encode ()).hexdigest ()#line:56
    return OOOOOOO0OO0000O0O #line:57
def format_msg ():#line:59
    OO0000O0O000O00OO =""#line:60
    for O0000OO0OOO000O00 in msg_list :#line:61
        OO0000O0O000O00OO +=str (O0000OO0OOO000O00 )+"\r\n"#line:62
    return OO0000O0O000O00OO #line:63
def timi_new ():#line:65
    return str (int (time .time ()*1000 ))#line:66
class CityEarth :#line:69
    def __init__ (OO000O0OOO0OO0O0O ,O0OOO00OO0000O000 ,O000OO0OOOOOOO00O ):#line:71
        try :#line:72
            OO000O0OOO0OO0O0O .msg =O000OO0OOOOOOO00O #line:73
            OO000O0OOO0OO0O0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:74
            OO000O0OOO0OO0O0O .token =O0OOO00OO0000O000 .split ('&')[0 ]#line:75
            OO000O0OOO0OO0O0O .innerId =O0OOO00OO0000O000 .split ('&')[1 ]#line:76
            OO000O0OOO0OO0O0O .doneeNo =O0OOO00OO0000O000 .split ('&')[2 ]#line:77
        except :#line:78
            print ('变量格式错误')#line:79
    def base_info (OO00O000O00O0O000 ):#line:82
        try :#line:83
            OO00O000O00O0O000 .watched_ad ()#line:85
            OOOOOO0OO0OOOOO00 =f'__{timi_new()}'#line:86
            OOOOOO000000O00O0 ={'authorization':OO00O000O00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OO0OOOOO00 ),'signstring':OOOOOO0OO0OOOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            O0O0O0O0OOO00OOOO =requests .request ('get',f'{host}/user',headers =OOOOOO000000O00O0 ).json ()#line:96
            if 'status'in O0O0O0O0OOO00OOOO :#line:98
                if O0O0O0O0OOO00OOOO ['status']==200 :#line:99
                    O00000OOOOOO0OOO0 =O0O0O0O0OOO00OOOO ['data']['nickname']#line:100
                    OO0O000OOO0OO00OO =O0O0O0O0OOO00OOOO ['data']['inner_id']#line:101
                    OO00OO0OOOOOO0O0O =O0O0O0O0OOO00OOOO ['data']['assets']['gold']#line:102
                    OOO000OO0O0OO0000 =O0O0O0O0OOO00OOOO ['data']['level']#line:103
                    print (f'【账号信息】:昵称:{O00000OOOOOO0OOO0[:5]}丨ID:{OO0O000OOO0OO00OO}丨等级:{OOO000OO0O0OO0000}丨种子:{str(OO00OO0OOOOOO0O0O).split(".")[0]}')#line:104
                if O0O0O0O0OOO00OOOO ['status']==401 :#line:105
                    print (O0O0O0O0OOO00OOOO ['message'])#line:106
                    OO00O000O00O0O000 .msg .append ('有账号失效了')#line:107
                    return False #line:108
                if O0O0O0O0OOO00OOOO ['status']==500 :#line:109
                    return False #line:110
            return True #line:111
        except Exception as O0O0OOO0OOO000OO0 :#line:112
            print (O0O0OOO0OOO000OO0 )#line:113
    def sealing (OOO0O0OO000OOOO0O ):#line:116
        try :#line:117
            OO00O00OOO000O0O0 =f'__{timi_new()}'#line:118
            O000O0OO0O000OO00 ={'authorization':OOO0O0OO000OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OOO000O0O0 ),'signstring':OO00O00OOO000O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:127
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O000O0OO0O000OO00 )#line:128
            requests .request ('get',f'{host}/packsack/list',headers =O000O0OO0O000OO00 )#line:129
            requests .request ('get',f'{host}/friends/invited/ad',headers =O000O0OO0O000OO00 )#line:130
            requests .request ('get',f'{host}/assets/gold/rank',headers =O000O0OO0O000OO00 )#line:131
            requests .request ('get',f'{host}/user',headers =O000O0OO0O000OO00 )#line:132
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O000O0OO0O000OO00 )#line:133
            requests .request ('get',f'{host}/finance/get-power-list',headers =O000O0OO0O000OO00 )#line:134
            requests .request ('post',f'{host}/announcement/announcement',headers =O000O0OO0O000OO00 )#line:135
            requests .request ('get',f'{host}/game/getAllData',headers =O000O0OO0O000OO00 )#line:136
            requests .request ('get',f'{host}/assets',headers =O000O0OO0O000OO00 )#line:137
        except Exception as O0000O000000OOOO0 :#line:138
            print (O0000O000000OOOO0 )#line:139
    def withdraw (OOO000O0OO0O0OOO0 ):#line:143
        O00OOOO0OO000O000 =f'__{timi_new()}'#line:144
        OOO0OO0O00000O0O0 ={'authorization':OOO000O0OO0O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0OO000O000 ),'signstring':O00OOOO0OO000O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
        OO0O00OOOO0O0O00O =requests .request ('get',f'{host}/assets',headers =OOO0OO0O00000O0O0 ).json ()#line:154
        if 'status'in OO0O00OOOO0O0O00O :#line:156
            if OO0O00OOOO0O0O00O ['status']==200 :#line:157
                O00O00O00O0OOO00O =OO0O00OOOO0O0O00O ['data']['cash']#line:158
                if float (O00O00O00O0OOO00O )>20 :#line:159
                    O00OOOO0OO000O000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:160
                    OOO0OO0O00000O0O0 ={'authorization':OOO000O0OO0O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0OO000O000 ),'signstring':O00OOOO0OO000O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
                    OOO0OO00OO0O00O0O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:170
                    O0O0OOOO0000OOO0O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOO0OO0O00000O0O0 ,data =OOO0OO00OO0O00O0O ).json ()#line:172
                    print (O0O0OOOO0000OOO0O )#line:173
    def invitenum (OOO0O00OO0OOOOOO0 ):#line:176
        O0O0OOOO0OOO00000 =f'__{timi_new()}'#line:177
        O0OO00000O0OO0O0O ={'authorization':OOO0O00OO0OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOO0OOO00000 ),'signstring':O0O0OOOO0OOO00000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
        O0OO000000OO00OOO =requests .request ('get',f'{host}/invite/invitenum',headers =O0OO00000O0OO0O0O ).json ()#line:187
        if 'status'in O0OO000000OO00OOO :#line:189
            if O0OO000000OO00OOO ['status']==200 :#line:190
                OOO0OOO000OO0OOO0 =O0OO000000OO00OOO ['data']['invited_count']#line:191
                O00O0OO000OOO00O0 =O0OO000000OO00OOO ['data']['invited_second_count']#line:192
                print (f'【我的邀请】:直邀好友:{OOO0OOO000OO0OOO0}丨间邀好友:{O00O0OO000OOO00O0}')#line:193
    def game_map (OO0O0OOOOO0OOO0OO ):#line:196
        try :#line:197
            O0OOOO00O0OOO00O0 =f'__{timi_new()}'#line:198
            O0OO0O0000OOO000O ={'authorization':OO0O0OOOOO0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00O0OOO00O0 ),'signstring':O0OOOO00O0OOO00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            O0OOO0OOO00OOO0OO =requests .request ('get',f'{host}/game/map',headers =O0OO0O0000OOO000O ).json ()#line:208
            if 'status'in O0OOO0OOO00OOO0OO :#line:210
                if O0OOO0OOO00OOO0OO ['status']==200 :#line:211
                    for O00OOO00O0O0OO00O in O0OOO0OOO00OOO0OO ['data']['list'][0 ]['crops']:#line:212
                        OO000OOO0OO00O0OO =O00OOO00O0O0OO00O ['level']#line:214
                        if OO000OOO0OO00O0OO ==41 :#line:215
                            OOOO0OOO0OOO0000O =O00OOO00O0O0OO00O ['crop_name']#line:216
                            O0O0OOO0OOO0O0OOO =O00OOO00O0O0OO00O ['count']#line:217
                            if O0O0OOO0OOO0O0OOO >0 :#line:218
                                print (f'【农业资产】:{OOOO0OOO0OOO0000O}丨数量:{O0O0OOO0OOO0O0OOO}')#line:219
        except Exception as O00OOO0O00O0000O0 :#line:220
            print (O00OOO0O00O0000O0 )#line:221
    def give_gold (OOO00OO0OO0O0O00O ):#line:224
        try :#line:225
            O0O0O0O0O000O0O0O =f'__{timi_new()}'#line:226
            OOOO0OOO0OO0000OO ={'authorization':OOO00OO0OO0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0O000O0O0O ),'signstring':O0O0O0O0O000O0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:235
            OO00OO0OOO000OO00 =requests .request ('get',f'{host}/user',headers =OOOO0OOO0OO0000OO ).json ()#line:236
            if 'status'in OO00OO0OOO000OO00 :#line:237
                if OO00OO0OOO000OO00 ['status']==200 :#line:238
                    if float (OOO00OO0OO0O0O00O .doneeNo )!=0 :#line:239
                        O0OO0O00OO0OOO0O0 =OO00OO0OOO000OO00 ['data']['assets']['gold']#line:240
                        if float (O0OO0O00OO0OOO0O0 )>float (OOO00OO0OO0O0O00O .innerId ):#line:241
                            O0OO0OO0000O00O00 =int (float (O0OO0O00OO0OOO0O0 )/1.1 )#line:242
                            O0O0O0O0O000O0O0O =f'_doneeNo={OOO00OO0OO0O0O00O.doneeNo}&quantity={O0OO0OO0000O00O00}_{timi_new()}'#line:243
                            OOOO0OOO0OO0000OO ={'authorization':OOO00OO0OO0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0O000O0O0O ),'signstring':O0O0O0O0O000O0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
                            OOO000O000O00OO0O ={"quantity":O0OO0OO0000O00O00 ,"doneeNo":OOO00OO0OO0O0O00O .doneeNo }#line:256
                            OOO00OO0O0O0OOO00 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOO0OOO0OO0000OO ,data =OOO000O000O00OO0O ).json ()#line:257
                            if 'status'in OOO00OO0O0O0OOO00 :#line:259
                                if OOO00OO0O0O0OOO00 ['status']==200 :#line:260
                                    if OOO00OO0O0O0OOO00 ['data']:#line:261
                                        print (f'【赠送种子】:赠送{O0OO0OO0000O00O00}种子给{OOO00OO0OO0O0O00O.doneeNo}成功')#line:262
                    else :#line:263
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:264
        except Exception as OO00O0OOO00O00000 :#line:265
            print (OO00O0OOO00O00000 )#line:266
    def invitation (O0000O0O00O00O0O0 ):#line:268
        try :#line:269
            _OOOOOOO0OO0OO0O0O =float (bundled_def ())/4 #line:270
            O00O0OOO0O00OOO0O =f'_innerId={int(_OOOOOOO0OO0OO0O0O)}_{timi_new()}'#line:271
            OOO00OOOO0OO0OO00 ={'authorization':O0000O0O00O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO0O00OOO0O ),'signstring':O00O0OOO0O00OOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:280
            O0OOO00OO00O0OOOO ={"innerId":int (_OOOOOOO0OO0OO0O0O )}#line:281
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO00OOOO0OO0OO00 ,data =O0OOO00OO00O0OOOO )#line:282
        except Exception as OOOOOOO0O0O000000 :#line:283
            print (OOOOOOO0O0O000000 )#line:284
    def winning_rewards (OOO0OOO0O0O0OO00O ):#line:287
        try :#line:288
            OOO0O0O0OOOO00OOO =f'__{timi_new()}'#line:289
            OO00OOO00O00O0O00 ={'authorization':OOO0OOO0O0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OOOO00OOO ),'signstring':OOO0O0O0OOOO00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:298
            OOO0O000O0O00O000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO00OOO00O00O0O00 ).json ()#line:299
            if 'status'in OOO0O000O0O00O000 :#line:301
                if OOO0O000O0O00O000 ['status']==200 :#line:302
                    if OOO0O000O0O00O000 ['data']['amount']:#line:303
                        O00O0O0O0O0OOO00O =OOO0O000O0O00O000 ['data']['amount']['gold']#line:304
                        return O00O0O0O0O0OOO00O #line:305
                    else :#line:306
                        return 0 #line:307
        except Exception as O0OOOO000O0OOO000 :#line:308
            print (O0OOOO000O0OOO000 )#line:309
    def certification (OOO0O00OO0000OOOO ):#line:312
        try :#line:313
            OO0OOO000O00OO00O =f'__{timi_new()}'#line:314
            OOO0O0OO00000O000 ={'authorization':OOO0O00OO0000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO000O00OO00O ),'signstring':OO0OOO000O00OO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OO0OO0O0OO00O0OOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO0O0OO00000O000 ).json ()#line:324
            if 'status'in OO0OO0O0OO00O0OOO :#line:326
                if OO0OO0O0OO00O0OOO ['status']==200 :#line:327
                    if OO0OO0O0OO00O0OOO ['data']['result']:#line:328
                        O0O00OO00OO00O0O0 =OO0OO0O0OO00O0OOO ['data']['nick_name']#line:329
                        return O0O00OO00OO00O0O0 #line:330
                    else :#line:331
                        return '未实名'#line:332
        except Exception as O000OOOOO0OO0OO00 :#line:333
            print (O000OOOOO0OO0OO00 )#line:334
    def crops_illustrated (OO0OOOO000OO0OOO0 ):#line:337
        try :#line:338
            O0000O0O0000O0000 =f'__{timi_new()}'#line:339
            O0OOO00O00O0O0O00 ={'authorization':OO0OOOO000OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0O0000O0000 ),'signstring':O0000O0O0000O0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:348
            O00000O0OOOO0O0OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OOO00O00O0O0O00 ).json ()#line:349
            if 'status'in O00000O0OOOO0O0OO :#line:351
                if O00000O0OOOO0O0OO ['status']==200 :#line:352
                    O00O0OO0OO0O00OOO =O00000O0OOOO0O0OO ['data'][0 ]['crops']#line:353
                    for O0000OO0O0OOO0OOO in O00O0OO0OO0O00OOO :#line:354
                        if O0000OO0O0OOO0OOO ['ill_clover_award']:#line:355
                            if float (O0000OO0O0OOO0OOO ['ill_clover_award'])>1 :#line:356
                                if O0000OO0O0OOO0OOO ['is_finish']:#line:357
                                    if not O0000OO0O0OOO0OOO ['is_getit']:#line:358
                                        if OO0OOOO000OO0OOO0 .certification ()!='未实名':#line:359
                                            O0000O0O0000O0000 =f'_award_level={O0000OO0O0OOO0OOO["level"]}_{timi_new()}'#line:360
                                            O0OOO00O00O0O0O00 ={'authorization':OO0OOOO000OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0O0000O0000 ),'signstring':O0000O0O0000O0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:369
                                            O000000O00O00O0O0 ={"award_level":O0000OO0O0OOO0OOO ['level']}#line:370
                                            O000O0OO000O0OO0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OOO00O00O0O0O00 ,json =O000000O00O00O0O0 ).json ()#line:372
                                            if 'status'in O000O0OO000O0OO0O :#line:373
                                                if O000O0OO000O0OO0O ['status']==200 :#line:374
                                                    OO00000OOO0O00000 =O000O0OO000O0OO0O ['data']['ill_clover_award']#line:375
                                                    print (f'【图鉴奖励】:领取{O0000OO0O0OOO0OOO["crop_name"]}成就丨奖励{OO00000OOO0O00000}叶子成功')#line:377
                                                if O000O0OO000O0OO0O ['status']==500 :#line:378
                                                    print (f'【图鉴奖励】:{O000O0OO000O0OO0O["message"]}')#line:379
        except Exception as O0O00OO0OO00O0000 :#line:380
            print (O0O00OO0OO00O0000 )#line:381
    def watched_ad (OOO000OO0000OOOOO ):#line:384
        try :#line:385
            OOOOO0O0OO0O0OOOO =f'__{timi_new()}'#line:386
            O00OOO00000OO00O0 ={'authorization':OOO000OO0000OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O0OO0O0OOOO ),'signstring':OOOOO0O0OO0O0OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:395
            O0OO000O00OO00O00 =requests .request ('get',f'{host}/game/getAllData',headers =O00OOO00000OO00O0 ).json ()#line:396
            if 'status'in O0OO000O00OO00O00 :#line:398
                if O0OO000O00OO00O00 ['status']==200 :#line:399
                    if 'offlineInfo'in O0OO000O00OO00O00 ['data']:#line:400
                        OO0O0000O0O0O00O0 =O0OO000O00OO00O00 ['data']['offlineInfo']['off_minute']#line:401
                        O00OOOOO0O00O0O00 =float (O0OO000O00OO00O00 ['data']['silver'])/1000000000000 #line:402
                        time .sleep (1 )#line:403
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00OOO00000OO00O0 ).json ()#line:404
                        time .sleep (2 )#line:405
                        OOO000O00OO0O00O0 =requests .request ('get',f'{host}/game/getAllData',headers =O00OOO00000OO00O0 ).json ()#line:406
                        if 'status'in OOO000O00OO0O00O0 :#line:408
                            if OOO000O00OO0O00O0 ['status']==200 :#line:409
                                OO0000OOO00O0O000 =float (OOO000O00OO0O00O0 ['data']['silver'])/1000000000000 #line:410
                                O0O000OOO0OO0OOO0 =str (OO0000OOO00O0O000 -O00OOOOO0O00O0O00 )[:6 ]#line:411
                                print (f'【离线奖励】:翻倍离线{OO0O0000O0O0O00O0}分钟奖励种子数量:{O0O000OOO0OO0OOO0}t粒')#line:412
        except Exception as O0O0OOO0OO00OO00O :#line:413
            print (O0O0OOO0OO00OO00O )#line:414
    def user_ad (OOOO0O000OO0O00O0 ):#line:417
        try :#line:418
            OO000O000OOOOO000 =f'__{timi_new()}'#line:419
            O0OOOO0O0OO0000OO ={'authorization':OOOO0O000OO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O000OOOOO000 ),'signstring':OO000O000OOOOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:428
            O00OOOO0OO0O0O000 =requests .request ('get',f'{host}/user/ad',headers =O0OOOO0O0OO0000OO ).json ()#line:429
            if 'status'in O00OOOO0OO0O0O000 :#line:431
                if O00OOOO0OO0O0O000 ['status']==200 :#line:432
                    O0OOOOO0O00OOO0O0 =O00OOOO0OO0O0O000 ['data']['max_time']#line:433
                    OOO00OO00000O0000 =O00OOOO0OO0O0O000 ['data']['watch_time']#line:434
                    O0OO00OO0O00O00O0 =O00OOOO0OO0O0O000 ['data']['added_time']#line:435
                    print (f'【获取种子】:获取种子剩余{O0OO00OO0O00O00O0 + O0OOOOO0O00OOO0O0 - OOO00OO00000O0000}次丨好友提供:{O0OO00OO0O00O00O0}次')#line:436
                    if O0OO00OO0O00O00O0 +O0OOOOO0O00OOO0O0 -OOO00OO00000O0000 >0 :#line:437
                        time .sleep (random .randint (16 ,19 ))#line:438
                        OOO00O00OOO00O000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OOOO0O0OO0000OO ).json ()#line:439
                        if 'status'in OOO00O00OOO00O000 :#line:441
                            if OOO00O00OOO00O000 ['status']==200 :#line:442
                                O000O0000O00OO00O =float (OOO00O00OOO00O000 ['data']['silver'])/1000000000000 #line:443
                                print (f'【获取种子】:获得种子:{int(O000O0000O00OO00O)}t粒')#line:444
                                return True #line:445
                            if OOO00O00OOO00O000 ['status']==500 :#line:446
                                O00OOO00O0O000OO0 =OOO00O00OOO00O000 ['message']#line:447
                                print (f'【获取种子】:{O00OOO00O0O000OO0}')#line:448
                                return False #line:449
        except Exception as O0O0000OO0O00OO0O :#line:450
            print (O0O0000OO0O00OO0O )#line:451
    def synthetic (O00000O000O0000O0 ):#line:454
        global id ,g #line:455
        try :#line:456
            O0000O00000OO00O0 =O00000O000O0000O0 .level_new ()#line:457
            OO0O000000OOO000O =random .randint (9 ,11 )#line:458
            OOO0000O0000O0000 =f'_site=8&targetSite={OO0O000000OOO000O}_{timi_new()}'#line:459
            O00000O0000OO0000 ={'accept':'application/json, text/plain, */*','authorization':O00000O000O0000O0 .token ,'timestamp':timi_new (),'sign':sign (OOO0000O0000O0000 ),'signstring':OOO0000O0000O0000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:474
            O0000OOO0OOO0OO00 ={"site":int (8 ),"targetSite":int (OO0O000000OOO000O )}#line:475
            requests .request ('post',f'{host}/game/crops/move',headers =O00000O0000OO0000 ,json =O0000OOO0OOO0OO00 )#line:476
            while True :#line:477
                O00OOO0OOOO0OOOOO =f'__{timi_new()}'#line:478
                O0OO0OO00000O0OOO ={'authorization':O00000O000O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OOOO0OOOOO ),'signstring':O00OOO0OOOO0OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:487
                OOOOO0O00OOOO0000 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0OO00000O0OOO ).json ()#line:488
                if 'status'in OOOOO0O00OOOO0000 :#line:490
                    if OOOOO0O00OOOO0000 ['status']==200 :#line:491
                        OOOO00OO0O0O00OOO =OOOOO0O00OOOO0000 ['data']['cropList']#line:492
                        O0O0000OOO000OO0O =OOOOO0O00OOOO0000 ['data']['gameCoreDataDBid']#line:493
                        OO0OO0O0OOOO0OO00 =0 #line:494
                        for O00OOO0OO00OO0OOO in OOOO00OO0O0O00OOO :#line:495
                            if not O00OOO0OO00OO0OOO :#line:496
                                O0O0OO0OOO00O00O0 =f'_crop_id={O0O0000OOO000OO0O}&site={OO0OO0O0OOOO0OO00}_{O00000O000O0000O0.time}'#line:497
                                OO00O0O0O00OOOO0O ={'authorization':O00000O000O0000O0 .token ,'timestamp':O00000O000O0000O0 .time ,'sign':sign (O0O0OO0OOO00O00O0 ),'signstring':O0O0OO0OOO00O00O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:506
                                O00O0O00OOO0O0OOO ={"site":OO0OO0O0OOOO0OO00 ,"crop_id":O0O0000OOO000OO0O }#line:507
                                OO00OOOOOO0000O0O =requests .request ('post',f'{host}/game/crops/buy',headers =OO00O0O0O00OOOO0O ,data =O00O0O00OOO0O0OOO ).json ()#line:508
                                time .sleep (random .randint (1 ,3 )/10 )#line:510
                                if 'status'in OO00OOOOOO0000O0O :#line:511
                                    if OO00OOOOOO0000O0O ['status']==200 :#line:512
                                        if OO00OOOOOO0000O0O ['message']=='种子数量不足':#line:513
                                            O0000O00000OO00O0 =O00000O000O0000O0 .level_new ()#line:514
                                            print (f'【种植合成】:{OO00OOOOOO0000O0O["message"]}')#line:515
                                            if not O00000O000O0000O0 .user_ad ():#line:516
                                                return False #line:517
                                    if OO00OOOOOO0000O0O ['status']==500 :#line:518
                                        print (f'【种植合成】:{OO00OOOOOO0000O0O["message"]}')#line:519
                                        return False #line:520
                            OO0OO0O0OOOO0OO00 +=1 #line:521
                        O00O000O0O00000OO =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0OO00000O0OOO ).json ()#line:522
                        O0OOO0O0OO000OO0O =O00O000O0O00000OO ['data']['cropList']#line:523
                        O0000O000O0O0O000 =False #line:524
                        for O00OOO0OO00OO0OOO in range (12 ):#line:525
                            id =O0OOO0O0OO000OO0O [O00OOO0OO00OO0OOO ]['level']#line:526
                            if float (O0000O00000OO00O0 )-float (id )>9 :#line:527
                                OO0OOO00OOO00OOO0 =f'_site={O00OOO0OO00OO0OOO}_{timi_new()}'#line:528
                                OOO0O00OOO0O0OOO0 ={'accept':'application/json, text/plain, */*','authorization':O00000O000O0000O0 .token ,'timestamp':timi_new (),'sign':sign (OO0OOO00OOO00OOO0 ),'signstring':OO0OOO00OOO00OOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:538
                                OO0OO00O00O0OOO0O ={"site":O00OOO0OO00OO0OOO }#line:539
                                OOOOOO00O0OO0O0O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO0O00OOO0O0OOO0 ,data =OO0OO00O00O0OOO0O ).json ()#line:541
                                if 'status'in OOOOOO00O0OO0O0O0 :#line:542
                                    if OOOOOO00O0OO0O0O0 ['status']==200 :#line:543
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:544
                            if id !=0 :#line:545
                                for O0OO0O00OOOOO000O in range (11 ):#line:546
                                    O0OO0OOO00O000OO0 =O0OO0O00OOOOO000O +1 #line:547
                                    g =O0OOO0O0OO000OO0O [O0OO0OOO00O000OO0 ]['level']#line:548
                                    if id ==g :#line:549
                                        OOO00000OO0O00O0O =O0OO0O00OOOOO000O +2 #line:550
                                        if OOO00000OO0O00O0O !=O00OOO0OO00OO0OOO +1 :#line:551
                                            OO0O00O00OOO0O000 =O00OOO0OO00OO0OOO +1 #line:552
                                            time .sleep (random .randint (1 ,3 )/10 )#line:554
                                            OOO0000O0000O0000 =f'_site={OO0O00O00OOO0O000 - 1}&targetSite={OOO00000OO0O00O0O - 1}_{timi_new()}'#line:555
                                            O00000O0000OO0000 ={'accept':'application/json, text/plain, */*','authorization':O00000O000O0000O0 .token ,'timestamp':timi_new (),'sign':sign (OOO0000O0000O0000 ),'signstring':OOO0000O0000O0000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:570
                                            O0O0OOOO00OO00OOO ={"site":int (OO0O00O00OOO0O000 -1 ),"targetSite":int (OOO00000OO0O00O0O -1 )}#line:571
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00000O0000OO0000 ,json =O0O0OOOO00OO00OOO )#line:572
                                            print (f'【种植合成】:位置{OO0O00O00OOO0O000}和位置{OOO00000OO0O00O0O}合出{int(id) + 1}级农作物')#line:573
                                            O0000O000O0O0O000 =True #line:574
                                    if O0000O000O0O0O000 :#line:575
                                        break #line:576
                                if O0000O000O0O0O000 :#line:577
                                    break #line:578
        except :#line:579
            O00000O000O0000O0 .synthetic ()#line:580
    def level_new (OOO000O0O000OOO00 ):#line:583
        try :#line:584
            O0O000O0OO0000O0O =f'__{timi_new()}'#line:585
            O0O000OOOO0OOOO00 ={'authorization':OOO000O0O000OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000O0OO0000O0O ),'signstring':O0O000O0OO0000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:594
            OOO0O00OO0OOO0OO0 =requests .request ('get',f'{host}/user',headers =O0O000OOOO0OOOO00 ).json ()#line:595
            if 'status'in OOO0O00OO0OOO0OO0 :#line:596
                if OOO0O00OO0OOO0OO0 ['status']==200 :#line:597
                    return float (OOO0O00OO0OOO0OO0 ['data']['level'])#line:598
        except Exception as O0OOO0OO00O0O00O0 :#line:599
            print (O0OOO0OO00O0O00O0 )#line:600
    def propsraffle (OO0O0000OO00OO000 ):#line:603
        try :#line:604
            while True :#line:605
                O000000O0OOO00O00 =f'__{timi_new()}'#line:606
                O0OO0000OOO00O000 ={'authorization':OO0O0000OO00OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O0OOO00O00 ),'signstring':O000000O0OOO00O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:615
                OOO00OOO00O0000O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OO0000OOO00O000 ).json ()#line:616
                if 'status'in OOO00OOO00O0000O0 :#line:618
                    if OOO00OOO00O0000O0 ['status']==200 :#line:619
                        O0OOO00000OOOO000 =OOO00OOO00O0000O0 ['data']['rows']#line:620
                        OOO0OO00OOOO000O0 =OOO00OOO00O0000O0 ['data']['vstate']#line:621
                        if O0OOO00000OOOO000 ==5 or O0OOO00000OOOO000 ==6 or O0OOO00000OOOO000 ==7 :#line:622
                            O00000O0O00000OO0 =OOO00OOO00O0000O0 ['data']['silver']#line:623
                            print (f'【转盘抽奖】:获得种子:{O00000O0O00000OO0}')#line:624
                        if O0OOO00000OOOO000 ==1 or O0OOO00000OOOO000 ==2 or O0OOO00000OOOO000 ==3 :#line:625
                            O0O0OOO000O0000OO =OOO00OOO00O0000O0 ['data']['clover']#line:626
                            print (f'【转盘抽奖】:获得三叶草:{O0O0OOO000O0000OO}')#line:627
                        if O0OOO00000OOOO000 ==4 or O0OOO00000OOOO000 ==8 :#line:628
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:629
                        if O0OOO00000OOOO000 =='抽奖次数已用完':#line:633
                            break #line:666
                time .sleep (random .randint (8 ,15 )/10 )#line:667
        except Exception as O000OO0OOOOOOOO00 :#line:668
            print (O000OO0OOOOOOOO00 )#line:669
    def friends_invitation (OO000OOOOO0OOO00O ):#line:672
        try :#line:673
            O0O0OOOO0OO0O00OO =f'__{timi_new()}'#line:674
            O0O0OOOOOO0O0OOO0 ={'authorization':OO000OOOOO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOO0OO0O00OO ),'signstring':O0O0OOOO0OO0O00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:683
            OOOOO00000O00O0OO =requests .request ('get',f'{host}/friends',headers =O0O0OOOOOO0O0OOO0 ).json ()#line:684
            if 'status'in OOOOO00000O00O0OO :#line:685
                if OOOOO00000O00O0OO ['status']==200 :#line:686
                    O000OOO0OO000O0OO =OOOOO00000O00O0OO ['data']['myInviteter']#line:687
                    if O000OOO0OO000O0OO :#line:688
                        OO0O0OOO00OOO0O00 =O000OOO0OO000O0OO ['user']['nickname']#line:689
                        OOO000OOOOOO000O0 =OO000OOOOO0OOO00O .certification ()#line:690
                        print (f'【查邀请人】:我的邀请人:{OO0O0OOO00OOO0O00}丨实名:{OOO000OOOOOO000O0}')#line:691
                    else :#line:692
                        if OO000OOOOO0OOO00O .innerId !='0':#line:693
                            OO000OOOOO0OOO00O .invitation ()#line:694
        except Exception as O0O0OOOOO0OOOOO00 :#line:695
            print (O0O0OOOOO0OOOOO00 )#line:696
    def add_clover (OOO0O00OOOOO0OO0O ):#line:699
        global golden_seed #line:700
        try :#line:701
            O0O00OOO0O00000OO =f'__{timi_new()}'#line:702
            OO00O00OO00OOOOOO ={'authorization':OOO0O00OOOOO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO0O00000OO ),'signstring':O0O00OOO0O00000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:711
            OOO0O0O00O00000O0 =requests .request ('get',f'{host}/assets/clovers',headers =OO00O00OO00OOOOOO ).json ()#line:712
            if 'status'in OOO0O0O00O00000O0 :#line:714
                if OOO0O0O00O00000O0 ['status']==200 :#line:715
                    O0000O000OOOO0O0O =OOO0O0O00O00000O0 ['data']['clover']#line:716
                    O00OOO0OOOO000000 =OOO0O0O00O00000O0 ['data']['used_clover']#line:717
                    O00OOO0O0OOO0O00O =float (O0000O000OOOO0O0O )-float (O00OOO0OOOO000000 )#line:718
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O00OOO0OOOO000000}')#line:719
                    if OOO0O00OOOOO0OO0O .certification ()!='未实名':#line:720
                        if O00OOO0O0OOO0O00O >1 :#line:721
                            O0O00OOO0O00000OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00OOO0O0OOO0O00O)}_{timi_new()}'#line:722
                            OO0OO0O00O00OOOOO ={'authorization':OOO0O00OOOOO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO0O00000OO ),'signstring':O0O00OOO0O00000OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:731
                            O0OOOOOOO00OOO0OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00OOO0O0OOO0O00O )}#line:732
                            OOO000OOO000O00O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0OO0O00O00OOOOO ,data =O0OOOOOOO00OOO0OO ).json ()#line:733
                            if 'status'in OOO000OOO000O00O0 :#line:735
                                if OOO000OOO000O00O0 ['status']==200 :#line:736
                                    print (f'【参与抽奖】:添加三叶草:{OOO000OOO000O00O0["data"]}丨数量:{O00OOO0O0OOO0O00O}')#line:737
                                if OOO000OOO000O00O0 ['status']==500 :#line:738
                                    print (f'【参与抽奖】:添加三叶草:{OOO000OOO000O00O0["message"]}')#line:739
            O00000O0O00O000O0 =requests .request ('get',f'{host}/lottery',headers =OO00O00OO00OOOOOO ).json ()#line:740
            O00OO0O00OO000O0O =OOO0O00OOOOO0OO0O .winning_rewards ()#line:742
            if 'status'in O00000O0O00O000O0 :#line:743
                if O00000O0O00O000O0 ['status']==200 :#line:744
                    O00O00O000O0OOOO0 =O00000O0O00O000O0 ['data'][0 ]['day_get_gold_quantity']#line:745
                    golden_seed +=float (O00O00O000O0OOOO0 )#line:746
                    print (f'【参与抽奖】:预计每天中{str(O00O00O000O0OOOO0)[:6]}颗金种子丨好友收益:{str(O00OO0O00OO000O0O)[:6]}')#line:747
        except Exception as O0O00O000000O00OO :#line:748
            print (O0O00O000000O00OO )#line:749
    def energy (OO00000OOO0000O00 ):#line:753
        try :#line:754
            while True :#line:755
                O000O0O00O00O0OOO =f'__{timi_new()}'#line:756
                OO0O0OO000OOO00O0 ={'authorization':OO00000OOO0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O00O00O0OOO ),'signstring':O000O0O00O00O0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:765
                O0000O0000OOO00OO =requests .request ('get',f'{host}/energy/general',headers =OO0O0OO000OOO00O0 ).json ()#line:766
                if 'status'in O0000O0000OOO00OO :#line:768
                    if O0000O0000OOO00OO ['status']==200 :#line:769
                        O0OO0OO0OO0OOOOO0 =O0000O0000OOO00OO ['data']['ordinary_water']#line:770
                        O0O0000O0OOO0O00O =O0000O0000OOO00OO ['data']['ordinary_fertilizer']#line:771
                        print (f'【我的营养】:肥料:{str(O0O0000O0OOO0O00O).split(".")[0]}丨水滴:{str(O0OO0OO0OO0OOOOO0).split(".")[0]}')#line:773
                        if float (O0O0000O0OOO0O00O )<96 :#line:774
                            time .sleep (random .randint (160 ,180 )/10 )#line:775
                            O0OO0000OO0O0O0OO =99 -float (O0O0000O0OOO0O00O )#line:776
                            OO0O00OOO0O00O0O0 ={"fertilizer":str (O0OO0000OO0O0O0OO ).split ('.')[0 ]}#line:777
                            OOOO0O0O0OOO0O000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0O0OO000OOO00O0 ).json ()#line:778
                            if 'status'in OOOO0O0O0OOO0O000 :#line:780
                                if OOOO0O0O0OOO0O000 ['status']==200 :#line:781
                                    print (f'【购买肥料】:看广告获取肥料:{OOOO0O0O0OOO0O000["message"]}')#line:782
                        if float (O0OO0OO0OO0OOOOO0 )<880 :#line:783
                            time .sleep (random .randint (160 ,180 )/10 )#line:784
                            O0OOOO00OOO0OO00O =999 -float (O0OO0OO0OO0OOOOO0 )#line:785
                            OOO000O0O0OOO000O ={"water":str (O0OOOO00OOO0OO00O ).split ('.')[0 ]}#line:786
                            OOOOO00OO0O00000O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0O0OO000OOO00O0 ).json ()#line:787
                            if 'status'in OOOOO00OO0O00000O :#line:789
                                if OOOOO00OO0O00000O ['status']==200 :#line:790
                                    print (f'【购买水滴】:看广告获取水滴:{OOOOO00OO0O00000O["message"]}')#line:791
                        if float (O0O0000O0OOO0O00O )>96 and float (O0OO0OO0OO0OOOOO0 )>880 :#line:792
                            break #line:793
        except Exception as O00000OO0OOO0O0O0 :#line:795
            print (O00000OO0OOO0O0O0 )#line:796
def bundled_def ():#line:798
    O00OO0O000O000O0O =['5570536','7750212','7911652','7911680','7805624']#line:799
    return O00OO0O000O000O0O [random .randint (0 ,len (O00OO0O000O000O0O )-1 )]#line:800
def version_of_the_validation ():#line:804
    return str ((77 -56 )/10 )#line:805
def gitee_validation ():#line:808
    try :#line:809
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:810
    except :#line:811
        sys .exit (0 )#line:812
def update_the_validation ():#line:816
    try :#line:817
        O0O00000OOOO00O00 =gitee_validation ()#line:818
        if version_of_the_validation ()<O0O00000OOOO00O00 ['CityEarth']['edition']:#line:819
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O00000OOOO00O00["CityEarth"]["edition"]}   ❌')#line:820
            print (f'更新内容=>>{O0O00000OOOO00O00["CityEarth"]["content"]}   👍')#line:821
        else :#line:822
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O00000OOOO00O00["CityEarth"]["edition"]}   ✅')#line:823
            print (f'更新内容=>> {O0O00000OOOO00O00["CityEarth"]["content"]}   👍')#line:824
    except Exception as OOO0000OOO00OOO0O :#line:825
        print (OOO0000OOO00OOO0O )#line:826
def os_qinglong ():#line:829
    if application in os .environ :#line:830
        OOO0OOO0O0000O0O0 =os .environ [application ].split ('\n')#line:831
        if len (OOO0OOO0O0000O0O0 )>0 :#line:832
            return OOO0OOO0O0000O0O0 #line:833
        else :#line:834
            print (f"{application}变量未启用")#line:835
            print ('脚本退出')#line:836
            sys .exit (1 )#line:837
    else :#line:838
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:840
        return os_built ()#line:841
def os_built ():#line:844
    if token :#line:845
        OOO0OOO000OOOO00O =token .split ('\n')#line:846
        if len (OOO0OOO000OOOO00O )>0 :#line:847
            return OOO0OOO000OOOO00O #line:848
    else :#line:849
        print (f"内置变量为空")#line:850
        print ('脚本结束')#line:851
        sys .exit (0 )#line:852
if __name__ =='__main__':#line:855
    start ()#line:856
