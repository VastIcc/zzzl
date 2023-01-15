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
        O0O00O0O0OOOOOOO0 =os_qinglong ()#line:6
        print (f"==========共找到{len(O0O00O0O0OOOOOOO0)}个账号==========")#line:7
        for O000O00OO0O0O0OOO in O0O00O0O0OOOOOOO0 :#line:8
            print (f"------------正在执行第{O0O00O0O0OOOOOOO0.index(O000O00OO0O0O0OOO) + 1}个账号------------")#line:9
            O00OO0OO0OO0OOOO0 =CityEarth (O000O00OO0O0O0OOO )#line:10
            if O00OO0OO0OO0OOOO0 .base_info ():#line:12
                O00OO0OO0OO0OOOO0 .friends_invitation ()#line:16
                O00OO0OO0OO0OOOO0 .add_clover ()#line:20
                O00OO0OO0OO0OOOO0 .energy ()#line:22
                O00OO0OO0OO0OOOO0 .game_map ()#line:24
                O00OO0OO0OO0OOOO0 .synthetic ()#line:26
                O00OO0OO0OO0OOOO0 .crops_illustrated ()#line:28
            else :#line:29
                print ('token失效')#line:30
            time .sleep (time_xx )#line:32
    except Exception as OOOO0OOO0OOO0OOO0 :#line:33
        print (OOOO0OOO0OOO0OOO0 )#line:34
