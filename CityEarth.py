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
cron: 12 */3 * * *
new Env('生城世朝')
项目地址  微信打开  http://share.sc19319.com/scsc/1932634
apk下载地址     https://sc19319.oss-cn-hangzhou.aliyuncs.com/scsc/test/1.9.3.1.S1.apk
抓取  http://test.scsc.sc19319.com 的authorization值
青龙变量 export ce_token="authorization&绑定邀请码"   不绑定填 0   多号换行
我的邀请码是  1932634
版本  0.3
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
        OO0OO0O00OO0O0O00 =os_qinglong ()#line:6
        print (f"==========共找到{len(OO0OO0O00OO0O0O00)}个账号==========")#line:7
        for OO0OOOO00O0OOOO00 in OO0OO0O00OO0O0O00 :#line:8
            print (f"------------正在执行第{OO0OO0O00OO0O0O00.index(OO0OOOO00O0OOOO00) + 1}个账号------------")#line:9
            O0OOOOO00OO0OOOO0 =CityEarth (OO0OOOO00O0OOOO00 )#line:10
            if O0OOOOO00OO0OOOO0 .base_info ():#line:12
                O0OOOOO00OO0OOOO0 .friends_invitation ()#line:16
                O0OOOOO00OO0OOOO0 .add_clover ()#line:20
                O0OOOOO00OO0OOOO0 .energy ()#line:22
                O0OOOOO00OO0OOOO0 .game_map ()#line:24
                O0OOOOO00OO0OOOO0 .synthetic ()#line:26
                O0OOOOO00OO0OOOO0 .crops_illustrated ()#line:28
            else :#line:29
                print ('token失效')#line:30
            time .sleep (time_xx )#line:32
    except Exception as O0OOO00OO00O000O0 :#line:33
        print (O0OOO00OO00O000O0 )#line:34
