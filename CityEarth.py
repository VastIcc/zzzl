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
zh_mony = '3'               # 每次小号金种子不足转赠数量 最好设置低于你赠送的那个数，不然会直接转走
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
        O00OO0O0OO00O0OOO =os_qinglong ()#line:10
        print (f"==========共找到{len(O00OO0O0OO00O0OOO)}个账号==========")#line:11
        for OOOOO00OOOOOO00OO in O00OO0O0OO00O0OOO :#line:12
            OO000O000OOO0OO0O =[]#line:13
            print (f"------------正在执行第{O00OO0O0OO00O0OOO.index(OOOOO00OOOOOO00OO) + 1}个账号------------")#line:14
            O00O00000OO0O00O0 =CityEarth (OOOOO00OOOOOO00OO ,OO000O000OOO0OO0O )#line:15
            def O00000OO00O0OOO00 ():#line:17
                if O00O00000OO0O00O0 .base_info ():#line:19
                    O00O00000OO0O00O0 .sealing ()#line:21
                    O00O00000OO0O00O0 .invitenum ()#line:23
                    O00O00000OO0O00O0 .game_map ()#line:25
                    O00O00000OO0O00O0 .friends_invitation ()#line:27
                    O00O00000OO0O00O0 .energy ()#line:29
                    O00O00000OO0O00O0 .add_clover ()#line:31
                    O00O00000OO0O00O0 .propsraffle ()#line:33
                    O00O00000OO0O00O0 .synthetic ()#line:35
                    O00O00000OO0O00O0 .crops_illustrated ()#line:37
                    O00O00000OO0O00O0 .give_gold ()#line:39
                    O00O00000OO0O00O0 .withdraw ()#line:41
            O0000OO0000O0000O =threading .Thread (target =O00000OO00O0OOO00 )#line:43
            O0000OO0000O0000O .start ()#line:44
            time .sleep (time_xx )#line:45
        print (f"------------正在处理推送通知------------")#line:46
        time .sleep (0.5 )#line:47
        O00OO0O0O00OOO0OO =format_msg ()#line:48
        send (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00OO0O0O00OOO0OO +' ')#line:49
    except Exception as O000O00O0O0OO00O0 :#line:50
        print (O000O00O0O0OO00O0 )#line:51
