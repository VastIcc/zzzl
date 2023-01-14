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
版本  0.1
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
        O0OO00OOO000O00OO =os_qinglong ()#line:6
        print (f"==========共找到{len(O0OO00OOO000O00OO)}个账号==========")#line:7
        for OOO0O00000O0O00O0 in O0OO00OOO000O00OO :#line:8
            print (f"------------正在执行第{O0OO00OOO000O00OO.index(OOO0O00000O0O00O0) + 1}个账号------------")#line:9
            O000OOOOO0OO000OO =CityEarth (OOO0O00000O0O00O0 )#line:10
            if O000OOOOO0OO000OO .base_info ():#line:12
                O000OOOOO0OO000OO .friends_invitation ()#line:14
                O000OOOOO0OO000OO .propsraffle ()#line:16
                O000OOOOO0OO000OO .add_clover ()#line:18
                O000OOOOO0OO000OO .energy ()#line:20
                O000OOOOO0OO000OO .game_map ()#line:22
                O000OOOOO0OO000OO .synthetic ()#line:24
            else :#line:26
                print ('token失效')#line:27
            time .sleep (time_xx )#line:29
    except Exception as OOOOOO0OO0O0OO00O :#line:30
        print (OOOOOO0OO0O0OO00O )#line:31
class CityEarth :#line:34
    def __init__ (OOOO0000OO00OOOOO ,O00OOOO0OO0OOO00O ):#line:36
        try :#line:37
            OOOO0000OO00OOOOO .token =O00OOOO0OO0OOO00O .split ('&')[0 ]#line:38
            OOOO0000OO00OOOOO .innerId =O00OOOO0OO0OOO00O .split ('&')[1 ]#line:39
            OOOO0000OO00OOOOO .headers ={'authorization':OOOO0000OO00OOOOO .token ,'Host':'test.scsc.sc19319.com'}#line:43
        except Exception as OOOOOO00OO000O00O :#line:44
            print ('变量格式错误')#line:45
    def base_info (O00O0OO0000OO000O ):#line:48
        try :#line:49
            O000OO0O0000OO0O0 =requests .request ('get',f'{host}/api/user',headers =O00O0OO0000OO000O .headers ).json ()#line:50
            if 'status'in O000OO0O0000OO0O0 :#line:52
                if O000OO0O0000OO0O0 ['status']==200 :#line:53
                    OO0000OO00O000OO0 =O000OO0O0000OO0O0 ['data']['nickname']#line:54
                    OO0O00O0O0O000OO0 =O000OO0O0000OO0O0 ['data']['inner_id']#line:55
                    OO0O0000OO0O0OO0O =O000OO0O0000OO0O0 ['data']['assets']['gold']#line:56
                    print (f'【账号信息】:昵称:{OO0000OO00O000OO0}丨ID:{OO0O00O0O0O000OO0}丨金种子:{str(OO0O0000OO0O0OO0O).split(".")[0]}')#line:57
                if O000OO0O0000OO0O0 ['status']==401 :#line:58
                    return False #line:59
            return True #line:60
        except Exception as OO0O0000O00O0000O :#line:61
            print (OO0O0000O00O0000O )#line:62
    def user_ad (O0O0O0O00O0OO0O0O ):#line:65
        O0OO0O0O0O00OO00O =requests .request ('get',f'{host}/api/user/ad',headers =O0O0O0O00O0OO0O0O .headers ).json ()#line:66
        if 'status'in O0OO0O0O0O00OO00O :#line:68
            if O0OO0O0O0O00OO00O ['status']==200 :#line:69
                OO00OOOO0O0OOO0O0 =O0OO0O0O0O00OO00O ['data']['max_time']#line:70
                O0O0000000000000O =O0OO0O0O0O00OO00O ['data']['watch_time']#line:71
                print (f'【获取种子】:获取种子机会剩余{OO00OOOO0O0OOO0O0 - O0O0000000000000O}次')#line:72
                if OO00OOOO0O0OOO0O0 -O0O0000000000000O >0 :#line:73
                    time .sleep (random .randint (16 ,19 ))#line:74
                    O00OOOO0O0OO0OO0O =requests .request ('post',f'{host}/api/game/watched-ad-forSilver',headers =O0O0O0O00O0OO0O0O .headers ).json ()#line:75
                    if 'status'in O00OOOO0O0OO0OO0O :#line:77
                        if O00OOOO0O0OO0OO0O ['status']==200 :#line:78
                            O0OOOOO0O00O0OOOO =O00OOOO0O0OO0OO0O ['data']['silver']#line:79
                            print (f'【获取种子】:获得种子:{O0OOOOO0O00O0OOOO}')#line:80
                            return True #line:81
                        if O00OOOO0O0OO0OO0O ['status']==500 :#line:82
                            OO000000O000OOO00 =O00OOOO0O0OO0OO0O ['message']#line:83
                            print (f'【获取种子】:{OO000000O000OOO00}')#line:84
                            return False #line:85
    def synthetic (O00OO0O000O0O000O ):#line:88
        global id ,g #line:89
        try :#line:90
            while True :#line:91
                OOOOO00OOOO0OO0O0 =requests .request ('get',f'{host}/api/game/getAllData',headers =O00OO0O000O0O000O .headers ).json ()#line:92
                if 'status'in OOOOO00OOOO0OO0O0 :#line:94
                    if OOOOO00OOOO0OO0O0 ['status']==200 :#line:95
                        OOOO0OO0000OO0O0O =OOOOO00OOOO0OO0O0 ['data']['cropList']#line:96
                        OOOOO00O000OO0O0O =OOOOO00OOOO0OO0O0 ['data']['gameCoreDataDBid']#line:97
                        O0OOO0000O0OO0OO0 =0 #line:98
                        for O00OOO0000O0O0O00 in OOOO0OO0000OO0O0O :#line:99
                            if not O00OOO0000O0O0O00 :#line:100
                                O00O0000O00OO000O ={"site":O0OOO0000O0OO0OO0 ,"crop_id":OOOOO00O000OO0O0O }#line:101
                                OOOOOOO0OOOOO0O00 =requests .request ('post',f'{host}/api/game/crops/buy',headers =O00OO0O000O0O000O .headers ,data =O00O0000O00OO000O ).json ()#line:102
                                if 'status'in OOOOOOO0OOOOO0O00 :#line:104
                                    if OOOOOOO0OOOOO0O00 ['status']==200 :#line:105
                                        if OOOOOOO0OOOOO0O00 ['message']=='种子数量不足':#line:106
                                            print (f'【购买合成】:{OOOOOOO0OOOOO0O00["message"]}')#line:107
                                            if not O00OO0O000O0O000O .user_ad ():#line:108
                                                return False #line:109
                                        print (f'【购买合成】:购买农作物,位置{O0OOO0000O0OO0OO0}')#line:110
                                    if OOOOOOO0OOOOO0O00 ['status']==500 :#line:111
                                        print (f'【购买合成】:{OOOOOOO0OOOOO0O00["message"]}')#line:112
                                        return False #line:113
                                time .sleep (random .randint (3 ,5 )/10 )#line:114
                            O0OOO0000O0OO0OO0 +=1 #line:115
                        OOO0000000O0O00OO =requests .request ('get',f'{host}/api/game/getAllData',headers =O00OO0O000O0O000O .headers ).json ()#line:116
                        OO00OO00OOOO000O0 =OOO0000000O0O00OO ['data']['cropList']#line:117
                        OO0O000OOOOOOO0OO =False #line:118
                        for O00OOO0000O0O0O00 in range (12 ):#line:119
                            id =OO00OO00OOOO000O0 [O00OOO0000O0O0O00 ]['level']#line:120
                            if id !=0 :#line:121
                                for OO00OO0OOOO00OOO0 in range (11 ):#line:122
                                    O00OO0OOO00OO0000 =OO00OO0OOOO00OOO0 +1 #line:123
                                    g =OO00OO00OOOO000O0 [O00OO0OOO00OO0000 ]['level']#line:124
                                    if id ==g :#line:125
                                        OO0O0O0O0O0O0O0O0 =OO00OO0OOOO00OOO0 +2 #line:126
                                        if OO0O0O0O0O0O0O0O0 ==O00OOO0000O0O0O00 +1 :#line:127
                                            pass #line:128
                                        else :#line:129
                                            time .sleep (random .randint (3 ,5 )/10 )#line:130
                                            OO0O000000O00OO0O =O00OOO0000O0O0O00 +1 #line:131
                                            OOOOOO0OO0OOOO0O0 ={"site":OO0O000000O00OO0O -1 ,"targetSite":OO0O0O0O0O0O0O0O0 -1 }#line:133
                                            O0O00OO0OO00OO0O0 =requests .request ('post',f'{host}/api/game/crops/move',headers =O00OO0O000O0O000O .headers ,data =OOOOOO0OO0OOOO0O0 ).json ()#line:135
                                            if 'status'in O0O00OO0OO00OO0O0 :#line:137
                                                if O0O00OO0OO00OO0O0 ['status']==200 :#line:138
                                                    pass #line:139
                                            print ('【购买合成】:',OO0O000000O00OO0O ,OO0O0O0O0O0O0O0O0 ,'合成成功')#line:141
                                            OO0O000OOOOOOO0OO =True #line:142
                                    if OO0O000OOOOOOO0OO :#line:143
                                        break #line:144
                                if OO0O000OOOOOOO0OO :#line:145
                                    break #line:146
        except Exception as O0OOOOO000O0O0O0O :#line:147
            O00OO0O000O0O000O .synthetic ()#line:148
    def propsraffle (O0OOO00OO0O0O00OO ):#line:152
        try :#line:153
            while True :#line:154
                O0OOOO000000OOO00 =requests .request ('get',f'{host}/api/propsraffle/lucky',headers =O0OOO00OO0O0O00OO .headers ).json ()#line:155
                if 'status'in O0OOOO000000OOO00 :#line:157
                    if O0OOOO000000OOO00 ['status']==200 :#line:158
                        OO0O000O00O00O000 =O0OOOO000000OOO00 ['data']['rows']#line:159
                        if OO0O000O00O00O000 ==5 or OO0O000O00O00O000 ==6 or OO0O000O00O00O000 ==7 :#line:160
                            O0000OO0O00O0OOOO =O0OOOO000000OOO00 ['data']['silver']#line:161
                            print (f'【转盘抽奖】:获得种子:{O0000OO0O00O0OOOO}')#line:162
                        if OO0O000O00O00O000 ==1 or OO0O000O00O00O000 ==2 or OO0O000O00O00O000 ==3 :#line:163
                            OO0OO0O0O0O000O0O =O0OOOO000000OOO00 ['data']['clover']#line:164
                            print (f'【转盘抽奖】:获得三叶草:{OO0OO0O0O0O000O0O}')#line:165
                        if OO0O000O00O00O000 ==4 or OO0O000O00O00O000 ==8 :#line:166
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:167
                        if OO0O000O00O00O000 =='抽奖次数已用完':#line:171
                            OOOOO00OOO00O00O0 =random .randint (160 ,190 )/10 #line:172
                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{OOOOO00OOO00O00O0}秒获取抽奖机会')#line:173
                            time .sleep (OOOOO00OOO00O00O0 )#line:174
                            O000OO0O00O0O0O0O =requests .request ('get',f'{host}/api/propsraffle/lucky/adverti/restore',headers =O0OOO00OO0O0O00OO .headers ).json ()#line:175
                            if 'status'in O000OO0O00O0O0O0O :#line:177
                                if O000OO0O00O0O0O0O ['status']==200 :#line:178
                                    print (f'【转盘抽奖】:{O000OO0O00O0O0O0O["message"]}')#line:179
                                if O000OO0O00O0O0O0O ['status']==500 :#line:180
                                    print (f'【转盘抽奖】:{O000OO0O00O0O0O0O["message"]}')#line:181
                                    break #line:182
                            time .sleep (random .randint (10 ,15 )/10 )#line:183
                time .sleep (random .randint (8 ,15 )/10 )#line:184
        except Exception as OO00OOO00O00O000O :#line:185
            print (OO00OOO00O00O000O )#line:186
    def friends_invitation (O00000O00O0OO0OOO ):#line:189
        try :#line:190
            O0O000O0000000OOO =requests .request ('get','http://test.scsc.sc19319.com/api/friends',headers =O00000O00O0OO0OOO .headers ).json ()#line:191
            if 'status'in O0O000O0000000OOO :#line:192
                if O0O000O0000000OOO ['status']==200 :#line:193
                    OO000O0OOOOO00O0O =O0O000O0000000OOO ['data']['myInviteter']#line:194
                    if OO000O0OOOOO00O0O :#line:195
                        OO0O000O0O0OOO0OO =OO000O0OOOOO00O0O ['user']['nickname']#line:196
                        print (f'【绑邀请码】:我的邀请人:{OO0O000O0O0OOO0OO}')#line:197
                    else :#line:198
                        if O00000O00O0OO0OOO .innerId !='0':#line:199
                            print ('【绑邀请码】:绑定邀请码')#line:200
                            O0OOO0OO000O000O0 ={"innerId":O00000O00O0OO0OOO .innerId }#line:201
                            O0O00OOOO00OO0OOO =requests .request ('post',f'{host}/api/friends/my-invitation',headers =O00000O00O0OO0OOO .headers ,data =O0OOO0OO000O000O0 ).json ()#line:202
                            print (O0O00OOOO00OO0OOO )#line:203
                        else :#line:204
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:205
        except Exception as OOO00O0OO0O0O0OOO :#line:206
            print (OOO00O0OO0O0O0OOO )#line:207
    def add_clover (OO0O00O00OOOOO0OO ):#line:211
        try :#line:212
            O00000O0O0O0OOOO0 =requests .request ('get',f'{host}/api/assets/clovers',headers =OO0O00O00OOOOO0OO .headers ).json ()#line:213
            if 'status'in O00000O0O0O0OOOO0 :#line:215
                if O00000O0O0O0OOOO0 ['status']==200 :#line:216
                    OO0OOOO0O0OO0000O =O00000O0O0O0OOOO0 ['data']['clover']#line:217
                    O0O0O0OOOOO000000 =O00000O0O0O0OOOO0 ['data']['used_clover']#line:218
                    OO00O0OO000O00OOO =float (OO0OOOO0O0OO0000O )-float (O0O0O0OOOOO000000 )#line:219
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0O0O0OOOOO000000}')#line:220
                    if OO00O0OO000O00OOO >1 :#line:221
                        OO00OO000OOO00OOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":OO00O0OO000O00OOO }#line:222
                        OOOO0O00O00OO00OO =requests .request ('post','http://test.scsc.sc19319.com/api/lottery/add-stake',headers =OO0O00O00OOOOO0OO .headers ,data =OO00OO000OOO00OOO ).json ()#line:224
                        if 'status'in OOOO0O00O00OO00OO :#line:226
                            if OOOO0O00O00OO00OO ['status']==200 :#line:227
                                print (f'【参与抽奖】:添加三叶草:{OOOO0O00O00OO00OO["data"]}丨数量:{OO00O0OO000O00OOO}')#line:228
        except Exception as O0000O0OOOOOO0OO0 :#line:229
            print (O0000O0OOOOOO0OO0 )#line:230
    def energy (O0OO0000O00O0OO0O ):#line:233
        OO0OO00OOOO000O00 =requests .request ('get',f'{host}/api/energy/general',headers =O0OO0000O00O0OO0O .headers ).json ()#line:234
        if 'status'in OO0OO00OOOO000O00 :#line:236
            if OO0OO00OOOO000O00 ['status']==200 :#line:237
                O00000000OO0000OO =OO0OO00OOOO000O00 ['data']['ordinary_water_consumptions']#line:238
                if float (O00000000OO0000OO )<80 :#line:239
                    O0OO00O000OOOOOOO =99 -float (O00000000OO0000OO )#line:240
                    OO0O0OO0O0OOO00O0 ={"fertilizer":str (O0OO00O000OOOOOOO ).split ('.')[0 ]}#line:241
                    O00O000O000OOO00O =requests .request ('post',f'{host}/api/energy/general/buy/fertilizer',headers =O0OO0000O00O0OO0O .headers ,data =OO0O0OO0O0OOO00O0 ).json ()#line:242
                    if 'status'in O00O000O000OOO00O :#line:244
                        if O00O000O000OOO00O ['status']==200 :#line:245
                            print (f'【购买肥料】:{O00O000O000OOO00O["message"]}')#line:246
                O0OOOO0OO00O0OO0O =OO0OO00OOOO000O00 ['data']['ordinary_water_consumptions']#line:247
                if float (O0OOOO0OO00O0OO0O )<800 :#line:248
                    O0OOO00O000OOO00O =999 -float (O0OOOO0OO00O0OO0O )#line:249
                    OO000O0O00O0O0O0O ={"water":str (O0OOO00O000OOO00O ).split ('.')[0 ]}#line:250
                    OOOO000O0O0OO0OO0 =requests .request ('post',f'{host}/api/energy/general/buy/water',headers =O0OO0000O00O0OO0O .headers ,data =OO000O0O00O0O0O0O ).json ()#line:251
                    if 'status'in OOOO000O0O0OO0OO0 :#line:252
                        if OOOO000O0O0OO0OO0 ['status']==200 :#line:253
                            print (f'【购买水滴】:{OOOO000O0O0OO0OO0["message"]}')#line:254
    def game_map (OOOO0OO00OOOOOOO0 ):#line:258
        OO0OOOOOO0OOO0O00 =requests .request ('get',f'{host}/api/game/map',headers =OOOO0OO00OOOOOOO0 .headers ).json ()#line:259
        OOOO0O00OO0O0O00O =0 #line:261
        if 'status'in OO0OOOOOO0OOO0O00 :#line:262
            if OO0OOOOOO0OOO0O00 ['status']==200 :#line:263
                OO0OO0OOO0OOOOO00 =OO0OOOOOO0OOO0O00 ['data']['list'][0 ]['crops']#line:264
                for O0O00O0OO0000O0O0 in OO0OO0OOO0OOOOO00 :#line:266
                    O0OO00OOOOOOO00OO =O0O00O0OO0000O0O0 ['count']#line:268
                    if O0OO00OOOOOOO00OO >0 :#line:269
                        OOOO0O00OO0O0O00O +=1 #line:271
                if OOOO0O00OO0O0O00O >8 :#line:273
                    print ('卖掉低级农作物')#line:274
                    O0OOOO0000OO0OO0O =OO0OO0OOO0OOOOO00 [0 ]['id']#line:275
                    OOO00O0O0O00O0000 ={"crop_id":O0OOOO0000OO0OO0O ,"num":1 }#line:276
                    O000O0OOO000O0000 =requests .request ('post',f'{host}/api/game/crops/sellForGold',headers =OOOO0OO00OOOOOOO0 .headers ,data =OOO00O0O0O00O0000 ).json ()#line:277
                    if 'status'in O000O0OOO000O0000 :#line:279
                        if O000O0OOO000O0000 ['status']==200 :#line:280
                            print ('卖出成功')#line:281
