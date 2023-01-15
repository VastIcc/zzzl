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
        O00OOO000O00O0O0O =os_qinglong ()#line:6
        print (f"==========共找到{len(O00OOO000O00O0O0O)}个账号==========")#line:7
        for O000O00OOO00OO00O in O00OOO000O00O0O0O :#line:8
            print (f"------------正在执行第{O00OOO000O00O0O0O.index(O000O00OOO00OO00O) + 1}个账号------------")#line:9
            O00O0OOO0000000OO =CityEarth (O000O00OOO00OO00O )#line:10
            if O00O0OOO0000000OO .base_info ():#line:12
                O00O0OOO0000000OO .friends_invitation ()#line:16
                O00O0OOO0000000OO .add_clover ()#line:20
                O00O0OOO0000000OO .energy ()#line:22
                O00O0OOO0000000OO .game_map ()#line:24
                O00O0OOO0000000OO .synthetic ()#line:26
                O00O0OOO0000000OO .crops_illustrated ()#line:28
            else :#line:29
                print ('token失效')#line:30
            time .sleep (time_xx )#line:32
    except Exception as O00OOOO000OO0O0OO :#line:33
        print (O00OOOO000OO0O0OO )#line:34
class CityEarth :#line:37
    def __init__ (O000000OOOOO0000O ,O00O00OO0O0O0OO0O ):#line:39
        try :#line:40
            O000000OOOOO0000O .token =O00O00OO0O0O0OO0O .split ('&')[0 ]#line:41
            O000000OOOOO0000O .innerId =O00O00OO0O0O0OO0O .split ('&')[1 ]#line:42
            O000000OOOOO0000O .headers ={'authorization':O000000OOOOO0000O .token ,'Host':'test.scsc.sc19319.com'}#line:46
        except Exception as OOO000O00OOO000O0 :#line:47
            print ('变量格式错误')#line:48
    def base_info (OO0000OO00000000O ):#line:51
        try :#line:52
            O0O0O00O0O0OOOO0O =requests .request ('get',f'{host}/api/user',headers =OO0000OO00000000O .headers ).json ()#line:53
            if 'status'in O0O0O00O0O0OOOO0O :#line:55
                if O0O0O00O0O0OOOO0O ['status']==200 :#line:56
                    OOOO0OOO0O00O00O0 =O0O0O00O0O0OOOO0O ['data']['nickname']#line:57
                    OOOO0O00000O0OOO0 =O0O0O00O0O0OOOO0O ['data']['inner_id']#line:58
                    OOOO000OO00OOO000 =O0O0O00O0O0OOOO0O ['data']['assets']['gold']#line:59
                    OO0O00O0O0OO0OOO0 =O0O0O00O0O0OOOO0O ['data']['level']#line:60
                    print (f'【账号信息】:昵称:{OOOO0OOO0O00O00O0}丨ID:{str(OOOO0O00000O0OOO0)[:3] + "**"+ str(OOOO0O00000O0OOO0)[5:]}丨农作物等级:{OO0O00O0O0OO0OOO0}丨金种子:{str(OOOO000OO00OOO000).split(".")[0]}')#line:61
                if O0O0O00O0O0OOOO0O ['status']==401 :#line:62
                    return False #line:63
            return True #line:64
        except Exception as O00OOOOO0O0O00OO0 :#line:65
            print (O00OOOOO0O0O00OO0 )#line:66
    def crops_illustrated (OOOOOO0O000O0O00O ):#line:70
        OOOOOOO000000OOOO =requests .request ('get',f'{host}/api/game/crops/illustrated',headers =OOOOOO0O000O0O00O .headers ).json ()#line:71
        if 'status'in OOOOOOO000000OOOO :#line:73
            if OOOOOOO000000OOOO ['status']==200 :#line:74
                O00OO0OOO000000OO =OOOOOOO000000OOOO ['data'][0 ]['crops']#line:75
                for OO000OOOOO0OO00O0 in O00OO0OOO000000OO :#line:76
                    if OO000OOOOO0OO00O0 ['ill_clover_award']:#line:77
                        if float (OO000OOOOO0OO00O0 ['ill_clover_award'])>1 :#line:78
                            if OO000OOOOO0OO00O0 ['is_finish']:#line:79
                                if not OO000OOOOO0OO00O0 ['is_getit']:#line:80
                                    OO0O00OO00O00OOOO ={"award_level":OO000OOOOO0OO00O0 ['level']}#line:81
                                    O00O0OOOO0O00O0OO =requests .request ('post',f'{host}/api/game/crops/illustrated/award',headers =OOOOOO0O000O0O00O .headers ,json =OO0O00OO00O00OOOO ).json ()#line:82
                                    if 'status'in O00O0OOOO0O00O0OO :#line:83
                                        if O00O0OOOO0O00O0OO ['status']==200 :#line:84
                                            OOO00OOOOOO0O0O00 =O00O0OOOO0O00O0OO ['data']['ill_clover_award']#line:85
                                            print (f'【图鉴奖励】:领取{OO000OOOOO0OO00O0["crop_name"]}成就丨奖励{OOO00OOOOOO0O0O00}种子成功')#line:86
                                        if O00O0OOOO0O00O0OO ['status']==500 :#line:87
                                            print (f'【图鉴奖励】:{O00O0OOOO0O00O0OO["message"]}')#line:88
    def watched_ad (O0O00O00OOOO00O0O ):#line:91
        O0O0OO0O0O0000O0O =requests .request ('post',f'{host}/api/game/watched-ad',headers =O0O00O00OOOO00O0O .headers ).json ()#line:92
        print (O0O0OO0O0O0000O0O )#line:93
    def user_ad (O0000O00000OOOOO0 ):#line:99
        O0O0OOO0OOOO0OOOO =requests .request ('get',f'{host}/api/user/ad',headers =O0000O00000OOOOO0 .headers ).json ()#line:100
        if 'status'in O0O0OOO0OOOO0OOOO :#line:102
            if O0O0OOO0OOOO0OOOO ['status']==200 :#line:103
                O000OOO00O0OOOOO0 =O0O0OOO0OOOO0OOOO ['data']['max_time']#line:104
                O0O00O0O00OO0OOOO =O0O0OOO0OOOO0OOOO ['data']['watch_time']#line:105
                print (f'【获取种子】:获取种子机会剩余{O000OOO00O0OOOOO0 - O0O00O0O00OO0OOOO}次')#line:106
                if O000OOO00O0OOOOO0 -O0O00O0O00OO0OOOO >0 :#line:107
                    time .sleep (random .randint (16 ,19 ))#line:108
                    O000OO0OO0OO00OO0 =requests .request ('post',f'{host}/api/game/watched-ad-forSilver',headers =O0000O00000OOOOO0 .headers ).json ()#line:109
                    if 'status'in O000OO0OO0OO00OO0 :#line:111
                        if O000OO0OO0OO00OO0 ['status']==200 :#line:112
                            O0OOO000O00OOO0O0 =O000OO0OO0OO00OO0 ['data']['silver']#line:113
                            print (f'【获取种子】:获得种子:{O0OOO000O00OOO0O0}')#line:114
                            return True #line:115
                        if O000OO0OO0OO00OO0 ['status']==500 :#line:116
                            OOOO00OOOOOO0OOOO =O000OO0OO0OO00OO0 ['message']#line:117
                            print (f'【获取种子】:{OOOO00OOOOOO0OOOO}')#line:118
                            return False #line:119
    def synthetic (O0OOOOOO00OOOO0O0 ):#line:122
        global id ,g #line:123
        try :#line:124
            while True :#line:125
                O0O0O0O00OO000000 =requests .request ('get',f'{host}/api/game/getAllData',headers =O0OOOOOO00OOOO0O0 .headers ).json ()#line:126
                if 'status'in O0O0O0O00OO000000 :#line:128
                    if O0O0O0O00OO000000 ['status']==200 :#line:129
                        O00000OO0O0O00OOO =O0O0O0O00OO000000 ['data']['cropList']#line:130
                        OOO0O0OO0OOOO000O =O0O0O0O00OO000000 ['data']['gameCoreDataDBid']#line:131
                        O0O00OO00OO00OOO0 =0 #line:132
                        for OOOOO0OO000O000O0 in O00000OO0O0O00OOO :#line:133
                            if not OOOOO0OO000O000O0 :#line:134
                                O0000OO0OO00OOO0O ={"site":O0O00OO00OO00OOO0 ,"crop_id":OOO0O0OO0OOOO000O }#line:135
                                OO0O0000O0OOOOOOO =requests .request ('post',f'{host}/api/game/crops/buy',headers =O0OOOOOO00OOOO0O0 .headers ,data =O0000OO0OO00OOO0O ).json ()#line:136
                                if 'status'in OO0O0000O0OOOOOOO :#line:138
                                    if OO0O0000O0OOOOOOO ['status']==200 :#line:139
                                        if OO0O0000O0OOOOOOO ['message']=='种子数量不足':#line:140
                                            print (f'【购买合成】:{OO0O0000O0OOOOOOO["message"]}')#line:141
                                            if not O0OOOOOO00OOOO0O0 .user_ad ():#line:142
                                                return False #line:143
                                        print (f'【购买合成】:购买农作物,位置{O0O00OO00OO00OOO0}')#line:144
                                    if OO0O0000O0OOOOOOO ['status']==500 :#line:145
                                        print (f'【购买合成】:{OO0O0000O0OOOOOOO["message"]}')#line:146
                                        return False #line:147
                                time .sleep (random .randint (3 ,5 )/10 )#line:148
                            O0O00OO00OO00OOO0 +=1 #line:149
                        O0O00O0OO0O0O00OO =requests .request ('get',f'{host}/api/game/getAllData',headers =O0OOOOOO00OOOO0O0 .headers ).json ()#line:150
                        O00OOOO0O0OO0O000 =O0O00O0OO0O0O00OO ['data']['cropList']#line:151
                        O00OO00O0O000O0O0 =False #line:152
                        for OOOOO0OO000O000O0 in range (12 ):#line:153
                            id =O00OOOO0O0OO0O000 [OOOOO0OO000O000O0 ]['level']#line:154
                            if id !=0 :#line:155
                                for O0O0O0O00OO0OOO00 in range (11 ):#line:156
                                    OOOOO0OO0O0000O00 =O0O0O0O00OO0OOO00 +1 #line:157
                                    g =O00OOOO0O0OO0O000 [OOOOO0OO0O0000O00 ]['level']#line:158
                                    if id ==g :#line:159
                                        O00OO0OO0O0O0O000 =O0O0O0O00OO0OOO00 +2 #line:160
                                        if O00OO0OO0O0O0O000 ==OOOOO0OO000O000O0 +1 :#line:161
                                            pass #line:162
                                        else :#line:163
                                            time .sleep (random .randint (3 ,5 )/10 )#line:164
                                            OO0O0OO0O0O00O0O0 =OOOOO0OO000O000O0 +1 #line:165
                                            OO000000OOOO0000O ={"site":OO0O0OO0O0O00O0O0 -1 ,"targetSite":O00OO0OO0O0O0O000 -1 }#line:167
                                            OO0OOO0000OO000OO =requests .request ('post',f'{host}/api/game/crops/move',headers =O0OOOOOO00OOOO0O0 .headers ,data =OO000000OOOO0000O ).json ()#line:169
                                            if 'status'in OO0OOO0000OO000OO :#line:171
                                                if OO0OOO0000OO000OO ['status']==200 :#line:172
                                                    pass #line:173
                                            print ('【购买合成】:',OO0O0OO0O0O00O0O0 ,O00OO0OO0O0O0O000 ,'合成成功')#line:175
                                            O00OO00O0O000O0O0 =True #line:176
                                    if O00OO00O0O000O0O0 :#line:177
                                        break #line:178
                                if O00OO00O0O000O0O0 :#line:179
                                    break #line:180
        except Exception as O0OOO00OO000OO0O0 :#line:181
            O0OOOOOO00OOOO0O0 .synthetic ()#line:182
    def propsraffle (OO00OO00O00O00000 ):#line:186
        try :#line:187
            while True :#line:188
                O0O0O0O000OOOO0OO =requests .request ('get',f'{host}/api/propsraffle/lucky',headers =OO00OO00O00O00000 .headers ).json ()#line:189
                if 'status'in O0O0O0O000OOOO0OO :#line:191
                    if O0O0O0O000OOOO0OO ['status']==200 :#line:192
                        OOO0O0OOOO0O000OO =O0O0O0O000OOOO0OO ['data']['rows']#line:193
                        if OOO0O0OOOO0O000OO ==5 or OOO0O0OOOO0O000OO ==6 or OOO0O0OOOO0O000OO ==7 :#line:194
                            O0OO0OO000OO0O0OO =O0O0O0O000OOOO0OO ['data']['silver']#line:195
                            print (f'【转盘抽奖】:获得种子:{O0OO0OO000OO0O0OO}')#line:196
                        if OOO0O0OOOO0O000OO ==1 or OOO0O0OOOO0O000OO ==2 or OOO0O0OOOO0O000OO ==3 :#line:197
                            O0O0OO0OO0OO0OO00 =O0O0O0O000OOOO0OO ['data']['clover']#line:198
                            print (f'【转盘抽奖】:获得三叶草:{O0O0OO0OO0OO0OO00}')#line:199
                        if OOO0O0OOOO0O000OO ==4 or OOO0O0OOOO0O000OO ==8 :#line:200
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:201
                        if OOO0O0OOOO0O000OO =='抽奖次数已用完':#line:205
                            OOO0OOO0O000O0OOO =random .randint (160 ,190 )/10 #line:206
                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{OOO0OOO0O000O0OOO}秒获取抽奖机会')#line:207
                            time .sleep (OOO0OOO0O000O0OOO )#line:208
                            OO0O0OOO000O0O000 =requests .request ('get',f'{host}/api/propsraffle/lucky/adverti/restore',headers =OO00OO00O00O00000 .headers ).json ()#line:209
                            if 'status'in OO0O0OOO000O0O000 :#line:211
                                if OO0O0OOO000O0O000 ['status']==200 :#line:212
                                    print (f'【转盘抽奖】:{OO0O0OOO000O0O000["message"]}')#line:213
                                if OO0O0OOO000O0O000 ['status']==500 :#line:214
                                    print (f'【转盘抽奖】:{OO0O0OOO000O0O000["message"]}')#line:215
                                    break #line:216
                            time .sleep (random .randint (10 ,15 )/10 )#line:217
                time .sleep (random .randint (8 ,15 )/10 )#line:218
        except Exception as O0OO00OO0O00000O0 :#line:219
            print (O0OO00OO0O00000O0 )#line:220
    def friends_invitation (OOOOO0O0OO0OO0O0O ):#line:223
        try :#line:224
            OO0OOOO000000OOO0 =requests .request ('get','http://test.scsc.sc19319.com/api/friends',headers =OOOOO0O0OO0OO0O0O .headers ).json ()#line:225
            if 'status'in OO0OOOO000000OOO0 :#line:226
                if OO0OOOO000000OOO0 ['status']==200 :#line:227
                    O0O00O0000O00O0OO =OO0OOOO000000OOO0 ['data']['myInviteter']#line:228
                    if O0O00O0000O00O0OO :#line:229
                        O000O0OO0OOO000O0 =O0O00O0000O00O0OO ['user']['nickname']#line:230
                        print (f'【绑邀请码】:我的邀请人:{O000O0OO0OOO000O0}')#line:231
                    else :#line:232
                        if OOOOO0O0OO0OO0O0O .innerId !='0':#line:233
                            print ('【绑邀请码】:绑定邀请码')#line:234
                            O0OO0O000O0OO0O00 ={"innerId":OOOOO0O0OO0OO0O0O .innerId }#line:235
                            OO00O0OO00OO000OO =requests .request ('post',f'{host}/api/friends/my-invitation',headers =OOOOO0O0OO0OO0O0O .headers ,data =O0OO0O000O0OO0O00 ).json ()#line:236
                            print (OO00O0OO00OO000OO )#line:237
                        else :#line:238
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:239
        except Exception as OO00O00O0OO0000O0 :#line:240
            print (OO00O00O0OO0000O0 )#line:241
    def add_clover (O00OO000O000O0000 ):#line:245
        try :#line:246
            OO000OO00OO00O0O0 =requests .request ('get',f'{host}/api/assets/clovers',headers =O00OO000O000O0000 .headers ).json ()#line:247
            if 'status'in OO000OO00OO00O0O0 :#line:249
                if OO000OO00OO00O0O0 ['status']==200 :#line:250
                    O0O0O0000000OO0OO =OO000OO00OO00O0O0 ['data']['clover']#line:251
                    OOO0000O00O0O00OO =OO000OO00OO00O0O0 ['data']['used_clover']#line:252
                    O0O0O0000O0OO0O00 =float (O0O0O0000000OO0OO )-float (OOO0000O00O0O00OO )#line:253
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OOO0000O00O0O00OO}')#line:254
                    if O0O0O0000O0OO0O00 >1 :#line:255
                        O00O0O00O0OO000O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O0O0000O0OO0O00 )}#line:256
                        OO00OOOOOO0O0OO0O =requests .request ('post',f'{host}/api/lottery/add-stake',headers =O00OO000O000O0000 .headers ,data =O00O0O00O0OO000O0 ).json ()#line:257
                        if 'status'in OO00OOOOOO0O0OO0O :#line:259
                            if OO00OOOOOO0O0OO0O ['status']==200 :#line:260
                                print (f'【参与抽奖】:添加三叶草:{OO00OOOOOO0O0OO0O["data"]}丨数量:{O0O0O0000O0OO0O00}')#line:261
        except Exception as O000O00O0OOO0000O :#line:262
            print (O000O00O0OOO0000O )#line:263
    def energy (OOO0O0OOO0O0OOO0O ):#line:266
        OOO00OOO00000OO00 =requests .request ('get',f'{host}/api/energy/general',headers =OOO0O0OOO0O0OOO0O .headers ).json ()#line:267
        if 'status'in OOO00OOO00000OO00 :#line:269
            if OOO00OOO00000OO00 ['status']==200 :#line:270
                OO0O0OOO00O000OO0 =OOO00OOO00000OO00 ['data']['ordinary_water_consumptions']#line:271
                if float (OO0O0OOO00O000OO0 )<80 :#line:272
                    OO00OO0O0O0OO00O0 =99 -float (OO0O0OOO00O000OO0 )#line:273
                    OOOOO0OOOO00OO0O0 ={"fertilizer":str (OO00OO0O0O0OO00O0 ).split ('.')[0 ]}#line:274
                    OOOO0OOOOO0OO0O00 =requests .request ('post',f'{host}/api/energy/general/buy/fertilizer',headers =OOO0O0OOO0O0OOO0O .headers ,data =OOOOO0OOOO00OO0O0 ).json ()#line:275
                    if 'status'in OOOO0OOOOO0OO0O00 :#line:277
                        if OOOO0OOOOO0OO0O00 ['status']==200 :#line:278
                            print (f'【购买肥料】:{OOOO0OOOOO0OO0O00["message"]}')#line:279
                OO0O000O0OO00000O =OOO00OOO00000OO00 ['data']['ordinary_water_consumptions']#line:280
                if float (OO0O000O0OO00000O )<800 :#line:281
                    OO000O000OOOOOOO0 =999 -float (OO0O000O0OO00000O )#line:282
                    OO000OOO0O0OOOOOO ={"water":str (OO000O000OOOOOOO0 ).split ('.')[0 ]}#line:283
                    OO0OOO0O0OOOOO00O =requests .request ('post',f'{host}/api/energy/general/buy/water',headers =OOO0O0OOO0O0OOO0O .headers ,data =OO000OOO0O0OOOOOO ).json ()#line:284
                    if 'status'in OO0OOO0O0OOOOO00O :#line:285
                        if OO0OOO0O0OOOOO00O ['status']==200 :#line:286
                            print (f'【购买水滴】:{OO0OOO0O0OOOOO00O["message"]}')#line:287
    def game_map (O0O0OO000O000OO00 ):#line:291
        O00OOO000O00OOOOO =requests .request ('get',f'{host}/api/game/map',headers =O0O0OO000O000OO00 .headers ).json ()#line:292
        OO0O0O00OO0OOOO0O =0 #line:294
        if 'status'in O00OOO000O00OOOOO :#line:295
            if O00OOO000O00OOOOO ['status']==200 :#line:296
                OOOOO0O0OOO000O00 =O00OOO000O00OOOOO ['data']['list'][0 ]['crops']#line:297
                for OOOOOOO000O0OOOOO in OOOOO0O0OOO000O00 :#line:299
                    O000000OOOO0OO0OO =OOOOOOO000O0OOOOO ['count']#line:301
                    if O000000OOOO0OO0OO >0 :#line:302
                        OO0O0O00OO0OOOO0O +=1 #line:304
                if OO0O0O00OO0OOOO0O >8 :#line:306
                    print ('卖掉低级农作物')#line:307
                    O00O0O0000OOOOOO0 =OOOOO0O0OOO000O00 [0 ]['id']#line:308
                    O00O00O000O000O0O ={"crop_id":O00O0O0000OOOOOO0 ,"num":1 }#line:309
                    OOO0OOO00OOOOO00O =requests .request ('post',f'{host}/api/game/crops/sellForGold',headers =O0O0OO000O000OO00 .headers ,data =O00O00O000O000O0O ).json ()#line:310
                    if 'status'in OOO0OOO00OOOOO00O :#line:312
                        if OOO0OOO00OOOOO00O ['status']==200 :#line:313
                            print ('卖出成功')#line:314
