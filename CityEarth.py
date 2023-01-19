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
抓取  http://test.scsc.sc19319.com 的authorization值
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
        O0OO000O0OOO00O00 =os_qinglong ()#line:6
        print (f"==========共找到{len(O0OO000O0OOO00O00)}个账号==========")#line:7
        for O0000OO0OO0O00OOO in O0OO000O0OOO00O00 :#line:8
            print (f"------------正在执行第{O0OO000O0OOO00O00.index(O0000OO0OO0O00OOO) + 1}个账号------------")#line:9
            OOO00OOOOOOOO0O00 =CityEarth (O0000OO0OO0O00OOO )#line:10
            if OOO00OOOOOOOO0O00 .base_info ():#line:12
                OOO00OOOOOOOO0O00 .friends_invitation ()#line:16
                OOO00OOOOOOOO0O00 .add_clover ()#line:20
                OOO00OOOOOOOO0O00 .energy ()#line:22
                OOO00OOOOOOOO0O00 .synthetic ()#line:26
                OOO00OOOOOOOO0O00 .crops_illustrated ()#line:28
            else :#line:29
                print ('token失效')#line:30
            time .sleep (time_xx )#line:32
    except Exception as O0OOO00000000000O :#line:33
        print (O0OOO00000000000O )#line:34