def version_of_the_validation ():#line:285
    return str ((57 -56 )/10 )#line:286
def gitee_validation ():#line:288
    try :#line:289
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:290
    except Exception as O000O0O0OO000O000 :#line:291
        sys .exit (0 )#line:292
def update_the_validation ():#line:298
    try :#line:299
        OOO000O0OO0O0O00O =gitee_validation ()#line:300
        if version_of_the_validation ()<OOO000O0OO0O0O00O ['CityEarth']['edition']:#line:301
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO000O0OO0O0O00O["CityEarth"]["edition"]}   ❌')#line:302
            print (f'更新内容=>>{OOO000O0OO0O0O00O["CityEarth"]["content"]}   👍')#line:303
        else :#line:304
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO000O0OO0O0O00O["CityEarth"]["edition"]}   ✅')#line:305
            print (f'更新内容=>> {OOO000O0OO0O0O00O["CityEarth"]["content"]}   👍')#line:306
    except Exception as O0O0O0OOOOOOO0000 :#line:307
        print (O0O0O0OOOOOOO0000 )#line:308
def os_qinglong ():#line:311
    if application in os .environ :#line:312
        O00OOO000000O0O0O =os .environ [application ].split ('\n')#line:313
        if len (O00OOO000000O0O0O )>0 :#line:314
            return O00OOO000000O0O0O #line:315
        else :#line:316
            print (f"{application}变量未启用")#line:317
            print ('脚本退出')#line:318
            sys .exit (1 )#line:319
    else :#line:320
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:321
        return os_built ()#line:322
def os_built ():#line:325
    if token :#line:326
        OOOOO000O00O00000 =token .split ('\n')#line:327
        if len (OOOOO000O00O00000 )>0 :#line:328
            return OOOOO000O00O00000 #line:329
    else :#line:330
        print (f"内置变量为空")#line:331
        print ('脚本结束')#line:332
        sys .exit (0 )#line:333
if __name__ =='__main__':#line:336
    start ()#line:337