def give_gold (O00OO0OO00OOOO0OO ):#line:54
        try :#line:55
            O00OO0O000O0OO0OO =zh_mony #line:56
            O000O0O00O0O0OO0O =f'_doneeNo={O00OO0OO00OOOO0OO}&quantity={O00OO0O000O0OO0OO}_{timi_new()}'#line:57
            O000O0OOO0000OO00 ={'source':'scsc','authorization':token_zs .split ('&')[0 ],'timestamp':str (timi_new ()),'sign':sign (O000O0O00O0O0OO0O ),'signstring':O000O0O00O0O0OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:67
            OO00OOOOO0OO000O0 ={"quantity":O00OO0O000O0OO0OO ,"doneeNo":O00OO0OO00OOOO0OO }#line:71
            O000O0O00OO000OO0 =requests .request ('post',f'{host}/finance/give-gold',headers =O000O0OOO0000OO00 ,data =OO00OOOOO0OO000O0 ).json ()#line:72
            if 'status'in O000O0O00OO000OO0 :#line:74
                if O000O0O00OO000OO0 ['status']==200 :#line:75
                    if O000O0O00OO000OO0 ['data']:#line:76
                        print (f'【赠送种子】:赠送{O00OO0O000O0OO0OO}种子给{O00OO0OO00OOOO0OO}成功')#line:77
                if O000O0O00OO000OO0 ['status']==401 :#line:78
                    print (f'【赠送种子】:{O000O0O00OO000OO0["message"]}')#line:79
                if O000O0O00OO000OO0 ['status']==500 :#line:80
                    print (f'【赠送种子】:{O000O0O00OO000OO0["message"]}')#line:81
        except Exception as OOOO0O00OO0OO00OO :#line:82
            print (OOOO0O00OO0OO00OO )#line:83
def sign (OO0O0000O0OOOOOOO ):#line:86
    O0OO0OO0000O000OO =hashlib .md5 (OO0O0000O0OOOOOOO .encode ()).hexdigest ()#line:87
    O00O0OO0OO00O000O ="scsc%^&*"+O0OO0OO0000O000OO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:88
    OO000OO0O000O00O0 =hashlib .md5 (O00O0OO0OO00O000O .encode ()).hexdigest ()#line:89
    return OO000OO0O000O00O0 #line:90
def format_msg ():#line:92
    OOO000000000O0000 =""#line:93
    for OO000O0OO0000O000 in msg_list :#line:94
        OOO000000000O0000 +=str (OO000O0OO0000O000 )+"\r\n"#line:95
    return OOO000000000O0000 #line:96
def timi_new ():#line:98
    return str (int (time .time ()*1000 ))#line:99
class CityEarth :#line:102
    def __init__ (OO00OOO00O000OO00 ,O0O0O000OO0O00O00 ,O00O0O0O0000OOOO0 ):#line:104
        try :#line:105
            OO00OOO00O000OO00 .msg =O00O0O0O0000OOOO0 #line:106
            OO00OOO00O000OO00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:107
            OO00OOO00O000OO00 .token =O0O0O000OO0O00O00 .split ('&')[0 ]#line:108
            OO00OOO00O000OO00 .innerId =O0O0O000OO0O00O00 .split ('&')[1 ]#line:109
            OO00OOO00O000OO00 .doneeNo =O0O0O000OO0O00O00 .split ('&')[2 ]#line:110
        except :#line:111
            print ('变量格式错误')#line:112
    def base_info (OO00O00O000OOO0OO ):#line:115
        try :#line:116
            OO00O00O000OOO0OO .watched_ad ()#line:118
            O0OO000000OO00O00 =f'__{timi_new()}'#line:119
            O0O000OO0O0OO0O0O ={'source':'scsc','authorization':OO00O00O000OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000000OO00O00 ),'signstring':O0OO000000OO00O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:129
            O0000O00O00OO0O0O =requests .request ('get',f'{host}/user',headers =O0O000OO0O0OO0O0O ).json ()#line:130
            if 'status'in O0000O00O00OO0O0O :#line:132
                if O0000O00O00OO0O0O ['status']==200 :#line:133
                    O00O0OOO0OOO000OO =O0000O00O00OO0O0O ['data']['nickname']#line:134
                    OO0000OO0O0OO0OO0 =O0000O00O00OO0O0O ['data']['inner_id']#line:135
                    O0000OO000OOOOOO0 =O0000O00O00OO0O0O ['data']['assets']['gold']#line:136
                    OO00OOO0O00000OO0 =O0000O00O00OO0O0O ['data']['level']#line:137
                    print (f'【账号信息】:昵称:{O00O0OOO0OOO000OO[:5]}丨ID:{OO0000OO0O0OO0OO0}丨等级:{OO00OOO0O00000OO0}丨金种子:{str(O0000OO000OOOOOO0).split(".")[0]}')#line:138
                if O0000O00O00OO0O0O ['status']==401 :#line:139
                    print (O0000O00O00OO0O0O ['message'])#line:140
                    OO00O00O000OOO0OO .msg .append ('有账号失效了')#line:141
                    return False #line:142
                if O0000O00O00OO0O0O ['status']==500 :#line:143
                    return False #line:144
            return True #line:145
        except Exception as O0O0O000O0000000O :#line:146
            print (O0O0O000O0000000O )#line:147
    def sealing (OO0O0OOO000OO0000 ):#line:150
        try :#line:151
            O0O0O000OO00O0OO0 =f'__{timi_new()}'#line:152
            O0000O0OOOOOOO0OO ={'source':'scsc','authorization':OO0O0OOO000OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000OO00O0OO0 ),'signstring':O0O0O000OO00O0OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:162
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0000O0OOOOOOO0OO )#line:163
            requests .request ('get',f'{host}/packsack/list',headers =O0000O0OOOOOOO0OO )#line:164
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0000O0OOOOOOO0OO )#line:165
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0000O0OOOOOOO0OO )#line:166
            requests .request ('get',f'{host}/user',headers =O0000O0OOOOOOO0OO )#line:167
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0000O0OOOOOOO0OO )#line:168
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0000O0OOOOOOO0OO )#line:169
            requests .request ('post',f'{host}/announcement/announcement',headers =O0000O0OOOOOOO0OO )#line:170
            requests .request ('get',f'{host}/game/getAllData',headers =O0000O0OOOOOOO0OO )#line:171
            requests .request ('get',f'{host}/assets',headers =O0000O0OOOOOOO0OO )#line:172
        except Exception as OO00OOO0OO0000O00 :#line:173
            print (OO00OOO0OO0000O00 )#line:174
    def withdraw (O00000OOO0OOO000O ):#line:178
        OO0OO0O0OOO00O0OO =f'__{timi_new()}'#line:179
        O0O00OO00OO0OOO00 ={'source':'scsc','authorization':O00000OOO0OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0OOO00O0OO ),'signstring':OO0OO0O0OOO00O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:189
        OO0O0000OO0OO0000 =requests .request ('get',f'{host}/assets',headers =O0O00OO00OO0OOO00 ).json ()#line:190
        if 'status'in OO0O0000OO0OO0000 :#line:192
            if OO0O0000OO0OO0000 ['status']==200 :#line:193
                O00O000O00OOO0O0O =OO0O0000OO0OO0000 ['data']['cash']#line:194
                if float (O00O000O00OOO0O0O )>20 :#line:195
                    OO0OO0O0OOO00O0OO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:196
                    O0O00OO00OO0OOO00 ={'authorization':O00000OOO0OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0OOO00O0OO ),'signstring':OO0OO0O0OOO00O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:205
                    OOO00OO0O00O00000 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:206
                    O0OO00OO00000OOO0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O00OO00OO0OOO00 ,data =OOO00OO0O00O00000 ).json ()#line:208
                    print (O0OO00OO00000OOO0 )#line:209
    def invitenum (O0OO0OO0OO000OO00 ):#line:212
        O0OOOOOO0OOO0000O =f'__{timi_new()}'#line:213
        OOO0O000OO00O0OOO ={'source':'scsc','authorization':O0OO0OO0OO000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOO0OOO0000O ),'signstring':O0OOOOOO0OOO0000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:223
        O0O000OO0OOO0O0OO =requests .request ('get',f'{host}/invite/invitenum',headers =OOO0O000OO00O0OOO ).json ()#line:224
        if 'status'in O0O000OO0OOO0O0OO :#line:226
            if O0O000OO0OOO0O0OO ['status']==200 :#line:227
                O0O0000000OO0OO0O =O0O000OO0OOO0O0OO ['data']['invited_count']#line:228
                O0O00O000OO00OOOO =O0O000OO0OOO0O0OO ['data']['invited_second_count']#line:229
                print (f'【我的邀请】:直邀好友:{O0O0000000OO0OO0O}丨间邀好友:{O0O00O000OO00OOOO}')#line:230
    def game_map (O0O0OO0O0OOOO00OO ):#line:233
        try :#line:234
            OOO0O000O00OO000O =f'__{timi_new()}'#line:235
            OO00000O00OO0OO0O ={'source':'scsc','authorization':O0O0OO0O0OOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O00OO000O ),'signstring':OOO0O000O00OO000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            O00O0O0000OO00000 =requests .request ('get',f'{host}/game/map',headers =OO00000O00OO0OO0O ).json ()#line:246
            if 'status'in O00O0O0000OO00000 :#line:248
                if O00O0O0000OO00000 ['status']==200 :#line:249
                    for O0O000000OO0O000O in O00O0O0000OO00000 ['data']['list'][0 ]['crops']:#line:250
                        OO00000O00OOOOOO0 =O0O000000OO0O000O ['level']#line:252
                        if OO00000O00OOOOOO0 ==41 :#line:253
                            O0OO00OO0O0OO00OO =O0O000000OO0O000O ['crop_name']#line:254
                            OO0OO00OO0O000O0O =O0O000000OO0O000O ['count']#line:255
                            if OO0OO00OO0O000O0O >0 :#line:256
                                print (f'【农业资产】:{O0OO00OO0O0OO00OO}丨数量:{OO0OO00OO0O000O0O}')#line:257
        except Exception as OO0OOO00O0O0O0OO0 :#line:258
            print (OO0OOO00O0O0O0OO0 )#line:259
    def give_gold (OO000OO0O0OO0O0O0 ):#line:262
        try :#line:263
            OO00OOOOOO000OOO0 =f'__{timi_new()}'#line:264
            OOOO000000O0O0O0O ={'source':'scsc','authorization':OO000OO0O0OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOOOO000OOO0 ),'signstring':OO00OOOOOO000OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:274
            O0O00O0OO0O000OO0 =requests .request ('get',f'{host}/user',headers =OOOO000000O0O0O0O ).json ()#line:275
            if 'status'in O0O00O0OO0O000OO0 :#line:276
                if O0O00O0OO0O000OO0 ['status']==200 :#line:277
                    if float (OO000OO0O0OO0O0O0 .doneeNo )!=0 :#line:278
                        OO000OOOOOO000O00 =O0O00O0OO0O000OO0 ['data']['assets']['gold']#line:279
                        if float (OO000OOOOOO000O00 )>float (OO000OO0O0OO0O0O0 .innerId ):#line:280
                            OOO000O0OO0OO0000 =int (float (OO000OOOOOO000O00 )/1.1 )#line:281
                            OO00OOOOOO000OOO0 =f'_doneeNo={OO000OO0O0OO0O0O0.doneeNo}&quantity={OOO000O0OO0OO0000}_{timi_new()}'#line:282
                            OOOO000000O0O0O0O ={'source':'scsc','authorization':OO000OO0O0OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOOOO000OOO0 ),'signstring':OO00OOOOOO000OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:292
                            OO00OO000OO000000 ={"quantity":OOO000O0OO0OO0000 ,"doneeNo":OO000OO0O0OO0O0O0 .doneeNo }#line:296
                            OO000O0000OO00OO0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOO000000O0O0O0O ,data =OO00OO000OO000000 ).json ()#line:297
                            if 'status'in OO000O0000OO00OO0 :#line:299
                                if OO000O0000OO00OO0 ['status']==200 :#line:300
                                    if OO000O0000OO00OO0 ['data']:#line:301
                                        print (f'【赠送种子】:赠送{OOO000O0OO0OO0000}种子给{OO000OO0O0OO0O0O0.doneeNo}成功')#line:302
                    else :#line:303
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:304
        except Exception as O0OOO00OOOOO0OOOO :#line:305
            print (O0OOO00OOOOO0OOOO )#line:306
    def invitation (O0OO0O000O0O0000O ):#line:308
        try :#line:309
            _OO00OOOOOOOO00O00 =float (bundled_def ())/4 #line:310
            OO0O0000O000O00O0 =f'_innerId={int(_OO00OOOOOOOO00O00)}_{timi_new()}'#line:311
            O0O0O0O000O0000O0 ={'source':'scsc','authorization':O0OO0O000O0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000O000O00O0 ),'signstring':OO0O0000O000O00O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:321
            O00OOOOOOO0OOO0OO ={"innerId":int (_OO00OOOOOOOO00O00 )}#line:322
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0O0O0O000O0000O0 ,data =O00OOOOOOO0OOO0OO )#line:323
        except Exception as OO0000OO0O00O0O0O :#line:324
            print (OO0000OO0O00O0O0O )#line:325
    def winning_rewards (O0O000OOO00000O0O ):#line:328
        try :#line:329
            O000O000O0OO00OO0 =f'__{timi_new()}'#line:330
            O00OO0O0OO000OO00 ={'source':'scsc','authorization':O0O000OOO00000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000O0OO00OO0 ),'signstring':O000O000O0OO00OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:340
            O00O0O0O0O00000OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00OO0O0OO000OO00 ).json ()#line:341
            if 'status'in O00O0O0O0O00000OO :#line:343
                if O00O0O0O0O00000OO ['status']==200 :#line:344
                    if O00O0O0O0O00000OO ['data']['amount']:#line:345
                        OOO00OOOO00O00O00 =O00O0O0O0O00000OO ['data']['amount']['gold']#line:346
                        return OOO00OOOO00O00O00 #line:347
                    else :#line:348
                        return 0 #line:349
        except Exception as O00O0OOOOOOO00O0O :#line:350
            print (O00O0OOOOOOO00O0O )#line:351
    def certification (O0O000OO00000OO0O ):#line:354
        try :#line:355
            OOO0O0OO000OOO000 =f'__{timi_new()}'#line:356
            OO0O000OO00OO000O ={'source':'scsc','authorization':O0O000OO00000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO000OOO000 ),'signstring':OOO0O0OO000OOO000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:366
            OO00OO0O0OO0O00O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0O000OO00OO000O ).json ()#line:367
            if 'status'in OO00OO0O0OO0O00O0 :#line:369
                if OO00OO0O0OO0O00O0 ['status']==200 :#line:370
                    if OO00OO0O0OO0O00O0 ['data']['result']:#line:371
                        OO0OO0O00OOO0O000 =OO00OO0O0OO0O00O0 ['data']['nick_name']#line:372
                        return OO0OO0O00OOO0O000 #line:373
                    else :#line:374
                        return '未实名'#line:375
        except Exception as O0OO0O00OOO0OO0OO :#line:376
            print (O0OO0O00OOO0OO0OO )#line:377
    def crops_illustrated (OOO0OO00O0O0OOO00 ):#line:380
        try :#line:381
            OO0000000O0O00OO0 =f'__{timi_new()}'#line:382
            O0O00000OO00OOO0O ={'source':'scsc','authorization':OOO0OO00O0O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000000O0O00OO0 ),'signstring':OO0000000O0O00OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:392
            OOOOOOOOO000OO00O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O00000OO00OOO0O ).json ()#line:393
            if 'status'in OOOOOOOOO000OO00O :#line:395
                if OOOOOOOOO000OO00O ['status']==200 :#line:396
                    OO00O0O000O00OOOO =OOOOOOOOO000OO00O ['data'][0 ]['crops']#line:397
                    for O0000OOOO00O00O00 in OO00O0O000O00OOOO :#line:398
                        if O0000OOOO00O00O00 ['ill_clover_award']:#line:399
                            if float (O0000OOOO00O00O00 ['ill_clover_award'])>1 :#line:400
                                if O0000OOOO00O00O00 ['is_finish']:#line:401
                                    if not O0000OOOO00O00O00 ['is_getit']:#line:402
                                        if OOO0OO00O0O0OOO00 .certification ()!='未实名':#line:403
                                            OO0000000O0O00OO0 =f'_award_level={O0000OOOO00O00O00["level"]}_{timi_new()}'#line:404
                                            O0O00000OO00OOO0O ={'source':'scsc','authorization':OOO0OO00O0O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000000O0O00OO0 ),'signstring':OO0000000O0O00OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:414
                                            O000OOO000OOO00O0 ={"award_level":O0000OOOO00O00O00 ['level']}#line:415
                                            O0OO0O0000OO00O00 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O00000OO00OOO0O ,json =O000OOO000OOO00O0 ).json ()#line:417
                                            if 'status'in O0OO0O0000OO00O00 :#line:418
                                                if O0OO0O0000OO00O00 ['status']==200 :#line:419
                                                    OOOO000O0OO0OOO0O =O0OO0O0000OO00O00 ['data']['ill_clover_award']#line:420
                                                    print (f'【图鉴奖励】:领取{O0000OOOO00O00O00["crop_name"]}成就丨奖励{OOOO000O0OO0OOO0O}☘️')#line:422
                                                if O0OO0O0000OO00O00 ['status']==500 :#line:423
                                                    print (f'【图鉴奖励】:{O0OO0O0000OO00O00["message"]}')#line:424
        except Exception as OOOOO000O0OO0OO00 :#line:425
            print (OOOOO000O0OO0OO00 )#line:426
    def watched_ad (OOOOOOO00OO0000O0 ):#line:429
        try :#line:430
            O0O0O0OOOO00O0O0O =f'__{timi_new()}'#line:431
            OO000OOO0OOO0OO0O ={'source':'scsc','authorization':OOOOOOO00OO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOO00O0O0O ),'signstring':O0O0O0OOOO00O0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:441
            O0O0O0OO00O0O00O0 =requests .request ('get',f'{host}/game/getAllData',headers =OO000OOO0OOO0OO0O ).json ()#line:442
            if 'status'in O0O0O0OO00O0O00O0 :#line:444
                if O0O0O0OO00O0O00O0 ['status']==200 :#line:445
                    if 'offlineInfo'in O0O0O0OO00O0O00O0 ['data']:#line:446
                        time .sleep (random .randint (3 ,5 ))#line:447
                        O0O0O000OOOOO00O0 =O0O0O0OO00O0O00O0 ['data']['offlineInfo']['off_minute']#line:448
                        O00000O0000OOOOO0 =float (O0O0O0OO00O0O00O0 ['data']['silver'])/1000000000000 #line:449
                        time .sleep (1 )#line:450
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO000OOO0OOO0OO0O ).json ()#line:451
                        time .sleep (2 )#line:452
                        O0OO0O000O0OO000O =requests .request ('get',f'{host}/game/getAllData',headers =OO000OOO0OOO0OO0O ).json ()#line:453
                        if 'status'in O0OO0O000O0OO000O :#line:455
                            if O0OO0O000O0OO000O ['status']==200 :#line:456
                                O0O000OOOOO0OOOOO =float (O0OO0O000O0OO000O ['data']['silver'])/1000000000000 #line:457
                                OO00O0O0O0OO000OO =str (O0O000OOOOO0OOOOO -O00000O0000OOOOO0 )[:6 ]#line:458
                                print (f'【离线奖励】:翻倍离线{O0O0O000OOOOO00O0}分钟奖励🌱数量:{OO00O0O0O0OO000OO}t粒')#line:459
        except Exception as OO0OOOOO0O0O00O00 :#line:460
            print (OO0OOOOO0O0O00O00 )#line:461
    def user_ad (OO0OO00OO0O000OOO ):#line:464
        try :#line:465
            O0OOOO00000O0O000 =f'__{timi_new()}'#line:466
            OOOOOOOO0O0000000 ={'source':'scsc','authorization':OO0OO00OO0O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00000O0O000 ),'signstring':O0OOOO00000O0O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:476
            OO000O0OO0O0O0O0O =requests .request ('get',f'{host}/user/ad',headers =OOOOOOOO0O0000000 ).json ()#line:477
            if 'status'in OO000O0OO0O0O0O0O :#line:479
                if OO000O0OO0O0O0O0O ['status']==200 :#line:480
                    OOO0OOO00O00O0000 =OO000O0OO0O0O0O0O ['data']['max_time']#line:481
                    OOOO00OOOOO0OO00O =OO000O0OO0O0O0O0O ['data']['watch_time']#line:482
                    O000O00OOO0O00O0O =OO000O0OO0O0O0O0O ['data']['added_time']#line:483
                    print (f'【获取种子】:获取🌱剩余{O000O00OOO0O00O0O + OOO0OOO00O00O0000 - OOOO00OOOOO0OO00O}次丨好友提供:{O000O00OOO0O00O0O}次')#line:484
                    if O000O00OOO0O00O0O +OOO0OOO00O00O0000 -OOOO00OOOOO0OO00O >0 :#line:485
                        time .sleep (random .randint (16 ,19 ))#line:486
                        O0000000OO0000000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOOOOOOO0O0000000 ).json ()#line:487
                        if 'status'in O0000000OO0000000 :#line:489
                            if O0000000OO0000000 ['status']==200 :#line:490
                                O00OO00O0000OOO00 =float (O0000000OO0000000 ['data']['silver'])/1000000000000 #line:491
                                print (f'【获取种子】:获得🌱:{int(O00OO00O0000OOO00)}t粒')#line:492
                                return True #line:493
                            if O0000000OO0000000 ['status']==500 :#line:494
                                O0O0OOO000O00000O =O0000000OO0000000 ['message']#line:495
                                print (f'【获取种子】:{O0O0OOO000O00000O}')#line:496
                                return False #line:497
        except Exception as O00OOO000O0OOO0OO :#line:498
            print (O00OOO000O0OOO0OO )#line:499
    def synthetic (O00O000000O00O0O0 ):#line:502
        global id ,g #line:503
        try :#line:504
            OO0OO0O000000OOOO =O00O000000O00O0O0 .level_new ()#line:505
            OO00O00O0OOO0OOOO =random .randint (9 ,11 )#line:506
            OOOO000O0O0000000 =f'_site=8&targetSite={OO00O00O0OOO0OOOO}_{timi_new()}'#line:507
            O0OOOO0O000O00O00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00O000000O00O0O0 .token ,'timestamp':timi_new (),'sign':sign (OOOO000O0O0000000 ),'signstring':OOOO000O0O0000000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:523
            OOO00O0OOO0O00000 ={"site":int (8 ),"targetSite":int (OO00O00O0OOO0OOOO )}#line:524
            requests .request ('post',f'{host}/game/crops/move',headers =O0OOOO0O000O00O00 ,json =OOO00O0OOO0O00000 )#line:525
            while True :#line:526
                OOO0O000OOO0O0OOO =f'__{timi_new()}'#line:527
                OOO0OOO0O0OO000OO ={'source':'scsc','authorization':O00O000000O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000OOO0O0OOO ),'signstring':OOO0O000OOO0O0OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:537
                OOO000OO0O0O0O0OO =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OOO0O0OO000OO ).json ()#line:538
                if 'status'in OOO000OO0O0O0O0OO :#line:540
                    if OOO000OO0O0O0O0OO ['status']==200 :#line:541
                        O0O0OO00O00O0OOO0 =OOO000OO0O0O0O0OO ['data']['cropList']#line:542
                        OO00O0OO0OO0O0O00 =OOO000OO0O0O0O0OO ['data']['gameCoreDataDBid']#line:543
                        O0000OO0O0OOO00O0 =float (OOO000OO0O0O0O0OO ['data']['silver'])/1000000000000 #line:544
                        O0O000OO00OOOOOOO =0 #line:549
                        for OO0O0O000OO0O0O0O in O0O0OO00O00O0OOO0 :#line:550
                            if not OO0O0O000OO0O0O0O :#line:551
                                O000OO00O00O0O0OO =f'_crop_id={OO00O0OO0OO0O0O00}&site={O0O000OO00OOOOOOO}_{O00O000000O00O0O0.time}'#line:552
                                OO0O0O000000O00O0 ={'source':'scsc','authorization':O00O000000O00O0O0 .token ,'timestamp':O00O000000O00O0O0 .time ,'sign':sign (O000OO00O00O0O0OO ),'signstring':O000OO00O00O0O0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:562
                                OOOO00OO00O00OO0O ={"site":O0O000OO00OOOOOOO ,"crop_id":OO00O0OO0OO0O0O00 }#line:563
                                OOOO0000OO000O0OO =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O0O000000O00O0 ,data =OOOO00OO00O00OO0O ).json ()#line:564
                                time .sleep (random .randint (1 ,3 )/10 )#line:566
                                if 'status'in OOOO0000OO000O0OO :#line:567
                                    if OOOO0000OO000O0OO ['status']==200 :#line:568
                                        if OOOO0000OO000O0OO ['message']=='种子数量不足':#line:569
                                            OO0OO0O000000OOOO =O00O000000O00O0O0 .level_new ()#line:570
                                            print (f'【种植合成】:{OOOO0000OO000O0OO["message"]}')#line:571
                                            if not O00O000000O00O0O0 .user_ad ():#line:572
                                                return False #line:573
                                    if OOOO0000OO000O0OO ['status']==500 :#line:574
                                        print (f'【种植合成】:{OOOO0000OO000O0OO["message"]}')#line:575
                                        return False #line:576
                            O0O000OO00OOOOOOO +=1 #line:577
                        O000O00OOO00OOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OOO0O0OO000OO ).json ()#line:578
                        OOO00OOOOO0OO00OO =O000O00OOO00OOOO0 ['data']['cropList']#line:579
                        O0O00O0O000O00OOO =False #line:580
                        for OO0O0O000OO0O0O0O in range (12 ):#line:581
                            id =OOO00OOOOO0OO00OO [OO0O0O000OO0O0O0O ]['level']#line:582
                            if float (OO0OO0O000000OOOO )-float (id )>9 :#line:583
                                OO0OOOOOO0O0O00OO =f'_site={OO0O0O000OO0O0O0O}_{timi_new()}'#line:584
                                O000O000O0OOO0O0O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00O000000O00O0O0 .token ,'timestamp':timi_new (),'sign':sign (OO0OOOOOO0O0O00OO ),'signstring':OO0OOOOOO0O0O00OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:595
                                O00O00O0000000000 ={"site":OO0O0O000OO0O0O0O }#line:596
                                OOOO00OO00O0OO0O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000O000O0OOO0O0O ,data =O00O00O0000000000 ).json ()#line:598
                                if 'status'in OOOO00OO00O0OO0O0 :#line:599
                                    if OOOO00OO00O0OO0O0 ['status']==200 :#line:600
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:601
                            if id !=0 :#line:602
                                for OOOOOOO00O0O0000O in range (11 ):#line:603
                                    O00O0O00O0OOO0O0O =OOOOOOO00O0O0000O +1 #line:604
                                    g =OOO00OOOOO0OO00OO [O00O0O00O0OOO0O0O ]['level']#line:605
                                    if id ==g :#line:606
                                        O00000O00OO0O0000 =OOOOOOO00O0O0000O +2 #line:607
                                        if O00000O00OO0O0000 !=OO0O0O000OO0O0O0O +1 :#line:608
                                            OO0OO000O000O00O0 =OO0O0O000OO0O0O0O +1 #line:609
                                            time .sleep (random .randint (1 ,3 )/10 )#line:611
                                            OOOO000O0O0000000 =f'_site={OO0OO000O000O00O0 - 1}&targetSite={O00000O00OO0O0000 - 1}_{timi_new()}'#line:612
                                            O0OOOO0O000O00O00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00O000000O00O0O0 .token ,'timestamp':timi_new (),'sign':sign (OOOO000O0O0000000 ),'signstring':OOOO000O0O0000000 ,'version':version ,'Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:628
                                            OO0OO0OO0OOOOOOO0 ={"site":int (OO0OO000O000O00O0 -1 ),"targetSite":int (O00000O00OO0O0000 -1 )}#line:629
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0OOOO0O000O00O00 ,json =OO0OO0OO0OOOOOOO0 )#line:630
                                            O0O00O0O000O00OOO =True #line:632
                                    if O0O00O0O000O00OOO :#line:633
                                        break #line:634
                                if O0O00O0O000O00OOO :#line:635
                                    break #line:636
        except :#line:637
            O00O000000O00O0O0 .synthetic ()#line:638
    def level_new (O000000000OOO0O0O ):#line:641
        try :#line:642
            OOO0OO0O00OO00O0O =f'__{timi_new()}'#line:643
            OO000OO0000O0O00O ={'source':'scsc','authorization':O000000000OOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O00OO00O0O ),'signstring':OOO0OO0O00OO00O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:653
            OO0OO00O00O000OO0 =requests .request ('get',f'{host}/user',headers =OO000OO0000O0O00O ).json ()#line:654
            if 'status'in OO0OO00O00O000OO0 :#line:655
                if OO0OO00O00O000OO0 ['status']==200 :#line:656
                    return float (OO0OO00O00O000OO0 ['data']['level'])#line:657
        except Exception as O0O000OO0O000O000 :#line:658
            print (O0O000OO0O000O000 )#line:659
    def propsraffle (OOOOO000OOOO0O0OO ):#line:662
        try :#line:663
            while True :#line:664
                O0O0O000OO0O000O0 =f'__{timi_new()}'#line:665
                O0O0O000O0OO000O0 ={'source':'scsc','authorization':OOOOO000OOOO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000OO0O000O0 ),'signstring':O0O0O000OO0O000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:675
                O00OOO0OO00000OO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O0O000O0OO000O0 ).json ()#line:676
                if 'status'in O00OOO0OO00000OO0 :#line:678
                    if O00OOO0OO00000OO0 ['status']==200 :#line:679
                        O000O0000OOOO00OO =O00OOO0OO00000OO0 ['data']['rows']#line:680
                        O00O0OOO0000O00OO =O00OOO0OO00000OO0 ['data']['vstate']#line:681
                        if O000O0000OOOO00OO ==5 or O000O0000OOOO00OO ==6 or O000O0000OOOO00OO ==7 :#line:682
                            OO00O000OOO0OOO00 =O00OOO0OO00000OO0 ['data']['silver']#line:683
                            print (f'【转盘抽奖】:获得种子:{OO00O000OOO0OOO00}')#line:684
                        if O000O0000OOOO00OO ==1 or O000O0000OOOO00OO ==2 or O000O0000OOOO00OO ==3 :#line:685
                            OO00OOO000000OO00 =O00OOO0OO00000OO0 ['data']['clover']#line:686
                            print (f'【转盘抽奖】:获得三叶草:{OO00OOO000000OO00}')#line:687
                        if O000O0000OOOO00OO ==4 or O000O0000OOOO00OO ==8 :#line:688
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:689
                        if O000O0000OOOO00OO =='抽奖次数已用完':#line:693
                            break #line:726
                time .sleep (random .randint (8 ,15 )/10 )#line:727
        except Exception as O0000OO0OO00OOOO0 :#line:728
            print (O0000OO0OO00OOOO0 )#line:729
    def friends_invitation (O00O00O00O00O000O ):#line:732
        try :#line:733
            OO00OOO00O0OO0O0O =f'__{timi_new()}'#line:734
            O0OOO0OOOOOO000OO ={'source':'scsc','authorization':O00O00O00O00O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO00O0OO0O0O ),'signstring':OO00OOO00O0OO0O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:744
            OOOO0O00O000O00OO =requests .request ('get',f'{host}/friends',headers =O0OOO0OOOOOO000OO ).json ()#line:745
            if 'status'in OOOO0O00O000O00OO :#line:746
                if OOOO0O00O000O00OO ['status']==200 :#line:747
                    OOOOO0O0OOOOOOOOO =OOOO0O00O000O00OO ['data']['myInviteter']#line:748
                    if OOOOO0O0OOOOOOOOO :#line:749
                        OO000O0OO0O0OO0OO =OOOOO0O0OOOOOOOOO ['user']['nickname']#line:750
                        O00O0O00O000OO0OO =O00O00O00O00O000O .certification ()#line:751
                        print (f'【查邀请人】:我的邀请人:{OO000O0OO0O0OO0OO}丨实名:{O00O0O00O000OO0OO}')#line:752
                    else :#line:753
                        if O00O00O00O00O000O .innerId !='0':#line:754
                            O00O00O00O00O000O .invitation ()#line:755
        except Exception as OOOOOO0OOOOOO0O0O :#line:756
            print (OOOOOO0OOOOOO0O0O )#line:757
    def add_clover (O000OO0OO00OO0OOO ):#line:760
        global golden_seed #line:761
        try :#line:762
            OOOO00O00OOO0O00O =f'__{timi_new()}'#line:763
            OO0000OO00OO0O00O ={'source':'scsc','authorization':O000OO0OO00OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O00OOO0O00O ),'signstring':OOOO00O00OOO0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:773
            OOO0O000000OOO000 =requests .request ('get',f'{host}/assets/clovers',headers =OO0000OO00OO0O00O ).json ()#line:774
            if 'status'in OOO0O000000OOO000 :#line:776
                if OOO0O000000OOO000 ['status']==200 :#line:777
                    OO00O0OOOO0OO0OO0 =OOO0O000000OOO000 ['data']['clover']#line:778
                    OO0O0O0O0O00OO0OO =OOO0O000000OOO000 ['data']['used_clover']#line:779
                    O000O000OO0O0OOO0 =float (OO00O0OOOO0OO0OO0 )-float (OO0O0O0O0O00OO0OO )#line:780
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO0O0O0O0O00OO0OO}')#line:781
                    if O000OO0OO00OO0OOO .certification ()!='未实名':#line:782
                        if O000O000OO0O0OOO0 >1 :#line:783
                            OOOO00O00OOO0O00O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O000O000OO0O0OOO0)}_{timi_new()}'#line:784
                            OOOO0O0O0OO00O0OO ={'source':'scsc','authorization':O000OO0OO00OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O00OOO0O00O ),'signstring':OOOO00O00OOO0O00O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
                            O00OOOO0OOOOO00O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O000O000OO0O0OOO0 )}#line:795
                            OO0OOO0OO000OO00O =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOO0O0O0OO00O0OO ,data =O00OOOO0OOOOO00O0 ).json ()#line:796
                            if 'status'in OO0OOO0OO000OO00O :#line:798
                                if OO0OOO0OO000OO00O ['status']==200 :#line:799
                                    print (f'【参与抽奖】:添加☘️:{OO0OOO0OO000OO00O["data"]}丨数量:{O000O000OO0O0OOO0}')#line:800
                                if OO0OOO0OO000OO00O ['status']==500 :#line:801
                                    print (f'【参与抽奖】:添加☘️:{OO0OOO0OO000OO00O["message"]}')#line:802
            O0OOO0O0O0O0O0000 =requests .request ('get',f'{host}/lottery',headers =OO0000OO00OO0O00O ).json ()#line:803
            OO0000O000O00O00O =O000OO0OO00OO0OOO .winning_rewards ()#line:805
            if 'status'in O0OOO0O0O0O0O0000 :#line:806
                if O0OOO0O0O0O0O0000 ['status']==200 :#line:807
                    O0O00O0OO000OOOOO =O0OOO0O0O0O0O0000 ['data'][0 ]['day_get_gold_quantity']#line:808
                    golden_seed +=float (O0O00O0OO000OOOOO )#line:809
                    O0OOOO0OO00OOOOOO =O0OOO0O0O0O0O0000 ['data'][1 ]['value']#line:810
                    O00O0OOO0O0O00OO0 =O0OOO0O0O0O0O0000 ['data'][0 ]['join_number']#line:811
                    O0O000OO0OOOO00OO =int (float (O0OOO0O0O0O0O0000 ['data'][0 ]['totalValue']))#line:812
                    O0OO0O0OOO0O00O0O =float (O0OOOO0OO00OOOOOO /O0O000OO0OOOO00OO )*10000 #line:813
                    OO000OO0O0O00OOOO =O0O000OO0OOOO00OO /O00O0OOO0O0O00OO0 #line:814
                    print (f'【参与抽奖】:预计每天中{str(O0O00O0OO000OOOOO)[:6]}颗金种子丨好友收益:{str(OO0000O000O00O00O)[:6]}')#line:815
                    print (f'【抽奖统计】:每1万☘️中{str(O0OO0O0OOO0O00O0O)[:6]}颗金种子丨☘️人均:{str(OO000OO0O0O00OOOO)[:7]}️')#line:816
        except Exception as OOO0OO0000OOO0OOO :#line:817
            print (OOO0OO0000OOO0OOO )#line:818
    def energy (O0O00O00OOO0OOOO0 ):#line:822
        try :#line:823
            while True :#line:824
                O0O00OO0O0OO00OO0 =f'__{timi_new()}'#line:825
                O00O0000OO0000OOO ={'source':'scsc','authorization':O0O00O00OOO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0O0OO00OO0 ),'signstring':O0O00OO0O0OO00OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:835
                O00OO0O0OO0OO0O0O =requests .request ('get',f'{host}/energy/general',headers =O00O0000OO0000OOO ).json ()#line:836
                if 'status'in O00OO0O0OO0OO0O0O :#line:838
                    if O00OO0O0OO0OO0O0O ['status']==200 :#line:839
                        O0O000O00O000O00O =O00OO0O0OO0OO0O0O ['data']['ordinary_water']#line:840
                        O0OOO0OO000O0O000 =O00OO0O0OO0OO0O0O ['data']['ordinary_fertilizer']#line:841
                        O0OOO00O0O0O0O0O0 =O00OO0O0OO0OO0O0O ['data']['videoStatus']#line:842
                        O0O0OO00O00OO00O0 =O00OO0O0OO0OO0O0O ['data']['waterVideoKey']#line:843
                        print (f'【我的营养】:肥料:{str(O0OOO0OO000O0O000).split(".")[0]}丨水滴:{str(O0O000O00O000O00O).split(".")[0]}')#line:844
                        if float (O0OOO0OO000O0O000 )<96 :#line:845
                            if O0OOO00O0O0O0O0O0 :#line:846
                                time .sleep (random .randint (160 ,180 )/10 )#line:847
                                O00OO0O00OOO00OO0 =99 -float (O0OOO0OO000O0O000 )#line:848
                                O0OO00OO0OO0OOOO0 ={"fertilizer":str (O00OO0O00OOO00OO0 ).split ('.')[0 ]}#line:849
                                O00OO000O0O0OOO00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00O0000OO0000OOO ).json ()#line:850
                                if 'status'in O00OO000O0O0OOO00 :#line:852
                                    if O00OO000O0O0OOO00 ['status']==200 :#line:853
                                        print (f'【购买肥料】:看广告获取肥料:{O00OO000O0O0OOO00["message"]}')#line:854
                                    if O00OO000O0O0OOO00 ['status']==500 :#line:855
                                        print (f'【购买肥料】:看广告获取肥料:{O00OO000O0O0OOO00["message"]}')#line:856
                                        break #line:857
                            if energy :#line:858
                                if float (O0OOO0OO000O0O000 )<float (fertilizer_quantity ):#line:859
                                    O0OOO00OOOOO00O00 =f'_fertilizer=10_{timi_new()}'#line:860
                                    OOOOOO0O000OOOO00 ={'source':'scsc','authorization':O0O00O00OOO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OOOOO00O00 ),'signstring':O0OOO00OOOOO00O00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:870
                                    O0O0OOO000O0OOOOO ={"fertilizer":"10"}#line:871
                                    O0OO0OOO000OO0000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOOOO0O000OOOO00 ,data =O0O0OOO000O0OOOOO ).json ()#line:872
                                    if 'status'in O0OO0OOO000OO0000 :#line:874
                                        if O0OO0OOO000OO0000 ['status']==200 :#line:875
                                            print (f'【购买肥料】:购买肥料:{O0OO0OOO000OO0000["message"]}丨数量:10')#line:876
                                        if O0OO0OOO000OO0000 ['status']==500 :#line:877
                                            print (f'【购买肥料】:购买肥料:{O0OO0OOO000OO0000["message"]}丨数量:10')#line:878
                                            OO0OOOO00O0000O0O =f'__{timi_new()}'#line:879
                                            OO000OO00O00OOOOO ={'source':'scsc','authorization':O0O00O00OOO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO00O0000O0O ),'signstring':OO0OOOO00O0000O0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:889
                                            O0O0OOO0O00OO0OOO =requests .request ('get',f'{host}/user',headers =OO000OO00O00OOOOO ).json ()#line:890
                                            if 'status'in O0O0OOO0O00OO0OOO :#line:891
                                                if O0O0OOO0O00OO0OOO ['status']==200 :#line:892
                                                    OO000OO000OOOOO00 =O0O0OOO0O00OO0OOO ['data']['inner_id']#line:893
                                                    give_gold (OO000OO000OOOOO00 )#line:894
                        if float (O0O000O00O000O00O )<880 :#line:896
                            if O0O0OO00O00OO00O0 :#line:897
                                time .sleep (random .randint (160 ,180 )/10 )#line:898
                                OOO0O00O0O000O00O =999 -float (O0O000O00O000O00O )#line:899
                                OOOOO0OOOO0OOO00O ={"water":str (OOO0O00O0O000O00O ).split ('.')[0 ]}#line:900
                                OO00O00OO0O0000OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00O0000OO0000OOO ).json ()#line:901
                                if 'status'in OO00O00OO0O0000OO :#line:903
                                    if OO00O00OO0O0000OO ['status']==200 :#line:904
                                        print (f'【购买水滴】:看广告获取水滴:{OO00O00OO0O0000OO["message"]}')#line:905
                                    if OO00O00OO0O0000OO ['status']==500 :#line:906
                                        print (f'【购买水滴】:看广告获取水滴:{OO00O00OO0O0000OO["message"]}')#line:907
                                        break #line:908
                            if energy :#line:909
                                if float (O0O000O00O000O00O )<float (wadverti_quantity ):#line:910
                                    OOOO0OO00O00OO0O0 =f'_water=100_{timi_new()}'#line:911
                                    OOOO0O000OO0O00O0 ={'source':'scsc','authorization':O0O00O00OOO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00O00OO0O0 ),'signstring':OOOO0OO00O00OO0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:921
                                    OOO000OO000O000O0 ={"water":"100"}#line:922
                                    O0O00OO00000O0000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOO0O000OO0O00O0 ,data =OOO000OO000O000O0 ).json ()#line:923
                                    if 'status'in O0O00OO00000O0000 :#line:925
                                        if O0O00OO00000O0000 ['status']==200 :#line:926
                                            print (f'【购买水滴】:购买水滴:{O0O00OO00000O0000["message"]}丨数量:100')#line:927
                                        if O0O00OO00000O0000 ['status']==500 :#line:928
                                            print (f'【购买水滴】:购买水滴:{O0O00OO00000O0000["message"]}丨数量:100')#line:929
                        break #line:933
        except Exception as OO000000O000OO00O :#line:935
            print (OO000000O000OO00O )#line:936
