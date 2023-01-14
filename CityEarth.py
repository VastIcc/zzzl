# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import requests
    import random
    import threading
except Exception as e:
    t = re.findall("d '(.*?)'", str(e))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
cron: 12 */6 * * *
new Env('生城世朝')
项目地址  微信打开  http://share.sc19319.com/scsc/1932634
apk下载地址     https://sc19319.oss-cn-hangzhou.aliyuncs.com/scsc/test/1.9.3.1.S1.apk
抓取  http://test.scsc.sc19319.com 的authorization值
青龙变量 export ce_token="authorization&绑定邀请码"   不绑定填 0   多号换行
我的邀请码是  1932634
版本  0.2
"""
application = 'ce_token'  # 变量名
token = ''


time_xx = random.randint(8, 12)          # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://test.scsc.sc19319.com'#line:2
def start ():#line:3
    try :#line:4
        update_the_validation ()#line:5
        OO0O0O00O00O00OOO =os_qinglong ()#line:6
        print (f"==========共找到{len(OO0O0O00O00O00OOO)}个账号==========")#line:7
        for O0OO000OO0000O000 in OO0O0O00O00O00OOO :#line:8
            print (f"------------正在执行第{OO0O0O00O00O00OOO.index(O0OO000OO0000O000) + 1}个账号------------")#line:9
            OO0OOO000OO0O0OOO =CityEarth (O0OO000OO0000O000 )#line:10
            if OO0OOO000OO0O0OOO .base_info ():#line:12
                OO0OOO000OO0O0OOO .friends_invitation ()#line:14
                OO0OOO000OO0O0OOO .add_clover ()#line:18
                OO0OOO000OO0O0OOO .energy ()#line:20
                OO0OOO000OO0O0OOO .game_map ()#line:22
                OO0OOO000OO0O0OOO .synthetic ()#line:24
            else :#line:26
                print ('token失效')#line:27
            time .sleep (time_xx )#line:29
    except Exception as OO000O00O00O0O0O0 :#line:30
        print (OO000O00O00O0O0O0 )#line:31
class CityEarth :#line:34
    def __init__ (OOO00OO0OO00000O0 ,O0OO000000O00O000 ):#line:36
        try :#line:37
            OOO00OO0OO00000O0 .token =O0OO000000O00O000 .split ('&')[0 ]#line:38
            OOO00OO0OO00000O0 .innerId =O0OO000000O00O000 .split ('&')[1 ]#line:39
            OOO00OO0OO00000O0 .headers ={'authorization':OOO00OO0OO00000O0 .token ,'Host':'test.scsc.sc19319.com'}#line:43
        except Exception as O000O00O00O000000 :#line:44
            print ('变量格式错误')#line:45
    def base_info (O0000O00OOOOOOO0O ):#line:48
        try :#line:49
            O0OOO000O0OO000OO =requests .request ('get',f'{host}/api/user',headers =O0000O00OOOOOOO0O .headers ).json ()#line:50
            if 'status'in O0OOO000O0OO000OO :#line:52
                if O0OOO000O0OO000OO ['status']==200 :#line:53
                    OO0OOO0O0OO00OO0O =O0OOO000O0OO000OO ['data']['nickname']#line:54
                    O0OO000O0OOO0OO0O =O0OOO000O0OO000OO ['data']['inner_id']#line:55
                    O00OOOO00OOOO00OO =O0OOO000O0OO000OO ['data']['assets']['gold']#line:56
                    O0O0OO0OOO0OOOO0O =O0OOO000O0OO000OO ['data']['level']#line:57
                    print (f'【账号信息】:昵称:{OO0OOO0O0OO00OO0O}丨ID:{str(O0OO000O0OOO0OO0O)[:3] + "**"+ str(O0OO000O0OOO0OO0O)[5:]}丨等级:{O0O0OO0OOO0OOOO0O}丨金种子:{str(O00OOOO00OOOO00OO).split(".")[0]}')#line:58
                if O0OOO000O0OO000OO ['status']==401 :#line:59
                    return False #line:60
            return True #line:61
        except Exception as OO000OO000O00O0OO :#line:62
            print (OO000OO000O00O0OO )#line:63
    def user_ad (O0OO00O0OO00000OO ):#line:66
        O0O0000O0OO0O0O0O =requests .request ('get',f'{host}/api/user/ad',headers =O0OO00O0OO00000OO .headers ).json ()#line:67
        if 'status'in O0O0000O0OO0O0O0O :#line:69
            if O0O0000O0OO0O0O0O ['status']==200 :#line:70
                OOO000O0000000OO0 =O0O0000O0OO0O0O0O ['data']['max_time']#line:71
                OO0OOO0OO0O000OO0 =O0O0000O0OO0O0O0O ['data']['watch_time']#line:72
                print (f'【获取种子】:获取种子机会剩余{OOO000O0000000OO0 - OO0OOO0OO0O000OO0}次')#line:73
                if OOO000O0000000OO0 -OO0OOO0OO0O000OO0 >0 :#line:74
                    time .sleep (random .randint (16 ,19 ))#line:75
                    O000O0000000OOO0O =requests .request ('post',f'{host}/api/game/watched-ad-forSilver',headers =O0OO00O0OO00000OO .headers ).json ()#line:76
                    if 'status'in O000O0000000OOO0O :#line:78
                        if O000O0000000OOO0O ['status']==200 :#line:79
                            OOOO0000OO00OOOO0 =O000O0000000OOO0O ['data']['silver']#line:80
                            print (f'【获取种子】:获得种子:{OOOO0000OO00OOOO0}')#line:81
                            return True #line:82
                        if O000O0000000OOO0O ['status']==500 :#line:83
                            O0OOOOO0OO00OOO0O =O000O0000000OOO0O ['message']#line:84
                            print (f'【获取种子】:{O0OOOOO0OO00OOO0O}')#line:85
                            return False #line:86
    def synthetic (OOOO0OOOO0O00O0OO ):#line:89
        global id ,g #line:90
        try :#line:91
            while True :#line:92
                OOO00OO0O0OOO0OO0 =requests .request ('get',f'{host}/api/game/getAllData',headers =OOOO0OOOO0O00O0OO .headers ).json ()#line:93
                if 'status'in OOO00OO0O0OOO0OO0 :#line:95
                    if OOO00OO0O0OOO0OO0 ['status']==200 :#line:96
                        O00O00OO000O0O000 =OOO00OO0O0OOO0OO0 ['data']['cropList']#line:97
                        O00O0O00OOO00O0O0 =OOO00OO0O0OOO0OO0 ['data']['gameCoreDataDBid']#line:98
                        O00OOO00000O00O00 =0 #line:99
                        for O000OOO0OOO0O0O00 in O00O00OO000O0O000 :#line:100
                            if not O000OOO0OOO0O0O00 :#line:101
                                OO0O0O00OOOO00O0O ={"site":O00OOO00000O00O00 ,"crop_id":O00O0O00OOO00O0O0 }#line:102
                                O00OO00OOOOOOO000 =requests .request ('post',f'{host}/api/game/crops/buy',headers =OOOO0OOOO0O00O0OO .headers ,data =OO0O0O00OOOO00O0O ).json ()#line:103
                                if 'status'in O00OO00OOOOOOO000 :#line:105
                                    if O00OO00OOOOOOO000 ['status']==200 :#line:106
                                        if O00OO00OOOOOOO000 ['message']=='种子数量不足':#line:107
                                            print (f'【购买合成】:{O00OO00OOOOOOO000["message"]}')#line:108
                                            if not OOOO0OOOO0O00O0OO .user_ad ():#line:109
                                                return False #line:110
                                        print (f'【购买合成】:购买农作物,位置{O00OOO00000O00O00}')#line:111
                                    if O00OO00OOOOOOO000 ['status']==500 :#line:112
                                        print (f'【购买合成】:{O00OO00OOOOOOO000["message"]}')#line:113
                                        return False #line:114
                                time .sleep (random .randint (3 ,5 )/10 )#line:115
                            O00OOO00000O00O00 +=1 #line:116
                        O0O0O0O0OOO000O00 =requests .request ('get',f'{host}/api/game/getAllData',headers =OOOO0OOOO0O00O0OO .headers ).json ()#line:117
                        OO0OOO0O0O0O00O00 =O0O0O0O0OOO000O00 ['data']['cropList']#line:118
                        OO000O00O0OOOO0O0 =False #line:119
                        for O000OOO0OOO0O0O00 in range (12 ):#line:120
                            id =OO0OOO0O0O0O00O00 [O000OOO0OOO0O0O00 ]['level']#line:121
                            if id !=0 :#line:122
                                for OOO00O0O0OO000000 in range (11 ):#line:123
                                    OOOOO0O00OOOOO000 =OOO00O0O0OO000000 +1 #line:124
                                    g =OO0OOO0O0O0O00O00 [OOOOO0O00OOOOO000 ]['level']#line:125
                                    if id ==g :#line:126
                                        OOO0OO00OO0OOO0O0 =OOO00O0O0OO000000 +2 #line:127
                                        if OOO0OO00OO0OOO0O0 ==O000OOO0OOO0O0O00 +1 :#line:128
                                            pass #line:129
                                        else :#line:130
                                            time .sleep (random .randint (3 ,5 )/10 )#line:131
                                            O0OOO0OO0OO000O0O =O000OOO0OOO0O0O00 +1 #line:132
                                            O0OOOO000OO0OO00O ={"site":O0OOO0OO0OO000O0O -1 ,"targetSite":OOO0OO00OO0OOO0O0 -1 }#line:134
                                            OO0O0O0000OO0O000 =requests .request ('post',f'{host}/api/game/crops/move',headers =OOOO0OOOO0O00O0OO .headers ,data =O0OOOO000OO0OO00O ).json ()#line:136
                                            if 'status'in OO0O0O0000OO0O000 :#line:138
                                                if OO0O0O0000OO0O000 ['status']==200 :#line:139
                                                    pass #line:140
                                            print ('【购买合成】:',O0OOO0OO0OO000O0O ,OOO0OO00OO0OOO0O0 ,'合成成功')#line:142
                                            OO000O00O0OOOO0O0 =True #line:143
                                    if OO000O00O0OOOO0O0 :#line:144
                                        break #line:145
                                if OO000O00O0OOOO0O0 :#line:146
                                    break #line:147
        except Exception as O0000OOOOO000OO00 :#line:148
            OOOO0OOOO0O00O0OO .synthetic ()#line:149
    def propsraffle (OO0000OOOOOO0OO00 ):#line:153
        try :#line:154
            while True :#line:155
                O000O0OO0OOO000OO =requests .request ('get',f'{host}/api/propsraffle/lucky',headers =OO0000OOOOOO0OO00 .headers ).json ()#line:156
                if 'status'in O000O0OO0OOO000OO :#line:158
                    if O000O0OO0OOO000OO ['status']==200 :#line:159
                        O00000000O00O0O0O =O000O0OO0OOO000OO ['data']['rows']#line:160
                        if O00000000O00O0O0O ==5 or O00000000O00O0O0O ==6 or O00000000O00O0O0O ==7 :#line:161
                            O00OO000OOO0O00OO =O000O0OO0OOO000OO ['data']['silver']#line:162
                            print (f'【转盘抽奖】:获得种子:{O00OO000OOO0O00OO}')#line:163
                        if O00000000O00O0O0O ==1 or O00000000O00O0O0O ==2 or O00000000O00O0O0O ==3 :#line:164
                            O00O0OOO0O0O00O00 =O000O0OO0OOO000OO ['data']['clover']#line:165
                            print (f'【转盘抽奖】:获得三叶草:{O00O0OOO0O0O00O00}')#line:166
                        if O00000000O00O0O0O ==4 or O00000000O00O0O0O ==8 :#line:167
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:168
                        if O00000000O00O0O0O =='抽奖次数已用完':#line:172
                            OO000O00OOO0O00O0 =random .randint (160 ,190 )/10 #line:173
                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{OO000O00OOO0O00O0}秒获取抽奖机会')#line:174
                            time .sleep (OO000O00OOO0O00O0 )#line:175
                            O0O00O0OOO0OOOOOO =requests .request ('get',f'{host}/api/propsraffle/lucky/adverti/restore',headers =OO0000OOOOOO0OO00 .headers ).json ()#line:176
                            if 'status'in O0O00O0OOO0OOOOOO :#line:178
                                if O0O00O0OOO0OOOOOO ['status']==200 :#line:179
                                    print (f'【转盘抽奖】:{O0O00O0OOO0OOOOOO["message"]}')#line:180
                                if O0O00O0OOO0OOOOOO ['status']==500 :#line:181
                                    print (f'【转盘抽奖】:{O0O00O0OOO0OOOOOO["message"]}')#line:182
                                    break #line:183
                            time .sleep (random .randint (10 ,15 )/10 )#line:184
                time .sleep (random .randint (8 ,15 )/10 )#line:185
        except Exception as O00OOO00O0O0000OO :#line:186
            print (O00OOO00O0O0000OO )#line:187
    def friends_invitation (O0OO00O0OO00OO00O ):#line:190
        try :#line:191
            OO0OO0OO0OOO0OOO0 =requests .request ('get','http://test.scsc.sc19319.com/api/friends',headers =O0OO00O0OO00OO00O .headers ).json ()#line:192
            if 'status'in OO0OO0OO0OOO0OOO0 :#line:193
                if OO0OO0OO0OOO0OOO0 ['status']==200 :#line:194
                    OOOO00O00OOOOO0O0 =OO0OO0OO0OOO0OOO0 ['data']['myInviteter']#line:195
                    if OOOO00O00OOOOO0O0 :#line:196
                        O0O000OO000O0O0O0 =OOOO00O00OOOOO0O0 ['user']['nickname']#line:197
                        print (f'【绑邀请码】:我的邀请人:{O0O000OO000O0O0O0}')#line:198
                    else :#line:199
                        if O0OO00O0OO00OO00O .innerId !='0':#line:200
                            print ('【绑邀请码】:绑定邀请码')#line:201
                            OOOOOO0O0O00O0000 ={"innerId":O0OO00O0OO00OO00O .innerId }#line:202
                            OO0OO0OO0OO0OOOO0 =requests .request ('post',f'{host}/api/friends/my-invitation',headers =O0OO00O0OO00OO00O .headers ,data =OOOOOO0O0O00O0000 ).json ()#line:203
                            print (OO0OO0OO0OO0OOOO0 )#line:204
                        else :#line:205
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:206
        except Exception as O00OO00O000000OO0 :#line:207
            print (O00OO00O000000OO0 )#line:208
    def add_clover (O00000OO0O0O00O0O ):#line:212
        try :#line:213
            OOO0000OO000OOOOO =requests .request ('get',f'{host}/api/assets/clovers',headers =O00000OO0O0O00O0O .headers ).json ()#line:214
            if 'status'in OOO0000OO000OOOOO :#line:216
                if OOO0000OO000OOOOO ['status']==200 :#line:217
                    OOOOOO00000O0000O =OOO0000OO000OOOOO ['data']['clover']#line:218
                    OOO0O00O000OO0000 =OOO0000OO000OOOOO ['data']['used_clover']#line:219
                    O00O0O00OOOOO0O00 =float (OOOOOO00000O0000O )-float (OOO0O00O000OO0000 )#line:220
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OOO0O00O000OO0000}')#line:221
                    if O00O0O00OOOOO0O00 >1 :#line:222
                        O00O000OO0O00OOOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":O00O0O00OOOOO0O00 }#line:223
                        OOOO0OO000OO0OO00 =requests .request ('post','http://test.scsc.sc19319.com/api/lottery/add-stake',headers =O00000OO0O0O00O0O .headers ,data =O00O000OO0O00OOOO ).json ()#line:225
                        if 'status'in OOOO0OO000OO0OO00 :#line:227
                            if OOOO0OO000OO0OO00 ['status']==200 :#line:228
                                print (f'【参与抽奖】:添加三叶草:{OOOO0OO000OO0OO00["data"]}丨数量:{O00O0O00OOOOO0O00}')#line:229
        except Exception as OO00O000000OOO00O :#line:230
            print (OO00O000000OOO00O )#line:231
    def energy (OO00O0OOO000O0O00 ):#line:234
        O0O00O00OOO00OOO0 =requests .request ('get',f'{host}/api/energy/general',headers =OO00O0OOO000O0O00 .headers ).json ()#line:235
        if 'status'in O0O00O00OOO00OOO0 :#line:237
            if O0O00O00OOO00OOO0 ['status']==200 :#line:238
                OO0OOO0OOOOOO0000 =O0O00O00OOO00OOO0 ['data']['ordinary_water_consumptions']#line:239
                if float (OO0OOO0OOOOOO0000 )<80 :#line:240
                    O0O0O0O00O0OOO0OO =99 -float (OO0OOO0OOOOOO0000 )#line:241
                    OO00OO0OO0O000OOO ={"fertilizer":str (O0O0O0O00O0OOO0OO ).split ('.')[0 ]}#line:242
                    O00O000OO00O00000 =requests .request ('post',f'{host}/api/energy/general/buy/fertilizer',headers =OO00O0OOO000O0O00 .headers ,data =OO00OO0OO0O000OOO ).json ()#line:243
                    if 'status'in O00O000OO00O00000 :#line:245
                        if O00O000OO00O00000 ['status']==200 :#line:246
                            print (f'【购买肥料】:{O00O000OO00O00000["message"]}')#line:247
                O0OO0000O0O0O000O =O0O00O00OOO00OOO0 ['data']['ordinary_water_consumptions']#line:248
                if float (O0OO0000O0O0O000O )<800 :#line:249
                    O0O00O0OOOOOOOOO0 =999 -float (O0OO0000O0O0O000O )#line:250
                    O0O0OO0O00O00O00O ={"water":str (O0O00O0OOOOOOOOO0 ).split ('.')[0 ]}#line:251
                    OO0O000O0OOOO0O00 =requests .request ('post',f'{host}/api/energy/general/buy/water',headers =OO00O0OOO000O0O00 .headers ,data =O0O0OO0O00O00O00O ).json ()#line:252
                    if 'status'in OO0O000O0OOOO0O00 :#line:253
                        if OO0O000O0OOOO0O00 ['status']==200 :#line:254
                            print (f'【购买水滴】:{OO0O000O0OOOO0O00["message"]}')#line:255
    def game_map (O0O00O0O00O0OO0O0 ):#line:259
        O0OO00O00O0O0OO00 =requests .request ('get',f'{host}/api/game/map',headers =O0O00O0O00O0OO0O0 .headers ).json ()#line:260
        OOOOOOO000000OO00 =0 #line:262
        if 'status'in O0OO00O00O0O0OO00 :#line:263
            if O0OO00O00O0O0OO00 ['status']==200 :#line:264
                O0O000OO0OO0O000O =O0OO00O00O0O0OO00 ['data']['list'][0 ]['crops']#line:265
                for OO0O0OO000OO00OOO in O0O000OO0OO0O000O :#line:267
                    O00OOOO0OOO00O00O =OO0O0OO000OO00OOO ['count']#line:269
                    if O00OOOO0OOO00O00O >0 :#line:270
                        OOOOOOO000000OO00 +=1 #line:272
                if OOOOOOO000000OO00 >8 :#line:274
                    print ('卖掉低级农作物')#line:275
                    O000O0000O00OO0O0 =O0O000OO0OO0O000O [0 ]['id']#line:276
                    O0000OOO0O0OO0OOO ={"crop_id":O000O0000O00OO0O0 ,"num":1 }#line:277
                    OOO000OOOO00OOOO0 =requests .request ('post',f'{host}/api/game/crops/sellForGold',headers =O0O00O0O00O0OO0O0 .headers ,data =O0000OOO0O0OO0OOO ).json ()#line:278
                    if 'status'in OOO000OOOO00OOOO0 :#line:280
                        if OOO000OOOO00OOOO0 ['status']==200 :#line:281
                            print ('卖出成功')#line:282
def version_of_the_validation ():#line:286
    return str ((58 -56 )/10 )#line:287
def gitee_validation ():#line:289
    try :#line:290
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:291
    except Exception as O0000OO0OOO00O0O0 :#line:292
        sys .exit (0 )#line:293
def update_the_validation ():#line:299
    try :#line:300
        O00O0O0O0O0O00OOO =gitee_validation ()#line:301
        if version_of_the_validation ()<O00O0O0O0O0O00OOO ['CityEarth']['edition']:#line:302
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0O0O0O0O00OOO["CityEarth"]["edition"]}   ❌')#line:303
            print (f'更新内容=>>{O00O0O0O0O0O00OOO["CityEarth"]["content"]}   👍')#line:304
        else :#line:305
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0O0O0O0O00OOO["CityEarth"]["edition"]}   ✅')#line:306
            print (f'更新内容=>> {O00O0O0O0O0O00OOO["CityEarth"]["content"]}   👍')#line:307
    except Exception as O0OOOOOO00OO0OO0O :#line:308
        print (O0OOOOOO00OO0OO0O )#line:309
def os_qinglong ():#line:312
    if application in os .environ :#line:313
        OOO0O000O000OOOOO =os .environ [application ].split ('\n')#line:314
        if len (OOO0O000O000OOOOO )>0 :#line:315
            return OOO0O000O000OOOOO #line:316
        else :#line:317
            print (f"{application}变量未启用")#line:318
            print ('脚本退出')#line:319
            sys .exit (1 )#line:320
    else :#line:321
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:322
        return os_built ()#line:323
def os_built ():#line:326
    if token :#line:327
        OOO0O0O00O000O0OO =token .split ('\n')#line:328
        if len (OOO0O0O00O000O0OO )>0 :#line:329
            return OOO0O0O00O000O0OO #line:330
    else :#line:331
        print (f"内置变量为空")#line:332
        print ('脚本结束')#line:333
        sys .exit (0 )#line:334
if __name__ =='__main__':#line:337
    start ()#line:338