class CityEarth :#line:37
    def __init__ (OO0O0O0OO000OO0O0 ,OOO0000OOO000OOO0 ):#line:39
        try :#line:40
            OO0O0O0OO000OO0O0 .token =OOO0000OOO000OOO0 .split ('&')[0 ]#line:41
            OO0O0O0OO000OO0O0 .innerId =OOO0000OOO000OOO0 .split ('&')[1 ]#line:42
            OO0O0O0OO000OO0O0 .headers ={'authorization':OO0O0O0OO000OO0O0 .token ,'Host':'test.scsc.sc19319.com'}#line:46
        except Exception as OOOOOO0OO00O0000O :#line:47
            print ('变量格式错误')#line:48
    def base_info (O0OOO0O0000OOOO00 ):#line:51
        try :#line:52
            OOOOOOOO00000O0OO =requests .request ('get',f'{host}/api/user',headers =O0OOO0O0000OOOO00 .headers ).json ()#line:53
            if 'status'in OOOOOOOO00000O0OO :#line:55
                if OOOOOOOO00000O0OO ['status']==200 :#line:56
                    O0O0000OOO0O00O00 =OOOOOOOO00000O0OO ['data']['nickname']#line:57
                    O0O0O0000000OO00O =OOOOOOOO00000O0OO ['data']['inner_id']#line:58
                    O000000OOOOOOOOO0 =OOOOOOOO00000O0OO ['data']['assets']['gold']#line:59
                    O00O00OOOO0O0OOOO =OOOOOOOO00000O0OO ['data']['level']#line:60
                    print (f'【账号信息】:昵称:{O0O0000OOO0O00O00}丨ID:{str(O0O0O0000000OO00O)[:3] + "**"+ str(O0O0O0000000OO00O)[5:]}丨农作物等级:{O00O00OOOO0O0OOOO}丨金种子:{str(O000000OOOOOOOOO0).split(".")[0]}')#line:61
                if OOOOOOOO00000O0OO ['status']==401 :#line:62
                    return False #line:63
            return True #line:64
        except Exception as OOOO00O00O00O0OO0 :#line:65
            print (OOOO00O00O00O0OO0 )#line:66
    def crops_illustrated (OOO000000O000000O ):#line:70
        OO0OOO0O0O00OO00O =requests .request ('get',f'{host}/api/game/crops/illustrated',headers =OOO000000O000000O .headers ).json ()#line:71
        if 'status'in OO0OOO0O0O00OO00O :#line:72
            if OO0OOO0O0O00OO00O ['status']==200 :#line:73
                O0OOOOO0O0O00OO00 =OO0OOO0O0O00OO00O ['data'][0 ]['crops']#line:74
                for O00OOO0OO0O0OO000 in O0OOOOO0O0O00OO00 :#line:75
                    if O00OOO0OO0O0OO000 ['ill_clover_award']:#line:76
                        if float (O00OOO0OO0O0OO000 ['ill_clover_award'])>1 :#line:77
                            if O00OOO0OO0O0OO000 ['is_finish']:#line:78
                                if not O00OOO0OO0O0OO000 ['is_getit']:#line:79
                                    OOO0OO00O0OOOOO0O ={"award_level":O00OOO0OO0O0OO000 ['level']}#line:80
                                    O000OOOOOOOOOOO0O =requests .request ('post',f'{host}/api/game/crops/illustrated/award',headers =OOO000000O000000O .headers ,data =OOO0OO00O0OOOOO0O ).json ()#line:81
                                    if 'status'in O000OOOOOOOOOOO0O :#line:82
                                        if O000OOOOOOOOOOO0O ['status']==200 :#line:83
                                            O0O0OOOOOO0OOOOO0 =O000OOOOOOOOOOO0O ['data']['ill_clover_award']#line:84
                                            print (f'【图鉴奖励】:领取{O00OOO0OO0O0OO000["crop_name"]}奖励{O0O0OOOOOO0OOOOO0}种子成功')#line:85
    def watched_ad (OOOOOO00OO000OO00 ):#line:90
        OO000OO00OOOOOOOO =requests .request ('post',f'{host}/api/game/watched-ad',headers =OOOOOO00OO000OO00 .headers ).json ()#line:91
        print (OO000OO00OOOOOOOO )#line:92
    def user_ad (O00OOO0O0O0OOOOOO ):#line:98
        O0OO000OOOOO0O0O0 =requests .request ('get',f'{host}/api/user/ad',headers =O00OOO0O0O0OOOOOO .headers ).json ()#line:99
        if 'status'in O0OO000OOOOO0O0O0 :#line:101
            if O0OO000OOOOO0O0O0 ['status']==200 :#line:102
                O0OOO00OOOOO0OOO0 =O0OO000OOOOO0O0O0 ['data']['max_time']#line:103
                O0OOOO0000000OOO0 =O0OO000OOOOO0O0O0 ['data']['watch_time']#line:104
                print (f'【获取种子】:获取种子机会剩余{O0OOO00OOOOO0OOO0 - O0OOOO0000000OOO0}次')#line:105
                if O0OOO00OOOOO0OOO0 -O0OOOO0000000OOO0 >0 :#line:106
                    time .sleep (random .randint (16 ,19 ))#line:107
                    OO0O00OO0O00O0000 =requests .request ('post',f'{host}/api/game/watched-ad-forSilver',headers =O00OOO0O0O0OOOOOO .headers ).json ()#line:108
                    if 'status'in OO0O00OO0O00O0000 :#line:110
                        if OO0O00OO0O00O0000 ['status']==200 :#line:111
                            O0000OOO000OO000O =OO0O00OO0O00O0000 ['data']['silver']#line:112
                            print (f'【获取种子】:获得种子:{O0000OOO000OO000O}')#line:113
                            return True #line:114
                        if OO0O00OO0O00O0000 ['status']==500 :#line:115
                            OO0OOOO0OO00O0000 =OO0O00OO0O00O0000 ['message']#line:116
                            print (f'【获取种子】:{OO0OOOO0OO00O0000}')#line:117
                            return False #line:118
    def synthetic (O0O00OOO00O0OO0O0 ):#line:121
        global id ,g #line:122
        try :#line:123
            while True :#line:124
                OOO000OOO0000O0OO =requests .request ('get',f'{host}/api/game/getAllData',headers =O0O00OOO00O0OO0O0 .headers ).json ()#line:125
                if 'status'in OOO000OOO0000O0OO :#line:127
                    if OOO000OOO0000O0OO ['status']==200 :#line:128
                        O00OO0O0O0O000000 =OOO000OOO0000O0OO ['data']['cropList']#line:129
                        O000OOOOO0OO0O0OO =OOO000OOO0000O0OO ['data']['gameCoreDataDBid']#line:130
                        O000O00O0OO0OOOO0 =0 #line:131
                        for O00O0OO0OO00O000O in O00OO0O0O0O000000 :#line:132
                            if not O00O0OO0OO00O000O :#line:133
                                OO0OOOO0O00O0O000 ={"site":O000O00O0OO0OOOO0 ,"crop_id":O000OOOOO0OO0O0OO }#line:134
                                O0O000OOOO00000OO =requests .request ('post',f'{host}/api/game/crops/buy',headers =O0O00OOO00O0OO0O0 .headers ,data =OO0OOOO0O00O0O000 ).json ()#line:135
                                if 'status'in O0O000OOOO00000OO :#line:137
                                    if O0O000OOOO00000OO ['status']==200 :#line:138
                                        if O0O000OOOO00000OO ['message']=='种子数量不足':#line:139
                                            print (f'【购买合成】:{O0O000OOOO00000OO["message"]}')#line:140
                                            if not O0O00OOO00O0OO0O0 .user_ad ():#line:141
                                                return False #line:142
                                        print (f'【购买合成】:购买农作物,位置{O000O00O0OO0OOOO0}')#line:143
                                    if O0O000OOOO00000OO ['status']==500 :#line:144
                                        print (f'【购买合成】:{O0O000OOOO00000OO["message"]}')#line:145
                                        return False #line:146
                                time .sleep (random .randint (3 ,5 )/10 )#line:147
                            O000O00O0OO0OOOO0 +=1 #line:148
                        OO0O0OOO0000OOO0O =requests .request ('get',f'{host}/api/game/getAllData',headers =O0O00OOO00O0OO0O0 .headers ).json ()#line:149
                        OO0OO00OOO0O000OO =OO0O0OOO0000OOO0O ['data']['cropList']#line:150
                        O0O0OO000OOO00O00 =False #line:151
                        for O00O0OO0OO00O000O in range (12 ):#line:152
                            id =OO0OO00OOO0O000OO [O00O0OO0OO00O000O ]['level']#line:153
                            if id !=0 :#line:154
                                for O00OO0O0OO0O0000O in range (11 ):#line:155
                                    OOO0O0OO0O0OO0000 =O00OO0O0OO0O0000O +1 #line:156
                                    g =OO0OO00OOO0O000OO [OOO0O0OO0O0OO0000 ]['level']#line:157
                                    if id ==g :#line:158
                                        OO0O000OO0000OOO0 =O00OO0O0OO0O0000O +2 #line:159
                                        if OO0O000OO0000OOO0 ==O00O0OO0OO00O000O +1 :#line:160
                                            pass #line:161
                                        else :#line:162
                                            time .sleep (random .randint (3 ,5 )/10 )#line:163
                                            OOO0OO0000O000OOO =O00O0OO0OO00O000O +1 #line:164
                                            OOOO000OOOO0O00OO ={"site":OOO0OO0000O000OOO -1 ,"targetSite":OO0O000OO0000OOO0 -1 }#line:166
                                            OO0O0O00000000000 =requests .request ('post',f'{host}/api/game/crops/move',headers =O0O00OOO00O0OO0O0 .headers ,data =OOOO000OOOO0O00OO ).json ()#line:168
                                            if 'status'in OO0O0O00000000000 :#line:170
                                                if OO0O0O00000000000 ['status']==200 :#line:171
                                                    pass #line:172
                                            print ('【购买合成】:',OOO0OO0000O000OOO ,OO0O000OO0000OOO0 ,'合成成功')#line:174
                                            O0O0OO000OOO00O00 =True #line:175
                                    if O0O0OO000OOO00O00 :#line:176
                                        break #line:177
                                if O0O0OO000OOO00O00 :#line:178
                                    break #line:179
        except Exception as OO0000O00000O0000 :#line:180
            O0O00OOO00O0OO0O0 .synthetic ()#line:181
    def propsraffle (O0OOOOOOOO0OO0O0O ):#line:185
        try :#line:186
            while True :#line:187
                O0OO00OOO00000OO0 =requests .request ('get',f'{host}/api/propsraffle/lucky',headers =O0OOOOOOOO0OO0O0O .headers ).json ()#line:188
                if 'status'in O0OO00OOO00000OO0 :#line:190
                    if O0OO00OOO00000OO0 ['status']==200 :#line:191
                        OOO000O0OO000O00O =O0OO00OOO00000OO0 ['data']['rows']#line:192
                        if OOO000O0OO000O00O ==5 or OOO000O0OO000O00O ==6 or OOO000O0OO000O00O ==7 :#line:193
                            O0O00OO0000O0000O =O0OO00OOO00000OO0 ['data']['silver']#line:194
                            print (f'【转盘抽奖】:获得种子:{O0O00OO0000O0000O}')#line:195
                        if OOO000O0OO000O00O ==1 or OOO000O0OO000O00O ==2 or OOO000O0OO000O00O ==3 :#line:196
                            OO0000000O00OO0OO =O0OO00OOO00000OO0 ['data']['clover']#line:197
                            print (f'【转盘抽奖】:获得三叶草:{OO0000000O00OO0OO}')#line:198
                        if OOO000O0OO000O00O ==4 or OOO000O0OO000O00O ==8 :#line:199
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:200
                        if OOO000O0OO000O00O =='抽奖次数已用完':#line:204
                            O0OO000OO0OO0O00O =random .randint (160 ,190 )/10 #line:205
                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{O0OO000OO0OO0O00O}秒获取抽奖机会')#line:206
                            time .sleep (O0OO000OO0OO0O00O )#line:207
                            O00000OO00O0O00OO =requests .request ('get',f'{host}/api/propsraffle/lucky/adverti/restore',headers =O0OOOOOOOO0OO0O0O .headers ).json ()#line:208
                            if 'status'in O00000OO00O0O00OO :#line:210
                                if O00000OO00O0O00OO ['status']==200 :#line:211
                                    print (f'【转盘抽奖】:{O00000OO00O0O00OO["message"]}')#line:212
                                if O00000OO00O0O00OO ['status']==500 :#line:213
                                    print (f'【转盘抽奖】:{O00000OO00O0O00OO["message"]}')#line:214
                                    break #line:215
                            time .sleep (random .randint (10 ,15 )/10 )#line:216
                time .sleep (random .randint (8 ,15 )/10 )#line:217
        except Exception as O0OO0O0O000O00OOO :#line:218
            print (O0OO0O0O000O00OOO )#line:219
    def friends_invitation (OO0O0OO00000OO000 ):#line:222
        try :#line:223
            OOOOO00OOO0O000O0 =requests .request ('get','http://test.scsc.sc19319.com/api/friends',headers =OO0O0OO00000OO000 .headers ).json ()#line:224
            if 'status'in OOOOO00OOO0O000O0 :#line:225
                if OOOOO00OOO0O000O0 ['status']==200 :#line:226
                    O00O000OO0O0OOO0O =OOOOO00OOO0O000O0 ['data']['myInviteter']#line:227
                    if O00O000OO0O0OOO0O :#line:228
                        OO0OOOOOOOOO00OO0 =O00O000OO0O0OOO0O ['user']['nickname']#line:229
                        print (f'【绑邀请码】:我的邀请人:{OO0OOOOOOOOO00OO0}')#line:230
                    else :#line:231
                        if OO0O0OO00000OO000 .innerId !='0':#line:232
                            print ('【绑邀请码】:绑定邀请码')#line:233
                            OOO0O0O0O000O0000 ={"innerId":OO0O0OO00000OO000 .innerId }#line:234
                            O0OOO0O0OO00000O0 =requests .request ('post',f'{host}/api/friends/my-invitation',headers =OO0O0OO00000OO000 .headers ,data =OOO0O0O0O000O0000 ).json ()#line:235
                            print (O0OOO0O0OO00000O0 )#line:236
                        else :#line:237
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:238
        except Exception as OOOOO0O0O0000OO00 :#line:239
            print (OOOOO0O0O0000OO00 )#line:240
    def add_clover (OO00OO000O0O00000 ):#line:244
        try :#line:245
            O0O0000000OO0O0O0 =requests .request ('get',f'{host}/api/assets/clovers',headers =OO00OO000O0O00000 .headers ).json ()#line:246
            if 'status'in O0O0000000OO0O0O0 :#line:248
                if O0O0000000OO0O0O0 ['status']==200 :#line:249
                    OO0O00000000O0O00 =O0O0000000OO0O0O0 ['data']['clover']#line:250
                    OOO000O0OOO000000 =O0O0000000OO0O0O0 ['data']['used_clover']#line:251
                    OOO0000O0OO0O0O0O =float (OO0O00000000O0O00 )-float (OOO000O0OOO000000 )#line:252
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OOO000O0OOO000000}')#line:253
                    if OOO0000O0OO0O0O0O >1 :#line:254
                        OO00000OO0O0O00OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":OOO0000O0OO0O0O0O }#line:255
                        O0OO0OOO00OOO00OO =requests .request ('post','http://test.scsc.sc19319.com/api/lottery/add-stake',headers =OO00OO000O0O00000 .headers ,data =OO00000OO0O0O00OO ).json ()#line:257
                        if 'status'in O0OO0OOO00OOO00OO :#line:259
                            if O0OO0OOO00OOO00OO ['status']==200 :#line:260
                                print (f'【参与抽奖】:添加三叶草:{O0OO0OOO00OOO00OO["data"]}丨数量:{OOO0000O0OO0O0O0O}')#line:261
        except Exception as OO0O0OOOOO0000000 :#line:262
            print (OO0O0OOOOO0000000 )#line:263
    def energy (O000O0O0OO0OO0OOO ):#line:266
        OOO0OOOOO000O0O00 =requests .request ('get',f'{host}/api/energy/general',headers =O000O0O0OO0OO0OOO .headers ).json ()#line:267
        if 'status'in OOO0OOOOO000O0O00 :#line:269
            if OOO0OOOOO000O0O00 ['status']==200 :#line:270
                OOO0O0OOOO0000OOO =OOO0OOOOO000O0O00 ['data']['ordinary_water_consumptions']#line:271
                if float (OOO0O0OOOO0000OOO )<80 :#line:272
                    OOO00OO000O0O0OO0 =99 -float (OOO0O0OOOO0000OOO )#line:273
                    OO000000O0OO00OOO ={"fertilizer":str (OOO00OO000O0O0OO0 ).split ('.')[0 ]}#line:274
                    O00O0O0O00000OO00 =requests .request ('post',f'{host}/api/energy/general/buy/fertilizer',headers =O000O0O0OO0OO0OOO .headers ,data =OO000000O0OO00OOO ).json ()#line:275
                    if 'status'in O00O0O0O00000OO00 :#line:277
                        if O00O0O0O00000OO00 ['status']==200 :#line:278
                            print (f'【购买肥料】:{O00O0O0O00000OO00["message"]}')#line:279
                OOO0O0000OO0OO00O =OOO0OOOOO000O0O00 ['data']['ordinary_water_consumptions']#line:280
                if float (OOO0O0000OO0OO00O )<800 :#line:281
                    OOOO00O000O0OOO0O =999 -float (OOO0O0000OO0OO00O )#line:282
                    O00O0OO0O00000OO0 ={"water":str (OOOO00O000O0OOO0O ).split ('.')[0 ]}#line:283
                    O0O0O0O0O000OOOO0 =requests .request ('post',f'{host}/api/energy/general/buy/water',headers =O000O0O0OO0OO0OOO .headers ,data =O00O0OO0O00000OO0 ).json ()#line:284
                    if 'status'in O0O0O0O0O000OOOO0 :#line:285
                        if O0O0O0O0O000OOOO0 ['status']==200 :#line:286
                            print (f'【购买水滴】:{O0O0O0O0O000OOOO0["message"]}')#line:287
    def game_map (O0O0OOO0OOO00O0OO ):#line:291
        OO0O0OOO0OO00OOO0 =requests .request ('get',f'{host}/api/game/map',headers =O0O0OOO0OOO00O0OO .headers ).json ()#line:292
        OO0OO0OOO0O0O0O0O =0 #line:294
        if 'status'in OO0O0OOO0OO00OOO0 :#line:295
            if OO0O0OOO0OO00OOO0 ['status']==200 :#line:296
                O00O0OOO000O0OOOO =OO0O0OOO0OO00OOO0 ['data']['list'][0 ]['crops']#line:297
                for O0OOOO0OOO0O0OOO0 in O00O0OOO000O0OOOO :#line:299
                    O0OOO0OOO0O0OOOO0 =O0OOOO0OOO0O0OOO0 ['count']#line:301
                    if O0OOO0OOO0O0OOOO0 >0 :#line:302
                        OO0OO0OOO0O0O0O0O +=1 #line:304
                if OO0OO0OOO0O0O0O0O >8 :#line:306
                    print ('卖掉低级农作物')#line:307
                    O0000O000O0OOO00O =O00O0OOO000O0OOOO [0 ]['id']#line:308
                    O0000000OO0O0000O ={"crop_id":O0000O000O0OOO00O ,"num":1 }#line:309
                    O0O0OOO00O0OOOOOO =requests .request ('post',f'{host}/api/game/crops/sellForGold',headers =O0O0OOO0OOO00O0OO .headers ,data =O0000000OO0O0000O ).json ()#line:310
                    if 'status'in O0O0OOO00O0OOOOOO :#line:312
                        if O0O0OOO00O0OOOOOO ['status']==200 :#line:313
                            print ('卖出成功')#line:314
