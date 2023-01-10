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
@ 我的邀请码是    5678568
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
            O00OOOOO000O0O00O =os_qinglong ()#line:12
            print (f"==========共找到{len(O00OOOOO000O0O00O)}个账号==========")#line:13
            for O000OO0O00O0O0000 in O00OOOOO000O0O00O :#line:14
                print (f"------------正在执行第{O00OOOOO000O0O00O.index(O000OO0O00O0O0000) + 1}个账号------------")#line:15
                O00OOO0O00O0O0OOO =MeterCat (O000OO0O00O0O0000 )#line:16
                if O00OOO0O00O0O0OOO .base_info ():#line:18
                    O00OOO0O00O0O0OOO .roll ()#line:22
                    O00OOO0O00O0O0OOO .withdraw ()#line:24
                    time .sleep (random .randint (3 ,5 ))#line:26
                else :#line:27
                    print (f'第{O00OOOOO000O0O00O.index(O000OO0O00O0O0000) + 1}个账号token失效')#line:28
    except Exception as O00OOOO0OOOOO0O0O :#line:29
        print (O00OOOO0OOOOO0O0O )#line:30
class MeterCat :#line:33
    def __init__ (O00O000OOOO00000O ,O00O000000O0OO000 ):#line:35
        try :#line:36
            O00O000OOOO00000O .token =O00O000000O0OO000 #line:37
            O00O000OOOO00000O .headers ={'user-agent':'Dart/2.10 (dart:io)','accept-encoding':'gzip','content-length':'0','host':'api.shimiyou.com:9080',}#line:43
        except Exception as OOOO00OO0O0O000OO :#line:44
            print ('变量格式错误')#line:45
    def base_info (OOOO0O00000OOO0OO ):#line:48
        global user #line:49
        try :#line:50
            OO00OOOOOOOOOOO0O =requests .request ('get',f'{host}/lvxingapp/mine/getmyinfo?jwt={OOOO0O00000OOO0OO.token}',headers =OOOO0O00000OOO0OO .headers ).json ()#line:51
            if 'errcode'in OO00OOOOOOOOOOO0O :#line:53
                if OO00OOOOOOOOOOO0O ['errcode']==2 :#line:54
                    print (f'【账号信息】：{OO00OOOOOOOOOOO0O["errmsg"]}')#line:55
                    return False #line:56
                if OO00OOOOOOOOOOO0O ['errcode']==0 :#line:57
                    user =str (OO00OOOOOOOOOOO0O ['data']['user']['id'])#line:58
                    O0O00OOO0O0OO00O0 =OO00OOOOOOOOOOO0O ['data']['user']['nickname']#line:59
                    O0OOOO0000O000OOO =OO00OOOOOOOOOOO0O ['data']['user']['fen']#line:60
                    OOOO0OOOOOOOO0000 =user [:2 ]+'***'+user [5 :]#line:61
                    print (f'【账号信息】:ID:{OOOO0OOOOOOOO0000}丨昵称:{O0O00OOO0O0OO00O0}丨余额:{O0OOOO0000O000OOO}')#line:62
            return True #line:63
        except Exception as O0OOOOOO00OOO0O0O :#line:64
            print (O0OOOOOO00OOO0O0O )#line:65
    def withdraw (O000O0OO0OO00OOOO ):#line:69
        global amount #line:70
        try :#line:71
            O0O000OOO0O0O00O0 =requests .request ('get',f'{host}/lvxingapp/mine/getmyinfo?jwt={O000O0OO0OO00OOOO.token}',headers =O000O0OO0OO00OOOO .headers ).json ()#line:72
            if 'errcode'in O0O000OOO0O0O00O0 :#line:73
                if not O0O000OOO0O0O00O0 ['data']['user']['zhifubao']:#line:74
                    print (f'【余额提现】:未实名退出提现')#line:75
                    return False #line:76
            while True :#line:77
                OO0OOO000O0O00O00 =requests .request ('get',f'{host}/lvxingapp/mine/getmyinfo?jwt={O000O0OO0OO00OOOO.token}',headers =O000O0OO0OO00OOOO .headers ).json ()#line:78
                if 'errcode'in OO0OOO000O0O00O00 :#line:79
                    O0000O00O00O0000O =OO0OOO000O0O00O00 ['data']['user']['fen']#line:80
                    if O0000O00O00O0000O <0.3 :#line:81
                        print ('【余额提现】:余额不足0.3退出提现')#line:82
                        break #line:83
                    if O0000O00O00O0000O >20 :#line:84
                        amount =20 #line:85
                    elif O0000O00O00O0000O >50 :#line:86
                        amount =50 #line:87
                    elif O0000O00O00O0000O >100 :#line:88
                        amount =100 #line:89
                    if 20 >O0000O00O00O0000O >0.3 :#line:90
                        amount =0.3 #line:91
                    OO0O000OO00000O00 =requests .request ('get',f'{host}/lvxingapp/mine/withdraw?amount={amount}&amount_name=&user_name=&jwt={O000O0OO0OO00OOOO.token}',headers =O000O0OO0OO00OOOO .headers ).json ()#line:92
                    if 'errcode'in OO0O000OO00000O00 :#line:94
                        if OO0O000OO00000O00 ['errcode']==0 :#line:95
                            print (f'【余额提现】:提现成功丨金额:{amount}')#line:96
                        if OO0O000OO00000O00 ['errcode']==10045 :#line:97
                            print (f'【余额提现】:{OO0O000OO00000O00["errmsg"]}')#line:98
                            break #line:99
                        if OO0O000OO00000O00 ['errcode']==10012 :#line:100
                            print (f'【余额提现】:{OO0O000OO00000O00["errmsg"]}')#line:101
                            break #line:102
                        if OO0O000OO00000O00 ['errcode']==10068 :#line:103
                            print (f'【余额提现】:{OO0O000OO00000O00["errmsg"]}')#line:104
                            break #line:105
                time .sleep (2 )#line:106
        except Exception as O0000OO0OOOOO000O :#line:107
            print (O0000OO0OOOOO000O )#line:108
    def vid1eoCa2llB3ack4 (OOOOO0OO0000OOO0O ):#line:113
        try :#line:114
            O00000O0OOOOOO00O =requests .request ('get',f'{host}/lvxingapp/hall/reqrollquan?jwt={OOOOO0OO0000OOO0O.token}',headers =OOOOO0OO0000OOO0O .headers ).json ()#line:115
            if 'errcode'in O00000O0OOOOOO00O :#line:117
                if O00000O0OOOOOO00O ['errcode']==0 :#line:118
                    OOOOO000O000000O0 =O00000O0OOOOOO00O ['data']['quancount']#line:119
                    print (f'【转盘抽奖】:剩余获取转盘机会:{OOOOO000O000000O0}次')#line:120
                    if float (OOOOO000O000000O0 )>0 :#line:121
                        O0OOO00OOOO00OO00 =random .randint (320 ,350 )/10 #line:122
                        print (f'【转盘抽奖】:等待{O0OOO00OOOO00OO00}秒获取转盘次数')#line:123
                        time .sleep (O0OOO00OOOO00OO00 )#line:124
                        O00OOO0O0000O0O0O =requests .request ('get',f'{host}/lvxingapp/config/vid1eoCa2llB3ack4?user_id={user}&reward_amount=1&reward_name=%E6%8A%BD%E5%A5%96%E6%AC%A1%E6%95%B0&jwt={OOOOO0OO0000OOO0O.token}',headers =OOOOO0OO0000OOO0O .headers ).json ()#line:125
                        if 'isValid'in O00OOO0O0000O0O0O :#line:126
                            return False #line:127
                    else :#line:128
                        return False #line:129
            return True #line:130
        except Exception as O0O0OOO0OOOOOOO00 :#line:131
            print (O0O0OOO0OOOOOOO00 )#line:132
    def roll (OOO0O0O0OO00O0O00 ):#line:136
        try :#line:137
            while True :#line:138
                OOO000OOOO000OOO0 =requests .request ('get',f'{host}/lvxingapp/hall/roll?jwt={OOO0O0O0OO00O0O00.token}',headers =OOO0O0O0OO00O0O00 .headers ).json ()#line:139
                if 'errcode'in OOO000OOOO000OOO0 :#line:141
                    if OOO000OOOO000OOO0 ['errcode']==20007 :#line:142
                        print (f'【转盘抽奖】:{OOO000OOOO000OOO0["errmsg"]}')#line:143
                        if not OOO0O0O0OO00O0O00 .vid1eoCa2llB3ack4 ():#line:144
                            break #line:145
                    if OOO000OOOO000OOO0 ['errcode']==0 :#line:146
                        OOO0000OO0O00000O =OOO000OOOO000OOO0 ['data']['tp']#line:147
                        if OOO0000OO0O00000O ==8 :#line:148
                            print ('【转盘抽奖】:获得现金')#line:149
                        else :#line:150
                            print ('【转盘抽奖】:获得金币')#line:151
                time .sleep (random .randint (1 ,3 ))#line:153
        except Exception as OO0O0OO0OO000O000 :#line:154
            print (OO0O0OO0OO000O000 )#line:155
    def movedog (OOOO0OO0O0OOOOO0O ):#line:158
        global pos1 ,pos1 ,lvl_new #line:159
        try :#line:160
            for O0OO00OO00O00O000 in range (2000 ):#line:161
                OOO00O0O0O0OO0O00 =random .randint (2 ,8 )#line:162
                OO0OO0OOOO0OO0OO0 =requests .request ('get',f'{host}/lvxingapp/hall/movedog?jwt={OOOO0OO0O0OOOOO0O.token}&pos1=1&pos2={OOO00O0O0O0OO0O00}',headers =OOOO0OO0O0OOOOO0O .headers ).json ()#line:163
                OOOO0OO0O0OOOOO0O .loadshop ()#line:165
                OO0O0000000000OO0 =OO0OO0OOOO0OO0OO0 ['data']['room']#line:166
                O000O0OO000000OOO =False #line:167
                for O0OO00OO00O00O000 in range (12 ):#line:168
                    O00000OO000O00OOO =OO0O0000000000OO0 [O0OO00OO00O00O000 ]['lvl']#line:169
                    if O00000OO000O00OOO !=0 :#line:170
                        for OOO0O0OOOO00OOOO0 in range (11 ):#line:171
                            OO0O0O0O0O00OO000 =OOO0O0OOOO00OOOO0 +1 #line:172
                            OO0O0OO0OOOO0O000 =OO0O0000000000OO0 [OO0O0O0O0O00OO000 ]['lvl']#line:173
                            if O00000OO000O00OOO ==OO0O0OO0OOOO0O000 :#line:174
                                O0OOO00OOOOO0OOO0 =OOO0O0OOOO00OOOO0 +2 #line:175
                                if O0OOO00OOOOO0OOO0 ==O0OO00OO00O00O000 +1 :#line:176
                                    pass #line:177
                                else :#line:178
                                    time .sleep (random .randint (3 ,5 )/10 )#line:179
                                    O0OOOO0OOOO00000O =O0OO00OO00O00O000 +1 #line:180
                                    OOOO0OO0O0OOOOO0O .hecheng (O0OOOO0OOOO00000O ,O0OOO00OOOOO0OOO0 )#line:181
                                    O000O0OO000000OOO =True #line:183
                            if O000O0OO000000OOO :#line:184
                                break #line:185
                        if O000O0OO000000OOO :#line:186
                            break #line:187
        except Exception as O00O0OO0OO0O000O0 :#line:188
            print (O00O0OO0OO0O000O0 )#line:189
    def hecheng (OO0O0O00O0OOOO000 ,OOO000OO0O00000O0 ,OO0O0000OO0O00OO0 ):#line:193
        try :#line:194
            OOOOO0OO000OO0O0O =requests .request ('get',f'{host}/lvxingapp/hall/hecheng?jwt={OO0O0O00O0OOOO000.token}&from={OOO000OO0O00000O0}&to={OO0O0000OO0O00OO0}',headers =OO0O0O00O0OOOO000 .headers ).json ()#line:195
            if 'errcode'in OOOOO0OO000OO0O0O :#line:197
                if OOOOO0OO000OO0O0O ['errcode']==0 :#line:198
                    print (f'{OOO000OO0O00000O0}和{OO0O0000OO0O00OO0}合成成功')#line:199
            else :#line:201
                print (OOOOO0OO000OO0O0O )#line:202
        except Exception as O00OO00O000000000 :#line:204
            print (O00OO00O000000000 )#line:205
    def loadshop (O0O0O0000OO00O000 ):#line:208
        try :#line:209
            OOO0O0000O0O00O00 =requests .request ('get',f'{host}/lvxingapp/hall/loadshop?jwt={O0O0O0000OO00O000.token}',headers =O0O0O0000OO00O000 .headers ).json ()#line:210
            if 'data'in OOO0O0000O0O00O00 :#line:212
                OO0O00OOOOOOO00OO =list (reversed (OOO0O0000O0O00O00 ['data']['shoplist']))#line:213
                for O0000O00O00OOO000 in OO0O00OOOOOOO00OO :#line:214
                    OOO00OO0OO0O0O00O =O0000O00O00OOO000 ['price']#line:215
                    if float (OOO00OO0OO0O0O00O )<float (OOO0O0000O0O00O00 ['data']['coin']):#line:216
                        O0O0O0000OO00O000 .buydog (O0000O00O00OOO000 ['lvl'])#line:218
                        break #line:219
        except Exception as OO0O00O0OOOO000O0 :#line:220
            print (OO0O00O0OOOO000O0 )#line:221
    def buydog (OOOOO0OOOO0O0OO0O ,OOO0O000OOO00OO00 ):#line:225
        try :#line:226
            OO0OO0O00O000OO00 =requests .request ('get',f'{host}/lvxingapp/hall/buydog?jwt={OOOOO0OOOO0O0OO0O.token}&did={OOO0O000OOO00OO00}&t=2',headers =OOOOO0OOOO0O0OO0O .headers ).json ()#line:227
            if 'errcode'in OO0OO0O00O000OO00 :#line:229
                if OO0OO0O00O000OO00 ['errcode']==0 :#line:230
                    OOO0O000OOO00OO00 =OO0OO0O00O000OO00 ['data']['did']#line:231
                    print (f'购买{OOO0O000OOO00OO00}级猫成功')#line:232
                if OO0OO0O00O000OO00 ['errcode']==20001 :#line:233
                    print (OO0OO0O00O000OO00 ['errmsg'])#line:234
                if OO0OO0O00O000OO00 ['errcode']==20002 :#line:235
                    print (OO0OO0O00O000OO00 ['errmsg'])#line:236
                if OO0OO0O00O000OO00 ['errcode']==30006 :#line:237
                    print (OO0OO0O00O000OO00 ['errmsg'])#line:238
        except Exception as O00O0OOO0O0OO00O0 :#line:239
            print (O00O0OOO0O0OO00O0 )#line:240