class CityEarth :#line:37
    def __init__ (OOOOOOO0OOO0O000O ,OOO0OO000O00O0000 ):#line:39
        try :#line:40
            OOOOOOO0OOO0O000O .token =OOO0OO000O00O0000 .split ('&')[0 ]#line:41
            OOOOOOO0OOO0O000O .innerId =OOO0OO000O00O0000 .split ('&')[1 ]#line:42
            OOOOOOO0OOO0O000O .headers ={'authorization':OOOOOOO0OOO0O000O .token ,'Host':'test.scsc.sc19319.com'}#line:46
        except Exception as O0O0OOO00OOO0OOO0 :#line:47
            print ('变量格式错误')#line:48
    def base_info (O0O0OOO0OOOO0OOO0 ):#line:51
        try :#line:52
            OOOOOO0OOOOO0O0OO =requests .request ('get',f'{host}/api/user',headers =O0O0OOO0OOOO0OOO0 .headers ).json ()#line:53
            if 'status'in OOOOOO0OOOOO0O0OO :#line:55
                if OOOOOO0OOOOO0O0OO ['status']==200 :#line:56
                    O0O000OO0OO00O0O0 =OOOOOO0OOOOO0O0OO ['data']['nickname']#line:57
                    O0O0O0O0O000OO000 =OOOOOO0OOOOO0O0OO ['data']['inner_id']#line:58
                    OOOO0OO00OOO0OOO0 =OOOOOO0OOOOO0O0OO ['data']['assets']['gold']#line:59
                    O0OOO000O00O0OO0O =OOOOOO0OOOOO0O0OO ['data']['level']#line:60
                    print (f'【账号信息】:昵称:{O0O000OO0OO00O0O0}丨ID:{str(O0O0O0O0O000OO000)[:3] + "**"+ str(O0O0O0O0O000OO000)[5:]}丨农作物等级:{O0OOO000O00O0OO0O}丨金种子:{str(OOOO0OO00OOO0OOO0).split(".")[0]}')#line:61
                if OOOOOO0OOOOO0O0OO ['status']==401 :#line:62
                    return False #line:63
            return True #line:64
        except Exception as OOOO0000OOOO0O000 :#line:65
            print (OOOO0000OOOO0O000 )#line:66
    def crops_illustrated (O00O0OOOO0OOOO00O ):#line:70
        O00O000O000O0000O =requests .request ('get',f'{host}/api/game/crops/illustrated',headers =O00O0OOOO0OOOO00O .headers ).json ()#line:71
        if 'status'in O00O000O000O0000O :#line:73
            if O00O000O000O0000O ['status']==200 :#line:74
                OO000OOO00O0OOO00 =O00O000O000O0000O ['data'][0 ]['crops']#line:75
                for O0O0O00OO00OO0OO0 in OO000OOO00O0OOO00 :#line:76
                    if O0O0O00OO00OO0OO0 ['ill_clover_award']:#line:77
                        if float (O0O0O00OO00OO0OO0 ['ill_clover_award'])>1 :#line:78
                            if O0O0O00OO00OO0OO0 ['is_finish']:#line:79
                                if not O0O0O00OO00OO0OO0 ['is_getit']:#line:80
                                    O0OOOOOOO0O00OOOO ={"award_level":O0O0O00OO00OO0OO0 ['level']}#line:81
                                    O0000OO00000O0O0O =requests .request ('post',f'{host}/api/game/crops/illustrated/award',headers =O00O0OOOO0OOOO00O .headers ,json =O0OOOOOOO0O00OOOO ).json ()#line:82
                                    if 'status'in O0000OO00000O0O0O :#line:83
                                        if O0000OO00000O0O0O ['status']==200 :#line:84
                                            OO00O00OOO0OOOO0O =O0000OO00000O0O0O ['data']['ill_clover_award']#line:85
                                            print (f'【图鉴奖励】:领取{O0O0O00OO00OO0OO0["crop_name"]}成就丨奖励{OO00O00OOO0OOOO0O}种子成功')#line:86
                                        if O0000OO00000O0O0O ['status']==500 :#line:87
                                            print (f'【图鉴奖励】:{O0000OO00000O0O0O["message"]}')#line:88
    def watched_ad (O0OOOOOOOOOO0O00O ):#line:91
        O0OO000OO000000OO =requests .request ('post',f'{host}/api/game/watched-ad',headers =O0OOOOOOOOOO0O00O .headers ).json ()#line:92
        print (O0OO000OO000000OO )#line:93
    def user_ad (OOO00O0O0000OOO00 ):#line:99
        O0O000OO00O0000OO =requests .request ('get',f'{host}/api/user/ad',headers =OOO00O0O0000OOO00 .headers ).json ()#line:100
        if 'status'in O0O000OO00O0000OO :#line:102
            if O0O000OO00O0000OO ['status']==200 :#line:103
                O0O0O0O0O00O0OOOO =O0O000OO00O0000OO ['data']['max_time']#line:104
                O0OOOOO0OOO000OOO =O0O000OO00O0000OO ['data']['watch_time']#line:105
                OOOO0OOO00OO00OOO =O0O000OO00O0000OO ['data']['added_time']#line:106
                print (f'【获取种子】:获取种子剩余{O0O0O0O0O00O0OOOO - O0OOOOO0OOO000OOO}次丨好友活跃剩余:{OOOO0OOO00OO00OOO}次')#line:107
                if O0O0O0O0O00O0OOOO -O0OOOOO0OOO000OOO >0 or OOOO0OOO00OO00OOO >0 :#line:108
                    time .sleep (random .randint (16 ,19 ))#line:109
                    OOOO0OO0OOOOOOO00 =requests .request ('post',f'{host}/api/game/watched-ad-forSilver',headers =OOO00O0O0000OOO00 .headers ).json ()#line:110
                    if 'status'in OOOO0OO0OOOOOOO00 :#line:112
                        if OOOO0OO0OOOOOOO00 ['status']==200 :#line:113
                            OOO0000OOOOO0O00O =OOOO0OO0OOOOOOO00 ['data']['silver']#line:114
                            print (f'【获取种子】:获得种子:{OOO0000OOOOO0O00O}')#line:115
                            return True #line:116
                        if OOOO0OO0OOOOOOO00 ['status']==500 :#line:117
                            OOO0OOO0000OOOO0O =OOOO0OO0OOOOOOO00 ['message']#line:118
                            print (f'【获取种子】:{OOO0OOO0000OOOO0O}')#line:119
                            return False #line:120
    def synthetic (OO0O0O000O0OOOO0O ):#line:123
        global id ,g #line:124
        try :#line:125
            while True :#line:126
                OOOOOO0O0O0O0OO0O =requests .request ('get',f'{host}/api/game/getAllData',headers =OO0O0O000O0OOOO0O .headers ).json ()#line:127
                if 'status'in OOOOOO0O0O0O0OO0O :#line:129
                    if OOOOOO0O0O0O0OO0O ['status']==200 :#line:130
                        O000000O00O00OO0O =OOOOOO0O0O0O0OO0O ['data']['cropList']#line:131
                        O00O000OOO000OO00 =OOOOOO0O0O0O0OO0O ['data']['gameCoreDataDBid']#line:132
                        OOO0OOO0OOOOOO00O =0 #line:133
                        for OOOO000O00O00O0O0 in O000000O00O00OO0O :#line:134
                            if not OOOO000O00O00O0O0 :#line:135
                                OOOOOOOO0OOO00OOO ={"site":OOO0OOO0OOOOOO00O ,"crop_id":O00O000OOO000OO00 }#line:136
                                O0000000O0O0O000O =requests .request ('post',f'{host}/api/game/crops/buy',headers =OO0O0O000O0OOOO0O .headers ,data =OOOOOOOO0OOO00OOO ).json ()#line:137
                                if 'status'in O0000000O0O0O000O :#line:139
                                    if O0000000O0O0O000O ['status']==200 :#line:140
                                        if O0000000O0O0O000O ['message']=='种子数量不足':#line:141
                                            print (f'【购买合成】:{O0000000O0O0O000O["message"]}')#line:142
                                            if not OO0O0O000O0OOOO0O .user_ad ():#line:143
                                                return False #line:144
                                        print (f'【购买合成】:购买农作物,位置{OOO0OOO0OOOOOO00O}')#line:145
                                    if O0000000O0O0O000O ['status']==500 :#line:146
                                        print (f'【购买合成】:{O0000000O0O0O000O["message"]}')#line:147
                                        return False #line:148
                                time .sleep (random .randint (3 ,5 )/10 )#line:149
                            OOO0OOO0OOOOOO00O +=1 #line:150
                        O0OOOO00OOO00OOOO =requests .request ('get',f'{host}/api/game/getAllData',headers =OO0O0O000O0OOOO0O .headers ).json ()#line:151
                        O0OO000000OOO0O00 =O0OOOO00OOO00OOOO ['data']['cropList']#line:152
                        O00OO00O00000O000 =False #line:153
                        for OOOO000O00O00O0O0 in range (12 ):#line:154
                            id =O0OO000000OOO0O00 [OOOO000O00O00O0O0 ]['level']#line:155
                            if id !=0 :#line:156
                                for OOO0OO000O0OO0OO0 in range (11 ):#line:157
                                    OOOO0000OOOOO0O00 =OOO0OO000O0OO0OO0 +1 #line:158
                                    g =O0OO000000OOO0O00 [OOOO0000OOOOO0O00 ]['level']#line:159
                                    if id ==g :#line:160
                                        OO0OO00O0OOOOO000 =OOO0OO000O0OO0OO0 +2 #line:161
                                        if OO0OO00O0OOOOO000 ==OOOO000O00O00O0O0 +1 :#line:162
                                            pass #line:163
                                        else :#line:164
                                            time .sleep (random .randint (3 ,5 )/10 )#line:165
                                            O00OOO00O0O0OOO0O =OOOO000O00O00O0O0 +1 #line:166
                                            O0O00000OO0OOOOO0 ={"site":O00OOO00O0O0OOO0O -1 ,"targetSite":OO0OO00O0OOOOO000 -1 }#line:168
                                            O0O0O0O0O0O00O0O0 =requests .request ('post',f'{host}/api/game/crops/move',headers =OO0O0O000O0OOOO0O .headers ,data =O0O00000OO0OOOOO0 ).json ()#line:170
                                            if 'status'in O0O0O0O0O0O00O0O0 :#line:172
                                                if O0O0O0O0O0O00O0O0 ['status']==200 :#line:173
                                                    pass #line:174
                                            print ('【购买合成】:',O00OOO00O0O0OOO0O ,OO0OO00O0OOOOO000 ,'合成成功')#line:176
                                            O00OO00O00000O000 =True #line:177
                                    if O00OO00O00000O000 :#line:178
                                        break #line:179
                                if O00OO00O00000O000 :#line:180
                                    break #line:181
        except Exception as OOOO0OOOO00OO0OO0 :#line:182
            OO0O0O000O0OOOO0O .synthetic ()#line:183
    def propsraffle (O0O0O00OOOOOOOOO0 ):#line:187
        try :#line:188
            while True :#line:189
                OO000OOOO000OO00O =requests .request ('get',f'{host}/api/propsraffle/lucky',headers =O0O0O00OOOOOOOOO0 .headers ).json ()#line:190
                if 'status'in OO000OOOO000OO00O :#line:192
                    if OO000OOOO000OO00O ['status']==200 :#line:193
                        OOOO0OOOO0OOOO000 =OO000OOOO000OO00O ['data']['rows']#line:194
                        if OOOO0OOOO0OOOO000 ==5 or OOOO0OOOO0OOOO000 ==6 or OOOO0OOOO0OOOO000 ==7 :#line:195
                            OO00OOO0OOOOO00OO =OO000OOOO000OO00O ['data']['silver']#line:196
                            print (f'【转盘抽奖】:获得种子:{OO00OOO0OOOOO00OO}')#line:197
                        if OOOO0OOOO0OOOO000 ==1 or OOOO0OOOO0OOOO000 ==2 or OOOO0OOOO0OOOO000 ==3 :#line:198
                            OOOO000000O0O0000 =OO000OOOO000OO00O ['data']['clover']#line:199
                            print (f'【转盘抽奖】:获得三叶草:{OOOO000000O0O0000}')#line:200
                        if OOOO0OOOO0OOOO000 ==4 or OOOO0OOOO0OOOO000 ==8 :#line:201
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:202
                        if OOOO0OOOO0OOOO000 =='抽奖次数已用完':#line:206
                            OO00O00000OO000O0 =random .randint (160 ,190 )/10 #line:207
                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{OO00O00000OO000O0}秒获取抽奖机会')#line:208
                            time .sleep (OO00O00000OO000O0 )#line:209
                            OOOOO00O00O000000 =requests .request ('get',f'{host}/api/propsraffle/lucky/adverti/restore',headers =O0O0O00OOOOOOOOO0 .headers ).json ()#line:210
                            if 'status'in OOOOO00O00O000000 :#line:212
                                if OOOOO00O00O000000 ['status']==200 :#line:213
                                    print (f'【转盘抽奖】:{OOOOO00O00O000000["message"]}')#line:214
                                if OOOOO00O00O000000 ['status']==500 :#line:215
                                    print (f'【转盘抽奖】:{OOOOO00O00O000000["message"]}')#line:216
                                    break #line:217
                            time .sleep (random .randint (10 ,15 )/10 )#line:218
                time .sleep (random .randint (8 ,15 )/10 )#line:219
        except Exception as OO0OO00OOOO00O0OO :#line:220
            print (OO0OO00OOOO00O0OO )#line:221
    def friends_invitation (OOO0O000000OO000O ):#line:224
        try :#line:225
            OOO0OO000000O0OOO =requests .request ('get','http://test.scsc.sc19319.com/api/friends',headers =OOO0O000000OO000O .headers ).json ()#line:226
            if 'status'in OOO0OO000000O0OOO :#line:227
                if OOO0OO000000O0OOO ['status']==200 :#line:228
                    O00000O000O0OOOOO =OOO0OO000000O0OOO ['data']['myInviteter']#line:229
                    if O00000O000O0OOOOO :#line:230
                        OOO0OO0OO0OOOO000 =O00000O000O0OOOOO ['user']['nickname']#line:231
                        print (f'【绑邀请码】:我的邀请人:{OOO0OO0OO0OOOO000}')#line:232
                    else :#line:233
                        if OOO0O000000OO000O .innerId !='0':#line:234
                            print ('【绑邀请码】:绑定邀请码')#line:235
                            O0OO00O00000OO0OO ={"innerId":OOO0O000000OO000O .innerId }#line:236
                            OO0OO0000OOOOO000 =requests .request ('post',f'{host}/api/friends/my-invitation',headers =OOO0O000000OO000O .headers ,data =O0OO00O00000OO0OO ).json ()#line:237
                            print (OO0OO0000OOOOO000 )#line:238
                        else :#line:239
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:240
        except Exception as OO0000OOOO00OOOOO :#line:241
            print (OO0000OOOO00OOOOO )#line:242
    def add_clover (O0O0OO00O0O000OOO ):#line:246
        try :#line:247
            OOOOO000OO00000OO =requests .request ('get',f'{host}/api/assets/clovers',headers =O0O0OO00O0O000OOO .headers ).json ()#line:248
            if 'status'in OOOOO000OO00000OO :#line:250
                if OOOOO000OO00000OO ['status']==200 :#line:251
                    OO00OO0O000O0O000 =OOOOO000OO00000OO ['data']['clover']#line:252
                    OO00OO0OO0000000O =OOOOO000OO00000OO ['data']['used_clover']#line:253
                    OOO000OO00OOOOO00 =float (OO00OO0O000O0O000 )-float (OO00OO0OO0000000O )#line:254
                    print (f'【参与抽奖】:参与抽奖的三叶草:{OO00OO0OO0000000O}')#line:255
                    if OOO000OO00OOOOO00 >1 :#line:256
                        OO00O0OOOO000000O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO000OO00OOOOO00 )}#line:257
                        O00O0OO0O0OO0OOO0 =requests .request ('post',f'{host}/api/lottery/add-stake',headers =O0O0OO00O0O000OOO .headers ,data =OO00O0OOOO000000O ).json ()#line:258
                        if 'status'in O00O0OO0O0OO0OOO0 :#line:260
                            if O00O0OO0O0OO0OOO0 ['status']==200 :#line:261
                                print (f'【参与抽奖】:添加三叶草:{O00O0OO0O0OO0OOO0["data"]}丨数量:{OOO000OO00OOOOO00}')#line:262
        except Exception as OO00OOO00OOO0O000 :#line:263
            print (OO00OOO00OOO0O000 )#line:264
    def energy (O0000OO00OO0OO0O0 ):#line:267
        OO0O00OO0O00OO0O0 =requests .request ('get',f'{host}/api/energy/general',headers =O0000OO00OO0OO0O0 .headers ).json ()#line:268
        if 'status'in OO0O00OO0O00OO0O0 :#line:270
            if OO0O00OO0O00OO0O0 ['status']==200 :#line:271
                OOO0000O00O0O0OO0 =OO0O00OO0O00OO0O0 ['data']['ordinary_water_consumptions']#line:272
                if float (OOO0000O00O0O0OO0 )<80 :#line:273
                    O0O000O0O0OO00000 =99 -float (OOO0000O00O0O0OO0 )#line:274
                    OOOO0O00OOO000O0O ={"fertilizer":str (O0O000O0O0OO00000 ).split ('.')[0 ]}#line:275
                    OOOOOO0OOO00O0OO0 =requests .request ('post',f'{host}/api/energy/general/buy/fertilizer',headers =O0000OO00OO0OO0O0 .headers ,data =OOOO0O00OOO000O0O ).json ()#line:276
                    if 'status'in OOOOOO0OOO00O0OO0 :#line:278
                        if OOOOOO0OOO00O0OO0 ['status']==200 :#line:279
                            print (f'【购买肥料】:{OOOOOO0OOO00O0OO0["message"]}')#line:280
                OO0O0000O0O00OO00 =OO0O00OO0O00OO0O0 ['data']['ordinary_water_consumptions']#line:281
                if float (OO0O0000O0O00OO00 )<800 :#line:282
                    O0000O0OO0OOO00OO =999 -float (OO0O0000O0O00OO00 )#line:283
                    O000O0O00OO0OOOO0 ={"water":str (O0000O0OO0OOO00OO ).split ('.')[0 ]}#line:284
                    O0OO0O00OOO000O0O =requests .request ('post',f'{host}/api/energy/general/buy/water',headers =O0000OO00OO0OO0O0 .headers ,data =O000O0O00OO0OOOO0 ).json ()#line:285
                    if 'status'in O0OO0O00OOO000O0O :#line:286
                        if O0OO0O00OOO000O0O ['status']==200 :#line:287
                            print (f'【购买水滴】:{O0OO0O00OOO000O0O["message"]}')#line:288
    def game_map (OO0000OO00000OO00 ):#line:292
        OOOO0OO00000OOOO0 =requests .request ('get',f'{host}/api/game/map',headers =OO0000OO00000OO00 .headers ).json ()#line:293
        OO0O0O0OO000O0OO0 =0 #line:295
        if 'status'in OOOO0OO00000OOOO0 :#line:296
            if OOOO0OO00000OOOO0 ['status']==200 :#line:297
                OO0O000O0O0O0OOOO =OOOO0OO00000OOOO0 ['data']['list'][0 ]['crops']#line:298
                for O00OO0OO0OO0OO00O in OO0O000O0O0O0OOOO :#line:300
                    O00OO00O00O0OO0OO =O00OO0OO0OO0OO00O ['count']#line:302
                    if O00OO00O00O0OO0OO >0 :#line:303
                        OO0O0O0OO000O0OO0 +=1 #line:305
                if OO0O0O0OO000O0OO0 >8 :#line:307
                    print ('卖掉低级农作物')#line:308
                    O000OOOOOOO000OO0 =OO0O000O0O0O0OOOO [0 ]['id']#line:309
                    O00000OO0O00OO0O0 ={"crop_id":O000OOOOOOO000OO0 ,"num":1 }#line:310
                    OO00000O0O00OOOO0 =requests .request ('post',f'{host}/api/game/crops/sellForGold',headers =OO0000OO00000OO00 .headers ,data =O00000OO0O00OO0O0 ).json ()#line:311
                    if 'status'in OO00000O0O00OOOO0 :#line:313
                        if OO00000O0O00OOOO0 ['status']==200 :#line:314
                            print ('卖出成功')#line:315