def version_of_the_validation ():#line:318
    return str ((59 -56 )/10 )#line:319
def gitee_validation ():#line:321
    try :#line:322
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:323
    except Exception as O00OO0O000O0O0O0O :#line:324
        sys .exit (0 )#line:325
def update_the_validation ():#line:331
    try :#line:332
        OOOOOO0OOO0OO0OO0 =gitee_validation ()#line:333
        if version_of_the_validation ()<OOOOOO0OOO0OO0OO0 ['CityEarth']['edition']:#line:334
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOOO0OOO0OO0OO0["CityEarth"]["edition"]}   ❌')#line:335
            print (f'更新内容=>>{OOOOOO0OOO0OO0OO0["CityEarth"]["content"]}   👍')#line:336
        else :#line:337
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOOO0OOO0OO0OO0["CityEarth"]["edition"]}   ✅')#line:338
            print (f'更新内容=>> {OOOOOO0OOO0OO0OO0["CityEarth"]["content"]}   👍')#line:339
    except Exception as O0O000O0O00OOOOO0 :#line:340
        print (O0O000O0O00OOOOO0 )#line:341
def os_qinglong ():#line:344
    if application in os .environ :#line:345
        O0OO000O0OO0O00O0 =os .environ [application ].split ('\n')#line:346
        if len (O0OO000O0OO0O00O0 )>0 :#line:347
            return O0OO000O0OO0O00O0 #line:348
        else :#line:349
            print (f"{application}变量未启用")#line:350
            print ('脚本退出')#line:351
            sys .exit (1 )#line:352
    else :#line:353
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:354
        return os_built ()#line:355
def os_built ():#line:358
    if token :#line:359
        O0O0O0000OOOOOOOO =token .split ('\n')#line:360
        if len (O0O0O0000OOOOOOOO )>0 :#line:361
            return O0O0O0000OOOOOOOO #line:362
    else :#line:363
        print (f"内置变量为空")#line:364
        print ('脚本结束')#line:365
        sys .exit (0 )#line:366
if __name__ =='__main__':#line:369
    start ()#line:370