def version_of_the_validation ():#line:243
    return str ((59 -56 )/10 )#line:244
def gitee_validation ():#line:246
    try :#line:247
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:248
    except Exception as O0000OOOO000OO0OO :#line:249
        sys .exit (0 )#line:250
def update_the_validation ():#line:253
    try :#line:254
        O000O00O0O0OOO0OO =gitee_validation ()#line:255
        if version_of_the_validation ()<O000O00O0O0OOO0OO ['MeterCat']['edition']:#line:256
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000O00O0O0OOO0OO["MeterCat"]["edition"]}   ❌')#line:257
            print (f'更新内容=>>{O000O00O0O0OOO0OO["MeterCat"]["content"]}   👍')#line:258
        else :#line:259
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000O00O0O0OOO0OO["MeterCat"]["edition"]}   ✅')#line:260
            print (f'更新内容=>> {O000O00O0O0OOO0OO["MeterCat"]["content"]}   👍')#line:261
            return True #line:262
    except Exception as OO0OO00O00OO00OOO :#line:263
        print (OO0OO00O00OO00OOO )#line:264
def os_qinglong ():#line:266
    try :#line:267
        if application in os .environ :#line:268
            O0OO0000O000OO0OO =os .environ [application ].split ('\n')#line:269
            if len (O0OO0000O000OO0OO )>0 :#line:270
                return O0OO0000O000OO0OO #line:271
            else :#line:272
                print (f"{application}变量未启用")#line:273
                print ('脚本退出')#line:274
                sys .exit (1 )#line:275
        else :#line:276
            print (f"{application}变量为空\n尝试使用内置变量")#line:277
            return os_built ()#line:278
    except Exception as O00OOO000OO000OO0 :#line:279
        print (O00OOO000OO000OO0 )#line:280
def os_built ():#line:282
    try :#line:283
        if token :#line:284
            O00OO00OO0000O000 =token .split ('\n')#line:285
            if len (O00OO00OO0000O000 )>0 :#line:286
                return O00OO00OO0000O000 #line:287
        else :#line:288
            print (f"内置变量为空")#line:289
            print ('脚本退出')#line:290
            sys .exit (0 )#line:291
    except Exception as O0O0OOOOOOOO00OOO :#line:292
        print (O0O0OOOOOOOO00OOO )#line:293
if __name__ =='__main__':#line:296
    start ()#line:297