class CityEarth :#line:37
    def __init__ (OO0OOOO0O0O000OOO ,OOOO00OO0000O00O0 ):#line:39
        try :#line:40
            OO0OOOO0O0O000OOO .token =OOOO00OO0000O00O0 .split ('&')[0 ]#line:41
            OO0OOOO0O0O000OOO .innerId =OOOO00OO0000O00O0 .split ('&')[1 ]#line:42
            OO0OOOO0O0O000OOO .headers ={'authorization':OO0OOOO0O0O000OOO .token ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:48
        except Exception as OOO000000O000OOOO :#line:49
            print ('变量格式错误')#line:50
    def base_info (OO00000O0OO0OOOO0 ):#line:53
        try :#line:54
            OO0O0OO0OO000OO00 =requests .request ('get',f'{host}/user',headers =OO00000O0OO0OOOO0 .headers ).json ()#line:55
            if 'status'in OO0O0OO0OO000OO00 :#line:57
                if OO0O0OO0OO000OO00 ['status']==200 :#line:58
                    O0OOOOOOO0OOO00O0 =OO0O0OO0OO000OO00 ['data']['nickname']#line:59
                    OOOO0O0000OOOO0OO =OO0O0OO0OO000OO00 ['data']['inner_id']#line:60
                    O000O000OOO00OOOO =OO0O0OO0OO000OO00 ['data']['assets']['gold']#line:61
                    O0O00OOO0OO0OOOO0 =OO0O0OO0OO000OO00 ['data']['level']#line:62
                    print (f'【账号信息】:昵称:{O0OOOOOOO0OOO00O0}丨ID:{str(OOOO0O0000OOOO0OO)[:3] + "**"+ str(OOOO0O0000OOOO0OO)[5:]}丨农作物等级:{O0O00OOO0OO0OOOO0}丨金种子:{str(O000O000OOO00OOOO).split(".")[0]}')#line:63
                if OO0O0OO0OO000OO00 ['status']==401 :#line:64
                    return False #line:65
            return True #line:66
        except Exception as O00O00OO0OO0O0O00 :#line:67
            print (O00O00OO0OO0O0O00 )#line:68
    def crops_illustrated (OOO000OO00OOO0O0O ):#line:72
        OOO0O000O000OOO0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO000OO00OOO0O0O .headers ).json ()#line:73
        if 'status'in OOO0O000O000OOO0O :#line:75
            if OOO0O000O000OOO0O ['status']==200 :#line:76
                O0O0O00000O0O0O00 =OOO0O000O000OOO0O ['data'][0 ]['crops']#line:77
                for OOO0OOOO0O00O0000 in O0O0O00000O0O0O00 :#line:78
                    if OOO0OOOO0O00O0000 ['ill_clover_award']:#line:79
                        if float (OOO0OOOO0O00O0000 ['ill_clover_award'])>1 :#line:80
                            if OOO0OOOO0O00O0000 ['is_finish']:#line:81
                                if not OOO0OOOO0O00O0000 ['is_getit']:#line:82
                                    O0OO0OO0OO0OO0O0O ={"award_level":OOO0OOOO0O00O0000 ['level']}#line:83
                                    O0O0OOOOO00O0O000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO000OO00OOO0O0O .headers ,json =O0OO0OO0OO0OO0O0O ).json ()#line:84
                                    if 'status'in O0O0OOOOO00O0O000 :#line:85
                                        if O0O0OOOOO00O0O000 ['status']==200 :#line:86
                                            OO0O0OO000OO00000 =O0O0OOOOO00O0O000 ['data']['ill_clover_award']#line:87
                                            print (f'【图鉴奖励】:领取{OOO0OOOO0O00O0000["crop_name"]}成就丨奖励{OO0O0OO000OO00000}种子成功')#line:88
                                        if O0O0OOOOO00O0O000 ['status']==500 :#line:89
                                            print (f'【图鉴奖励】:{O0O0OOOOO00O0O000["message"]}')#line:90
    def watched_ad (O0OO0OO0000O0O00O ):#line:93
        OO000OO00OOOO00OO =requests .request ('post',f'{host}/game/watched-ad',headers =O0OO0OO0000O0O00O .headers ).json ()#line:94
        print (OO000OO00OOOO00OO )#line:95
    def user_ad (O00O0OO0O0OOOO00O ):#line:101
        O00OO0O0OO00OOOO0 =requests .request ('get',f'{host}/user/ad',headers =O00O0OO0O0OOOO00O .headers ).json ()#line:102
        if 'status'in O00OO0O0OO00OOOO0 :#line:104
            if O00OO0O0OO00OOOO0 ['status']==200 :#line:105
                O00O000OO0000OO0O =O00OO0O0OO00OOOO0 ['data']['max_time']#line:106
                OOOOO000OOO0O0OO0 =O00OO0O0OO00OOOO0 ['data']['watch_time']#line:107
                O0OO00O00OO0OOO0O =O00OO0O0OO00OOOO0 ['data']['added_time']#line:108
                print (f'【获取种子】:获取种子剩余{O0OO00O00OO0OOO0O + O00O000OO0000OO0O - OOOOO000OOO0O0OO0}次丨好友提供:{O0OO00O00OO0OOO0O}次')#line:109
                if O0OO00O00OO0OOO0O +O00O000OO0000OO0O -OOOOO000OOO0O0OO0 >0 :#line:110
                    time .sleep (random .randint (16 ,19 ))#line:111
                    O00OOOO00000O0O0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00O0OO0O0OOOO00O .headers ).json ()#line:112
                    if 'status'in O00OOOO00000O0O0O :#line:114
                        if O00OOOO00000O0O0O ['status']==200 :#line:115
                            O0O00OOO0O00O0OOO =O00OOOO00000O0O0O ['data']['silver']#line:116
                            print (f'【获取种子】:获得种子:{O0O00OOO0O00O0OOO}')#line:117
                            return True #line:118
                        if O00OOOO00000O0O0O ['status']==500 :#line:119
                            OO000OOOO00O000OO =O00OOOO00000O0O0O ['message']#line:120
                            print (f'【获取种子】:{OO000OOOO00O000OO}')#line:121
                            return False #line:122
    def synthetic (OO0O000000000OOO0 ):#line:125
        global id ,g #line:126
        try :#line:127
            while True :#line:128
                OOO0O00OOO000000O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O000000000OOO0 .headers ).json ()#line:129
                if 'status'in OOO0O00OOO000000O :#line:131
                    if OOO0O00OOO000000O ['status']==200 :#line:132
                        O0O0O00OO000O00O0 =OOO0O00OOO000000O ['data']['cropList']#line:133
                        O00O000O0OO0O0OOO =OOO0O00OOO000000O ['data']['gameCoreDataDBid']#line:134
                        O0OO0O00OO0O00O0O =0 #line:135
                        for OO0O0OO0O0OO00OOO in O0O0O00OO000O00O0 :#line:136
                            if not OO0O0OO0O0OO00OOO :#line:137
                                OO0OO0O00OO0000O0 ={"site":O0OO0O00OO0O00O0O ,"crop_id":O00O000O0OO0O0OOO }#line:138
                                OO000OOO0000OOOO0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O000000000OOO0 .headers ,data =OO0OO0O00OO0000O0 ).json ()#line:139
                                if 'status'in OO000OOO0000OOOO0 :#line:141
                                    if OO000OOO0000OOOO0 ['status']==200 :#line:142
                                        if OO000OOO0000OOOO0 ['message']=='种子数量不足':#line:143
                                            print (f'【购买合成】:{OO000OOO0000OOOO0["message"]}')#line:144
                                            if not OO0O000000000OOO0 .user_ad ():#line:145
                                                return False #line:146
                                        print (f'【购买合成】:购买农作物,位置{O0OO0O00OO0O00O0O}')#line:147
                                    if OO000OOO0000OOOO0 ['status']==500 :#line:148
                                        print (f'【购买合成】:{OO000OOO0000OOOO0["message"]}')#line:149
                                        return False #line:150
                                time .sleep (random .randint (3 ,5 )/10 )#line:151
                            O0OO0O00OO0O00O0O +=1 #line:152
                        O000OOO0O00OOOO00 =requests .request ('get',f'{host}/game/getAllData',headers =OO0O000000000OOO0 .headers ).json ()#line:153
                        O0000O000OO000O0O =O000OOO0O00OOOO00 ['data']['cropList']#line:154
                        O000O00000OO0OO00 =False #line:155
                        for OO0O0OO0O0OO00OOO in range (12 ):#line:156
                            id =O0000O000OO000O0O [OO0O0OO0O0OO00OOO ]['level']#line:157
                            if id !=0 :#line:158
                                for OO0O00O0O0O00000O in range (11 ):#line:159
                                    O0O0O0O00O0OO0OOO =OO0O00O0O0O00000O +1 #line:160
                                    g =O0000O000OO000O0O [O0O0O0O00O0OO0OOO ]['level']#line:161
                                    if id ==g :#line:162
                                        OO00O0OO0OO0O0OO0 =OO0O00O0O0O00000O +2 #line:163
                                        if OO00O0OO0OO0O0OO0 ==OO0O0OO0O0OO00OOO +1 :#line:164
                                            pass #line:165
                                        else :#line:166
                                            time .sleep (random .randint (3 ,5 )/10 )#line:167
                                            OO000000O0OOOOO0O =OO0O0OO0O0OO00OOO +1 #line:168
                                            OO0OO000OO0OOO0OO ={"site":OO000000O0OOOOO0O -1 ,"targetSite":OO00O0OO0OO0O0OO0 -1 }#line:170
                                            O0OO0OOOOO000OO00 =requests .request ('post',f'{host}/game/crops/move',headers =OO0O000000000OOO0 .headers ,data =OO0OO000OO0OOO0OO ).json ()#line:172
                                            if 'status'in O0OO0OOOOO000OO00 :#line:174
                                                if O0OO0OOOOO000OO00 ['status']==200 :#line:175
                                                    pass #line:176
                                            print ('【购买合成】:',OO000000O0OOOOO0O ,OO00O0OO0OO0O0OO0 ,'合成成功')#line:178
                                            O000O00000OO0OO00 =True #line:179
                                    if O000O00000OO0OO00 :#line:180
                                        break #line:181
                                if O000O00000OO0OO00 :#line:182
                                    break #line:183
        except Exception as OOO0OO0000O0O00OO :#line:184
            OO0O000000000OOO0 .synthetic ()#line:185
    def propsraffle (OO0OOOOO000000OOO ):#line:189
        try :#line:190
            while True :#line:191
                OOOO00O0O0O0O00O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0OOOOO000000OOO .headers ).json ()#line:192
                if 'status'in OOOO00O0O0O0O00O0 :#line:194
                    if OOOO00O0O0O0O00O0 ['status']==200 :#line:195
                        OO0O000OOO00000OO =OOOO00O0O0O0O00O0 ['data']['rows']#line:196
                        if OO0O000OOO00000OO ==5 or OO0O000OOO00000OO ==6 or OO0O000OOO00000OO ==7 :#line:197
                            OOO00O00OO00O0O0O =OOOO00O0O0O0O00O0 ['data']['silver']#line:198
                            print (f'【转盘抽奖】:获得种子:{OOO00O00OO00O0O0O}')#line:199
                        if OO0O000OOO00000OO ==1 or OO0O000OOO00000OO ==2 or OO0O000OOO00000OO ==3 :#line:200
                            O00OO0OO00O0O0OOO =OOOO00O0O0O0O00O0 ['data']['clover']#line:201
                            print (f'【转盘抽奖】:获得三叶草:{O00OO0OO00O0O0OOO}')#line:202
                        if OO0O000OOO00000OO ==4 or OO0O000OOO00000OO ==8 :#line:203
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:204
                        if OO0O000OOO00000OO =='抽奖次数已用完':#line:208
                            O00OOOOOOO0OOO000 =random .randint (160 ,190 )/10 #line:209
                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{O00OOOOOOO0OOO000}秒获取抽奖机会')#line:210
                            time .sleep (O00OOOOOOO0OOO000 )#line:211
                            OO0000OO0OOOOO00O =requests .request ('get',f'{host}/propsraffle/lucky/adverti/restore',headers =OO0OOOOO000000OOO .headers ).json ()#line:212
                            if 'status'in OO0000OO0OOOOO00O :#line:214
                                if OO0000OO0OOOOO00O ['status']==200 :#line:215
                                    print (f'【转盘抽奖】:{OO0000OO0OOOOO00O["message"]}')#line:216
                                if OO0000OO0OOOOO00O ['status']==500 :#line:217
                                    print (f'【转盘抽奖】:{OO0000OO0OOOOO00O["message"]}')#line:218
                                    break #line:219
                            time .sleep (random .randint (10 ,15 )/10 )#line:220
                time .sleep (random .randint (8 ,15 )/10 )#line:221
        except Exception as O0O0O00O00O0OO0OO :#line:222
            print (O0O0O00O00O0OO0OO )#line:223
    def friends_invitation (O0O00OO0O0O0OOOO0 ):#line:226
        try :#line:227
            OO0OO00O0000OOOOO =requests .request ('get',f'{host}/friends',headers =O0O00OO0O0O0OOOO0 .headers ).json ()#line:228
            if 'status'in OO0OO00O0000OOOOO :#line:229
                if OO0OO00O0000OOOOO ['status']==200 :#line:230
                    OO00OOOOO0O00O000 =OO0OO00O0000OOOOO ['data']['myInviteter']#line:231
                    if OO00OOOOO0O00O000 :#line:232
                        OOO00OOO0OO0OO0OO =OO00OOOOO0O00O000 ['user']['nickname']#line:233
                        print (f'【绑邀请码】:我的邀请人:{OOO00OOO0OO0OO0OO}')#line:234
                    else :#line:235
                        if O0O00OO0O0O0OOOO0 .innerId !='0':#line:236
                            print ('【绑邀请码】:绑定邀请码')#line:237
                            O000OO0OOOO00OOOO ={"innerId":O0O00OO0O0O0OOOO0 .innerId }#line:238
                            OO00O00OO0O0000O0 =requests .request ('post',f'{host}/friends/my-invitation',headers =O0O00OO0O0O0OOOO0 .headers ,data =O000OO0OOOO00OOOO ).json ()#line:239
                            print (OO00O00OO0O0000O0 )#line:240
                        else :#line:241
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:242
        except Exception as O0000O0OOOO0O00OO :#line:243
            print (O0000O0OOOO0O00OO )#line:244
    def add_clover (OO0000OOO0000000O ):#line:248
        try :#line:249
            OO0O00O0OOO0O0OOO =requests .request ('get',f'{host}/assets/clovers',headers =OO0000OOO0000000O .headers ).json ()#line:250
            if 'status'in OO0O00O0OOO0O0OOO :#line:252
                if OO0O00O0OOO0O0OOO ['status']==200 :#line:253
                    O0000O0000O0O00OO =OO0O00O0OOO0O0OOO ['data']['clover']#line:254
                    OO000O000OO000000 =OO0O00O0OOO0O0OOO ['data']['used_clover']#line:255
                    O0OOO000OO00O0O0O =float (O0000O0000O0O00OO )-float (OO000O000OO000000 )#line:256
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OO000O000OO000000}')#line:257
                    if O0OOO000OO00O0O0O >1 :#line:258
                        OO00OOOO000OOOO0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OOO000OO00O0O0O )}#line:259
                        OOOO0OO00OO0OO0O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0000OOO0000000O .headers ,data =OO00OOOO000OOOO0O ).json ()#line:260
                        if 'status'in OOOO0OO00OO0OO0O0 :#line:262
                            if OOOO0OO00OO0OO0O0 ['status']==200 :#line:263
                                print (f'【参与抽奖】:添加三叶草:{OOOO0OO00OO0OO0O0["data"]}丨数量:{O0OOO000OO00O0O0O}')#line:264
        except Exception as OOOOO0OO00O00O0OO :#line:265
            print (OOOOO0OO00O00O0OO )#line:266
    def energy (OO0OO0OO000000O00 ):#line:269
        O0O0OOOOO00OOO0O0 =requests .request ('get',f'{host}/energy/general',headers =OO0OO0OO000000O00 .headers ).json ()#line:270
        if 'status'in O0O0OOOOO00OOO0O0 :#line:272
            if O0O0OOOOO00OOO0O0 ['status']==200 :#line:273
                OOOO0OO000000OO00 =O0O0OOOOO00OOO0O0 ['data']['ordinary_water_consumptions']#line:274
                if float (OOOO0OO000000OO00 )<80 :#line:275
                    OO00O0O00OOO00OOO =99 -float (OOOO0OO000000OO00 )#line:276
                    OO0000OO00000OO00 ={"fertilizer":str (OO00O0O00OOO00OOO ).split ('.')[0 ]}#line:277
                    O0O0O0OOOO0OOO0O0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0OO0OO000000O00 .headers ,data =OO0000OO00000OO00 ).json ()#line:278
                    if 'status'in O0O0O0OOOO0OOO0O0 :#line:280
                        if O0O0O0OOOO0OOO0O0 ['status']==200 :#line:281
                            print (f'【购买肥料】:{O0O0O0OOOO0OOO0O0["message"]}')#line:282
                OOOO0000O0O000O00 =O0O0OOOOO00OOO0O0 ['data']['ordinary_water_consumptions']#line:283
                if float (OOOO0000O0O000O00 )<800 :#line:284
                    O00OOOOO0OO00O0OO =999 -float (OOOO0000O0O000O00 )#line:285
                    OOO0OOO0OOO0O00OO ={"water":str (O00OOOOO0OO00O0OO ).split ('.')[0 ]}#line:286
                    OO0O00OOOO00O0OOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0OO0OO000000O00 .headers ,data =OOO0OOO0OOO0O00OO ).json ()#line:287
                    if 'status'in OO0O00OOOO00O0OOO :#line:288
                        if OO0O00OOOO00O0OOO ['status']==200 :#line:289
                            print (f'【购买水滴】:{OO0O00OOOO00O0OOO["message"]}')#line:290
    def game_map (O00OOOOO0O000O00O ):#line:294
        OOO0O0OO0OO000OOO =requests .request ('get',f'{host}/game/map',headers =O00OOOOO0O000O00O .headers ).json ()#line:295
        O000O0OOOOOOOO0OO =0 #line:297
        if 'status'in OOO0O0OO0OO000OOO :#line:298
            if OOO0O0OO0OO000OOO ['status']==200 :#line:299
                OOOO00O0O0O00O0O0 =OOO0O0OO0OO000OOO ['data']['list'][0 ]['crops']#line:300
                print (OOOO00O0O0O00O0O0 )#line:301
                for O000OOOO00O0OO00O in OOOO00O0O0O00O0O0 :#line:302
                    O0O0OOOOOO000O0OO =O000OOOO00O0OO00O ['count']#line:304
                    if O0O0OOOOOO000O0OO >0 :#line:305
                        O000O0OOOOOOOO0OO +=1 #line:307
                if O000O0OOOOOOOO0OO >8 :#line:309
                    print ('卖掉低级农作物')#line:310
                    O0O0OOO00OO000OOO =OOOO00O0O0O00O0O0 [0 ]['earnings']#line:311
                    OOO00O00OOO00OO0O ={"crop_id":O0O0OOO00OO000OOO ,"num":1 }#line:312
                    OO00O00OOOO0O0O00 =requests .request ('post',f'{host}/game/crops/sellForGold',headers =O00OOOOO0O000O00O .headers ,data =OOO00O00OOO00OO0O ).json ()#line:313
                    print (OO00O00OOOO0O0O00 )#line:314
                    if 'status'in OO00O00OOOO0O0O00 :#line:315
                        if OO00O00OOOO0O0O00 ['status']==200 :#line:316
                            print ('卖出成功')#line:317
