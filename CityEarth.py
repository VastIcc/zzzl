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
apk下载地址     https://sc19319.oss-cn-hangzhou.aliyuncs.com/scsc/test/1.9.3.1.S9.apk
抓取  http://scsc.sc19319.com 的authorization值
青龙变量 export ce_token="authorization&绑定邀请码"   不绑定填 0   多号换行
我的邀请码是  1932634
版本  0.4
"""
application = 'ce_token'  # 变量名
token = ''


time_xx = random.randint(8, 12)          # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://scsc.sc19319.com'#line:2
def start ():#line:3
    try :#line:4
        update_the_validation ()#line:5
        OOO00000O000O0000 =os_qinglong ()#line:6
        print (f"==========共找到{len(OOO00000O000O0000)}个账号==========")#line:7
        for OOOOOOOO0O000OO00 in OOO00000O000O0000 :#line:8
            print (f"------------正在执行第{OOO00000O000O0000.index(OOOOOOOO0O000OO00) + 1}个账号------------")#line:9
            OOO0OO0O0O0O0000O =CityEarth (OOOOOOOO0O000OO00 )#line:10
            if OOO0OO0O0O0O0000O .base_info ():#line:12
                OOO0OO0O0O0O0000O .friends_invitation ()#line:16
                OOO0OO0O0O0O0000O .add_clover ()#line:20
                OOO0OO0O0O0O0000O .energy ()#line:22
                OOO0OO0O0O0O0000O .game_map ()#line:24
                OOO0OO0O0O0O0000O .synthetic ()#line:26
                OOO0OO0O0O0O0000O .crops_illustrated ()#line:28
            else :#line:29
                print ('token失效')#line:30
            time .sleep (time_xx )#line:32
    except Exception as OO0000000OO0000O0 :#line:33
        print (OO0000000OO0000O0 )#line:34
class CityEarth :#line:37
    def __init__ (OOO00OOOO0OOO00OO ,O00O0O00OO0000000 ):#line:39
        try :#line:40
            OOO00OOOO0OOO00OO .token =O00O0O00OO0000000 .split ('&')[0 ]#line:41
            OOO00OOOO0OOO00OO .innerId =O00O0O00OO0000000 .split ('&')[1 ]#line:42
            OOO00OOOO0OOO00OO .headers ={'authorization':OOO00OOOO0OOO00OO .token ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:49
        except Exception as OOO000OOO0OO0OO00 :#line:50
            print ('变量格式错误')#line:51
    def base_info (OO0O0OOOOOO00O0OO ):#line:54
        try :#line:55
            O00O0000O0O0OO0O0 =requests .request ('get',f'{host}/user',headers =OO0O0OOOOOO00O0OO .headers ).json ()#line:56
            if 'status'in O00O0000O0O0OO0O0 :#line:58
                if O00O0000O0O0OO0O0 ['status']==200 :#line:59
                    OO000O0000OO0O0O0 =O00O0000O0O0OO0O0 ['data']['nickname']#line:60
                    OOOOOOO0O0O00OOOO =O00O0000O0O0OO0O0 ['data']['inner_id']#line:61
                    O000O00OOOO000O0O =O00O0000O0O0OO0O0 ['data']['assets']['gold']#line:62
                    OOO00O0O000000O00 =O00O0000O0O0OO0O0 ['data']['level']#line:63
                    print (f'【账号信息】:昵称:{OO000O0000OO0O0O0}丨ID:{str(OOOOOOO0O0O00OOOO)[:3] + "**"+ str(OOOOOOO0O0O00OOOO)[5:]}丨农作物等级:{OOO00O0O000000O00}丨金种子:{str(O000O00OOOO000O0O).split(".")[0]}')#line:64
                if O00O0000O0O0OO0O0 ['status']==401 :#line:65
                    return False #line:66
            return True #line:67
        except Exception as OO00OO00OOOO0OO0O :#line:68
            print (OO00OO00OOOO0OO0O )#line:69
    def crops_illustrated (O0OO0O000O0O0O00O ):#line:73
        OOO00O00O0O000OO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OO0O000O0O0O00O .headers ).json ()#line:74
        if 'status'in OOO00O00O0O000OO0 :#line:76
            if OOO00O00O0O000OO0 ['status']==200 :#line:77
                O00O0O00O0O0000O0 =OOO00O00O0O000OO0 ['data'][0 ]['crops']#line:78
                for OO00OO0OO0O00OOOO in O00O0O00O0O0000O0 :#line:79
                    if OO00OO0OO0O00OOOO ['ill_clover_award']:#line:80
                        if float (OO00OO0OO0O00OOOO ['ill_clover_award'])>1 :#line:81
                            if OO00OO0OO0O00OOOO ['is_finish']:#line:82
                                if not OO00OO0OO0O00OOOO ['is_getit']:#line:83
                                    O0OOO0000OO0OO0O0 ={"award_level":OO00OO0OO0O00OOOO ['level']}#line:84
                                    O0O0OO0OOO0000O0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OO0O000O0O0O00O .headers ,json =O0OOO0000OO0OO0O0 ).json ()#line:85
                                    if 'status'in O0O0OO0OOO0000O0O :#line:86
                                        if O0O0OO0OOO0000O0O ['status']==200 :#line:87
                                            O00OOOO00000O00O0 =O0O0OO0OOO0000O0O ['data']['ill_clover_award']#line:88
                                            print (f'【图鉴奖励】:领取{OO00OO0OO0O00OOOO["crop_name"]}成就丨奖励{O00OOOO00000O00O0}种子成功')#line:89
                                        if O0O0OO0OOO0000O0O ['status']==500 :#line:90
                                            print (f'【图鉴奖励】:{O0O0OO0OOO0000O0O["message"]}')#line:91
    def watched_ad (OOO00OOO000O0OO0O ):#line:94
        OOO00000OOOOOO0O0 =requests .request ('post',f'{host}/game/watched-ad',headers =OOO00OOO000O0OO0O .headers ).json ()#line:95
        print (OOO00000OOOOOO0O0 )#line:96
    def user_ad (OOO000OO0O0O00O0O ):#line:102
        O0O0OOO000OO000OO =requests .request ('get',f'{host}/user/ad',headers =OOO000OO0O0O00O0O .headers ).json ()#line:103
        if 'status'in O0O0OOO000OO000OO :#line:105
            if O0O0OOO000OO000OO ['status']==200 :#line:106
                OO0O000OOOO00OOO0 =O0O0OOO000OO000OO ['data']['max_time']#line:107
                OOO0OO00O0OOOO00O =O0O0OOO000OO000OO ['data']['watch_time']#line:108
                O0O00O0O0OOOO0OOO =O0O0OOO000OO000OO ['data']['added_time']#line:109
                print (f'【获取种子】:获取种子剩余{O0O00O0O0OOOO0OOO + OO0O000OOOO00OOO0 - OOO0OO00O0OOOO00O}次丨好友提供:{O0O00O0O0OOOO0OOO}次')#line:110
                if O0O00O0O0OOOO0OOO +OO0O000OOOO00OOO0 -OOO0OO00O0OOOO00O >0 :#line:111
                    time .sleep (random .randint (16 ,19 ))#line:112
                    O0O0O0O000OOO0O00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO000OO0O0O00O0O .headers ).json ()#line:113
                    if 'status'in O0O0O0O000OOO0O00 :#line:115
                        if O0O0O0O000OOO0O00 ['status']==200 :#line:116
                            O00OO000000OO00OO =O0O0O0O000OOO0O00 ['data']['silver']#line:117
                            print (f'【获取种子】:获得种子:{O00OO000000OO00OO}')#line:118
                            return True #line:119
                        if O0O0O0O000OOO0O00 ['status']==500 :#line:120
                            OOOO00O0OOO0O0O0O =O0O0O0O000OOO0O00 ['message']#line:121
                            print (f'【获取种子】:{OOOO00O0OOO0O0O0O}')#line:122
                            return False #line:123
    def synthetic (O000O0O00O00O0OOO ):#line:126
        global id ,g #line:127
        try :#line:128
            while True :#line:129
                OOO0O00OO00000O00 =requests .request ('get',f'{host}/game/getAllData',headers =O000O0O00O00O0OOO .headers ).json ()#line:130
                if 'status'in OOO0O00OO00000O00 :#line:132
                    if OOO0O00OO00000O00 ['status']==200 :#line:133
                        O0OOOO0OOOO0OO0OO =OOO0O00OO00000O00 ['data']['cropList']#line:134
                        O00O0O00OOOOOOOO0 =OOO0O00OO00000O00 ['data']['gameCoreDataDBid']#line:135
                        O000000OO00000O00 =0 #line:136
                        for OO0000O00O00O0000 in O0OOOO0OOOO0OO0OO :#line:137
                            if not OO0000O00O00O0000 :#line:138
                                OOO000OO0OO000OOO ={"site":O000000OO00000O00 ,"crop_id":O00O0O00OOOOOOOO0 }#line:139
                                OOOO00O00OO0O00O0 =requests .request ('post',f'{host}/game/crops/buy',headers =O000O0O00O00O0OOO .headers ,data =OOO000OO0OO000OOO ).json ()#line:140
                                if 'status'in OOOO00O00OO0O00O0 :#line:142
                                    if OOOO00O00OO0O00O0 ['status']==200 :#line:143
                                        if OOOO00O00OO0O00O0 ['message']=='种子数量不足':#line:144
                                            print (f'【购买合成】:{OOOO00O00OO0O00O0["message"]}')#line:145
                                            if not O000O0O00O00O0OOO .user_ad ():#line:146
                                                return False #line:147
                                        print (f'【购买合成】:购买农作物,位置{O000000OO00000O00}')#line:148
                                    if OOOO00O00OO0O00O0 ['status']==500 :#line:149
                                        print (f'【购买合成】:{OOOO00O00OO0O00O0["message"]}')#line:150
                                        return False #line:151
                                time .sleep (random .randint (3 ,5 )/10 )#line:152
                            O000000OO00000O00 +=1 #line:153
                        OOOO0O0O0OO000O00 =requests .request ('get',f'{host}/game/getAllData',headers =O000O0O00O00O0OOO .headers ).json ()#line:154
                        O0OO00OO0000OOO00 =OOOO0O0O0OO000O00 ['data']['cropList']#line:155
                        O000OOOO000O00OOO =False #line:156
                        for OO0000O00O00O0000 in range (12 ):#line:157
                            id =O0OO00OO0000OOO00 [OO0000O00O00O0000 ]['level']#line:158
                            if id !=0 :#line:159
                                for OOO00O0OO0O0OO0O0 in range (11 ):#line:160
                                    O0O000OO0OO0OOO0O =OOO00O0OO0O0OO0O0 +1 #line:161
                                    g =O0OO00OO0000OOO00 [O0O000OO0OO0OOO0O ]['level']#line:162
                                    if id ==g :#line:163
                                        O00OOOOOO0O0OO000 =OOO00O0OO0O0OO0O0 +2 #line:164
                                        if O00OOOOOO0O0OO000 ==OO0000O00O00O0000 +1 :#line:165
                                            pass #line:166
                                        else :#line:167
                                            time .sleep (random .randint (3 ,5 )/10 )#line:168
                                            OO0OOO0O0O00000OO =OO0000O00O00O0000 +1 #line:169
                                            OO0O0OO000O0OOO0O ={"site":OO0OOO0O0O00000OO -1 ,"targetSite":O00OOOOOO0O0OO000 -1 }#line:171
                                            OO0OOOOO00000000O =requests .request ('post',f'{host}/game/crops/move',headers =O000O0O00O00O0OOO .headers ,data =OO0O0OO000O0OOO0O ).json ()#line:173
                                            if 'status'in OO0OOOOO00000000O :#line:175
                                                if OO0OOOOO00000000O ['status']==200 :#line:176
                                                    pass #line:177
                                            print ('【购买合成】:',OO0OOO0O0O00000OO ,O00OOOOOO0O0OO000 ,'合成成功')#line:179
                                            O000OOOO000O00OOO =True #line:180
                                    if O000OOOO000O00OOO :#line:181
                                        break #line:182
                                if O000OOOO000O00OOO :#line:183
                                    break #line:184
        except Exception as O00O000O00O0O0000 :#line:185
            O000O0O00O00O0OOO .synthetic ()#line:186
    def propsraffle (O0O0O00O00OOOOOOO ):#line:190
        try :#line:191
            while True :#line:192
                O0OO0O0OO00OO0O00 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O0O00O00OOOOOOO .headers ).json ()#line:193
                if 'status'in O0OO0O0OO00OO0O00 :#line:195
                    if O0OO0O0OO00OO0O00 ['status']==200 :#line:196
                        OO0O0OOOO0O00OO0O =O0OO0O0OO00OO0O00 ['data']['rows']#line:197
                        if OO0O0OOOO0O00OO0O ==5 or OO0O0OOOO0O00OO0O ==6 or OO0O0OOOO0O00OO0O ==7 :#line:198
                            OO0O00O00OOOOO0O0 =O0OO0O0OO00OO0O00 ['data']['silver']#line:199
                            print (f'【转盘抽奖】:获得种子:{OO0O00O00OOOOO0O0}')#line:200
                        if OO0O0OOOO0O00OO0O ==1 or OO0O0OOOO0O00OO0O ==2 or OO0O0OOOO0O00OO0O ==3 :#line:201
                            OO000000OOOO0O000 =O0OO0O0OO00OO0O00 ['data']['clover']#line:202
                            print (f'【转盘抽奖】:获得三叶草:{OO000000OOOO0O000}')#line:203
                        if OO0O0OOOO0O00OO0O ==4 or OO0O0OOOO0O00OO0O ==8 :#line:204
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:205
                        if OO0O0OOOO0O00OO0O =='抽奖次数已用完':#line:209
                            O0OO00000O0000O0O =random .randint (160 ,190 )/10 #line:210
                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{O0OO00000O0000O0O}秒获取抽奖机会')#line:211
                            time .sleep (O0OO00000O0000O0O )#line:212
                            O00OOOOOOO000OOOO =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =O0O0O00O00OOOOOOO .headers ).json ()#line:213
                            if 'status'in O00OOOOOOO000OOOO :#line:215
                                if O00OOOOOOO000OOOO ['status']==200 :#line:216
                                    print (f'【转盘抽奖】:{O00OOOOOOO000OOOO["message"]}')#line:217
                                if O00OOOOOOO000OOOO ['status']==500 :#line:218
                                    print (f'【转盘抽奖】:{O00OOOOOOO000OOOO["message"]}')#line:219
                                    break #line:220
                            time .sleep (random .randint (10 ,15 )/10 )#line:221
                time .sleep (random .randint (8 ,15 )/10 )#line:222
        except Exception as O0OO00O0OOOOO0O0O :#line:223
            print (O0OO00O0OOOOO0O0O )#line:224
    def friends_invitation (O0000OO00O00000OO ):#line:227
        try :#line:228
            OOOO0OOOO0000O0OO =requests .request ('get',f'{host}/friends',headers =O0000OO00O00000OO .headers ).json ()#line:229
            if 'status'in OOOO0OOOO0000O0OO :#line:230
                if OOOO0OOOO0000O0OO ['status']==200 :#line:231
                    O0OO000OO000OO00O =OOOO0OOOO0000O0OO ['data']['myInviteter']#line:232
                    if O0OO000OO000OO00O :#line:233
                        O00OO0OOOO000O00O =O0OO000OO000OO00O ['user']['nickname']#line:234
                        print (f'【绑邀请码】:我的邀请人:{O00OO0OOOO000O00O}')#line:235
                    else :#line:236
                        if O0000OO00O00000OO .innerId !='0':#line:237
                            print ('【绑邀请码】:绑定邀请码')#line:238
                            OO00OOOO00OOOOO00 ={"innerId":O0000OO00O00000OO .innerId }#line:239
                            OO0OO000O0O000OO0 =requests .request ('post',f'{host}/friends/my-invitation',headers =O0000OO00O00000OO .headers ,data =OO00OOOO00OOOOO00 ).json ()#line:240
                            print (OO0OO000O0O000OO0 )#line:241
                        else :#line:242
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:243
        except Exception as O0O0O00000OO00OOO :#line:244
            print (O0O0O00000OO00OOO )#line:245
    def add_clover (OOOOO0O000OO0O0O0 ):#line:249
        try :#line:250
            OO0O000OOOO0000O0 =requests .request ('get',f'{host}/assets/clovers',headers =OOOOO0O000OO0O0O0 .headers ).json ()#line:251
            if 'status'in OO0O000OOOO0000O0 :#line:253
                if OO0O000OOOO0000O0 ['status']==200 :#line:254
                    OO00O00O0O0000000 =OO0O000OOOO0000O0 ['data']['clover']#line:255
                    OO00OO00OOO00O0O0 =OO0O000OOOO0000O0 ['data']['used_clover']#line:256
                    O000O0OO0OOO0OOO0 =float (OO00O00O0O0000000 )-float (OO00OO00OOO00O0O0 )#line:257
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OO00OO00OOO00O0O0}')#line:258
                    if O000O0OO0OOO0OOO0 >1 :#line:259
                        OOO0O0OO0OOO00O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O000O0OO0OOO0OOO0 )}#line:260
                        O000OO0OO0000OOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOOO0O000OO0O0O0 .headers ,data =OOO0O0OO0OOO00O0O ).json ()#line:261
                        if 'status'in O000OO0OO0000OOOO :#line:263
                            if O000OO0OO0000OOOO ['status']==200 :#line:264
                                print (f'【参与抽奖】:添加三叶草:{O000OO0OO0000OOOO["data"]}丨数量:{O000O0OO0OOO0OOO0}')#line:265
        except Exception as O0O000OOOO0O0000O :#line:266
            print (O0O000OOOO0O0000O )#line:267
    def energy (O0OO0OO0000O0OO0O ):#line:270
        OO0OOOO0OOO0000OO =requests .request ('get',f'{host}/energy/general',headers =O0OO0OO0000O0OO0O .headers ).json ()#line:271
        if 'status'in OO0OOOO0OOO0000OO :#line:273
            if OO0OOOO0OOO0000OO ['status']==200 :#line:274
                OO0OOO0O0000O0OO0 =OO0OOOO0OOO0000OO ['data']['ordinary_water_consumptions']#line:275
                if float (OO0OOO0O0000O0OO0 )<80 :#line:276
                    O00OO0OO0OOOO00O0 =99 -float (OO0OOO0O0000O0OO0 )#line:277
                    O0OOO0O0OOO0OO0O0 ={"fertilizer":str (O00OO0OO0OOOO00O0 ).split ('.')[0 ]}#line:278
                    OOOOO00O00OO0O000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0OO0OO0000O0OO0O .headers ,data =O0OOO0O0OOO0OO0O0 ).json ()#line:279
                    if 'status'in OOOOO00O00OO0O000 :#line:281
                        if OOOOO00O00OO0O000 ['status']==200 :#line:282
                            print (f'【购买肥料】:{OOOOO00O00OO0O000["message"]}')#line:283
                OOOOOO00OOOOO0O00 =OO0OOOO0OOO0000OO ['data']['ordinary_water_consumptions']#line:284
                if float (OOOOOO00OOOOO0O00 )<800 :#line:285
                    OO0O0O0O000OOOO00 =999 -float (OOOOOO00OOOOO0O00 )#line:286
                    O00OO0000OOO00000 ={"water":str (OO0O0O0O000OOOO00 ).split ('.')[0 ]}#line:287
                    OOO00OO000OOOO00O =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0OO0OO0000O0OO0O .headers ,data =O00OO0000OOO00000 ).json ()#line:288
                    if 'status'in OOO00OO000OOOO00O :#line:289
                        if OOO00OO000OOOO00O ['status']==200 :#line:290
                            print (f'【购买水滴】:{OOO00OO000OOOO00O["message"]}')#line:291
    def game_map (OO0O00O00O000OO0O ):#line:295
        OOOOO00O00OO00OOO =requests .request ('get',f'{host}/game/map',headers =OO0O00O00O000OO0O .headers ).json ()#line:296
        O0OO00000OO0OOO00 =0 #line:298
        if 'status'in OOOOO00O00OO00OOO :#line:299
            if OOOOO00O00OO00OOO ['status']==200 :#line:300
                O0O0OOO0000000O00 =OOOOO00O00OO00OOO ['data']['list'][0 ]['crops']#line:301
                for O0O000OOOO0OO0000 in O0O0OOO0000000O00 :#line:303
                    OOO0OOO00000OOO0O =O0O000OOOO0OO0000 ['count']#line:305
                    if OOO0OOO00000OOO0O >0 :#line:306
                        O0OO00000OO0OOO00 +=1 #line:308
                if O0OO00000OO0OOO00 >8 :#line:310
                    print ('卖掉低级农作物')#line:311
                    O000O0000OO0OOO00 =O0O0OOO0000000O00 [0 ]['id']#line:312
                    O00O000O0OO0000OO ={"crop_id":O000O0000OO0OOO00 ,"num":1 }#line:313
                    O0O000O0OOOOOO0O0 =requests .request ('post',f'{host}/game/crops/sellForGold',headers =OO0O00O00O000OO0O .headers ,data =O00O000O0OO0000OO ).json ()#line:314
                    if 'status'in O0O000O0OOOOOO0O0 :#line:316
                        if O0O000O0OOOOOO0O0 ['status']==200 :#line:317
                            print ('卖出成功')#line:318
def version_of_the_validation ():#line:322
    return str ((60 -56 )/10 )#line:323
def gitee_validation ():#line:325
    try :#line:326
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:327
    except Exception as OOO0O00OOOO0O0O0O :#line:328
        sys .exit (0 )#line:329
def update_the_validation ():#line:335
    try :#line:336
        O0OO00OOO0OOOOOOO =gitee_validation ()#line:337
        if version_of_the_validation ()<O0OO00OOO0OOOOOOO ['CityEarth']['edition']:#line:338
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00OOO0OOOOOOO["CityEarth"]["edition"]}   ❌')#line:339
            print (f'更新内容=>>{O0OO00OOO0OOOOOOO["CityEarth"]["content"]}   👍')#line:340
        else :#line:341
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00OOO0OOOOOOO["CityEarth"]["edition"]}   ✅')#line:342
            print (f'更新内容=>> {O0OO00OOO0OOOOOOO["CityEarth"]["content"]}   👍')#line:343
    except Exception as O0OO0OO0OO0O0O00O :#line:344
        print (O0OO0OO0OO0O0O00O )#line:345
def os_qinglong ():#line:348
    if application in os .environ :#line:349
        OOOOOO00OOO0OO000 =os .environ [application ].split ('\n')#line:350
        if len (OOOOOO00OOO0OO000 )>0 :#line:351
            return OOOOOO00OOO0OO000 #line:352
        else :#line:353
            print (f"{application}变量未启用")#line:354
            print ('脚本退出')#line:355
            sys .exit (1 )#line:356
    else :#line:357
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:358
        return os_built ()#line:359
def os_built ():#line:362
    if token :#line:363
        O0000O00O000O000O =token .split ('\n')#line:364
        if len (O0000O00O000O000O )>0 :#line:365
            return O0000O00O000O000O #line:366
    else :#line:367
        print (f"内置变量为空")#line:368
        print ('脚本结束')#line:369
        sys .exit (0 )#line:370
if __name__ =='__main__':#line:373
    start ()#line:374
