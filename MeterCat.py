# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import requests
    import random
except Exception as e:
    t = re.findall("d '(.*?)'", str(e))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
cron: 6 */6 * * *
new Env('拾米猫0.3')
@ 每天3块左右
@ app下载地址 https://ci-shimiyou.oss-cn-hangzhou.aliyuncs.com/apk/shimimao-1.apk
@ 抓取域名http://api.shimiyou.com:9080  jwt的值
@ 青龙变量 export smmtoken="token"     多号换行
@ 我的邀请码是5678568
@ 版本0.3
"""
application = 'smmtoken'  # 变量名
token = ''  # 调试token


#####################################################下面不要动#####################################################
pos1 =1 #line:1
pos2 =2 #line:2
lvl_new =0 #line:3
mobile =0 #line:4
user =0 #line:5
amount =0 #line:6
host ='http://api.shimiyou.com:9080'#line:7
git ='https://gitee.com'#line:8
def start ():#line:9
    try :#line:10
        if update_the_validation ():#line:11
            OO00OOO0OO0O0O00O =os_qinglong ()#line:12
            print (f"==========共找到{len(OO00OOO0OO0O0O00O)}个账号==========")#line:13
            for O0O0OOOO0O0O0OO00 in OO00OOO0OO0O0O00O :#line:14
                print (f"------------正在执行第{OO00OOO0OO0O0O00O.index(O0O0OOOO0O0O0OO00) + 1}个账号------------")#line:15
                OOO000OOOO0000O0O =MeterCat (O0O0OOOO0O0O0OO00 )#line:16
                if OOO000OOOO0000O0O .base_info ():#line:18
                    OOO000OOOO0000O0O .roll ()#line:22
                    OOO000OOOO0000O0O .withdraw ()#line:24
                    time .sleep (random .randint (3 ,5 ))#line:26
                else :#line:27
                    print ('token失效')#line:28
    except Exception as OOO00OO0O0OOOO000 :#line:29
        print (OOO00OO0O0OOOO000 )#line:30
class MeterCat :#line:33
    def __init__ (OOOOO00O000OO0000 ,O0O000O00OO0OO0O0 ):#line:35
        try :#line:36
            OOOOO00O000OO0000 .token =O0O000O00OO0OO0O0 #line:37
            OOOOO00O000OO0000 .headers ={'user-agent':'Dart/2.10 (dart:io)','accept-encoding':'gzip','content-length':'0','host':'api.shimiyou.com:9080',}#line:43
        except Exception as O0O00O0O000000000 :#line:44
            print ('变量格式错误')#line:45
    def base_info (OO00OOOO00OOOO00O ):#line:48
        global user #line:49
        try :#line:50
            O0000OOOOOO00OOO0 =requests .request ('get',f'{host}/lvxingapp/mine/getmyinfo?jwt={OO00OOOO00OOOO00O.token}',headers =OO00OOOO00OOOO00O .headers ).json ()#line:51
            if 'errcode'in O0000OOOOOO00OOO0 :#line:53
                user =str (O0000OOOOOO00OOO0 ['data']['user']['id'])#line:54
                OOO000OO00O00O000 =O0000OOOOOO00OOO0 ['data']['user']['nickname']#line:55
                OOOO00OOO00OO0000 =O0000OOOOOO00OOO0 ['data']['user']['fen']#line:56
                O00O00OO0OOO0OOOO =user [:2 ]+'***'+user [5 :]#line:57
                print (f'【账号信息】:ID:{O00O00OO0OOO0OOOO}丨昵称:{OOO000OO00O00O000}丨余额:{OOOO00OOO00OO0000}')#line:58
            return True #line:59
        except Exception as O0OO0OOOOO0O00OO0 :#line:60
            print (O0OO0OOOOO0O00OO0 )#line:61
    def withdraw (OO000OO0OOO0O0O0O ):#line:65
        global amount #line:66
        try :#line:67
            OOOOOOO00000O0000 =requests .request ('get',f'{host}/lvxingapp/mine/getmyinfo?jwt={OO000OO0OOO0O0O0O.token}',headers =OO000OO0OOO0O0O0O .headers ).json ()#line:68
            if 'errcode'in OOOOOOO00000O0000 :#line:69
                if not OOOOOOO00000O0000 ['data']['user']['zhifubao']:#line:70
                    print (f'【余额提现】:未实名退出提现')#line:71
                    return False #line:72
            while True :#line:73
                OO0OO0O0O0O000000 =requests .request ('get',f'{host}/lvxingapp/mine/getmyinfo?jwt={OO000OO0OOO0O0O0O.token}',headers =OO000OO0OOO0O0O0O .headers ).json ()#line:74
                if 'errcode'in OO0OO0O0O0O000000 :#line:75
                    O00O0000O00O00OOO =OO0OO0O0O0O000000 ['data']['user']['fen']#line:76
                    if O00O0000O00O00OOO <0.3 :#line:77
                        print ('【余额提现】:余额不足0.3退出提现')#line:78
                        break #line:79
                    if O00O0000O00O00OOO >20 :#line:80
                        amount =20 #line:81
                    elif O00O0000O00O00OOO >50 :#line:82
                        amount =50 #line:83
                    elif O00O0000O00O00OOO >100 :#line:84
                        amount =100 #line:85
                    if 20 >O00O0000O00O00OOO >0.3 :#line:86
                        amount =0.3 #line:87
                    O000O0OO00O000O00 =requests .request ('get',f'{host}/lvxingapp/mine/withdraw?amount={amount}&amount_name=&user_name=&jwt={OO000OO0OOO0O0O0O.token}',headers =OO000OO0OOO0O0O0O .headers ).json ()#line:88
                    if 'errcode'in O000O0OO00O000O00 :#line:90
                        if O000O0OO00O000O00 ['errcode']==0 :#line:91
                            print ('【余额提现】:0.3提现成功')#line:92
                        if O000O0OO00O000O00 ['errcode']==10045 :#line:93
                            print (f'【余额提现】:{O000O0OO00O000O00["errmsg"]}')#line:94
                            break #line:95
                        if O000O0OO00O000O00 ['errcode']==10012 :#line:96
                            print (f'【余额提现】:{O000O0OO00O000O00["errmsg"]}')#line:97
                            break #line:98
                        if O000O0OO00O000O00 ['errcode']==10068 :#line:99
                            print (f'【余额提现】:{O000O0OO00O000O00["errmsg"]}')#line:100
                            break #line:101
                time .sleep (2 )#line:102
        except Exception as O000O0O0OO0O0OO00 :#line:103
            print (O000O0O0OO0O0OO00 )#line:104
    def vid1eoCa2llB3ack4 (OOOO00OO000O00OOO ):#line:109
        try :#line:110
            OOO000O000O00O000 =requests .request ('get',f'{host}/lvxingapp/hall/reqrollquan?jwt={OOOO00OO000O00OOO.token}',headers =OOOO00OO000O00OOO .headers ).json ()#line:111
            if 'errcode'in OOO000O000O00O000 :#line:113
                if OOO000O000O00O000 ['errcode']==0 :#line:114
                    OOO0O000OOO0OO00O =OOO000O000O00O000 ['data']['quancount']#line:115
                    print (f'【转盘抽奖】:剩余获取转盘机会:{OOO0O000OOO0OO00O}次')#line:116
                    if float (OOO0O000OOO0OO00O )>0 :#line:117
                        OO000O0OO0O00OO00 =random .randint (320 ,350 )/10 #line:118
                        print (f'【转盘抽奖】:等待{OO000O0OO0O00OO00}秒获取转盘次数')#line:119
                        time .sleep (OO000O0OO0O00OO00 )#line:120
                        OOOOOO0OOO000000O =requests .request ('get',f'{host}/lvxingapp/config/vid1eoCa2llB3ack4?user_id={user}&reward_amount=1&reward_name=%E6%8A%BD%E5%A5%96%E6%AC%A1%E6%95%B0&jwt={OOOO00OO000O00OOO.token}',headers =OOOO00OO000O00OOO .headers ).json ()#line:121
                        if 'isValid'in OOOOOO0OOO000000O :#line:122
                            return False #line:123
                    else :#line:124
                        return False #line:125
            return True #line:126
        except Exception as O0O0O00OO0000OOOO :#line:127
            print (O0O0O00OO0000OOOO )#line:128
    def roll (OO00O000O000O0000 ):#line:132
        try :#line:133
            while True :#line:134
                OOO0O0O0OO0O0O0OO =requests .request ('get',f'{host}/lvxingapp/hall/roll?jwt={OO00O000O000O0000.token}',headers =OO00O000O000O0000 .headers ).json ()#line:135
                if 'errcode'in OOO0O0O0OO0O0O0OO :#line:137
                    if OOO0O0O0OO0O0O0OO ['errcode']==20007 :#line:138
                        print (f'【转盘抽奖】:{OOO0O0O0OO0O0O0OO["errmsg"]}')#line:139
                        if not OO00O000O000O0000 .vid1eoCa2llB3ack4 ():#line:140
                            break #line:141
                    if OOO0O0O0OO0O0O0OO ['errcode']==0 :#line:142
                        OOOOOOO00O0O0OOOO =OOO0O0O0OO0O0O0OO ['data']['tp']#line:143
                        if OOOOOOO00O0O0OOOO ==8 :#line:144
                            print ('【转盘抽奖】:获得现金')#line:145
                        else :#line:146
                            print ('【转盘抽奖】:获得金币')#line:147
                time .sleep (random .randint (1 ,3 ))#line:149
        except Exception as OO0O0000000OOO0OO :#line:150
            print (OO0O0000000OOO0OO )#line:151
    def movedog (O0OO0000O0OOOOO00 ):#line:154
        global pos1 ,pos1 ,lvl_new #line:155
        try :#line:156
            for O0000O0OO00OO00OO in range (2000 ):#line:157
                OOOO0O00OO000OO0O =random .randint (2 ,8 )#line:158
                O000O00OOOO0O000O =requests .request ('get',f'{host}/lvxingapp/hall/movedog?jwt={O0OO0000O0OOOOO00.token}&pos1=1&pos2={OOOO0O00OO000OO0O}',headers =O0OO0000O0OOOOO00 .headers ).json ()#line:159
                O0OO0000O0OOOOO00 .loadshop ()#line:161
                O0O00OO0000OO0OOO =O000O00OOOO0O000O ['data']['room']#line:162
                OOOOOO0O0000OO00O =False #line:163
                for O0000O0OO00OO00OO in range (12 ):#line:164
                    OOOOO00O0O0OO0O0O =O0O00OO0000OO0OOO [O0000O0OO00OO00OO ]['lvl']#line:165
                    if OOOOO00O0O0OO0O0O !=0 :#line:166
                        for O0O0O0O0OOOO0O00O in range (11 ):#line:167
                            O000O00OO0O0000O0 =O0O0O0O0OOOO0O00O +1 #line:168
                            OOO0OOOO0OOOOOOOO =O0O00OO0000OO0OOO [O000O00OO0O0000O0 ]['lvl']#line:169
                            if OOOOO00O0O0OO0O0O ==OOO0OOOO0OOOOOOOO :#line:170
                                O0OOO000O0OOOO000 =O0O0O0O0OOOO0O00O +2 #line:171
                                if O0OOO000O0OOOO000 ==O0000O0OO00OO00OO +1 :#line:172
                                    pass #line:173
                                else :#line:174
                                    time .sleep (random .randint (3 ,5 )/10 )#line:175
                                    OOOOO0000O0O00OO0 =O0000O0OO00OO00OO +1 #line:176
                                    O0OO0000O0OOOOO00 .hecheng (OOOOO0000O0O00OO0 ,O0OOO000O0OOOO000 )#line:177
                                    OOOOOO0O0000OO00O =True #line:179
                            if OOOOOO0O0000OO00O :#line:180
                                break #line:181
                        if OOOOOO0O0000OO00O :#line:182
                            break #line:183
        except Exception as OOO0O0OOOO0OO0OOO :#line:184
            print (OOO0O0OOOO0OO0OOO )#line:185
    def hecheng (O0OO0O0000O0000OO ,O000O000000O0000O ,OOO0OO000O00O00O0 ):#line:189
        try :#line:190
            O0000OO000O00000O =requests .request ('get',f'{host}/lvxingapp/hall/hecheng?jwt={O0OO0O0000O0000OO.token}&from={O000O000000O0000O}&to={OOO0OO000O00O00O0}',headers =O0OO0O0000O0000OO .headers ).json ()#line:191
            if 'errcode'in O0000OO000O00000O :#line:193
                if O0000OO000O00000O ['errcode']==0 :#line:194
                    print (f'{O000O000000O0000O}和{OOO0OO000O00O00O0}合成成功')#line:195
            else :#line:197
                print (O0000OO000O00000O )#line:198
        except Exception as OOO0OOOOO00O0O0O0 :#line:200
            print (OOO0OOOOO00O0O0O0 )#line:201
    def loadshop (O0OOOOOOO000O0OOO ):#line:204
        try :#line:205
            OOOO0OO0O0O0O0000 =requests .request ('get',f'{host}/lvxingapp/hall/loadshop?jwt={O0OOOOOOO000O0OOO.token}',headers =O0OOOOOOO000O0OOO .headers ).json ()#line:206
            if 'data'in OOOO0OO0O0O0O0000 :#line:208
                OOO0OO00OO0O000OO =list (reversed (OOOO0OO0O0O0O0000 ['data']['shoplist']))#line:209
                for OOO00OO0O00OO00OO in OOO0OO00OO0O000OO :#line:210
                    O0OO0OOOO000O0OO0 =OOO00OO0O00OO00OO ['price']#line:211
                    if float (O0OO0OOOO000O0OO0 )<float (OOOO0OO0O0O0O0000 ['data']['coin']):#line:212
                        O0OOOOOOO000O0OOO .buydog (OOO00OO0O00OO00OO ['lvl'])#line:214
                        break #line:215
        except Exception as OOO0O0OO0OOOOO0O0 :#line:216
            print (OOO0O0OO0OOOOO0O0 )#line:217
    def buydog (O0O00OO000000000O ,OOOO0OO0O00OOOO00 ):#line:221
        try :#line:222
            OO0OOOOOO0OO0O00O =requests .request ('get',f'{host}/lvxingapp/hall/buydog?jwt={O0O00OO000000000O.token}&did={OOOO0OO0O00OOOO00}&t=2',headers =O0O00OO000000000O .headers ).json ()#line:223
            if 'errcode'in OO0OOOOOO0OO0O00O :#line:225
                if OO0OOOOOO0OO0O00O ['errcode']==0 :#line:226
                    OOOO0OO0O00OOOO00 =OO0OOOOOO0OO0O00O ['data']['did']#line:227
                    print (f'购买{OOOO0OO0O00OOOO00}级猫成功')#line:228
                if OO0OOOOOO0OO0O00O ['errcode']==20001 :#line:229
                    print (OO0OOOOOO0OO0O00O ['errmsg'])#line:230
                if OO0OOOOOO0OO0O00O ['errcode']==20002 :#line:231
                    print (OO0OOOOOO0OO0O00O ['errmsg'])#line:232
                if OO0OOOOOO0OO0O00O ['errcode']==30006 :#line:233
                    print (OO0OOOOOO0OO0O00O ['errmsg'])#line:234
        except Exception as OO0O00OO0O0OO0O0O :#line:235
            print (OO0O00OO0O0OO0O0O )#line:236
def version_of_the_validation ():#line:239
    return str ((59 -56 )/10 )#line:240
def gitee_validation ():#line:242
    try :#line:243
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:244
    except Exception as OOO0OO000OOO00000 :#line:245
        sys .exit (0 )#line:246
def update_the_validation ():#line:249
    try :#line:250
        O00OOO00000O0OO00 =gitee_validation ()#line:251
        if version_of_the_validation ()<O00OOO00000O0OO00 ['MeterCat']['edition']:#line:252
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OOO00000O0OO00["MeterCat"]["edition"]}   ❌')#line:253
            print (f'更新内容=>>{O00OOO00000O0OO00["MeterCat"]["content"]}   👍')#line:254
        else :#line:255
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OOO00000O0OO00["MeterCat"]["edition"]}   ✅')#line:256
            print (f'更新内容=>> {O00OOO00000O0OO00["MeterCat"]["content"]}   👍')#line:257
            return True #line:258
    except Exception as OOO0O0O000OO00O0O :#line:259
        print (OOO0O0O000OO00O0O )#line:260
def os_qinglong ():#line:262
    try :#line:263
        if application in os .environ :#line:264
            OO00OO00OOOO000O0 =os .environ [application ].split ('\n')#line:265
            if len (OO00OO00OOOO000O0 )>0 :#line:266
                return OO00OO00OOOO000O0 #line:267
            else :#line:268
                print (f"{application}变量未启用")#line:269
                print ('脚本退出')#line:270
                sys .exit (1 )#line:271
        else :#line:272
            print (f"{application}变量为空\n尝试使用内置变量")#line:273
            return os_built ()#line:274
    except Exception as OO0O0OOO0OOOOO0O0 :#line:275
        print (OO0O0OOO0OOOOO0O0 )#line:276
def os_built ():#line:278
    try :#line:279
        if token :#line:280
            O00OO0O0O0O0OO00O =token .split ('\n')#line:281
            if len (O00OO0O0O0O0OO00O )>0 :#line:282
                return O00OO0O0O0O0OO00O #line:283
        else :#line:284
            print (f"内置变量为空")#line:285
            print ('脚本退出')#line:286
            sys .exit (0 )#line:287
    except Exception as O0OOOOO0O0O0OOO0O :#line:288
        print (O0OOOOO0O0O0OOO0O )#line:289
if __name__ =='__main__':#line:292
    start ()#line:293