def version_of_the_validation ():#line:318
    return str ((59 -56 )/10 )#line:319
def gitee_validation ():#line:321
    try :#line:322
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:323
    except Exception as OOO0O00O0OOO00O0O :#line:324
        sys .exit (0 )#line:325
def update_the_validation ():#line:331
    try :#line:332
        OO000O00000O0O0OO =gitee_validation ()#line:333
        if version_of_the_validation ()<OO000O00000O0O0OO ['CityEarth']['edition']:#line:334
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO000O00000O0O0OO["CityEarth"]["edition"]}   ❌')#line:335
            print (f'更新内容=>>{OO000O00000O0O0OO["CityEarth"]["content"]}   👍')#line:336
        else :#line:337
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO000O00000O0O0OO["CityEarth"]["edition"]}   ✅')#line:338
            print (f'更新内容=>> {OO000O00000O0O0OO["CityEarth"]["content"]}   👍')#line:339
    except Exception as O0O000OO0000O0O0O :#line:340
        print (O0O000OO0000O0O0O )#line:341
def os_qinglong ():#line:344
    if application in os .environ :#line:345
        OO0O0O00O000O000O =os .environ [application ].split ('\n')#line:346
        if len (OO0O0O00O000O000O )>0 :#line:347
            return OO0O0O00O000O000O #line:348
        else :#line:349
            print (f"{application}变量未启用")#line:350
            print ('脚本退出')#line:351
            sys .exit (1 )#line:352
    else :#line:353
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:354
        return os_built ()#line:355
def os_built ():#line:358
    if token :#line:359
        OOO00O000OO0OOOO0 =token .split ('\n')#line:360
        if len (OOO00O000OO0OOOO0 )>0 :#line:361
            return OOO00O000OO0OOOO0 #line:362
    else :#line:363
        print (f"内置变量为空")#line:364
        print ('脚本结束')#line:365
        sys .exit (0 )#line:366
if __name__ =='__main__':#line:369
    start ()#line:370