def version_of_the_validation ():#line:319
    return str ((59 -56 )/10 )#line:320
def gitee_validation ():#line:322
    try :#line:323
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:324
    except Exception as OOOOO0O000O0000OO :#line:325
        sys .exit (0 )#line:326
def update_the_validation ():#line:332
    try :#line:333
        OO0OOOOO0O0O000OO =gitee_validation ()#line:334
        if version_of_the_validation ()<OO0OOOOO0O0O000OO ['CityEarth']['edition']:#line:335
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OOOOO0O0O000OO["CityEarth"]["edition"]}   ❌')#line:336
            print (f'更新内容=>>{OO0OOOOO0O0O000OO["CityEarth"]["content"]}   👍')#line:337
        else :#line:338
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OOOOO0O0O000OO["CityEarth"]["edition"]}   ✅')#line:339
            print (f'更新内容=>> {OO0OOOOO0O0O000OO["CityEarth"]["content"]}   👍')#line:340
    except Exception as OOO0O0OO00OOOOO00 :#line:341
        print (OOO0O0OO00OOOOO00 )#line:342
def os_qinglong ():#line:345
    if application in os .environ :#line:346
        O0OOO000OO0O0O000 =os .environ [application ].split ('\n')#line:347
        if len (O0OOO000OO0O0O000 )>0 :#line:348
            return O0OOO000OO0O0O000 #line:349
        else :#line:350
            print (f"{application}变量未启用")#line:351
            print ('脚本退出')#line:352
            sys .exit (1 )#line:353
    else :#line:354
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:355
        return os_built ()#line:356
def os_built ():#line:359
    if token :#line:360
        OO00OOO00000O0OOO =token .split ('\n')#line:361
        if len (OO00OOO00000O0OOO )>0 :#line:362
            return OO00OOO00000O0OOO #line:363
    else :#line:364
        print (f"内置变量为空")#line:365
        print ('脚本结束')#line:366
        sys .exit (0 )#line:367
if __name__ =='__main__':#line:370
    start ()#line:371
