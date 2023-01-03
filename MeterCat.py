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
new Env('拾米猫0.2')
@ 每天3块左右
@ app下载地址 https://ci-shimiyou.oss-cn-hangzhou.aliyuncs.com/apk/shimimao-1.apk
@ 抓取域名http://api.shimiyou.com:9080  jwt的值
@ 青龙变量 export smmtoken="token"     多号换行
@ 我的邀请码是5678568
@ 版本0.2
"""
application = 'smmtoken'  # 变量名
token = ''  # 调试token


#####################################################下面不要动#####################################################
pos1 =1 #line:1
pos2 =2 #line:2
lvl_new =0 #line:3
mobile =0 #line:4
user =0 #line:5
host ='http://api.shimiyou.com:9080'#line:6
git ='https://gitee.com'#line:7
def start ():#line:8
    try :#line:9
        if update_the_validation ():#line:10
            OOOO0O000O000O0OO =os_qinglong ()#line:11
            print (f"==========共找到{len(OOOO0O000O000O0OO)}个账号==========")#line:12
            for O0OOOOOO0O000O000 in OOOO0O000O000O0OO :#line:13
                print (f"------------正在执行第{OOOO0O000O000O0OO.index(O0OOOOOO0O000O000) + 1}个账号------------")#line:14
                O00OOO00OOOO000OO =MeterCat (O0OOOOOO0O000O000 )#line:15
                if O00OOO00OOOO000OO .base_info ():#line:17
                    O00OOO00OOOO000OO .roll ()#line:21
                    O00OOO00OOOO000OO .withdraw ()#line:23
                    time .sleep (random .randint (3 ,5 ))#line:25
                else :#line:26
                    print ('token失效')#line:27
    except Exception as O0OO000O0O00O0O0O :#line:28
        print (O0OO000O0O00O0O0O )#line:29
class MeterCat :#line:32
    def __init__ (O0OO00OO000O00000 ,O0O000OOO0OOOO00O ):#line:34
        try :#line:35
            O0OO00OO000O00000 .token =O0O000OOO0OOOO00O #line:36
            O0OO00OO000O00000 .headers ={'user-agent':'Dart/2.10 (dart:io)','accept-encoding':'gzip','content-length':'0','host':'api.shimiyou.com:9080',}#line:42
        except Exception as OOO0O0O00OO00O000 :#line:43
            print ('变量格式错误')#line:44
    def base_info (OO0OOO00O0000OO0O ):#line:47
        global user #line:48
        try :#line:49
            OO0000OO0O0O000OO =requests .request ('get',f'{host}/lvxingapp/mine/getmyinfo?jwt={OO0OOO00O0000OO0O.token}',headers =OO0OOO00O0000OO0O .headers ).json ()#line:50
            if 'errcode'in OO0000OO0O0O000OO :#line:52
                user =str (OO0000OO0O0O000OO ['data']['user']['id'])#line:53
                OOO00OO0O0O0OOOOO =OO0000OO0O0O000OO ['data']['user']['nickname']#line:54
                OOOO000O00000O000 =OO0000OO0O0O000OO ['data']['user']['fen']#line:55
                O00O000O0OOO00OOO =user [:2 ]+'***'+user [5 :]#line:56
                print (f'【账号信息】:ID:{O00O000O0OOO00OOO}丨昵称:{OOO00OO0O0O0OOOOO}丨余额:{OOOO000O00000O000}')#line:57
            return True #line:59
        except Exception as O0OOOOO00OOO0O00O :#line:60
            print (O0OOOOO00OOO0O00O )#line:61
    def withdraw (OO00O0O0OOO0O00O0 ):#line:65
        try :#line:66
            OO0O000O0O000O00O =requests .request ('get',f'{host}/lvxingapp/mine/getmyinfo?jwt={OO00O0O0OOO0O00O0.token}',headers =OO00O0O0OOO0O00O0 .headers ).json ()#line:67
            if 'errcode'in OO0O000O0O000O00O :#line:68
                if not OO0O000O0O000O00O ['data']['user']['zhifubao']:#line:69
                    print (f'【余额提现】:未实名退出提现')#line:70
                    return False #line:71
            while True :#line:72
                OO000O0O0O0000000 =requests .request ('get',f'{host}/lvxingapp/mine/getmyinfo?jwt={OO00O0O0OOO0O00O0.token}',headers =OO00O0O0OOO0O00O0 .headers ).json ()#line:73
                if 'errcode'in OO000O0O0O0000000 :#line:74
                    OOOOO0O0O000O0OO0 =OO000O0O0O0000000 ['data']['user']['fen']#line:75
                    if 20 >OOOOO0O0O000O0OO0 >0.3 :#line:76
                        O0O0O0000O00O000O =requests .request ('get',f'{host}/lvxingapp/mine/withdraw?amount=0.3&amount_name=&user_name=&jwt={OO00O0O0OOO0O00O0.token}',headers =OO00O0O0OOO0O00O0 .headers ).json ()#line:77
                        if 'errcode'in O0O0O0000O00O000O :#line:79
                            if O0O0O0000O00O000O ['errcode']==0 :#line:80
                                print ('【余额提现】:0.3提现成功')#line:81
                            if O0O0O0000O00O000O ['errcode']==10045 :#line:82
                                print (f'【余额提现】:{O0O0O0000O00O000O["errmsg"]}')#line:83
                                break #line:84
                            if O0O0O0000O00O000O ['errcode']==10012 :#line:85
                                print (f'【余额提现】:{O0O0O0000O00O000O["errmsg"]}')#line:86
                                break #line:87
                    else :#line:88
                        print ('【余额提现】:余额不足0.3退出提现')#line:89
                        break #line:90
                    if OOOOO0O0O000O0OO0 >20 :#line:91
                        O0O0O0000O00O000O =requests .request ('get',f'{host}/lvxingapp/mine/withdraw?amount=20&amount_name=&user_name=&jwt={OO00O0O0OOO0O00O0.token}',headers =OO00O0O0OOO0O00O0 .headers ).json ()#line:92
                        if 'errcode'in O0O0O0000O00O000O :#line:94
                            if O0O0O0000O00O000O ['errcode']==0 :#line:95
                                print ('【余额提现】:20提现成功')#line:96
                            if O0O0O0000O00O000O ['errcode']==10045 :#line:97
                                print (f'【余额提现】:{O0O0O0000O00O000O["errmsg"]}')#line:98
                                break #line:99
                            if O0O0O0000O00O000O ['errcode']==10012 :#line:100
                                print (f'【余额提现】:{O0O0O0000O00O000O["errmsg"]}')#line:101
                                break #line:102
                time .sleep (2 )#line:103
        except Exception as OO0OO00000000000O :#line:104
            print (OO0OO00000000000O )#line:105
    def vid1eoCa2llB3ack4 (OO0O0O0O0000O0OOO ):#line:110
        try :#line:111
            O00O00OOOO0000000 =requests .request ('get',f'{host}/lvxingapp/hall/reqrollquan?jwt={OO0O0O0O0000O0OOO.token}',headers =OO0O0O0O0000O0OOO .headers ).json ()#line:112
            if 'errcode'in O00O00OOOO0000000 :#line:114
                if O00O00OOOO0000000 ['errcode']==0 :#line:115
                    O00O0O0O0O00O00O0 =O00O00OOOO0000000 ['data']['quancount']#line:116
                    print (f'【转盘抽奖】:剩余获取转盘机会:{O00O0O0O0O00O00O0}次')#line:117
                    if float (O00O0O0O0O00O00O0 )>0 :#line:118
                        OOO0OO0OO00O0OOOO =random .randint (310 ,350 )/10 #line:119
                        print (f'【转盘抽奖】:等待{OOO0OO0OO00O0OOOO}秒获取转盘次数')#line:120
                        time .sleep (OOO0OO0OO00O0OOOO )#line:121
                        O0O0O000OO0O00OO0 =requests .request ('get',f'{host}/lvxingapp/config/vid1eoCa2llB3ack4?user_id={user}&reward_amount=1&reward_name=%E6%8A%BD%E5%A5%96%E6%AC%A1%E6%95%B0&jwt={OO0O0O0O0000O0OOO.token}',headers =OO0O0O0O0000O0OOO .headers ).json ()#line:122
                        if 'isValid'in O0O0O000OO0O00OO0 :#line:123
                            return False #line:124
                    else :#line:125
                        return False #line:126
            return True #line:127
        except Exception as OOO0O0OOOO000O0OO :#line:128
            print (OOO0O0OOOO000O0OO )#line:129
    def roll (OOOO0000O0O000000 ):#line:133
        try :#line:134
            while True :#line:135
                O00O0O00O00O0OOO0 =requests .request ('get',f'{host}/lvxingapp/hall/roll?jwt={OOOO0000O0O000000.token}',headers =OOOO0000O0O000000 .headers ).json ()#line:136
                if 'errcode'in O00O0O00O00O0OOO0 :#line:138
                    if O00O0O00O00O0OOO0 ['errcode']==20007 :#line:139
                        print (f'【转盘抽奖】:{O00O0O00O00O0OOO0["errmsg"]}')#line:140
                        if not OOOO0000O0O000000 .vid1eoCa2llB3ack4 ():#line:141
                            break #line:142
                    if O00O0O00O00O0OOO0 ['errcode']==0 :#line:143
                        O0OOOOO0OO0O0O0O0 =O00O0O00O00O0OOO0 ['data']['tp']#line:144
                        if O0OOOOO0OO0O0O0O0 ==8 :#line:145
                            print ('【转盘抽奖】:获得现金')#line:146
                        else :#line:147
                            print ('【转盘抽奖】:获得金币')#line:148
                time .sleep (random .randint (1 ,3 ))#line:150
        except Exception as O00O00OO0000OOO00 :#line:151
            print (O00O00OO0000OOO00 )#line:152
    def movedog (O00O0OOO00OO0O0OO ):#line:155
        global pos1 ,pos1 ,lvl_new #line:156
        try :#line:157
            for O000OO00O00O0OOOO in range (2000 ):#line:158
                O0O0O000O000O00O0 =random .randint (2 ,8 )#line:159
                OOOOO000OOOOOOOOO =requests .request ('get',f'{host}/lvxingapp/hall/movedog?jwt={O00O0OOO00OO0O0OO.token}&pos1=1&pos2={O0O0O000O000O00O0}',headers =O00O0OOO00OO0O0OO .headers ).json ()#line:160
                O00O0OOO00OO0O0OO .loadshop ()#line:162
                O0OO00O0OOO0OOO0O =OOOOO000OOOOOOOOO ['data']['room']#line:163
                O0000O0O0OO0O00O0 =False #line:164
                for O000OO00O00O0OOOO in range (12 ):#line:165
                    O0OOOO0OOO0O00OO0 =O0OO00O0OOO0OOO0O [O000OO00O00O0OOOO ]['lvl']#line:166
                    if O0OOOO0OOO0O00OO0 !=0 :#line:167
                        for O00OO0OO0O0OOOOOO in range (11 ):#line:168
                            OO0O000O0O0O00OO0 =O00OO0OO0O0OOOOOO +1 #line:169
                            O0OO00O00OOO0O000 =O0OO00O0OOO0OOO0O [OO0O000O0O0O00OO0 ]['lvl']#line:170
                            if O0OOOO0OOO0O00OO0 ==O0OO00O00OOO0O000 :#line:171
                                OO000OOOOOOO00OO0 =O00OO0OO0O0OOOOOO +2 #line:172
                                if OO000OOOOOOO00OO0 ==O000OO00O00O0OOOO +1 :#line:173
                                    pass #line:174
                                else :#line:175
                                    time .sleep (random .randint (3 ,5 )/10 )#line:176
                                    O0OOO0000O0O0OOOO =O000OO00O00O0OOOO +1 #line:177
                                    O00O0OOO00OO0O0OO .hecheng (O0OOO0000O0O0OOOO ,OO000OOOOOOO00OO0 )#line:178
                                    O0000O0O0OO0O00O0 =True #line:180
                            if O0000O0O0OO0O00O0 :#line:181
                                break #line:182
                        if O0000O0O0OO0O00O0 :#line:183
                            break #line:184
        except Exception as OOO00O00O000O0O00 :#line:185
            print (OOO00O00O000O0O00 )#line:186
    def hecheng (O000000O00OO00OO0 ,O0OOOO0OOO00OO0OO ,OOO00OO000OO000OO ):#line:192
        try :#line:193
            OO000OO000000OO00 =requests .request ('get',f'{host}/lvxingapp/hall/hecheng?jwt={O000000O00OO00OO0.token}&from={O0OOOO0OOO00OO0OO}&to={OOO00OO000OO000OO}',headers =O000000O00OO00OO0 .headers ).json ()#line:194
            if 'errcode'in OO000OO000000OO00 :#line:196
                if OO000OO000000OO00 ['errcode']==0 :#line:197
                    print (f'{O0OOOO0OOO00OO0OO}和{OOO00OO000OO000OO}合成成功')#line:198
            else :#line:200
                print (OO000OO000000OO00 )#line:201
        except Exception as O0O00O00OOO0O0000 :#line:203
            print (O0O00O00OOO0O0000 )#line:204
    def loadshop (O0OOOO0O0O0O0O00O ):#line:207
        try :#line:208
            O00OOOO0O00O0O00O =requests .request ('get',f'{host}/lvxingapp/hall/loadshop?jwt={O0OOOO0O0O0O0O00O.token}',headers =O0OOOO0O0O0O0O00O .headers ).json ()#line:209
            if 'data'in O00OOOO0O00O0O00O :#line:211
                OOOO000O0OO000OO0 =list (reversed (O00OOOO0O00O0O00O ['data']['shoplist']))#line:212
                for OOO0O000000O0000O in OOOO000O0OO000OO0 :#line:213
                    OO0OOO0000OOO0OO0 =OOO0O000000O0000O ['price']#line:214
                    if float (OO0OOO0000OOO0OO0 )<float (O00OOOO0O00O0O00O ['data']['coin']):#line:215
                        O0OOOO0O0O0O0O00O .buydog (OOO0O000000O0000O ['lvl'])#line:217
                        break #line:218
        except Exception as O00OOO000OO0O0OO0 :#line:219
            print (O00OOO000OO0O0OO0 )#line:220
    def buydog (O0OO0O0000O0OO0O0 ,O00OO0O000OO00O00 ):#line:224
        try :#line:225
            OO0O000O000O0OO0O =requests .request ('get',f'{host}/lvxingapp/hall/buydog?jwt={O0OO0O0000O0OO0O0.token}&did={O00OO0O000OO00O00}&t=2',headers =O0OO0O0000O0OO0O0 .headers ).json ()#line:226
            if 'errcode'in OO0O000O000O0OO0O :#line:228
                if OO0O000O000O0OO0O ['errcode']==0 :#line:229
                    O00OO0O000OO00O00 =OO0O000O000O0OO0O ['data']['did']#line:230
                    print (f'购买{O00OO0O000OO00O00}级猫成功')#line:231
                if OO0O000O000O0OO0O ['errcode']==20001 :#line:232
                    print (OO0O000O000O0OO0O ['errmsg'])#line:233
                if OO0O000O000O0OO0O ['errcode']==20002 :#line:234
                    print (OO0O000O000O0OO0O ['errmsg'])#line:235
                if OO0O000O000O0OO0O ['errcode']==30006 :#line:236
                    print (OO0O000O000O0OO0O ['errmsg'])#line:237
        except Exception as O0O00OOO00OOO00O0 :#line:238
            print (O0O00OOO00OOO00O0 )#line:239
def version_of_the_validation ():#line:242
    return str ((58 -56 )/10 )#line:243
def gitee_validation ():#line:245
    try :#line:246
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:247
    except Exception as OO000OOO00O00OOOO :#line:248
        sys .exit (0 )#line:249
def update_the_validation ():#line:252
    try :#line:253
        O0OOOOOOOO00OO0O0 =gitee_validation ()#line:254
        if version_of_the_validation ()<O0OOOOOOOO00OO0O0 ['MeterCat']['edition']:#line:255
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOOOOOO00OO0O0["MeterCat"]["edition"]}   ❌')#line:256
            print (f'更新内容=>>{O0OOOOOOOO00OO0O0["MeterCat"]["content"]}   👍')#line:257
        else :#line:258
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOOOOOO00OO0O0["MeterCat"]["edition"]}   ✅')#line:259
            print (f'更新内容=>> {O0OOOOOOOO00OO0O0["MeterCat"]["content"]}   👍')#line:260
            return True #line:261
    except Exception as OO0O0OO00O00OO00O :#line:262
        print (OO0O0OO00O00OO00O )#line:263
def os_qinglong ():#line:265
    try :#line:266
        if application in os .environ :#line:267
            O0OO0OO0OOO00OO0O =os .environ [application ].split ('\n')#line:268
            if len (O0OO0OO0OOO00OO0O )>0 :#line:269
                return O0OO0OO0OOO00OO0O #line:270
            else :#line:271
                print (f"{application}变量未启用")#line:272
                print ('脚本退出')#line:273
                sys .exit (1 )#line:274
        else :#line:275
            print (f"{application}变量为空\n尝试使用内置变量")#line:276
            return os_built ()#line:277
    except Exception as O0O0OOOO0OOOO00O0 :#line:278
        print (O0O0OOOO0OOOO00O0 )#line:279
def os_built ():#line:281
    try :#line:282
        if token :#line:283
            O00O0OO00OO0O0O0O =token .split ('\n')#line:284
            if len (O00O0OO00OO0O0O0O )>0 :#line:285
                return O00O0OO00OO0O0O0O #line:286
        else :#line:287
            print (f"内置变量为空")#line:288
            print ('脚本退出')#line:289
            sys .exit (0 )#line:290
    except Exception as O0O000OO0O00OO0OO :#line:291
        print (O0O000OO0O00OO0OO )#line:292
if __name__ =='__main__':#line:295
    start ()#line:296