def version_of_the_validation ():#line:321
    return str ((60 -56 )/10 )#line:322
def gitee_validation ():#line:324
    try :#line:325
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:326
    except Exception as O0O00O0000O0O0O0O :#line:327
        sys .exit (0 )#line:328
def update_the_validation ():#line:334
    try :#line:335
        O0O0O00O0OOOO000O =gitee_validation ()#line:336
        if version_of_the_validation ()<O0O0O00O0OOOO000O ['CityEarth']['edition']:#line:337
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0O00O0OOOO000O["CityEarth"]["edition"]}   ❌')#line:338
            print (f'更新内容=>>{O0O0O00O0OOOO000O["CityEarth"]["content"]}   👍')#line:339
        else :#line:340
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0O00O0OOOO000O["CityEarth"]["edition"]}   ✅')#line:341
            print (f'更新内容=>> {O0O0O00O0OOOO000O["CityEarth"]["content"]}   👍')#line:342
    except Exception as O000O000OO0OO0O00 :#line:343
        print (O000O000OO0OO0O00 )#line:344
def os_qinglong ():#line:347
    if application in os .environ :#line:348
        O00OO0OOOOOOO0OOO =os .environ [application ].split ('\n')#line:349
        if len (O00OO0OOOOOOO0OOO )>0 :#line:350
            return O00OO0OOOOOOO0OOO #line:351
        else :#line:352
            print (f"{application}变量未启用")#line:353
            print ('脚本退出')#line:354
            sys .exit (1 )#line:355
    else :#line:356
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:357
        return os_built ()#line:358
def os_built ():#line:361
    if token :#line:362
        OOOOO0000O0OO0OO0 =token .split ('\n')#line:363
        if len (OOOOO0000O0OO0OO0 )>0 :#line:364
            return OOOOO0000O0OO0OO0 #line:365
    else :#line:366
        print (f"内置变量为空")#line:367
        print ('脚本结束')#line:368
        sys .exit (0 )#line:369
if __name__ =='__main__':#line:372
    start ()#line:373