def bundled_def ():#line:938
    O000OO000OO0O00OO =['5570536','7750212','7911652','7911680','7805624']#line:939
    return O000OO000OO0O00OO [random .randint (0 ,len (O000OO000OO0O00OO )-1 )]#line:940
def version_of_the_validation ():#line:944
    return str ((82 -56 )/10 )#line:945
def gitee_validation ():#line:948
    try :#line:949
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:950
    except :#line:951
        sys .exit (0 )#line:952
def update_the_validation ():#line:956
    try :#line:957
        O0OOOO0OOOOOOO0O0 =gitee_validation ()#line:958
        if version_of_the_validation ()<O0OOOO0OOOOOOO0O0 ['CityEarth']['edition']:#line:959
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOO0OOOOOOO0O0["CityEarth"]["edition"]}   ❌')#line:960
            print (f'更新内容=>>{O0OOOO0OOOOOOO0O0["CityEarth"]["content"]}   🎉')#line:961
        else :#line:962
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOO0OOOOOOO0O0["CityEarth"]["edition"]}   ✅')#line:963
            print (f'更新内容=>> {O0OOOO0OOOOOOO0O0["CityEarth"]["content"]}   🎉')#line:964
    except Exception as O0OOOOO00OO00OO0O :#line:965
        print (O0OOOOO00OO00OO0O )#line:966
def os_qinglong ():#line:969
    if application in os .environ :#line:970
        OO0O0OO000O0OOOOO =os .environ [application ].split ('\n')#line:971
        if len (OO0O0OO000O0OOOOO )>0 :#line:972
            return OO0O0OO000O0OOOOO #line:973
        else :#line:974
            print (f"{application}变量未启用")#line:975
            print ('脚本退出')#line:976
            sys .exit (1 )#line:977
    else :#line:978
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:980
        return os_built ()#line:981
def os_built ():#line:984
    if token :#line:985
        OO0OO000000OOOO0O =token .split ('\n')#line:986
        if len (OO0OO000000OOOO0O )>0 :#line:987
            return OO0OO000000OOOO0O #line:988
    else :#line:989
        print (f"内置变量为空")#line:990
        print ('脚本结束')#line:991
        sys .exit (0 )#line:992
if __name__ =='__main__':#line:995
    start ()#line:996
