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
@ 版本  2.6
"""
application = 'ce_token'  # 变量名
token = ''

##################################配置区##################################
energy = False              # True 为用金种子添加肥料    False 为不添加肥料和水滴
token_zs = ''               # 设置有金种子的号给没金种子的号赠送区购买金种子 这里请填有金种子多的账号数据
zh_mony = '5'               # 每次小号金种子不足转赠数量
fertilizer_quantity = 40    # 低于肥料数量就用金种子购买肥料， 每次10
wadverti_quantity = 500     # 低于水滴数量就用金种子购买水滴， 每次100
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
        O0OO00OO00O0000O0 =os_qinglong ()#line:10
        print (f"==========共找到{len(O0OO00OO00O0000O0)}个账号==========")#line:11
        for OO00OO00O00OOOO00 in O0OO00OO00O0000O0 :#line:12
            OO00OO0OO00000OOO =[]#line:13
            print (f"------------正在执行第{O0OO00OO00O0000O0.index(OO00OO00O00OOOO00) + 1}个账号------------")#line:14
            OOO0O0000000O0OO0 =CityEarth (OO00OO00O00OOOO00 ,OO00OO0OO00000OOO )#line:15
            def O00000OO000OOO00O ():#line:17
                if OOO0O0000000O0OO0 .base_info ():#line:19
                    OOO0O0000000O0OO0 .sealing ()#line:21
                    OOO0O0000000O0OO0 .invitenum ()#line:23
                    OOO0O0000000O0OO0 .game_map ()#line:25
                    OOO0O0000000O0OO0 .friends_invitation ()#line:27
                    OOO0O0000000O0OO0 .energy ()#line:29
                    OOO0O0000000O0OO0 .add_clover ()#line:31
                    OOO0O0000000O0OO0 .propsraffle ()#line:33
                    OOO0O0000000O0OO0 .synthetic ()#line:35
                    OOO0O0000000O0OO0 .crops_illustrated ()#line:37
                    OOO0O0000000O0OO0 .give_gold ()#line:39
                    OOO0O0000000O0OO0 .withdraw ()#line:41
            OOO0O0OOOO0O000OO =threading .Thread (target =O00000OO000OOO00O )#line:43
            OOO0O0OOOO0O000OO .start ()#line:44
            time .sleep (time_xx )#line:45
        print (f"------------正在处理推送通知------------")#line:46
        time .sleep (0.5 )#line:47
        O0OO00OO0OOOOO0OO =format_msg ()#line:48
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0OO00OO0OOOOO0OO +' ')#line:49
    except Exception as O0O0OOO0OOOOOOO00 :#line:50
        print (O0O0OOO0OOOOOOO00 )#line:51
def give_gold (OOOOOOOO0000OO0OO ):#line:54
        try :#line:55
            O0O000OOOOOO00OOO =zh_mony #line:56
            O00OOO0O0O0OO0000 =f'_doneeNo={OOOOOOOO0000OO0OO}&quantity={O0O000OOOOOO00OOO}_{timi_new()}'#line:57
            O0OO00OOOOO00OOOO ={'source':'scsc','authorization':token_zs .split ('&')[0 ],'timestamp':str (timi_new ()),'sign':sign (O00OOO0O0O0OO0000 ),'signstring':O00OOO0O0O0OO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:67
            O00O00OOOOO0OO000 ={"quantity":O0O000OOOOOO00OOO ,"doneeNo":OOOOOOOO0000OO0OO }#line:71
            O0O0OO00O000O000O =requests .request ('post',f'{host}/finance/give-gold',headers =O0OO00OOOOO00OOOO ,data =O00O00OOOOO0OO000 ).json ()#line:72
            if 'status'in O0O0OO00O000O000O :#line:74
                if O0O0OO00O000O000O ['status']==200 :#line:75
                    if O0O0OO00O000O000O ['data']:#line:76
                        print (f'【赠送种子】:赠送{O0O000OOOOOO00OOO}种子给{OOOOOOOO0000OO0OO}成功')#line:77
                if O0O0OO00O000O000O ['status']==401 :#line:78
                    print (f'【赠送种子】:{O0O0OO00O000O000O["message"]}')#line:79
                if O0O0OO00O000O000O ['status']==500 :#line:80
                    print (f'【赠送种子】:{O0O0OO00O000O000O["message"]}')#line:81
        except Exception as OOO0OO0OOOOO0O00O :#line:82
            print (OOO0OO0OOOOO0O00O )#line:83
def sign (OO00OO00O0O0OOO00 ):#line:86
    O0OOO0O0OO000OO0O =hashlib .md5 (OO00OO00O0O0OOO00 .encode ()).hexdigest ()#line:87
    OO0OO00OOOOO0O0OO ="scsc%^&*"+O0OOO0O0OO000OO0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:88
    O000OOO0OO0OO0OO0 =hashlib .md5 (OO0OO00OOOOO0O0OO .encode ()).hexdigest ()#line:89
    return O000OOO0OO0OO0OO0 #line:90
def format_msg ():#line:92
    O0O00OO00O00O000O =""#line:93
    for O0O000O0000O00O0O in msg_list :#line:94
        O0O00OO00O00O000O +=str (O0O000O0000O00O0O )+"\r\n"#line:95
    return O0O00OO00O00O000O #line:96
def timi_new ():#line:98
    return str (int (time .time ()*1000 ))#line:99
class CityEarth :#line:102
    def __init__ (O0000O0O0O000OOO0 ,OO0O0OOOO0OO0000O ,OO0O00OOO000OO00O ):#line:104
        try :#line:105
            O0000O0O0O000OOO0 .msg =OO0O00OOO000OO00O #line:106
            O0000O0O0O000OOO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:107
            O0000O0O0O000OOO0 .token =OO0O0OOOO0OO0000O .split ('&')[0 ]#line:108
            O0000O0O0O000OOO0 .innerId =OO0O0OOOO0OO0000O .split ('&')[1 ]#line:109
            O0000O0O0O000OOO0 .doneeNo =OO0O0OOOO0OO0000O .split ('&')[2 ]#line:110
        except :#line:111
            print ('变量格式错误')#line:112
    def base_info (O0O0O00OOOOO0OO0O ):#line:115
        try :#line:116
            O0O0O00OOOOO0OO0O .watched_ad ()#line:118
            OO0OOOO0000O00OOO =f'__{timi_new()}'#line:119
            O000OO0O0OO0OOOOO ={'source':'scsc','authorization':O0O0O00OOOOO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0000O00OOO ),'signstring':OO0OOOO0000O00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:129
            O0OOO00O00OO0OOOO =requests .request ('get',f'{host}/user',headers =O000OO0O0OO0OOOOO ).json ()#line:130
            if 'status'in O0OOO00O00OO0OOOO :#line:132
                if O0OOO00O00OO0OOOO ['status']==200 :#line:133
                    OO00O0000OO00OOO0 =O0OOO00O00OO0OOOO ['data']['nickname']#line:134
                    O00O0OO0O000OOO00 =O0OOO00O00OO0OOOO ['data']['inner_id']#line:135
                    OOOOO00OO0O00O000 =O0OOO00O00OO0OOOO ['data']['assets']['gold']#line:136
                    OOOOOOO00O000O0OO =O0OOO00O00OO0OOOO ['data']['level']#line:137
                    print (f'【账号信息】:昵称:{OO00O0000OO00OOO0[:5]}丨ID:{O00O0OO0O000OOO00}丨等级:{OOOOOOO00O000O0OO}丨金种子:{str(OOOOO00OO0O00O000).split(".")[0]}')#line:138
                if O0OOO00O00OO0OOOO ['status']==401 :#line:139
                    print (O0OOO00O00OO0OOOO ['message'])#line:140
                    O0O0O00OOOOO0OO0O .msg .append ('有账号失效了')#line:141
                    return False #line:142
                if O0OOO00O00OO0OOOO ['status']==500 :#line:143
                    return False #line:144
            return True #line:145
        except Exception as OOOO00OO00O0OO0OO :#line:146
            print (OOOO00OO00O0OO0OO )#line:147
    def sealing (OOO0O0OOOOOOOOOOO ):#line:150
        try :#line:151
            OOOOOO0OO0OO000O0 =f'__{timi_new()}'#line:152
            OO0O0OOOOOO0OO0O0 ={'source':'scsc','authorization':OOO0O0OOOOOOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OO0OO000O0 ),'signstring':OOOOOO0OO0OO000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:162
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0O0OOOOOO0OO0O0 )#line:163
            requests .request ('get',f'{host}/packsack/list',headers =OO0O0OOOOOO0OO0O0 )#line:164
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0O0OOOOOO0OO0O0 )#line:165
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0O0OOOOOO0OO0O0 )#line:166
            requests .request ('get',f'{host}/user',headers =OO0O0OOOOOO0OO0O0 )#line:167
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0O0OOOOOO0OO0O0 )#line:168
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0O0OOOOOO0OO0O0 )#line:169
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0O0OOOOOO0OO0O0 )#line:170
            requests .request ('get',f'{host}/game/getAllData',headers =OO0O0OOOOOO0OO0O0 )#line:171
            requests .request ('get',f'{host}/assets',headers =OO0O0OOOOOO0OO0O0 )#line:172
        except Exception as O000O00O00O0OOO0O :#line:173
            print (O000O00O00O0OOO0O )#line:174
    def withdraw (OO0O0OOOOOOOOO0OO ):#line:178
        OO0OO0OOOOO00OOOO =f'__{timi_new()}'#line:179
        OOO0000O000O00OOO ={'source':'scsc','authorization':OO0O0OOOOOOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OOOOO00OOOO ),'signstring':OO0OO0OOOOO00OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:189
        OO0000000O000O0OO =requests .request ('get',f'{host}/assets',headers =OOO0000O000O00OOO ).json ()#line:190
        if 'status'in OO0000000O000O0OO :#line:192
            if OO0000000O000O0OO ['status']==200 :#line:193
                OOOO0OO000O0O000O =OO0000000O000O0OO ['data']['cash']#line:194
                if float (OOOO0OO000O0O000O )>20 :#line:195
                    OO0OO0OOOOO00OOOO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:196
                    OOO0000O000O00OOO ={'authorization':OO0O0OOOOOOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OOOOO00OOOO ),'signstring':OO0OO0OOOOO00OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:205
                    OO0OOO000OOOOOOOO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:206
                    O0OOO000O0000OOO0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOO0000O000O00OOO ,data =OO0OOO000OOOOOOOO ).json ()#line:208
                    print (O0OOO000O0000OOO0 )#line:209
    def invitenum (OO0OOOO0OO0O0OO00 ):#line:212
        O0000O00OO0O0OO00 =f'__{timi_new()}'#line:213
        O00OO0000OOO0O000 ={'source':'scsc','authorization':OO0OOOO0OO0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00OO0O0OO00 ),'signstring':O0000O00OO0O0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:223
        OOO0OOOO000OO000O =requests .request ('get',f'{host}/invite/invitenum',headers =O00OO0000OOO0O000 ).json ()#line:224
        if 'status'in OOO0OOOO000OO000O :#line:226
            if OOO0OOOO000OO000O ['status']==200 :#line:227
                OO0000OOO00OOOOO0 =OOO0OOOO000OO000O ['data']['invited_count']#line:228
                O000OO0000OOOO0O0 =OOO0OOOO000OO000O ['data']['invited_second_count']#line:229
                print (f'【我的邀请】:直邀好友:{OO0000OOO00OOOOO0}丨间邀好友:{O000OO0000OOOO0O0}')#line:230
    def game_map (O00O00O0O000000OO ):#line:233
        try :#line:234
            OO00O00OO0O0O000O =f'__{timi_new()}'#line:235
            OOOOOO0OOOO0O00O0 ={'source':'scsc','authorization':O00O00O0O000000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO0O0O000O ),'signstring':OO00O00OO0O0O000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            OO00OO00O0OOO0O0O =requests .request ('get',f'{host}/game/map',headers =OOOOOO0OOOO0O00O0 ).json ()#line:246
            if 'status'in OO00OO00O0OOO0O0O :#line:248
                if OO00OO00O0OOO0O0O ['status']==200 :#line:249
                    for OOO00O0O000000000 in OO00OO00O0OOO0O0O ['data']['list'][0 ]['crops']:#line:250
                        OO0O0O000O0OO0000 =OOO00O0O000000000 ['level']#line:252
                        if OO0O0O000O0OO0000 ==41 :#line:253
                            OOO0O0O0O0OO0O000 =OOO00O0O000000000 ['crop_name']#line:254
                            OO00000OO000OOO0O =OOO00O0O000000000 ['count']#line:255
                            if OO00000OO000OOO0O >0 :#line:256
                                print (f'【农业资产】:{OOO0O0O0O0OO0O000}丨数量:{OO00000OO000OOO0O}')#line:257
        except Exception as O000O0O0O000000O0 :#line:258
            print (O000O0O0O000000O0 )#line:259
    def give_gold (OO000OO0O00O000OO ):#line:262
        try :#line:263
            OOOO00O0OO0OO00OO =f'__{timi_new()}'#line:264
            OOO00OOOOOOO00O0O ={'source':'scsc','authorization':OO000OO0O00O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0OO0OO00OO ),'signstring':OOOO00O0OO0OO00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:274
            O0O0000O000O0O000 =requests .request ('get',f'{host}/user',headers =OOO00OOOOOOO00O0O ).json ()#line:275
            if 'status'in O0O0000O000O0O000 :#line:276
                if O0O0000O000O0O000 ['status']==200 :#line:277
                    if float (OO000OO0O00O000OO .doneeNo )!=0 :#line:278
                        O0OO0OO0O0000O000 =O0O0000O000O0O000 ['data']['assets']['gold']#line:279
                        if float (O0OO0OO0O0000O000 )>float (OO000OO0O00O000OO .innerId ):#line:280
                            O0O00O0000000OO0O =int (float (O0OO0OO0O0000O000 )/1.1 )#line:281
                            OOOO00O0OO0OO00OO =f'_doneeNo={OO000OO0O00O000OO.doneeNo}&quantity={O0O00O0000000OO0O}_{timi_new()}'#line:282
                            OOO00OOOOOOO00O0O ={'source':'scsc','authorization':OO000OO0O00O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0OO0OO00OO ),'signstring':OOOO00O0OO0OO00OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:292
                            OO0OOOOOO000O0O0O ={"quantity":O0O00O0000000OO0O ,"doneeNo":OO000OO0O00O000OO .doneeNo }#line:296
                            O0OOOO0OO0OO0OO0O =requests .request ('post',f'{host}/finance/give-gold',headers =OOO00OOOOOOO00O0O ,data =OO0OOOOOO000O0O0O ).json ()#line:297
                            if 'status'in O0OOOO0OO0OO0OO0O :#line:299
                                if O0OOOO0OO0OO0OO0O ['status']==200 :#line:300
                                    if O0OOOO0OO0OO0OO0O ['data']:#line:301
                                        print (f'【赠送种子】:赠送{O0O00O0000000OO0O}种子给{OO000OO0O00O000OO.doneeNo}成功')#line:302
                    else :#line:303
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:304
        except Exception as O0000O0OOO00OOO0O :#line:305
            print (O0000O0OOO00OOO0O )#line:306
    def invitation (O00O00OO0OOO0O000 ):#line:308
        try :#line:309
            _OO0OOOOO0000O0O0O =float (bundled_def ())/4 #line:310
            O0O00OOO00OOOO00O =f'_innerId={int(_OO0OOOOO0000O0O0O)}_{timi_new()}'#line:311
            O000OOO0O0O000OO0 ={'source':'scsc','authorization':O00O00OO0OOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO00OOOO00O ),'signstring':O0O00OOO00OOOO00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:321
            OO0OOO000OO0OO0OO ={"innerId":int (_OO0OOOOO0000O0O0O )}#line:322
            requests .request ('post',f'{host}/friends/my-invitation',headers =O000OOO0O0O000OO0 ,data =OO0OOO000OO0OO0OO )#line:323
        except Exception as OOOO000O00O0OO000 :#line:324
            print (OOOO000O00O0OO000 )#line:325
    def winning_rewards (O0O0OO0OOOOOO0000 ):#line:328
        try :#line:329
            OO0OO0OOO0OO0O00O =f'__{timi_new()}'#line:330
            O000O00OO00OO000O ={'source':'scsc','authorization':O0O0OO0OOOOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OOO0OO0O00O ),'signstring':OO0OO0OOO0OO0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:340
            O0O0OO00OOO000OOO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O000O00OO00OO000O ).json ()#line:341
            if 'status'in O0O0OO00OOO000OOO :#line:343
                if O0O0OO00OOO000OOO ['status']==200 :#line:344
                    if O0O0OO00OOO000OOO ['data']['amount']:#line:345
                        OO00O0O0OOO0OOOO0 =O0O0OO00OOO000OOO ['data']['amount']['gold']#line:346
                        return OO00O0O0OOO0OOOO0 #line:347
                    else :#line:348
                        return 0 #line:349
        except Exception as O0O0OO0O0OOO00O0O :#line:350
            print (O0O0OO0O0OOO00O0O )#line:351
    def certification (OO0000OO000OO0O00 ):#line:354
        try :#line:355
            OO000O00O00O0O0OO =f'__{timi_new()}'#line:356
            OO0O0OO00O00OO0O0 ={'source':'scsc','authorization':OO0000OO000OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00O00O0O0OO ),'signstring':OO000O00O00O0O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:366
            OO0OO0O00O000000O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0O0OO00O00OO0O0 ).json ()#line:367
            if 'status'in OO0OO0O00O000000O :#line:369
                if OO0OO0O00O000000O ['status']==200 :#line:370
                    if OO0OO0O00O000000O ['data']['result']:#line:371
                        OOO00O0O0OO0O00O0 =OO0OO0O00O000000O ['data']['nick_name']#line:372
                        return OOO00O0O0OO0O00O0 #line:373
                    else :#line:374
                        return '未实名'#line:375
        except Exception as O00OOO000O0OO0O0O :#line:376
            print (O00OOO000O0OO0O0O )#line:377
    def crops_illustrated (OO00OOO0OO0O0OOO0 ):#line:380
        try :#line:381
            O00O0O0O0OOO000O0 =f'__{timi_new()}'#line:382
            OO00O0O0OOOO00O00 ={'source':'scsc','authorization':OO00OOO0OO0O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O0OOO000O0 ),'signstring':O00O0O0O0OOO000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:392
            OO00O0OO00OOOO00O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO00O0O0OOOO00O00 ).json ()#line:393
            if 'status'in OO00O0OO00OOOO00O :#line:395
                if OO00O0OO00OOOO00O ['status']==200 :#line:396
                    O00OO000O000OOOOO =OO00O0OO00OOOO00O ['data'][0 ]['crops']#line:397
                    for O000OOO0000OOOO0O in O00OO000O000OOOOO :#line:398
                        if O000OOO0000OOOO0O ['ill_clover_award']:#line:399
                            if float (O000OOO0000OOOO0O ['ill_clover_award'])>1 :#line:400
                                if O000OOO0000OOOO0O ['is_finish']:#line:401
                                    if not O000OOO0000OOOO0O ['is_getit']:#line:402
                                        if OO00OOO0OO0O0OOO0 .certification ()!='未实名':#line:403
                                            O00O0O0O0OOO000O0 =f'_award_level={O000OOO0000OOOO0O["level"]}_{timi_new()}'#line:404
                                            OO00O0O0OOOO00O00 ={'source':'scsc','authorization':OO00OOO0OO0O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O0OOO000O0 ),'signstring':O00O0O0O0OOO000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:414
                                            O00O0O0OOO0O0O0OO ={"award_level":O000OOO0000OOOO0O ['level']}#line:415
                                            OO00O0OOOOO00O00O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO00O0O0OOOO00O00 ,json =O00O0O0OOO0O0O0OO ).json ()#line:417
                                            if 'status'in OO00O0OOOOO00O00O :#line:418
                                                if OO00O0OOOOO00O00O ['status']==200 :#line:419
                                                    O000OOOOOOO0OO0O0 =OO00O0OOOOO00O00O ['data']['ill_clover_award']#line:420
                                                    print (f'【图鉴奖励】:领取{O000OOO0000OOOO0O["crop_name"]}成就丨奖励{O000OOOOOOO0OO0O0}☘️')#line:422
                                                if OO00O0OOOOO00O00O ['status']==500 :#line:423
                                                    print (f'【图鉴奖励】:{OO00O0OOOOO00O00O["message"]}')#line:424
        except Exception as OOO0O0O000O0O0OOO :#line:425
            print (OOO0O0O000O0O0OOO )#line:426
    def watched_ad (OO0O0O0OO0O0O000O ):#line:429
        try :#line:430
            O000OO000OO0OO000 =f'__{timi_new()}'#line:431
            OOO000O0000000O0O ={'source':'scsc','authorization':OO0O0O0OO0O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO000OO0OO000 ),'signstring':O000OO000OO0OO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:441
            OOO0O000OOO0OO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO000O0000000O0O ).json ()#line:442
            if 'status'in OOO0O000OOO0OO0O0 :#line:444
                if OOO0O000OOO0OO0O0 ['status']==200 :#line:445
                    if 'offlineInfo'in OOO0O000OOO0OO0O0 ['data']:#line:446
                        time .sleep (random .randint (3 ,5 ))#line:447
                        OO0O000000O0OO000 =OOO0O000OOO0OO0O0 ['data']['offlineInfo']['off_minute']#line:448
                        OOO0O00OOOO0OOOOO =float (OOO0O000OOO0OO0O0 ['data']['silver'])/1000000000000 #line:449
                        time .sleep (1 )#line:450
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO000O0000000O0O ).json ()#line:451
                        time .sleep (2 )#line:452
                        O0OO00O0OO000000O =requests .request ('get',f'{host}/game/getAllData',headers =OOO000O0000000O0O ).json ()#line:453
                        if 'status'in O0OO00O0OO000000O :#line:455
                            if O0OO00O0OO000000O ['status']==200 :#line:456
                                OOOOOO000000OO00O =float (O0OO00O0OO000000O ['data']['silver'])/1000000000000 #line:457
                                O000O0OO00OO0O0O0 =str (OOOOOO000000OO00O -OOO0O00OOOO0OOOOO )[:6 ]#line:458
                                print (f'【离线奖励】:翻倍离线{OO0O000000O0OO000}分钟奖励🌱数量:{O000O0OO00OO0O0O0}t粒')#line:459
        except Exception as O0O0O0000O000000O :#line:460
            print (O0O0O0000O000000O )#line:461
    def user_ad (O0OO0OO0000O000OO ):#line:464
        try :#line:465
            OOOO00O0000000O0O =f'__{timi_new()}'#line:466
            OOOO00OO00O00O0O0 ={'source':'scsc','authorization':O0OO0OO0000O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0000000O0O ),'signstring':OOOO00O0000000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:476
            OO0OOO0O00O0O000O =requests .request ('get',f'{host}/user/ad',headers =OOOO00OO00O00O0O0 ).json ()#line:477
            if 'status'in OO0OOO0O00O0O000O :#line:479
                if OO0OOO0O00O0O000O ['status']==200 :#line:480
                    OO0O0O0O0O00OO0O0 =OO0OOO0O00O0O000O ['data']['max_time']#line:481
                    OOO000O00O0000OO0 =OO0OOO0O00O0O000O ['data']['watch_time']#line:482
                    OOO00OOOO00OO0O0O =OO0OOO0O00O0O000O ['data']['added_time']#line:483
                    print (f'【获取种子】:获取🌱剩余{OOO00OOOO00OO0O0O + OO0O0O0O0O00OO0O0 - OOO000O00O0000OO0}次丨好友提供:{OOO00OOOO00OO0O0O}次')#line:484
                    if OOO00OOOO00OO0O0O +OO0O0O0O0O00OO0O0 -OOO000O00O0000OO0 >0 :#line:485
                        time .sleep (random .randint (16 ,19 ))#line:486
                        OOO0OOO000OOO00O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOOO00OO00O00O0O0 ).json ()#line:487
                        if 'status'in OOO0OOO000OOO00O0 :#line:489
                            if OOO0OOO000OOO00O0 ['status']==200 :#line:490
                                O00OOOO0OOOO0OOOO =float (OOO0OOO000OOO00O0 ['data']['silver'])/1000000000000 #line:491
                                print (f'【获取种子】:获得🌱:{int(O00OOOO0OOOO0OOOO)}t粒')#line:492
                                return True #line:493
                            if OOO0OOO000OOO00O0 ['status']==500 :#line:494
                                OO0000O0O00O0OO0O =OOO0OOO000OOO00O0 ['message']#line:495
                                print (f'【获取种子】:{OO0000O0O00O0OO0O}')#line:496
                                return False #line:497
        except Exception as OOOO0OOOO00O0OOO0 :#line:498
            print (OOOO0OOOO00O0OOO0 )#line:499
    def synthetic (O000O0OOO000O0OOO ):#line:502
        global id ,g #line:503
        try :#line:504
            OO0000000O0O00000 =O000O0OOO000O0OOO .level_new ()#line:505
            O0O0O0OO00O0O0O00 =random .randint (9 ,11 )#line:506
            O0000OOOOO0000OOO =f'_site=8&targetSite={O0O0O0OO00O0O0O00}_{timi_new()}'#line:507
            OO0O000OO000O0O00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000O0OOO000O0OOO .token ,'timestamp':timi_new (),'sign':sign (O0000OOOOO0000OOO ),'signstring':O0000OOOOO0000OOO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:523
            O00OO0OOOOOOOOOOO ={"site":int (8 ),"targetSite":int (O0O0O0OO00O0O0O00 )}#line:524
            requests .request ('post',f'{host}/game/crops/move',headers =OO0O000OO000O0O00 ,json =O00OO0OOOOOOOOOOO )#line:525
            while True :#line:526
                O0OOOO0OO00O0O0OO =f'__{timi_new()}'#line:527
                OOO0OO0OO00OOOO0O ={'source':'scsc','authorization':O000O0OOO000O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OO00O0O0OO ),'signstring':O0OOOO0OO00O0O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:537
                OO0O00OOO0OOO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OO0OO00OOOO0O ).json ()#line:538
                if 'status'in OO0O00OOO0OOO0O0O :#line:540
                    if OO0O00OOO0OOO0O0O ['status']==200 :#line:541
                        OO0000O0OOOOOO000 =OO0O00OOO0OOO0O0O ['data']['cropList']#line:542
                        OOO0OOOOO000OOO0O =OO0O00OOO0OOO0O0O ['data']['gameCoreDataDBid']#line:543
                        OOOOOO0O0O000O00O =float (OO0O00OOO0OOO0O0O ['data']['silver'])/1000000000000 #line:544
                        OOO0O0O000O000000 =0 #line:549
                        for OO0O0OOO000OOOOOO in OO0000O0OOOOOO000 :#line:550
                            if not OO0O0OOO000OOOOOO :#line:551
                                O0000000OOO0O0000 =f'_crop_id={OOO0OOOOO000OOO0O}&site={OOO0O0O000O000000}_{O000O0OOO000O0OOO.time}'#line:552
                                OO00OO0OOO0O000O0 ={'source':'scsc','authorization':O000O0OOO000O0OOO .token ,'timestamp':O000O0OOO000O0OOO .time ,'sign':sign (O0000000OOO0O0000 ),'signstring':O0000000OOO0O0000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:562
                                OOOO00O000OOOO00O ={"site":OOO0O0O000O000000 ,"crop_id":OOO0OOOOO000OOO0O }#line:563
                                O00O0OOOO0O0000OO =requests .request ('post',f'{host}/game/crops/buy',headers =OO00OO0OOO0O000O0 ,data =OOOO00O000OOOO00O ).json ()#line:564
                                time .sleep (random .randint (1 ,3 )/10 )#line:566
                                if 'status'in O00O0OOOO0O0000OO :#line:567
                                    if O00O0OOOO0O0000OO ['status']==200 :#line:568
                                        if O00O0OOOO0O0000OO ['message']=='种子数量不足':#line:569
                                            OO0000000O0O00000 =O000O0OOO000O0OOO .level_new ()#line:570
                                            print (f'【种植合成】:{O00O0OOOO0O0000OO["message"]}')#line:571
                                            if not O000O0OOO000O0OOO .user_ad ():#line:572
                                                return False #line:573
                                    if O00O0OOOO0O0000OO ['status']==500 :#line:574
                                        print (f'【种植合成】:{O00O0OOOO0O0000OO["message"]}')#line:575
                                        return False #line:576
                            OOO0O0O000O000000 +=1 #line:577
                        OO0OOO000OO0O00O0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OO0OO00OOOO0O ).json ()#line:578
                        OOOOO00O000O0O0OO =OO0OOO000OO0O00O0 ['data']['cropList']#line:579
                        O00OOO0OOO0O0OOO0 =False #line:580
                        for OO0O0OOO000OOOOOO in range (12 ):#line:581
                            id =OOOOO00O000O0O0OO [OO0O0OOO000OOOOOO ]['level']#line:582
                            if float (OO0000000O0O00000 )-float (id )>9 :#line:583
                                OO0OO0OO0OO0OO0O0 =f'_site={OO0O0OOO000OOOOOO}_{timi_new()}'#line:584
                                OO0000OO000OO0OOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000O0OOO000O0OOO .token ,'timestamp':timi_new (),'sign':sign (OO0OO0OO0OO0OO0O0 ),'signstring':OO0OO0OO0OO0OO0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:595
                                OOOO0OO00O0000OO0 ={"site":OO0O0OOO000OOOOOO }#line:596
                                OO0O00OO0OO00O000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0000OO000OO0OOO ,data =OOOO0OO00O0000OO0 ).json ()#line:598
                                if 'status'in OO0O00OO0OO00O000 :#line:599
                                    if OO0O00OO0OO00O000 ['status']==200 :#line:600
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:601
                            if id !=0 :#line:602
                                for O000O0OO0OO000O0O in range (11 ):#line:603
                                    O0O0O0000000000OO =O000O0OO0OO000O0O +1 #line:604
                                    g =OOOOO00O000O0O0OO [O0O0O0000000000OO ]['level']#line:605
                                    if id ==g :#line:606
                                        O0OO0OOO00O00OO00 =O000O0OO0OO000O0O +2 #line:607
                                        if O0OO0OOO00O00OO00 !=OO0O0OOO000OOOOOO +1 :#line:608
                                            OOOO0O0OO000OOOO0 =OO0O0OOO000OOOOOO +1 #line:609
                                            time .sleep (random .randint (1 ,3 )/10 )#line:611
                                            O0000OOOOO0000OOO =f'_site={OOOO0O0OO000OOOO0 - 1}&targetSite={O0OO0OOO00O00OO00 - 1}_{timi_new()}'#line:612
                                            OO0O000OO000O0O00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000O0OOO000O0OOO .token ,'timestamp':timi_new (),'sign':sign (O0000OOOOO0000OOO ),'signstring':O0000OOOOO0000OOO ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:628
                                            O0OO000O0OO000O00 ={"site":int (OOOO0O0OO000OOOO0 -1 ),"targetSite":int (O0OO0OOO00O00OO00 -1 )}#line:629
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0O000OO000O0O00 ,json =O0OO000O0OO000O00 )#line:630
                                            O00OOO0OOO0O0OOO0 =True #line:632
                                    if O00OOO0OOO0O0OOO0 :#line:633
                                        break #line:634
                                if O00OOO0OOO0O0OOO0 :#line:635
                                    break #line:636
        except :#line:637
            O000O0OOO000O0OOO .synthetic ()#line:638
    def level_new (OOO0OO0OO0OOOOO0O ):#line:641
        try :#line:642
            OOO000O00O00O00O0 =f'__{timi_new()}'#line:643
            O0O0OO0OOOO0O000O ={'source':'scsc','authorization':OOO0OO0OO0OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O00O00O00O0 ),'signstring':OOO000O00O00O00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:653
            OO00O0OOO0O000OO0 =requests .request ('get',f'{host}/user',headers =O0O0OO0OOOO0O000O ).json ()#line:654
            if 'status'in OO00O0OOO0O000OO0 :#line:655
                if OO00O0OOO0O000OO0 ['status']==200 :#line:656
                    return float (OO00O0OOO0O000OO0 ['data']['level'])#line:657
        except Exception as O0000O00O0O00000O :#line:658
            print (O0000O00O0O00000O )#line:659
    def propsraffle (OOO00OO0O0OO0O0O0 ):#line:662
        try :#line:663
            while True :#line:664
                OOO00OOO0O0O000O0 =f'__{timi_new()}'#line:665
                OOO00O0O00O00000O ={'source':'scsc','authorization':OOO00OO0O0OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO0O0O000O0 ),'signstring':OOO00OOO0O0O000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:675
                O0000OO0O00O00O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO00O0O00O00000O ).json ()#line:676
                if 'status'in O0000OO0O00O00O0O :#line:678
                    if O0000OO0O00O00O0O ['status']==200 :#line:679
                        OO0OO0O0OOOO00000 =O0000OO0O00O00O0O ['data']['rows']#line:680
                        O000OO0O00000OOO0 =O0000OO0O00O00O0O ['data']['vstate']#line:681
                        if OO0OO0O0OOOO00000 ==5 or OO0OO0O0OOOO00000 ==6 or OO0OO0O0OOOO00000 ==7 :#line:682
                            OO0000OO00O0OOO00 =O0000OO0O00O00O0O ['data']['silver']#line:683
                            print (f'【转盘抽奖】:获得种子:{OO0000OO00O0OOO00}')#line:684
                        if OO0OO0O0OOOO00000 ==1 or OO0OO0O0OOOO00000 ==2 or OO0OO0O0OOOO00000 ==3 :#line:685
                            O00000OO0000O0OO0 =O0000OO0O00O00O0O ['data']['clover']#line:686
                            print (f'【转盘抽奖】:获得三叶草:{O00000OO0000O0OO0}')#line:687
                        if OO0OO0O0OOOO00000 ==4 or OO0OO0O0OOOO00000 ==8 :#line:688
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:689
                        if OO0OO0O0OOOO00000 =='抽奖次数已用完':#line:693
                            break #line:726
                time .sleep (random .randint (8 ,15 )/10 )#line:727
        except Exception as OO0O0O00OOO0O0000 :#line:728
            print (OO0O0O00OOO0O0000 )#line:729
    def friends_invitation (OOO0O00OO0OOOO0OO ):#line:732
        try :#line:733
            O000O00O0OO000O00 =f'__{timi_new()}'#line:734
            O0OO000OOOO00000O ={'source':'scsc','authorization':OOO0O00OO0OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00O0OO000O00 ),'signstring':O000O00O0OO000O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:744
            O00O000OOOO0O0O00 =requests .request ('get',f'{host}/friends',headers =O0OO000OOOO00000O ).json ()#line:745
            if 'status'in O00O000OOOO0O0O00 :#line:746
                if O00O000OOOO0O0O00 ['status']==200 :#line:747
                    OO000O0OO0O000OO0 =O00O000OOOO0O0O00 ['data']['myInviteter']#line:748
                    if OO000O0OO0O000OO0 :#line:749
                        OOO00O0OOO00000O0 =OO000O0OO0O000OO0 ['user']['nickname']#line:750
                        OO0O00O000000O00O =OOO0O00OO0OOOO0OO .certification ()#line:751
                        print (f'【查邀请人】:我的邀请人:{OOO00O0OOO00000O0}丨实名:{OO0O00O000000O00O}')#line:752
                    else :#line:753
                        if OOO0O00OO0OOOO0OO .innerId !='0':#line:754
                            OOO0O00OO0OOOO0OO .invitation ()#line:755
        except Exception as O0OO0000OO0000OOO :#line:756
            print (O0OO0000OO0000OOO )#line:757
    def add_clover (OOOOO000OOO0OOOO0 ):#line:760
        global golden_seed #line:761
        try :#line:762
            OOO0OO0OOOOOO0O00 =f'__{timi_new()}'#line:763
            OO0OOOO0OOOO0000O ={'source':'scsc','authorization':OOOOO000OOO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OOOOOO0O00 ),'signstring':OOO0OO0OOOOOO0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:773
            O0OO0O0OO000O0OOO =requests .request ('get',f'{host}/assets/clovers',headers =OO0OOOO0OOOO0000O ).json ()#line:774
            if 'status'in O0OO0O0OO000O0OOO :#line:776
                if O0OO0O0OO000O0OOO ['status']==200 :#line:777
                    O0OO000OO000000OO =O0OO0O0OO000O0OOO ['data']['clover']#line:778
                    OOO0O0O0OO00OOOO0 =O0OO0O0OO000O0OOO ['data']['used_clover']#line:779
                    O00O0OOO00O0O00O0 =float (O0OO000OO000000OO )-float (OOO0O0O0OO00OOOO0 )#line:780
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOO0O0O0OO00OOOO0}')#line:781
                    if OOOOO000OOO0OOOO0 .certification ()!='未实名':#line:782
                        if O00O0OOO00O0O00O0 >1 :#line:783
                            OOO0OO0OOOOOO0O00 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00O0OOO00O0O00O0)}_{timi_new()}'#line:784
                            O00OOO000OOO0OO0O ={'source':'scsc','authorization':OOOOO000OOO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OOOOOO0O00 ),'signstring':OOO0OO0OOOOOO0O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
                            O000OOOO000OOO000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00O0OOO00O0O00O0 )}#line:795
                            OO00OOO0O0O0OOOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =O00OOO000OOO0OO0O ,data =O000OOOO000OOO000 ).json ()#line:796
                            if 'status'in OO00OOO0O0O0OOOOO :#line:798
                                if OO00OOO0O0O0OOOOO ['status']==200 :#line:799
                                    print (f'【参与抽奖】:添加☘️:{OO00OOO0O0O0OOOOO["data"]}丨数量:{O00O0OOO00O0O00O0}')#line:800
                                if OO00OOO0O0O0OOOOO ['status']==500 :#line:801
                                    print (f'【参与抽奖】:添加☘️:{OO00OOO0O0O0OOOOO["message"]}')#line:802
            O0OOO0O0O0000OO00 =requests .request ('get',f'{host}/lottery',headers =OO0OOOO0OOOO0000O ).json ()#line:803
            OO0000OOO0000O0OO =OOOOO000OOO0OOOO0 .winning_rewards ()#line:805
            if 'status'in O0OOO0O0O0000OO00 :#line:806
                if O0OOO0O0O0000OO00 ['status']==200 :#line:807
                    O0O0000O0O000000O =O0OOO0O0O0000OO00 ['data'][0 ]['day_get_gold_quantity']#line:808
                    golden_seed +=float (O0O0000O0O000000O )#line:809
                    OO000O0000OO0OOO0 =O0OOO0O0O0000OO00 ['data'][1 ]['value']#line:810
                    O0O0O0O0O000OOO0O =O0OOO0O0O0000OO00 ['data'][0 ]['join_number']#line:811
                    OOO0O0000OO00OOO0 =int (float (O0OOO0O0O0000OO00 ['data'][0 ]['totalValue']))#line:812
                    O00O0O000OO0OOOO0 =float (OO000O0000OO0OOO0 /OOO0O0000OO00OOO0 )*10000 #line:813
                    OOO00O0OOOO0000O0 =OOO0O0000OO00OOO0 /O0O0O0O0O000OOO0O #line:814
                    print (f'【参与抽奖】:预计每天中{str(O0O0000O0O000000O)[:6]}颗金种子丨好友收益:{str(OO0000OOO0000O0OO)[:6]}')#line:815
                    print (f'【抽奖统计】:每1万☘️中{str(O00O0O000OO0OOOO0)[:6]}颗金种子丨☘️人均:{str(OOO00O0OOOO0000O0)[:7]}️')#line:816
        except Exception as OO0OO00O0000OO0O0 :#line:817
            print (OO0OO00O0000OO0O0 )#line:818
    def energy (OO0O00OO0OO000000 ):#line:822
        try :#line:823
            while True :#line:824
                OO0O00O000OO0O00O =f'__{timi_new()}'#line:825
                OOOOO0O00OO0OOO00 ={'source':'scsc','authorization':OO0O00OO0OO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O000OO0O00O ),'signstring':OO0O00O000OO0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:835
                OOOOOOO000000OO0O =requests .request ('get',f'{host}/energy/general',headers =OOOOO0O00OO0OOO00 ).json ()#line:836
                if 'status'in OOOOOOO000000OO0O :#line:838
                    if OOOOOOO000000OO0O ['status']==200 :#line:839
                        O0OOOO0O00OO00O0O =OOOOOOO000000OO0O ['data']['ordinary_water']#line:840
                        OOOOOOO0O00000OOO =OOOOOOO000000OO0O ['data']['ordinary_fertilizer']#line:841
                        OO0OOO0O0OOO0O00O =OOOOOOO000000OO0O ['data']['videoStatus']#line:842
                        O000O0OOO0O0O0000 =OOOOOOO000000OO0O ['data']['waterVideoKey']#line:843
                        print (f'【我的营养】:肥料:{str(OOOOOOO0O00000OOO).split(".")[0]}丨水滴:{str(O0OOOO0O00OO00O0O).split(".")[0]}')#line:844
                        if float (OOOOOOO0O00000OOO )<96 :#line:845
                            if OO0OOO0O0OOO0O00O :#line:846
                                time .sleep (random .randint (160 ,180 )/10 )#line:847
                                OOO0O0O000OOOO0O0 =99 -float (OOOOOOO0O00000OOO )#line:848
                                O000OO0OO0OO0OO00 ={"fertilizer":str (OOO0O0O000OOOO0O0 ).split ('.')[0 ]}#line:849
                                O00OO0O0000OO0O00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOOO0O00OO0OOO00 ).json ()#line:850
                                if 'status'in O00OO0O0000OO0O00 :#line:852
                                    if O00OO0O0000OO0O00 ['status']==200 :#line:853
                                        print (f'【购买肥料】:看广告获取肥料:{O00OO0O0000OO0O00["message"]}')#line:854
                                    if O00OO0O0000OO0O00 ['status']==500 :#line:855
                                        print (f'【购买肥料】:看广告获取肥料:{O00OO0O0000OO0O00["message"]}')#line:856
                                        break #line:857
                            if energy :#line:858
                                if float (OOOOOOO0O00000OOO )<float (fertilizer_quantity ):#line:859
                                    OO00OOOOOOOO00O0O =f'_fertilizer=10_{timi_new()}'#line:860
                                    O000OOO0OO0OO0OOO ={'source':'scsc','authorization':OO0O00OO0OO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOOOOOO00O0O ),'signstring':OO00OOOOOOOO00O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:870
                                    O0000OO0OO00OOOOO ={"fertilizer":"10"}#line:871
                                    OOO0OO0OOOO00O00O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O000OOO0OO0OO0OOO ,data =O0000OO0OO00OOOOO ).json ()#line:872
                                    if 'status'in OOO0OO0OOOO00O00O :#line:874
                                        if OOO0OO0OOOO00O00O ['status']==200 :#line:875
                                            print (f'【购买肥料】:购买肥料:{OOO0OO0OOOO00O00O["message"]}丨数量:10')#line:876
                                        if OOO0OO0OOOO00O00O ['status']==500 :#line:877
                                            print (f'【购买肥料】:购买肥料:{OOO0OO0OOOO00O00O["message"]}丨数量:10')#line:878
                                            OOOO0O0OOOOO0OO00 =f'__{timi_new()}'#line:879
                                            O0OOO000OO0OO000O ={'source':'scsc','authorization':OO0O00OO0OO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0OOOOO0OO00 ),'signstring':OOOO0O0OOOOO0OO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:889
                                            OO00OOO0O0OO00000 =requests .request ('get',f'{host}/user',headers =O0OOO000OO0OO000O ).json ()#line:890
                                            if 'status'in OO00OOO0O0OO00000 :#line:891
                                                if OO00OOO0O0OO00000 ['status']==200 :#line:892
                                                    OO0000OOOOO000000 =OO00OOO0O0OO00000 ['data']['inner_id']#line:893
                                                    give_gold (OO0000OOOOO000000 )#line:894
                        if float (O0OOOO0O00OO00O0O )<880 :#line:896
                            if O000O0OOO0O0O0000 :#line:897
                                time .sleep (random .randint (160 ,180 )/10 )#line:898
                                OO0O000000O000000 =999 -float (O0OOOO0O00OO00O0O )#line:899
                                O0000OOO0OO0O0OO0 ={"water":str (OO0O000000O000000 ).split ('.')[0 ]}#line:900
                                OOO000O00O0000O00 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOOO0O00OO0OOO00 ).json ()#line:901
                                if 'status'in OOO000O00O0000O00 :#line:903
                                    if OOO000O00O0000O00 ['status']==200 :#line:904
                                        print (f'【购买水滴】:看广告获取水滴:{OOO000O00O0000O00["message"]}')#line:905
                                    if OOO000O00O0000O00 ['status']==500 :#line:906
                                        print (f'【购买水滴】:看广告获取水滴:{OOO000O00O0000O00["message"]}')#line:907
                                        break #line:908
                            if energy :#line:909
                                if float (O0OOOO0O00OO00O0O )<float (wadverti_quantity ):#line:910
                                    OO000O000O0000OOO =f'_water=100_{timi_new()}'#line:911
                                    O00OO0O000OOO00O0 ={'source':'scsc','authorization':OO0O00OO0OO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O000O0000OOO ),'signstring':OO000O000O0000OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:921
                                    OO0O000OO0O0OO000 ={"water":"100"}#line:922
                                    O0OOO0O0O0O000000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O00OO0O000OOO00O0 ,data =OO0O000OO0O0OO000 ).json ()#line:923
                                    if 'status'in O0OOO0O0O0O000000 :#line:925
                                        if O0OOO0O0O0O000000 ['status']==200 :#line:926
                                            print (f'【购买水滴】:购买水滴:{O0OOO0O0O0O000000["message"]}丨数量:100')#line:927
                                        if O0OOO0O0O0O000000 ['status']==500 :#line:928
                                            print (f'【购买水滴】:购买水滴:{O0OOO0O0O0O000000["message"]}丨数量:100')#line:929
                        break #line:933
        except Exception as OOO0OOO0OOO0000OO :#line:935
            print (OOO0OOO0OOO0000OO )#line:936
def bundled_def ():#line:938
    O0O000O0O00OO0OO0 =['5570536','7750212','7911652','7911680','7805624']#line:939
    return O0O000O0O00OO0OO0 [random .randint (0 ,len (O0O000O0O00OO0OO0 )-1 )]#line:940
def version_of_the_validation ():#line:944
    return str ((82 -56 )/10 )#line:945
def gitee_validation ():#line:948
    try :#line:949
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:950
    except :#line:951
        sys .exit (0 )#line:952
def update_the_validation ():#line:956
    try :#line:957
        OO000OO000OOOO000 =gitee_validation ()#line:958
        if version_of_the_validation ()<OO000OO000OOOO000 ['CityEarth']['edition']:#line:959
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO000OO000OOOO000["CityEarth"]["edition"]}   ❌')#line:960
            print (f'更新内容=>>{OO000OO000OOOO000["CityEarth"]["content"]}   🎉')#line:961
        else :#line:962
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO000OO000OOOO000["CityEarth"]["edition"]}   ✅')#line:963
            print (f'更新内容=>> {OO000OO000OOOO000["CityEarth"]["content"]}   🎉')#line:964
    except Exception as O0OOOO0000000O0OO :#line:965
        print (O0OOOO0000000O0OO )#line:966
def os_qinglong ():#line:969
    if application in os .environ :#line:970
        OOO00O0OOO0000OO0 =os .environ [application ].split ('\n')#line:971
        if len (OOO00O0OOO0000OO0 )>0 :#line:972
            return OOO00O0OOO0000OO0 #line:973
        else :#line:974
            print (f"{application}变量未启用")#line:975
            print ('脚本退出')#line:976
            sys .exit (1 )#line:977
    else :#line:978
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:980
        return os_built ()#line:981
def os_built ():#line:984
    if token :#line:985
        OO0OO0OO0OOOO0000 =token .split ('\n')#line:986
        if len (OO0OO0OO0OOOO0000 )>0 :#line:987
            return OO0OO0OO0OOOO0000 #line:988
    else :#line:989
        print (f"内置变量为空")#line:990
        print ('脚本结束')#line:991
        sys .exit (0 )#line:992
if __name__ =='__main__':#line:995
    start ()#line:996
